# Independent proof audit: fixed-rate readiness and heterogeneous exits

Date: 22 September 2026. This is an internal adversarial proof audit, not an
external review or a novelty certification. The immutable active checkpoint was
read in full. Root `python verify.py` was actually run during this audit and
passed, reproducing both historical reports without changing their originals.

## 1. Audit outcome

No error was found in the homogeneous Proposition 1 or Theorem 2 under their
stated reflected-fluid dynamics and initialization allowance. Their main
limitation is the strength of the model assumptions, especially simultaneous
full-rate erosion of every positive preparation.

The heterogeneous support/upkeep reduction is valid under the same assumptions.
It is elementary once the exit problem is defined correctly; the reduction
alone should not be represented as a substantial novelty result.

The heterogeneous scheduling problem also has an all-policy serial reduction
from ready/cold states. The potential in Section 3 gives a direct proof that
every finite feasible schedule is at least as slow as the serial schedule with
the **same completion order**. This includes arbitrary preemption and parallel
allocation. A separate scheduling researcher in this workspace independently
checked the potential and its boundary cases. This is still an internal
collaborative mathematical check.

## 2. Homogeneous proof audit

The checkpoint's inequality

$$Q'\leq\sum_i v_i-d\,|\{i:p_i>0\}|$$

is correct with reflection. At zero, the contribution is
`max(v_i-d,0) <= v_i`; at a positive interior state it is `v_i-d`; at the upper
boundary it is `min(v_i-d,0) <= v_i-d`. In particular, one must not subtract `d`
for a cold coordinate. The checkpoint does not make that mistake.

For its exit potential `Z`, the claimed upper bound on `Z'` is also correct.
When some unfinished preparation is positive, at least one full `d` loss is
incurred. When every unfinished preparation is zero, any positive growth
requires an allocation exceeding `d`; its reflected gain pays that loss. On a
positive-measure set on which all coordinates remain zero, their derivatives
vanish almost everywhere. The latter observation resolves any apparent issue
at switching instants.

The piecewise-linear increasing `Phi` is locally Lipschitz on the relevant
compact interval when the first net rate is positive. Its composition with an
absolutely continuous `Z` admits the stated almost-everywhere chain rule.
Backward motion of `Z` does not invalidate the bound. At a level set of a
breakpoint, `Z'=0` almost everywhere. The arbitrary denominator value at the
final endpoint is immaterial.

If the available capacity is no greater than `d`, no initially cold module
can begin positive progress under maximum invalidation, so the infinite-time
case is exact. This includes equality. An already ready module is different:
its instantaneous transfer may increase the available capacity before any
cold preparation is attempted.

The support argument only asserts necessity. Having `k_H` arbitrarily tiny
positive preparations does **not** itself make a state ready. The averaging
proof needs only the necessary support condition, so it does not confuse these
claims.

## 3. Heterogeneous seriality: an independent potential proof

Assume finitely many modules with `M_i>0`, `a_i>=0`, `d_i>=0`, initial spare
capacity `s>=0`, common resource units, and the checkpoint's componentwise
reflected dynamics with maximum invalidation `rho_i=d_i`. All initially ready
modules have already transferred; every remaining module starts cold. Available
reconciliation capacity is

$$b=s+\sum_{i\text{ already transferred}}a_i.$$

It is nondecreasing. Immediate transfer is allowed and has no downside. Delayed
transfer would not defeat the lower bound below, but cannot improve the optimum.

For a stage between transfers with `b>0`, define

$$W_b(p)=\sum_{i\text{ unfinished}:d_i<b}\frac{p_i}{b-d_i}.$$

An unfinished coordinate with `d_i>=b` must still be zero: capacity was never
larger in the past, and its allocation has therefore never exceeded its loss
rate. It cannot have acquired positive preparation from a cold start.

For each eligible coordinate `d_i<b`, `0<=v_i<=b` gives

$$\frac{v_i-d_i}{b-d_i}\leq\frac{v_i}{b}.$$

Indeed this inequality is equivalent to `d_i v_i <= d_i b`. It remains true
for the reflected derivative at both boundaries: at zero replace the numerator
by `max(v_i-d_i,0)`; when `v_i<=d_i`, the resulting left side is zero, and when
`v_i>d_i`, the same displayed calculation applies. At `M_i`, clipping the
derivative downward preserves the inequality. Consequently,

