# Pass 29: boundary faces and a necessary cold-handoff order

23 September 2026. This note proves two reductions for the common-drain
question. An upkeep minimum with two or more physical partials must have a
cold coordinate. For three modules, any failure of concentration therefore
has exactly two partials and one cold module. In every normalized maximal-loss
witness, that cold module must hand off strictly after the earlier partial.
Neither statement excludes cold work interleaved after that first partial,
nor proves a three-module concentration theorem.

The proofs use the complete [partial-order theorem](2026-09-23-pass28-partial-order.md)
and extend the time variation in the
[two-module common-drain proof](2026-09-23-pass26-common-drain.md).
They concern the ordinary zero-deficit problem with physical initial caps.
An initially full nominal coordinate under positive request-time deficit is
generally physically subfull in the effective problem; that coordinate
cannot be replaced by an immediate handoff in these reductions.

## 1. Setting and precise conclusions

Retain the independent immutable-drain interface: finitely many modules,
positive sizes and proportional loss coefficients, nonnegative released
reservations, a common positive drain duration ell, normal spare capacity
s, and deadline H. Variable upkeep is

$$L(x)=\sum_i\gamma_i x_i,\qquad 0\leq x_i\leq M_i.$$

Preparation is upper-reflected at its physical cap. Maximal simultaneous
proportional loss is admissible, and all smaller allowed loss histories
must be covered. Ownership handoff ends preparation loss; release of the
source reservation follows after the independent drain. There are no
unbudgeted drain loads or preparation impulses. Write

$$D=H-\ell,\qquad d_i=\gamma_i M_i.$$

The actual ready set and minimum attainment are those of pass 28. When
`H<ell` no state is ready, and when `H=ell` only the all-full state is
ready. The nontrivial arguments below take D positive and a ready minimum.

**No-cold-face theorem.** At any minimum of L, if every coordinate is
strictly positive, at most one coordinate is physically partial. Equivalently,
any minimum with at least two coordinates in `(0,M_i)` has at least one
zero coordinate. This is a finite-n structural necessary condition, not
an all-dimensional concentration theorem.

**Three-module reduction.** If a three-module minimum has more than one
physical partial, it has exactly two partials A and B and one cold module C.
In every first-hit maximal-loss witness,

$$\gamma_A>\gamma_B,\qquad t_A<t_B,\qquad t_C>t_A,
\qquad v_B=0\text{ almost everywhere before }t_A.$$

The labels A and B are set by their handoff order. The first, second and
fourth assertions are inherited from pass 28. The strict inequality for
C is proved here; it includes exclusion of the tie `t_C=t_A`.

## 2. A two-module tail with a frozen prefix

Consider a putative minimum with two design-interior coordinates A and B,
coefficients `alpha>beta>0`, and first-hit times `r<tau<T<=D`.
Suppose every other module has already handed off by r. Keep every other
initial coordinate, its inputs and its handoff fixed. Also freeze A's and
B's recorded inputs through r. They may have received preparation during
this prefix. Let

$$I_A=\int_0^r e^{\alpha u}v_A(u)\,du,
\qquad I_B=\int_0^r e^{\beta u}v_B(u)\,du.$$

Assume, as the pair theorem supplies at a minimum, that B receives no input
before A's handoff. In that application `I_B=0`; retaining the symbol makes
the global-time accounting explicit. The capacity supplied independently
of A and B is a nondecreasing finite step function

$$b(u)=s+\sum_{j\ne A,B}a_j\mathbf 1_{u\geq t_j+\ell}.$$

The prefix includes fixed release events that may occur after r. No clock
reset is made: the cost weights stay alpha and beta on the original initial
variables, rather than on their decayed values at r.

Any unused capacity between r and tau can be assigned to A and offset by
a sufficiently small discounted reduction of its positive initial state.
The changed A path decreases before the added input and agrees afterward.
No other path or release changes. Thus it would strictly improve upkeep.
The same argument applies to B after tau. Consequently a minimum under
these hypotheses must use

$$v_A(u)=b(u)\quad(r<u<\tau),\qquad
v_B(u)=b(u)+a_A\mathbf 1_{u\geq\tau+\ell}
\quad(\tau<u<T).                                      \tag{1}$$

This is a necessary structure at this putative minimum. It is not serial
optimality for prescribed arbitrary initial states.

The terminal B time must be D. Indeed, its input after tau is nondecreasing.
A path starting subfull cannot first reach its cap in finite time unless
its input immediately before that hit is strictly greater than d_B.
Keeping A and the prefix fixed and extending T slightly then reduces the
initial B required for terminal equality. The nondecreasing input prevents
an earlier cap crossing. Positivity and strict initial-cap room persist
for a sufficiently small extension. If T were below D this would be a
cheaper ready state.

Now vary A's handoff t in a neighborhood of tau, with B's handoff fixed
at D. Continue to use (1) with tau replaced by t. The exact global initial
values are

$$\begin{aligned}
x_A(t)&=M_A e^{\alpha t}-I_A-
             \int_r^t e^{\alpha u}b(u)\,du,\\
