# Pass 9: stronger state coverage, a sharper prior-art question

22 September 2026. This is a scientific and source-comparison assessment of
the [fixed-loss partial-state theorem](2026-09-22-pass9-partial-states.md) and
the [smooth-loss full-state theorem](2026-09-22-pass9-smooth-partial.md).
It supplements the [pass-6 prior-art audit](2026-09-22-pass6-prior-art.md).
Proof status, source access, and publication significance are separate judgments.

## 1. Assessment

The partial-state result is a substantive improvement to the repository's
mathematics. It removes the cold-state restriction, proves dominance over
parallel and preemptive allocations, and supplies an exact membership oracle
for the full ready region. A finite permutation minimum also makes attainment
explicit. Those are useful results regardless of eventual publication.

The proof simultaneously **weakens the case that completion-released capacity
introduces a new scheduling principle**. Its decisive operation is to complete
one job early and postpone the other jobs' service. Postponement preserves
total allocated work while reducing deterioration of that work. Completing
jobs earlier only needs to leave at least the old capacity available. The
values and additive form of the released rates do not drive the exchange.

This makes the relevant comparison a precise extension of classical
nonpreemption results for deteriorating jobs. It does not establish that those
results already contain this theorem. Their closest full proofs are still
uninspected. The correct status is a proved internal extension with a specific
unresolved prior-art test, not a new general readiness law or a certified
publication contribution.

## 2. What the new proof actually uses

The complete fixed-loss note was read in this pass, including the first-job
work bound (1), spare-capacity allocation (2), cumulative-service inequalities
(3), reflected suffix formula (4), induction, robustness, and forward DP (7).

If the old schedule first completes module `i` at `T` and the new full-speed
first stage ends at `tau`, the key inequalities are

$$V_i(T)\geq b\tau,\qquad
 U_j^{\mathrm{new}}(t)\leq U_j(t),\qquad
 U_j^{\mathrm{new}}(T)=U_j(T)\quad(j\ne i).$$

The first pays for the early stage without stealing uncompensated work from
other modules. The latter two say exactly that their service has moved later.
The reflection formula proves terminal-state dominance, including loss of
initial preparation at zero. This is a genuine all-allocation argument; merely
matching an earlier paper's serial objective would still not prove it.

On the resource side the construction uses at most the old capacity `b`
until the original first-completion time. Additional early completions remove
future work and cannot reduce feasible capacity. During suffix replay, every
previously completed module can be retained as completed. Hence a theorem
comparison should test monotone resource availability under earlier
completions, rather than treating the particular expression
`s+sum completed a_i` as the conceptual dividing line. A broader monotone set
capacity is a natural consequence to check from the same argument; it is not
an independently established contribution in this assessment.

No claim of preservation of the original complete completion order is needed.
This matters when comparing proofs: an earlier permutation-dominance theorem
could be sufficient even if its transformation changes later completion order.

### 2.1 Smooth loss makes the deterioration comparison more explicit

The complete smooth-loss note was also read: sections 1–7, the integrating-factor
proof of input-postponement dominance, first-job traversal/work inequality,
measurable repayment, robust serial reduction, subset recurrence, compactness
through bounded serial witnesses, and the stationary upkeep construction.
Its nondecreasing Lipschitz loss assumption gives an integrating-factor kernel
which increases with service time. Equal total input shifted later therefore
has no smaller terminal effect. This is the exact structural property to
compare with an earlier deterioration theorem, rather than only comparing
whether the papers use linear or nonlinear rates.

For a fixed capacity `b` and a module satisfying `b>g_i(M_i)`, introduce the
remaining-time coordinate

$$R_i(p;b)=\int_p^{M_i}\frac{dq}{b-g_i(q)}.$$

Full-speed service makes `R_i'=-1`. Waiting makes
`R_i'=g_i(p)/(b-g_i(p))>=0`. With fractional allocation `v_i=theta_i*b`,

$$R_i'=-\theta_i+(1-\theta_i)
             \frac{g_i(p_i)}{b-g_i(p_i)}.$$

Thus, within an accessible-capacity stage, the model has ordinary unit-speed
processing in this coordinate and job-specific deterioration while waiting.
The transformation is our derivation, not a claimed theorem from Glazebrook.
When capacity increases, `R_i(p;b)` decreases for unchanged physical progress.
This produces simultaneous monotone contractions of other jobs' remaining-time
coordinates. Jobs with `b<=g_i(M_i)` require separate treatment: their integral
is not a finite ordinary workload, and they may become finishable only after
another completion. These barriers and contractions are concrete hypotheses
to check in the closest theorem or its proof.

