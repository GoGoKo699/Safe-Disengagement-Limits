# Pass 10: an explicit heterogeneous frontier with a common proportional loss rate

22 September 2026. This note solves the continuous preparation-allocation
problem left by the [full-state smooth-loss theorem](2026-09-22-pass9-smooth-partial.md)
for the important restricted case `g_i(p)=gamma*p` with a **common** `gamma`.
Module sizes and released capacities may differ. It proves the existence of an
optimal initial state with fully ready modules, at most one partial module, and
otherwise cold modules, and gives an exact subset computation of recurring cost.

The fractional-knapsack method and subset dynamic programming are standard
optimization tools. Publication novelty of the derived reduction, ordered
weights, and resulting concentration theorem is **not established**. This is
an ideal-model result, not a validated engineering handoff protocol.

## 1. Model, domain, and recurring-cost objective

Let `N={1,...,n}`, `n>=1`. Each module has finite size `M_i>0` and released
source capacity `a_i>=0`. The common proportional-loss coefficient is
`gamma>0`, and spare source capacity obeys the strict assumption

    s > max_i gamma*M_i.                                      (1)

This guarantees that every subfull module is individually finishable at every
post-request capacity. It avoids inaccessible-stage and zero-denominator
boundaries. No extension across (1) is asserted here.

Preparation follows the reflected dynamics on `[0,M_i]`, with admissible losses
`0<=rho_i(t)<=gamma*p_i(t)`. The simultaneous maximal feedback
`rho_i=gamma*p_i` is permitted. Normal work satisfies
`u+sum_i v_i<=s`, with nonnegative allocations. At a request optional work stops,
and each instantaneous independent cutover releases `a_i`. Receiver resources,
state sufficiency, ownership, and paid initialization have the same explicit
restrictions as the preceding notes. Positive cutover or delayed release is
not included.

Policies are deterministic, causal, measurable, bounded, and may prepare
modules in parallel or preemptively. Every request deadline must hold for every
allowed preceding and subsequent loss history. Let `F(p)` be the exact robust
exit time from arbitrary initial preparation `p`.

For finite `H>=0`, define

    C(H) = min { gamma*sum_i p_i : 0<=p_i<=M_i, F(p)<=H }.     (2)

The full-state theorem proves that a serial full-capacity schedule attains
`F(p)`, and that the ready set in (2) is compact and nonempty. Thus this
minimum exists. It also proves that, with paid initialization, the exact
maximum indefinitely guaranteed optional rate is `s-C(H)` if `C(H)<=s`;
otherwise indefinitely uniform readiness is infeasible.

We now compute (2) explicitly. It is convenient to use the transformed deadline

    X = exp(gamma*H) >= 1,
    C_X(X) = C(log(X)/gamma).                                 (3)

Affine and rational statements below concern `X`, not the physical deadline
`H` itself.

## 2. A fixed serial order produces one linear deadline inequality

Fix a permutation `pi=(pi_1,...,pi_n)` and write

    b_r = s + sum_{h<r} a_{pi_h},
    D_r = b_r-gamma*M_{pi_r} > 0.

Use the following valid schedule: serve each module in this order, at the
entire currently available capacity; unserved modules receive zero allocation.
A module initially full may deliberately wait for its turn and decay. Such
waiting is allowed for this comparison, although immediately transferring it
could only improve the optimum. A full module whose turn occurs at time zero
has a zero-duration stage.

If stage `r` starts at global time `t_{r-1}`, the unserved module has preparation
`p_{pi_r}*exp(-gamma*t_{r-1})` on the maximal-loss history. Its stage duration is

    (1/gamma)*log[
        (b_r-gamma*p_{pi_r}*exp(-gamma*t_{r-1}))/D_r ].

Set `x_r=exp(gamma*t_r)`, with `x_0=1`. The stage recurrence becomes

    x_r = (b_r*x_{r-1}-gamma*p_{pi_r})/D_r.                   (4)

It is valid over the entire preparation box. Indeed, by induction `x_r>=1`,
and

    x_r-x_{r-1}
      = gamma*(M_{pi_r}*x_{r-1}-p_{pi_r})/D_r >= 0.

