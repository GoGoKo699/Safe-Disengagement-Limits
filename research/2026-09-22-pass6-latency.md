# Positive residual-drain time breaks immediate-release scheduling

22 September 2026. Pass 6 interface stress test. This note gives exact small
counterexamples to extending the earlier serial theorem across a positive
post-handoff resource-release delay. The delay is motivated by a specific
accounting obligation, not added to preserve a novelty claim. This is a
conditional service-interface model, not a verified implementation or a claim
of publication novelty.

## 1. Which delay can legitimately stop invalidation?

An unresolved ownership transfer is not an immutable task: if the old source
can still acknowledge mutations unavailable to the receiver, its state continues
to change and copying cannot simply stop. A finalization timer does not resolve
that issue.

The narrower interface studied here has two distinct events:

1. **Ownership handoff.** The receiver has sufficient committed state, including
   every state-changing acknowledged obligation. An independently supported
   fence makes it responsible for subsequent essential requests. The old source
   cannot newly acknowledge source-exclusive mutations; pending ownership
   decisions and requests are independently resolved. Its remaining work cannot
   change the receiver's required state.
2. **Residual drain completion.** Already accepted immutable source obligations,
   such as final transmission of fixed response data, finish. The source remains
   available to discharge them and retains its reserved resource rate until then.

Essential new service continues at the independently provisioned receiver.
Essential old obligations continue at the cooperative source. Neither may pause
without whatever delay tolerance the service contract expressly provides. The
primary is fully removable only when both kinds of obligations no longer need it.

This accounting is appropriate only if residual work really is immutable and
its execution is separately assured. If a response can mutate receiver state,
or if late writes have not been transferred, the model does not apply. It also
does not solve the positive propagation-delay obstruction to exact hot state
*before* the fence. State sufficiency and an independently supported ownership
fence remain interface obligations.

## 2. Mathematical residual-drain model

Keep the fixed-rate reflected preparation dynamics and shared source capacity.
Module `i` has preparation size `M_i>0`, released rate `a_i>0`, and maximum
invalidation `d_i>=0`. When its preparation first reaches `M_i`, it may perform
the ownership handoff and enter a residual drain of fixed duration `ell_i>0`.
It needs no further reconciliation and suffers no preparation invalidation
after that event. Its drain retains its prescribed source reservation `a_i`.
At the drain's end this reservation is released. Drains can run simultaneously
using their already accounted independent reservations.

If `D(t)` is the set whose drains have ended, the preparation budget is

    sum_i v_i(t) <= s + sum_{i in D(t)} a_i.

No additional unbudgeted copy engine or receiver resource is assumed. A fixed
duration drain can be read as an exact stage or as an adversarially attainable
worst-case bound; the examples use its full duration. A fully ready module at
request time can start its drain immediately, but it releases no source capacity
until the drain ends. Completion of all drains is the removal deadline.

Two restrictions must be distinguished:

- **Module-by-module removal:** finish both preparation and drain of a module
  before starting another module's preparation.
- **Uninterrupted preparation:** prepare one module at a time without leaving
  it partly prepared to work on another; already started drains may overlap.

The zero-delay theorem merges these notions. With positive drains they differ.
The first counterexample defeats module-by-module removal. The second defeats
even uninterrupted preparation, although its attaining schedule never needs
simultaneous allocation to multiple preparation jobs.

## 3. Two modules: overlap already helps

Take two initially cold identical modules with

    s=2, M_1=M_2=1, a_1=a_2=2,
    d_1=d_2=1, ell_1=ell_2=1.

The exact optimal guaranteed total time is **3**:

| Time | Preparation work | Residual drains |
|---|---|---|
| `[0,1]` | Prepare A at rate 2, net progress 1 | None |
| `[1,2]` | Prepare B at rate 2, net progress 1 | A |
| `[2,3]` | None | B; A has released its reservation |

For the matching lower bound choose both losses at their maxima. The first
preparation completion cannot occur before time one, so the first drain cannot
finish before time two. If the last preparation finishes no earlier than time
two, its own unit drain forces total time at least three. If both preparations
finished before time two, no capacity would yet have been released. The
potential consisting of completed preparation plus unfinished useful preparation
then has derivative at most `s-d=1` until both are prepared. It starts at zero
and must reach two, ruling out that case. Hence no parallel/preemptive policy
finishes removal before time three.

