# Heterogeneous post-request scheduling: exact serial dominance

Date: 22 September 2026. This note extends the fixed-rate active model outside
the immutable checkpoint. It does not establish publication novelty or a
physical application. The proof is an internal analytic result; finite checks
are supporting checks, not its policy-class justification.

## 1. Question, policy class, and value

There are finitely many modules, indexed by `N`. Module `i` has preparation size
`M_i>0`, released source capacity `a_i>=0`, and maximum invalidation rate
`d_i>=0`. All parameters are finite. The original model's strict `a_i>0` is
included. Spare source capacity is `s>=0`. Receiver resources and essential
service are accounted for exactly as in the active checkpoint: module cutovers
are independent and instantaneous, and the fallback is independently provisioned.

At request time, a subset `S` is fully ready and the complement is cold. Transfer
`S` immediately. For a completed set `C`, available preparation capacity is

    b(C) = s + sum_{i in C} a_i.

Every unfinished module follows the checkpoint's reflected preparation dynamics
on `[0,M_i]`, with its own `d_i`. Policies may use arbitrary measurable bounded
allocations, parallel work, preemption, idling, and history-dependent decisions.
They must obey `sum v_i <= b(C)` at every time except irrelevant switching
instants. Actual losses may simultaneously equal `d_i` for every unfinished
module. A policy must meet its deadline for every allowed loss history.

Let `tau(S)` be the infimum of guaranteed completion deadlines from this
ready/cold state. This statement does not cover arbitrary partially prepared
initial states. The cold-state restriction is used explicitly in the proof.

For a permutation `pi` of `N\S`, define

    L(pi;S) = sum_{r=1}^{|N\S|}
        M_{pi_r} / (s + sum_{j in S} a_j
                        + sum_{h<r} a_{pi_h} - d_{pi_r}).

A permutation is admissible only when every denominator is strictly positive;
otherwise assign it value infinity. The empty permutation has value zero.

**Theorem 1 (heterogeneous serial dominance).**

    tau(S) = min_pi L(pi;S).

If the minimum is finite, an attaining robust policy processes one cold module
at a time, using all available capacity, in a minimizing order. Moreover, on
the maximum-loss history, every finite feasible schedule takes at least the
serial time of its own completion order, with simultaneous completions ordered
arbitrarily. Parallelism and preemption cannot improve the optimum.

There are finitely many permutations, so a finite minimum is attained. No
limiting-policy or strict-deadline gap is hidden in the expression.

## 2. Weighted-potential proof

It suffices for the lower bound to choose the admissible deterministic history
`rho_i(t)=d_i` for all unfinished modules. Follow any finite completing policy on
this history. Capacity `b` never decreases, since `a_i>=0`.

If current `b=0`, cold preparation cannot grow. Thus a finite schedule with any
cold work requires positive capacity. On every open interval between cutovers
with `b>0`, define

    W_b(p) = sum_{unfinished i: d_i<b} p_i/(b-d_i).

Any unfinished module with `d_i>=b` has `p_i=0`: it started cold and at all earlier
times its allocation was at most the current capacity, which is at most `d_i`.
The reflected dynamics therefore never allowed it to leave zero.

For an included module and any feasible `0<=v_i<=b`, the reflected derivative
satisfies

    p_i'/(b-d_i) <= v_i/b.                         (1)

At an interior point, (1) follows from `d_i*v_i<=d_i*b`. At zero, if `v_i<=d_i`
its left side is zero; otherwise the same algebra applies. At the upper boundary
the derivative is `min(v_i-d_i,0)`, and (1) remains true. Summing gives

    W_b' <= (sum_i v_i)/b <= 1                    (2)

almost everywhere between cutovers. This includes intervals of lost progress,
wasted work, and arbitrary switching of the allocation.

