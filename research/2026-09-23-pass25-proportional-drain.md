# Pass 25: unequal residual drains can defeat proportional upkeep concentration

23 September 2026. The instantaneous-transfer concentration theorem identifies
ownership handoff, cessation of preparation loss, and release of source
capacity as one event. The accounted interface in
[pass 6](2026-09-22-pass6-latency.md) separates ownership handoff from
completion of immutable source obligations. This note changes its preparation
law to proportional loss and gives an exact two-module counterexample:
the unique minimum-upkeep ready state has two genuinely partial coordinates.

The lower bound covers arbitrary parallel, preemptive, adaptive and idle
exit policies. It does not infer optimality from a failed serial theorem.
The witness is maintainable with positive optional capacity, so it is not
an inaccessible optimum above the normal operating budget. A separate exact
reduction shows that some common-drain instances retain concentration.

These are interface sensitivity results in an ideal model. The note does
not establish publication novelty, validate a physical proportional-loss
mechanism, solve a general drain scheduler, or claim that an arbitrarily
small latency perturbation defeats concentration.

## 1. Proportional preparation with accounted immutable drains

Each module has size `M_i>0`, proportional coefficient `gamma_i>0`, source
reservation `a_i>0`, and residual-drain duration `ell_i>0`. Before ownership
handoff, preparation is upper-reflected at `M_i` and obeys

$$p_i'=v_i-\rho_i,\qquad
0\leq\rho_i(t)\leq\gamma_i p_i(t),\qquad v_i(t)\geq0.$$

All coordinatewise allowed losses may occur simultaneously; in particular,
the feedback history `rho_i=gamma_i p_i` on every unfinished module is
admissible. Controls are bounded, measurable and causal, with no impulses.

Ownership handoff may occur once the coordinate is full. A full coordinate
may wait before handoff, but then remains subject to its preparation loss
and source allocation until handoff actually occurs. At handoff:

- The independently provisioned receiver has sufficient committed state and
  independently supported ownership authority for subsequent essential work.
- Preparation loss stops; there is no further preparation allocation for that
  module.
- Its immutable old source obligations begin a drain lasting exactly
  `ell_i`, retaining the existing source reservation `a_i` throughout.

Only completion of that drain releases `a_i` for preparing other modules.
Drains may overlap using their already reserved resources. If D(t) is the
set of completed drains, then the post-request preparation budget is

$$\sum_{i\text{ not handed off}}v_i(t)
\leq s+\sum_{i\in D(t)}a_i.$$

The primary is removable only when every drain has ended. The drain may also
be interpreted as an attainable worst-case duration bound, provided the
adversary can realize all stated durations together.

Before a request there are no handoffs or drains, and normal preparation
and optional work obey `sum v_i+u<=s`. No release is available for normal
warmup. The receiver, fence and drain reservations are the accounted
interface assumptions from pass 6. The drain must genuinely be immutable:
it cannot conceal unresolved writes or source-exclusive obligations that
would still change the receiver's required state. This model does not repair
the separate pre-fence propagation and consistency limitations.

For a deadline H, define the actual robust ready set

$$\mathcal R_H^{\rm drain}
=\{p:\text{one causal exit policy finishes every drain by }H
\text{ for every admissible future loss history}\}.$$

If `F_drain` is used as notation for an infimum of robust completion times,
membership here means an actual policy meeting H, not an assumed attainment
of that infimum. The proof below establishes a minimum over this actual-ready
set directly and supplies its attaining policy; it requires no general
attainment theorem for drain scheduling. Write

$$L(p)=\sum_i\gamma_i p_i$$

for normal maximum-loss upkeep.

## 2. Exact two-module instance

Take

$$s=4,\qquad (\gamma_A,\gamma_B)=(2,1),\qquad
(M_A,M_B)=(1/2,3),$$

any positive released rates `a_A,a_B`, and

$$H=\log10,\qquad
\ell_A=\log(100/11),\qquad
\ell_B=\log(10/3).                                      \tag{1}$$

Every feasible policy must hand off A and B by their respective deadlines

$$h_A=H-\ell_A=\log(11/10),\qquad
h_B=H-\ell_B=\log3.                                    \tag{2}$$

These satisfy

$$0<h_A<h_B<\ell_B<\ell_A.$$

