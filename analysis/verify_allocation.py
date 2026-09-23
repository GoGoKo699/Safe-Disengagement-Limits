#!/usr/bin/env python3
"""Exact supporting certificates for the pass-20/21 allocation comparison.

These small Fraction-only checks validate displayed identities, cap/deadline
membership, sign factors and objective gaps. They do not inspect literature,
prove the universal concentration theorem, or certify arbitrary solvers.
The written notes supply the geometric and all-step exchange arguments.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from itertools import permutations
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def rational_strings(values):
    return [str(value) for value in values]


def invert_stages(capacity, gamma, sizes, exp_times):
    """Recover q using rational exp(t) and positive integer gamma only."""
    assert len(capacity) == len(gamma) == len(sizes) == len(exp_times)
    previous, preparation = Q(1), []
    for b, g, size, current in zip(capacity, gamma, sizes, exp_times):
        assert isinstance(g, int) and g > 0
        denominator = b - g * size
        assert denominator > 0 and current >= previous >= 1
        preparation.append((b * previous ** g - denominator * current ** g) / g)
        previous = current
    return tuple(preparation)


def raw_time_certificate():
    capacity, gamma, sizes = (Q(2), Q(2)), (1, 1), (Q(1), Q(1))
    exp_A, exp_B = (Q(3, 2), Q(5, 2)), (Q(2), Q(7, 2))
    q_A = invert_stages(capacity, gamma, sizes, exp_A)
    q_B = invert_stages(capacity, gamma, sizes, exp_B)
    assert q_A == (Q(1, 2), Q(1, 2))
    assert q_B == (Q(0), Q(1, 2))
    assert all(0 <= value <= Q(1, 2) for value in q_A + q_B)
    assert max(exp_A[-1], exp_B[-1]) == Q(7, 2)
    # At the arithmetic time midpoint, exp(t_1)=sqrt(3) and
    # exp(t_2)=sqrt(35)/2. Both sides of the alleged lower-bound
    # inequality sqrt(35)/2 >= 2*sqrt(3)-1/2 are positive.
    assert exp_A[0] * exp_B[0] == 3
    assert exp_A[1] * exp_B[1] == Q(35, 4)
    constant_gap = 4 * Q(3) + Q(1, 4) - Q(35, 4)
    assert constant_gap == Q(7, 2) > 0
    # Squared right minus squared left is 7/2 - 2*sqrt(3)>0,
    # because two positive terms satisfy (7/2)^2 > 2^2*3.
    final_squared_gap = constant_gap ** 2 - 4 * Q(3)
    assert final_squared_gap == Q(1, 4) > 0
    return {"exp_time_endpoints": [rational_strings(exp_A), rational_strings(exp_B)],
            "preparations": [rational_strings(q_A), rational_strings(q_B)],
            "exp_H": "7/2", "midpoint_squared_gap": "7/2-2*sqrt(3)",
            "positive_sign_certificate": str(final_squared_gap),
            "scope": "Exact midpoint exclusion in raw completion times. The same common-rate instance is linear after an exponential clock change."}


def convex_clock_certificates():
    exp_times = (Q(25, 16), Q(549, 320), Q(533, 256))
    gamma, sizes = (2, 1, 1), (Q(3), Q(2), Q(2))
    caps = (Q(29, 10), Q(19, 10), Q(19, 10))
    preparation = invert_stages((Q(10),) * 3, gamma, sizes, exp_times)
    assert preparation == (Q(15, 128), Q(19, 10), Q(1, 2))
    assert 0 < preparation[0] < caps[0]
    assert preparation[1] == caps[1]
    assert 0 < preparation[2] < caps[2]
    z = tuple(value ** 2 for value in exp_times)
    assert z[1] == ((10 * exp_times[0] - caps[1]) / 8) ** 2
    assert z[2] == Q(533, 256) ** 2
    # L_2''(z)=positive_factor*z^(-3/2); derive the factor from
    # A=b/D, B=gamma*U/D, r=gamma/lambda rather than a floating Hessian.
    A, B, r = Q(10, 8), caps[1] / 8, Q(1, 2)
    convex_factor = A * B * (1-r)
    assert convex_factor == Q(19, 128) > 0
    # The terminal face objective is 10*sqrt(z1)-4*z1+2*sqrt(z2).
    face_hessian_factors = (10 * r * (r-1), 2 * r * (r-1))
    assert face_hessian_factors == (Q(-5, 2), Q(-1, 2))
    assert all(factor < 0 for factor in face_hessian_factors)

    mixed_times = (Q(6, 5), Q(59, 48), Q(1451, 1152))
    mixed_caps = (Q(4), Q(3, 4), Q(3, 4))
    mixed_q = invert_stages((Q(25),) * 3, (2, 1, 1),
                            (Q(9, 2), Q(1), Q(1)), mixed_times)
    assert mixed_q == (Q(49, 50), Q(1, 2), Q(1, 2))
    assert all(0 < q < cap for q, cap in zip(mixed_q, mixed_caps))
    # lambda=4: f11=z1^(-7/4)*[-75/16+4*z1^(1/4)],
    # f22=-(3/16)*z2^(-7/4). Rational exp(t1) supplies the root.
    r1, r2 = Q(1, 2), Q(1, 4)
    first_factor = 25 * r2 * (r2-1) - 16 * r1 * (r1-1) * mixed_times[0]
    second_factor = r2 * (r2-1)
    assert first_factor == Q(9, 80) > 0
    assert second_factor == Q(-3, 16) < 0
    return {"curved_extreme_point_fixture": {
                "lambda": "2", "exp_times": rational_strings(exp_times),
                "z": rational_strings(z), "preparation": rational_strings(preparation),
                "caps": rational_strings(caps), "active_middle_lower_bound": True,
                "active_terminal_deadline": True, "middle_convexity_factor": str(convex_factor),
                "face_hessian_factors": rational_strings(face_hessian_factors),
                "scope": "Cap membership and positive curvature support the written extremality proof. This point is not an optimum; no general extreme-point or concentration claim is mechanically proved."},
            "indefinite_hessian_fixture": {
                "lambda": "4", "exp_times": rational_strings(mixed_times),
                "preparation": rational_strings(mixed_q), "caps": rational_strings(mixed_caps),
                "hessian_factors": rational_strings((first_factor, second_factor)),
                "scope": "Opposite exact signs at a strictly cap-interior fixed-horizon point in the specified clock; other transformations are not excluded."}}


def augmented_feasible(point, cap=Q(9, 10)):
    x, y, slack = point
    if not (0 <= x <= cap and 0 <= y <= cap and slack >= 0 and sum(point) == 2):
        return False
    assert 3-2*x > 0 and y+4 > 0
    return (y+4) ** 2 >= 9 * (3-2*x)


def exchange_certificate():
    P, origin = (Q(13, 25), Q(1, 5), Q(32, 25)), (Q(3, 8), Q(1, 2), Q(9, 8))
    assert augmented_feasible(P) and augmented_feasible(origin)
    for x, y, _ in (P, origin):
        assert (y+4) ** 2 == 9 * (3-2*x)
    gradient = (Q(2), Q(1), Q(0))
    linear_gap = sum((g*(p-q) for g, p, q in zip(gradient, P, origin)), Q(0))
    assert linear_gap == Q(-1, 100)
    b = (Q(157, 80), Q(19, 20), Q(-9, 80))
    assert tuple(q/10 + beta for q, beta in zip(origin, b)) == gradient

    def objective(point):
        return sum((value ** 2 / 20 + beta * value for value, beta in zip(point, b)), Q(0))

    quadratic_gap = objective(P)-objective(origin)
    assert quadratic_gap == Q(-1299, 400000) < 0
    labels, directions, delta = ("x", "y", "slack"), [], Q(1, 100)
    excluded = {(0, 1): (Q(9), Q(-1), Q(3, 8)),
                (0, 2): (Q(18), Q(0), Q(3, 8)),
                (1, 2): (Q(9), Q(-1), Q(1, 2))}
    x, y, _ = origin
    for source, target in permutations(range(3), 2):
        direction = tuple(Q(int(i == target)-int(i == source)) for i in range(3))
        derivative = gradient[target]-gradient[source]
        # The deadline violation polynomial along this straight exchange is
        # 9*(3-2*x(delta))-(y(delta)+4)^2 = c1*delta+c2*delta^2.
        c1 = -18 * direction[0] - 2 * (y+4) * direction[1]
        c2 = -direction[1] ** 2
        sample = tuple(q + delta*d for q, d in zip(origin, direction))
        if (source, target) in excluded:
            expected_c1, expected_c2, upper = excluded[source, target]
            assert (c1, c2) == (expected_c1, expected_c2)
            assert c1 > 0 and c2 <= 0 and c1+c2*upper > 0
            assert not augmented_feasible(sample) and derivative < 0
            scope = "Polynomial sign certificate on the displayed full box-allowed interval; the note explains the all-step implication."
            record = {"direction": f"{labels[source]} to {labels[target]}",
                      "exchangeable": False, "positive_step_upper_bound": str(upper),
                      "violation_polynomial_coefficients": rational_strings((Q(0), c1, c2)),
                      "positive_factor_lower_bound": str(c1+c2*upper), "scope": scope}
        else:
            assert augmented_feasible(sample) and derivative > 0
            record = {"direction": f"{labels[source]} to {labels[target]}",
                      "exchangeable": True, "feasible_witness_step": str(delta),
                      "witness": rational_strings(sample)}
        record["objective_directional_derivative"] = str(derivative)
        directions.append(record)
    return {"P": rational_strings(P), "Q": rational_strings(origin),
            "cap": "9/10", "gradient_at_Q": rational_strings(gradient),
            "linear_cost_gap_P_minus_Q": str(linear_gap),
            "quadratic_cost_gap_P_minus_Q": str(quadratic_gap), "directions": directions,
            "scope": "Direct fixed-order preparation-plus-slack formulation only. Feasible equal-amount exchanges meet derivative tests at Q, yet P has lower linear and shared-quadratic cost. No statement about every encoding or the union over orders."}


def independent_price_certificate():
    epsilon, source_budget = Q(1, 100), Q(2)
    gamma, sizes, releases, prices = (1, 2), (Q(1), Q(1)), (Q(2), Q(0)), (Q(6), Q(1))
    strict_orders = []
    for order in permutations(range(2)):
        capacity = source_budget
        for i in order:
            if capacity <= gamma[i] * sizes[i]:
                break
            capacity += releases[i]
        else:
            strict_orders.append(order)
    assert strict_orders == [(0, 1)]
    q = invert_stages((Q(2), Q(4)), gamma, sizes, (Q(3, 2), Q(2)))
    assert q == (Q(1, 2), Q(1, 2))
    cap = Q(1)-epsilon
    nominal = tuple(value+epsilon for value in q)
    assert all(0 < value < cap for value in q)
    assert nominal == (Q(51, 100), Q(51, 100))
    assert all(epsilon < p < 1 for p in nominal)
    assert 2 * (2-q[0]) ** 2 - q[1] == 4  # exp(2H)=4
    price = sum((w*p for w, p in zip(prices, nominal)), Q(0))
    physical_upkeep = sum((g*p for g, p in zip(gamma, nominal)), Q(0))
    assert price == Q(357, 100)
    assert physical_upkeep == Q(153, 100) < source_budget
    assert source_budget-physical_upkeep == Q(47, 100)

    # Full two-positive-coordinate lower bound, in ascending powers of q1:
    # 6*q1 + 2*(2-q1)^2 - 4 + 7*epsilon.
    lower_polynomial = (Q(4) + sum(prices)*epsilon, Q(6)-Q(8), Q(2))
    completed_square = (price + Q(2)*Q(1, 2)**2, -Q(4)*Q(1, 2), Q(2))
    assert lower_polynomial == completed_square
    assert completed_square[2] > 0
    # q1=0 needs q2>=4, outside the cap. q2=0 needs
    # q1>=2-sqrt(2), with a strictly higher nominal price.
    assert 2*(2-Q(0))**2-4 == 4 > cap
    sqrt_upper = Q(283, 200)
    assert sqrt_upper > 0 and sqrt_upper**2-Q(2) == Q(89, 40000) > 0
    root_branch_price_constant = prices[0]*(Q(2)+epsilon)
    assert root_branch_price_constant == Q(603, 50)
    assert root_branch_price_constant-prices[0]*sqrt_upper == price
    # The one-positive-coordinate branch exists: 0<2-sqrt(2)<99/100.
    assert Q(2)**2 > 2
    assert (Q(2)-cap)**2 < 2 and Q(2)-cap > 0
    normalized_prices = tuple(w/g for w, g in zip(prices, gamma))
    B, d_min = source_budget+sum(releases), min(g*M for g, M in zip(gamma, sizes))
    sufficient_ratio_bound = B/(B-d_min)
    normalized_ratio = max(normalized_prices)/min(normalized_prices)
    assert sufficient_ratio_bound == Q(4, 3)
    assert normalized_ratio == 12 > sufficient_ratio_bound
    return {"s": "2", "gamma": list(gamma), "M": rational_strings(sizes),
            "a": rational_strings(releases), "prices": rational_strings(prices),
            "epsilon": str(epsilon), "caps": [str(cap), str(cap)], "exp_H": "2",
            "strict_orders_zero_based": [list(order) for order in strict_orders],
            "worst_corner": rational_strings(q), "nominal": rational_strings(nominal),
            "nominal_price": str(price), "physical_upkeep": str(physical_upkeep),
            "optional_rate": str(source_budget-physical_upkeep),
            "two_positive_support_lower_polynomial": rational_strings(lower_polynomial),
            "completed_square": "357/100+2*(q1-1/2)^2",
            "one_positive_support_price": "603/50-6*sqrt(2)",
            "sqrt2_strict_upper_bound": str(sqrt_upper),
            "root_bound_squared_gap": "89/40000",
            "normalized_price_ratio": str(normalized_ratio),
            "sufficient_preserving_ratio_bound": str(sufficient_ratio_bound),
            "scope": "Exact recurrence and arithmetic behind the written support-exhaustion proof of a unique two-partial nominal optimum. The checker does not replace the all-policy seriality theorem or verify the general sufficient price-region proposition."}


def verify():
    return {"schema_version": 1, "status": "PASS", "arithmetic": "fractions.Fraction only",
            "scope": "Exact supporting arithmetic for displayed allocation comparison fixtures. Written proofs supply the universal geometry, concentration and source-hypothesis conclusions; no literature-wide novelty or general optimization certificate.",
            "raw_time_midpoint": raw_time_certificate(),
            "convex_clock": convex_clock_certificates(),
            "equal_amount_exchange": exchange_certificate(),
            "independent_price_counterexample": independent_price_certificate()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "build" / "allocation-verification.json")
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
    print(f"PASS: exact allocation geometry and exchange certificates.\n{target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
