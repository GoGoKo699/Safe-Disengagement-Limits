# Pass 29: three common drains can defeat upkeep concentration

23 September 2026. This note gives a three-module counterexample to
common-drain concentration beyond the two-module theorem. It proves a
strict separation over **all** concentrated initial states and all allowed
exit policies. The matching feasible witness uses uninterrupted preparation
in the order A, B, C; preemption is not required for the failure.

The result is an internal mathematical finding in the existing independent
immutable-drain interface. It is not an exact formula for the unrestricted
minimum, an engineering validation, or a publication-priority claim.

The subsequent [pass-30 proof](2026-09-23-pass30-exact-optimum.md) establishes
the exact unique optimum. Its [continuation](2026-09-23-pass30-robust-common-drain.md)
adds the exact positive-tolerance frontier and parameter robustness. The
separation proof below is preserved as the argument that precedes those results.

## 1. Model and exact fixture

Use the proportional-loss, independently released reservation model from
[pass 26](2026-09-23-pass26-common-drain.md). Before handoff, preparation has
upper-reflected dynamics with simultaneous adversarial losses
`0<=rho_i<=gamma_i*p_i`. Ownership handoff requires fullness, stops loss,
and starts an independent drain. Each drain retains its reservation until
completion; normal operation permits no handoffs. All coordinates start in
`[0,M_i]`. Variable upkeep is `L(x)=sum_i gamma_i*x_i`.

Set spare capacity, common drain, handoff deadline and removal deadline to

$$s=1,\qquad \ell=\log 2,\qquad D=\log4=2\ell,
\qquad H=D+\ell=\log8.$$

| Module | Coefficient $\gamma_i$ | Size $M_i$ | Released rate $a_i$ |
|---|---:|---:|---:|
| A | $2$ | $27/242$ | $6075/2662$ |
| B | $1$ | $7/20$ | $1$ |
| C | $3$ | $11679823/10222080$ | $1$ |

Write

$$\begin{gathered}
a=a_A,\quad d_C=3M_C=\frac{11679823}{3407360},\\
P=1-2M_A=\frac{94}{121},\qquad
Q=1-M_B=\frac{13}{20},\\
k=\frac{8a}{9}=\frac{2700}{1331},\qquad
K=\frac{243}{40}.
\end{gathered} \tag{1}$$

Useful identities and strict inequalities are

$$d_C=2+a-\frac{2187}{2560},\qquad
(2+a)64-d_C64=9K,$$

$$d_C-(1+a)=\frac{373}{2560}>0,\qquad
 d_C-2=\frac{4865103}{3407360}>0. \tag{2}$$

The candidate initial state and its upkeep are

$$x^*=\left(\frac3{100},\frac18,0\right),\qquad
L(x^*)=\frac{37}{200}. \tag{3}$$

Both positive coordinates are strictly below their physical caps. We will
show that every concentrated ready state has upkeep strictly above

$$B_*=\frac{1851}{10000}
=\frac{37}{200}+\frac1{10000}. \tag{4}$$

Here concentrated means at most one coordinate strictly between zero and
its physical cap. Initially full coordinates are explicitly included in
this definition and in the exclusion below.

## 2. Matching robust feasible witness

On maximal loss, give the entire available preparation resource to A until
`t=log(11/10)`, then to B until `u=log(3/2)`, then to C until D.
Both first handoffs occur before ell, so neither releases capacity before
B is handed off. The first two terminal balances are

$$2x_A=1-Pe^{2t}=\frac3{50},\qquad
x_B=e^t-Qe^u=\frac18.$$

C starts cold at u and receives rate 1 until `t+ell`, rate `1+a` until
`u+ell`, then rate `2+a` until D. Its terminal balance is

$$\begin{aligned}
3p_C(D)e^{3D}
&=(2+a)e^{3D}-9e^{3u}-8ae^{3t}\\
&=(2+a)64-9K=d_C64,
\end{aligned} \tag{5}$$

because

$$e^{3u}+ke^{3t}=\frac{27}{8}
+\frac{2700}{1331}\frac{1331}{1000}=\frac{243}{40}.$$

A and B reach their caps from below under constant full-rate input. C has
nondecreasing input; its prescribed terminal equality and subfull start
exclude an earlier cap crossing followed by a return to the cap. In
particular, (2) prevents C from reaching its cap before both reservations
are released. These are therefore legitimate first-hit handoffs. A and B
finish their drains before H; C finishes its drain at H.

Under smaller losses, replay the same planned allocations and handoff
times. Scalar reflected comparison guarantees at least the maximal-loss
preparation at each planned handoff, and all planned releases remain
available. Thus (3) is actually robustly ready, not merely feasible on one
favorable history. Its upkeep is below the normal spare capacity.

