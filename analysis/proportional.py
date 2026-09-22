"""Exact common-gamma proportional-loss exit and maintenance calculations.

The API uses the rational multiplier X = exp(gamma * H), not a rational time H.
Inputs are integers or Fractions. Modules have positive sizes and nonnegative releases,
gamma is positive, and s > max_i gamma*M_i. Initialization is paid separately.
The written seriality and concentration proofs justify the finite algorithms;
this implementation does not establish their continuous-time optimality.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import cached_property, lru_cache


def rational(value: int | Fraction, name: str) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError(f"{name} must be an integer or Fraction")
    return Fraction(value)


@dataclass(frozen=True)
class Module:
    M: Fraction
    a: Fraction

    def __post_init__(self) -> None:
        for name in ("M", "a"):
            object.__setattr__(self, name, rational(getattr(self, name), name))
        if self.M <= 0 or self.a < 0:
            raise ValueError("Require M > 0 and a >= 0")


@dataclass(frozen=True)
class Exit:
    multiplier: Fraction
    order: tuple[int, ...]


@dataclass(frozen=True)
class Readiness:
    deadline_multiplier: Fraction
    state: tuple[Fraction, ...]
    order: tuple[int, ...]
    upkeep: Fraction
    exit_multiplier: Fraction
    nominal_feasible: bool
    optional_throughput: Fraction | None


@dataclass(frozen=True)
class Model:
    s: Fraction
    gamma: Fraction
    modules: tuple[Module, ...]

    def __post_init__(self) -> None:
        for name in ("s", "gamma"):
            object.__setattr__(self, name, rational(getattr(self, name), name))
        object.__setattr__(self, "modules", tuple(self.modules))
        if not self.modules:
            raise ValueError("Require at least one module")
        if any(not isinstance(module, Module) for module in self.modules):
            raise TypeError("modules must contain proportional.Module instances")
        if self.gamma <= 0 or self.s <= max(self.gamma * m.M for m in self.modules):
            raise ValueError("Require gamma > 0 and s > max_i gamma*M_i")

    @property
    def full_mask(self) -> int:
        return (1 << len(self.modules)) - 1

    def _check_mask(self, mask: int) -> None:
        if isinstance(mask, bool) or not isinstance(mask, int):
            raise TypeError("mask must be an integer")
        if not 0 <= mask <= self.full_mask:
            raise ValueError("mask contains an invalid module index")

    def _state(self, state: tuple[int | Fraction, ...]) -> tuple[Fraction, ...]:
        state = tuple(rational(p, "preparation") for p in state)
        if len(state) != len(self.modules):
            raise ValueError("state must have one entry per module")
        if any(p < 0 or p > m.M for p, m in zip(state, self.modules)):
            raise ValueError("Require 0 <= p_i <= M_i")
        return state

    def _ready_mask(self, state: tuple[Fraction, ...]) -> int:
        return sum(1 << i for i, (p, m) in enumerate(zip(state, self.modules)) if p == m.M)

    def capacity(self, mask: int) -> Fraction:
        self._check_mask(mask)
        return self._capacities[mask]

    @cached_property
    def _capacities(self) -> tuple[Fraction, ...]:
        values = [self.s] * (self.full_mask + 1)
        for mask in range(1, self.full_mask + 1):
            bit = mask & -mask
            values[mask] = values[mask ^ bit] + self.modules[bit.bit_length() - 1].a
        return tuple(values)

    def schedule_multiplier(self, state: tuple[int | Fraction, ...],
                            order: tuple[int, ...]) -> Fraction:
        """Evaluate a serial witness, transferring every initially full module at zero.

        The order must contain each initially subfull module exactly once.
        Unserved module i has preparation p_i(0)/x at global multiplier x.
        """
        state = self._state(state)
        order = tuple(order)
        mask = self._ready_mask(state)
        remaining = {i for i in range(len(self.modules)) if not mask & (1 << i)}
        if (any(isinstance(i, bool) or not isinstance(i, int) for i in order)
                or len(order) != len(remaining) or set(order) != remaining):
            raise ValueError("order must list every initially subfull module once")
        x = Fraction(1)
        for i in order:
            b, m = self.capacity(mask), self.modules[i]
            x = (b * x - self.gamma * state[i]) / (b - self.gamma * m.M)
            mask |= 1 << i
        return x

    def exit_schedule(self, state: tuple[int | Fraction, ...]) -> Exit:
        """Optimal full-state exit via earliest-arrival forward subset DP.

        There are O(n*2**n) rational operations, excluding rational bit costs.
        The returned order is deterministic; no universal priority is asserted.
        """
        state = self._state(state)
        ready = self._ready_mask(state)
        earliest: dict[int, Fraction] = {ready: Fraction(1)}
        parent: dict[int, tuple[int, int]] = {}
        for mask in range(ready, self.full_mask + 1):
            if mask not in earliest:
                continue
            b, x = self.capacity(mask), earliest[mask]
            for i, m in enumerate(self.modules):
                if mask & (1 << i):
                    continue
                next_mask = mask | (1 << i)
                candidate = (b * x - self.gamma * state[i]) / (b - self.gamma * m.M)
                if next_mask not in earliest or candidate < earliest[next_mask]:
                    earliest[next_mask] = candidate
                    parent[next_mask] = (mask, i)
        order: list[int] = []
        mask = self.full_mask
        while mask != ready:
            mask, i = parent[mask]
            order.append(i)
        return Exit(earliest[self.full_mask], tuple(reversed(order)))

    def exit_multiplier(self, state: tuple[int | Fraction, ...]) -> Fraction:
        return self.exit_schedule(state).multiplier

    def cold_multiplier(self, ready_mask: int = 0) -> Fraction:
        """Optimal exit multiplier for a ready/cold state."""
        self._check_mask(ready_mask)
        return self._cold_multiplier(ready_mask)

    @lru_cache(maxsize=None)
    def _cold_multiplier(self, mask: int) -> Fraction:
        if mask == self.full_mask:
            return Fraction(1)
        b = self.capacity(mask)
        return min(b / (b - self.gamma * m.M) * self._cold_multiplier(mask | (1 << i))
                   for i, m in enumerate(self.modules) if not mask & (1 << i))

    def cold_order(self, ready_mask: int = 0) -> tuple[int, ...]:
        """An attaining serial order for the ready/cold multiplier."""
        self._check_mask(ready_mask)
        order: list[int] = []
        mask = ready_mask
        while mask != self.full_mask:
            b, target = self.capacity(mask), self.cold_multiplier(mask)
            for i, m in enumerate(self.modules):
                next_mask = mask | (1 << i)
                if (not mask & (1 << i)
                        and b / (b - self.gamma * m.M) * self.cold_multiplier(next_mask) == target):
                    order.append(i)
                    mask = next_mask
                    break
            else:
                raise RuntimeError("No attaining cold transition")
        return tuple(order)

    def readiness(self, deadline_multiplier: int | Fraction) -> Readiness:
        """Minimum common-gamma upkeep at a rational transformed deadline X>=1.

        Enumerates fully ready subsets and one possible partial module. A
        partial-first witness attains the returned cost; partial-first need
        not optimize the exit time of every already prescribed partial state.
        Negative optional throughput is reported as infeasible, never attained.
        """
        X = rational(deadline_multiplier, "deadline_multiplier")
        if X < 1:
            raise ValueError("Require deadline_multiplier >= 1")
        costs = [Fraction(0)] * (self.full_mask + 1)
        for mask in range(1, self.full_mask + 1):
            bit = mask & -mask
            costs[mask] = costs[mask ^ bit] + self.gamma * self.modules[bit.bit_length() - 1].M
        best_cost = costs[self.full_mask]
        best: tuple[int, int | None, Fraction] = (self.full_mask, None, Fraction(0))
        for mask in range(self.full_mask):
            b = self.capacity(mask)
            for i, m in enumerate(self.modules):
                if mask & (1 << i):
                    continue
                tail = self.cold_multiplier(mask | (1 << i))
                if X < tail:
                    continue
                q = max(Fraction(0), (b - (b - self.gamma * m.M) * X / tail) / self.gamma)
                cost = costs[mask] + self.gamma * q
                if cost < best_cost:
                    best_cost, best = cost, (mask, i, q)
        mask, partial, q = best
        state = tuple(m.M if mask & (1 << i) else q if i == partial else Fraction(0)
                      for i, m in enumerate(self.modules))
        if partial is None:
            order: tuple[int, ...] = ()
        else:
            tail_order = self.cold_order(mask | (1 << partial))
            order = (partial,) + tail_order if q < self.modules[partial].M else tail_order
        feasible = best_cost <= self.s
        return Readiness(X, state, order, best_cost, self.schedule_multiplier(state, order),
                         feasible, self.s - best_cost if feasible else None)
