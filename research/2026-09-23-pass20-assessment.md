# Pass 20 assessment: what the allocation comparison establishes

23 September 2026. Repository research only. The user's current direction
defers manuscript writing to the final stage; the existing `paper/` tree is
preserved without edits or builds. This assessment supersedes the open
comparison in the pass-19 assessment, without changing that historical note.

## Decision

The strengthened concentration theorem survives the specific prior-allocation
tests completed here. This means that the inspected theorems have not been
shown to imply its general statement; it does **not** mean publication
novelty has been established. The important progress is a more precise
comparison, including positive reductions that limit the claim.

The candidate remains: in the S1 proportional model, every minimizer of
decay-linked preparation cost under a strict-order deadline, individual caps
and nonnegative support charges has at most one interior preparation. This
includes every nominal minimum at fixed positive request-time shortfall.
All-policy seriality justifies the finite-order oracle first; the subsequent
allocation comparison need not independently reproduce the control reduction.

## Tested routes and retained overlap

| Route | Evidence and result | Scope of the conclusion |
|---|---|---|
| Deteriorating-job investment | Liu–Xiong (2021), full relevant model and allocation proofs: fixed-order inverse-power allocation becomes a convex cost of affine time increments. S1 raw timing caps can be nonconvex. | Direct investment and invertible affine timing identifications do not supply the theorem. Arbitrary nonlinear encodings are not excluded. |
| Nested convex allocation | Vidal–Gribel–Jaillet (2019), complete model and Theorem 2 proof: convex separable costs with affine nested sums. | Its stated monotonicity result does not give the S1 endpoint/every-minimizer conclusion by the displayed completion-time substitution. |
| General exchange-based reduction | Schoot Uiterkamp–Gerards–Hurink, complete relevant definitions, Condition 1, Theorem 1 proof and corollaries. The feasible set need not be convex, so nonconvexity is not an objection to this theorem. | An exact S1 fixed-order preparation-plus-slack set fails the actual exchange optimality hypothesis, even for the shared quadratic objective family. This rules out that direct application, not the theorem or all reformulations. |
| Common exponential timing coordinates | A proved transformation `z_k=exp(lambda*t_k)`, `lambda>=max gamma_i`, makes every fixed-order timing domain convex. | Positive reduction retained. The objective is not generally convex or concave in those coordinates, and the domain need not be polyhedral. |
| Generic concave minimization at an extreme point | An exact convex-clock extreme point has two interior preparations, even on a face with concave objective. | Extremality alone does not imply the preparation pattern. The exhibited point is not an optimum. |
| Nonincreasing-rate fixed orders | A stage-dependent power recursion makes the terminal deadline function concave in preparation. A box-section vertex argument gives some concentrated optimum. | This restricted existence statement is standard allocation geometry. It does not establish every-minimizer concentration for arbitrary orders. |
| Common-rate specialization | The earlier exact linear-allocation reduction continues to apply, with support charges constant on a fixed support. | No new general allocation principle is claimed for common rates, caps, or support charges. |

The full source records and mathematical details are in the
[deterioration comparison](2026-09-23-pass20-deterioration-prior-art.md),
[nested/exchange comparison](2026-09-23-pass20-nested-allocation.md), and
[geometry audit](2026-09-23-pass20-geometry.md). They distinguish inspected
proofs from metadata-only or inaccessible leads. Third-party full texts have
not been added to the repository.

The lead workspace additionally inspected the published version of
Schoot Uiterkamp–Gerards–Hurink, *On a reduction for a class of resource
allocation problems*, INFORMS Journal on Computing **34**(3), 1387–1402
(2022), [DOI 10.1287/ijoc.2021.1104](https://doi.org/10.1287/ijoc.2021.1104),
using the [publisher PDF](https://pubsonline.informs.org/doi/pdf/10.1287/ijoc.2021.1104)
and [institutional published copy](https://research.utwente.nl/files/283900769/ijoc.2021.1104.pdf).
The exchangeable-pair definition, Condition 1, complete Theorem 1 proof and
Corollaries 1–3 agree with the scope used in the preprint comparison. In
particular, exchangeability uses some positive amount, not only a local
tangent direction. The exact counterexample excludes all admissible amounts
in the problematic direction. This is a bounded inspection of the relevant
result, not an audit of the whole published paper.

## What remains mathematically distinctive in this comparison

With two interior preparations separated by fixed prepared stages, preserve
the second selected completion time and vary the first. The objective along
the resulting feasible curve has the form

$$c(t)=-A e^{\alpha t}+B e^{\beta G(t)},\qquad
B>A>0,\quad G'>0,\quad G''\le0,\quad G(0)\ge0,\quad t\ge0.$$

Concavity gives `G(t)>=t*G'(t)`. At any stationary point this forces
`beta*G'(t)<alpha`, and the second derivative of c is strictly negative.
Every proposed minimum with two interior preparations is therefore excluded.
The proof uses a curved compensation path, not an equal-amount transfer,
and obtains a strict every-minimizer conclusion, not just existence of an
extreme optimum. These are the features a successful attribution must match.

This is still an elementary local argument. Finding that familiar allocation
models do not directly fit is not evidence that the argument is new, important,
or operationally validated. The ideal command-gated standby contract and
independent-resource counterpolicies from pass 17 remain part of the assessment.

## Review, follow-on, and research priority

The [independent internal review](2026-09-23-pass20-review.md) checked the
strengthened proof, convexification, exact certificates, restricted reduction
and source-hypothesis failure. No correction was required. This is internal
review, not outside certification. Exact arithmetic checks support the finite
fixtures; all continuum claims rest on the written proofs.

The coefficient comparison `B>A` raises a useful next boundary: does the
concentration survive independent objective prices? That question was taken
up immediately in [pass 21](2026-09-23-pass21-price-boundary.md). It gives a
sufficient open price region preserving every-minimizer concentration and an
exact positive-tolerance, physically maintainable two-partial optimum outside
that region. The sufficient region is not claimed sharp, and no extra active
physical-budget inequality is silently added to its theorem.

After that boundary is recorded, the decisive attribution target is the
one-dimensional curved-exchange argument itself. More inverse-power examples,
parameter classifications or a general numerical solver would not answer
that question. The next bounded pass checks primary generalized-concavity or
nonlinear-allocation results for this exact scope. Manuscript work remains last.

**Follow-on completed in this session:**
[pass 22](2026-09-23-pass22-curved-exchange-attribution.md) finds a positive
reduction of that scalar mechanism to standard log-concavity composition,
with an elementary strictness check. Consequently the residual should not
be advertised as a new one-dimensional optimization lemma. The model-specific
S1 concentration result remains valid; its significance and priority remain
unsettled. The next work order turns to the existing critical-viability
separation as another candidate for a bounded structural comparison.
