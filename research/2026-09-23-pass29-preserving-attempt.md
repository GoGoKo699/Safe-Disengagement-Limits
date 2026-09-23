# Pass 29: a slower cold module cannot support two partial minima

23 September 2026. This note records a preserving subclass, an exact
failure of an initial counterexample attempt, and rational separation
certificates for the subsequently calibrated common-drain counterexample.
The all-policy counterexample proof is in the companion
[cold-module test](2026-09-23-pass29-cold-test.md). All claims here concern
the ordinary zero-tolerance objective with no fixed support charges.

Use the model and actual robust readiness of
[pass 28](2026-09-23-pass28-partial-order.md), with three modules, common
positive drain `ell`, physical initial caps, positive released rates and
linked upkeep `L(x)=sum_i gamma_i*x_i`. Put `D=H-ell`. Recorded maximal-loss
witnesses are normalized to first-hit handoffs; feasible modified witnesses
are robust by the replay argument in that note.

## 1. A useful extension of the first-gap improvement

At a minimum, suppose an earlier module i has `x_i<M_i`, a later module j
has `0<x_j<M_j`, and `gamma_i<=gamma_j`. The earlier initial state may be
zero. This configuration is impossible.

Indeed, the first-gap construction in pass 28, Section 3, needs only room
to **increase** the earlier initial state and room to **decrease** the later
one. Its discounted-gap crossing advances i's handoff from tau to tau'.
Increase its initial state by eta and transfer its old input on
`[tau',tau]` to j, lowering j's initial state by the corresponding discounted
integral. The resource use is unchanged except for i's earlier helpful
release; all other paths are unchanged. The exact cost change is

