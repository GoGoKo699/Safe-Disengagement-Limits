# Passes 23–25: contribution decision after viability and drain tests

23 September 2026. Repository research only; the earlier manuscript remains
unchanged. This note separates proved model statements, primary-source
reductions, and unresolved significance. It supersedes no historical proof by
silently editing it.

## 1. What survives the viability comparison

The [primary comparison](2026-09-23-pass23-viability-prior-art.md) expresses
normal operation exactly as a positive linear control system with a simplex
input constraint **and a box path constraint**. Reflected input waste can be
discarded without changing trajectories. For upward targets and readiness
regions, maximal-loss reachability/viability suffices for robust existence by
replaying its controls and using scalar comparison.

Cold startup into indefinite readiness is membership of the cold state in a
capture basin of a viability kernel. Finite domination of an upkeep optimum
is capture of a smaller, invariant upward target. Those are standard concepts;
the general distinction between them is not an S1 contribution. The inspected
Aubin–Catté framework applies directly at this level. The displayed smooth
bang-control theorem of Broucke–Turriff does not apply to the direct full-input
encoding because its relative-degree assumption fails. This excludes that
encoding only; it is not a claim against every possible reformulation.

The [linear reachability note](2026-09-23-pass23-positive-reachability.md)
identifies the exact uncapped support-function reduction to Girard–Le Guernic.
An explicit counterexample shows why intersecting the uncapped terminal set
with the box does not enforce the path constraint. The constrained endpoint
set is still compact, convex and downward closed. None of these standard
linear-control facts proves the schedule-generated S1 dimension boundary.

In particular, the source comparison gives a two-dimensional non-S1 ready
region with the same positive normal upkeep and resource constraint where
finite warmup permits indefinite readiness but its unique optimum is never
finitely dominated. Thus the S1 theorem for at most two modules needs the
particular exit-schedule geometry. It is not a generic positive-systems fact.
The [internal proof review](2026-09-23-pass23-proof-review.md) finds no defect
in the existing S1 two-versus-three-module result, within its stated domain.
The result compares **cold-state membership**, not equality of entire capture
basins or viability kernels.

## 2. Persistence does not remove the precision limitation

The [calibrated family](2026-09-23-pass24-critical-family.md) proves that the
three-module separation is not restricted to the earlier numerical fixture.
Strict sufficient inequalities give a unique critical concentrated optimum,
an all-policy obstruction to finite domination, and an explicit uniform tail
bound for a finitely warmed ready trajectory. The independent parameters range
over an open set while the deadline is calibrated to keep `C(H)=s`.

That calibration is essential. No open set in an independently varied deadline
is claimed. Any fixed positive request-time deficit still requires strictly
more upkeep than `s`. The reviewed dissipation argument bounds even dynamic
residence in the tolerance-ready region by

$$\text{duration}\leq\frac{\sum_iM_i}{\gamma_{\min}\epsilon}.$$

This is an elementary consequence of the existing precision theorem, not a
new viability principle. The critical separation is retained as an ideal
model boundary and a secondary structural result. It is not promoted as a
tolerance-resistant operating benefit or used to clear publication priority.

## 3. A load-bearing handoff assumption fails a stronger test

The next pass returns to the concentration candidate's service interface.
The [proportional-drain counterexample](2026-09-23-pass25-proportional-drain.md)
uses the previously defined immutable residual-drain interface: ownership
handoff stops preparation loss, while a separately timed drain retains the
source reservation before releasing capacity. New essential requests are
already independently served; immutable old obligations and their resource
reservation remain explicitly accounted for.

With two modules, proportional coefficients `(2,1)`, preparation caps
`(1/2,3)`, spare budget `4`, and deadline `log(10)`, drains
`(log(100/11),log(10/3))` produce the unique minimum-upkeep ready state

$$p^*=(37/200,7/5),\qquad L(p^*)=177/100<4.$$

Both coordinates are partial. A discounted-work lower bound covers arbitrary
parallel, interrupted, adaptive preparation policies on the maximal-loss
history. A matching policy guarantees the deadline on all admissible loss
histories. Strict maintenance slack supplies finite normal cold startup and
positive recurring optional throughput. This is not another critical-budget
artifact and does not rely on independent prices or nonlinear loss.

It also survives a fixed request-time deficit: for
`0<=epsilon<=63/200`, the unique nominal minimum is `p*+(epsilon,epsilon)`
and its upkeep is `177/100+3*epsilon`. Both coordinates remain partial below
the upper endpoint, and upkeep stays strictly below `4` even at that endpoint.
Above it, the first module's scalar deadline barrier makes readiness
infeasible. Thus this particular failure is not removed by the precision
contract that defeats the critical-viability benefit.

The mechanism has an exact limitation: no drain can finish before either
required handoff in this fixture. The unequal drain tails therefore impose
unequal preparation deadlines under constant spare capacity. Delayed release
does not itself assist the attaining preparation. Positive release rates may
be arbitrary because their release occurs too late to change this deadline
problem. The displayed dual argument is elementary discounted allocation;
no new general optimization method is claimed.

For a **common** drain duration `ell` with `ell<=H<=2*ell`, all handoffs must
occur by `H-ell` before any release can help. Readiness then reduces exactly to
instantaneous S1 with zero releases and deadline `H-ell`; the established
concentration theorem survives. Hence positive delay alone is not proved to
destroy concentration. The unequal induced deadlines in the counterexample
are a specific obstruction, and the common-drain regime allowing useful
intermediate releases remains separate.

## 4. Revised decision and next question

The repository now has a more precise assumption-to-conclusion map:

| Statement | Disposition |
|---|---|
| Generic viability can differ from finite capture of an optimum | Standard framework and elementary examples; not a contribution claim |
| Exact S1 two-versus-three-module critical boundary | Internally checked, persists on a calibrated family; priority and operational significance unresolved |
| Critical indefinite readiness with fixed positive shortfall tolerance | Impossible at the unchanged budget, including dynamic policies |
| Proportional loss alone forces one-partial upkeep concentration | False with the accounted heterogeneous residual drains |
| Instantaneous-handoff concentration, including positive tolerance | Existing theorem remains valid in its original model |
| Every positive residual drain destroys concentration | Not established; common long drains reduce to the preserving zero-release case |
| Current project has established publication novelty or an application | Still unresolved |

The next focused task is to distinguish heterogeneous preparation deadlines
from delayed, endogenous capacity release. Test common positive drains in the
remaining `H>2*ell` regime, with a bounded comparison to allocation/scheduling
results before a new general theorem or solver is attempted. A direct prior-art
reduction, an all-policy counterexample, or a proved restricted preservation
result would each answer a meaningful part of this question. Merely evaluating
serial schedules would not: the earlier fixed-loss drain examples already
show why that policy restriction is unsafe.

Manuscript work remains deferred. These findings narrow the candidate rather
than establish a submission-ready result.
