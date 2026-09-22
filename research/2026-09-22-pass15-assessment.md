# Pass 15: referee assessment of the concentration paper candidate

22 September 2026. Continuation base:
`bb1e34f41338745c88ae486d493a053c658fb3d1`.
This assessment reads the complete current pass-11 unequal-decay theorem and
source audit, pass-12 frontier, pass-13 barriers, and pass-14 critical-target
startup proofs. It subsequently reads the complete pass-15 critical-viability
and two-module boundary notes, including the three-module algebraic
certificate. It revisits the pass-10 quadratic separation and the pass-6
and pass-8 interface findings. It is an internal scientific assessment, not
an independent human referee report or a novelty certification.

## 1. Decision

**Begin a narrow working manuscript now.** The reason is the existence of a
coherent theorem and a meaningful boundary, not completion of a checklist or
failure to find an identical paper. Further parameter extensions are less
valuable than testing whether this argument can stand as one clearly motivated,
fully attributed paper. This decision authorizes no submission or formal
release, and the current evidence does not justify calling the paper
submission-ready.

The central claim should be:

> In the independent instantaneous-handoff model with positive module-specific
> proportional loss, every minimum-maintenance preparation state meeting a
> robust removal deadline has at most one partially prepared module.

The main companion results are an explicit finite frontier, the necessity of
allowing a cold prefix when decay rates differ, and an exact quadratic-loss
counterexample to the concentration principle. A suitable working title is
*Concentrating perishable preparation for deadline readiness*. This identifies
the actual mathematical object without claiming a universal law of safe
controller removal.

The manuscript should be written around that claim now, with its unresolved
attribution and interpretation recorded conspicuously in development status.
It should not be a compilation of all fifteen research passes. If the focused
presentation reveals that the concentration theorem is only a direct known
special case or has too little meaning outside its assumptions, that negative
decision must remain available.

## 2. What has been learned mathematically

The optimization is over an initial vector, not merely an exit order:

$$C(H)=\min\left\{\sum_i\gamma_i p_i:
0\leq p_i\leq M_i,\ F(p)\leq H\right\}.$$

The full-state serial theorem makes `F` an exact minimum over finite serial
orders even though the original policy class allows adaptive, fractional,
parallel, and preemptive allocations. The concentration proof then removes
continuous degrees of freedom from a minimizing state. It does not assume
that the controller was already choosing a ready/cold policy.

Its decisive step is to vary two consecutive partial coordinates in an
attaining serial schedule while preserving the completion time of the later
one. Intervening cold stages retain fixed durations. The later suffix is
therefore unchanged. The varying maintenance cost has the form

$$c(x)=\gamma_jx+K(A-\gamma_jx)^{\gamma_k/\gamma_j}-Q.$$

When the exponent is below one, strict concavity rules out an interior local
minimum. When it is at least one, the available-capacity inequalities make
the derivative strictly negative. This dichotomy works for every pair of
positive decay coefficients, rather than requiring one common exponential
clock. Actual finite accessibility of the chosen stages supplies the needed
positive denominators; a global ample-capacity assumption is unnecessary.

The strict conclusion concerns **every** optimizer. The associated cold-prefix
condition also has useful content: a cold module preceding the partial module
in an optimal state's witnessing order must have a strictly larger decay
coefficient. This is not a complete index policy, and the pass-12 two-module
example proves that eliminating such prefixes can worsen the global optimum.

After concentration, a full subset, a cold prefix, one distinguished partial
module, and a cold suffix suffice. Pass 12 computes the required partial
amount explicitly and optimizes the two cold segments by ordinary subset
recurrences. Its `O(n*3^n)` count is a real scalar-evaluation count, not a
polynomial-time or exact rational-arithmetic claim. The common-rate case has
the stronger `O(n*2^n)` rational transformed-deadline specialization. Neither
subset dynamic programming nor solving a scalar exponential equation should
be advertised as an independent algorithmic invention.

