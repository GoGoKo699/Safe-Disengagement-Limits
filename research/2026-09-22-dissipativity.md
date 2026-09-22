# The recurring-cost proof is a dissipativity argument

22 September 2026. Follow-on prior-art audit after the heterogeneous reduction.

**Decision:** do not claim the bounded-potential averaging principle, or optimal
stationary operation by itself, as a new contribution. The readiness geometry
and evaluation of the resulting resource frontier must carry any residual claim.

## Source actually inspected

T. Faulwasser, M. Korda, C. N. Jones and D. Bonvin,
*On turnpike and dissipativity properties of continuous-time optimal control
problems*, Automatica 81 (2017), 297–304,
[DOI](https://doi.org/10.1016/j.automatica.2017.03.012),
[arXiv full text, v2](https://arxiv.org/pdf/1509.07315v2).

Inspected full sections 1.1 and 1.3, Definition 1, equations (7), (11), (12a),
and section 2, Theorems 3–4 and their proof (PDF pages 2–5, using printed page
numbers). The paper defines optimal steady operation through an all-trajectory
asymptotic average comparison. A bounded storage inequality implies that
comparison by division by the horizon. Theorem 4 does not require strict
dissipativity. Its general setup assumes a Lipschitz vector field on compact
state/input sets. Those regularity assumptions do not automatically cover our
reflected, discontinuous boundary dynamics. We therefore identify the actual
storage inequality and reproduce its elementary consequence below, rather than
claim a verbatim application of every hypothesis of Theorem 4. Other sections,
numerical results and converse turnpike claims are not needed here.

## Exact identification in S1

On the allowed maximum-loss history, define the state constraint as the
deadline-ready set `R_H`. Let `c*=D(H)` in the heterogeneous fixed-rate model.
The support lemma and resource balance yield

```
Q(T)-Q(0) <= integral_0^T [(s-u(t))-c*] dt,
Q(p)=sum_i p_i,  0<=Q<=sum_i M_i.
```

This has precisely the integral dissipativity form with storage `Q`, stage cost
`ell=s-u` (all capacity unavailable to optional work, including waste), and
steady cost `ell*=c*`. The attaining ready subset supplies a feasible equilibrium
with this cost whenever `c*<=s`. Dividing by `T` gives

```
liminf average(s-u) >= c*,
limsup average(u) <= s-c*.
```

The bounded-storage proof is already established mathematics. The adaptation
needed here is to verify the statewise support inequality and to compute which
subsets meet the exit deadline. The uncertainty quantifier is dealt with by
selecting one permitted worst-case history for the lower bound and constructing
a policy valid for all histories; no stochastic turnpike assertion follows.

This identifies a proof-method reduction, not an assertion that the cited paper
contains the formula for `F(S)` or `D(H)`. Conversely, the absence of those
symbols in that paper is not a positive novelty argument for S1.

## Why simply smoothing the erosion law is insufficient novelty

Suppose a related model has nonnegative statewise total loss `L(p)` and
`Q'<=s-u-L(p)` along an allowed worst-case history. If

```
c_H = inf_{p in R_H} L(p),
```

then the same integration gives the average bound `s-c_H`. If this infimum is
attained at a robustly maintainable constant state, with maintenance allocation
of total cost `c_H<=s`, that state attains the bound. These are explicit
conditions; neither attainment nor maintainability is automatic for an
arbitrary loss law or coupled control interface.

Thus a state-dependent-loss extension could improve operational fidelity, but
the generic averaging argument would remain a standard storage certificate.
The scientific question would be the exit-ready region and the optimizer,
or a justified mechanism that prevents static attainment. The archived
one-module proportional-loss countermodel is consistent with this observation.

## Consequence for the research program

The recurring formula is useful for interpretation and computation, but not
sufficient evidence for a standalone paper. The [scheduling comparison](2026-09-22-literature-audit.md)
also reduces the equal-release/equal-loss exit theorem to earlier scheduling.
The fully heterogeneous potential, the failure of simple ordering rules, and
the startup distinction should be audited together. These are current research
results, not a declaration of a novel general control principle.
