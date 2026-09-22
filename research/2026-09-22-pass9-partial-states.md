# Arbitrary partial states in the instantaneous fixed-loss model

22 September 2026. Research pass 9. This note resolves the previously open
extension from ready/cold states to arbitrary partial initial preparation.
Full-speed serial preparation remains optimal in the instantaneous-release
fixed-loss model. A forward subset dynamic program computes the exact exit
time of every specified initial state. This is an internal mathematical result;
publication novelty and operational validation remain separate questions.

## 1. Model and statement

There are finitely many independent modules with finite `M_i>0`, `a_i>=0`,
`d_i>=0`, spare capacity `s>=0`, and initial preparations
`p_i^0 in [0,M_i]`. The original strictly positive-release model is included.
An unfinished module has the fixed-rate reflected dynamics on `[0,M_i]`, with
arbitrary measurable loss `0<=rho_i(t)<=d_i`. Every simultaneous componentwise
bounded loss history is allowed, including constant maximum loss. Allocations
are nonnegative, bounded, measurable, and causal. They may be parallel,
preemptive, idle, and history dependent.

On completion, a module can transfer instantaneously and irreversibly. This
ends its preparation loss and releases `a_i` at the same event. If `S` has
transferred, the preparation budget is

    b(S)=s+sum_{i in S} a_i.

There are no handoff delays, residual drains, dependencies, or additional
resource charges. The positive-drain counterexamples in pass 6 do not satisfy
this model. Independent receiver resources and sufficient transfer state remain
the explicit assumptions of the previous instantaneous-release notes.

Let `S0={i:p_i^0=M_i}`. Transferring these modules at time zero cannot hurt:
their work and losses disappear, and capacity weakly increases. More generally,
an immediate transfer at any full preparation cannot hurt. A delayed-transfer
schedule can be replayed on a virtual system while omitting work on the already
transferred module; every other allocation still fits and every other state can
match its virtual counterpart. Thus immediate transfers may be assumed when
proving an optimal value.

**Theorem 1 (serial dominance from arbitrary partial states).** From every
initial state `p^0`, the optimal robust removal time is the minimum over the
finitely many full-speed serial permutations of `N\S0`, after transferring
`S0` at time zero. In a serial stage only the selected module receives
preparation; the other unfinished preparations decay passively. Every finite
feasible maximum-loss schedule can be replaced by such a serial schedule with
no later final completion. A finite permutation minimum is attained robustly.

The replacement is not claimed to preserve the original schedule's complete
completion order. The earlier cold-state potential establishes a stronger
same-order inequality in its narrower domain; the exchange proof here does not
extend that stronger statement.

## 2. Minimum allocation needed by the first completed module

Work under simultaneous maximum loss and assume initially full modules have
already transferred. Suppose a finite schedule's first further transfer is
module `i` at time `T>0`. Its capacity before that transfer is the constant
`b=b(S0)`. Immediate transfer may be assumed, so no unfinished preparation
has reached its upper boundary before `T`.

Put `Delta=M_i-p_i^0>0`. On the set where `p_i>0`, its derivative is
`v_i-d_i` almost everywhere; on the zero set the derivative of the absolutely
continuous preparation is zero almost everywhere. If `L` is the measure of
its positive-state times in `[0,T]`, then

    Delta = integral_{p_i>0} v_i(t)dt - d_i*L
          <= (b-d_i)*L.

Hence a finite first completion requires `b>d_i`. Define its earliest
full-speed completion time

    tau=(M_i-p_i^0)/(b-d_i).

We have `T>=L>=tau`. More importantly, its total allocated work satisfies

    V_i(T)=integral_0^T v_i(t)dt
           >= Delta+d_i*L >= b*tau.                         (1)

This bound includes histories in which the initial preparation is partly or
entirely lost and rebuilt. Wasted allocation at zero cannot improve it.
If `d_i=0`, (1) is the usual required-work bound. If `b<=d_i`, a nonfull
module cannot grow to full preparation at this capacity, including at equality.

## 3. Exact exchange for bounded measurable allocations

Run module `i` alone at full rate `b` from time zero to `tau`, and transfer it
then. All other modules receive zero preparation during this interval. Their
lost allocations will be postponed, not assumed free.

