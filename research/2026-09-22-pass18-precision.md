# Pass 18: exact-full endpoints and one-sided preparation uncertainty

22 September 2026. This note tests the dependence of the proportional-loss
results on an exactly full initial coordinate. An infinitesimal preparation
deficit can remove an instantaneous transfer and expose a finite-time rate
barrier. The resulting discontinuity is real even when cold post-request exit
is finite. Nevertheless, every strictly positive optional-work frontier is
unchanged by the one-sided limiting envelope defined below. Critical,
zero-optional readiness can fail this test.

The model remains the ideal instantaneous independent-transfer model. This
is a mathematical sensitivity result, not a hardware error model or a claim
that a fixed positive error allowance has zero maintenance cost. The original
endpoint convention and historical results are not changed.

## 1. Definition and exact scheduling formula

Use the pass-9/pass-11 model with a positive finite number of modules,

$$M_i>0,\quad \gamma_i>0,\quad a_i\geq0,\quad s\geq0,
\qquad d_i=\gamma_iM_i,\qquad b(S)=s+\sum_{i\in S}a_i.$$

The uncertainty includes simultaneous maximal proportional loss. Write
`F(p)` for the original exact robust exit time. For `epsilon>0` let

$$p_i^{\epsilon}=\max\{p_i-\epsilon,0\},\qquad
F_-(p)=\lim_{\epsilon\downarrow0}F(p^{\epsilon}).       \tag{1}$$

The limit exists in the extended nonnegative reals: preparation is increasing
as epsilon decreases, and exit time is nonincreasing. Every coordinate of
`p^epsilon` is strictly below its physical full threshold. An error box with
independent deficits between zero and epsilon has this same worst corner,
by monotonicity of `F`. Epsilon is a common absolute preparation deficit in
the model's charged work units, rather than a relative error percentage.

Call a permutation `pi` **strictly accessible** when every one of its stages
satisfies

$$b(S_{k-1})>d_{\pi_k},\qquad
S_{k-1}=\{\pi_1,\ldots,\pi_{k-1}\}.                    \tag{2}$$

This definition includes stages whose coordinates are initially full. Let
`P` be the finite family of these permutations. For `pi in P` define, on the
entire closed preparation box,

$$\begin{aligned}
t_0&=0,\\
t_k&=\frac1{\gamma_{\pi_k}}
\log\frac{b(S_{k-1})e^{\gamma_{\pi_k}t_{k-1}}
                 -\gamma_{\pi_k}p_{\pi_k}}
                {b(S_{k-1})-d_{\pi_k}},\\
G_{\pi}(p)&=t_n.                                         \tag{3}
\end{aligned}$$

Every denominator is positive. The logarithm argument is positive, and
`t_k>=t_{k-1}`: subtracting the denominator times
`exp(gamma_i*t_{k-1})` from the numerator gives
`d_i*exp(gamma_i*t_{k-1})-gamma_i*p_i>=0`. These are actual serial schedules,
including a zero-length stage when a full coordinate is selected at time
zero. A full coordinate left until positive time decays while waiting and
must be prepared again; it is not silently transferred for free.

**Theorem 1 (one-sided envelope).** With the minimum over an empty family
defined as infinity,

$$F_-(p)=\min_{\pi\in\mathcal P}G_{\pi}(p).             \tag{4}$$

If cold post-request exit is blocked, `F_-` is identically infinite. If cold
exit is finite, `F_-` is finite and continuous on the entire closed box.
Moreover `F(p)<=F_-(p)` everywhere, with equality whenever no coordinate of
`p` is initially full.

**Proof.** Every `p^epsilon` is subfull. The all-state serial theorem and
the strict scalar rate barrier give
`F(p^epsilon)=min_{pi in P}G_pi(p^epsilon)`. The family `P` depends on the
capacities and thresholds, not on epsilon or the initial preparation.
The closure theorem in pass 13 says `P` is empty exactly when cold exit is
blocked. In the nonempty case each recurrence in (3) is continuous on the
compact box, and a finite minimum commutes with the limit in (1). This proves
(4), finiteness, and continuity. Monotonicity gives `F(p)<=F(p^epsilon)`.
For a subfull `p`, the same serial argument directly gives (4) for `F(p)`.

The envelope can be evaluated by a forward subset dynamic program from
`E(empty)=0`, using (3) for every strictly accessible edge. In contrast with
the original oracle, it does not initialize the completed set with all
initially full modules. Earliest arrival still dominates every later arrival
at the same subset. The operation count is `O(n*2^n)` scalar exponential,
logarithmic, and comparison operations with `O(2^n)` memory, without a claimed
bit-complexity or certified floating-point implementation.

