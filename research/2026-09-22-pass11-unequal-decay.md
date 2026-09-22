# Pass 11: unequal proportional decay still forces concentration

22 September 2026. The common coefficient in the pass-10 concentration theorem
is unnecessary. Positive proportional loss with module-specific coefficients
still forces every upkeep-minimizing readiness state to have at most one
genuinely partial coordinate. The proof uses a two-coordinate exchange in an
attaining serial schedule. It does not use a common exponential transform and
does not claim that an arbitrary concentrated state's partial module should
be processed first.

This is an ideal-model theorem. The independent instantaneous-transfer
interface, paid initialization, and unresolved attribution questions from the
preceding notes remain in force. The result is not a publication-novelty or
physical-implementation claim.

## 1. Model and statement

Use the [pass-9 smooth-loss model](2026-09-22-pass9-smooth-partial.md), with

$$M_i>0,\qquad a_i\geq0,\qquad \gamma_i>0,\qquad
g_i(p)=\gamma_i p.$$

There are finitely many modules, source spare capacity is `s>=0`, and a
completed set `C` supplies preparation capacity

$$b(C)=s+\sum_{i\in C}a_i.$$

Before completion the maximum-loss dynamics are `p_i'=v_i-gamma_i*p_i`, with
upper reflection at `M_i`, nonnegative measurable allocations, and aggregate
rate at most `b(C)`. Each independently transferable full module releases
`a_i` instantaneously. Robust policies allow every simultaneous loss history
`0<=rho_i(t)<=gamma_i*p_i(t)`, including maximum feedback on every module.

Let `F(p)` be the exact robust exit time from the initial vector `p`. For a
finite deadline `H>=0`, define

$$C(H)=\min\left\{\sum_i\gamma_i p_i:
0\leq p_i\leq M_i,\ F(p)\leq H\right\}.                 \tag{1}$$

Pass 9 proves that the ready set in (1) is compact and nonempty, and that a
finite optimal exit is attained by a full-capacity serial schedule after
immediately transferring all initially full modules. Nonemptiness holds even
when spare capacity is zero: the all-full vector exits immediately. Since the
objective in (1) is continuous, a minimizing vector exists.

Call a coordinate **partial** when `0<p_i<M_i`.

**Theorem (unequal proportional concentration).** Every minimizing vector in
(1) has at most one partial coordinate. Consequently a minimizing state
consists of a fully ready subset, at most one partial module, and otherwise
cold modules.

Sections 2–4 first establish the assertion under the transparent sufficient
condition

$$s>\max_i\gamma_i M_i.                                  \tag{2}$$

Section 5 removes (2). The final theorem applies for every `s>=0` under the
other displayed assumptions. Strict positivity of each `gamma_i` is retained.

## 2. Exact two-module elimination

Take two modules, assume (2), and first consider the serial order `1,2`. Put

$$b_1=s,\quad b_2=s+a_1,\quad
D_1=b_1-\gamma_1M_1>0,\quad D_2=b_2-\gamma_2M_2>0.$$

For initial preparation `(x,y)`, let `t_1` be the first completion time and
`T` the final time. Modules may initially be full and deliberately wait for
their specified turns; these are valid comparison schedules over the entire
closed preparation box. The exact maximum-loss equations give

$$e^{\gamma_1t_1}=\frac{b_1-\gamma_1x}{D_1},\qquad
D_2e^{\gamma_2T}=b_2e^{\gamma_2t_1}-\gamma_2y.$$

Thus this order meets deadline `H` exactly when

$$y\geq f_H(x):=
\frac{b_2\left((b_1-\gamma_1x)/D_1\right)^{\gamma_2/\gamma_1}
-D_2e^{\gamma_2H}}{\gamma_2}.                              \tag{3}$$

For each fixed `x` its least-cost feasible second coordinate is
`max(0,f_H(x))`, provided that value does not exceed `M_2`. This accounts for
cold and full clipping explicitly. If both coordinates of an optimum for
this order were strictly interior, its second coordinate would lie on the
positive, unclipped branch of (3). The relevant objective there is

$$c(x)=\gamma_1x+
b_2\left((b_1-\gamma_1x)/D_1\right)^{\gamma_2/\gamma_1}
-D_2e^{\gamma_2H}.                                       \tag{4}$$

If `gamma_2<gamma_1`, the positive power in (4) lies strictly between zero
and one, so `c` is strictly concave. It has no local minimum at an interior
point of the feasible interval. If `gamma_2>=gamma_1`, differentiation gives

$$c'(x)=\gamma_1-
\frac{b_2\gamma_2}{D_1}
e^{(\gamma_2-\gamma_1)t_1}<0.                              \tag{5}$$

