# Continuation checkpoint: passes 6–10

22 September 2026. This continuation started from clean `main` at
`a1583cda84eddb9d1b0552358f48b5c8ccdd08b8`, agreeing with the fetched remote.
WORKSPACE.md and the current research order governed the work. Both original
checkpoint reports and the two then-current research reports reproduced before
new edits. The original license and historical checkpoint contents remain
preserved; all new proofs and checks are outside those directories.

## Main result and current assessment

The strongest current candidate is now a complete all-state scheduling result:
serial full-capacity preparation attains the optimal robust exit time from
arbitrary partial states under reflected fixed loss or nondecreasing Lipschitz
smooth loss vanishing at zero. A forward subset computation retains elapsed
time and passive initial-state decay. The new proof uses a first-completion
exchange and postponement of other work, rather than assuming the earlier
cold-state potential applies unchanged.

For smooth loss, bounded serial-duration witnesses prove compactness of the
ready set. Minimum stationary loss is attained and gives exact initialized
recurring upkeep. In the common proportional-coefficient subclass, a global
time transformation and strictly ordered preparation weights prove that some
upkeep optimizer has full modules, at most one partial module, and a cold
remainder. An explicit subset/cold-tail formula computes that frontier using
exact rationals when the transformed deadline is rational.

These are internally audited theorems, not external review or machine-verified
proofs. They are a stronger mathematical package than the initial checkpoint,
but **publication novelty and submission readiness remain unestablished**.
The closest deteriorating-progress permutation proofs remain uninspected, and
the exchange mechanism now makes that comparison more important. An explicit
algorithm or a familiar optimization step is not sufficient evidence of novelty.

## Research loop and decisions

| Pass | Finding | Decision and next question |
|---|---|---|
| 6 | Fixed-capacity decay reduces to ordinary workload arguments; a finite-record interface distinguishes acknowledgment, independent information, receiver freshness, and response timing. Delayed resource release has exact overlap/preemption counterexamples. | Preserve the coupled theorem with unresolved attribution. Replace unjustified continuous update-rate interpretations by explicit event timing. |
| 7 | A spaced atomic-update model has an exact age-dependent exit/readiness value and linear upkeep frontier. Its entire normal constraint reduces to one standard sporadic task. | Retain as a solved benchmark and prior-art reduction. Test the excluded ability to freeze source updates early. |
| 8 | Permitting a bounded final frozen-copy interval changes the exact frontier; enough response slack can eliminate upkeep. The stop-and-copy budget is established migration practice. | Keep protocol classes explicit. Return to the original unresolved arbitrary-partial-state scheduling gap. |
| 9 | First-completion exchange proves full-state seriality for fixed and smooth loss; forward subset labels solve the exit oracle. Compactness establishes attainment of general smooth minimum upkeep. | Develop a computable, substantive consequence rather than package an implicit optimization as a closed formula. |
| 10 | Common proportional loss with heterogeneous sizes/releases gives ordered affine weights, global concentration, and an explicit exact transformed-deadline frontier. | Prefer this structural package as the central candidate. Test its sharp scope and settle theorem-level attribution before drafting a submission. |

Original pass orders are preserved in `work_orders/archive/006...010`.
[CURRENT.md](../work_orders/CURRENT.md) gives the exact next pass and restart
commands. It investigates unequal proportional coefficients and the closest
permutation theorems; it does not presume concentration or novelty extends.

## Counterexamples and qualifications retained

- Delayed immutable source drains: the exact two-module optimum is `3`, versus
  `10/3` for module-by-module removal. A separate three-module optimum is
  `37/9`, versus `38/9` for the best uninterrupted-preparation schedule.
  The fixed-loss support/upkeep argument survives only through an unresolved
  *actual deadline-feasibility* oracle; it does not solve that drain scheduler.
- Equally cold preparations can have different safe exit deadlines under
  time-spaced updates. Replacing jumps by their mean dirty rate fails in both
  directions. Positive pipeline delay alone does not forbid earlier source
  freeze, and independent queued operations are not free resources.
- Arbitrary-partial seriality does not preserve an arbitrary schedule's
  complete completion order. Nor must every concentrated state prepare its
  partial module first: the exact two-module multiplier witness in pass 10
  refutes that stronger statement.
- Concentration fails for general smooth loss. With two quadratic-loss
  modules, an explicitly feasible two-partial state costs `32/25`, strictly
  less than every concentrated state at the chosen rational deadline. This
  is a certified upper/lower separation, not an exact solution of the entire
  quadratic frontier or a counterexample to unequal proportional coefficients.
- General smooth upkeep is an attained finite-dimensional optimization.
  Only the stated common-coefficient subclass has the new explicit frontier.
  Paid initialization, simultaneous maximum loss, independent instantaneous
  cutovers, and the strict accessible-budget condition retain their stated roles.

## Verification and continuity

All verification remains small, local, and Python-standard-library based.
The baseline runner reproduces immutable checkpoint reports in temporary copies.
New reports distinguish exact rational computations, explicitly finite test
domains, and floating analytic identities with tolerances. No finite test
enumerates all measurable policies; those claims rest on the written proofs.

The new verification routes are:

- `analysis/verify_handoff.py`: prescribed drain schedules, finite-update and
  bounded-freeze identities, event priority, and finite-prefix work accounting.
- `analysis/verify_partial_states.py`: forward fixed-loss subset labels versus
  independent permutations, reflection/postponement checks, sampled lower-loss
  histories, and separately labeled proportional-flow identities.
- `analysis/verify_proportional.py`: cold and full-state multipliers, frontier
  queries versus independent per-order linear optimization, returned witnesses,
  homogeneous regression, and exact boundary counterexamples.

The complete reproduction commands and byte-for-byte report comparisons are
in STATUS.md and CURRENT.md. Publication of this checkpoint must use a
non-forced update after reconciling the remote. The committed archive is checked
separately from the working tree, and the published tree must equal that tested
tree. No submission, external contact, expenditure, or formal release is part
of this research checkpoint.