## 2. Where the original and limiting oracles agree

**Proposition 2 (accessible full prefix).** Let `S={i:p_i=M_i}`. If the
members of `S` admit an order which satisfies (2) starting from the empty
set, then

$$F_-(p)=F(p).                                           \tag{5}$$

This includes the empty set, and in particular holds if `d_i<s` for every
`i in S`.

**Proof.** Put that order of full coordinates first. Each stage has length
zero and releases its capacity before the next one. Follow an optimal
original schedule from the remaining subfull coordinates; every subsequent
finite stage is strictly accessible. This constructs a strict permutation
with value `F(p)`. Combine it with `F<=F_-`. If `F(p)` is infinite, the same
inequality already gives equality in the extended sense.

There is a useful consequence directly in terms of upkeep
`L(p)=sum_i gamma_i*p_i`. If `L(p)<s`, every full coordinate has `d_i<s`,
so (5) holds. If `L(p)=s`, it still holds unless `p` is supported on exactly
one full coordinate whose loss is `d_i=s`. Indeed, a full coordinate with
`d_i>=s` already consumes all of the nonnegative upkeep sum, and equality
forces every other coordinate to be zero. This identifies the sole possible
economically critical endpoint obstruction; it does not say every such
singleton actually has a discontinuity.

## 3. The limiting maintenance problem and concentration under maintainability

For finite `H>=0`, set

$$\mathcal R^-_H=\{p:F_-(p)\leq H\},\qquad
C_-(H)=\min_{p\in\mathcal R^-_H}L(p),                   \tag{6}$$

with value infinity if the feasible set is empty. If cold exit is finite,
Theorem 1 makes the set compact and nonempty: the all-full vector has zero
length in every strict order. Thus the minimum is attained. If cold exit is
blocked, the set is empty for every finite deadline. Always

$$C_-(H)\geq C(H).                                       \tag{7}$$

The same storage bound and constant-maintenance construction as in pass 9
apply to this contract. The feasible set is upward closed; on maximal loss
any normal trajectory in it has `Q'<=s-u-C_-(H)`, where `Q=sum_i p_i`.
Conversely, an attained minimum with cost at most s is preserved from below
by allocations `v_i=gamma_i*p_i`. Thus the initialized optimal optional rate
for the limiting contract is `s-C_-(H)` when `C_-(H)<=s`, and indefinite
readiness is impossible otherwise. These assertions concern membership in
the limiting set (6), with its fixed-tolerance interpretation addressed below.

**Theorem 3 (strict optional slack is unchanged).** If `C(H)<s`, then

$$C_-(H)=C(H).                                           \tag{8}$$

More generally, equality holds whenever an original minimizing state has a
strictly accessible full prefix. At `C(H)=s`, failure of equality is possible
only if every original minimizer is a full singleton with full loss `s` and
all other coordinates cold.

**Proof.** At any original minimizer with `L(p)=C(H)<s`, Proposition 2
gives `F_-(p)=F(p)<=H`. This supplies the reverse inequality to (7). The
same argument proves the accessible-prefix extension. At equality `C(H)=s`,
every minimizer which is not a full singleton of cost `s` has each of its
full losses strictly below `s`, so it too supplies a reverse inequality.

Consequently the one-sided limiting contract has exactly the same positive
optional throughput `s-C(H)` whenever the original contract has positive
optional throughput. This is a statement about the limiting contract (6),
whose maintained state must satisfy that contract; a fixed error allowance
is distinguished in Section 5.

**Theorem 4 (concentration in the maintainable regime).** If
`C_-(H)<=s`, every minimizer in (6) has at most one partial coordinate.

**Proof.** First `C(H)=C_-(H)`. Otherwise (7) gives
`C(H)<C_-(H)<=s`, and Theorem 3 supplies the contradictory equality.
Every minimizer of (6) is an original feasible state with cost `C(H)`;
it is therefore an original minimizer. The pass-11 concentration theorem
applies to every such minimizer.

This proof deliberately claims concentration only when `C_-(H)<=s`.
The unrestricted case `C_-(H)>s` can have initially full coordinates which
cannot be placed in a zero-length strict prefix. Such coordinates may lie
between two partial coordinates in an attaining strict order, and their
waiting decay invalidates a direct copy of pass 11's constant cold-prefix
duration argument. That extension is not needed to characterize any
indefinitely maintainable limiting contract and remains unproved here.

