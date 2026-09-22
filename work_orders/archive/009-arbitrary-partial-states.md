# Pass 9: settle the existing arbitrary-partial-state gap

22 September 2026. Pass 8 completed; its order is preserved in
`archive/008-bounded-freeze-policy.md`. This pass is underway.

## Why this is the next question

The finite-update/freeze calculations now have exact proofs and explicit
standard scheduling/migration reductions. Do not add variants to evade that
assessment. Return to H4/G3, the unresolved full-state domain of the core
coupled-decay theorem. A postponement exchange may extend serial optimality
from ready/cold states to arbitrary partial preparation.

## Tasks

1. Prove or refute the first-completion exchange for arbitrary bounded measurable
   allocations. Account for extinction, upper saturation, initially full jobs,
   and allocation needed to complete the first job.
2. Check the smooth monotone Lipschitz extension: postponing service should
   increase final scalar preparation, but this requires a proof, not analogy.
3. Derive a forward earliest-completion subset algorithm with time-dependent
   passive initial stock. Do not reuse the ready/cold recurrence unchanged.
4. Add exact fixed-rate DP/permutation checks and separately labeled smooth
   analytic checks. The all-policy claim must rest on the written exchange proof.
5. Reassess heterogeneous smooth recurring upkeep only if the ready region and
   attainment can be established. Preserve the difference between an explicit
   exit oracle and a solved finite-dimensional upkeep optimization.
6. Record the strengthened scope and its relation to the old theorem. Do not
   infer preservation of the original completion order or publication novelty.

Read WORKSPACE.md, AGENTS.md, STATUS.md, the original scheduling and
state-dependent-loss proofs, pass-6 source comparison, and passes7–8 decisions.
Run all existing verification routes. Preserve LICENSE and historical
checkpoints; reconcile current remote before committing a verified checkpoint.
