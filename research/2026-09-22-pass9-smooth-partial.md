# Pass 9: smooth loss from arbitrary partial preparation

22 September 2026. This note closes the arbitrary-initial-state scheduling gap
for nonnegative nondecreasing Lipschitz loss functions that vanish at zero. It
also gives an attained finite-dimensional recurring-cost optimization. These
are results inside the stated ideal fluid model; novelty and a physical
realization remain unresolved. Positive propagation, finite cutover, and
protocol restrictions remain separate questions from earlier passes.

The [fixed-loss partial-state note](2026-09-22-pass9-partial-states.md) proves a
related theorem with reflected constant loss. Its measurable allocation
postponement construction is used below. Neither arbitrary-partial theorem is
merely an application of the earlier cold-state potential.

## 1. Model and claims

For each module `i`, let `M_i>0`, `a_i>=0`, and

$$g_i:[0,M_i]\longrightarrow[0,\infty)$$

be nondecreasing and Lipschitz, with `g_i(0)=0`. Source spare capacity is `s>=0`.
Maximum-loss preparation dynamics, before transfer, are

$$p_i'=v_i-g_i(p_i)\quad(0\leq p_i<M_i),$$

with upper reflection `p_i'=min(v_i-g_i(M_i),0)` at `M_i`. At zero the formula
already gives the nonnegative derivative `v_i`. Allocations are nonnegative,
measurable, bounded, and may be parallel or preemptive. With completed set `C`,
their sum is at most

$$b(C)=s+\sum_{i\in C}a_i.$$

A full module may transfer instantaneously, releasing its capacity and ending
its loss. Cutovers have no cost or coupling penalty. Smaller actual loss rates
`0<=rho_i(t)<=g_i(p_i(t))` are permitted, and the simultaneous maximum feedback
`rho_i(t)=g_i(p_i(t))` is an admissible adversarial history. Initial preparation
`p^0` is arbitrary in the closed product box, not restricted to ready/cold.
Policies and deadline guarantees are deterministic and robust for every
allowed loss history.

**Theorem 1 (full-state serial optimum).** From any initial preparation vector,
if finite exit is feasible, some policy that immediately transfers initially
full modules and then prepares one module at a time at the entire available
capacity attains the optimal robust exit time. The order is optimized; the
theorem does not claim preservation of an arbitrary schedule's completion order.
The finite optimum is attained by one of finitely many orders.

**Theorem 2 (attained recurring reduction).** Let `F(p)` denote this exact
full-state exit time and, for a finite deadline `H>=0`, define

$$\mathcal R_H=\{p:F(p)\leq H\},\qquad
C(H)=\min_{p\in\mathcal R_H}\sum_i g_i(p_i).$$

The set `R_H` is nonempty and compact, so this minimum is attained. With paid
initialization, exact guaranteed long-run optional throughput is `s-C(H)` when
`C(H)<=s`; otherwise indefinite all-request-time readiness is infeasible.
This is an attained optimization over a finite-dimensional compact set. It is
not a closed-form frontier, a convexity result, or a polynomial-time algorithm.

## 2. Delaying input improves terminal preparation

The following scalar lemma replaces the fixed-loss reflected suffix formula.
Extend `g` constantly beyond `M`, preserving nonnegativity, monotonicity, and
Lipschitz continuity. For this lemma alone use the uncapped equation

$$y'=v-g(y),\qquad y(0)=y_0\geq0.$$

Solutions remain nonnegative because `g(0)=0` and `v>=0`. Suppose two input
functions have cumulative difference

$$D(t)=\int_0^t(v_{\rm new}-v_{\rm old})\,dr\leq0,
\qquad D(T)=0.$$

Then `y_new(T)>=y_old(T)`: postponing a fixed amount of service cannot worsen
terminal preparation under nondecreasing loss.

**Proof.** Let `z=y_new-y_old` and set

$$\alpha(t)=
\begin{cases}
\dfrac{g(y_{\rm new})-g(y_{\rm old})}{y_{\rm new}-y_{\rm old}},
&y_{\rm new}\ne y_{\rm old},\\
0,&y_{\rm new}=y_{\rm old}.
\end{cases}$$

This measurable coefficient obeys `0<=alpha<=Lip(g)`, and
`z'=v_new-v_old-alpha*z`. Variation of constants, with equal initial states,
gives

$$z(T)=\int_0^T k(t)(v_{\rm new}-v_{\rm old})(t)\,dt,
\quad k(t)=\exp\left(-\int_t^T\alpha(r)\,dr\right).$$

Since `k'=alpha*k>=0`, integration by parts yields

$$z(T)=-\int_0^T k'(t)D(t)\,dt\geq0.$$

