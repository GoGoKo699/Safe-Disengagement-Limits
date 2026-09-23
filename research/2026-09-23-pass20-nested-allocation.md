# Pass 20: nested allocation and equal-amount exchange tests

23 September 2026. Repository research only; manuscript work is paused.
This note compares the complete
[pass-19 capped concentration theorem](2026-09-22-pass19-tolerance-concentration.md)
and [completion-time formulation](2026-09-22-pass20-completion-time-formulation.md)
with two primary allocation results. The complete pass-11 and pass-17
comparison notes were also read. All counterexamples below are deductions
made in this audit, not claims made by the cited authors about S1.

The useful finding is a precise failed reduction. A general allocation
theorem applies beyond convex feasible sets, so nonconvexity alone is an
insufficient objection. Its actual equal-amount exchange optimality
condition fails for an explicit S1 fixed-order region, including after
adding a constant-total slack coordinate. The strengthened S1 theorem is
not obtained by that direct substitution. This does not establish priority
or rule out another change of variables.

## 1. Primary sources and inspected scope

**Vidal–Gribel–Jaillet.** T. Vidal, D. Gribel, P. Jaillet,
*Separable Convex Optimization with Nested Lower and Upper Constraints*,
INFORMS Journal on Optimization **1**(1), 71–90 (2019),
[DOI 10.1287/ijoo.2018.0004](https://doi.org/10.1287/ijoo.2018.0004).
The inspected text is the August 2018
[author accepted manuscript](https://www.mit.edu/~jaillet/general/RAP-NC-ArXiv.pdf),
not an assumed identical publisher layout. Read the complete Section 1
model, equations (1)–(8), and Section 3.1 through Theorem 2 and its complete
proof, including Algorithm 1. In this manuscript the model is on pages 2–3
and Theorems 1–2 on pages 13–15. Costs are convex and separable; constraints
bound affine partial sums, individual variables, and their total. Theorem 2
gives existence of an optimal solution between two ordered optimal
solutions at smaller and larger resource totals. Its proof uses convex
subgradients and feasible transfers that preserve cost. It is not an
endpoint-concentration theorem. Later algorithmic, complexity, and
experimental claims were not audited here.

**Schoot Uiterkamp–Gerards–Hurink.** M. H. H. Schoot Uiterkamp,
M. E. T. Gerards, J. L. Hurink, *On a reduction for a class of resource
allocation problems*,
[arXiv:2008.11829v1](https://arxiv.org/abs/2008.11829v1),
26 August 2020;
[full HTML](https://arxiv.org/html/2008.11829),
[versioned PDF](https://arxiv.org/pdf/2008.11829v1).
Read complete Sections 2–3, including Condition 1, Theorem 1 and its complete
proof, and Corollaries 1–3. The objective family is
`sum_i a_i f(x_i/a_i+b_i)`, with `a_i>0` and common convex `f`.
Theorem 1 transfers quadratic optimality to this family when its specified
exchange optimality condition holds. That theorem explicitly allows a
general nonempty feasible set, rather than requiring convexity. Its proof
transfers the quadratic derivative inequalities through the monotonic
derivatives of `f`. The usual nested and submodular applications have affine
resource constraints. The appendix proofs and later application-specific
algorithms were not audited or used here.

These texts were openly accessible. A bounded search also surfaced the
earlier Vidal–Jaillet–Maculan decomposition paper, but its proofs were only
partially inspected, and no separate theorem-level conclusion relies on it.
Previously inaccessible Glazebrook endpoints were not retried. No third-party
paper is added to this repository.

## 2. The direct nested convex formulation is not established

For the fixed accessible order, retain the pass-20 notation
`D_k=b_k-gamma_k*M_k>0`. The exact completion-time constraints are

$$\phi_k(t_{k-1};U_k)\le t_k\le
\phi_k(t_{k-1};0),\qquad t_n\le H.$$

Replacing durations by cumulative times is an invertible linear change,
but these constraints are not thereby affine partial-sum bounds. The
continuous upkeep is a sum of differences of exponentials. Separability
alone establishes neither the feasible-set nor the objective hypotheses
needed for the direct nested convex model.

Here is an exact illustration of the first difficulty, deliberately using
a common coefficient so that its limitations are visible. Take

$$s=3,\quad a_1=a_2=0,\quad\gamma_1=\gamma_2=1,
\quad M=(3/2,1),\quad\epsilon=1/2,
\quad U=(1,1/2),\quad H=\log(11/4).$$

In order 1,2 the inversion is

$$q_1=3-\frac32e^{t_1},\qquad q_2=3e^{t_1}-2e^{t_2}.$$

The completion vectors

$$A=(\log(4/3),\log(7/4)),\qquad
B=(\log2,\log(11/4))$$

come respectively from `q=(1,1/2)` and `q=(0,1/2)`, and are feasible.
Their midpoint would require

$$q_1=3-\sqrt6,\qquad
q_2=2\sqrt6-\frac{\sqrt{77}}2>\frac12.$$

For the last strict inequality, `4*sqrt(6)>1+sqrt(77)` follows by
squaring positive sides and then using `9>sqrt(77)`. Thus the midpoint
violates the second preparation cap. The raw completion-time region is
nonconvex. The certificate applies to genuine uniform positive tolerance,
not just an arbitrary choice of caps.

**This is only a coordinate-specific obstruction.** In this very example,
the original preparation variables already give the known common-rate LP.
More generally, the
[geometry audit](2026-09-23-pass20-geometry.md) obtains a positive result:
for `lambda>=max_i gamma_i`, put `z_k=exp(lambda*t_k)` and
`r_k=gamma_k/lambda`. Each lower timing bound becomes

$$z_k\ge\psi_k(z_{k-1}),\qquad
\psi_k(z)=\left(\frac{b_kz^{r_k}-\gamma_kU_k}{D_k}\right)^{1/r_k}.$$

For `z>=1`, its interior expression is positive and `psi_k` is convex;
writing `A=b_k/D_k`, `B=gamma_k*U_k/D_k`, its second derivative is

$$A(1-r_k)Bz^{r_k-2}(Az^{r_k}-B)^{1/r_k-2}\ge0.$$

The upper timing bound becomes affine. Hence the fixed-order domain is
convex in these common exponential coordinates. Any claim that S1 cannot
be convexified would be false.

What remains to be proved for a convex allocation reduction is the
objective and constraint-class identification. For example, in the
pass-17 instance `s=3`, `M=(1,1)`, `gamma=(2,1)`, order 1,2, and
`H=log2`, choose `lambda=2`. On the feasible affine slice `z_2=4`,

$$q_1=(3-z_1)/2,\qquad q_2=3\sqrt{z_1}-4,
\qquad 16/9\le z_1\le25/9.$$

The linked upkeep on that slice is

$$2q_1+q_2=3\sqrt{z_1}-z_1-1,$$

which has strictly negative second derivative. Thus this explicit
convexification does not produce a convex objective even when support
charges vanish. It also does not turn every nonlinear lower graph into
an affine nested constraint. The statement is about the displayed
coordinates; other formulations are not excluded.

## 3. The broader exchange theorem needs its actual hypothesis

For a feasible set `C`, the second source calls `(i,k)` exchangeable at `x`
when `x+delta*(e_k-e_i)` belongs to `C` for some `delta>0`.
Its Condition 1 requires these derivative comparisons to be sufficient
and necessary for optimality of the separable convex objective:

$$\phi_k^+(x_k)\ge\phi_i^-(x_i)
\quad\text{for every exchangeable pair }(i,k).$$

S1's pass-19 variation does not transfer an equal amount of preparation
between two coordinates. It preserves a completion time along a curved
feasible path, with other preparation coordinates fixed. One cannot replace
that variation by equal-amount resource transfers without a proof.

The following exact counterexample shows why this distinction matters.
Use the pass-17 fixed-order instance

$$s=3,\quad a_1=a_2=0,\quad M_1=M_2=1,
\quad\gamma_1=2,\quad\gamma_2=1,\quad H=\log2.$$

The order 1,2 feasible set in preparation coordinates is

$$0\le x,y\le1,\qquad y\ge3\sqrt{3-2x}-4.$$

Add the natural nonnegative slack `w=2-x-y`, so the augmented set `C`
has the fixed total `x+y+w=2`. This addition does not solve the exchange
problem. Consider its two points

$$Q=(3/8,1/2,9/8),\qquad
P=(13/25,1/5,32/25).$$

Both meet the fixed-order deadline exactly. At Q the gradient of linked
upkeep `2x+y` is `(2,1,0)`. The six directed equal-amount exchanges behave
as follows:

| Transfer | Feasibility from Q for a positive amount | Directional derivative of `2x+y` |
|---|---|---:|
| `x` to `y` | Impossible for every amount allowed by the box | `-1` |
| `x` to `w` | Impossible: decreasing `x` increases required `y` | `-2` |
| `y` to `w` | Impossible: Q is on the deadline boundary | `-1` |
| `y` to `x` | Feasible for sufficiently small amounts | `1` |
| `w` to `x` | Feasible for sufficiently small amounts | `2` |
| `w` to `y` | Feasible for sufficiently small amounts | `1` |

For the first row, a transfer of amount `delta` requires
`0<delta<=3/8` and yields `x=3/8-delta`, `y=1/2+delta`.
Feasibility would require

$$3\sqrt{9/4+2\delta}\le9/2+\delta.$$

Squaring positive sides gives the reverse strict inequality because
the left square minus the right square is `delta*(9-delta)>0`.
Thus the obstruction covers the source's definition using *some*
positive amount, and not just infinitesimal moves. All other rows follow
from coordinate monotonicity or a sufficiently small perturbation of
the displayed boundary. Self-pairs have zero derivative.

Consequently every exchangeable pair satisfies Condition 1's derivative
inequality at Q, although

$$2P_x+P_y=31/25<5/4=2Q_x+Q_y.$$

Q is not optimal. Condition 1 fails for this direct fixed-order
preparation-plus-slack formulation, even with a linear convex objective.

### The failure also occurs for the shared quadratic family

To avoid relying only on a linear objective with differing slopes, take
the second source's parameters

$$a=(10,10,10),\qquad
b=(157/80,19/20,-9/80),\qquad f(v)=v^2/2.$$

These are allocation parameters, unrelated to S1's capacity-release
notation. The resulting convex objective, up to an additive constant, is

$$\Phi(x,y,w)=\frac{x^2+y^2+w^2}{20}
+\frac{157}{80}x+\frac{19}{20}y-\frac9{80}w.$$

Its gradient at Q is again `(2,1,0)`, so the same exchange comparisons
all hold. But

$$P-Q=(29/200,-3/10,31/200),$$

and the exact quadratic difference is

$$\Phi(P)-\Phi(Q)
=-\frac1{100}+\frac1{20}
 \left[\left(\frac{29}{200}\right)^2
       +\left(\frac3{10}\right)^2
       +\left(\frac{31}{200}\right)^2\right]
=-\frac{1299}{400000}<0.$$

This is a direct failure of the required condition even for the family
used to initiate the source's reduction. It is not a counterexample to
that source theorem: its hypothesis is absent.

An independent `fractions.Fraction` calculation checked both deadline
equalities, fixed totals, reduced cap membership, the three gradient
entries, and the exact cost difference. The direction exclusions above
are written inequalities; no sampled numerical search establishes them.

The construction remains inside the positive-tolerance capped box
`U_1=U_2=9/10`, obtained from `epsilon=1/10`. Both displayed points keep
the same positive preparation support, so the two nominal support charges
are constant in their linked-cost comparison. The table's excluded
directions remain excluded after restricting the box; each allowed
direction still has a sufficiently small feasible step. The additional
slack remains defined with total 2.

**Scope:** this certificate concerns the fixed order 1,2. It does not
claim that the same exchange condition fails after taking the union over
orders, or after a different nonlinear encoding with other auxiliary
variables. The pass-19 theorem uses a single attaining order to obtain its
local contradiction; a direct fixed-order prior-art substitution was the
route tested here.

## 4. Attribution and the remaining claim

The existing common-rate LP reduction and its standard allocation
attribution remain valid. In particular, neither caps nor a nonconvex
appearance in raw time coordinates undo that reduction. For nonzero
support charges, a fixed support makes those charges constant; an
unqualified convex formulation across support changes would need further
work.

The two inspected sources do not directly yield pass 19's statement that
**every** minimizer concentrates for arbitrary accessible orders, unequal
positive rates, and the specified linked upkeep prices. The reasons are
now hypothesis-level: the displayed convex clock need not have a convex
objective or affine nested bounds, and the direct augmented preparation
formulation fails equal-amount exchange optimality. The S1 proof instead
uses its particular curved exchange and proves strictly negative second
derivative at every stationary point of that exchange cost.

This is a bounded source comparison, not an impossibility theorem about
all reductions or a literature-wide novelty result. The positive
convexification and the fixed-order, nonincreasing-rate concave-allocation
reduction in the [geometry audit](2026-09-23-pass20-geometry.md) must be
retained in the combined assessment. The latter gives existence of a
concentrated optimum for those coefficient orders by a standard box-section
vertex argument; it does not supply pass 19's every-minimizer result for
arbitrary orders.
No computational complexity bound, general greedy rule, or operational
validation follows from this audit.
