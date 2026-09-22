# An exact continuous readiness frontier for homogeneous modules

22 September 2026. Research pass 5. This note solves the recurring-readiness
question for a homogeneous proportional-invalidation alternative. It does not
merely substitute smooth stage times into the fixed-rate hot-subset formula:
one partially prepared module is generally necessary for attaining the smooth
frontier. The frontier is continuous and piecewise analytic, generally with
kinks. Publication novelty and a validated physical interface remain open.

## 1. Model and precise question

There are `n>=1` independent modules with common preparation size `M>0`,
released capacity `a>0`, proportional-loss constant `gamma>0`, and fully ready
loss rate `d=gamma*M`. Spare capacity satisfies the strict assumption `s>d`.
All parameters are finite. The prescribed normal service, independent fallback,
shared source budget, instantaneous cutover, and paid initialization contract
are those of the active checkpoint.

Replace the fixed-rate uncertainty by

    0 <= rho_i(t) <= gamma*p_i(t),

with reflected dynamics on `[0,M]`. Actual loss bounds are evaluated at the
actual state. Simultaneously maximal loss `rho_i=gamma*p_i` is an admissible
feedback adversary. Policies may be causal, parallel, preemptive, time varying,
and adaptive, with bounded measurable allocations. The guarantee concerns
every allowed update history and every counterfactual request time.

Normal operation obeys `u+sum_i v_i<=s`, with nonnegative optional work `u`.
After a request optional work stops, and after `J` cutovers the preparation
budget is `s+a*J`. No module transfers before the request. Arbitrary initial
partial preparation is allowed if its initialization has been paid for.

For an initial total preparation `Q in [0,n*M]`, ask for the best robust exit
time among **all distributions** of that total across modules. The answer is
not asserted to be the exit time of every distribution with that same total.

## 2. Aggregate lower bound from arbitrary partial states

On the simultaneous maximal-loss history during exit, let

    Z(t) = M*J(t) + sum_{unfinished i} p_i(t).

A cutover increases `M*J` by `M` and removes exactly `M` from the other sum, so
`Z` is continuous and absolutely continuous across the finitely many cutovers.
It starts at the pre-request total `Q`, including any modules transferred at
time zero, and finishes at `n*M`.

The reflected dynamics and budget give, almost everywhere,

    Z' <= s+a*J - gamma*sum_{unfinished i} p_i
       = s+(a+d)*J - gamma*Z.

Since `J<=floor(Z/M)`,

    Z' <= f(Z),
    f(z) = s+(a+d)*floor(z/M)-gamma*z.             (1)

For `k*M<=z<(k+1)*M`, this envelope is

    f(z) = b_k-gamma*(z-k*M),   b_k=s+k*a.

The assumption `s>d` makes it uniformly positive on `[0,n*M]`; values at the
finitely many breakpoints do not affect integrals. Define

    T(Q) = integral_Q^{n*M} dz/f(z).               (2)

The increasing potential `Phi(z)=integral_0^z dy/f(y)` is continuous and
Lipschitz. Its composition with `Z` has derivative at most one almost
everywhere. At a breakpoint, the derivative of `Z` vanishes at almost every
time spent at that level, so the finitely many derivative discontinuities of
`Phi` cause no gap. This also permits trajectories that lose preparation.
Integration gives

    every robust exit from total Q takes at least T(Q).       (3)

The bound is over the full policy class, not just serial schedules. Its lower
bound adversary is one admissible state-feedback rule, not a claim about benign
loss histories.

## 3. Concentrated preparation attains the bound

Write `Q=k*M+r` with `k=floor(Q/M)` and `0<=r<M`; handle `Q=n*M` separately.
Prepare exactly `k` modules fully, one additional module to `r` if `r>0`, and
leave the rest cold. At the request transfer the `k` ready modules immediately.
If `r>0`, allocate all available `b_k` to that partial module first; if `r=0`,
start with any cold module. Complete all subsequent modules serially.

