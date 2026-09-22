# Pass 20 opening: exact completion-time variables

22 September 2026. This is the algebraic start of the next prior-art test,
not a completed literature comparison or an additional paper claim. The
remaining work is specified by work_orders/CURRENT.md.

Fix a strictly accessible order, indexed by k=1,...,n. Write b_k for its
capacity, gamma_k for the current module's coefficient,
d_k=gamma_k*M_k, D_k=b_k-d_k>0, and 0<=U_k<=M_k for its preparation cap.
The pass-19 objective permits a nonnegative support charge h_k, which is zero
for the limiting problem and gamma_k*epsilon for positive nominal tolerance.

## Exact bijection

For the full-capacity serial order, let t_0=0 and t_k be the global completion
time of stage k. Solving its recurrence gives

$$q_k=\frac{b_k e^{\gamma_k t_{k-1}}-D_k e^{\gamma_k t_k}}{\gamma_k}.$$

Define the same stage map

$$\phi_k(t;q)=\frac1{\gamma_k}\log\frac{b_k e^{\gamma_k t}-\gamma_kq}{D_k}.$$

The cap constraints and deadline are equivalent to

$$\phi_k(t_{k-1};U_k)\leq t_k\leq\phi_k(t_{k-1};0),
\quad k=1,\ldots,n,\qquad t_n\leq H.$$

The lower bound is at least t_{k-1}, so nonnegative chronological stage
times are automatic. Conversely, any such time vector gives q in the capped
box by the displayed inversion, and substituting q recovers precisely that
full-capacity schedule. Thus this is a bijection for the fixed order, including
zero caps and possible zero-duration stages at full physical endpoints.
The upper bound is affine:
phi_k(t;0)=t+log(b_k/D_k)/gamma_k. The lower bound is increasing and concave.
An epigraph of a concave lower bound need not be convex, so this rewriting
does not itself establish a convex allocation reduction.

## Linked objective

The continuous part of upkeep telescopes by adjacent completion times:

$$\sum_k\gamma_kq_k
=b_1+\sum_{k=1}^{n-1}
 \left[b_{k+1}e^{\gamma_{k+1}t_k}-D_ke^{\gamma_kt_k}\right]
 -D_ne^{\gamma_nt_n}.$$

Add the support terms sum_k h_k*1[q_k>0], with q obtained by the inversion.
Positive support is equivalent to a strict upper timing inequality, while
q_k=0 is equivalent to t_k=phi_k(t_{k-1};0). The objective is separable in
completion times only before these support indicators and the linked timing
constraints are taken into account. Arbitrary independent preparation prices
would change the coefficients of the adjacent terms; the linked gamma prices
are not cosmetic.

## What this does and does not settle

This supplies a precise target for comparison with separable optimization
under nested nonlinear constraints. It is a coupled change of variables,
which the pass-17 scalar-clock non-reduction did not exclude. No inspected
source is claimed to answer this formulation yet. Do not infer an extreme-
point theorem from separability, a polynomial algorithm from the chain shape,
or a convex model from the concavity of each stage map.

Continue with the bounded primary-source search and exact theorem/quantifier
comparison in CURRENT.md. Keep any resulting prior-art reduction as a finding.
The core paper and the pass-19 assessment remain unchanged by this algebraic
preparation for the comparison.
