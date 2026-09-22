# Pass 8: exact readiness with a bounded final freeze

22 September 2026. This note extends the [spaced-update benchmark](2026-09-22-pass7-finite-updates.md)
by permitting one final frozen serialization stage. It proves an optimum inside
an explicit protocol class. It is not a universal optimum over replication,
logging, or handover architectures, and it makes no novelty claim.
The [companion pipeline-policy note](2026-09-22-pass8-pipeline-policy.md) provides
the separate interpretation and accounting of positive propagation and response
slack.

## 1. Model, policy class, and the meaning of `B`

Retain one versioned service record with copy work `M>0`, spare source rate
`s>0`, full-copy time `L=M/s`, and atomic whole-version updates separated by
at least `Delta>L`. Time zero is a verified update with preparation `p=0` and
age `a=0`. Future updates, including their possible nonarrival, are unknown;
update detection and the age observation are immediate.

During normal operation the source continues its prescribed mutable essential
service. An update resets all useful preparation of the current version to
zero. Between updates, allocated copying rate `v>=0` increases preparation up
to `M`; optional throughput `u>=0` obeys `u+v<=s`. No normal-mode freeze is
allowed. As before, actual removal is a counterfactual request along this
normal deployment, not a repeated shutdown/restart cycle.

After a request, a deterministic causal policy may copy at any rate at most
`s` while continuing mutable source service. It may then invoke **one
irreversible final freeze**:

- Freeze stops all source-owned mutations. New operations are placed in an
  independently provisioned queue and resolved at the receiver under the
  explicitly agreed service contract.
- The current frozen version and all required old obligations must be
  serialized completely before the source departs. Later incoming overwrites
  cannot be used to skip this required serialization within the protocol class.
- Let `B` satisfy `0<=B<=L`. Freeze is admissible exactly when the remaining
  serialization work can be completed at rate `s` in at most `B`. Equivalently,
  `(M-p)/s<=B` at the freeze instant. It must actually finish that final
  serialization within `B`; running at rate `s` is always permitted.
- There are no additional freezes, temporary source-service pauses, alternate
  source-independent logs supplying the missing version, or hidden paths that
  bypass the required copy work. Completion without an earlier freeze is
  treated as a zero-duration freeze at completion.

**`B` is the admitted maximum frozen serialization duration.** It is a protocol
parameter, not automatically a measured service response allowance minus a
network delay. Mapping it into a response budget additionally requires bounds
on propagation, application, queued requests, and fencing. The companion note
must be read before making that interpretation.

If freeze and a new update coincide, freeze takes precedence, and that update
is routed to the independent queue/receiver. In normal mode an update still
resets preparation, including any complete copy. Readiness is required on both
sides of normal update events. The exact equality cases below use this event
order.

The completion objective is **source departure after all required serialization**.
It need not equal the later time when independently transmitted data reaches
the receiver or all queued operations have been answered. Those later times
must fit the separately specified essential-service contract. The present
theorem does not make them disappear.

## 2. Exact post-request exit value

For a request state `(p,a)`, set

$$r=(M-p)/s,\qquad e=\max\{0,\Delta-a\},
\qquad q=(r-B)_+.$$

`q` is the earliest possible freeze time on a continuation with no update:
before that time, at most `s*q` further work can be prepared, so more than
`s*B` would remain. Let `T_B(p,a)` be the least uniform source-departure bound
over the stated causal protocol class.

**Theorem 1.**

$$T_B(p,a)=
\begin{cases}
r,&q\leq e,\\
r+L-B,&q>e.
\end{cases}$$

The second value can be a supremum rather than a realized maximum; the
full-rate strategy below attains it as a uniform guarantee.

**Upper bound.** Copy at rate `s` until the remaining work is at most `s*B`,
freeze immediately, and continue serialization at rate `s` until departure.

If `q<=e`, freeze occurs before any possible update or at the same instant as
the earliest update. Freeze priority prevents that tied update from resetting
the frozen version. Total serialization takes `r`, including the final stage.

If `q>e`, an update may occur at some time `theta<q`. If none does, departure
takes `r`. After the first reset, the strategy reaches admissible freeze after
`L-B` additional time and departs after `L`. Since `L-B<=L<Delta`, no further
update can arrive before that freeze. Source departure is therefore
`theta+L<q+L=r+L-B`. Updates after the freeze enter the independent queue and
do not invalidate frozen work. This proves the claimed upper bound.

**Lower bound over arbitrary causal schedules and freeze decisions.** On a
continuation with no update, every policy needs at least `r` time to serialize
the missing work. This proves optimality when `q<=e`.

