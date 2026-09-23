# Pass 22: the curved exchange has a standard log-concavity derivation

23 September 2026. Repository research only. This bounded attribution pass
examines the one-dimensional mechanism isolated in passes 19–21. It finds
a positive reduction to standard concave composition and log-concavity.
The exchange lemma should therefore not be presented as a new general
optimization principle. Its use in this particular serial preparation model
and the priority of the resulting concentration theorem remain separate
questions.

Only the two sources below were inspected for this pass. No additional
parameter variant, solver, manuscript edit or manuscript build was pursued.

## 1. Sources and inspected scope

**Boyd–Vandenberghe.** S. Boyd and L. Vandenberghe, *Convex Optimization*,
Cambridge University Press, 2004, author-hosted
[full book](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf).
Read Section 3.2.4's scalar composition statement, domain qualifications and
complete proof, equations (3.9)–(3.14), printed pages 83–86; the definition
in Section 3.4.1, page 95; and Section 3.5.1, page 104. The required standard
facts are concave nonincreasing composition with a convex inner function,
and the implication from log-concavity to quasiconcavity. The negative-infinity
extension of the concave outer function must respect its monotonicity.

**Agrawal–Boyd.** A. Agrawal and S. Boyd, *Disciplined quasiconvex
programming*, Optimization Letters **14**, 1643–1657 (2020),
[DOI 10.1007/s11590-020-01561-8](https://doi.org/10.1007/s11590-020-01561-8),
[author-hosted final paper](https://web.stanford.edu/~boyd/papers/pdf/dqcp.pdf).
Read Sections 2.1–2.2, printed pages 1644–1647, including Theorem 1 and
both complete proofs. The theorem propagates quasiconvexity through suitable
monotone compositions; its sign-reversed quasiconcave version is noted.
Section 2.1 gives the superlevel/Jensen characterization relevant to endpoint
minimization. Neither statement supplies strict endpoint behavior merely
from non-strict quasiconcavity.

No claim about these sources' later algorithms, software or applications is
used. The following formulas apply their general facts to the S1 exchange;
they are not asserted to be a separately stated theorem in either source.

## 2. Exact function class and the positive region

The scalar class to be checked is

$$c(t)=-A e^{\alpha t}+B e^{\beta G(t)},\qquad t\ge0,
\qquad 0<A<B,\quad \alpha,\beta>0, \tag{1}$$

where G is twice continuously differentiable, increasing and concave on
nonnegative times, with `G'(t)>0`, `G''(t)<=0`, and `G(0)>=0`.
The S1 composed stage maps satisfy these regularity conditions.

Define

$$v(t)=\log(A/B)+\alpha t-\beta G(t),
\qquad \eta(t)=e^{v(t)}. \tag{2}$$

Then v is convex and `v(0)<0`. The set

$$D=\{t\ge0:v(t)<0\}=\{t\ge0:c(t)>0\}$$

is an interval containing zero. On D the exact factorization is

$$\log c(t)=\log B+\beta G(t)+h(v(t)),
\qquad h(u)=\log(1-e^u),\quad u<0. \tag{3}$$

Direct differentiation gives

$$h'(u)=-\frac{e^u}{1-e^u}<0,
\qquad h''(u)=-\frac{e^u}{(1-e^u)^2}<0.$$

Thus h is concave and decreasing. Its concave extended-value convention
sets `h(u)=-infinity` for `u>=0`, which remains nonincreasing on the real
line. The standard scalar composition rule applies to h and convex v.
Adding the concave term `beta*G` shows that `log c` is concave on D.
The positive portion of the exchange cost is consequently log-concave.

This is a substantive reduction, not a claim that an arbitrary difference
of log-concave functions is log-concave. Formula (3), its sign domain and
the convexity of the specific exponent difference supply the hypotheses.
Nor is c assumed positive on its full domain: its remaining region must
still be checked.

## 3. The nonpositive region is strictly decreasing

Suppose `c(t)<=0`, so `v(t)>=0`. Then `t>0`, since `v(0)<0`. Convexity of
v and its tangent inequality imply

$$v'(t)\ge\frac{v(t)-v(0)}t>0. \tag{4}$$

Using `c=B*exp(beta*G)*(1-eta)`, differentiation gives

$$c'(t)=B e^{\beta G(t)}
\left[\beta G'(t)(1-\eta(t))-\eta(t)v'(t)\right]<0, \tag{5}$$

because `eta>=1`. Thus once c reaches zero it strictly decreases thereafter;
it cannot return to its positive region. Equivalently, convex v with
`v(0)<0` can leave the negative half-line at most once in nonnegative time.

These facts establish quasiconcavity on the whole domain. For a positive
level, c's superlevel set is an interval by (3). Its zero superlevel set is
the convex set `{v<=0}`. For a negative level, the superlevel set includes
the initial positive region and then an initial portion of the strictly
decreasing nonpositive tail, hence is again an interval. If no nonpositive
tail exists, these negative superlevel sets are the whole domain.

## 4. Why this gives the strict exclusion needed by S1

Generic quasiconcavity alone says an interval contains an endpoint with no
larger value; a constant objective shows why this does not exclude interior
minimizers. The every-minimizer statement needs the following strict check.

On D, differentiation of (3) yields

$$\begin{aligned}
(\log c)'(t)&=\frac{\beta G'(t)-\alpha\eta(t)}{1-\eta(t)},\\
(\log c)''(t)&=\frac{\beta G''(t)}{1-\eta(t)}
-\frac{\eta(t)(\alpha-\beta G'(t))^2}{(1-\eta(t))^2}.
\tag{6}
\end{aligned}$$

At a stationary point of c in D, the first equation gives
`beta*G'=alpha*eta`. Since `0<eta<1`, the second becomes

$$ (\log c)''(t)
=\frac{\beta G''(t)}{1-\eta(t)}-\alpha^2\eta(t)<0. \tag{7}$$

At such a point `c''=c*(log c)''<0`. There are no stationary points in the
nonpositive region by (5). Therefore every stationary point is a strict
local maximum, and c has no interior local minimum on any nontrivial
subinterval of nonnegative time.

This independently recovers the exact strict conclusion used in pass 19.
The log-concavity closure is standard; the short derivative calculation
checks the necessary strictness for this expression. It does not establish
a new theorem about minimizing every quasiconcave function, or about every
multivariable allocation objective.

## 5. Mapping back to the preparation exchange

In pass 19 the variable cost, after omitting additive constants, has (1)
with `A=D_j`, `B=b_k`, `alpha=gamma_j`, `beta=gamma_k`; nonnegative releases
and the positive requirement of j give `b_k>=b_j>D_j`. G composes all
intervening fixed-preparation stages. Those stages may be cold, prepared,
or at their caps. The physical stage maps give exactly the monotonicity,
concavity and nonnegative value at zero used above.

In pass 21 the same substitution is `A=r_j*D_j`, `B=r_k*b_k`, where
`r_i=w_i/gamma_i`. Its sufficient price condition is precisely what ensures
`B>A`. No new generalized-concavity argument is needed for that extension.

The remaining model work is to justify that two interior preparation
coordinates give a two-sided feasible interval of this form, keep support
charges constant, preserve the second completion time and suffix, and
choose an attaining strict order without differentiating over orders.
Pass 19 supplies those steps. Standard interval quasiconcavity alone does
not supply them, nor a global quasiconcavity statement in preparation or
completion-time coordinates.

## 6. Attribution decision and remaining question

The scalar no-interior-minimum mechanism is now reduced to standard
composition/log-concavity plus an explicit strictness check. It should be
described as an application of established generalized-concavity tools.
Pass 20's failed direct nested-allocation substitutions do not make this
one-dimensional mechanism novel, and those failures do not certify the
priority of the S1 theorem.

The remaining precise attribution question is whether an existing
perishable-preparation or initial-investment scheduling result already
identifies the same feasible curved exchanges with arbitrary prepared
intermediate stages and links their coefficients so that **every** minimum
concentrates. No inspected source in this bounded pass states that S1
conclusion, but absence from these two sources is not evidence of absence
from the literature. The candidate contribution, if it survives further
assessment, lies in that model-specific structural result and its meaningful
scope, rather than a new general allocation or quasiconcavity principle.

This positive reduction should narrow the contribution assessment before
any further theorem variants are added. No numerical verification is needed
for the elementary derivative identities beyond independent mathematical
review; finite arithmetic checks elsewhere are not evidence of priority.