Define

    alpha_r = b_r/D_r,
    A_pi = product_{r=1}^n alpha_r,
    w_r = (gamma/D_r)*product_{h>r} alpha_h.

Expanding (4) yields the affine formula

    x_n = A_pi - sum_{r=1}^n w_r*p_{pi_r}.                    (5)

Thus meeting `H` in this serial order is exactly the linear inequality

    sum_r w_r*p_{pi_r} >= A_pi-X.                            (6)

An arbitrary-partial serial optimum from pass 9 is represented among these
orders by putting its initially full modules first. Conversely, every schedule
used to derive (5) is feasible. Therefore the actual ready set is the finite
union of the box-constrained halfspaces (6), one for each permutation. This
does not assert that their union is convex.

## 3. Strictly ordered weights force concentration

The adjacent weights satisfy

    w_r/w_{r+1}
      = b_{r+1}/(b_r-gamma*M_{pi_r}) > 1.                    (7)

The inequality is strict even when `a_{pi_r}=0`, since `gamma*M_{pi_r}>0`.
Earlier positions therefore buy more deadline improvement per unit of initial
preparation than later positions in this *fixed order*.

Minimizing `sum_i p_i` subject to (6) and `0<=p_i<=M_i` is the fractional-
knapsack problem with strictly decreasing efficiencies `w_1>...>w_n`.
For completeness, if an earlier position `j` is not full and a later position
`k` is positive, decrease the later preparation by a sufficiently small `eta`
and increase the earlier preparation by `eta*w_k/w_j`. The weighted sum stays
unchanged, both bounds remain satisfied, and total preparation strictly
decreases. Hence no minimum can have this configuration.

If `A_pi<=X`, the minimum is the all-cold state. Otherwise the minimizing
preparation fills an initial prefix to capacity, then at most one additional
module partially, leaving the remaining suffix cold. Feasibility is never an
issue for `X>=1`: putting every module at `M_i` makes every stage duration zero,
so (5) gives `sum_r w_r*M_{pi_r}=A_pi-1`.

There are finitely many permutations. Taking the best of their attained
linear-program minima proves the following structural result.

**Theorem 1 (heterogeneous concentration with common proportional loss).**
Under (1), some minimizing state in (2) consists of a fully ready set `S`, at
most one partial module `i` outside it, and all remaining modules cold. It
admits a deadline-feasible schedule that transfers `S` immediately, prepares
`i` first if needed, and then completes the cold suffix serially.

This is an existence theorem about a globally cost-minimizing state and a
matching schedule. It does not say that the partially prepared module must be
first in the *optimal exit schedule of every concentrated state*. Section 7
gives an exact counterexample to that stronger, false statement.

## 4. Ready/cold subset oracle in exponential coordinates

For `S subset N`, let

    b(S) = s + sum_{j in S} a_j.

Starting with `S` fully ready and all other modules cold, transfer `S` at time
zero. Let `F_cold(S)` be the exact remaining exit time and define

    P(S) = exp(gamma*F_cold(S)).

The serial theorem gives

    P(N) = 1,
    P(S) = min_{i not in S}
        [ b(S)/(b(S)-gamma*M_i) * P(S union {i}) ].           (8)

This is a minimum over the full post-request allocation policy class, because
the preceding theorem supplies a serial optimum. Every denominator is positive
under (1), and all values are finite. Storing a minimizing successor also gives
an attaining cold-tail order.

## 5. Explicit recurring frontier without continuous optimization

Choose a ready set `S` and a module `i` outside it. Put

    b = b(S),
    P_tail = P(S union {i}).

Consider initial preparation `M_j` on `S`, `q` on `i`, and zero elsewhere.
Transferring `S` immediately, processing `i` first, and using an optimal cold
tail has exponential completion factor

    [(b-gamma*q)/(b-gamma*M_i)] * P_tail.                     (9)

This is the exact duration of the displayed feasible strategy, not necessarily
the optimal exit time of that particular initial vector.

