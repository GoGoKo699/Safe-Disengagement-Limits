# Pass 8: positive propagation delay and the admissible handoff policy

22 September 2026. This operational companion to the finite-update benchmark
separates three questions: when information is independent of the source, when
the receiver can answer, and whether the protocol may freeze the source before
copying finishes. The central negative finding is that a positive-delay pipeline
does not justify forbidding earlier freeze. With sufficient contracted response
slack, early freeze removes the benchmark's restart penalty and can eliminate
its recurring preparation cost.

No implemented protocol or new general distributed-systems theorem is claimed.
The source/receiver fence remains an explicitly idealized control primitive.

## 1. A narrow interface and what its resources must include

Use the single full-replacement register of
[pass 7](2026-09-22-pass7-finite-updates.md), with transfer work `M`, spare source
serialization rate `s`, `L=M/s`, and source update spacing `Delta>L`.
An admitted operation is either a read of the register or an atomic full-version
overwrite. The service history must be linearizable: completed writes cannot
be revoked, and reads must correspond to a legal operation order respecting
real-time precedence.

The following are explicit interface assumptions, not deductions from `M/s`:

- A reliable FIFO pipe is independent of the source after injection. Each
  injected unit arrives exactly `delta>0` later, with no source retransmission,
  acknowledgment processing, power, proxying, or instruction needed thereafter.
  Data merely queued in removable source memory or its source-dependent NIC does
  not count as injected.
- The receiver has independent computation, power, state storage, client access,
  and bounded request queues. A bound `t_apply` must cover the processing and
  response work relevant to every admitted queued request, including queue
  interference. A per-request execution bound without a queue bound is
  insufficient.
- An independently supported ingress/ownership fence gives a total order to the
  old committed prefix and subsequent operations. After the fence, new admitted
  requests and their complete payloads are retained independently. The source
  cannot acknowledge a new exclusive mutation of the frozen prefix.
- The clean construction below initially assumes no uncompleted source-owned
  obligations at the fence. The extension to preexisting pending requests needs
  additional accounting, given in section 5. They are never silently dropped.
- Versions and chunks are identifiable, stale chunks are discarded, and all
  required per-version transmission work is charged to `M`. The copy itself
  remains a divisible-work idealization; real packet overhead or indivisible
  chunks may change exact endpoints.

Injection rate at most `s` means at most `s*delta` units of copying data are in
flight. Their independent buffering is paid. Receiver storage must include the
current reconstruction, tags, and the admitted-operation queue. Positive update
spacing bounds the number of different version tags simultaneously in the pipe;
unbounded historical logging is not a free extra resource.

There is also a crucial information boundary: pre-fence overwrite payloads must
not already be available in a sufficient independent log for free. If an ingress
retains every full replacement value outside the source, then that log already
contains the service state, and the premise that copying `M` work is necessary
must be reconsidered. Clients are not assumed to be an available replay service.

## 2. Conditional simulation of the copy-then-fence benchmark

First impose the protocol restriction that source-owned updates continue until
the *current* version is completely injected; only then may ownership freeze
and move. Interpret `p` as useful current-version work already injected into
independent resources, whether received or still in flight. It is not exact
receiver-local freshness.

An overwrite still resets useful `p` to zero. Old injected chunks physically
survive, but an arbitrary replacement can make them irrelevant. Between updates,
copying at rate `v` grows useful injection at rate `v`, exactly as in pass 7.
At `p=M`, every unit needed for the committed current version is independent
of the source. The ideal fence commits, the source may depart, and the receiver
has the entire version no later than `delta` afterward.

Under the declared queue bound and

    R >= delta + t_apply,

newly admitted post-fence operations may wait for assembly and still meet their
original response allowance `R`. The receiver applies them in fence order.
Thus, within this copy-then-fence policy class and the stated obligation boundary,
pass 7's exact **source-departure** times and recurring-cost formula are unchanged.
For an all-request-time interpretation, that obligation boundary must hold at
every admissible request time; checking only quiescent request states would not
establish the full recurring frontier for a busier service.
Positive `delta` is charged to the response contract and independent resources,
not erased from the accounting. Receiver-ready completion would be a different
deadline objective.

