"""Numerical frontier for unequal positive proportional loss coefficients.

Parameters and accessibility tests are rational. Times, exponentials, costs,
and deadline comparisons use binary64 floating arithmetic and are NOT certified
exact decisions. One cold-prefix subset DP is processed at a time, giving
O(n*3**n) transcendental/arithmetic evaluations and O(2**n) working labels.
The returned state is clipped to its physical box and its schedule is recounted;
this is a numerical consistency check, not a formal feasibility certificate.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction as Q
import math

DEFAULT_TOLERANCE = 1e-10


def rational(value, name):
    if isinstance(value, bool) or not isinstance(value, (int, Q)):
        raise TypeError(f"{name} must be an integer or Fraction")
    return Q(value)


def finite_float(value, name):
    try:
        result = float(value)
    except (OverflowError, ValueError) as exc:
        raise ValueError(f"{name} cannot be represented as a finite float") from exc
    if not math.isfinite(result):
        raise ValueError(f"{name} must have a finite floating representation")
    return result


@dataclass(frozen=True)
class ProportionalModule:
    M: Q
    a: Q
    gamma: Q

    def __post_init__(self):
        for name in ("M", "a", "gamma"):
            object.__setattr__(self, name, rational(getattr(self, name), name))
        if self.M <= 0 or self.a < 0 or self.gamma <= 0:
            raise ValueError("Require M>0, a>=0, and gamma>0")
        for name in ("M", "gamma"):
            if finite_float(getattr(self, name), name) <= 0:
                raise ValueError(f"{name} underflows binary64")
        finite_float(self.a, "a")
        if finite_float(self.gamma * self.M, "gamma*M") <= 0:
            raise ValueError("gamma*M underflows binary64")


@dataclass(frozen=True)
class ProportionalModel:
    s: Q
    modules: tuple[ProportionalModule, ...]

    def __post_init__(self):
        object.__setattr__(self, "s", rational(self.s, "s"))
        object.__setattr__(self, "modules", tuple(self.modules))
        if self.s < 0 or not self.modules:
            raise ValueError("Require s>=0 and at least one module")
        if any(not isinstance(m, ProportionalModule) for m in self.modules):
            raise TypeError("modules must contain ProportionalModule objects")
        finite_float(self.s, "s")


@dataclass(frozen=True)
class NumericalFrontier:
    deadline: float
    upkeep: float
    preparation: tuple[float, ...]
    ready: tuple[int, ...]
    partial_index: int | None
    order: tuple[int, ...]
    completion_time: float
    nominal_feasible_estimate: bool
    optional_throughput_estimate: float | None
    comparison_tolerance: float
    precision: str = "Binary64 estimates; transcendental and deadline comparisons are not certified."


def subset_tables(model):
    n = len(model.modules)
    capacities, costs = [model.s] * (1 << n), [Q(0)] * (1 << n)
    for mask in range(1, 1 << n):
        bit = mask & -mask
        i, previous = bit.bit_length() - 1, mask ^ bit
        capacities[mask] = capacities[previous] + model.modules[i].a
        costs[mask] = costs[previous] + model.modules[i].gamma * model.modules[i].M
    finite_float(capacities[-1], "total capacity")
    finite_float(costs[-1], "total upkeep")
    return capacities, costs


def cold_edge(module, capacity):
    """Exact rational barrier check, then a floating logarithmic stage value."""
    loss = module.gamma * module.M
    denominator = capacity - loss
    if denominator <= 0:
        return math.inf
    ratio = loss / denominator
    try:
        numeric_ratio = float(ratio)
    except OverflowError:
        numeric_ratio = math.inf
    logarithm = (math.log1p(numeric_ratio) if math.isfinite(numeric_ratio) else
                 math.log((capacity / denominator).numerator) - math.log((capacity / denominator).denominator))
    value = logarithm / float(module.gamma)
    if not math.isfinite(value) or value <= 0:
        raise ArithmeticError("Cold stage outside supported floating range; rescale or use certified arithmetic")
    return value


def cold_values(model, capacities):
    full = len(capacities) - 1
    times, successor = [math.inf] * len(capacities), [None] * len(capacities)
    times[full] = 0.0
    for mask in range(full - 1, -1, -1):
        for i, module in enumerate(model.modules):
            if mask >> i & 1:
                continue
            nxt = mask | (1 << i)
            edge = cold_edge(module, capacities[mask])
            value = edge + times[nxt]
            if value < times[mask]:
                times[mask], successor[mask] = value, i
    return times, successor


def prefix_values(model, capacities, ready):
    # Enumerate only supersets of ready. Reinitializing/scanning a full 2**n
    # table for every ready set would incur 4**n work, defeating the stated bound.
    labels, previous = {ready: 0.0}, {}
    free, sub = (len(capacities) - 1) ^ ready, 0
    while True:
        mask = ready | sub
        elapsed = labels.get(mask, math.inf)
        if math.isfinite(elapsed):
            for i, module in enumerate(model.modules):
                if mask >> i & 1:
                    continue
                candidate = elapsed + cold_edge(module, capacities[mask])
                nxt = mask | (1 << i)
                if candidate < labels.get(nxt, math.inf):
                    labels[nxt], previous[nxt] = candidate, (mask, i)
        if sub == free:
            break
        sub = (sub - free) & free
    return labels, previous


def needed_partial(module, capacity, prefix, tail, deadline, tolerance):
    denominator = capacity - module.gamma * module.M
    if denominator <= 0:
        return None
    b, D, gamma, M = map(float, (capacity, denominator, module.gamma, module.M))
    if b <= 0 or D <= 0:
        raise ArithmeticError("Positive stage denominator underflows binary64")
    log_a = math.log(b) + gamma * prefix
    log_b = math.log(D) + gamma * (deadline - tail)
    if not math.isfinite(log_a) or not math.isfinite(log_b):
        raise ArithmeticError("Candidate exponential outside supported floating range")
    if log_b >= log_a:
        return 0.0
    # Compute the positive exponential difference without overflowing either
    # exponential. Only candidates within the finite physical box are retained.
    log_q = log_a + math.log(-math.expm1(log_b - log_a)) - math.log(gamma)
    cap = M + tolerance * max(1.0, M)
    if log_q > math.log(cap):
        return None
    return min(M, max(0.0, math.exp(log_q)))


def recount_schedule(model, preparation, planned_order):
    """Numerically replay the witness, transferring every initially full job at zero."""
    sizes = tuple(float(m.M) for m in model.modules)
    ready = tuple(i for i, p in enumerate(preparation) if p == sizes[i])
    completed = sum(1 << i for i in ready)
    capacities, _ = subset_tables(model)
    elapsed, order = 0.0, []
    for i in planned_order:
        if completed >> i & 1:
            continue
        module = model.modules[i]
        denominator = capacities[completed] - module.gamma * module.M
        if denominator <= 0:
            return math.inf, ready, tuple(order)
        gamma, M, D = float(module.gamma), sizes[i], float(denominator)
        if D <= 0:
            raise ArithmeticError("Positive witness denominator underflows binary64")
        passive = min(M, max(0.0, preparation[i] * math.exp(-gamma * elapsed)))
        ratio = gamma * (M - passive) / D
        increment = (math.log1p(ratio) if math.isfinite(ratio) else
                     math.log(gamma * (M - passive)) - math.log(D)) / gamma
        elapsed += increment
        completed |= 1 << i
        order.append(i)
    if completed != (1 << len(model.modules)) - 1:
        raise ValueError("Witness order omits an unfinished module")
    return elapsed, ready, tuple(order)


def frontier(model: ProportionalModel, deadline, tolerance=DEFAULT_TOLERANCE) -> NumericalFrontier:
    """Return a floating frontier estimate and a recounted concentrated witness.

    A cold prefix before the one partial module is included. The comparison
    tolerance does not turn the result into a certified endpoint decision.
    """
    if not isinstance(model, ProportionalModel):
        raise TypeError("model must be ProportionalModel")
    if isinstance(deadline, bool) or not isinstance(deadline, (int, float, Q)):
        raise TypeError("deadline must be a finite number")
    H = finite_float(deadline, "deadline")
    tolerance = finite_float(tolerance, "tolerance")
    if H < 0 or tolerance <= 0:
        raise ValueError("Require deadline>=0 and tolerance>0")
    capacities, ready_costs = subset_tables(model)
    full = len(capacities) - 1
    cold, successor = cold_values(model, capacities)
    best_cost, best = float(ready_costs[full]), (full, full, None, 0.0)
    if H > 0:
        for ready in range(full + 1):
            base = float(ready_costs[ready])
            if base >= best_cost:
                continue
            if cold[ready] <= H + tolerance * max(1.0, H) and base < best_cost:
                best_cost, best = base, (ready, ready, None, 0.0)
            labels, _ = prefix_values(model, capacities, ready)
            for mask, prefix in labels.items():
                if not math.isfinite(prefix):
                    continue
                for i, module in enumerate(model.modules):
                    if mask >> i & 1:
                        continue
                    tail = cold[mask | (1 << i)]
                    if not math.isfinite(tail):
                        continue
                    q = needed_partial(module, capacities[mask], prefix, tail, H, tolerance)
                    if q is None:
                        continue
                    candidate = base + float(module.gamma) * q
                    if candidate < best_cost:
                        best_cost, best = candidate, (ready, mask, i, q)
    ready, prefix_mask, partial, q = best
    preparation = [float(m.M) if ready >> i & 1 else 0.0 for i, m in enumerate(model.modules)]
    planned = []
    if partial is not None:
        preparation[partial] = q
        _, previous = prefix_values(model, capacities, ready)
        mask, reverse = prefix_mask, []
        while mask != ready:
            parent, job = previous[mask]
            reverse.append(job)
            mask = parent
        planned.extend(reversed(reverse))
        planned.append(partial)
        mask = prefix_mask | (1 << partial)
    else:
        mask = ready
    while mask != full:
        job = successor[mask]
        if job is None:
            raise ArithmeticError("Selected numerical candidate has no finite cold tail")
        planned.append(job)
        mask |= 1 << job
    completion, actual_ready, order = recount_schedule(model, tuple(preparation), tuple(planned))
    if completion > H + tolerance * max(1.0, H):
        raise ArithmeticError("Recounted witness exceeds numerical deadline tolerance")
    upkeep = math.fsum(float(m.gamma) * p for m, p in zip(model.modules, preparation))
    partials = [i for i, (m, p) in enumerate(zip(model.modules, preparation)) if 0 < p < float(m.M)]
    if len(partials) > 1:
        raise ArithmeticError("Constructed witness unexpectedly has multiple partial coordinates")
    feasible = upkeep <= float(model.s)
    return NumericalFrontier(H, upkeep, tuple(preparation), actual_ready, partials[0] if partials else None,
                             order, completion, feasible, float(model.s) - upkeep if feasible else None, tolerance)
