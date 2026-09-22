# Pass 14: critical-budget startup depends on which preparation can be banked

22 September 2026. The recurring frontier permits paid initialization of a
minimizing readiness state. That allowance cannot always be replaced by a
finite warmup from cold using the ordinary normal-operation budget. This note
settles concentrated fixed targets at exact maintenance equality and
gives two positive-deadline examples with `C(H)=s`: one can reach readiness
from cold in finite time, and the other cannot reach any ready state in finite
time.

The result is inside the same independent instantaneous-transfer fluid model.
It neither supplies an operational proportional-invalidation mechanism nor
claims publication novelty. In particular, a warmup interval below does not
come with the removal deadline guarantee; guaranteed deployment begins only
after warmup has finished.

## 1. Fixed-target startup question

There are finitely many modules, with sizes `M_k>0`, coefficients
`gamma_k>0`, and maximum-loss normal dynamics

$$p_k'=v_k-\gamma_kp_k,$$

upper-reflected at `M_k`. Inputs are nonnegative and measurable, and their
sum is at most the fixed spare capacity `s`. Normal operation starts cold.
No module transfers during warmup, so no reservation is released. Essential
service continues using its separately reserved resources. Optional normal
work may be set to zero; allowing it cannot help preparation. All smaller
losses `0<=rho_k<=gamma_k*p_k` are also allowed, and maximum feedback is a
simultaneous admissible history.

Fix a nonzero concentrated target: a fully ready set `S`, a partial module
`i` outside `S` with preparation `r` in `(0,M_i)`, and all other coordinates
zero. Write `d_j=gamma_j*M_j` and `beta=gamma_i`. Impose exact equality of
target maintenance and normal capacity:

$$s=\sum_{j\in S}d_j+\beta r>0.                          \tag{1}$$

The question is whether a deterministic causal normal policy can guarantee
reaching a state componentwise at least this target in finite time, without
preloaded preparation. Target allocations `v_k=gamma_k*p_k^*` maintain such
domination indefinitely once reached.

**Theorem (critical concentrated target).** Under (1), finite robust cold
reachability of a state dominating the target is possible if and only if

$$\text{some }j\in S\text{ has }\gamma_j>\beta.            \tag{2}$$

When `S` is empty, this condition is false. A nonzero target containing only
full and cold modules, with maintenance exactly `s`, is never reachable from
cold in finite time. The zero target is immediately reachable and is excluded
from these critical impossibility statements.

This classifies each particular concentrated target, not arbitrary
readiness-set reachability. It does not assert that every ready target must
be a minimizing target, or that an unreachable chosen target excludes all
other ready states.

## 2. Necessity: no slower-decaying partial reserve to use

Suppose every full module in `S` has coefficient at most `beta`. On the
allowed maximal-loss history, define the support total relative to target:

$$Z(t)=\sum_{j\in S}p_j(t)+p_i(t)
-\left(\sum_{j\in S}M_j+r\right).$$

Upper reflection only reduces its derivative. Allocations to coordinates
outside this support consume budget without increasing this total. Thus,
almost everywhere,

$$\begin{aligned}
Z'
&\leq s-\sum_{j\in S}\gamma_jp_j-\beta p_i\\
&=-\beta Z+\sum_{j\in S}(\beta-\gamma_j)(p_j-M_j)\\
&\leq-\beta Z,
\end{aligned}                                           \tag{3}$$

because each `p_j<=M_j`. Starting cold gives `Z(0)<0`, and integration yields
`Z(t)<=Z(0)*exp(-beta*t)<0` at every finite time. A state dominating the target
would have `Z>=0`. It is therefore unreachable, even with arbitrary
preemptive, parallel, or bursty normal controls. This allowed history also
rules out a robust finite-time guarantee.

For a nonzero full/cold target without a partial coordinate, choose
`beta_0=max_{j in S} gamma_j` and define `Z=sum_{j in S}(p_j-M_j)`. The same
calculation gives `Z'<=-beta_0*Z` when `s=sum_{j in S}d_j`. Hence `Z(t)<0`
for every finite time, which excludes completing the full target. This
handles the no-partial boundary separately rather than treating it as a
limiting case of (2).

## 3. Sufficiency: a strict-slack predecessor and one final interval

First record an elementary exact warmup fact. For any nonzero target vector
`z` in the physical box with

