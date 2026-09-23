# Pass 28: partial-coordinate ordering with arbitrary independent drains

23 September 2026. The pair exchanges used in the
[two-module common-drain proof](2026-09-23-pass26-common-drain.md) do not
require either member of the pair to be the first module handed off in the
whole system. This note gives their exact general scope.

With any finite number of modules and arbitrary positive immutable-drain
durations, the genuinely interior coordinates of a minimum-upkeep design
must hand off in strictly decreasing order of their proportional-loss
coefficients, in a maximal-loss witness normalized to hand off at first
fullness. A later such coordinate receives no preparation input before an
earlier one hands off. In particular, there is at most one interior
coordinate per distinct coefficient. When all coefficients are equal,
every minimum concentrates even with arbitrarily many unequal drains.

These conclusions concern minimum initial upkeep. They do not establish
global serial optimality from arbitrary given initial states, prohibit
intervening cold-module work, or settle concentration for many unequal
coefficients. They are internally proved structural results, not a new
general scheduling algorithm or a publication-priority claim.

## 1. Model and precise statement

Use the independent immutable-drain interface from
[pass 25](2026-09-23-pass25-proportional-drain.md), now with finite `n>=1`:

$$M_i>0,\qquad\gamma_i>0,\qquad a_i\geq0,\qquad
\ell_i>0,\qquad s\geq0.$$

Before its ownership handoff, module i has upper-reflected preparation with
input `v_i>=0` and loss `0<=rho_i<=gamma_i*p_i`. Every simultaneous such
history is admissible, including maximal proportional feedback on all
unfinished coordinates. Ownership handoff requires physical fullness,
stops preparation loss, and starts an independent immutable drain of fixed
duration `ell_i`. The preexisting source reservation `a_i` remains occupied
until that drain ends, then becomes preparation capacity. Thus

$$\sum_{i\text{ not handed off}}v_i(t)
\leq s+\sum_{j:t_j+\ell_j\leq t}a_j,$$

where t_j denotes an actual handoff. There are no impulses, shared drain
bottlenecks, or additional unbudgeted drain loads. New essential service
is independently supported after ownership handoff; the source remains for
its immutable obligations until drain completion. A loss-stopping handoff
is not an unresolved ownership decision. Normal operation has no handoffs
or releases.

The actual robust ready set `R_H^drain` contains initial states for which
one causal exit policy finishes every drain by the finite deadline H on
every admissible future loss history. Introduce design caps and nonnegative
fixed support charges,

$$0\leq U_i\leq M_i,\qquad h_i\geq0,\qquad
J(x)=\sum_i\gamma_i x_i+\sum_{i:x_i>0}h_i.                \tag{1}$$

The coefficients of variable upkeep remain the physical loss coefficients.
The support charges are used for the positive-tolerance corollary; they
do not affect a local variation that preserves positive support.

A **first-hit maximal-loss witness** is a feasible recorded maximal-loss
input schedule in which each ownership handoff occurs at the first time
that coordinate is full. Every actual ready state admits such a witness,
as proved below. These witnesses are analytical representatives. No claim
is made that every deliberately delayed ownership policy, or every realized
smaller-loss handoff order, has the same ordering properties.

**Theorem.** The actual ready set is compact. Whenever the intersection
with `0<=x_i<=U_i` is nonempty, J attains a minimum. At any such minimum,
let

$$P=\{i:0<x_i<U_i\}.$$

In every first-hit maximal-loss witness for that state:

1. The handoff times of the members of P are distinct.
2. If `i,j in P` and `t_i<t_j`, then `gamma_i>gamma_j`.
3. For this ordered pair, `v_j=0` almost everywhere on `[0,t_i)`.

Consequently,

$$|P|\leq\bigl|\{\gamma_i:1\leq i\leq n\}\bigr|.         \tag{2}$$

In particular, if the coefficients are common, every minimum has at most
one design-interior coordinate. Taking physical caps `U_i=M_i` and zero
support charges gives ordinary minimum-upkeep concentration for any number
of common-coefficient modules, even with unequal drains.

For smaller caps, (2) concerns interior coordinates relative to U. A
coordinate at its design cap may still be physically subfull; the theorem
does not relabel that coordinate as ready for ownership transfer.

## 2. Existence and canonical witnesses

If `H<max_i ell_i`, the ready set is empty. Otherwise each handoff lies
in the compact interval `[0,D_i]`, where `D_i=H-ell_i>=0`. An all-full
state is ready by immediate handoffs, though the smaller design box may
still contain no ready state.

On maximal loss, discard allocation wasted by upper reflection. This
preserves each path and cannot increase input use. For prescribed handoffs
t_i, extend each useful input by zero after its handoff and set

$$z_i(t)=x_i+\int_0^t e^{\gamma_i r}v_i(r)\,dr.$$

Up to t_i the exact path conditions are

$$0\leq z_i(t)\leq M_i e^{\gamma_i t},\qquad
z_i(t_i)=M_i e^{\gamma_i t_i},                           \tag{3}$$