x_B(t)&=M_B e^{\beta D}-I_B-
             \int_t^D e^{\beta u}b(u)\,du
             -a_A\int_{\min(D,t+\ell)}^D e^{\beta u}\,du.
\end{aligned}                                          \tag{2}$$

There is a genuine two-sided feasible neighborhood. Both original initials
are positive and strictly below their relevant initial design caps.
Their continuous changes in (2) preserve those inequalities. On `[0,r]`,
both original paths have a strictly positive physical-cap margin because
their first hits are later than r; the fixed prefix inputs and sufficiently
small initial changes preserve that margin and nonnegativity. After r,
A receives the nondecreasing input b. B decays until t and subsequently
receives nondecreasing input `b+a_A*1_{u>=t+ell}`. A subfull unreflected
path with such an input and terminal value exactly at its cap cannot have
crossed the cap earlier: any finite crossing from below requires input
strictly above its full-loss rate, after which that nondecreasing input
would keep the unreflected path above the cap. Thus all intermediate cap
conditions hold, including at input jumps. Other paths and releases are
unchanged. Robust replay supplies readiness under smaller loss histories.

On a smooth interval with constant value b_0 of b, put
`q=1` if `t+ell<D`, and `q=0` if `t+ell>D`. Up to a constant independent
of t, the variable upkeep from (2) is

$$W(t)=K+(d_A-b_0)e^{\alpha t}
          +(b_0+q a_A e^{\beta\ell})e^{\beta t}.        \tag{3}$$

The old finite first hit of A implies `b(tau-)>d_A`.
This follows because A is subfull at r and b is nondecreasing. It remains
true on each sufficiently near smooth branch, including on both sides of
a jump at tau. At a stationary point of (3),

$$W''(t)=\alpha(b_0-d_A)e^{\alpha t}(\beta-\alpha)<0.$$

So no smooth point in this neighborhood is a local minimum. At a baseline
capacity jump of size Delta b at t_0, the derivative jump is

$$\Delta b\,\bigl(-\alpha e^{\alpha t_0}
                         +\beta e^{\beta t_0}\bigr)<0
\quad\text{if }\Delta b>0.                             \tag{4}$$

At the transition `t_0=D-ell`, the A-release contribution instead gives

$$W'_+(t_0)-W'_-(t_0)=-\beta a_A e^{\beta D}\leq0.      \tag{5}$$

Coincident jumps add. A strictly downward derivative jump cannot give a
local minimum; when its total size is zero, the adjacent expression is
the same smooth function and its stationary point is a strict maximum.
Thus no kink is a minimum either. This contradicts the original minimum.

**Tail exclusion.** Two interior coordinates satisfying the pair-order
conditions cannot be the last two unfinished modules after a frozen prefix
ending strictly before the earlier one's first hit. The argument permits
arbitrary earlier inputs to those two modules and any fixed finite set of
nonnegative reservation releases. It needs their common final handoff
deadline; independently binding unequal deadlines can prevent this
two-sided variation.

## 3. Initially full faces and the all-partial face

Suppose a physical-cap minimum has no zero coordinate and at least two
partials. In a first-hit witness every initially full module hands off at
time zero. Every other module is an interior partial. By pass 28 these
partials hand off at distinct times in strictly decreasing coefficient
order, and a later partial receives no input before any earlier partial
hands off.

Choose the last two partials A and B. Every other module has handed off
strictly before A. Choose r at the latest of those earlier handoffs, or
r=0 when there are none. Since A and B are initially subfull and inputs
are bounded, `r<t_A<t_B`. The frozen-prefix tail exclusion gives a
contradiction. This proves the no-cold-face theorem.

For three modules this separately excludes both alternatives to the proposed
cold shape: two partials with an initially full third module, and three
partials. In the full-third case its handoff is at zero, giving the explicit
baseline `b(t)=s+a_C*1_{t>=ell}`. Equation (4) is the missing derivative
check at that exogenous capacity jump. For the all-partial case, freeze the
first partial's handoff and apply the same lemma to the last pair.

If there are exactly two partials A and B and a cold C, the same tail lemma
also rules out `t_C<t_A`: freeze the entire recorded prefix through
`r=t_C`. In particular, this exclusion does not assume C was prepared
contiguously, require front-loading cold work, or prohibit earlier input
to A. The strict inequality `r<t_A` is what preserves the prefix cap margin.
The remaining tie is handled separately next.

## 4. A cold module cannot tie the earlier partial's handoff

Assume three modules with two interior partials A, B and cold C at a minimum,
and suppose a first-hit witness has

$$t_A=t_C=\tau<t_B,\qquad \alpha=\gamma_A>\gamma_B=\beta.$$

The pair theorem gives zero B input before tau. No module has released a
reservation before tau, so

$$v_A(u)\leq s-v_C(u)\quad\text{almost everywhere before }\tau. \tag{6}$$

After tau only B needs preparation. The no-idling and last-handoff arguments
above give full available input to B and `t_B=D`. C's positive physical
size and bounded input imply `tau>0`.

