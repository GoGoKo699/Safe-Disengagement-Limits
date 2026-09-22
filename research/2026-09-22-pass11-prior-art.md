# Pass 11: concentration, controllable work, and the remaining attribution boundary

22 September 2026. This bounded audit began from committed main
`6400737695eba9091389859724f783e03d8c1e8f`. It reads the complete
[pass-10 frontier](2026-09-22-pass10-proportional-frontier.md), including its
quadratic counterexample, and the complete
[pass-11 unequal-decay theorem](2026-09-22-pass11-unequal-decay.md), sections
1–6. The latter was written concurrently with this audit. It also carries
forward the inspected-source/access distinctions in the
[pass-9 assessment](2026-09-22-pass9-assessment.md). It does not certify
publication novelty.

## 1. Finding

The common-decay fixed-order preparation optimization is exactly a standard
box-constrained linear resource-allocation problem. An accessible primary
paper supplies its general greedy theorem. Once the affine deadline
inequality is known, existence of an optimum with at most one partial
coordinate follows from elementary linear programming; taking a finite union
over orders does not make that conclusion a new optimization principle.
The strict ordering of the particular S1 coefficients gives the additional
full-prefix property needed by pass 10's shorter global computation.

The unequal-decay theorem is a different claim. Its fixed-order deadline
boundary need not be affine, and its local exchange excludes two partial
coordinates in **every** upkeep minimizer, even with initially inaccessible
rates. The reduction below does not establish that theorem. Its comparison
should center on the nonlinear, cost-improving exchange, together with the
full-state serial reduction that makes the exchange sufficient for arbitrary
post-request allocations.

There is also a close, fully accessible deterioration-and-resource-allocation
precursor. It has an exact restricted match to the common-decay serial
recurrence. This reinforces that affine timing/resource tradeoffs should not
be presented as a new scheduling idea. Neither inspected source closes the
unequal-decay comparison. That is a bounded finding about specified texts,
not evidence that no earlier theorem exists.

## 2. Primary texts and actual inspection

### 2.1 Controllable processing times and a general greedy theorem