Suppose `q>e`. Any policy with a finite guarantee has a first freeze time `t_f`
along its no-update continuation, counting completion as freeze if needed.
The admissibility rule forces `t_f>=q`. Choose the first update at
`t_f-epsilon`, where positive `epsilon` is small enough that this time exceeds
`e`. By causality, until that update the policy follows exactly its no-update
history, so it has not frozen. The update resets preparation to zero. Choose
no further updates. A complete new `M` units must now be serialized; even an
adaptive policy requires at least `L` additional time before departure.
Consequently its exit time is at least

$$t_f-\epsilon+L\geq q-\epsilon+L.$$

Letting `epsilon` tend to zero shows that no uniform bound smaller than
`q+L=r+L-B` is possible. A policy that never freezes/completes on the no-update
history has no finite uniform guarantee. This proves the all-policy lower
bound inside the specified class.

The argument does not assume a fixed pre-request schedule or a predicted next
update. It uses the first freeze on a counterfactual no-update history to
construct an admissible adverse history for each deterministic policy.

## 3. Exact normal readiness threshold

Immediately after an update, a full `M` units must still be serialized before
departure. Hence `H<L` is infeasible from the stated initialization and across
arbitrary normal updates, for every permitted `B`.

If `H>=2L-B`, zero preparation is sufficient at all ages by Theorem 1, so no
normal copying is required. This includes `B=L`, for which the threshold is
`H=L`: freeze immediately and serialize the whole version.

For the nontrivial region

$$L\leq H<2L-B,$$

define

$$h=H-L+B\in[B,L),\qquad K=M-sh=2M-sH-sB>0.$$

The no-reset branch of Theorem 1 is feasible exactly when `q<=e`, equivalently
`r<=e+B`; its exit time is at most `L<=H`. The other branch meets the deadline
exactly when `r<=h`. Taking their union gives the exact readiness condition

$$r\leq\max(e+B,h).$$

Since `h>=B`, this is equivalent to

$$p\geq p_{H,B}(a):=
\max\{0,M-s\max(\Delta-a+B,h)\}.$$

The threshold is zero until age

$$A=\Delta+B-L,$$

then rises at rate `s`, and reaches the plateau `K` at age

$$D=\Delta+L-H.$$

In this region `0<A<D<=Delta` and `D-A=K/s`. At each actual update,
preparation and the threshold both reset to zero. At `H=L`, `D=Delta`; the
normal pre-update limit is required even when the update arrives exactly at
that age.

The same preparation can again have distinct age-dependent values. For
`B<L`,

$$T_B(0,0)=L,\qquad
T_B(0,a)=2L-B\quad(a\geq\Delta).$$

At `B=L` these values coincide. The ability to freeze the whole record removes
this particular timing dependence by changing the permitted service protocol.

## 4. Exact guaranteed long-run optional throughput

Use the same objective as pass 7: maximize over uniformly ready deterministic
normal policies the worst-update-history long-run lower average of optional
throughput. The update histories include periodic minimum-spacing updates,
larger gaps, and no future update.

**Theorem 2.**

$$U_{*,B}(H)=
\begin{cases}
\text{infeasible},&0\leq H<L,\\
s-\dfrac{2M-sH-sB}{\Delta},&L\leq H<2L-B,\\
s,&H\geq2L-B.
\end{cases}$$

Equivalently, for `H>=L` the recurring copy cost is

$$c_B(H)=\frac{(2M-sH-sB)_+}{\Delta}.$$

**Attaining policy.** On each normal update interval, set `v=0` until age `A`,
then `v=s` on ages `[A,D]`, then `v=0` until the next update; set `u=s-v`.
Its preparation is

$$p(a)=s\min\{\max(a-A,0),D-A\},$$

exactly the readiness threshold. Since `D<=Delta`, every ramp finishes before
the next possible update, or meets it at the endpoint. On a request use
Theorem 1's full-rate copy-then-freeze policy.

Every completed update interval costs exactly `K`, and a final partial
interval costs at most `K`. Thus for every duration `t`,

$$\int_0^t v(r)\,dr\leq
K\bigl(\lfloor t/\Delta\rfloor+1\bigr),$$

and

$$\int_0^t u(r)\,dr\geq(s-K/\Delta)t-K.$$

This establishes the stated guaranteed long-run lower average. It also shows
that a final update followed by an indefinitely quiet interval incurs only
one final finite maintenance cost.