Here `t_1>=0`, `b_2>=b_1>D_1`, and `gamma_2>=gamma_1`. Thus it again has no
interior local minimum. The reversed order has the same argument with the
indices interchanged. The full-state serial theorem makes these two orders
sufficient for all post-request policies. Therefore no two-module upkeep
minimum can have two partial coordinates.

This calculation is not an assumption that the ready set is convex. The
power in (3) generally prevents the common-gamma halfspace representation.
The boundary alternatives include a cold coordinate or a full coordinate;
each already has the claimed concentration shape.

## 3. A general serial order: vary two consecutive partial coordinates

Suppose a deadline-feasible initial vector contains at least two partial
coordinates. Choose an attaining serial exit schedule, transferring all
initially full modules at time zero. Among the remaining modules choose two
partial coordinates `j,k` that are consecutive **among partial coordinates**
in that serial order. Every intervening module is cold initially. Earlier or
later partial coordinates are allowed.

Let `t_0` be the start time of stage `j`, `t_j` its end, and `t_k` the end of
stage `k` in this schedule. Write `b_j,b_k` for the available capacities of
the two stages and

$$D_j=b_j-\gamma_jM_j>0,\qquad
D_k=b_k-\gamma_kM_k>0.$$

Each intervening cold module has preparation zero when its turn starts,
since its passive proportional flow stays zero. Its stage duration depends
only on its own parameters and the completed set, not on absolute start
time. The sum `L>=0` of these intervening durations is consequently constant
when only initial preparation of `j,k` changes. Stage `k` starts at `t_j+L`.

Keep the entire schedule before `j` fixed. Replace `p_j` by `x`, so

$$t_j(x)=\frac1{\gamma_j}
\log\frac{b_j e^{\gamma_jt_0}-\gamma_jx}{D_j}.             \tag{6}$$

Choose the replacement `y(x)` for `p_k` so that stage `k` still ends at the
original global time `t_k`:

$$\gamma_k y(x)=
b_ke^{\gamma_kL}
\left(\frac{b_je^{\gamma_jt_0}-\gamma_jx}{D_j}
\right)^{\gamma_k/\gamma_j}
-D_ke^{\gamma_kt_k}.                                     \tag{7}$$

At the original value `x=p_j`, equation (7) gives `y=p_k`. Both coordinates
are strictly interior, so continuity gives a two-sided open interval of
admissible variations retaining `0<x<M_j` and `0<y(x)<M_k`. All other initial
coordinates are unchanged. Capacities and cold-stage durations depend on
the fixed order, not on the initial preparation amounts.

The constructed times are genuine nonnegative stage times. Formula (6) has
`t_j(x)>=t_0` because `x<=M_j` and `t_0>=0`. For the second stage, with
`u=t_j(x)+L>=0`, equation (7) and `y(x)<=M_k` imply

$$D_ke^{\gamma_kt_k}
=b_ke^{\gamma_ku}-\gamma_ky(x)
\geq D_ke^{\gamma_ku},$$

and hence `t_k>=u`. There is no extra negative-duration constraint hidden in
the algebra. Locally these durations are strictly positive because the two
chosen initial coordinates remain subfull.

After stage `k` ends, the global time and completed set agree exactly with
the original schedule. Every later unserved module has its original initial
preparation and has simply decayed passively to that same time. The whole
remaining suffix therefore reproduces the original schedule. The new vector
meets the same final deadline, not merely an approximate deadline.

## 4. Strict local cost improvement

Only the maintenance cost of the chosen pair varies. Its sum is

$$\begin{aligned}
c(x)
&=\gamma_jx+\gamma_ky(x)\\
&=\gamma_jx+b_ke^{\gamma_kL}
\left(\frac{b_je^{\gamma_jt_0}-\gamma_jx}{D_j}
\right)^{\gamma_k/\gamma_j}
-D_ke^{\gamma_kt_k}.                                     \tag{8}
\end{aligned}$$

If `gamma_k<gamma_j`, the exponent is strictly between zero and one. The
nonconstant affine base is positive, so the nonlinear term and hence `c`
are strictly concave. At every point of the open variation interval, at
least one sufficiently small one-sided change strictly lowers `c`. For
example, strict concavity places the current value strictly above the
average of two equally spaced neighboring values.

If `gamma_k>=gamma_j`, its derivative is

$$c'(x)=\gamma_j-
\frac{b_k\gamma_k}{D_j}
e^{\gamma_kL}e^{(\gamma_k-\gamma_j)t_j(x)}<0.              \tag{9}$$

Indeed `b_k>=b_j>D_j>0`, both times in the exponential factors are
nonnegative, and `gamma_k>=gamma_j>0`. A sufficiently small increase in `x`
therefore strictly lowers cost, with (7) decreasing `y` and keeping both
coordinates interior.

