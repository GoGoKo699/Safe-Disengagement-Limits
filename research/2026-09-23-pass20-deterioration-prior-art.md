# Pass 20: deteriorating jobs and the completion-time comparison

23 September 2026. Base: `b1bbd00f986efa5b935302fb175737174a7f89af`.
This is a bounded primary-source audit of the full
[pass-19 capped concentration theorem](2026-09-22-pass19-tolerance-concentration.md)
using the exact
[completion-time formulation](2026-09-22-pass20-completion-time-formulation.md).
The full pass-11, pass-15, and pass-17 comparisons were also read. Manuscript
work is paused under the user's current instruction.

## Finding

An additional accessible deterioration-and-investment theorem reduces to
convex inverse-power allocation. It does not establish the strengthened
S1 concentration theorem by either a direct investment identification or
the proposed completion-time change of variables. The latter comparison
can be made exact: the inspected model has affine timing constraints,
whereas the S1 feasible set in completion times can already be nonconvex
with two stages. This is a failure of specified reductions, not a priority
certificate or a claim against every nonlinear encoding.

The old reductions remain in force. Common-rate fixed-order allocation is
ordinary linear allocation; adding caps or locally constant support charges
does not create a new exchange principle. The residual unequal-rate claim
is the absence of an interior minimum along each admissible two-coordinate
exchange, including a fixed prepared block between the varying coordinates.

## 1. Primary source inspected in full for the relevant result