First consider delaying only A's handoff to `tau+h`, fixing C's handoff
and both recorded inputs before tau. Allocate all available capacity to A
between tau and its new handoff and then to B; adjust both initial states
by their terminal equations. C's release is now a fixed baseline step at
`tau+ell`. The right derivative of the combined upkeep at h=0 is

$$K_+=\alpha e^{\alpha\tau}(d_A-s)
       +\beta s e^{\beta\tau}
       +\beta a_A e^{\beta(\tau+\ell)}
                         \mathbf1_{\tau+\ell<D}.       \tag{7}$$

If `K_+<0`, then necessarily `s>d_A`. For all sufficiently small positive
h, the required initial A decreases; its entire old prefix path therefore
decreases. It starts the new short full-rate segment strictly subfull and
hits its cap exactly at `tau+h`. B's slightly increased initial state stays
below its cap, decays until its new input start, and then follows a
nondecreasing input to terminal fullness at D. Thus this is a feasible
strict cost improvement. The C path and its drain remain unchanged.

It remains to exclude `K_+>=0`. Use the first-gap construction of pass 28:

$$g(u)=e^{\alpha u}(M_A-p_A(u)).$$

For small eta positive, let `tau'<tau` be the first time `g(tau')=eta`.
Then `tau'` tends to tau. Increase initial A by eta, preserve its old input
up to tau', and hand it off there. Give B A's removed old input on
`[tau',tau]`. Also give B the extra reservation a_A made available by A's
advanced drain, on

$$[\min(D,\tau'+\ell),\min(D,\tau+\ell)].$$

For a sufficiently small advance that second interval, if nonempty, starts
after tau; C has already handed off and B is the only unfinished module.
Decrease initial B by the discounted integral of both added inputs. Its
path stays below the old path until all additions are complete and equals
it afterward. Positivity and strict initial-cap room persist. Pointwise
capacity is preserved before tau and increased by exactly the advanced
A release on the second interval. Thus this is a feasible perturbation,
with C and every other recorded event unchanged.

Write `Delta=tau-tau'`, and let

$$w(u)=\alpha e^{\alpha u}-\beta e^{\beta u}>0.$$

The exact cost change is

$$\begin{aligned}
\Delta L={}&\int_{\tau'}^\tau w(u)v_A(u)\,du
       -\alpha d_A\int_{\tau'}^\tau e^{\alpha u}\,du\\
&-\beta a_A\int_{\min(D,\tau'+\ell)}^{\min(D,\tau+\ell)}
                                      e^{\beta u}\,du.
\end{aligned}                                          \tag{8}$$

Using (6), bounded inputs and continuity of the exponential weights gives

$$\Delta L\leq -K_-\Delta
            -w(\tau)\int_{\tau'}^\tau v_C(u)\,du
            +o(\Delta),                               \tag{9}$$

where

$$K_-=\alpha e^{\alpha\tau}(d_A-s)
       +\beta s e^{\beta\tau}
       +\beta a_A e^{\beta(\tau+\ell)}
                         \mathbf1_{\tau+\ell\leq D}.
                                                               \tag{10}$$

The difference between (7) and (10) is intentional at the release kink:
advancing a drain ending exactly at D creates usable capacity; delaying
it does not. Hence `K_->=K_+>=0`.

C is strictly subfull before its first hit at tau. Its exact maximal-loss
balance on the short final interval gives

$$\begin{aligned}
\int_{\tau'}^\tau v_C(u)\,du
 &=M_C-p_C(\tau')+\gamma_C\int_{\tau'}^\tau p_C(u)\,du\\
 &\geq(d_C+o(1))\Delta.
\end{aligned}                                          \tag{11}$$

Here continuity gives `p_C(u)->M_C` uniformly on the shrinking interval,
and `d_C=gamma_C*M_C>0`. Equations (9)--(11) therefore yield

$$\Delta L\leq-w(\tau)d_C\Delta+o(\Delta)<0$$

for a sufficiently small advance. This contradicts minimality in the
remaining case. The tie is impossible, completing the three-module
reduction.

## 5. What remains open

Any three-module common-drain failure must have two partial coordinates,
one cold coordinate, and a cold handoff strictly after the first partial.
The cold module can still receive preparation before that first handoff;
the ordering of its handoff does not make its preparation serial. Its
later handoff and release remain endogenous, so freezing them need not
leave the two-sided variation used in Section 2 feasible.

This note does not compare every possible interleaving in that remaining
case, establish a global counterexample, or provide an exact upkeep oracle.
The no-cold theorem concerns physical initial caps at zero deficit. The
tail lemma itself permits interior design caps on its two variable
coordinates, but it does not dispose of physically subfull coordinates
that are on an effective design bound in the positive-deficit problem.

No numerical search is used or needed for these reductions. Their
all-policy scope rests on the existing robust-replay and pair-exchange
arguments plus the explicit feasible variations above. Priority and
operational-model limitations remain those of the current contribution
assessment; these structural reductions do not supply novelty clearance.
