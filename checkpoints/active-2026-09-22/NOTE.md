# The recurring cost of preserving a live handover

**S1 / Falling — 22 September 2026**

**Status:** a proved result for an explicitly restricted mathematical model, with
finite checks. Publication novelty and applicability to a concrete controller
architecture are **not established**. This does not supersede the passive
commitment benchmark. The present model introduces active reconciliation and
capacity released by completed handovers; it is not a theorem about the previous
fixed-demand kernel model.

## 1. Question and accounting

A primary controller provides a fixed prescribed normal-mode service to `n`
independent modules. An independently provisioned fallback can provide their
essential service, but it needs current handover state. Preparing that state
competes with discretionary work at the primary. Ordinary operation changes
state, so preparation may have to be refreshed. After a removal request, the
primary cooperates while modules transfer one by one. Each completed transfer
frees primary capacity for remaining transfers. After the deadline, no module
may depend on the primary.

We ask for the maximum indefinitely sustainable discretionary throughput while
preserving a worst-case handover deadline **at every possible request time**.
The request is counterfactual along an otherwise uninterrupted normal deployment;
we do not model repeated shutdown/restart cycles.

This is a service-state handover abstraction, not an instruction to copy the
same unwanted AI onto another machine. The fallback algorithm, its independent
resources and its ability to supply the required essential service are assumed
available. What is prepared is the operational state/configuration needed for
handover. A deployment must verify that this is a sufficient interface. The
mathematics does not prove that copying data guarantees safe control.

### 1.1 Parameters

- `n >= 1`: number of identical, independently switchable service modules.
- `a > 0`: primary resource rate consumed by one module in normal mode and
  throughout its unfinished handover.
- `P = n*a + s`, `s >= 0`: primary capacity and spare capacity after the fixed
  normal service load.
- `M > 0`: useful reconciliation work needed for one fully ready module.
- `d >= 0`: per-module maximum invalidation/recopy rate while primary-controlled.
- `H >= 0`: finite cooperative removal deadline.

Rates are measured in a common bottleneck-resource equivalent. An example is a
source-local communication interface shared between ordinary stateful traffic
and reconciliation. Receiver capacity is a **separate pre-provisioned resource**;
it is not silently included in `P`. A claim about minimum *total* infrastructure
cost would have to optimize receiver resources too, which this note does not.

All `n` modules remain in the prescribed primary normal mode before a request.
The fallback supplies an essential-service floor, not necessarily the full
normal-mode quality. Moving modules permanently to fallback before a request is
therefore a different quality-of-service policy, outside this theorem. There is
also an explicitly optional throughput `u(t)` that can stop immediately at a
request without creating unmodeled continuing obligations.

### 1.2 What must not be hidden

Independent fallback operation includes whatever sensing, actuation, state,
energy and communications essential service needs. Once handover finishes, it
may not ask the primary for missing pages, schedules, interpretations or control
instructions. Handed-over modules release `a` units of the primary bottleneck
without increasing the primary load of other modules.

Modules are independent and identical. There are no global consistency barriers,
shared-primary services that remain needed after all modules transfer, finite
receiver bottlenecks, stochastic failures during the grace period, or positive
cutover latencies. A ready module transfers instantaneously. Essential services
cannot be paused or throttled to finish copying. These are substantive model
restrictions, not claims about all implementations.

## 2. Preparation dynamics and uncertainty

For each module, useful preparation is `p_i(t) in [0,M]`:

- `p_i=0`: no useful preparation (cold).
- `0<p_i<M`: partially prepared.
- `p_i=M`: fully current and immediately switchable (hot/ready).

Let `v_i(t)>=0` be allocated reconciliation work. Actual invalidation may vary as
`rho_i(t) in [0,d]`. The bounded reflected fluid model is

    p_i' = max(v_i-rho_i, 0)          at p_i=0,
    p_i' = v_i-rho_i                 for 0<p_i<M,
    p_i' = min(v_i-rho_i, 0)          at p_i=M.

State trajectories are interpreted as bounded absolutely continuous reflected
solutions with measurable bounded allocations. Values on switching instants are
irrelevant to almost-everywhere inequalities. Policies may be adaptive,
time-varying, preemptive and parallel, and may move preparation between modules.

The requested guarantee is robust for every allowed invalidation history. For
lower bounds the adversary may choose `rho_i=d` at all times. For upper bounds a
policy that works at this maximum rate also works for smaller actual rates.

### 2.1 Load-bearing modeling choice

When a module has *any* useful preparation, worst-case invalidation may consume
it at rate `d`, irrespective of the amount already prepared. This represents a
worst-case overwrite/recopy workload targeting the currently useful portion.
It is not a claim that all application writes have this pattern, nor that the
invalidation rate must be independent of prepared size in typical workloads.
The fluid constant-rate migration expression has precedent (see LITERATURE.md),
but extending it to every possible partial preparation is an explicit robust
model choice here.

