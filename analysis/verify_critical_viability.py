#!/usr/bin/env python3
"""Exact supporting identities for the three-module critical-viability example.

The rational checks verify the displayed phase identities, global-cost case
inequalities and a sufficient interval certificate. The written proofs supply
the all-policy and all-time conclusions. Floating frontier/schedule checks are
separately labeled numerical consistency checks, not certified optimization.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from itertools import product
import json
import math
from pathlib import Path
import sys

from unequal_proportional import (ProportionalModel as Model, ProportionalModule as Module,
                                  frontier, recount_schedule)

ROOT = Path(__file__).resolve().parents[1]
TOLERANCE = 2e-9


def verify():
    counts = {key: 0 for key in ("exact_global_cost_case_groups", "exact_target_obstruction_states",
                               "exact_phase_identity_groups", "exact_interval_certificates",
                               "exact_rational_path_samples", "floating_path_schedule_checks",
                               "floating_frontier_checks")}
    model = Model(1, (Module(Q(1, 2), 2, 1), Module(1, 33, 2), Module(3, 1, Q(1, 2))))
    target = (Q(1, 2), Q(1, 4), Q(0))
    H = math.log(5 / 2) / 2 + 2 * math.log(24 / 23)
    multiplier_2H = Q(5, 2) * Q(24, 23) ** 4
    assert multiplier_2H < 3
    assert 6 * 23 ** 4 - 5 * 24 ** 4 == 20166 > 0
    assert sum((m.gamma * p for m, p in zip(model.modules, target)), Q(0)) == 1
    # At the target A transfers immediately. B then C give exp(2H) exactly.
    b_B, D_B, b_C, D_C = Q(3), Q(1), Q(36), Q(69, 2)
    assert (b_B - 2 * target[1]) / D_B == Q(5, 2)
    assert b_C / D_C == Q(24, 23)
    counts["exact_global_cost_case_groups"] += 1
    # For cost<=one, B/C cannot be initially full. If no module is full,
    # only A is accessible initially; only one coordinate can be partial in
    # a minimizing state by the separately proved concentration theorem.
    assert model.modules[1].gamma * model.modules[1].M == 2 > 1
    assert model.modules[2].gamma * model.modules[2].M == Q(3, 2) > 1
    assert model.modules[0].gamma * model.modules[0].M < model.s
    assert all(m.gamma * m.M >= model.s for m in model.modules[1:])
    # A cold already takes log2 > H; if only A is partial, either cold B's
    # first stage takes .5log3 > H, or cold C's first stage takes 2log2 > H.
    assert multiplier_2H < 3 < 4
    assert 2 ** 4 > 3
    counts["exact_global_cost_case_groups"] += 1
    # With A full and C partial, cost<=one implies q_C<=one. Starting C
    # then takes at least 2log(5/3), which exceeds H; starting cold B fails too.
    assert Q(1, 2) + Q(1, 2) * Q(1) == 1
    assert (Q(3) - Q(1, 2) * Q(1)) / (Q(3) - Q(3, 2)) == Q(5, 3)
    assert Q(5, 3) ** 4 > 3 > multiplier_2H
    counts["exact_global_cost_case_groups"] += 1
    # With A full and B partial, C cannot go first. Deadline equality in
    # B-then-C requires q_B=1/4, and any lower q violates the deadline.
    for q in (Q(0), Q(1, 8), Q(1, 4)):
        multiplier = (3 - 2 * q) * Q(24, 23) ** 4
        assert (multiplier <= multiplier_2H) == (q >= Q(1, 4))
        assert (Q(1, 2) + 2 * q <= 1) == (q <= Q(1, 4))
    assert (3 - Q(5, 2)) / 2 == Q(1, 4)
    counts["exact_global_cost_case_groups"] += 1
    # Fixed target obstruction: z=p_A+p_B-3/4 obeys z'<=-2z under
    # normal budget 1. Upper reflection and arbitrary underuse are included.
    for pA, pB in product((Q(k, 8) for k in range(5)), (Q(0), Q(1, 4), Q(1, 2), Q(1))):
        z = pA + pB - Q(3, 4)
        for vA_units in range(5):
            for vB_units in range(5 - vA_units):
                vA, vB = Q(vA_units, 4), Q(vB_units, 4)
                derivative_A, derivative_B = vA - pA, vB - 2 * pB
                if pA == Q(1, 2):
                    derivative_A = min(derivative_A, Q(0))
                if pB == 1:
                    derivative_B = min(derivative_B, Q(0))
                assert derivative_A + derivative_B <= 1 - pA - 2 * pB
                assert 1 - pA - 2 * pB == -2 * z + pA - Q(1, 2) <= -2 * z
                counts["exact_target_obstruction_states"] += 1
    # Phase one v_C=one from cold for 2log2 yields p_C=2(1-1/2)=one.
    assert Q(1) / Q(1, 2) * (1 - Q(1, 2)) == 1 < model.modules[2].M
    # Phase two lasts 14log2 before guaranteed deployment: x=exp(-t/2)=1/128.
    x0 = Q(1, 128)
    assert 2 ** 7 == 128 and 2 + 14 == 16
    assert Q(1, 2) + Q(1, 2) == 1
    counts["exact_phase_identity_groups"] += 1
    # Sufficient certificate for every real 0<x<=1/128: coefficients are
    # nonnegative, so 108x+63x^3 is bounded by its rational endpoint value.
    endpoint_coefficient = 108 * x0 + 63 * x0 ** 3
    assert endpoint_coefficient < 1
    assert 1 - x0 - x0 ** 3 > 0
    assert Q(5, 2) > 1  # Fourth-root derivative on [5/2,infinity) is <1/4.
    counts["exact_interval_certificates"] += 1
    samples = sorted({Q(j, 128 * 16) for j in range(1, 17)} | {Q(1, 129), Q(1, 4096)})
    maximum_deadline_excess = -math.inf
    maximum_formula_error = 0.0
    for x in samples:
        assert 0 < x <= x0
        pA, pB, pC = (1 - x ** 2) / 2, (1 - x ** 4) / 4, x
        state = (pA, pB, pC)
        assert all(0 < p < m.M for p, m in zip(state, model.modules))
        upkeep = pA + 2 * pB + pC / 2
        total = pA + pB + pC
        assert upkeep == 1 + (x - x ** 2 - x ** 4) / 2 > 1
        assert total == Q(3, 4) + x - x ** 2 / 2 - x ** 4 / 4 > Q(3, 4)
        derivatives = (x ** 2 / 2, x ** 4 / 2, -x / 2)
        assert derivatives == (Q(1, 2) - pA, Q(1, 2) - 2 * pB, -pC / 2)
        assert sum(derivatives) == 1 - upkeep < 0
        # Exact serial exponential identities before the final fourth root.
        exp_tA = (1 - pA) / Q(1, 2)
        assert exp_tA == 1 + x ** 2
        Y = 3 * exp_tA ** 2 - 2 * pB
        assert Y == Q(5, 2) + 6 * x ** 2 + Q(7, 2) * x ** 4
        assert 72 * (Y - Q(5, 2)) / 4 == 108 * x ** 2 + 63 * x ** 4
        assert 108 * x + 63 * x ** 3 <= endpoint_coefficient < 1
        assert 108 * x ** 2 + 63 * x ** 4 < x
        counts["exact_rational_path_samples"] += 1
        # Float replay is supplemental; the interval certificate above, with
        # the analytic fourth-root concavity argument, carries uniform timing.
        replay, ready, order = recount_schedule(model, tuple(float(p) for p in state), (0, 1, 2))
        formula = 2 * math.log((72 * float(Y) ** 0.25 - float(x)) / 69)
        assert ready == () and order == (0, 1, 2)
        assert abs(replay - formula) <= TOLERANCE
        assert replay < H
        maximum_formula_error = max(maximum_formula_error, abs(replay - formula))
        maximum_deadline_excess = max(maximum_deadline_excess, replay - H)
        counts["floating_path_schedule_checks"] += 1
    # The integrated excess upkeep after guaranteed deployment is finite:
    # Q(x0)-lim Q = x0-x0^2/2-x0^4/4, consistent with Q'=one-upkeep.
    reserve = x0 - x0 ** 2 / 2 - x0 ** 4 / 4
    assert reserve > 0
    assert target[0] + target[1] + target[2] == Q(3, 4)
    counts["exact_phase_identity_groups"] += 1
    result = frontier(model, H)
    assert abs(result.upkeep - 1) <= TOLERANCE
    assert all(abs(p - float(q)) <= TOLERANCE for p, q in zip(result.preparation, target))
    counts["floating_frontier_checks"] += 1
    return {
        "schema_version": 1, "status": "PASS",
        "scope": "Rational support checks for the displayed three-module example and its all-time interval certificate, plus separately labeled floating consistency checks. Not an exhaustion of normal policies, proof of global optimality, or certified floating deadline decision.",
        "parameters": {"s": "1", "modules": [{"M": "1/2", "gamma": "1", "a": "2"},
                                                  {"M": "1", "gamma": "2", "a": "33"},
                                                  {"M": "3", "gamma": "1/2", "a": "1"}],
                       "H": "log(5/2)/2+2*log(24/23)", "unique_minimum_cost_target": ["1/2", "1/4", "0"],
                       "exact_minimum_upkeep": "1"},
        "exact_arithmetic": "fractions.Fraction; integer/rational transformed-time comparisons",
        "counts": counts,
        "domains": {"target_obstruction": "p_A=0,1/8,...,1/2; p_B in {0,1/4,1/2,1}; quarter-capacity allocation simplex",
                    "path_samples": "x=j/2048 for j=1..16, plus 1/129 and 1/4096",
                    "uniform_interval_certificate": "0<x<=1/128; endpoint 108/128+63/128^3<1 with nonnegative polynomial coefficients",
                    "global_cost_cases": "Four exact case groups supporting the written concentration-based exhaustion"},
        "warmup": {"phase1": {"allocation": ["0", "0", "1"], "duration": "2*log(2)", "end_state": ["0", "0", "1"]},
                   "phase2": {"allocation": ["1/2", "1/2", "0"], "duration_before_guarantee": "14*log(2)",
                              "continued_allocation_after_guarantee": True},
                   "total_finite_warmup": "16*log(2)", "guarantee_starts_after_warmup": True},
        "uniform_path": {"x": "exp(-t/2), where t is elapsed phase-two time",
                         "state": ["(1-x^2)/2", "(1-x^4)/4", "x"],
                         "upkeep": "1+(x-x^2-x^4)/2 > 1 for 0<x<=1/128",
                         "total_preparation": "3/4+x-x^2/2-x^4/4, decreasing to 3/4 after warmup",
                         "finite_excess_upkeep_integral": str(reserve),
                         "interval_endpoint_coefficient": str(endpoint_coefficient)},
        "floating_checks": {"tolerance": TOLERANCE, "frontier_upkeep": result.upkeep,
                            "maximum_schedule_formula_error": maximum_formula_error,
                            "maximum_recounted_deadline_excess": maximum_deadline_excess,
                            "certified": False},
        "interpretation": "The minimum-cost target is unreachable from cold, but a finite warmup reaches a trajectory that stays ready forever and approaches that target. The written proof supplies the universal policy/time claims; no readiness guarantee is assumed during warmup."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "build" / "critical-viability-verification.json")
    args = parser.parse_args()
    if sys.flags.optimize:
        parser.error("Do not use -O, -OO, or PYTHONOPTIMIZE: assertions must run")
    target = args.output.resolve()
    immutable = (ROOT / "checkpoints").resolve()
    if target == immutable or immutable in target.parents:
        parser.error("Output cannot overwrite an immutable checkpoint")
    result = verify()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: exact critical-viability fixture checks and floating identities.\n{target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
