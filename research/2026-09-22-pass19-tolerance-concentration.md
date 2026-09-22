# Pass 19: concentration survives finite request-time tolerance

22 September 2026. This pass resolves both structural questions left open
in pass 18. Every upkeep-minimizing **nominal** state under a fixed positive
request-time deficit has at most one partial coordinate, whenever the
deadline is feasible. Unequal positive proportional coefficients are allowed,
and the conclusion does not require upkeep below the normal source budget.
Every minimum of the one-sided limiting problem also concentrates at every
feasible budget.

The proof replaces the earlier constant-duration treatment of intervening
cold modules by a concavity property of their global-time maps. Those maps
remain concave when intervening modules have fixed positive preparation,
including an upper-bound amount. This is an internally derived and
independently checked mathematical result in the existing ideal model;
publication novelty and physical interpretation remain separate questions.
The pass-18 note is retained as the research record of the earlier open scope.

## 1. The strict-order oracle and a capped allocation problem

Use the positive proportional model with a positive finite number of modules,

$$M_i>0,\quad \gamma_i>0,\quad a_i\geq0,\quad s\geq0,
\qquad d_i=\gamma_iM_i,\quad b(S)=s+\sum_{i\in S}a_i.$$

Let `P` be the family of permutations whose every stage satisfies
`b(prefix)>d_i`. It is empty exactly when cold post-request exit is blocked.
For an order in this family, the global completion time of a selected module
with fixed initial preparation q is obtained from its start time t by

$$\phi_i(t;q)=\frac1{\gamma_i}
 \log\frac{b_i e^{\gamma_i t}-\gamma_i q}{b_i-d_i},
 \qquad 0\leq q\leq M_i,\quad t\geq0.                  \tag{1}$$

Here `b_i` denotes its stage capacity in the fixed order. Composing these
maps from time zero defines `G_pi(q)`. Pass 18 proves that

$$E(q)=\min_{\pi\in\mathcal P}G_\pi(q)                  \tag{2}$$

is exactly the one-sided limiting oracle `F_-(q)`. It agrees with the
original oracle `F(q)` whenever all q_i are subfull. A full q_i is not
silently transferred for free in (2): its own stage must still pass the
strict rate test. If cold exit is finite, E is a finite continuous function
on the closed preparation box.

Consider caps and nonnegative fixed support charges

$$0\leq U_i\leq M_i,\qquad h_i\geq0,$$

and the optimization

$$\min\left\{J(q):E(q)\leq H,\ 0\leq q_i\leq U_i\right\},
\qquad
J(q)=\sum_i\gamma_iq_i+\sum_{i:q_i>0}h_i.               \tag{3}$$

The charges simply provide a concise statement covering the nominal-state
conversion in Section 4; no new physical mechanism is being proposed. The
linear upkeep prices remain the proportional coefficients, not arbitrary
weights. For finite H, feasibility implies `P` is nonempty. The feasible
set is then compact, and J is lower semicontinuous because its jumps at
zero have nonnegative size. A minimum exists whenever the set is nonempty.

**Theorem 1 (capped strict-order concentration).** Every minimizer of (3)
has at most one coordinate satisfying `0<q_i<U_i`.

The following proof does not rely on convexity of the feasible set, a fixed
optimal permutation throughout a neighborhood, or an exchange across a
support-change discontinuity.

## 2. Concavity of the elapsed-time map

For one stage in (1), put `D=b-gamma*M>0`. Differentiation with q fixed gives

$$\phi'(t)=\frac{b e^{\gamma t}}
                         {b e^{\gamma t}-\gamma q}\geq1,
\qquad
\phi''(t)=-\gamma\phi'(t)(\phi'(t)-1)\leq0.           \tag{4}$$

The denominator is positive for every `t>=0`, since
`b-gamma*q>=b-gamma*M>0`. Also `phi(0)>=0`, and `phi(t)>=t`:
after subtracting `D*exp(gamma*t)` from the logarithm numerator, the
remainder is `d*exp(gamma*t)-gamma*q>=0`.

Let G be the composition of any consecutive block of such fixed-preparation
stages. The empty block means `G(t)=t`. Increasing concave maps compose to
an increasing concave map, so in every case

$$G'(t)>0,\qquad G''(t)\leq0,\qquad G(0)\geq0.
\quad\text{Consequently}\quad G(t)\geq tG'(t).          \tag{5}$$

