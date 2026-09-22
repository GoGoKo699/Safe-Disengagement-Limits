# Pass 6: the remaining scheduling claim is a coupled reduction

22 September 2026. Started from `a1583cd` and the pass-6 work order.
This is a primary-source comparison and mathematical reduction record, not a
novelty certificate. No historical checkpoint or source paper is modified.

## 1. Outcome

The existing serial objective is already an experience-based scheduling
objective; the previous [audit](2026-09-22-literature-audit.md), section 6,
records the exact parameter embedding. This pass removes another possible
claim: **with no capacity released on completion, both the constant-loss and
smooth-loss cold-state serial results reduce to established continuous-resource
workload arguments.** The reductions are given below, including their
infeasibility boundaries.

Moreover, after an elementary change of progress coordinate, a smooth-loss job
at fixed capacity has unit progress when served and deteriorates when waiting.
Nonpreemption theorems for this general kind of job predate this project.
Glazebrook (1992, 1993) are particularly close, but their full assumptions and
proofs were not accessible in this pass. Their abstracts expressly address
preemption and permutation optimality, so the literature gap cannot be
dismissed by labeling those papers stochastic or by merely counting different
parameters.

The residual candidate is narrow: simultaneous fractional allocation and
decaying progress can be reduced to a serial schedule **when a completion
changes the capacity, and consequently the dynamics of all remaining jobs,
according to the completed identities**. The current proof establishes that
claim within its stated model. This audit has not established that the claim
is new or sufficiently substantial for a paper. Manuscript novelty language
must remain provisional.

## 2. Access decisions and exact inspection scope

### 2.1 Requested experience-based manuscripts

The following full manuscripts remain unretrieved:

