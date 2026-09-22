# Research status

**22 September 2026 — lead workspace research, passes 1–5.**
Started from `main` at `dbafc04df679ce5b5d22a8c9654c85dbea234cb0`.

## Decision

Continue theorem-led research. The heterogeneous exit oracle is solved, cold
startup exposes a distinct role for partial preparation, and serial dominance
extends to smooth erosion. The homogeneous proportional model also has an
explicit full-state recurring frontier. However, meaningful publication novelty
and a validated fallback interface remain unresolved. The homogeneous clearing
formula reduces to prior scheduling; bounded-storage averaging is established;
even the heterogeneous serial objective belongs to an existing scheduling
lineage. These reductions narrow the possible contribution.

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
| H4 | H1 proves serial optimality from arbitrary partial initial states | Not claimed |
| I1 | Critical two-module cold reachability is `sum p_i<=max M_i` | Complete proof for `d_i>0`, `s=d_1+d_2` |
| I2 | Best post-warmup deadline is `min M_i/max(a_i+d_i)` in I1 | Complete lower bound and robust construction |
| I3 | Unreachable optimal fully ready subset precludes cold-start readiness | False; exact reachable partial-state counterexample, with unchanged upkeep |
| G1 | Ready/cold serial dominance under monotone Lipschitz state loss | Complete integral-potential proof; exact non-Lipschitz equality counterexample retained |
| G2 | Homogeneous proportional model has exact continuous upkeep frontier | Complete aggregate-potential proof for `s>gamma*M`; concentrated preparation attains it |
| G3 | Smooth heterogeneous upkeep follows from the ready/cold recurrence | Not established; full-state readiness remains unresolved |
| V1 | Both archived reports reproduce unchanged | Executed before and after new work |
| V2 | New finite checks reproduce | Exact fixed-rate/startup checks and separately labeled smooth-law analytic checks; tracked reports |
| E1 | Copying sufficient state establishes independent essential service | Not demonstrated for an implementation; explicit interface obligations recorded |
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

The original license and both dated checkpoints remain unchanged. Current
assessments supersede candidate novelty wording in historical records.

## Verification route

```sh
python verify.py
python -B analysis/verify_heterogeneous.py
cmp build/heterogeneous-verification.json results/heterogeneous-verification.json
python -B analysis/verify_state_dependent.py
cmp build/state-dependent-verification.json results/state-dependent-verification.json
```

Exact fixed-rate checks include 640 heterogeneous models, 3,592 DP/permutation
comparisons, 4,932 deadline probes, 2,232 homogeneous comparisons, reflected
potential inequalities, ordering witnesses, and startup constructions across
729 parameter choices. The smooth verifier separates exact local algebra from
floating evaluations of logarithms/exponentials and reports tolerances.
Counts are not independent experiments. The continuous-time theorems rest on
the written proofs; no verification run establishes novelty or an application.

## Next decisive work

Resolve the residual novelty against the closest primary scheduling theorems,
and make one finite-state fallback interface precise enough to test its update
and cutover assumptions. A theorem about preparation alone is not yet a service
safety certificate. Do not begin a manuscript merely to package the accumulated
lemmas. [CURRENT.md](work_orders/CURRENT.md) contains exact restart commands,
source leads, and the next concrete decision.
