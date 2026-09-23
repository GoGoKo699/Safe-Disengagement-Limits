# Continuation: allocation attribution and the price boundary

23 September 2026. Started from actual local and remote `main` at
`b1bbd00f986efa5b935302fb175737174a7f89af`, tree
`ffb40aec4a666c8442c983c5083abcfebfa0c7df`. This is a provenance anchor,
not an instruction to reset the branch. The latest user direction is
repository research first, manuscript writing last. WORKSPACE.md and
AGENTS.md now record that direction; the continuing research mandate remains.

## Completed scientific work

**Pass 20 — prior allocation test.** Read the full strengthened concentration
proof and its preceding source comparisons. The new audit inspected the
relevant primary theorem proofs for deteriorating-job investment, nested
convex allocation and generalized exchange-based allocation. An exact
fixed-order S1 preparation-plus-slack set fails the last source's actual
exchange optimality condition, including for its shared quadratic family.
The result is a failed direct substitution, not a counterexample to that
source theorem or a claim against every nonlinear encoding.

Positive reductions are retained: a common exponential clock convexifies
every fixed-order timing domain; common rates reduce to linear allocation;
nonincreasing-rate fixed orders admit a standard reverse-convex proof of
existence of a concentrated optimum. An exact convex-clock extreme point
has two interior preparations even on a concave-objective face. It is not
an optimum, so the example only excludes an extreme-point shortcut.

Read the complete [assessment](2026-09-23-pass20-assessment.md),
[geometry](2026-09-23-pass20-geometry.md),
[nested/exchange source comparison](2026-09-23-pass20-nested-allocation.md),
[deterioration comparison](2026-09-23-pass20-deterioration-prior-art.md), and
[independent internal review](2026-09-23-pass20-review.md).

**Pass 21 — independent prices.** The concentration proof survives whenever
normalized prices satisfy its ordered-pair coefficient inequality. A simple
sufficient open neighborhood is given explicitly. Arbitrary positive prices
fail: with positive request-time tolerance, an exact two-module example has
unique nominal optimum `(51/100,51/100)`, price `357/100` and physical upkeep
`153/100<2`. All supports and possible orders are accounted for. The theorem's
price region is sufficient, not sharp, and does not include an extra active
physical-budget constraint. Read the full
[price-boundary proof](2026-09-23-pass21-price-boundary.md).

**Pass 22 — positive scalar attribution.** Standard concave composition
makes the positive region of the exchange cost log-concave; the nonpositive
region decreases strictly. A short explicit curvature check gives the
every-minimizer strictness. Relevant full source statements and proofs were
read in Boyd–Vandenberghe and Agrawal–Boyd; the lead workspace also inspected
them independently. The scalar mechanism must not be presented as a new
optimization principle. The S1 model-specific theorem remains correct, but
its priority and scientific significance remain unresolved. Read the full
[attribution note](2026-09-23-pass22-curved-exchange-attribution.md).

The geometry, source-condition counterexample, price theorem/counterexample,
log-concavity calculation and new verifier received independent internal
checks. No outside review or machine-checked continuum proof is claimed.

## Verification actually executed

At entry, the root checkpoint runner and all eight then-current analytical
suites passed. Their reports reproduced the tracked bytes. After adding the
new allocation checker, the root runner plus all nine analytical suites
passed again, with all nine analytical reports byte-identical to `results/`.
The complete current commands are in [STATUS.md](../STATUS.md).

The new [allocation verifier](../analysis/verify_allocation.py) uses exact
`fractions.Fraction` arithmetic. Its [report](../results/allocation-verification.json)
has SHA256
`0756a39212fa4492f705f0e22550f387dbaf28453d975a4c55ff3c0f9af4cbb6`.
It checks displayed geometric identities/sign factors, all six directed
equal-amount exchange certificates, the quadratic improvement, and the
independent-price support-case arithmetic. It does not verify literature,
the universal concentration theorem, or arbitrary feasible-set geometry.

Two author-run repeats and a separate review run reproduced the report.
`-O`, `-OO` and `PYTHONOPTIMIZE=1` were tested and rejected before sentinel
output writes. Immutable-checkpoint directory, existing-file, absent-child
and symlink output targets were rejected; checkpoint hashes stayed unchanged.
No additional numerical test was needed for pass 22's analytic identities.

Before publishing, verify the committed archive, compare its tree with the
published tree and re-read the remote ref. The publish commit message records
the tested local commit/tree and completed archive verification; local working
execution alone must not be called a committed-snapshot run. Use a non-forced
update only. The API may create a different commit identifier for an identical
tested tree; preserve the local commit history and verify tree equality.

## Preserved material and access limits

The original LICENSE blob remains
`e17a781bf47c4aadf18b68fc593846a1193b86c1`. Both dated checkpoint directories
and the entire `paper/` tree are unchanged from the starting commit. No paper
was edited or built. All prior analytical reports and historical research
notes are preserved; changes are in new research notes/code and current
navigation/phase instructions. No third-party full texts were added.

Each source note marks exactly what was inspected and which leads remained
inaccessible or abstract-only. Older failed Glazebrook endpoints were not
retried. No spending, outreach, submission, formal release, or large simulation
occurred. Publication novelty and an operationally justified application remain
open; the positive reductions narrow the claim instead of manufacturing novelty.

## Exact restart

1. Inspect the actual branch, HEAD, remote main and working changes. Preserve
   concurrent work; do not reset to this note's starting SHA. Read actual
   WORKSPACE.md first, then AGENTS.md, README.md, STATUS.md and CURRENT.md.
2. Run the ten suites and nine report comparisons in STATUS.md. Check the
   LICENSE and historical checkpoints; preserve the existing manuscript tree.
3. Read the full pass-20 assessment, pass-21 proof and pass-22 attribution
   note above, together with their exact source/geometry notes. The scalar
   exchange's standard derivation is now an established overlap in this
   workspace, not a novelty question to reopen without evidence.
4. Execute [pass 23](../work_orders/CURRENT.md): read the full pass-14 target
   criterion, pass-15 viability and two-module proofs, meaning/assessment
   notes, and pass-18 precision theorem. The
   [pass-23 opening](2026-09-23-pass23-viability-opening.md) already gives a
   scalar generic separation, so generic asymptotic-versus-finite reachability
   is not the candidate contribution. Its bounded primary-source audit remains
   unfinished. Test the specific S1 dimension boundary and retain the loss of
   the critical guarantee under any fixed positive request-time tolerance.
5. Record a justified contribution decision, archive the order, choose the
   next scientific task and continue within the session. Manuscript writing
   remains the last step. Research does not run in the background after this
   checkpoint ends.
