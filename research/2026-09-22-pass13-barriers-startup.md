# Pass 13: rate barriers, the eventual upkeep floor, and cold startup

22 September 2026. This note characterizes finite-exit feasibility and the
eventual deadline/upkeep plateau for positive proportional loss. It also
separates paid initialized readiness from readiness that can be reached after
a finite cold warmup under the prescribed normal load. The threshold-closure
calculation is elementary; no novelty claim is made for threshold activation,
scalar equilibrium barriers, or bounded-storage averaging.

The [unequal-decay concentration note](2026-09-22-pass11-unequal-decay.md) was
read in full for this pass. Its local exchange and all-budget extension are
consistent with the results below. The closure and plateau proofs themselves
need positive proportional losses and the full-state serial theorem, rather
than the stronger conclusion that every cost minimizer has at most one partial
coordinate. This is an internal analytic check, not external review.

## 1. Model and notation

Use the instantaneous independent-transfer model with finitely many modules,

    M_i>0,  gamma_i>0,  a_i>=0,  s>=0,
    g_i(p)=gamma_i*p,  d_i=gamma_i*M_i>0.

All parameters are finite. Here `d_i` denotes the loss at **full** preparation;
it is not the constant-loss law of the earlier fixed-rate model. Actual losses
satisfy `0<=rho_i(t)<=gamma_i*p_i(t)`, and simultaneous maximum feedback is
allowed. Once a full module transfers, it stops losing preparation and releases
`a_i` immediately. A transferred set `S` gives capacity

    b(S)=s+sum_{i in S} a_i.

Before a request no module transfers, so preparation and nonnegative optional
work share the fixed normal budget `s`. Independent receiver resources, a
sufficient transfer state, instantaneous ownership transfer, and the absence
of cross-module barriers remain assumptions.

Write `F(p)` for the exact robust exit time from an arbitrary initial vector.
Let `F_cold(S)` denote this time when precisely `S` is full and the rest cold,
with `S` transferred immediately. The value may be infinity. For each finite
`H>=0`, the attained minimum maintenance cost is

    C(H)=min_{F(p)<=H} sum_i gamma_i*p_i.

The full-state smooth theorem proves compactness of the ready set and
attainment of this minimum. It also proves that indefinite all-request-time
readiness with paid initialization is feasible exactly when `C(H)<=s`, with
maximum guaranteed optional rate `s-C(H)`.

## 2. A closure test decides whether any finite exit is possible

For a proposed initially full seed set `S`, start with `C_0=S` and repeatedly
add every currently eligible module:

    C_{r+1}=C_r union {i not in C_r : b(C_r)>d_i}.

The iteration stabilizes after at most `n` strict enlargements. Denote the
result by `Cl(S)`. The strict inequality is essential: equality is a finite-time
barrier, not an eligible stage.

The same result is obtained by adding eligible modules one at a time, in any
order, until none remains. Nonnegative releases make the operation monotone.
Every sequentially added module lies in the parallel iteration's terminal
set, while every terminal sequential set is closed and contains the seed.
The parallel iteration is the least such closed set, proving order independence.
The same argument gives monotonicity and idempotence:

    S subset T implies Cl(S) subset Cl(T),
    Cl(Cl(S))=Cl(S).

**Theorem 1 (finite-exit test).** For every initial state `p`, let
`S(p)={i:p_i=M_i}`. Then

    F(p)<infinity  if and only if  Cl(S(p))=N.                (1)

In particular, arbitrarily large but strictly partial initial preparation
cannot bypass a rate barrier.

**Proof.** Transfer the initially full modules immediately. At capacity `b`,
a subfull module can reach `M_i` under maximum loss in finite time exactly when
`b>d_i`. Its full-rate flow has equilibrium `b/gamma_i`; if that equilibrium
is below `M_i`, it cannot reach the target from below, and at equality the
target is approached only asymptotically. This includes a subfull initial state
above the lower equilibrium: its maximum possible drift is then negative, so
it cannot climb to `M_i`.

