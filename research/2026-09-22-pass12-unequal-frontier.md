# Pass 12: an explicit readiness frontier for unequal proportional losses

22 September 2026, continuing from `6400737695eba9091389859724f783e03d8c1e8f`.
The [unequal-decay concentration theorem](2026-09-22-pass11-unequal-decay.md)
shows that an optimal upkeep state has at most one genuinely partial module.
The partial module need not be prepared first after the initially full modules
transfer. This note handles every possible cold prefix, obtains a finite subset
algorithm, and gives an exact two-module instance where allowing that prefix
strictly improves the globally optimal upkeep.

The theorem applies to arbitrary nonnegative spare capacity, with inaccessible
stages explicitly excluded. It does not assume `s>max_i gamma_i*M_i`. The
algorithm is exponential, uses real logarithmic/exponential values in general,
and is not a rational-field or polynomial-time complexity claim. Publication
novelty and a justified physical proportional-loss interface remain unresolved.

## 1. Model and established ingredients

There are `n>=1` independent modules, with finite

    M_i>0, gamma_i>0, a_i>=0, s>=0,
    d_i=gamma_i*M_i.

Useful preparation lies in `[0,M_i]`, follows reflected fluid dynamics, and
has allowed loss `0<=rho_i(t)<=gamma_i*p_i(t)`. Simultaneous maximal feedback
loss is permitted. Independent instantaneous cutovers release `a_i`. Normal
optional and preparation allocations obey `u+sum_i v_i<=s`; optional work
stops at a request. All receiver resources and initialization remain separately
paid, as in the preceding model. Positive handoff latency and delayed release
are not included.

Policies are deterministic and may be causal, measurable, preemptive, parallel,
and adaptive, as in the full-state serial theorem. The
deadline guarantee applies to every admissible preceding and future loss
history and every counterfactual request time. Define

    C(H)=min {sum_i gamma_i*p_i : F_full(p)<=H},    H>=0,      (1)

where `F_full` is the exact robust exit time from an arbitrary preparation
vector.

Two previously proved results are used:

1. [Full-state seriality and compactness](2026-09-22-pass9-smooth-partial.md):
   an attaining serial full-capacity exit exists whenever finite exit is
   possible; all initially full modules may transfer at time zero; the ready
   set for finite `H` is compact and nonempty. A subfull module can complete
   at capacity `b` only if `b>d_i`.
2. [Unequal-rate concentration](2026-09-22-pass11-unequal-decay.md): every
   minimizing preparation vector in (1) has at most one coordinate strictly
   between zero and its `M_i`. This holds also when some cold stages are
   inaccessible. It does not force the partial module to precede cold ones.

These ingredients reduce the remaining problem to a ready set, one optional
partial module, a cold prefix, and a cold suffix. No continuous preparation
optimization remains after the candidate formulas below.

## 2. Cold-stage and cold-tail values

For a set `D` of completed modules, put

    b(D)=s+sum_{j in D} a_j,
    d(S)=sum_{j in S} d_j.

The exact stage time of a cold module is

    c_i(b)=log[b/(b-d_i)]/gamma_i,    if b>d_i,
           infinity,               otherwise.               (2)

Equality `b=d_i` is inaccessible in finite time from a subfull state, not a
zero-work special case. If every remaining module is already full, they can
transfer instantaneously without using (2).

Let `F(D)` be the exact exit time when `D` are initially full and all others
are cold, after transferring `D` at time zero. Then

    F(N)=0,
    F(D)=min_{i not in D, b(D)>d_i}
             [c_i(b(D))+F(D union {i})].                     (3)

An empty minimum is infinity. Infinite suffixes are excluded. Equation (3)
is exact over all policies by the serial theorem, and a finite minimum stores
an attaining order.

## 3. Earliest completion of a chosen cold prefix

Fix the initially ready set `S`. For `C subset N\S`, let `L_S(C)` be the
earliest time to finish precisely the cold prefix jobs in `C`, before serving
any other nonready module. Use the forward subset recurrence

    L_S(empty)=0,
    L_S(C)=min_{j in C, b(S union (C\{j}))>d_j}
        [L_S(C\{j})+c_j(b(S union (C\{j})))].                (4)

An unreachable state has value infinity. The capacity depends only on the
completed set; all unserved prefix jobs are cold. Thus (4) is the ordinary
exact subset recurrence for the selected prefix. An unserved partial module
outside `S union C` receives no allocation during this time and passively
decays; it does not alter any prefix duration.

The empty prefix is valid even when `b(S)=0`. No division by zero is performed
for that base case. Any nonempty accessible edge still requires `b>d_j>0`.

## 4. Exact candidate with one partial module at an arbitrary position

Choose disjoint `S,C`, and `i not in S union C`. Initialize every member of `S`
fully, module `i` to `q`, and all others cold. Transfer `S` immediately, execute
the cold prefix `C`, prepare `i`, then finish the cold suffix.

