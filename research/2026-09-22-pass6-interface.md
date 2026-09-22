# Pass 6: acknowledged obligations, propagation delay, and a finite-record interface

22 September 2026. This note supplies an abstract interface and a causal
obstruction, not an implementation or a novel distributed-systems impossibility
theorem. It preserves the distinction between exact receiver state, safe source
removal, and a bounded essential-service response time.

## 1. Finding

Unrestricted source-local acknowledgments and a positive information-delivery
delay do not permit continuously exact receiver freshness. This already fails
for one unpredictable bit, regardless of spare copying bandwidth.

That observation does **not** imply that the source must remain powered on for
the entire propagation delay. Independently powered network buffers, durable
logs, and packets already in flight can carry obligations after the source
departs. If the fallback may defer its response until that information arrives,
safe removal can precede receiver freshness. The timing constraint is on the
sum of remaining grace and permitted response delay, not automatically on grace
alone.

The continuous preparation theorems therefore remain idealized analytical
results. To interpret their hot state as a physical handover interface, the
protocol must pay for synchronous acknowledgment, a bounded final fence, or an
explicit response-latency/tolerance contract. None is supplied merely by naming
a dirty-page rate.

## 2. A minimal independent service shard

One shard stores a fixed finite number `N` of records drawn from a finite
alphabet. Its operations are idempotent `put(record,value)` and `get(record)`.
A single ordered writer suffices for the obstruction below; no consensus,
crash detector, Byzantine participant, or non-idempotent external effect is
needed. The smallest instance has `N=1` and a one-bit value.

The essential contract has three explicit parts:

1. **Acknowledged obligations:** a read invoked after an acknowledged write,
   with no intervening write, must return that value. More generally, the
   serial read/write history must respect completed operation order. Handing
   over cannot silently revoke an acknowledgment.
2. **Service:** an admitted request has a specified response allowance `R`.
   Accepted pending requests cannot disappear during handover. If the desired
   service requires immediate responses or an unbroken processing rate, setting
   a larger `R` is a contract change, not a proof of the original guarantee.
3. **Independence:** after source departure, correctness and response timing
   may depend only on the paid independent resources listed below. No source
   page fault, proxy, response generation, or instruction interpretation remains.

The sufficient transferable state includes current records, ownership state,
and all already accepted but unfinished obligations. There is an explicit
finite admission/queue bound; request tags, pending responses, and retry state
within that bound are included in the state budget. A one-time planned transfer
needs only the old/new ownership phases, not an unbounded history of controller
restarts. For the one-write obstruction, there is one acknowledged write and
one later read, so none of these bookkeeping details carries the argument.

| Resource | Explicit provision or accounting |
|---|---|
| Receiver | Independent code, processing capacity, record storage, pending-request buffers, credentials, power, and client network path |
| Routing and ownership | An independently supported fence that stops old ownership from accepting new obligations and establishes the new route; any latency and messages are paid |
| In-flight data | Only buffers/links whose delivery survives source departure count as independent; data left solely in source RAM does not |
| Source bottleneck | Normal source traffic, state transfer, acknowledgment traffic, and optional traffic share the declared budget if that is the intended resource model |
| Source release | The source rate `a_i` is released only when its client traffic and any source-dependent residual work actually cease |
| Outstanding requests | Every accepted request is completed, transferred with sufficient state, or independently queued under its original service deadline |

A routing change does not itself establish consistent ownership. Nor can the
model charge a destination's traffic or its coordination service to an invisible
free resource. These provisions are assumptions of this abstract service class;
they have not been demonstrated for a deployed system.

## 3. Causal obstruction and its correct deadline statement

Let `delta_min>0` be a lower bound on how quickly a newly revealed bit at the
source can affect any information available to the receiver's responding
process. Every independent route that could reveal that bit is included in this
definition. It is a causal **lower** bound, not a guarantee that delivery occurs
by that time.

