# Continuation checkpoint: viability attribution and the drain boundary

23 September 2026. Repository research only. The user directed that manuscript
writing be the last step; no manuscript file was edited or rebuilt.

## Starting repository state and completed work

This continuation began on clean actual `main` at
`8882d1959f62b2e8c54c68eef24848b20347583b`, tree
`60d31a0a5b3263125df662d4676e9c012a63dc9c`. Remote main matched that commit.
These are provenance anchors, not instructions to reset later work. The
actual WORKSPACE.md was read first, followed by current instructions, status,
work order, provenance, full relevant proof/checkpoint notes and source records.
The baseline ten suites passed and all nine earlier analytical reports matched
their tracked bytes before new work.

Three substantive passes were completed and the next was opened:

1. **Pass 23: bounded viability/reachability audit.** Normal maximal-loss
   operation is exactly positive linear control with simplex input and box
   path constraints. Robust cold entry into indefinite readiness is standard
   capture of a viability kernel; domination of an upkeep optimum is capture
   of a smaller invariant target. The S1 two-module result concerns cold
   membership, not equality of whole kernels/basins. The generic distinction
   is standard. An explicit non-S1 upward region violates the two-module
   implication under the same leaky dynamics and positive linked upkeep,
   isolating the role of exit-schedule geometry. An uncapped support formula
   has a direct primary-source reduction; a separate exact example shows
   that a terminal box intersection cannot impose state path caps.
2. **Pass 24: calibrated critical family.** Explicit strict inequalities
   extend the three-module separation beyond one fixture. The proof gives a
   unique concentrated critical optimum, an all-policy finite-domination
   obstruction, and an analytical uniform ready-tail bound after finite
   warmup. The deadline is calibrated to retain equality `C(H)=s`; no open
   region in independently varied deadlines is claimed. Any fixed positive
   request deficit still excludes indefinite ready residence, even under
   dynamic policies. This remains a secondary ideal-model boundary.
3. **Pass 25: accounted proportional-drain counterexample.** Heterogeneous
   immutable drain durations induce two different handoff deadlines. With
   spare capacity four, coefficients `(2,1)` and caps `(1/2,3)`, the unique
   minimum is `(37/200,7/5)` with cost `177/100`: both coordinates are partial.
   A discounted-work bound covers every admissible policy; a matching robust
   schedule attains it. Finite cold warmup and positive optional capacity are
   explicit. Fixed request-time tolerance has exact minimum
   `177/100+3*epsilon` for `0<=epsilon<=63/200`, infinity above; concentration
   still fails below the endpoint. No release helps the witness. Common long
   drains instead reduce exactly to zero-release instantaneous S1 and retain
   concentration. This is an assumption boundary, not a general solver or
   established novelty against allocation/scheduling theory.
4. **Pass 26 opening only.** Fixed handoff times yield a linear allocation
   formulation with path caps and a useful dual lower certificate. A restricted
   two-module serial branch with common drains has no smooth interior local
   minimum and no minimum caused solely by the release-transition kink. The
   all-policy question remains open; the calculation does not justify serial
   optimality or establish concentration for the remaining model.

## Durable reading route

- [Revised contribution decision](2026-09-23-pass23-25-assessment.md).
- [Viability primary-source comparison](2026-09-23-pass23-viability-prior-art.md),
  [linear reachability reduction and cap counterexample](2026-09-23-pass23-positive-reachability.md),
  and [internal critical/precision proof review](2026-09-23-pass23-proof-review.md).
- [Calibrated family proof](2026-09-23-pass24-critical-family.md).
- [Full drain counterexample, precision theorem and preserving subclass](2026-09-23-pass25-proportional-drain.md),
  [separate internal review](2026-09-23-pass25-review.md),
  [exact supporting checker](../analysis/verify_proportional_drain.py), and
  [new report](../results/proportional-drain-verification.json).
