# Pass 15 companion: critical startup has an exact two-module boundary

22 September 2026, continuing from `bb1e34f41338745c88ae486d493a053c658fb3d1`.
The [three-module critical-viability note](2026-09-22-pass15-critical-viability.md)
shows why reaching a minimum-cost target need not be necessary for entering
indefinite readiness. This companion proves that the proposed implication
nevertheless holds with two modules. The distinction concerns the existing
proportional-loss model, not a new operational assumption or a novelty claim.

## 1. Question and result

Use two independent modules with finite parameters

    M_i>0, gamma_i>0, a_i>=0, s>0.

Normal preparation starts cold and obeys the reflected maximum-loss dynamics
`p_i'=v_i-gamma_i*p_i`, with nonnegative measurable allocations whose sum is
at most `s`. No module transfers during normal operation or warmup. Smaller
losses are also allowed, and simultaneous maximum feedback is admissible.
Post-request exit uses the independent instantaneous transfers and released
capacities of the preceding notes. Policies are deterministic and causal;
preemption, parallel preparation, and adaptation are permitted.

Let `F(p)` be the exact robust exit time, and fix a finite deadline `H>=0`
such that

    C(H)=min_{F(p)<=H} sum_i gamma_i*p_i=s.                  (1)

Assume cold post-request exit is finite. The blocked-cold case is already
excluded by the [barrier theorem](2026-09-22-pass13-barriers-startup.md).
The warmup is finite but need not satisfy the removal deadline; the guarantee
begins at its end and must continue indefinitely at every request time.

**Theorem (two-module critical startup).** Under these assumptions, finite
robust cold warmup followed by indefinite `H`-readiness is possible if and
only if some minimizing target in (1) passes the
[critical fixed-target test](2026-09-22-pass14-critical-startup.md).
Equivalently, some minimizer has one full module and one genuinely partial
module, with the full module's loss coefficient strictly larger than the
partial module's coefficient.

The minimizing target need not be unique. The conclusion is existence of a
reachable minimum, not that every ready trajectory reaches its limiting
minimum in finite time. The three-module counterexample shows that the
dimension restriction is substantive.

For one module, finite cold exit requires `s>gamma_1*M_1`, whereas
`C(H)<=gamma_1*M_1<s`; the critical case considered here is therefore absent.

## 2. Consequence of critical convergence

The convergence lemma in the main pass-15 note applies on the allowed
maximum-loss history. An indefinitely ready critical trajectory satisfies,
after warmup,

    Q'= (p_1+p_2)' <= s-sum_i gamma_i*p_i <=0.              (2)

Its excess upkeep has finite integral. Bounded controls and the physical box
give a uniform Lipschitz bound, so the upkeep tends to `s`. Concentration
makes the minimizing set finite: choosing its full set and possible partial
identity determines the latter's amount from its cost. Compactness and
continuity then force the trajectory to converge to one minimizing vector
`p^*`, even when several minima exist.

In particular, with `Q^*=p_1^*+p_2^*`, monotonicity gives

    Q(t)>=Q^*                                               (3)

at every time after warmup. The argument below excludes each possible
unreachable limiting shape. It does not assume stationary normal controls.

## 3. One full and one partial coordinate

Write the limiting target as `(M_A,r_B)`, with coefficients `alpha,beta` and
`0<r_B<M_B`. If `alpha>beta`, the target is robustly reachable by the
pass-14 construction, so the necessary conclusion is already established.

Otherwise `alpha<=beta`, and criticality says

    s=alpha*M_A+beta*r_B.

On the entire maximum-loss history starting cold, not merely after readiness
begins, let `Z=Q-(M_A+r_B)`. Upper reflection can only decrease its derivative:

    Z'<=-beta*Z+(beta-alpha)*(p_A-M_A)<=-beta*Z.             (4)

Since `Z(0)<0`, it remains strictly negative at every finite time. This
contradicts (3). An unreachable minimum of this shape therefore cannot be the
limit of an indefinitely ready trajectory reached from cold.

## 4. A partial coordinate and a cold coordinate

Write `p_A^*=r`, `p_B^*=0`, `0<r<M_A`, with `alpha=gamma_A`. Criticality
gives `alpha*r=s`, whereas `alpha*M_A>s`. Thus A cannot complete first at
the initial post-request capacity `s`, even from its partial preparation.
Any finite attaining serial order at the target must finish cold B before A.

The optimizer-prefix corollary of
[unequal-rate concentration](2026-09-22-pass11-unequal-decay.md) then gives
`beta=gamma_B>alpha`: every cold predecessor of the partial module in a
minimizing target's feasible order has the larger loss coefficient.

Let `Z=Q-r`. On the maximum-loss cold history,

    Z'<=-alpha*Z-(beta-alpha)*p_B<=-alpha*Z.                 (5)

