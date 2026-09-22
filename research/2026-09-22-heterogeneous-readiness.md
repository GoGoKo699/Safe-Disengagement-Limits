# Heterogeneous readiness: exact recurring cost

22 September 2026. Research pass 1, starting from
`dbafc04df679ce5b5d22a8c9654c85dbea234cb0` on `main`.

**Status:** analytical result within the archived fixed-rate model, now with
heterogeneous modules. The scheduling problem is solved by a finite subset
recurrence in the [companion proof](2026-09-22-heterogeneous-scheduling.md).
Neither a validated application nor publication novelty is established.

## 1. Contract and quantifiers

Let `N={1,...,n}`, with `n>=1`, finite `M_i>0`, `a_i>0`, `d_i>=0`, spare
capacity `s>=0`, and finite deadline `H>=0`. Normal capacity is
`P=s+sum_i a_i`. Before a request all modules remain on the primary, consuming
the prescribed load `sum_i a_i`. Preparation and immediately cancellable
optional work satisfy `sum_i v_i(t)+u(t)<=s`, with nonnegative allocations.

Each preparation `p_i` lies in `[0,M_i]` and follows the reflected dynamics of
active checkpoint section 2, with its own `M_i,d_i`. The uncertainty set permits
**every simultaneous** measurable collection `0<=rho_i(t)<=d_i`; in particular,
all components can equal their maxima forever. Bounded measurable causal
allocations and absolutely continuous reflected states are admitted. There are
no impulses, free state transfers between modules, or preparatory cutovers in
normal mode. The maximum-invalidation history suffices for lower bounds.

On request, optional work stops; every fully prepared module can transfer
instantaneously. If the transferred set is `S`, available preparation capacity
is `b(S)=s+sum_{i in S}a_i`. Unfinished modules retain their prescribed load
and update bounds. Completion removes their dependence on the primary and
their subsequent invalidation from this accounting.

Independent destination service, state sufficiency, direct communications,
atomic ownership transfer, and absence of intermodule barriers are assumptions.
The receiver's infrastructure and paid initial preparation are outside `P`.
The guarantee concerns cooperative removal, with a reliable primary during
grace, not sudden failure. See the [operational audit](2026-09-22-literature-audit.md).

Let `R_H` consist of states from which one causal exit policy meets the deadline
for every admissible future update history. A normal policy must keep `p(t)`
in `R_H` at **every** counterfactual request time, for every allowed preceding
history. The request need not actually occur. We optimize a guaranteed optional
long-run rate over indefinitely continuing normal deployments, allowing a
suitable paid initial state. All upper bounds below hold on one common allowed
history; a matching policy attains the rate for all histories.

## 2. Exact post-request computation

Write `F(S)` for optimal worst-case exit time when precisely `S` is fully ready
and the rest is cold. Transfer `S` at time zero. The companion theorem proves

```
F(N) = 0
F(S) = min over i not in S with b(S)>d_i of
       { M_i/(b(S)-d_i) + F(S union {i}) }.
```

An empty minimum is infinity. This is an exact minimum over the full
parallel/preemptive policy class, and a finite value is attained by a serial
permutation. Thus `F(S)<=H` includes the deadline endpoint without assuming
that an abstract infimum is attained. Computing all values takes `O(n*2^n)`
arithmetic operations and `O(2^n)` storage; this is not a polynomial-time or
bit-complexity claim. Rational inputs admit exact arithmetic.

The homogeneous checkpoint is recovered by `M_i=M, a_i=a, d_i=d`. No claim of
serial optimality from **arbitrary partial** initial states is made here.

## 3. Support domination

For a request state `p`, let `S(p)={i:p_i>0}`. Replacing every positive component
by `M_i` and immediately transferring these modules cannot worsen exit:
unfinished outside modules start at the same zero state, additional capacity is
available, and all work on modules in `S(p)` disappears. Independence and
nonnegative capacity releases are essential to this comparison. One can replay
the original exit policy on a virtual copy and ignore its allocations to the
gratuitously transferred modules, transferring other modules earlier if ready.

Consequently,

```
p in R_H  implies  F(S(p)) <= H.
```

This implication is one-way. Positive but tiny preparations need not be ready
for the deadline.

## 4. Exact upkeep and feasibility

Define

```
D(H) = min { sum_{i in S} d_i : S subset N, F(S)<=H }.
```

The minimum exists because there are finitely many sets and `F(N)=0`.
For every robust normal policy, on the simultaneous maximum-invalidation
history, every `T>0` obeys

```
integral_0^T u(t) dt <= (s-D(H))*T + Q(0)-Q(T),
Q(t) = sum_i p_i(t).
```

**Proof.** At positive interior states, `p_i'=v_i-d_i`; at `M_i` the derivative
is at most this quantity; at zero the derivative is at most `v_i`.
Therefore, almost everywhere,

```
Q' <= sum_i v_i - sum_{i:p_i>0} d_i <= s-u-D(H).
```

The last inequality uses support domination at each request time. Integration
proves the finite-horizon claim. Since `0<=Q<=sum_i M_i`, division by `T` gives
`limsup average(u)<=s-D(H)` without assuming a time average exists. The argument
covers rotation, parallel refresh, partial preparation, and bursty allocations.

If `D(H)<=s`, choose a minimizing set `S*`, initialize it fully, keep it ready
with allocations `v_i=d_i` on `S*` and zero outside, and use
`u=s-D(H)`. Smaller actual losses cannot reduce its preparedness. At a request,
the attaining serial schedule for `F(S*)` meets the deadline. Thus the exact
maximum guaranteed optional rate is `s-D(H)`.

If `D(H)>s`, an indefinite ready deployment is impossible, even with `u=0`.
Any ready interval under maximum invalidation has
`T<=Q(0)/(D(H)-s)`. This is an upper bound on duration, not an attained lifetime.
Negative throughput is never interpreted as feasible.

## 5. Boundary and initialization checks

- `H=0` requires every module fully ready, so `D(0)=sum_i d_i`.
- If cold exit meets `H`, then `D(H)=0`; this does not require initialization.
- Zero-loss modules may be initialized once without recurring cost. A zero
  upkeep result does not assert zero initialization cost.
- `s=0` is allowed. Positive upkeep is then infeasible; a ready zero-loss set
  may still release capacity on request. With no initial ready modules and
  `s=0`, no cold module can make progress, even when `d_i=0`.
- The attaining construction starts from a paid chosen state, not from cold
  operation under the prescribed full load. Budget equality can block a cold
  ramp. No all-request-time guarantee is asserted during an unready ramp.
- `F` depends on preparation sizes and released capacities; `D` is not obtained
  by sorting upkeep costs alone. Deadline endpoints use exact comparisons.
- A constraint on total invalidation, spatial locality of writes, a receiver
  bottleneck, positive cutover time, or state-dependent loss changes the model.

## 6. What this pass establishes

The proposed heterogeneous reduction is valid and no longer contains an
uncharacterized exit oracle. The structural work is the scheduling lower bound;
the support and averaging argument is elementary. It is inappropriate to
promote heterogeneity or the no-rotation principle alone into a novelty claim.

The next pass tests whether the exponential recurrence collapses to a simple
ordering rule, and checks the precise relation to established scheduling and
dissipativity results. The [ordering note](2026-09-22-ordering-limits.md) records
the resulting counterexamples; the [prior-art reduction](2026-09-22-dissipativity.md)
records the averaging overlap. Verification is separate from the proof.
