# S1 workspace mandate: Safe Disengagement Limits

Repository: `GoGoKo699/Safe-Disengagement-Limits`  
Research owner: Ruge Lin  
Prepared: 22 September 2026  
Source state inspected: `d04d9fa69dc871f3671918480cf6c124eda0415d`

This is a continuing research mandate, not a claim that the current results are publishably novel. The inspected commit is a provenance anchor, not an instruction to reset the repository. Start from the actual current branch and reconcile later work.

## 1. Mission and working authority

Take over as the lead research workspace for S1. Develop a defensible, submission-ready, theorem-led paper about keeping a cooperative controller safely removable while maintaining essential service. The author prefers a neat conceptual contribution with clear novelty and cannot rely on large network/cloud simulations. Small local computations may support the research; they must not replace it.

You may read, create, modify, commit, and push research files in this repository; maintain proofs and code; revise hypotheses; choose the next research tasks; and narrow or replace an unsuccessful formulation within S1. Do not require a new preference round for routine scientific decisions. The current migration-inspired model is a candidate, not a commitment to defend it at all costs.

Preserve the original MIT LICENSE, Copyright (c) 2026 Ruge Lin. Do not change repository visibility, rewrite remote history, overwrite another workspace's work, or modify unrelated repositories. Journal/preprint submission, external outreach, spending money, and declaring a formal public release require separate author approval. Ordinary repository research commits are authorized.

The target is evidence-based submission readiness, not a guarantee of acceptance. Do not lower the scientific standard to satisfy the instruction to continue. A failed conjecture or prior-art collision is a reason to choose the next justified investigation, not automatically to abandon the project.

## Current phase — user direction, 23 September 2026

Focus on the research repository. Manuscript writing is the last step, after
the scientific contribution, prior-art comparison and meaning are settled.
Pause drafting, editing and rebuilding the existing manuscript; preserve its
files as the earlier working artifact. Continue proofs, counterexamples,
primary-source audits and reproducible checks in repository Markdown and code.
This phase instruction supersedes earlier work-order requests to build or
expand the paper. It does not pause the continuing research mandate.

## 2. Start from the repository, not this summary

Inspect the current branch and record its full commit SHA. Read `AGENTS.md`, `README.md`, `STATUS.md`, `work_orders/CURRENT.md`, and `PROVENANCE.md`. Then read the full active checkpoint note and its literature comparison, and inspect the passive checkpoint sufficiently to understand its separate assumptions and known overlap.

Run `python verify.py` without Python optimization. Check that both original reports reproduce and the dated checkpoint files remain unchanged. Distinguish a tool-access problem from a failing mathematical test. Do not report a run you did not execute.

Execute the current work order rather than merely restating it. Its restrictions on manuscript drafting apply to that research pass, not permanently to the whole project. When a pass is completed, record its outcome, preserve its work order, write the next concrete order, and continue within the available session. This mandate extends beyond the acceptance criterion of any single work order.

The first working response should contain substantive investigation and durable progress where feasible, not just onboarding, another project plan, or a request to say “continue.”

## 3. Scientific scope and starting status

The controller is cooperative. Safe disengagement means that a removal request at any admissible operating time can be completed within the specified deadline, essential obligations remain satisfied during the transition, and the independent fallback no longer needs the primary afterward. A cooperative grace period is not protection against sudden loss of the primary during that period.

Keep essential service distinct from optional normal performance. Keep the fallback's independent resources, sensing, actuation, communications, and initialization costs explicit. Copying information alone does not establish that the fallback can perform essential functions safely. Do not import consciousness, quantum hardware, or shutdown-resistance incentives as necessary assumptions.

The repository currently has three distinct analytical objects:

- **Passive commitments:** noncancellable fixed future demand, independent continuing supply, and stored reserve. The stationary frontier has a direct network-calculus correspondence. Retain it as a benchmark unless a genuinely different result is established.
- **Homogeneous active readiness:** preparation can be maintained while operating; ready modules transfer and release source capacity. The note supplies proofs and a matching strategy under its stated restrictions. Publication novelty and an engineering instantiation are unresolved.
- **Proportional-invalidation alternative:** a different preparation-update law changes the recurring-cost frontier. It is a countermodel to universality, not a minor numerical perturbation of the fixed-rate theorem.