The strategy can meet `X` with some `0<=q<=M_i` if and only if
`X>=P_tail`. When eligible, its smallest required partial preparation is

    q_{S,i}(X)
       = max{0, b-(b-gamma*M_i)*X/P_tail}/gamma.              (10)

Eligibility guarantees `q_{S,i}<=M_i`. Equality corresponds to treating `i` as
another fully ready module; zero corresponds to starting a cold module first.
Both endpoint cases are legitimate.

Define the candidate maintenance cost

    K_{S,i}(X)
       = gamma*sum_{j in S} M_j
         + max{0, b(S)-(b(S)-gamma*M_i)*X/P(S union {i})},
       for X>=P(S union {i}).                               (11)

Then the explicit frontier is

    C_X(X) = min {
        gamma*sum_{j in N} M_j,
        K_{S,i}(X) for S subset N, i not in S,
                       X>=P(S union {i})
    }.                                                      (12)

**Theorem 2 (explicit heterogeneous common-loss frontier).** Equation (12)
equals the continuous all-state minimum (2). It attains the exact recurring
maintenance cost and gives a minimizing preparation vector and a feasible
request-time schedule.

**Proof.** Every candidate in (12) comes with the feasible construction (9),
so its cost cannot be below the minimum in (2). Conversely, Theorem 1 supplies
a global minimizer with a full prefix, at most one partial module, and a cold
suffix in some feasible order. If all modules are full, the explicit all-ready
candidate represents it. Otherwise choose its ready prefix `S` and its next
module `i`, allowing `q=0`. Replacing that order's cold suffix by the optimal
tail in (8) cannot worsen the deadline. Reducing `q` to (10) preserves
feasibility and cannot increase cost. Thus some candidate in (12) costs no more
than the minimum in (2). The two inequalities prove equality and attainment.

The proof does not assume that an arbitrary concentrated vector should process
its partial module first. It selects a concentrated optimizer from the
fixed-order linear programs, and only then improves its cold suffix.

## 6. All-request-time performance, computation, and endpoints

Write `C=C_X(exp(gamma*H))`. On the allowed maximal-loss normal history, any
uniformly ready policy obeys

    Q' <= s-u-gamma*Q <= s-u-C,
    Q=sum_i p_i.

Therefore every normal duration `T>0` satisfies

    integral_0^T u(t)dt <= (s-C)*T + Q(0)-Q(T).               (13)

Bounded `Q` gives the long-run upper bound `s-C`, and when `C>s` it rules out
indefinite readiness even with zero optional work. If `C<=s`, initialize an
attaining vector from (12), allocate `v_i=gamma*p_i^*` during normal operation,
and set `u=s-C`. It is stationary under maximal loss and remains componentwise
at least the target under smaller allowed loss. Every request then meets `H`.
This proves exact attainment of the robust optional rate. Initialization is
paid; cold-start reachability under the same normal load is not asserted.

The computation has two finite stages:

1. Evaluate (8) over all subsets in decreasing size.
2. At a given `X`, examine (11) for every pair `(S,i)` and the all-ready case.

With subset capacity/size sums available, this uses `O(n*2^n)` arithmetic
operations and comparisons per query, including the one-time table construction,
and `O(2^n)` storage. Reusing the table for later deadlines avoids rebuilding it.
These are arithmetic-operation counts, not a bit-complexity or polynomial-time
claim. It is not necessary to enumerate `n!` orders in the implementation.

If `s`, `gamma`, `M_i`, `a_i`, and `X` are rational, all table entries,
eligibility tests, candidate costs, and attaining preparation amounts use exact
rational arithmetic. A rational physical `H` need not make
`X=exp(gamma*H)` rational. Such inputs require appropriately controlled
exponential evaluation or a symbolic/certified representation; floating
comparisons must not be described as exact rational deadline decisions.

The endpoint and shape checks are:

- `X=1`, equivalently `H=0`, requires all modules fully ready, so
  `C_X(1)=gamma*sum_i M_i`.
- `C_X(X)=0` exactly when `X>=P(empty)`, since positive `gamma` makes zero
  maintenance possible only at the all-cold state.