The full-state serial theorem supplies a finite serial exit whenever any finite
robust exit exists. Every subsequent module in such an order satisfies the
strict eligibility test, so closure contains all modules. Conversely, a closure
ordering supplies eligible full-rate stages. Each stage takes finite time from
any subfull starting value, even from zero, and smaller loss cannot delay it.
The resulting serial policy is a robust finite exit. This proves (1).

For reference, the exact cold values can be computed separately by

    F_cold(N)=0,
    F_cold(S)=min over i not in S with b(S)>d_i of
        {log[b(S)/(b(S)-d_i)]/gamma_i + F_cold(S union {i})}.

An empty or wholly infinite minimum is infinity. Closure tests whether this
value is finite; it does not replace the calculation of its deadline.

## 3. The eventual upkeep floor is attained at a finite deadline

Call `S` a successful seed when `Cl(S)=N`, and define

    D_inf=min_{Cl(S)=N} sum_{i in S} d_i.                    (2)

The family is finite and nonempty because `N` is a successful seed. Its
minimum is attained. The notation describes an eventual finite-deadline floor;
it does not permit an infinite-time exit or silently change the readiness
contract to asymptotic completion.

**Theorem 2 (exact eventual plateau).** Let

    H_star=min {F_cold(S): Cl(S)=N,
                           sum_{i in S}d_i=D_inf}.          (3)

Then `H_star` is finite, and for every finite `H>=0`,

    C(H)>=D_inf,
    C(H)=D_inf  if and only if  H>=H_star.                  (4)

At a plateau deadline, every minimizing vector is a pure full/cold state:
its full set is a minimum-cost successful seed meeting that deadline.

**Proof.** If `p` is ready for any finite deadline, Theorem 1 makes its full
set `S(p)` a successful seed. Hence

    sum_i gamma_i*p_i
      = sum_{i in S(p)}d_i + sum_{i not in S(p)}gamma_i*p_i
      >= D_inf.

Every minimum-cost successful seed has a finite `F_cold(S)`, so (3) is an
attained finite minimum. Its full/cold state has cost `D_inf` and meets every
deadline at least `H_star`, proving one implication in (4).

Conversely, if `C(H)=D_inf`, choose an attained minimizing state. Its successful
full seed already costs at least `D_inf`; since all coefficients are strictly
positive, equality leaves no positive preparation outside that seed. The state
is therefore full/cold, its seed costs exactly `D_inf`, and its cold exit time
is at most `H`. Thus `H>=H_star`. This also proves the assertion about every
plateau minimizer. No unattained infimum can create an earlier plateau.

For example, if cold exit is finite, the empty seed is successful. Because
each `d_i>0`, it is the unique zero-cost seed. Thus `D_inf=0` and
`H_star=F_cold(empty)`. If cold exit is blocked, then `D_inf>0`.

## 4. Blocked cold exit consumes at least the entire spare budget

Let

    K=Cl(empty),  R=N\K.

Suppose `R` is nonempty, so cold exit is not finite. Since `K` is closed,

    d_i>=b(K)>=s  for every i in R.                          (5)

Every successful seed intersects `R`. Otherwise it is a subset of `K`, whose
closure remains within `Cl(K)=K`. Consequently,

    D_inf>=b(K)>=s.                                         (6)

This is stronger than a positive seed-cost claim. If any positively releasing
module belongs to `K`, then `b(K)>s` and the eventual floor exceeds the entire
normal spare budget.

**Corollary 3 (optional work and initialized feasibility).**

- Some finite deadline admits indefinite initialized readiness exactly when
  `D_inf<=s`.
- Some finite deadline admits a strictly positive guaranteed optional rate
  exactly when `s>0` and cold exit is finite.
- If cold exit is blocked and `D_inf>s`, no finite deadline admits indefinite
  readiness, even with paid initialization and zero optional work.