Write

    t=L_S(C),
    b=b(S union C),
    R=F(S union C union {i}).

This candidate is considered only when `t` and `R` are finite and `b>d_i`.
At time `t`, the partial module has `q*exp(-gamma_i*t)`. Its completion time
measured from the original request is

    Phi_i(t;q,b)
      = log[(b*exp(gamma_i*t)-gamma_i*q)/(b-d_i)]/gamma_i.    (5)

For `0<=q<=M_i`, this is at least `t`. At fixed `q,b`, it is strictly
increasing in `t`:

    partial Phi_i/partial t
      = b*exp(gamma_i*t)
        / [b*exp(gamma_i*t)-gamma_i*q] > 0.                  (6)

Consequently an earlier prefix completion always improves, or preserves, the
attainable deadline. There is no hidden advantage to choosing a slower prefix
to reduce the decay of the waiting module. The optimal cold suffix duration
is independent of the elapsed time because every suffix job is cold.

The total displayed strategy takes `Phi_i(t;q,b)+R`. Solving its deadline
inequality gives the least required initial preparation

    q_{S,C,i}(H)
       = max{0,
           b*exp(gamma_i*t)
           - (b-d_i)*exp(gamma_i*(H-R))
         }/gamma_i.                                        (7)

If this exceeds `M_i`, discard the candidate. Otherwise its upkeep is

    K_{S,C,i}(H)=d(S)+gamma_i*q_{S,C,i}(H).                   (8)

The value `q=0` simply represents a cold job in the distinguished position.
The endpoint `q=M_i` may be retained as a valid schedule that voluntarily
delays that full module. Its immediate-transfer alternative can only help.
If `b<=d_i`, do not try to rescue a singular formula by setting `q=M_i`:
that initial full state belongs instead among the ready/cold candidates below.

## 5. Explicit frontier including all inaccessible-rate boundaries

Include a pure ready/cold candidate of cost `d(S)` whenever `F(S)<=H`.
In particular, `S=N` is always included because `F(N)=0`. The exact frontier is

    C(H)=min {
        d(S) for S subset N with F(S)<=H,
        K_{S,C,i}(H) for disjoint S,C, i not in S union C,
          L_S(C)<infinity, b(S union C)>d_i,
          F(S union C union {i})<infinity,
          0<=q_{S,C,i}(H)<=M_i
    }.                                                      (9)

**Theorem (unequal proportional frontier).** Equation (9) equals the compact
all-state minimum (1), for all stated nonnegative source budgets and releases.
It supplies an attaining initial state and a finite schedule whenever the
selected candidate is used. It leaves no continuous optimization oracle.

**Proof.** Every listed candidate is feasible by its explicit construction, so
its cost is at least the minimum in (1). Conversely take an attained minimizer
of (1). Concentration says it has a fully ready set `S` and at most one partial
module. If it has no partial module, the ready/cold candidate represents it.
Otherwise let `i` be the partial module and take an attaining serial schedule
after immediately transferring `S`. Partition its other modules into the cold
prefix `C` before `i` and the cold suffix after it.

Each actual cold prefix edge and the partial stage are accessible. Replacing
the prefix by (4) gives an earlier arrival at the same completed set. Equation
(6) shows this cannot worsen completion of `i`. Replacing the cold suffix by
(3) also cannot worsen exit. Finally reduce `q` to (7), if necessary, without
violating the deadline. Thus (9) contains a feasible candidate of cost no
greater than the global minimum. Equality follows.

This argument uses concentration of a minimizing state; it does not impose
partial-first scheduling on a prescribed concentrated vector. It also does not
assume that nearly full preparation can cross a finite-time equilibrium barrier.

## 6. Recurring throughput and computational scope

Under maximal loss, a uniformly ready normal policy satisfies

    Q'<=s-u-sum_i gamma_i*p_i<=s-u-C(H),
    Q=sum_i p_i.

Hence for each duration `T>0`,

    integral_0^T u(t)dt <= [s-C(H)]*T+Q(0)-Q(T).              (10)

Bounded preparation supplies the all-history minimax upper bound. If `C(H)<=s`,
pay for an attaining initialization, allocate `v_i=gamma_i*p_i^*` normally,
and use `u=s-C(H)`. Scalar comparison keeps preparation at least the target
under every smaller allowed loss history; the displayed request-time strategy
therefore meets `H`. If `C(H)>s`, indefinite readiness is impossible even with
zero optional work. Negative throughput is never interpreted as feasible.

Precompute the cold tails (3). For each ready set `S`, evaluate its prefix
table (4), inspect all distinguished `i` outside each prefix, and discard that
prefix table when moving to the next `S`.

The disjoint-pair count is `3^n`; the total prefix transitions are
`n*3^(n-1)`, and the partial-position candidates have the same count. Thus the
algorithm uses `O(n*3^n)` scalar evaluations and comparisons, plus
`O(n*2^n)` cold-tail work. Processing ready sets sequentially requires
`O(2^n)` working storage, excluding optional output/certificate storage.

