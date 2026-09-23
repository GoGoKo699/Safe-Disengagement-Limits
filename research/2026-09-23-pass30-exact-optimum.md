# Pass 30: the common-drain counterexample has an exact unique optimum

23 September 2026. This note strengthens the
[pass-29 strict separation](2026-09-23-pass29-cold-test.md) without changing
that earlier finding. In its exact three-module common-drain fixture, the
displayed state is the unique minimum-upkeep ready initial state:

$$x^*=\left(\frac3{100},\frac18,0\right),\qquad
\min_{x\in\mathcal R_H^{\rm drain}}L(x)=\frac{37}{200}.$$

This is a claim about the initial state, not uniqueness of an exit policy.
It concerns the ordinary zero-deficit physical-cap model. The proof uses
the all-policy concentrated comparison and the fixture-specific serial
reduction already established in pass 29, then an exact one-variable
convexity certificate. It does not assume that every common-drain system
has a serial optimal schedule.

## 1. Fixture and established reductions

Use the existing proportional-loss interface, simultaneous maximal-loss
adversary, independent immutable drains and linked upkeep
`L(x)=2x_A+x_B+3x_C`. The parameters are

$$\begin{gathered}
s=1,\qquad (\gamma_A,\gamma_B,\gamma_C)=(2,1,3),\\
(M_A,M_B,M_C)=
 \left(\frac{27}{242},\frac7{20},\frac{11679823}{10222080}\right),\\
(a_A,a_B,a_C)=\left(\frac{6075}{2662},1,1\right),\qquad
\ell=\log2,\quad D=\log4,\quad H=\log8.
\end{gathered}                                          \tag{1}$$

Pass 28 supplies compactness of the actual robust ready set and attainment
of the continuous upkeep objective. Pass 29 supplies all the following
facts over the full allowed policy class:

- The displayed state x* is robustly ready, at cost `J=37/200`.
- Every concentrated ready state costs strictly more than `1851/10000>J`.
  This comparison includes initial-full states, positive initial C,
  prewarming, parallel input and preemption.
- Every global minimum has C cold and A, B both physically partial. To see
  the C assertion, its cap-loss rate exceeds the resource available without
  either A's or B's release. Thus each earlier handoff precedes C. If C had
  positive initial preparation, the earlier no-faster first-gap exchange
  could increase an earlier subfull coordinate and decrease C, strictly
  lowering cost. The earlier coordinate is allowed to be initially cold
  because there are no fixed support charges. All full coordinates cost
  more than J. The concentrated comparison then forces both A and B positive.
- For any ready state with upkeep at most `1851/10000`, both A/B handoffs
  occur before ell, hence before any release. Two first-completion
  front-loading steps on constant-capacity intervals give a same-initial-state
  full-rate serial A/B prefix, then full input to C. This is the localized
  pass-9 exchange, not a general pending-drain induction.

At a minimum, the pass-28 partial-order theorem requires A to hand off
before B. Front-loading that first completion preserves this order:
the other subfull coordinates receive no input before the new first
handoff and cannot become full during that interval. The second handoff
is B, since the rate barriers force C last. Consequently each global
minimum has an A,B,C serial witness with the same initial state.

## 2. A scalar lower bound for every global minimum

Write

$$P=\frac{94}{121},\qquad Q=\frac{13}{20},\qquad
k=\frac{2700}{1331},\qquad K=\frac{243}{40}.$$

Let `X=exp(t_A)` and `Y=exp(t_B)` in the serial witness of a global
minimum. The first two handoffs occur before ell and before either
reservation release. Their exact balances give

$$2x_A=1-PX^2,\qquad x_B=X-QY,$$

so

$$L(x)=1-PX^2+X-QY.                                   \tag{2}$$

C starts cold. Its terminal preparation at D, allowing an unreflected
virtual extension after an earlier actual full hit, meets its cap only if

$$Y^3+kX^3\leq K.                                     \tag{3}$$