$$Q_z=\sum_kz_k>0,\qquad K_z=\sum_k\gamma_kz_k<s,$$

let `theta(0)=0` and use

$$\theta'=\frac{s-K_z\theta}{Q_z},\qquad
v_k=z_k(\theta'+\gamma_k\theta).                         \tag{4}$$

Until `theta=1`, allocations are nonnegative and sum exactly to `s`, and the
maximum-loss solution is `p_k=theta*z_k`. It reaches `z` at finite time

$$T_z=\frac{Q_z}{K_z}\log\frac{s}{s-K_z}.                 \tag{5}$$

Here `K_z>0` follows from positive coefficients and a nonzero target. No
coordinate exceeds its cap before that time; a target coordinate equal to
its cap reaches it at the terminal time. Under smaller losses, scalar
comparison instead reaches a vector at least `z` by the same time. The zero
target needs no warmup. Thus strict maintenance slack suffices for finite
robust reachability of any fixed target, not only concentrated ones.

Now assume (2), choose such a full module `j`, and write `alpha=gamma_j>beta`.
Keep every other full module's maintenance allocation fixed, leaving the
pair's capacity

$$b=d_j+\beta r.$$

Choose a positive interval length satisfying

$$\delta<\min\left\{
\frac1\alpha\log\frac{b}{\beta r},
\frac1\beta\log\frac{M_i}{r}\right\}.$$

Both bounds are strictly positive. Define a predecessor vector `z` by leaving
all other full and cold target coordinates unchanged and setting

$$z_j=\frac{b-\beta r e^{\alpha\delta}}{\alpha},\qquad
z_i=r e^{\beta\delta}.                                  \tag{6}$$

The bounds on `delta` ensure `0<z_j<M_j` and `r<z_i<M_i`. Its total
maintenance is

$$K_z=s+\beta r\left(e^{\beta\delta}-e^{\alpha\delta}\right)
<s.                                                       \tag{7}$$

Reach a vector at least `z` from cold using (4)–(5). Then for exactly `delta`
allocate `b` to module `j`, zero to `i`, and `d_l` to each other full target
module `l`. The aggregate allocation is exactly `s`. From the virtual
maximum-loss predecessor (6), direct solution of the two scalar equations
gives `p_j(delta)=M_j` and `p_i(delta)=r`; every other target coordinate is
unchanged. The j coordinate increases to its cap only at the end, while the
i coordinate decays toward `r` from above, so both trajectories stay in their
bounds. Thus the virtual trajectory reaches the original target exactly in
the finite total time `T_z+delta`.

Scalar comparison makes this schedule robust from the actual state at least
`z` and under smaller losses. A j coordinate arriving at its cap early stays
there because `b>d_j`; other full coordinates are held at their maintenance
allocations. At the end, switch to the original target's maintenance vector.
Its sum is `s`, and it preserves target domination indefinitely.

For two modules with a full target `(M,r)` and coefficients `(alpha,beta)`,
this theorem reduces to the exact criterion `beta<alpha`. The additional
preparation in the slower-decaying partial coordinate supplies the final
interval; no full module releases capacity during this normal warmup.

## 4. An exact globally optimal ready state at equality that is reachable

Take

$$s=1,\qquad H=\log(9/5),$$

with module parameters

| Module | Size | Loss coefficient | Released rate | Full maintenance |
|---|---:|---:|---:|---:|
| A | `2/5` | `2` | `1` | `4/5` |
| B | `1` | `1` | `1/10` | `1` |

The target

$$p_A^*=2/5,\qquad p_B^*=1/5                              \tag{8}$$

has maintenance cost exactly one. At a request, transfer A immediately.
The resulting capacity is two, and B's exact maximum-loss completion time is

$$\log\frac{2-1/5}{2-1}=\log(9/5)=H.$$

Thus `C(H)<=1`. To certify global equality, use
[unequal-rate concentration](2026-09-22-pass11-unequal-decay.md) and
full-state seriality. Every minimizing vector has at most one partial module.
The possibilities at cost less than one are exhausted as follows.

- Any initially full B already costs one, so it cannot occur in a cheaper
  vector.
- If A is initially full and B has preparation `q`, immediate A transfer
  leaves the single-module exit time `log(2-q)`. Meeting `H` requires
  `q>=1/5`, giving maintenance at least `4/5+1/5=1`.
- If neither module is full and only A is partial, B is cold. A must complete
  first, because a subfull B cannot reach full at initial capacity
  `s=gamma_B*M_B=1`. Even an instantaneous A completion would leave B's cold
  stage `log(2)>H`.
- If neither is full and only B is partial, A is cold and must complete first
  by the same B barrier. A's cold stage alone is `(1/2)*log(5)>H`, since
  `5>(9/5)^2`.

The all-cold vector is included in these infeasibility arguments. Hence no
cheaper minimizing vector exists and

$$C(H)=1=s.                                               \tag{9}$$

This uses all-policy seriality and concentration, not an unsupported search
over a few initial states. Cold exit itself is finite in this model: after a
request, cold A then cold B takes `(1/2)*log(5)+log(2)`. The obstruction at
shorter deadlines is readiness rather than an absolute inability to exit.

Here the partial target decays more slowly than the full target, so the
theorem applies. A particularly simple exact warmup is:

1. Allocate `(v_A,v_B)=(3/5,2/5)` for `T=log(10)`. Maximum-loss preparation
   becomes `(297/1000,9/25)`.
2. Allocate `(1,0)` for `(1/2)*log(203/100)`. A reaches `2/5`, and B retains

   $$\frac{18}{5\sqrt{203}}>\frac15,$$

   with strictness certified by `324>203`.
3. Switch to `(4/5,1/5)` indefinitely. Both coordinates remain at least the
   target under every admissible loss history.

The exact virtual warmup length is `(1/2)*log(203)`. Both source allocations
sum to the normal capacity one. All states respect their preparation bounds;
no module transfers and no release is used during warmup. After it finishes,
every requested removal meets `H`. Optional throughput is zero at this
critical budget, consistent with the exact recurring frontier.

## 5. An equally critical positive-deadline model where no ready state is reachable

For comparison take two identical modules with

$$s=1,\quad M_A=M_B=3/4,\quad
\gamma_A=\gamma_B=1,\quad a_A=a_B=1,\quad H=\log(7/5).$$

One full module and the other prepared to `1/4` have total maintenance one.
After immediate transfer of the full module, the remaining exit time is

$$\log\frac{2-1/4}{2-3/4}=\log(7/5)=H.$$

The common-rate concentration theorem gives `C(H)=1`. Explicitly, without
an initially full module, processing the partial module first leaves a cold
last stage of `log(8/5)>H`, while processing a cold module first already takes
`log(4)>H`. These alternatives also exclude the all-cold vector. With one
initially full module, meeting the deadline requires at least `1/4` on the
other. The all-full vector costs `3/2`. Thus a cheaper optimum is excluded.
Since the loss coefficient is one, every `H`-ready vector consequently satisfies

$$p_A+p_B\geq1.$$

But on the maximal-loss normal history from cold,

$$Q'= (p_A+p_B)'\leq1-Q,\qquad Q(0)=0,$$

so

$$Q(t)\leq1-e^{-t}<1$$

at every finite time. No normal policy can reach any `H`-ready vector in
finite time, not merely the displayed optimizing target. Cold post-request
exit remains finite: the serial time is `log(32/5)`. Both examples therefore
have positive deadlines, positive releases, positive spare capacity, and a
finite cold exit time.

## 6. Consequence for the initialization assumption

Exact maintenance equality `C(H)=s` does not decide finite cold startup.
Sections 4 and 5 give globally certified models with opposite answers. In the
first, excess preparation can be held in a slower-decaying partial coordinate
while a faster-decaying full coordinate finishes. In the second, the total
preparation inequality prohibits reaching the ready set in finite time.

The theorem in Sections 1–3 classifies each concentrated target in any finite
dimension but does not settle readiness-set reachability. A target
may be unreachable even when some other ready vector is reachable. Section 5
avoids that ambiguity by bounding every ready state's total preparation;
Section 4 avoids it by explicitly reaching a globally minimizing ready target.

Paid initialization remains a substantive allowance in the recurring frontier.
Where a finite normal warmup is provided, it can replace external preloading
only after accepting that the removal guarantee starts at the end of warmup.
The earlier impossible warmup histories are preserved; the equality cases
have not been redefined to manufacture a general startup guarantee.
