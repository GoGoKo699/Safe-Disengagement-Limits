# Research status

**22 September 2026 — lead workspace research, passes 1–19 complete; strengthened contribution under prior-art assessment.**
Latest continuation started from `main` at
`16dca7e14950e13e4a292600ee39b2a3aeca9ec1`.

## Decision

The strongest current candidate is concentration of initial readiness under
unequal positive proportional loss. Every upkeep minimizer has at most one
partial module, for all nonnegative source budgets. A matching cold-prefix
algorithm computes the frontier using O(n*3^n) real scalar evaluations. An exact
counterexample proves that a cold prefix can improve the global optimum.
The common-coefficient O(n*2^n) rational transformed-deadline algorithm remains
a useful specialization. General nonlinear smooth loss can require multiple
partial modules; its quadratic counterexample remains visible.

Rate barriers now have an exact closure characterization and a minimum upkeep
floor reached at a finite deadline. A blocked cold exit precludes finite normal
warmup to any ready state; paid initialization can still support a zero-optional
critical case. Strict maintenance slack permits finite warmup. At budget
equality, the new fixed-target criterion and two exact examples distinguish
reachable unequal-rate readiness from an unreachable common-rate frontier.

Meaningful publication novelty and a justified operational interface remain
unresolved. The latest source audit explicitly embeds common-decay fixed-order
optimization into established linear resource allocation, and adds an accessible
deteriorating-repair nonpreemption proof. The unequal-decay concentration exchange
is the focused residual candidate. A correct new derivation is not a priority
claim, and the closest older deterioration proofs remain partly inaccessible.

The finite-record audit now separates source departure, independent
recoverability, exact receiver freshness, and response deadlines. Delayed
capacity release breaks serial optimality; atomic updates make age part of
readiness; allowing a bounded final freeze changes the recurring cost. The
finite-update upkeep calculation reduces exactly to a standard sporadic task,
and the frozen-copy allowance is established migration practice. These are
useful corrections and benchmarks, not replacement novelty claims.

A complete [working manuscript and checked PDF](paper/README.md) now exist.
Recovery-source verification has completed; all nine current suites pass. The six
prior reports match, and the missing critical-viability report has been
regenerated reproducibly. Original lost artifacts are not claimed recovered.
The historical interruption remains recorded in its unchanged continuation
note. No submission readiness, formal release, external review or engineering
validation is asserted.

Pass 17 inspected a complete nonlinear fixed-deadline allocation proof and
excluded two precisely stated identifications with S1. This supports a concrete
model distinction without proving literature-wide novelty. The assumption
audit gives exact independent-maintenance and early-transfer counterpolicies:
the value is conditional source-bottleneck upkeep, not a universal total-system
cost of controller removal. Positive capacity release is not needed for
concentration.

Pass 18 resolves the vanishing request-time shortfall boundary. The strict-order
exit envelope is continuous when cold exit is finite. If C(H)<s, its minimum
upkeep equals C(H); if its minimum is at most s, every limiting minimizer
concentrates. For H>0 the fixed-tolerance costs converge to this limiting value.
An exact cold-finite two-module instance has C=1=s but limiting cost 7/6,
and C_epsilon=7/6+5*epsilon for 0<epsilon<=1/15. The persistent jump is stronger
than the elementary margin cost, which already rules out critical readiness
at any positive tolerance. These are one-time request deficits, not recurring
normal disturbances.

Pass 19 resolves the remaining concentration questions: every nominal minimum
at fixed positive tolerance and every limiting minimum concentrates, with
unequal positive coefficients and at every feasible budget. The new exchange
uses increasing concave completion-time maps for prepared intermediate stages;
a stationary two-interior exchange can only be a strict local maximum.
The common-rate route remains ordinary linear allocation. No unchanged
positive-tolerance frontier algorithm or complexity bound is inferred.

Pass 15 resolves critical ready-region startup. Every indefinitely ready
maximal-loss trajectory at C(H)=s converges to one minimum, but three modules
can sustain readiness after finite cold warmup even when that unique minimum
cannot be robustly reached or dominated. The proposed fixed-target necessity
is false. The companion proof establishes its validity for at most two modules
in the finite-cold-exit domain. A conditional standby-resource interpretation
is explicit; its early-activation and independent-resource restrictions still
need a justified application class.

## Claim ledger