$$
-\gamma_i M_i(e^{\gamma_i\tau}-e^{\gamma_i\tau'})
+\int_{\tau'}^\tau
 (\gamma_i e^{\gamma_i r}-\gamma_j e^{\gamma_j r})v_i(r)\,dr<0.
$$

There is no support charge for turning a cold coordinate positive. The
argument therefore applies to that endpoint as well as to two interior
coordinates. It also excludes simultaneous handoffs with these coefficient
inequalities. This extension would require modification for positive fixed
support charges and is not asserted for them.

There is a corresponding input restriction. If A is interior and a cold
module C has `gamma_C<gamma_A`, no positive C input is possible while A is
unfinished at a minimum. Choose a small nonzero portion h on a compact
interval before both first hits, move that input from C to A, lower initial
A by `integral exp(gamma_A*r)*h(r) dr`, and increase initial C by
`integral exp(gamma_C*r)*h(r) dr`. A's path only decreases before the
transfer is complete; C's path only increases, with a strict cap margin on
that compact interval. The initial/support perturbation is allowed, and
the cost decreases strictly. If C had already handed off, the first-gap
argument above already excludes its lower coefficient.

For equal coefficients the input exchange has zero cost. A sufficiently
small exchange would create another minimum having A and C both interior
with equal coefficients, contrary to pass 28. Thus the same prohibition
holds for `gamma_C=gamma_A` at a global minimum. This equality argument uses
the every-minimizer conclusion of pass 28, rather than claiming a strict
exchange where none exists.

## 2. Preserving theorem for a slower cold third module

**Theorem.** A minimum cannot have two interior coordinates A and B and a
cold coordinate C with

$$0<\gamma_C\leq\min(\gamma_A,\gamma_B).$$

This is a statement about global minima over all initial states and
policies. Competitors may turn C positive. It is not an optimum restricted
to the face `x_C=0`.

Write `alpha=gamma_A>gamma_B=beta` after ordering the two partial handoffs
by pass 28, and write `c=gamma_C<=beta`. The preceding restrictions force
the first-hit order A, B, C and prohibit B or C input before A, and C input
before B. Any unused capacity while A or B is unfinished could be given
to that positive initial coordinate and offset by a strict reduction of its
initial state. Thus, at the putative minimum, A receives full capacity
until its handoff t, and B receives full capacity from t until its handoff u.

After u, give C full available capacity until its first hit. This may
advance C's old handoff, which only helps feasibility. Its earliest finish
must be D. Otherwise, decrease initial B slightly, allowing its full-rate
handoff to move slightly later, and still finish C before D. To justify
this continuity step, a subfull coordinate under nondecreasing full-rate
input can first reach its cap in finite time only at a capacity level
strictly exceeding its proportional upkeep at the cap. Both B's and C's
crossings are therefore transversal. The explicit integral formulas below
also give continuity at their finite capacity jumps. This would strictly
lower the initial objective.

Consequently every supposed minimum of this shape has a full-rate serial
witness A, B, C, with C finishing exactly at D. This serial conclusion is
derived only at the supposed minimum and is not claimed for arbitrary
given initial states.

The case `s=0` is infeasible for this shape, since there is no initially
full module and hence no input or release. For `s>0`, let

$$
\begin{gathered}
d_A=\alpha M_A,\quad d_B=\beta M_B,\quad
z=e^{ct},\quad w=e^{cu},\quad E=e^{c\ell},\quad Z=e^{cD},\\
p=\alpha/c>q=\beta/c\geq1,\qquad A=s-d_A>0.
\end{gathered}
$$

We have `1<z<w<Z`. The cold terminal equation is exactly

$$
s(Z-w)+a_A[Z-\max(w,Ez)]_+
       +a_B[Z-Ew]_+=cM_C Z.                         \tag{1}
$$

For each z near its current value, the left side is continuous and
strictly decreasing in w, with slope at most `-s` wherever differentiable.
It therefore determines a unique continuous local w(z), which is
piecewise affine. All changed initial coordinates remain strictly interior
by continuity. A and B have nonnegative full-rate paths with nondecreasing
input and prescribed terminal equality, so they cannot have crossed their
caps earlier. C starts cold and has the same nondecreasing-input property.
Thus these are actual two-sided feasible variations, rather than merely
formal endpoint equations.

### Smooth portions

If `Ez<w`, A releases before B hands off. Equation (1) fixes w independently
of z. The initial upkeep is

$$
W=s-Az^p+(s+a_A E^q)z^q-(s+a_A-d_B)w^q.             \tag{2}
$$

The coefficient `s+a_A-d_B` is positive, because B reaches its cap from
below in finite time. At every stationary point of (2), its second
derivative is `A*p*z^(p-2)*(q-p)<0`; hence none is a local minimum.

If `w<Ez<Z`, A releases after B but before D. Now B finishes while its
input is still s, so `B=s-d_B>0`. On each branch of the B-release cutoff,

$$
w=K-kz,\qquad
k=\frac{a_A E}{b}>0,\qquad
b=s+a_B E\,\mathbf1_{Ew<Z},
$$

where K is constant on the branch. The objective is

$$W=s-Az^p+sz^q-Bw^q.                              \tag{3}$$

Its derivative divided by the positive `z^(p-1)` is

$$
\frac{W'(z)}{z^{p-1}}
=-Ap+sqz^{q-p}+Bqk\,w^{q-1}z^{1-p}.                \tag{4}
$$

This expression strictly decreases: `q-p<0`, `p>1`, `q>=1`, and w
decreases with z. A stationary point can therefore only be a strict
maximum. This is the step using the cold coefficient bound `c<=beta`.

If `Ez>Z`, A releases after D. Equation (1) again fixes w, and (3) reduces
to a constant plus `-Az^p+sz^q`. The same stationary-point argument applies.

### All release boundaries

The objective is continuous at the branch boundaries. Its derivative
jumps downward as z increases:

- At `Ez=w`, the jump from (2) to (3) is
  `q*a_A*E^q*z^(q-1)*(B/b-1)<0`, since `B=s-d_B<s<=b`.
- At `Ez=Z`, the positive derivative contribution
  `B*q*k*w^(q-1)` disappears.
- At `Ew=Z` within the middle region, w decreases through the cutoff,
  so b increases from s to `s+a_B E`; k and the same positive derivative
  contribution decrease.

Coincident boundaries obey the same one-sided formulas, with the b value
on the applicable adjacent middle branch. Outside the middle region w is
constant, so an equality `Ew=Z` does not itself create another varying
branch. A downward derivative jump cannot be a local minimum. Together
with (2)--(4), this excludes every interior point of the feasible variation
and proves the theorem.

At a feasible boundary `Ez=w`, B reaches its cap exactly when A's release
arrives. State continuity means it must already be able to reach that cap
under the preceding rate s, so `s>d_B` and the boundary's `B=s-d_B` is
strictly positive. The derivative formula does not assume an inaccessible
rate on the adjacent side.

No conclusion is drawn here for a cold coefficient larger than beta.
In particular, replacing `q>=1` in (4) by `q<1` would invalidate the
monotonicity argument, not extend the proof.

## 3. A high-rate cold-last local minimum is not automatically global

The following fixture was investigated jointly during pass 29:

$$
\begin{gathered}
(\gamma_A,\gamma_B,\gamma_C)=(2,1,3),\qquad s=4,\\
M_A=95/108,\quad M_B=1,\quad M_C=18133/10368,\\
a_A=5/4,\quad a_B=1,\quad a_C>0,\quad
\ell=\log2,\quad D=\log4,\quad H=\log8.
\end{gathered}
$$

The serial A, B, C construction with `exp(t)=4/3`, `exp(u)=3/2` has

$$x_A=2/243,\qquad x_B=5/6,\qquad x_C=0,\qquad
L=413/486.$$

Its positive local curvature along the cold terminal constraint is useful
evidence that the two-module curvature proof cannot simply be copied when
`gamma_C>gamma_A`. It does not certify a global two-partial minimum.

In fact a concentrated state is cheaper. Put

$$r=(3467/2076)^{1/3},$$

hand A off at `log r`, and prepare initially cold B at full rate 4 until
its handoff at `log(4r/3)`. Both handoffs precede A's drain completion,
and B's drain completes before D. Set

$$x_A=\frac12\left(4-\frac{121}{54}r^2\right),\qquad
x_B=x_C=0.                                         \tag{5}$$

This A initial state is strictly between zero and its cap. For example,
`1<r<6/5` proves both inequalities directly. After B hands off, give C
all available capacity. Its discounted terminal balance is

$$
\begin{aligned}
3M_C\,64
&=4\left[64-\left(\frac{4r}{3}\right)^3\right]
 +\frac54(64-8r^3)
 +\left[64-8\left(\frac{4r}{3}\right)^3\right]\\
&=400-\frac{346}{9}r^3=\frac{18133}{54}.
\end{aligned}
$$

Thus C reaches its physical cap exactly at D. Full-rate nondecreasing
inputs and terminal equality guarantee the first-hit path conditions;
robust replay supplies the all-loss guarantee. C's own released capacity
is immaterial because it is handed off last.

The cost of (5) is strictly below the proposed two-partial cost:

$$
4-\frac{121}{54}(3467/2076)^{2/3}<\frac{413}{486}.
$$

This comparison needs no floating-point evidence. It is equivalent to
`r^2>1531/1089`, and positive quantities may be cubed and squared to give

$$
\left(\frac{3467}{2076}\right)^2
-\left(\frac{1531}{1089}\right)^3
=\frac{6386586797825}{618437517507216}>0.
$$

For orientation only, the costs are approximately 0.845897 and 0.849794.
This is a failed global counterexample preserved as a research finding,
not a concentration theorem for the remaining high-rate cases.

## 4. Exact certificates for the calibrated counterexample

The companion counterexample uses

$$
\begin{gathered}
(\gamma_A,\gamma_B,\gamma_C)=(2,1,3),\quad s=1,\\
M_A=27/242,\quad M_B=7/20,\quad M_C=11679823/10222080,\\
a_A=6075/2662,\quad a_B=1,\quad a_C>0,\qquad
\ell=\log2,\quad D=\log4,\quad H=\log8.
\end{gathered}
$$

Its displayed two-partial state has `x_A=3/100`, `x_B=1/8`, `x_C=0`
and upkeep `J=37/200`. The stronger comparison threshold below is

$$\bar J=1851/10000=J+1/10000.$$

Every physically full coordinate costs more than this threshold. Thus a
concentrated state below it has at most one positive coordinate, and by
upward readiness comparison it suffices to exclude the three one-positive
states whose entire upkeep equals the threshold. The all-cold state is
componentwise dominated by any of these states.

### Audit of the all-policy reduction used by the certificates

The two relevant cold barriers are exact:

$$
3M_C-(1+a_A)=373/2560>0,\qquad 3M_C>2=1+a_B.
$$

From any subfull C, ownership handoff is impossible before **both** A and
B have released their reservations. Until either release, the other
possibly released reservation leaves total capacity strictly below C's
upkeep at its cap. Scalar comparison and uniqueness prevent reaching that
cap. Hence C is necessarily last; if the deadline is met, both A and B
hand off before `D-ell=ell`.

The first-completion front-loading argument of
[pass 9, Section 3](2026-09-22-pass9-smooth-partial.md) applies to the
globally first handoff here. Before it there are no earlier pending drains,
so capacity is the constant s. Postpone other inputs using only this old
capacity, exactly as in that argument. The newly earlier first handoff also
has an earlier drain completion. At the old first-handoff time all other
preparations dominate their old values unless already handed off; every
new release is no later than the corresponding old release. The original
suffix remains feasible. This is a single first-stage replacement, not an
induction through general pending-drain systems.

The companion uses a second constant-window front-loading step: both
lower-rate handoffs occur before ell, while no drain can release before
ell. The capacity before the second old handoff is therefore still the
constant s. Applying the same postponement argument to that second
handoff finishes the serial reduction. Pending drains do not invalidate
this step because none can end inside its comparison interval.

There is also an independent weighted-input argument for the second
stage which is useful even when that external capacity is nonconstant.
After the first prefix, only the other lower-rate module J and C remain.
Let `kappa=gamma_C>gamma_J`, start the stage at r, and let f
be J's full-external-capacity path with first hit tau. External capacity
here means the fixed schedule of the first module's release, excluding
J's own release. Any other path handing J off at v has `v>=tau`,
`p_J<=f` before tau, and `p_J<=M_J` afterward. Integrating its linear
dynamics gives

$$
\int_r^v e^{\kappa t}v_J(t)\,dt
=M_J e^{\kappa v}-p_J(r)e^{\kappa r}
 -(\kappa-\gamma_J)\int_r^v e^{\kappa t}p_J(t)\,dt.
$$

Comparison with the full-rate prefix yields the exact inequality

$$
I_J\geq I_{\rm early}
 +\frac{\gamma_J}{\kappa}M_J
   (e^{\kappa v}-e^{\kappa\tau})\geq I_{\rm early}.
$$

The same initial-state term cancels, so J need not start cold. The total
discounted input potentially available to C is external capacity minus
`I_J`, plus the tail of J's released reservation. Earlier completion both
minimizes the subtracted term and maximizes that release tail. C's initial
state at r is unchanged. Therefore the full-rate second stage, followed
by full-rate C, has no smaller C terminal preparation than an arbitrary
competitor. This bound allows cold prewarming and arbitrary parallel or
preemptive allocations. If the constructed C path first hits earlier,
hand it off then; this only improves the deadline guarantee.

Either second-stage argument completes the reduction to the two serial
orders A, B, C and B, A, C without assuming general seriality in a
delayed-release model. The weighted alternative uses C's strictly larger
coefficient. The companion's two constant-window replacements instead
use the scalar barriers and `D=2*ell` to keep both comparison intervals
before any release; they do not independently require the coefficient
ordering in the weighted inequality.

### Six rational positive gaps

Write

$$
\begin{gathered}
A=94/121,\quad v=13/20,\quad k=2700/1331,\quad K=243/40,\\
z_-=22691/20000,\quad r_-=10241/10000,\quad b_-=167/100,\quad
q=(1-\bar J)/v=8149/6500.
\end{gathered}
$$

The needed lower bounds on radicals follow from positive rational square
differences:

$$
\begin{aligned}
121/94-z_-^2&=570393/18800000000>0,\\
(1-\bar J)/A-r_-^2&=875193/4700000000>0,\\
(v^{-2}-\bar J)/A-b_-^2&=3104247/158860000>0.
\end{aligned}
$$

Let X and Y denote exponentials of A's and B's handoff times, respectively.
For A first the exact cold deficit is

$$F_A(X,Y)=9(Y^3+kX^3-K);$$

for B first it is

$$F_B(X,Y)=(1+8a_A)X^3+8Y^3-9K.$$

Readiness of the serial state requires this deficit to be at most the
initial C upkeep `3x_C`. Both polynomials strictly increase in X and Y.
All six listed lower arguments preserve the relevant earlier-release
branch: in the exact schedules the second handoff precedes the first
module's drain completion. The table gives positive lower bounds on the
deficit minus available C upkeep.

| Positive initial coordinate | Order | Lower bound expression | Exact positive value |
|---|---|---|---|
| A | A, B, C | `F_A(r_-,r_-/v)` | `2920478879781/21970000000000` |
| A | B, A, C | `F_B(b_-,1/v)` | `187570811109141/2924207000000` |
| B | A, B, C | `F_A(z_-,(z_--Jbar)/v)` | `8534290422217221/233936560000000000` |
| B | B, A, C | `F_B(q*z_-,q)` | `48262213047342791426186382849/2924207000000000000000000000` |
| C | A, B, C | `F_A(z_-,z_-/v)-Jbar` | `4599746533873437861/233936560000000000` |
| C | B, A, C | `F_B(z_-/v,1/v)-Jbar` | `224213187551044101/2924207000000000` |

Here `Jbar` in plain-text table expressions denotes the displayed
`bar J`. For example, in the third row the exact A handoff exponential
is `11/sqrt(94)>z_-`, while B's is `(11/sqrt(94)-bar J)/v`.
The same monotonic substitution explains each row; there are no numerical
root or time-grid tolerances.

Consequently all concentrated states of upkeep at most `bar J` are
infeasible, while the companion's explicit two-partial policy is ready
at upkeep `J`. The certified gap is at least `1/10000` at the displayed
threshold. These arithmetic certificates do not assert that the displayed
two-partial state is the global optimizer or that its cost is the exact
optimum. Compactness ensures a global minimum exists, and the strict
separation forces every such minimum to be nonconcentrated.

The generalized first-gap argument in Section 1 gives a further check:
at a global minimum below this budget, C cannot be positive. Otherwise
either earlier A or earlier B is subfull with smaller coefficient, and
advancing that earlier handoff strictly lowers cost by increasing its
initial state and decreasing C's. Thus every minimizing state below the
displayed bound has C cold, and the nonconcentration means A and B are
both genuinely interior. This is an optimal-state conclusion, distinct
from the all-policy six-case separation above.

## 5. Scope and research decision

The preserving subclass shows that a three-module failure with two
partials and a cold third must have the cold coefficient strictly larger
than the smaller partial coefficient. The first local-minimum fixture
shows why the former exponential curvature argument can fail beyond that
boundary; its concentrated competitor shows why local curvature alone
does not settle the global question. The recalibrated fixture and the
all-policy reduction do supply a strict global separation, with explicit
rational room in its concentrated-state comparison.

The first-gap and input exchanges are ordinary discounted-allocation
arguments inherited from earlier proofs. No novelty claim is made for
this subclass, the exact arithmetic, or the counterexample. Its prior-art
significance requires the separate comparison in the current research
pass. No numerical optimizer, discretized control solver, manuscript
change or outside validation is used here.