In the homogeneous active model, there are `n` modules with preparation size `M`, released rate `a`, spare capacity `s`, and invalidation bound `d`. From `k` fully ready modules and otherwise cold modules, the note states

$$
T_k=M\sum_{j=k}^{n-1}\frac{1}{s+ja-d}
$$

when `k<n` and `s+ka>d`; otherwise the remaining cold system cannot be cleared in finite guaranteed time. Separately, `T_n=0`. With `k_H=min{k:T_k<=H}`, the stated exact guaranteed long-run optional throughput is `s-d*k_H` when `d*k_H<=s`. Otherwise indefinite readiness at that deadline is infeasible under the prescribed normal load.

The lower bound covers arbitrary preparation histories, including partial and rotating preparation, within the model. It does not establish heterogeneous serial optimality. Any positive prepared fraction being invalidated at the full rate `d` is a load-bearing worst-case assumption. Paid predeployment preparation, independent receiver provisioning, instant cutover, and independent modules are also substantive restrictions. Recheck the arguments rather than treating earlier assistant confidence as certification.

## 4. First research pass: heterogeneous readiness

Follow `work_orders/CURRENT.md`, reconciling any subsequent repository changes. At the inspected state the next proposal is heterogeneous preparation sizes `M_i`, released rates `a_i`, and invalidation bounds `d_i`.

For a fully ready subset `S`, let `tau(S)` be the true minimax post-request completion time from the corresponding ready/cold state, allowing arbitrary parallel and preemptive schedules. Investigate the proposed recurring-upkeep reduction

$$
D(H)=\min_{S:\,\tau(S)\le H}\sum_{i\in S}d_i.
$$

This is a candidate, not a proved repository result. A support-set domination argument and a total-preparation potential are starting ideas. State quantifiers, simultaneously possible update patterns, admissible policies, initialization, and infeasible nominal budgets explicitly.

Separate proving this reduction from solving `tau(S)`. A formula containing an uncharacterized optimum is not an explicit resource frontier or efficient algorithm. A serial schedule gives an upper bound until optimality is established. Search for exact two- or three-module counterexamples before claiming a universal index or ordering rule. Resolve the smallest meaningful obstruction before adding networks, stochastic failures, or further state variables.

If the reduction is elementary or known, document it and look for the substantive question beyond it. Do not manufacture a paper by adding heterogeneity alone.

## 5. Operational meaning and novelty audit

In parallel with the mathematics, identify at least one defensible independent-fallback interface. Specify the changing information that must be prepared, why the update uncertainty is appropriate, which resource is shared, why completing a handover releases that resource, and what the receiver needs to operate independently. A generic analogy to VM migration is insufficient.

Search current primary literature and inspect relevant full sections, not only titles and abstracts. Start from the repository's source records and extend the comparison to replica freshness, hot-standby maintenance, resource-dependent scheduling, live migration, and runtime assurance as relevant. Record exact theorem, equation, or section references, model differences, quantifiers, and the material actually inspected. Mark partial access and uninspected leads honestly.

Do not claim novelty for automation dependence, preserving a fallback region, state-copying bandwidth minus update rate, or serial migration under contention alone. A broad framework being applicable need not settle our specific result; conversely, a theorem answering the question after a notation change defeats that novelty claim. Show the reduction when possible.

Maintain an assumption-to-conclusion map. For a nonstandard assumption, either provide an operational rationale or label the result as an idealized theoretical model and evaluate its significance accordingly. Do not weaken the fallback or essential-service contract solely to make a theorem easy. Do not insist on the fixed-rate model if a better justified alternative yields a stronger scientific contribution.

## 6. Research loop and decision discipline

