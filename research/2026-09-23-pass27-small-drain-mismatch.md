# Pass 27: arbitrarily small drain mismatch can defeat concentration

23 September 2026. Repository research only. This family refines the
[pass-25 residual-drain counterexample](2026-09-23-pass25-proportional-drain.md).
All physical parameters and the removal deadline stay fixed except the two
drain durations. Their positive difference can be arbitrarily small, while
the unique minimum-upkeep state has two partial coordinates. A positive
request-time tolerance and positive normal upkeep slack persist for every
member, but both vanish in the common-drain limit. The cost advantage over
concentrated states also vanishes. This is not instability near a fixed
common-drain instance with a positive preparation window.

## 1. Interface and parameter family

Use the full pass-25 interface: preparation loss is proportional until
ownership handoff, then stops; immutable drains retain their source
reservations until they end. Before a request there are no handoffs. All
coordinatewise loss histories `0<=rho_i<=gamma_i*p_i` are jointly allowed,
including simultaneous maximal feedback. Controls are bounded, measurable
and causal, with no impulses; preparation is upper-reflected at its cap.
The receiver independently serves new essential work after handoff. The
deadline requires both drains, not just both preparation phases, to finish.

Fix any positive released rates `a_A,a_B` and

$$s=4,\qquad \gamma=(2,1),\qquad M=(1/2,3),\qquad H=\log10.$$

For `1<y<=11/10`, set

$$h_A=\log y,\quad h_B=4\log y,\qquad
\ell_A=H-h_A,\quad\ell_B=H-h_B. \tag{1}$$

These are positive drains and `0<h_A<h_B<ell_B<ell_A`, because
`y^8<10`. Thus no drain can finish before either required handoff, even if
it starts at time zero. Every feasible preparation policy has capacity four
throughout its handoff interval, independent of the positive release rates.

Define the candidate effective preparation and its upkeep by

$$q_A^*=\frac{4-3y^2}{2},\qquad q_B^*=4y-y^4,
\qquad C=4-3y^2+4y-y^4. \tag{2}$$

Both coordinates are partial. Indeed, `1<y^2<=121/100<4/3` gives
`0<q_A^*<1/2`; also `q_B^*>4-y^4>0`, while

$$g_B:=3-q_B^*=y^4-4y+3=(y-1)^2(y^2+2y+3)>0. \tag{3}$$

Write `g_A=1/2-q_A^*=3(y^2-1)/2`. Then `C=4-2g_A-g_B<4`.

## 2. Lower bounds over every exit policy

Take any actually robustly ready initial state x and follow its guaranteed
policy on simultaneous maximal loss. Let its handoff times satisfy
`0<=t_A<=h_A`, `0<=t_B<=h_B`. Initial-full, held-full, simultaneous,
parallel and interrupted policies are included. Before handoff, discarded
allocation at the upper cap is a nonnegative function w_i. Integration gives

$$x_i=M_i e^{\gamma_i t_i}
-\int_0^{t_i}e^{\gamma_i t}v_i(t)\,dt
+\int_0^{t_i}e^{\gamma_i t}w_i(t)\,dt. \tag{4}$$

This identity also holds at zero handoff time. Dropping the reflected-waste
term preserves a lower bound. The discounted upkeep weights satisfy
`2*exp(2t)>exp(t)` for every nonnegative time.

If A hands off first, the shared budget bounds weighted input by `8*exp(2t)`
before t_A and by `4*exp(t)` between t_A and t_B. Hence

$$L(x)=2x_A+x_B\ge W(t_A,t_B)
=4-3e^{2t_A}+4e^{t_A}-e^{t_B}. \tag{5}$$

Both partial derivatives are strictly negative:
`W_A=2*exp(t_A)*(2-3*exp(t_A))<0`, `W_B=-exp(t_B)<0`.
Thus `L(x)>=W(h_A,h_B)=C`.

If B hands off no later than A, bound all weighted input until t_A by
`8*exp(2t)`: A's weight dominates while both are available, and only A
remains after B hands off. Equation (4) then gives

$$L(x)\ge4-3e^{2t_A}+3e^{t_B}
\ge7-3y^2=:G. \tag{6}$$

The last bound uses `t_A<=h_A` and `t_B>=0`. Its gap is
`G-C=y^4-4y+3=g_B>0`. These two cases exhaust all policies, without assuming
serial optimality. The discounted-input bounds are ordinary linear
allocation certificates, not a new duality theorem.

## 3. Attainment, robustness and uniqueness

Start at (2), give rate four to A until h_A, hand it off, then give rate four
to B until h_B and hand it off. On maximal loss,

$$p_A(h_A)=2+(q_A^*-2)e^{-2h_A}=1/2,
\qquad p_B(h_B)=q_B^*e^{-h_B}+4(1-e^{-(h_B-h_A)})=3.$$

A increases to its cap. B first decays, then increases to its cap; its
growth rate after A's handoff is `4-p_B>=1` inside the box. Both drains
finish exactly at H. Under smaller losses, scalar comparison keeps states
above these virtual trajectories. Scheduled rate four holds any early full
coordinate at its cap until its planned handoff, since it exceeds both full
loss rates. Thus the same schedule is robust.

