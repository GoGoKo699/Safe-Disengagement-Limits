# Scheduling, maintenance, and independent fallback: source audit

Inspected 22 September 2026 against repository base
`dbafc04df679ce5b5d22a8c9654c85dbea234cb0`.
This is a targeted research audit, not a novelty certificate or deployment validation.
Historical checkpoints remain unchanged.

## Decision

The homogeneous post-request clearing theorem has a direct route through existing
state-dependent-speed scheduling. This includes unequal preparation sizes when
released capacity and invalidation rate remain common. The reduction below is
stronger evidence of overlap than the previous migration analogy. Do not present
the homogeneous clearing sum, serial optimality in that subclass, or its
unequal-size extension as an independently novel scheduling result.

The heterogeneous recurring-upkeep question is still a distinct mathematical
object, but a combination of elementary domination, a bounded-storage average
bound, and standard scheduling may be too weak for publication. Subsequent
same-day work proved [heterogeneous serial dominance](2026-09-22-heterogeneous-scheduling.md)
and completed the [dissipativity comparison](2026-09-22-dissipativity.md).
Section 6 below records the resulting narrower contribution boundary and a
further prior-art reduction of the serial objective. The invalidation/interface
model remains a substantive question. No absence-of-prior-art claim is made here.

## 1. Primary-source records

### 1.1 Ayesta, Prabhu, and Righter: state-dependent service rates

