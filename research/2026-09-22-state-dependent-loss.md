# Serial handover under smooth state-dependent invalidation

22 September 2026. Research pass 4. This pass tests whether the preceding
serial-scheduling result depends on the fixed-rate model's weakest operational
assumption: losing preparation at the full rate whenever any useful preparation
exists. It proves that serial optimality survives a broad smooth alternative.
It does not extend the fixed-rate upkeep staircase, establish publication
novelty, or validate an engineering deployment.

## 1. Alternative model and theorem

Keep finite independent modules with `M_i>0`, `a_i>=0`, spare capacity `s>=0`,
instantaneous cutover, independently provisioned fallback, and the same
nonnegative shared allocation budget. Replace the invalidation law by a function

    g_i : [0,M_i] -> [0,infinity),

which is nondecreasing and Lipschitz, with `g_i(0)=0`. All parameters and
Lipschitz constants are finite. Allowed loss processes satisfy

    0 <= rho_i(t) <= g_i(p_i(t))

at the actual state. State derivatives are `v_i-rho_i` in the interior, with the
same lower and upper reflection as the active checkpoint. Measurable bounded
causal allocations, arbitrary parallelism, preemption, and adaptive decisions
are allowed. The guarantee is robust for every admissible loss process, including
simultaneous maximal loss `rho_i(t)=g_i(p_i(t))`.
This maximal adversary is a permitted feedback rule evaluated at the actual
state, not a single predetermined numeric loss trace shared by different
policies.

This is an alternative uncertainty set. It is not a derivation of a smooth law
from the fixed-rate model. In particular the discontinuous fixed-rate boundary
rule is not included in the Lipschitz class.

For `b>=0`, define the cold serial stage time

    c_i(b) = integral_0^{M_i} dq/(b-g_i(q)),  if b>g_i(M_i),
             infinity,                     otherwise.       (1)

Because `g_i` is nondecreasing, `g_i(M_i)=max g_i`. From fully ready set `S` and
otherwise cold modules, transfer `S` immediately and put
`b(C)=s+sum_{i in C}a_i`.

**Theorem 1.** The exact optimal guaranteed post-request completion time is the
minimum, over permutations of `N\S`, of

    sum_r c_{pi_r}(b(S union {pi_1,...,pi_{r-1}})).             (2)

An infinite stage makes an order infeasible. A finite minimum is attained by
allocating all available capacity to one cold module at a time. Every finite
maximal-loss schedule takes at least the value in (2) for its own completion
order, with arbitrary linearization of simultaneous cutovers.

As before, this is a theorem from ready/cold states. It does not characterize
optimal scheduling or readiness from arbitrary partially prepared states.

## 2. Finite-time accessibility and the equality barrier

Suppose current capacity is `b>0`. Since completed handovers only release
capacity, every earlier allocation to an unfinished module was at most `b`.
Its maximal-loss trajectory from zero is dominated by the scalar full-capacity
trajectory `x'=b-g_i(x)`, reflected on `[0,M_i]`. This is the standard scalar
comparison property for a Lipschitz vector field: at a first crossing the
controlled state cannot have greater forward drift. Equivalently, apply a
Gronwall estimate to the positive part of the trajectory difference.

If `b<=g_i(M_i)`, let

    r = min {q in [0,M_i] : g_i(q)>=b}.

Continuity and `g_i(0)=0<b` give `r>0` and `g_i(r)=b`. If `L` is a positive
Lipschitz constant, then for `q<r`,

    0 < b-g_i(q) = g_i(r)-g_i(q) <= L*(r-q).

Consequently the full-capacity time integral diverges as `q` approaches `r`.
The barrier `r` cannot be reached in finite time. This includes the equality
case `b=g_i(M_i)`, even if the barrier is exactly `M_i`. If the loss function is
identically zero, no positive-`b` barrier exists and stage time is `M_i/b`.

It follows that at any finite time under maximal loss, an unfinished module
has `g_i(q)<b` for every `q<=p_i`, even when it cannot yet finish at current
capacity. A module completing at finite time necessarily has `b>g_i(M_i)`.
These facts justify every denominator used below. For `b=0`, the allocation
budget and `g_i(0)=0` keep all cold states at zero, so a nonempty cold system
cannot complete before some external capacity change; none exists in this model.

Lipschitz regularity is substantive for the equality claim. For example,
`g(q)=1-sqrt(1-q)` on `[0,1]` is nonnegative, nondecreasing, continuous and zero
at zero, but not Lipschitz at one. At `b=1=g(1)`, the full-rate time is
`integral_0^1 dq/sqrt(1-q)=2`, finite. This counterexample prevents silently
weakening the theorem's regularity assumption to continuity.

## 3. Integral-potential proof of serial dominance

Fix the admissible simultaneous maximal-loss history. Between cutovers with
`b>0`, define

    G_i(p;b) = integral_0^p dq/(b-g_i(q)),
    W_b(p) = sum_{unfinished i} G_i(p_i;b).                    (3)

Section 2 shows these quantities are finite at every finite reachable state.
On each closed interval preceding a finite next cutover the reached states
remain strictly inside any inaccessible barrier, so the chain rule and
integration below apply to absolutely continuous trajectories. Jobs unable to
finish at current capacity still contribute their finite partial integral;
unlike the fixed-rate proof, their partial preparation need not vanish.

