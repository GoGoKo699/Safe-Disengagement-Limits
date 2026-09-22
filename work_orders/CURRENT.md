# Continue pass 16: verify the recovered research checkpoint, then assess contribution

22 September 2026. Start from the actual current branch. Never reset to a
historical provenance commit or overwrite uncommitted work.

## What happened

Pass 15 proved critical convergence, found a three-module counterexample to
fixed-target startup necessity, and proved the two-module boundary. A complete
working paper was authored, internally audited and compiled to 16 pages.
All eight local verifier suites passed; all seven research reports matched.

The execution environment disconnected during PDF inspection, before a local
commit. The sources were preserved through GitHub from recorded authored
content. The compiled PDF and new critical-viability JSON could not be retrieved.
This recovery commit is not claimed to be an execution-tested snapshot.
Read research/2026-09-22-continuation-pass15-16.md before resuming.

## Exact restart

Read WORKSPACE.md from the actual current branch first, then AGENTS.md,
README.md, STATUS.md, the pass-15 full proofs, assessment, meaning note,
pass-16 manuscript review, and paper/README.md. Preserve all old local files:
they may contain the original PDF and report when the runtime reconnects.

```sh
git status --short --branch
git fetch origin
git rev-parse HEAD origin/main
```

If the original checkout contains unreconciled work, create a fresh detached
worktree at the current fetched head, using an unused directory:

```sh
git worktree add --detach ../SDL-recovery-verify origin/main
cd ../SDL-recovery-verify
```

Do not delete, reset, or blindly replace the original working tree. Compare
its authored content with the preserved source files when it becomes available.

## Complete the artifact and verification gate

```sh
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
python -B analysis/verify_unequal_proportional.py
cmp build/unequal-proportional-verification.json results/unequal-proportional-verification.json
python -B analysis/verify_critical_viability.py
python paper/build.py
pdftoppm -r 100 -png paper/manuscript.pdf build/paper/page
pdftotext -layout paper/manuscript.pdf build/paper/manuscript.txt
```

Review the new viability report, exact/floating scope and source reconstruction.
If the old local report is recovered, compare the full bytes. Preserve any
difference instead of changing expected output to conceal it. Once checked,
track results/critical-viability-verification.json and add its byte comparison.
Inspect every rendered PDF page and cite/link the actual resulting artifact.

Verify the final source wording: measurable loss histories; transfers normalized
to first hit; prefix corollary applies to orders meeting H; optional-rate
guarantee uses each history's liminf time average; startup impossibility is
robust, not a claim about benign histories. The all-budget common-gamma rational
corollary is analytic; do not imply the old reference solver implements it.

Keep original LICENSE blob e17a781bf47c4aadf18b68fc593846a1193b86c1 and checkpoint
trees unchanged. Commit, rerun from an archive of that exact commit, reconcile
the current remote, publish non-forced, and verify the resulting tree.

## Next scientific task after recovery

Continue without treating artifact recovery as completion of the mandate.
Use the actual paper to address its strongest concrete referee objection:

- Conduct one bounded theorem-level comparison with an accessible nonlinear
  controllable-work / initial-investment fixed-deadline result. Use the source
  leads in the pass-15 assessment, avoid repeating blocked endpoints, and
  record exact feasible-set, objective, policy and quantifier mappings.
  A reduction supersedes the novelty claim; incomplete access establishes
  neither equivalence nor absence.
- Refine the ideal standby-service interpretation against the free independent
  premaintenance and early-activation alternatives identified in the meaning
  note. Produce an assumption-to-conclusion map for the paper. Do not exclude
  an admissible alternative merely to preserve a positive lower bound.
- Reassess the focused claim. If prior work absorbs it or its ideal meaning is
  too weak, record that finding and choose a justified S1 revision. Do not add
  parameters merely to defer the decision.

Archive each completed order and update status and continuity before the next
pass. No outreach, submission, spending, or formal release is authorized.