Equality in (6) cannot yield the global minimum C. Equality in (5) forces
both handoff deadlines to be tight, all input to A before h_A and to B
afterward, and no reflected waste on maximal loss. The strict difference
between discounted weights excludes sharing during A's phase. Equation (4)
then uniquely determines the initial state (2). Consequently C is the
attained global minimum and q* its unique minimizing state.

## 4. Exact penalty for concentrated states at zero deficit

Individual input bounds in (4) imply, for every ready initial state,

$$x_A\ge\frac{4-3y^2}{2}>0,\qquad x_B\ge4-y^4>0. \tag{7}$$

Neither coordinate can be cold. A concentrated state therefore has at least
one full coordinate. If B is full, (7) gives upkeep at least
`3+2*q_A^*=G`; attain it by handing off B at zero and preparing A at rate
four until h_A. If A is full, (7) gives upkeep at least `5-y^4`; attain it
by handing off A at zero and preparing B at rate four until h_B. Neither
construction uses a released reservation. Since

$$G-(5-y^4)=(y^2-1)(y^2-2)<0,$$

the exact best concentrated upkeep is G. Its excess over unrestricted
upkeep is exactly g_B. This comparison concerns zero request-time deficit;
it is not asserted to be the concentration penalty at positive tolerance.

## 5. Positive request-time tolerance and finite normal startup

Use the same one-time deficit contract as pass 18: a nominal state p must
be ready from every request state between `(p-epsilon)_+` and p. Its worst
corner q obeys (7), so both effective coordinates are positive and
`p_i=q_i+epsilon`. Every feasible nominal state has
`L(p)=L(q)+3*epsilon>=C+3*epsilon`.

The smaller cap margin is g_B. Indeed,

$$2(g_A-g_B)=(y-1)(9+y-2y^2-2y^3)>0, \tag{8}$$

because the bracket is at least
`10-2*(11/10)^2-2*(11/10)^3=2459/500>0`. Therefore

$$C_\epsilon^{\rm drain}(H)=C+3\epsilon,
\qquad 0\le\epsilon\le g_B, \tag{9}$$

with unique nominal minimum `p=q*+(epsilon,epsilon)`. Both nominal
coordinates are partial for `0<=epsilon<g_B`; at `epsilon=g_B`, B is full.
Comparison with the same planned schedule proves readiness for every
request state above its worst corner q*.
The maximum upkeep in (9) is `C+3g_B=4-2(g_A-g_B)<4`.
For `epsilon>g_B` the optimum may change. Equation (9) makes no feasibility
or value claim there; B's cap binding at the old optimum does not establish
infeasibility of all other effective states.

Every nominal minimum on (9) admits finite cold normal warmup. For such a
target p, put `K=L(p)<4` and `Q=p_A+p_B>0`. The virtual path `theta*p` with

$$\theta'=(4-K\theta)/Q,\quad\theta(0)=0,
\qquad v_i=p_i(\theta'+\gamma_i\theta)$$

uses exactly capacity four and reaches theta=1 at
`T=(Q/K)*log(4/(4-K))<infinity`, within all preparation caps. Reflected
comparison guarantees domination under smaller losses. Thereafter allocations
`v_i=gamma_i*p_i` preserve domination and leave optional rate `4-K>0`.
No handoff occurs during warmup; the removal guarantee begins after it.

## 6. Small mismatch and the collapsing limit

The drain difference is `delta=ell_A-ell_B=3*log y`. For every positive
absolute mismatch bound, choose y sufficiently close to one so that delta
is below it, and choose, for example, `epsilon=g_B/2>0`. This gives a
unique two-partial nominal optimum with positive normal slack. There is
therefore no uniform positive absolute mismatch threshold guaranteeing
concentration across this family, even with all non-drain parameters fixed.

The scale of this conclusion matters. Writing `eta=y-1`, exact expansions
give

$$g_B=6\eta^2+4\eta^3+\eta^4,
\qquad4-C=6\eta+9\eta^2+4\eta^3+\eta^4.$$

As y decreases to one, both drains tend to H and both handoff windows tend
to zero; their ratio `h_B/h_A` remains four. The limiting state is fully
prepared and has upkeep four. The
admissible tolerance, optional capacity and concentration penalty vanish.
In particular,

$$\lim_{y\downarrow1}\frac{G-C}{(\ell_A-\ell_B)^2}
=\lim_{\eta\downarrow0}\frac{6\eta^2+4\eta^3+\eta^4}
 {9\log(1+\eta)^2}=\frac23.$$

This is an asymptotic limit, not a uniform finite-mismatch inequality or a
constant positive advantage. The family does not show local instability
near a fixed common drain with positive preparation time, nor preservation
of a fixed positive tolerance as mismatch vanishes. It records a precise
boundary to a uniform extension of concentration. Its elementary allocation
certificates and delivery-deadline mechanism are not claimed as a new central
result or as novelty against the scheduling literature.
