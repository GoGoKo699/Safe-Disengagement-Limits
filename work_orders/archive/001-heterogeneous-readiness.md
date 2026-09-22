# S1 next research pass: heterogeneous readiness and operational meaning

**Status:** pending. Bootstrap and reproduction are complete; this research pass has not been executed by the bootstrap.

## Objective

Determine whether the active-readiness result exposes a useful structural principle beyond identical modules, and audit that principle against existing replication/maintenance theory. Keep the work analytical and locally checkable.

## Starting point

Read STATUS.md and the active NOTE.md, especially preparation dynamics, Proposition 1, Theorem 2, startup accounting, and the proportional countermodel. The historical passive model is a benchmark, not the same control problem.

## Work

1. Formulate heterogeneous sizes `M_i`, released capacities `a_i`, and invalidation bounds `d_i`, retaining a shared spare budget and genuine independence after exit. State which capacities and update histories can occur simultaneously. Initially avoid adding a graph, stochastic failures, or an unknown controller.

2. Test the following proposed reduction; it is not a proved repository result. For each initially ready subset `S`, let `tau(S)` be the true minimax post-request completion time from that ready/cold state, allowing arbitrary parallel and preemptive schedules. Does minimizing `sum_{i in S} d_i` subject to `tau(S)<=H` exactly characterize sustainable recurring upkeep? A support-set domination plus total-preparation argument is a candidate route. Treat initialization and infeasible nominal budgets explicitly. Do not present this as an explicit computable frontier until `tau(S)` is characterized.

3. Investigate the scheduling subproblem in the smallest nontrivial heterogeneous family. A plausible serial strategy gives an upper bound, not an optimum. Look for a two- or three-module counterexample before asserting any index/order rule. Distinguish exact rational counterexamples from discretization artifacts. Escalate to a broader model only when it answers a concrete obstruction.

4. Find a defensible independent-fallback interface and a matching update uncertainty model. Search and inspect primary sources on recurring replica freshness, hot standby maintenance, and resource-dependent migration. Record any exact theorem-level overlap. Constant dirty-rate precedent does not by itself justify full-rate invalidation of every arbitrarily small prepared fraction.

## Deliverables

A new dated note outside the immutable checkpoints; explicit proof status for each claim; small verifier/counterexample checks where useful; source-level comparison; updated STATUS.md and this work order. Keep failed conjectures and exact prior-art reductions as findings.

## Acceptance and scope

A successful pass can end in a proof, a counterexample, an exact reduction to established work, or a clearly isolated unresolved step. It need not manufacture a positive result. It may not declare an uncharacterized scheduling oracle solved, claim an application without an interface, or promote finite tests to a theorem.

No large simulations, cloud jobs, manuscript drafting, venue ranking, or new user preference round. Run root verification before and after changes; preserve LICENSE and historical checkpoint hashes. Report the actual commit and remaining research decision.


## Completion record — 22 September 2026

Executed from `dbafc04df679ce5b5d22a8c9654c85dbea234cb0`. Heterogeneous
seriality and the exact recurring reduction are proved in the new research
notes, with a finite subset algorithm and separate exact verifier. The first
pass led to ordering/prior-art, startup, and state-dependent-loss passes rather
than ending at the oracle reduction. This file preserves the initial work order;
the pending label above describes its starting state.