- `C_X` is continuous, nonincreasing, and piecewise affine on `X>=1`. For each
  permutation, the fractional-knapsack value has those properties and finitely
  many pieces; taking the minimum over finitely many such functions preserves
  continuity and piecewise affinity. With rational model parameters, its
  breakpoints in `X` are rational. This does **not** establish convexity: a
  minimum of convex value functions need not be convex.
- In physical `H`, the cost is continuous and piecewise exponential, generally
  with kinks, rather than piecewise affine in time.
- For one module, (12) gives
  `C(H)=max{0,s-(s-gamma*M)*exp(gamma*H)}`, recovering the archived result.
- For equal `M_i=M` and `a_i=a`, it reduces to the
  [homogeneous proportional frontier](2026-09-22-proportional-readiness.md).

## 7. A concentrated state's partial module need not go first

Take `gamma=1/10`, `s=1`, and the following initially prepared modules:

| Module | M | a | Initial preparation |
|---|---:|---:|---:|
| A | 1 | 1 | `1/10` |
| B | `1/10` | 100 | 0 |

The strict rate condition (1) holds. This already has the concentrated shape:
one partial module and one cold module. Yet preparing the partial A first gives
exponential completion factor

    X_AB = (11/10)*(200/199) = 220/199.

Preparing cold B first gives

    x_B = 100/99,
    X_BA = [101*x_B-(1/10)*(1/10)]/(101-1/10)
         = 1009901/998910 < 220/199.

Since logarithm is increasing, B first has strictly smaller exit time. Its large
capacity release outweighs the decay of A while waiting. Thus (9) must be read
as a candidate strategy whose global search is exact by the concentration
proof, not as a formula for the optimal exit of every already concentrated
state. The full-state scheduling recurrence from pass 9 remains the correct
oracle for a prescribed arbitrary initial vector.

## 8. Assumption-to-conclusion map and research status

| Assumption | What uses it |
|---|---|
| Common `gamma>0` | A single global transform `x=exp(gamma*t)` makes the fixed-order deadline affine in initial preparation and makes upkeep proportional to its unweighted sum. |
| `s>max_i gamma*M_i` | Every serial denominator is positive across the whole preparation box; no inaccessible-rate boundary needs separate cases. |
| `a_i>=0`, instantaneous independent cutover | The arbitrary-partial serial theorem and subset capacity accounting apply. Delayed release is a different scheduling problem. |
| Full product loss uncertainty | Simultaneous maximal proportional loss supplies the common lower-bound history; scalar comparison supplies robustness under smaller losses. |
| Paid initialization | A cost-minimizing state can be used at the start of the guaranteed deployment without a false cold-start claim. |

The result closes the continuous-allocation gap for heterogeneous modules with
a common proportional coefficient. It does not solve unequal-`gamma_i`
maintenance, inaccessible initial-rate regimes, positive-latency handoff,
state-dependent update delivery, or constrained startup. A physically justified
proportional robust envelope and theorem-level novelty comparison remain
unresolved. The next scientific assessment must compare the all-policy serial
reduction and concentration result with prior work, rather than claiming novelty
for fractional knapsack, exponentiation of a scalar flow, or subset dynamic
programming alone.

## 9. Exact nonlinear counterexample to concentration

The concentration theorem does not extend to every smooth monotone loss law,
even when the modules and their loss functions are identical. The following
certificate uses rational inequalities only. It establishes a strict separation
from every concentrated state; it does not compute the exact optimal exit time
or the exact minimum upkeep in the nonlinear model.

### 9.1 Alternative model and a feasible two-partial state

Take two identical modules with

    M_1=M_2=1,  a_1=a_2=1/100,  s=10,
    g_1(p)=g_2(p)=p^2,  H=23/500.

The allowed loss is `0<=rho_i(t)<=p_i(t)^2`, with the same instantaneous
independent transfer model as above. The function `p^2` is nonnegative,
nondecreasing, and Lipschitz with constant two on `[0,1]`, and vanishes at zero.
Both releases are strictly positive and `s>max_i g_i(M_i)=1`. Thus neither a
zero release nor an inaccessible initial capacity causes the separation.

