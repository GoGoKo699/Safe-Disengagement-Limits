#!/usr/bin/env python3
"""Small exact checks for the S1 active-readiness model; not a theorem prover.

Run with Python 3.10+ and no third-party packages:
    python verify.py
The checked parameter grids are deliberately finite. The analytic proofs are in
NOTE.md. Nothing here is an empirical validation of live migration or control.
"""
from __future__ import annotations

import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path
from typing import Sequence


def drift(p: F | int, v: F | int, d: F | int, M: F | int):
    """Worst-case reflected preparation drift under fixed-rate invalidation."""
    if not (0 <= p <= M) or v < 0 or d < 0 or M <= 0:
        raise ValueError("Invalid state, rate or preparation size")
    if p == 0:
        return max(v - d, 0)
    if p == M:
        return min(v - d, 0)
    return v - d


def exit_times(n: int, a: F, s: F, d: F, M: F) -> list[F | None]:
    """T[k]: exact cold-tail completion time with k initially ready modules.

    None represents infinity. A ready module transfers instantaneously.
    """
    if n < 1 or a <= 0 or M <= 0 or min(s, d) < 0:
        raise ValueError("Invalid model parameters")
    out: list[F | None] = [None] * n + [F(0)]
    for k in range(n - 1, -1, -1):
        rate = s + k * a - d
        if rate > 0 and out[k + 1] is not None:
            out[k] = M / rate + out[k + 1]
    return out


def readiness_count(times: Sequence[F | None], H: F) -> int:
    if H < 0:
        raise ValueError("Deadline must be nonnegative")
    return next(k for k, t in enumerate(times) if t is not None and t <= H)


def check_nominal_inequality() -> int:
    count = 0
    # Integer-scaled grids: these are exact rational states/rates, not rounding.
    for n in range(1, 4):
        for p in itertools.product(range(5), repeat=n):
            support = sum(x > 0 for x in p)
            for v in itertools.product(range(5), repeat=n):
                for d in range(4):
                    derivative = sum(drift(x, y, d, 4) for x, y in zip(p, v))
                    assert derivative <= sum(v) - d * support
                    count += 1
    return count


def check_transition_potential_inequality() -> int:
    count = 0
    for n in range(1, 4):
        for initially_ready in range(n):
            m = n - initially_ready
            for initial_slack, a, d in itertools.product((1, 2, 4), (1, 2), (0, 1, 2)):
                b = initial_slack + initially_ready * a
                if b <= d:
                    continue
                for completed in range(m):
                    remaining = m - completed
                    capacity = b + a * completed
                    # Uniform allocation grid, filtered to feasible total rate.
                    allocations = [v for v in itertools.product(range(7), repeat=remaining)
                                   if sum(v) <= capacity]
                    for p in itertools.product(range(4), repeat=remaining):
                        z = 4 * completed + sum(p)
                        for v in allocations:
                            zdot = sum(drift(x, y, d, 4) for x, y in zip(p, v))
                            assert zdot <= capacity - d
                            assert capacity - d <= b + a * (z // 4) - d
                            count += 1
    return count


def check_curves_and_matching_policies() -> dict[str, int]:
    counts = {"parameter_curves": 0, "finite_serial_stages": 0,
              "deadline_thresholds": 0, "feasible_matching_policies": 0}
    for n, a, s, d, M in itertools.product(
            range(1, 9), (F(1, 2), F(1), F(2), F(4)),
            (F(0), F(1, 4), F(1, 2), F(1), F(2), F(3), F(4)),
            (F(0), F(1, 4), F(1, 2), F(1), F(2)),
            (F(1, 2), F(1), F(2))):
        times = exit_times(n, a, s, d, M)
        counts["parameter_curves"] += 1
        for k in range(n):
            if times[k] is None:
                assert s + k * a <= d
            else:
                direct = sum((M / (s + j * a - d) for j in range(k, n)), F(0))
                assert times[k] == direct
                assert times[k + 1] is not None and times[k] > times[k + 1]
                # Full rate to one cold module achieves one stage exactly.
                rate = s + k * a
                dt = M / (rate - d)
                assert dt * drift(F(0), rate, d, M) == M
                counts["finite_serial_stages"] += 1
        deadlines = {F(0), F(1), F(2), F(10)}
        for t in times:
            if t is not None:
                deadlines.add(t)
                deadlines.add(t + F(1, 1000))
                if t >= F(1, 1000):
                    deadlines.add(t - F(1, 1000))
        for H in deadlines:
            k = readiness_count(times, H)
            assert times[k] is not None and times[k] <= H
            assert all(t is None or t > H for t in times[:k])
            counts["deadline_thresholds"] += 1
            if k * d <= s:
                p = [M] * k + [F(0)] * (n - k)
                v = [d] * k + [F(0)] * (n - k)
                optional = s - k * d
                assert optional >= 0 and optional + sum(v) == s
                assert all(drift(x, y, d, M) == 0 for x, y in zip(p, v))
                counts["feasible_matching_policies"] += 1
    return counts


def check_proportional_countermodel() -> int:
    count = 0
    for M, d, extra, fraction in itertools.product(
            (0.5, 1.0, 3.0), (0.2, 0.6, 1.0),
            (0.2, 1.0, 3.0), (0.0, 0.1, 0.5, 0.9, 1.0, 1.1)):
        s = d + extra
        gamma = d / M
        cold = math.log(s / (s - d)) / gamma
        H = fraction * cold
        upkeep = max(0.0, s - (s - d) * math.exp(gamma * H))
        p = upkeep / gamma
        assert -1e-10 <= p <= M + 1e-10
        actual = math.log((s - gamma * p) / (s - d)) / gamma
        assert actual <= H + 1e-9
        if fraction < 1:
            assert abs(actual - H) < 1e-9
        assert abs(upkeep - gamma * p) < 1e-12
        count += 1
    return count


def as_json(t: F | None):
    return {"exact": str(t) if t is not None else "infinity",
            "decimal": float(t) if t is not None else None}


def main() -> None:
    results = {
        "status": "PASS",
        "scope": "Finite algebraic and local-certificate checks only; continuous theorem proved in NOTE.md.",
        "nominal_local_inequality_cases": check_nominal_inequality(),
        "transition_local_inequality_cases": check_transition_potential_inequality(),
        "curve_and_construction_checks": check_curves_and_matching_policies(),
        "proportional_countermodel_float_checks": check_proportional_countermodel(),
    }
    n, a, s, d, M = 3, F(3), F(1), F(3, 5), F(3)
    times = exit_times(n, a, s, d, M)
    results["example"] = {
        "parameters": {"n": n, "a": str(a), "s": str(s), "d": str(d), "M": str(M)},
        "exit_times": [as_json(t) for t in times],
        "deadlines": [{"H": str(H), "k": readiness_count(times, H),
                       "required_upkeep": str(d * readiness_count(times, H)),
                       "indefinitely_feasible": d * readiness_count(times, H) <= s,
                       "optimal_optional_rate": str(s - d * readiness_count(times, H))
                       if d * readiness_count(times, H) <= s else None}
                      for H in (F(9), F(2), F(1), F(0))],
    }
    target = Path(__file__).resolve().with_name("RESULTS.json")
    target.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