U. Ayesta, B. Prabhu, R. Righter, *Scheduling in a single-server queue with
state-dependent service rates*, Probability in the Engineering and Informational
Sciences 34(4), 507–521 (2020); published online 2019.
[DOI](https://doi.org/10.1017/S0269964819000160),
[author manuscript](https://hal.science/hal-01783136/document).

**Inspected:** manuscript sections 1–2, section 3 model/objective, complete
sections 4–5 including Lemma 1, Theorems 1–2, and Corollaries 1–5. These are
manuscript pages 1–11; numbering should be checked against the final journal PDF
before submission. The HAL cover identifies version 1, deposited 2 May 2018.

The server capacity `C(j)` depends on jobs remaining; preemption, processor
sharing, and idling are permitted. Section 3 equation (1) includes makespan by
choosing holding cost `g(j)=1{j>0}`. Section 4 Lemma 1 reduces policies to SRPT
with deferred job release. Section 5 Theorem 1 gives a linear program; Theorem 2
characterizes the optimum through cost/capacity ratios. Corollary 4(iv) makes
SRPT optimal for makespan when capacity decreases with jobs remaining.

**Boundary:** common released capacity with durable work maps directly to this
model. Distinct released capacities and losses of partial work do not map merely
by renaming its parameters. Section 2 below supplies a relaxation for common
invalidation and common release.

### 1.2 Gawiejnowicz: earlier nonpreemptive makespan result

S. Gawiejnowicz, *A note on scheduling on a single processor with speed dependent
on a number of executed jobs*, Information Processing Letters 57(6), 297–300
(1996). [DOI](https://doi.org/10.1016/0020-0190(96)00021-X),
[author-uploaded accepted manuscript](https://www.researchgate.net/publication/220112801_A_Note_on_Scheduling_on_a_Single_Processor_with_Speed_Dependent_on_a_Number_of_Executed_Jobs).

**Inspected:** full accepted-manuscript text, sections 1–2 and Theorems 2–6,
including proofs. The hosting page identifies the upload as the author's own.

Section 1 assumes independent nonpreemptive jobs and positional speed `v(j)`;
makespan is the sum of processing requirements divided by those speeds.
Section 2.1 Theorem 3 gives shortest-processing-time order for increasing speed;
the argument uses the rearrangement inequality. Theorem 6 sorts arbitrary speed
positions against job sizes.

**Boundary:** this already covers the ordering of serial schedules with equal
capacity releases and common invalidation after setting
`v(j)` proportional to `b+(j-1)a-d`. It does not establish arbitrary-preemptive
optimality in the decaying preparation model; the previous source and our
relaxation supply that step.

### 1.3 Timmermans and Vredeveld: preemptive scheduling precursor

V. Timmermans, T. Vredeveld, *Scheduling with State-Dependent Machine Speed*,
WAOA 2015, LNCS 9499, 196–208.
[DOI](https://doi.org/10.1007/978-3-319-28684-6_17).
The inspected primary text is the three-page MAPSP 2015 precursor,
*Scheduling with state-dependent machine speeds*, proceedings pp. 56–58:
[hosted proceedings](https://orbi.uliege.be/bitstream/2268/182862/1/Proceedings%20MAPSP%202015.pdf).

**Inspected:** complete precursor, sections 1–2, model definition, Lemma 1,
and references. The full WAOA chapter was not retrieved; do not cite its theorem
numbering as inspected.

The model permits infinitesimal preemption and speed depending on the number of
completed jobs. Its objective is weighted total completion time. The precursor
describes an LP for fixed completion order and a structural lemma permitting
simultaneous completion groups with no partly served later group at a group
completion. Its cited makespan predecessor is Gawiejnowicz (1996).

**Boundary:** this corroborates an established scheduling lineage. It does not
provide the heterogeneous S1 upkeep theorem.

### 1.4 Cho and Garcia-Molina: recurring freshness allocation

J. Cho, H. Garcia-Molina, *Synchronizing a Database to Improve Freshness*,
ACM SIGMOD (2000), 117–128.
[Primary full text](https://sigmodrecord.org/publications/sigmodRecord/0006/pdfs/Synchronizing%20a%20Database%20to%20Improve%20Freshness.pdf).

**Inspected:** freshness/age definitions and Poisson update model in sections
2.1–2.3, synchronization choices in section 3, and complete section 5.3
(Problem 1, Example 4, Table 5, concluding comparison of the objectives).

Section 2.2 derives expected freshness `exp(-lambda*t)` between refreshes.
Section 5.3 allocates a fixed aggregate refresh frequency to maximize average
freshness or minimize age. Its example optimally gives no refreshes to one
rapidly changing object for the freshness objective. Thus heterogeneous refresh
allocation and choosing which objects to neglect are established questions.

**Boundary:** this is stochastic, average freshness with discrete object
refreshes, rather than robust completion readiness at every time. Finite
post-request clearing, released primary service capacity, and fluid partial-copy
invalidation do not appear in the inspected optimization. These differences
preclude a simple literal parameter substitution; they do not establish novelty.

### 1.5 Gąsieniec et al.: perpetual maintenance and bounded-stock drift

L. Gąsieniec et al., *Perpetual maintenance of machines with different urgency
requirements*, [arXiv:2202.01567v2](https://arxiv.org/html/2202.01567v2),
25 August 2023 (subsequently JCSS).

**Inspected:** introduction's full model definition, all-times maximum-height
objective and total-height lower-bound argument; section 3/4.1 material on the
Pinwheel connection; Theorem 4.1 statement. The approximation proofs were not
audited.

Objects accumulate weighted age and service resets one object. Discrete service
is limited to one reset per slot; the continuous version incurs travel time.
The introduction obtains a maintenance lower bound by showing that total height
would otherwise increase while each component is bounded. This is a close
precedent for the elementary bounded-storage averaging method itself.

**Boundary:** its reset/travel constraints differ from divisible simultaneous
refresh effort. In particular, average aggregate load need not characterize
feasibility with discrete maintenance. Adding packetized refreshes to S1 would
require a fresh theorem and a Pinwheel comparison.

### 1.6 Migration papers: claims now excluded

**Kherbache, Hermenier, and Madelaine**, *Scheduling Live Migration of Virtual
Machines*, [author full text](https://www.btrplace.org/pubs/kherbache-tcc17.pdf).
Reinspected section 5.3, especially equations (10)–(12) and its model-comparison
discussion. Equation (10) is exactly memory divided by bandwidth minus constant
dirty-page rate. Their comparison also explains why replacing richer memory
activity with one constant rate loses accuracy. This establishes the familiar
single-stage denominator; it does not validate constant full-rate loss at every
positive partial preparation. No experiments were reproduced here.

**Lu et al., vHaul**, [author full text](https://huilucs.github.io/pubs/vhaul.pdf).
Inspected complete section IV, including Algorithm 1 and parameterization, plus
section III's sequential/parallel comparison. The operational scheduling rule
sorts a resource-utilization/migration-duration product as a heuristic for
pending-request effects; migration traffic has a dedicated shared link. This is
not an exact minimax theorem for the S1 dynamics. It does establish that service
coupling and the ordering of sequential migrations are old subjects.

**He, Toosi, and Buyya**, [arXiv:2111.08936v1](https://arxiv.org/html/2111.08936v1).
Reinspected sections IV-A–IV-D, equations (1)–(6), and scheduling paragraph in
V-A. A resource-dependency graph governs concurrent migration groups; completed
migrations unblock later ones. Arrival times/deadlines concern actual request
queues. This does not itself answer counterfactual readiness maintenance before
a request. Its sequential/concurrent conclusions should not be imported as a
general all-policy proof for heterogeneous S1.

**Clark et al.**, [NSDI 2005 full text](https://www.usenix.org/legacy/events/nsdi05/tech/full_papers/clark/clark_html/).
Reinspected introduction, related-work residual dependencies, and design opening;
the historical checkpoint records the broader original inspection. The paper
uses a final pause-and-copy and specifically distinguishes removing residual
source dependency. Neither dependence-free handover nor updating copied state
is a new S1 concept. S1's instantaneous zero-pause cutover needs its own
justification.

## 2. Explicit clearing-time reduction

This is a derivation performed in this pass, using the scheduling result above;
it is not represented as a quotation from prior work.

Consider `r>=1` cold remaining modules with arbitrary positive `M_i`, common
invalidation `d`, common released rate `a`, and initial post-cutover spare rate
`b`. If `b<=d`, no cold module can start increasing against maximal invalidation,
so no first completion is possible. Suppose `b>d`.
The separate empty case has clearing time zero.

Take any feasible decaying-preparation schedule under maximal invalidation.
Let `J_o(t)` be its completed-module count. Define a virtual durable job of size
`M_i` for each module, serving it at rate `(p_i'(t))_+` until it has accumulated
`M_i` work, then ignoring further assigned virtual work. Accumulated positive
variation dominates net change from the cold state. Therefore each virtual job
finishes no later than its original module: `J_v(t)>=J_o(t)`.

At almost every time, a strictly increasing original coordinate satisfies
`p_i'=v_i-d`, including at the lower reflected boundary when it increases. If
there is at least one such coordinate,

    sum_i (p_i')_+ <= sum_i v_i - d <= b+a*J_o-d.

If none increases the left side is zero and the inequality still holds because
`b>d`. Stopping virtual work at completion can only reduce its assigned total.
Thus the virtual schedule obeys

    total virtual processing rate <= b+a*J_v-d.

It is feasible for a durable-job server with capacity

    C(j)=b+(r-j)*a-d,       j=1,...,r,

when `j` jobs remain. Consequently the durable optimum is a lower bound on
every original completion time. Ayesta–Prabhu–Righter Corollary 4(iv) applies:
this capacity decreases with the number of remaining jobs, so SRPT minimizes
makespan. With no arrivals and initially cold jobs, this is serial increasing
`M_i` order. That same serial schedule is feasible in the original model and
has exactly the relaxed stage times. Hence, writing `(i)` for sorted sizes,

    tau = sum_{j=0}^{r-1} M_(j+1)/(b+j*a-d).

This is an exact reduction for that subclass, including the historical
homogeneous formula. The argument does not replace `a` or `d` by an average
when they differ between modules. It also does not assert optimality from
arbitrary initially partial preparations: serial processing can lose other
initial partial work in that setting.

## 3. Operational interface: a contract, not a certified implementation

A defensible narrow interpretation is planned retirement of a cooperative
primary hosting independent stateful service shards. The fallback runs a
preinstalled conservative service implementation. It does not copy or depend
on the primary's decision-making algorithm. This is an abstract application
class to test; there is no deployment evidence yet.

| Contract item | Required interpretation or evidence |
|---|---|
| Essential service | Each shard has an explicit request/response safety contract, including already acknowledged obligations. Optional optimization may cease. |
| Transfer state | A sufficient state interface includes current records, sequence/duplicate-suppression state, outstanding accepted obligations, and ownership epoch. A memory image alone is not a sufficiency proof. |
| Shared primary resource | A source network interface carries prescribed normal client traffic of rate `a_i`, optional traffic, and reconciliation bytes in the same capacity units. CPU cost must be separately provisioned or explicitly included. |
| Released capacity | After ownership transfer, clients communicate directly with the fallback through its own interface. No proxying, page faults, directory lookup, or command interpretation remains on the source. Only then is `a_i` released. |
| Independent receiver | Destination computation, storage, networking, power, credentials and code are available before readiness begins and are separately paid for. Shared infrastructure must not depend on the retired controller. |
| Cutover | An independently supported ownership fence routes each subsequent request exactly once and prevents split-brain service. Atomicity and zero latency are idealizations in the present theorem. |
| Updates | While source-owned, the prescribed service mutates the transferred state. A justified update uncertainty set must be derived from this interface rather than fitted only to a convenient migration formula. |
| Independence | No cross-shard consistency barrier or other shared-primary obligation remains. A coupled system requires a different model. |
| Physical control | For an actuator application, the receiver additionally requires its own sensing, actuation access, calibrated state estimation, and a proof that its conservative policy preserves the essential safety set. The service-shard illustration does not provide these. |

The source-NIC interpretation makes capacity release concrete, but is not
universal: a dedicated migration link may release no additional copying
bandwidth after ordinary service moves. Likewise, independently logged updates
can remove the assumed competition. Such architectures are alternative resource
models, not counterexamples inside the stated one.

## 4. What full-rate invalidation requires

The current uncertainty model permits every module with `p_i>0` to lose useful
preparation at rate `d_i`, simultaneously across modules, regardless of how
small `p_i` is. This is stronger than a bound on average update traffic.

An operational adversary realizing this fluid envelope must be allowed to
target currently copied state, without an address-locality, minimum-event-size,
or per-location update restriction. As the prepared set changes it can keep
targeting newly useful material. Aggregate update budgets must permit all
per-module maxima together. This can be a conservative worst-case abstraction
of arbitrary overwrites; the audit has not identified empirical evidence that
it is tight for a real fallback interface.

There is a further exact-state issue: `p=M` maintained continuously at effort
`d` presumes no finite propagation delay, packet granularity, serialization
barrier, or ownership-transfer delay. A real standby with a nonzero-latency
update path is generally temporarily behind after each update. A proof using
an essential-service tolerance or a bounded final cooperative handoff can be
meaningful, but must account for that tolerance or delay explicitly.

The support-cost mechanism is therefore assumption-sensitive. Restricting
updates to known locations, independent logging, or proportional exposure can
make preserving a small prepared subset cheaper. The archived proportional
countermodel already proves that a staircase cannot be inferred from finite
state size and a worst-case total update rate alone.

Two useful next investigations are: (i) derive a copied-state erosion envelope
from an explicit finite-record interface and compare its fluid limit; (ii)
characterize readiness under state-dependent erosion, keeping cutover and
essential-service obligations fixed. These are better motivated than adding
parameters to preserve a staircase by definition.

## 5. Access record and remaining audit tasks

Primary PDFs were downloaded for local text extraction outside the repository;
no third-party papers are committed. The web tool could not fetch HAL and
reported the full MAPSP PDF too large, but direct HTTPS retrieval succeeded.
The successful primary retrieval, rather than those web failures, determines
the inspection scope above.

| Retrieved PDF | SHA-256 of inspected bytes |
|---|---|
| Ayesta–Prabhu–Righter HAL manuscript | `9adda38b4bbc010c899e9fd82f63b5a45346b0986a8d4df1f1688882d8162aec` |
| MAPSP 2015 complete proceedings | `2417b0f4b12aaff65e71d20830bde8fe0bccb77a16824d5dc3ea4187223f1d63` |
| Cho–Garcia-Molina | `db1fdce02a3bf06ca38005c6978d996d69a5b5c198b9525cdb96db060138355f` |
| Kherbache–Hermenier–Madelaine | `b82c57c9f151e0b96f23a13cf52e744671badb372acac3990cf01e18a035f75c` |
| vHaul | `8a19411b63b3b95d1652a79092ff44a2e93fc00fb384c6491e236b26e1cc8f94` |
| Cheng et al. 2013 institutional PDF | `2b0d928c94368637a8de5a65a975b56d2ea5fda51a43c1174c0b8898885c91da` |

Remaining tasks are narrowly specified:

1. Complete the experience-based scheduling audit in section 6. The serial
   objective has a further prior-art embedding; the arbitrary-allocation
   decaying-state equivalence remains the theorem requiring comparison.
2. The recurring-upkeep dissipativity audit is complete in
   [the separate note](2026-09-22-dissipativity.md): treat the bounded-storage
   average argument as an established method. Its specific reflected model is
   handled directly, without silently importing smooth-system assumptions.
3. Recover the complete WAOA chapter if its finer claims become relevant.
4. The historical lead *Does Partial Replication Pay Off?* remains uninspected
   beyond its bibliographic record and must not support an absence claim.
5. Build and verify one finite-record fallback interface before making an
   engineering applicability claim. The contract in section 3 is a design
   obligation, not evidence that a chosen implementation satisfies it.

## 6. Follow-up: unequal releases, learning schedules, and changing loss laws

This follow-up responds to the same-day heterogeneous serial-dominance proof.
The distinction is between its policy-class reduction and the finite serial
optimization problem left after that reduction.

### 6.1 Nested capacity regions do not supply this reduction

B. Sadiq, G. de Veciana, *Balancing SRPT Prioritization vs Opportunistic Gain in
Wireless Systems with Flow Dynamics*, ITC 22 (2010),
[DOI](https://doi.org/10.1109/ITC.2010.5608716),
[primary manuscript text](https://www.researchgate.net/publication/224184887_Balancing_SRPT_prioritization_vs_opportunistic_gain_in_wireless_systems_with_flow_dynamics).
The manuscript's first author is Bilal Sadiq; the hosting profile attribution
differs, so use the paper's byline.

**Inspected:** complete sections II-A, III, IV-A/B, and V-A, including definition
1, equations (2)–(5), and Theorem 1. The theorem's detailed proof is deferred to
technical report [20], which was not inspected.

Section II-A removes user identity from the capacity law by scaling file sizes.
Section III requires symmetric capacity regions and exact coordinate-section
nesting. Section V-A minimizes total flow time for durable jobs over a
polymatroid region, via SRPT with highest possible rates.

**Boundary:** in S1, deleting job `i` expands the surviving simplex from capacity
`b` to `b+a_i`. Its smaller-job region therefore is not the coordinate section
of the earlier simplex. Job-specific invalidation also lies outside that
durable-work model. This source is a useful comparison, not a reduction of the
heterogeneous cold-state theorem.

### 6.2 A verified serial subclass is learning-effect scheduling

T. C. E. Cheng, S.-C. Tseng, P.-J. Lai, W.-C. Lee,
*Single-Machine Scheduling with Accelerating Learning Effects*, Mathematical
Problems in Engineering (2013), article 816235,
[DOI](https://doi.org/10.1155/2013/816235),
[institutional full text](https://ira.lib.polyu.edu.hk/bitstream/10397/17136/1/Cheng_Single-machine_scheduling.pdf).

**Inspected:** complete introduction, section 2 model/equation (1), Lemma 1
and proof, adjacent-swap equations (9)–(13), and Property 1 with its proof.
Other objective-function proofs were not needed for this comparison.

Its duration model is `P_j(1+sum_{k<r} alpha_{r,k} P_[k])^q`, `q<0`;
Property 1 gives an SPT makespan optimum under its coefficient conditions.

**Exact serial mapping:** suppose `d_i=d`, `a_i=c*M_i`, and initial capacity
`b0>d`. Put `P_i=M_i/(b0-d)`, `alpha_{r,k}=c`, and `q=-1`.
Then its duration equals

    M_i / (b0-d + sum_{j completed} a_j).

Thus this unequal-release subclass's serial order is already covered. The
paper does not establish equivalence to arbitrary allocations with decaying
partial preparation. It is evidence against claiming the serial expression
itself as a new scheduling model.

### 6.3 Stronger general-objective overlap, with a remaining access limit

A. Janiak, W. Janiak, R. Rudek, A. Wielgus,
*Solution algorithms for the makespan minimization problem with the general
learning model*, Computers & Industrial Engineering 56(4), 1301–1308 (2009),
[DOI](https://doi.org/10.1016/j.cie.2008.07.019),
[publisher record](https://www.sciencedirect.com/science/article/pii/S0360835208001654).

**Inspected:** complete publisher-rendered introduction, including the
job-specific experience definition; only preview fragments of sections 2–5
and the conclusion were accessible. No complexity proof or algorithm theorem
from this paper is treated as verified.

The introduction describes nonincreasing positive processing functions `P_i(E)`.
Experience increases by job-specific `e_i>=1`, with fraction `beta_i` credited
at start and the remainder at completion. It attributes this formulation to
Janiak and Rudek (2007).

**Our embedding:** for positive releases and `b0>max_i d_i`, take
`epsilon=min_i a_i`, `e_i=a_i/epsilon`, `beta_i=0`, and

    P_i(E) = M_i/(b0 + epsilon*E - d_i).

These are positive decreasing functions and reproduce every serial S1
duration. This establishes overlap of the reduced objective with an existing
model class, not a prior proof of S1 serial dominance. Zero releases and
infinite-duration infeasibility require separate treatment. The broad class's
reported hardness does not prove hardness of this rational subclass.

The earlier sources are explicit remaining retrieval targets:
Janiak–Rudek (2007),
[The learning effect: Getting to the core of the problem](https://doi.org/10.1016/j.ipl.2007.03.013),
and Janiak–Rudek (2008),
[A new approach to the learning effect: Beyond the learning curve restrictions](https://doi.org/10.1016/j.cor.2007.04.007).
Only bibliographic/abstract records for these two papers were inspected;
their theorem-level details remain open. In particular, do not transfer their
pseudopolynomial or hardness claims to S1 by association.

### 6.4 What remains a candidate contribution

The candidate theorem is now precisely the reduction from arbitrary shared
allocations, preemption, and state loss to a serial schedule with
identity-dependent released capacity. The serial permutation objective,
subset dynamic programming once that reduction holds, and bounded-storage
upkeep averaging are insufficient novelty claims by themselves.

For a proposed state-dependent loss `ell_i(p)`, a serial stage would take

    T_i(b) = integral_0^{M_i} 1/(b-ell_i(x)) dx

when that integral represents a finite accessible traversal. This is an
elementary scalar separation-of-variables calculation. Where all relevant
stages are finite, `T_i(b0+epsilon*E)` is again a decreasing experience-based
duration function. Any substantive extension must justify the all-policy
reduction, handle inaccessible states and equilibrium barriers, and connect
the loss envelope to the fallback contract. An integral formula alone does
not escape the existing scheduling lineage. This paragraph is a mathematical
comparison, not an assertion that a nonlinear serial-dominance theorem has
already been established in the cited literature.