Again `Z(0)<0` makes `Q(t)<r=Q^*` at every finite time, contradicting (3).
This case uses the order restriction on minimizing states; a cold module's
loss coefficient cannot be assigned an arbitrary comparison sign.

## 5. A full coordinate and a cold coordinate

Write `p_A^*=M_A`, `p_B^*=0`, with coefficients `alpha,beta`. Criticality
gives `s=alpha*M_A`. If `beta>=alpha`, the same whole-state comparison gives

    [Q-M_A]'<=-alpha*(Q-M_A)-(beta-alpha)*p_B
              <=-alpha*(Q-M_A).                           (6)

Thus `Q(t)<M_A=Q^*` on every finite maximum-loss cold history, again
contradicting (3).

It remains to treat `beta<alpha`. A scalar comparison, valid under every
normal allocation on that history, gives

    p_A(t)<=M_A*(1-exp(-alpha*t))<M_A                      (7)

for every finite time. At a request from a state with A subfull, A cannot
complete first: its available rate is exactly its full loss `s=alpha*M_A`.
Consequently every nearby ready state with A subfull must use the serial
order B then A. A neighborhood of `p^*` also has B subfull.

We show that this order cannot meet `H` at `p^*`, even if one deliberately
postpones its initially full A. If either stage is inaccessible, the assertion
is immediate. Otherwise put

    D_B=s-beta*M_B>0,
    b_2=s+a_B,
    D_A=b_2-alpha*M_A>0,
    t_B=log(s/D_B)/beta.

Suppose this delayed-full order were feasible at `p^*`, and denote its final
time by `T<=H`. Increase initial B preparation from zero to `x>0`, and choose
initial A preparation `y(x)` to keep the same final time:

    y(x)=[b_2*((s-beta*x)/D_B)^(alpha/beta)
          -D_A*exp(alpha*T)]/alpha.                       (8)

At `x=0`, `y(0)=M_A`. Its derivative is negative, so for sufficiently small
positive `x`, both `0<x<M_B` and `0<y(x)<M_A`. These are genuine feasible
serial stages with unchanged positive denominators. Their maintenance
derivative at zero is

    d/dx [beta*x+alpha*y(x)] at x=0
       = beta-alpha*(b_2/D_B)*exp((alpha-beta)*t_B)<0.      (9)

Indeed `alpha>beta`, `b_2>=s>D_B`, and `t_B>0`. Equation (8) would therefore
give a strictly cheaper `H`-ready state, contradicting (1). This rules out the
delayed-full B-then-A order at the limiting target.

When the order has accessible stages, its completion time is continuous near
`p^*` by the displayed flow formulas. Since its time at the target exceeds
`H`, it remains infeasible in some neighborhood. When a denominator is
inaccessible, it stays inaccessible for nearby subfull states because stage
capacities do not depend on initial preparation. Hence no state with A
subfull in a sufficiently small neighborhood of `p^*` is ready. Equation (7)
and convergence to `p^*` contradict indefinite readiness.

This argument does not assume that `H=F(p^*)`. An initially full barrier
coordinate can produce deadline slack; the cost-improving variation in
(8)–(9), rather than a shortcut assertion, excludes the competing order.

## 6. Both coordinates full and completion of the proof

If both coordinates of a minimizing target are full, criticality says
`s=d_A+d_B`. If `H>0`, transfer B at time zero and reduce A's initial
preparation by a sufficiently small positive amount. Its resulting capacity
`s+a_B` is strictly greater than `d_A`, since `d_B>0`. Its completion time
therefore tends continuously to zero as that reduction tends to zero. This
produces a cheaper state meeting `H`, a contradiction. Thus this minimizing
shape can occur here only when `H=0`.

At deadline zero every module must be full initially. The nonzero pure-full
critical-target obstruction from pass 14 excludes finite cold reachability.
The all-cold vector cannot minimize (1), because its maintenance is zero
whereas `s>0`.

Concentration exhausts the shapes in Sections 3–6. An indefinitely ready
cold-start trajectory must converge to a minimum, and every minimum failing
the fixed-target test has now been excluded as its limit. This proves
necessity. Conversely, a minimizing target passing that test can be reached
or dominated after finite robust warmup, and its maintenance allocation of
total rate `s` preserves domination indefinitely. Its robust exit policy then
meets `H` at every later request, proving sufficiency.

## 7. Scope

The two-module equivalence is a boundary result for critical normal startup.
It neither strengthens the general concentration theorem nor restores a
fixed-target reduction in higher dimensions. The separate three-module
construction remains an exact counterexample to that reduction. Both results
retain paid receiver resources, the proportional loss envelope, and
instantaneous independent post-request transfers; their physical applicability
and theorem-level attribution remain separate research questions.
