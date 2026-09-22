#!/usr/bin/env python3
"""Finite exact checks of full-state fixed-loss scheduling and exchange identities.

DP values are compared with independent stage-by-stage permutation evaluation.
Piecewise control checks support the written exchange proof; they do not exhaust
measurable policies. Optional proportional-loss identities use declared floats.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from itertools import permutations, product
import json
import math
from pathlib import Path
import sys

from heterogeneous import Model, Module
from partial_states import solve_partial

ROOT = Path(__file__).resolve().parents[1]
TOLERANCE = 2e-12


def direct_order(model, initial, order, loss_mode="maximum"):
    """Independent stage evolution, explicitly decaying all waiting modules."""
    state = list(initial)
    completed = {i for i, (p, m) in enumerate(zip(state, model.modules)) if p == m.M}
    elapsed = Q(0)
    for stage, i in enumerate(order):
        assert i not in completed
        capacity = model.s + sum((model.modules[j].a for j in completed), Q(0))
        factors = tuple(Q(1) if loss_mode == "maximum" else Q(0) if loss_mode == "zero"
                        else Q(1, 2) if loss_mode == "half" else Q((j + stage) % 3, 2)
                        for j in range(len(model.modules)))
        losses = tuple(m.d * factor for m, factor in zip(model.modules, factors))
        if capacity <= losses[i]:
            return None
        duration = (model.modules[i].M - state[i]) / (capacity - losses[i])
        assert duration > 0
        for j in range(len(state)):
            if j != i and j not in completed:
                state[j] = max(Q(0), state[j] - losses[j] * duration)
        state[i] = model.modules[i].M
        completed.add(i)
        elapsed += duration
    assert len(completed) == len(model.modules)
    return elapsed


def check_state(model, initial, counts):
    ready = tuple(i for i, (p, m) in enumerate(zip(initial, model.modules)) if p == m.M)
    remaining = tuple(i for i in range(len(initial)) if i not in ready)
    best = None
    for order in permutations(remaining):
        value = direct_order(model, initial, order)
        if value is not None:
            best = value if best is None else min(best, value)
        counts["independent_permutation_evaluations"] += 1
    result = solve_partial(model, initial)
    assert result.initial_ready == ready and result.time == best
    assert (result.order is None) == (best is None)
    if best is not None:
        assert tuple(sorted(result.order)) == remaining
        assert direct_order(model, initial, result.order) == best
    if all(p in (0, m.M) for p, m in zip(initial, model.modules)):
        assert result.time == model.exit_time(sum(1 << i for i in ready))
        counts["ready_cold_oracle_agreements"] += 1
    counts["partial_state_DP_comparisons"] += 1
    if best is not None and counts["partial_state_DP_comparisons"] % 7 == 0:
        for mode in ("zero", "half", "alternating"):
            actual = direct_order(model, initial, result.order, mode)
            assert actual is not None and actual <= best
            counts["smaller_loss_attaining_order_checks"] += 1


def finite_DP_checks(counts):
    jobs = tuple(Module(M, a, d) for M, a, d in product((1, 2), (1, 2), (0, 1, 2)))
    for spare, modules in product((0, 1, 2), product(jobs, repeat=2)):
        model = Model(spare, modules)
        for fractions in product((Q(0), Q(1, 2), Q(1)), repeat=2):
            check_state(model, tuple(m.M * f for m, f in zip(modules, fractions)), counts)
        counts["parameter_models"] += 1
    alphabet = (Module(1, 1, 0), Module(2, 1, 1), Module(1, 2, 2))
    for spare, modules in product((0, 1, 3), product(alphabet, repeat=3)):
        model = Model(spare, modules)
        for fractions in product((Q(0), Q(1, 2), Q(1)), repeat=3):
            check_state(model, tuple(m.M * f for m, f in zip(modules, fractions)), counts)
        counts["parameter_models"] += 1
    for seed in range(3):
        modules = tuple(Module(1 + (seed + i) % 3, 1 + (seed + 2 * i) % 4,
                               Q((seed + i) % 5, 2)) for i in range(4))
        model = Model(Q(seed + 1, 2), modules)
        for fractions in product((Q(1, 4), Q(3, 4)), repeat=4):
            check_state(model, tuple(m.M * f for m, f in zip(modules, fractions)), counts)
        counts["parameter_models"] += 1
    for seed in range(2):
        modules = tuple(Module(1 + (seed + i) % 3, 1 + (seed + i) % 4,
                               Q((seed + 2 * i) % 4, 2)) for i in range(5))
        model = Model(Q(seed + 1), modules)
        for shift in range(4):
            initial = tuple(m.M * Q((shift + i) % 5, 4) for i, m in enumerate(modules))
            check_state(model, initial, counts)
        counts["parameter_models"] += 1


def cumulative(segments, t, coordinate=0):
    total, elapsed = Q(0), Q(0)
    for duration, vector in segments:
        used = min(duration, max(Q(0), t - elapsed))
        total += vector[coordinate] * used
        elapsed += duration
    return total


def boundaries(segments):
    points, elapsed = [Q(0)], Q(0)
    for duration, _ in segments:
        elapsed += duration
        points.append(elapsed)
    return points


def lower_reflected_terminal(initial, loss, segments, coordinate=0):
    state = initial
    for duration, vector in segments:
        state = max(Q(0), state + (vector[coordinate] - loss) * duration)
    return state


def reflection_formula(initial, loss, segments, coordinate=0):
    points = boundaries(segments)
    T, total = points[-1], cumulative(segments, points[-1], coordinate)
    return max([Q(0), initial + total - loss * T]
               + [total - cumulative(segments, r, coordinate) - loss * (T - r) for r in points])


def postponement_checks(counts):
    for capacity, loss, initial, f1, f2 in product((Q(1), Q(2), Q(3)),
                                                   (Q(0), Q(1, 2), Q(1), Q(2)),
                                                   (Q(0), Q(1, 2), Q(1)),
                                                   (Q(0), Q(1, 2), Q(1)),
                                                   (Q(0), Q(1, 2), Q(1))):
        original = ((Q(1, 2), (capacity * f1,)), (Q(1, 2), (capacity * f2,)))
        total = cumulative(original, Q(1))
        start = 1 - total / capacity
        postponed = ((start, (Q(0),)), (1 - start, (capacity,)))
        assert cumulative(postponed, Q(1)) == total
        for t in set(boundaries(original) + boundaries(postponed)):
            assert cumulative(postponed, t) <= cumulative(original, t)
        old = lower_reflected_terminal(initial, loss, original)
        new = lower_reflected_terminal(initial, loss, postponed)
        for schedule, state in ((original, old), (postponed, new)):
            assert state == reflection_formula(initial, loss, schedule)
            counts["exact_reflection_formula_checks"] += 1
        assert new >= old
        # Replay the same two-piece suffix; no upper hit occurs with M=10.
        suffix = ((Q(1, 2), (capacity / 2,)), (Q(1, 2), (Q(0),)))
        assert lower_reflected_terminal(new, loss, suffix) >= lower_reflected_terminal(old, loss, suffix)
        assert max(old, new) < 10
        counts["exact_postponement_and_suffix_checks"] += 1


def exchange_checks(counts):
    # Both examples have first completion i=0 at T=1. Other modules stay below
    # their targets. The construction retains original controls after tau and
    # repays displaced prefix work through the explicit FIFO spare-capacity map.
    cases = ((Q(4), (Q(3), Q(5)), (Q(1), Q(1, 2)), (Q(1), Q(0)),
              ((Q(1, 2), (Q(2), Q(2))), (Q(1, 2), (Q(4), Q(0))))),
             (Q(6), (Q(3), Q(5), Q(5)), (Q(1), Q(2), Q(1, 2)), (Q(0), Q(1, 4), Q(1)),
              ((Q(1, 2), (Q(3), Q(2), Q(1))), (Q(1, 2), (Q(5), Q(0), Q(1))))))
    summaries = []
    for capacity, targets, losses, initial, original in cases:
        tau = (targets[0] - initial[0]) / (capacity - losses[0])
        assert lower_reflected_terminal(initial[0], losses[0], original) == targets[0]
        assert cumulative(original, Q(1), 0) >= capacity * tau
        debts = [cumulative(original, tau, j) for j in range(1, len(initial))]
        original_debts = tuple(debts)
        new = [(tau, (capacity,) + (Q(0),) * (len(initial) - 1))]
        time = Q(0)
        for duration, vector in original:
            segment_end = time + duration
            left = max(tau, time)
            remaining = max(Q(0), segment_end - left)
            base = (Q(0),) + vector[1:]
            spare = capacity - sum(base)
            while remaining > 0:
                pending = next((j for j, debt in enumerate(debts) if debt > 0), None)
                if pending is None or spare == 0:
                    new.append((remaining, base))
                    break
                used = min(remaining, debts[pending] / spare)
                new_vector = list(base)
                new_vector[pending + 1] += spare
                new.append((used, tuple(new_vector)))
                debts[pending] -= used * spare
                remaining -= used
            time = segment_end
        assert not any(debts) and sum(duration for duration, _ in new) == 1
        assert all(sum(vector) <= capacity for _, vector in new)
        old_terminal, new_terminal = [], []
        for j in range(1, len(initial)):
            for t in set(boundaries(original) + boundaries(new)):
                assert cumulative(new, t, j) <= cumulative(original, t, j)
            assert cumulative(new, Q(1), j) == cumulative(original, Q(1), j)
            old = lower_reflected_terminal(initial[j], losses[j], original, j)
            improved = lower_reflected_terminal(initial[j], losses[j], new, j)
            assert improved >= old
            assert all(lower_reflected_terminal(initial[j], losses[j], new[:k], j) < targets[j]
                       for k in range(1, len(new) + 1))
            old_terminal.append(old)
            new_terminal.append(improved)
        # Include zero release in this standalone exchange check, even though
        # the existing Model constructor used by the DP requires positive a_i.
        for release in (Q(0), Q(2)):
            assert all(sum(vector) <= capacity + release for _, vector in new[1:])
            suffix_rate = (capacity + release) / (len(initial) - 1)
            for j, (old, improved) in enumerate(zip(old_terminal, new_terminal), start=1):
                suffix = ((Q(1, 4), (suffix_rate,)),)
                assert lower_reflected_terminal(improved, losses[j], suffix) >= lower_reflected_terminal(old, losses[j], suffix)
            counts["explicit_exchange_constructions"] += 1
        summaries.append({"original_first_completion": "1", "new_first_completion": str(tau),
                          "postponed_prefix_work": [str(x) for x in original_debts],
                          "old_other_terminal_states": [str(x) for x in old_terminal],
                          "new_other_terminal_states": [str(x) for x in new_terminal]})
    return summaries


def proportional_checks(counts):
    def step(p, rate, gamma, duration):
        return p + rate * duration if gamma == 0 else p * math.exp(-gamma * duration) - rate / gamma * math.expm1(-gamma * duration)
    max_error = 0.0
    for M, capacity, gamma, fraction in product((0.5, 1.0, 2.0), (1.0, 2.0, 3.0),
                                               (0.0, 0.25, 0.5, 1.0), (0.0, 0.25, 0.75)):
        if capacity <= gamma * M:
            continue
        initial = M * fraction
        for wait in (0.0, 0.5, 2.0):
            passive = initial * math.exp(-gamma * wait)
            duration = ((M - passive) / capacity if gamma == 0 else
                        math.log((capacity - gamma * passive) / (capacity - gamma * M)) / gamma)
            reached = step(passive, capacity, gamma, duration)
            error = abs(reached - M) / max(1.0, M)
            assert error <= TOLERANCE
            max_error = max(max_error, error)
            counts["floating_proportional_partial_stages"] += 1
    for capacity, gamma, initial, f1, f2 in product((1.0, 2.0), (0.0, 0.25, 1.0),
                                                   (0.0, 0.5, 1.0), (0.0, 0.5, 1.0), (0.0, 0.5, 1.0)):
        old = step(step(initial, capacity * f1, gamma, 0.5), capacity * f2, gamma, 0.5)
        start = 1 - (f1 + f2) / 2
        new = step(step(initial, 0, gamma, start), capacity, gamma, 1 - start)
        assert new + TOLERANCE * max(1.0, old, new) >= old
        old_suffix = step(old, capacity / 2, gamma, 0.5)
        new_suffix = step(new, capacity / 2, gamma, 0.5)
        assert new_suffix + TOLERANCE * max(1.0, old_suffix, new_suffix) >= old_suffix
        counts["floating_proportional_postponement_checks"] += 1
    return {"tolerance": TOLERANCE, "maximum_stage_scaled_absolute_error": max_error,
            "scope": "Analytic exponential segment evolution only; no numerical ODE integration or general nonlinear-loss verification."}


def edge_and_validation_checks(counts):
    model = Model(2, (Module(1, 1, 1), Module(1, 1, 1)))
    initial = (Q(1, 2), Q(1, 2))
    assert solve_partial(model, initial).time == 1
    assert Q(1, 2) / (2 - 1) + Q(1, 2) / (3 - 1) == Q(3, 4)  # Incorrect no-waiting-decay shortcut.
    reversal = Model(1, (Module(1, 1, 0), Module(1, 2, 0)))
    assert reversal.optimal_order() == (1, 0)
    partial = solve_partial(reversal, (Q(9, 10), Q(0)))
    assert partial.order == (0, 1) and partial.time == Q(3, 5)
    stalled = Model(1, (Module(1, 1, 1),))
    assert solve_partial(stalled, (Q(1, 2),)).time is None
    assert solve_partial(stalled, (Q(1),)).time == 0
    zero = Model(0, (Module(1, 1, 0),))
    assert solve_partial(zero, (Q(1, 2),)).time is None
    assert solve_partial(zero, (Q(1),)).order == ()
    invalid = (lambda: solve_partial(None, initial), lambda: solve_partial(model, (Q(0),)),
               lambda: solve_partial(model, (Q(-1), Q(0))), lambda: solve_partial(model, (Q(2), Q(0))),
               lambda: solve_partial(model, (0.5, Q(0))), lambda: solve_partial(model, (True, Q(0))))
    for operation in invalid:
        try:
            operation()
        except (TypeError, ValueError):
            counts["invalid_input_rejections"] += 1
        else:
            raise AssertionError("Invalid partial state accepted")
    return {"waiting_decay_matters": {"exact_time": "1", "incorrect_ignored_decay_value": "3/4"},
            "initial_preparation_changes_order": {"cold_optimal_order": [1, 0], "partial_optimal_order": [0, 1], "partial_optimum": "3/5"}}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "build" / "partial-state-verification.json")
    args = parser.parse_args()
    if sys.flags.optimize:
        parser.error("Do not use -O, -OO, or PYTHONOPTIMIZE: assertions must run")
    target = args.output.resolve()
    immutable = (ROOT / "checkpoints").resolve()
    if target == immutable or immutable in target.parents:
        parser.error("Output cannot overwrite an immutable checkpoint")
    counts = {key: 0 for key in ("parameter_models", "partial_state_DP_comparisons", "independent_permutation_evaluations",
                               "ready_cold_oracle_agreements", "smaller_loss_attaining_order_checks", "exact_reflection_formula_checks",
                               "exact_postponement_and_suffix_checks", "explicit_exchange_constructions",
                               "floating_proportional_partial_stages", "floating_proportional_postponement_checks", "invalid_input_rejections")}
    examples = edge_and_validation_checks(counts)
    finite_DP_checks(counts)
    postponement_checks(counts)
    examples["measurable_exchange_piecewise_instances"] = exchange_checks(counts)
    floats = proportional_checks(counts)
    report = {"schema_version": 1, "status": "PASS",
              "scope": "Exact DP/permutation agreement, reflection/postponement and explicit exchange instances, sampled smaller-loss robustness, plus floating proportional identities. Not a measurable-policy exhaustion, continuous-time theorem proof, empirical validation, or novelty audit.",
              "domains": {
                  "two_module_DP": "432 ordered parameter models: M,a in {1,2}, d in {0,1,2}, s in {0,1,2}; all cold/half/full initial states",
                  "three_module_DP": "81 ordered models from (M,a,d)={(1,1,0),(2,1,1),(1,2,2)} and s in {0,1,3}; all cold/half/full states",
                  "larger_DP": "Three deterministic four-module models with all quarter/three-quarter states; two five-module models with four explicit fractional patterns each",
                  "exact_postponement": "Two half-unit control segments; b in {1,2,3}, d in {0,1/2,1,2}, p0 in {0,1/2,1}, each rate in {0,b/2,b}; right-packed work and identical suffix",
                  "exchange": "Two specified rational two/three-module control histories, each checked with released capacity zero and two; all cumulative-control breakpoints checked",
                  "smaller_losses": "Every seventh finite DP case: zero, half-maximum, and stage-dependent alternating loss fractions {0,1/2,1}",
                  "implementation_limit": "DP reuses existing Model/Module validation a_i>0; theorem's a_i=0 extension receives standalone exchange checks only",
                  "float_checks": "Proportional partial stages with M in {1/2,1,2}, b in {1,2,3}, gamma in {0,1/4,1/2,1}; fractional initial states and waits; two-piece postponed controls (grids in verifier)"},
              "exact_arithmetic": "fractions.Fraction", "floating_arithmetic": floats, "counts": counts, "examples": examples}
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: partial-state exact finite checks and floating identities.\n{target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