The last inequality follows by evaluating the tangent inequality for a
concave differentiable G at zero:
`G(0)<=G(t)-t*G'(t)`. Each composition is analytic on `t>=0` (with a
smooth extension to a neighborhood of every finite nonnegative time), so
the second derivatives used below exist. Cold coordinates produce affine
maps; prepared coordinates add concavity but do not invalidate (5).

## 3. A two-coordinate exchange has no interior local minimum

Suppose a minimum in (3) has two coordinates j,k strictly between their
caps. Choose a strict order attaining E(q), with j occurring before k.
All other initial coordinates will remain fixed, including every intervening
coordinate. Let `t_0` be the fixed start time of j, let t be its variable
completion time, and let `t_k` remain its original completion time for k.
Write

$$\alpha=\gamma_j,\quad \beta=\gamma_k,\quad
D_j=b_j-d_j>0,\quad D_k=b_k-d_k>0.$$

Let G map the completion of j to the start of k through all intervening
stages. Solving the two variable stage equations for their initial
preparations gives

$$q_j(t)=\frac{b_j e^{\alpha t_0}-D_j e^{\alpha t}}\alpha,
\qquad
q_k(t)=\frac{b_k e^{\beta G(t)}-D_k e^{\beta t_k}}\beta.
                                                               \tag{6}$$

At the original t these are the original preparations. Since both lie
strictly inside positive caps, a two-sided open interval of t preserves
`0<q_j(t)<U_j` and `0<q_k(t)<U_k`. In particular their support charges stay
constant. The original j and k stages have strictly positive duration:
their preparations are below their physical thresholds. Therefore a small
enough interval retains nonnegative durations. Every intervening map remains
valid on its nonnegative input, and after stage k the completed set and
global time agree with the original schedule. The entire suffix is unchanged.
Each perturbed vector is feasible for the same deadline using this one order.

Up to terms independent of t, its objective is

$$c(t)=-D_j e^{\alpha t}+b_k e^{\beta G(t)}.             \tag{7}$$

A local minimum in the open interval would satisfy `c'(t)=0`. We show
instead that every stationary point has `c''(t)<0`. At a stationary point,

$$\alpha D_j e^{\alpha t}
 =\beta b_k G'(t)e^{\beta G(t)}.                         \tag{8}$$

If `beta*G'(t)>=alpha`, inequality (5), with `t>=0`, gives
`beta*G(t)>=alpha*t`. The right side of (8) would then be at least
`alpha*b_k*exp(alpha*t)`, strictly greater than its left side because
nonnegative releases and `d_j>0` imply

$$b_k\geq b_j>D_j.$$

This contradiction proves `beta*G'(t)<alpha` at every stationary point.
Differentiating again and using (8) yields

$$c''(t)=\alpha D_j e^{\alpha t}
 \left[\beta G'(t)+\frac{G''(t)}{G'(t)}-\alpha\right]<0. \tag{9}$$

Thus the restricted cost has no interior local minimum. This contradicts
the global minimizing property of the proposed vector and proves Theorem 1.
The construction permits arbitrary fixed preparations between j and k; they
need not be cold or at an endpoint. The role of endpoint constraints is only
to ensure a two-sided variation for the chosen pair.

## 4. Application to limiting and positive-tolerance nominal states

Taking `U_i=M_i` and `h_i=0` in Theorem 1 proves:

**Corollary 2 (limiting concentration at all budgets).** Whenever the
finite-deadline problem `C_-(H)` is feasible, every minimizing state has at
most one partial coordinate. The restriction `C_-(H)<=s` from pass 18 is
unnecessary.

For a fixed positive epsilon, the nominal state p must satisfy the original
deadline from `q=(p-epsilon)_+`. An optimizer cannot have
`0<p_i<=min(epsilon,M_i)`: replacing that coordinate by zero leaves q
unchanged and strictly lowers upkeep. In particular, if `M_i<=epsilon`,
every optimizer sets p_i to zero.

On the remaining support the conversion is exact:

$$p_i=\begin{cases}0,&q_i=0,\\q_i+\epsilon,&q_i>0,
\end{cases}
\qquad
U_i=(M_i-\epsilon)_+,\qquad h_i=\gamma_i\epsilon.       \tag{10}$$

