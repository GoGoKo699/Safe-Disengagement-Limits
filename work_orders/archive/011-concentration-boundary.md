# Pass 11: test the sharp concentration boundary and settle attribution

22 September 2026. Passes 6–10 are recorded in the continuation note; their
original work orders are preserved in `archive/006...010`. This is the next
research pass, not a submission-readiness declaration.

## Exact restart

Use the actual current branch. Do not reset to any historical provenance SHA.

```sh
git status --short
git fetch origin
git log -5 --oneline
git rev-parse HEAD origin/main
python verify.py
python -B analysis/verify_heterogeneous.py
cmp build/heterogeneous-verification.json results/heterogeneous-verification.json
python -B analysis/verify_state_dependent.py
cmp build/state-dependent-verification.json results/state-dependent-verification.json
python -B analysis/verify_handoff.py
cmp build/handoff-verification.json results/handoff-verification.json
python -B analysis/verify_partial_states.py
cmp build/partial-state-verification.json results/partial-state-verification.json
python -B analysis/verify_proportional.py
cmp build/proportional-frontier-verification.json results/proportional-frontier-verification.json
```

Read WORKSPACE.md, AGENTS.md, README.md, STATUS.md,
`research/2026-09-22-continuation-record.md`, the full pass-9 fixed/smooth
proofs and assessment, and the full pass-10 frontier including its nonlinear
counterexample. Read pass-6 interface/drain and pass-8 pipeline/freeze notes
before attaching an operational interpretation. Earlier archived proofs are
still valid in their stated domains; current scope is given by later notes.

## Central candidate and remaining gates

The strongest mathematical package is now arbitrary-partial serial dominance,
an exact forward exit algorithm, and the heterogeneous common-proportional
concentration/frontier theorem. The storage averaging, subset DP, and
fractional-knapsack method alone are established tools. The one-record reset
and final-freeze benchmarks have explicit prior-art reductions and should not
replace the central claim.

Two gates remain before a defensible paper can be selected: the exact relation
to earlier deteriorating-progress permutation theorems, and whether the
ideal instantaneous handoff captures a consequential service class. Do not
assert novelty because the closest proofs were inaccessible. Do not infer a
robust proportional erosion envelope from uniform-random-update expectation.

## First mathematical task: is common proportional decay necessary?

Pass 10 proves concentration with common gamma. Its exact quadratic-loss
counterexample shows that concentration fails for general monotone smooth
loss, even for two identical modules with positive releases and ample capacity.
It does not answer the intermediate case `g_i(p)=gamma_i*p` with unequal
positive coefficients.

1. Start with two modules, keeping `s>max_i gamma_i*M_i`. For each serial
   order derive the exact deadline constraint from the pass-9 stage formula.
   Eliminate one initial preparation and examine the resulting one-variable
   maintenance objective, including clipping and all initially full cases.
2. Prove concentration in this smallest case or produce an exact counterexample.
   Only then test three modules with small rational instances and analytically
   certified inequalities. Numerical optimization alone does not prove a
   negative or global optimum.
3. If concentration extends, identify the replacement for the common-gamma
   affine-weight proof and state the resulting algorithm's actual strength.
   If it fails, preserve the smallest useful witness. Do not add parameters
   merely to advertise heterogeneity as novelty.

## Parallel attribution task, with bounded retrieval

The closest outstanding full texts are Glazebrook (1992), NRL 39(5):613–633,
and Glazebrook (1993), JAP 30(1):184–193, DOI `10.2307/3214631`.
Previous legitimate publisher/author/repository searches reached abstracts
and references, not their full proofs. Reuse the source records; do not repeat
failed endpoints indefinitely or purchase/contact anyone without authorization.

If a legitimate accessible copy becomes available, compare its actual
hypotheses and proof with: initial partial progress, arbitrary fractional
service, input-postponement dominance, completion-induced capacity gains or
remaining-work contractions, inaccessible stages, and pathwise deadline
attainment. Determine whether S1 is a direct corollary, a modest extension, or
has a substantive unmatched result. The concentration/frontier claim also
needs its own model-level comparison; calling its final LP fractional knapsack
neither establishes nor defeats that entire claim.

## Decision after this pass

Choose one theorem-led claim and explicitly assess what it teaches beyond the
closest inspected results. Preserve failed extensions and reductions. A working
manuscript becomes justified only around a surviving, meaningful claim with
honest attribution; a submission package additionally needs resolved material
proof/novelty gaps, a checked manuscript/PDF, references, and referee assessment.
No current record asserts that these gates have passed.

Keep LICENSE and both checkpoint directories unchanged, preserve concurrent
work, and verify an actual committed tree before reporting completion. Ordinary
research commits/pushes remain authorized. Outreach, submission, spending, and
formal release remain outside this authorization.
