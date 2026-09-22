# S1 — Passive commitments: proof and novelty checkpoint

**Date:** 22 September 2026.  **Status:** analytical benchmark, not a manuscript or a certified novelty claim.

S1 asks when a cooperative controller can be retired while preserving service
that cannot be cancelled. This checkpoint studies a restricted model in which
past activity creates a fixed, deterministic future demand profile. It does not
model an intelligent controller's decisions about redesigning that profile.

## Main result

Let `g(a)` be mandatory resource demand at age `a` from one unit of admitted
activity, and let `G(h) = integral_h^infinity g(a) da`. Normal service capacity
is `C`. After any removal request the primary remains for at most `H` time,
after which only independent supply rate `B` and stored reserve `E` remain.
The primary cannot shorten or cancel commitments.

The maximum long-run admission rate, over all globally bounded measurable
admission histories safe for every possible request time, is

    lambda_* = min(C/G(0), inf_{s>0: Q_H(s)>0} (E+B*s)/Q_H(s)),
    Q_H(s) = integral_H^(H+s) G(h) dh.

The infimum over an empty set is infinity. Constant admission at `lambda_*`,
starting from empty history, attains the rate. Equivalently, its required stock is

    E_min(lambda,B,H) = integral_H^infinity max(lambda*G(h)-B, 0) dh.

`NOTE.md` gives definitions, resource accounting, the all-history upper bound,
a matching construction, limiting cases, and explicit limitations.

## Novelty outcome

The stationary formula corresponds to established network calculus;
the all-history upper bound uses elementary averaging.
**Do not market this checkpoint as a new general safe-shutdown theorem.**
See `LITERATURE.md` for the primary sources inspected and precise limits of
what this comparison establishes. The active-conversion problem remains open
within this project; no model, proof, or novelty claim for it is contained here.

## Verification

Run with Python 3.10 or newer, with no third-party dependencies:

    python verify.py --output validation.json

The report records exact rational checks of a finite discrete analogue and
continuous triangular-profile identities. Counts refer to different test
categories, not disjoint independent experiments. They do not replace the proof,
validate an engineering application, or establish novelty.

Files: `NOTE.md`, `LITERATURE.md`, `verify.py`, `validation.json`, `MANIFEST.sha256`.
No repository has been created, and no license has been chosen for this local
checkpoint. This package does not contain third-party article copies.
