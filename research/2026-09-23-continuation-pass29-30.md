# Continuation checkpoint: exact common-drain failure and robustness

23 September 2026. Research repository only. No manuscript file was edited
or rebuilt. This session started on clean actual main at
`9421ea335e53d558be2d95a361908c0b7b579458`, tree
`8734fc892ad468f74a69645f9f2a5c71d02d6fee`; remote main matched.
These are provenance anchors, not instructions to reset later work.

## Completed research

Actual WORKSPACE.md was read first, followed by current instructions,
navigation/status/provenance and work order, the full relevant preceding
proofs, reviews and comparisons. All eleven preexisting verification suites
passed at baseline and all ten analytical reports matched their references.

Pass 29 initially tested a cold module interleaving with two partials.
The successful counterexample needed no interleaving: a cold final module
requires released capacity from both earlier modules. Two barriers force
both earlier handoffs before any release, so two localized constant-capacity
front-loadings cover all allowed policies. Six rational inequalities exclude
every concentrated state up to `1851/10000`, while an explicit two-partial
policy costs `37/200`. An earlier local-minimum calibration had a cheaper
concentrated policy and remains recorded as a failed counterexample.

Additional reductions prove that common-drain minima with multiple partials
need a cold coordinate, and that a cold third module no faster than either
partial cannot sustain the three-module failure. These are ordinary
physical-cap, zero-deficit conclusions; their cold-activation exchanges
must not silently drop positive support charges.

Pass 30 proves the fixture's exact unique optimum `(3/100,1/8,0)` and
value `37/200`. Every global minimum is first shown to have A/B partial
and C cold and to admit the A,B,C witness. The scalar relaxation then has
a strictly positive rational lower bound on its curvature over the entire
relevant interval. Equality recovers the unique initial state; no uniqueness
of exit policies is asserted.

The exact positive-tolerance continuation has unique nominal optimum
`(3/100+epsilon,1/8+epsilon,0)` and upkeep `37/200+3*epsilon` for
`0<=epsilon<=1/30000`. The proof uses the exact zero-deficit minimum and
the minimum coefficient sum over a positive support of size at least two.
The endpoint is a certified range, not an infeasibility threshold.

At fixed epsilon `1/100000`, a slightly more prepared nominal witness
costs `0.18506<0.1851` and has strict deadline slack. It is deliberately
near-optimal, not the exact nominal optimizer. Its normal upkeep is below
the original spare rate and finite radial cold warmup is explicit. A
joint-parameter closed-graph proof and continuity of this strict serial
witness establish a relative open common-drain family with fixed positive
tolerance and a concentrated-cost advantage. No numerical neighborhood
radius, general scheduling algorithm or optimizer formula at perturbed
parameters is supplied.

## Reading and scientific status

Start with the [current assessment](2026-09-23-pass29-30-assessment.md), then
read the complete [counterexample](2026-09-23-pass29-cold-test.md),
[exact optimum](2026-09-23-pass30-exact-optimum.md),
[precision/startup/open-family proof](2026-09-23-pass30-robust-common-drain.md),
[internal review](2026-09-23-pass29-30-review.md), and
[source comparison](2026-09-23-pass29-prior-art.md).
The [boundary-face proof](2026-09-23-pass29-boundary-faces.md) and
[preserving/failed-attempt/certificate note](2026-09-23-pass29-preserving-attempt.md)
record the other reductions and exact arithmetic.

Root read the full main and companion proofs, exact certificate arguments
and review. Separate agents independently checked the all-policy scope,
global optimization, support handling, event boundaries and perturbation
claims. The finite verifier was derived from the stated balances and
compared with the rational certificates. These are internal reviews and
reproducible arithmetic, not human external certification or formal proof
assistant verification.

Two new primary comparisons cover resource-producing project scheduling
and budget minimization. Root separately retrieved the first primary PDF
and read its relevant full model/exchange/continuous sections. The second
PDF request failed, but its versioned primary HTML supplied the full model
and Theorem 2 / Corollary 3 proofs. Source release and initial-resource
investment are established themes. The direct mappings tested do not
preserve the full S1 problem; that is not priority clearance. No third-party
full text was added to the repository or inaccessible old endpoint repeatedly
retried. Operational meaning remains conditional on the accounted source
bottleneck, independent service and immutable-drain interface.

The old current order is archived as
[029](../work_orders/archive/029-common-drain-cold-test.md), with its relative
research link adjusted for its new location. The instructions otherwise
remain unchanged. [030](../work_orders/archive/030-exact-common-drain-robustness.md)
records the completed follow-on questions and outcomes. The next task is
[pass 31](../work_orders/CURRENT.md): a focused contribution and service-meaning
audit, not an automatic higher-dimensional extension. Manuscript work stays
last and submission readiness remains unestablished.

## Verification and publication

The new `analysis/verify_common_drain.py` uses exact rational arithmetic for
the witness, barrier and event inequalities, all six concentrated-state
certificates, global curvature constants, positive-tolerance endpoints and
strict-slack witness, and the failed calibration comparison. Its report
explicitly limits these checks to arithmetic; the continuous all-policy
claims rest on the proofs. Its optimization and protected-output guards
were checked. The current route contains twelve suites and eleven analytical
report comparisons, all run after integration.

Before publishing, test a fresh archive of a fixed local commit and compare
all eleven reports. The publish commit message records the actual tested
commit/tree and completed gate. Re-read remote main, preserve concurrent
changes, update non-forcibly and verify the resulting tree. If the connected
GitHub API creates a different commit identifier for the same tested tree,
preserve the local tested commit on its own branch before synchronizing main.
Do not describe working-tree execution alone as committed verification.

The original LICENSE blob remains
`e17a781bf47c4aadf18b68fc593846a1193b86c1`. Both dated checkpoint directories,
every earlier research note and analytical report, old verification code and
the full paper/ tree are unchanged from the starting commit. Only current
README/STATUS/work-order navigation and new research/code/report files changed.
No manuscript build, outside contact, spending, submission or formal release
occurred.

## Exact restart

1. Inspect actual branch, HEAD, remote main and uncommitted changes. Read
   actual WORKSPACE.md first; do not reset to the provenance anchor above.
   Read AGENTS, README, STATUS, this continuation and CURRENT.
2. Run the twelve suites and eleven report comparisons in STATUS, preserving
   original LICENSE, checkpoints and manuscript. Read the complete new proofs
   and source limitations rather than relying on the current summary.
3. Execute pass 31's bounded prior-theorem and concrete-interface audit.
   Preserve the exact minimum, certified epsilon interval, nonquantified
   open-family conclusion and unresolved significance as separate claims.
   Do not call endogenous resource production, convexity or front-loading
   a new general scheduling principle.
4. Record a concrete reduction, retained contribution or failed interface;
   archive/update the order and continue with the next justified S1 task
   within the available session. Do not accumulate parameter variants to
   avoid the novelty and meaning questions.
5. At limits, verify and publish a coherent checkpoint with exact restart
   instructions. No research continues in the background after the turn ends.
