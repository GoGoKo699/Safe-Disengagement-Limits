# Pass 24: the critical-startup separation persists in a calibrated family

23 September 2026. This follow-on answers a limited significance question
from the pass-23 proof audit: is the three-module separation an isolated
algebraic coincidence? The explicit strict inequalities below give a
nonempty open family of physical model parameters with the same separation,
when the deadline is calibrated to a specified critical target. The proof
uses the existing concentration and seriality results and an elementary
derivative bound. It is not a general viability classification or a claim
of novelty for asymptotic reachability.

The [pass-23 review](2026-09-23-pass23-proof-review.md) gives the separate
all-policy impossibility under every fixed positive request-time tolerance
at the unchanged critical source budget. Nothing here weakens that result.

## 1. Explicit sufficient conditions

Use three modules A, B, C with positive sizes, positive proportional loss
coefficients

$$\gamma_A=\alpha,\qquad\gamma_B=\beta,\qquad
\gamma_C=\kappa,$$

nonnegative released capacities, and normal budget `s>0`. Write

$$d_A=\alpha M_A,\quad d_B=\beta M_B,\quad
d_C=\kappa M_C,\quad b=s+a_A,\quad c=b+a_B.$$

For a strictly accessible scalar stage define

$$\tau_i(q;v)=\frac1{\gamma_i}
\log\frac{v-\gamma_iq}{v-d_i},\qquad v>d_i.$$

Assume

$$0<\kappa<\alpha<\beta,\qquad
d_A<s<\min\{d_B,d_C\},\qquad
b>\max\{d_B,d_C\}.                                      \tag{1}$$

Set

$$r=\frac{s-d_A}{\beta},\qquad
r_C=\frac{s-d_A}{\kappa},\qquad
H=\tau_B(r;b)+\tau_C(0;c).                               \tag{2}$$

The inequalities imply `0<r<M_B`, `0<r_C<M_C`, and `c>d_C`, so every
quantity is well-defined and `H>0`. Impose the additional strict gap

$$H<\min\{\tau_A(0;s),\ \tau_B(0;b),\
                         \tau_C(r_C;b)\}.               \tag{3}$$

The condition for a cold C stage need not be listed separately:
`tau_C(0;b)>tau_C(r_C;b)>H` follows from (3).

**Theorem.** Under (1)–(3):

1. Cold post-request exit is finite, and the unique minimum-upkeep
   `H`-ready state is `p^*=(M_A,r,0)`, with `C(H)=s`.
2. No normal policy starting cold can guarantee finite reach or domination
   of this unique minimum.
3. A finite normal warmup followed by constant normal allocations enters
   indefinite robust `H`-readiness. Every finite-time virtual state on the
   guaranteed tail is different from, and does not dominate, `p^*`.

All claims retain the repository's full policy and loss-history conventions:
nonnegative measurable allocations, total normal allocation at most s,
simultaneously admissible maximal loss, upper reflection, no normal
transfers, and the instantaneous independent post-request transfer model.
The guarantee begins after warmup.

## 2. Global optimum and the unreachable target

The order A, B, C is strictly accessible from cold by (1), so cold exit is
finite. At `p^*`, A transfers at time zero, B has initial preparation r,
and C is cold. The same order takes exactly H and has maintenance

$$L(p^*)=d_A+\beta r=s.$$

If a cheaper ready state existed, an attained minimum would have cost at
most s and would be concentrated by the established every-minimizer
theorem. To identify all such possible minima, neither B nor C can be full,
because `d_B>s` and `d_C>s`.

If A is subfull, it must complete first: B and C are inaccessible at initial
capacity s whenever they are subfull. If A is cold, its own stage already
exceeds H by (3). If A is genuinely partial, concentration makes B and C
cold. Whichever of B or C is next has a cold duration exceeding H by (3),
even before including A's positive completion time. Thus A must be full.