together with nonnegative inputs and the stated capacity inequality.
Conversely, replaying any such path under smaller losses makes the actual
reflected state at least the maximal-loss path at every planned handoff.
Thus the same planned handoffs and drain completions are feasible on every
loss history. This proves that existence of a path (3) is equivalent to
actual robust readiness, rather than an assumption of optimal-time
attainment.

For completeness, the compactness argument from pass 26 extends to finite
n without change in its hypotheses. Given convergent ready initial states,
extract a subsequence of their handoff vectors converging in
`product_i [0,D_i]`. Their useful inputs are uniformly bounded by
`s+sum_i a_i`. On a common finite time interval containing all handoffs,
extract a weak-star convergent input subsequence and uniformly convergent
integrated paths. The integral equations pass to the limit. Nonnegativity
and zero input after the corresponding limiting handoff are preserved.
The finitely many capacity-step indicators converge almost everywhere
except at their limiting release times; testing against nonnegative
integrable functions preserves the input budget. Uniform path convergence
and handoff-time convergence preserve (3), including terminal equality.
Hence the limiting state is actually ready.

The physical initial box is compact, proving compactness of the ready set.
Intersecting it with the design box and minimizing the lower semicontinuous
objective (1) gives attainment. Nonnegative support charges are needed for
this lower semicontinuity; no general unbounded-horizon compactness claim is
used.

Finally, a maximal-loss witness can be normalized to first-hit handoffs.
For each module advance its handoff to its first full state, omit all of
that module's later old preparation allocations, and keep the other
recorded inputs unchanged. Other module paths are independent and unchanged
up to their own first full states. Each reservation is released no later,
and every released rate is nonnegative, so available capacity never falls
below that of the original witness. Every drain also ends no later. This
operation produces the stated first-hit witness, still robust by replay.

## 3. Advancing an earlier, no-faster interior coordinate strictly improves cost

Fix a minimum and one of its first-hit maximal-loss witnesses. Suppose two
design-interior coordinates A and B have handoff times

$$\tau=t_A\leq t_B=T,\qquad
\alpha=\gamma_A\leq\beta=\gamma_B.$$

Both initials are positive and physically subfull, so `tau>0`. Neither
coordinate has reflected waste before its own first hit. Define

$$g(t)=e^{\alpha t}(M_A-p_A(t)),\qquad 0\leq t\leq\tau.$$

This continuous gap is positive before tau and zero at tau. For sufficiently
small `eta>0`, let `tau'<tau` be its first crossing of eta. Then
`tau'->tau` as `eta->0`: the original gap has a positive minimum on every
compact interval lying strictly before tau.

Increase initial A by eta, replay its old input until tau', and hand it
off there. Its new path is the old path plus `eta*exp(-alpha*t)`, so it
is strictly subfull before tau' and exactly full at tau'. Choose eta small
enough to preserve `x_A+eta<U_A`.

Let