These are real-arithmetic evaluation counts. Unequal rates produce general
logarithmic and exponential expressions; even rational model parameters do not
make the candidate values rational. Floating code requires explicit numerical
comparison tolerances or certified intervals where exact eligibility matters.
The common-rate rational-`X` method in pass 10 remains a stronger arithmetic
specialization and avoids enumerating cold prefixes.

The prefix restriction proved in pass 11 can prune candidates: in an optimal
state's attaining order, every cold module preceding a genuinely partial `i`
must have `gamma_j>gamma_i`. The full enumeration in (9) is already exact and
does not rely on implementing this pruning. No polynomial-time claim follows.

Boundary checks include:

- `H=0` requires every module full, so `C(0)=sum_i d_i`.
- Zero upkeep occurs exactly when `F(empty)<=H`, because all `gamma_i>0`.
- `s=0` is allowed; no initially cold module moves before some initially full
  module releases positive capacity. The empty-prefix and all-ready cases
  remain well defined.
- Zero `a_i` are allowed, but completing such a module adds no capacity.
- Paid all-ready initialization always gives a finite individual exit; it need
  not be maintainable within the normal budget.
- Cold startup under the same normal load remains a separate reachability
  question, not part of the initialization allowance.

## 7. Exact global separation from a partial-first frontier

Consider two modules with

    s=1, H=log(3),

| Module | M | a | gamma | d=gamma*M |
|---|---:|---:|---:|---:|
| A | `1/2` | `3/10` | `1` | `1/2` |
| B | `1/2` | `1/10` | `1/2` | `1/4` |

The strict high-capacity condition of pass 10's domain is satisfied, so this
separation is not caused by inaccessible stages. Concentration reduces the
global minimum to pure ready/cold states and the four possibilities below.
Each entry gives the minimum maintenance cost `gamma_i*p_i` for that order
when only its indicated module is initially partial.

| Partial module | Preparation order | Exact required maintenance |
|---|---|---|
| A | A then B | `29/1352` |
| B | A then B | `(26*sqrt(2)-21*sqrt(3))/20` |
| B | B then A | `1-(3/4)*sqrt(18/11)` |
| A | B then A | `7/45` |

To verify these expressions, cold A at initial capacity one takes `log(2)`;
cold B there takes `2*log(4/3)`. After A releases capacity, B has
`b=13/10`, `b-d_B=21/20`, and cold duration `2*log(26/21)`. After B releases,
A has `b=11/10`, `b-d_A=3/5`, and cold duration `log(11/6)`. Substitution in
(7), with empty or one-job prefix, gives exactly the four entries.

The second entry is positive, since

    (26*sqrt(2))^2-(21*sqrt(3))^2=1352-1323=29>0.

Rationalizing it gives

    C_* = 29/[20*(26*sqrt(2)+21*sqrt(3))].                   (11)

The exact bounds `sqrt(2)>7/5` and `sqrt(3)>17/10` imply its denominator is
greater than `1442`, and hence greater than `1352`. Therefore
`C_*<29/1352`. Also `sqrt(18/11)<13/10`, so the third entry exceeds
`1/40>29/1352`. The fourth entry `7/45` is larger as well.

Any initially full module costs at least `1/4`, which exceeds the first two
entries. Neither all-cold order meets the deadline: their exponential total
times are respectively

    exp(T_AB)=1352/441>3,
    exp(T_BA)=88/27>3.

These comparisons exhaust all concentrated states and all serial orders;
concentration and seriality then exclude every other initial distribution or
post-request allocation policy. Thus the exact global upkeep is `C_*`, attained
at

    p_A=0,
    p_B=(26*sqrt(2)-21*sqrt(3))/10,

with **cold A first, partial B second**. These preparations satisfy their
bounds. The best rule restricted to transferring its ready set and processing
its partial module first instead gives `29/1352`, strictly worse.

This is a global-maintenance separation, not merely two different exit orders
for one prescribed state. It proves why the common-rate partial-first formula
cannot be reused unchanged even though the one-partial concentration theorem
extends to unequal rates. The preceding cold module has the larger loss
coefficient, consistent with the prefix condition in pass 11.

## 8. Scientific status

The unequal-rate proportional problem now has an explicit finite frontier,
including inaccessible cold starts, and a matching initialized normal policy.
The remaining algorithmic questions concern simplification and exact numerical
representation, not an uncharacterized continuous optimization.

Neither this extension nor the common-rate result has established publication
novelty. The underlying arbitrary-partial serial reduction, concentration
exchange, and cold-prefix structure require a theorem-level prior-art
comparison. The independent-service and update-envelope restrictions remain
those of the model; no empirical safety or submission-readiness claim follows
from the exact formulas.