| Source | What was actually available |
|---|---|
| Janiak–Rudek (2007), *The learning effect: Getting to the core of the problem*, [DOI 10.1016/j.ipl.2007.03.013](https://doi.org/10.1016/j.ipl.2007.03.013) | Publisher bibliographic record, first-page access link, references; author-profile/ResearchGate abstract record. No complete model/proof. |
| Janiak–Rudek (2008), *A new approach to the learning effect: Beyond the learning curve restrictions*, [DOI 10.1016/j.cor.2007.04.007](https://doi.org/10.1016/j.cor.2007.04.007) | Complete publisher-rendered introduction and abstract; remaining section previews. |
| Janiak–Janiak–Rudek–Wielgus (2009), *Solution algorithms for the makespan minimization problem with the general learning model*, [DOI 10.1016/j.cie.2008.07.019](https://doi.org/10.1016/j.cie.2008.07.019) | Complete publisher-rendered introduction as recorded in the preceding audit; sections 2–5 only partial previews. |

This pass tried exact-title, DOI/PII, author-site, and institutional-PDF searches.
The author publication page supplied bibliography rather than downloadable
manuscripts. The OpenAlex record for the 2007 DOI returned no repository full
text; other attempted metadata requests timed out. That is an access report,
not proof that no open copy exists. No purchase or request to an author was made.

Consequently, no theorem on hardness, pseudopolynomial algorithms, or
preemption is imported from those uninspected sections. The established
objective embedding remains valid on the domain specified in the previous
audit; it alone does not settle the larger allocation policy class.

### 2.2 Continuous-resource serial concentration: full proof inspected

J. Błażewicz, M. Machowiak, J. Węglarz, G. Mounié, D. Trystram,
*Scheduling Malleable Tasks with Convex Processing Speed Functions*,
Computación y Sistemas 4(2), 158–165 (2000).
[Publisher PDF](https://www.cys.cic.ipn.mx/index.php/CyS/article/download/938/2114);
[author-uploaded full text](https://www.researchgate.net/publication/220398755_Schedulling_Malleable_Task_with_Convex_Processing_Speed_Functions).

**Inspected:** section 2; complete sections 4–5, equation (2), Theorem 4.1
and proof, Corollary 5.1 and proof. The publisher PDF endpoint failed in the web
tool; the author-uploaded text was accessible. The latter has OCR errors;
the mathematical statements were checked against their surrounding derivations.

The continuous relaxation has durable progress `x_i'=f_i(r_i(t))` and a fixed
resource bound `sum r_i<=m`. Theorem 4.1 expresses minimum makespan through the
convex hull of achievable rate vectors. Corollary 5.1 gives consecutive
full-resource execution for convex rates. Section 2's application begins with
nonpreemptable tasks, but the section-4 relaxation explicitly varies allocation
over time and proves the lower bound used for the consecutive construction.
The result does not contain state-dependent decay or completion-induced
changes in the available resource. Section 3 below uses its linear-rate case,
avoiding ambiguity about rate functions that vanish on a positive interval.

### 2.3 Preemptive deterioration: genuinely close, full proof unavailable

K. D. Glazebrook, *Single-machine scheduling of stochastic jobs subject to
deterioration or delay*, Naval Research Logistics 39(5), 613–633 (1992).
[Publisher record](https://onlinelibrary.wiley.com/doi/10.1002/1520-6750%28199208%2939%3A5%3C613%3A%3AAID-NAV3220390503%3E3.0.CO%3B2-P).

**Inspected:** abstract, metadata, and references only. The abstract describes
progress during processing, deterioration during waiting, and conditions
ensuring a nonpreemptive optimum inside a preemptive policy class. The standard
PDF endpoint did not yield accessible full text; direct retrieval returned
HTTP 403. No theorem number or specific sufficient condition is treated as read.

K. D. Glazebrook, *On permutation policies for the scheduling of deteriorating
stochastic jobs on a single machine*, Journal of Applied Probability 30(1),
184–193 (March 1993), [DOI 10.2307/3214631](https://doi.org/10.2307/3214631),
[Cambridge record](https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/on-permutation-policies-for-the-scheduling-of-deteriorating-stochastic-jobs-on-a-single-machine/C84FBD649FDBCC23A42CD289E62E2FF7).

**Inspected:** abstract, bibliographic metadata, and reference list only.
The publisher describes job-specific deterioration, preemptive scheduling,
and sufficient conditions for a permutation policy minimizing expected
makespan. Full text requires access. The 2016 online date is digitization;
the paper is from 1993. Exact state space, regularity, degeneracy to
deterministic processing, and cross-job dependencies must be checked before
claiming either subsumption or separation.

### 2.4 Two accessible comparisons that do not close that gate

S. Browne, U. Yechiali, *Scheduling Deteriorating Jobs on a Single Processor*,
Operations Research 38(3), 495–498 (1990),
[author-hosted paper](https://business.columbia.edu/sites/default/files-efs/pubfiles/6356/Browne_deteriorating_jobs.pdf).
The delegated source audit inspected complete sections 1–2, Lemma 1 and
Propositions 1–2 with derivations. Waiting grows required work as
`Y_i(t)=X_i+a_i*t`; deterioration stops when service starts. The policy class is
nonpreemptive and nonidling from the outset. Its ordering theorem therefore
does not eliminate arbitrary fractional S1 allocations. This is a model
comparison, not a statement about every paper citing it.

M. Żurowski, *Some remarks on preemptive scheduling of jobs with a learning
effect*, IWDSP 2018, [complete official proceedings](https://iwdsp2018.wmi.amu.edu.pl/wp-content/uploads/2018/09/iwdsp2018.pdf),
[author-uploaded text](https://www.researchgate.net/publication/348090282_Some_remarks_on_preemptive_scheduling_of_jobs_with_a_learning_effect).
**Inspected:** complete four-page contribution, sections 1–4 and references
(printed pages 95–98 in the inspected proceedings version).
It studies two machines and positional learning, treating a split job's pieces
as new jobs. Its examples show that unrestricted repeated splitting can
artificially earn further learning, after which the paper restricts the
preemption convention. These are different dynamics from S1. The useful lesson
is that a serial processing-time formula does not define its own preemptive
extension; that extension must be specified and proved separately.

## 3. Exact no-release reductions

These are deductions in this audit, rather than theorem statements attributed
to the cited authors. Let all `a_i=0`, so `b>0` is fixed until completion.
All unfinished jobs start cold.

### 3.1 Constant loss

If `b<=d_i` for any required cold job, that job can never leave zero under
maximum loss. Otherwise define `alpha_i=(b-d_i)/b>0`. Under maximum loss the
reflected preparation trajectory satisfies

    p_i'(t) <= alpha_i*v_i(t).

This follows at positive state from `v_i<=b`; at zero reflection gives the
same inequality. Compare with a durable job of size `M_i`, rate
`x_i'=alpha_i*v_i`, and the same allocation budget. It finishes no later than
the original job. The transformed demand is `M_i/alpha_i`, so the usual
total-work lower bound gives

    T >= (sum_i M_i/alpha_i)/b = sum_i M_i/(b-d_i).

Serial full allocation attains equality in the original system. Hence this
entire heterogeneous-loss fixed-capacity subclass follows from a standard
durable-work relaxation, not a new scheduling principle.

### 3.2 Smooth monotone loss

Use the regularity and accessibility facts proved in
[the state-dependent-loss note](2026-09-22-state-dependent-loss.md).
If `b<=g_i(M_i)` for any required job, its full-capacity trajectory encounters
an inaccessible equilibrium barrier, so completion is impossible. Otherwise
put

    z_i=G_i(p_i;b)=integral_0^{p_i} dq/(b-g_i(q)),
    c_i(b)=G_i(M_i;b).

The chain rule gives, including boundary reflection,

    z_i' <= v_i/b.

A durable comparison job of size `c_i(b)` with rate `v_i/b` is therefore no
harder. Its aggregate rate is at most one, giving `T>=sum_i c_i(b)`.
Consecutive full allocation attains equality. The familiar coordinate change
plus ordinary workload conservation proves this subclass exactly.

### 3.3 The same coordinates identify the deterioration lineage

For an interior state set `theta_i=v_i/b` and write
`h_i(z_i)=g_i(p_i)/(b-g_i(p_i))`. Before any capacity change,

    z_i' = theta_i - (1-theta_i)*h_i(z_i).

Full service yields unit progress; no service yields deterioration; fractional
service gives their convex combination. Since `g_i` is nondecreasing, `h_i`
is nondecreasing on the accessible interval. In the constant-loss model this
passive deterioration is constant, with reflection at zero.

This is why preemptive deteriorating-progress results require a real theorem
comparison. The existence of an integral in the S1 proof is not itself a
distinguishing feature.

## 4. Where the current reduction goes beyond the verified substitutions

After job `j` completes, capacity changes from `b` to `b+a_j`. Every remaining
job's coordinate `G_i(p_i;b)`, endpoint `c_i(b)`, and passive deterioration
function change. At fixed physical preparation `p_i`, its integral coordinate
weakly decreases. The repository proof charges the completed job's stage time
to a downward potential jump and also uses the decreases of all surviving
coordinates. This handles partial preparation accumulated before that change.

The fixed-capacity convex-hull theorem cannot simply be applied separately on
each stage: later stages start with partially prepared jobs, while the desired
serial comparison starts them cold. Discarding those partial states without
an accounting argument would assume the result. Likewise, the earlier
experience-based embedding identifies costs of **already serial** schedules;
it does not establish how fractional trajectories behave between completions.

A basic counterexample shows why this distinction is logical, not merely
terminological. Consider two unit jobs with `b(C)=1+|C|`, zero loss, and alternate
allocation dynamics `p_i'=sqrt(b(C)*v_i)`. Every full-allocation serial stage has
duration `1/b(C)`, exactly the zero-loss S1 serial duration. Serial completion
takes `1+1/2=3/2`. Splitting the initial capacity equally completes both jobs
at time `sqrt(2)<3/2`. Thus identical serial objectives can coexist with
different answers to the all-allocation question. This alternate law is not
an S1 counterexample; it refutes inferring serial dominance from objective
matching alone.

## 5. Contribution boundary and next decisive comparison

The following descriptions are currently defensible:

1. The homogeneous count-speed clearing subclass and the serial
   experience-based objective have established scheduling predecessors.
2. Fixed-capacity decaying preparation reduces to standard workload
   conservation after a scalar change of coordinates or linear relaxation.
3. The repository contains a complete proof for the coupled completion-release
   model. Its novelty remains unresolved; the closest inaccessible
   preemptive-deterioration papers are material, not cosmetic, gaps.

The next literature action should be access to Glazebrook (1992/1993) and the
requested experience-based manuscripts through an available legitimate copy,
followed by a model/theorem table. In particular check whether completion of
one job can alter another job's processing/deterioration law, whether a
deterministic cold-state specialization is permitted, and whether the proof
already uses the same time-to-completion potential with monotone jumps.
Do not replace this comparison with more generic keyword searches, claim
novelty because access failed, or inherit hardness from a broader class.

While that access gap remains, the scientifically useful parallel task is the
explicit delayed service-shard interface and its handoff obligation. It tests
whether the coupled theorem captures a real constraint at all. A paper can be
organized around a provisional theorem for internal review, but submission
readiness has not been established by this pass.
