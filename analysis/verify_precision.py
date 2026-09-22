#!/usr/bin/env python3
"""Exact finite checks for the one-sided preparation-precision boundary.

This independent standard-library checker uses rational common-rate serial
recurrences and exhaustive two-dimensional LP vertex enumeration. The written
pass-18 proof, not the finite samples, supplies the limiting and universal
claims. Separate rational certificates support pass 17's fixed-order
nonconvexity example and pass 19's local exchange with a prepared middle
module; these do not characterize the union over orders or global optima.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from itertools import combinations, permutations, product
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def multiplier(s, gamma, modules, preparation, initial_full=()):
    """Minimum exp(gamma*T), or None; modules are (M,a) rational pairs.

    With initial_full empty this is the strict-order envelope, even if a
    coordinate is full. Passing every full coordinate instead implements the
    original instantaneous-transfer convention. No floating arithmetic is used.
    """
    completed = frozenset(initial_full)
    remaining = tuple(i for i in range(len(modules)) if i not in completed)
    initial_capacity = s + sum((modules[i][1] for i in completed), Q(0))
    best = None
    for order in permutations(remaining):
        capacity, elapsed = initial_capacity, Q(1)
        for i in order:
            M, release = modules[i]
            denominator = capacity - gamma * M
            if denominator <= 0:
                break
            updated = (capacity * elapsed - gamma * preparation[i]) / denominator
            assert updated >= elapsed >= 1
            elapsed = updated
            capacity += release
        else:
            best = elapsed if best is None else min(best, elapsed)
    return best


def polygon_vertices(constraints):
    """Vertices of a bounded 2D polyhedron a*x+b*y>=c, by all line pairs."""
    vertices = set()
    for (a, b, c), (d, e, f) in combinations(constraints, 2):
        determinant = a * e - b * d
        if determinant == 0:
            continue
        x, y = (c * e - b * f) / determinant, (a * f - c * d) / determinant
        if all(u * x + v * y >= w for u, v, w in constraints):
            vertices.add((x, y))
    return vertices


def tolerance_optimum(epsilon):
    """Independently enumerate all four max(p-epsilon,0) regions."""
    bounds = ((Q(1), Q(0), Q(0)), (Q(-1), Q(0), Q(-1, 2)),
              (Q(0), Q(1), Q(0)), (Q(0), Q(-1), Q(-1)))
    vertices = set()
    for active_A, active_B in product((False, True), repeat=2):
        constraints = list(bounds)
        constraints.append((Q(1 if active_A else -1), Q(0), epsilon if active_A else -epsilon))
        constraints.append((Q(0), Q(1 if active_B else -1), epsilon if active_B else -epsilon))
        weight_A, weight_B = Q(4 if active_A else 0), Q(1 if active_B else 0)
        constraints.append((weight_A, weight_B, Q(8, 3) + epsilon * (weight_A + weight_B)))
        vertices.update(polygon_vertices(constraints))
    if not vertices:
        return None, ()
    cost = min(x + y for x, y in vertices)
    minimizers = tuple(sorted((x, y) for x, y in vertices if x + y == cost))
    return cost, minimizers


def verify():
    counts = {key: 0 for key in ("strict_oracle_grid_states", "original_oracle_grid_states",
                                "endpoint_identities", "tolerance_LP_instances",
                                "nonconvex_certificate_points", "prepared_middle_exchange_states")}
    s = gamma = Q(1)
    modules = ((Q(1, 2), Q(1)), (Q(1), Q(1)))
    deadline_multiplier = Q(4, 3)
    # A is accessible first; B is not. The recurrence must still account
    # for a full B waiting and decaying when it is not transferred at zero.
    for pA, pB in product((Q(k, 12) for k in range(7)), (Q(k, 12) for k in range(13))):
        state = (pA, pB)
        strict = multiplier(s, gamma, modules, state)
        assert strict == 4 - 4 * pA - pB
        counts["strict_oracle_grid_states"] += 1
        full = tuple(i for i in range(2) if state[i] == modules[i][0])
        original = multiplier(s, gamma, modules, state, full)
        if pB < 1:
            assert original == strict
        else:
            assert original == (2 - pA) / Q(3, 2)
        assert original <= strict
        counts["original_oracle_grid_states"] += 1
    assert multiplier(s, gamma, modules, (Q(0), Q(0))) == 4
    assert multiplier(s, gamma, modules, (Q(0), Q(1))) == 3
    assert multiplier(s, gamma, modules, (Q(0), Q(1)), (1,)) == deadline_multiplier
    assert multiplier(s, gamma, modules, (Q(1, 2), Q(1))) == 1
    counts["endpoint_identities"] += 4
    # The subfull-B/original branch equals the strict halfspace. Its closed
    # LP minimum is attained below B's full endpoint, so closure adds no
    # spurious lower cost. The separate full-B face has unique cost-one point.
    regular_cost, regular_minimizers = tolerance_optimum(Q(0))
    assert regular_cost == Q(7, 6)
    assert regular_minimizers == ((Q(1, 2), Q(2, 3)),)
    full_B_cost, full_B_minimizer = Q(1), (Q(0), Q(1))
    assert full_B_cost < regular_cost
    assert multiplier(s, gamma, modules, full_B_minimizer, (1,)) == deadline_multiplier
    counts["tolerance_LP_instances"] += 1
    epsilon_samples = (Q(1, 1000), Q(1, 120), Q(1, 60), Q(1, 30), Q(1, 15),
                       Q(1, 14), Q(1, 2), Q(1), Q(2))
    records = []
    for epsilon in epsilon_samples:
        cost, minimizers = tolerance_optimum(epsilon)
        if epsilon <= Q(1, 15):
            expected = (Q(1, 2), Q(2, 3) + 5 * epsilon)
            assert cost == Q(7, 6) + 5 * epsilon
            assert minimizers == (expected,)
            worst = tuple(max(p - epsilon, Q(0)) for p in expected)
            assert all(worst[i] < modules[i][0] for i in range(2))
            assert multiplier(s, gamma, modules, worst) == deadline_multiplier
            assert cost >= full_B_cost + epsilon
        else:
            assert cost is None and minimizers == ()
            maximal_worst = tuple(max(M - epsilon, Q(0)) for M, _ in modules)
            assert multiplier(s, gamma, modules, maximal_worst) > deadline_multiplier
        records.append({"epsilon": str(epsilon), "cost": None if cost is None else str(cost),
                        "minimizing_vertices": [[str(v) for v in point] for point in minimizers]})
        counts["tolerance_LP_instances"] += 1
    # Pass 17: squaring is order preserving because both sides are positive.
    P, R = (Q(13, 25), Q(1, 5)), (Q(3, 8), Q(1, 2))
    midpoint = tuple((a + b) / 2 for a, b in zip(P, R))
    assert midpoint == (Q(179, 400), Q(7, 20))
    for x, y in (P, R):
        assert 0 < x < 1 and 0 < y < 1
        assert 9 * (3 - 2 * x) == (y + 4) ** 2
        counts["nonconvex_certificate_points"] += 1
    x, y = midpoint
    assert 0 < x < 1 and 0 < y < 1
    squared_gap = 9 * (3 - 2 * x) - (y + 4) ** 2
    assert squared_gap == Q(9, 400) > 0
    counts["nonconvex_certificate_points"] += 1
    # Pass 19: an interior stationary maximum along a deadline-preserving
    # exchange, with a positive middle coordinate fixed at its nominal cap.
    # These three rational states illustrate the exchange mechanism. They
    # neither optimize the instance globally nor prove the general theorem.
    exchange_s, exchange_epsilon = Q(10), Q(1, 10)
    exchange_M, exchange_gamma = (Q(3), Q(2), Q(2)), (Q(2), Q(1), Q(1))
    exchange_cap = tuple(M - exchange_epsilon for M in exchange_M)
    z_star, E, q_middle = Q(25, 16), Q(533, 256), Q(19, 10)
    center_cost = Q(971, 320)
    exchange_records = []
    for displacement in (Q(-1, 100), Q(0), Q(1, 100)):
        z = z_star + displacement
        q_j = (exchange_s - 4 * z ** 2) / 2
        exp_middle = (exchange_s * z - q_middle) / 8
        q_k = exchange_s * exp_middle - 8 * E
        actual = (q_j, q_middle, q_k)
        nominal = tuple(q + exchange_epsilon for q in actual)
        assert 0 < q_j < exchange_cap[0]
        assert q_middle == exchange_cap[1]
        assert 0 < q_k < exchange_cap[2]
        assert 1 < z < exp_middle < E
        assert all(0 < p <= M for p, M in zip(nominal, exchange_M))
        # Exact three-stage recurrence in the unchanged order j,middle,k.
        assert (exchange_s - 2 * q_j) / (exchange_s - 2 * exchange_M[0]) == z ** 2
        assert (exchange_s * z - q_middle) / (exchange_s - exchange_M[1]) == exp_middle
        assert (exchange_s * exp_middle - q_k) / (exchange_s - exchange_M[2]) == E
        nominal_cost = sum((g * p for g, p in zip(exchange_gamma, nominal)), Q(0))
        assert nominal_cost == center_cost - 4 * displacement ** 2 < exchange_s
        if displacement == 0:
            assert q_j == Q(15, 128) and q_k == Q(1, 2)
        else:
            assert center_cost - nominal_cost == Q(1, 2500)
        exchange_records.append({"z": str(z), "worst_corner": [str(v) for v in actual],
                                 "nominal": [str(v) for v in nominal],
                                 "exp_middle_completion": str(exp_middle),
                                 "nominal_cost": str(nominal_cost),
                                 "cost_decrease_from_center": str(center_cost - nominal_cost)})
        counts["prepared_middle_exchange_states"] += 1
    return {
        "schema_version": 1, "status": "PASS", "arithmetic": "fractions.Fraction only",
        "scope": "Exact finite checks of the precision fixture using an independent serial recurrence and 2D polyhedral vertex enumeration, plus fixed-order nonconvexity and prepared-middle local-exchange certificates; no numerical optimization or floating decisions. Written proofs supply continuum, policy, limit and optimality claims beyond these finite instances.",
        "counts": counts,
        "critical_fixture": {"s": "1", "gamma": "1", "modules": [{"M": "1/2", "a": "1"}, {"M": "1", "a": "1"}],
                             "exp_H": "4/3", "strict_exp_F": "4-4*p_A-p_B",
                             "cold_exp_F": "4", "full_B_original_exp_F": "4/3", "full_B_strict_exp_F": "3",
                             "original_cost": str(full_B_cost), "original_minimizer": [str(v) for v in full_B_minimizer],
                             "limiting_cost": str(regular_cost), "limiting_minimizer": [str(v) for v in regular_minimizers[0]],
                             "nonvanishing_cost_gap": str(regular_cost - full_B_cost)},
        "fixed_tolerance_samples": records,
        "tolerance_method": "For each epsilon, enumerate all pairwise boundary intersections in each of the four affine regions of max(p-epsilon,0), discard infeasible points, and minimize p_A+p_B over retained vertices. Null cost denotes an empty feasible set.",
        "nonconvex_fixed_order_certificate": {"endpoints": [[str(v) for v in P], [str(v) for v in R]],
                                               "midpoint": [str(v) for v in midpoint], "positive_squared_gap": str(squared_gap),
                                               "scope": "Prescribed order 1 then 2 only; no claim about the union over orders or general nonlinear reductions."},
        "prepared_middle_exchange": {"s": "10", "gamma": ["2", "1", "1"], "M": ["3", "2", "2"],
                                     "a": ["0", "0", "0"], "epsilon": "1/10", "exp_H": str(E),
                                     "z_star": str(z_star), "center_nominal_cost": str(center_cost),
                                     "local_cost_formula": "971/320-4*(z-25/16)^2", "samples": exchange_records,
                                     "scope": "Three exact states on one fixed-deadline exchange with a nominally full prepared middle module. Both neighboring states lower upkeep by 1/2500. This is a local stationary maximum certificate, not a global optimizer check or a proof of the general exchange theorem."}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / "build" / "precision-verification.json")
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
    print(f"PASS: exact precision, fixed-order nonconvexity and prepared-middle exchange checks.\n{target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
