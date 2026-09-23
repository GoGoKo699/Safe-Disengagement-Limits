# Passes 29–30: a minimal common-drain concentration failure

23 September 2026. The current result is a precise boundary in the existing
independent-fallback model: two common-drain modules always admit only
concentrated upkeep minima, but three can have a unique two-partial minimum.
The three-module failure survives fixed positive request tolerance, finite
cold startup, and a relative open neighborhood of common-drain parameters.
Manuscript writing remains the final step. Publication novelty and an
operationally justified application are still unresolved.

## 1. The surviving central claim

Initial preparation is perishable at rates bounded by $\gamma_i p_i$.
Full-state ownership handoff stops that loss, but an immutable residual
drain retains the source reservation until its end. Upkeep prices equal
the physical decay coefficients. The source remains cooperative throughout
the allowed grace period, and an independently provisioned receiver takes
over new essential service at ownership handoff.

| Assumptions | Minimum-upkeep structure | Proof |
|---|---|---|
| Instantaneous release, arbitrary finite module count and positive coefficients | Every minimum has at most one partial module | Pass 11, extended to nominal tolerance in pass 19 |
| Arbitrary independent drains, common coefficient, arbitrary finite module count | Every minimum has at most one partial module | Pass 28 |
| Common drain, two modules, unequal positive coefficients allowed | Every minimum has at most one partial module | Pass 26 |
| Common drain, three unequal-coefficient modules | Concentration can fail at a unique global minimum | Passes 29–30 |
| Common drain, no initially cold module at a minimum | At most one partial module | Pass 29 boundary-face theorem |

Thus three is the smallest module count for common-drain failure. This is
not a classification of all unequal-coefficient systems. In particular,
the displayed example uses three distinct coefficients; the sharp boundary
in coefficient classes is not established and is not the next task.

The exact fixture has $s=1$, $\gamma=(2,1,3)$, common
$\ell=\log2$, and removal deadline $H=\log8$. Its unique optimum is

$$x^*=(3/100,1/8,0),\qquad C(H)=37/200.$$

Every concentrated ready state costs strictly more than $1851/10000$.
For the one-time request-deficit contract, the exact nominal frontier is

$$
C_\epsilon=37/200+3\epsilon,\qquad
p^*_\epsilon=(3/100+\epsilon,1/8+\epsilon,0),
\quad 0\leq\epsilon\leq1/30000.
$$

The nominal optimizer is unique on that certified interval. Its endpoint
does not assert infeasibility or a different optimizer beyond the interval.
The open-family result concerns persistence of nonconcentration with a
fixed positive tolerance and slack, not persistence of these exact rational
optimum coordinates or this affine formula at perturbed parameters.

## 2. What was actually learned

The work order began with cold work interrupting two partial modules as the
possible obstruction. The successful example needs no interruption or
unequal handoff deadlines. A cold final module cannot reach its preparation
cap until both earlier reservations release. Meeting its deadline therefore
couples both earlier handoff times. Splitting maintained preparation across
those earlier modules can be strictly cheaper than fully preparing either
one or preparing only one partially.

The positive coefficients of proportional loss are essential to the model,
but proportional loss by itself does not force concentration once this
release timing is accounted for. The common-drain two-module proof succeeds
because its timing variation has no additional cold terminal constraint.
The additional cold constraint changes that geometry, even when every
allowed schedule can be reduced to a serial witness for the particular
low-budget fixture. Scheduling preemption and preparation concentration are
therefore separate questions.

A failed earlier calibration had a strict two-partial local minimum but a
cheaper concentrated schedule. It remains recorded with an exact comparison.
The successful global proof is stronger for a specific reason: cap-rate
barriers force both earlier handoffs into the interval before any release;
two justified constant-capacity front-loadings then cover arbitrary
prewarming, parallel inputs and interruption. Six exact inequalities exclude
every concentrated state below a larger budget. A further global convexity
bound proves the exact unique optimum. No time grid or numerical scheduler
supplies those global quantifiers.

## 3. Operational meaning and source comparison

The conditional design decision is now sharper: under the stated interface,
equal drain bounds do not justify restricting the maintained design to full
modules plus one partial module. The counterexample quantifies a strictly
positive recurring source-budget penalty for doing so. There is spare normal
capacity, finite cold warmup and positive request tolerance; the finding does
not rely on a critical-budget startup singularity or an infinitesimal
accuracy limit.

The interface remains an idealization. Preparation must stand for sufficient
handover state; the receiver must independently sustain new essential work;
the old source must remain responsible only for immutable obligations whose
drains use the already charged reservations. Proportional invalidation is
an adversarial fluid law, not a measured universal update model. The source
budget excludes separately provisioned receiver resources. Free independent
premaintenance and early permanent transfer remain material counterpolicies
to broader claims. No implementation or unavoidable total-system shutdown
cost is inferred.

The [bounded source audit](2026-09-23-pass29-prior-art.md) inspects complete
relevant results in resource-producing project scheduling and budget
minimization. Endogenous resource release, initial investment and clustering
exchanges are established. The tested direct mappings do not preserve the
joint initial-preparation objective, calendar-time loss and handoff deadline.
This is a scoped mapping result, not literature-wide priority clearance.
The source that uses process-local resource profiles does not by itself
model continuing decay while a preparation task is paused.

Root separately read the first source's model, full relevant exchange proofs
and continuous extension, and the second source's model and full Theorem 2 /
Corollary 3 proofs. The second PDF request failed, but its versioned primary
HTML was accessible. No new source is being accepted solely on a delegated
summary, and no third-party full text was stored in the repository.

## 4. Proof and verification route

1. [All-policy separation and failed calibration](2026-09-23-pass29-cold-test.md).
2. [Exact unique optimum](2026-09-23-pass30-exact-optimum.md).
3. [Exact positive-tolerance frontier, warmup and open-family proof](2026-09-23-pass30-robust-common-drain.md).
4. [Boundary faces](2026-09-23-pass29-boundary-faces.md) and
   [slower-cold preservation and rational certificates](2026-09-23-pass29-preserving-attempt.md).
5. [Independent internal review](2026-09-23-pass29-30-review.md) and
   [source comparison](2026-09-23-pass29-prior-art.md).
6. [Exact arithmetic verifier](../analysis/verify_common_drain.py) and
   [tracked finite report](../results/common-drain-verification.json).

The verifier checks exact identities and strict rational inequalities. It
does not certify the continuous-time transformations, compactness, uniqueness
over all policies, open-neighborhood argument, or novelty. Those statements
rest on the complete proofs and internal adversarial reviews. These reviews
are not external human certification.

## 5. Next contribution decision

The mathematical boundary now has an exact optimum and explicit robustness,
so adding another module, coefficient class or price variant is not the
next justified step. The next pass must assess whether the surviving claim
is meaningfully different from the closest preparation-investment and
deteriorating-task allocation results, and whether one concrete service
interface warrants the charged-source assumptions. If the result reduces
to prior work, record the reduction. If the interface cannot be justified,
retain an explicitly abstract resource-allocation theorem and reassess its
significance; do not invent an engineering deployment to rescue it.

The project remains in research. A theorem with a complete internal proof
and reproducible arithmetic is not, by itself, submission readiness.