The use of an uncapped equation is only a comparison device. If a newly
constructed real trajectory reaches `M` earlier, transfer it at that first
hit and discard its later planned allocations. That only increases capacity
available to other modules. For a module that never reaches `M` before the
comparison time, the uncapped and physical trajectories agree. Thus an
uncapped overshoot is not mistakenly counted as stored physical preparation.

## 3. Front-loading a first completion

Initially full modules may be transferred immediately without harming any
other module. Work with the remaining subfull modules and their resulting
capacity `b`. If `b=0`, none can increase, so finite exit is impossible.

Consider any finite schedule on the maximum-loss history, and its first
completion, module `i` at time `T`. Transfer each full module immediately;
holding a full module cannot improve the optimum. Before `T` capacity is the
constant `b`, and no other module has completed.

Finite completion of a subfull module requires `b>g_i(M_i)`. If `b<=g_i(M_i)`,
the full-rate scalar solution cannot reach `M_i` from below in finite time:
a root of `b-g_i` is a barrier, and Lipschitz uniqueness prevents crossing or
finite-time arrival at an equilibrium. A state above a lower root cannot climb
past it toward `M_i`, either. Smaller allocations cannot help.

Set

$$\tau=\int_{p_i^0}^{M_i}\frac{dq}{b-g_i(q)}.$$

This is the time to complete `i` immediately at full capacity. Along the
original first-stage trajectory, the scalar potential
`W_i(p)=integral_0^p dq/(b-g_i(q))` satisfies

$$W_i'\leq v_i/b,$$

because `(v_i-g_i(p))/(b-g_i(p))<=v_i/b` for `0<=v_i<=b`. Hence its total
allocated work `V_i` up to `T` obeys

$$V_i\geq b\tau.$$

If `W` is all work allocated to the other modules before `T`, the shared
budget consequently gives

$$W\leq b(T-\tau).$$

There is enough rate-`b` time after `tau` to postpone all of their earlier work.
For clarity, the exact measurable construction from the fixed-loss note is
repeated here. For each `j!=i`, let `E_j=integral_0^tau v_j` be its early work.
On `[tau,T]`, retain its old allocation and use spare rate

$$h(t)=b-\sum_{j\ne i}v_j(t)\geq0$$

to repay all the `E_j` in any fixed module order. Indeed,

$$\int_\tau^T h(t)\,dt
=b(T-\tau)-W+\sum_{j\ne i}E_j
\geq\sum_{j\ne i}E_j.$$

If `H(t)=integral_tau^t h`, an explicit cumulative repayment to module `j` is

$$A_j(t)=\min\left\{E_j,
\max\left(0,H(t)-\sum_{\ell\text{ before }j}E_\ell\right)\right\}.$$

These functions are absolutely continuous, satisfy `A_j(T)=E_j`, and have
`sum A_j'<=h` almost everywhere. Use zero allocation to other modules before
`tau`, and `v_j+A_j'` afterward. Their aggregate rate is at most `b` and each
module's cumulative input is no greater than before at every intermediate
time, with the same total at `T`.

Now run module `i` at rate `b` from zero to `tau`, and transfer it. Its released
capacity makes the subsequent postponed allocations feasible, since they use
at most the old `b`. The scalar postponement lemma shows that at time `T` every
other module has at least its original preparation, unless it has already
completed, which is better. Stop newly completed modules and omit their later
allocations; this cannot hurt the remaining construction.

At time `T`, the completed set and remaining state therefore dominate those
of the original schedule. Replay the original suffix, omitting allocations
to already completed modules. Scalar comparison preserves the state ordering,
and capacity is never smaller, so final exit is no later than before.

After the newly front-loaded completion at `tau`, apply this same argument
inductively to the smaller remaining system. The base case of one module is
full-rate scalar copying. This produces a serial full-capacity schedule no
slower than any original feasible schedule, proving the lower-bound part of
Theorem 1. The resulting later order need not be the original order.

For robustness, follow an optimizing serial order under smaller actual losses.
One may compare with its virtual maximum-loss trajectory and transfer each
module no later than its virtual completion. Larger preparation and earlier
capacity release cannot delay the subsequent virtual schedule. The serial
policy therefore attains its maximum-loss completion bound for every allowed
history. Finitely many orders establish finite attainment.

## 4. Exact forward subset dynamic program

For a fixed initial vector `p^0`, let `q_i(t)` be its passive decay flow:

$$q_i'=-g_i(q_i),\qquad q_i(0)=p_i^0.$$

An as-yet unserved module in any serial schedule has exactly this state at
global time `t`, regardless of the order of previous modules. Let
`R={i:p_i^0=M_i}`. Transfer `R` at time zero, set `E(R)=0`, and set all other
unreached subset values to infinity. For each reached completed set `C` and
`i` outside it, a finite transition is possible if and only if
`b(C)>g_i(M_i)`, and its value is

$$E(C)+\int_{q_i(E(C))}^{M_i}\frac{dq}{b(C)-g_i(q)}.$$

