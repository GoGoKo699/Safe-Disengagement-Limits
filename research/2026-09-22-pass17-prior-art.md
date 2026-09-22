# Pass 17: a fixed-deadline nonlinear investment comparison

22 September 2026. Read against recovered main
`16dca7e14950e13e4a292600ee39b2a3aeca9ec1`, including the full current
`paper/math.tex`, `paper/related-work.tex`, and the pass-11 and pass-15
attribution records. This is a bounded theorem-level comparison, not a
literature-wide priority certificate.

## 1. Finding

An accessible nonlinear resource-allocation result does **not** absorb the
unequal-rate concentration theorem through either of two natural model
identifications. Its fixed-deadline feasible set is convex, whereas an S1
fixed-order deadline region can be nonconvex. Furthermore, a common smooth
change of time cannot turn S1's waiting-dependent initial preparation into
start-independent operation durations using coordinatewise investment
variables. Both statements below have explicit proofs.

These are concrete failures of specified reductions. They are not a proof
that no more elaborate reduction, earlier exchange theorem, or older
deterioration result exists. The inspection strengthens the focused residual
claim relative to this particular source; it does not establish submission
readiness or convert the exponential subset enumeration into a new algorithmic
principle.

## 2. Source and exact inspection scope

B.-C. Choi and M.-J. Park, *Two-machine flow shop scheduling with convex
resource consumption functions*, Optimization Letters **17**, 1241–1259
(2023), online 16 September 2022,
[publisher full text](https://link.springer.com/article/10.1007/s11590-022-01934-1),
[publisher PDF](https://link.springer.com/content/pdf/10.1007/s11590-022-01934-1.pdf),
DOI `10.1007/s11590-022-01934-1`.

**Inspected:** complete Sections 1–3; especially Section 2's model and Section
3, Lemma 3 and its complete proof, equations (10)–(11), printed pages
1247–1248. Lemma 4's proof and Corollary 1 were also read. Later complexity
and approximation proofs are not audited or used here. The
[2023 correction](https://link.springer.com/article/10.1007/s11590-023-01982-1)
changes access/licensing, not this mathematics.

The embedded fixed-deadline subproblem minimizes
\(\sum_j c_j u_j\), for positive \(u_j,c_j,w_j,k\), subject to
\(\sum_j(w_j/u_j)^k\leq\delta\). Its KKT proof gives
\(u_j=(\lambda k w_j^k/c_j)^{1/(k+1)}\).
The surrounding model chooses resource amounts and nonpreemptive operation
orders on two machines. This comparison uses the displayed subproblem itself,
not a claim that the full flow shop equals S1.

All necessary proof text was legitimately accessible without payment or
contact. Previously blocked Glazebrook endpoints were not retried. The
partial-access leads retained in pass 15 remain uninspected.

## 3. Feasible-set, objective, and quantifier comparison

The following are our mathematical comparison and deductions, not claims made
by Choi and Park about S1.

| Item | Inspected fixed-deadline subproblem | S1 problem being assessed |
|---|---|---|
| Decision | Positive investment vector \(u\) | Initial preparation \(p_i\in[0,M_i]\), then an exit policy |
| Deadline | Sum of durable durations \((w_j/u_j)^k\) | Worst-case exit time \(F(p)\leq H\) |
| Price | Linear \(c\cdot u\) | Linked upkeep \(\sum_i\gamma_i p_i\) |
| Control scope | Static investment in the displayed block | Causal parallel/preemptive allocations; seriality is proved |
| Quantifier | Deterministic block feasibility | Every allowed loss history, including simultaneous maximal feedback |

One should remove irrelevant differences before deciding the comparison. Set
all S1 releases to zero, work on maximum feedback, and use the established
seriality theorem. S1 then also has a deterministic fixed-order investment
problem. Thus neither uncertainty terminology nor permission to preempt is,
by itself, a novelty argument for the concentration theorem. The remaining
question is its investment/deadline geometry.

The natural identification of prices is \(u_i=p_i\), \(c_i=\gamma_i\),
possibly after positive affine rescaling and translation of individual
coordinates. It preserves a linear objective, but it fails to identify the
feasible sets. S1's initial investment continues decaying before its service
stage, whereas its usefulness in the displayed source subproblem is encoded
in a duration independent of the stage's start time. Sections 4–5 make this
failure precise, including a class of changes of clock.

The result in the source is also not a statement that all but one investment
lie on bounds. As an elementary check, take two terms, \(k=w_i=c_i=1\),
and \(\delta=2\). The problem is

\[
 \min(u_1+u_2),\qquad 1/u_1+1/u_2\leq2,
\]

whose unique optimum is \((1,1)\): the product of the two displayed sums is
at least four, with equality only when the coordinates agree. Both variables
are interior even if one adds inactive bounds \(1/2\leq u_i\leq2\).
This example is a deduction from that optimization model, not a counterexample
to S1: the models have different feasible sets. It also reinforces the
existing attribution that dispersed allocations under nonlinear resource
laws are familiar. The quadratic S1 example is useful specifically because
it locates a boundary of S1's concentration theorem while retaining seriality.

## 4. An exact nonconvex S1 fixed-order region

Consider an S1 instance with

\[
 s=3,\quad a_1=a_2=0,\quad M_1=M_2=1,\quad
 \gamma_1=2,\quad\gamma_2=1,\quad H=\log2.
\]

Every cold stage is accessible. For initial states \((x,y)\in(0,1)^2\)
and prescribed order \(1,2\), the proportional stage equations give

\[
 e^{2t_1}=3-2x,
 \qquad
 e^{t_2}=\frac{3\sqrt{3-2x}-y}{2}.
\]

Consequently the fixed-order deadline constraint is

\[
 y\geq 3\sqrt{3-2x}-4. \tag{1}
\]

Two states meeting the deadline with equality are

\[
 P=(13/25,1/5),\qquad Q=(3/8,1/2).
\]

Their midpoint is \(R=(179/400,7/20)\). For \(R\) to satisfy (1),
one would need

\[
 3\sqrt{421/200}\leq87/20.
\]

Both sides are positive, but their squared values are respectively
\(7578/400\) and \(7569/400\), so the inequality fails. The fixed-order
feasible region is nonconvex, strictly inside the preparation box and away
from all accessibility or full-transfer boundaries.

In contrast, for \(k>0\), each function \(u\mapsto(w/u)^k\) has strictly
positive second derivative on \(u>0\). Its sum has convex sublevel sets.
Affine inverse images and affine sections of convex sets are convex.
Therefore no affine change of investment coordinates can exactly identify
this S1 fixed-order feasible set with the inspected fixed-deadline subproblem,
even if extra affine bounds or fixed coordinates are allowed.

This statement is deliberately restricted to the proposed fixed-order
identification. It does not claim that the displayed midpoint fails every
S1 order, or that the global ready set has this exact two-dimensional
description. A finite union over orders and arbitrary nonlinear coupled
encodings are not ruled out by a convexity observation.

## 5. Why a common change of clock does not yield durable durations

Here is a broader, still explicitly delimited obstruction. Fix one accessible
S1 stage with \(\gamma,M>0\), capacity \(b>\gamma M\), and
\(D=b-\gamma M>0\). A module having initial preparation \(p\in(0,M)\)
and starting service at global time \(t\geq0\) completes at

\[
 T(t,p)=\frac1\gamma\log\frac{b e^{\gamma t}-\gamma p}{D}. \tag{2}
\]

**Claim.** There is no \(C^1\) common clock \(f:[0,\infty)\to\mathbb R\)
with \(f'>0\), and differentiable function \(h\) on an open preparation
interval \(I\subset(0,M)\), such that

\[
 f(T(t,p))-f(t)=h(p) \tag{3}
\]

for all \(t\geq0\) and \(p\in I\). In particular, composing any
coordinatewise differentiable investment map with a start-independent
duration law does not supply such an identity.

**Proof.** Differentiate (3) in \(p\), using
\(T_p=-1/(D e^{\gamma T})\):

\[
 f'(T)e^{-\gamma T}=-D h'(p). \tag{4}
\]

For each fixed \(p\), \(T(t,p)\) continuously increases to infinity as
\(t\) ranges from zero to infinity. Thus the left-hand function in (4)
is constant on a ray. All such rays overlap, so a common constant \(K>0\)
satisfies \(f'(z)=K e^{\gamma z}\) for all sufficiently large \(z\).
Choose \(t\) large enough that both \(t\) and \(T(t,p)\) lie in that ray.
Differentiating (3) in \(t\) then gives

\[
 0=f'(T)T_t-f'(t)
   =K e^{\gamma t}(b/D-1)>0,
\]

because \(T_t=b e^{\gamma t}/(D e^{\gamma T})\) and \(b>D\).
This contradiction proves the claim.

The domain and scope matter. The claim concerns a single common physical
clock and preparation variables chosen before waiting, over all start times
and an open interval of preparation. It does not exclude transformations
depending on the entire schedule, auxiliary variables, finitely sampled
identities, or reductions tailored to a single deadline. Nor does it
contradict the exact common-rate affine-deterioration reduction from pass 11:
that transformed model **retains** start-time dependence and therefore does
not satisfy (3).

No unequal-rate assumption was needed for this obstruction. Its purpose is
to distinguish perishing initial preparation from durable controllable work,
not to claim a new unequal-rate theorem by changing terminology.

## 6. Consequence for the paper and the next decision

Relative to the inspected nonlinear fixed-deadline KKT result, the central
S1 theorem is a materially different structural statement: every minimizing
initial vector has at most one partial coordinate despite nonlinear,
potentially nonconvex fixed-order constraints. The source result does not
prove it under the tested identifications. The S1 proof instead uses the
linked prices \(\gamma_i\) in its two-coordinate strict concavity/decreasing
derivative dichotomy. This is precisely the residual result to assess; it is
not a claim of first use of exchange arguments, first scheduling with
nonlinear investment, or first concentration under any deterioration model.

The new comparison can be incorporated in the paper in a short paragraph,
citing Lemma 3 and explaining the geometry. The auxiliary non-reduction
proofs belong in this audit record unless a referee specifically needs them;
they should not displace the central theorem. All exact prior-art reductions
already established in pass 11 remain in force.

No repeated blocked-source search is justified merely to obtain a more
favorable verdict. The outstanding questions remain whether another
accessible theorem genuinely contains the pair exchange, and whether the
ideal preparation/transfer contract merits a standalone paper. Progress on
the operational assumption audit is more valuable now than adding further
capacity parameters. Mathematical correctness, attribution, operational
meaning, and the compiled artifact remain separate gates.