$$\frac{d}{dt}W_b(p(t))\leq\frac{\sum_i v_i(t)}b\leq1$$

almost everywhere in that stage.

When module `i` transfers, it contributes `M_i/(b-d_i)` to the potential just
before removal. The capacity changes to `b+a_i`. Existing remaining eligible
terms decrease or stay unchanged because their denominators increase. Newly
eligible terms were zero, by the preceding cold-state observation. Thus the
downward jump of the potential is at least

$$\frac{M_i}{b-d_i}.$$

Initially and finally the potential is zero. Integrating its derivative over
all stages and summing the jumps therefore gives, for the schedule's completion
order `pi`,

$$T\geq\sum_j
\frac{M_{\pi_j}}{s+\sum_{i\text{ initially ready}}a_i+
                    \sum_{\ell<j}a_{\pi_\ell}-d_{\pi_j}}.$$

Each denominator encountered in a finite schedule is strictly positive. Running
these modules serially in order `pi`, at their entire currently available
capacity, attains the right side. Taking the minimum over finitely many orders
establishes an attained optimum. A permutation with a nonpositive stage
denominator is infeasible and assigned infinite cost.

Boundary details:

- If `b=0` and any cold module remains, no progress is possible until another
  ready module transfers. After the initial ready transfers there is none, so
  exit is impossible. This avoids dividing by zero in the potential.
- At `d_i=b`, module `i` remains zero and is excluded. If capacity later rises
  past `d_i`, its newly included term is exactly zero at that moment.
- `d_i=0` is valid whenever `b>0`; the local inequality becomes equality for an
  unclipped coordinate. `a_i=0` is also allowed, producing no denominator drop.
- Simultaneous completions can be placed in any order as zero-time transfers.
  Each intermediate potential jump still has the required sign. The associated
  serial order uses the successive increased capacities, giving a legitimate
  lower bound.
- Arbitrary measurable bounded allocations, negative partial-progress
  derivatives, idle intervals, and repeated preparation loss are allowed.
  There are at most `n` transfers, so only finitely many potential jumps occur.

There is also an exact inefficiency decomposition. For a schedule ending at
its final transfer,