The first statement follows by combining the plateau with `C(H)<=s`. For the
second, finite cold exit permits the always-cold normal policy at optional rate
`s`, with any deadline at least `F_cold(empty)`. Conversely, a positive optional
rate needs `C(H)<s`, which contradicts (6) when cold exit is blocked; it also
needs `s>0` because optional allocations are nonnegative and budget limited.

There is an exact description of the remaining equality case. If cold exit is
blocked and `D_inf<=s`, choose a minimum seed. It contains a residual module
whose cost is at least `b(K)>=s`; every other seed member has strictly positive
cost. Equality therefore forces

    D_inf=s=b(K),
    S={i} for a residual module i with d_i=s.                 (7)

Every minimum seed is such a singleton. For any finite deadline, initialized
indefinite readiness in this blocked case is thus possible exactly when

    there exists i with d_i=s and F_cold({i})<=H.            (8)

Its exact optional rate is zero. Every minimizing readiness vector at such a
deadline has only that one full module and is cold elsewhere. If no singleton
meets the deadline, `C(H)>s`. This conclusion uses actual finite exit values,
not merely the existence of a successful seed.

## 5. A blocked cold system cannot reach finite-exit readiness by normal warmup

Now require cold initial preparation and a finite warmup during which all
prescribed normal service continues. No module may transfer during warmup,
so capacity remains `s`, regardless of any module becoming ready. Optional
work may be turned off. The deadline guarantee begins only after warmup;
requiring it from the cold initial instant is a stronger contract.

On the allowed maximum-loss history, each coordinate obeys the scalar bound

    p_i(t)<= (s/gamma_i)*(1-exp(-gamma_i*t)).                 (9)

This follows by comparison with allocating the whole normal budget to that
coordinate; upper reflection can only reduce the resulting value. If
`d_i>=s`, equation (9) is strictly below `M_i` at every finite time when `s>0`.
For `s=0`, the coordinate remains zero and is likewise subfull.

If cold exit is blocked, every residual module in (5) has `d_i>=s`. None can
be full after any finite warmup on this history. Thus the full set at every
finite warmup time is a subset of `K`, and its closure is a subset of `K`.
Theorem 1 then gives infinite robust exit time from that state, no matter how
close its residual partial preparations are to full.

**Theorem 4 (robust cold-start obstruction).** If `Cl(empty)!=N`, no finite
normal-budget warmup can guarantee arrival at any state with a finite robust
exit deadline. This is a statement against the allowed maximum-loss history;
benign loss histories can behave differently. It applies in particular to the
initialized zero-optional singleton states in (8), which cannot be prepared
from cold in finite time under that same normal budget.

Conversely, if cold exit is finite, the cold state already meets every deadline
`H>=F_cold(empty)`. Leaving preparation at zero preserves that readiness during
normal operation and makes all spare capacity optional. No warmup is needed
for those deadlines. This does not by itself decide shorter-deadline startup.

## 6. Strict maintenance slack suffices for finite normal warmup

There is a general sufficient condition for a specified deadline, including
shorter deadlines when cold exit is finite.

**Theorem 5 (finite warmup with strict slack).** If `C(H)<s`, a finite warmup
from cold under the prescribed normal load can reach a target from which
indefinite all-request-time readiness for `H` is maintained.

**Proof.** Choose an attained minimizing target `p^*` and write `C=C(H)`. If
`C=0`, positivity of all `gamma_i` makes the target cold, so no warmup is needed.
Otherwise choose one `kappa>1` with `kappa*C<=s`. For each positive target
coordinate, initially allocate the constant boost

    v_i=kappa*gamma_i*p_i^*.

Under maximal loss the coordinate follows
`p_i(t)=kappa*p_i^*(1-exp(-gamma_i*t))` until it first reaches its target.
This happens at the finite predetermined time

    t_i=log[kappa/(kappa-1)]/gamma_i.

