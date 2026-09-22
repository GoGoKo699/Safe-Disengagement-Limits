# Pass 17: the charged bottleneck, completion embargo, and service meaning

22 September 2026. Continuation base:
`16dca7e14950e13e4a292600ee39b2a3aeca9ec1`.
This is an internal assumption and significance audit, not an engineering
validation or an external referee report. It reads the current manuscript's
model, seriality and concentration proofs and introduction, the full pass-15
meaning and assessment notes, and the full pass-6 interface and pass-8
pipeline-policy notes. No historical checkpoint is changed.

## 1. Finding

The precise constrained resource is **pre-request input through a specified
shared bottleneck**, needed to preserve enough perishable preparation for a
later common deadline. It is not the total cost of independent essential
service, the total energy of the primary and receivers, or an unavoidable
cost of keeping a controller removable under every service-preserving policy.

Two parts of the story can be separated exactly:

1. Positive capacity release and controller removal are not needed for the
   concentration theorem. It already applies when every `a_i=0`, and its
   mathematical interpretation can be command-triggered completion of a
   portfolio of perishable jobs with a constant preparation capacity.
2. Charging every preactivation input to the source and forbidding absorbing
   completion before the command are necessary to the *stated source-cost
   interpretation*. If either independent premaintenance or early permanent
   activation is admissible at no cost to that objective, a positive source
   upkeep lower bound can disappear. Sections 4 and 5 give exact policies;
   this is stronger than saying that those possibilities need discussion.

There is consequently a coherent minimal ideal scheduling class, stated in
section 3, and a negative application finding: the existing thermal-reserve
illustration has not established why its receivers cannot independently
maintain preparation or activate early while preserving the desired service.
It does not yet justify a physical lower bound on the source's cost. This
finding does not refute the theorem under its declared control class.

## 2. Assumption-to-conclusion map

Write `L(p)=sum_i gamma_i p_i`. The static result minimizes `L` over states
whose worst-case completion time `F(p)` is at most `H`. The recurring result
additionally restricts normal controls and uses `Q=sum_i p_i` as bounded
storage. The following distinctions should be visible in the paper.

| Assumption | Conclusion it actually supports | What is not implied when weakened |
| --- | --- | --- |
| Independent scalar states `0<=p_i<=M_i`, complete for deciding completion, with no hidden activation path | The stated feasible set and the pair exchange describe all admissible preparation states | A sufficient certificate or conservative threshold alone does not characterize all physically feasible exits |
| Positive proportional loss and maintenance price `gamma_i` on `p_i` | The concentration exchange is strictly concave or strictly decreasing, excluding two partial coordinates in every minimum | Arbitrary independent investment prices do not inherit the derivative sign; smooth monotone loss alone is insufficient by the quadratic counterexample |
| All relevant input enters through the single rate budget; input is divisible and has no additional module rate caps | Full-rate serial schedules are admissible; normal total input obeys the storage inequality | An independently powered input is not charged source upkeep; additional rate limits can invalidate the serial construction |
| The simultaneous maximum feedback `rho_i=gamma_i p_i` is an admissible history for every policy | It provides the matching robust lower bound on exit time and upkeep | An upper envelope for a smaller physical uncertainty family only proves a conservative achievable design |
| Every smaller admissible loss obeys the same statewise envelope and input/transfer comparison | A maximum-loss schedule and maintained target guarantee the deadline on every allowed history | A mean drift is not a pathwise deadline guarantee |
| Completion can be committed at `p_i=M_i`, then removes its source preparation obligation | Completed modules can be omitted from later schedules, and initial full modules exit at zero time | A merely hot receiver with source-dependent control, fuel, logging, or unfinished obligations has not completed this interface |
| Completion releases `a_i>=0` immediately, independently of other modules | Earlier completion never reduces capacity; the proof uses `b_k>=b_j` | Positive release is not needed for concentration, and the proof supplies no general claim for capacity that decreases after completion |
| No module completes or transfers during normal mode | The same `n` unfinished obligations remain at every counterfactual request; `Q'<=s-u-L(p)` applies to a fixed readiness problem | A service-preserving early permanent transfer can remove the very obligation whose maintenance is being lower-bounded |
| Paid initial preparation and separately paid receiver operation | Stationary upkeep achieves the initialized long-run value, with receiver costs outside that value | This does not prove finite cold startup, finite initialization cost under the normal budget, or total-system optimality |
| Bounded stored preparation | A one-time reserve cannot improve asymptotic optional throughput beyond `s-C(H)` | This does not imply finite arrival at a stationary optimum: the critical three-module example disproves that implication |
| Cooperative source throughout the grace period, instantaneous service-preserving switching, paid independent continuation | Completion of all modules can be interpreted as safe source departure within the specified service interface | Neither abrupt-failure tolerance nor a network ownership protocol follows from the resource equations |

