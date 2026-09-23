# Pass 30: positive tolerance and an open common-drain separation

23 September 2026. This follows the exact three-module separation in
[pass 29](2026-09-23-pass29-cold-test.md). The separation survives a fixed
positive request-time preparation shortfall, finite cold startup, and a
neighborhood of model parameters with a common drain duration. The
[exact zero-deficit optimum](2026-09-23-pass30-exact-optimum.md) also gives an
exact positive-tolerance cost and unique nominal optimizer on an explicit
interval. No numerical neighborhood radius is claimed.

## 1. The strict gap available from pass 29

Keep the three-module independent-drain interface and the parameter vector

$$
s=1,\quad \gamma=(2,1,3),\quad
M=\left(\frac{27}{242},\frac7{20},\frac{11679823}{10222080}\right),
\quad a=\left(\frac{6075}{2662},1,1\right),
\quad \ell=\log 2,\quad H=\log 8.
$$

Write $D=H-\ell=\log4$ and $L(p)=2p_A+p_B+3p_C$.
Pass 29 proves two different statements:

1. The state $x=(3/100,1/8,0)$ is actually robustly ready, with
   $L(x)=J=37/200$.
2. Every physically concentrated ready state has cost strictly greater than
   $B=1851/10000$. The bound covers all schedules, including interrupted
   and parallel preparation, not only the displayed serial policy.

Here concentrated means at most one coordinate strictly between zero and
its physical cap; arbitrary full and cold coordinates are allowed. The
exact ready set is compact, as is its intersection with the closed union
of concentrated faces. Thus the restricted minimum exists and is strictly
above B. In particular, the certified gap over the exhibited state exceeds
$B-J=1/10000$. Pass 29 establishes J as a feasible cost. The separate
[exact-optimum proof](2026-09-23-pass30-exact-optimum.md) subsequently proves
that J is the unrestricted minimum and x is its unique minimizing state.

## 2. A strictly early two-partial exit

Let $\eta=1/100000$ and increase both positive coordinates by eta:

$$q=x+(\eta,\eta,0).$$

Use full-rate serial preparation in order A, B, C, with every handoff at
first fullness. Before A and B hand off no reservation has yet released.
Put $A_0=94/121$, $B_0=13/20$, and let X and Y be the exponentials of
their handoff times. Their exact values obey

$$
X^2=\frac{1-2q_A}{A_0},\qquad
Y=\frac{X-q_B}{B_0}.
$$

The strict initial-cap margins give $X>1$ and $Y>X$; the latter also
follows from $q_B<d_BX$, where $d_B=7/20$. Since both initial amounts
have increased,

$$1<X<\frac{11}{10}<Y<\frac32<2.$$

For example, $X>109/100$ follows by squaring, and then
$Y>(109/100-q_B)/B_0>11/10$. All of these are rational comparisons after
the one positive square root is bounded. In particular the strict event
order is unchanged:

$$t_A<t_B<t_A+\ell<t_B+\ell<D.$$

The unreflected terminal balance for C when given full available input
after B is

$$
3p_C(D)=1+a_A+a_B
-\frac{9Y^3+8a_AX^3}{64}.
$$

At the old X=11/10 and Y=3/2 this equals $3M_C$. Both terms subtracted
are now strictly smaller, so $p_C(D)>M_C$ in this comparison equation.
C starts cold and receives nondecreasing input. Its actual first full
hit therefore occurs strictly before D. The two rate barriers from pass
29 still prevent this hit until both earlier reservations have released.
Every drain finishes strictly before H.

This establishes a genuine deadline margin without evaluating a logarithm
numerically. Under a smaller allowed loss history, replay of the virtual
maximal-loss policy remains feasible and achieves the same strict bound.
Extra nominal preparation has not been treated as extra source capacity.

## 3. Exact fixed-positive-deficit frontier

Use the repository's one-time request-deficit contract. For every

$$0\leq\epsilon\leq\frac1{30000},$$

the unique minimum nominal state and exact nominal upkeep are

$$
p^*_\epsilon=x+(\epsilon,\epsilon,0),\qquad
C_\epsilon=\frac{37}{200}+3\epsilon.
$$

The effective worst corner is x, so the displayed target is feasible and
its cost is at most B throughout the stated interval. The physical cap
margins are larger than this epsilon. At epsilon zero, uniqueness is the
separate exact-optimum theorem. For positive epsilon, let p be any nominal
minimum. Attainment follows from the continuous deficit map, closed
readiness, and compact physical box.

Its cost is at most B. Any nominal state meeting the deficit contract is
also exactly ready from itself, by upward comparison. Thus p cannot be
concentrated, by pass 29, and cannot contain a physically full coordinate,
since each full cost exceeds B. It has at least two positive coordinates.
At a minimum none can satisfy $0<p_i\leq\epsilon$: setting such a
coordinate to zero leaves the worst corner unchanged and strictly lowers
upkeep. Therefore its effective corner $q=(p-\epsilon)_+$ has the same
support, and

$$
L(p)=L(q)+\epsilon\sum_{i:q_i>0}\gamma_i
\geq J+3\epsilon.
$$

Here actual readiness of q gives $L(q)\geq J$, and every support of at
least two coordinates has coefficient sum at least $1+2=3$. Equality in
the displayed bound forces $L(q)=J$, hence q=x by the unique exact
optimum. It then forces the nominal state asserted above. No fixed charge
was silently dropped when a cold coordinate was activated.

Every concentrated nominal ready state is an exactly ready concentrated
state, so its cost remains strictly above B. In particular,

$$C_\epsilon=J+3\epsilon\leq B<C^{\mathrm{conc}}_\epsilon.$$

