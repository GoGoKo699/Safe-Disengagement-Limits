# Pass 15: critical ready-region viability and the focused paper claim

22 September 2026. Passes 11–14 are recorded in
`research/2026-09-22-continuation-pass11-14.md`; their original orders are
preserved in `archive/011...014`. This order starts after a coherent research
checkpoint, not after a declaration of novelty or submission readiness.

## Exact restart

Use the actual current branch. Never reset to a provenance SHA.

```sh
git status --short --branch
git fetch origin
git rev-parse HEAD origin/main
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
```

Read WORKSPACE.md first, then AGENTS.md, README.md, STATUS.md, the latest
continuation record, complete pass-11 concentration and source-audit notes,
pass-12 frontier, pass-13 barriers, and pass-14 critical startup. Revisit the
full pass-9 smooth proof when using all-policy seriality or compactness.
Read pass-6 interface/drain and pass-8 pipeline notes before asserting any
operational interpretation. Historical checkpoints remain immutable.

## Surviving mathematical package

Every upkeep minimizer under positive proportional loss has at most one
partial module, even with unequal coefficients and inaccessible initial rates.
An optimal cold prefix before a partial module uses only larger decay
coefficients. The explicit general frontier requires O(n*3^n) real scalar
evaluations, while common decay retains its exact rational transformed-deadline
specialization. A quadratic-loss counterexample marks a genuine boundary.

Threshold closure decides whether finite exit is possible and yields an exact
upkeep floor attained at a finite deadline. A blocked cold system cannot reach
any ready state through finite normal warmup. With C(H)<s, a finite warmup is
constructive. At C(H)=s, a specified concentrated target with one partial
coordinate is reachable exactly when some full coordinate has a larger gamma;
a nonzero pure-full critical target is unreachable. Exact positive-deadline
models show both possible answers for sustainable critical startup.

## First task: do fixed-target tests settle full-region startup?

Work within the same model, with cold exit finite and C(H)=s>0. A guarantee
begins after a finite normal-budget warmup; no module transfers during normal
operation. Determine whether indefinite robust H-readiness can be entered
from cold only if some minimizing concentrated target passes the pass-14 test.
The test is sufficient. Its necessity for the entire ready region is not proved.

1. Start with two modules. Enumerate the exact serial deadline regions and
   distinguish reaching one ready state from entering a forward viable region.
   Preserve any counterexample in exact or analytically certified form.
2. A useful intermediate proof target: on the maximal-loss history, an
   indefinitely ready critical trajectory has Q nonincreasing and finite
   integral of the excess upkeep sum(gamma_i*p_i)-s. Uniform Lipschitz bounds
   may force upkeep to s. Concentration makes the minimizing set finite
   (each full set and partial identity determine its amount at fixed cost).
   Check whether the trajectory must converge to one minimum. Convergence
   alone does not prove finite domination or reachability of that target.
3. If all minimizing targets fail the fixed-target test, either prove an
   invariant separating every cold-reachable viable trajectory from the ready
   region, or find a trajectory approaching an unreachable target while
   remaining ready. Do not assume stationary policies exhaust this question.
4. Stop extending startup if it contributes only technical volume. Record the
   exact remaining obstruction and return to the main concentration claim.

## Parallel contribution and source decision

The focused candidate is the unequal-rate concentration exchange plus its
explicit frontier and nonlinear failure. The common-rate fixed-order problem
is standard box-constrained linear allocation after the proven transform.
The latest audit has actual full-section comparisons with Shioura et al.,
Wei et al., and Gehlot et al. Their precise limitations are recorded; they do
not certify absence of an earlier unequal-rate theorem.

Compare the candidate with initial-investment/controllable-work results under
nonlinear deterioration, with maintenance weights tied to decay. Avoid
repeating inaccessible Glazebrook endpoints indefinitely. An accessible
predecessor would narrow the claim; an abstract alone cannot settle it.
Do not claim a new nonpreemption principle, subset method, or averaging law.

Make an explicit referee-style decision about a working manuscript around one
surviving claim. Explain the mathematical information gained, its ideal-model
meaning, and the exact unresolved attribution risk. Do not assemble a paper
merely to collect pass notes, nor defer all conceptual assessment by adding
more parameters. Submission readiness still requires the mandate's full
correctness, meaning, attribution, manuscript/PDF, and assessment criteria.

## Continuity and authority

Run every suite and byte comparison from a committed archive, not only the
working tree. Confirm original LICENSE/checkpoint contents and the actual
remote parent before a non-forced update. Verify the published tree equals the
tested tree and preserve concurrent work. The unequal-rate reference code uses
floating deadline comparisons and must not be described as a certified exact
solver. Ordinary research commits/pushes are authorized; outside contact,
spending, submission, and formal release require separate approval.
