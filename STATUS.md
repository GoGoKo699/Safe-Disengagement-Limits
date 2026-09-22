# Research status

**22 September 2026 — lead workspace research, passes 1–10.**
Latest continuation started from `main` at
`a1583cda84eddb9d1b0552358f48b5c8ccdd08b8`.

## Decision

Continue theorem-led research. The exit oracle now covers arbitrary partial
preparation for fixed and monotone smooth loss. Compactness gives an attained
heterogeneous smooth upkeep optimization, and the common proportional-coefficient
subclass has an explicit concentration theorem and computable frontier. Cold
startup remains distinct from paid initialized upkeep. Meaningful publication novelty
and a validated fallback interface remain unresolved. The homogeneous clearing
formula reduces to prior scheduling; bounded-storage averaging is established;
even the heterogeneous serial objective belongs to an existing scheduling
lineage. Fixed-capacity decay also reduces to ordinary workload conservation.
These reductions narrow the possible contribution to the coupled capacity-release
theorem, whose novelty remains unresolved against close inaccessible sources.

The finite-record audit now separates source departure, independent
recoverability, exact receiver freshness, and response deadlines. Delayed
capacity release breaks serial optimality; atomic updates make age part of
readiness; allowing a bounded final freeze changes the recurring cost. The
finite-update upkeep calculation reduces exactly to a standard sporadic task,
and the frozen-copy allowance is established migration practice. These are
useful corrections and benchmarks, not replacement novelty claims.

No submission readiness, complete manuscript, formal release, external review,
or engineering validation is asserted.

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
| L1 | Adding drain time to the old serial recurrence remains optimal | False; exact two-module optimum `3` versus `10/3` |
| L2 | Overlapping drains restore uninterrupted-preparation optimality | False; exact three-module optimum `37/9` versus best uninterrupted `38/9` |
| L3 | Fixed-loss upkeep reduction survives independent residual drains | Proved using actually deadline-feasible subsets; the new oracle is not solved; no feasible state below `max ell_i` |
| J1 | A copied-work amount suffices to characterize spaced-update readiness | False; identical cold preparation has exit bounds `L` or `2L` depending on update age |
| J2 | One-version spaced-update recurring frontier | Proved with specified event priority and cold-at-update initialization; exact reduction to sporadic-task scheduling |
| J3 | A mean dirty-rate substitution recovers atomic-reset readiness | False in both directions; distinct uncertainty sets explicitly compared |
| B1 | Permitted final freeze changes the exit/upkeep frontier | Complete restricted-protocol proof; `B=0` recovers J2, `B=L` permits zero upkeep at `H=L` |
| B2 | B1 is optimal over all service-preserving handover protocols | Not claimed; early routing, source responses, logs, replay, and alternate information paths can change the class |
| V1 | Both archived reports reproduce unchanged | Executed before and after new work |
| V2 | New finite checks reproduce | Fixed-rate/startup, handoff, partial-state, and proportional-frontier reports; exact arithmetic and floating analytic checks explicitly separated |
| E1 | Copying sufficient state establishes independent essential service | Not demonstrated for an implementation; acknowledgment, independent-pipe, queue, and fence assumptions explicit |
| E2 | Positive receiver information delay forces equal source survival time | False without accounting for independent in-flight resources and permitted response delay |
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

[The continuation record](research/2026-09-22-continuation-record.md) records
the decisions between passes and the remaining submission-readiness gates.

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
```

Exact fixed-rate checks include 640 heterogeneous models, 3,592 DP/permutation
comparisons, 4,932 deadline probes, 2,232 homogeneous comparisons, reflected
potential inequalities, ordering witnesses, and startup constructions across
729 parameter choices. The smooth verifier separates exact local algebra from
floating evaluations of logarithms/exponentials and reports tolerances.
Counts are not independent experiments. The continuous-time theorems rest on
the written proofs; no verification run establishes novelty or an application.

## Next decisive work

Assess the full-state serial reduction and explicit proportional frontier against
the closest scheduling theorems, and test the scope of concentration without
claiming a new method merely from the subset or knapsack calculations. The
finite-state interface is now explicit enough to expose consequential control
restrictions; it still does not validate instantaneous safe handoff. Do not begin
a manuscript merely to package accumulated lemmas. [CURRENT.md](work_orders/CURRENT.md)
contains exact restart commands, source gates, and the next concrete decision.
