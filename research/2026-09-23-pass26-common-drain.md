# Pass 26: two modules with a common drain retain upkeep concentration

23 September 2026. This note resolves the all-policy question opened in
[pass 26](2026-09-23-pass26-common-drain-opening.md). For two modules with
one common positive immutable-drain duration, every minimum-upkeep ready
state has at most one partial coordinate. This remains true when an early
drain releases capacity before the other module has finished preparation.

The proof does not assume that arbitrary fixed initial states admit an
optimal serial schedule. It assumes two interior coordinates at a putative
upkeep minimum and derives enough structure for that particular optimum to
exclude it. The key step is an initial-state/input exchange before the first
handoff. A capped version also yields concentration of nominal minima under
fixed positive request-time preparation tolerance.

This is an internal mathematical result in the ideal interface. It is not
a general drain-scheduling algorithm, a theorem for three or more modules,
an operational validation, or a priority claim. The
[unequal-drain counterexample](2026-09-23-pass25-proportional-drain.md)
remains unchanged.

## 1. Model, actual readiness and theorem

Use the proportional residual-drain interface from pass 25, with two
modules, positive sizes and coefficients, positive released reservations,
normal spare capacity `s>=0`, and one common duration `ell>0`. Loss before
ownership handoff is any simultaneous measurable history satisfying
`0<=rho_i<=gamma_i*p_i`; the maximal feedback history on both coordinates
is allowed. Preparation is upper-reflected at its physical cap `M_i`.
Ownership handoff requires a full coordinate and ends its preparation loss.
The source reservation `a_i` is released only at the end of its subsequent
immutable drain. No normal-operation handoffs or releases are available.

An actual ready state has one causal exit policy under which every drain
finishes by H for every allowed future loss history. Define this set as
`R_H^drain`. Membership asserts an attained guarantee, rather than comparing
H with an unproved attainable infimum of schedule lengths. Let

$$D=H-\ell,\qquad L(x)=\gamma_1x_1+\gamma_2x_2.$$

When `H>=ell`, every ownership handoff must finish by the common deadline D.
We first allow additional design caps `0<=U_i<=M_i` and nonnegative fixed
support charges `h_i>=0`:

$$J(x)=L(x)+\sum_{i:x_i>0}h_i,\qquad
0\leq x_i\leq U_i.                                    \tag{1}$$

The support charges are only a convenient device for the nominal-state
corollary below. The variable upkeep coefficients remain the physical
proportional-loss coefficients.

**Theorem.** The actual ready set is compact. Whenever its intersection
with the design box is nonempty, (1) attains a minimum, and every minimum
has at most one coordinate satisfying `0<x_i<U_i`.

In particular, taking `U_i=M_i` and zero support charges proves ordinary
physical concentration for two common-drain modules at every feasible
deadline and every upkeep budget. With smaller caps, the conclusion refers
to the design box, not to physical fullness at `M_i`.

If `H<ell`, the ready set is empty. If `H=ell`, every module must be full
initially and hand off at time zero. If `s=0`, a feasible maximal-loss
schedule must have an initially full module: before any such handoff and
drain there is no preparation input or released capacity. Thus a state with
two subfull coordinates is infeasible. These cases already imply the
claimed concentration. The nontrivial proof below assumes `s>0`, `D>0`.

## 2. Compactness and robust replay

On maximal loss, upper reflection can be removed by deleting the part of
an allocation wasted at the cap. This preserves the state path, decreases
resource use, and gives ordinary linear dynamics up to each planned handoff.
For prescribed handoff times `t_i in [0,D]`, extend useful inputs by zero
after their own handoff and write

$$z_i(t)=x_i+\int_0^t e^{\gamma_i r}v_i(r)\,dr.$$

The exact path conditions are

$$\begin{gathered}
v_i\geq0,\quad v_i=0\text{ after }t_i,\\
\sum_i v_i(t)\leq s+\sum_i a_i\mathbf1_{t\geq t_i+\ell}
\quad\text{almost everywhere},\\
0\leq z_i(t)\leq M_i e^{\gamma_i t}\quad(0\leq t\leq t_i),
\qquad z_i(t_i)=M_i e^{\gamma_i t_i}.                    \tag{2}
\end{gathered}$$

A reflected robust policy supplies such a maximal-loss realization.
Conversely, any path satisfying (2) can replay these measurable inputs and
planned handoff times under every smaller allowed loss. Reflected scalar
comparison keeps the actual preparation at least the virtual preparation
until the planned handoff, so the coordinate is full at that time. Every
reservation is released at its planned drain completion, making the input
budget valid on every history. Hence (2), allowing the times to vary, is
equivalent to actual robust readiness.