If A is full and B is the possible partial coordinate, the cost constraint
gives `q_B<=r`. Cold C cannot go first after A because its own duration
exceeds H. The remaining order has total time

$$\tau_B(q_B;b)+\tau_C(0;c),$$

which is strictly decreasing in q_B. Meeting H therefore forces `q_B=r`.
If A is full and C is the possible partial coordinate, cost at most s gives
`q_C<=r_C`. Cold B first takes more than H. C first takes at least
`tau_C(r_C;b)>H`. The state with only A full and the other coordinates cold
is included in these cases.

Hence `p^*` is the only concentrated ready state of cost at most s. The
attained-minimum and every-minimizer concentration results give both global
equality `C(H)=s` and uniqueness. This is not an unsupported restriction of
arbitrary states to concentrated ones.

For the normal cold-start obstruction on the admissible maximal-loss
history, put

$$Z=p_A+p_B-(M_A+r).$$

Allocations to C cannot increase the budget available to A and B. Reflection
can only reduce the derivative. Thus

$$Z'\leq s-\alpha p_A-\beta p_B
=-\beta Z+(\beta-\alpha)(p_A-M_A)\leq-\beta Z.$$

Since `Z(0)=-(M_A+r)<0`, at every finite time

$$Z(t)\leq-(M_A+r)e^{-\beta t}<0.                        \tag{4}$$

Every state dominating `p^*` would have `Z>=0`. This rules out a robust
finite domination guarantee under every admissible normal policy.

## 3. Explicit robust warmup and tail estimate

Choose any

$$0<z<\min\{M_C,s/\kappa\}.$$

Allocate all normal capacity to C for

$$T_C^{\rm warm}=\frac1\kappa\log\frac{s}{s-\kappa z}.$$

The virtual maximal-loss state is then `(0,0,z)`. From this time onward,
use constant allocations

$$v_A=d_A,\qquad v_B=\beta r=s-d_A,\qquad v_C=0.$$

Their sum is exactly s. At elapsed time t in this second phase, the virtual
trajectory is

$$p_A(t)=M_A(1-e^{-\alpha t}),\qquad
p_B(t)=r(1-e^{-\beta t}),\qquad
p_C(t)=z e^{-\kappa t}.                                 \tag{5}$$

It remains inside the physical box. To certify all sufficiently late request
times, use the serial order A, B, C. Denote its completion map on the entire
box by `G(q)`. The accessible-stage recurrence gives

$$\begin{aligned}
t_A&=\frac1\alpha\log\frac{s-\alpha q_A}{s-d_A},\\
t_{AB}&=\frac1\beta\log
            \frac{b e^{\beta t_A}-\beta q_B}{b-d_B},\\
G(q)&=\frac1\kappa\log
            \frac{c e^{\kappa t_{AB}}-\kappa q_C}{c-d_C}.
\end{aligned}                                           \tag{6}$$

All denominators are strictly positive by (1). These maps are smooth on a
neighborhood of the closed box and strictly decrease with every initial
preparation coordinate. They describe a feasible schedule even if a later
coordinate is initially full: its waiting loss is included in (6).

Let

$$\begin{aligned}
T_{AB}^{0}&=\tau_A(0;s)+\tau_B(0;b),\\
m&=\frac{e^{-\kappa T_{AB}^{0}}}{c}>0,\\
L_A&=\frac{c}{c-d_C}\frac{b}{b-d_B}\frac1{s-d_A},\\
L_B&=\frac{c}{c-d_C}\frac1{b-d_B},\\
K&=L_A M_A+L_Br>0.
\end{aligned}                                           \tag{7}$$

On the entire preparation box, direct differentiation gives

$$|\partial_{q_A}G|\leq L_A,\qquad
|\partial_{q_B}G|\leq L_B,\qquad
-\partial_{q_C}G\geq m.                                 \tag{8}$$

