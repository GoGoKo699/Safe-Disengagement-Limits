#!/usr/bin/env python3
"""Exact finite certificates for the passes 29--30 common-drain separation.

Fraction-only arithmetic checks the three-module witness, six concentrated
branch deficits, global convexity coefficients, positive-deficit certificates,
and the failed earlier fixture's concentrated competitor. The research notes
supply the continuous-policy reduction, calculus, robust comparison and
existence arguments. This is neither a control search, an independent formal
proof, nor a novelty assessment.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REPORT_NAME = "common-drain-verification.json"


def strings(values):
    return [str(value) for value in values]


def arc(initial, rate, gamma, exp_duration):
    """Endpoint of p'=rate-gamma*p for positive integer gamma."""
    return rate / gamma + (initial - rate / gamma) / exp_duration ** gamma


def bracket_square(square, lower, upper):
    assert 0 < lower < upper
    assert lower ** 2 < square < upper ** 2
    return lower, upper


def certificates():
    s = Q(1)
    gamma = (2, 1, 3)
    sizes = (Q(27, 242), Q(7, 20), Q(11679823, 10222080))
    released = (Q(6075, 2662), Q(1), Q(1))
    full = tuple(g * size for g, size in zip(gamma, sizes))
    a = released[0]
    exp_ell, exp_D, exp_H = Q(2), Q(4), Q(8)
    assert exp_ell ** 2 == exp_D
    assert exp_D * exp_ell == exp_H
    P, V = s - full[0], s - full[1]
    k = 8 * a / 9
    K = (s + released[0] + released[1] - full[2]) * exp_D ** 3 / 9
    assert (P, V, k, K) == (Q(94, 121), Q(13, 20), Q(2700, 1331), Q(243, 40))

    initial = (Q(3, 100), Q(1, 8), Q(0))
    cost = sum((g * x for g, x in zip(gamma, initial)), Q(0))
    threshold = Q(1851, 10000)
    assert cost == Q(37, 200)
    assert threshold - cost == Q(1, 10000)
    assert 0 < initial[0] < sizes[0] and 0 < initial[1] < sizes[1]
    assert initial[2] == 0 and cost < threshold < s
    full_gaps = tuple(d - threshold for d in full)
    assert all(gap > 0 for gap in full_gaps)
    barriers = (full[2] - (s + a), full[2] - (s + released[1]))
    assert barriers == (Q(373, 2560), Q(4865103, 3407360))
    assert full[2] < s + a + released[1]

    X, Y = Q(11, 10), Q(3, 2)
    assert 1 < X < Y < exp_ell < exp_ell * X < exp_ell * Y < exp_D
    assert (s - gamma[0] * initial[0]) / P == X ** 2
    assert (s * X - initial[1]) / V == Y
    at_A = arc(initial[0], s, gamma[0], X)
    B_waiting = initial[1] / X
    at_B = arc(B_waiting, s, gamma[1], Y / X)
    assert (at_A, at_B) == sizes[:2]
    assert initial[0] < at_A < s / gamma[0]
    assert 0 < B_waiting < initial[1] < at_B < s / gamma[1]
    C_at_A_release = arc(Q(0), s, gamma[2], exp_ell * X / Y)
    C_at_B_release = arc(C_at_A_release, s + a, gamma[2], Y / X)
    C_at_D = arc(C_at_B_release, s + a + released[1], gamma[2], exp_D / (exp_ell * Y))
    assert 0 < C_at_A_release < C_at_B_release < C_at_D == sizes[2]
    assert C_at_A_release < s / gamma[2]
    assert C_at_B_release < (s + a) / gamma[2] < sizes[2]
    assert sizes[2] < (s + a + released[1]) / gamma[2]
    terminal_input = (
        s * (exp_D ** 3 - Y ** 3)
        + a * (exp_D ** 3 - (exp_ell * X) ** 3)
        + released[1] * (exp_D ** 3 - (exp_ell * Y) ** 3)
    )
    assert terminal_input == full[2] * exp_D ** 3
    assert Y ** 3 + k * X ** 3 == K

    # Derive each deficit from the discounted C balance. These formulas
    # apply when both handoffs precede ell and the second precedes the
    # first reservation release; the six boxes below certify that branch.
    def deficit_AB(x, y, c_upkeep=Q(0)):
        raw = full[2] * exp_D ** 3 - c_upkeep - (
            s * (exp_D ** 3 - y ** 3)
            + a * (exp_D ** 3 - (exp_ell * x) ** 3)
            + released[1] * (exp_D ** 3 - (exp_ell * y) ** 3)
        )
        assert raw == 9 * (y ** 3 + k * x ** 3 - K) - c_upkeep
        return raw

    def deficit_BA(x, y, c_upkeep=Q(0)):
        raw = full[2] * exp_D ** 3 - c_upkeep - (
            s * (exp_D ** 3 - x ** 3)
            + a * (exp_D ** 3 - (exp_ell * x) ** 3)
            + released[1] * (exp_D ** 3 - (exp_ell * y) ** 3)
        )
        assert raw == (1 + 8 * a) * x ** 3 + 8 * y ** 3 - 9 * K - c_upkeep
        return raw

    assert deficit_AB(X, Y) == 0
    # The written proof reduces all global minima to the relaxed curve
    # Y0=(K-k*X^3)^(1/3), F=1-P*X^2+X-V*Y0. Check the exact
    # coefficients supporting its global second-derivative lower bound.
    Y_bar = Q(51, 32)
    Y_left_cubed = K - k
    assert Y_left_cubed == Q(215433, 53240) > 0
    Y_cube_gap = Y_bar ** 3 - Y_left_cubed
    assert Y_cube_gap == Q(378837, 218071040) > 0
    curvature_lower = -2 * P + 2 * V * k / Y_bar ** 2 + 2 * V * k ** 2 / Y_bar ** 5
    assert curvature_lower == Q(11951206724, 2515363286777) > 0
    derivative_terms = (1 - 2 * P * X, V * k * X ** 2 / Y ** 2)
    assert derivative_terms == (Q(-39, 55), Q(39, 55))
    assert sum(derivative_terms, Q(0)) == 0
    F_at_witness = 1 - P * X ** 2 + X - V * Y
    assert F_at_witness == cost

    # Exact positive-deficit interval: the nominal optimizer adds epsilon
    # to each of the two positive coordinates, leaving effective state x*.
    # The support-sum lower bound belongs to the written argument; these
    # finite coefficient and endpoint checks do not prove its prerequisites.
    epsilon_max = Q(1, 30000)
    exact_nominal_at_endpoint = (initial[0] + epsilon_max, initial[1] + epsilon_max, Q(0))
    assert all(0 <= value < cap for value, cap in zip(exact_nominal_at_endpoint, sizes))
    assert tuple(max(Q(0), value - epsilon_max) for value in exact_nominal_at_endpoint) == initial
    support_sums = (gamma[0] + gamma[1], gamma[0] + gamma[2], gamma[1] + gamma[2], sum(gamma))
    assert min(support_sums) == gamma[0] + gamma[1] == 3
    assert cost + 3 * epsilon_max == threshold
    assert sum((g * value for g, value in zip(gamma, exact_nominal_at_endpoint)), Q(0)) == threshold
    # The positive cubic coefficients certify coordinatewise monotonicity
    # on positive arguments, without sampling any real-valued handoff time.
    assert 9 > 0 and 8 * a > 0 and 1 + 8 * a > 0
    zlo, zhi = bracket_square(1 / P, Q(22691, 20000), Q(227, 200))
    rlo, rhi = bracket_square((1 - threshold) / P, Q(10241, 10000), Q(103, 100))
    blo, bhi = bracket_square((1 / V ** 2 - threshold) / P, Q(167, 100), Q(42, 25))
    square_gaps = (1 / P - zlo ** 2, (1 - threshold) / P - rlo ** 2,
                   (1 / V ** 2 - threshold) / P - blo ** 2)
    assert square_gaps == (Q(570393, 18800000000), Q(875193, 4700000000),
                           Q(3104247, 158860000))
    q = (1 - threshold) / V
    assert q == Q(8149, 6500)
    # Each entry consists of the only positive coordinate, serial order,
    # exact rational lower/upper boxes for (exp(t_A), exp(t_B)), initial
    # C upkeep, and the displayed lower deficit. Strict root inequalities
    # imply these lower deficits underestimate the actual deficits.
    cases = (
        ("A", "ABC", (rlo, rhi), (rlo / V, rhi / V), Q(0),
         Q(2920478879781, 21970000000000)),
        ("A", "BAC", (blo, bhi), (1 / V, 1 / V), Q(0),
         Q(187570811109141, 2924207000000)),
        ("B", "ABC", (zlo, zhi), ((zlo - threshold) / V, (zhi - threshold) / V), Q(0),
         Q(8534290422217221, 233936560000000000)),
        ("B", "BAC", (q * zlo, q * zhi), (q, q), Q(0),
         Q(48262213047342791426186382849, 2924207000000000000000000000)),
        ("C", "ABC", (zlo, zhi), (zlo / V, zhi / V), threshold,
         Q(4599746533873437861, 233936560000000000)),
        ("C", "BAC", (zlo / V, zhi / V), (1 / V, 1 / V), threshold,
         Q(224213187551044101, 2924207000000000)),
    )
    branch_reports = []
    for coordinate, order, xb, yb, c_upkeep, expected in cases:
        assert 1 < xb[0] <= xb[1] < exp_ell
        assert 1 < yb[0] <= yb[1] < exp_ell
        if order == "ABC":
            assert xb[1] < yb[0] and yb[1] < exp_ell * xb[0]
            deficit = deficit_AB(xb[0], yb[0], c_upkeep)
        else:
            assert yb[1] < xb[0] and xb[1] < exp_ell * yb[0]
            deficit = deficit_BA(xb[0], yb[0], c_upkeep)
        assert deficit == expected > 0
        branch_reports.append({
            "positive_coordinate": coordinate, "order": order,
            "exp_tA_bounds": strings(xb), "exp_tB_bounds": strings(yb),
            "initial_C_upkeep": str(c_upkeep), "deficit_strict_lower_bound": str(deficit),
        })

    # A nominal deficit-tolerant witness has two epsilon of extra nominal
    # preparation, leaving one epsilon extra after the worst deficit.
    epsilon = Q(1, 100000)
    nominal = (initial[0] + 2 * epsilon, initial[1] + 2 * epsilon, Q(0))
    effective = tuple(max(Q(0), value - epsilon) for value in nominal)
    assert effective == (initial[0] + epsilon, initial[1] + epsilon, Q(0))
    assert all(0 <= value < cap for value, cap in zip(nominal, sizes))
    nominal_cost = sum((g * value for g, value in zip(gamma, nominal)), Q(0))
    assert nominal_cost == cost + 6 * epsilon == Q(9253, 50000)
    assert threshold - nominal_cost == Q(1, 25000) > 0
    precision_X_squared = (s - gamma[0] * effective[0]) / P
    precision_X_upper = Q(109999, 100000)
    assert 1 < precision_X_squared < precision_X_upper ** 2 < X ** 2
    precision_Y_lower = (1 - effective[1]) / V
    precision_Y_upper = (precision_X_upper - effective[1]) / V
    assert 1 < precision_Y_lower < precision_Y_upper < Y
    # Y>X follows from (1-V)*X>effective_B; Y<2X follows
    # from V>1/2 and positive effective_B. Thus the unchanged branch
    # remains valid, and both releases occur before D.
    assert (1 - V) > effective[1] > 0 and V > Q(1, 2)
    assert exp_ell * precision_Y_upper < exp_D
    precision_deficit_upper = deficit_AB(precision_X_upper, precision_Y_upper)
    assert precision_deficit_upper < 0
    terminal_slack_lower = -precision_deficit_upper / (gamma[2] * exp_D ** 3)
    assert terminal_slack_lower > 0

    # Preserve the failed first calibration: its stationary serial point
    # has a cheaper one-positive competitor. Radical comparisons use only
    # positive square/cube inequalities, not floating-point evaluations.
    old_s, old_a = Q(4), Q(5, 4)
    old_sizes = (Q(95, 108), Q(1), Q(18133, 10368))
    old_P = old_s - gamma[0] * old_sizes[0]
    old_X, old_Y = Q(4, 3), Q(3, 2)
    old_initial = ((old_s - old_P * old_X ** 2) / gamma[0],
                   old_s * old_X - (old_s - old_sizes[1]) * old_Y, Q(0))
    assert old_initial == (Q(2, 243), Q(5, 6), Q(0))
    old_cost = sum((g * value for g, value in zip(gamma, old_initial)), Q(0))
    assert old_cost == Q(413, 486)
    assert (old_s * (64 - old_Y ** 3) + old_a * (64 - 8 * old_X ** 3)
            + (64 - 8 * old_Y ** 3)) == gamma[2] * old_sizes[2] * 64
    r_cubed = Q(3467, 2076)
    r_upper = Q(6, 5)
    assert 1 < r_cubed < r_upper ** 3
    assert 0 < (old_s - old_P * r_upper ** 2) / gamma[0] < old_sizes[0]
    assert (old_s - old_P) / gamma[0] == old_sizes[0]
    # Competitor's exp(t_B)=4*r/3. The two handoffs precede
    # ell; second handoff precedes first release; releases precede D.
    assert 1 < Q(4, 3) < exp_ell and Q(4, 3) * r_upper < exp_ell
    assert exp_ell * Q(4, 3) * r_upper < exp_D
    competitor_terminal_input = (
        old_s * (64 - Q(4, 3) ** 3 * r_cubed)
        + old_a * (64 - 8 * r_cubed)
        + (64 - 8 * Q(4, 3) ** 3 * r_cubed)
    )
    assert competitor_terminal_input == Q(18133, 54) == gamma[2] * old_sizes[2] * 64
    comparison_threshold = (old_s - old_cost) / old_P
    assert comparison_threshold == Q(1531, 1089)
    comparison_gap = r_cubed ** 2 - comparison_threshold ** 3
    assert comparison_gap == Q(6386586797825, 618437517507216) > 0

    return {
        "schema_version": 1, "status": "PASS", "arithmetic": "fractions.Fraction only",
        "scope": "Finite identities, radical bounds and sign certificates for the displayed witnesses, six branches, global convexity bound and positive-deficit endpoint. Research notes supply all-policy reduction, calculus, robust comparison, compactness, exact optimum and separation proofs. No time grid, numerical optimizer, independent formal proof or novelty certification.",
        "fixture": {
            "s": str(s), "gamma": list(gamma), "M": strings(sizes), "released_rates": strings(released),
            "exp_common_drain": str(exp_ell), "exp_handoff_deadline": str(exp_D), "exp_removal_deadline": str(exp_H),
            "initial": strings(initial), "upkeep": str(cost), "comparison_budget": str(threshold),
            "budget_gap": str(threshold - cost), "full_coordinate_budget_gaps": strings(full_gaps),
            "C_barrier_gaps_without_B_without_A": strings(barriers),
        },
        "witness": {
            "exp_handoffs": strings((X, Y, exp_D)), "A_B_handoff_preparations": strings((at_A, at_B)),
            "C_at_A_release_B_release_D": strings((C_at_A_release, C_at_B_release, C_at_D)),
            "discounted_C_input": str(terminal_input), "C_terminal_constraint_K": str(K),
        },
        "concentrated_certificates": {"radical_square_lower_gaps": strings(square_gaps), "branches": branch_reports},
        "exact_optimum_certificates": {
            "Y0_at_left_endpoint_cubed": str(Y_left_cubed), "Y0_global_strict_upper": str(Y_bar),
            "upper_cube_gap": str(Y_cube_gap), "global_F_second_derivative_strict_lower": str(curvature_lower),
            "F_prime_at_witness_terms": strings(derivative_terms), "F_prime_at_witness": "0",
            "F_at_witness": str(F_at_witness),
            "meaning": "Exact arithmetic supporting the written global convexity and equality argument; the verifier does not formalize calculus or the all-policy reduction.",
        },
        "exact_positive_deficit_certificates": {
            "epsilon_interval": "0<=epsilon<=1/30000", "nominal_optimizer_expression": "(3/100+epsilon,1/8+epsilon,0)",
            "optimal_upkeep_expression": "37/200+3*epsilon", "epsilon_endpoint": str(epsilon_max),
            "nominal_state_at_endpoint": strings(exact_nominal_at_endpoint), "endpoint_upkeep": str(threshold),
            "coefficient_sums_for_supports_AB_AC_BC_ABC": list(support_sums), "minimum_support_sum": min(support_sums),
            "meaning": "Endpoint and coefficient certificates for the written exact positive-deficit theorem; larger epsilon is uncharacterized, not certified infeasible.",
        },
        "positive_deficit": {
            "epsilon": str(epsilon), "nominal_state": strings(nominal), "worst_effective_state": strings(effective),
            "nominal_upkeep": str(nominal_cost), "gap_below_comparison_budget": str(threshold - nominal_cost),
            "exp_tA_squared": str(precision_X_squared), "exp_tA_strict_upper": str(precision_X_upper),
            "exp_tB_strict_upper": str(precision_Y_upper), "C_virtual_terminal_slack_strict_lower": str(terminal_slack_lower),
            "meaning": "The strict-deadline-slack nominal witness has extra preparation beyond the exact nominal optimizer. It supports the written local perturbation argument; no maximum tolerable deficit or neighborhood radius is certified.",
        },
        "failed_first_calibration": {
            "two_partial_initial": strings(old_initial), "two_partial_upkeep": str(old_cost),
            "concentrated_exp_tA_cubed": str(r_cubed), "concentrated_upkeep_expression": "4-(121/54)*(3467/2076)^(2/3)",
            "discounted_C_input": str(competitor_terminal_input), "strict_cost_comparison_square_cube_gap": str(comparison_gap),
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "build" / REPORT_NAME)
    args = parser.parse_args()
    if sys.flags.optimize:
        parser.error("Do not use -O, -OO, or PYTHONOPTIMIZE: assertions must run")
    target = args.output.resolve()
    immutable = (ROOT / "checkpoints").resolve()
    if target == immutable or immutable in target.parents:
        parser.error("Output cannot overwrite an immutable checkpoint")
    old_reports = (ROOT / "results").resolve()
    if (target == old_reports or old_reports in target.parents) and target != old_reports / REPORT_NAME:
        parser.error("Output cannot overwrite another tracked report")
    result = certificates()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: exact three-module common-drain separation certificates.\n{target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
