# Pass 7: an exact readiness frontier with spaced atomic version updates

22 September 2026. This is a complete analytical benchmark for a restricted
hybrid model. It replaces continuous erosion by finitely separated version
events, while keeping fractional transmission and an ideal instantaneous final
fence. It does not solve the positive-propagation interface gap identified in
[pass 6](2026-09-22-pass6-interface.md), establish publication novelty, or claim
an implemented service.

## 1. Model and guarantee

There is one service record with fixed transfer work `M>0`. A cooperative source
continues the prescribed essential service while preparing an independently
provisioned receiver. The spare shared preparation/optional-work rate is `s>0`.
Write

$$L=M/s.$$

An update replaces the record's version and invalidates **all** preparation of
the previous version, including a complete previously current copy. Preparation
`p` is reset to zero. This is an explicit whole-version reset assumption, not a
claim about append-only logs or arbitrary record modifications. Between updates,
useful preparation is durable and satisfies the reflected dynamics

$$p'=v\quad\text{for }0\leq p<M,\qquad p'=0\quad\text{at }p=M,$$

where `v>=0` is allocated copying work. Work allocated at `p=M` is wasted. During
normal operation `u>=0` is optional throughput and

$$u+v\leq s.$$

Updates occur at times `t_0=0<t_1<t_2<...`, with

$$t_{j+1}-t_j\geq\Delta>L.$$

The sequence may be finite: no further update is an admissible continuation.
The source detects updates immediately and knows the age
`a=t-max{t_j:t_j<=t}`. It knows neither the next update time nor whether there
will be another. At the verified initial update, `p(0)=0` and `a(0)=0`.

Policies are deterministic and causal. They must preserve a removal deadline
at every normal operating time against every admissible future update sequence.
Optional work stops immediately at a request and creates no continuing
obligation. The source may then use rate `s` for copying while continuing
essential service. Once the current version is completely available at the
receiver, an ideal atomic ownership fence ends source dependence.

**Simultaneous-event convention.** If a requested handover's final copy and an
update coincide, completed handover/fencing occurs first and the same-time new
mutation is routed to the receiver. A normal-mode copy reaching `M` without a
handover request does not fence ownership: an update still resets it to zero.
The normal readiness requirement is checked on both sides of update events.
The exact exit formula below uses this ordering, particularly at equality.

Positive propagation, packet serialization details beyond the fluid copying
rate, update detection latency, and ownership-protocol delay are outside this
benchmark. Receiver computation, storage, traffic, and its ability to continue
essential service are separately provisioned. None is inferred from the
scalar preparation variable.

## 2. Exact post-request value from an age-labelled state

For a request state `(p,a)`, define the remaining full-rate copy time and the
earliest permitted next-update delay by

$$r=(M-p)/s,\qquad e=\max\{0,\Delta-a\}.$$

Let `T(p,a)` be the smallest uniform completion bound achievable over all
admissible future updates, allowing any causal preemptive/adaptive allocation.

**Theorem 1.**

$$T(p,a)=
\begin{cases}
r,&r\leq e,\\
r+L,&r>e.
\end{cases}$$

In the second case, the value can be a supremum of realized exit times rather
than an attained worst-case duration. It is nevertheless an attained uniform
bound: copying continuously at rate `s` guarantees completion within it.

**Upper bound.** Copy at rate `s`. If `r<=e`, the current version is complete
before any permissible update, or simultaneously with the earliest one; the
completion-priority convention covers the latter case. Exit takes `r`.

If `r>e`, either no update occurs before completion and exit takes `r`, or the
first update occurs at some `theta<r`, resetting preparation. The new version
then takes exactly `L` to copy. A further update cannot occur for at least
`Delta>L`, so it cannot interrupt this second copy. Exit therefore takes
`theta+L<r+L` in the interrupted case. The displayed uniform upper bound follows.

**Lower bound over all causal policies.** With no future update, no policy can
complete in less than `r`, proving the first case's optimality. For the second
case, consider any policy that claims a finite uniform completion bound, and
let `t_c>=r` be its completion time along the continuation with no future
update. Choose a first update just before `t_c`, at `t_c-epsilon`, with positive
`epsilon` small enough that this time exceeds `e`. Causality makes the policy's
behavior before that update identical to its no-update behavior; it has not
yet completed. The reset leaves a full `M` units to transmit, requiring at
least `L` additional time under any allocation. Choose no further updates.
Its exit time is therefore at least