Every q in these capped boxes is subfull relative to M_i, so `F(q)=E(q)`.
The nominal upkeep `L(p)` is precisely J(q) from (3). Conversely every
admissible q gives an admissible p by (10), with the same objective and
deadline. A q_i at its positive upper cap corresponds to p_i=M_i; zero
corresponds to p_i=0; an interior positive q_i corresponds to
`epsilon<p_i<M_i`.

**Corollary 3 (fixed-tolerance concentration).** For every epsilon>0 and
finite H with feasible `C_epsilon(H)`, every minimizing nominal state has
at most one partial coordinate. This holds for unequal positive coefficients
and without the restriction `C_epsilon(H)<=s`.

The worst-corner state itself need not be concentrated relative to the
physical thresholds M_i. For example, several nominally full coordinates
become several strictly partial coordinates `M_i-epsilon`. The theorem is
about the nominal design, or equivalently endpoint concentration in the
reduced capped box. It does not misidentify `M_i-epsilon` as transfer-ready.

## 5. Earlier routes considered and why the proof needed strengthening

The initial common-coefficient route was valid but narrower. For a fixed
strict order, `exp(gamma*T)` is affine in q. Its earlier positional benefit
strictly exceeds each later one: the adjacent benefit ratio is
`b_next/(b_i-d_i)>1`. Two interior coordinates can be exchanged while
preserving the positive support and deadline, strictly lowering upkeep.
This is a standard linear-allocation reduction, not a separate novelty claim.

The first unequal-coefficient attempt sought a three-stage counterexample
with partial, upper-capped, and partial initial coordinates. Unlike cold
intervening stages, the capped stage does not add a constant duration.
The resulting objective can have positive curvature at some points, so a
direct assertion of global concavity would be false. That observation did
not produce a local minimum: in the exact exchange above, positive or zero
curvature at a stationary point is impossible. The concave-map inequality
`G(t)>=t*G'(t)` supplies the missing constraint. No numerical search or
approximate stationary point is used as evidence for the theorem.

The theorem was independently reviewed against the following possible gaps:
the maps are defined for all nonnegative global times; fixed intermediate
full coordinates are allowed in the limiting oracle; positive durations and
cap bounds give a genuine open variation interval; support charges do not
change; and the preserved second completion time reproduces the entire
remaining schedule. The argument uses a single attaining order and does not
differentiate the nonsmooth minimum over orders.

For an exact illustration of the new exchange, take three modules with
`s=10`, zero releases, coefficients `(2,1,1)`, sizes `(3,2,2)`, and
`epsilon=1/10`. Fix the middle worst-corner preparation at its cap
`q_2=19/10`, and use the order 1,2,3. Put

$$z=e^{t_1},\quad z_*=\frac{25}{16},\quad
e^H=\frac{533}{256},\qquad
q_1(z)=\frac{10-4z^2}{2},\quad
e^{G(t_1)}=\frac{10z-19/10}{8},\quad
q_3(z)=10e^{G(t_1)}-8e^H.$$

At z=z_* these give `q_1=15/128`, `q_3=1/2`. The nominal state is
`p=q+(1/10,1/10,1/10)`, with its second coordinate full and the others
partial, and its upkeep is exactly `971/320<10`. Along this exact
deadline-preserving family, nominal upkeep satisfies

$$L(p(z))-L(p(z_*))=-4(z-z_*)^2.$$

Both rational perturbations `z=z_*+1/100` and `z=z_*-1/100` keep every
preparation within its bounds and reduce upkeep by `1/2500`. Thus the
stationary exchange point is a strict local maximum even with a prepared
upper-capped module between the two variable coordinates. This is a local
mechanism check, not a global optimality or minimum-cost certificate for
the fixture.

## 6. Consequence and remaining computational scope

Finite request-time preparation tolerance preserves the nominal concentration
structure. Together with pass 18, the conclusion separates shape from cost:
the minimum can retain endpoint concentration while suffering a nonvanishing
cost jump at an exact-full barrier. The fixed-tolerance critical example
already has a concentrated nominal optimum; it is fully consistent with this
theorem.

This does not justify reusing the earlier full-subset frontier recursion
unchanged. Nominally full modules still begin a positive-tolerance request
below their transfer thresholds and must be scheduled. The result reduces
the nominal state patterns to a full subset, at most one partial coordinate,
and zero elsewhere; a computational frontier must still account for the
waiting decay and processing of that nominally full subset. No new operation
count or certified transcendental root procedure is claimed in this note.
