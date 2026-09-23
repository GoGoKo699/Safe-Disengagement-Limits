# Pass 29 opening: the cold third module is the remaining obstruction

23 September 2026. This note poses the next bounded test. It is not a
three-module theorem or a counterexample.

The [general partial-order theorem](2026-09-23-pass28-partial-order.md)
already handles any number of modules with a common coefficient, even with
unequal drains. The [two-module result](2026-09-23-pass26-common-drain.md)
handles unequal coefficients with a common drain. A higher-dimensional
question is justified only if it tests a mechanism outside those conclusions.

The smallest such state has two interior partials with unequal coefficients
and a third module initially cold. Write the partials as A and B with
`gamma_A>gamma_B`, and normalize a maximal-loss witness to first-hit handoffs.
At any putative minimum the pair theorem requires A to hand off before B,
with no B input before A's handoff. It says nothing comparable about input
to the cold module C: lowering its initial preparation in the exchange is
infeasible because that initial preparation is zero.

Cold work can therefore interrupt the partial pair's preparation. Its
handoff and later release depend on the allocation, so moving A's timing
while keeping the suffix fixed may no longer be feasible. This is the
specific unresolved step in extending the two-module curvature argument.
A rate barrier alone does not create a hard intermediate deadline: C may
receive useful preparation before a resource release even if it cannot yet
reach its full cap. Such prewarming must be included in any lower bound.

The next test keeps three modules, one common positive drain, ordinary
decay-linked upkeep, and arbitrary admissible controls. An exact
counterexample must compare with **all** initial states and policies,
including states with positive preparation in C. Optimizing only within
the face `x_C=0` cannot establish a global two-partial minimum. A preserving
theorem must deal with other possible minimizing faces too; this opening
does not establish that every possible failure has the selected cold shape.

A third initially full module gives a scheduled release and is a useful
comparison, but it is not interchangeable with a cold module's endogenous
event. No general theorem for that additional case is claimed here either.
The fixed-loss preemption examples remain warnings, not proportional-loss
counterexamples.

Use at most one focused cycle of analytical reduction and targeted exact
falsification before reassessing significance. A precise missing lemma is
preferable to a claimed solver based on serial enumeration. Do not expand
to four modules or numerical control optimization merely because this
question is open. The [contribution assessment](2026-09-23-pass26-28-assessment.md)
explains the surviving ideal-model meaning and unresolved priority.