- [Next pass's opening calculation](2026-09-23-pass26-common-drain-opening.md)
  and [current work order](../work_orders/CURRENT.md).

The prior CURRENT was archived unchanged as
[order 023](../work_orders/archive/023-critical-viability-attribution.md).
[Order 024](../work_orders/archive/024-calibrated-critical-family.md) and
[order 025](../work_orders/archive/025-proportional-drain-boundary.md) record
the justified follow-ons retrospectively, explicitly with their outcomes.
The [passes 20–22 continuation](2026-09-23-continuation-pass20-22.md) and all
older research notes remain unchanged.

## Source inspection and review scope

The pass-23 bounded primary comparison inspected three close results:

- Aubin–Catté (2002): the evolutionary-system and viability/capture
  definitions, Theorem 3.3 proof, and its recorded auxiliary arguments.
- Broucke–Turriff (2010): the control model and relative-degree assumptions,
  relevant lemmas/propositions and the complete Theorems 17–18 proofs in the
  source comparison's inspection record. The direct `g=I` encoding fails an
  assumption; alternative encodings are not ruled out.
- Girard–Le Guernic (2008): model, support-function ingredients, Proposition
  5 and its complete proof. Its source formula is uncapped; the note retains
  that limitation. The 2010 extension and other abstract-only leads are not
  represented as fully read.

Exact URLs, theorem/section references, mappings and access limits are in the
linked source notes. The workspace source-inspection record includes work by
separate agents; it is not a claim of external human review. Root rechecked
the retrieved central definitions/formulas, proof artifacts and model
reductions. No third-party papers were added to the repository. The drain
countermodel's direct allocation reasoning is not presented as a new general
optimization theorem; its publication priority remains unresolved.

The critical-family proof and final drain proof received separate internal
agent review. Root also read the complete new drain proof, precision section,
checker and opening calculation. These are mathematical internal audits,
not machine-verified proofs, external certification, or literature clearance.

## Verification and publish procedure

After the research changes, all **eleven** current suites executed successfully
and all **ten** analytical reports matched byte-for-byte. The new checker uses
only exact rational arithmetic: trajectory and waiting endpoints, weighted
integral identities, polynomial sign factors, handoff-order gap, no-early-
release inequality, cold warmup and precision constants. It does not search
the continuous control space or prove the all-policy theorem. Its repeated
output and rejection guards for optimization and immutable-checkpoint output
were checked. Existing code and all earlier reports are unchanged.

Run the complete commands in [STATUS.md](../STATUS.md). Publication must also
test an archive of a fixed **committed** tree, compare all ten reports, and
check protected contents. A working-tree run is not a committed-snapshot run.
The publish commit message records the tested local commit and tree plus the
archive verification actually completed. If the connected GitHub API creates
a different commit identifier with the same tree, preserve local commit
history and verify exact tree equality after fetching the published ref.
Read remote main immediately before updating it and never force the update.

The original LICENSE blob remains
`e17a781bf47c4aadf18b68fc593846a1193b86c1`. Both historical checkpoint
directories, all earlier reports and research notes, and the entire `paper/`
tree are preserved from the starting commit. No paper build is part of this
checkpoint. No spending, outreach, submission, formal release or large
simulation occurred. Scientific novelty and an operationally justified
application are still unresolved.

## Exact restart

1. Inspect the actual branch, HEAD, remote main and working changes. Preserve
   concurrent work; do not reset to the starting SHA above. Read current
   WORKSPACE.md first, then AGENTS.md, README.md, STATUS.md and CURRENT.md.
2. Run the eleven suites and ten report comparisons in STATUS; preserve the
   license, historical checkpoints and manuscript. Read the full new proof
   and comparison notes above, not just this continuation.
3. Execute pass 26 in the stated two-module common-drain domain `H>2*ell`.
   All handoffs share deadline `D=H-ell`; early drains may release useful
   capacity. Fixed-time allocation and serial-branch calculus are available,
   but their missing all-policy step is not established. Include both
   handoff orders, initially full states, reflection and active caps.
4. Seek a proved preservation result, exact all-policy counterexample, or
   direct prior-art reduction. Keep any source comparison bounded and read
   relevant full proofs. Do not start a general solver, silently revive
   seriality, or treat failed direct source substitutions as novelty evidence.
5. Record the result, archive/update the work order and continue with the next
   justified task within the session. Manuscript writing remains the final
   step. Research does not run in the background after this checkpoint ends.
