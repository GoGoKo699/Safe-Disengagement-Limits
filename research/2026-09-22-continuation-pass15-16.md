# Continuation record: passes 15 and 16, including execution recovery

22 September 2026. Started clean on main at
bb1e34f41338745c88ae486d493a053c658fb3d1,
tree 4e207d02e421e98f3ffebe34647b6104c37a1ad6, matching fetched origin/main.
WORKSPACE.md was read from the actual branch before research. The seven
baseline suites passed, with the six existing research reports byte-identical.

## Pass 15: full-region critical startup

The proposed necessity of a reachable minimum is false with three modules.
The full proof is in pass15-critical-viability.md. It first establishes that
every indefinitely ready maximal-loss trajectory at C(H)=s>0 converges to a
single minimum: excess upkeep is integrable, its Lipschitz continuity forces
it to vanish, and compactness plus every-minimum concentration makes the
minimizing set finite.

The exact instance has s=1 and triples (M,gamma,a):
A=(1/2,1,2), B=(1,2,33), C=(3,1/2,1).
Its deadline is H=log(5/2)/2+2log(24/23), and its unique minimum is
p*=(1/2,1/4,0), with upkeep one. A support-sum differential inequality
excludes robust finite normal reachability or domination of p* from cold.

Prepare C alone for 2log2, then allocate (1/2,1/2,0) forever. At elapsed
second-phase time t, x=exp(-t/2) gives
p=((1-x^2)/2,(1-x^4)/4,x).
For x<=1/128, an exact fourth-root concavity bound certifies an A,B,C exit
strictly before H. Total warmup is 16log2. All later request times and all
smaller allowed losses are covered by scalar comparison. The additional
reserve pays integrable excess upkeep while the trajectory approaches p*.

The separate two-module note proves necessity in dimension two under finite
cold exit. It handles all concentrated limiting shapes, including the
delicate full/cold target by a deadline-preserving cost improvement rather
than assuming the deadline equals the target exit time. One module has no
critical instance in this domain. Both new proofs received independent
internal agent reads; no substantive proof defect was found.

The contribution assessment recommends a focused working manuscript, not
submission readiness. It adds a full-section comparison with Li–Wang–Wang
(2015), retains exact earlier common-rate reductions, and marks inaccessible
older proofs honestly. The meaning note supplies a conditional deterministic
reserve interface and exposes independent-maintainer and early-transfer
alternatives. No physical implementation was validated.

## Pass 16: working manuscript and internal audit

Complete LaTeX sources were assembled around unequal-rate concentration,
supporting seriality/upkeep, an explicit finite frontier, the globally useful
cold-prefix example, quadratic failure, and critical-startup separation.
The two-module classification stays in the research archive to limit scope.
The common-coefficient rational transformed-deadline corollary now has an
all-budget analytic formulation; the old ample-budget solver was not changed.

Combined proof review corrected a missing TeX backslash, robust reachability
wording, deadline qualification of the optimizer-prefix corollary, first-hit
transfer normalization, and the exact long-run guarantee definition. Recovered
math source also explicitly requires measurable loss histories. These are
recorded in the manuscript review; they are internal checks, not human peer
review or formal verification.

A successful local build produced 16 pages (375116 bytes at the first completed
compile), with no unresolved references or overfull boxes. A subsequent build
and page-render command exited successfully. The execution environment then
became offline before rendered pages could be inspected. Consequently no
visually checked PDF is claimed and no inaccessible PDF is committed.

## Verification before interruption

All eight suites passed: root checkpoint reproduction, heterogeneous,
state-dependent, handoff, partial-state, proportional, unequal-proportional,
and critical-viability. The seven working-tree research reports matched their
then-present tracked/intended report bytes. The new viability report had exact
global-cost case checks, a rational interval certificate, phase identities,
and separately labeled floating schedule/frontier checks. Its -O and immutable
checkpoint output guards rejected invalid execution as intended.

The original LICENSE hashed to e17a781bf47c4aadf18b68fc593846a1193b86c1.
No checkpoint file differed from the starting commit. These statements describe
executed working-tree checks before interruption, not the recovered commit.

## Environment failure and preservation method

The local exec transport disconnected, then returned recovery timeout and
environment_offline. Local source reads, image inspection and the review-file
write became unavailable. The GitHub repository connection remained available.
The remote main was re-read and still at the starting commit.

To avoid losing the research, agents recovered complete authored file contents
from their successful write/read records and created immutable GitHub blobs.
The parent assembled one non-forced recovery checkpoint from those blobs and
new explicit recovery navigation. No filesystem snapshot could be hashed after
the disconnect. Thus exact identity with every final local byte is not claimed.
The preservation inventory is in results/recovery-source-inventory.json.

The verifier source was recovered from a complete successful read plus its
recorded wording patch. The full new JSON report was not accessible and was
not reconstructed from partial floating summaries. It must be regenerated and
reviewed. The manuscript review is a reconstructed compact final review; its
original longer local file write failed. The main preamble/build source were
recovered from authored content, with development status updated to reflect
the interruption. README, STATUS, CURRENT and this record explicitly describe
the remaining gate rather than inheriting premature 'checked PDF' wording.

The recovered source blobs were read back through the connected API and their
canonical Git SHA-1 values independently recalculated. All 41 manuscript labels
and ten bibliography entries passed a static reference/citation check. The
parent also checked the final measurability, first-hit transfer, deadline-H
prefix and liminf-average wording through that readback. These checks do not
execute Python or compile LaTeX. Final committed-snapshot execution, PDF
rebuild and visual inspection remain open. CURRENT.md gives exact restart
commands and instructs preservation of any original local files upon recovery.

## Continuing scientific decision

The mathematical startup question is resolved, while publication novelty and
ideal-model significance remain unsettled. Finish the interrupted artifact
verification, then address a concrete attribution or interface objection from
the actual manuscript. Do not treat a source checkpoint, successful finite
tests, or a 16-page draft as submission readiness. No submission, outside
contact, payment or formal release occurred.
