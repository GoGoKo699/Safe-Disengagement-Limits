# Pass 21: stability and failure under independent preparation prices

23 September 2026. Repository research only; manuscript writing remains
deferred. This pass examines a boundary of the strengthened concentration
theorem. Positive proportional loss coefficients still govern the physical
dynamics, but positive objective prices need not equal those coefficients.

Concentration survives an explicit open region of prices around the linked
case. It does not survive arbitrary independent prices: an exact two-module
instance with positive request-time tolerance has a unique nominal optimum
with two partial coordinates, and that nominal state is physically
maintainable below the source budget. The price region below is sufficient,
not claimed sharp or necessary. No new operational implementation is asserted.

## 1. Model and the role of the changed objective

Use the pass-19 strict-order model with

$$M_i>0,\quad \gamma_i>0,\quad a_i\ge0,\quad s\ge0,
\qquad d_i=\gamma_iM_i,\qquad b(S)=s+\sum_{i\in S}a_i.$$

Let E be the minimum completion time over orders whose every stage satisfies
`b(prefix)>d_i`. Assume a nonempty finite-deadline feasible set in the capped
box `0<=q_i<=U_i<=M_i`. Replace the linked objective by

$$J_w(q)=\sum_i w_iq_i+\sum_{i:q_i>0}h_i,
\qquad w_i>0,\quad h_i\ge0. \tag{1}$$

The actual loss coefficients remain `gamma_i`. In particular, the source
rate needed to maintain a nominal state p is still `sum_i gamma_i*p_i`.
An economic or other independent price objective does not replace that
physical rate by `sum_i w_i*p_i`.

The optimization in (1) has no additional active physical-upkeep inequality;
it is the same capped deadline problem with a changed objective. The
counterexample below separately checks physical maintainability at its
optimum. Compactness and lower semicontinuity give existence whenever this
deadline problem is feasible.

## 2. A sufficient price region preserving every-minimizer concentration

Put `r_i=w_i/gamma_i`. In any fixed strictly accessible order, select two
interior coordinates j before k, and keep all other preparations fixed.
Use pass 19's variation t of the completion time of j while retaining the
completion time of k. Write `alpha=gamma_j`, `beta=gamma_k`,
`D_j=b_j-d_j`, and let G be the composed intermediate-stage map. It satisfies

$$G'(t)>0,\qquad G''(t)\le0,\qquad G(0)\ge0,
\qquad G(t)\ge tG'(t).$$

Up to an additive constant, the price along this feasible variation is

$$c_w(t)=-A e^{\alpha t}+B' e^{\beta G(t)},
\qquad A=r_jD_j>0,\qquad B'=r_kb_k>0. \tag{2}$$

The support charges remain fixed locally. If

$$r_kb_k>r_jD_j, \tag{3}$$

then at a stationary point

$$\alpha A e^{\alpha t}
=\beta B'G'(t)e^{\beta G(t)}.$$

Were `beta*G'(t)>=alpha`, the tangent inequality and `t>=0` would give
`beta*G(t)>=alpha*t`, so the right side would be at least
`alpha*B'*exp(alpha*t)>alpha*A*exp(alpha*t)`, a contradiction. Consequently

$$c_w''(t)=\alpha A e^{\alpha t}
\left[\beta G'(t)+\frac{G''(t)}{G'(t)}-\alpha\right]<0. \tag{4}$$

Exactly the pass-19 local argument excludes an interior minimum.

**Proposition 1.** If (3) holds for every ordered pair of distinct stages in
every strictly accessible order, then every minimizer of (1) has at most
one coordinate strictly between zero and its positive cap. The same is
true for one fixed order if (3) is required only within that order.

For the global statement choose an order attaining E at a proposed minimum.
A same-order feasible variation already contradicts global minimality; no
differentiation of the minimum over orders is used. Requiring every pair is
convenient and sufficient. A particular instance could satisfy a weaker
condition on the pairs that can actually be interior at a minimum.

There is a simple order-independent sufficient bound. Define

$$B=s+\sum_i a_i,\qquad d_{\min}=\min_i d_i>0,
\qquad r_{\min}=\min_i r_i,\quad r_{\max}=\max_i r_i.$$

Feasibility implies a strict order exists, hence `B>d_min`. Nonnegative
releases give `b_j<=b_k<=B`, and therefore

$$\frac{D_j}{b_k}
=\frac{b_j-d_j}{b_k}
\le1-\frac{d_j}{b_k}
\le1-\frac{d_{\min}}B.$$

It follows that (3) holds whenever

$$\boxed{\frac{r_{\max}}{r_{\min}}<\frac{B}{B-d_{\min}}.} \tag{5}$$

In particular, the explicitly open neighborhood

$$\left|\frac{w_i}{\gamma_i}-1\right|\le\delta
\quad\text{for all }i,
\qquad 0\le\delta<\frac{d_{\min}}{2B-d_{\min}} \tag{6}$$