To prove closedness, take ready states `x^(m)` converging to x. Choose
corresponding witnesses (2). A subsequence has convergent handoff times
`t_i^(m)->t_i` in `[0,D]`. All useful inputs are bounded by the same finite
constant `s+a_1+a_2`, so a further subsequence converges weak-star in
`L^infinity([0,D])`. The integrated paths are uniformly bounded and
equicontinuous; extract a uniformly convergent subsequence as well.
Variation of constants identifies its limit with the weak-star limiting
inputs and initial state x.

Nonnegativity and the input-zero condition after each limiting handoff
pass to the limit. The capacity step functions converge almost everywhere
away from their finitely many limiting release times. Testing the budget
inequality against nonnegative integrable functions and using dominated
convergence preserves it almost everywhere. For each `t<t_i`, the cap
inequality holds for all sufficiently large m and hence in the limit.
Uniform convergence and convergence of the handoff times give
`z_i(t_i)=M_i*exp(gamma_i*t_i)` and the remaining endpoint cap condition.
Thus the limiting path satisfies (2), proving closedness.

The initial physical box is compact, so the ready set is compact. Its
intersection with the design box is compact too. The objective (1) is
lower semicontinuous because the support charges are nonnegative. A minimum
therefore exists whenever that intersection is nonempty. No general
time-optimal drain-schedule existence claim is required.

## 3. First-hit handoffs at a putative two-interior minimum

Assume for contradiction that a minimum has both
`0<x_i<U_i`. In particular, both initial coordinates are physically
subfull and strictly positive. All sufficiently small initial perturbations
used below preserve the positive support, so the fixed support charges do
not change.

Choose a maximal-loss witness. Ownership handoff may be advanced to the
first time its coordinate becomes full: omit its subsequent preparation
allocations, start its independent drain earlier, and keep every other
module's original recorded input. The earlier reservation release never
reduces available capacity; independent other states are unchanged. Applying
this to each module yields a witness with first-hit handoffs. It is robust
by the replay argument above.

Call a first-handed module A, its time `tau>0`, its coefficient alpha,
and the other module B, with coefficient beta and handoff time `T>=tau`.
If both hand off together, choose A with the smaller coefficient. Before
their first handoff both paths are strictly below their caps, no drain has
released a reservation, and there is no reflected waste.

### A has the smaller or equal coefficient

Suppose `alpha<=beta`. Define the discounted gap

$$g(t)=e^{\alpha t}(M_A-p_A(t)),\qquad 0\leq t\leq\tau.$$

It is continuous, positive before tau, and zero at tau. For sufficiently
small `eta>0`, let `tau'<tau` be the first time `g(tau')=eta`.
Then `tau'->tau` as `eta->0`. Increase initial A by eta and replay its
old input until tau'. It remains below its cap until tau' and is full there;
hand it off at tau'.

Set

