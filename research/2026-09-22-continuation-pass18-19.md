# Precision and concentration continuation: passes 18–19

22 September 2026. This session began from main
16dca7e14950e13e4a292600ee39b2a3aeca9ec1. Passes 16–17 recovered executable
sources, completed a source comparison, and audited the service assumptions;
see continuation-pass16-17.md. No lost original report/PDF identity is claimed.

## Results now established internally

Pass 18 defines a single request-time preparation deficit and proves its
strict-order one-sided envelope. With finite cold exit, that envelope is
continuous on the preparation box. Its minimum equals the original minimum
under strict budget slack; fixed-positive-tolerance costs converge to it for
positive deadlines. An exact two-module critical example has original upkeep
1 and limiting upkeep 7/6, with positive-tolerance cost 7/6+5*epsilon up to
epsilon=1/15 and infeasibility above. The jump persists as epsilon tends to
zero. It is stronger than the elementary positive-margin cost, which already
precludes exact critical indefinite readiness at every positive tolerance.

Pass 19 resolves both structural gaps left in the pass-18 note. Every
minimizing nominal state at fixed positive tolerance concentrates, for unequal
positive decay coefficients and all feasible budgets. Every limiting-envelope
minimum also concentrates, including upkeep above the normal budget. Each
fixed-preparation stage defines an increasing concave map of global time.
Their composition satisfies G(t)>=t*G'(t); this forces every stationary
interior pair exchange to have a negative second derivative. The exchange
allows prepared intermediate modules, including ones at their caps.

The full note states a capped-allocation theorem with nonnegative fixed
support charges, then applies it exactly to nominal tolerance. Its common-
coefficient route remains ordinary linear allocation. The earlier assumption
that only cold intermediate stages could be handled was an incomplete proof
route, not a counterexample. Preserve the pass-18 open-question language as
historical and read it together with the pass-19 resolution.

The new proof does not automatically give a tolerance frontier algorithm or
inherit the earlier O(n*3^n) bound. Nominally full modules remain subfull at
request time and must themselves be scheduled. The maintained state and the
worst-corner state are explicitly distinguished in the paper.

## Proof and artifact evidence

The pass-18 and pass-19 reviews independently checked the complete derivations
and final compressed manuscript sections. They found no mathematical defect.
They are internal reviews, not external certification or a priority search.

The new Fraction-only checker compares 91 strict-oracle states and 91 original-
oracle states; enumerates exact LP vertices for ten tolerance instances;
checks the pass-17 nonconvex midpoint certificate; and checks three rational
states of a prepared-middle exchange. Both neighboring states in that last
fixture reduce upkeep by 1/2500. This illustrates a local stationary maximum,
not a global optimizer. The report is 4,738 bytes with SHA-256
26e15a97200d47f66544ba6c42ff01d9a189a4e23455286a701ce5a772dd041c.
Optimization and immutable-checkpoint-output guards were exercised.

All nine current verification suites ran successfully after integration;
all eight generated research reports matched their tracked reports byte for
byte. LICENSE and both checkpoint trees remained identical to the starting
commit. The LaTeX build resolved its references without overfull boxes.
Every page of the final 20-page PDF was rendered and visually inspected.
The pre-metadata-fix working artifact was 407,549 bytes with SHA-256
1466531cb0d9443c58ca3f50defde2cb43e90a7785ae4ef00886a72d717f7058.
These are actual integrated-working-tree checks. The separate committed-
snapshot record records the archive tests and the final reproducible PDF;
do not infer that a working-tree run alone verifies a published commit.

## Restart exactly here

1. Read WORKSPACE.md from the actual current branch, then AGENTS.md, README.md,
   STATUS.md and work_orders/CURRENT.md. Reconcile the remote branch rather
   than resetting to an old provenance hash.
2. Read the complete pass-19 tolerance-concentration proof, pass-19 review,
   pass-19 assessment, and pass-18 precision proof. The key paper result is
   Proposition 7.3 in the current 20-page artifact; the numbered labels can
   change in later builds. Keep the original concentration theorem central.
3. Run the nine commands and eight report comparisons in STATUS.md without
   optimized Python. Build paper/build.py and inspect changed pages.
4. Continue pass 20's targeted prior-art comparison. Its opening note already
   gives an exact coupled completion-time formulation and linked objective;
   those identities were independently checked. The source comparison of
   this formulation has not yet been performed. The next action is the
   bounded primary-source inspection described in CURRENT.md, not another
   derivation of the same algebra or an unrequested general solver.
5. Preserve exact prior-art reductions, the source-budget counterpolicies,
   original LICENSE and both immutable checkpoints. After a substantive pass,
   record its result, archive the current order and choose the next justified
   task. No paper submission, outreach, spending or formal release is authorized.

Submission readiness remains unestablished. The current strongest candidate
is a structural theorem for command-gated perishable preparation with linked
maintenance prices. Its robust geometry is now clearer; literature-wide
priority and a justified essential-service implementation remain open.