**Proposition 1 (no continuous exact local hot state with early local ack).**
Suppose the source receives an unpredictable bit at time `t0` and acknowledges
the corresponding write before `t0+delta_min`. Then the receiver cannot already
have a sufficient exact local state for every such acknowledged write at every
time.

**Proof.** Compare executions in which the bit is zero and one. Before
`t0+delta_min`, the receiver has the same accessible information in both
executions. A later read with no intervening write requires different answers.
A single receiver state cannot supply both answers correctly. Randomness does
not help a zero-error guarantee: couple the random choices in both executions.
The proof uses one fresh bit and does not depend on record volume or on a
specific replication algorithm. Unrelated earlier preparation cannot encode
the bit before it is revealed.

**Proposition 2 (grace plus response allowance).** Suppose that same write is
locally acknowledged at `t0`, a removal request follows immediately, source
departure must occur by `t0+H`, and a read invoked at departure must be answered
within `R`. Under the preceding information-delay assumption, a necessary
condition for a uniform exact guarantee is

$$H+R\geq\delta_{\min}.$$

Indeed, if `H+R<delta_min`, even departure at the latest allowed time leaves
the read's response due before the receiver can distinguish the two executions.
Departing earlier cannot help. This proposition does not require the source to
remain alive while independently deliverable packets travel.

More generally, if the last locally acknowledged fresh write is revealed at
time `c`, departure occurs at `T`, and the post-departure response allowance is
`R`, then

$$T-c+R\geq\delta_{\min}$$

is necessary for that write. If fresh bits may be revealed and locally acknowledged arbitrarily
near departure, any fixed preceding grace period is insufficient to eliminate
the residual information delay: the necessary limit is `R>=delta_min` unless
the protocol changes the acknowledgment rule or fences the old writer early.

These are necessary conditions only. To give a constructive deadline, one also
needs a delivery **upper** bound `Delta_max`, finite serialization capacity,
receiver processing bounds, and a bounded ownership/routing protocol. A lower
bound on propagation speed alone cannot certify any finite handover deadline.

For the one-bit experiment with a reliable independent pipe of constant delay
`delta`, no serialization cost, and an already established independent route,
the information part of the bound is sharp: inject the bit at `t0`, let the
source depart while it travels, and answer at or after `t0+delta`. This is a
small theoretical witness about information timing, not a full handover
implementation or a way to hide routing/fencing costs.

## 4. Honest alternative contracts and their costs

### 4.1 Delay commitment rather than requiring zero-delay replication

Require that an externally acknowledged operation already be recoverable from
independent state or a sufficient independent log. New source-local speculative
state may remain ahead, but it cannot create an external obligation prematurely.
On planned removal, unresolved operations and ownership are settled by an
explicit protocol; a pending operation is not silently counted as completed.

Let `delta_ind` instead bound how quickly fresh source information can reach
any sufficient, independently recoverable state. Every fresh information-bearing
write incurs at least `delta_ind` before this commit condition can be satisfied.
This may be less than `delta_min`: a nearby independent log can commit a write
before the responding receiver learns it, provided later delivery fits the
service contract. If commitment specifically requires receiver-accessible
information, the relevant bound is `delta_min`. In the simple protocol that waits for a
receiver acknowledgment to return to the source, its replication contribution
to response latency is forward delivery plus receiver processing plus reverse
delivery. A round trip is a cost of that protocol, not a universal information
lower bound; a receiver that replies directly to the client has different
accounting.

The corresponding throughput cost also remains. For arbitrary fresh update
payloads that must remain independently recoverable, enough distinguishing
information must cross the source/independent-resource boundary. Metadata,
acknowledgments, log storage, replay processing, and bounded queue occupancy
are additional costs. A payload-bandwidth bound by itself does not guarantee
response latency.

This permits continuous recoverability of **acknowledged** service state with
positive network delay. It does not mean that both execution states are equal
at every physical instant. Applying an S1 fluid theorem to this interface would
require redefining preparation as sufficient committed/replay state and
rederiving its resource and loss law; substituting a measured update rate is
not enough.

### 4.2 Bounded final fence with explicit response slack

