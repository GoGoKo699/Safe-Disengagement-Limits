#!/usr/bin/env python3
"""Small numerical cross-checks and exact fixtures for unequal proportional loss.

The solver uses floating transcendental comparisons, not certified optimization.
Independent permutation/one-partial searches use bisection of direct serial
trajectories. Common-gamma rational LPs and algebraic fixtures are exact.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from itertools import permutations
import json
import math
from pathlib import Path
import sys

from unequal_proportional import (ProportionalModel as Model, ProportionalModule as Module,
                                  cold_values, frontier, subset_tables)

ROOT = Path(__file__).resolve().parents[1]
COMPARISON_TOLERANCE = 2e-9


def independent_permutation_frontier(model, H, counts):
    """Enumerate ready sets, complete orders and every possible partial position.

    Required partial preparation is found by bisection of the serial ODE stage
    times, without the candidate inversion or any subset DP from the solver.
    Full candidate coordinates may wait for their declared turn; this remains
    a valid schedule and the ready-set enumeration includes immediate transfer.
    """
    n = len(model.modules)
    best = float(sum((m.gamma * m.M for m in model.modules), Q(0)))
    for mask in range(1 << n):
        ready = tuple(i for i in range(n) if mask >> i & 1)
        remaining = tuple(i for i in range(n) if not mask >> i & 1)
        base = float(sum((model.modules[i].gamma * model.modules[i].M for i in ready), Q(0)))
        for order in permutations(remaining):
            capacity = model.s + sum((model.modules[i].a for i in ready), Q(0))
            stages = []
            for i in order:
                m = model.modules[i]
                D = capacity - m.gamma * m.M
                stages.append((i, float(m.M), float(m.gamma), float(D), D > 0))
                capacity += m.a
            def finish(partial, amount):
                elapsed = 0.0
                for i, M, gamma, D, eligible in stages:
                    p = amount * math.exp(-gamma * elapsed) if i == partial else 0.0
                    if p == M:
                        continue
                    if not eligible:
                        return math.inf
                    elapsed += math.log1p(gamma * (M - p) / D) / gamma
                return elapsed
            counts["independent_complete_orders"] += 1
            if finish(None, 0.0) <= H:
                best = min(best, base)
            for partial in remaining:
                M = float(model.modules[partial].M)
                if finish(partial, M) > H:
                    continue
                low, high = 0.0, M
                if finish(partial, 0.0) <= H:
                    high = 0.0
                else:
                    for _ in range(60):
                        middle = (low + high) / 2
                        if finish(partial, middle) <= H:
                            high = middle
                        else:
                            low = middle
                best = min(best, base + float(model.modules[partial].gamma) * high)
                counts["independent_partial_position_minimizations"] += 1
    return best


def numerical_models():
    models = [Model(s, (Module(1, a, gamma),)) for s, a, gamma in
              ((0, 0, 1), (1, 0, 1), (2, 0, 1), (Q(1, 2), 1, Q(1, 2)))]
    models += [Model(s, modules) for s, modules in (
        (0, (Module(1, 3, 1), Module(1, 0, 2))),
        (1, (Module(1, 0, 1), Module(1, 2, 2))),
        (1, (Module(1, 1, 2), Module(1, 1, Q(1, 2)))),
        (2, (Module(1, 0, Q(1, 2)), Module(2, 1, 1))),
        (Q(3, 2), (Module(2, 1, Q(1, 2)), Module(1, 0, 1))),
        (1, (Module(Q(1, 2), Q(3, 10), 1), Module(Q(1, 2), Q(1, 10), Q(1, 2)))),
    )]
    for n, seeds in ((3, range(4)), (4, range(2))):
        for seed in seeds:
            modules = tuple(Module(Q(1 + (seed + i) % 3, 2), Q((seed + 2 * i) % 4, 2),
                                   Q(1 + (seed + i) % 3, 2)) for i in range(n))
            models.append(Model(Q(seed + 1, 2), modules))
    return models


def numerical_checks(counts):
    maximum_cost_error = 0.0
    maximum_deadline_excess = 0.0
    for model in numerical_models():
        for H in (0.0, 0.25, 1.0, 3.0, 10.0):
            result = frontier(model, H)
            independent = independent_permutation_frontier(model, H, counts)
            error = abs(result.upkeep - independent) / max(1.0, abs(independent))
            assert error <= COMPARISON_TOLERANCE
            assert all(0 <= p <= float(m.M) for p, m in zip(result.preparation, model.modules))
            assert len([p for p, m in zip(result.preparation, model.modules) if 0 < p < float(m.M)]) <= 1
            assert result.completion_time <= H + COMPARISON_TOLERANCE * max(1.0, H)
            assert abs(result.upkeep - math.fsum(float(m.gamma) * p for m, p in zip(model.modules, result.preparation))) <= COMPARISON_TOLERANCE
            if H == 0:
                assert result.ready == tuple(range(len(model.modules))) and result.completion_time == 0
            maximum_cost_error = max(maximum_cost_error, error)
            maximum_deadline_excess = max(maximum_deadline_excess, result.completion_time - H)
            counts["numerical_frontier_comparisons"] += 1
    # Pure barriers: a subfull single module cannot arrive at its equilibrium
    # in finite time; finite H therefore requires the exactly full state.
    for spare in (Q(0), Q(1, 2), Q(1)):
        result = frontier(Model(spare, (Module(1, 0, 1),)), 100.0)
        assert result.preparation == (1.0,) and result.upkeep == 1.0
        counts["exact_barrier_structure_checks"] += 1
    return maximum_cost_error, maximum_deadline_excess


def common_gamma_fractional_knapsack(model, gamma, X, counts):
    """Independent exact whole-box fixed-order LP from rational weights."""
    best = None
    for order in permutations(range(len(model.modules))):
        capacity = model.s
        factors, denominators = [], []
        for i in order:
            D = capacity - gamma * model.modules[i].M
            assert D > 0
            factors.append(capacity / D)
            denominators.append(D)
            capacity += model.modules[i].a
        A = math.prod(factors)
        weights, tail = [Q(0)] * len(order), Q(1)
        for position in range(len(order) - 1, -1, -1):
            weights[position] = gamma * tail / denominators[position]
            tail *= factors[position]
        assert sum((w * model.modules[i].M for w, i in zip(weights, order)), Q(0)) == A - 1
        assert all(x > y for x, y in zip(weights, weights[1:]))
        required, prepared_total = max(Q(0), A - X), Q(0)
        for weight, i in zip(weights, order):
            prepared = min(model.modules[i].M, required / weight)
            prepared_total += prepared
            required -= weight * prepared
        assert required == 0
        cost = gamma * prepared_total
        best = cost if best is None else min(best, cost)
        counts["exact_common_gamma_permutation_LPs"] += 1
    return best


def common_gamma_checks(counts):
    maximum_error = 0.0
    for n in range(1, 5):
        for gamma in (Q(1, 2), Q(1, 3)):
            modules = tuple(Module(Q(2 + i % 2, 2), Q(i % 3, 2), gamma) for i in range(n))
            model = Model(max(m.gamma * m.M for m in modules) + 1, modules)
            for X in (Q(1), Q(5, 4), Q(2), Q(4), Q(10)):
                exact = common_gamma_fractional_knapsack(model, gamma, X, counts)
                H = math.log(float(X)) / float(gamma)
                result = frontier(model, H)
                error = abs(result.upkeep - float(exact)) / max(1.0, abs(float(exact)))
                assert error <= COMPARISON_TOLERANCE
                maximum_error = max(maximum_error, error)
                counts["common_gamma_exact_reference_comparisons"] += 1
    return maximum_error


def exact_pair_fixtures(counts):
    # gamma_j=1, gamma_k=2: endpoint multiplier21/8, b_j=3,b_k=4,
    # D_j=D_k=2. The equal-endpoint cost decreases strictly in x.
    last = None
    for x in (Q(2, 5), Q(9, 20), Q(1, 2), Q(11, 20), Q(3, 5)):
        y = ((3 - x) ** 2 - Q(21, 4)) / 2
        assert 0 < x < 1 and 0 < y < 1
        assert (4 * ((3 - x) / 2) ** 2 - 2 * y) / 2 == Q(21, 8)
        cost = x + 2 * y
        assert last is None or cost < last
        last = cost
        counts["exact_pair_endpoint_identities"] += 1
    # At a cold predecessor with gamma_j<=gamma_k, an interior move can
    # strictly improve pair cost. Both schedules retain endpoint multiplier4.
    boundary_costs = []
    for x in (Q(0), Q(1, 100)):
        y = ((3 - x) ** 2 - 8) / 2
        assert 0 <= x < 1 and 0 < y < 1
        assert (4 * ((3 - x) / 2) ** 2 - 2 * y) / 2 == 4
        boundary_costs.append(x + 2 * y)
        counts["exact_pair_endpoint_identities"] += 1
    assert boundary_costs[1] < boundary_costs[0]
    # gamma_j=2,gamma_k=1: three rational square roots make the x values
    # equally spaced, permitting an exact strict-concavity certificate.
    t = Q(1, 100)
    roots = (Q(3, 2) * (1 - t * t - 2 * t) / (1 + t * t),
             Q(3, 2), Q(3, 2) * (1 - t * t + 2 * t) / (1 + t * t))
    xs, costs = [], []
    for root in roots:
        x, y = (3 - root * root) / 2, 4 * root - Q(11, 2)
        assert 0 < x < 1 and 0 < y < 1
        assert (4 * root - y) / 3 == Q(11, 6)
        xs.append(x)
        costs.append(2 * x + y)
        counts["exact_pair_endpoint_identities"] += 1
    assert xs[1] == (xs[0] + xs[2]) / 2
    assert costs[1] - (costs[0] + costs[2]) / 2 == Q(12, 10001) > 0
    assert min(costs[0], costs[2]) < costs[1]
    return {"increasing_coefficient_pair": "Exact decreasing-cost equal-endpoint identities with gamma=(1,2)",
            "decreasing_coefficient_pair": {"gamma": ["2", "1"], "strict_midpoint_concavity_gap": "12/10001"}}


def global_cold_prefix_fixture(counts):
    model = Model(1, (Module(Q(1, 2), Q(3, 10), 1), Module(Q(1, 2), Q(1, 10), Q(1, 2))))
    # Exact rational certificates around the algebraic optimum. Rationalizing
    # its numerator gives 29/[20*(26*sqrt(2)+21*sqrt(3))].
    assert (26 ** 2) * 2 - (21 ** 2) * 3 == 29
    assert Q(7, 5) ** 2 < 2 and Q(17, 10) ** 2 < 3
    denominator_lower = 20 * (26 * Q(7, 5) + 21 * Q(17, 10))
    assert denominator_lower == 1442 > 1352
    assert Q(29, 1442) < Q(29, 1352)
    assert Q(18, 11) < Q(13, 10) ** 2
    assert 1 - Q(3, 4) * Q(13, 10) == Q(1, 40) > Q(29, 1352)
    assert Q(7, 45) > Q(29, 1352) and Q(1, 4) > Q(29, 1352)
    assert 2 * Q(26, 21) ** 2 == Q(1352, 441) > 3
    assert Q(4, 3) ** 2 * Q(11, 6) == Q(88, 27) > 3
    counts["exact_global_cold_prefix_certificates"] += 1
    expected = 29 / (20 * (26 * math.sqrt(2) + 21 * math.sqrt(3)))
    result = frontier(model, math.log(3))
    independent = independent_permutation_frontier(model, math.log(3), counts)
    assert abs(result.upkeep - expected) <= COMPARISON_TOLERANCE
    assert abs(independent - expected) <= COMPARISON_TOLERANCE
    assert result.ready == () and result.partial_index == 1 and result.order == (0, 1)
    assert result.upkeep < float(Q(29, 1352))
    assert result.completion_time <= math.log(3) + COMPARISON_TOLERANCE
    return {"parameters": {"s": "1", "A": {"M": "1/2", "a": "3/10", "gamma": "1"},
                           "B": {"M": "1/2", "a": "1/10", "gamma": "1/2"}, "H": "log(3)"},
            "global_upkeep_algebraic": "29/[20*(26*sqrt(2)+21*sqrt(3))]",
            "floating_upkeep": result.upkeep, "attaining_order": list(result.order),
            "partial_index": result.partial_index,
            "strict_comparison": "Optimum < 29/1442 < 29/1352, while every partial-first candidate costs at least 29/1352; ready states cost >= 1/4 and the cold state misses H.",
            "scope": "The rational inequalities certify the displayed algebraic comparisons; the numerical solver output itself is not a certified transcendental endpoint decision."}


def closure_seed_checks(counts):
    def closure(model, seed):
        completed = seed
        while True:
            capacity = model.s + sum((m.a for i, m in enumerate(model.modules) if completed >> i & 1), Q(0))
            added = sum(1 << i for i, m in enumerate(model.modules)
                        if not completed >> i & 1 and capacity > m.gamma * m.M)
            if not added:
                return completed
            completed |= added
    models = numerical_models() + [Model(1, (Module(1, 2, 1), Module(1, 0, 2)))]
    maximum_plateau_error = 0.0
    for model in models:
        n, full = len(model.modules), (1 << len(model.modules)) - 1
        capacities, costs = subset_tables(model)
        cold, _ = cold_values(model, capacities)
        successful = []
        cold_closure = closure(model, 0)
        cold_blocked = cold_closure != full
        if cold_blocked:
            assert all(m.gamma * m.M >= capacities[cold_closure] >= model.s
                       for i, m in enumerate(model.modules) if not cold_closure >> i & 1)
        for seed in range(1 << n):
            reachable = closure(model, seed) == full
            enumeration = False
            remaining = tuple(i for i in range(n) if not seed >> i & 1)
            for order in permutations(remaining):
                capacity = capacities[seed]
                feasible = True
                for i in order:
                    m = model.modules[i]
                    if capacity <= m.gamma * m.M:
                        feasible = False
                        break
                    capacity += m.a
                enumeration |= feasible
                counts["exact_accessible_permutation_checks"] += 1
            assert reachable == enumeration == math.isfinite(cold[seed])
            counts["exact_closure_subset_comparisons"] += 1
            if reachable:
                successful.append(seed)
                if cold_blocked:
                    selected = [m for i, m in enumerate(model.modules) if seed >> i & 1]
                    assert seed & (full ^ cold_closure)
                    assert costs[seed] >= capacities[cold_closure] >= model.s
                    assert any(m.gamma * m.M >= model.s for m in selected)
                    counts["exact_seed_barrier_inequalities"] += 1
                    if costs[seed] == model.s:
                        assert capacities[cold_closure] == model.s
                        assert len(selected) == 1 and selected[0].gamma * selected[0].M == model.s
                        counts["exact_seed_equality_singletons"] += 1
        minimum = min(costs[seed] for seed in successful)
        H_star = min(cold[seed] for seed in successful if costs[seed] == minimum)
        assert math.isfinite(H_star)
        for H in (H_star, H_star + 0.25, H_star + 1):
            cost = frontier(model, H).upkeep
            error = abs(cost - float(minimum)) / max(1.0, abs(float(minimum)))
            assert error <= COMPARISON_TOLERANCE
            maximum_plateau_error = max(maximum_plateau_error, error)
            counts["floating_seed_plateau_probes"] += 1
    # Nontrivial equality case: initialization buys a seed costing exactly the
    # normal spare rate, but no full seed is reachable from cold in finite time
    # under the same maximal-loss normal dynamics.
    equality = models[-1]
    assert closure(equality, 0) != 3 and closure(equality, 1) == 3
    assert equality.modules[0].gamma * equality.modules[0].M == equality.s
    assert equality.s / equality.modules[0].gamma == equality.modules[0].M
    assert equality.s / equality.modules[1].gamma < equality.modules[1].M
    H_star = math.log(3) / 2
    assert abs(frontier(equality, H_star).upkeep - 1) <= COMPARISON_TOLERANCE
    return {"maximum_floating_plateau_scaled_error": maximum_plateau_error,
            "equality_fixture": {"s": "1", "modules": [{"M": "1", "a": "2", "gamma": "1"},
                                                          {"M": "1", "a": "0", "gamma": "2"}],
                                 "minimum_seed_cost": "1", "plateau_start": "log(3)/2",
                                 "cold_start_obstruction": "Normal full-rate equilibria are M_A and M_B/2; the first is approached only asymptotically and the second is below target."},
            "scope": "Closure, accessibility and seed comparisons use exact rational arithmetic. Plateau endpoint values are floating consistency checks, not certified transcendental comparisons."}


def critical_startup_fixtures(counts):
    reachable = Model(1, (Module(Q(2, 5), 1, 2), Module(1, Q(1, 10), 1)))
    target = (Q(2, 5), Q(1, 5))
    assert 2 * target[0] + target[1] == 1
    assert (2 - target[1]) / (2 - 1) == Q(9, 5)
    # Displayed all-concentrated lower-bound cases, evaluated algebraically.
    assert reachable.s == reachable.modules[1].gamma * reachable.modules[1].M
    assert Q(2) > Q(9, 5) and Q(5) > Q(9, 5) ** 2
    assert reachable.modules[1].gamma * reachable.modules[1].M >= 1
    assert 2 - Q(9, 5) == target[1]
    result = frontier(reachable, math.log(9 / 5))
    assert abs(result.upkeep - 1) <= COMPARISON_TOLERANCE
    counts["critical_startup_float_frontier_checks"] += 1
    counts["exact_critical_startup_fixtures"] += 1
    # T=log(10): exponentials for gamma_A=2 and gamma_B=1 are rational.
    vA, vB = Q(3, 5), Q(2, 5)
    assert vA + vB == 1
    pA = vA / 2 * (1 - Q(1, 100))
    pB = vB * (1 - Q(1, 10))
    assert pA == Q(297, 1000) and pB == Q(9, 25)
    counts["exact_warmup_phase_identities"] += 2
    # A then receives full rate for tau=.5*log(203/100).
    after_A = Q(1, 2) + (pA - Q(1, 2)) * Q(100, 203)
    assert after_A == target[0]
    assert pB * 10 == Q(18, 5)
    assert 324 > 203 and 324 < 25 * 203  # r < 18/(5*sqrt203) < M_B.
    assert 100 * Q(203, 100) == 203  # Total warmup is .5*log203.
    counts["exact_warmup_phase_identities"] += 2
    # Alternative finite predecessor: it has strict maintenance slack but is
    # not claimed H-ready. The subsequent full-A interval maps it to the target.
    predecessor = (Q(89, 250), Q(6, 25))
    cost = 2 * predecessor[0] + predecessor[1]
    assert cost == Q(119, 125) < 1
    kappa = Q(125, 119)
    assert kappa * cost == 1 and kappa / (kappa - 1) == Q(125, 6)
    assert Q(1, 2) + (predecessor[0] - Q(1, 2)) / Q(6, 5) ** 2 == target[0]
    assert predecessor[1] / Q(6, 5) == target[1]
    counts["exact_warmup_phase_identities"] += 2
    unreachable = Model(1, (Module(Q(3, 4), 1, 1), Module(Q(3, 4), 1, 1)))
    exact = common_gamma_fractional_knapsack(unreachable, Q(1), Q(7, 5), counts)
    assert exact == 1
    assert (Q(2) - Q(1, 4)) / (Q(2) - Q(3, 4)) == Q(7, 5)
    assert Q(8, 5) > Q(7, 5) and Q(3, 2) > 1
    result_unreachable = frontier(unreachable, math.log(7 / 5))
    assert abs(result_unreachable.upkeep - 1) <= COMPARISON_TOLERANCE
    counts["critical_startup_float_frontier_checks"] += 1
    counts["exact_critical_startup_fixtures"] += 1
    return {
        "reachable_critical_case": {"s": "1", "modules": [{"M": "2/5", "a": "1", "gamma": "2"},
                                                              {"M": "1", "a": "1/10", "gamma": "1"}],
                                    "H": "log(9/5)", "exact_upkeep": "1", "target": ["2/5", "1/5"],
                                    "warmup": [{"allocation": ["3/5", "2/5"], "duration": "log(10)",
                                                "end_state": ["297/1000", "9/25"]},
                                               {"allocation": ["1", "0"], "duration": "log(203/100)/2",
                                                "end_state": ["2/5", "18/(5*sqrt(203))"]}],
                                    "predecessor_alternative": {"state": ["89/250", "6/25"], "upkeep": "119/125",
                                                                "full_A_interval": "log(6/5)", "end_state": ["2/5", "1/5"]}},
        "unreachable_critical_case": {"s": "1", "M": ["3/4", "3/4"], "gamma": ["1", "1"], "a": ["1", "1"],
                                      "H": "log(7/5)", "exact_upkeep": "1",
                                      "analytic_obstruction": "Every ready state's total preparation is at least1, while cold normal Q(t)<=1-exp(-t)<1 for every finite t."},
        "scope": "Checks displayed rational/exponential identities and numerical frontier values. Global optimality and finite-time impossibility rely on the written proofs; no readiness guarantee is asserted during warmup."}


def validation_checks(counts):
    good = Model(2, (Module(1, 0, 1),))
    invalid = (lambda: Module(0, 0, 1), lambda: Module(1, -1, 1), lambda: Module(1, 0, 0),
               lambda: Module(1.0, 0, 1), lambda: Model(-1, good.modules), lambda: Model(1, ()),
               lambda: frontier(good, -1), lambda: frontier(good, math.inf), lambda: frontier(good, math.nan),
               lambda: frontier(good, True), lambda: frontier(good, 1, tolerance=0))
    for operation in invalid:
        try:
            operation()
        except (TypeError, ValueError):
            counts["invalid_input_rejections"] += 1
        else:
            raise AssertionError("Invalid input accepted")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "build" / "unequal-proportional-verification.json")
    args = parser.parse_args()
    if sys.flags.optimize:
        parser.error("Do not use -O, -OO, or PYTHONOPTIMIZE: assertions must run")
    target = args.output.resolve()
    immutable = (ROOT / "checkpoints").resolve()
    if target == immutable or immutable in target.parents:
        parser.error("Output cannot overwrite an immutable checkpoint")
    counts = {key: 0 for key in ("numerical_frontier_comparisons", "independent_complete_orders",
                               "independent_partial_position_minimizations", "exact_barrier_structure_checks",
                               "exact_common_gamma_permutation_LPs", "common_gamma_exact_reference_comparisons",
                               "exact_pair_endpoint_identities", "exact_global_cold_prefix_certificates", "invalid_input_rejections",
                               "exact_accessible_permutation_checks", "exact_closure_subset_comparisons",
                               "exact_seed_barrier_inequalities", "exact_seed_equality_singletons", "floating_seed_plateau_probes",
                               "critical_startup_float_frontier_checks", "exact_critical_startup_fixtures", "exact_warmup_phase_identities")}
    validation_checks(counts)
    numerical_error, deadline_excess = numerical_checks(counts)
    common_error = common_gamma_checks(counts)
    pairs = exact_pair_fixtures(counts)
    global_example = global_cold_prefix_fixture(counts)
    seeds = closure_seed_checks(counts)
    startup = critical_startup_fixtures(counts)
    report = {"schema_version": 1, "status": "PASS",
              "scope": "Finite numerical comparisons against independent permutation/bisection search and exact common-gamma rational LP references; exact pair/global-prefix fixtures, closure/seed comparisons, floating plateau identities and critical-startup fixture identities. Not a proof of concentration, all-policy optimization, certified floating endpoint decisions, or novelty.",
              "domain": {"numerical_models": "16 deterministic models with n=1..4, including a=0, s=0, initial rate barriers and unequal gamma; deadlines 0,1/4,1,3,10 plus the cold-prefix fixture at log(3)",
                         "common_gamma": "n=1..4, gamma in {1/2,1/3}, unequal M and a including zero release, s=max(gamma*M)+1; rational transformed deadline X in {1,5/4,2,4,10}",
                         "exact_fixtures": "Two-coordinate monotonic/concave exchanges, a cold-boundary exchange, and the two-module global cold-prefix example",
                         "closure_and_seeds": "Every subset of the 16 numerical models plus one two-module equality-seed example; all remaining permutations; three floating deadline probes at/above each computed minimum-seed plateau time",
                         "critical_startup": "The two specified pass14 two-module fixtures; exact warmup phase identities and one strict-slack predecessor"},
              "numerical_arithmetic": {"method": "Python binary64 log/exp; 60-step independent bisections",
                                       "comparison_tolerance": COMPARISON_TOLERANCE,
                                       "solver_admission_tolerance": 1e-10,
                                       "maximum_independent_cost_scaled_error": numerical_error,
                                       "maximum_common_gamma_cost_scaled_error": common_error,
                                       "maximum_recounted_deadline_excess": deadline_excess,
                                       "certified": False},
              "exact_arithmetic": "fractions.Fraction for eligibility, common-gamma LP references and stated algebraic comparison certificates",
              "counts": counts, "examples": {"pair_algebra": pairs, "global_cold_prefix": global_example,
                                               "accessibility_and_seed_plateau": seeds, "critical_startup": startup}}
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: unequal-proportional finite numerical checks and exact fixtures.\n{target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
