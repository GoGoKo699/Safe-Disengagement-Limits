# Pass 3: startup under the prescribed normal load

22 September 2026. **Completed for the two-module critical family.**

Question: when upkeep equals spare capacity, does an unreachable optimal fully
ready subset prevent cold warmup into an indefinitely ready state?

Outcome: no. For two positive-loss modules with `s=d_1+d_2`, the cold reachable
set is exactly `sum p_i<=max M_i`, and the best post-warmup deadline is
`min M_i/max(a_i+d_i)`. Reachable partial equilibria can meet a deadline that no
reachable pure ready/cold subset meets, while charging the proven upkeep.
Full initialization of a nonempty subset requires strict excess capacity.

Proof, exact counterexample, and boundaries are in
`research/2026-09-22-startup.md`; exact checks are included in
`analysis/verify_heterogeneous.py`. Warmup does not carry the final deadline
guarantee. Higher-dimensional startup is not solved.

The next justified pass tests the full-rate loss assumption against smooth
state-dependent erosion, keeping independent service and resources explicit.