If the restricted positive-tolerance ready set is empty, its cost is
infinity; otherwise its minimum is attained on the closed concentrated
faces. The endpoint $\epsilon=1/30000$ is included because the
concentrated bound is strict. Larger epsilon is not characterized here;
this certificate endpoint is not an infeasibility threshold.

For the open-neighborhood argument below, choose
$\epsilon=\eta=1/100000$ and use the slightly more prepared nominal target

$$p=x+(2\epsilon,2\epsilon,0).$$

Its worst corner is the strictly early q of Section 2. This target costs

$$L(p)=J+6\epsilon=\frac{9253}{50000}=0.18506<B.$$

It is not the nominal optimizer: the additional preparation buys strict
deadline slack for a perturbation argument. The same fixed positive
request tolerance and a strict concentrated-cost advantage are preserved.

## 4. Normal operation and finite cold warmup

The preceding nominal target has strict normal upkeep slack:

$$1-L(p)=\frac{40747}{50000}>0.$$

After paid initialization, holding at least p by allocating
$v_i=\gamma_i p_i$ and the remaining rate to optional work guarantees
readiness at every admissible request time. Under maximal proportional
loss the target is stationary. Under smaller losses it can rise; scalar
comparison keeps it above p. This is the source-resource accounting of
the model, not the total resource cost of the independent receiver.

The same target can be reached in finite time from cold before deployment
without exceeding the original normal budget. Let $Q=\sum_i p_i>0$ and
$K=L(p)<1$. Use the virtual path $p_i(t)=\theta(t)p_i$, with

$$
\theta'=\frac{1-K\theta}{Q},\qquad \theta(0)=0,
\qquad v_i(t)=p_i\bigl(\theta'(t)+\gamma_i\theta(t)\bigr).
$$

All inputs are nonnegative, their sum is one, and the maximal-loss path
obeys the stated dynamics. It reaches the target at

$$t_{\mathrm{warm}}=\frac{Q}{K}\log\frac1{1-K}<\infty.$$

At smaller losses, comparison gives a state at least as prepared at this
time; reflected caps do not invalidate that lower comparison. The readiness
guarantee begins after warmup. No all-request-time guarantee is asserted
during startup, and the request deficit is not an unmodeled continuous
normal disturbance.

## 5. Persistence under parameter changes

The strict separation is not tied to the exact equality $D=2\ell$ used
to certify the base instance. Keep three modules and the same independent
drain interface, and allow $(s,\gamma,M,a,\ell,H)$ to vary near the
displayed vector, with one common positive ell and positive sizes and rates.
The following argument proves a relative open neighborhood; it does not
give a computed radius or a uniform statement far from this vector.

First, actual robust readiness has a closed graph locally in these
parameters. To see this, take convergent parameter and ready-state
sequences in a compact neighborhood with a common finite horizon bound.
Choose maximal-loss useful-input witnesses as in pass 28. Their handoff
times and bounded inputs have convergent subsequences, respectively in
finite-dimensional compact intervals and weak-star in $L^\infty$.
Integrated discounted paths converge uniformly along a further subsequence.
The exponentials and cap functions vary continuously with the coefficients
and sizes. The finitely many release-step functions converge almost
everywhere, including when event times coalesce. Terminal equality, all
path caps, nonnegative inputs, and the capacity inequalities therefore
pass to the limit. The limiting handoffs obey the limiting deadline.
Robust replay makes the limit actually ready.

Second, the graph of physical concentration is closed as the caps vary.
There are finitely many choices of the possible interior coordinate and
of whether each other coordinate is zero or at its cap. Passing to one
fixed choice along a subsequence preserves that face at the limit.

It follows that some neighborhood has **no concentrated ready state of
cost at most B**. Otherwise a sequence of such nearby states would have
a convergent subsequence, since the boxes remain uniformly bounded. The
closed-graph conclusions and continuity of upkeep would produce a
concentrated ready state of cost at most B at the base parameters,
contradicting Section 1.

Finally keep the fixed nominal p and epsilon of Section 3. All physical
cap inequalities are strict. Its worst corner q has a serial witness
with strict handoff order, strict resource/cap crossing inequalities, and
strict deadline slack. The scalar flows and simple cap-hitting times
depend continuously on the parameters in this neighborhood; the release
events stay in the same strict order. Thus this fixed nominal target
remains epsilon-ready after restricting the neighborhood. Its cost stays
below B and below s by continuity. The same radial warmup construction
continues to work with the perturbed coefficients and source budget.

Hence a relative open family of common-drain models has fixed positive
request tolerance, finite cold startup, normal optional slack, and a
strict advantage over every concentrated design. H may vary independently
within this neighborhood; it is not calibrated to an equality such as
$C(H)=s$. This is a local ideal-model statement, not a robustness claim
against changing the service interface or introducing a shared drain
bottleneck.

## 6. Contribution boundary

Combined with pass 26, this makes three the smallest module count at which
a common drain can defeat minimum-upkeep concentration. Common coefficients
still preserve concentration for any module count by pass 28. The displayed
failure uses three distinct coefficients; no sharp classification by the
number of coefficient classes is claimed.

The witness does not require interrupted preparation or unequal deadlines.
The cold module needs released capacity from both earlier handoffs, so its
deadline couples their preparation times. This is distinct from pass 27's
shrinking unequal-deadline family, where the certified tolerance and
advantage vanish in the common-drain limit. Established compactness,
comparison and resource-accounting arguments supply the robustness steps;
they are not presented as new general control or scheduling principles.
Publication novelty and an operationally justified application remain
unresolved. No manuscript work or external certification is implied.
