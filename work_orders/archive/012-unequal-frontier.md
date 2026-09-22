# Pass 12: compute the unequal-decay frontier and test its policy structure

22 September 2026. Continuation base: `6400737695eba9091389859724f783e03d8c1e8f`.
The original pass-11 order is preserved in `archive/011-concentration-boundary.md`.

## Finding carried forward

The consecutive-partial exchange proves that every upkeep minimizer for positive
proportional coefficients has at most one genuinely partial coordinate. The
coefficients need not agree. The proof only needs accessibility of the stages
in an attained feasible serial schedule, so the global large-capacity condition
is unnecessary. Full details and audit are being recorded in
`research/2026-09-22-pass11-unequal-decay.md`.

Concentration alone does not say that the partial module should be processed
before every cold module. Resolve this distinction for a globally optimal
readiness state, beyond the prescribed-state counterexample in pass 10.

## Tasks

1. Derive a finite frontier by choosing an initially full set, a cold prefix,
   one partial module, and a cold suffix. Prove why the earliest cold prefix
   and shortest cold suffix suffice for each chosen set.
2. Handle inaccessible stages explicitly, including zero spare capacity,
   zero releases, initially full modules, and ready/cold states with no partial
   module. State the actual operation count and numeric representation limits.
3. Prove an exact small counterexample if the partial-first restriction loses
   global optimality. Preserve all competing cases, not only two schedules.
4. Implement a small local reference calculation with independently enumerated
   orders. Label floating evaluations honestly; use exact inequalities for
   the separating counterexample. Keep original reports and checkpoints intact.
5. Continue bounded primary-source comparison for the full-state serial theorem
   and the initial-readiness concentration result. Inaccessible sources do not
   establish novelty.

After recording these results, choose the next question they expose. A useful
candidate is whether inaccessible rates leave a positive upkeep floor even as
the deadline grows, and what that implies for paid initialization versus cold
startup. Do not expand parameters just to accumulate variants.

## Verification and authority

Run the complete baseline and report comparisons from STATUS.md before and
after changes. Test the actual committed archive and verify the published tree.
Read the remote branch before committing; preserve concurrent work. LICENSE and
both historical checkpoint directories remain immutable. Ordinary research
commits and pushes are authorized; outreach, spending, submission, and formal
release are not. No novelty or submission-readiness declaration follows from
the mathematical extension alone.