Either case yields a strictly cheaper deadline-feasible vector. A vector
with two partial coordinates consequently cannot minimize (1). Applying
this contradiction to an attained global minimum proves the theorem under
(2). In fact it proves the stronger statement about **every** minimizer,
without an iterative exchange, an endpoint limit, or selection of a special
minimum.

## 5. Removing the initially ample-capacity condition

The argument needs positive denominators only in the actual serial stages
used by a feasible state. It does not need all modules to be accessible at
the original capacity `s`.

For arbitrary `s>=0`, choose an attaining finite serial schedule for a ready
state, and transfer all initially full modules immediately. Every remaining
module is initially subfull and stays subfull while waiting. A proportional
stage with available rate `b` can reach `M_i` from below in finite time if
and only if

$$b>\gamma_iM_i.$$

At equality its full-rate trajectory approaches `M_i` only asymptotically;
below equality its equilibrium is below `M_i`. Thus every stage of the
chosen finite schedule has strictly positive denominator. This includes
the two selected partial stages and all intervening cold stages.

The small variations (6)–(7) retain both selected coordinates in their
interiors, and leave the order and all capacities unchanged. All stage
denominators stay positive. The proof in Sections 3–4 now applies verbatim.

**Corollary (all source budgets).** The concentration theorem holds for all
`s>=0`, including inaccessible initial rates and zero spare capacity. Those
cases affect which ready vectors and serial orders are feasible; they do
not permit an upkeep-minimizing vector with two partial coordinates.

The statement is consistent with degenerate cases. For `H=0`, every module
must initially be full. If the only ready state for a chosen deadline is
all-full, the assertion is immediate. If some releases are zero, (9) is
still strict because `b_j>D_j`, using `gamma_jM_j>0`. If a coefficient were
zero, strictness and the claim about every minimum would require a separate
formulation: zero-cost partial coordinates could be present without making
the objective worse. That extension is not asserted here.

## 6. A necessary condition on cold modules before the partial one

**Corollary (optimizer prefix).** Suppose a minimizing state has a genuinely
partial module `k`. In any deadline-feasible serial schedule for that state
which transfers all initially full modules at time zero, every cold module
`j` occurring before `k` satisfies

$$\gamma_j>\gamma_k.$$

**Proof.** Concentration has already excluded every other partial coordinate,
so the modules between such a `j` and `k` are cold. Apply (6)–(9), now at
`x=p_j=0` rather than an interior value. If `gamma_j<=gamma_k`, the derivative
in (9) is strictly negative. A sufficiently small positive change in `x`
is feasible, and (7) strictly decreases the initially interior coordinate
`p_k` while keeping it interior. The endpoint of stage `k` and the entire
suffix are unchanged. This gives a strictly cheaper ready vector, contrary
to minimality. The rate-barrier argument in Section 5 still applies.

This is a condition on schedules witnessing an **upkeep-minimizing** state,
not an index rule for arbitrary concentrated states. In particular, when all
coefficients are equal, a minimizing state's partial module must precede all
cold modules in such a schedule. Unequal coefficients permit a cold prefix
only from strictly faster-decaying modules; the statement does not establish
that every such prefix is useful or sufficient.

## 7. What this changes, and what it does not

The result extends the structural conclusion of the
[common-decay frontier](2026-09-22-pass10-proportional-frontier.md) to unequal
positive proportional coefficients and arbitrary source budgets. The exact
quadratic-loss counterexample in that note remains valid. It separates
proportional loss from general monotone smooth loss, while equality of the
proportional coefficients is no longer a necessary concentration assumption.

The recurring reduction from pass 9 still gives the exact guaranteed normal
optional throughput `s-C(H)` when `C(H)<=s`, and rules out indefinite
all-request-time readiness when `C(H)>s`. Its proof uses the total-storage
potential and simultaneous maximal loss. An attaining target is initialized
at paid cost and maintained using `v_i=gamma_i*p_i`; under smaller losses the
actual state remains at least that target. Concentration is a statement about
the minimizing target, not a cold-start reachability claim.

Two algorithmic cautions remain:

- Unequal coefficients do not admit the single affine exponential recurrence
  used in pass 10. Its rational transformed-deadline arithmetic and
  `O(n*2^n)` frontier formula cannot simply be carried over.
- Concentration does not imply that the one partial module precedes every
  cold module in a relevant serial order. Section 6 restricts a possible
  optimizer's cold prefix to strictly faster-decaying modules but does not
  eliminate that prefix. An exact frontier algorithm must account for it
  unless a separate theorem removes it.

The proof supplies the structural input for such a finite frontier
characterization. A separate algorithm must state its own feasibility tests,
rate-barrier treatment, transcendental representation, and operation count.
The standard scalar-flow calculation, serial reduction, compactness, and
cost averaging remain separately attributable ingredients; this local
exchange result does not by itself settle the literature comparison or the
operational significance of the full model.
