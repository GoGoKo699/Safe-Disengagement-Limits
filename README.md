# Safe Disengagement Limits

**How much useful operation must a system give up to keep its controller safely removable?**

Theory-first research on cooperative, bounded-time handover to an independent fallback. The controller obeys the removal request; the difficulty is keeping essential service running after it leaves. This project studies resource accounting, not an agent's incentive to resist shutdown.

**Research status:** every upkeep-minimizing state has at most one partial
module under unequal positive proportional loss, even with inaccessible initial
rates. An explicit frontier accounts for cold modules before that partial module.
Rate barriers and critical-budget startup have separate exact results. These
are theorems in an idealized instantaneous-handoff model; publication novelty
remains **unestablished**. There is no validated implementation, external proof
review, or submission-ready paper. See [STATUS.md](STATUS.md).

## Start here

| Reading goal | Entry point |
|---|---|
| Read the strongest current result | [Unequal-decay concentration](research/2026-09-22-pass11-unequal-decay.md) and [explicit frontier](research/2026-09-22-pass12-unequal-frontier.md) |
| Check the all-state scheduling foundation | [Fixed-loss seriality](research/2026-09-22-pass9-partial-states.md), [smooth extension and attained upkeep](research/2026-09-22-pass9-smooth-partial.md) |
| Separate paid initialization and cold startup | [Rate barriers and upkeep floor](research/2026-09-22-pass13-barriers-startup.md), [critical-budget criterion and counterexamples](research/2026-09-22-pass14-critical-startup.md) |
| Compute the common-decay rational specialization | [Concentration theorem and exact transformed-deadline frontier](research/2026-09-22-pass10-proportional-frontier.md) |
| Understand the latest interface findings | [Acknowledged obligations and positive delay](research/2026-09-22-pass6-interface.md), [pipeline policy limits](research/2026-09-22-pass8-pipeline-policy.md) |
| See what delayed capacity release changes | [Exact overlap/preemption counterexamples and surviving upkeep reduction](research/2026-09-22-pass6-latency.md) |
| Account for finite updates and service slack | [Atomic-update theorem](research/2026-09-22-pass7-finite-updates.md), [bounded final freeze](research/2026-09-22-pass8-bounded-freeze.md), [sporadic-task reduction](research/2026-09-22-pass7-prior-art.md) |
| Understand the current candidate result | [Heterogeneous readiness: definitions and exact upkeep](research/2026-09-22-heterogeneous-readiness.md) |
| Check the all-policy exit optimum | [Weighted-potential proof and subset algorithm](research/2026-09-22-heterogeneous-scheduling.md) |
| See why simple ordering rules fail | [Exact ordering counterexamples](research/2026-09-22-ordering-limits.md) |
| Separate startup from long-run upkeep | [Exact two-module cold-start threshold](research/2026-09-22-startup.md) |
| Change the invalidation law | [State-dependent erosion and serial dominance](research/2026-09-22-state-dependent-loss.md) |
| Read the explicit continuous upkeep frontier | [Homogeneous proportional readiness](research/2026-09-22-proportional-readiness.md) |
| See the assumption that changes the conclusion | [Proportional-invalidation countermodel, section 8](checkpoints/active-2026-09-22/NOTE.md#8-assumption-stress-test-a-smooth-alternative-removes-the-staircase) |
| Check overlap with established research | [Latest concentration audit](research/2026-09-22-pass11-prior-art.md), [full-state contribution assessment](research/2026-09-22-pass9-assessment.md), [earlier coupled-scheduling audit](research/2026-09-22-pass6-prior-art.md), [source reductions](research/2026-09-22-literature-audit.md), and [dissipativity reduction](research/2026-09-22-dissipativity.md) |
| Audit the proof boundaries | [Internal proof audit](research/2026-09-22-proof-audit.md) and [referee-style assessment](research/2026-09-22-referee-assessment.md) |
| Understand the earlier benchmark | [Passive commitments](checkpoints/passive-2026-09-22/NOTE.md) |
| Reproduce the finite checks | Run `python verify.py` from the repository root |
| Continue the investigation | [Current work order](work_orders/CURRENT.md) and [agent instructions](AGENTS.md) |

A first reading should pair a mathematical result with its interface and
prior-art boundaries. The homogeneous result below is a simple special case.
Both dated checkpoints remain immutable historical records.

## Full-state results

An exchange argument now proves that some full-speed serial exit schedule is
optimal from **every** initial preparation vector, for both reflected fixed
loss and nondecreasing Lipschitz smooth loss vanishing at zero. Completing one
module early frees enough time to postpone the other allocations; later copying
suffers no greater terminal deterioration. A forward subset algorithm tracks
elapsed time and passive decay, so partial states are included explicitly.

For smooth loss, the deadline-ready set is compact. Minimum total loss over
that set is attained and gives exact initialized recurring upkeep. With
proportional loss `gamma_i*p_i`, **every** upkeep minimizer has a full subset,
at most one partial module, and a cold remainder. The coefficients may differ;
the theorem permits all nonnegative source budgets and capacity releases.
The proof varies two partial coordinates while preserving an exit schedule's
completion time. General smooth loss does not share this property: an exact
quadratic-loss counterexample requires multiple partial coordinates.

Unequal coefficients can make a cold prefix optimal before the partial module.
The [general frontier](research/2026-09-22-pass12-unequal-frontier.md) handles
that prefix in `O(n*3^n)` logarithmic/exponential scalar evaluations, with
`O(2^n)` working storage. These are exponential real-evaluation counts;
the reference implementation uses floating arithmetic with stated limitations.
For common `gamma` and `s>max_i gamma*M_i`, the earlier
[transformed-deadline algorithm](research/2026-09-22-pass10-proportional-frontier.md)
uses `O(n*2^n)` arithmetic operations and exact rationals when its parameters
and `X=exp(gamma*H)` are rational.

A [rate-barrier closure](research/2026-09-22-pass13-barriers-startup.md)
determines whether any finite exit is possible from the initially full set.
The cheapest successful full set gives an upkeep floor reached at a finite
deadline. If the cold state cannot exit at all, normal cold warmup cannot
reach any deadline-ready state. Even when cold exit is finite, the equality
`C(H)=s` does not decide startup: [exact contrasting examples](research/2026-09-22-pass14-critical-startup.md)
and a fixed-target criterion show why the decay rates matter.

These results retain independent instantaneous handoffs and paid initialization
unless a separate warmup construction is supplied. Classical deterioration and
controllable-processing scheduling account for several proof ingredients and
special cases. The [current comparison](research/2026-09-22-pass11-prior-art.md)
identifies the unequal-decay exchange as the residual candidate, without
claiming publication priority or a demonstrated engineering implementation.

## Ready/cold fixed-loss specialization

Module `i` has preparation size `M_i`, released capacity `a_i`, and maximum
invalidation rate `d_i`. Let `F(S)` be the optimal exit time from a fully ready
set `S` with all other modules cold, and `b(S)=s+sum_{i in S}a_i`. Then

```
F(N)=0
F(S)=min_i {M_i/(b(S)-d_i)+F(S union {i})},
       over i not in S with b(S)>d_i.
D(H)=min_{S:F(S)<=H} sum_{i in S}d_i.
```

An empty minimum for `F` is infinite. The exact guaranteed optional throughput
is `s-D(H)` when `D(H)<=s`; otherwise indefinite readiness is infeasible.
The weighted-potential proof establishes serial optimality before using the
recurrence. Evaluating all subsets costs `O(n*2^n)` arithmetic operations.
The formula covers arbitrary normal preparation histories after paid
initialization. The separate full-state theorem above supplies the formerly
unresolved extension to arbitrary partially prepared request states.

Partial preparation can still matter for **startup**. For two modules with
`d_i>0` and `s=d_1+d_2`, cold normal-operation warmup can reach exactly the
maximum-loss states with `p_1+p_2<=max(M_1,M_2)`. The smallest deadline that can
then be maintained is

```
H_warm = min(M_1,M_2) / max(a_1+d_1,a_2+d_2).
```

The full-ready state is unreachable under that critical normal budget, yet a
partial stationary state may attain this deadline. Warmup is paid, and the
guarantee begins after it. See the [example and proof](research/2026-09-22-startup.md).

With proportional loss `gamma*p`, the homogeneous model instead has a
continuous, piecewise analytic upkeep frontier. An aggregate-potential bound
shows that concentrating a prescribed total preparation into full modules and
at most one partial module gives the best exit deadline. This solves the
homogeneous smooth recurring problem for `s>gamma*M`. Passes 9–10 now extend
the state oracle and solve the heterogeneous common-coefficient subclass.
See the [earlier homogeneous proof](research/2026-09-22-proportional-readiness.md).

## Homogeneous special case

There are `n` identical, independently switchable services. While primary-controlled, each uses resource rate `a`. After this prescribed normal load, spare capacity `s` is shared between optional throughput and preparing current handover state. Full preparation requires work `M`; any positive preparation may become outdated at rate up to `d`. On a removal request, optional work stops. A fully prepared service transfers immediately to a separately provisioned fallback, releasing rate `a` for the remaining transfers. Essential service is uninterrupted, and all dependence on the primary must end within deadline `H`.

For `k` fully prepared services and an otherwise unprepared system, the exact worst-case exit time is

$$
T_k=M\sum_{j=k}^{n-1}\frac{1}{s+ja-d},
$$

when `k<n` and `s+ka>d`. Otherwise `T_k` is infinite; `T_n=0`. Define `k_H` as the smallest `k` with `T_k<=H`.

The exact maximum guaranteed long-run **optional** throughput is

$$
u^*(H)=s-dk_H,
$$

provided `dk_H<=s`. When `dk_H>s`, indefinitely maintaining that deadline is infeasible under the prescribed normal load. Keeping exactly `k_H` services fully prepared attains the bound after paid initialization. A potential argument and an averaging inequality cover parallel, preemptive, partial, and rotating preparations—not only the attaining schedule.

This does not say that full normal service has throughput `u*`: the mandatory normal load `na` is still delivered. It also does not guarantee a cold start or survival of a sudden primary failure during the cooperative grace period.

## The boundary matters

The new service analysis distinguishes receiver freshness from safe source
departure: independently sustained in-flight information can arrive after the
source leaves if the actual response deadline permits it. Positive delay and
ownership fencing still require explicit accounting. Copying alone establishes
neither independent service nor a complete handover protocol.

When capacity is released only after an immutable residual drain, overlapping
handoffs and even interrupted preparation can be strictly necessary. The old
serial recurrence cannot just acquire an extra drain-time term. Its support
upkeep argument survives only with a new, unresolved deadline-feasibility oracle.

For a single version with atomic updates separated by `Delta>M/s`, preparation
age matters. If a declared protocol permits at most `B` time units of final
frozen copying, `0<=B<=M/s`, the exact normal upkeep in that model is
`max(0,2*M-s*H-s*B)/Delta` for `H>=M/s`; smaller deadlines are infeasible at
a reset. This is a restricted protocol theorem. Its normal work constraint
reduces to standard sporadic-task scheduling, and its frozen-copy budget is
the familiar stop-and-copy allowance. Neither is presented as a new general law.

The fixed-rate invalidation assumption is load-bearing. A one-service proportional-invalidation model gives a **continuous** maintenance frontier instead of the staircase above. The staircase is not a universal law of dependence.

The independent fallback, its essential-service capability, and a sufficient handover interface are assumed, not created by copying data. Services have no shared-state cutover barriers; cutover has zero latency; receiver resources are provisioned separately. These restrictions and excluded alternatives are explicit in the [active model](checkpoints/active-2026-09-22/NOTE.md).

The earlier passive model concerns noncancellable, fixed demand profiles and independent supply plus stored reserve. Its stationary frontier overlaps directly with network calculus. It remains a benchmark, not the main publication claim. The two models must not be merged by notation alone.

## Reproduce locally

Python 3.10 or newer; standard library only:

```sh
python verify.py
python -B analysis/verify_heterogeneous.py
python -B analysis/verify_state_dependent.py
python -B analysis/verify_handoff.py
python -B analysis/verify_partial_states.py
python -B analysis/verify_proportional.py
python -B analysis/verify_unequal_proportional.py
```

The root runner checks checkpoint hashes, runs both original verifiers in temporary directories, and compares their complete reports with the archived reports. It writes `build/verification.json` without modifying the checkpoints. It refuses optimized Python because the original verifiers use assertions.

The active checkpoint includes 65,100 local maintenance-inequality cases, 27,992 transition-inequality cases, and 3,360 parameter curves. The passive checkpoint includes 9,720 frontier cases. These categories are not independent experiments, and the finite tests do not prove continuous-time claims, validate an application, or establish novelty. See [the bootstrap reproduction record](results/bootstrap-verification.json).

No large simulations, model training, external datasets, or network access are needed for these checks.

The new verifier uses exact rational arithmetic for subset/permutation
comparisons, potential inequalities, deadline endpoints, ordering witnesses,
and the two-module startup construction. Its [tracked report](results/heterogeneous-verification.json)
states every checked domain and count. It writes to `build/`; that report
must match the tracked one byte-for-byte. These checks support, but do not
replace, the continuous-time proofs.

The [separate state-dependent report](results/state-dependent-verification.json)
distinguishes exact local inequalities from floating logarithmic/exponential
identity checks with explicit tolerances. Compare both outputs with their
tracked reports using the commands in [STATUS.md](STATUS.md).

The [handoff report](results/handoff-verification.json) reconstructs the exact
drain schedules and checks finite-update/freeze identities, event boundaries,
and finite-prefix resource accounting using rational arithmetic. These are
small finite checks, not searches over all continuous-time policies.

The [partial-state report](results/partial-state-verification.json) checks the
forward algorithm against independent serial permutations, while separating
rational checks from floating smooth-flow identities. The [proportional report](results/proportional-frontier-verification.json)
checks exact transformed-deadline queries against independent per-order linear
optimization and reconstructs the returned preparation and exit witnesses. The
[unequal-decay report](results/unequal-proportional-verification.json) separates
exact algebraic and rate-barrier certificates from floating DP/permutation
comparisons. Those numerical comparisons are a reference check, not certified
transcendental deadline decisions.

## Provenance and license

The research question was inspired by the science-fiction setting of Ruge Lin's *Falling* (《坠落》). The mathematical models are explicit research formulations, not claims that the fiction's mechanisms are physically established. The story and third-party papers are not redistributed here.

The two checkpoint directories preserve the supplied research packages byte-for-byte. Their historical statements about having no repository refer to their creation time; current repository status and licensing are given here. See [PROVENANCE.md](PROVENANCE.md).

[MIT License](LICENSE), Copyright (c) 2026 Ruge Lin. The repository's original license is preserved unchanged.