By contrast, module-by-module removal takes

    1/(2-1) + 1 + 1/(2+2-1) + 1 = 10/3.

Thus adding a drain time to each stage of the old subset recurrence gives a
strictly suboptimal answer. Two modules are the smallest possible overlap
example; with only one module there is no other preparation to overlap.

## 4. Three modules: preempting preparation is strictly necessary

Now take `s=1` and three modules. A is fully ready at the request; B and C are
cold. Every drain lasts one time unit.

| Module | Initial preparation | M | a | d | ell |
|---|---|---:|---:|---:|---:|
| A | Fully ready | 1 | 2 | 0 | 1 |
| B | Cold | 1 | 6 | 2 | 1 |
| C | Cold | 5 | 1 | 0 | 1 |

Start A's drain at time zero. Preparation capacity is one until time one and
three thereafter, until another drain ends. B cannot acquire positive
preparation at capacity one against loss rate two; C can use that interval.

The exact optimal guaranteed removal time is **37/9**, attained as follows:

| Time | Preparation action | Relevant event |
|---|---|---|
| `[0,1]` | Give capacity 1 to C; reach `p_C=1` | A drains |
| `[1,2]` | Preempt C; give capacity 3 to B; net progress 1 | A has released 2 |
| `[2,3]` | Resume C at capacity 3; reach `p_C=4` | B drains |
| `[3,28/9]` | Finish C's last unit at capacity 9 | B has released 6 |
| `[28/9,37/9]` | None | C drains |

The useful preparation stored in C does not decay because `d_C=0`. This is an
allowed heterogeneous instance. The proof does not claim that the same witness
works with common strictly positive invalidation rates.

### 4.1 Best uninterrupted-preparation schedules

There are only two preparation orders for the cold modules. Starting a drain
earlier only helps, so A's drain starts at zero. Full allocation to the current
preparation job gives its earliest possible progress and cannot delay either
drain release.

- **B then C:** B cannot progress before time one and finishes at time two.
  C then receives three units of work during B's unit drain, followed by its
  remaining two units at capacity nine. C finishes preparation at `29/9` and
  drains until `38/9`.
- **C then B:** C gets one unit before time one and its remaining four at
  capacity three, finishing at `7/3`. During C's unit drain, B prepares at net
  rate one and finishes at `10/3`; its drain ends at `13/3`.

Idling cannot improve either order. Therefore the best uninterrupted-preparation
time is `38/9`, strictly above the preemptive schedule's `37/9`.

### 4.2 Lower bound over every policy

Choose maximal invalidation. Before the first preparation completion of B or C,
the total allocated preparation work by time `t>=1` is at most `3*t-2`.
Producing useful amount `p` in B requires at least `3*p` allocated work: on its
last positive-preparation interval the net growth rate is at most `3-2=1`,
so the interval lasts at least `p`, and its full-rate loss consumes at least
`2*p` extra work. Any earlier erased preparation only increases the cost.

**B completes preparation first at time `t`.** Necessarily `t>=2`. At most
`3*t-5` work has reached the durable C, leaving at least `10-3*t` when this
quantity is positive. B's drain ends at `t+1`; until then capacity remains three,
and afterward it is nine unless C is already finished.

For `2<=t<=7/3`, at least three units of C remain, so C's preparation completes
no earlier than

    t+1 + (7-3*t)/9.

Adding C's own unit drain gives total time at least
`25/9+2*t/3>=37/9`. For `7/3<=t<=10/3`, the remaining-work bound instead gives
C preparation completion no earlier than
`t+(10-3*t)/3=10/3`, hence removal no earlier than `13/3`. This remains a valid
lower bound if C actually needs more than one pre-release time unit, because
then its completion is later still. For `t>=10/3`, B's own drain already forces
time at least `13/3`.

**C completes preparation first at time `t`.** Necessarily `t>=7/3`. It has
consumed five units, so B's useful preparation is at most `t-7/3`, as well as
at most one. Until C's drain ends at `t+1`, B's net growth rate is at most one.
For `t<=10/3`, its preparation cannot finish before
`t+1-(t-7/3)=10/3`; the potential capacity increase at `t+1` cannot create an
earlier completion. Its unit drain therefore forces time at least `13/3`.
For `t>=10/3`, C's own drain already supplies that lower bound. Simultaneous
preparation completions require at least `10/3` and are covered by either case.

