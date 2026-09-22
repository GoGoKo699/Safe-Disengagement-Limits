# Internal referee-style assessment

22 September 2026. This is a separate internal adversarial reading of the
current proofs and implementation. It is not external peer review, engineering
validation, or a novelty certificate. The assessment covers the heterogeneous
readiness, scheduling, ordering, startup, state-dependent-loss, and homogeneous
proportional-readiness notes, including research pass 5.

## Assessment

The project has defensible model-internal theorems, but is **not yet submission
ready**. No mathematical error was found in the audited statements under their
explicit assumptions. The strongest current structural result is the
all-policy serial-dominance theorem from ready/cold states: a weighted potential
reduces arbitrary measurable parallel/preemptive schedules to a finite
permutation minimum. Its integral version extends to nonnegative monotone
Lipschitz loss functions vanishing at zero. Publication novelty remains an open
question, and the shared-resource fallback interface is an idealized contract,
not a verified implementation.

The homogeneous proportional-loss frontier is now another complete result:
under `s>d`, an aggregate progress bound identifies the best exit time among
all distributions of a fixed total preparation, and a concentrated distribution
attains it. Its inversion gives the exact continuous recurring frontier. This
solves the homogeneous recurring question without claiming that total
preparation alone characterizes every individual state's exit time.

The critical-budget startup result supplies a useful distinction: sustainable
partial readiness may be reachable from cold when every deadline-sufficient
fully ready subset is unreachable. It does not contradict the initialized
fixed-loss upkeep formula. This is more informative than treating paid
initialization as a disposable technicality.

## Proof findings

| Claim | Audit result and essential restriction |
|---|---|
| Fixed-loss serial dominance | The local potential derivative is at most one, including both reflecting boundaries. Each cutover drops the potential by at least its serial stage cost. Nonnegative releases and cold initial unfinished modules justify the otherwise inaccessible `d_i>=b` states being zero. |
| Simultaneous completions and endpoints | Zero-time linearization is valid for every ordering of a simultaneous group. There are finitely many cutovers and permutations. A finite permutation minimum is attained, so using `F(S)<=H`, including equality, has no hidden infimum gap. |
| Support domination | Granting full preparation to every positive coordinate and transferring it removes work and increases available capacity. Independence, nonnegative releases, and the absence of transfer penalties are necessary. The implication is one-way; a tiny positive support does not itself guarantee readiness. |
| All-request-time upkeep | One simultaneously admissible maximum-loss history gives `Q'<=s-u-D(H)` almost everywhere. Bounded absolutely continuous `Q` yields the finite-horizon bound and the long-run upper bound without assuming a time average exists. Static initialized maintenance attains the bound for every allowed history. |
| Boundary cases | `d_i=0`, `s=0`, exact `b=d_i`, all-ready exit, and `D(H)=s` are treated correctly. Zero upkeep is not zero startup cost. If `D(H)>s`, the duration expression is an upper bound, not an attained lifetime. |
| Two-module startup | At `s=d_1+d_2` with both `d_i>0`, the triangle `p_1+p_2<=max(M_1,M_2)` is both invariant from cold and exactly reachable. The first-transfer deficit bound and matching endpoint construction establish `H_warm=min(M_1,M_2)/max(a_1+d_1,a_2+d_2)`. The readiness guarantee begins after warmup. |
| Smooth-loss serial dominance | The maximal adversary is explicitly a state-feedback rule, not a common numerical loss trace across policies. The Lipschitz barrier prevents finite-time completion when `b<=g_i(M_i)`. Reachable partial integrals stay finite, their sum grows at rate at most one, and capacity increases decrease the remaining integrals. |
| Limits of general smooth extension | The continuous non-Lipschitz example reaches the equality barrier in finite time and correctly excludes a broader regularity claim. Smooth loss does not preserve the fixed-loss upkeep staircase. For general heterogeneous smooth loss, the full-state loss minimum remains conditional on attainment and does not characterize the ready-state set. |
| Homogeneous proportional frontier | For `s>d=gamma*M`, the aggregate variable `Z=M*J+sum p_i` is continuous across cutovers and obeys the stated scalar progress envelope. Its positive reciprocal defines a Lipschitz potential; the breakpoint chain rule is valid because `Z'=0` almost everywhere on each level set. Concentrated initial preparation attains the integral lower bound for every fixed total. |
| Proportional recurring cost and endpoints | The minimum required total `Q_H` gives `Q'<=s-u-gamma*Q_H` on the maximal feedback-loss history. Static full modules plus at most one partial module attain this bound. The exponential inversion, continuity at segment endpoints, `H=0`, `H=T_0`, feasibility condition, and finite cold-ramp obstruction at `c(H)=s` are correct within the stated strict `s>d` domain. |