This is pass 29's exact C balance. Both A/B releases are before D. After
both have released, the available rate strictly exceeds C's cap-loss rate,
so an earlier C hit cannot be lost under the virtual full-rate extension.
Thus (3) is necessary even if C's actual handoff precedes D.

Define on the interval `X>=1`, `K-kX^3>0`,

$$Y_0(X)=(K-kX^3)^{1/3},\qquad
F(X)=1-PX^2+X-QY_0(X).                                \tag{4}$$

Every witness above has `X>=1`, positive Y and `Y<=Y_0(X)`. Since Q is
positive, (2)--(3) imply

$$L(x)\geq F(X).                                      \tag{5}$$

The interval in (4) deliberately relaxes the remaining physical initial
constraints and the serial order. A lower bound on this larger interval
remains valid; no discarded constraint is needed to attain the proposed
minimum.

## 3. Exact global convexity and equality

For brevity write `Y_0=Y_0(X)`. Differentiating (4) gives

$$\begin{aligned}
Y_0'&=-\frac{kX^2}{Y_0^2},\\
F'&=1-2PX+\frac{QkX^2}{Y_0^2},\\
F''&=-2P+\frac{2QkX}{Y_0^2}
                  +\frac{2Qk^2X^4}{Y_0^5}.            \tag{6}
\end{aligned}$$

The function Y_0 decreases on the whole interval. At its left endpoint,

$$Y_0(1)^3=\frac{215433}{53240},\qquad
\left(\frac{51}{32}\right)^3-Y_0(1)^3
=\frac{378837}{218071040}>0.$$

Therefore `X>=1` and `0<Y_0(X)<51/32` in (6) yield the uniform exact bound

$$\begin{aligned}
F''(X)
&>-2P+\frac{2Qk}{(51/32)^2}
                 +\frac{2Qk^2}{(51/32)^5}\\
&=\frac{11951206724}{2515363286777}>0.                  \tag{7}
\end{aligned}$$

This is strict convexity on the entire relaxed interval, not a local
curvature check or a numerical scan. At

$$X_* = \frac{11}{10},\qquad Y_0(X_*)=\frac32,$$

one has exactly

$$1-2PX_*=-\frac{39}{55},\qquad
\frac{QkX_*^2}{Y_0(X_*)^2}=\frac{39}{55}.$$

Thus `F'(X_*)=0`, and (7) proves that X* is the unique global minimizer
of F on its interval. Its value is

$$F(X_*)=1-\frac{94}{100}+\frac{11}{10}-\frac{39}{40}
        =\frac{37}{200}.                              \tag{8}$$

For an arbitrary global minimum x, (5)--(8) imply `L(x)>=37/200`.
The explicit robust policy from pass 29 attains that value, proving the
claimed exact optimum. Equality in (5) forces `Y=Y_0(X)`, since Q is
strictly positive. Equality in (8) forces `X=11/10`, so `Y=3/2`.
Substituting these unique exponentials into the initial balances in
Section 2 gives

$$x_A=\frac3{100},\qquad x_B=\frac18,\qquad x_C=0.$$

This proves uniqueness of the global initial-state optimizer over the
entire actual robust ready set. In particular, it does not merely optimize
the cold face or select the best member of a serial family while ignoring
other allowed policies.

## 4. Interpretation and limits

The counterexample now has a global lower bound and a matching robust
policy at the exact same upkeep. Its unique minimum has two partial
coordinates despite all three drains having the same positive duration.
Together with pass 26, this makes three the smallest module count at
which common-drain concentration fails in the stated model. Pass 29's
strict concentrated-state gap remains independently useful for tolerance
and perturbation questions.

The earlier unsuccessful calibration remains a failed counterexample;
the present global certificate does not rehabilitate it. No generic
common-drain optimizer, uniqueness of all optimal schedules, positive-deficit
value formula, empirical implementation or publication novelty follows
from this calculation. Its global quantifiers rely on the complete
fixture-specific reductions and the exact rational inequality (7).