The quadratic counterexample is especially valuable. It proves that all
concentrated states are infeasible or more expensive than a feasible
two-partial state, using exact work bounds over the full policy class. Serial
optimality still holds there. Thus the paper can distinguish two structural
questions that a reader might otherwise conflate: concentrating post-request
service and concentrating pre-request investment. Smoothness, monotone loss,
identical modules, and seriality do not by themselves imply the latter.

## 3. What should and should not be claimed against prior work

The [pass-11 source audit](2026-09-22-pass11-prior-art.md) supplies exact
substitutions and inspection scopes, rather than a title-only comparison.
Its conclusions remain binding:

| Ingredient | Assessment for the proposed paper |
|---|---|
| Common-rate fixed-order concentration | Standard one-constraint box LP after the proved affine transform; Shioura–Shakhlevich–Strusevich's inspected greedy theorem includes it. |
| Affine resource/deterioration recurrence | Wei–Wang–Ji contains an exact restricted serial recurrence under a change of clock; this is a genuine prior-art reduction. |
| Nonpreemption with deteriorating partial progress | Gehlot–Sundaram–Ukkusuri has an inspected nonpreemption proof in a discrete repair model with absorbing failure. Older Glazebrook results remain a closer unresolved theorem-access issue. Do not claim a new nonpreemption principle. |
| Unequal-rate minimum-upkeep concentration | The inspected LP and common-linear-deterioration results do not establish its nonlinear two-coordinate exchange. This is the focused residual candidate, not a certified first result. |
| Recurring optimum from minimum upkeep | The bounded-storage/dissipativity argument is established methodology; its value here is the now-explicit quantity it connects to performance. |

The objective weights are substantive. They are exactly `gamma_i`, the rates
needed to maintain preparation under maximum loss. An arbitrary independent
linear price vector does not inherit the derivative sign without another
proof. Similarly, capacity release is compatible with concentration but is
not its cause: the theorem includes `a_i=0`, and the exchange chiefly uses
nondecreasing available capacity. A claim that released resources create a
new concentration principle would overstate the argument.

The remaining comparison is therefore specific: does a prior nonlinear
controllable-work or initial-investment theorem already exclude two interior
investments under this deadline geometry and these linked maintenance costs?
Showing that an older source has some nonlinear resource function is not an
exact reduction. Conversely, changing vocabulary from processing time to
readiness would not create novelty if its feasible set, objective, and policy
class map exactly.

### 3.1 Bounded nonlinear controllable-work comparison in this pass