| ID | Claim | Current status |
|---|---|---|
| P1 | Passive admission/supply/stock frontier | Archived analytical benchmark; reproduced |
| P2 | Passive stationary formula is a new shutdown law | Not claimed; network-calculus overlap |
| A1 | Homogeneous ready/cold exit time | Internal proof audit passed; explicit reduction to prior state-dependent-speed scheduling recorded |
| A2 | Exact homogeneous recurring upkeep | Correct under archived assumptions; averaging has dissipativity precedent; standalone novelty not established |
| A3 | Partial/rotating preparation improves fixed-rate worst-case mean throughput | Ruled out by A2 and H2 with paid initialization |
| A4 | Upkeep staircase is update-law independent | False; proportional countermodel retained and generalized in G2 |
| A5 | Equal-load granularity limit | Archived idealized corollary; not free practical partitioning |
| H1 | Heterogeneous serial exit optimum from ready/cold states | Complete weighted-potential proof over arbitrary parallel/preemptive policies; attained permutation minimum |
| H2 | `D(H)=min_{S:F(S)<=H}sum_S d_i` gives exact upkeep | Complete proof and attaining robust policy; explicit exponential subset computation |
| H3 | A scalar local priority solves every heterogeneous order | False; exact capacity reversal, fixed-capacity cycle, and greedy failure |
| H4 | Serial optimality from arbitrary partial initial states | Now proved separately by first-completion exchange; forward time-dependent subset DP is exact; no preservation of the original completion order claimed |
| I1 | Critical two-module cold reachability is `sum p_i<=max M_i` | Complete proof for `d_i>0`, `s=d_1+d_2` |
| I2 | Best post-warmup deadline is `min M_i/max(a_i+d_i)` in I1 | Complete lower bound and robust construction |
| I3 | Unreachable optimal fully ready subset precludes cold-start readiness | False; exact reachable partial-state counterexample, with unchanged upkeep |
| G1 | Ready/cold serial dominance under monotone Lipschitz state loss | Complete integral-potential proof; exact non-Lipschitz equality counterexample retained |
| G2 | Homogeneous proportional model has exact continuous upkeep frontier | Complete aggregate-potential proof for `s>gamma*M`; concentrated preparation attains it |
| G3 | Arbitrary-partial smooth exit and heterogeneous recurring upkeep | Full-state seriality and forward flow/integral DP proved; compact ready set gives attained minimum loss; general continuous optimization is not solved in closed form |
| G4 | Heterogeneous common-gamma proportional frontier | Complete concentration proof under `s>max gamma*M_i`; some optimum has at most one partial module; exact rational transformed-deadline algorithm |
| G5 | Every concentrated state should process its partial module first | False; exact two-module multiplier counterexample retained |
| G6 | At most one partial module suffices for all monotone smooth losses | False; exact quadratic-loss counterexample separates a two-partial state from every concentrated state |
| G7 | Unequal proportional coefficients destroy concentration | False; every upkeep minimizer has at most one partial coordinate, including inaccessible initial rates |
| G8 | Unequal-rate upkeep has a finite explicit frontier | Proved via full set, cold prefix, one partial module and cold tail; O(n*3^n) real evaluations, not exact rational or polynomial complexity |
| G9 | A partial-first restriction preserves the global upkeep optimum | False for unequal rates; exact two-module log(3) separation |
| G10 | Cold modules preceding an optimal partial module can have any decay rate | False; every such predecessor must have strictly larger gamma |
| I4 | Partial preparation can bypass proportional finite-time rate barriers | False; finite exit is equivalent to closure of the initially full set |
| I5 | A sufficiently loose deadline always removes upkeep | False; minimum successful-seed cost is the exact eventual floor, attained at a finite deadline |
| I6 | C(H)=s settles finite cold-start feasibility | False; exact reachable and unreachable positive-deadline examples, with cold exit finite in both |
| I7 | Nonzero critical concentrated target can be reached from cold | Exact fixed-target criterion: with one partial coordinate, some full coordinate must decay faster; pure-full critical targets are unreachable |
| I8 | Critical viable trajectories converge to one upkeep minimum | Proved by dissipation, Lipschitz continuity, compactness, and finiteness of the minimizing set |
| I9 | Indefinite critical readiness after cold warmup requires a reachable optimum | False with three modules: unique unreachable optimum, finite warmup and uniform deadline certificate; true with at most two modules in the stated domain |
| Q1 | Vanishing one-sided request deficits preserve minimum upkeep | True for C(H)<s; false at equality, with exact finite-cold-exit jump 1 to 7/6 |
| Q2 | The limiting precision frontier concentrates | Every minimizer does at every feasible budget; pass-19 prepared-stage exchange removes the pass-18 restriction |
| Q5 | Fixed positive tolerance destroys unequal-rate concentration | False: every nominal upkeep minimum still has at most one partial coordinate; exact capped-support exchange proof |
| Q3 | Positive-tolerance costs approach C_-(H) | Proved for finite cold exit and H>0; H=0 is an explicit exception |
| Q4 | Critical exact readiness tolerates a positive safety margin | False whenever C(H)=s>0: C_epsilon>=C+gamma_min*epsilon; the jump example gives a stronger nonvanishing gap |
| M1 | Focused working manuscript exists | Editable sources, compiled/visually inspected PDF and internal proof audit; novelty and meaning remain under assessment |
| V3 | Recovery checkpoint sources execute | All eight recovered suites passed, plus the new precision suite; six old reports match and new reports reproduce; original lost bytes unavailable |
| L1 | Adding drain time to the old serial recurrence remains optimal | False; exact two-module optimum `3` versus `10/3` |
| L2 | Overlapping drains restore uninterrupted-preparation optimality | False; exact three-module optimum `37/9` versus best uninterrupted `38/9` |
| L3 | Fixed-loss upkeep reduction survives independent residual drains | Proved using actually deadline-feasible subsets; the new oracle is not solved; no feasible state below `max ell_i` |
| J1 | A copied-work amount suffices to characterize spaced-update readiness | False; identical cold preparation has exit bounds `L` or `2L` depending on update age |
| J2 | One-version spaced-update recurring frontier | Proved with specified event priority and cold-at-update initialization; exact reduction to sporadic-task scheduling |
| J3 | A mean dirty-rate substitution recovers atomic-reset readiness | False in both directions; distinct uncertainty sets explicitly compared |
| B1 | Permitted final freeze changes the exit/upkeep frontier | Complete restricted-protocol proof; `B=0` recovers J2, `B=L` permits zero upkeep at `H=L` |
| B2 | B1 is optimal over all service-preserving handover protocols | Not claimed; early routing, source responses, logs, replay, and alternate information paths can change the class |
| V1 | Both archived reports reproduce unchanged | Executed before and after new work |
| V2 | New finite checks reproduce | All research reports, including unequal proportional loss and barriers; exact certificates and floating reference checks explicitly separated |
| E1 | Copying sufficient state establishes independent essential service | Not demonstrated for an implementation; acknowledgment, independent-pipe, queue, and fence assumptions explicit |
| E2 | Positive receiver information delay forces equal source survival time | False without accounting for independent in-flight resources and permitted response delay |
| E3 | C(H) is an unavoidable total-system cost of removability | Not claimed; independent premaintenance can move upkeep outside the source objective, and early permanent activation can remove the standby problem |
| N2 | Inspected nonlinear fixed-deadline investment theorem directly gives concentration | Specified affine feasible-set and durable-duration clock reductions excluded; arbitrary reductions and priority remain unresolved |
| N1 | Current package is a meaningfully novel paper | Unresolved; current source reductions exclude several tempting claims |
| R1 | External peer review or machine-verified proofs | No; internal adversarial audits and finite code checks only |