For clarity, a stage with coefficient gamma, capacity v and full loss d has
time derivative at most `v/(v-d)` and preparation derivative in absolute
value at most `1/(v-d)`. Applying the chain rule gives the first two bounds.
For the last coordinate,

$$-\partial_{q_C}G
=\frac1{c e^{\kappa t_{AB}}-\kappa q_C}
\geq\frac1{c e^{\kappa T_{AB}^{0}}}=m,$$

because preparation can only reduce the cold completion time `T_AB^0`.

Apply (8) first to the increase of C from zero, and then to the decreases
of A and B from their target values. Since `G(p^*)=H`, equation (5) implies

$$\begin{aligned}
G(p(t))-H
&\leq L_AM_Ae^{-\alpha t}+L_Br e^{-\beta t}
                         -mz e^{-\kappa t}\\
&\leq K e^{-\alpha t}-mz e^{-\kappa t}.
\end{aligned}                                           \tag{9}$$

The second inequality uses `beta>alpha`. The slow reserve has
`kappa<alpha`; consequently every

$$t\geq T_{\rm tail}
:=\max\left\{0,\frac{\log(2K/(mz))}{\alpha-\kappa}\right\}    \tag{10}$$

satisfies

$$G(p(t))-H\leq-\tfrac12mz e^{-\kappa t}<0.$$

Thus the finite total warmup `T_C^warm+T_tail` is followed by readiness at
every later request time. Its bound is conservative and is not claimed to
minimize warmup duration. Under every smaller admissible loss history,
scalar comparison makes the actual preparation at least the virtual path;
upper reflection preserves that comparison. Upward closure of readiness
and the request-time comparison theorem therefore give the robust claim.
The normal policy never transfers a module or uses a released capacity.

At every finite t, the A and B coordinates in (5) are below their target
values, while C remains positive. The state cannot dominate `p^*` and
converges to it only as `t` tends to infinity. The strict readiness margin
in (9) tends to zero as well.

## 4. Nonempty open parameter family and the exact limitation

The pass-15 fixture lies strictly inside these sufficient conditions:

$$s=1,\quad (M_A,M_B,M_C)=(1/2,1,3),\quad
(\alpha,\beta,\kappa)=(1,2,1/2),\quad
(a_A,a_B,a_C)=(2,33,1).$$

Here `r=1/4`, `r_C=1`, `b=3`, `c=36`, and

$$H=\tfrac12\log(5/2)+2\log(24/23).$$

The exact comparison

$$5\cdot24^4=1658880<1679046=6\cdot23^4$$

gives `H<(1/2)log3=tau_B(0;b)`. Also
`(1/2)log3<log2=tau_A(0;s)`. Finally

$$\tau_C(r_C;b)=2\log(5/3)>\tfrac12\log3>H,$$

where the first strict comparison is equivalent to `625>243`. Thus no
floating-point test is needed to place the fixture in the family.

Every condition in (1) and (3) is a strict inequality of continuous
functions of the independent positive model parameters. Their joint
solution set contains an open neighborhood of the fixture in that parameter
space. In each instance H is assigned by (2), and the preceding global
certificate proves criticality and uniqueness afresh. This is stronger than
asserting that an optimizer should vary continuously across a possibly
singular exact-full endpoint.

The openness is in the model parameters **with the deadline calibrated by
(2)**. In the enlarged parameter space where H is also independently varied,
these instances lie on the critical graph; this note does not claim an open
region of exact equality `C(H)=s`. Nor does parameter persistence imply a
fixed positive request-time tolerance or a uniform positive readiness
margin. At the same source budget, the pass-18 precision lower bound and
the pass-23 dissipation argument still exclude indefinite positive-tolerance
readiness for every member of this family.

The family therefore removes an isolated-parameter objection to the exact
dimension boundary. It does not repair the ideal transfer assumptions,
establish operational applicability, or decide publication novelty. No new
simulation, solver or parameter classification is needed for this finding.
