#!/usr/bin/env python3
"""Small checks for a proportional-loss instance of the exit potential.

Algebraic inequalities use exact Fraction arithmetic. Logarithmic integrals and
their ODE inverse identities use floats with an explicit tolerance. No claim of
continuous-time policy exhaustion, numerical proof, or publication novelty.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from itertools import product
import json
import math
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
TOLERANCE = 2e-12


def integral_potential(b: Q, gamma: Q, p: Q) -> float:
    if p == 0:
        return 0.0
    if b <= gamma * p:
        return math.inf
    if gamma == 0:
        return float(p / b)
    return -math.log1p(-float(gamma * p / b)) / float(gamma)


def concentrated_exit(n: int, M: Q, a: Q, gamma: Q, s: Q, total: Q) -> float:
    """Best exit at this total preparation; arbitrary states can be slower."""
    if total == n * M:
        return 0.0
    k, r = int(total // M), total % M
    b, d = s + k * a, gamma * M
    first = math.log1p(float(gamma * (M - r) / (b - d))) / float(gamma)
    return first + sum(integral_potential(s + j * a, gamma, M) for j in range(k + 1, n))


def inverse_upkeep(n: int, M: Q, a: Q, gamma: Q, s: Q, H: float) -> float:
    times = [concentrated_exit(n, M, a, gamma, s, k * M) for k in range(n + 1)]
    if H >= times[0]:
        return 0.0
    for k in range(n):
        if times[k + 1] <= H <= times[k]:
            b, d = s + k * a, gamma * M
            return float((k + 1) * d) - float(b - d) * math.expm1(float(gamma) * (H - times[k + 1]))
    raise AssertionError("Deadline not covered by the inverse frontier")


def homogeneous_frontier_checks(counts: dict) -> dict:
    max_error = 0.0
    for n, M, a, d, extra in product(range(1, 5), (Q(1), Q(2)), (Q(1), Q(2)),
                                    (Q(1, 2), Q(1)), (Q(1, 2), Q(1))):
        gamma, s = d / M, d + extra
        for k in range(n):
            b = s + k * a
            tail = sum(integral_potential(s + j * a, gamma, M) for j in range(k + 1, n))
            # The current-stage integral vanishes at r=M, agreeing with the
            # adjacent piece exactly as an analytic expression; check its float evaluation.
            endpoint = math.log(float((b - d) / (b - d))) / float(gamma) + tail
            adjacent = concentrated_exit(n, M, a, gamma, s, (k + 1) * M)
            assert abs(endpoint - adjacent) <= TOLERANCE * max(1.0, abs(adjacent))
            counts["frontier_boundary_continuities"] += 1
            for j in range(5):
                r, total = M * j / 4, k * M + M * j / 4
                H = concentrated_exit(n, M, a, gamma, s, total)
                independent_integral = (integral_potential(b, gamma, M)
                                        - integral_potential(b, gamma, r) + tail)
                assert abs(H - independent_integral) <= TOLERANCE * max(1.0, abs(H))
                cost = inverse_upkeep(n, M, a, gamma, s, H)
                expected = float(gamma * total)
                error = abs(cost - expected) / max(1.0, abs(expected))
                assert error <= TOLERANCE
                max_error = max(max_error, error)
                counts["proportional_frontier_identity_points"] += 1
                # Budget feasibility is gamma*Q<=s; initialized concentrated
                # states are attained at that exact maintenance allocation.
                prepared = (M,) * k + ((r,) if k < n else ()) + (Q(0),) * (n - k - 1)
                assert sum(prepared) == total
                assert sum(gamma * p for p in prepared) == gamma * total
        assert inverse_upkeep(n, M, a, gamma, s,
                              concentrated_exit(n, M, a, gamma, s, Q(0)) + 1) == 0
        if n == 1:
            cold = concentrated_exit(n, M, a, gamma, s, Q(0))
            for j in range(6):
                H = cold * j / 4
                archived = max(0.0, float(s) - float(s - d) * math.exp(float(gamma) * H))
                actual = inverse_upkeep(n, M, a, gamma, s, H)
                assert abs(actual - archived) <= TOLERANCE * max(1.0, abs(archived))
                counts["single_module_archived_identity_points"] += 1
    # Local Z=M*J+sum(p_i) bound with arbitrary preparation arrangements.
    # Reflection at full/zero states and underused allocations are included.
    for n, M, a, gamma in product(range(1, 4), (Q(1), Q(2)), (Q(1), Q(2)), (Q(1, 2), Q(1))):
        d, s = gamma * M, gamma * M + Q(1, 2)
        for J in range(n):
            b, remaining = s + J * a, n - J
            for state in product((Q(0), M / 2, M), repeat=remaining):
                Z = M * J + sum(state)
                if Z == n * M:
                    continue
                F = s + (a + d) * int(Z // M) - gamma * Z
                assert F > 0
                for allocation_units in product(range(5), repeat=remaining):
                    if sum(allocation_units) > 4:
                        continue
                    allocation = tuple(b * k / 4 for k in allocation_units)
                    growth = Q(0)
                    for p, v in zip(state, allocation):
                        derivative = v - gamma * p
                        if p == 0:
                            derivative = max(derivative, Q(0))
                        if p == M:
                            derivative = min(derivative, Q(0))
                        growth += derivative
                    assert growth <= sum(allocation) - gamma * sum(state)
                    assert growth <= b - gamma * sum(state) <= F
                    counts["aggregate_envelope_checks"] += 1
            for j in range(4):
                r = M * j / 4
                Z = M * J + r
                F = s + (a + d) * int(Z // M) - gamma * Z
                assert b - gamma * r == F
                counts["concentrated_envelope_equalities"] += 1
    archived_example = inverse_upkeep(1, Q(1), Q(1), Q(1, 2), Q(1), math.log(2))
    assert abs(archived_example - (1 - 1 / math.sqrt(2))) <= TOLERANCE
    return {"assumptions": "Homogeneous M,a,d>0; gamma=d/M and s>d; paid initialization.",
            "interpretation": "T(Q) is a lower bound for every preparation state of total Q, attained by a concentrated state; arbitrary states with equal Q need not have equal exit times.",
            "floating_domain": "n=1..4; M,a in {1,2}; d in {1/2,1}; s=d+extra with extra in {1/2,1}; quarter-module initial amounts.",
            "exact_aggregate_domain": "n=1..3; M,a in {1,2}; gamma in {1/2,1}; s=gamma*M+1/2; every transfer count, cold/half/full remaining states, quarter-capacity allocation simplex.",
            "maximum_inverse_scaled_absolute_error": max_error,
            "single_module_archived_example_upkeep": archived_example}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "build" / "state-dependent-verification.json")
    args = parser.parse_args()
    if sys.flags.optimize:
        parser.error("Do not use -O, -OO, or PYTHONOPTIMIZE: assertions must run")
    target = args.output.resolve()
    immutable = (ROOT / "checkpoints").resolve()
    if target == immutable or immutable in target.parents:
        parser.error("Output cannot overwrite an immutable checkpoint")
    counts = {key: 0 for key in ("exact_reflected_derivative_checks", "exact_capacity_coefficient_checks",
                               "finite_proportional_stages", "blocked_stage_checks", "floating_jump_checks",
                               "non_Lipschitz_counterexample_points", "frontier_boundary_continuities",
                               "proportional_frontier_identity_points", "single_module_archived_identity_points",
                               "aggregate_envelope_checks", "concentrated_envelope_equalities")}
    max_inverse_relative_error = 0.0
    for b, gamma, M in product((Q(0), Q(1, 2), Q(1), Q(2), Q(3)),
                               (Q(0), Q(1, 4), Q(1, 2), Q(1), Q(2)),
                               (Q(1, 2), Q(1), Q(2))):
        stage = integral_potential(b, gamma, M)
        # A target can be unreachable at this capacity while its smaller partial
        # states still have finite potential. Include these accessible states.
        for k, j in product(range(5), repeat=2):
            p, v = M * k / 4, b * j / 4
            loss = gamma * p
            if b <= loss:
                continue
            growth = v - loss
            if p == 0:
                growth = max(growth, Q(0))
            if p == M:
                growth = min(growth, Q(0))
            assert growth / (b - loss) <= v / b
            counts["exact_reflected_derivative_checks"] += 1
        for a, k in product((Q(1, 2), Q(1), Q(2)), range(5)):
            p = M * k / 4
            if b > gamma * p:
                assert 1 / (b + a - gamma * p) <= 1 / (b - gamma * p)
                counts["exact_capacity_coefficient_checks"] += 1
        if b <= gamma * M:
            assert math.isinf(stage)
            counts["blocked_stage_checks"] += 1
            continue
        assert math.isfinite(stage)
        reached = float(b) * stage if gamma == 0 else -float(b / gamma) * math.expm1(-float(gamma) * stage)
        error = abs(reached - float(M)) / max(1.0, float(M))
        assert error <= TOLERANCE
        assert float(M / b) - TOLERANCE <= stage <= float(M / (b - gamma * M)) + TOLERANCE
        max_inverse_relative_error = max(max_inverse_relative_error, error)
        counts["finite_proportional_stages"] += 1
        for a, k in product((Q(1, 2), Q(1), Q(2)), range(5)):
            p = M * k / 4
            # One completed module and one retained module with the same gamma/M;
            # the inequality itself only requires nonnegative retained preparation.
            before = stage + integral_potential(b, gamma, p)
            after = integral_potential(b + a, gamma, p)
            scale = max(1.0, before, after, stage)
            assert before - after + TOLERANCE * scale >= stage
            counts["floating_jump_checks"] += 1
    # Outside the Lipschitz class: g(q)=1-sqrt(1-q), b=M=1.
    # For rational t in [0,2], the square root along this trajectory is rational,
    # so verify the identity exactly without floating square-root evaluation.
    for k in range(17):
        t = Q(k, 8)
        p, derivative = t - t * t / 4, 1 - t / 2
        assert 0 <= p <= 1 and derivative >= 0
        assert 1 - p == derivative * derivative
        counts["non_Lipschitz_counterexample_points"] += 1
    assert p == 1 and derivative == 0  # Reaches the endpoint in finite time 2.
    frontier_report = homogeneous_frontier_checks(counts)
    report = {
        "schema_version": 1, "status": "PASS",
        "scope": "Finite checks for g(p)=gamma*p: exact local algebra/coefficient monotonicity, aggregate exit envelope, floating logarithmic stage/jump and homogeneous frontier/inverse identities; exact points on an excluded non-Lipschitz counterexample. Not a continuous-time proof, general-loss theorem verification, empirical validation, or novelty audit.",
        "domain": "b in {0,1/2,1,2,3}; gamma in {0,1/4,1/2,1,2}; M in {1/2,1,2}; quarter-size state and quarter-capacity allocation grids; released a in {1/2,1,2}.",
        "exact_arithmetic": "fractions.Fraction: reflected (v-gamma*p)/(b-gamma*p)<=v/b and capacity coefficient decrease",
        "floating_arithmetic": {"formula": "c=-log(1-gamma*M/b)/gamma; c=M/b when gamma=0; infinity when b<=gamma*M",
                                "inverse": "p(c)=-(b/gamma)*expm1(-gamma*c), with p(c)=b*c when gamma=0",
                                "scaled_absolute_tolerance": TOLERANCE,
                                "maximum_inverse_scaled_absolute_error": max_inverse_relative_error},
        "counts": counts,
        "homogeneous_readiness_frontier": frontier_report,
        "excluded_counterexample": {"loss": "g(q)=1-sqrt(1-q), not Lipschitz at q=1",
                                     "capacity_and_target": "b=M=1",
                                     "trajectory": "p(t)=t-t^2/4, 0<=t<=2",
                                     "conclusion": "Finite-time arrival at p=1 despite b=g(1); the strict eligibility rule needs the stated regularity assumption."},
    }
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: exact algebra and floating analytic-identity checks.\n{target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