At that time reduce its allocation to `gamma_i*p_i^*`. Give zero allocation
to coordinates with zero target. The total allocation is always at most
`kappa*C<=s`, so all normal service continues within its stated budget. Each
target is reached by `T=max_{p_i^*>0} t_i`. Smaller loss reaches at least the
same preparation at each prescribed switch and cannot subsequently lower it
below the target. The argument includes a full target and upper reflection.

After warmup, keep the maintenance allocations and use optional rate `s-C`.
Scalar comparison and the target's robust exit policy guarantee the deadline
at every subsequent request. No such guarantee has been asserted during the
warmup itself. The warmup is finite and paid, rather than free initialization.

Strict slack is not a general necessity condition. The blocked cold case has
the impossibility above, but the subsequent
[critical-startup theorem](2026-09-22-pass14-critical-startup.md) classifies
finite cold reachability of each concentrated target at `C(H)=s` and gives
globally certified critical-budget examples with opposite startup outcomes.
Unequal coefficients can permit finite warmup at equality. That target
classification does not decide reachability of an arbitrary ready region.
In the common-coefficient case, the aggregate bound
`Q(t)<=s*(1-exp(-gamma*t))/gamma` rules out finite cold warmup at a positive
critical target: every ready state would require `gamma*Q>=C(H)=s`.

## 7. Exact boundary examples

**A critical singleton is maintainable but cannot be started cold.** Take one
module with `M=gamma=s=a=1`. Its full loss is `d=1=s`. Cold closure is empty,
the only successful seed is the full module, and

    D_inf=C(H)=1 for every finite H>=0,  H_star=0.

Paid full initialization permits zero optional work and instantaneous exit.
But cold normal preparation is at most `1-exp(-t)<1` for every finite time.
From any subfull state `p_0`, the full-rate post-request flow is
`1-(1-p_0)*exp(-t)<1` at every finite time as well.
An arbitrarily generous finite deadline does not remove this equality barrier.

**A below-threshold singleton cannot sustain readiness.** Keep
`M=gamma=a=1`, but set `s=1/2`. Again `D_inf=C(H)=1` at every finite deadline.
Now `D_inf>s`, so even paid full initialization cannot support indefinitely
ready normal operation. Negative optional throughput is not a feasible rate.

**A release cascade can make cold readiness free.** Take

    gamma_1=gamma_2=1,  s=1,
    (M_1,M_2)=(1/2,3/2),  (a_1,a_2)=(1,1).

Module 1 is eligible at capacity one; its release makes module 2 eligible at
capacity two. Thus cold closure is all modules, even though the second module
cannot be fully prepared from cold while normal capacity remains one. The
unique eligible first stage is module 1, and exact cold exit takes

    log[1/(1-1/2)] + log[2/(2-3/2)] = log(8).

Therefore `D_inf=0`, `H_star=log(8)`, and deadlines at least `log(8)` permit
optional rate one with no normal preparation or warmup. Replacing closure by
the stronger condition `s>max_i d_i` would incorrectly reject this instance.

## 8. Research scope and next question

These results give exact answers about finite-exit barriers, the earliest
eventual maintenance plateau, existence of positive optional throughput, and
robust startup when cold exit is blocked. They do not alter the model's
essential-service, independent-receiver, or instantaneous-release assumptions.
The thresholds are properties of the ideal proportional-loss model, not
implementation-independent laws of controller removal.

The plateau can be computed by checking successful seed subsets and their
minimum cold exit times; no claim of a polynomial-time seed-selection algorithm
or a new threshold-activation method follows. The strict-slack construction
provides a useful sufficient startup condition. Pass 14 subsequently resolves
the critical concentrated-target question and shows why maintenance equality
alone does not decide startup. General ready-region reachability remains
separate from both that target theorem and the common-coefficient obstruction.

Any publication claim must still distinguish the full-state scheduling,
concentration, and initialization conclusions from established scheduling,
maintenance, and control results. The present note records the exact model
consequences and their boundaries without asserting novelty certification.