When module `i` cuts over, it has `p_i=M_i`, and necessarily `d_i<b`: it could
never have reached positive preparation at any prior capacity otherwise.
Removing its term drops the potential by `M_i/(b-d_i)`. Increasing capacity from
`b` to `b+a_i` weakly decreases every remaining included coefficient. Newly
included modules satisfying `b<=d_j<b+a_i` have zero preparation, by the preceding
cold-state observation. Thus the total downward jump is at least

    M_i/(b-d_i).                                  (3)

When several modules complete simultaneously, linearize their cutovers in any
order at that same instant. The same jump inequality holds for each, using the
capacity after the preceding zero-time cutovers. This produces exactly the
denominators in `L(pi;S)`.

Initially all unfinished preparation is zero, and after the final cutover there
are no unfinished modules. Hence the potential starts and ends at zero.
Integrate (2) over all intervals and sum (3) over the finitely many cutovers:

    completion time >= sum of potential drops >= L(pi;S).

This proves the all-policy lower bound. It also proves that if every serial
order is inadmissible then no finite feasible schedule exists.

For the upper bound, select an admissible order and allocate all current
capacity to its next module. Under maximum loss its net progress is exactly
`b-d_i>0`, so the stage takes `M_i/(b-d_i)`. Smaller actual losses cannot delay
completion under the same full-capacity rule. Transfer immediately and continue.
This policy attains `L(pi;S)` robustly, proving the theorem.

The proof fails as written if capacity can decrease, if partial initial
preparation is granted for modules with `d_i>=b`, or if the loss law is changed.
It makes no claim about those altered problems.

## 3. Exact subset dynamic program

The theorem gives a finite explicit computation, rather than an expression in
terms of an uncharacterized continuous-time optimum. Write `F(C)` for the
remaining time when precisely `C` have transferred and all others are cold:

    F(N) = 0,
    F(C) = min_{i not in C: b(C)>d_i}
               [M_i/(b(C)-d_i) + F(C union {i})].  (4)

An empty minimum is infinity. Evaluate subsets in decreasing size. Then
`tau(S)=F(S)`. With precomputed subset capacity sums, (4) uses `O(n*2^n)`
arithmetic operations and `O(2^n)` stored values; this is an exponential exact
algorithm, not a polynomial-time or complexity-hardness claim. Rational inputs
permit exact rational comparisons, with separate representation of infinity.

This solves the post-request quantity needed by the separate recurring-upkeep
reduction. It does not itself prove that reduction or establish the practical
cost of evaluating many large instances.

Boundary cases are explicit: `F(N)=0`; a zero denominator is inadmissible; `d_i=0`
does not make a zero-capacity cold start possible; and readiness is assumed paid
for before the request as in the checkpoint.

## 4. Follow-on ordering pass

The [separate ordering note](2026-09-22-ordering-limits.md) gives an exact two-job
capacity reversal, a fixed-capacity three-job preference cycle, and a strict
counterexample to a natural greedy rule even without invalidation. These delimit
possible simplifications of the subset recurrence; they do not establish
complexity hardness or publication novelty.

## 5. Status and next scientific task

The heterogeneous serial optimum and its boundary cases have a complete written
proof. The weighted-potential argument was proposed and separately checked by
two internal research agents; this is not independent external review.
`analysis/verify_heterogeneous.py` supplies exact finite checks, including direct
permutation comparisons and the ordering obstructions. Its output must be read
for the actual checked domain; none of these checks enumerate all measurable
policies.

Publication novelty remains unresolved. Resource-dependent scheduling is a
close prior-art class; the repository's current literature comparison must be
read alongside this result. In particular, seriality itself must not be
advertised as new merely because the variables describe controller handover.
The [current source audit](2026-09-22-literature-audit.md) now records exact
subclass reductions and an embedding of the serial objective in experience-based
scheduling. The [upkeep proof](2026-09-22-heterogeneous-readiness.md) integrates
this theorem. Remaining tasks are the novelty of the all-policy reduction and
a justified independent-fallback interface, as specified in the current work order.