The cases exhaust arbitrary parallel, preemptive, adaptive, or idle policies.
The worst-case optimum is at least `37/9`, and the displayed strategy attains it.
For smaller losses, following its planned handoff times after attaining at
least the required preparation preserves the same upper bound; no robust
guarantee relies on the adversary delaying a release.

## 5. What survives, what fails, and what is still open

The old serial theorem depends on resource being released at the same event
that removes the preparation job and its invalidation. Here these events are
separated. A removal-only subset no longer determines capacity: drain age and
remaining finalization times matter. The earlier potential may still supply
partial lower bounds, but its tight serial construction no longer follows.

The two-module example invalidates the simple proposal to add `ell_i` to each
old serial stage. The three-module example is stronger: even a scheduler that
overlaps all residual drains but never interrupts preparation can be suboptimal.
A timed capacity release creates a useful interval for a durable module before
a more rapidly invalidated module becomes preparable. This mechanism is absent
from the instantaneous-release model.

These are exact small counterexamples, not a hardness result or a solved general
latency model. Section 6 preserves an abstract recurring-upkeep reduction, but
does not evaluate its deadline-feasibility oracle. The examples do not invalidate
the earlier theorems under their stated instantaneous-release assumption.

The operational conclusion is conditional but concrete: if a proposed fallback
interface leaves immutable, source-resident essential obligations after ownership
transfer, either include that drain and its held resources in the handover model,
or arrange for those obligations to be transferred independently. Treating them
as zero time or free capacity changes the optimization problem. The pre-fence
freshness and fencing issues must still be resolved separately.

## 6. Fixed-loss support upkeep survives as an oracle reduction

The loss of serial optimality does not by itself destroy the fixed-rate
recurring-upkeep argument. The distinction is between the following exact
reduction and evaluating the post-request feasibility problem it contains.
This is an internal analytic result, not external review or an operational
validation of the drain interface.

### 6.1 Contract and actual deadline feasibility

Use the fixed-rate model of section 2, with finite `M_i>0`, `a_i>0`, `d_i>=0`,
`ell_i>0`, and `s>=0`. Before a request, all modules remain source-owned,
none has begun its drain, and normal preparation plus optional work obey

    sum_i v_i(t)+u(t)<=s,    u(t)>=0.

All componentwise measurable loss histories `0<=rho_i(t)<=d_i` are allowed
simultaneously while a module remains in preparation. In particular, the full
maximum vector is allowed throughout normal operation. Preparations are
absolutely continuous reflected states; allocations are bounded, measurable,
and causal, with no impulses. Loss ceases only at ownership handoff. Every drain
then takes its fixed `ell_i`, holds its existing source reservation, and ends
independently of other drains. The subsequent capacity release is nonnegative.
There are no extra handoff costs, consistency barriers, or shared drain
bottlenecks beyond the reservations already charged. These restrictions are
essential to the comparison below.

Let `R_H^drain` be the states from which **there exists one causal exit policy**
whose last drain ends by finite deadline `H>=0` for **every** allowed future
loss history. Define the finite family

    A_H = {S subset N : the state p_i=M_i for i in S,
                         p_i=0 otherwise belongs to R_H^drain}.

Membership means actual guaranteed completion by `H`. It is not defined by
comparing `H` with an unproved attainable infimum of exit times. The earlier
finite-permutation attainment proof is unavailable in this drain model.

Write `ell_max=max_i ell_i`. Every module's handoff occurs at or after the
request, so its drain cannot end before `ell_i`. Thus no state is deadline
feasible if `H<ell_max`. Conversely, an all-ready state hands off every module
at time zero and finishes all drains exactly at `ell_max`. In particular,

    A_H is nonempty if and only if H>=ell_max,

and the all-ready state's exact optimal removal time is `ell_max`, not zero.

For `H>=ell_max`, define

    D_drain(H) = min_{S in A_H} sum_{i in S} d_i.              (1)

This is an attained minimum over a finite nonempty family. A minimizing set
has an actual robust exit policy by the definition of `A_H`; no general
existence theorem for a time-optimal drain schedule is being assumed.

### 6.2 Support domination with unfinished drains

