# Pass 8: charge the permitted final service pause

22 September 2026. Pass 7's original order is preserved under
`archive/007-finite-update-readiness.md`. This pass is underway.

## Why continue in this direction

The finite-update exit theorem is proved, but its recurring frontier reduces
exactly to one standard sporadic task. Its policy class also forbids freezing
source updates before copying completes. A service contract that allows queued
requests can permit an earlier immutable snapshot, eliminating resets during
final copying. Therefore the pass-7 benchmark is not an optimum over every
handover protocol satisfying an unspecified service requirement.

## Tasks

1. Give an independent reliable-pipe interpretation of injected preparation,
   accounting for positive delivery delay, bounded pending requests, response
   allowance, and certified ownership routing.
2. Preserve a precise early-freeze counterpolicy: with enough response slack,
   freeze immediately, copy the immutable remaining version, and leave while
   independent delivery completes. Show exactly which pass-7 control assumption
   this changes.
3. Generalize to a permitted final frozen-copy duration `B` between zero and
   `L=M/s`. Derive the exact exit value and recurring frontier over this
   explicitly restricted staging-policy class. Audit causal lower bounds,
   same-time freeze/update order, startup, and `B=0,L` endpoints.
4. Record the standard sporadic-task and stop-and-copy reductions. Do not claim
   a universal optimal protocol, novel queuing principle, or engineering
   implementation. Add exact arithmetic checks to the separate handoff verifier.
5. Decide whether a central claim survives or another precise question is
   needed. Keep the strongest failed inference conspicuous in current status.

Read WORKSPACE.md, AGENTS.md, STATUS.md, the pass-6 service/drain notes, and both
pass-7 notes. Reproduce all checks listed in STATUS.md. Keep the original
license and historical checkpoints unchanged. Reconcile the actual remote
branch before committing and use a non-forced update.