This is a map of the present arguments, not a list of conditions proved
logically necessary for every conceivable concentration theorem. For example,
some specific models with module rate limits might still concentrate, but
that would need its own proof.

## 3. Minimal ideal class and the zero-release reduction

A minimal class is a **command-gated perishable preparation service**:

- There are independent jobs. Each job has a bounded amount of useful
  preparatory work, lost proportionally to its current amount. Restoring that
  work consumes one common, explicitly charged preparation resource.
- Before a command, a job remains in the preparation phase even if fully
  prepared. Its preparation continues to deteriorate. A completion operation
  is not yet authorized.
- The command opens a completion phase. At its threshold a job can be
  completed instantaneously. Completion is absorbing and eliminates further
  calls on the preparation resource. Every job must complete within `H` of
  the command; the command may arrive at any time during the promised
  readiness interval.
- Optional pre-command work competes for the same resource. Initialization is
  paid separately. There is no independent input channel or uncharged action
  that suspends deterioration while retaining command readiness.

These are an ideal contract and dynamics, not claims about observed equipment.
In particular, the completion embargo is part of what this service sells:
preparedness for a future command while remaining in the pre-completion mode.
A reader who only wants eventual completion and allows it immediately has a
different, easier problem, analyzed in section 5.

**Exact zero-release reduction.** Set every `a_i=0` in the current model.
Interpret a request as the common completion command and transfer as job
completion. Leave `p_i`, `M_i`, `gamma_i`, `s`, allocations, loss histories,
and the deadline unchanged. Every original admissible trajectory maps to a
trajectory of the ideal job service, and conversely. The feasible initial
vectors, value `F(p)`, upkeep objective and policies are identical. This is
an equality of models, not an analogy or a new theorem.

The concentration proof continues to be strict: for the two chosen partial
jobs its capacities satisfy `b_k=b_j=s>D_j`, so the derivative in the
nonconcave case is still negative. No positive release enters the strictness.
The nonlinear-loss counterexample also distinguishes preparation geometry
from serial scheduling; release is not an explanation of that distinction.

Thus the central result is about the interaction of proportional perishability,
its linked maintenance prices, a completion deadline, and an absorbing
completion operation. Nonnegative releases extend the allowed scheduling
architecture. They do not create the concentration principle. Nothing in
this reduction requires an intelligent controller, a power generator, an
information copy, a network, or an agent's willingness to be shut down.

The reduction narrows the contribution claim and helps choose comparisons:
initial investment and deteriorating-work scheduling are central prior art.
It does not establish novelty or practical demand for the ideal contract.
A theory paper can study this precise class; a controller-removal application
still needs the additional service mapping rather than inheriting it from
terminology.

## 4. Exact counterpolicy: independent premaintenance

Consider the one-module instance

$$M=1,\qquad \gamma=1,\qquad s=2,\qquad a=0,
\qquad H=\log(3/2).$$

Under the original maximum-loss dynamics, allocating the full exit capacity
gives `p'=2-p`, so

$$F(p)=\log(2-p),\qquad 0\leq p\leq1.$$

This is also a lower bound on every schedule by scalar comparison. Therefore
`F(p)<=H` exactly when `p>=1/2`, and

$$C(H)=\tfrac12,\qquad u^*_{\mathrm{original}}=\tfrac32.$$

Now enlarge the controls by allowing an independent input `w` with
`0<=w<=1/2`, not counted against the source budget `u+v<=2`. The preparation
dynamics become `p'=v+w-rho`, with the same reflected cap and loss envelope
`0<=rho<=p`. After paid initialization at `p=1/2`, set `v=0`, `w=1/2`, and
`u=2` in normal mode. Under maximum loss the preparation is constant; under
smaller losses it stays at least `1/2`. On a request set `u=0`, turn off `w`
if desired, and use the original rate-2 exit schedule. Every request still
meets the original `H`.

Thus the enlarged policy class achieves the maximum normal optional rate
`u=s=2`, exceeding the claimed original value by exactly `C(H)=1/2`.
All essential behavior assumed by the original transfer primitive is
unchanged. The difference is an additional allowed resource route. The
independent input costs `1/2` per unit time: the policy eliminates *source*
maintenance, not maintenance in the total system.

More generally, an independent input capable of supplying
`w_i=gamma_i p_i^*` maintains any chosen ready target without source
preparation; a source policy need not pay `C(H)` in that enlarged class.
Whether such input is physically possible is an interface question. An
independent supply that cannot couple to preparation does not automatically
provide this control. Conversely, the mere existence of a later independent
supply does not prove that earlier coupling is impossible.

This counterpolicy identifies precisely what an application must show:
not merely that a primary *can* maintain the reserve, but that admissible
alternatives cannot maintain it without consuming the resource being
optimized, or else that their cost is included in the objective.

