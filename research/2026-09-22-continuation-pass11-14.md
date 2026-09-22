# Continuation checkpoint: unequal decay, barriers, and critical startup

22 September 2026. This continuation started on clean `main` at
`6400737695eba9091389859724f783e03d8c1e8f`, matching the fetched remote.
WORKSPACE.md was read from that actual branch, followed by the current mandate,
work order, full relevant proofs, checkpoint notes, and literature comparisons.
All six existing verification suites passed before edits; their research reports
matched tracked results. The original LICENSE and both historical checkpoints
are preserved.

## Main finding

For positive proportional preparation loss, equality of the coefficients is
unnecessary: **every** minimum-upkeep readiness vector has a full set, at most
one partial module, and a cold remainder. This holds for all nonnegative source
budgets, including initially inaccessible stages. The proof preserves the
completion time of the second of two partial modules and changes their initial
preparation. Its pair cost is either strictly concave or strictly monotone, so
a two-partial vector cannot minimize upkeep.

That theorem does not preserve the common-rate partial-first schedule. Every
cold predecessor of an optimal partial module must have a larger decay
coefficient, and an exact two-module instance proves that such a predecessor
can strictly reduce the globally optimal upkeep. A cold-prefix subset algorithm
computes the full unequal-rate frontier with O(n*3^n) real scalar evaluations
and O(2^n) working storage. It includes inaccessible-rate boundaries and pure
ready/cold candidates. Its numerical implementation uses floating logarithms
and exponentials; it is not a certified exact transcendental solver.

The strongest candidate contribution is this concentration structure and its
consequences, contrasted with the preserved nonlinear quadratic-loss failure.
Publication novelty remains unresolved. The new primary-source audit explicitly
maps the common-rate fixed-order calculation to established linear allocation,
records a restricted affine-deterioration recurrence embedding, and inspects
an accessible nonpreemption proof for deteriorating repair states. The unequal-
rate nonlinear exchange is not supplied by those particular reductions. This
bounded comparison does not establish priority, and the older Glazebrook proofs
remain inaccessible at theorem level.

## Research decisions

| Pass | Result | Next scientifically justified question |
|---|---|---|
| 11 | Unequal positive rates retain concentration for every minimizer; actual-stage accessibility removes the global ample-capacity assumption. A prefix-rate condition recovers the common-rate partial-first result. | Compute the frontier without assuming away cold prefixes. |
| 12 | Explicit full-set/cold-prefix/partial/cold-tail computation; exact global counterexample to partial-first-only optimization. | Determine what rate barriers imply for arbitrarily loose deadlines and initialization. |
| 13 | Initially full-set closure characterizes any finite exit. Minimum successful-seed cost is the exact upkeep plateau reached at a finite deadline. Blocked cold exit precludes all finite normal warmup and any positive optional rate. Strict maintenance slack permits finite warmup. | Resolve critical equality C(H)=s without importing the common-rate aggregate obstruction. |
| 14 | A concentrated critical target is finitely reachable from cold exactly when it has a partial coordinate and some full coordinate decays faster. Pure-full critical targets are unreachable. Exact positive-deadline models demonstrate both reachable and unreachable sustainable readiness at C(H)=s. | Separate fixed-target reachability from the still-open full ready-region viability problem, and assess the focused paper claim. |

The original orders are preserved in `work_orders/archive/011...014`.
[CURRENT.md](../work_orders/CURRENT.md) is the exact restart and next decision.
New proofs are in the pass-11, pass-12, pass-13 and pass-14 notes linked by
STATUS.md. They supplement the earlier records without changing archived claims.

## Important boundaries

- Proportional loss means the robust state-dependent envelope
  `rho_i<=gamma_i*p_i`, not an expected random-update rate. No measured system
  or validated fallback implementation has been supplied.
- Instantaneous independent cutovers and nonnegative released capacity remain
  essential. The earlier positive-drain seriality counterexamples still apply.
- Common-rate rational transformed-deadline arithmetic is stronger than the
  general floating reference implementation and remains separately available.
- The concentration cost is the actual stationary loss `sum gamma_i*p_i`.
  Arbitrary external investment weights do not inherit its derivative sign.
- Critical startup is characterized for a specified concentrated target.
  The theorem does not exclude reaching a different, more expensive ready state
  and sustaining readiness along a trajectory that approaches the minimum set.
- Warmup is paid and finite where constructed. The guarantee starts after it;
  no handoffs or released capacities are used during normal warmup.
- The fixed-loss partial-state startup counterexample from the earlier record
  is unaffected; it uses a different loss law and budget boundary.

## Internal review and verification

The unequal-rate exchange, general frontier, exact cold-prefix separation,
barrier/plateau proof, and critical-target argument each received a separate
internal mathematical audit. No external human review or machine-checked proof
is claimed. A code review caught an implementation that scanned all masks for
each ready set; it was corrected to enumerate only supersets so that the code's
work matches the stated O(n*3^n) evaluation bound.

`analysis/verify_unequal_proportional.py` separates rational eligibility,
exchange identities, global counterexample inequalities, closure/seed checks,
and critical-warmup certificates from floating frontier comparisons. Its
independent reference enumerates complete orders and uses scalar bisection,
while the solver uses subset prefix/tail values and the derived formula.
Common-rate cases are compared with exact rational per-order optimization.
The finite domain and all actual counts are recorded in
`results/unequal-proportional-verification.json`.

All reproduction commands and report comparisons are in STATUS.md. Publication
of this checkpoint requires the same commands to pass from a committed Git
archive, unchanged historical hashes, a non-forced remote update after checking
its current parent, and equality of the tested and published trees. The Git
commit identifies that verified snapshot; this source does not guess its own
future commit hash.

No manuscript or submission readiness is declared. The next order is chosen
from the remaining proof, significance and attribution questions, rather than
from a need to accumulate additional model variants. No outside contact,
submission, expenditure, or formal release is part of this continuation.