$$J_\beta=\int_{\tau'}^\tau e^{\beta t}v_A(t)\,dt.$$

Decrease initial B by `J_beta`. On `[tau',tau]`, add A's old input to
B's old input. Before tau' and after tau, retain B's old input. Keep the
initial states, inputs and handoff times of every other module exactly
as in the old witness. Choose eta small enough that `J_beta<x_B`, which
is possible because inputs are bounded and the interval shrinks to zero.
Both changed initial coordinates remain strictly inside their design caps.

Before tau', B's new state differs from its old state by
`-J_beta*exp(-beta*t)`. Between tau' and tau the difference is

$$-e^{-\beta t}\int_t^\tau e^{\beta r}v_A(r)\,dr.$$

It is therefore never increased before tau and matches the old path from
tau onward. It stays positive because the old maximal-loss path is at
least `x_B*exp(-beta*t)` before its handoff, and the discounted decrease
is at most J_beta. Thus no cap or lower-bound violation is introduced, and
B still hands off at T, including the possible case `T=tau`.

This perturbation remains feasible in the presence of all other modules.
On `[tau',tau]`, replacing A's old input by an equal addition to B's input
preserves total preparation use. Elsewhere total use is unchanged. Only
A's release time changes, from `tau+ell_A` to `tau'+ell_A`, which is
earlier. With `a_A>=0`, every other module's unchanged recorded input still
fits the capacity budget. Its state and its planned handoff and drain end
remain unchanged. No hypothesis about A being globally first, about equal
drains, or about an absence of intervening other releases is needed.

The original A terminal balance supplies

$$\int_{\tau'}^\tau e^{\alpha t}v_A(t)\,dt
=M_A(e^{\alpha\tau}-e^{\alpha\tau'})+\eta.$$

The support does not change, and the objective change is consequently

$$\begin{aligned}
\Delta J&=\alpha\eta-\beta J_\beta\\
&=-\alpha M_A(e^{\alpha\tau}-e^{\alpha\tau'})
+\int_{\tau'}^\tau
 (\alpha e^{\alpha t}-\beta e^{\beta t})v_A(t)\,dt<0.
\end{aligned}                                           \tag{4}$$

For nonnegative t and `alpha<=beta`, the integrand coefficient is
nonpositive, while the first term is strictly negative. Robust replay of
the modified maximal-loss witness makes the new state actually ready.
This contradicts its supposed minimum.

If two interior coordinates had simultaneous handoffs, label the one with
the smaller coefficient A and apply (4). Thus their times must be distinct.
For different times, (4) excludes a nondecreasing coefficient pair. This
proves assertions 1 and 2, and already proves the coefficient-class bound
(2).

## 4. A later interior coordinate receives no input before an earlier one hands off

Now take two interior coordinates at a minimum with `tau=t_A<t_B`.
Section 3 gives `alpha=gamma_A>gamma_B=beta`. Suppose B has positive
input on a set of positive measure before tau. Choose a nonnegative
nonzero portion h of this input supported in a compact interval strictly
before tau; such a portion exists if the input is not almost everywhere
zero there. Make its amplitude small, and transfer h from B's input to
A's. At the same time set

$$x_A'=x_A-\int e^{\alpha r}h(r)\,dr,\qquad
x_B'=x_B+\int e^{\beta r}h(r)\,dr.                       \tag{5}$$

After the end of h's support, both paths exactly match their originals.
Before then A's new state is at most its old state, and B's is at least
its old state. Decrease the amplitude so that both initials remain
strictly inside their design caps. Positivity of A is preserved by making
its discounted reduction smaller than x_A. B has a strictly positive cap
margin on the compact interval up to the end of h's support, because its
first full hit occurs later than tau; making h small preserves that margin.
Therefore both first-hit handoff times are unchanged.

Every other coordinate, input and handoff is unchanged, and the pair's
total input is unchanged pointwise. Thus all releases, all capacity budgets
and all other module paths agree with the old witness. The variable and
total objective change is

$$\Delta J=\int
 (-\alpha e^{\alpha r}+\beta e^{\beta r})h(r)\,dr<0,      \tag{6}$$

since `alpha>beta` and `r>=0`. This contradiction proves assertion 3.
It also specifies why the argument still works when nonpartial modules
receive preparation or release capacity between the pair's handoffs.

## 5. Positive request-time tolerance

For a common absolute deficit allowance `epsilon>0`, nominal state p must
be actually ready from every request-time state between its worst corner
`q=(p-epsilon)_+` and p. The uncertainty is a one-time request-time
shortfall, not an additional continuous stream of normal losses. Monotone
replay under the independent-drain interface makes worst-corner readiness
equivalent to this contract.

At a minimum no coordinate satisfies `0<p_i<=min(epsilon,M_i)`:
setting it to zero leaves q unchanged and strictly lowers upkeep. On the
remaining support `p_i=q_i+epsilon`. Hence the nominal problem is exactly
(1), with

$$U_i=(M_i-\epsilon)_+,\qquad h_i=\gamma_i\epsilon.$$

The theorem proves attainment whenever this problem is feasible and bounds
the number of nominally partial coordinates by the number of distinct
proportional coefficients. In particular, for a common coefficient,
**every minimum nominal state has at most one partial coordinate**, for
any finite number of modules and arbitrary positive independent drains.

Here q at its positive upper cap corresponds to a physically full nominal
coordinate p, while an interior positive q corresponds to
`epsilon<p_i<M_i`. A zero cap forces nominal zero at a minimum. The
effective worst corner need not contain physically full modules: this is
a statement about the nominal design, not a claim that `M_i-epsilon` is
transfer-ready. No equality of optimum costs between zero and positive
tolerance is asserted.

## 6. Structural meaning and limits

The two-partial counterexamples in passes 25 and 27 have unequal
coefficients, with the larger coefficient handed off first. They therefore
obey the ordering restriction rather than contradicting it. Their differing
handoff deadlines can stop the further time variation used in pass 26;
the present pair theorem does not exclude such an optimum when two
distinct coefficients are available.

For two modules, the surviving results now separate two cases precisely:
common drains permit arbitrary positive coefficients by pass 26, while
common coefficients permit arbitrary positive drains by this note. The
two-module failures need both heterogeneities. For more modules, this note
settles common coefficients but does not settle general unequal-coefficient
concentration with common drains.

The input restriction concerns only coordinates strictly inside their
initial design caps. Cold modules, design-capped modules and initially full
modules can intervene, provide useful releases, or interrupt work on an
interior coordinate. The proof does not show that all preparation is
contiguous or that the entire schedule is serial. It also does not assert
the same handoff order on every smaller-loss realization; the ordering is
for first-hit maximal-loss witnesses at a minimum.

The exchanges rely on the shared input resource, linked upkeep weights,
positive proportional loss, independent fixed drains and nonnegative
released reservations. Advancing a handoff would require another argument
if it created an unbudgeted drain load, blocked another drain, or left
state-changing ownership obligations unresolved. The model's operational
and prior-art limitations therefore remain substantive. This finding is a
structural consequence of the explicit pair improvement, not a novelty
claim for discounted allocation or a solved general resource scheduler.