A source can stop accepting new source-owned mutations, settle the admitted
old prefix, and put subsequent requests in an independent bounded queue. Once
the old prefix is frozen, the remaining repair state is durable. If its
serialized size is `W`, reserved source transmission rate is `c>0`, reliable
delivery delay is at most `Delta_max`, receiver application takes at most
`t_apply`, and the remaining ownership/routing step takes at most `t_fence`,
then a simple sequential handoff completes receiver readiness within

$$F=W/c+\Delta_{\max}+t_{\rm apply}+t_{\rm fence}.$$

Any earlier time needed to close admission or determine the frozen prefix must
be added. Under these explicitly sequential stages, the formula is an upper
bound; overlap can reduce it. It does not assert an optimal deadline.

If the link and all transmitted bytes are already independently sustained, the
source can sometimes depart after serialization, before the destination is
ready. Then later delivery, application, and fence time must fit the service's
post-departure response allowance. If completion instead means an acknowledged
receiver-ready state, or the link needs source retransmission, the corresponding
confirmation/retransmission obligations must be included before departure.

Queuing preserves a bounded-response contract only if it fits its actual
latency and resource budgets. For illustration, under a fluid request-work
arrival envelope `sigma+lambda*t`, a receiver of rate `mu>0`, `mu>=lambda`, starting
after a delay `F` needs buffer at least `sigma+lambda*F`; the familiar
rate-latency bound is response delay at most `F+sigma/mu`. Discrete requests
require their packet/service-size allowances as well. These elementary queue
bounds are accounting examples, not new S1 results or evidence that a real
application has that slack. A contract that forbids such waiting cannot use
this construction unchanged.

### 4.3 Explicit tolerance

An application may instead permit a stated amount of stale state, output
error, or lost recent work. Such tolerance can make an asynchronously lagging
standby sufficient, but it changes the essential-service contract. The
single-register exact-acknowledgment obligation above allows no lost write;
returning its old value is not an acceptable implementation of that contract.

### 4.4 A post-fence drain is a separate stage

After sufficient committed state and ownership have transferred, the receiver
may already serve essential traffic while the source drains immutable old
responses or transport obligations. If those obligations cannot change receiver
state, preparation invalidation may stop while the original source load remains
reserved until drain completion. Other shard preparation may overlap this drain.
This is a coherent model for the separate delayed-release investigation.

If the alleged drain still accepts new writes or determines previously
unresolved service outcomes, its state is not frozen and invalidation cannot
simply be turned off. Positive drain time is also not a replacement for the
pre-fence propagation and consistency accounting above.

## 5. What finite records imply about erosion

Let each record, including the metadata needed for its current version, have
fixed transfer size `ell`, and let `M=N*ell`. Call a copied record useful only
when its receiver version is current for the chosen commit contract. An
overwrite can invalidate at most one such record. It invalidates none if that
record was already stale. A delivery contributes useful preparation only if
the delivered version is still sufficient when it arrives.

If overwrite count satisfies the pathwise envelope

$$A(t+h)-A(t)\leq\sigma+\lambda h,$$

then cumulative invalidation work obeys

$$E(t,t+h)\leq\ell\sigma+\ell\lambda h.$$

Without any additional useful copying or delivery during the interval, one also has

$$E(t,t+h)\leq\min\{p(t),\ell[A(t+h)-A(t)]\}.$$

The latter cap by initial preparation is not valid when useful new preparation
arrives inside the interval, whether through a first copy or a recopy. For
example, initially zero preparation can receive a record and then lose it to
one overwrite. With such arrivals a valid stock bound instead adds all newly
useful preparation to `p(t)`. The former event bound remains valid in either
case. Simultaneous module envelopes require an
aggregate workload that actually permits all those maxima together.

Thus a constant dirty-work rate `d=ell*lambda` is a conservative fluid envelope
when record granularity and burst work are made negligible and updates may
target whichever records are currently prepared. It is not an exact
continuous-time law for finite atomic records. At a positive but sub-record
prepared amount, there need not even be a completed record to invalidate.

