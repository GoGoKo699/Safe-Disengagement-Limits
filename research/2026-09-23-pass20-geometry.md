# Pass 20: exact geometry of the allocation comparison

23 September 2026. This is a mathematical audit of the strengthened
pass-19 exchange, using the exact completion-time formulation from the
pass-20 opening. It does not make claims about uninspected literature.
The source comparisons are recorded separately. Manuscript work is paused.

## 1. Findings and the scope of the reductions

There are useful positive reductions, and they should be kept visible:

1. A common exponential clock with a sufficiently large exponent makes
   every fixed-order timing domain **convex**.
2. In the common-coefficient case, the preparation problem reduces to a
   linear allocation problem, as already recorded in pass 19.
3. For a fixed order of nonincreasing coefficients, the deadline can be
   written as a single concave function bounded above. A usual vertex
   argument then proves the **existence** of a concentrated optimum.

None of these observations alone recovers pass 19's statement that **every**
minimizer concentrates, for arbitrary unequal coefficient orders and fixed
nonnegative support charges. In particular, an explicit convex-clock feasible
extreme point below has two interior preparation coordinates, even in a case
where the transformed objective is concave. Thus a generic statement that
concave minimization attains its minimum at an extreme point is too weak to
identify the preparation pattern. This is a failure of that proof shortcut,
not a proof that no prior theorem or more elaborate reduction applies.

Throughout, fix one strictly accessible order and write

\[
b_k> d_k=\gamma_k M_k>0,\qquad D_k=b_k-d_k>0,
\quad 0\leq U_k\leq M_k.
\]

The capacities are nondecreasing along the order because releases are
nonnegative. The stage map and its inverse are

\[
\phi_k(t;q)=\frac1{\gamma_k}
\log\frac{b_ke^{\gamma_kt}-\gamma_kq}{D_k},
\qquad
\gamma_kq_k=b_ke^{\gamma_kt_{k-1}}-D_ke^{\gamma_kt_k}.
\]

All statements concern this fixed-order formulation unless a larger scope is
explicitly stated. No assertion of a universally optimal sorted order is used.

## 2. Raw completion times can be nonconvex, including common rates

Take two modules with common coefficient one, zero releases, source capacity
two, physical sizes one, and caps one half. Choose deadline
`H = log(7/2)`. The timing constraints are

\[
\log(3/2)\leq t_1\leq\log 2,
\qquad
\log(2e^{t_1}-1/2)\leq t_2\leq t_1+\log 2,
\qquad t_2\leq H.
\]

Both time vectors

\[
A=(\log(3/2),\log(5/2)),\qquad
B=(\log 2,\log(7/2))
\]

are feasible: their preparations are respectively `(1/2,1/2)` and
`(0,1/2)`. Their arithmetic midpoint would require

\[
\frac{\sqrt{35}}2\geq 2\sqrt3-\frac12,
\]

which is false. The difference of the squared right and left sides is
`7/2 - 2 sqrt(3) > 0`. Thus the timing set is nonconvex. The example also
has the exact cap shape produced by positive tolerance `epsilon = 1/2`.

However, replacing each time by `z_k = exp(t_k)` makes these very constraints
linear. Raw-time nonconvexity therefore cannot exclude a coupled
allocation reduction. It is only a statement about the displayed coordinates.

## 3. Every order has a convex timing formulation

Choose any `lambda >= max_k gamma_k`, and put

\[
z_k=e^{\lambda t_k},\quad z_0=1,\quad
r_k=\gamma_k/\lambda\in(0,1].
\]

The cap constraints become

\[
L_k(z_{k-1})\leq z_k\leq
\left(\frac{b_k}{D_k}\right)^{1/r_k}z_{k-1},
\qquad
L_k(z)=\left(\frac{b_kz^{r_k}-\gamma_kU_k}{D_k}\right)^{1/r_k},
\tag{1}
\]

and the deadline is `z_n <= exp(lambda H)`. All coordinates are at least
one. For `A=b_k/D_k`, `B=gamma_k U_k/D_k`, and `r=r_k`, differentiation gives

\[
L_k''(z)=A B(1-r)z^{r-2}(Az^r-B)^{1/r-2}\geq0. \tag{2}
\]

The expression is defined on the relevant domain because
`b_k z^r - gamma_k U_k >= D_k > 0`. Thus every lower constraint is the
epigraph of a convex function, every upper constraint is affine, and their
intersection with the deadline halfspace is convex. Equation (1), together
with the inverse preparation formula, is an exact bijection; it does not
relax feasibility or change the fixed order.

