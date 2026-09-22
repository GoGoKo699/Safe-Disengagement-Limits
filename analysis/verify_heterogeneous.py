#!/usr/bin/env python3
"""Small deterministic exact checks supporting the heterogeneous proof.

This does not exhaust continuous trajectories or establish novelty. Run with
ordinary (not optimized) Python. The default output is disposable build output;
pass --output results/heterogeneous-verification.json to refresh the tracked report.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from itertools import permutations, product
import json
from pathlib import Path
import sys

from heterogeneous import Model, Module

ROOT = Path(__file__).resolve().parents[1]


def serial_time(model: Model, mask: int, order: tuple[int, ...]) -> Q | None:
    """Direct serial evaluation; deliberately does not call the DP."""
    b = model.s + sum((m.a for i, m in enumerate(model.modules) if mask >> i & 1), Q(0))
    total = Q(0)
    for i in order:
        m = model.modules[i]
        if b <= m.d:
            return None
        total += m.M / (b - m.d)
        b += m.a
    return total


def direct_times(model: Model, counts: dict) -> dict[int, Q | None]:
    values = {}
    for mask in range(model.full_mask + 1):
        remaining = tuple(i for i in range(len(model.modules)) if not mask >> i & 1)
        best = None
        best_order = None
        for order in permutations(remaining):
            counts["permutation_evaluations"] += 1
            value = serial_time(model, mask, order)
            if value is not None and (best is None or (value, order) < (best, best_order)):
                best, best_order = value, order
        assert model.exit_time(mask) == best
        assert model.optimal_order(mask) == best_order
        values[mask] = best
        counts["subset_DP_comparisons"] += 1
    return values


def check_frontier(model: Model, times: dict, counts: dict) -> None:
    thresholds = sorted({value for value in times.values() if value is not None})
    probes = sorted(set(thresholds + [(x + y) / 2 for x, y in zip(thresholds, thresholds[1:])]
                        + [thresholds[-1] + 1]))
    previous = None
    for H in probes:
        direct = []
        for mask, time in times.items():
            if time is not None and time <= H:
                indices = tuple(i for i in range(len(model.modules)) if mask >> i & 1)
                direct.append((sum((model.modules[i].d for i in indices), Q(0)), indices, time))
        cost, ready, time = min(direct)
        result = model.readiness(H)
        assert (result.upkeep, result.ready, result.exit_time) == (cost, ready, time)
        assert result.nominal_feasible == (cost <= model.s)
        assert result.optional_throughput == (model.s - cost if cost <= model.s else None)
        assert previous is None or cost <= previous
        previous = cost
        counts["deadline_threshold_and_interval_probes"] += 1
    for mask, time in times.items():
        for i in range(len(model.modules)):
            superset_time = times[mask | (1 << i)]
            if time is not None:
                assert superset_time is not None and superset_time <= time
            counts["ready_set_monotonicity_edges"] += 1


def finite_instances(counts: dict) -> None:
    # Exhaust all ordered two-module assignments on the stated finite grid.
    jobs = tuple(Module(M, a, d) for M, a, d in product((1, 2), (1, 2), (0, 1, 2)))
    models = [Model(s, pair) for s in (0, 1, 2) for pair in product(jobs, repeat=2)]
    # Exhaust a deliberately small three-module alphabet, including blocked jobs.
    alphabet = (Module(1, 1, 0), Module(2, 1, 1), Module(1, 2, 2), Module(2, 2, 3))
    models += [Model(s, triple) for s in (0, 1, 3) for triple in product(alphabet, repeat=3)]
    # Deterministic asymmetric four/five-module instances; no random sampling.
    for n, seeds in ((4, range(12)), (5, range(4))):
        for seed in seeds:
            modules = tuple(Module(1 + (seed + 2 * i) % 5,
                                   1 + (2 * seed + i) % 4,
                                   Q((seed + 3 * i) % 7, 2)) for i in range(n))
            models.append(Model(Q(seed % 5, 2), modules))
    for model in models:
        times = direct_times(model, counts)
        check_frontier(model, times, counts)
        counts["heterogeneous_models"] += 1


def homogeneous_specialization(counts: dict) -> None:
    for n, M, a, d, s in product(range(1, 6), (Q(1), Q(3, 2)), (1, 2), (0, 1, 2), (0, 1, 3)):
        model = Model(s, (Module(M, a, d),) * n)
        for mask in range(1 << n):
            k = mask.bit_count()
            expected = (Q(0) if k == n else None if s + k * a <= d else
                        M * sum((Q(1, s + j * a - d) for j in range(k, n)), Q(0)))
            assert model.exit_time(mask) == expected
            counts["homogeneous_formula_comparisons"] += 1
    # The archived numerical example is checked exactly, without editing/importing it.
    model = Model(1, (Module(3, 3, Q(3, 5)),) * 3)
    assert [model.exit_time((1 << k) - 1) for k in range(4)] == [Q(4815, 544), Q(735, 544), Q(15, 32), Q(0)]
    assert [model.readiness(H).upkeep for H in (9, 2, 1, 0)] == [Q(0), Q(3, 5), Q(6, 5), Q(9, 5)]


def reflected_derivative(p: Q, M: Q, v: Q, d: Q) -> Q:
    return max(v - d, Q(0)) if p == 0 else min(v - d, Q(0)) if p == M else v - d


def local_potential_checks(counts: dict) -> None:
    # Normal-operation upkeep inequality permits arbitrary initialized states,
    # including positive preparation with loss exceeding the available rate.
    for d1, d2, v1, v2 in product((Q(0), Q(1, 2), Q(1), Q(2)), repeat=4):
        for p1, p2 in product((Q(0), Q(1, 2), Q(1)), repeat=2):
            growth = (reflected_derivative(p1, Q(1), v1, d1)
                      + reflected_derivative(p2, Q(1), v2, d2))
            support_loss = (d1 if p1 > 0 else Q(0)) + (d2 if p2 > 0 else Q(0))
            assert growth <= v1 + v2 - support_loss
            counts["normal_upkeep_reflection_states"] += 1
    # Each allocation grid sums to at most b. Boundary states include reflection;
    # d >= b is allowed only at zero, as required by cold-state reachability.
    for b in (Q(0), Q(1, 2), Q(1), Q(2), Q(3)):
        losses = (Q(0), b / 2, b, b + 1)
        for d1, d2 in product(losses, repeat=2):
            for p1, p2 in product((Q(0), Q(1, 2), Q(1)), repeat=2):
                if (d1 >= b and p1 != 0) or (d2 >= b and p2 != 0):
                    continue
                for k1 in range(5):
                    for k2 in range(5 - k1):
                        derivative = Q(0)
                        for p, d, v in ((p1, d1, b * k1 / 4), (p2, d2, b * k2 / 4)):
                            growth = reflected_derivative(p, Q(1), v, d)
                            if d < b:
                                assert growth / (b - d) <= v / b
                                derivative += growth / (b - d)
                            else:
                                assert growth == 0
                        assert derivative <= 1
                        counts["reflected_local_allocation_states"] += 1
    # A completion raises b. Newly eligible modules were cold; all retained
    # positive weights fall. Verify the complete potential jump, not just one term.
    for b, a, M in product((Q(1), Q(2), Q(3)), (Q(1), Q(2)), (Q(1), Q(2))):
        for completed_d in (Q(0), b / 2):
            for ds in product((Q(0), b / 2, b, b + 1), repeat=2):
                for ps in product((Q(0), Q(1, 2), Q(1)), repeat=2):
                    if any(d >= b and p != 0 for d, p in zip(ds, ps)):
                        continue
                    removed = M / (b - completed_d)
                    before = removed + sum((p / (b - d) for d, p in zip(ds, ps) if d < b), Q(0))
                    after = sum((p / (b + a - d) for d, p in zip(ds, ps) if d < b + a), Q(0))
                    assert before - after >= removed
                    counts["completion_potential_jumps"] += 1


def examples(counts: dict) -> dict:
    pair = (Module(2, 4, 0), Module(1, 1, 0))
    assert serial_time(Model(1, pair), 0, (0, 1)) == Q(11, 5)
    assert serial_time(Model(1, pair), 0, (1, 0)) == 2
    assert serial_time(Model(4, pair), 0, (0, 1)) == Q(5, 8)
    assert serial_time(Model(4, pair), 0, (1, 0)) == Q(13, 20)
    cycle = (Module(2, 4, 2), Module(6, 5, 1), Module(5, 1, 0))
    pairs = ((0, 1, Q(3), Q(10, 3)), (1, 2, Q(29, 8), Q(11, 3)), (2, 0, Q(8, 3), Q(19, 7)))
    for i, j, forward, backward in pairs:
        local = Model(3, (cycle[i], cycle[j]))
        assert serial_time(local, 0, (0, 1)) == forward
        assert serial_time(local, 0, (1, 0)) == backward
        assert forward < backward
    greedy = Model(1, (Module(3, 1, 0), Module(5, 4, 0), Module(6, 6, 0)))
    mask, order = 0, []
    while mask != greedy.full_mask:
        b = greedy.capacity(mask)
        scores = sorted((m.M + b * m.M / m.a, i) for i, m in enumerate(greedy.modules) if not mask >> i & 1)
        assert len(scores) == 1 or scores[0][0] < scores[1][0]
        i = scores[0][1]
        order.append(i)
        mask |= 1 << i
    assert tuple(order) == (0, 1, 2)
    assert serial_time(greedy, 0, tuple(order)) == Q(13, 2)
    assert greedy.exit_time() == Q(356, 55)
    assert greedy.optimal_order() == (1, 2, 0)
    assert Q(356, 55) < Q(13, 2)
    direct_times(greedy, counts)
    # All-ready, zero-spare, durable preparation, and exact d=b stalling.
    blocked = Model(0, (Module(1, 1, 0),))
    assert blocked.exit_time() is None and blocked.exit_time(1) == 0
    assert blocked.readiness(0).nominal_feasible and blocked.readiness(0).upkeep == 0
    equality = Model(1, (Module(1, 1, 1),))
    assert equality.exit_time() is None and equality.readiness(100).upkeep == 1
    infeasible = Model(0, (Module(1, 1, 1),))
    assert not infeasible.readiness(0).nominal_feasible
    assert infeasible.readiness(0).optional_throughput is None
    return {
        "capacity_order_reversal": {"b=1": {"AB": "11/5", "BA": "2"}, "b=4": {"AB": "5/8", "BA": "13/20"}},
        "fixed_capacity_pair_cycle": {"b": "3", "AB_vs_BA": ["3", "10/3"], "BC_vs_CB": ["29/8", "11/3"], "CA_vs_AC": ["8/3", "19/7"]},
        "dynamic_pair_index_greedy_failure": {"greedy_order": [0, 1, 2], "greedy_time": "13/2", "optimal_order": [1, 2, 0], "optimal_time": "356/55"},
    }


def validation_checks(counts: dict) -> None:
    good = Model(1, (Module(1, 1, 0),))
    good.exit_time(1)  # Validate masks before cache lookup (True compares equal to 1).
    invalid = [lambda: Module(0, 1, 0), lambda: Module(1, 0, 0), lambda: Module(1, 1, -1),
               lambda: Module(1.0, 1, 0), lambda: Model(-1, good.modules), lambda: Model(1, ()),
               lambda: Model(True, good.modules), lambda: Model(1, (1,)), lambda: good.exit_time(-1),
               lambda: good.exit_time(2), lambda: good.exit_time(True), lambda: good.exit_time(1.0),
               lambda: good.readiness(-1), lambda: good.readiness(0.5)]
    for operation in invalid:
        try:
            operation()
        except (ValueError, TypeError):
            counts["invalid_input_rejections"] += 1
        else:
            raise AssertionError("Invalid parameter accepted")


def startup_checks(counts: dict) -> dict:
    """Check constructions and local boundary signs for the two-module theorem.

    Both d_i are strictly positive and s=d_1+d_2. The guarantee starts after
    warmup. These finite checks do not establish the continuous reachable-set
    characterization or optimize arbitrary partial-state exit trajectories.
    """
    def evolve(state, modules, allocation, duration):
        return tuple(min(m.M, max(Q(0), p + (v - m.d) * duration))
                     for p, m, v in zip(state, modules, allocation))

    for M1, M2, d1, d2, a1, a2 in product((1, 2, 3), (1, 2, 3),
                                        (Q(1, 2), Q(1), Q(2)),
                                        (Q(1, 2), Q(1), Q(2)),
                                        (1, 2, 3), (1, 2, 3)):
        modules = (Module(M1, a1, d1), Module(M2, a2, d2))
        s, Mmax, Mmin = d1 + d2, Q(max(M1, M2)), Q(min(M1, M2))
        donor = 0 if M1 >= M2 else 1
        receiver = 1 - donor
        # Every sampled point in the triangle is reached by two constant stages.
        for k1, k2 in product(range(5), repeat=2):
            target = (Q(M1 * k1, 4), Q(M2 * k2, 4))
            total = sum(target)
            if total > Mmax:
                continue
            first_allocation = tuple(s if i == donor else Q(0) for i in range(2))
            first_time = total / modules[receiver].d
            first_state = evolve((Q(0), Q(0)), modules, first_allocation, first_time)
            second_allocation = tuple(s if i == receiver else Q(0) for i in range(2))
            second_time = target[receiver] / modules[donor].d
            reached = evolve(first_state, modules, second_allocation, second_time)
            assert reached == target
            counts["startup_reachable_point_constructions"] += 1
        # Exact boundary allocations show the derivative cannot point out of Q<=Mmax.
        low = max(Q(0), Mmax - modules[1].M)
        high = min(modules[0].M, Mmax)
        for k in range(5):
            p1 = low + (high - low) * k / 4
            state = (p1, Mmax - p1)
            for k1 in range(5):
                for k2 in range(5 - k1):
                    derivative = sum(reflected_derivative(p, m.M, s * k / 4, m.d)
                                     for p, m, k in zip(state, modules, (k1, k2)))
                    assert derivative <= 0
                    counts["startup_invariant_boundary_checks"] += 1
        # Both possible first-cutover endpoints have residual exactly Mmin.
        endpoint_times = []
        for first in (0, 1):
            remaining = 1 - first
            prepared_other = Mmax - modules[first].M
            assert 0 <= prepared_other <= modules[remaining].M
            residual = modules[remaining].M - prepared_other
            assert residual == Mmin
            b = s + modules[first].a
            endpoint_times.append(residual / (b - modules[remaining].d))
        assert min(endpoint_times) == Mmin / max(a1 + d1, a2 + d2)
        counts["startup_endpoint_formula_checks"] += 1
    witness = Model(1, (Module(2, 1, Q(1, 2)), Module(1, 3, Q(1, 2))))
    warm1 = evolve((Q(0), Q(0)), witness.modules, (Q(1), Q(0)), Q(4))
    warm2 = evolve(warm1, witness.modules, (Q(0), Q(1)), Q(2))
    assert warm1 == (2, 0) and warm2 == (1, 1)
    assert evolve(warm2, witness.modules, (Q(1, 2), Q(1, 2)), Q(100)) == warm2
    assert witness.exit_time(1) == Q(2, 3) and witness.exit_time(2) == Q(4, 7)
    assert witness.readiness(Q(1, 2)).upkeep == 1
    assert (witness.modules[0].M - warm2[0]) / (witness.s + witness.modules[1].a - witness.modules[0].d) == Q(2, 7)
    return {"parameters": {"s": "1", "M": ["2", "1"], "a": ["1", "3"], "d": ["1/2", "1/2"], "H": "1/2"},
            "warmup": [{"allocation": ["1", "0"], "duration": "4", "end_state": ["2", "0"]},
                       {"allocation": ["0", "1"], "duration": "2", "end_state": ["1", "1"]}],
            "partial_state_exit_time": "2/7", "pure_singleton_exit_times": ["2/3", "4/7"],
            "recurring_upkeep": "1", "scope": "Warmup is paid and precedes the readiness guarantee; both losses are strictly positive."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "build" / "heterogeneous-verification.json")
    args = parser.parse_args()
    if sys.flags.optimize:
        parser.error("Do not use -O, -OO, or PYTHONOPTIMIZE: assertions must run")
    target = args.output.resolve()
    immutable = (ROOT / "checkpoints").resolve()
    if target == immutable or immutable in target.parents:
        parser.error("Output cannot overwrite an immutable checkpoint")
    counts = {key: 0 for key in ("heterogeneous_models", "permutation_evaluations", "subset_DP_comparisons",
              "deadline_threshold_and_interval_probes", "ready_set_monotonicity_edges", "homogeneous_formula_comparisons",
              "reflected_local_allocation_states", "normal_upkeep_reflection_states", "completion_potential_jumps", "invalid_input_rejections",
              "startup_reachable_point_constructions", "startup_invariant_boundary_checks", "startup_endpoint_formula_checks")}
    validation_checks(counts)
    finite_instances(counts)
    homogeneous_specialization(counts)
    local_potential_checks(counts)
    example_results = examples(counts)
    example_results["partial_startup_witness"] = startup_checks(counts)
    report = {"schema_version": 1, "status": "PASS", "arithmetic": "fractions.Fraction (exact)",
              "scope": "Finite DP/permutation agreement, threshold evaluation, reflected local inequalities and jumps, exact ordering counterexamples, and two-module startup constructions/invariant boundary checks. Not a continuous-time proof, empirical validation, or novelty audit.",
              "domain": {"two_modules": "All ordered pairs M,a in {1,2}, d in {0,1,2}; s in {0,1,2} (432 models)",
                         "three_modules": "All ordered triples from (M,a,d)={(1,1,0),(2,1,1),(1,2,2),(2,2,3)}; s in {0,1,3} (192 models)",
                         "larger_modules": "12 deterministic four-module and 4 deterministic five-module models; formulas in verifier",
                         "homogeneous": "n=1..5; M in {1,3/2}; a in {1,2}; d in {0,1,2}; s in {0,1,3}; every ready subset",
                         "local_potential": "Two unfinished modules; allocations on quarter-capacity simplex; cold/half/full states; d at 0,b/2,b,b+1; exact grids in verifier",
                         "startup": "Two modules; M,a in {1,2,3}, d in {1/2,1,2}, s=d1+d2 (729 models); quarter-size target grid and quarter-capacity allocation simplex; one separate exact witness",
                         "frontier": "Every finite exact exit threshold, intervening midpoint, and one point above the largest threshold"},
              "counts": counts, "examples": example_results}
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: exact heterogeneous finite checks.\n{target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