For each `j!=i`, write

    E_j=integral_0^tau v_j(t)dt.

On `[tau,T]`, retain every original allocation to these other modules and use
the spare rate

    h(t)=b-sum_{j!=i}v_j(t) >= 0

to repay their postponed work. The original capacity constraint and (1) give

    integral_tau^T h(t)dt
      = b*(T-tau)-sum_{j!=i} integral_tau^T v_j(t)dt
      >= sum_{j!=i} E_j.                                    (2)

There is an explicit bounded measurable allocation of this spare rate. Choose
any fixed ordering of the other modules, set

    H(t)=integral_tau^t h(u)du,
    A_j(t)=min(E_j, max(0,H(t)-sum_{k before j}E_k)),

and give module `j` its original allocation plus `A_j'(t)` on `[tau,T]`.
The functions `A_j` are absolutely continuous, their derivatives are
nonnegative almost everywhere, and `sum_j A_j'<=h`. Equation (2) ensures
`A_j(T)=E_j` for every module. The new aggregate allocation after `tau` is
at most `b`, while the actual available capacity is at least `b+a_i>=b`.
Thus the construction uses no impulses or approximation of measurable controls.

Let `U_j` and `U_j^new` denote cumulative original and new allocations to `j`.
Before `tau`, the new cumulative allocation is zero. Afterward it equals
`U_j(t)-E_j+A_j(t)`. Therefore

    U_j^new(t)<=U_j(t) for 0<=t<=T,
    U_j^new(T)=U_j(T).                                      (3)

Every postponed module receives the same total work by `T`, with its work
shifted later. This helps, rather than harms, terminal preparation under the
fixed-loss law. To verify the claim exactly, the lower-reflected trajectory
without an upper barrier has terminal state

    max{p_j^0+U_j(T)-d_j*T,
        sup_{0<=r<=T}[U_j(T)-U_j(r)-d_j*(T-r)], 0}.           (4)

Equation (3) leaves the first term unchanged and weakly increases every term
in the supremum. The original trajectory has no upper hit before the first
transfer `T`, so (4) gives its terminal preparation. If a new trajectory reaches
`M_j` before `T`, transfer it immediately and delete its later assigned work;
this only releases more capacity. Otherwise its actual trajectory agrees with
the lower-reflected trajectory throughout, and its state at `T` is at least
the original state. These comparisons apply independently to every module.

At time `T`, the new system has completed module `i`, possibly additional
modules, and every remaining preparation is at least its original counterpart.
Replaying the original suffix is feasible: reflected fixed-loss trajectories
are monotone in their initial states under the same allocations, and earlier
transfers only remove work and increase capacity. Thus the original completion
deadline is met with a full-speed first stage ending at `tau`.

The schedule after `tau` is a feasible schedule on one fewer unfinished
module, starting from the passive-decayed remaining preparations and capacity
`b+a_i`. Induct on the number of unfinished modules. The empty case is complete;
the one-module case is the full-speed traversal above. The induction replaces
the remaining schedule by a serial schedule without extending its final
completion. This proves the deterministic maximum-loss part of Theorem 1.

## 4. Robust attainment and boundary cases

For a chosen serial permutation, the maximum-loss trajectory is explicit.
At elapsed time `t`, an unserved module has preparation

    phi_i(t)=max(0,p_i^0-d_i*t).                              (5)

If the current completed set is `S` and `i` is selected next, its stage time is

    (M_i-phi_i(t))/(b(S)-d_i),                               (6)

provided `b(S)>d_i`. Otherwise the order is infeasible at that stage. Since
initially full modules were transferred at zero, every later selected module
has a strictly positive deficit, so a zero denominator cannot hide a zero-time
completion.

Run this order with actual full-capacity allocations and immediate transfers.
Smaller allowed losses retain at least as much preparation in every unserved
module. By induction through the stages, each selected module starts no later,
with no smaller preparation, than on the maximum-loss trajectory, and completes
no later. The same permutation therefore meets its computed deadline for every
allowed loss history.