## 5. Exact counterpolicy: early permanent activation

Suppose, instead, that transfers may occur before a removal request, preserve
the same essential service, remain permanent, and impose no separately
charged objective cost. Keep paid initialization, as in the initialized
throughput theorem. Initialize all modules at their thresholds and transfer
them immediately. Thereafter no source preparation obligation remains. Every
later removal request has completion time zero.

Even if optional performance is still capped at the original `s`, this policy
achieves `u=s` indefinitely. If normal optional work may additionally use all
released capacity, it achieves `u=s+sum_i a_i`. The latter is a changed budget;
the former already refutes any universally positive source-upkeep requirement
based only on preservation of the stated essential service. The one-module
instance in section 4 gives a strict comparison with its original `C(H)=1/2`.

The policy uses finite paid initial preparation, just as the original
stationary achievability argument does. It does not claim that all thresholds
can be reached from cold under an insufficient normal rate budget. Nor does
it guarantee readiness during an unprepared startup. Those are separate
contracts and cannot rescue a universal initialized lower bound against this
counterpolicy.

Accordingly, “the primary must own the service until a command” is a
substantive normal-mode requirement, not a consequence of the essential
service alone. It can define the ideal command-gated problem. For a practical
application it must be justified by the actual requested normal function or
by charged receiver operation, switching, wear, fuel, or other costs. Adding
such costs would be a different optimization problem; none is silently
inserted here merely to preserve a positive result.

This is the same policy-domain issue exposed by the pass-8 early-freeze
counterpolicy. In that other model, stopping future source-owned mutations
can make a frozen copy cheap while preserving the stated bounded-response
contract. Here early absorbing completion removes preparation obligations.
The mechanisms differ, but both invalidate extrapolation from a restricted
control class to all service-preserving protocols.

## 6. Status of the thermal interpretation

The pass-15 heat balance yields `p'=v-gamma p` by an explicit change of units.
That conditional algebra remains useful. It does not establish the
threshold-to-autonomy interface, the availability of every full-rate serial
input, negligible activation latency, or the absence of the two controls
above. A source might be required for preactivation because independent
supply only becomes usable after a genuine activation process; alternatively,
an auxiliary independent heater might be possible. No equipment-specific
facts in the inspected record settle this choice for the complete model.

In particular, postactivation self-sustenance does not itself prohibit early
activation. If early activation can preserve all essential service, the
source-cost question must include it or explicitly require the nominal
preactivation mode. Calling an independent continuation resource “paid” also
does not identify its marginal premaintenance or early-operation cost.
A one-time provisioning cost is compatible with free later operation in the
paper's source-only objective.

No new physical application claim is made in this pass, and no external
source was newly inspected. The pass-15 source-access record remains exactly
as stated there: Flatley--MacKay--Waterson section 1.1 and Proposition 2.1
were previously inspected for linear storage precedent, and Shao et al. was
inspected at abstract/metadata level only. Neither is upgraded here to a
validation of this combined interface. The full pass-6 and pass-8 audits are
used for their own explicit conditional constructions, not as proof of a
physical controller-removal implementation.

## 7. Concrete manuscript changes and assessment

The following changes are justified now; no new equipment claim is needed.

1. State near the model that `C(H)` is maintenance through the declared source
   bottleneck, conditional on normal-mode noncompletion. It excludes receiver
   provisioning and independent continuing operation.
2. State near the concentration theorem or introduction that it includes
   `a_i=0`: positive release and controller removal are applications of the
   structure, not causes of concentration. Use the exact job-service reduction
   to describe the minimal ideal interpretation in a short paragraph.
3. Replace the generic concern about independent receiver maintenance with
   the one-module counterpolicy or its short statement. Allowing independent
   premaintenance can remove the source-upkeep penalty without reducing total
   upkeep. Allowing free early permanent transfer can eliminate the standby
   problem entirely.
4. Keep the loss-envelope distinction explicit: a safe conservative design
   and a physically necessary resource minimum require different evidence.
5. Preserve the paper's present title and scheduling focus. Do not add a
   thermal deployment promise or relabel the result as an unavoidable
   AI/controller-removal cost. The related-work discussion should continue
   to prioritize deteriorating-work and controllable-investment results.

The mathematical claim has a clear interpretation within its ideal class:
minimum charged upkeep is concentrated despite heterogeneous decay, whereas
smooth nonlinear deterioration can require distributed preparation. The
current record has not established a physical essential-service class in
which the whole admissible control set matches that ideal contract. Submission
readiness therefore still requires a contribution judgment for the ideal
scheduling problem or a separately justified application mapping; the thermal
analogy alone does not settle it. Adding unmotivated receiver-cost parameters
would postpone that judgment rather than resolve the present objection.