C. Liu and C. Xiong, *Single machine resource allocation scheduling problems
with deterioration effect and general positional effect*, Mathematical
Biosciences and Engineering **18**(3), 2562–2578 (2021),
DOI [10.3934/mbe.2021130](https://doi.org/10.3934/mbe.2021130).
[Publisher article](https://www.aimspress.com/article/doi/10.3934/mbe.2021130),
[complete publisher PDF](https://www.aimspress.com/aimspress-data/mbe/2021/3/PDF/mbe-18-03-130.pdf).

**Inspection:** complete Sections 2–3, including equation (3), Lemmas 1–2
and their complete proofs, and Theorems 1–2 with their proofs; printed
pages 2564–2571. Section 1 was read for context. The later due-window
applications were not audited. The published PDF, not an abstract, supplied
the mathematics.

The model assumes nonpreemptive jobs with duration

$$p_j=\bigl((w_j/u_j)^k+bS_j\bigr)g(r),$$

positive investment, common positive `b,k`, and a positional factor `g`.
Its fixed-order reduction is a positive weighted sum of inverse powers of
investment. Lemma 2 minimizes linear investment cost under an upper bound
on that sum, giving an interior allocation formula. The inspected result
has no individual caps or activation charges. Theorem 2 transfers suitable
sequencing problems to a positional-cost formulation.

## 2. Our exact comparison in completion-time variables

The following calculations are deductions for this audit. They are not
claims made in the source about S1. Choose the makespan criterion and fix
an order. Use `c_r` for investment price, `g_r>0` for its positional factor,
and `t_0=0`. The source recurrence becomes

$$t_r=(1+bg_r)t_{r-1}+g_r(w_r/u_r)^k.$$

Define

$$\delta_r=t_r-(1+bg_r)t_{r-1}>0.
\qquad
u_r=w_r(g_r/\delta_r)^{1/k}.$$

This is a bijection for the prescribed no-idle order. Its fixed-deadline
problem is therefore

$$\min_t\sum_r c_rw_r(g_r/\delta_r)^{1/k},
\qquad \delta_r>0,\quad t_n\leq R.$$

Each `delta_r` is affine in the completion vector. The function
`delta^(-1/k)` is strictly convex on positive delta. Hence this is a convex
objective on a convex timing domain. Adding finite positive investment
bounds would merely add constant lower and upper bounds on delta; that
extension would retain convexity. This observation does not attribute a
bounded-investment theorem to the source.

Now fix a strictly accessible S1 order. Its exact inverse variables are

$$q_r=\frac{b_re^{\gamma_rt_{r-1}}-D_re^{\gamma_rt_r}}{\gamma_r},
\qquad D_r=b_r-\gamma_rM_r>0,$$

with linked constraints

$$\phi_r(t_{r-1};U_r)\leq t_r\leq\phi_r(t_{r-1};0),
\qquad
\phi_r(t;q)=\frac1{\gamma_r}
\log\frac{b_re^{\gamma_rt}-\gamma_rq}{D_r}.$$

The continuous cost is the difference-of-exponentials expression in the
opening note. In particular, it is not the positive sum of inverse powers
of affine time increments just displayed. More decisively, its timing
domain need not be convex.

**Two-stage timing-domain certificate.** Take any strictly accessible
two-stage S1 order with `0<U_i<=M_i` for both stages. The interval

$$I=[\phi_1(0;U_1),\phi_1(0;0)]$$

has positive length. Choose distinct `a,b` in this interval, and form

$$P=(a,\phi_2(a;U_2)),\qquad
Q=(b,\phi_2(b;U_2)).$$

Choose the finite deadline
`H=max(phi_2(a;U_2),phi_2(b;U_2))`. Both points satisfy every cap, timing,
and deadline constraint. But for `U_2>0`,

$$\phi_2''(t;U_2)
=-\gamma_2\phi_2'(t;U_2)(\phi_2'(t;U_2)-1)<0.$$

Their midpoint has second coordinate strictly less than
`phi_2((a+b)/2;U_2)`, violating its lower timing constraint. Thus the S1
completion-time feasible set is nonconvex. This conclusion holds even with
common decay rates; the familiar common-rate LP uses another transformation.

Consequently no invertible affine identification of these two timing domains
exists in general, nor can an affine lift followed by affine projection of
a convex domain produce this exact S1 set. A more general nonlinear lift
is not ruled out. The certificate is for the fixed order and selected
deadline; it is not a statement that every instance or every global union
over orders is nonconvex.

## 3. Objective, bounds, support, and quantifiers

For a genuine reduction of pass 19, a proposed allocation theorem must
preserve all of the following S1 features:

| Item | Required mapping |
|---|---|
| Objective | `sum gamma_i*q_i + sum h_i*1[q_i>0]`, with the same decay-linked linear prices |
| Bounds | `0<=q_i<=U_i<=M_i`, including `U_i=0` and support changes at zero |
| Deadline | The exact strict-order oracle `E(q)<=H`, rather than a weighted-sum surrogate |
| Quantifier | Every minimizer has at most one coordinate strictly between its caps |
| Order | At least one attained strict order can witness feasibility, but need not remain globally optimal nearby |
| Original controls | Seriality must first justify use of the finite-order oracle for the original causal, divisible, preemptive policy class |

The policy-class issue must not be overstated. Once S1's serial reduction
has been proved, an allocation theorem need only solve the resulting
deterministic problem. It need not independently discuss adversarial loss
histories. Conversely, a deterministic scheduling theorem alone does not
prove that reduction.

A theorem producing some extreme optimum is insufficient to establish the
every-minimizer statement without an additional strictness argument. An
objective scalarization also needs justification: minimizing a weighted sum
of time and investment does not automatically recover each fixed-deadline
optimum in a nonconvex problem.

The activation charges in pass 19 are constant on the open exchange
neighborhood, so they play no role in the derivative calculation. Their
nonnegativity supplies lower semicontinuity at zero and hence existence on
the compact feasible box. Caps guarantee that the selected partial pair
admits a two-sided variation. These extensions are useful for the exact
finite-tolerance application; they should not be counted as separate
discoveries in allocation theory.

The strengthened proof's actual work is instead the inequality
`G(t)>=t*G'(t)` for the intervening concave time map and the conclusion that
every stationary exchange point has strictly negative second derivative.
The source above contains no result identified here that substitutes for
that argument. This does not establish that the argument has no earlier
antecedent elsewhere.

## 4. Additional bounded leads and access limits

An author-hosted manuscript by R. Rudek and A. Rudek,
[*A critical note on “On a single machine-scheduling problem with separated
position and resource effects”*](https://radoslawrudek.pl/doc/Rudek_Critical_Note_Resource.pdf),
was read completely (three pages). It displays a linear compression
allocation rule with caps: allocate available resource by decreasing
effectiveness until exhausted. Its Property 1 and Algorithm 1 describe
ordinary bounded linear greedy allocation. This is relevant precedent for
endpoint allocation, but supplies no identified unequal-exponential
exchange theorem. The original 2011 article's complete proof was not
retrieved; this reply is not a substitute for auditing that proof or a basis
for adjudicating the associated authors' dispute.

The publisher endpoint for the original Rudek–Rudek article,
DOI [10.1016/j.camwa.2011.06.030](https://doi.org/10.1016/j.camwa.2011.06.030),
returned an access failure. Oron's
[*Scheduling controllable processing time jobs in a deteriorating
environment*](https://doi.org/10.1057/jors.2013.5) was available only at
abstract/metadata level in this pass; its complete allocation proof remains
uninspected. A correction exists,
DOI [10.1057/jors.2015.96](https://doi.org/10.1057/jors.2015.96), but its
publisher endpoint also failed. No conclusion about the correction's
mathematical effect is drawn. The Lawler–Moore functional-equation lead,
DOI [10.1287/mnsc.16.1.77](https://doi.org/10.1287/mnsc.16.1.77), was screened
at publisher abstract level only and is not used as theorem evidence.

The older Glazebrook endpoints were not retried. No payment or outside
contact occurred, and no third-party full text was added to this repository.

## 5. Decision supported by this audit

Retain pass 19 as a mathematically specific candidate result, with novelty
unresolved. The new source adds a genuine fixed-deadline comparison but
lands in the previously identified convex inverse-power family; collecting
further variants of that same family has diminishing value. The remaining
high-value comparison is a general allocation theorem that allows the exact
nonlinear chain constraints, or a documented transformation preserving both
the linked objective and all endpoint/every-minimizer conclusions. Until
such a source or reduction is supplied, neither a novelty clearance nor a
prior-art collapse is justified.
