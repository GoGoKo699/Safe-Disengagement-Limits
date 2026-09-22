# Pass 6: resolve the remaining novelty and interface gap

22 September 2026. **Next pass.** Passes 1–5 and their original questions are
preserved under `work_orders/archive/`; the findings are in `research/`.

## Exact restart

Work from the actual current branch; do not reset to the historical base.

```sh
git status --short
git fetch origin
git log -5 --oneline
git rev-parse HEAD origin/main
python verify.py
python -B analysis/verify_heterogeneous.py
cmp build/heterogeneous-verification.json results/heterogeneous-verification.json
python -B analysis/verify_state_dependent.py
cmp build/state-dependent-verification.json results/state-dependent-verification.json
```

Reconcile any concurrent work before editing. Read WORKSPACE.md, AGENTS.md,
STATUS.md, the heterogeneous readiness and scheduling proofs, startup,
state-dependent loss, proportional readiness, current source comparison,
dissipativity note, and internal referee assessment. Historical checkpoints and
LICENSE remain immutable. Startup is paid and its tight guarantee begins only
after warmup. All claims of novelty remain provisional.

## Question to resolve before drafting

What does S1 teach beyond existing learning/state-dependent-speed scheduling
and the standard bounded-storage averaging principle, for a defensible fallback
interface? Candidate residual claims are the all-allocation serial reduction,
its state-dependent version, and the separation between optimal recurring cost
and startup reachability. Do not assert all of these are new.

1. Inspect the complete closest primary experience-based scheduling papers,
   including Janiak et al. (2009), DOI `10.1016/j.cie.2008.07.019`, following
   the exact model mapping and access limits in the current literature audit.
   Its job-specific accumulated experience already expresses a substantial
   subclass of the heterogeneous serial objective. Determine whether its actual
   theorems also imply the arbitrary-parallel decaying-preparation reduction,
   or just solve/restrict the resulting permutation problem. Do not import
   hardness from an abstract or a broader superclass.
2. Compare the integral-potential and proportional full-state results with
   state-dependent service, learning, and deterioration models at theorem level.
   Record an exact substitution or the specific unmatched quantifier. A subset
   DP, familiar denominator, or renamed application is not a contribution.
3. Make one minimal finite-record service-shard interface explicit: sufficient
   state, acknowledged obligations, independent receiver budget, routing and
   ownership fence, positive update delay, and how cutover frees the copying
   resource. Derive its permissible erosion envelope. Test whether exact hot
   readiness survives; if it does not, preserve that obstruction and formulate
   a bounded final handoff or an explicit service tolerance without silently
   weakening the essential-service contract.
4. Use the outcome to select one central result. If the serial reduction is
   known, test the startup/readiness separation against constrained-reachability
   literature before adding new dimensions. If a meaningful residual theorem
   survives and its interface is defensible, update the mandate's readiness
   assessment and begin a manuscript around that result. Otherwise continue
   the next precise proof/counterexample/reduction task and record why.

## Boundaries and acceptance

A full paper is not authorized for submission by this work order. No outside
contact, spending, formal release, large simulation, or neural training.
A useful pass yields a proof, a genuine prior-art reduction, a concrete
interface obstruction, or a precisely isolated gap. Preserve negative findings.
Do not mistake a cold ready/cold oracle for full-state smooth readiness; do not
extend the two-module startup formula without proof. Run all current verifiers,
read the remote branch, use non-forced updates, and verify committed contents.