## 3. Why all policies reduce to two orders for this fixture

This section is a fixture-specific reduction. It does not assert general
serial optimality with positive drains.

Consider any initial state with upkeep at most B_*. Its individual full
costs satisfy

$$2M_A=\frac{27}{121}>B_*,\qquad
M_B=\frac7{20}>B_*,\qquad d_C>B_*.$$

Hence every coordinate is physically subfull. On maximal loss, (2) implies
that C cannot reach its cap before **both** A and B have released their
reservations: without A, input capacity is at most 2; without B it is at
most `1+a`; either rate is strictly below `3M_C`. A subfull proportional
trajectory cannot hit its cap while its available input stays below the
cap's loss rate. This holds for positive initial C as well as cold C.

If a schedule finishes C by D, both releases must occur strictly before
its handoff. Release exactly at C's first hit would not allow a continuous
state to cross the preceding strict rate barrier. Therefore

$$t_A+\ell<t_C\leq D=2\ell,\qquad
  t_B+\ell<t_C\leq D=2\ell,$$

and consequently

$$t_A<\ell,\qquad t_B<\ell. \tag{6}$$

No reservation can be released before ell, regardless of which subfull
module hands off first. All preparation leading to the first two handoffs
therefore occurs with constant capacity 1.

We may now apply the **first-completion front-loading lemma**, not the
instantaneous-release serial theorem as a whole. Its full proof is in
[pass 9, Section 3](2026-09-22-pass9-smooth-partial.md). For clarity, the
part used here is the following. At constant capacity b, if a subfull
module is the first to finish, completing it immediately at full rate
takes time tau and uses `b*tau` work. Its original total allocated work
was at least `b*tau`, by the scalar potential
`W'(p)=1/(b-g(p))`. Thus all other original input before the first handoff
can be postponed to after tau without exceeding the old capacity. Delaying
a fixed amount of input under nondecreasing loss cannot reduce its terminal
preparation. Early handoff and its earlier independent drain release only
increase future resource availability. The original initial state is
unchanged.

Apply this once to the globally first module, which is A or B. Apply it
again to the other member of that pair, using the feasible modified
schedule and its still constant-capacity interval before ell. The argument
postpones C's work while keeping or increasing its preparation at the
comparison times. Both A/B handoffs and therefore both releases are no
later. The resulting same-initial-state schedule prepares A then B, or B
then A, each at full rate, with no C input before the second handoff.
Give C all available input thereafter. This cannot delay its first hit.

Thus every robustly ready state of upkeep at most B_* has a maximal-loss
witness in one of the two orders

$$A\longrightarrow B\longrightarrow C,
\qquad B\longrightarrow A\longrightarrow C. \tag{7}$$

The reduction includes arbitrary original prewarming, parallel allocation,
preemption, idle time, reflected waste, positive initial C, and adaptive
policies: choose the simultaneously maximal-loss realization, delete
reflection waste, and perform the deterministic transformations above.
It is sufficient for a robust lower bound because every robust policy must
succeed on that realization.

A schedule may hand C off earlier than D. Once both reservations have
released, the available rate `2+a` is strictly greater than d_C. Extending
C's unreflected virtual full-rate trajectory to D therefore leaves its
state at least M_C. Conversely, if the serial virtual trajectory is still
below M_C at D, it could not have handed C off earlier. This justifies the
terminal test at D without assuming that every feasible policy binds D.

## 4. Exact exclusion of every concentrated state

With no full coordinates, a concentrated state of upkeep at most B_* lies
below one of these three states, coordinate by coordinate:

$$\left(\frac{B_*}{2},0,0\right),\qquad
(0,B_*,0),\qquad
\left(0,0,\frac{B_*}{3}\right). \tag{8}$$

Actual readiness is upward closed by scalar comparison and no-later
independent releases. It is therefore enough to prove that none of (8) is
ready. This also excludes the all-cold state; no positivity assumption is
being made about a putative optimizer.

Let X and Y denote `exp(t_A)` and `exp(t_B)`. In order A,B,C, the first two
terminal equations and the C terminal deficit are

$$X^2=\frac{1-2x_A}{P},\qquad
Y=\frac{X-x_B}{Q},$$

$$\Delta_{AB}=9(Y^3+kX^3-K)-3x_C. \tag{9}$$

In order B,A,C, they are

$$Y=\frac{1-x_B}{Q},\qquad
X^2=\frac{Y^2-2x_A}{P},$$

$$\Delta_{BA}=(1+8a)X^3+8Y^3-9K-3x_C. \tag{10}$$

