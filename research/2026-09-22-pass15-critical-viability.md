# Pass 15: critical readiness can be sustained without reaching any optimum

22 September 2026, continuing from
`bb1e34f41338745c88ae486d493a053c658fb3d1`.

The fixed-target startup test from pass 14 is sufficient, but is not necessary,
for entering indefinite readiness from cold. A three-module example below has
`C(H)=s>0` and a unique upkeep-minimizing state which no finite normal warmup
can robustly reach or dominate. Nevertheless a finite warmup enters a robust policy
that meets the deadline at every subsequent request time. Its preparation
approaches the optimum while remaining different from it at every finite
time.

First we prove the proposed convergence lemma: on maximal loss, every
indefinitely ready critical trajectory converges to one minimizing state.
The counterexample shows exactly why convergence does not imply finite
reachability of that state. The separate
[two-module boundary](2026-09-22-pass15-two-module-boundary.md) establishes
that the proposed necessity does hold for at most two modules in its stated
domain. Three modules are therefore enough, and two are insufficient, for
this separation.

These are results in the existing ideal proportional-loss model. They do not
resolve the physical update-envelope question or establish publication
novelty. In particular, no readiness promise is made during the finite warmup.

## 1. Model and the distinction being tested

Use the pass-9/pass-11 model with finitely many independent modules,
`M_i>0`, `gamma_i>0`, `a_i>=0`, and normal spare capacity `s>0`. Preparation is
upper-reflected at `M_i`; allocations are nonnegative, measurable, and satisfy

$$u+\sum_i v_i\leq s$$

during normal operation. No module transfers during warmup or subsequent
normal operation. Source capacity releases occur only following a removal
request, under the established instantaneous independent-transfer interface.
The loss uncertainty contains every simultaneous history
`0<=rho_i(t)<=gamma_i*p_i(t)`, including maximal feedback on every coordinate.

Write

$$L(p)=\sum_i\gamma_i p_i,\qquad
\mathcal R_H=\{p:F(p)\leq H\},\qquad
C(H)=\min_{p\in\mathcal R_H}L(p),$$

where `H>=0` is finite and `F` is the exact robust exit time. Pass 9 proves
that `R_H` is nonempty and compact, and pass 11 proves that every minimizing
state has at most one genuinely partial coordinate. Throughout this note the
budget is critical:

$$C(H)=s>0.                                               \tag{1}$$

A **finite entry into indefinite readiness** means a normal policy starting
from cold which, after a finite warmup, stays in `R_H` at every subsequent
counterfactual request time, for every allowed loss history. It need not reach
a stationary state. The warmup must use the same normal capacity and cannot
transfer modules in order to manufacture additional capacity.

Pass 14 characterizes finite cold domination of each concentrated target
whose maintenance equals `s`. With a partial target of coefficient `beta`,
some full target coordinate must have coefficient larger than `beta`; a
nonzero purely full/cold critical target cannot be reached. Such a reachable
minimizing target can be maintained and therefore suffices for indefinite
readiness. The question is whether one must exist whenever finite entry is
possible. Section 3 onward answers no.

## 2. Every maximal-loss critical ready trajectory converges to one minimum

**Theorem 1 (convergence at the critical budget).** Suppose a normal trajectory
on the simultaneous maximal-loss history belongs to `R_H` for all `t>=T_0`.
Then it converges to a single upkeep-minimizing state `p^*`. Moreover,

$$\int_{T_0}^{\infty}\bigl(L(p(t))-s+u(t)\bigr)\,dt
\leq Q(T_0)-\lim_{t\to\infty}Q(t)<\infty,
\qquad Q=\sum_i p_i.                                    \tag{2}$$

In particular, excess upkeep tends to zero, but neither finite-time arrival
at the minimum nor eventual stationarity is asserted.

**Proof.** Reflection and the normal budget give almost everywhere

$$Q'\leq s-u-L(p).$$

Readiness and (1) imply `L(p)>=s`. Thus `Q` is nonincreasing after `T_0` and
bounded below by zero, so it has a finite limit. Integration gives (2).

Each normal state coordinate is uniformly Lipschitz: its derivative has
absolute value at most `max(s,gamma_i*M_i)`. Consequently `L(p(t))-s` is a
nonnegative uniformly Lipschitz function after `T_0`. Its finite integral
forces it to tend to zero. Indeed, if values remained above some positive
epsilon at arbitrarily late times, the Lipschitz bound would give disjoint
intervals of a fixed positive width on which the values exceed half that
epsilon, contradicting integrability. Hence

$$L(p(t))\longrightarrow s.                              \tag{3}$$

Let `K={p in R_H:L(p)=s}` be the minimizing set. Compactness of `R_H` and
continuity of `L` imply

$$\operatorname{dist}(p(t),K)\longrightarrow0.            \tag{4}$$

Otherwise a sequence staying a fixed distance from `K` would have a limit
point in `R_H`; (3) would put that point in `K`, a contradiction.