When `U_k>0` and `gamma_k<lambda`, (2) is strictly positive. The convex set
can consequently have curved boundary pieces and need not be a polyhedron.
When all coefficients equal `lambda`, all constraints become affine. With
unequal coefficients, convexity by itself supplies neither a polyhedral
allocation model nor an endpoint count for preparation variables.

The linked continuous objective in these coordinates is

\[
b_1+\sum_{k=1}^{n-1}
 \left[b_{k+1}z_k^{r_{k+1}}-D_kz_k^{r_k}\right]
 -D_nz_n^{r_n}.                                      \tag{3}
\]

The support charge is still `h_k` when the upper constraint in (1) is strict,
and zero when it is an equality. Such charges cannot be discarded when
applying a smooth separable-objective theorem.

Nor is (3) automatically concave after fixing the terminal time. For a
specific certificate, take zero releases, all capacities 25,

\[
\gamma=(2,1,1),\quad M=(9/2,1,1),\quad
D=(16,24,24),\quad U=(4,3/4,3/4),\quad \lambda=4.
\]

Fix `exp(H) = 1451/1152` and consider preparations
`q=(49/50,1/2,1/2)`, all strictly inside their caps. Their times satisfy

\[
e^{t_1}=6/5,\quad e^{t_2}=59/48,\quad e^{t_3}=1451/1152.
\]

On the fixed-terminal-time face, (3), up to a constant, is

\[
f(z_1,z_2)=25z_1^{1/4}-16z_1^{1/2}+z_2^{1/4}.
\]

At the displayed interior point its two diagonal Hessian entries have signs

\[
f_{11}=z_1^{-7/4}(-75/16+4z_1^{1/4})
       =\frac9{80}z_1^{-7/4}>0,
\qquad
f_{22}=-\frac3{16}z_2^{-7/4}<0.
\]

The fixed-horizon feasible set contains a relative open neighborhood there,
because all three preparations are strictly inside their caps. Hence the
objective is neither convex nor concave on that set. This certificate
concerns the specified valid clock `lambda=4`; it does not rule out a more
favorable clock for this instance.

## 4. A convex-clock extreme point with two interior preparations

The stronger obstruction to an immediate extreme-point argument uses the
exact pass-19 exchange fixture. Let

\[
s=10,\quad a_i=0,\quad \gamma=(2,1,1),\quad M=(3,2,2),
\quad U=(29/10,19/10,19/10),\quad e^H=533/256.
\]

Use order `1,2,3` and the convex clock `lambda=2`. Consider

\[
z_1=(25/16)^2,\qquad
z_2=(549/320)^2,\qquad
z_3=(533/256)^2.
\tag{4}
\]

Inverting the stage equations gives

\[
q_1=15/128,\qquad q_2=19/10=U_2,\qquad q_3=1/2.
\]

Thus the first and third preparations lie strictly inside their positive
caps. The middle lower timing constraint is active:

\[
z_2=L_2(z_1),\qquad
L_2(z)=\left(\frac{10\sqrt z-19/10}{8}\right)^2.
\tag{5}
\]

This function is strictly convex on the relevant positive interval by (2).
The point (4) is an extreme point of the **full** convex timing domain.
Indeed, any convex combination of two feasible points that equals (4)
must have the same terminal coordinate in both points: the deadline is
active and both terminal coordinates are at most that value. Equality in
the active lower constraint (5), together with strict convexity, then
forces the first coordinates to be equal. The two second coordinates are
each at least `L_2(z_1)` and average to that value, so they too are equal.

The continuous objective on this fixed-horizon face, up to a constant, is

\[
10\sqrt{z_1}-4z_1+2\sqrt{z_2},
\]

which is strictly concave. Nevertheless the extreme point just exhibited
has two interior preparation coordinates. It is **not** a minimizing state:
the exact exchange in pass 19 proves it is a strict local maximum along the
middle-cap curve. That distinction is the point of the certificate.
An extreme-point existence theorem for concave minimization does not say
which extreme points can minimize, and does not provide the desired endpoint
count in these coordinates. The linked exchange inequality supplies the
additional exclusion.

