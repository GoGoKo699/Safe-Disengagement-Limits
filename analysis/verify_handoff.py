#!/usr/bin/env python3
"""Exact finite checks for handoff-interface counterexamples.

Reconstruct prescribed rational event schedules and sample local lower-bound
inequalities. This does not optimize over arbitrary real-time policies or prove
the continuous-policy lower bounds. See the accompanying research notes.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import product
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class DrainModule:
    M: Q
    a: Q
    d: Q
    ell: Q


def prescribed_schedule(modules, spare, initial, segments, initial_handoffs, counts):
    """Check one explicit schedule, splitting at every capacity-release event.

    A segment is (duration, constant allocations, endpoint handoffs). State
    updates use the maximal allowed fixed losses and exact reflected dynamics.
    All drains must have ended by the prescribed schedule's final time.
    """
    state, t, drains, released = list(initial), Q(0), {}, set()
    def handoff(indices):
        for i in indices:
            assert i not in drains and state[i] == modules[i].M
            drains[i] = t + modules[i].ell
    handoff(initial_handoffs)
    events = []
    for duration, allocation, finish in segments:
        assert duration > 0 and len(allocation) == len(modules)
        released.update(i for i, end in drains.items() if end <= t)
        capacity = spare + sum((modules[i].a for i in released), Q(0))
        assert all(v >= 0 for v in allocation) and sum(allocation) <= capacity
        assert not any(t < end < t + duration for end in drains.values())
        for i, (module, v) in enumerate(zip(modules, allocation)):
            if i in drains:
                assert v == 0
                continue
            state[i] = min(module.M, max(Q(0), state[i] + (v - module.d) * duration))
        t += duration
        handoff(finish)
        events.append({"time": str(t), "capacity_during_segment": str(capacity),
                       "preparation": [str(p) for p in state], "handoffs": list(finish)})
        counts["prescribed_schedule_segments"] += 1
    assert len(drains) == len(modules) and all(end <= t for end in drains.values())
    counts["prescribed_schedules"] += 1
    return t, events


def latency_checks(counts):
    two = (DrainModule(Q(1), Q(2), Q(1), Q(1)),) * 2
    overlap = ((Q(1), (Q(2), Q(0)), (0,)),
               (Q(1), (Q(0), Q(2)), (1,)),
               (Q(1), (Q(0), Q(0)), ()))
    sequential = ((Q(1), (Q(2), Q(0)), (0,)),
                  (Q(1), (Q(0), Q(0)), ()),
                  (Q(1, 3), (Q(0), Q(4)), (1,)),
                  (Q(1), (Q(0), Q(0)), ()))
    time2, events2 = prescribed_schedule(two, Q(2), (Q(0), Q(0)), overlap, (), counts)
    serial2, serial_events2 = prescribed_schedule(two, Q(2), (Q(0), Q(0)), sequential, (), counts)
    assert time2 == 3 and serial2 == Q(10, 3) and time2 < serial2
    three = (DrainModule(Q(1), Q(2), Q(0), Q(1)),
             DrainModule(Q(1), Q(6), Q(2), Q(1)),
             DrainModule(Q(5), Q(1), Q(0), Q(1)))
    preempt = ((Q(1), (Q(0), Q(0), Q(1)), ()),
               (Q(1), (Q(0), Q(3), Q(0)), (1,)),
               (Q(1), (Q(0), Q(0), Q(3)), ()),
               (Q(1, 9), (Q(0), Q(0), Q(9)), (2,)),
               (Q(1), (Q(0), Q(0), Q(0)), ()))
    BC = ((Q(1), (Q(0), Q(0), Q(0)), ()),
          (Q(1), (Q(0), Q(3), Q(0)), (1,)),
          (Q(1), (Q(0), Q(0), Q(3)), ()),
          (Q(2, 9), (Q(0), Q(0), Q(9)), (2,)),
          (Q(1), (Q(0), Q(0), Q(0)), ()))
    CB = ((Q(1), (Q(0), Q(0), Q(1)), ()),
          (Q(4, 3), (Q(0), Q(0), Q(3)), (2,)),
          (Q(1), (Q(0), Q(3), Q(0)), (1,)),
          (Q(1), (Q(0), Q(0), Q(0)), ()))
    actual3, events3 = prescribed_schedule(three, Q(1), (Q(1), Q(0), Q(0)), preempt, (0,), counts)
    bc_time, bc_events = prescribed_schedule(three, Q(1), (Q(1), Q(0), Q(0)), BC, (0,), counts)
    cb_time, cb_events = prescribed_schedule(three, Q(1), (Q(1), Q(0), Q(0)), CB, (0,), counts)
    assert actual3 == Q(37, 9) and bc_time == Q(38, 9) and cb_time == Q(13, 3)
    assert actual3 < min(bc_time, cb_time)
    # Two-module no-release aggregate potential: at least one unfinished job,
    # rate budget two and fixed loss one force aggregate derivative <=one.
    for unfinished in (1, 2):
        for state in product((Q(0), Q(1, 2), Q(1)), repeat=unfinished):
            for units in product(range(5), repeat=unfinished):
                if sum(units) > 4:
                    continue
                derivative = Q(0)
                for p, u in zip(state, units):
                    growth = Q(u, 2) - 1
                    if p == 0:
                        growth = max(growth, Q(0))
                    if p == 1:
                        growth = min(growth, Q(0))
                    derivative += growth
                assert derivative <= 1
                counts["two_module_potential_states"] += 1
    # Before either B/C handoff, v_B<=three. This exact local inequality
    # integrates from cold to work_B>=three*p_B, including resets to zero.
    for p, v in product((Q(0), Q(1, 4), Q(1, 2), Q(3, 4), Q(1)),
                         (Q(k, 4) for k in range(13))):
        growth = v - 2
        if p == 0:
            growth = max(growth, Q(0))
        if p == 1:
            growth = min(growth, Q(0))
        assert growth <= v / 3
        counts["three_module_work_loss_states"] += 1
    # Sample each analytic lower-bound interval, including all transition points.
    for k in range(13):
        t = Q(2) + Q(k, 36)  # [2,7/3]
        remaining = 10 - 3 * t
        finish_C = t + 1 + (remaining - 3) / 9
        lower = finish_C + 1
        assert remaining >= 3
        assert lower == Q(25, 9) + 2 * t / 3 >= Q(37, 9)
        counts["three_module_lower_bound_samples"] += 1
        t = Q(7, 3) + Q(k, 12)  # [7/3,10/3]
        remaining = 10 - 3 * t
        assert 0 <= remaining <= 3
        assert t + remaining / 3 + 1 == Q(13, 3)
        # If C is first, B has at most t-7/3 preparation and cannot finish
        # before 10/3 while its net growth is at most one.
        prepared_B = t - Q(7, 3)
        assert 0 <= prepared_B <= 1
        assert t + (1 - prepared_B) == Q(10, 3) <= t + 1
        counts["three_module_lower_bound_samples"] += 2
        t = Q(10, 3) + Q(k, 4)
        assert t + 1 >= Q(13, 3) > Q(37, 9)
        counts["three_module_lower_bound_samples"] += 1
    # Simultaneous B/C readiness needs >=three+five allocated units.
    assert (Q(3) + Q(5) + Q(2)) / 3 == Q(10, 3)
    return {
        "two_modules": {"overlap_time": str(time2), "module_by_module_time": str(serial2),
                        "overlap_events": events2, "module_by_module_events": serial_events2},
        "three_modules": {"preemptive_time": str(actual3), "B_then_C_time": str(bc_time), "C_then_B_time": str(cb_time),
                          "preemptive_events": events3, "B_then_C_events": bc_events, "C_then_B_events": cb_events},
    }


def reset_exit_bound(M, s, delta, prepared, age):
    """Least uniform bound; the second branch can be an unattained supremum."""
    L, residual = M / s, (M - prepared) / s
    earliest = max(Q(0), delta - age)
    return residual if residual <= earliest else residual + L


def reset_checks(counts):
    # Instant reset events are a separate update model. The verified initial
    # reset is at time zero; subsequent spacings are at least delta > M/s.
    for M, s, separation_factor, fraction in product((Q(1), Q(2)), (Q(1), Q(2)),
                                                     (Q(3, 2), Q(2), Q(3)),
                                                     (Q(0), Q(1, 4), Q(1, 2), Q(3, 4))):
        L = M / s
        delta, h = separation_factor * L, fraction * L
        H, K = L + h, M - s * h
        assert reset_exit_bound(M, s, delta, Q(0), Q(0)) == L
        assert reset_exit_bound(M, s, delta, Q(0), delta) == 2 * L
        ages = {j * (delta + L) / 12 for j in range(13)} | {delta - L, delta - h, delta}
        for prepared, age in product((M * j / 8 for j in range(9)), sorted(ages)):
            bound = reset_exit_bound(M, s, delta, prepared, age)
            threshold = max(Q(0), M - s * max(delta - age, h))
            assert (bound <= H) == (prepared >= threshold)
            assert bound <= 2 * L
            counts["reset_readiness_equivalence_states"] += 1
            residual, earliest = (M - prepared) / s, max(Q(0), delta - age)
            if residual > earliest:
                # An update approaching the uninterrupted completion time from
                # below gives a strict sequence converging to residual+L.
                gaps = []
                for k in (2, 4, 8):
                    update = earliest + (residual - earliest) * (1 - Q(1, k))
                    assert earliest <= update < residual
                    completion = update + L
                    assert completion < bound and update + delta > completion
                    gaps.append(bound - completion)
                    counts["reset_supremum_witnesses"] += 1
                assert gaps[0] > gaps[1] > gaps[2] > 0
        for age in sorted(ages):
            prepared = s * min(max(age - (delta - L), Q(0)), L - h)
            assert 0 <= prepared <= M
            assert reset_exit_bound(M, s, delta, prepared, age) <= H
            counts["reset_attaining_policy_states"] += 1
        # Pre-update readiness at every sampled admissible update age and the
        # reset state after the event are both required, not just one side.
        for age in (delta, Q(3, 2) * delta, 2 * delta, 3 * delta):
            assert reset_exit_bound(M, s, delta, K, age) <= H
            assert reset_exit_bound(M, s, delta, Q(0), Q(0)) == L <= H
            counts["reset_event_boundary_pairs"] += 1
        # An update at the exact completion time does not precede cutover.
        for residual in (Q(0), L / 2, L):
            assert reset_exit_bound(M, s, delta, M - s * residual, delta - residual) == residual
            counts["reset_completion_priority_equalities"] += 1
        def copied_by(time, starts):
            return s * sum((max(Q(0), min(time, start + delta - h) - (start + delta - L))
                            for start in starts if start + delta - L < time), Q(0))
        # Distinct deterministic admissible update calendars; explicitly account
        # for each full-rate copying window and finite unfinished final cycles.
        for multipliers in ((Q(1), Q(1), Q(1)),
                            (Q(3, 2), Q(1), Q(2)),
                            (Q(2), Q(3), Q(1))):
            starts = [Q(0)]
            for multiplier in multipliers:
                starts.append(starts[-1] + multiplier * delta)
            probes = set(starts)
            for start in starts:
                probes.update((start + delta - L, start + delta - (L + h) / 2, start + delta - h))
            for time in sorted(probes):
                copied = copied_by(time, starts)
                assert 0 <= copied <= s * time
                assert copied <= K * (int(time // delta) + 1)
                counts["reset_finite_prefix_accounting"] += 1
        for periods in (1, 2, 4):
            time = periods * delta
            copied = copied_by(time, [j * delta for j in range(periods + 1)])
            assert copied == periods * K
            assert (s * time - copied) / time == s - K / delta
            counts["reset_periodic_cost_identities"] += 1
        # Shorter than L is infeasible immediately after a reset. At 2L every
        # state is ready without copying; the upper endpoint has cost zero.
        assert reset_exit_bound(M, s, delta, Q(0), Q(0)) > L / 2
        for age in sorted(ages):
            assert reset_exit_bound(M, s, delta, Q(0), age) <= 2 * L
    # One compact numerical illustration in exact units.
    M, s, delta, H = Q(1), Q(1), Q(2), Q(3, 2)
    L, h = M / s, H - M / s
    K = M - s * h
    assert K == Q(1, 2) and K / delta == Q(1, 4)
    comparisons = []
    for spacing, deadline, expected_reset, expected_fluid in (
            (Q(3), Q(7, 4), Q(1, 12), Q(0)),
            (Q(3, 2), Q(2), Q(0), Q(2, 3))):
        reset_cost = max(Q(0), 2 - deadline) / spacing
        mean_loss = 1 / spacing
        fluid_cold_time = 1 / (1 - mean_loss)
        fluid_cost = Q(0) if deadline >= fluid_cold_time else mean_loss
        assert (reset_cost, fluid_cost) == (expected_reset, expected_fluid)
        counts["mean_rate_substitution_counterexamples"] += 1
        comparisons.append({"M": "1", "s": "1", "delta": str(spacing), "H": str(deadline),
                            "reset_cost": str(reset_cost), "fluid_cost_at_mean_rate": str(fluid_cost)})
    return {"parameters": {"M": str(M), "s": str(s), "delta": str(delta), "H": str(H)},
            "copying_age_window": [str(delta - L), str(delta - h)],
            "work_per_update_cycle": str(K), "worst_case_long_run_upkeep": str(K / delta),
            "guaranteed_optional_rate": str(s - K / delta),
            "mean_rate_substitution_counterexamples": comparisons,
            "convention": "Cutover completion wins a simultaneous update; r+L denotes a least uniform bound, possibly not attained by any one update time.",
            "scope": "Reset-update uncertainty with a verified reset at deployment start; distinct from continuous fluid invalidation."}


def freeze_exit_bound(M, s, delta, prepared, age, freeze_budget):
    """Single irreversible final freeze, admissible once residual<=freeze_budget."""
    L, residual = M / s, (M - prepared) / s
    earliest = max(Q(0), delta - age)
    pre_freeze = max(residual - freeze_budget, Q(0))
    return residual if pre_freeze <= earliest else residual + L - freeze_budget


def freeze_checks(counts):
    for M, s, separation_factor in product((Q(1), Q(2)), (Q(1), Q(2)), (Q(3, 2), Q(2), Q(3))):
        L = M / s
        delta = separation_factor * L
        base_ages = {j * (delta + L) / 8 for j in range(9)} | {delta - L, delta}
        for prepared, age in product((M * j / 4 for j in range(5)), sorted(base_ages)):
            residual = (M - prepared) / s
            assert freeze_exit_bound(M, s, delta, prepared, age, Q(0)) == reset_exit_bound(M, s, delta, prepared, age)
            counts["freeze_zero_budget_agreements"] += 1
            assert freeze_exit_bound(M, s, delta, prepared, age, L) == residual
            counts["freeze_full_budget_identities"] += 1
            previous = None
            for B in (Q(0), L / 4, L / 2, 3 * L / 4, L):
                bound = freeze_exit_bound(M, s, delta, prepared, age, B)
                assert previous is None or bound <= previous
                previous = bound
                counts["freeze_monotonicity_states"] += 1
        # Fix H while varying B for an independent recurring-cost monotonicity check.
        for H in (L, 5 * L / 4, 3 * L / 2, 7 * L / 4, 2 * L):
            costs = [max(Q(0), 2 * M - s * H - s * B) / delta
                     for B in (Q(0), L / 4, L / 2, 3 * L / 4, L)]
            assert all(x >= y >= 0 for x, y in zip(costs, costs[1:]))
            assert costs[-1] == 0
            counts["freeze_cost_monotonicity_deadlines"] += 1
        for B, H_fraction in product((Q(0), L / 2, L), (Q(0), Q(1, 2), Q(1))):
            H = L + H_fraction * (L - B)
            h, K = H - L + B, 2 * M - s * H - s * B
            begin, end = delta + B - L, delta + L - H
            assert 0 < begin <= end <= delta and K == s * (end - begin)
            assert 0 <= K / s <= end <= delta and end - K / s == begin
            ages = base_ages | {begin, end}
            for prepared, age in product((M * j / 4 for j in range(5)), sorted(ages)):
                bound = freeze_exit_bound(M, s, delta, prepared, age, B)
                threshold = max(Q(0), M - s * max(delta - age + B, h))
                assert (bound <= H) == (prepared >= threshold)
                assert (prepared >= threshold) == (prepared + s * max(end - age, Q(0)) >= K)
                assert bound <= 2 * L - B
                counts["freeze_readiness_states"] += 1
                counts["freeze_sporadic_deadline_equivalences"] += 1
                residual, earliest = (M - prepared) / s, max(Q(0), delta - age)
                pre_freeze = max(residual - B, Q(0))
                assert 0 <= residual - pre_freeze <= B
                if pre_freeze > earliest:
                    gaps = []
                    for k in (2, 4, 8):
                        update = earliest + (pre_freeze - earliest) * (1 - Q(1, k))
                        assert earliest <= update < pre_freeze
                        completion = update + L
                        assert update + delta > completion
                        assert completion < bound
                        # After reset, copy L-B before the final freeze and B
                        # during it. This always respects the per-freeze budget.
                        final_freeze = update + L - B
                        assert final_freeze >= update and completion - final_freeze == B
                        gaps.append(bound - completion)
                        counts["freeze_supremum_witnesses"] += 1
                    assert gaps[0] > gaps[1] > gaps[2] > 0
            for age in sorted(ages):
                prepared = s * min(max(age - begin, Q(0)), end - begin)
                assert 0 <= prepared <= M
                assert prepared == max(Q(0), M - s * max(delta - age + B, h))
                assert freeze_exit_bound(M, s, delta, prepared, age, B) <= H
                if K > 0:
                    assert (freeze_exit_bound(M, s, delta, Q(0), age, B) <= H) == (age <= begin)
                counts["freeze_policy_states"] += 1
            for age in (delta, Q(3, 2) * delta, 2 * delta):
                assert freeze_exit_bound(M, s, delta, K, age, B) <= H
                assert freeze_exit_bound(M, s, delta, Q(0), Q(0), B) == L <= H
                counts["freeze_event_boundary_pairs"] += 1
            # The final freeze precedes an update at its exact starting instant.
            for residual in (Q(0), L / 2, L):
                pre_freeze = max(residual - B, Q(0))
                age = delta - pre_freeze
                assert freeze_exit_bound(M, s, delta, M - s * residual, age, B) == residual
                counts["freeze_priority_equalities"] += 1
            def copied_by(time, starts):
                return s * sum((max(Q(0), min(time, start + end) - (start + begin))
                                for start in starts if start + begin < time), Q(0))
            for multipliers in ((Q(1), Q(1), Q(1)),
                                (Q(3, 2), Q(1), Q(2)),
                                (Q(2), Q(3), Q(1))):
                starts = [Q(0)]
                for multiplier in multipliers:
                    starts.append(starts[-1] + multiplier * delta)
                probes = set(starts)
                for start in starts:
                    probes.update((start + begin, start + (begin + end) / 2, start + end))
                for time in sorted(probes):
                    copied = copied_by(time, starts)
                    assert 0 <= copied <= s * time
                    assert copied <= K * (int(time // delta) + 1)
                    counts["freeze_finite_prefix_accounting"] += 1
            for periods in (1, 2, 4):
                time = periods * delta
                copied = copied_by(time, [j * delta for j in range(periods + 1)])
                assert copied == periods * K
                assert (s * time - copied) / time == s - K / delta
                counts["freeze_periodic_cost_identities"] += 1
            assert freeze_exit_bound(M, s, delta, Q(0), Q(0), B) > L / 2
            if B == L:
                assert K == 0 and begin == end == delta
    M, s, delta, H, B = Q(1), Q(1), Q(2), Q(3, 2), Q(1, 4)
    K = 2 * M - s * H - s * B
    assert K / delta == Q(1, 8)
    return {"parameters": {"M": str(M), "s": str(s), "delta": str(delta), "H": str(H), "B": str(B)},
            "copying_age_window": [str(delta + B - M / s), str(delta + M / s - H)],
            "work_per_update_cycle": str(K), "worst_case_long_run_upkeep": str(K / delta),
            "guaranteed_optional_rate": str(s - K / delta),
            "scope": "One irreversible final source-mutation freeze; its remaining serialization time is at most B. Independent queuing, service delay allowance, and protocol slack are assumptions, not physical validation.",
            "convention": "Final freeze wins a simultaneous update; the interrupted exit formula is a least uniform bound, possibly an unattained supremum."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "build" / "handoff-verification.json")
    args = parser.parse_args()
    if sys.flags.optimize:
        parser.error("Do not use -O, -OO, or PYTHONOPTIMIZE: assertions must run")
    target = args.output.resolve()
    immutable = (ROOT / "checkpoints").resolve()
    if target == immutable or immutable in target.parents:
        parser.error("Output cannot overwrite an immutable checkpoint")
    counts = {key: 0 for key in ("prescribed_schedules", "prescribed_schedule_segments", "two_module_potential_states",
                               "three_module_work_loss_states", "three_module_lower_bound_samples",
                               "reset_readiness_equivalence_states", "reset_supremum_witnesses",
                               "reset_attaining_policy_states", "reset_event_boundary_pairs",
                               "reset_completion_priority_equalities", "reset_finite_prefix_accounting",
                               "reset_periodic_cost_identities", "mean_rate_substitution_counterexamples",
                               "freeze_zero_budget_agreements", "freeze_full_budget_identities",
                               "freeze_monotonicity_states", "freeze_cost_monotonicity_deadlines",
                               "freeze_readiness_states", "freeze_supremum_witnesses", "freeze_policy_states",
                               "freeze_sporadic_deadline_equivalences",
                               "freeze_event_boundary_pairs", "freeze_priority_equalities",
                               "freeze_finite_prefix_accounting", "freeze_periodic_cost_identities")}
    examples = latency_checks(counts)
    examples["finite_reset_updates"] = reset_checks(counts)
    examples["bounded_final_freeze"] = freeze_checks(counts)
    report = {"schema_version": 1, "status": "PASS", "arithmetic": "fractions.Fraction (exact)",
              "scope": "Prescribed rational drain schedules, finite lower-bound samples, reset-update readiness/cost identities, and bounded-final-freeze identities; not optimization over arbitrary continuous-time policies, a theorem proof, operational validation, or novelty evidence.",
              "domain": {"schedules": "Five explicitly listed two/three-module schedules, split at every handoff and capacity-release event",
                         "two_module_potential": "One/two unfinished modules; states in {0,1/2,1}; allocations in {0,1/2,1,3/2,2} with total<=2",
                         "three_module_work_loss": "B preparation in {0,1/4,1/2,3/4,1}; rate v_B=0,1/4,...,3",
                         "three_module_lower_bounds": "13 rational samples on each of the three piecewise time intervals; middle interval checked for both first-completion cases",
                         "reset_updates": "M,s in {1,2}; L=M/s; delta/L in {3/2,2,3}; (H-L)/L in {0,1/4,1/2,3/4}; eighth-size preparations, rational age grid plus exact boundary ages; three deterministic update calendars and periodic cycles",
                         "bounded_freeze": "M,s in {1,2}; delta/L in {3/2,2,3}; B/L in {0,1/2,1}; H=L+fraction*(L-B), fraction in {0,1/2,1}; quarter-size preparations and rational ages with exact ramp boundaries; monotonicity on B/L={0,1/4,1/2,3/4,1}; three update calendars"},
              "counts": counts, "examples": examples}
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: exact handoff finite checks.\n{target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