The concentration statement concerns the limiting cost `C_-`, not minimizers
at a fixed positive tolerance. Even a nominally full coordinate becomes
strictly subfull at the worst corner of a positive deficit box, so the
original free-full-prefix exchange cannot simply establish concentration
for `C_epsilon`. Convergence of optimal costs does not prove such a structural
statement about finite-tolerance optimizers.

## 4. A smallest exact critical discontinuity with finite cold exit

Take two modules with

$$s=\gamma_A=\gamma_B=1,\qquad
M_A=\tfrac12,\quad M_B=1,\qquad a_A=a_B=1.               \tag{9}$$

Cold exit is finite. The only strictly accessible order is A then B, since
initial capacity one equals B's full loss. The recurrence (3) gives, on the
whole closed box,

$$e^{F_-(p)}=4-4p_A-p_B.                                \tag{10}$$

At `p=(0,1)`, the original oracle transfers B at time zero and prepares A
at capacity two. Therefore

$$F(0,1)=\log(4/3),\qquad F_-(0,1)=\log3.               \tag{11}$$

The positive gap persists despite finite cold exit `F(0,0)=log4`.
For the positive deadline

$$H=\log(4/3),                                          \tag{12}$$

the original optimum and regularized optimum are exactly

$$C(H)=1=s,\quad p^*=(0,1),\qquad
C_-(H)=\tfrac76>s,\quad p^-=(\tfrac12,\tfrac23).       \tag{13}$$

To verify globality, the limiting constraint (10) is the halfspace
`4p_A+p_B>=8/3`. Since A has four times the deadline benefit per unit upkeep,
every minimum first saturates A at `1/2`, then sets B to `2/3`, costing
`7/6`. More explicitly, the constraint gives
`p_A+p_B>=8/3-3p_A>=7/6`, with equality only at the displayed point.

For the original oracle, every state with `p_B<1` satisfies the same
inequality (10), including states with A full at time zero, and hence costs
at least `7/6` if ready. A state with B full costs at least one, and `(0,1)`
meets the deadline. Thus `(0,1)` is the unique original minimum. The original
critical target can be maintained using rate one; the limiting contract has
no indefinitely maintainable state at this deadline by the same total-storage
bound used for the original frontier.

Two modules are necessary for a discontinuity subject to finite cold exit.
For one module, finite cold exit requires `s>d`, and the continuous scalar
formula `F(p)=gamma^{-1}log[(s-gamma*p)/(s-d)]` applies through the full
endpoint. A one-module discontinuity is possible only by abandoning the
finite-cold-exit requirement (for example `s=d`, already recorded in pass 13).

## 5. The limiting envelope is not a fixed positive tolerance

Equation (1) allows the deficit to approach zero. If `F_-(p)<H`, continuity
along the deficit path ensures some positive epsilon for which
`F(p^epsilon)<=H`, and hence the same bound for every smaller independent
deficit. If `F_-(p)=H`, no positive epsilon need preserve the exact deadline.
For example, the all-full vector has `F_-=0` when cold exit is finite, while
every positive uniform deficit leaves all modules subfull and requires
strictly positive exit time.

There is nevertheless an exact limiting optimization interpretation for
positive deadlines. Define the fixed-tolerance design cost

$$C_{\epsilon}(H)=\inf\{L(p):F(p^{\epsilon})\leq H\},    \tag{14}$$

with infinity for an empty feasible set. Preparation `p` is the nominal
maintained state; (14) permits a one-time unknown undershoot of at most
epsilon in each coordinate at the request. Equivalently, it must meet the
deadline from every request-time state `z` with
`max(0,p_i-epsilon)<=z_i<=p_i`. This is not a continuous stream of additional
disturbances during normal maintenance or a model of recurrent measurement
errors. The upkeep objective remains that of the maintained state p.

**Proposition 5 (positive-deadline cost limit).** If cold exit is finite and
`H>0`, then

$$\lim_{\epsilon\downarrow0}C_{\epsilon}(H)=C_-(H).     \tag{15}$$

**Proof.** For every fixed epsilon and every p, monotonicity gives
`F_-(p)<=F(p^epsilon)`, so `C_epsilon(H)>=C_-(H)`. Let p minimize (6).
If `F_-(p)<H`, the same p is feasible in (14) for sufficiently small epsilon.
Otherwise `F_-(p)=H>0`, so p is not all-full. Increase every nonfull
coordinate by an arbitrarily small positive amount within its bound. For
each strict permutation, its final time in (3) strictly decreases: a changed
coordinate strictly advances its own stage, and every subsequent recurrence
is strictly increasing in the preceding time. In particular an order
attaining `F_-(p)=H` becomes strictly faster. Thus the perturbed state q has
`F_-(q)<H` with `L(q)` arbitrarily close to `L(p)`, and q is feasible for all
sufficiently small positive epsilons. This gives the matching upper limit.

