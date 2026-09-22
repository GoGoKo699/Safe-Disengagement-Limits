#!/usr/bin/env python3
"""Exact finite checks for S1's passive-commitment benchmark.

Python >= 3.10, standard library only. These finite discrete checks do not
prove the continuous-time theorem and are not infrastructure simulations.
Run: python verify.py --output validation.json
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
from itertools import product
import json
from pathlib import Path
from typing import Sequence


def tails(g: Sequence[F]) -> list[F]:
    return [sum(g[h:], F(0)) for h in range(len(g))]


def residual(g: Sequence[F], u: Sequence[F], phase: int) -> list[F]:
    """Cut after admission at phase, before that slot's service.
    u has a periodic infinite prehistory for this finite test.
    g[j] is service in age-slot j. No new admission follows the cut.
    """
    return [sum((u[(phase-a) % len(u)] * g[a+h]
                 for a in range(len(g)-h)), F(0))
            for h in range(len(g))]


def required_stock(d: Sequence[F], b: F) -> F:
    # Worst interval deficit, not just worst prefix. Brute force, independent
    # of the inventory simulation below.
    return max([F(0)] + [sum(d[i:j], F(0))-b*(j-i)
                        for i in range(len(d)) for j in range(i+1, len(d)+1)])


def simulate(d: Sequence[F], b: F, e: F) -> bool:
    stock = e
    for demand in d:
        stock = min(e, stock+b-demand)
        if stock < 0:
            return False
    return True


def frontier(g: Sequence[F], c: F, b: F, e: F, h: int) -> F:
    caps = [c / sum(g, F(0))]
    q = F(0)
    for n, tail in enumerate(tails(g)[h:], 1):
        q += tail
        if q:
            caps.append((e+b*n)/q)
    return min(caps)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('validation.json'))
    args = parser.parse_args()
    kernels = [tuple(map(F, v)) for v in
               [(1,), (1,1,1,1), (0,2), (2,0,0,1), (1,2,0,1,2)]]
    kernels.append((F(1),F(1,2),F(1,4),F(1,8),F(1,16)))
    schedules = [tuple(v) for p in range(1,5)
                 for v in product((F(0), F(1,2), F(1)), repeat=p)]
    counts = dict(periodic_schedules=len(schedules), kernels=len(kernels),
                  phase_average_identities=0, resource_frontier_cases=0,
                  inventory_exactness_cases=0, constant_attainment_cases=0,
                  continuous_triangle_cases=0)
    for g in kernels:
        tg = tails(g)
        for u in schedules:
            mean = sum(u, F(0))/len(u)
            ds = [residual(g,u,p) for p in range(len(u))]
            c = max(d[0] for d in ds)
            assert c >= mean*sum(g,F(0))
            for j in range(len(g)):
                assert sum((d[j] for d in ds),F(0))/len(ds) == mean*tg[j]
                counts['phase_average_identities'] += 1
            for h in range(len(g)+1):
                for b in (F(0),F(1,2),F(2)):
                    demands = [d[h:] for d in ds]
                    requirements = [required_stock(d,b) for d in demands]
                    e = max(requirements)
                    for d, req in zip(demands,requirements):
                        assert simulate(d,b,req)
                        if req:
                            assert not simulate(d,b,req/2)
                        counts['inventory_exactness_cases'] += 1
                    floor = sum((max(F(0),mean*t-b) for t in tg[h:]),F(0))
                    assert e >= floor
                    cap = frontier(g,c,b,e,h)
                    assert mean <= cap
                    # A constant rate at the computed upper bound has nominal
                    # load c or less and needs no more than the given stock.
                    dc = [cap*t for t in tg[h:]]
                    assert cap*sum(g,F(0)) <= c
                    assert required_stock(dc,b) <= e
                    assert simulate(dc,b,e)
                    counts['resource_frontier_cases'] += 1
                    counts['constant_attainment_cases'] += 1
                    if len(set(u)) == 1:
                        assert e == floor
                        assert cap == mean
    # A delayed commitment refutes a prefix-only criterion for an arbitrary
    # post-cut demand history. Reservoir overflow discards early spare supply.
    delayed = [F(0),F(2)]
    prefix = max([F(0)] + [sum(delayed[:j],F(0))-j for j in (1,2)])
    assert prefix == 0 and required_stock(delayed,F(1)) == 1
    assert not simulate(delayed,F(1),F(0))
    # Independent rational integration of the triangular continuous demand.
    for length in range(1,13):
        for h in range(length+3):
            d = F(max(length-h,0))
            for rate in (F(1,4),F(1,2),F(1),F(2),F(3)):
                for b in (F(0),F(1,4),F(1),F(2),F(5)):
                    crossing = max(F(0), d-b/rate)
                    integrated = rate*(d*crossing-crossing*crossing/2)-b*crossing
                    closed = max(F(0),rate*d-b)**2/(2*rate)
                    assert integrated == closed
                    counts['continuous_triangle_cases'] += 1
    report = {
        'status': 'PASS', 'arithmetic': 'fractions.Fraction (exact rational)',
        'counts': counts,
        'prefix_only_counterexample': {
            'demand': [0,2], 'independent_rate': 1,
            'prefix_deficit_bound': 0, 'true_stock_requirement': 1},
        'scope': 'Finite discrete analogues and rational triangle identities; '
                 'not a proof of the continuous theorem, empirical validation, '
                 'or a novelty certification.'}
    args.output.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2))

if __name__ == '__main__':
    main()
