"""Exact finite-subset calculations for the heterogeneous fixed-loss model.

Only integer and Fraction inputs are accepted. ``None`` denotes an infinite
exit time; it never denotes zero. The written proof, rather than this dynamic
program, establishes optimality over continuous-time parallel/preemptive policies.
State space and running time are exponential in the number of modules.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache


def rational(value: int | Fraction, name: str) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError(f"{name} must be an integer or Fraction")
    return Fraction(value)


@dataclass(frozen=True)
class Module:
    M: Fraction
    a: Fraction
    d: Fraction

    def __post_init__(self) -> None:
        for name in ("M", "a", "d"):
            object.__setattr__(self, name, rational(getattr(self, name), name))
        if self.M <= 0 or self.a <= 0 or self.d < 0:
            raise ValueError("Require M > 0, a > 0, and d >= 0")


@dataclass(frozen=True)
class Readiness:
    deadline: Fraction
    ready: tuple[int, ...]
    upkeep: Fraction
    exit_time: Fraction
    nominal_feasible: bool
    optional_throughput: Fraction | None


@dataclass(frozen=True)
class Model:
    s: Fraction
    modules: tuple[Module, ...]

    def __post_init__(self) -> None:
        object.__setattr__(self, "s", rational(self.s, "s"))
        object.__setattr__(self, "modules", tuple(self.modules))
        if self.s < 0 or not self.modules:
            raise ValueError("Require s >= 0 and at least one module")
        if any(not isinstance(module, Module) for module in self.modules):
            raise TypeError("modules must contain Module instances")

    @property
    def full_mask(self) -> int:
        return (1 << len(self.modules)) - 1

    def _check_mask(self, ready_mask: int) -> None:
        if isinstance(ready_mask, bool) or not isinstance(ready_mask, int):
            raise TypeError("ready_mask must be an integer")
        if not 0 <= ready_mask <= self.full_mask:
            raise ValueError("ready_mask contains an invalid module index")

    def capacity(self, ready_mask: int) -> Fraction:
        self._check_mask(ready_mask)
        return self.s + sum((module.a for i, module in enumerate(self.modules)
                             if ready_mask & (1 << i)), Fraction(0))

    def exit_time(self, ready_mask: int = 0) -> Fraction | None:
        """Optimal robust time from this fully-ready/otherwise-cold state."""
        self._check_mask(ready_mask)
        return self._exit_time(ready_mask)

    @lru_cache(maxsize=None)
    def _exit_time(self, ready_mask: int) -> Fraction | None:
        if ready_mask == self.full_mask:
            return Fraction(0)
        b = self.capacity(ready_mask)
        best: Fraction | None = None
        for i, module in enumerate(self.modules):
            if ready_mask & (1 << i) or b <= module.d:
                continue
            tail = self.exit_time(ready_mask | (1 << i))
            if tail is not None:
                candidate = module.M / (b - module.d) + tail
                best = candidate if best is None else min(best, candidate)
        return best

    def optimal_order(self, ready_mask: int = 0) -> tuple[int, ...] | None:
        """Lexicographically first attaining serial order, or None if blocked."""
        target = self.exit_time(ready_mask)
        if target is None:
            return None
        order: list[int] = []
        while ready_mask != self.full_mask:
            b = self.capacity(ready_mask)
            for i, module in enumerate(self.modules):
                if ready_mask & (1 << i) or b <= module.d:
                    continue
                next_mask = ready_mask | (1 << i)
                tail = self.exit_time(next_mask)
                if tail is not None and module.M / (b - module.d) + tail == target:
                    order.append(i)
                    ready_mask, target = next_mask, tail
                    break
            else:
                raise RuntimeError("No attaining transition for finite DP value")
        return tuple(order)

    def readiness(self, deadline: int | Fraction) -> Readiness:
        """Minimum fixed ready-set upkeep; initialization must be paid separately.

        Infeasibility under the normal load is reported explicitly. A negative
        optional rate is not returned as physically attainable throughput.
        """
        deadline = rational(deadline, "deadline")
        if deadline < 0:
            raise ValueError("deadline must be nonnegative")
        candidates = []
        for mask in range(self.full_mask + 1):
            time = self.exit_time(mask)
            if time is not None and time <= deadline:
                ready = tuple(i for i in range(len(self.modules)) if mask & (1 << i))
                upkeep = sum((self.modules[i].d for i in ready), Fraction(0))
                candidates.append((upkeep, ready, time))
        upkeep, ready, time = min(candidates)
        feasible = upkeep <= self.s
        return Readiness(deadline, ready, upkeep, time, feasible,
                         self.s - upkeep if feasible else None)