At each stage there is only one unfinished module with positive preparation,
so equality holds in the envelope (1) except at irrelevant endpoints. Under
maximal loss, the first stage has duration

    log[(b_k-gamma*r)/(b_k-d)]/gamma,

followed by the cold serial stages at capacities `b_{k+1},...,b_{n-1}`.
Smaller allowed losses cannot delay this construction, by scalar comparison
with `p'=b_k-gamma*p`. Therefore it attains (2) robustly. If `Q=n*M`, all
modules transfer at time zero and `T(n*M)=0`.

**Theorem 1 (best readiness at a fixed total).** Among all initial states with
total preparation `Q`, the minimum guaranteed exit time is exactly `T(Q)`.
Concentrating that total into fully ready modules, at most one partial module,
and otherwise cold modules attains it. A state from which deadline `H` is
guaranteed must have `T(Q)<=H`, but that scalar condition is not claimed
sufficient for an arbitrary distribution of the same total.

For convenience define the ready/cold endpoint times

    T_k = T(k*M)
        = sum_{j=k}^{n-1} log[b_j/(b_j-d)]/gamma,
    T_n = 0.                                                 (4)

For `Q=k*M+r<n*M`, the full expression is

    T(Q) = T_{k+1}
           + log[(b_k-gamma*r)/(b_k-d)]/gamma.                 (5)

It is continuous and strictly decreasing from finite `T_0` to zero.

The preparation shape matters even with two modules. Take
`n=2`, `M=a=gamma=1`, `s=2`, and total `Q=1`. The concentrated state `(1,0)`
exits in `log(3/2)`, whereas the evenly spread state `(1/2,1/2)` has exact
optimal time `log(2)`. To verify the latter without restricting schedules,
let `t` be the first cutover time on maximal loss. Before that cutover each
module satisfies `p_i(t)<=2-(3/2)*exp(-t)`, so `t>=log(3/2)`. Total preparation
is at most `2-exp(-t)`, leaving at most `x=1-exp(-t)` in the other module.
Its remaining stage at capacity three takes at least
`log[(2+exp(-t))/2]`. Total time is consequently at least
`log(exp(t)+1/2)>=log(2)`. Full allocation to one module until `log(3/2)`
leaves `1/3` in the other; its final stage takes `log(4/3)`, attaining the bound.
Thus the scalar necessary condition really is insufficient for arbitrary
states, while the concentrated construction makes it sufficient by design.

## 4. Exact recurring cost at every request time

For a finite deadline `H>=0`, let

    Q_H = min {Q in [0,n*M] : T(Q)<=H},
    c(H) = gamma*Q_H.                                        (6)

The minimum exists by continuity, and `Q_H=0` for `H>=T_0`. Theorem 1 implies
that every uniformly ready normal policy has total preparation `Q(t)>=Q_H`
at every possible request time along the maximal-loss history.

During normal operation, upper reflection can only reduce progress, so

    Q' <= s-u-gamma*Q <= s-u-c(H).

Consequently, for every normal duration `L>0`,

    integral_0^L u(t)dt <= [s-c(H)]*L + Q(0)-Q(L).             (7)

Bounded preparation implies
`limsup_{L->infinity} average(u)<=s-c(H)` on this admissible history. This
covers rotating, bursty, and partially prepared policies without assuming an
average exists or a steady state is reached.

If `c(H)<=s`, initialize the concentrated state of total `Q_H` from section 3.
Allocate `d` to each of its full modules, `gamma*r` to its possible partial
module, and zero to the cold modules. Use constant optional rate `s-c(H)`.
Under maximal loss this maintains the state exactly. Under smaller losses,
scalar comparison keeps each preparation at or above its target, so the same
exit strategy completes no later. Thus (7) is sharp.

If `c(H)>s`, indefinite uniform readiness is impossible even with `u=0`.
For example (7) and `Q(L)>=Q_H` give the finite ready-interval upper bound

    L <= [Q(0)-Q_H]/[c(H)-s].                                 (8)

