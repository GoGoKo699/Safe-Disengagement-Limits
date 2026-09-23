# Pass 21: the price assumption in concentration

23 September 2026. This follow-on arose from pass 20's allocation comparison.
The exchange proof uses a strict comparison between its two exponential
coefficients. Determine whether decay-linked prices are essential or stable.

1. Replace objective coefficients gamma_i by positive w_i while retaining
   the original proportional loss dynamics, caps and nonnegative support
   charges. Derive a sufficient condition for the same every-minimizer proof.
2. Give an explicit order-independent neighborhood of the linked prices if
   possible. Label it sufficient unless sharpness is proved.
3. Test arbitrary independent prices with a small exact counterexample.
   Cover all supports and all admissible orders before claiming a global
   optimum. Prefer a positive-tolerance example whose nominal optimum is
   physically maintainable under the unchanged loss coefficients.
4. Distinguish economic preparation prices from physical source upkeep.
   An added active physical-budget constraint is a separate problem.
5. Obtain independent internal proof review and add exact arithmetic
   certificates. Preserve earlier reports and all manuscript files.

Outcome: the full sufficient cone and unique two-partial nominal optimum
are in research/2026-09-23-pass21-price-boundary.md. The proof was independently
reviewed; the finite certificates are in analysis/verify_allocation.py and
results/allocation-verification.json. Continue with attribution of the actual
curved-exchange lemma, rather than optimizing the sufficient price bound.
