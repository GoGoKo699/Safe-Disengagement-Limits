# Passive commitments and uniform safe exit

**22 September 2026 — a research benchmark, not a novelty-certified result.**

## 1. Scope and physical accounting

An optional activation can create service that becomes mandatory once it has
been initiated. This note asks for useful long-run activity while preserving the
ability to retire the primary provider at every possible request time. It is a
proposed mathematical model, not a literal reconstruction of the fiction.

There is one fungible, storable resource, such as a fluid inventory or idealized
energy supply. We do **not** assume that arbitrary computational throughput or
human expertise can be stored in a battery.

* `C` is the total service rate available while the primary is available. It is
  not `C+B`; independent capacity must not be counted twice.
* `B` is service supply available independently after the primary departs.
* `E` is a separately counted, initially full, independent reserve stock. It is
  held intact during ordinary operation and the grace period in this model.
  It is lossless, with no charge or discharge rate limit. After departure it
  may be recharged only from unused `B`; overflow may be discarded. The
  attaining policy below does not require recharge.
* `H` is the maximum cooperative grace period after a retirement request.
  The primary is completely absent afterward. `H=0` is immediate removal.
* Any unrelated baseline essential service is outside these residual budgets
  and must have its own independent provision. New optional admissions may
  stop at a request, but none of the induced obligations may be dropped.

An operational application would have to justify these idealizations and include
inventory losses, finite discharge power, constraints on independent control,
and any missing essential-service obligations. They are not established here.

We assume perfect knowledge of demand profiles and a cooperative, fully reliable
primary during the grace period. Independence includes the sensing and control
needed to operate the reserve, not merely possession of its material contents.
Repeated shutdown-and-restart cycles and reserve restoration are not modeled.

## 2. Mathematical model

Let `g: [0,infinity) -> [0,infinity)` be measurable and integrable, with

    0 < G0 := integral_0^infinity g(a) da < infinity.

One unit of activation creates demand rate `g(a)` at age `a`. The profile is
fixed: service cannot be advanced, delayed, cancelled, or changed by a control
intervention. `g` need not decrease.

Let `u(t)` be a nonnegative measurable admission rate, globally bounded by some
finite constant. There is no prescribed common admission-rate ceiling, but an
application may add one. History is empty before time zero. Nominal demand is

    D(t) = integral_0^t u(s) g(t-s) ds.

Nominal feasibility requires `D(t) <= C` almost everywhere. For each request
`tau >= 0`, all new admissions stop, and the residual demand at elapsed time `h`
is

    d_tau(h) = integral_0^tau u(s) g(tau+h-s) ds.

The primary can serve this residual until time `tau+H`. Afterward the independent
rate and reserve must meet every demand at its prescribed time. For example,
with an independent rate `B`, inventory `e` obeys an ideal storage balance,
`0 <= e <= E`, permitting spillage when full; no uncounted replenishment is allowed.

The exit guarantee is counterfactual at every time: on the no-retirement nominal
history, **each** `tau` must admit such a safe transition. It is not a guarantee
only for a chosen convenient date. Resource feasibility is deterministic, not
an expectation or a probability-of-success statement.

The objective is upper long-run average admission:

    lambda_bar(u) = limsup_{T -> infinity} (1/T) integral_0^T u(t) dt.

This admits nonstationary and bursty histories, including ones with no ordinary
Cesaro limit. A randomized policy satisfying the resource requirements pathwise
also satisfies the upper bound pathwise; no expected-performance extension is
being asserted.

Define

    G(h) = integral_h^infinity g(a) da,
    Q_H(s) = integral_H^(H+s) G(h) dh.

`G` is nonincreasing even when `g` is not. `Q_H(s)` is finite for finite `s`, since
`Q_H(s) <= s G0`.

## 3. Theorem: exact maximum admission rate

For finite nonnegative `C,B,E,H`, define (the loss-of-capability interpretation
normally has `B<=C`, although the algebra does not require this)

    L_exit = inf_{s>0: Q_H(s)>0} (E+B*s)/Q_H(s),
    lambda_* = min(C/G0, L_exit).

An empty infimum is `+infinity`. Then:

1. Every nominal history uniformly safe for retirement has
   `lambda_bar(u) <= lambda_*`.
2. Constant admission `u(t)=lambda_*`, starting from empty history, is nominally
   feasible and uniformly retirement-safe, so the bound is attained.

Thus burstiness and history-dependent admission cannot increase the optimum
in this particular model. This conclusion is not asserted once the controller
can change the profiles themselves.