This duration bound is not asserted attained. Negative optional throughput
is a certificate of infeasibility, never an attainable performance value.

**Theorem 2 (continuous recurring frontier).** With paid initialization, the exact
maximum indefinitely guaranteed optional rate is `s-c(H)` when `c(H)<=s`;
otherwise no indefinitely ready deployment exists under the prescribed normal
load. The minimizing construction needs at most one partial module.

## 5. Closed form and boundary checks

For any segment `T_{k+1}<=H<=T_k`, where `k=0,...,n-1`, inversion of (5) gives

    c(H) = k*d + b_k
           - (b_k-d)*exp[gamma*(H-T_{k+1})].                  (9)

For `H>=T_0`, set `c(H)=0`. At the two ends of segment `k`,

    c(T_{k+1})=(k+1)*d,
    c(T_k)=k*d.

Adjacent segments therefore match continuously. In particular:

- `H=0` gives `Q_H=n*M` and `c(0)=n*d`.
- `H=T_0` gives `Q_H=0`, `c(H)=0`, and optional rate `s`.
- For `n=1`, (9) is precisely the archived proportional formula
  `c(H)=max(0,s-(s-d)*exp(gamma*H))`.
- The cost is continuous and strictly decreasing on `[0,T_0]`, with possible
  derivative changes at the endpoint times. It is not the fixed-rate staircase.
- Indefinite feasibility is equivalently
  `H>=T(min(n*M,s/gamma))`. If `s>=n*d`, every nonnegative deadline is feasible.
- At a critical positive target `c(H)=s`, paid initialization matters: from a
  cold start under the fully prescribed normal load, maximal loss implies
  `Q(t)<=s*(1-exp(-gamma*t))/gamma<s/gamma` for every finite time. Such a target
  cannot be reached in a finite cold ramp at this same capacity.

The case `gamma=0` is separate, because (9) contains division by `gamma` in
the endpoint times. Preparation is then durable and every deadline can be met
with zero recurring maintenance by paying once to initialize all modules fully;
the maximal optional rate is `s`. This assertion does not provide free
initialization or guarantee a cold start at an arbitrarily short deadline.

The main proof deliberately assumes `s>d`. It does not claim that formulas
(2), (5), or (9) extend across zero or negative stage denominators. Cases with
`s<=d` require their own accessibility and feasible-domain treatment.

## 6. Interpretation and limits

The proportional alternative now has an explicit homogeneous recurring
frontier, rather than an oracle defined over unknown partial readiness states.
The result also identifies an optimal architecture of preparation: full modules
plus at most one partial module. It is a model-internal statement about how to
allocate useful preparation, not a physical validation of proportional updates.

The proof relies on identical module sizes, releases, and proportional-loss
constants. Their equality lets a single aggregate variable dominate progress
and makes the concentrated construction exact. The heterogeneous smooth
recurring frontier remains open. The arbitrary-partial-state optimal exit
problem is not solved even here; only the best exit among states of fixed total
is needed and established.

This theorem and its exact relation to scheduling, maintenance, and standby
literature still require a primary-source novelty audit. The result must not be
promoted into a universal law of controller dependence. It does show why the
shape of the readiness cost can change while all-policy lower bounds and simple
attaining policies remain available.

## 7. Supporting verification

Run `python analysis/verify_state_dependent.py` without Python optimization.
The report `results/state-dependent-verification.json` records the tested
domains and distinguishes exact rational inequalities from floating analytic
identities. The recorded pass includes 9,440 exact aggregate-envelope checks,
192 concentrated-state equalities, 800 frontier/inverse points, 160 endpoint
continuity checks, and 96 single-module comparisons with the archived formula.
Floating comparisons use a stated `2e-12` scaled tolerance. These are small
supporting checks; the written proof, not finite enumeration or simulation,
establishes the unrestricted policy and request-time quantifiers.