At an interior state,

    dG_i/dt = (v_i-g_i(p_i))/(b-g_i(p_i)) <= v_i/b,           (4)

because `0<=v_i<=b` and `g_i(p_i)>=0`. At zero the derivative is `v_i/b`,
since `g_i(0)=0`; upper reflection can only lower the left side. Thus

    W_b' <= sum_i v_i/b <= 1.                               (5)

When module `i` transfers, its removed potential is exactly `c_i(b)`. Capacity
then increases to `b+a_i`; every remaining integral weakly decreases because
its denominator increases pointwise. There is no need to assume unfinishable
jobs have zero preparation. Therefore the downward jump in `W` is at least
`c_i(b)`. Linearizing simultaneous cutovers gives the same conclusion one
module at a time.

All unfinished modules start cold, and no unfinished modules remain at the
end, so the potential starts and ends at zero. Integrating (5) and summing the
jumps proves that completion time is at least the serial sum for the same
completion order.

For attainment, use a minimizing finite order. At stage capacity `b`, maximal
loss and full allocation give `p'=b-g_i(p)>0`; separation of variables gives
exactly (1). Any smaller allowed loss satisfies `p'>=b-g_i(p)` before upper
reflection, so scalar comparison ensures completion no later. Earlier cutovers
only increase capacity. The finite set of permutations has an attained minimum,
establishing the robust optimum in (2), including deadline endpoints.

The same subset recurrence holds with stage term `c_i(b(C))`:

    F(N)=0,
    F(C)=min_{i not in C} [c_i(b(C)) + F(C union {i})].         (6)

This uses `O(n*2^n)` arithmetic and stage-integral evaluations. For general
functions, evaluating integrals and comparing values are additional analytic
or numerical tasks; (6) is not an exact rational algorithm in that generality.

## 4. Proportional invalidation

For `g_i(p)=gamma_i*p`, `gamma_i>=0`, formula (1) becomes

    c_i(b) = log[b/(b-gamma_i*M_i)]/gamma_i,
             when gamma_i>0 and b>gamma_i*M_i;
    c_i(b) = M_i/b, when gamma_i=0 and b>0;
    c_i(b) = infinity otherwise.                            (7)

Thus heterogeneous cold serial dominance persists in the proportional model.
The full-capacity solution
`p(t)=(b/gamma_i)*(1-exp(-gamma_i*t))` verifies the positive-`gamma_i` stage
formula directly. At `b=gamma_i*M_i>0`, it approaches `M_i` asymptotically;
it does not finish in finite time. If every module is already ready, total
completion time is zero independently of these cold-stage conditions.

This demonstrates precisely what depends on the fixed-rate choice: the
support-based recurring-cost staircase does, while the cold serial scheduling
property does not.

## 5. Why the fixed-rate upkeep formula does not transfer

Support domination still gives a necessary condition: gratuitously making every
positive preparation fully ready and transferring those modules makes exit
easier. But at a partially prepared normal state the actual maximal recurring
loss is now `sum_i g_i(p_i)`, which can be strictly below the sum of the fully
ready losses `sum_{i:p_i>0} g_i(M_i)`. The fixed-rate proof's support-cost lower
bound is therefore unavailable.

The active checkpoint already gives a strict one-module witness. With
`M=1`, `s=1`, `g(p)=p/2`, and `H=log(2)`, the minimum ready preparation is
`p_H=2-sqrt(2)`. Keeping it at that level costs

    g(p_H)=1-1/sqrt(2) < 1/2=g(M).

The cold system does not meet this deadline, so a hot-subset-only formula would
require the full cost `1/2` and would be wrong. Partial readiness changes the
answer even though cold serial scheduling remains optimal.

One may define an abstract ready-state set `R_H` and write

    C(H)=inf_{p in R_H} sum_i g_i(p_i).

The total-preparation inequality gives an average-rate upper bound `s-C(H)`.
If a minimizing ready state `p*` exists and its cost is at most `s`, allocations
`g_i(p_i*)` keep the actual state at or above `p*` for every allowed loss process
by scalar comparison. More preparation cannot harm readiness under this
Lipschitz model, so this gives a matching constant-target construction. This
observation still contains the
uncharacterized full-state readiness set, unlike the explicit fixed-rate subset
reduction. It is not a solved heterogeneous smooth recurring frontier. In
particular, (6) evaluates ready/cold states and does not determine `R_H`.

## 6. Status, checks, and next question

The written proof establishes serial dominance for the stated smooth monotone
Lipschitz class. The non-Lipschitz equality example is an exact counterexample
to a tempting weakening of the assumptions. No corresponding general theorem
for all arbitrary initial partial states or an explicit smooth upkeep frontier
is claimed.

The [following pass](2026-09-22-proportional-readiness.md) gives an explicit
full-state recurring frontier for homogeneous proportional loss when `s>d`.
Heterogeneous smooth readiness remains unresolved. The remaining research
questions include whether a justified update model supports that interpretation,
and whether this integral potential is already covered by scheduling theory.
This extension removes one possible overclaim about the special role of
fixed-rate invalidation; it does not by itself establish a publishable
contribution.

Supporting checks are in `analysis/verify_state_dependent.py` and
`results/state-dependent-verification.json`. Exact rational local inequalities
are separated from floating stage/inverse evaluations. These finite checks do
not establish the theorem for arbitrary Lipschitz functions.