The same stationary frontier can be expressed as

    F(lambda;B,H) = integral_H^infinity [lambda G(h)-B]_+ dh,
    lambda_* = max{lambda >= 0: lambda G0 <= C and F(lambda;B,H) <= E}.

The integral is an extended nonnegative integral; in particular `F(0;B,H)=0`,
including when an unweighted tail moment is infinite.

### 3.1 Convolution averaging lemma

Suppose `u >= 0` is globally bounded, `w >= 0` is integrable, and
`(u*w)(t) <= K` almost everywhere for `t >= 0`, with empty initial history.
Then

    lambda_bar(u) integral_0^infinity w(a) da <= K.

Proof. Let `A(T)=integral_0^T u(t)dt` and fix `M>0`. Tonelli's theorem gives,
for `T>M`,

    integral_0^T (u*w)(t)dt
      = integral_0^T u(s) [integral_0^(T-s) w(a)da] ds
      >= A(T-M) integral_0^M w(a)da.

The left side is at most `KT`. Global boundedness of `u` implies
`|A(T)-A(T-M)|/T <= M ||u||_infinity/T -> 0`. Divide by `T`, take the limsup,
and then let `M -> infinity`. This proves the claim without assuming a mean
limit exists or an age moment of `w` is finite.

### 3.2 Upper bound for arbitrary histories

Apply the lemma with `w=g` and `K=C` to obtain `lambda_bar G0 <= C`.

Now fix any finite `s>0`. After the primary departs, the mandatory resource
needed in the next `s` units of time cannot exceed `E+B*s`. This is a necessary
condition even if the reserve is full at departure and perfectly controllable:

    integral_H^(H+s) d_tau(h) dh <= E+B*s, for every tau.

By Tonelli this is `(u*w_H,s)(tau) <= E+B*s`, where

    w_H,s(a) = integral_H^(H+s) g(a+h) dh,  a >= 0.

This kernel is integrable and its total mass is `Q_H(s)`. The lemma yields

    lambda_bar Q_H(s) <= E+B*s.

Taking all `s` gives `lambda_bar <= L_exit`. This upper bound does not assume
that the residual demand of an arbitrary nonstationary history is monotone.
It gives the fallback every allowed benefit, including a full reserve.

### 3.3 Matching construction from empty history

For `u(t)=lambda`,

    D(t) = lambda integral_0^t g(a) da <= lambda G0,
    d_tau(h) = lambda integral_h^(h+tau) g(a) da <= lambda G(h).

The main resource can therefore handle the grace period whenever
`lambda G0 <= C`. After it departs, use independent supply up to the actual
demand (at most `B`) and draw the positive remainder from the reserve.
The total stock draw is bounded by

    integral_H^infinity [lambda G(h)-B]_+ dh = F(lambda;B,H).

No recharging, advance service, or continuing primary action is needed.

Since `G` is nonincreasing, `lambda G(h)-B` crosses zero at most once, up to
flat portions. Consequently

    F(lambda;B,H)
       = sup_{s>=0} {lambda Q_H(s)-B*s}.

This identity includes infinite values. The inequalities defining `lambda_*`
ensure that the supremum is at most `E`. Thus the construction attains the
upper bound, with no assumption of an actual infinite predeployment history.

For a fixed constant admission rate, `F` is also the exact stock required
uniformly over all `tau`. Its necessity follows from the upper-bound argument,
or by letting `tau` increase in each finite-prefix inequality.

### 3.4 Why prefix deficits alone are not a general certificate

For a general nonstationary residual, starting-full storage with capacity `E`
requires checking deficits across all subintervals, not only prefixes from
departure. Earlier surplus may have spilled from a full reservoir.

Discrete counterexample: demand in consecutive slots `[0,2]`, independent
supply `B=1`. Every prefix has cumulative demand at most cumulative supply,
so the prefix bound suggests `E=0`. But one unit of storage is actually needed
for the second slot. With zero capacity, first-slot surplus is lost.

Our theorem uses prefixes only for a necessary upper bound. Sufficiency is
proved by dominance by a monotone stationary envelope, not by falsely applying
a prefix-only sufficiency test to every possible history.

## 4. Fixed-duration commitments

Let `g(a)=1` for `0<=a<L`, and zero otherwise. Each unit of admitted activity
requires one unit of service rate for duration `L`. Set `d=(L-H)_+`.
For `lambda>0`,

    G(h)=(L-h)_+,
    F(lambda;B,H) = [(lambda d-B)_+]^2/(2 lambda).

The shape is triangular: after admissions stop, the committed population
shrinks linearly under constant admission. The stock covers the area above
independent supply.

