# Working paper sources

**Concentrating perishable preparation for deadline readiness**,
Ruge Lin, 22 September 2026.

This is a working research draft, not a submission-ready paper or formal release.
Every deadline-ready state minimizing upkeep under unequal positive
proportional loss has at most one partial module.

## Recovery status

Complete sources were authored and compiled locally to a 16-page PDF with no
undefined references or overfull boxes. The execution environment disconnected
during final visual inspection, before a local commit. This checkpoint
preserves text recovered through the repository connection. It does not contain
the inaccessible PDF or claim that these recovered bytes have been compiled
or execution-tested. See [the continuation record](../research/2026-09-22-continuation-pass15-16.md).

## Build

The editable files are main.tex, math.tex, boundaries.tex, related-work.tex,
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
quadratic-loss and critical-startup separations. The complete two-module
startup classification remains in its separate research note.

The [manuscript audit](../research/2026-09-22-pass16-manuscript-review.md) records
internal proof checks, not external peer review. The
[assessment](../research/2026-09-22-pass15-assessment.md) preserves reductions and
incomplete theorem access. The [meaning note](../research/2026-09-22-pass15-meaning.md)
explains the conditional standby-resource class and its control restrictions.

Run all commands in [STATUS.md](../STATUS.md). Continuous-time claims rest on
proofs; finite checks do not establish novelty or an implementation.
The all-budget common-coefficient rational corollary is an analytic extension,
not a claim that the earlier ample-budget solver acquired new eligibility rules.

The unchanged [LICENSE](../LICENSE) applies. No submission, outside contact,
spending, or formal release is represented by this checkpoint.