X.-J. Li, J.-J. Wang and X.-R. Wang (2015), *Single-Machine Scheduling with
Learning Effect, Deteriorating Jobs and Convex Resource Dependent Processing
Times*, Asia-Pacific Journal of Operational Research **32**, article 1550033,
DOI `10.1142/S0217595915500335`.
[Full author-uploaded manuscript](https://www.researchgate.net/publication/284788654_Single-Machine_Scheduling_with_Learning_Effect_Deteriorating_Jobs_and_Convex_Resource_Dependent_Processing_Times).

**Inspected:** complete section 2 and section 3, including Lemmas 1–3,
equations (1)–(7), Algorithm 1 and Theorem 1's proof. Jobs are nonpreemptive,
with duration

$$P_j(t,u,r)=((a_j/u_j)^k+b t)r^\alpha,$$

where `u_j>0` is nonrenewable investment, `k>0`, `b>=0` is common, and
`alpha<=0`. Theorem 1 minimizes a weighted scheduling-cost/resource-cost sum.
Equation (4) separates fixed-order costs into convex inverse-power resource
terms. Lemma 2 differentiates them, and Algorithm 1 uses rearrangement for
sequencing. Under positive cost coefficients, the allocation formula gives
positive investment to every job. This is not an inspected fixed-deadline
concentration theorem. Section 4 and other sources cited in its introduction
are not certified by this inspection.

Our direct comparison uses the S1 stage duration from initial preparation
`p`, after waiting until time `t`, at fixed accessible capacity `b`:

$$\tau_i(t,p;b)=\frac1{\gamma_i}
\log\frac{b-\gamma_i p e^{-\gamma_i t}}{b-\gamma_iM_i}.$$

Its interaction between waiting and initial preparation satisfies

$$\frac{\partial^2\tau_i}{\partial t\,\partial p}
=\frac{\gamma_i b e^{-\gamma_i t}}
 {(b-\gamma_i p e^{-\gamma_i t})^2}>0.$$

In the inspected duration above, the corresponding mixed derivative in
`t,u` is zero. Thus the direct identification of resource `u` with initial
preparation `p` fails before considering finite caps or capacity releases.
This calculation excludes that simple model substitution, not every possible
transformation or every theorem in the literature. In particular, it does
not supersede the exact common-rate clock substitution already recorded in
pass 11.

This source also discourages a broad novelty claim for dispersed optimal
investment under nonlinear resource laws. The S1 quadratic example matters
as a precise counterexample to S1's concentration theorem, while the general
phenomenon of nonlinear costs producing distributed allocations is familiar.

Two additional close records remained partial-access leads. The
[Li–Wang *Scheduling jobs with deterioration effect and controllable processing time* page](https://www.researchgate.net/publication/309450142_Scheduling_jobs_with_deterioration_effect_and_controllable_processing_time)
exposes a first-page publisher preview, not its claimed fixed-deadline proof.
Wang, Zhang and He's
[*A unified analysis for scheduling problems with variable processing times*](https://www.aimsciences.org/article/doi/10.3934/jimo.2021008),
JIMO **18** (2022), 1063–1077, has accessible model tables, but its full-text
link explicitly requires subscription/payment. Neither theorem was treated
as inspected. A publisher preview of Leyvand–Shabtay–Steiner (2010), DOI
`10.1016/j.ejor.2010.02.026`, likewise did not expose a complete proof.
No payment, outside request, or repeated blocked-endpoint search followed.
These access limits leave attribution uncertainty; they do not support a
claim of literature-wide absence.

## 4. Ideal-model meaning and the operational limitation

The mathematical interpretation is coherent: useful preparation is a
perishable quantity, preparation and optional work share a fixed normal
budget, a removal request suspends optional work, and independently complete
modules may transfer and release source reservations. The theorem answers
whether minimum ongoing maintenance should be spread across many incomplete
modules. Under the specified proportional law it should not. Under the
quadratic law it sometimes must be.

That is presently an **ideal scheduling/control interpretation**. The
repository has not supplied a physical replication protocol that realizes
all of the model's assumptions. In particular:

- A finite-record overwrite process with conditionally uniform addresses can
  give expected proportional invalidation. It does not supply the pathwise
  bound `rho_i<=gamma_i*p_i`, or justify simultaneous maximal losses on every
  module, used by the robust theorem.
- With positive information delay, a local acknowledgement does not imply
  that the receiver already has sufficient state. Independent logs or queued
  requests can change the relevant departure deadline, but their response,
  storage, replay, and coordination costs must be paid.
- Reaching a scalar preparation cap is not itself a proof of ownership
  transfer, accepted-request preservation, or independent essential service.
  The fence and the instant release of `a_i` remain assumed primitives.
- Allowing an early freeze changes the admissible control class. The pass-8
  counterpolicy shows that sufficient response slack can remove the recurring
  preparation cost of another proposed benchmark. A service contract cannot
  silently exclude that option just to preserve a lower bound.

The full-service interface must therefore remain an explicit ideal assumption
in a working manuscript. Calling it a VM-migration model or substituting an
empirical dirty-page rate would not repair these issues. Nor should a
theorem about an expected stochastic drift be presented as a pathwise removal
guarantee. A later implementation or approximation theorem could justify a
particular application, but none is proved by the current notes.

This limitation narrows the suitable claim; it does not logically refute the
mathematics. A theoretical paper can study an ideal resource model when the
question and structural information are sufficiently useful. Whether the
present idealization has that significance is a genuine referee risk, not
something solved by adding examples or more parameters.

## 5. Initialization and startup: preserve the distinction, limit the scope

Pass 14 materially improves the interpretation of paid initialization. At
exact maintenance equality, a concentrated target with a partial coordinate
is reachable from cold in finite normal time precisely when some full target
coordinate decays faster than that partial coordinate. A nonzero pure-full
critical target is unreachable. The proof both constructs a predecessor
with strict maintenance slack and supplies a separating inequality in the
opposite case. The two globally certified positive-deadline examples show
that equality `C(H)=s` alone does not decide cold startup.

The new [critical-viability note](2026-09-22-pass15-critical-viability.md)
proves that the fixed-target criterion does not characterize entry into
indefinite readiness. Its exact three-module instance has a unique critical
upkeep optimum that is unreachable and cannot be dominated after any finite
cold warmup. Nevertheless, a finite warmup followed by fixed normal
allocations gives an indefinitely ready trajectory converging to that optimum.
Preparation in a third, slowly decaying coordinate compensates for the
remaining deficits in the optimum's support. The deadline certificate holds
for every subsequent request time and every allowed loss history; this is
stronger than merely plotting an asymptotic trajectory.

The same note proves that every maximal-loss critical ready trajectory
converges to one of finitely many minimizing states. Compactness, finite
excess-upkeep integral, and uniform Lipschitz bounds supply that argument.
The construction shows why this convergence does not imply finite target
reachability. The [two-module companion](2026-09-22-pass15-two-module-boundary.md)
proves necessity of a reachable optimum with at most two modules in its
finite-cold-exit domain. Thus the three-module separation identifies a real
dimension boundary, rather than a failure caused only by a chosen target.

This is a stronger initialization companion than a generic observation that
warmup costs resources. It separates exact long-run value, stationary
attainment with paid initialization, and viability after finite cold entry.
Convergence and dissipation are standard ideas; the contribution under
assessment is the explicit separation inside this model, not a new general
turnpike or asymptotic-controllability principle. These results should not
displace concentration as the main claim or open an indefinite search for a
complete viability classification.

For the core paper, state initialization before the recurring throughput
claim and include the strict-slack finite warmup construction or its short
corollary. Give the critical viable-trajectory separation as a short boundary
result, with the algebraic certificate and smaller-dimension classification
in an appendix. Threshold-closure details can also remain supplementary
unless needed to explain an equilibrium barrier in the main proof.
The theorem does not guarantee removability during an unprepared warmup.

## 6. Concrete manuscript scope and referee risks

The body should contain the model and quantifiers, the serial reduction as a
supporting theorem with careful attribution, the unequal-rate concentration
theorem, the finite frontier, and the two separating examples. The quadratic
example should sit next to the positive theorem, where it explains its
assumptions. The cold-before-partial example should accompany the algorithm,
where it explains why the larger candidate class is necessary. Recurring
throughput is a consequence of these results and the known storage argument.

The strongest anticipated objections are:

1. **Priority:** an older nonlinear controllable-work result may absorb the
   concentration exchange, or an older nonpreemption proof may require only
   a routine extension to cover the serial reduction. The known reductions
   must be shown, not hidden in broad related-work language.
2. **Model significance:** the precise pathwise proportional loss and perfect
   transfer primitive lack an established essential-service implementation.
   The paper must be assessed as an ideal theoretical contribution until
   that gap is closed.
3. **Scope inflation:** a short exchange plus exponential enumeration is not
   automatically a broad new scheduling theory. The nonlinear separation and
   interpretation must explain what the reader learns beyond a formal variant.
4. **Endpoint sensitivity:** initially full coordinates can transfer at once,
   whereas strictly partial coordinates may face an equilibrium barrier.
   Near-full preparation is not interchangeable with full preparation.
   Proofs and examples must keep these cases explicit.
5. **Evidence:** the local reference code uses floating comparisons for general
   unequal rates. Exact analytic examples and written proofs carry the claims;
   enumeration is supporting verification, not a certified solver or proof
   over continuous parameters.

The next useful artifact is a complete short working draft with these claims
and limits visible, followed by an adversarial read against the closest full
sources. No large simulation is needed to make that draft reviewable. Novelty,
model significance, complete presentation, and a checked paper artifact still
have to be established before the repository can meet its submission standard.