satisfies (5), since `(1+delta)/(1-delta)<B/(B-d_min)`.
Thus exact equality of price and loss coefficients is not required for
the concentration proof. The bound can be conservative; neither failure
of (5) nor equality at its boundary is a counterexample by itself.

For uniform positive nominal tolerance epsilon, replace caps by
`U_i=(M_i-epsilon)_+` and support charges by `h_i=w_i*epsilon`.
As in pass 19, every optimizer is represented by `p_i=0` if `q_i=0` and
`p_i=q_i+epsilon` otherwise. Prices are strictly positive, so nominal
amounts between zero and epsilon with no surviving preparation are dominated
by zero. Proposition 1 then gives concentration of every nominal optimum
under the same price condition.

## 3. An exact counterexample outside the sufficient region

Take two modules with

$$s=2,\quad M=(1,1),\quad \gamma=(1,2),\quad a=(2,0),
\qquad H=\log2,\qquad \epsilon=\frac1{100},\qquad w=(6,1). \tag{7}$$

For nominal state p, the worst request-time preparation is
`q=(p-epsilon)_+`. Every such q is strictly below its physical threshold.
The only strictly accessible order is 1 then 2: initially module 2 has
`d_2=s=2`, which blocks its first completion from a subfull state; module 1
has `d_1=1<s`, and releasing its capacity makes the second stage capacity 4.
The existing all-policy seriality result therefore makes this one-order
oracle the true deadline oracle for these request states.

The two stage equations are

$$e^{t_1}=2-q_1,\qquad
e^{2t_2}=2(2-q_1)^2-q_2.$$

Consequently the deadline is exactly

$$q_2\ge 2(2-q_1)^2-4,
\qquad 0\le q_1,q_2\le\frac{99}{100}. \tag{8}$$

At any optimum there is no nominal coordinate in `(0,epsilon]`: replacing
it by zero leaves q unchanged and strictly lowers its price. For each
positive q coordinate, the corresponding nominal amount is `q_i+epsilon`.
Thus the following support cases exhaust all possible minima.

If both q coordinates are positive, (8) gives

$$\begin{aligned}
w\cdot p
&=6q_1+q_2+\frac7{100}\\
&\ge 6q_1+2(2-q_1)^2-4+\frac7{100}\\
&=\frac{357}{100}+2\left(q_1-\frac12\right)^2. \tag{9}
\end{aligned}$$

Equality is attained uniquely at

$$q^*=\left(\frac12,\frac12\right),\qquad
p^*=\left(\frac{51}{100},\frac{51}{100}\right),\qquad
w\cdot p^*=\frac{357}{100}. \tag{10}$$

These preparations lie within the caps and meet the deadline exactly.

If `q_1=0`, (8) demands `q_2>=4`, so this support is infeasible. If
`q_2=0`, feasibility requires `q_1>=2-sqrt(2)` and the least nominal price
on that branch is

$$6\left(2-\sqrt2+\frac1{100}\right)
=\frac{603}{50}-6\sqrt2
>\frac{357}{100}. \tag{11}$$

For a rational certificate of the strict inequality, `sqrt(2)<283/200`
because `2<80089/40000`; substituting this bound into (11) gives exactly
`357/100` as a strict lower bound. The branch is feasible since
`0<2-sqrt(2)<99/100`, but it cannot minimize.

Equations (9)–(11) prove that p* is the unique optimum over all nominal
states, not merely a local stationary point or a comparison with selected
concentrated candidates. Both nominal coordinates are strictly partial.
The physical upkeep is nevertheless

$$\gamma\cdot p^*=\frac{153}{100}<s=2. \tag{12}$$

Thus the failure does not rely on an unmaintainable nominal state. Starting
from paid initialization at p*, assigning `v_i=gamma_i*p_i*` maintains it
with worst proportional loss and leaves optional source rate `47/100`.

This example has normalized prices `r=(6,1/2)`. The global sufficient bound
has `B=4`, `d_min=1`, and requires a ratio below `4/3`; the example's ratio
is 12. Failure well outside the sufficient region does not determine the
largest possible preserving region or settle its boundary.

## 4. Research consequence

The original linked-price theorem has two distinct safeguards. Its
concentration is stable under a quantitative range of price perturbations;
it is not a universal law for every positively weighted allocation objective.
The exact example above preserves the same S1 dynamics, all-policy deadline
oracle and positive shortfall convention while changing only the objective.
It therefore locates a mathematical assumption that a broader prior-art
reduction or application must retain or replace with an explicit condition.

The results here are proof-based internal deductions. Small exact checks
can verify the displayed recurrence and rational arithmetic, but do not
replace the continuum proof or establish novelty. Determining a sharp price
region, adding an independent active physical-budget constraint, or changing
the loss law would be separate questions; none is implicitly resolved here.