A. Shioura, N. V. Shakhlevich, V. A. Strusevich, *Decomposition algorithms for
submodular optimization with applications to parallel machine scheduling
with controllable processing times*, Mathematical Programming **153**,
495–534 (2015), published online 17 September 2014.
[Full publisher text](https://link.springer.com/article/10.1007/s10107-014-0814-9),
DOI `10.1007/s10107-014-0814-9`.

**Read:** complete section 2; section 3.1, equations (2)–(8) and Theorems 1–2;
section 3.2 and its scheduling reformulations; section 4.1, Lemma 1 and its
complete proof. Theorem 2 is stated there as an established greedy result,
with attribution, rather than proved anew. Later decomposition proofs were
not audited.

Jobs have processing times between chosen bounds. Linear compression cost
is minimized subject to a common completion deadline. Processing is durable;
parallel machines have fixed speeds. Their generic LP (4) maximizes a linear
objective over submodular subset inequalities intersected with a box.
Theorem 2 gives the solution by decreasing objective weights using increments
of the box-modified rank function. Lemma 1 proves associated saturation and
bound properties. These are stronger general tools than the single-constraint
LP needed below; their scheduling model does not supply S1's decay/release
dynamics.

### 2.2 A deterioration/resource-allocation recurrence

C.-M. Wei, J.-B. Wang, P. Ji, *Single-machine scheduling with
time-and-resource-dependent processing times*, Applied Mathematical Modelling
**36**, 792–798 (2012), DOI `10.1016/j.apm.2011.07.005`.
[Author-uploaded full paper](https://www.researchgate.net/publication/257161380_Single-machine_scheduling_with_time-and-resource-dependent_processing_times).

**Read:** complete sections 2–3, including equations (1)–(7) and the assignment
argument. Their nonpreemptive job duration is `a_j+b*t-theta*u_j`, with common
`b,theta>=0`, start time `t`, and bounded nonrenewable resource `u_j`.
Equation (4) expands completion time as a weighted affine function of resource
allocations. Their weighted objective combines scheduling criteria and
resource cost; equations (6)–(7) choose endpoint allocations and reduce
sequencing to assignment. These sections do not prove the fixed-deadline
concentration theorem sought here. Other sections were not needed for this
comparison.

### 2.3 A precise preemptive-deterioration model

S. Yu, P. W. H. Wong, *Online Scheduling of Simple Linear Deteriorating Jobs
to Minimize Total General Completion Time*.
[Full author manuscript](https://cgi.csc.liv.ac.uk/~pwong/publications/tcs2013.pdf),
dated 18 November 2012, associated with the 2013 publication.

**Read:** complete introduction and section 2, including the preemption
definition and Lemmas 1–2; not the complete later competitive-analysis proofs.
The main online model has job duration `b_j*s_j`, where `s_j` is start time.
Its preemptive benchmark changes a remaining deterioration coefficient on
interruption. Lemma 1 characterizes completion through a product of service
interval endpoint ratios. The paper attributes that characterization and
the following preemptive optimality result to Ng et al. (2010); their original
proofs are not reproduced here and were not retrieved in this pass.

Original reference: C. T. Ng, S. Li, T. C. E. Cheng, J. Yuan, *Preemptive
scheduling with simple linear deterioration on a single machine*, Theoretical
Computer Science **411**, 3578–3586 (2010), DOI
`10.1016/j.tcs.2010.05.032`.
[Primary institutional record](https://research.polyu.edu.hk/en/publications/preemptive-scheduling-with-simple-linear-deterioration-on-a-singl/).
This original source has abstract/metadata access only in this audit.

### 2.4 An accessible nonpreemption proof for deteriorating repair states

H. Gehlot, S. Sundaram, S. V. Ukkusuri, *Optimal Policies for Recovery of
Multiple Systems After Disruptions*,
[arXiv:1904.11615v2](https://arxiv.org/html/1904.11615), 7 April 2020.
**Read:** complete section II and section III-A, including Lemma 1 and
Theorem 1 with their full proofs. Discrete slots select one component for
fixed repair increments; unselected components suffer fixed decrements.
Both zero and full health are absorbing. Given initial health, the objective
is the weight of permanently repaired components. When every deterioration
increment is at least its repair increment, Theorem 1 removes preemptions
while repairing the same subset sooner. Lemma 1 postpones a partially repaired
component and uses ceiling-duration inequalities and the rate condition to
preserve survival. This is a substantive, inspectable predecessor for the
nonpreemption argument.

Our comparison: S1 permits repair from zero, fractional continuous allocations,
proportional state-dependent losses, and capacity gains. The source optimizes
no initial-health investment. These differences prevent a direct theorem
substitution; they do not establish that its proof cannot be adapted.

The same authors' *Control Policies for Recovery of Interdependent Systems
After Disruptions*,
[arXiv:2009.11453v1](https://arxiv.org/html/2009.11453), 24 September 2020,
was also inspected through complete sections II and III-A. Its Theorem 1
adds precedence constraints and a finite deadline; the essential numerical
inequalities in its Lemma 1 refer back to the preceding paper. Later theorem
proofs were not audited here. These manuscripts should be cited by their
inspected versions, without assuming identity with a later journal version.

## 3. Exact common-decay LP embedding

This substitution is our derivation, using pass 10's established coefficients.
For a fixed order `pi`, write its deadline constraint as

$$A_\pi-\sum_r w_rp_{\pi_r}\leq X,\qquad
0\leq p_{\pi_r}\leq M_{\pi_r},\qquad X=e^{\gamma H}\geq1.$$

The pass-10 identity is

$$\sum_r w_rM_{\pi_r}=A_\pi-1.$$

Set

$$y_r=w_r(M_{\pi_r}-p_{\pi_r}),\qquad
U_r=w_rM_{\pi_r},\qquad B=X-1.$$

Minimizing upkeep `gamma*sum p_i` is exactly equivalent to

$$\max\sum_r\frac{\gamma}{w_r}y_r,\qquad
0\leq y_r\leq U_r,\qquad \sum_r y_r\leq B.               \tag{1}$$

This is the source's LP (4) with lower bounds zero and submodular rank

$$\varphi(\varnothing)=0,\qquad
\varphi(A)=B\quad(A\ne\varnothing).$$

Its box-modified rank is

$$\widetilde\varphi(A)=\min\left(B,\sum_{r\in A}U_r\right).$$

Theorem 2 therefore fills the `y` variables in decreasing order of
`gamma/w_r`. Pass 10 proves

$$\frac{w_r}{w_{r+1}}
=\frac{b_{r+1}}{b_r-\gamma M_{\pi_r}}>1.$$

Consequently the `y` fill order is the reverse service order. Translating
back gives a full preparation prefix, at most one partial coordinate, and a
cold suffix. This mapping handles `B=0` and a deadline loose enough to allow
all preparation to be zero.

The distinctions matter:

| Conclusion | What establishes it |
|---|---|
| Some optimal fixed-order allocation has at most one partial coordinate | A linear objective over a box with one additional inequality; coefficient ordering is unnecessary for this cardinality statement. |
| A concentrated optimum exists over the finite union of orders | Choose the best fixed-order optimum; this is a direct consequence of the preceding LP fact. |
| Preparation occupies a prefix of the particular exit order | The strict S1 coefficient ordering, followed by the standard greedy rule. |
| The fixed-order inequality describes arbitrary post-request allocation possibilities after minimizing over orders | The S1 scalar-flow formula and all-policy serial theorem; the generic LP source does not establish this reduction. |

Thus the common-decay cardinality conclusion should receive stronger prior-art
attribution than the earlier assessment's standalone phrasing may suggest.
The useful result is the justified reduction and its resulting computable
frontier, not a new fractional-knapsack theorem. This is not a claim that
the complete ready region is a single submodular polyhedron: its description
still takes a union over orders.

## 4. Exact restricted affine-deterioration comparison

Here too the substitution is ours. Restrict S1 to identical module sizes
`M`, common `gamma`, zero capacity releases, and `s>gamma*M`. For a prescribed
serial order, set

$$D=s-\gamma M,\qquad z_r=e^{\gamma t_r}-1.$$

The S1 recurrence becomes

$$z_r=\frac{s}{D}z_{r-1}+\frac{\gamma M}{D}
       -\frac{\gamma}{D}p_{\pi_r}.$$

In the Wei–Wang–Ji recurrence, take their common deterioration coefficient
`b=gamma*M/D`, basic duration `a_j=gamma*M/D`, resource effectiveness
`theta=gamma/D`, resource amount `u_j=p_j`, and bound `m_j=M`.
Then their completion coordinate is exactly `z_r`. Their permitted bound
`m_j<=a_j/theta` holds with equality. A physical deadline `H` corresponds
to the transformed deadline `e^(gamma*H)-1`.

This identifies a genuine serial-objective overlap. It does not identify
physical time with transformed time, reproduce the recurring-maintenance
interpretation, or remove the need to justify nonpreemption in S1. The cited
model assumes nonpreemption. Its particular common recurrence coefficients
also do not directly represent general heterogeneous sizes, released rates,
or unequal proportional decay coefficients. Its weighted-sum objective is
not automatically equivalent to the entire fixed-deadline frontier when
orders are optimized; no unproved scalarization equivalence is used here.

## 5. Why the inspected preemptive benchmark is not an exact decay reduction

Yu–Wong's stated service-interval characterization is

$$\prod_k\frac{t_{f,k}}{t_{s,k}}=1+b$$

for completion of a job with initial deterioration coefficient `b`.
Our interpretation is immediate: in the clock `z=log t`, its required work
is `log(1+b)`. Service over `[t_s,t_f]` removes
`log(t_f/t_s)` units, and waiting does not undo previously removed units.
This benchmark has durable progress in that clock.

S1 proportional loss makes earned preparation decay while a module waits.
Its common-decay change of variable `q=e^(gamma*t)*p` removes passive decay,
but makes the completion threshold `e^(gamma*t)*M` move with time. It does
not turn the model into the fixed workload identity above. Therefore this
specific preemptive-deterioration source does not establish the S1 exchange
merely because both descriptions use the word deterioration. A more elaborate
equivalence is neither proved nor ruled out by this observation.

## 6. Unequal decay is the stronger remaining comparison

The complete pass-11 proof was read after obtaining the preceding reductions.
For consecutive partial coordinates `j,k` in an attained serial schedule,
fixing the end of stage `k` gives the pair-cost expression

$$c(x)=\gamma_jx+K(A-\gamma_jx)^{\gamma_k/\gamma_j}-Q,$$

with positive constants determined by that schedule. If `gamma_k<gamma_j`,
the expression is strictly concave locally. If `gamma_k>=gamma_j`, the
available-capacity inequality makes it strictly decreasing. Either case
rules out an interior pair at a minimum. Intervening cold jobs contribute
an unchanged duration; after stage `k`, the old suffix can be reproduced.
Actual stage accessibility supplies the positive denominators without a
global ample-capacity hypothesis.

This is not an application of (1): the exponent generally differs from one.
Neither the inspected submodular LP theorem nor the inspected common-linear-
deterioration recurrence supplies that nonlinear exchange. Moreover, generic
LP extreme-point reasoning gives existence of a concentrated optimizer, not
the pass-11 claim about every optimizer. This difference is meaningful,
although it does not establish priority for the exchange argument.

The appropriate remaining candidate is therefore a structural theorem for
initial-readiness investment under unequal proportional deterioration and
completion-dependent available capacity. The exact scope is important:
positive `gamma_i`, nonnegative releases, instantaneous independent transfers,
finite deadline, and the maintenance weights specifically `gamma_i`.
Arbitrary independent cost weights do not inherit the displayed derivative
sign without a separate argument. General smooth loss also does not inherit
concentration, as the quadratic counterexample already proves.

An algorithm based on full subsets, a possible cold prefix, one partial
module, and a cold suffix is a consequence to assess separately. The
common-decay `O(n*2^n)` formula and rational transformed-deadline arithmetic
must not be attributed to the unequal-decay result. At completion of this
audit, the next frontier note was being developed; no unseen proof or
operation count from that work is certified here.

## 7. Access limits and bounded next comparison

The closest Glazebrook 1992/1993 permutation/nonpreemption proofs remain
uninspected, as documented in pass 9. Their abstracts cannot certify either
an exact reduction or a separation. Previously failed retrieval endpoints
were not repeatedly retried in this pass.

A later primary record was checked: K. D. Glazebrook and H. M. Mitchell,
*An index policy for a stochastic scheduling model with improving/deteriorating
jobs*, Naval Research Logistics **49**, 706–721 (2002), DOI
`10.1002/nav.10036`.
[Institutional record](https://eprints.ncl.ac.uk/65712).
It describes improvement while active, deterioration while passive, and
indexability/optimality under conditions, but explicitly has no full text
in that repository. Only its abstract and metadata were inspected. It
cannot resolve the present theorem comparison.

No paywall purchase, outside contact, or absence-based novelty inference was
used. The accessible texts narrow the proposed claim substantially: standard
resource allocation absorbs the common-decay fixed-order optimization, and
classical affine deterioration contains a restricted serial recurrence.
The unequal-decay exchange remains the focused residual candidate, with
priority and the possible applicability of older deterioration proofs still
unresolved. Its mathematical correctness, publication significance, and
operational justification remain separate questions.
