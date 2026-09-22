#!/usr/bin/env python3
"""Exact finite checks of the common-gamma heterogeneous readiness frontier.

Checks use transformed deadlines X=exp(gamma*H) as rational input. Independent
permutation enumeration and per-order fractional-knapsack optimization check
the subset algorithms. They do not exhaust continuous-time policies or prove
the concentration theorem, operational applicability, or publication novelty.
A separately labeled quadratic-loss fixture checks exact analytic certificates
showing that proportional concentration does not extend to every smooth loss.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from itertools import permutations, product
import json
from pathlib import Path
import sys

from proportional import Model, Module

ROOT = Path(__file__).resolve().parents[1]


def direct_order(model: Model, state: tuple[Q, ...], order: tuple[int, ...]) -> Q:
    """Use passive decay and local stage multipliers, without the subset DP."""
    b = model.s + sum((m.a for m, p in zip(model.modules, state) if p == m.M), Q(0))
    x = Q(1)
    for i in order:
        m = model.modules[i]
        passive = state[i] / x
        local = (b - model.gamma * passive) / (b - model.gamma * m.M)
        assert local >= 1
        x *= local
        b += m.a
    return x


def permutation_exit(model: Model, state: tuple[Q, ...]) -> Q:
    remaining = tuple(i for i, (m, p) in enumerate(zip(model.modules, state)) if p < m.M)
    return min(direct_order(model, state, order) for order in permutations(remaining))


def affine_orders(model: Model) -> list[tuple[Q, tuple[Q, ...], tuple[int, ...]]]:
    """Compute x_final=A-sum_i w_i*p_i for every complete serial order.

    An initially full module may wait until its position in this auxiliary
    feasible schedule class. All orders are enumerated, including those that
    transfer all initially full modules immediately. Thus optimizing over the
    union gives the same frontier, without relying on the candidate formula.
    """
    rows = []
    for order in permutations(range(len(model.modules))):
        A, weights, b = Q(1), [Q(0)] * len(model.modules), model.s
        for i in order:
            m = model.modules[i]
            alpha = b / (b - model.gamma * m.M)
            beta = model.gamma / (b - model.gamma * m.M)
            A *= alpha
            weights = [w * alpha for w in weights]
            weights[i] += beta
            b += m.a
        assert A - sum((w * m.M for w, m in zip(weights, model.modules)), Q(0)) == 1
        rows.append((A, tuple(weights), order))
    return rows


def knapsack_frontier(model: Model, X: Q, rows: list) -> tuple[Q, tuple[Q, ...]]:
    """Minimize linear upkeep under each affine order's deadline halfspace.

    For a fixed order each unit of initial p_i costs gamma and reduces the
    exit multiplier by w_i. Filling decreasing weights is exact fractional
    knapsack. No concentrated-state or partial-first assumption is imposed.
    """
    candidates = []
    for A, weights, _ in rows:
        deficit = max(Q(0), A - X)
        state = [Q(0)] * len(model.modules)
        for i in sorted(range(len(model.modules)), key=lambda j: (-weights[j], j)):
            amount = min(model.modules[i].M, deficit / weights[i])
            state[i] = amount
            deficit -= weights[i] * amount
        assert deficit == 0
        assert A - sum((w * p for w, p in zip(weights, state)), Q(0)) <= X
        candidates.append((model.gamma * sum(state), tuple(state)))
    return min(candidates)


def heterogeneous_models():
    for n, seed in product(range(1, 5), range(8)):
        gamma = (Q(1, 3), Q(2, 3))[seed % 2]
        modules = tuple(Module(Q(1 + (2 * i + seed) % 5, 1 + (seed + i) % 2),
                               Q(1 + (3 * i + seed) % 7, 1 + (seed // 2) % 2))
                        for i in range(n))
        s = max(gamma * m.M for m in modules) + Q(1 + seed % 3, 2)
        yield Model(s, gamma, modules)
    for n, mixed in product(range(1, 5), (False, True)):
        modules = tuple(Module(Q(i + 1, 2), Q(i % 2 if mixed else 0)) for i in range(n))
        yield Model(Q(n, 4) + 1, Q(1, 2), modules)


def check_heterogeneous(counts: dict) -> None:
    for model in heterogeneous_models():
        counts["heterogeneous_models"] += 1
        n = len(model.modules)
        for fractions in product((Q(0), Q(1, 3), Q(1)), repeat=n):
            state = tuple(m.M * f for m, f in zip(model.modules, fractions))
            result = model.exit_schedule(state)
            assert result.multiplier == permutation_exit(model, state)
            assert direct_order(model, state, result.order) == result.multiplier
            assert model.schedule_multiplier(state, result.order) == result.multiplier
            counts["full_state_dp_permutation_comparisons"] += 1
        cold_values = []
        for mask in range(model.full_mask + 1):
            state = tuple(m.M if mask & (1 << i) else Q(0)
                          for i, m in enumerate(model.modules))
            cold = model.cold_multiplier(mask)
            assert cold == permutation_exit(model, state) == model.exit_multiplier(state)
            assert direct_order(model, state, model.cold_order(mask)) == cold
            cold_values.append(cold)
            counts["cold_subset_dp_permutation_comparisons"] += 1
        Xs = {Q(1), model.cold_multiplier(), model.cold_multiplier() + 1}
        boundaries = sorted(set(cold_values))
        Xs.update(boundaries)
        Xs.update((lo + hi) / 2 for lo, hi in zip(boundaries, boundaries[1:]))
        rows = affine_orders(model)
        counts["affine_order_constraints"] += len(rows)
        previous = None
        for X in sorted(Xs):
            result = model.readiness(X)
            independent_cost, independent_state = knapsack_frontier(model, X, rows)
            assert result.upkeep == independent_cost
            assert model.exit_multiplier(independent_state) <= X
            assert result.exit_multiplier == direct_order(model, result.state, result.order) <= X
            assert model.exit_multiplier(result.state) <= result.exit_multiplier
            assert result.upkeep == model.gamma * sum(result.state)
            assert sum(0 < p < m.M for p, m in zip(result.state, model.modules)) <= 1
            assert result.nominal_feasible == (result.upkeep <= model.s)
            assert result.optional_throughput == (model.s - result.upkeep
                                                   if result.nominal_feasible else None)
            if not result.nominal_feasible:
                counts["nominally_infeasible_deadlines"] += 1
            if previous is not None:
                assert result.upkeep <= previous
                counts["monotonicity_comparisons"] += 1
            previous = result.upkeep
            if X == 1:
                assert result.upkeep == model.gamma * sum(m.M for m in model.modules)
                assert result.state == tuple(m.M for m in model.modules)
            if X >= model.cold_multiplier():
                assert result.upkeep == 0 and all(p == 0 for p in result.state)
                counts["zero_upkeep_plateau_checks"] += 1
            counts["frontier_knapsack_comparisons"] += 1
            counts["per_order_knapsack_optimizations"] += len(rows)


def check_homogeneous(counts: dict) -> None:
    for n, M, a, gamma in product(range(1, 5), (Q(1, 2), Q(2)),
                                 (Q(1), Q(3)), (Q(1, 3), Q(1))):
        s = gamma * M + Q(1, 2)
        model = Model(s, gamma, (Module(M, a),) * n)
        tails = [Q(1)] * (n + 1)
        for k in range(n - 1, -1, -1):
            b = s + k * a
            tails[k] = b / (b - gamma * M) * tails[k + 1]
        for k in range(n):
            b = s + k * a
            for j in range(5):
                r = M * j / 4
                X = (b - gamma * r) / (b - gamma * M) * tails[k + 1]
                expected = gamma * (k * M + r)
                result = model.readiness(X)
                assert result.upkeep == expected
                counts["homogeneous_frontier_regressions"] += 1


def check_counterexample(counts: dict) -> dict:
    model = Model(1, Q(1, 10), (Module(1, 1), Module(Q(1, 10), 100)))
    state = (Q(1, 10), Q(0))
    partial_first = direct_order(model, state, (0, 1))
    cold_first = direct_order(model, state, (1, 0))
    assert partial_first == Q(220, 199)
    assert cold_first == Q(1009901, 998910) < partial_first
    assert model.exit_schedule(state).order == (1, 0)
    assert model.exit_multiplier(state) == cold_first
    counts["prescribed_partial_first_counterexamples"] += 1
    return {"gamma": "1/10", "s": "1", "modules": [{"M": "1", "a": "1"},
            {"M": "1/10", "a": "100"}], "initial_state": ["1/10", "0"],
            "partial_first_multiplier": str(partial_first),
            "cold_first_multiplier": str(cold_first),
            "meaning": "Partial-first is not optimal for every prescribed concentrated state; it suffices for an upkeep-minimizing witness."}


def check_validation(counts: dict) -> None:
    model = Model(2, 1, (Module(1, 1),))
    cases = [
        (TypeError, lambda: Module(1.0, 1)),
        (TypeError, lambda: Module(True, 1)),
        (ValueError, lambda: Module(0, 1)),
        (ValueError, lambda: Module(1, -1)),
        (ValueError, lambda: Model(1, 1, (Module(1, 1),))),
        (ValueError, lambda: Model(2, 0, (Module(1, 1),))),
        (ValueError, lambda: Model(2, 1, ())),
        (TypeError, lambda: Model(2, 1, ((1, 1),))),
        (TypeError, lambda: model.readiness(1.0)),
        (TypeError, lambda: model.readiness(True)),
        (ValueError, lambda: model.readiness(Q(1, 2))),
        (ValueError, lambda: model.exit_multiplier(())),
        (ValueError, lambda: model.exit_multiplier((Q(3, 2),))),
        (ValueError, lambda: model.exit_multiplier((Q(-1, 2),))),
        (TypeError, lambda: model.exit_multiplier((0.5,))),
        (ValueError, lambda: model.cold_multiplier(2)),
        (TypeError, lambda: model.cold_multiplier(True)),
        (ValueError, lambda: model.schedule_multiplier((Q(0),), ())),
        (ValueError, lambda: model.schedule_multiplier((Q(0),), (0, 0))),
        (ValueError, lambda: model.schedule_multiplier((Q(0),), (True,))),
        (ValueError, lambda: model.schedule_multiplier((Q(1),), (0,))),
    ]
    for expected, call in cases:
        try:
            call()
        except expected:
            counts["input_validation_rejections"] += 1
        else:
            raise AssertionError(f"Expected {expected.__name__}")


def check_quadratic_boundary(counts: dict) -> dict:
    """Verify rational certificates, not a quadratic exit or upkeep oracle.

    Two modules have g(p)=p**2. During the first serial stage its prepared
    module has net rate at least s-M**2; the passive module loses at most
    p(0)**2 per unit time. After one cutover the second has net rate at least
    s+a-M**2. These give a feasible distributed-state upper time bound.
    Any exit by H receives at most (s+a)*H work before the final cutover.
    Ignoring all loss gives necessary work bounds for concentrated states.
    """
    M, a, s, H, p = Q(1), Q(1, 100), Q(10), Q(23, 500), Q(4, 5)
    first_time = (M - p) / (s - M * M)
    passive_lower = p - p * p * first_time
    second_time = (M - passive_lower) / (s + a - M * M)
    time_upper = first_time + second_time
    upkeep = 2 * p * p
    assert first_time == Q(1, 45)
    assert passive_lower == Q(884, 1125) > 0
    assert second_time == Q(964, 40545)
    assert time_upper == Q(373, 8109)
    assert H - time_upper == Q(7, 4054500) > 0
    assert upkeep == Q(32, 25) < s
    work_upper = (s + a) * H
    # A no-full concentrated state has at most M total preparation initially.
    # Reaching two full targets requires at least M additional work, even
    # without loss; the available work is strictly smaller.
    assert work_upper == Q(23023, 50000) < M
    partial_lower = M - work_upper
    concentrated_cost_lower = M * M + partial_lower * partial_lower
    assert partial_lower == Q(26977, 50000)
    assert concentrated_cost_lower - upkeep == Q(27758529, 2500000000) > 0
    assert 2 * M * M > concentrated_cost_lower  # The both-full case.
    counts["quadratic_nonconcentration_certificates"] += 1
    return {
        "scope": "Separate nonlinear-loss boundary fixture; exact analytic bounds, not an implementation or solution of the quadratic optimization problem.",
        "model": "n=2; M_1=M_2=1; a_1=a_2=1/100; s=10; g_1(p)=g_2(p)=p^2 on [0,1]; physical deadline H=23/500.",
        "distributed_state": [str(p), str(p)],
        "distributed_upkeep": str(upkeep),
        "first_stage_time_upper": str(first_time),
        "remaining_preparation_lower": str(passive_lower),
        "second_stage_time_upper": str(second_time),
        "exit_time_upper": str(time_upper),
        "deadline_margin": str(H - time_upper),
        "available_copy_work_upper": str(work_upper),
        "one_full_required_partial_lower": str(partial_lower),
        "concentrated_upkeep_lower": str(concentrated_cost_lower),
        "strict_upkeep_gap_lower": str(concentrated_cost_lower - upkeep),
        "conclusion": "The displayed two-partial state meets H at upkeep 32/25, while every deadline-feasible state with at most one partial module has strictly greater upkeep. General monotone smooth loss does not inherit the common-linear concentration theorem; no unequal-gamma conclusion is inferred."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "build" / "proportional-frontier-verification.json")
    args = parser.parse_args()
    if sys.flags.optimize:
        parser.error("Do not use -O, -OO, or PYTHONOPTIMIZE: assertions must run")
    target = args.output.resolve()
    immutable = (ROOT / "checkpoints").resolve()
    if target == immutable or immutable in target.parents:
        parser.error("Output cannot overwrite an immutable checkpoint")
    counts = {name: 0 for name in (
        "heterogeneous_models", "full_state_dp_permutation_comparisons",
        "cold_subset_dp_permutation_comparisons", "affine_order_constraints",
        "frontier_knapsack_comparisons", "per_order_knapsack_optimizations",
        "monotonicity_comparisons", "nominally_infeasible_deadlines",
        "zero_upkeep_plateau_checks", "homogeneous_frontier_regressions",
        "prescribed_partial_first_counterexamples", "input_validation_rejections",
        "quadratic_nonconcentration_certificates")}
    check_heterogeneous(counts)
    check_homogeneous(counts)
    counterexample = check_counterexample(counts)
    check_validation(counts)
    quadratic_boundary = check_quadratic_boundary(counts)
    report = {
        "schema_version": 1, "status": "PASS",
        "scope": "Exact finite checks of common-gamma full-state exit DP, ready/cold multiplier DP, and heterogeneous recurring frontier against all-permutation affine-constraint fractional-knapsack optimization; separately labeled analytic quadratic-loss nonconcentration certificate. Not an exhaustion of continuous-time policies, proof of concentration, empirical validation, or novelty assessment.",
        "arithmetic": "fractions.Fraction only. Proportional-model input is rational X=exp(gamma*H), rather than rational physical H. The separate quadratic fixture uses a rational physical deadline and analytic time/work bounds.",
        "assumptions": "Proportional calculations: gamma>0, M_i>0, a_i>=0, s>max_i gamma*M_i; independent instantaneous cutover; paid initialization. The separately labeled quadratic fixture has its own model.",
        "domain": {
            "heterogeneous": "n=1..4, seeds=0..7; gamma=(1/3,2/3)[seed%2]; M_i=(1+(2*i+seed)%5)/(1+(seed+i)%2); a_i=(1+(3*i+seed)%7)/(1+(seed//2)%2); s=max gamma*M_i+(1+seed%3)/2.",
            "zero_releases": "For every n=1..4, gamma=1/2, M_i=(i+1)/2, s=n/4+1; either all a_i=0 or a_i=i%2 (zero-based indices).",
            "initial_states": "Each p_i/M_i in {0,1/3,1}; all Cartesian products.",
            "deadlines": "All distinct cold-subset multipliers, every adjacent midpoint, X=1, and cold-full-system multiplier plus 1.",
            "homogeneous": "n=1..4; M in {1/2,2}; a in {1,3}; gamma in {1/3,1}; s=gamma*M+1/2; all k=0..n-1 and partial fractions {0,1/4,1/2,3/4,1}."},
        "counts": counts,
        "prescribed_partial_first_counterexample": counterexample,
        "quadratic_nonconcentration_boundary": quadratic_boundary,
    }
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: exact proportional exit and readiness checks.\n{target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