In particular `h_B<ell_B` is exactly the comparison `9<10`. Even a drain
started at request time zero cannot finish before either required handoff.
Thus the preparation budget remains exactly four throughout every feasible
policy's preparation phase, regardless of how large the positive releases
are. Initially full modules and delayed handoffs are included in this
statement.

**Theorem.** The unique minimum-upkeep state in `R_H^drain` is

$$p^*=(37/200,\ 7/5),\qquad
\min_{p\in\mathcal R_H^{\rm drain}}L(p)
=177/100.                                               \tag{3}$$

Both coordinates are strictly between zero and their physical full caps.
Thus the conclusion that every upkeep minimum has at most one partial
coordinate fails under this residual-drain interface, even though all
preparation losses are proportional and the minimum lies strictly below s.

## 3. Lower bound over every admissible exit policy

Fix any ready initial state x and one of its guaranteed exit policies.
Follow the admissible simultaneous maximal-loss history, and denote the
actual ownership-handoff times by `t_A,t_B`. They satisfy
`0<=t_A<=h_A` and `0<=t_B<=h_B`. This includes an initially full coordinate
handed off at zero, a full coordinate held until later, and simultaneous
handoffs.

Before its handoff, upper reflection can be written almost everywhere as

$$p_i'=v_i-\gamma_i p_i-w_i,\qquad w_i\geq0,$$

where w_i is allocation discarded at the upper cap. Integrating to handoff
gives

$$x_i=M_i e^{\gamma_i t_i}
-\int_0^{t_i}e^{\gamma_i t}v_i(t)\,dt
+\int_0^{t_i}e^{\gamma_i t}w_i(t)\,dt.                  \tag{4}$$

The same identity holds when `t_i=0`, with zero integrals. Dropping the last
nonnegative term yields a lower bound without assuming that the trajectory
first touches the cap exactly at handoff.

### B hands off no later than A

If `t_B<=t_A`, then `t_B<=h_A`. Since B can receive no more than rate four,
(4) gives

$$x_B\geq3e^{t_B}-4(e^{t_B}-1)
=4-e^{t_B}\geq4-e^{h_A}=29/10.$$

Consequently `L(x)=2x_A+x_B>=29/10>177/100`. This case includes simultaneous
handoffs and an initially full B handed off at time zero.

### A hands off first

Suppose `t_A<t_B`. Multiply (4) by each coefficient and add. The reflected
terms remain nonnegative, so

$$\begin{aligned}
L(x)\geq e^{2t_A}+3e^{t_B}
&-\int_0^{t_A}\left(2e^{2t}v_A(t)+e^tv_B(t)\right)dt\\
&-\int_{t_A}^{t_B}e^tv_B(t)\,dt.                         \tag{5}
\end{aligned}$$

For every `t>=0`, `2e^{2t}>e^t`. The capacity bound therefore gives

