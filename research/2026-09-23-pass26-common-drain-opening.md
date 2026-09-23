# Pass 26 opening: isolate common residual drains

23 September 2026. This is an opening calculation and exact restart task,
**not a completed pass or an all-policy concentration theorem**. Use the
[pass-25 proportional-drain interface](2026-09-23-pass25-proportional-drain.md).
Its two-partial optimum uses unequal latest handoff deadlines and no useful
capacity release. The next question removes that unequal-deadline mechanism.

The [pass-6 fixed-loss examples](2026-09-22-pass6-latency.md), Sections 3–4,
were re-read: overlapping drains beats module-by-module removal, and a
three-module instance requires preempting preparation. Those examples use
fixed-rate loss and do not settle proportional loss. They prohibit importing
the instantaneous seriality theorem merely because drains share one duration.

## 1. Fixed handoff times give a linear allocation problem

Prescribe handoff times `t_i>=0` satisfying `t_i+ell_i<=H`, and set

$$T=\max_i t_i,\qquad
b(t)=s+\sum_{j:t_j+\ell_j\leq t}a_j.$$

The maximal-loss preparation path before each handoff is represented by

$$z_i(t)=x_i+\int_0^t e^{\gamma_i r}v_i(r)\,dr,
\qquad p_i(t)=e^{-\gamma_i t}z_i(t),\quad 0\leq t\leq t_i.$$

Minimize `sum gamma_i*x_i` subject to

$$\begin{gathered}
0\leq x_i\leq M_i,\qquad v_i(t)\geq0,\qquad
v_i(t)=0\quad(t>t_i),\\
\sum_{i:t<t_i}v_i(t)\leq b(t)\quad\text{almost everywhere},\\
0\leq z_i(t)\leq M_i e^{\gamma_i t}\quad(0\leq t\leq t_i),
\qquad z_i(t_i)=M_i e^{\gamma_i t_i}.
\end{gathered} \tag{1}$$

For fixed times these are linear constraints on the initial state and
measurable inputs, including the continuum of intermediate cap constraints.
Reflection does not invalidate this formulation: replace allocation at an
upper cap by its useful part `min(v_i,gamma_i*M_i)`, thereby removing waste
without increasing its budget. Conversely every constrained path in (1) is
an admissible reflected path. A coordinate may reach its cap early and wait
before ownership handoff; it remains subject to loss until `t_i`.

An admissible maximal-loss schedule with these planned handoffs is robust:
the same inputs under smaller losses produce at least the virtual preparation
by scalar comparison, so all planned handoffs remain possible. Conversely
any robust policy supplies a maximal-loss realization with some handoff
times. Thus the fixed-time representation is exact, but optimizing over the
times themselves is a separate problem; b then also changes with the times.

A useful lower certificate needs no strong-duality or optimizer-existence
claim. For any constants `0<=lambda_i<=gamma_i`, terminal integration and
the pointwise input budget give

$$L(x)\geq\sum_i\lambda_iM_i e^{\gamma_i t_i}
-\int_0^T b(t)\max\left(\{0\}\cup
\{\lambda_i e^{\gamma_i t}:t<t_i\}\right)dt. \tag{2}$$

Indeed, `L(x)>=sum lambda_i*x_i`; substitute the terminal identities in
(1) and bound the weighted inputs by their largest coefficient times b.
Equivalently, nonnegative reflected waste can be discarded before this
calculation. Intermediate caps may make (2) loose. Pass 25 uses
`lambda_i=gamma_i` and proves equality by an explicit feasible schedule.
This is discounted-input linear allocation reasoning, not a new general
duality theorem or a solution of the variable-handoff problem.

## 2. Common drains: what is already reduced

Let every `ell_i=ell>0` and put `D=H-ell`. All handoffs must occur by D.
For `ell<=H<=2*ell`, no drain releases capacity before any required
preparation can still benefit. The full ready set equals the instantaneous
zero-release ready set at deadline D, as proved in pass 25. Concentration
survives in that subclass. For `H<ell` the ready set is empty.

The unresolved regime is `0<2*ell<H`, where `D>ell` and a common drain
can end while other preparation is still needed.

## 3. Two-module serial branch: an explicit calculation

Consider the restricted policy family A then B: give all available
preparation capacity to A until its handoff at t, then to B until its
handoff at D. Drains overlap preparation. Write

$$\alpha=\gamma_A,\quad\beta=\gamma_B,\quad
d_A=\alpha M_A,\quad d_B=\beta M_B,\quad a=a_A.$$

Assume `0<t<D`, `s>d_A`, and retain only t for which the formulas below
give initial coordinates strictly inside their physical caps and valid
preparation paths. For example, B needs `s+a>d_B` if it completes after
A's release, or `s>d_B` if it finishes without that release. This family
does not include every parallel, preemptive, idle or adaptive policy.

In both release regimes the required A preparation is

$$\alpha x_A=s-(s-d_A)e^{\alpha t}.$$

When `t+ell<=D`, direct integration of B's allocation gives

$$\beta x_B=(d_B-s-a)e^{\beta D}
+(s+a e^{\beta\ell})e^{\beta t},$$

so its total upkeep is

$$W_-(t)=s-(s-d_A)e^{\alpha t}
-(s+a-d_B)e^{\beta D}+(s+a e^{\beta\ell})e^{\beta t}.
\tag{3}$$

When `t+ell>=D`, no release contributes before B's handoff, and

$$W_+(t)=s-(s-d_A)e^{\alpha t}
-(s-d_B)e^{\beta D}+s e^{\beta t}. \tag{4}$$

Each smooth branch has the form `constant-A*exp(alpha*t)+C*exp(beta*t)`,
where `A=s-d_A>0` and `C>=s>A`. If `beta>=alpha`, its derivative is
strictly positive for `t>=0`. If `beta<alpha`, then at every stationary
point

$$W''(t)=\alpha A e^{\alpha t}(\beta-\alpha)<0.$$

Thus a smooth interior stationary point cannot be a local minimum.
The two expressions agree at `t_0=D-ell`, and their one-sided derivatives
satisfy

$$W_+'(t_0)-W_-'(t_0)=-\beta a e^{\beta D}<0. \tag{5}$$

Where both neighboring branches are physically feasible, this downward
jump also excludes a local minimum at the release transition. A minimum
there would require the left derivative to be nonpositive and the right
derivative nonnegative, contrary to (5). If physical caps end a branch,
the endpoint must instead be assessed with its actual state constraints.

The calculation fixes B's handoff at D and restricts allocations to the
specified family. It neither proves that an arbitrary optimum has this
form nor proves concentration for arbitrary common-drain policies.

## 4. Exact next task and stopping rule

Test the two-module common-drain model with `0<2*ell<H` over the full
admissible policy class. Either prove that no minimum can have two partial
coordinates, using a valid all-policy bound or reduction, or produce an
exact counterexample and a matching lower certificate. Include both actual
handoff orders, initial-full states, reflected waste and active cap cases.
If the obstruction is instead an unproved scheduling lemma, record that
lemma precisely; do not replace its proof by the branch calculation above.

Do not expand to a general scheduling solver or claim novelty before a
targeted comparison with scheduling under delivery tails and preparation
deadlines. This opening establishes a fixed-time formulation and a restricted
calculation only. The common-drain all-policy question remains **OPEN**.
