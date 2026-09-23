# Pass 30: exact common-drain optimum and robustness — completed

23 September 2026. This retrospective work-order record follows the completed
pass-29 all-policy concentration separation. The task was to strengthen that
specific result, without adding modules or developing a numerical scheduler.

The questions were whether the exhibited two-partial state is the actual
global optimizer, and whether its advantage survives fixed positive request
error, paid cold startup and a non-calibrated parameter neighborhood.

The [exact-optimum proof](../../research/2026-09-23-pass30-exact-optimum.md)
establishes the unique global initial state `(3/100,1/8,0)` and value
`37/200`. The proof first uses all-policy support and order reductions;
only then does a uniform scalar curvature bound establish globality.

The [robustness proof](../../research/2026-09-23-pass30-robust-common-drain.md)
establishes the exact unique nominal optimizer
`(3/100+epsilon,1/8+epsilon,0)` with value `37/200+3*epsilon` for
`0<=epsilon<=1/30000`. A slightly more prepared witness supplies strict
deadline slack, fixed positive tolerance, normal optional throughput and
finite radial cold warmup. Joint-parameter compactness preserves the strict
concentrated gap in a relative open common-drain family. No neighborhood
radius or exact optimizer formula for perturbed parameters is asserted.

Separate internal reviews and exact rational certificate checks passed.
The [assessment](../../research/2026-09-23-pass29-30-assessment.md) selects
contribution and operational-meaning review as the next task. These findings
do not clear publication novelty or authorize manuscript work or submission.