If updates are spatially restricted, append-only, compressible, proportional to
prepared size, or served by independent logs, the model must change. Section 8
solves a smooth proportional-invalidation alternative to show exactly which
feature of the conclusion does not survive. We do not infer this dynamics from
human skill loss or the fiction.

During normal operation,

    u(t) + sum_i v_i(t) <= s.

Let `Q(t)=sum_i p_i(t)` and `m(t)=#{i:p_i(t)>0}`. Under maximum invalidation,

    Q'(t) <= sum_i v_i(t) - d*m(t).                 (1)

At a positive interior state the contribution is equality. At the upper boundary
it is at most `v_i-d`; at zero it is at most `v_i`. Thus (1) also holds with
reflection and wasted work.

## 3. Exact exit time with some modules already ready

At a request, optional work stops. Transfer every fully ready module immediately.
Suppose `k` modules were ready and the other `n-k` were cold. Let `T_k` denote the
optimal worst-case time to finish removing the primary.

**Proposition 1.**

    T_n = 0.

For `k<n`,

    T_k = infinity,                          if s+k*a <= d,
    T_k = M * sum_{j=k}^{n-1} 1/(s+j*a-d),   if s+k*a > d.       (2)

This is an optimum over every feasible parallel/preemptive/adaptive handover
schedule, not an assumption that only serial schedules are allowed.

### 3.1 Attaining policy

After transferring `k` ready modules, primary service still consumes `(n-k)*a`.
All remaining capacity `s+k*a` is allocated to one cold module. Under maximum
invalidation its net progress is `s+k*a-d`, so it reaches `M` in
`M/(s+k*a-d)` time. Transfer it, freeing another `a`, and repeat. Other cold
modules remain at zero without maintenance. The elapsed time is (2). For actual
invalidation below `d`, each stage finishes no later.

### 3.2 Why arbitrary parallel preparation cannot beat (2)

Assume `b:=s+k*a>d` and write `r=n-k` for the initially cold modules. During
handover let `J(t)` be the number of these `r` modules already transferred, and
let

    Z(t) = M*J(t) + sum_{unfinished i} p_i(t).

We can transfer ready modules immediately without loss of optimality: this
releases capacity and removes future reconciliation work. Such a transfer changes
`J` but does not change `Z`, so `Z` is absolutely continuous. We have

    J(t) <= floor(Z(t)/M).

At almost every time,

    Z'(t) <= b + a*J(t) - d.                       (3)

To see (3), when some unfinished `p_i>0`, its invalidation alone subtracts at
least `d` from useful aggregate work; additional positive preparations only add
more losses. When all unfinished `p_i=0`, either no preparation grows (in which
case `Z'=0 <= b+aJ-d`) or at least one allocation exceeds `d`, again giving the
bound. Allocations to zero states that do not exceed `d` cannot produce progress.

Consequently,

    Z' <= b + a*floor(Z/M) - d.

Define the continuous, increasing, piecewise-linear potential on `[0,r*M]`

    Phi(z) = integral_0^z dy / (b+a*floor(y/M)-d).

The denominator is positive. Its values at finitely many interval boundaries
can be chosen arbitrarily. The chain rule gives `(Phi(Z(t)))'<=1` almost
everywhere; when `Z` remains at a boundary its derivative is zero. This also
handles schedules that lose preparation and make `Z` decrease. Therefore

    finish_time >= Phi(r*M)-Phi(0)
                = M * sum_{j=0}^{r-1} 1/(b+j*a-d)
                = T_k.

This proves the minimax lower bound. If `b<=d`, every allocation to each initially
cold module is at most `d`; under maximum invalidation all remain at zero until
one transfers, and none can transfer. Thus the infinite case is exact.

## 4. The exact recurring readiness cost

For finite deadline `H`, define

    k_H = min{k in {0,...,n}: T_k <= H}.             (4)

The set is nonempty because `T_n=0`. `T_k` is strictly decreasing wherever finite
and `k<n`.

**Theorem 2.** Any normal-operation policy that preserves an `H`-deadline exit
at every possible request time satisfies, along the allowed maximum-invalidation
history, for every duration `t>0`,

    integral_0^t u(r) dr <= (s-d*k_H)*t + Q(0)-Q(t)
                         <= (s-d*k_H)*t + n*M.      (5)

In particular, every robustly guaranteed upper long-run throughput obeys

    limsup_{t->infinity} (1/t) integral_0^t u(r)dr <= s-d*k_H.    (6)