If update addresses instead are conditionally uniform and independent of the
currently prepared set, the expected invalidated work per update is

$$\ell\,p/M,$$

giving expected drift `(lambda*ell/M)*p`. This supports a proportional loss
**expectation** under that stochastic assumption. It does not establish the
robust pathwise bound `rho<=gamma*p` used in the proportional readiness theorem:
a single realized update can target a prepared record and destroy an entire
record's useful preparation. Replacing an expectation by that adversarial bound
would be an unjustified change of quantifiers.

Finally, with positive copy delay, source allocation `v(t)` is not the
instantaneous arrival of useful current data. A faithful state description has
at least the current copied state and an in-flight/committed-delivery component,
or a protocol that makes the latter irrelevant to the selected contract. The
existing reflected fluid equations do not follow solely from the event-count
bound above.

## 6. Relation to the existing theorems

The fixed-rate and proportional theorems remain correct for their specified
ideal dynamics. The finite-record interface neither refutes their mathematics
nor validates their physical tightness.

The precise limit issue is important: letting record size, delivery delay,
and fence time approach zero may motivate bulk-work approximations, but
continuously exact receiver freshness fails after an early local acknowledgment
for **every positive** causal delay. An all-times exact hot-state assertion
does not automatically survive that limit uniformly. Any approximation theorem
must specify the service tolerance or response slack in which convergence is
claimed.

The next justified modeling task is therefore to keep acknowledged obligations
and deadline slack explicit in a finite-update or staged-handoff model. The
old fluid theorems can then serve as benchmarks. A claim that their recurring
cost is an implementation-independent law of safe controller removal is not
supported by this pass.

## 7. Primary-source inspection and novelty boundary

These sources support the systems comparisons below; the elementary
indistinguishability argument and finite-record bounds were derived in this
pass. No empirical results were reproduced.

1. **Scales, Nelson, and Venkitachalam (2010), _The Design of a Practical System
   for Fault-Tolerant Virtual Machines_.**
   [Primary paper, university-hosted copy](https://cs-people.bu.edu/liagos/651-2022/papers/vm-ft.pdf).
   Inspected complete §§2.2–2.3, PDF pp. 3–4 (printed pp. 32–33).
   Their protocol withholds external output until the backup acknowledges
   sufficient replay information; this need not stop primary execution. Takeover
   includes replay and separate split-brain control. The paper explicitly does
   not promise every output is produced exactly once. This establishes prior
   art for acknowledgment gating and separates recoverable logs from already
   replayed execution state. It does not validate S1's independent-shard,
   shared-source-budget model.
2. **Van Renesse and Schneider (OSDI 2004), _Chain Replication for Supporting
   High Throughput and Availability_.**
   [USENIX full text](https://www.usenix.org/legacy/event/osdi04/tech/full_papers/renesse/renesse_html/).
   Inspected §2's object/request specification, §3's protocol description, and
   the opening of §3.1 defining the abstract history and pending requests.
   Updates propagate along the chain; the tail handles reads and generates
   replies. The specification also explicitly allows ignored pending requests,
   so its availability contract must not be silently substituted for S1's
   bounded response guarantee. Replication before acknowledgment is established
   design practice, not a new S1 mechanism.
3. **Clark et al. (NSDI 2005), _Live Migration of Virtual Machines_.**
   [USENIX full text](https://www.usenix.org/legacy/events/nsdi05/tech/full_papers/clark/clark_html/).
   Reinspected §§3.1–3.3, particularly the complete staged design in §3.3.
   It explicitly includes stop-and-copy, confirmation of a consistent receiver
   image, commitment, and activation; it also treats network-state relocation
   without continued source forwarding. These are prior-art boundary examples,
   not proof that an essential-service contract allowing no pause is met.

None of these comparisons is an absence-of-prior-art claim for the new S1
scheduling lemmas. This interface pass establishes a necessary correction to
their operational interpretation, rather than a submission-ready contribution.