The set `K` is finite. Every member is concentrated. A chosen full set `S`
with no partial coordinate determines one vector; with a chosen partial
identity `i`, its amount is forced by the fixed cost:

$$p_i=\frac{s-\sum_{j\in S}\gamma_jM_j}{\gamma_i}.$$

Only amounts strictly between zero and `M_i` are partial, and only finitely
many `(S,i)` choices exist. Endpoint coincidences only reduce the number of
distinct vectors.

Choose disjoint small neighborhoods of the points of `K`. By (4), the
continuous trajectory eventually lies in their union. It cannot move from
one neighborhood to another without leaving that union, so it eventually
stays near one fixed member of `K`. Applying (4) within that neighborhood
proves convergence to that member. This proves the theorem.

This argument is a compactness and dissipation result, not a statement that
stationary policies exhaust critical readiness. It also shows that optional
work has only a finite total budget after entry on the maximal-loss history;
the exact asymptotic optional rate is zero, as the recurring frontier states.

## 3. Exact three-module instance and its unique optimum

Take `s=1` and the following strictly positive parameters:

| Module | Size `M` | Coefficient `gamma` | Released rate `a` | Full maintenance |
|---|---:|---:|---:|---:|
| A | `1/2` | `1` | `2` | `1/2` |
| B | `1` | `2` | `33` | `2` |
| C | `3` | `1/2` | `1` | `3/2` |

Set

$$H=\frac12\log(5/2)+2\log(24/23),\qquad
p^*=(1/2,\ 1/4,\ 0).                                   \tag{5}$$

The target maintenance is `L(p^*)=1`. Transfer full A immediately at a
request. Capacity becomes three, so B starting from `1/4` takes
`(1/2)*log(5/2)`. After B completes, capacity is 36. Cold C then takes

$$2\log\frac{36}{36-3/2}=2\log(24/23).$$

Thus `p^*` is `H`-ready and `C(H)<=1`.

For the matching global certificate, note the exact comparison

$$H<\frac12\log3<\log2,                                 \tag{6}$$

whose first inequality is equivalent to

$$5\cdot24^4=1658880<1679046=6\cdot23^4.$$

An attained minimizing state has maintenance at most one and is concentrated
by pass 11. Neither B nor C can be initially full at that cost. The following
cases exhaust every such concentrated candidate.

**A is not full.** At initial capacity one, subfull B and C are inaccessible:
their full loss rates are two and `3/2`. Therefore A must complete first.
If A is cold, its first stage takes `log2>H`. If A is partial, concentration
makes both B and C cold. After A, preparing B first already takes
`(1/2)*log3>H`, while preparing C first already takes `2*log2>H`. Thus this
case cannot meet the deadline, even if A's own duration is omitted.

**A is full and B is the possible partial coordinate.** Cold C first takes
`2*log2>H`, so B must go first. For initial B preparation `q`, this displayed
order takes

$$\frac12\log(3-2q)+2\log(24/23).$$

Meeting (5) requires `q>=1/4`; the cost bound `1/2+2q<=1` requires the
opposite inequality. Hence the only feasible candidate in this case at cost
at most one is exactly `p^*`.

**A is full and C is the possible partial coordinate.** The cost bound gives
`p_C<=1`. Cold B first already takes `(1/2)*log3>H`. If C is first, its
duration is at least

$$2\log\frac{3-(1/2)\cdot1}{3-3/2}
=2\log(5/3)>\frac12\log3>H.$$

The comparison in the middle follows from `625>243`. The state with only A
full and no partial coordinate is also covered by these cases.

Consequently no cheaper minimizing state exists, and the only minimizing
state is

$$C(H)=1=s,\qquad K=\{p^*\}.                             \tag{7}$$

This is an all-policy conclusion: the exhaustive candidate argument is
licensed by the proved all-state concentration and seriality theorems. It
does not assume that arbitrary initial states are concentrated.

Cold post-request exit is finite: serial A, B, C takes

$$\log2+\frac12\log3+2\log(24/23).$$

Thus the example is in the work order's finite-cold-exit domain despite its
inaccessible individual initial stages.

## 4. The unique optimum cannot be reached or dominated in finite normal time

In `p^*`, the full coordinate A has coefficient one, while the partial
coordinate B has coefficient two. It fails the pass-14 target criterion.
For completeness, its direct obstruction on maximal loss is

$$Z=p_A+p_B-3/4,\qquad
Z'\leq1-p_A-2p_B=-2Z+(p_A-1/2)\leq-2Z.$$

This bound permits arbitrary normal allocations, including allocations to C:
such allocations only reduce the budget available to A and B. Starting cold
gives `Z(0)=-3/4`, so

$$Z(t)\leq-(3/4)e^{-2t}<0                                \tag{8}$$

for every finite time. Any vector dominating `p^*` would instead have
`p_A+p_B>=3/4`. No normal policy can guarantee finite domination of the sole
minimizer. This is the obstruction which the viable trajectory below avoids.

## 5. A finite warmup followed by indefinite robust readiness