The simultaneous-event convention is retained: if final current-version
injection, a requested fence, and a new overwrite coincide, the fence commits
first and that overwrite belongs to the independently queued new-owner suffix.
A normal-mode copy finishing with no handoff request does not freeze ownership;
a subsequent or same-time source overwrite can still reset it.

This is a conditional simulation of a specified control class. The arbitrary
full-state premise prevents departure before sufficient current information has
crossed the independent boundary: choose no further overwrite and a read of the
unknown state. It does **not** prove that the source must continue accepting
overwrites until that crossing is complete.

## 3. Early freeze is a different admissible control action

The missing alternative is to freeze ownership while some snapshot work is
still at the cooperative source, then finish transmitting that immutable
snapshot. Source departure need not coincide with freeze.

Suppose the service contract instead allows

    R >= L + delta + t_apply,

under the same independent finite-queue provisions. At a removal request use:

1. The ideal fence closes the old source prefix and independently queues every
   newly admitted read and overwrite in a fixed order. The old register is now
   immutable. No new source-local acknowledgment is issued.
2. If `p` useful units of this version were already injected, transmit the
   remaining `M-p` at rate `s`. The source remains present for this work and
   departs after `r=(M-p)/s<=L`.
3. The receiver assembles the frozen version by time `r+delta`. It then applies
   queued operations in order, with the declared `t_apply` response bound.

All pre-fence acknowledged overwrites are represented in the frozen snapshot.
A queued read preceding the first queued overwrite sees that snapshot; a later
read sees the proper subsequent value. Operations are linearized in the chosen
ingress order during receiver execution, within their invocation-response
intervals. Writes received during copying do not alter the frozen old snapshot,
and cannot force its transmission to restart.

The complete payload of a post-fence overwrite is paid independent queue data.
It is not an uncharged pre-fence replica. The construction does not rely on a
future overwrite occurring: a continuation with no further writes is handled by
finishing the old snapshot.

**Exact negative result for the proposed mapping.** At request states satisfying
the stated obligation boundary, if this early-freeze action is allowed, a normal
policy can use `v=0`, `u=s` indefinitely and, upon removal,
freeze and transmit one cold snapshot in time `L`. Its recurring preparation
cost is zero for every source-departure deadline `H>=L`. This reaches the maximum
possible optional rate `s` within the declared resource budget. By contrast,
pass 7's copy-then-fence restriction requires cost `M/Delta` at `H=L` and positive
cost throughout `L<=H<2L`.

These statements concern different admissible transition actions. They are not
a counterexample to pass 7's theorem as defined. They do refute the claim that
adding an independent delayed pipe and bounded response slack automatically
makes pass 7 optimal over all service-preserving handoff protocols. The same
larger `R` can satisfy both protocols, while the early-freeze policy is excluded
only by pass 7's control restriction.

The source never leaves with missing source-only information in this
counterpolicy. It stays for the residual serialization. The improvement comes
from stopping new invalidations, rather than from hiding unfinished work after
departure.

## 4. A bounded final frozen-copy interval

An intermediate protocol can explicitly allow freeze only when residual
serialization time obeys

    r=(M-p)/s <= B,    0<=B<=L.

This is a precise *admissible-action budget*. Independent queuing with
`R>=B+delta+t_apply` certifies that budget under the preceding assumptions.
`B=0` recovers copy-then-fence; `B=L` permits the full early-freeze construction.
The [separate bounded-freeze proof](2026-09-22-pass8-bounded-freeze.md) analyzes the resulting age-dependent
deadline and upkeep problem. This companion does not infer its policy class
solely from an informal mention of downtime.

In particular, reserving an application-time *upper bound* does not prove the
converse that `r>B` violates service. The implementation might process faster,
serve reads from the still-live source, stream sufficient response data before
full assembly, or use another independent information path.

