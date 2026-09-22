# Pass 10: compute the heterogeneous common-proportional frontier

22 September 2026. Pass 9 completed; its order is preserved in
`archive/009-arbitrary-partial-states.md`. This pass is underway.

## Finding to develop

The first-completion exchange proves full-speed serial optimality from every
partial initial state for fixed loss and monotone Lipschitz smooth loss.
Forward earliest-time subset labels solve the full-state exit oracle. Compact
serial-duration witnesses give an attained heterogeneous smooth minimum-upkeep
optimization. These strengthen the core theorem but do not establish novelty.

For proportional erosion with a common coefficient gamma and unequal sizes
and released rates, the change of time variable X=exp(gamma*t) makes each
serial transition affine in the initial preparations. Ordered coefficients
may reduce the upkeep problem to prefix concentration and a finite explicit
subset computation, extending the previously homogeneous result.

## Tasks

1. Prove the affine transition, strict ordering of preparation coefficients,
   and fractional-knapsack concentration for each serial order. Distinguish
   existence of an optimal concentrated state from optimality of processing
   the partial module first for every such state.
2. Prove the global ready-subset/one-partial/cold-tail cost formula, including
   all-ready, zero-cost, nominal-infeasibility, and equality cases. Keep the
   strict accessible-budget condition s>max(gamma*M_i) explicit.
3. Compute cold-state multipliers and frontier queries using exact rational
   arithmetic when parameters and transformed deadline X are rational.
   Do not describe evaluation at arbitrary real H as exact rational arithmetic.
4. Compare against independently enumerated permutations and per-order linear
   constraints on small instances; retain exact counterexamples to stronger
   unwarranted claims. Internal audits and finite checks are not external review.
5. Update the contribution assessment and select the next decisive task.
   The generic smooth frontier is an attained finite-dimensional optimization;
   this pass may solve the common-coefficient subclass explicitly. Neither
   fact resolves the closest deteriorating-progress prior-art gate.

Preserve LICENSE, historical checkpoints, concurrent work, and previous reports.
Read WORKSPACE.md, AGENTS.md, STATUS.md, both pass-9 proofs, and the current
source assessment. Reproduce all verification routes before publishing an
ordinary authorized research commit.
