# Pass 23: positive linear reachability is the normal-operation baseline

23 September 2026. This comparison concerns normal preparation before a
request, including cold warmup. It keeps the post-request transfer schedule
inside the definition of the deadline-ready set. It does not replace that
set by an arbitrary halfspace, remove preparation caps, or claim a new
reachability algorithm.

The conclusion is a partial prior-art reduction with an exact scope. Normal
preparation is a state-constrained positive linear control system. Its
uncapped endpoint support function is a direct substitution into an
inspected published result. The two-versus-three-module critical-startup
boundary additionally uses the shape of the S1 deadline-ready set; that
boundary does not follow from the inspected support-function formula alone.
This observation is not a priority clearance for the boundary.

## 1. Primary source and inspection record

Antoine Girard and Colas Le Guernic, *Efficient Reachability Analysis for
Linear Systems using Support Functions*, Proceedings of the 17th IFAC World
Congress, Seoul, 2008, pp. 8966–8971.
[Proceedings PDF](https://skoge.folk.ntnu.no/prost/proceedings/ifac2008/data/papers/0569.pdf).

Inspected §2, §3.1 including Proposition 3 and its complete proof, §3.3, and
the complete §4: continuous-time model (9), Proposition 5, equation (10),
and its full proof across pp. 8969–8970. Proposition 5 gives the endpoint
support function for a linear system with compact convex initial and input
sets. Its proof uses variation of constants, pointwise upper bounds by input
support functions, and a maximizing support-vector control. It has no path
state constraints or infinite-horizon readiness conclusion.

The 2010 journal extension, *Reachability analysis of linear systems using
support functions*, DOI
[10.1016/j.nahs.2009.03.002](https://doi.org/10.1016/j.nahs.2009.03.002),
was located but its full relevant proof was not inspected: publisher access
was denied, a USC copy timed out/returned an error, and another mirror
denied access. No conclusion below is attributed to that extension.

The formula specialization and cap analysis below are written out here;
they are not reported as new theorems of the cited paper.

## 2. Exact comparison objects

Let

$$B=\prod_{i=1}^n[0,M_i],\qquad
\Gamma=\operatorname{diag}(\gamma_1,\ldots,\gamma_n),\qquad
U_s=\{v\in\mathbb R^n:v\geq0,\ \mathbf1^Tv\leq s\}.$$

All sizes and coefficients are positive, and `s>0`. During normal operation
there are no transfers and no capacity releases. Optional work can be set to
zero when testing existence of a cold-start policy. The maximal admissible
loss history is simultaneous proportional loss on every coordinate.

| Object | Normal control formulation | Additional S1 information |
|---|---|---|
| Dynamics | `p'=-Gamma*p+v`, `v in U_s`, with box path constraints | Smaller losses are covered by coordinatewise comparison |
| Cold state | `p(0)=0` | Warmup has no removal-deadline guarantee |
| Fixed target | Reach `z`, or a state dominating `z` | A critical concentrated target is tested in pass 14 |
| Deadline-ready region | A specified closed upward set `R_H` in `B` | `R_H={p:F(p)<=H}` comes from post-request scheduling and releases |
| Criticality | Minimum of `L(p)=sum gamma_i*p_i` over `R_H` equals `s` | Concentration makes the set of minima finite |
| Indefinite entry | Reach a state admitting a path that stays in `R_H` forever | Pass 15 compares this with reaching a minimum |
| Dimension boundary | Linear normal dynamics make sense in every dimension | The two-module proof uses ordering and endpoint properties of `F` |

An arbitrary compact convex input set in the source includes the simplex
`U_s`; positivity and a shared resource do not by themselves create a new
normal reachability problem.

## 3. Removing reflection without removing the box

On the maximal-loss history, reflected dynamics agree with

$$p_i'=v_i-\gamma_i p_i$$

below `M_i`, and their derivative at the cap is
`min(v_i-gamma_i*M_i,0)`. There is an exact equivalence of trajectory classes:

> The reflected maximal-loss normal trajectories with inputs in `U_s` are
> exactly the trajectories of the ordinary linear system with inputs in
> `U_s` that stay in `B` at every intermediate time.

To prove the first direction, replace the input on a capped coordinate by
`min(v_i,gamma_i*M_i)` and leave every other input unchanged. This deletes
only input discarded by reflection, preserves nonnegativity, and cannot
increase the sum. The state and its derivative do not change. Conversely,
an absolutely continuous trajectory of the linear system staying in the box
has derivative zero almost everywhere on a level set `p_i=M_i`. Thus its
input there equals `gamma_i*M_i` almost everywhere, and reflection does not
change the trajectory. Statements about derivatives are almost-everywhere
statements, which is sufficient for measurable controls.

Let `A_T` denote the endpoints reached at fixed finite time `T` by these
box-constrained linear trajectories from cold. It is compact, convex, and
downward closed in the nonnegative orthant.

* Convexity follows by taking convex combinations of controls and their
  corresponding paths. The input simplex and every box constraint are
  convex.
* Compactness follows from bounded controls and the variation-of-constants
  formula. For a sequence of admissible controls, a weak-star convergent
  subsequence in `L^infinity([0,T])` preserves the simplex constraints. Its
  corresponding paths have a uniformly convergent subsequence by uniform
  boundedness and equicontinuity. The integral equation passes to the limit,
  and the limit stays in the closed box. Thus endpoint limits are attained.
* If an attained endpoint is `x` and `0<=y<=x`, scale the entire trajectory
  and control in coordinate `i` by `y_i/x_i` when `x_i>0`, and by zero
  otherwise. The resulting linear trajectory ends exactly at `y`, stays in
  the box, and consumes no more input at any time.

Consequently, reaching a state dominating a fixed target `z` at time `T`
is equivalent to `z in A_T`. This elementary downward-closure fact does not
mean that reaching a ready state requires reaching a minimum-cost ready
state: a general ready state need not dominate any such minimum.

The deterministic maximal-loss path also settles the existence quantifier
for robust cold entry into an upward target or an upward path constraint.
Necessity follows because maximal loss is allowed. For sufficiency, replay
the chosen measurable normal allocation as an open-loop schedule. Under
every smaller loss history, reflected scalar comparison keeps the actual
state above the virtual maximal-loss state. Upward target membership is
therefore preserved. An input produced by a deterministic feedback policy
along its maximal-loss realization can likewise be replayed. This argument
concerns existence, not optimal feedback implementation under an unknown
initial state.

## 4. Direct support-function reduction, with its limitation

Temporarily omit the upper caps and call the cold endpoint set `A_T^free`.
The source's Proposition 5 applies with

$$A=-\Gamma,\qquad I=\{0\},\qquad V=U_s.$$

The simplex support function is

$$h_{U_s}(w)=s\max\{0,w_1,\ldots,w_n\}.$$

Hence the exact uncapped support function is

$$h_{A_T^{\rm free}}(\ell)
=s\int_0^T\max\{0,\ell_1e^{-\gamma_1t},\ldots,
\ell_ne^{-\gamma_nt}\}\,dt. \tag{1}$$

There is also a direct proof: multiply the variation-of-constants formula
by `ell`, bound each integrand by the simplex support function, and allocate
the full input to an index attaining the largest positive discounted
coefficient. Choose the smallest index at ties and use zero input when all
coefficients are nonpositive. This gives a measurable maximizing input and
attains the integral. No discretization or simulation is involved.

Both endpoint sets are downward closed. Membership of a nonnegative target
in either compact convex endpoint set can thus be tested with all
nonnegative support directions. To see why, if a separating direction has
negative components, replace it by its positive part. Downward closure lets
a support maximizer set the negative coordinates to zero without leaving
the set, so the support value is unchanged, while its value on a
nonnegative target cannot decrease.

For `A_T`, however, the support value includes every intermediate cap
constraint. Equation (1) is only an upper bound:

$$h_{A_T}(\ell)\leq h_{A_T^{\rm free}}(\ell). \tag{2}$$

Deleting reflection is exact only because the box remains a path
constraint. Intersecting the uncapped terminal set with the physical box is
not a substitute, as the following exact example shows.

Take two coordinates with

$$s=1,\qquad \gamma=(1,2),\qquad M=(1/2,3/10).$$

The terminal vector `M` belongs to an uncapped reachable set at finite time.
First put all input into coordinate one until it has reached

$$z=\frac12\sqrt{\frac52}<1,$$

which takes `-log(1-z)`. Then put all input into coordinate two for
`(1/2)log(5/2)`. Its terminal value is
`(1/2)(1-2/5)=3/10`, while the first coordinate decays to `1/2`.
The earlier value `z>1/2` violates the first cap.

No capped normal policy reaches `M` at any finite time. Define
`Z=p_1+p_2-4/5`. On maximal loss,

$$Z'\leq1-p_1-2p_2
=-\frac1{10}-2Z+(p_1-1/2)
\leq-\frac1{10}-2Z.$$

Starting from `Z(0)=-4/5` gives

$$Z(t)\leq-\frac1{20}-\frac34e^{-2t}<0.$$

The desired endpoint has `Z=0`, a contradiction. Thus, for the displayed
uncapped arrival time,

$$A_T\ne A_T^{\rm free}\cap B.$$

This is a cap warning, not an S1 deadline-ready counterexample or a
counterexample to the source theorem, whose hypotheses do not contain
these path caps.

## 5. What the support-function reduction settles and leaves

Let `K_H` be the set of initial states from which some maximal-loss normal
trajectory stays in `R_H` for all future times. This is the ordinary
controlled viability kernel of `R_H` for the box-constrained linear system.
It is upward closed within `B`: replay a viable input from a larger state
and use reflected comparison. Robust finite cold entry into indefinite
readiness is therefore precisely

$$\text{there exists finite }T\text{ with }A_T\cap K_H\ne\varnothing.
\tag{3}$$

Equation (3) is a definition-level control reduction, not an explicit
calculation of `K_H`. Proposition 5 does not supply that kernel or replace
it by the set of stationary minima.

The generic parts of the existing startup package should be attributed
accordingly. Linear variation of constants, compact reachable sets,
input-resource support functions, finite versus asymptotic reachability,
and replay under monotone disturbances are standard mechanisms. Pass 14's
barriers and strict-slack constructions are explicit elementary calculations
inside this control class. Pass 15's dissipation-plus-compactness convergence
argument must not be advertised as a new general viability principle.

The S1 two-module proof uses additional facts absent from (1):

1. Every minimum of the schedule-generated ready region concentrates, so
   there are finitely many critical minima.
2. A partial/cold minimizing state obeys a coefficient-order restriction
   inherited from its post-request serial schedule.
3. A full/cold minimum at an exact initial rate barrier has a local
   alternative-order obstruction, including the effect of instantaneous
   transfer at the full endpoint.

For two modules those facts let the proof exclude every unreachable limiting
shape. A three-module state can use a third, slower-decaying coordinate that
is cold in the limiting optimum. Its positive transient preparation can
keep the state ready while the first two coordinates remain below the
unreachable target's support sum. The exact pass-15 example proves that
possibility; the support-function result neither states it nor rules it out.

The residual assessment is consequently narrow: the smallest-dimension
separation is a model-specific geometric statement still needing its own
significance and priority assessment. The existence of a familiar normal
control embedding removes broad conceptual novelty claims but does not,
on its own, prove the complete S1 boundary to be a corollary.

## 6. Positive precision excludes dynamic critical readiness too

The fixed positive request-time deficit contract in
[pass 18](2026-09-22-pass18-precision.md) applies to a nominal state `p` and
requires readiness of `q=(p-epsilon)_+`. It is a one-time deficit at a
counterfactual request, not an additional continuous disturbance during
normal operation.

At an originally critical budget `C(H)=s>0`, every feasible nominal state
satisfies

$$L(p)\geq s+\gamma_{\min}\epsilon.$$

Thus any maximal-loss normal trajectory satisfying this fixed-tolerance
contract throughout an interval `[T_0,T_1]` obeys

$$\gamma_{\min}\epsilon(T_1-T_0)
+\int_{T_0}^{T_1}u(t)\,dt
\leq Q(T_0)-Q(T_1)\leq\sum_i M_i. \tag{4}$$

This integrates `Q'<=s-u-L(p)` and applies to arbitrary dynamic policies.
In particular it excludes indefinite readiness; it is not merely the
failure of one stationary optimum. The coarse finite-duration bound (4)
is an elementary corollary of the existing margin proof, not a new
quantitative frontier or evidence of engineering robustness.

The exact two-versus-three statement survives as a mathematical boundary
of the zero-tolerance idealization. It cannot be presented as a robust
critical-budget operating advantage. An operational interpretation would
need a positive maintenance margin or a different, explicitly justified
precision contract before this boundary could carry such a claim.
