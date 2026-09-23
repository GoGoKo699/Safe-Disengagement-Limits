#!/usr/bin/env python3
"""Exact supporting certificates for the pass-25 proportional-drain example.

Fraction-only identities check the displayed witness, discounted lower-bound
coefficients, scalar obstructions, cold warmup and precision endpoints. The
written proof covers all continuous policies and loss histories. These checks
are not a numerical control search, an independent proof of that theorem, or
a literature/novelty assessment.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def strings(values):
    return [str(value) for value in values]


def certificates():
    s = Q(4)
    gamma, sizes = (Q(2), Q(1)), (Q(1, 2), Q(3))
    full_loss = tuple(g * size for g, size in zip(gamma, sizes))
    exp_H = Q(10)
    exp_handoff = (Q(11, 10), Q(3))
    exp_drain = (Q(100, 11), Q(10, 3))
    assert full_loss == (Q(1), Q(3))
    assert Q(1) < exp_handoff[0] < exp_handoff[1]
    assert exp_handoff[1] < min(exp_drain) < max(exp_drain)
    assert exp_handoff[1] < exp_drain[1]  # Equivalent to 9 < 10.
    assert Q(3) ** 2 < exp_H
    assert tuple(t * drain for t, drain in zip(exp_handoff, exp_drain)) == (exp_H, exp_H)

    x, y = exp_handoff
    # Recover each initial coordinate from its actual active interval.
    p_A = (s - (s - full_loss[0]) * x ** 2) / gamma[0]
    p_B = s * x - (s - full_loss[1]) * y
    p = (p_A, p_B)
    assert p == (Q(37, 200), Q(7, 5))
    assert all(0 < value < size for value, size in zip(p, sizes))
    cost = sum((g * value for g, value in zip(gamma, p)), Q(0))
    assert cost == Q(177, 100) < s

    # Closed-form maximum-loss paths at their switching and terminal times.
    equilibrium = tuple(s / g for g in gamma)
    at_A_handoff = equilibrium[0] + (p_A - equilibrium[0]) / x ** 2
    B_waiting = p_B / x
    exp_B_active = y / x
    at_B_handoff = equilibrium[1] + (B_waiting - equilibrium[1]) / exp_B_active
    assert at_A_handoff == sizes[0]
    assert B_waiting == Q(14, 11)
    assert exp_B_active == Q(30, 11)
    assert at_B_handoff == sizes[1]
    # These strict endpoint/equilibrium relations certify the monotone active
    # arcs of z'=s-gamma*z. B's zero-input waiting arc strictly decreases.
    assert p_A < at_A_handoff < equilibrium[0]
    assert 0 < B_waiting < p_B < sizes[1]
    assert B_waiting < at_B_handoff < equilibrium[1]
    assert full_loss[0] < s and full_loss[1] < s

    # Discounted balances with zero reflection under the witness.
    A_weighted_input = s * (x ** 2 - 1)
    B_weighted_input = s * (y - x)
    assert gamma[0] * p_A == full_loss[0] * x ** 2 - A_weighted_input
    assert gamma[1] * p_B == full_loss[1] * y - B_weighted_input
    # Ascending coefficients of W(X,Y)=4+4X-3X^2-Y, with
    # X=exp(t_A), Y=exp(t_B). Derive them from the budget and full losses.
    W = (s, s, full_loss[0] - s, full_loss[1] - s)
    assert W == (Q(4), Q(4), Q(-3), Q(-1))
    lower_endpoint = W[0] + W[1] * x + W[2] * x ** 2 + W[3] * y
    assert lower_endpoint == cost
    # dW/dt_A = X*(4-6X) = -2X*(3X-2). On X>=1,
    # 3X-2>=1. This coefficient check supports the written all-time sign
    # proof rather than sampling a time grid.
    derivative_A = (W[1], 2 * W[2])
    assert derivative_A == (Q(4), Q(-6))
    derivative_factor_at_min_X = 3 * Q(1) - 2
    assert derivative_factor_at_min_X == 1 > 0
    assert W[3] < 0  # dW/dt_B = -Y < 0.
    # Before A is handed off, its discounted input weight exceeds B's:
    # 2X^2-X=X*(2X-1), with 2X-1>=1 for X>=1.
    weighted_advantage_coefficients = (Q(-1), Q(2))
    assert weighted_advantage_coefficients[0] + weighted_advantage_coefficients[1] == 1 > 0

    B_first_lower = s - (s - full_loss[1]) * x
    assert B_first_lower == Q(29, 10)
    assert B_first_lower - cost == Q(113, 100) > 0

    # Independent scalar deadline bounds force both effective initial
    # coordinates to be positive, including in the precision contract.
    scalar_A_lower = (s - (s - full_loss[0]) * x ** 2) / gamma[0]
    scalar_B_lower = (s - (s - full_loss[1]) * y) / gamma[1]
    assert scalar_A_lower == Q(37, 200) > 0
    assert scalar_B_lower == 1 > 0

    # Normal cold warmup has no handoffs: allocate (1,3) for log(2),
    # then maintain the target with gamma_i*p_i.
    warm_input, exp_warm = (Q(1), Q(3)), Q(2)
    warm = tuple(v / g * (1 - Q(1) / exp_warm ** int(g))
                 for v, g in zip(warm_input, gamma))
    assert sum(warm_input) == s
    assert warm == (Q(3, 8), Q(3, 2))
    assert all(target < value < cap for target, value, cap in zip(p, warm, sizes))
    assert tuple(value - target for value, target in zip(warm, p)) == (Q(19, 100), Q(1, 10))
    upkeep_input = tuple(g * target for g, target in zip(gamma, p))
    assert upkeep_input == (Q(37, 100), Q(7, 5))
    assert sum(upkeep_input) == cost
    optional = s - cost
    assert optional == Q(223, 100) > 0

    precision_cap = min(cap - target for cap, target in zip(sizes, p))
    assert precision_cap == Q(63, 200)
    assert sizes[0] - scalar_A_lower == precision_cap
    assert sizes[1] - p_B == Q(8, 5) > precision_cap
    precision_slope = sum(gamma)
    assert precision_slope == 3
    nominal_at_cap = tuple(value + precision_cap for value in p)
    assert nominal_at_cap == (Q(1, 2), Q(343, 200))
    assert nominal_at_cap[0] == sizes[0] and nominal_at_cap[1] < sizes[1]
    precision_cost_at_cap = sum((g * value for g, value in zip(gamma, nominal_at_cap)), Q(0))
    assert precision_cost_at_cap == cost + precision_slope * precision_cap == Q(543, 200)
    assert s - precision_cost_at_cap == Q(257, 200) > 0

    return {
        "schema_version": 1,
        "status": "PASS",
        "arithmetic": "fractions.Fraction only",
        "scope": "Exact identities and polynomial sign factors for the displayed two-module counterexample. The research note supplies the all-policy integration, robust comparison, uniqueness and precision proofs; no continuous-policy numerical search, independent formal proof or novelty certification.",
        "fixture": {
            "s": str(s), "gamma": strings(gamma), "M": strings(sizes),
            "released_rates": "arbitrary positive; none releases before either handoff deadline",
            "exp_H": str(exp_H), "exp_handoff_deadlines": strings(exp_handoff),
            "exp_drain_durations": strings(exp_drain),
            "no_early_release_sign_certificate": "9<10",
            "preparation": strings(p), "upkeep": str(cost), "both_strictly_partial": True,
        },
        "witness": {
            "B_preparation_at_A_handoff": str(B_waiting),
            "exp_B_active_duration": str(exp_B_active),
            "handoff_preparations": strings((at_A_handoff, at_B_handoff)),
            "full_rate_equilibria": strings(equilibrium),
            "discounted_weighted_inputs": strings((A_weighted_input, B_weighted_input)),
            "exp_drain_completion_times": strings(tuple(t * drain for t, drain in zip(exp_handoff, exp_drain))),
        },
        "lower_bound": {
            "W_coefficients_constant_X_Xsquared_Y": strings(W),
            "W_at_deadlines": str(lower_endpoint),
            "dW_dtA": "-2*X*(3*X-2), X=exp(t_A)>=1",
            "dW_dtA_positive_factor_lower_bound": str(derivative_factor_at_min_X),
            "dW_dtB": "-Y, Y=exp(t_B)>=1",
            "before_A_weight_advantage": "X*(2*X-1)>0 for X>=1",
            "B_first_upkeep_lower_bound": str(B_first_lower),
            "B_first_gap_above_optimum": str(B_first_lower - cost),
            "scalar_initial_lower_bounds": strings((scalar_A_lower, scalar_B_lower)),
        },
        "normal_warmup": {
            "input": strings(warm_input), "exp_duration": str(exp_warm),
            "preparation_after_warmup": strings(warm),
            "target_domination_gaps": strings(tuple(value - target for value, target in zip(warm, p))),
            "maintenance_input": strings(upkeep_input), "optional_rate": str(optional),
        },
        "positive_precision": {
            "feasible_epsilon_interval": "0<=epsilon<=63/200",
            "nominal_optimizer": "(37/200+epsilon, 7/5+epsilon)",
            "optimal_upkeep": "177/100+3*epsilon",
            "two_partial_interval": "0<=epsilon<63/200",
            "nominal_at_maximum_epsilon": strings(nominal_at_cap),
            "upkeep_at_maximum_epsilon": str(precision_cost_at_cap),
            "optional_rate_at_maximum_epsilon": str(s - precision_cost_at_cap),
            "infeasibility_above_cap": "q_A<37/200 violates the scalar handoff deadline bound",
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "build" / "proportional-drain-verification.json")
    args = parser.parse_args()
    if sys.flags.optimize:
        parser.error("Do not use -O, -OO, or PYTHONOPTIMIZE: assertions must run")
    target = args.output.resolve()
    immutable = (ROOT / "checkpoints").resolve()
    if target == immutable or immutable in target.parents:
        parser.error("Output cannot overwrite an immutable checkpoint")
    result = certificates()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"PASS: exact proportional-drain witness and lower-bound certificates.\n{target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
