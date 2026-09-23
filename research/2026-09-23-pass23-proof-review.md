# Pass 23: critical-startup proof and precision audit

23 September 2026. This is an internal adversarial mathematical review,
not an independent human review or a literature-priority assessment. The full
[pass-14 target proof](2026-09-22-pass14-critical-startup.md),
[pass-15 viability proof](2026-09-22-pass15-critical-viability.md),
[two-module companion](2026-09-22-pass15-two-module-boundary.md),
[pass-18 precision proof](2026-09-22-pass18-precision.md), and
[pass-19 concentration proof](2026-09-22-pass19-tolerance-concentration.md)
were read together with the current mandate and pass-23 opening.

## 1. Proof verdict and quantifiers

No mathematical defect was found in the reviewed critical-startup results.
Their combination establishes the stated two-versus-three-module boundary
inside the ideal proportional-loss model, subject to its finite-cold-exit
restriction. Several distinctions are essential to that verdict.

- The pass-14 obstruction is an all-policy obstruction on one admissible
  loss history: simultaneous maximal feedback. This suffices to disprove a
  guarantee against every admissible loss history. It need not obstruct a
  favorable-loss realization.
- The target theorem concerns finite domination of one specified critical
  target. It does not characterize entry into the whole deadline-ready set.
  The pass-15 construction therefore contradicts no conclusion of pass 14.
- The convergence theorem is stated on the maximal-loss history. Its storage
  derivative and excess-upkeep integral do not automatically hold on a
  smaller-loss history. The construction's readiness guarantee does hold
  on every history, by coordinatewise comparison with its explicit virtual
  maximal-loss path.
- In the convergence proof, integrability and uniform Lipschitz continuity
  force the excess upkeep to vanish. They initially imply approach to the
  minimizing set, not convergence to a point. The finite minimizing set,
  obtained from the every-minimizer concentration theorem, and continuity
  of the trajectory supply the final point-convergence step.
- A finite warmup is not itself deadline-ready. After that warmup the
  guarantee applies to every subsequent counterfactual request time; a
  realized request then starts the post-request schedule. There are no
  normal-operation transfers or normal-operation capacity releases.

The two-module proof uses more than the generic convergence argument. In its
partial/cold case the cold-prefix coefficient restriction is necessary for
the separating inequality. In its full/cold case with the slower cold
coordinate, the exact-full barrier must be handled separately: the
cost-decreasing delayed-full variation excludes a competing order at the
limit, and continuity then excludes nearby subfull ready states. The proof
does this without assuming that the optimal state's deadline is tight. The
all-full case treats deadline zero separately. Those details prevent the
generic scalar example in the pass-23 opening from invalidating the S1
dimension conclusion.

The three-module certificate also includes waiting decay correctly. Its
second-stage identity uses global completion time, and its final stage uses
the original request-time preparation in the slow coordinate. The exact
rational bound holds throughout the whole specified tail interval, rather
than only at selected request times.

The new [positive-reachability comparison](2026-09-23-pass23-positive-reachability.md)
was also read in full. Its exact reflection-to-linear-system reduction
retains the box as a path constraint. The compactness, convexity and downward
closure of finite-time endpoint sets, the nonnegative-support-direction
argument, and robust replay for upward target/path constraints are valid.
The terminal-box counterexample checks exactly: its uncapped intermediate
value satisfies `z^2=5/8<1`, and every capped path obeys
`Z(t)<=-1/20-(3/4)exp(-2t)<0`. No defect was found in these deductions. This
review of the comparison note is distinct from its author's primary-source
inspection record; it does not assert a second full reading of that source.

The source-comparison pass also supplies a useful non-S1 control example
with the same positive linear upkeep and leaky normal dynamics: take
`s=1`, coefficients `(2,1/2)`, caps `(1,1/2)`, and the upward region
`p_1+p_2^2/4>=1/2`. Its cost minimum is uniquely `(1/2,0)`, because the
minimum on the boundary is `1+(p_2-p_2^2)/2`, strictly greater than one
for `0<p_2<=1/2`. The first coordinate remains below `1/2` after every
finite cold history. Warming the second coordinate to `1/4` takes
`2 log(8/7)`; subsequent input `(1,0)` gives readiness excess
`exp(-t)/64-exp(-2t)/2`, nonnegative exactly when `t>=log32`.
These constants and the upward-comparison guarantee check. Thus even
positive upkeep and the same normal dynamics allow a two-dimensional
separation for another ready region. The S1 two-module result relies on
the schedule-generated ready geometry, not merely positivity or normal
resource constraints.

## 2. Positive tolerance excludes dynamic indefinite readiness

The fixed-tolerance lower bound in pass 18 is not merely an obstruction to
holding a stationary nominal state. Its stated all-policy implication is
correct and admits a short quantitative form.

Let `C(H)=s>0`, fix `epsilon>0`, and let

$$\mathcal R_{H,\epsilon}
=\{p:F((p-\epsilon)_+)\leq H\},\qquad
\eta=\gamma_{\min}\epsilon>0.$$

At every nominal state in this set, pass-18 Lemma 6 gives

$$L(p)\geq s+\eta.$$

On the admissible maximal-loss normal history, any measurable causal
allocation policy obeys, almost everywhere,

$$Q'\leq s-u-L(p)\leq-\eta-u,
\qquad Q=\sum_i p_i.$$

Consequently, if its nominal path remains in this fixed-tolerance ready set
throughout an interval `[T,T+\ell]`, then

$$\eta\ell+\int_T^{T+\ell}u(t)\,dt
\leq Q(T)-Q(T+\ell)\leq Q(T)\leq\sum_iM_i.$$

In particular,

$$\ell\leq\frac{Q(T)}{\gamma_{\min}\epsilon}
\leq\frac{\sum_iM_i}{\gamma_{\min}\epsilon}.$$

If the set is empty there is no entry at all. Otherwise this bound excludes
indefinite residence after any finite warmup, even for rotating, adaptive,
parallel or otherwise nonstationary preparation. It also excludes such
residence from paid initialization: finite stored preparation cannot fund a
strict recurring deficit forever. A robust guarantee is impossible because
it must include this maximal-loss history.

The tolerance is the repository's one-time request-time deficit contract,
tested at every possible request time. The proof does not impose a stream of
physical state resets during normal operation or assert impossibility under
every favorable loss history. No stochastic interpretation is needed.

This residence bound is an elementary consequence of the existing
dissipation inequality, not a new central contribution. It makes precise why
nonstationary viability cannot rescue the critical separation from a fixed
positive preparation tolerance at the unchanged source budget.

## 3. Which sensitivity question remains meaningful

The exact three-module example uses strict inequalities to exclude every
competing concentrated state, and the slow third coordinate decays strictly
more slowly than the target-support deficits. Its occurrence is therefore
not tied to the displayed integer coefficients or one special release rate.
The [pass-24 follow-on](2026-09-23-pass24-critical-family.md) gives explicit
open sufficient inequalities and a uniform tail certificate for this claim.

That follow-on calibrates the deadline to remain on `C(H)=s`. It does not
claim an open region of exact criticality when the deadline is independently
perturbed, and it does not restore positive-tolerance readiness. Parameter
persistence on a calibrated critical family and robustness to request-time
shortfall are different properties; here the former holds while the latter
fails.

The result's significance must therefore be assessed as a structural boundary
in an ideal resource model. Generic convergence, asymptotic approach without
finite arrival, and storage depletion cannot alone carry its novelty claim.
The source audit and contribution decision remain separate tasks.