At `H=0`, every positive-deficit problem is infeasible, whereas
`C_-(0)=sum_i d_i` in the finite-cold-exit case. The hypothesis `H>0` is
therefore essential. Even for positive deadlines, (15) states convergence
of costs, not equality at a specified positive precision and not attainment
of the zero-deficit optimum by a device with finite preparation resolution.

Combining (8) and (15), if `C(H)<s` and `H>0`, a sufficiently small positive
epsilon has `C_epsilon(H)<s`. Thus some positive normal optional rate survives
an actual positive request-time tolerance. Its optimal rate can decrease at
positive epsilon; only its limit is the original `s-C(H)`.

**Lemma 6 (ordinary positive-precision maintenance margin).** Let
`gamma_min=min_i gamma_i`. Whenever `C(H)>0` and epsilon is positive,

$$C_{\epsilon}(H)\geq C(H)+\gamma_{\min}\epsilon.        \tag{16}$$

This includes an infinite left side when the fixed-tolerance problem is
infeasible. Consequently every originally critical instance `C(H)=s>0`
loses indefinitely maintainable readiness under any positive request-time
deficit allowance as defined in (14).

**Proof.** For any feasible nominal state p, put `q=(p-epsilon)_+`.
Since q meets the original deadline, `L(q)>=C(H)>0`. Some coordinate q_i
is therefore positive, and for that coordinate `p_i=q_i+epsilon`.
Every other coordinate satisfies `p_j>=q_j`, so
`L(p)-L(q)>=gamma_i*epsilon>=gamma_min*epsilon`. Taking the infimum over
feasible p proves (16). At `C(H)=s>0`, (16) places the entire
fixed-tolerance ready set at upkeep strictly above the normal budget; the
total-storage bound excludes every indefinitely ready normal policy.

This elementary margin obstruction is general and is not a special feature
of the example below. The example's substantive endpoint effect is the
nonvanishing jump as epsilon tends to zero, rather than the loss of exact
critical feasibility at positive epsilon itself.

For the critical fixture (9)--(12), the fixed-tolerance cost is itself exact:

$$C_{\epsilon}(H)=
\begin{cases}
\tfrac76+5\epsilon,&0<\epsilon\leq\tfrac1{15},\\
+\infty,&\epsilon>\tfrac1{15}.
\end{cases}                                             \tag{17}$$

For the finite branch the unique minimizing nominal state is

$$p_A=\tfrac12,\qquad p_B=\tfrac23+5\epsilon.            \tag{18}$$

Indeed put `q=(p-epsilon)_+`. Every q is subfull and the deadline condition
is `4q_A+q_B>=8/3`. Both coordinates must be positive: either coordinate
alone has maximum weighted contribution strictly below `8/3`. Therefore
`L(p)=q_A+q_B+2epsilon`. As before, allocate preparation to A first, giving
`q_A=1/2-epsilon` and `q_B=2/3+4epsilon`. The latter satisfies the nominal
upper bound `q_B<=1-epsilon` exactly when `epsilon<=1/15`, proving the finite
branch. At epsilon greater than `1/15`, the maximal nominal state is already
infeasible: at the threshold its worst-corner weighted preparation equals
`8/3`, and it strictly decreases for larger epsilon until both coordinates
vanish. Monotonicity rules out every other nominal state. This is a genuine
nonvanishing critical cost jump under arbitrarily small positive tolerance,
not merely a mismatch at the zero-deadline endpoint.

## 6. Research consequence

Exact-full endpoints can affect qualitative feasibility, not merely numerical
conditioning. The two-module example proves this inside a finite-cold-exit
system and at a positive deadline, with an upkeep jump of `1/6` that does not
vanish with the tolerance. Loss of exact critical feasibility at positive
tolerance alone is the general elementary margin obstruction in Lemma 6,
not a distinctive consequence of this endpoint example. At the same time
the discontinuity has a sharp operational restriction: positive optional
slack protects the original minimum against the one-sided limiting envelope,
and every maintainable limiting minimum still concentrates. A fixed positive
preparation tolerance requires its own margin; its optimal cost approaches
this envelope for every positive deadline.

These conclusions add a sensitivity boundary to the existing mathematical
package. They do not establish an experimental resolution scale, alter the
instantaneous-transfer convention, claim novelty against a new body of
literature, or settle concentration above the normal maintenance budget.