There is also an open arc of the boundary (5) around (4), because the first
and third preparations are strictly interior. Consequently this particular
convex timing domain is not polyhedral. In particular, an invertible affine
change of these timing coordinates cannot make it a polytope defined only
by linear subset-sum inequalities, as in a polymatroid formulation. This
does not exclude nonlinear transformations, lifted nonlinear models, or a
different attribution theorem.

## 5. A positive reverse-convex reduction for ordered coefficients

Suppose the selected fixed order satisfies

\[
\gamma_1\geq\gamma_2\geq\cdots\geq\gamma_n>0.
\]

Use a different, stage-dependent exponential variable
`X_k = exp(gamma_k t_k)`. Direct substitution gives

\[
X_1=\frac{b_1-\gamma_1q_1}{D_1},\qquad
X_k=\frac{b_kX_{k-1}^{\gamma_k/\gamma_{k-1}}-\gamma_kq_k}{D_k}.
\tag{6}
\]

Each exponent in (6) belongs to `(0,1]`. A positive increasing concave
power composed with a positive concave function remains concave; subtracting
a linear coordinate preserves concavity. Induction proves that `X_n(q)` is
concave on the full capped preparation box. The deadline is

\[
X_n(q)\leq e^{\gamma_nH}.
\tag{7}
\]

Thus the ready set in this fixed order is a box intersected with one
reverse-convex inequality, meaning a concave function bounded above.

An elementary polytope argument now proves existence of a concentrated
optimum, including nonnegative support charges. Start with any optimum
`q*` and let `A` be its positive support. Fix all coordinates outside `A`
to zero and form the nonempty box section

\[
K=\left\{q:0\leq q_i\leq U_i\ (i\in A),\quad
  \sum_{i\in A}\gamma_iq_i=\sum_{i\in A}\gamma_iq_i^*\right\}.
\]

A concave function on a compact polytope attains its minimum at some vertex:
write any point as a convex combination of vertices and use the concavity
inequality. Choose such a vertex `v` minimizing `X_n` on `K`. Then
`X_n(v)<=X_n(q*)`, so it remains deadline-feasible. Every vertex of this
box section has at most one coordinate strictly between its bounds, since
two such coordinates admit a two-sided variation preserving its one linear
equality. Its continuous upkeep is unchanged; deleting any support can only
decrease the fixed charges. Optimality therefore makes `v` another optimum.

This is a genuine reduction of an **existence** statement for the specified
coefficient orders. It should not be presented as a new general allocation
principle. It does not prove the every-minimizer assertion: for example,
the generic concave constraint `2-q_1-q_2<=1` on the unit square, minimized
with objective `q_1+q_2`, admits every point with `q_1+q_2=1` as a minimum,
including `(1/2,1/2)`. S1 excludes this flat compensation by its linked
coefficients and stage maps. Nor does (6) cover arbitrary oscillating
coefficient orders; no claim that an optimal S1 order is always nonincreasing
has been established here.

## 6. The remaining attribution question

The correct target is consequently narrower than generic nonconvex
allocation, convexification, or extreme-point sparsity. Pass 19 uses an
exchange along a chain with a fixed second completion time. Its variable
cost has the exact form

\[
c(t)=-A e^{\alpha t}+B e^{\beta G(t)},\qquad
A>0,\ B>A,\ G'>0,\ G''\leq0,\ G(0)\geq0,\quad t\geq0.
\]

The inequality `G(t)>=t G'(t)` forces `beta G'(t)<alpha` at any stationary
point and hence forces its second derivative to be negative. The linked
upkeep and nonnegative releases produce `B>A`; support charges are constant
on the local exchange. A prior theorem containing this curved compensation
argument, with sufficient strictness to exclude **all** interior minima and
with arbitrary fixed prepared stages in the chain, would absorb the
strengthened result or supply its proper attribution.

The next decisive proof question is whether an inspected allocation theorem
has exactly that scope, perhaps after a coupled coordinate change that
preserves both the feasible exchanges and the objective. Merely showing a
convex feasible set, a separable objective, an extreme-point optimum, or an
equal-amount exchange condition is insufficient. These geometric deductions
identify the assumptions a successful comparison must actually verify;
they do not certify novelty.

The rational inversions in Sections 3–4, the sign coefficient `9/80`, and
the squared midpoint inequality in Section 2 were checked locally with
Python's exact `fractions.Fraction` arithmetic. These finite arithmetic
checks support the displayed certificates; the general convexity,
extremality, and existence conclusions rely on the written arguments above.