First allocate all spare capacity to C, using `(v_A,v_B,v_C)=(0,0,1)` for
`2*log2`. The virtual maximal-loss state becomes `(0,0,1)`. From that time on,
use the constant normal allocation

$$(v_A,v_B,v_C)=(1/2,1/2,0),\qquad u=0.                   \tag{9}$$

Let `t` denote elapsed time after this initial C preparation and put
`x=exp(-t/2)`. The virtual maximal-loss trajectory is exactly

$$p_A=\frac12(1-x^2),\qquad
p_B=\frac14(1-x^4),\qquad p_C=x.                         \tag{10}$$

All coordinates lie inside their physical bounds. They converge to `p^*`,
but A remains strictly below `1/2` at every finite time.

We now certify every request time for which `0<x<=1/128`, using the feasible
serial order A, B, C after the request. Let `t_A` and `t_{AB}` be global
completion times measured from that request. The scalar stage equations give

$$e^{t_A}=1+x^2,\qquad
e^{2t_{AB}}=Y(x):=\frac52+6x^2+\frac72x^4.               \tag{11}$$

For example, the second identity is
`3*(1+x^2)^2-2*p_B`, since B's stage capacity is three and its denominator is
`3-2=1`. Its waiting decay is already included in this global-time formula.
For C, capacity 36 and coefficient `1/2` give the final completion time `T`:

$$e^{T/2}=\frac{72Y(x)^{1/4}-x}{69},\qquad
e^{H/2}=\frac{72(5/2)^{1/4}}{69}.                        \tag{12}$$

Therefore it suffices to prove

$$72\left[Y(x)^{1/4}-(5/2)^{1/4}\right]\leq x.$$

The concavity of the fourth root and `5/2>1` give

$$\begin{aligned}
72\left[Y(x)^{1/4}-(5/2)^{1/4}\right]
&\leq \frac{18}{(5/2)^{3/4}}\left(6x^2+\frac72x^4\right)\\
&<108x^2+63x^4\\
&\leq x\left(\frac{108}{128}+\frac{63}{128^3}\right)
<x                                                        \tag{13}
\end{aligned}$$

whenever `0<x<=1/128`. The final strict inequality is an exact rational
comparison. This proves `T<H` for every finite request time in that interval;
equality is approached only in the limiting state.

The condition `x<=1/128` holds after `t=14*log2`. Including the initial C
preparation, the total warmup is therefore

$$T_{\mathrm{warm}}=16\log2.                             \tag{14}$$

No module transfers during this warmup or the subsequent normal policy. Both
allocation phases respect the normal capacity one. After warmup, every
counterfactual removal request meets `H` by the displayed post-request
strategy.

This guarantee is robust, not merely a calculation on one benign history.
The normal allocations use predetermined durations and the virtual maximal
trajectory above. Scalar comparison makes every actual coordinate under
smaller allowed losses at least the virtual value. The ready set is upward
closed by the established comparison argument; thus every actual state is
also ready. The serial request policy likewise finishes no later under
smaller losses. Upper reflection preserves these comparisons.

## 6. Why the critical convergence theorem is consistent with this example

Along (10), maintenance is

$$L(p)=1+\frac12x-\frac12x^2-\frac12x^4>1$$

for `0<x<=1/128`. It exceeds the sustainable stationary minimum at every
finite time, but its excess is integrable because `x=exp(-t/2)`. Total
preparation is

$$Q=\frac34+x-\frac12x^2-\frac14x^4,$$

which decreases to `3/4` during the guaranteed regime. The extra preparation
in C declines more slowly than the deficits in A and B. Its request-time
benefit pays for those remaining deficits, as the exact inequality (13)
demonstrates. The support total `p_A+p_B` stays strictly below `3/4`, so the
unreachable-target invariant (8) is never violated.

All three coordinates are partial at every finite time after entry. This
does not contradict concentration: that theorem classifies **minimum-cost
ready states**, and these transient ready states have cost strictly above
the minimum. Their stored preparation supplies that finite total excess
while the normal allocation uses exactly the available budget.

Thus the convergence theorem is sharp about its limitation. Critical ready
trajectories must approach a minimum, but can remain ready without reaching
or dominating any minimizing state in finite time.

## 7. Scientific consequence and stopping point

The pass-14 test settles critical startup to a chosen concentrated target,
and remains a useful sufficient test for entering indefinite readiness. It
is not a necessary test for the full ready region once three modules are
allowed. The companion two-module proof establishes the smaller boundary;
the example above supplies an exact separation with positive parameters,
finite cold exit, a unique minimum, and a fully specified robust policy.

This resolves the present work order's proposed equivalence. It does not
characterize every viable subset of `R_H` or claim an algorithm for general
cold-entry viability. Further expansion of that control problem is not
needed to preserve the finding. The concentration/frontier result and its
nonlinear boundary remain the principal mathematical package; startup now
has a precise warning against replacing viable transient preparation by
reachable stationary optima.