If `d>0`, the exact frontier is

    lambda_* = min(C/L,
        [B d + E + sqrt(E^2+2 B d E)] / d^2).

Special cases: `B=0` gives `lambda <= 2E/d^2`; `E=0` gives `lambda <= B/d`.
If `H>=L`, all these commitments expire before departure and
`lambda_*=C/L` even when `B=E=0`.

Example: `L=10`, `H=2`, `C=10`, `B=2`. Admission rate `lambda=1` creates
steady nominal demand 10. At departure, residual steady-envelope demand is 8;
18 units of reserve suffice and are necessary uniformly over deployment age.
With `E=0`, the maximum rate is instead `1/4`, even though ordinary capacity
alone permits rate 1. These numbers are dimensionless model quantities, not
an estimate for real infrastructure.

## 5. Finite ordinary resource does not imply finite exit stock

With `B=0`, Tonelli yields

    F(lambda;0,H) = lambda integral_H^infinity (a-H) g(a) da.

Nominal load is controlled by `integral g`. Uniform stock for retirement is
controlled by a different, age-weighted integral. For fixed finite `H`,
finite `G0` does not imply that this age-weighted quantity is finite.

Compare two deterministic profiles with the same total ordinary resource:

    g_short(a)=exp(-a),
    g_long(a)=1/(1+a)^2.

Both have `g(0)=1` and `G0=1`. At constant admission `lambda`, both approach
the same nominal demand `lambda`. With `B=0`, request age `tau`, and grace `H`,
the exact remaining stock demands are respectively

    E_short(tau)=lambda exp(-H)(1-exp(-tau)),
    E_long(tau)=lambda log[(1+H+tau)/(1+H)].

The first is uniformly bounded, while the second grows without bound. Every
finite-age request in the second system still has a finite stock requirement.
What fails is one finite reserve serving all possible ages of an indefinitely
productive deployment.

The theorem proves more than failure of a constant-rate design: with `g_long`,
finite `E`, finite `H`, and `B=0`, **every** uniformly exit-safe bounded admission
history has zero upper long-run average. This does not forbid infinitely many
admissions at a sublinear cumulative rate, or time-varying reserve budgets.

For `B>0`, the same profile has finite stationary reserve requirement. Let
`c=1+H`. If `lambda <= Bc`, it is zero. Otherwise,

    F(lambda;B,H) = lambda log[lambda/(Bc)] - lambda + Bc.

Thus positive continuing independent supply removes the divergence for a
fixed throughput, but the required stock grows as `B` tends to zero. A finite
battery and a permanent independent supply are not interchangeable resources.

The distinction is not only an infinite-support pathology. For finite `R>0`,
normalize a truncated profile as

    g_R(a) = [(1+R)/R] (1+a)^(-2) 1_{0<=a<=R}.

Every such profile has `G0=1` and finite support. At `H=B=0`,

    F(lambda;0,0) = lambda [(1+R)/R]
                         {log(1+R)+1/(1+R)-1},

which is unbounded as `R` grows. Thus no upper bound depending only on ordinary
per-activation resource `G0` can bound required stock across these profiles.

More generally, for `g(a)=(1+a)^(-alpha)`, `alpha>1`, finite nominal resource
requires only `alpha>1`, whereas finite stock with `B=0` at positive throughput
requires `alpha>2`. No stochastic or expected-lifetime interpretation is used.

## 6. Interpretation and publication status

The theorem identifies a concrete diagnostic: aggregate steady operating load
alone is insufficient to certify removal. The remaining age-profile of
noncancellable obligations matters. It also separates an independent rate,
a stored stock, and a cooperative grace period.

The stationary frontier corresponds to established network calculus
(see `LITERATURE.md`); the throughput upper bound adds elementary averaging. These facts are a
reason to retain the result as a baseline, not to declare a novel paper.

The critical model limitation is that the primary cannot change `g`. It merely
stops initiating work and waits. A genuinely different control problem would
allow limited, operationally justified conversion of existing obligations to
independent support, with conversion consuming resources also used for ordinary
service. No theorem or novelty claim for that extension is proved here.

## 7. Verification scope

`verify.py` checks finite discrete kernels, all ternary periodic admission
patterns of periods 1 through 4, every phase of withdrawal, several grace
periods and backup rates, and exact storage feasibility. It separately checks
the continuous triangular formula using rational arithmetic. The discrete
cutoff convention is after the current admission and before service in its
slot; it is not a silent numerical approximation of continuous time.

The proof above is analytical. Finite checks can expose algebra, indexing,
or certificate errors, but cannot establish the continuous-time theorem,
validate a real application, or certify novelty.