$$2e^{2t}v_A+e^tv_B\leq8e^{2t}
\quad\text{before A's handoff},$$

and `e^t v_B<=4e^t` after it. There are still no released reservations.
Integrating these pointwise bounds in (5) yields

$$L(x)\geq W(t_A,t_B)
:=4-3e^{2t_A}+4e^{t_A}-e^{t_B}.                         \tag{6}$$

For nonnegative times,

$$\partial_{t_A}W=2e^{t_A}(2-3e^{t_A})<0,\qquad
\partial_{t_B}W=-e^{t_B}<0.$$

Using each handoff deadline separately gives

$$\begin{aligned}
L(x)&\geq W(h_A,h_B)\\
&=4-3\frac{121}{100}+4\frac{11}{10}-3
=\frac{177}{100}.                                      \tag{7}
\end{aligned}$$

The two handoff cases exhaust every policy on the chosen maximal-loss
history. Therefore (7) is necessary for robust readiness, with no restriction
to serial, nonpreemptive or nonadaptive policies.

## 4. Attainment and uniqueness

Initialize at the state (3). Allocate four units to A and zero to B until
`h_A`, then hand off A. Allocate four units to B until `h_B`, then hand off
B. On maximal loss the global-time identities are

$$\begin{aligned}
p_A(h_A)&=2+(37/200-2)e^{-2h_A}=1/2,\\
p_B(h_B)&=(7/5)e^{-h_B}
+4\left(1-e^{-(h_B-h_A)}\right)=3.
\end{aligned}$$

The first identity uses `e^{2h_A}=121/100`; the second uses
`e^{h_B}=3` and `e^{h_A}=11/10`. A grows to its cap. B first decays from
`7/5`, then grows monotonically to three at `h_B`. Thus both trajectories
remain inside their caps, and their drains finish exactly at H by (1)–(2).

Under every smaller allowed loss history, scalar comparison keeps actual
preparation at least as large until the planned handoff. If a cap is reached
early, the scheduled allocation holds it there: rate four exceeds both full
losses, which are one and three. Upper reflection discards any excess.
The two planned handoffs and both drain deadlines are therefore feasible
on every history. No capacity release is used by this construction.

The objective of this ready state is exactly

$$2\frac{37}{200}+\frac75=\frac{177}{100},$$

proving attainment of the lower bound.

For uniqueness, equality cannot occur in the B-first case. In the A-first
case, strict decrease of W in each variable forces
`t_A=h_A` and `t_B=h_B`. Equality in the pointwise weighted input bounds
then forces `v_A=4,v_B=0` almost everywhere before `h_A`, and `v_B=4`
almost everywhere between `h_A` and `h_B`. The strict inequality of the
two weights rules out fractional allocation to B during the first phase.
Equality also forces zero reflected waste in (4). The integrated equations
then determine the initial coordinates uniquely:

$$x_A=2-\frac32e^{2h_A}=\frac{37}{200},\qquad
x_B=4e^{h_A}-e^{h_B}=\frac75.$$

These equality conclusions concern the maximal-loss realization of an
optimal policy. They are sufficient to establish uniqueness of its initial
state; no uniqueness of policy behavior on every smaller-loss history is
being asserted.

## 5. Normal maintainability and finite cold startup

The partial optimum can be maintained with constant normal allocations

$$v_A=37/100,\qquad v_B=7/5,$$

leaving optional rate `223/100`. Their sum is `177/100<4`, so the example
does not rely on a critical budget or an unsustainable nominal preparation
state. Under smaller losses the actual state stays at least the maintained
target. Larger preparation cannot hurt readiness here: the same prescribed
exit allocations hold any early full coordinates until the planned handoffs.

The existing total-storage argument also gives the matching recurring upper
bound directly for this instance. Every actually ready state has upkeep at
least `177/100`; on the maximal-loss normal history,

$$Q'\leq4-u-L(p)\leq223/100-u,\qquad Q=p_A+p_B.$$

Integrating and using bounded preparation limits the long-run optional rate
of any indefinitely ready normal policy to `223/100`. The constant policy
attains it after initialization. This elementary corollary does not presume
a solved general residual-drain feasibility oracle.

A particularly simple finite cold normal warmup uses allocations `(1,3)`
for time `log2`, with no handoffs or releases. The maximal-loss state is

$$p_A=\tfrac12(1-e^{-2\log2})=3/8>37/200,\qquad
p_B=3(1-e^{-\log2})=3/2>7/5.$$

It is inside the physical box and strictly dominates the optimum. Under
smaller losses, reflected comparison gives at least these amounts. Switch
at this time to the displayed maintenance allocations, which preserve
domination indefinitely. The removal guarantee starts after warmup; it is
not claimed during the unprepared interval.

## 6. The counterexample survives fixed positive request-time tolerance

Use the same precision contract as
[pass 18](2026-09-22-pass18-precision.md): a nominal state p must remain
ready when an unknown one-time deficit of at most `epsilon` is subtracted
from each coordinate at the request. Its worst corner is
`q=(p-epsilon)_+`. This is not a stream of state resets during normal
maintenance. Let `C_epsilon^drain(H)` be the infimum nominal upkeep over
states whose worst corner is actually robustly ready, with infinity when
there are none.

Every ready effective state q obeys two separate scalar necessary bounds.
Equation (4), the individual input upper bound four, and the handoff
deadlines imply

$$q_A\geq2-\tfrac32e^{2h_A}=37/200,\qquad
q_B\geq4-e^{h_B}=1.                                    \tag{8}$$

Thus both coordinates of q must be positive. Every feasible nominal state
therefore satisfies `p_i=q_i+epsilon` on both coordinates and

$$L(p)=L(q)+3\epsilon\geq177/100+3\epsilon.$$

The unique zero-deficit optimum `q=p^*` attains this lower bound whenever
`p=p^*+(epsilon,epsilon)` respects the nominal caps. The binding cap is A:

$$\epsilon\leq1/2-37/200=63/200.$$

Above this threshold every nominal state has
`q_A<=max(1/2-epsilon,0)<37/200`, violating (8). Consequently

$$C_\epsilon^{\rm drain}(H)=
\begin{cases}
177/100+3\epsilon,&0\leq\epsilon\leq63/200,\\
+\infty,&\epsilon>63/200.
\end{cases}                                            \tag{9}$$

In the finite branch the unique minimum nominal state is
`p=p^*+(epsilon,epsilon)`. It has two genuinely partial coordinates for
every `0<=epsilon<63/200`; at the endpoint A is full and B remains partial.
The maximum upkeep on this entire branch is

$$177/100+3(63/200)=543/200<4.$$

Every such nominal optimum is therefore sustainable with positive optional
capacity, including under the specified positive request-time deficit.
Constant maintenance at its nominal target preserves domination, and the
worst-corner exit policy is the one already constructed. Strict maintenance
slack also permits finite cold startup by the radial construction in
[pass 14](2026-09-22-pass14-critical-startup.md); no critical-target
reachability assumption is required. The total-storage bound with the new
nominal minimum gives the corresponding recurring optional optimum
`223/100-3epsilon` for this fixture.

This is a precision robustness result for one explicitly defined drain
fixture. It does not assert tolerance to arbitrary interface errors,
uncertain drain timing beyond the stated bounds, or every positive latency
perturbation. Its significance is that the concentration failure is not
confined to exact zero-slack preparation, unlike the critical-startup
separation audited in pass 23.

## 7. Positive drain time alone does not force failure

There is an exact surviving subclass. Suppose all modules have one common
drain duration `ell>0` and

$$\ell\leq H\leq2\ell,\qquad D=H-\ell.$$

Every handoff must occur by D, and every possible drain completion is at
least ell. Since `D<=ell`, no released capacity can affect preparation
before any required handoff. At equality, a release exactly at D cannot
help complete additional absolutely continuous preparation already required
by D; there are no impulses.

Thus the actual residual-drain ready set is exactly the instantaneous S1
ready set with all released rates set to zero and deadline D. In one
direction, replay any feasible drain preparation policy up to the handoffs;
it has had only capacity s available and completes them by D. In the other,
replay any such zero-release policy and start each drain at its handoff;
every drain then ends by `D+ell=H`. Both directions preserve the loss
histories and causal-policy quantifiers.

The established instantaneous concentration theorem therefore applies to
every minimum in this common-drain subclass. The endpoint `D=0` simply
requires every module initially full. For `H<ell` the drain ready set is
empty.

The counterexample instead has unequal drain durations, and consequently
unequal preparation deadlines. Its all-policy optimum lies where both
handoff deadlines are active. A scalar exchange preserving only the last
completion time need not preserve the earlier module's required handoff
time. This is the concrete constraint that prevents importing the
instantaneous concentration exchange.

## 8. Scope and research consequence

Adding the same constant `Delta>=0` to H and both drain durations in (1)
leaves the two handoff deadlines unchanged and preserves the entire proof.
Thus the counterexample also exists with arbitrarily long resource retention.
This observation is not an arbitrarily-small-delay result with all other
parameters fixed. In particular, Section 7 proves that positive drain time
can coexist with concentration.

Neither the witness nor its lower bound uses a timely capacity release:
the positive reservations stay occupied until preparation is already due.
The failure therefore cannot be attributed to an unproved complicated
release-order algorithm. Different drain lengths impose additional handoff
deadlines, and those constraints can force two partial investments to be
uniquely optimal even under proportional loss.

This finding removes a possible universal extension of the concentration
claim to the accounted immutable-drain interface. It does not contradict
the zero-drain theorem, validate the interface for a particular system, or
establish priority over scheduling with delivery tails and multiple
completion constraints. A targeted primary-source comparison is required
before assigning novelty to this boundary.