$$J_\beta=\int_{\tau'}^\tau e^{\beta t}v_A(t)\,dt.$$

Decrease initial B by `J_beta`, and during `[tau',tau]` give B the old
input of A in addition to its own old input. All other B inputs and its
planned handoff time T remain unchanged. For small eta, both new initial
states stay strictly inside their design caps because `J_beta->0`.

Until tau', the B path is decreased by `J_beta*exp(-beta*t)`; between
tau' and tau the decrease is

$$e^{-\beta t}\int_t^\tau e^{\beta r}v_A(r)\,dr.$$

Thus B never increases before tau, matches its old state at tau, and
subsequently follows its old path. It stays positive: the old path is at
least `x_B*exp(-beta*t)`, and choose `J_beta<x_B`. There is no new cap
violation. Reassigning A's old input preserves the aggregate budget, and
A's earlier drain release can only help.

The old A terminal balance gives

$$\int_{\tau'}^\tau e^{\alpha t}v_A(t)\,dt
=M_A(e^{\alpha\tau}-e^{\alpha\tau'})+\eta.$$

Consequently the change in variable upkeep is

$$\begin{aligned}
\Delta L&=\alpha\eta-\beta J_\beta\\
&=-\alpha M_A(e^{\alpha\tau}-e^{\alpha\tau'})
+\int_{\tau'}^\tau
 (\alpha e^{\alpha t}-\beta e^{\beta t})v_A(t)\,dt<0.
\end{aligned}                                           \tag{3}$$

The integral is nonpositive because `alpha<=beta` and `t>=0`; the first
term is strictly negative. This contradicts minimality. It also excludes
simultaneous handoffs by the labeling convention. This first-hit advance
would remain valid with unequal drains; it uses no common final deadline.

## 4. Fast-first case: the optimum itself must use full-rate serial preparation

It remains that `alpha>beta` and A hands off strictly before B. We derive
the input structure only under the assumption of a two-interior minimum.

Suppose B receives positive input before tau on a set of positive measure.
Choose a bounded nonnegative nonzero portion h of that input, supported in
an interval lying strictly before tau. Transfer h from B's input to A's,
and simultaneously replace the initial states by

$$x_A-\int e^{\alpha r}h(r)\,dr,\qquad
x_B+\int e^{\beta r}h(r)\,dr.                            \tag{4}$$

After h's support both state paths coincide with their originals. Earlier,
A only decreases, while B only increases. Choose h small enough that A
stays positive and both initials stay inside their design caps. B has a
strict cap margin on the compact interval before the support ends, because
its first hit is later than tau. Thus this perturbation is physically
feasible, preserves both handoff times, and changes upkeep by

$$\int(-\alpha e^{\alpha r}+\beta e^{\beta r})h(r)\,dr<0.$$

Any positive-measure input set before tau contains such a portion bounded
away from tau. Therefore B receives zero input almost everywhere before
tau at a minimum. Any unused capacity before tau likewise gives a strict
improvement: assign a small portion to A and lower its initial state by the
corresponding discounted amount. Its path decreases before that portion
and agrees afterward. It follows that

$$v_A=s,\qquad v_B=0\quad\text{almost everywhere on }(0,\tau).$$

Since A starts below its cap and reaches it in finite time, necessarily
`s>d_A=alpha*M_A`, and

$$\alpha x_A=s-(s-d_A)e^{\alpha\tau}.                    \tag{5}$$

After tau, B is the only module still requiring preparation. Its available
capacity before its handoff is the nondecreasing step function

$$c_\tau(t)=s+a_A\mathbf1_{t\geq\tau+\ell}.$$

Any unused capacity on a positive-measure subset of `(tau,T)` can be
assigned to B and offset by a small reduction in its initial preparation.
Its path then only decreases before that added input and matches afterward,
so the handoff times and capacity history are unchanged. Positivity follows
by making the discounted reduction smaller than `x_B`. Hence at a minimum

$$v_B=c_\tau(t)\quad\text{almost everywhere on }(\tau,T).$$

This is a necessary condition for this putative minimum, not a seriality
theorem for arbitrary given initial states. No fixed-loss latency result
has been imported.

## 5. The last handoff binds, with no hidden cap obstruction

A useful elementary fact for the preceding full-rate B path is the following.
Starting subfull, receiving no input until the first handoff and then a
nondecreasing capacity, a path whose terminal value equals `M_B` cannot
have reached that cap earlier. Reaching the cap in finite time from below
requires capacity strictly greater than `d_B=beta*M_B` at the crossing.
Once that capacity level has been reached it never decreases; a prior
crossing would force the unreflected path strictly above the cap thereafter,
contradicting its terminal equality. Nonnegative initial state and inputs
already preserve the lower bound. This reasoning also applies at the
single capacity jump: a jump in input does not jump the state.

Suppose `T<D`. Preserve A's handoff and extend the full-rate B phase to a
slightly later time `T'>T`, still below D. Choose its initial preparation as

$$x_B(T')=M_B e^{\beta T'}
-\int_\tau^{T'}e^{\beta r}c_\tau(r)\,dr.$$

Immediately after T its derivative with respect to T' is

$$e^{\beta T'}(d_B-c_\tau(T'))<0.$$

Indeed, the old first hit at T required final capacity strictly above d_B;
if T is the release time, the preceding capacity already had to allow
that finite first hit, and the subsequent jump cannot reduce it. Thus a
small extension lowers `x_B` while keeping it positive and inside its cap.
The preceding nondecreasing-capacity observation ensures the new path does
not hit its cap early. This produces a cheaper ready state, a contradiction.
Therefore every putative two-interior minimum in the remaining case has

$$T=D,\qquad 0<\tau<D.$$

The strict inequality `tau<D` also follows because B merely decayed before
tau and still has a strictly subfull state at that time.

## 6. Varying the first handoff excludes the remaining minimum

Vary the first handoff t near tau, allocate full capacity to A before t and
to B afterward, and fix B's handoff at D. Set `a=a_A`, `d_A=alpha*M_A`,
and `d_B=beta*M_B`. Solving the terminal equations gives

$$\alpha x_A(t)=s-(s-d_A)e^{\alpha t}.$$

If `t+ell<=D`, then

$$\beta x_B(t)=(d_B-s-a)e^{\beta D}
+(s+a e^{\beta\ell})e^{\beta t},$$

whereas if `t+ell>=D`,

$$\beta x_B(t)=(d_B-s)e^{\beta D}+s e^{\beta t}.$$

These formulas agree at the release transition. At the original tau both
initial coordinates are strictly interior to their design caps, so their
continuity preserves those strict inequalities on an open neighborhood of
tau. A's full-rate path is valid by (5). B's path is valid throughout that
neighborhood by the nondecreasing-capacity observation in Section 5:
the prescribed initial state is positive and subfull and the unreflected
terminal value is exactly its cap. Thus these are genuine two-sided feasible
variations, including when `tau=D-ell`. There is no omitted intermediate-cap
constraint cutting off one side of the variation.

The variable upkeep is, on the two branches,

$$\begin{aligned}
W_-(t)&=s-(s-d_A)e^{\alpha t}
-(s+a-d_B)e^{\beta D}+(s+a e^{\beta\ell})e^{\beta t},\\
W_+(t)&=s-(s-d_A)e^{\alpha t}
-(s-d_B)e^{\beta D}+s e^{\beta t}.
\end{aligned}                                           \tag{6}$$

Each smooth branch has the form `constant-A*exp(alpha*t)+C*exp(beta*t)`,
with `A=s-d_A>0` and `C>0`. We are in the remaining case `alpha>beta`.
At every stationary point,

$$W''(t)=\alpha A e^{\alpha t}(\beta-\alpha)<0.$$

Thus no smooth interior point is a local minimum. When the release
transition `t_0=D-ell` lies in the interval, the expressions are continuous
and the derivative jump is

$$W_+'(t_0)-W_-'(t_0)=-\beta a e^{\beta D}<0.             \tag{7}$$

A local minimum would require left derivative at most zero and right
derivative at least zero, which (7) rules out. If the transition lies
outside the interval, only the appropriate smooth branch is needed.
Support charges stay constant on every variation.

Every possible two-interior minimum has now been contradicted. Together
with Section 2 this proves the capped theorem, including existence and
the every-minimizer conclusion.

## 7. Fixed positive request-time tolerance

For `epsilon>0`, retain the same one-time request-time deficit contract as
passes 18 and 25: nominal p must meet the removal deadline from every state
between its worst corner `q=(p-epsilon)_+` and p. This is not an additional
continuous loss stream during normal maintenance. Upward comparison makes
actual readiness of that worst corner equivalent to this contract.

At an optimum, no coordinate can satisfy `0<p_i<=min(epsilon,M_i)`:
setting it to zero leaves q unchanged and strictly lowers nominal upkeep.
On every remaining positive coordinate, `p_i=q_i+epsilon`. Therefore the
nominal optimization is exactly (1) with

$$U_i=(M_i-\epsilon)_+,\qquad h_i=\gamma_i\epsilon.$$

Zero q corresponds to nominal zero, q at its positive cap corresponds to
nominal physical fullness, and an interior positive q corresponds to a
nominal amount strictly between epsilon and `M_i`. The theorem proves:

**Corollary.** Whenever fixed-positive-tolerance readiness is feasible for
two modules with a common drain, its minimum nominal upkeep is attained,
and every minimum nominal state has at most one partial coordinate.

The effective worst-corner state need not have a physically full coordinate;
the concentration statement concerns the nominal design, or equivalently
the reduced design caps. No claim is made that fixed tolerance leaves the
upkeep value or feasibility threshold unchanged.

## 8. What has and has not been resolved

For `ell<=H<=2*ell`, the common-drain ready set was already reduced in pass
25 to instantaneous zero-release readiness at deadline `D=H-ell`. The proof
here also covers the previously open regime `H>2*ell`, where an early drain
can release useful capacity. The common handoff deadline leaves a feasible
two-sided variation of the first handoff; the pass-25 unequal-drain witness
instead has an independently active earlier handoff deadline.

The decisive all-policy ingredients are the first-hit advance and the
discounted input/initial-state exchanges. The exponential stationary-point
calculation alone was already present in the opening and would not have
justified the result. Compactness is used to establish actual attainment;
no discretization or numerical search stands in for these arguments.

The proof does not settle fixed-initial-state serial optimality, general
multi-module common-drain concentration, a scheduling complexity question,
or an engineering implementation. It isolates a precise two-module boundary
between common and unequal immutable drains. The ordinary allocation
reasoning and the restricted exponential exchange require careful source
attribution before any residual novelty claim is made.
