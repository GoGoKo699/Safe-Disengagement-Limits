# Primary-source comparison and novelty limits

**S1 active-readiness checkpoint — inspected 22 September 2026.**

This is a targeted initial comparison, not a comprehensive novelty certification.
The passive-commitment results in the previous checkpoint remain a baseline
with known network-calculus overlap. The current candidate uses a new explicit
model of active reconciliation and endogenously released primary capacity.

## 1. Clark et al., Live Migration of Virtual Machines (NSDI 2005)

Primary full text:
https://www.usenix.org/legacy/events/nsdi05/tech/full_papers/clark/clark_html/

**Inspected:** introduction, related work, sections 3.1, 4, 5.2 and 5.3.

Pre-copy state may be dirtied again by a running workload. The paper distinguishes
execution downtime from the total time before a source host may be taken down.
It explicitly identifies residual source dependencies and avoids an unbounded
pull dependency in its chosen design. Its implemented completion includes a
final pause-and-copy phase. Dynamic bandwidth allocation trades interference
with longer downtime.

**Novelty boundary:** copying while operating, the danger of a remaining source
dependency, and contention between service and migration are old. Our strict
zero-pause model is a restriction, not a description of the full Clark scheme.
The present `p=M` handover condition idealizes an atomic cutover and does not
prove that a real process admits one.

## 2. Kherbache, Hermenier and Madelaine, Scheduling Live Migration of Virtual Machines

Author-hosted full manuscript:
https://www.btrplace.org/pubs/kherbache-tcc17.pdf

**Inspected:** abstract/introduction; scheduling constraints in section 4;
section 5.3 and equations (10)-(12), with rendered PDF page 8 inspected;
related-work discussions of dirty-page models.

mVM models workloads and network topology to choose schedules and bandwidths,
including sequential and parallel migration, deadlines/precedence and power
budgets. Equation (10), when comparing SimGrid's model, gives migration time
`mu/(bw-DPr)` for a constant dirty-page rate. The paper uses a more refined
two-stage workload model in its own approach and discusses the drawbacks of
single-rate approximations.

**Novelty boundary:** a term `M/(capacity-d)` is explicitly not new. Nor are
migration deadlines or deciding when to parallelize. The candidate result must
rest on the all-request-time recurring readiness frontier, not this denominator.
The paper is also evidence that a constant-rate approximation needs justification,
not blanket validation of our worst-case partial-preparation erosion model.

## 3. He, Toosi and Buyya, Efficient Large-Scale Multiple Migration Planning and
Scheduling in SDN-enabled Edge Computing (arXiv:2111.08936, 2021 version)

Primary full text:
https://arxiv.org/html/2111.08936v1
Abstract/version record:
https://arxiv.org/abs/2111.08936

**Inspected:** sections III, IV-A, IV-B and the stated objectives in IV-D.

The authors explicitly reserve service-network bandwidth when assigning migration
resources; memory dirtying affects migration and nonconvergence; completed
migrations change resource availability and trigger dependent migrations. Their
comparison of identical bandwidth-sharing migrations motivates sequential
execution of resource-dependent transfers and concurrency of independent ones.
Requests and urgency/deadlines are modeled dynamically.

**Novelty boundary:** sequential migration being better than arbitrary concurrency,
resource release/dependence, and responding to arbitrary arrival times are not
new. The candidate's counterfactual requirement is different: at *every* normal
time, a request must be feasible, and the objective measures the maintenance
cost **before** a request rather than the performance of an arriving request
queue. This distinction alone is not a novelty proof.

## 4. Hoffmann et al., Megaphone: Latency-conscious state migration for distributed
streaming dataflows (arXiv:1812.01371v2, 18 March 2019)

Primary full text:
https://arxiv.org/html/1812.01371v2
Abstract/version record:
https://arxiv.org/abs/1812.01371

**Inspected:** introduction; sections 2.1-2.3; formal correctness, migration and
completion properties in 3.2; migration strategies in 3.3; proof sketch in 3.4;
evaluation objectives in 5. We did not reproduce or independently audit their
experiments.

Megaphone subdivides migration at configurable granularity and prepares migration
coordination in advance, multiplexing fine-grained state movement with ongoing
processing. It compares all-at-once, fluid and batched strategies, and measures
both non-migration overhead and migration latency.

**Novelty boundary:** fine-grained handover, preparation ahead of time, and
overhead even when not migrating already have a close systems precedent. Our
homogeneous worst-case theorem is not a replacement for their correctness
mechanism. Its independently switchable units would require such a correctness
argument in any actual system.

## 5. KubeVirt official live-migration documentation

Primary current documentation:
https://kubevirt.io/user-guide/compute/live_migration/

**Inspected:** migration-strategy descriptions, convergence, auto-convergence,
post-copy behavior and service-pausing options. This is a live documentation
snapshot, not a version-frozen research paper.

The documentation distinguishes migration strategies and conditions under which
running-state copying does not converge. Alternative strategies have different
service and dependency consequences.

**Novelty boundary:** the cold-start nonconvergence case in our model must not be
presented as a general impossibility of live migration. Allowing throttling,
pausing, temporary extra resources or continuing source dependence changes the
problem. Those alternatives are excluded because the chosen guarantee forbids
them, not because they do not exist.

## 6. Leads not fully inspected

Stearley et al., Does Partial Replication Pay Off? (DSN Workshops, 2012),
DOI 10.1109/DSNW.2012.6264669; IEEE record:
https://ieeexplore.ieee.org/document/6264669/

The title and bibliographic record were located, but the primary full paper was
not accessible through the retrieved publisher page in this pass. It must not
be represented as fully reviewed or used to assert what its theorems omit.
Related replication/maintenance and resource-dependent scheduling literature
still needs a theorem-level audit.

## Current claim ledger

| Claim | Status |
|---|---|
| Ongoing operation can make removal difficult | Established background; not new |
| Migration bandwidth must compete with state updates | Established; explicit constant-rate formula located |
| Appropriate sequential migration can beat parallel migration | Established; not claimed new |
| Fine-grained/proactive migration and its steady overhead | Established; not claimed new |
| Exact Proposition 1 in the stated ideal homogeneous model | Proved in NOTE.md; novelty not established |
| Exact arbitrary-history recurring-cost Theorem 2 | Proved in NOTE.md; candidate residual contribution |
| Partial/rotating snapshots cannot improve this minimax mean bound | Part of Theorem 2; depends on fixed-rate erosion |
| Staircase is universal | False; section 8 gives a smooth countermodel |
| Real fallback autonomy follows from copying state | Not shown; application obligation |
| Publication-ready contribution | Not established |
