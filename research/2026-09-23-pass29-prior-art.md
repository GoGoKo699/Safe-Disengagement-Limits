# Pass 29: common drains and resource-producing scheduling

23 September 2026. Bounded primary-source audit for the three-module
common-drain [counterexample](2026-09-23-pass29-cold-test.md). Manuscript
writing remains paused. This note
extends the existing [delivery-tail comparison](2026-09-23-pass26-prior-art.md),
[deterioration comparison](2026-09-23-pass20-deterioration-prior-art.md), and
[generalized-concavity attribution](2026-09-23-pass22-curved-exchange-attribution.md).
Those reductions and access limits remain in force.

The new literature check does not clear novelty. Resource production,
resource release, initial-resource minimization, and exchanges that cluster
work are established scheduling themes. The relevant S1 question is the
specific concentration boundary with continuous perishable preparation,
decay-linked upkeep prices, a common drain, and the full policy class.

## 1. New sources and actual inspection

**A. Sahli, J. Carlier and A. Moukrim**, *Polynomial algorithms for some
scheduling problems with one nonrenewable resource*, RAIRO Operations
Research **55** (2021), 3493–3511,
[DOI 10.1051/ro/2021164](https://doi.org/10.1051/ro/2021164),
[complete primary PDF](https://www.numdam.org/item/10.1051/ro/2021164.pdf).
Read Sections 2–4.5, printed pp. 3495–3505: the model, complete proofs of
Theorems 3.1, 4.2, 4.5–4.8 and associated corollaries, and the continuous
extension. Section 1 supplied context; later special cases were not audited.
Events change a resource stock and obey time lags. Parallel chains admit
grouping and Johnson-rule ordering for minimum initial stock. Section 4.5
uses preemptive tasks with a prescribed production/consumption profile
indexed by elapsed processing time. The paper also explains how renewable
resource scheduling can be encoded with consumption and production events.
Consequently, the mere presence of endogenous resource release cannot
distinguish S1. The continuous extension describes a construction rather
than a separately numbered proof; it is not imported as an S1 theorem.

**M. Gottschau, F. Happach, M. Kaiser and C. Waldmann**, *Budget
Minimization with Precedence Constraints*,
[arXiv:1905.13740v2](https://arxiv.org/abs/1905.13740),
[complete primary PDF](https://arxiv.org/pdf/1905.13740), dated 26 June 2019.
Read the introductory model and attribution note, and complete Theorem 2
and Corollary 3 with their proofs, printed pp. 1–4. Fixed signed job costs
define a maximum-prefix-sum budget; processing times are omitted. Theorem 2
preserves the minimum budget after retaining only precedences from
nonnegative-cost jobs to negative-cost jobs. Its exchange proof restores
discarded precedences without increasing the budget. The authors explicitly
identify antecedents in maximum cumulative cost scheduling. The later
irreducible-block algorithm was not audited and is not used here.

These are the only two new full-result comparisons in this pass. Broader
search results were screened only to select them. Previously inaccessible
Chen, Glazebrook and other endpoints were not retried. Neither third-party
PDF is added to the repository.

## 2. What the direct resource interpretation preserves

The following are deductions about S1, rather than theorems attributed to
either paper. Let t_i be an ownership handoff, let ell be the common drain,
and put D=H-ell. A useful S1 witness obeys

$$
p_i'(t)=v_i(t)-\gamma_i p_i(t),\qquad
0\leq p_i(t)\leq M_i,
$$

before its first full-state handoff, with

$$
\sum_i v_i(t)\leq b(t),\qquad
b(t)=s+\sum_i a_i\mathbf1_{t\geq t_i+\ell},\qquad t_i\leq D.
$$

Interpreting a drain completion as a capacity-production event is valid at
the level of the available-rate bookkeeping. It does not make resource
production a new phenomenon. Likewise, the handoff-to-drain interval is an
ordinary positive time lag, and all common tails yield a common handoff
deadline. None of these identifications proves the concentration theorem
or its failure.

The missing object in a direct event-only representation is the evolving
preparation requirement. Holding a module idle for a time Delta changes
its positive preparation by the factor `exp(-gamma_i*Delta)`. This change
depends on elapsed calendar time even when that module receives no input.
Reordering fixed-cost events without tracking this change does not preserve
its handoff feasibility. Assigning a fixed signed cost to each S1 module
therefore does not reproduce the initial-state optimization.

The continuous-profile comparison has a related obstruction. Its local
progress clock freezes when its activity is interrupted. S1's preparation
continues to decay. Even on a serial segment with constant available rate
b and no earlier preparation input to that module, the duration from a
start t to handoff is

$$
\delta_i(t,x_i;b)=\frac1{\gamma_i}
\log\frac{b-\gamma_i x_i e^{-\gamma_i t}}
               {b-\gamma_i M_i},\qquad b>\gamma_i M_i.
$$

For `x_i>0` this depends on the calendar start. A source reservation can
also finish draining during this segment and change b. Selecting x_i is
thus not simply selecting a fixed duration or an invariant local resource
profile for that module.

These observations reject the stated substitutions, not every possible
encoding. A general event framework could be extended with clock-dependent
states, or a sufficiently elaborate reformulation might exist. No theorem
excluding all nonlinear lifts is claimed. Conversely, such a framework's
ability to describe the instance would not itself prove the minimum's
concentration structure.

## 3. The certificate ingredients remain ordinary allocation

Fix the handoff times. Then the capacity history is fixed and discounted
state coordinates give

$$
M_i e^{\gamma_i t_i}
=x_i+\int_0^{t_i} e^{\gamma_i u}v_i(u)\,du
$$

for reflection-free useful input. Allowing reflection or dropping a cap
only yields the corresponding necessary inequality. The fixed-time
allocation constraints are linear in the initial states and input measures.
Positive weighted sums of these inequalities are ordinary lower-bound
certificates.

A particularly useful relaxation assigns the shared pre-release input
between a required module and a cold terminal module. If the two discounted
weights are `e^(alpha*t)` and `e^(rho*t)` with `rho>alpha`, their ratio
`e^((alpha-rho)*t)` strictly decreases. To supply a fixed amount of the
first weighted work while sacrificing as little of the second as possible,
one fills the earliest times first. This is the elementary threshold or
bathtub allocation rule: exchanging a later assigned infinitesimal amount
with an earlier unassigned one proves it. A time threshold and its exact
integral supply the bound; a new general scheduling principle is not needed.

The final fixture admits a simpler route: its capacity barrier forces the
first two handoffs to occur before any release. Two applications of the
existing first-completion front-loading lemma then reduce the low-cost
competitors to A,B,C or B,A,C. The weighted relaxation above is not needed
by that final certificate. Nor does this fixture-specific reduction prove
serial optimality for arbitrary drain instances.

The substantive burden of a three-module separation is different. The
bound must cover every concentrated initial state, all handoff orders,
prewarming, simultaneous preparation, reflection, and initially full
coordinates. A feasible two-partial policy alone, or a local minimum along
one serial family, is insufficient. The
[preserved failed fixture](2026-09-23-pass29-preserving-attempt.md)
demonstrates that distinction: its local curvature did not prevent a
cheaper concentrated competitor.

## 4. What the three-module separation adds

The already proved common-drain two-module result and the arbitrary-n
common-coefficient result set a precise target. The pass-29 counterexample
provides a robust ready state of upkeep `37/200`, whereas every concentrated
ready state has upkeep strictly above `1851/10000`. Its global comparison
establishes the smallest module count, three, at which a common drain can
destroy concentration. Matching every module's handoff deadline is therefore
insufficient once a cold terminal obligation couples the earlier release
times. Read the complete counterexample proof for the rational fixture and
all-policy exclusions; this source comparison does not replace that proof.

That conclusion does not require interruption or parallel preparation to
be essential. The serial feasible witness beats every concentrated state
even when those competitors are allowed arbitrary policies. The failure
concerns the allocation of maintained preparation, while the
delayed releases couple the durations available to the cold terminal work.
Calling it a necessary preemption effect would misidentify the mechanism.

The minimal-dimension conclusion concerns this ideal proportional-loss
interface and ordinary zero-deficit physical caps. It does not show that
every three-module system requires multiple partials, that the exhibited
state is itself the unique or exact global minimizer, or that common drains
are always worse than instantaneous release. An explicit upper bound below
all concentrated costs proves a separation without giving the optimal
value or all its coordinates.

The subsequent [exact-optimum proof](2026-09-23-pass30-exact-optimum.md)
and [robustness continuation](2026-09-23-pass30-robust-common-drain.md) do
establish the unique optimizer, a certified exact nominal frontier and an
open family. Those conclusions require their separate arguments; they are
not inferred from this separation or from either scheduling source.

This narrows the potential contribution to a structural assumption boundary.
It does not settle priority, engineering adequacy, or publication value.
The prior-art search supplies no identified theorem that gives this boundary
by the tested substitutions; its bounded scope cannot establish absence
from the literature. Keep the distinction from established allocation,
resource production and generalized-concavity tools explicit in any later
contribution assessment. More dimensions or a larger simulation would not
resolve the remaining attribution and meaning questions.