$$t_c-\epsilon+L\geq r-\epsilon+L.$$

As `epsilon` tends to zero, no smaller uniform bound than `r+L` is possible.
This is an allowed adversarial update sequence for each deterministic policy;
it does not require the policy to know future updates. A policy that does not
complete on the no-update continuation already fails a finite guarantee.

## 3. Preparation alone is no longer a sufficient readiness state

The same amount of preparation has different exact exit values at different
ages:

$$T(0,0)=L,\qquad T(0,a)=2L\quad\text{for }a\geq\Delta.$$

Immediately after a known update, the interval before another update is long
enough to finish one complete copy. For an old version, an update may arrive
just before that copy would finish and force another full copy.

For `L<=H<2L`, a certificate depending only on `p` cannot both certify every
physically `H`-ready state and remain sound over unrestricted ages: it would
have to accept and reject `p=0` in these two states. This statement concerns
certification of the full state set. It is not an impossibility theorem for
every policy that chooses not to track age; such policies may maintain more
preparation or use a more conservative certificate.

The support-only reasoning and a static threshold in preparation from the
continuous-erosion model therefore cannot be transferred unchanged. The timing
information supplied by a verified update is part of readiness in this model.

## 4. Exact age-dependent readiness constraint

If `H<L`, a cold state immediately after an update cannot meet the deadline.
Consequently the required uniform deployment is impossible from the specified
cold initialization and across arbitrary later reset events.

If `H>=2L`, every state is ready: `r<=L` and Theorem 1 gives `T<=2L`. No normal
copying is needed and optional rate `s` is attainable.

Now suppose

$$L\leq H<2L,\qquad h=H-L\in[0,L).$$

In Theorem 1's first branch, `r<=e` suffices since `r<=L<=H`. In its second
branch, the deadline requires `r+L<=H`, equivalently `r<=h`. Thus the exact
union of the two admissible branches is

$$r\leq\max\{e,h\}.$$

Equivalently, uniform readiness at the current age requires and is implied by

$$p\geq p_H(a):=\max\{0,M-s\max(\Delta-a,h)\}.$$

The separate `max(0,Delta-a)` inside `e` is redundant here because `h>=0`.
The threshold is zero until age `Delta-L`, then rises with slope `s`, and
becomes constant at age `Delta-h`. Its plateau value is

$$K=M-sh=2M-sH.$$

Here `0<K<=M`. At `H=L`, the threshold approaches full preparation by age
`Delta`; at every actual update it resets to zero together with preparation,
because the newly known update age resets to zero.

## 5. Exact sustainable optional throughput

Define the best guaranteed throughput as the supremum over uniformly ready
normal policies of their worst-history long-run lower average:

$$U_*(H)=\sup_\pi\inf_{\{t_j\}}
\liminf_{t\to\infty}\frac1t\int_0^t u_\pi(r)\,dr.$$

The infimum includes finite update sequences and the sequence with no update
after zero. The guarantee is counterfactual along normal operation; an actual
request ends that normal deployment.

**Theorem 2.**

$$U_*(H)=
\begin{cases}
\text{infeasible},&0\leq H<L,\\
s-\dfrac{2M-sH}{\Delta},&L\leq H<2L,\\
s,&H\geq2L.
\end{cases}$$

The exact worst-case recurring copy cost on the middle interval is
`K/Delta`. It decreases linearly with `H` and matches zero at `H=2L`.

**Attaining normal policy.** After each detected update, copy nothing until
age `Delta-L`. Then allocate all `s` to copying until age `Delta-h`, reaching
`K`; allocate zero copying thereafter until the next update. Equivalently,

$$p(a)=s\min\{\max(a-(\Delta-L),0),L-h\}.$$

This is exactly the threshold `p_H(a)`. Set `u=s-v`. Since no update can occur
before age `Delta`, the ramp completes before the next update, or at it when
`H=L`. Every normal state before and after an update is ready. On a request,
the full-rate exit policy from Theorem 1 supplies the promised deadline.

The work used in each completed update interval is exactly `K`; the final
partial interval uses at most `K`. There are at most `floor(t/Delta)` further
updates by time `t`, so cumulative copying obeys

$$\int_0^t v(r)\,dr\leq K\bigl(\lfloor t/\Delta\rfloor+1\bigr).$$

This gives

$$\int_0^t u(r)\,dr\geq
\left(s-\frac K\Delta\right)t-K,$$

