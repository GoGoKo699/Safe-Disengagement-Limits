# Working paper sources

**Concentrating perishable preparation for deadline readiness**,
Ruge Lin, 22 September 2026.

This is a working research draft, not a submission-ready paper or formal release.
Every deadline-ready state minimizing upkeep under unequal positive
proportional loss has at most one partial module.

[Read the checked working PDF](manuscript.pdf).

## Recovery and research status

The preserved sources now execute successfully in a fresh checkout. All nine current
verification suites pass, and the missing critical-viability report has been
regenerated reproducibly. The initial recovered 16-page PDF was visually
inspected; the current 20-page draft adds the pass-17 source and assumption findings
and the precision boundary and stronger prepared-stage exchange.
All 20 rendered pages were visually inspected; no unresolved references or
overfull boxes remain. The continuation records the artifact hash and
committed-snapshot verification.
The final checked artifact and committed-snapshot evidence are recorded in the
continuation notes. The lost pre-interruption PDF/report were not recovered,
so no byte identity with those originals is asserted.

The new [fixed-deadline comparison](../research/2026-09-22-pass17-prior-art.md)
excludes specified reductions to an inspected convex investment problem;
it does not certify priority. The [assumption map](../research/2026-09-22-pass17-assumptions.md)
identifies source-only upkeep and normal-mode noncompletion as substantive
service restrictions. Submission readiness remains unresolved.

## Build

The editable files are main.tex, math.tex, boundaries.tex, precision.tex, related-work.tex,
and references.bib. With TeX Live, latexmk, pdfLaTeX, BibTeX and the packages
listed in main.tex, run from the repository root:

```sh
python paper/build.py
pdftoppm -r 100 -png paper/manuscript.pdf build/paper/page
pdftotext -layout paper/manuscript.pdf build/paper/manuscript.txt
```

Auxiliary files go into build/paper/. The builder fixes the metadata date,
rejects undefined references and overfull boxes, and writes paper/manuscript.pdf.
Inspect the rendered pages before describing the PDF as checked.
No network data or large simulation is required.

## Scope and scientific gates

The paper includes the arbitrary-policy serial reduction, exact initialized
upkeep, unequal-rate concentration, explicit frontier, and exact cold-prefix,
quadratic-loss and critical-startup separations. The precision section proves
strict-slack limiting stability and gives an exact critical endpoint jump;
it distinguishes that jump from the general positive cost of a safety margin.
A concave completion-time exchange establishes concentration for every feasible
positive tolerance and every finite limiting cost, including unequal rates. The complete two-module
startup classification remains in its separate research note.

The [manuscript audit](../research/2026-09-22-pass16-manuscript-review.md) records
internal proof checks, not external peer review. The
[assessment](../research/2026-09-22-pass15-assessment.md) preserves reductions and
incomplete theorem access. The [meaning note](../research/2026-09-22-pass15-meaning.md)
explains the conditional standby-resource class and its control restrictions.

The [precision review](../research/2026-09-22-pass18-review.md) records a separate
internal audit of the new boundary proofs. The [pass-19 review](../research/2026-09-22-pass19-review.md)
audits the stronger exchange, and the [assessment](../research/2026-09-22-pass19-assessment.md)
records its unresolved priority and service-meaning questions.

Run all commands in [STATUS.md](../STATUS.md). Continuous-time claims rest on
proofs; finite checks do not establish novelty or an implementation.
The all-budget common-coefficient rational corollary is an analytic extension,
not a claim that the earlier ample-budget solver acquired new eligibility rules.

[Committed-snapshot verification](../research/2026-09-22-committed-checkpoint-verification.md)
records the fresh-archive runs, the byte-identical 20-page rebuild, and the
final artifact hash.

The unchanged [LICENSE](../LICENSE) applies. No submission, outside contact,
spending, or formal release is represented by this checkpoint.