The ordering examples have the claimed limited force: a capacity-independent
priority fails, pair preferences can cycle at one capacity, and the displayed
adaptive pairwise index can fail globally even with zero loss. They prove
neither computational hardness nor the failure of algorithms using the whole
remaining set. Serial optimality from arbitrary partial initial states remains
outside both serial theorems.

## Implementation and finite checks

The recurrence and readiness calculation in `analysis/heterogeneous.py` agree
with the fixed-loss statements. Infinity is represented separately from zero;
zero denominators are rejected; deadline comparisons use exact rational
arithmetic; nominal infeasibility is not reported as negative attainable
throughput. The implementation requires `a_i>0`, whereas the scheduling and
startup proofs also permit `a_i=0`. That wider analytic case is not part of the
implementation's tested input domain.

During this audit, `python analysis/verify_heterogeneous.py` was actually run and
passed. Its report records 640 heterogeneous models, 3,592 subset/permutation
comparisons, 2,232 homogeneous formula comparisons, local reflected-derivative
and potential-jump checks, and startup constructions across 729 parameter
choices. These checks establish arithmetic and implementation agreement on the
stated finite domains. They do not enumerate all measurable policies; that
claim rests on the written proofs. The smooth-loss theorem was checked
analytically here, without claiming that this fixed-loss verifier tests it.
The subsequent homogeneous proportional proof was also audited analytically;
this reviewer did not rerun a verifier for that later pass. Any additional
checks reported elsewhere retain their own stated scope.

## Remaining obstacles and next decisive work

The repository's literature audit records a reduction of the homogeneous
clearing subclass to established state-dependent-speed scheduling. Its
dissipativity note identifies the recurring average bound as a standard bounded
storage argument. Those source records were read for this assessment; their
external primary texts were not independently retrieved again by this reviewer.
Neither result should carry the paper's novelty claim alone.

Section 6 of the source audit further records a learning-effect scheduling
embedding of the serial objective with unequal capacity releases. One subclass
has a full-text comparison; the more general processing-function model has
only a partially accessible paper, with theorem-level access limits stated.
These comparisons were read as repository records only, without independent
external retrieval for this assessment. They strengthen the reason to locate
any candidate novelty in the reduction from arbitrary allocations with loss,
or in a substantively distinct readiness theorem, rather than in the serial
permutation objective. The broad model's complexity claims do not establish
complexity of the S1 subclass.

The remaining novelty audit must determine whether identity-dependent capacity
release with fixed or state-dependent loss is already covered by an inspected
scheduling theorem, including its full policy class. If it is, record that
reduction and choose the next substantive question. Merely adding heterogeneous
parameters, a subset recurrence, or a new application name is insufficient.

The operational gap is equally concrete: derive an uncertainty envelope from a
finite-record or other explicit fallback interface, account for update latency
and ownership transfer, and check whether capacity actually becomes available
for preparation after a cutover. The present independent receiver contract
does not itself prove state sufficiency or essential-service safety.

For the next mathematical pass, heterogeneous smooth readiness and the full
exit-time function of arbitrary partial states remain unresolved; the cold
serial recurrence cannot be substituted for them. Homogeneous proportional
readiness is now solved for `s>d` in the precise optimal-total and recurring
sense above. Its prior-art relation, physical interpretation, and the omitted
`s<=d` domain require separate treatment. A paper should be built around a
surviving result with resolved prior-art scope and operational meaning; the
current internally sound results remain a research checkpoint rather than a
submission package.