## Reading route

1. [Heterogeneous definitions and upkeep](research/2026-09-22-heterogeneous-readiness.md),
   then the [scheduling proof](research/2026-09-22-heterogeneous-scheduling.md).
2. [Ordering failures](research/2026-09-22-ordering-limits.md) and
   [critical-budget startup](research/2026-09-22-startup.md).
3. [State-dependent scheduling](research/2026-09-22-state-dependent-loss.md) and
   [homogeneous proportional readiness](research/2026-09-22-proportional-readiness.md).
4. [Current primary-source comparison](research/2026-09-22-literature-audit.md),
   [dissipativity comparison](research/2026-09-22-dissipativity.md), and
   [internal referee assessment](research/2026-09-22-referee-assessment.md).
5. [Pass-6 residual prior art](research/2026-09-22-pass6-prior-art.md),
   [service interface](research/2026-09-22-pass6-interface.md), and
   [residual-drain results](research/2026-09-22-pass6-latency.md).
6. [Finite-update theorem](research/2026-09-22-pass7-finite-updates.md) and its
   [exact prior-art reduction](research/2026-09-22-pass7-prior-art.md).
7. [Bounded-freeze theorem](research/2026-09-22-pass8-bounded-freeze.md) and
   [pipeline interpretation and policy-class limits](research/2026-09-22-pass8-pipeline-policy.md).
8. [Arbitrary-partial fixed-loss theorem](research/2026-09-22-pass9-partial-states.md),
   [smooth full-state theorem and compactness](research/2026-09-22-pass9-smooth-partial.md),
   and [updated contribution assessment](research/2026-09-22-pass9-assessment.md).