Start from

    p_1=p_2=4/5.

The stationary target's total maintenance allocation is

    g_1(4/5)+g_2(4/5)=32/25.                                (14)

It is robustly deadline feasible. Prepare module 1 first at full rate ten.
Throughout its preparation, loss is at most one, so its net growth is at least
nine. It therefore finishes in time at most

    t_1 <= (1/5)/9 = 1/45.

While waiting without allocation, module 2 cannot increase above `4/5`; its
loss is consequently at most `16/25`. At the first cutover it retains at least

    p_2(t_1) >= 4/5-(16/25)*(1/45) = 884/1125.

The available preparation rate is now `1001/100`. Giving it all to module 2
yields net growth at least `901/100`, because loss is still at most one. Its
remaining deficit is at most `241/1125`, giving

    t_2 <= (241/1125)/(901/100) = 964/40545.

Hence this serial policy finishes for every allowed loss history within

    t_1+t_2 <= 373/8109 < 23/500,
    23/500-373/8109 = 7/4054500 > 0.                          (15)

These are upper bounds; equality with the true quadratic-loss traversal times
is not asserted. Allocating `16/25` to each module during normal operation
holds the target under maximal loss and prevents either coordinate from
falling below it under smaller loss. More preparation cannot harm robust exit
in this smooth independent model. With paid initialization, this is therefore
an all-request-time feasible policy of recurring upkeep `32/25<s`.

### 9.2 Every concentrated state is strictly more expensive or infeasible

A concentrated state has fully ready modules, at most one partial module,
and otherwise cold modules. Consider its possible forms. The following lower
bounds allow arbitrary post-request schedules, not only a particular serial
order.

**No full module.** Its initial total preparation is at most one. Let
`Z` be the number of transferred modules plus the total unfinished preparation.
Transfers leave `Z` unchanged, and nonnegative loss gives
`Z'<=sum_i v_i` almost everywhere. Completion requires `Z=2`, so at least one
additional unit of useful preparation must be produced. Until the final
transfer, at most one module's reservation has been released, so preparation
capacity is at most `1001/100`. But the entire deadline permits allocated work
at most

    (1001/100)*(23/500)=23023/50000 < 1.

Such a state is infeasible, regardless of how preparation is allocated.

**One full module and another prepared to `r`.** The latter module needs at
least `1-r` additional allocated work even if all subsequent loss were zero.
The same capacity bound gives the necessary condition

    r >= 1-(1001/100)*(23/500) = 26977/50000.

Its maximal-loss stationary maintenance cost is therefore at least

    1+r^2 >= 1+(26977/50000)^2 > 32/25,

with the exact strict gap

    1+(26977/50000)^2-32/25 = 27758529/2500000000 > 0.        (16)

Delaying the initially full module's transfer cannot evade this bound: it
cannot raise the available preparation capacity above `1001/100` before the
last transfer. The necessary work for the other coordinate remains `1-r`.

**Both modules full.** Their maintenance cost is two, also strictly larger
than `32/25`.

Thus every concentrated deadline-ready state has total loss strictly greater
than the feasible two-partial state's `32/25`. The full-state smooth-loss
theorem guarantees an attained minimum over ready states; no such minimum can
be concentrated in this example. Even without needing its exact value, (14)–(16)
disprove the existence of a concentrated optimizer for this nonlinear loss law.

### 9.3 Scientific scope

Serial optimality from arbitrary partial states survives here; what fails is
the concentration of optimal **initial readiness** into full modules plus one
partial module. The loss law is identical across both modules. The separation
therefore identifies proportionality, not merely equal module parameters or
smoothness, as a substantive restriction in Theorem 1.

This is not a counterexample for unequal proportional coefficients
`gamma_i`; that is a different unresolved extension. Nor is it an engineering
validation or publication-novelty claim. A separately labeled exact rational
fixture can verify the displayed inequalities without substituting finite
checks for the all-policy work lower bounds.