**Lemma.** If `p` belongs to `R_H^drain` and `S={i:p_i>0}`, then `S` belongs
to `A_H`.

**Proof.** Choose a robust policy from the original state `p`. In the improved
system, grant full preparation to every member of `S`, hand them all off at
time zero, and start their drains. They still hold their source reservations
until their respective times `ell_i`; no immediate resource release is assumed.

Run the original policy on a virtual system initialized at `p`. For virtual
members of `S`, supply maximum allowed loss `d_i` until their virtual handoff.
For modules outside `S`, supply their actual loss histories and give the real
modules exactly the virtual allocations and handoff times. Those modules start
cold in both systems and have identical reflected dynamics, so their
preparations, handoffs, and drain completions match. The virtual history is
admissible because all componentwise bounded loss combinations are permitted.
The simulation is causal: virtual support states use specified losses and the
original policy, while the other state histories agree with their real copies.

If a virtual support module hands off at time `t_i>=0`, its reservation is
released at `t_i+ell_i`. Its real counterpart releases at `ell_i`, no later.
All outside-support releases occur at the same times in both systems.
Consequently the real available preparation capacity is at least the virtual
capacity at every time. Omitting allocations to the already handed-off support
modules makes the replay feasible. This comparison can be continued through
every handoff and drain completion, including simultaneous events.

The original robust policy guarantees that all virtual drains finish by `H`
for the induced allowed history. The real support drains finish no later than
their virtual counterparts, and the other drains finish at the same times.
Thus the improved state has a causal robust policy meeting `H`, proving the
lemma. Early support handoff helps here because it ends preparation and starts
an independent fixed timer while retaining at most the same reservation as the
original source-owned module; no resource is charged twice or released early.

### 6.3 Exact recurring rate with paid initialization

A normal policy must remain in `R_H^drain` at every counterfactual request time,
for every allowed preceding loss history. Initialization may choose a paid
prepared state, as in the earlier recurring theorem; no readiness or cold-ramp
guarantee is supplied before that initialization is complete.

Assume `H>=ell_max`, and follow any such normal policy under simultaneous maximum
loss. With `Q(t)=sum_i p_i(t)`, the reflected dynamics and support lemma give,
almost everywhere,

    Q' <= sum_i v_i - sum_{i:p_i>0} d_i
       <= s-u-D_drain(H).

There are no normal-mode drains: the oracle affects which supports are ready,
while this resource balance is the original fixed-rate normal balance. For
every normal duration `T>0`, integration yields

    integral_0^T u(t)dt <= [s-D_drain(H)]*T + Q(0)-Q(T).       (2)

Since `0<=Q<=sum_i M_i`, the guaranteed long-run optional rate cannot exceed
`s-D_drain(H)`. This holds without assuming a time average exists; in
particular, the limsup average on the maximal-loss history is bounded by that
quantity. It covers partial, rotating, preemptive, and bursty preparation.

If `D_drain(H)<=s`, choose a minimizing set `S*` and initialize it fully, with
all other modules cold. Keep each `i in S*` at allocation `d_i`, and use
constant optional rate `s-D_drain(H)`. Every allowed normal loss history keeps
this same ready/cold state. At any request, execute one of the robust exit
policies whose existence is asserted by `S* in A_H`. It meets the deadline for
every future loss history. Hence the bound is attained.

If `D_drain(H)>s`, indefinite readiness is impossible, including with `u=0`.
Equation (2) gives the finite ready-interval upper bound

    T <= Q(0)/[D_drain(H)-s],

which is not asserted attained. If `H<ell_max`, no ready state exists at all,
and this finite-`D_drain` calculation does not apply.

**Theorem.** With paid initialization and no pre-request handoff or drain,
indefinite readiness is feasible exactly when `H>=ell_max` and
`D_drain(H)<=s`. In that case the exact maximum guaranteed optional rate is
`s-D_drain(H)`. Otherwise it is infeasible under the prescribed normal load.

This theorem preserves the support/upkeep reduction while replacing its solved
instantaneous-release scheduling subproblem by an unresolved deadline-feasibility
oracle. It is not an explicit general latency frontier, an efficient algorithm,
or a claim that adding drain times to the old subset recurrence works. It also
does not transfer to smooth state-dependent loss, where upkeep is not determined
solely by positive support. Cold startup under the normal resource budget remains
a separate reachability question.