Every robust policy must succeed on the maximum-loss history; sections 2–3
give a no-slower serial permutation on that history. Conversely every finite
serial permutation is robust by the preceding comparison. There are finitely
many permutations, so their finite minimum is attained. If none is finite,
there is no finite robust exit policy. This establishes Theorem 1, including
exact deadline endpoints.

Boundary cases are not exceptions to the proof:

- If all modules are initially ready, transfer them at zero and exit at zero.
- If `b(S0)=0` and a nonfull module remains, no first progress is possible,
  including when its loss rate is zero.
- A nonfull module with `d_i=b(S)` cannot finish until some other transfer
  increases capacity beyond its loss rate.
- Durable preparation `d_i=0` remains unchanged while its module is unserved.
- A zero capacity release `a_i=0` preserves the exchange argument because
  capacity still does not decrease.
- Simultaneous original completions are allowed. Immediate transfers of the
  new schedule may reorder them; no same-order conclusion is required.

## 5. Forward subset dynamic program for the full initial state

The elapsed time matters because unserved initial preparations decay. It would
be incorrect simply to reuse a backward cold-state value `F(S)` that ignores
time and the given initial state.

For each subset `S` containing `S0`, let `E(S)` be the earliest attained elapsed
time at which a serial prefix has transferred exactly the modules in `S`,
with no preparation given to the others. Set `E(S0)=0` and all other labels
initially to infinity. Process subsets in increasing size. From a finite label,
for each `i not in S` with `b(S)>d_i`, perform the relaxation

    E(S union {i}) = min(E(S union {i}),
        E(S)+(M_i-max(0,p_i^0-d_i*E(S)))/(b(S)-d_i)).         (7)

A subset can be reached at different times, but its earliest label suffices.
At absolute time `t`, every unserved coordinate of every serial prefix is
exactly (5); no extra state beyond elapsed time and the completed subset is
needed. If a prefix reaches `S` earlier, it can wait until a later prefix's
completion time. Then both have the same capacity and the same passive states,
so the earlier completion cannot impair any continuation.

For the immediate next serial stage this dominance is also explicit: with
`S` fixed, the function

    t -> t+(M_i-max(0,p_i^0-d_i*t))/(b(S)-d_i)

is increasing wherever the denominator is positive. Therefore an earliest
prefix cannot yield a later next completion than any later prefix with the
same completed set. Induction over subset size proves that (7) gives exactly
the earliest attained serial-prefix times. Every finite relaxation corresponds
to an actual full-speed stage, so no feasibility or attainment is lost by
keeping only one label.

**Theorem 2 (full-state exit computation).** The exact optimal robust exit time
from `p^0` is `E(N)`, with infinity if there is no finite label. A minimizing
serial order is recovered from predecessor labels. A given state is ready for
deadline `H` exactly when `E(N)<=H`.

With precomputed subset capacities, the computation uses `O(n*2^n)` arithmetic
operations and `O(2^n)` stored labels. Restricting to supersets of `S0` reduces
the actual state count. Rational parameters and rational initial preparations
give exact rational comparisons. This is an exponential arithmetic-operation
bound, not a polynomial-time or bit-complexity claim.

## 6. Scope and remaining comparison

This closes the arbitrary-partial-state scheduling gap for the instantaneous
fixed-loss model. It also supplies the full ready-state membership calculation,
rather than only the ready/cold values needed by the support-upkeep frontier.
The original recurring fixed-loss frontier itself remains unchanged: its
support domination and static attaining construction were already sufficient
without knowing the exit time of each partial state.

The proof uses fixed-loss terminal reflection identity (4). No smooth-loss
extension is claimed in this note without a separate comparison argument.
The counterexamples with positive residual-drain times remain valid. Their
suffix retains pending drain ages and future timed capacity releases; it is not
an instance of the induction hypothesis with current capacity `b+a_i`. Drains
already active at a request can also change capacity before the first new
preparation completion, defeating the constant-`b` premise of section 2.

This note establishes a mathematical extension, not publication novelty. Its
relation to work-conserving exchanges, perishable-work scheduling, and the
already inspected learning-effect serial objectives still requires an exact
primary-source comparison. No new simulation or empirical-validation claim is
made here.