If `d*k_H<=s`, the bound is attained, from suitable initialized preparation, by
keeping exactly `k_H` modules fully ready at maintenance rate `d` each, the rest
cold, and setting

    u(t)=s-d*k_H.                                    (7)

If `d*k_H>s`, no indefinitely sustainable policy can preserve the uniform exit
guarantee for this prescribed normal-mode load and these resources. The negative
right side is **not** a physically attainable negative throughput; it certifies
infeasibility.

### 4.1 Necessary number of nonzero preparations

Consider any request state with exactly `m` positive preparations. Give the
transition planner the gratuitous advantage of turning all these into fully
ready modules and transferring them instantly. This can only make exit easier:
there is less reconciliation left, more primary capacity, and no coupling
penalty by the independence assumptions. All other modules were cold.

Even this optimistic state requires `T_m` time. Hence `H`-readiness implies

    m >= k_H.                                       (8)

This is only a necessary condition on a general partial state, not a claim that
any `k_H` tiny preparations suffice. It is enough for the lower bound.

### 4.2 Averaging proof valid for rotating and bursty preparation

For a uniform guarantee, (8) must hold at every request time along nominal
operation. Combine (1), (8) and the normal resource budget:

    Q' <= sum_i v_i-d*m <= s-u-d*k_H.

Integrate and use `0<=Q<=n*M` to obtain (5) and (6). Thus neither a changing
identity of the prepared modules, partial snapshots, bursty refreshes, nor
arbitrarily preemptive sharing improves the minimax average bound.

### 4.3 Attainment and startup accounting

Initialize `k_H` modules with `p_i=M`. Allocate `v_i=d` to each of them during
normal operation; allocate zero to the other cold modules. The initialized
modules remain ready for every allowed invalidation history. The normal budget
holds iff `d*k_H<=s`, with optional rate (7). At any request, Proposition 1
finishes exit within `H`.

The initial `k_H*M` useful preparation is **not free**. It must be established
before the guaranteed normal deployment, for example during a deployment ramp
when the prescribed main workload is not yet fully running. Under a fully loaded
normal regime, initialization may not itself be possible, particularly at budget
equality. We do not claim the tight guarantee holds from a cold time-zero state.
A theorem with no initialization allowance must include that state constraint.

This is a minimax performance theorem: on quieter invalidation histories,
adaptive policies may achieve greater actual throughput. The upper bound is
forced by one allowed history, not asserted for every benign history.

## 5. Finite-time consequence

Preparation can temporarily mask an unsustainable maintenance budget. Equation
(5) quantifies how long. If `d*k_H>s` and `u>=0`, any exit-ready normal deployment
must have duration

    t <= n*M/(d*k_H-s).

More sharply, if `u>=u0` pointwise and `u0+d*k_H>s`, replace the denominator by
`u0+d*k_H-s`. Initial useful preparation `Q(0)` may replace `n*M`.

This is an upper bound, not necessarily an attainable deployment duration.
It separates an individual feasible exit and a temporarily ready deployment
from indefinitely maintaining the ability to exit at arbitrary times.

## 6. Exact three-module example

Use abstract resource/time units, not measurements of an application:

    n=3, a=3, P=10, s=1, M=3, d=3/5.

The fixed normal service consumes 9 capacity units. Optional work and readiness
maintenance compete for the remaining 1 unit.

| Initially fully ready k | Exact T_k | Decimal |
|---|---:|---:|
| 0 | 4815/544 | 8.851102941176471 |
| 1 | 735/544 | 1.3511029411764706 |
| 2 | 15/32 | 0.46875 |
| 3 | 0 | 0 |

| Deadline H | k_H | Required recurring maintenance | Indefinite normal deployment |
|---|---:|---:|---|
| 9 | 0 | 0 | Feasible; optional rate 1 |
| 2 | 1 | 3/5 | Feasible; optional rate 2/5 |
| 1 | 2 | 6/5 | Infeasible with spare capacity 1 |
| 0 | 3 | 9/5 | Infeasible with spare capacity 1 |

For `H=2`, keep one module ready. On request it transfers instantly, increasing
reconciliation capacity from 1 to 4. Finish the next in `3/(4-3/5)=15/17` time,
then the last in `3/(7-3/5)=15/32`, totaling `735/544`.

The optional rate `2/5` is not the total service throughput: the prescribed
normal-service resource load of 9 is still delivered. For `H=1`, a highly
prepared initial state may permit individual exits and a finite deployment;
what fails is indefinite uniform readiness under the fixed capacity.

## 7. Granularity as an idealized corollary

This section changes the architecture, not merely the notation. Suppose a
fixed total normal load `L`, state-reconciliation work `W`, and maximum update
budget `R` can actually be divided into `n` independent modules:

    a=L/n, M=W/n, d=R/n, P=L+s.