Update `E(C union {i})` with the minimum over such transitions. The final
value `E(N)` equals `F(p^0)`.

Keeping only the earliest completion time for a subset is valid. An earlier
schedule can wait until a later schedule's completion time; the unserved
modules then have exactly the same passive states and the completed-set
capacity agrees. Equivalently, the transition function is increasing in its
time argument because passive preparation is nonincreasing. A later arrival
at the same subset cannot improve any suffix.

This takes `O(n*2^n)` flow/integral evaluations and comparisons and `O(2^n)`
stored values. It is a finite scheduling characterization, not a guarantee
of cheap exact symbolic integration or a bit-complexity bound for arbitrary
function representations. It also does not optimize continuously over all
initial preparation vectors by itself.

For `g_i(p)=gamma_i*p`, passive state is `p_i^0 exp(-gamma_i*t)` and each
accessible stage has duration

$$\gamma_i^{-1}\log
\frac{b(C)-\gamma_i q_i(E(C))}{b(C)-\gamma_i M_i}.$$

The zero-loss case uses duration `(M_i-q_i)/b(C)` when `b(C)>0`.

## 5. Compact readiness set and attainment of the static minimum

The ready set is nonempty because the all-full state exits instantly. To prove
closedness, it is safer to use bounded schedule witnesses than to assume that
the explicit hitting-time formula is continuous at inaccessible-rate or
initially-full boundaries.

Fix a permutation of all modules and allow nonnegative serial stage lengths
`ell_1,...,ell_n` with sum at most `H`. In a stage, allocate the entire available
capacity `b(prefix)` to the selected module. A zero-length stage
is valid when that module is already full. For this closure argument a ready
module may voluntarily wait for its specified stage; immediate transfer could
only improve the resulting feasible exit.

Unserved passive flows and fixed-capacity reflected stage flows are continuous
in initial preparation and duration for Lipschitz `g_i`. Require that each
stage's endpoint equal its module's `M_i`. These are closed conditions on the
compact product of the initial preparation box and the stage-length simplex.
Their projection onto initial states is compact. Taking the finite union over
all permutations remains compact.

By Theorem 1 this projected set is exactly `R_H`: every ready state has an
attaining serial schedule within `H`, and every witness is a feasible
schedule. This proves compactness even when initially full sets change in a
limit or an accessible denominator approaches a barrier. Since `sum g_i(p_i)`
is continuous, its minimum over `R_H` exists. No unproved optimization
attainment is hidden in Theorem 2.

## 6. Exact recurring cost, with paid initialization

Along the simultaneous maximum feedback history in normal operation, set
`Q=sum p_i`. Upper reflection gives

$$Q'\leq\sum_i v_i-\sum_i g_i(p_i)
\leq s-u-C(H)$$

for every uniformly ready normal policy, since its state belongs to `R_H` at
every request time. Integration yields

$$\int_0^t u(r)\,dr\leq(s-C(H))t+Q(0)-Q(t).$$

Bounded `Q` proves the matching long-run upper bound under this allowed
adversary. If `C(H)>s`, it also rules out indefinite readiness with `u>=0`.

If `C(H)<=s`, choose an attained minimizing state `p^*`, pay for its
initialization, and allocate fixed normal copying `v_i=g_i(p_i^*)` and optional
rate `u=s-C(H)`. Under maximum feedback the state is stationary. Under smaller
actual losses it may rise; scalar comparison ensures it stays componentwise
at least `p^*`. Higher preparation does not make exit harder, by simulating a
virtual policy from `p^*`. Every request therefore meets `H`, and the constant
optional rate attains the bound.

The actual state is not claimed to remain exactly equal to `p^*` under benign
loss histories. Nor is this state claimed reachable from cold under the same
fully loaded normal budget. Its initialization is paid before the guaranteed
deployment, as in the historical theorem. Constrained startup remains a
separate reachability problem.

## 7. Scientific status

This note solves the all-policy full-state scheduling oracle for the stated
smooth class and establishes an attained exact static characterization of
heterogeneous recurring upkeep. It does not provide a general analytic formula
for `C(H)`, establish convexity of `R_H`, or show an efficient continuous
optimization algorithm. The compactness argument is a correctness result,
not a numerical procedure.

The postponement lemma uses monotonicity of loss, and its uncapped comparison
uses `g_i(0)=0`; the separate reflected fixed-loss argument must not be
silently substituted for an arbitrary discontinuous or nonmonotone loss law.
The exchange also relies on independent instantaneous cutovers and
nondecreasing source capacity. The earlier delayed-release counterexample
shows that changing those timing rules can invalidate seriality.

The bounded-storage averaging method remains established background. The
input-postponement and arbitrary-partial serial reduction require their own
theorem-level prior-art audit before any publication novelty claim. No
external mathematical review, implementation validation, or submission
readiness is asserted here.