In both cases positive Delta means the virtual C preparation at D falls
short of its cap. All six resulting A/B handoffs lie before ell and all
releases before D, as the branch formulas require. For example the largest
handoff exponential is `(20/13)*(11/sqrt(94))<2`.

The companion
[exact certificate note](2026-09-23-pass29-preserving-attempt.md)
records rational lower bounds for all six deficits. Its certificate uses

$$\begin{gathered}
\frac{22691}{20000}<\frac{11}{\sqrt{94}},\\
\frac{10241}{10000}<\sqrt{\frac{1-B_*}{P}},\qquad
\frac{167}{100}<\sqrt{\frac{(20/13)^2-B_*}{P}},
\end{gathered} \tag{11}$$

with each inequality certified by squaring positive rational quantities.
Every expression in (9) and (10) is increasing in the handoff exponentials
used for these lower bounds. The resulting exact positive deficits are:

| Positive coordinate in (8) | Order A,B,C: lower bound on Delta | Order B,A,C: lower bound on Delta |
|---|---:|---:|
| A | $2920478879781/21970000000000$ | $187570811109141/2924207000000$ |
| B | $8534290422217221/233936560000000000$ | $48262213047342791426186382849/2924207000000000000000000000$ |
| C | $4599746533873437861/233936560000000000$ | $224213187551044101/2924207000000000$ |

These are rational inequality certificates, not a grid search or numerical
optimizer. Equations (7)--(11) exclude the full policy class at all three
states in (8), and hence every concentrated state of upkeep at most B_*.

## 5. What the counterexample establishes

The actual ready set is compact by
[pass 28](2026-09-23-pass28-partial-order.md), and the upkeep objective is
continuous. Thus an unrestricted minimum is attained. Equation (3) bounds
its value above by 37/200; Section 4 excludes concentration at every value
up to 1851/10000. Therefore **every unrestricted minimum in this fixture
has at least two partial coordinates**.

The existing partial-order theorem additionally forces C to be cold at
such a minimum. If C were interior, it would have to hand off before every
other interior coordinate because its coefficient is largest. Yet the
rate barriers force A and B to hand off before C. Any earlier cold A or B
can instead be increased slightly while decreasing interior C, by the
first-hit advancement exchange (the earlier coordinate need not already
be positive when support charges are absent). That strictly improves
upkeep since its coefficient is smaller. Full coordinates are already
excluded below the candidate cost. Thus minima here have precisely the
form `A partial, B partial, C cold`.

This last structural conclusion does not identify their exact coordinates.
The displayed witness is not asserted to be the unique or exact global
minimizer. The proved quantitative statement is the gap

$$\inf\{L(x):x\text{ is concentrated and ready}\}
>\frac{1851}{10000}
>\frac{37}{200}
\geq\min\{L(x):x\text{ is ready}\}. \tag{12}$$

The strict first inequality follows because the concentrated subset of the
physical initial box is closed, its intersection with the compact ready
set is compact, and it is nonempty (the all-full state is concentrated).
Its minimum is therefore attained and Section 4 excludes every value at
or below B_*.

Combined with the two-module common-drain preservation theorem, three is
the smallest module count at which common-drain concentration can fail in
this model. All coefficients are positive and unequal; the arbitrary-size
common-coefficient preservation theorem remains intact. All rates, sizes,
and reservations have been retained in the same interface.

The failure is already visible along uninterrupted schedules. Completing
a cold final module depends on the pending releases of both earlier
modules. Holding the final handoff fixed couples both earlier handoff times;
this prevents importing the two-module timing variation unchanged. The
opening's focus on cold prewarming identified an incomplete mechanism:
actual prewarming is not needed for the eventual obstruction.

## 6. Preserved failed calibration and scope of the next task

An earlier exact calibration with coefficients `(2,1,3)`, spare capacity 4,
`a_A=5/4`, `a_B=1`, `M_A=95/108`, `M_B=1`,
`M_C=18133/10368`, and the same ell,D had a two-partial serial stationary
local minimum at `(2/243,5/6,0)`, of upkeep `413/486`. It did **not**
establish a global counterexample: a concentrated A-only schedule with
`exp(t_A)=(3467/2076)^(1/3)` had lower upkeep

$$4-\frac{121}{54}\left(\frac{3467}{2076}\right)^{2/3}
<\frac{413}{486}.$$

This failed calibration is retained because it illustrates why a local
curvature calculation or an optimization restricted to one initial-state
face cannot establish nonconcentration. The final fixture above passes
that missing all-policy concentrated comparison.

The next justified tests are to use the explicit gap for a positive
request-time deficit and to compare the exact boundary with close allocation
and delayed-release results. Neither a new dimension nor a general numerical
scheduler is required. Preserve the distinction between a strict separation,
an exact optimum, ordinary proof ingredients, and publication novelty.
