"""Exact full-state exit values for the instantaneous fixed-loss model.

Uses the existing Model/Module validation domain (in particular a_i > 0).
The pass-9 theorem also permits zero releases, which that existing constructor
does not represent. Fractions give exact arithmetic; None denotes infinity.
The forward subset DP uses O(n*2**n) rational operations and O(2**n) labels,
apart from input and the recovered order. This is not a bit-complexity bound.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from heterogeneous import Model, Module, rational


@dataclass(frozen=True)
class PartialExit:
    time: Fraction | None
    initial_ready: tuple[int, ...]
    order: tuple[int, ...] | None


def solve_partial(model: Model, preparation: tuple[int | Fraction, ...]) -> PartialExit:
    """Return an optimal time and one attaining serial order of nonready jobs.

    Initially full modules transfer at time zero and appear in initial_ready,
    not order. Equal-time labels retain the first encountered predecessor; no
    globally lexicographic tie-breaking property is asserted.
    """
    if not isinstance(model, Model):
        raise TypeError("model must be a heterogeneous.Model")
    preparation = tuple(preparation)
    if len(preparation) != len(model.modules):
        raise ValueError("preparation must have one entry per module")
    initial = tuple(rational(value, f"preparation[{i}]") for i, value in enumerate(preparation))
    if any(not 0 <= p <= module.M for p, module in zip(initial, model.modules)):
        raise ValueError("Require 0 <= preparation[i] <= M_i")
    ready = tuple(i for i, (p, module) in enumerate(zip(initial, model.modules)) if p == module.M)
    start = sum(1 << i for i in ready)
    earliest = {start: Fraction(0)}
    parent: dict[int, tuple[int, int]] = {}
    # Adding an absent bit increases the integer mask, so this is a topological
    # ordering of the subset DAG even without explicitly sorting by cardinality.
    for mask in range(start, model.full_mask + 1):
        if mask not in earliest:
            continue
        elapsed = earliest[mask]
        capacity = model.capacity(mask)
        for i, module in enumerate(model.modules):
            if mask & (1 << i) or capacity <= module.d:
                continue
            passive = max(Fraction(0), initial[i] - module.d * elapsed)
            candidate = elapsed + (module.M - passive) / (capacity - module.d)
            next_mask = mask | (1 << i)
            if next_mask not in earliest or candidate < earliest[next_mask]:
                earliest[next_mask] = candidate
                parent[next_mask] = (mask, i)
    if model.full_mask not in earliest:
        return PartialExit(None, ready, None)
    order = []
    mask = model.full_mask
    while mask != start:
        mask, i = parent[mask]
        order.append(i)
    return PartialExit(earliest[model.full_mask], ready, tuple(reversed(order)))