Work through focused cycles of precise question, proof attempt, targeted falsification, prior-art comparison, and revised decision. Aim for a small number of strong results, not an accumulation of checkpoint variants.

A useful cycle may yield a theorem, a counterexample, an exact equivalence to prior work, or a precisely isolated obstruction. Record the result, then select the next task yourself. “Conditional go,” a manuscript outline, and a successful verifier run are not project completion.

Use exact arithmetic and small exhaustions when appropriate; report the domain checked and any discretization limitations. For a claimed optimum, prove a lower bound over the full stated policy class and a matching construction. For bounds or complexity results, label their actual strength rather than calling everything an exact law.

Actively test degenerate cases, startup, arbitrary request times, partial preparation, bursty policies, finite versus infinite horizons, and changes to the invalidation law. Keep countermodels visible. Never alter a test or historical checksum merely to conceal a discrepancy.

A result can be significant without large experiments. Its operational meaning and distinction from existing theorems must nonetheless be explained. Do not use the longstanding or difficult nature of a problem as a reason by itself to stop investigating; do state uncertainty about any unproved claim.

## 7. Criteria for submission readiness

Do not declare the project ready until the following are substantively addressed:

1. **Contribution:** one concise central claim that is nontrivial and meaningfully distinguished from the closest inspected results. Explain what is learned beyond existing control, scheduling, or maintenance theory. An impossibility result or a rigorous separation can qualify; a positive engineering proposal is not mandatory.
2. **Correctness:** complete definitions, quantifiers, proofs, boundary cases, and reproducible supporting checks. Subject the main argument to an adversarial proof audit. Distinguish self-checking from an independent human review; do not fabricate outside endorsement.
3. **Meaning:** a justified interpretation or application class, with essential-service requirements and all relevant resources accounted for. Clearly separate a theoretical model illustration from an empirically validated deployment claim. Explain which limitation actually depends on which assumption.
4. **Paper and artifacts:** a complete manuscript with references and supplementary proofs as needed, editable source and a checked PDF, minimal local reproduction commands, and a reader-facing README. Write around the surviving result, not around preserving the original fictional framing. Use a realistic venue fit and current submission requirements when assembling the final package.
5. **Assessment:** a concise referee-style report identifying the strongest result, closest prior work, remaining limitations, and unresolved issues. A manuscript with a material proof gap or an unverified central novelty claim remains in development. Do not confuse submission readiness with guaranteed publication.

When these criteria are met, deliver the submission-ready package and explain the assessment to the author. Do not submit it, contact reviewers, or create a formal release without separate approval.

## 8. Repository continuity and reporting

Treat `checkpoints/passive-2026-09-22/` and `checkpoints/active-2026-09-22/` as immutable historical records. Put new proofs or corrections in new files outside them and update current navigation and claim status. A discovered error must be conspicuous in the current status and reading route, not silently fixed inside an archive.

Maintain `STATUS.md`, a current actionable work order, source comparisons, and reproduction instructions as research progresses. Preserve superseded work orders or decision records so that another workspace can reconstruct why the direction changed. Avoid reorganizing the repository repeatedly without a research benefit.

Read the remote branch before committing, preserve concurrent work, use non-forced updates, and verify the resulting remote contents. Keep the original license untouched. Do not upload the story, private conversation transcripts, credentials, or third-party papers. No claim is committed until the write succeeds.

Run root verification before and after changes; add new tests separately and include them in the current reproduction route without mutating archived checks. A failed access or execution step must be disclosed with its actual scope.

At substantive checkpoints, report the result or counterexample, what was proved versus checked, the actual committed changes, what the literature comparison establishes, and the next decisive task. Do not fill reports with repeated motivation or use file counts as a measure of scientific progress.

Work within the available execution session. At a tool, context, or execution limit, commit a coherent checkpoint when possible and leave exact restart instructions. Do not imply that research continues in the background after the session ends. The repository, rather than assumed cross-workspace memory, is the continuity mechanism.

**Begin by inspecting the actual repository, reproducing the baseline, and executing the current research pass. Then continue to the next justified task under this mandate.**