and proves a guaranteed long-run lower average of at least `s-K/Delta` for
every update sequence. If updates stop, the policy pays only one final finite
copying cost and thereafter has optional rate `s`.

**Matching lower bound on copying for every ready policy.** Choose periodic
updates `t_j=j*Delta`. Each interval starts with preparation zero. Readiness
requires reaching `K` by age `Delta-h` when `h>0`, so at least `K` copying
work is necessary in each complete interval. When `h=0`, readiness on ages
approaching `Delta` from below requires preparation approaching `M=K`; by
continuity between updates, integrated copying in that interval is at least
`M`. Wasted allocation cannot reduce this requirement.

Thus every uniformly ready policy uses at least `K` per periodic interval and
has long-run upper optional average at most `s-K/Delta` on that allowed
history. This also upper-bounds the worst-history lower average in the
definition of `U_*`, completing the proof. No enumeration or simulation is
needed for the all-policy quantifier.

The condition `Delta>L` ensures `K/Delta<=M/Delta<s`, so the attaining normal
policy's average optional throughput is positive even at the smallest feasible
deadline. Its instantaneous optional rate is zero during the preparation ramp;
the theorem optimizes a long-run average, not a pointwise optional-service floor.

## 6. Initialization, endpoints, and scope

- **Cold initialization is constrained.** For `L<=H<2L`, a cold initial state
  of known age `a_0` is already ready exactly when `a_0<=Delta-L`. Knowing an
  arbitrary old age is not sufficient. The theorem starts at the verified
  update at time zero, so its deadline guarantee needs no free initial copy.
  A different initial state may require explicitly paid warmup before the
  guarantee starts.
- **Update age is observable immediately.** Detection delay changes the state
  information and must be modeled; it is not charged implicitly to `s`.
- **`H=L` depends on exact event semantics.** The displayed exit formula accepts
  `r=e`, because final handover takes precedence over a same-time update. With
  a different priority, this state value and the delayed-ramp attainment can
  change. Alternative event semantics are not resolved here.
- **`H=2L` needs no limit policy.** Set normal copying to zero. The supremum
  bound of two copies is itself a valid uniform deadline, although individual
  adversarial exit histories may only approach it.
- **Whole-version resets are substantive.** Partial updates, useful surviving
  blocks, independent logs, or predictable next values change the model.
- **`Delta>L` is substantive.** Repeated resets cannot interrupt the second
  full-speed copy here. The critical/subcritical spacing cases are not covered.
- **This is not a fully packetized implementation.** Update events are atomic,
  while copy progress remains divisible. Positive propagation, finite fences,
  and response-latency accounting remain obligations from pass 6.

## 7. Why a mean dirty-rate substitution is not valid

The quantity `d_bar=M/Delta` is the maximum long-run reset payload per time in
the periodic case. It is not a pointwise continuous loss-rate bound. Atomic
resets allow bursts of size `M` but impose a quiet interval; the fixed-rate
fluid model allows a different set of histories without that event spacing.
Neither model is obtained by simply assigning the other's average rate.

For `M=s=1`, the discrepancy occurs in both directions:

| Spacing and deadline | Finite-update exact cost | Fixed-rate benchmark with `d=d_bar` |
|---|---:|---:|
| `Delta=3`, `H=7/4` | `1/12` | `0`, since its cold exit time is `3/2` |
| `Delta=3/2`, `H=2` | `0` | `2/3`, since its cold exit time is `3` |

These are comparisons of distinct uncertainty sets. They do not contradict the
fixed-rate theorem. They demonstrate why average update traffic alone does not
justify importing its readiness law into a discrete version-update interface.

## 8. Scientific status and prior-art task

The exact exit value, age-dependent readiness set, and average frontier have
complete proofs under the specified hybrid model. The strongest conceptual
lesson is that timing knowledge can be part of readiness: two equally cold
states have different guaranteed exits. The linear recurring cost is an
elementary per-cycle workload bound once the readiness threshold is known.

The existing [literature audit](2026-09-22-literature-audit.md) and
[interface comparison](2026-09-22-pass6-interface.md) remain required reading.
A dedicated [pass-7 prior-art comparison](2026-09-22-pass7-prior-art.md) examines
deterministic freshness, restartable copying, spaced interruptions, and
deadline/utilization results; its actual inspection status governs that audit.
No novelty claim is made. The next task is to determine whether this benchmark
has a useful unmatched theorem or is a prior-art reduction, before extending it
or selecting it as a paper's central result.