An exact service-derived threshold would need stronger assumptions. For example,
require the first post-freeze read to need the full old register, prohibit
source-assisted responses after freeze, choose no later overwrite, and impose an
unavoidable receiver/output delay `sigma` after the last required unit arrives.
For `r>0`, some required work must still be injected after freeze, so with exact
pipeline delay `delta` its earliest response occurs after `r+delta+sigma`.
At `r=0`, previously injected data may already have arrived, and a full extra
`delta` is not a necessary lower bound. If the positive-residual bounds are
simultaneously attainable, an allowance
`R` forces `r<=R-delta-sigma`. Without those additional hypotheses, `B` should
remain a declared protocol budget rather than a universal consequence of `R`.

## 5. Remaining obligations and scope

**Preexisting requests.** The clean counterpolicy conditions on no outstanding
source-owned operation at freeze. It is not, without more work, an all-operating-
time implementation for a service that allows such operations. One sufficient
extension is independently retaining every pending operation and its status,
including an unambiguous committed-prefix boundary, with maximum prior age `A`.
Transferred pending operations then need their remaining deadline to cover the
new wait; the conservative response allowance is
`R>=A+B+delta+t_apply`. The request/status information and processing must be
paid. An already generated response or non-idempotent effect may require more
state than a register snapshot. If these conditions fail, additional source
drain time must be included; the counterpolicy cannot simply discard old work.

**Response contract.** Independent queuing preserves a preexisting bounded-
response contract only when its actual `R`, admission envelope, and processing
capacity permit the wait. An immediate-response or uninterrupted-computation
requirement cannot be replaced by this looser contract without changing the
problem. Optional throughput does not stand in for essential response service.

**Fence latency.** Both protocols still use an ideal instantaneous certified
ownership primitive. A positive fence latency requires specifying when the old
prefix becomes immutable, which side owns intervening arrivals, what must remain
source-resident, and which messages survive source departure. It cannot be
absorbed into `delta` or `t_apply` without proving the corresponding schedule and
deadline accounting. This note handles positive copy propagation conditionally;
it does not claim to solve distributed ownership transfer.

**Post-departure updates.** Newly admitted overwrites belong to the new-owner
queue and execute there in order. They do not mutate the frozen source prefix.
The spacing assumption concerns externally arriving versions while they are
source-owned; early freeze changes which arrivals can invalidate the source
snapshot. That change is the mathematical reason the restart lower bound no
longer applies.

## 6. Targeted primary-literature comparison

**Kherbache, Hermenier, and Madelaine, _Scheduling Live Migration of Virtual
Machines_.** [Primary full text](https://www.btrplace.org/pubs/kherbache-tcc17.pdf).
Inspected complete sections 3.3.1 and 3.3.3, equations (2)–(5), manuscript
pages 3–5. The pre-copy description switches to suspended transfer once the
remaining dirty state fits the downtime allowance. Equation (3) subtracts
`D*bw(m)` as work reserved for that final phase; equation (5) adds downtime to
migration duration. Thus a residual-work budget equal to bandwidth times an
allowed stopped interval is established migration modeling, not a new S1 idea.
The paper does not supply this note's generic bounded-response queue contract
or prove the spaced-reset all-request-time upkeep theorem.

**Clark et al., _Live Migration of Virtual Machines_, NSDI 2005.**
[Primary full text](https://www.usenix.org/legacy/events/nsdi05/tech/full_papers/clark/clark_html/).
Inspected sections 3.1, 3.3, 5.3, and 6.3. The design separates source suspension,
remaining transfer, acknowledged commitment, and activation; rate control and
the evaluation distinguish transfer from resumption. It explicitly allows a
final stopped phase rather than requiring live copying to finish the entire
current state first. This is prior art for the control alternative exposed here.
Its implemented acknowledgment/failure protocol must not be identified with our
ideal fence, nor with early source departure into an independent deterministic
pipe. Its application measurements were not reproduced and do not validate our
service contract.

The interpretation, conditional simulations, and policy-class comparison in
this note are our deductions. The cited migration work establishes that early
freeze/stop-and-copy itself is familiar. The open research question is the exact
readiness guarantee under a justified restricted service protocol, not whether
copying can ever be completed after suspending updates.