Cold exit has finite worst-case time iff `s>R/n`. For finer partitions, the
first completed handover releases capacity sooner, while less update loss must
be paid simultaneously. Defining `kappa=W/L`, for `k/n -> f in [0,1]` as
`n->infinity` and `s>0`, the exact sum is a Riemann sum and gives

    T_k -> kappa * log((s+L)/(s+f*L)).

Thus for fixed deadline `H`, the ideal minimum ready fraction tends to

    f_H = max(0, ((s+L)*exp(-H/kappa)-s)/L),

and the recurring upkeep tends to `R*f_H`. Indefinite feasibility still requires
that upkeep not exceed `s`. This is not a result about zero-cost arbitrary
software partitioning. Shared state can prevent independent cutovers. Moreover,
if each handover unit has fixed additional preparation overhead `sigma>0`, then
`M=W/n+sigma` and the cold exit time diverges as `n` grows. The zero-overhead
limit must not be advertised as an unbounded practical gain.

## 8. Assumption stress test: a smooth alternative removes the staircase

For a single module, replace fixed-rate invalidation by proportional
invalidation of useful preparation:

    p'=v-gamma*p, clipped to [0,M], gamma=d/M.

Take `s>d>0`. The primary remains available during handover, and allocates
`v=s` after a request. The fastest transition from initial `p` is

    T(p) = (1/gamma) * log((s-gamma*p)/(s-d)).

Therefore meeting the deadline requires

    p >= p_H := max(0, [s-(s-d)*exp(gamma*H)]/gamma).

The exact minimum recurring upkeep and maximum optional throughput are

    c(H) = gamma*p_H = max(0, s-(s-d)*exp(gamma*H)),
    u_*(H) = s-c(H).

Proof of the all-history bound: normal readiness requires `p(t)>=p_H`, and the
reflected dynamics give `p'<=v-gamma*p<=s-u-gamma*p_H`. Integrate, use bounded
`p`, and divide by time. A constant `p=p_H`, `v=gamma*p_H` attains the bound
from that initialized state. Exit dynamics with maximal `v` give the displayed
transition time by explicit solution of the linear differential equation.

Unlike Theorem 2, this upkeep depends **continuously** on `H`. For example,
`M=1,d=1/2,s=1`, and `H=log(2)` give proportional upkeep `1-1/sqrt(2)`, about
0.2929. In the fixed-rate model at the same `H<2`, a positive preparation must
be maintained and the minimum upkeep is `1/2`.

This is a mathematical alternative, not a fitted model of average write traffic.
It shows the staircase is not a universal law of controller dependence. The
broader issue of a nonzero recurring cost survives, but its shape is controlled
by the update/invalidation model. With `d=0`, preparation is durable and there
is no recurring maintenance cost at all; finite initialization may suffice.

## 9. What is and is not new

The following are established ideas and are **not claimed here**: hot standby,
ongoing state replication, pre-copy bandwidth-versus-write-rate limitations,
resource contention in concurrent migrations, advantages of appropriate
sequential/fine-grained scheduling, and the distinction between moving execution
and removing residual dependence. See LITERATURE.md for directly inspected
primary sources and specific overlaps.

The candidate residual contribution is the combination of:

1. uniform readiness at every possible removal time rather than a fixed request;
2. one shared primary budget for normal optional performance, continuous
   readiness work and post-request conversion;
3. capacity released by each completed handover;
4. an exact all-policy lower bound, including rotating/partial preparations,
   matched by a simple initialized policy.

We have not located this exact theorem in the inspected sources. That is not
proof of novelty: the model is narrow, its ingredients are familiar, and a
specialist may recognize a reduction to prior scheduling/maintenance results.
The quantitative frontier, not the terminology, would need to survive review.
The proof is not independently peer-reviewed, machine-verified or an empirical
safety certificate. No application or venue acceptance is asserted.

## 10. Verification and next decision gates

`verify.py` uses only the Python standard library. Rational curve/construction
checks use `fractions.Fraction`; local inequalities use exact integer-scaled
grids. Only the smooth-model analytic identities use floating arithmetic with
explicit tolerances. RESULTS.json records actual counts.

The script checks both local inequalities in the proof, boundary reflection,
exact sequential stage times, deadline thresholds, feasible attaining maintenance
policies and the smooth countermodel formula. It does **not** enumerate all
continuous-time schedules or prove the theorem by simulation. The analytic
arguments above carry those quantifiers.

Before treating this as a paper, the next decisive work is to establish a
specific engineering interface for independent fallback and a defensible update
uncertainty set, check the exact frontier against replication/scheduling theory,
and test whether heterogeneity or cross-module coupling produces a stronger
structural statement rather than only more parameters. A small local verifier
is enough for the present work; no large cloud simulations or trained controller
are needed.