The transformation does not prove an exact global reduction to a published
single-machine model: its coordinate depends on current capacity, and the
fractional controls and barrier states must still be accounted for. It does
show why describing the result only as a new interaction between replication
and released resources would obscure the strongest predecessor.

The smooth theorem's attained static optimization is also stronger than the
earlier uncharacterized ready/cold oracle. Compactness is proved without assuming
continuity of hitting times at threshold states. Nevertheless, general
`C(H)=min sum g_i(p_i)` remains a continuous optimization over an implicitly
represented set. The proof does not turn it into a closed formula, establish
convexity, or supply a polynomial optimization algorithm. Its long-run bound
uses the already recorded bounded-storage argument; the contribution under
assessment is the explicit full-state structure supporting that argument.

## 3. Targeted primary-source comparison

### 3.1 Closest deterioration results: still a material access limit

K. D. Glazebrook (1992), *Single-machine scheduling of stochastic jobs subject
to deterioration or delay*, Naval Research Logistics 39(5), 613–633,
[publisher record](https://onlinelibrary.wiley.com/doi/10.1002/1520-6750%28199208%2939%3A5%3C613%3A%3AAID-NAV3220390503%3E3.0.CO%3B2-P).

The primary abstract explicitly has progress during processing, deterioration
while waiting, and conditions yielding a nonpreemptive optimum within a
preemptive class. It also describes a related class where processing causes
delays for waiting jobs. **Read in this pass:** abstract, references, metadata.
The direct PDF endpoint again redirected to an abstract page. A search snippet
mentioning an internal theorem was not treated as access to that theorem.

K. D. Glazebrook (1993), *On permutation policies for the scheduling of
deteriorating stochastic jobs on a single machine*, Journal of Applied
Probability 30(1), 184–193,
[publisher record](https://www.cambridge.org/core/journals/journal-of-applied-probability/article/abs/on-permutation-policies-for-the-scheduling-of-deteriorating-stochastic-jobs-on-a-single-machine/C84FBD649FDBCC23A42CD289E62E2FF7),
[DOI 10.2307/3214631](https://doi.org/10.2307/3214631).

The primary abstract specifies preemption, job-specific growth of processing
requirements while waiting, and sufficient conditions for a permutation policy
minimizing expected makespan. **Read in this pass:** abstract, references,
metadata. Full text remains access-restricted. The 2016 website date is
digitization; publication was March 1993.

The limited searches in this pass targeted postponement, nonpreemption under
deterioration, and completion-dependent capacity. They did not produce an
inspectable closer theorem. This is an access/search report, not evidence of
absence. Neither the word “stochastic” nor the lack of explicit resource-release
language in the abstracts establishes separation from a deterministic special
case or a monotone-coupling extension of their proofs.

### 3.2 Fully inspected state-dependent service comparison

U. Ayesta, B. Prabhu, R. Righter, *Scheduling in a single-server queue with
state-dependent service rates*, Probability in the Engineering and
Informational Sciences 34(4), 507–521 (2020),
[DOI 10.1017/S0269964819000160](https://doi.org/10.1017/S0269964819000160),
[author manuscript](https://hal.science/hal-01783136/document).

The previously retrieved full author manuscript was reread locally: complete
section 4, Lemma 1 and proof, and the section-5 setup; the earlier audit also
inspected Theorems 1–2 and Corollary 4. Lemma 1 couples arbitrary schedules to
SRPT-with-holding using majorization, preserving counts, departures, and total
durable workload. Capacity depends on the number of retained jobs. Section 5
then optimizes release times in the no-arrival model. Those arguments do not
contain the new note's terminal dominance under decay or identity-dependent
capacity. Their earlier homogeneous reduction remains valid; this inspection
does not justify an exact heterogeneous partial-state reduction to that paper.

### 3.3 Existing reductions remain properly scoped

The [pass-6 audit](2026-09-22-pass6-prior-art.md) already records complete
relevant proofs in Błażewicz et al. (2000) for fixed-capacity durable progress,
and the accessible model/proofs in Browne–Yechiali (1990), which assumes
nonpreemptive scheduling. Neither should now be cited as if it independently
proved the new all-partial-state exchange. In particular, initial preparation
which decays while waiting is not automatically equivalent to a fixed amount
of durable work. The Janiak–Rudek experience-based embedding still identifies
overlap of serial objectives, not equivalence of allocation policy classes.

## 4. What would settle the residual comparison

The closest full theorem and its proof should be tested against these four
specific features:

1. Known partial progress at the initial time, including passive decay to zero.
2. Fractional/preemptive service, with terminal progress improved when equal
   cumulative work is shifted later.
3. Immediate irreversible completions that may increase the feasible service
   rate for other jobs; some jobs may become finishable only after that gain.
4. A pathwise finite-deadline conclusion, including endpoint attainment,
   rather than only an expectation or a policy restricted in advance.

If an earlier theorem directly includes them, give the substitution. If its
proof extends after replacing fixed capacity by a larger available capacity,
record that modest extension honestly. Only a substantive unmatched conclusion
and a justified use for it would support a central contribution.

The forward subset DP exploits an ordinary dominance fact: among serial
prefixes with the same completed set, the earlier one leaves no less initial
preparation available for any continuation. Its exactness is valuable, but the
exponential subset recurrence is not an additional independent novelty claim.
Likewise, making the ready set explicit strengthens an upkeep optimization
based on it; it does not make bounded-storage averaging a new principle.

## 5. Research decision

Prefer this theorem to the one-record reset benchmark as the strongest current
mathematical candidate: it answers the project's original unresolved
all-partial-state question. Do not promote it to a paper merely because its
proof is now complete. The nearest deterioration results, the significance of
their possible monotone-capacity extension, and the instantaneous-handoff
interface remain the decisive gates. Further arbitrary parameter additions or
repeated unsuccessful searches do not resolve those gates.

## 6. Pass-10 follow-on: an explicit frontier and a stronger residual candidate

The complete [common-proportional-loss frontier](2026-09-22-pass10-proportional-frontier.md)
was read after the preceding assessment: sections 1–8, affine fixed-order
recurrence (4)–(6), adjacent-weight identity (7), concentration proof, subset
recurrence (8), candidate frontier (9)–(12), recurring attainment, computational
scope, endpoints, and the partial-first counterexample.

This result materially improves usability. Pass 9 gave an attained continuous
optimization over the ready set; pass 10 eliminates that continuous search for
its restricted class. It permits heterogeneous `M_i` and `a_i`, but requires
one common `gamma>0` and `s>max_i gamma*M_i`. The latter ensures every serial
stage is accessible throughout the preparation box. The resulting finite
computation is exact in rational transformed deadline `X=exp(gamma*H)` when
the other inputs are rational. It remains exponential in module count and
does not give exact rational arithmetic for an arbitrary rational physical
deadline `H`.

Three logically distinct ingredients should remain separated:

| Ingredient | Scientific assessment |
|---|---|
| Exponentiating the common scalar decay flow, fractional-knapsack optimization, and subset dynamic programming | Standard methods; none should be advertised as a new algorithmic principle. |
| Fixed-order affine deadline weights with the strict identity `w_r/w_(r+1)=b_(r+1)/(b_r-gamma*M_(pi_r))>1` | A specific derived property of this model. It identifies the order of preparation efficiencies despite heterogeneous sizes and capacity releases. |
| Taking the union of all serial orders and proving a globally upkeep-optimal state has a full set, at most one partial module, and a cold remainder | The substantive structural conclusion to compare with prior theorems. Together with the all-policy serial reduction it justifies the explicit frontier, rather than assuming a concentrated policy class. |

The last two ingredients are a stronger residual candidate than simply
restating the smooth static minimum. Their value is not negated because the
final fixed-order optimization is elementary. Equally, a correct composition
of standard tools does not establish that the structural conclusion is new
or important enough for a paper. “Derived in this repository” must not be
silently promoted to “previously unknown.”

The quantifiers in the concentration theorem are correctly narrow. It proves
existence of a globally cost-minimizing state with a matching partial-first
schedule after the full set transfers. It does not prove that partial-first
minimizes exit time from every prescribed concentrated state. The exact
counterexample in section 7 makes this distinction explicit and should remain
visible in any later presentation. Nor does the finite union of box-constrained
halfspaces imply that the full ready region is convex.

No additional source search was needed to assess those logical boundaries.
The prior-art gate in section 3 remains open: inspect the nearest deterioration
permutation theorem's actual conditions and determine whether its proof
already covers the all-partial-state serial reduction or extends to monotone
completion-dependent capacity directly. Then compare the common-decay
fixed-order preparation optimization at theorem level. An exact predecessor
for seriality would narrow the potential contribution to the concentration
and frontier result; it would not automatically prove or disprove that result's
novelty. Conversely, an unmatched affine-weight calculation cannot rescue an
unjustified claim of a new general nonpreemption principle.

The strongest current package is therefore the all-policy full-state reduction
plus the common-decay concentration/frontier, within their stated ideal model.
It is a better candidate for focused evaluation than further variants of the
one-record reset benchmark. The physical proportional-loss envelope,
instantaneous cutover assumptions, paid initialization, closest-source access,
and submission-readiness requirements remain unresolved where the main notes
say they are; pass 10 does not remove those gates.