9. [Heterogeneous proportional concentration and frontier](research/2026-09-22-pass10-proportional-frontier.md).
10. [Unequal-decay concentration](research/2026-09-22-pass11-unequal-decay.md),
    [explicit frontier and global cold-prefix separation](research/2026-09-22-pass12-unequal-frontier.md),
    and [current primary-source audit](research/2026-09-22-pass11-prior-art.md).
11. [Rate barriers and initialization](research/2026-09-22-pass13-barriers-startup.md),
    then [critical-budget startup](research/2026-09-22-pass14-critical-startup.md).

12. [Critical viability](research/2026-09-22-pass15-critical-viability.md),
    [two-module boundary](research/2026-09-22-pass15-two-module-boundary.md),
    [focused assessment](research/2026-09-22-pass15-assessment.md), and
    [operational meaning](research/2026-09-22-pass15-meaning.md).
13. [Working manuscript sources](paper/README.md) and
    [internal manuscript audit](research/2026-09-22-pass16-manuscript-review.md).

14. [Recovery verification](research/2026-09-22-pass16-recovery-verification.md),
    [fixed-deadline source comparison](research/2026-09-22-pass17-prior-art.md),
    and [source-budget assumption audit](research/2026-09-22-pass17-assumptions.md).
15. [Precision boundary](research/2026-09-22-pass18-precision.md) and
    [independent internal review](research/2026-09-22-pass18-review.md).
16. [Finite-tolerance concentration](research/2026-09-22-pass19-tolerance-concentration.md),
    [independent internal review](research/2026-09-22-pass19-review.md), and
    [updated contribution assessment](research/2026-09-22-pass19-assessment.md).

[The latest continuation](research/2026-09-22-continuation-pass18-19.md) records
the new results and exact restart instructions.

[The recovery and source-audit continuation](research/2026-09-22-continuation-pass16-17.md)
records passes 16–17. The [previous continuation](research/2026-09-22-continuation-pass15-16.md)
records passes 15–16 and the original execution interruption;
[passes 11–14](research/2026-09-22-continuation-pass11-14.md) remain recorded; the [earlier record](research/2026-09-22-continuation-record.md)
preserves passes 6–10 and their decisions.

The original license and both dated checkpoints remain unchanged. Current
assessments supersede candidate novelty wording in historical records.

## Verification route

```sh
python verify.py
python -B analysis/verify_heterogeneous.py
cmp build/heterogeneous-verification.json results/heterogeneous-verification.json
python -B analysis/verify_state_dependent.py
cmp build/state-dependent-verification.json results/state-dependent-verification.json
python -B analysis/verify_handoff.py
cmp build/handoff-verification.json results/handoff-verification.json
python -B analysis/verify_partial_states.py
cmp build/partial-state-verification.json results/partial-state-verification.json
python -B analysis/verify_proportional.py
cmp build/proportional-frontier-verification.json results/proportional-frontier-verification.json
python -B analysis/verify_unequal_proportional.py
cmp build/unequal-proportional-verification.json results/unequal-proportional-verification.json
python -B analysis/verify_critical_viability.py
cmp build/critical-viability-verification.json results/critical-viability-verification.json
python -B analysis/verify_precision.py
cmp build/precision-verification.json results/precision-verification.json
python paper/build.py
```

Exact fixed-rate checks include 640 heterogeneous models, 3,592 DP/permutation
comparisons, 4,932 deadline probes, 2,232 homogeneous comparisons, reflected
potential inequalities, ordering witnesses, and startup constructions across
729 parameter choices. The smooth verifier separates exact local algebra from
floating evaluations of logarithms/exponentials and reports tolerances.
Counts are not independent experiments. The continuous-time theorems rest on
the written proofs; no verification run establishes novelty or an application.

The recovered-source verification note records actual execution and the new
report's reproducibility; it does not invent a comparison with lost original
bytes. [Committed-snapshot verification](research/2026-09-22-committed-checkpoint-verification.md)
records actual fresh-archive execution and the byte-identical PDF rebuild.

## Next decisive work

Test the strengthened unequal-rate exchange against primary-source nonlinear
investment and nested-allocation theorems. In particular, a coupled change to
completion-time variables has not been excluded by the earlier common-clock
comparison. Preserve exact overlaps, distinguish a new derivation from priority,
and keep the ideal service contract and independent-resource counterpolicies
explicit. Avoid adding a general tolerance solver before this contribution
test is settled.
[CURRENT.md](work_orders/CURRENT.md) specifies the active task.