$$T-T_{\rm serial}(\pi)
=\int_0^T(1-W'(t))\,dt
+\sum_{\text{transfers }i}\ \sum_{\substack{j\text{ remaining}\\d_j<b}}
\frac{a_i p_j}{(b-d_j)(b+a_i-d_j)}\geq0.$$

Here `W'` is the within-stage derivative, and `b,p` are taken immediately before
each transfer in the chosen ordering. This identity follows by retaining the
entire potential jump instead of only its removed-module term. With `a_i>0`,
any other unfinished positive preparation at that transfer incurs a strictly
positive excess over its serial order. Heterogeneity does not by itself create
a benefit from parallel cold-start preparation in this model.

**Scope:** initially partial unfinished states need not have zero potential.
The proof above does not establish serial optimality from such states. The
readiness theorem only needs the ready/cold exit problem because its lower
bound grants optimistic completion of the normal state's positive support.

## 4. Heterogeneous support/upkeep reduction

Let `tau(S)` be the attained optimal robust exit time from the ready/cold state
whose ready set is `S`, and define

$$D(H)=\min_{S:\tau(S)\leq H}\sum_{i\in S}d_i.$$

The set is nonempty for finite `H>=0`, since the all-ready state exits instantly.
The serial theorem resolves a potential endpoint issue: if `tau` were merely
an unproved infimum, `tau(S)=H` would not on its own imply an exit policy meeting
the exact deadline. Here a minimum among finitely many serial permutations
attains every finite `tau(S)`.

Consider any robustly ready state `p` and `S={i:p_i>0}`. Replacing each positive
coordinate by a fully ready module and transferring it can only help: it removes
unfinished work, removes its future invalidation, and weakly increases capacity.
Independence excludes a penalty to the remaining modules. Every coordinate
outside `S` is already cold. Hence `tau(S)<=H`, and

$$\sum_{i:p_i>0}d_i\geq D(H).$$

This domination can be made policywise: run a virtual copy of the original
post-request policy, omit its allocations to the already transferred support,
and apply its allocations to the other coordinates. The virtual policy's
capacity is no larger than the real capacity at every time. Under the same
invalidation history, these other coordinates can match it. Maximum
componentwise invalidation supplies a common adversarial history for the
lower bound; it is not necessary to choose incompatible per-policy histories.

Along that allowed maximum history, `Q=sum_i p_i` satisfies

$$Q'\leq s-u-\sum_{i:p_i>0}d_i\leq s-u-D(H).$$

Thus every duration `t>0` in a uniformly ready deployment obeys

$$\int_0^t u(r)\,dr\leq(s-D(H))t+Q(0)-Q(t).$$

The long-run throughput is at most `s-D(H)` under this adversary. If `D(H)<=s`,
initialize a minimizing subset at full readiness, maintain module `i` in that
subset at rate `d_i`, keep all other modules cold, and allocate optional rate
`s-D(H)`. The serial exit schedule attains the deadline. Smaller actual
invalidation never makes that construction worse. If `D(H)>s`, bounded `Q`
rules out indefinite readiness even with zero optional work.

This is a robust worst-case performance theorem. It is not an assertion that
every benign history forces this throughput. Randomized policies, if admitted,
must satisfy the readiness contract pathwise; a guarantee only in expectation
would be a different problem.

## 5. Initialization and finite horizons

The fixed-subset attaining policy requires initialized full preparations. Their
total `sum_{i in S} M_i` is a real startup expense outside the theorem's
guaranteed normal deployment. Normal capacity sufficiency `D(H)<=s` does not
imply cold-state startup feasibility under that same fully loaded regime.
For example, one module with `s=d>0` can be kept fully ready but cannot grow
preparation from zero under maximum invalidation. At `s=d=0`, a preinitialized
module remains ready without upkeep, but a cold module still cannot be prepared.

When `D(H)>s` and `u>=0`, any ready finite deployment obeys

$$t\leq Q(0)/(D(H)-s)\leq\sum_i M_i/(D(H)-s).$$

This is only an upper bound. It need not be attainable and can be loose. For
`H=0`, all modules must be fully ready at every operating time; if their total
maintenance rate exceeds `s`, no positive-length ready deployment exists, even
though the displayed energy-style upper bound can be positive. For a pointwise
optional floor `u>=u_0`, replace the positive denominator by `u_0+D(H)-s`.

When some `d_i=0`, retaining their preparation has zero recurring cost.
The theorem correctly permits all such modules to be ready for free after
paid initialization. It does not attribute their startup work to ongoing upkeep.

## 6. Assumptions that cannot be silently weakened

| Assumption | Role in the proof | What changing it invalidates |
|---|---|---|
| All componentwise maxima can occur simultaneously | Supplies one allowed worst-case history and its summed support loss | A shared aggregate update budget needs a different lower bound |
| Any positive preparation can lose work at full `d_i` | Charges support independently of preparation magnitude | Proportional, spatially restricted, or log-based updates need new analysis |
| Capacity only increases on transfer | Keeps inaccessible cold coordinates at zero; potential denominators only improve | Added receiver/source load or transfer penalties can defeat seriality |
| All remaining coordinates start cold in the exit subproblem | Makes initial potential zero and newly eligible coordinates cold | Arbitrary partial-state seriality is not proved |
| Independent modules and independent receiver resources | Makes support completion and early transfer beneficial | Consistency barriers and hidden shared services can break domination |
| Zero-duration, zero-cost cutover | Allows the potential jumps and immediate capacity release | Cutover latency or work must enter the scheduling model |
| Readiness at every admissible normal time | Applies the support cost throughout the normal trajectory | A single known future request can favor temporary preparation |
| Paid initialized readiness | Makes the exact long-run upper bound attainable | Cold startup under fixed normal load is a separate reachability problem |

The homogeneous checkpoint already flags most of these restrictions. Their
continued visibility matters more than assigning the result a broad name.

## 7. Remaining scientific assessment

The proof establishes an exact finite optimization and a matching all-policy
lower bound inside the stated model. It does not establish a polynomial-time
ordering algorithm, a simple universal ranking index, practical correctness of
an independent fallback interface, or meaningful publication novelty. In
particular, the scheduling theorem's technical simplicity increases the
importance of checking resource-producing scheduling literature carefully.

The strongest next mathematical questions are whether the order optimization
has a useful structural/complexity characterization, and which defensible
update models retain a nontrivial readiness theorem. These should be assessed
against inspected prior results before being used as a paper's central claim.

## 8. Follow-on audit: homogeneous proportional-loss frontier

The fifth pass replaces discontinuous support loss by proportional loss
`g(p)=gamma*p`, with identical `M,a,gamma>0`, `d=gamma*M`, and **`s>d`**. This
audit found no gap in its total-preparation bound or attaining concentration
policy. The maximum adversary here is the state-dependent feedback
`rho_i(t)=gamma*p_i(t)`, simultaneously for all unfinished modules.

For arbitrary initial preparation with total `Q`, use

$$Z=MJ+\sum_{i\text{ unfinished}}p_i.$$

`Z` is continuous at a transfer because replacing a full coordinate by the
increase in `MJ` preserves its value. Under maximum loss, its within-stage
derivative satisfies

$$Z'\leq s+(a+d)J-\gamma Z
\leq s+(a+d)\lfloor Z/M\rfloor-\gamma Z=:f(Z).$$

The second inequality uses `J<=floor(Z/M)` and `a+d>0`; it remains valid when
preparation is decreasing. For `z=jM+r`, `0<=r<M`, the denominator is
`f(z)=s+ja-gamma*r`, which is bounded below by the strictly positive `s-d`.
Consequently `Phi(z)=integral_0^z dq/f(q)` is continuous, strictly increasing,
and Lipschitz on the compact domain. Its piecewise-smooth breakpoints do not
invalidate the almost-everywhere chain rule; at a breakpoint level set, `Z'`
vanishes almost everywhere. Thus every completing schedule obeys

$$T\geq G(Q):=\int_Q^{nM}\frac{dz}{f(z)}.$$

The state with `k` full preparations, one preparation `r`, and the rest cold,
where `Q=kM+r`, attains equality by transferring the full modules and then
preparing the remaining modules serially. `Q=nM` is the separate all-ready
case and has zero exit time. This proves the best possible exit at prescribed
total preparation, while leaving the exit time of a specified dispersed state
potentially larger.

That distinction is substantive. For example, take `n=2`, `M=1`, `a=1`,
`gamma=1/2`, `s=1`, and total preparation `Q=1`. State `(1,0)` exits in
`2 log(4/3)`. From `(1/2,1/2)`, even the earliest possible first cutover takes
at least `2 log(3/2)`, by allocating all capacity to that module. The latter
already exceeds the concentrated state's entire exit time. Therefore a bound
on total `Q` alone is a necessary readiness condition, not a sufficient
condition for every state with that total.

For `H` below the cold exit time, let `Q_H` be the unique solution of
`G(Q_H)=H`; for larger `H`, set `Q_H=0`. Normal-operation readiness necessarily
requires `Q>=Q_H`, and maximum-loss reflection gives

$$Q'\leq s-u-\gamma Q\leq s-u-\gamma Q_H.$$

The concentrated stationary state achieves upkeep `c(H)=gamma*Q_H` whenever
`c(H)<=s`, with paid initialization. Use fixed maintenance allocations
`v_i=gamma*p_i^*` at the target state. Under smaller actual losses, scalar
comparison ensures actual preparation stays at least `p_i^*`; it does not
require losses to be a predetermined common numerical time history. The
maximum-loss history forces the matching throughput bound. When `c(H)>s`,
bounded total preparation rules out indefinite readiness.

The proposed piecewise expression also checks algebraically. With

$$b_k=s+ka,\qquad
T_k=\sum_{j=k}^{n-1}\gamma^{-1}\log\frac{b_j}{b_j-d},
\qquad T_n=0,$$

for `T_{k+1}<=H<=T_k` it is

$$c(H)=kd+b_k-(b_k-d)e^{\gamma(H-T_{k+1})}.$$

At `H=T_k` this is `kd`, and at `H=T_{k+1}` it is `(k+1)d`, so adjacent pieces
match. Set `c(H)=0` for `H>=T_0`; `H=0` gives `nd`. For `n=1`, the expression
reduces exactly to the archived proportional countermodel
`max(0,s-(s-d)exp(gamma*H))`. These checks are analytic identities; finite
numeric checks are supporting verification.

The restriction `s>d` is used to keep every integration denominator strictly
positive. This proof does not cover the critical or subcritical spare-capacity
regimes. Nor does it transfer the discontinuous fixed-loss startup theorem to
the proportional model. The new result removes the need for the fixed-loss
assumption in this homogeneous frontier, but still relies on independent
modules, identical parameters, cooperative grace, and paid independent receiver
provisioning. A novelty or deployment claim does not follow from the proof.