**Matching bound for arbitrary ready policies.** Choose periodic updates with
period `Delta`. Every interval starts from zero preparation. The exact
readiness threshold requires `K` preparation by age `D<Delta` when `H>L`.
When `H=L`, its limit as age approaches `Delta` is `K`; bounded copy rate and
continuity between updates still require at least `K` integrated work in that
interval. Wasted work can only increase copying expenditure. Every periodic
interval therefore consumes at least `K`, and long-run optional upper average
is at most `s-K/Delta`. This upper-bounds the worst-history lower average and
matches the construction.

The result optimizes mean optional throughput. The attaining policy spends
all spare capacity on copying during its ramp; it does not provide a positive
pointwise optional-service floor.

## 5. Exact reduction of normal maintenance to one sporadic task

In the nontrivial region, normalize copying capacity to one and associate a
job with each update. Its execution requirement, relative deadline, and
minimum interarrival time are

$$C=K/s=2L-H-B,\qquad
D=\Delta+L-H,\qquad T=\Delta.$$

They satisfy `0<C<=D<=T`, with latest start

$$D-C=\Delta+B-L=A.$$

This is an exact normal-maintenance feasibility correspondence. Readiness
requires finishing at least `K` work by age `D`, so each ready policy completes
the associated job. Conversely, a policy that finishes that work by `D` cannot
at an earlier age `a<=D` have less than `K-s(D-a)` useful preparation: there
would be insufficient remaining capacity to meet the deadline. After `D`,
preparation is durable until the next update. Since no update occurs before
`T>=D`, jobs are not erased before their deadline. Hence meeting these per-job
deadlines enforces exactly the readiness threshold, up to useless extra work.

The recurring utilization is therefore the familiar `C/T`, multiplied by `s`
to return to source resource units. The all-request-time interpretation and
the exit oracle derive the task parameters, but the subsequent single-task
utilization calculation is not a new scheduling principle. The prior-art
comparison in [pass 7](2026-09-22-pass7-prior-art.md) applies to this reduction
with the changed execution requirement and deadline.

## 6. Initialization and boundary conditions

- `B=0` recovers pass 7 exactly: freezing can occur only at completed copy.
- `B=L` allows immediate freeze even from cold. Source departure takes `L`
  from reset; zero normal copying suffices for every `H>=L`.
- At `H=L`, recurring copy cost is `(M-sB)/Delta`. A normal state on the ramp
  may reach the freeze threshold exactly when the earliest new update arrives;
  freeze-before-update is therefore a substantive equality convention.
- At `H=2L-B`, no normal copying is needed. The worst-case exit may approach
  this value without attaining it; a least uniform upper bound is sufficient.
- For an initially cold state of arbitrary known age, in the nontrivial
  deadline range, readiness holds exactly when `a_0<=Delta+B-L`. Verified
  update time zero satisfies this. Otherwise a paid warmup or a different
  initial contract is necessary.
- `Delta>L`, whole-version invalidation, immediate event observation,
  fractional copying, and the stated one-freeze protocol remain assumptions.
  Alternative event ordering, shorter update spacing, several freezes, or
  alternative independent logs are not included in this theorem.
- Increasing `B` spends a different service resource: greater permissible
  final deferral of mutable source service. The saved recurring bandwidth does
  not establish a Pareto improvement without accounting for that deferral.

## 7. Prior art and interpretation

Bounded final stop-and-copy is established. Kherbache, Hermenier, and Madelaine,
_Scheduling Live Migration of Virtual Machines_,
[author-hosted primary paper](https://www.btrplace.org/pubs/kherbache-tcc17.pdf),
§§3.3.1 and 3.3.3, describes ending pre-copy once remaining dirty pages fit a
downtime allowance. Equation (3) explicitly contains `D*bw(m)` as the volume
sent after suspension. Those complete subsections and the equation were read
in this pass. Their model is not the whole-version, minimum-spacing adversary
used here, but the principle of allowing residual work up to bandwidth times
permitted stop duration is prior art. It must not be presented as a new S1
mechanism. No measurements or implementation were reproduced.

The positive-pipeline interpretation additionally requires the
[companion policy note](2026-09-22-pass8-pipeline-policy.md). In particular,
an application response allowance is not automatically equal to `B` plus a
propagation delay: independent admission, pending obligations, queue capacity,
service time, and certified ownership change must fit that budget. Merely
having a large nominal response allowance does not authorize an earlier freeze
outside the protocol's admitted maximum `B`.

This pass closes an explicit policy-class omission: if bounded final freezing
is permitted, the zero-freeze frontier is generally not optimal in that larger
class. The new frontier and its exact sporadic-task reduction are benchmark
findings, not established paper novelty. A proposed submission must distinguish
its contribution from both known stop-and-copy protocols and standard deadline
feasibility/utilization arguments.
