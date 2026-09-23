# Pass 23: viability and capture-basin comparison

23 September 2026. Repository research only. This note compares the exact
pass-15 question with two primary results; it does not certify novelty.
The comparison uses the full [critical-startup proof](2026-09-22-pass14-critical-startup.md),
[critical-viability proof](2026-09-22-pass15-critical-viability.md),
[two-module companion](2026-09-22-pass15-two-module-boundary.md), and
[pass-23 opening](2026-09-23-pass23-viability-opening.md).

## 1. The exact comparison target

The symbols below distinguish the physical box X, deadline region R, its
minimum-upkeep set K, and the region A of states dominating a minimum.
They must not be collapsed into a single target.

| Item | S1 quantity and quantifier | Required comparison |
|---|---|---|
| Normal dynamics | Reflected `p_i'=v_i-rho_i`, `0<=rho_i<=gamma_i*p_i` | Existence under maximal loss versus one policy for every allowed loss |
| Normal controls | Measurable `v_i>=0`, `sum v_i<=s`; optional work can be zero | No module transfer or source-capacity release before a request |
| Physical constraint | `X=product_i[0,M_i]` | State constraints continue throughout warmup |
| Deadline region | Closed upward set `R={p:F(p)<=H}` | F is the all-policy post-request exit time, with releases after instantaneous transfers |
| Initial state | `p(0)=0` | A finite warmup may lie outside R; the deadline guarantee begins afterward |
| Critical budget | `min_R L=s>0`, `L(p)=sum gamma_i*p_i` | Same s funds the warmup and indefinite subsequent normal operation |
| Viable entry | Finite cold entry followed by membership in R forever | Capture of the viability kernel of R |
| Minimum domination | Finite cold entry into `A={p in X: p>=k for some k in K}`, `K=argmin_R L` | Capture of A, followed by maintaining domination |
| Dimension boundary | At most two modules versus a three-module counterexample; finite cold post-request exit | Equivalence of two **cold-state membership questions**, not equality of entire basins |
| Precision | Every fixed positive request-time deficit raises critical nominal upkeep above s | The exact critical separation is not a finite-precision operational benefit |

The last row is the [pass-18 precision result](2026-09-22-pass18-precision.md),
not a condition supplied by the sources below. A smooth prescribed safe set
cannot automatically replace the schedule-generated R in the dimension claim.

## 2. Exact reduction of normal operation

Let `Gamma=diag(gamma_i)` and `U={v>=0:sum v_i<=s}`. Use the ordinary
Lipschitz affine control system

$$\dot p=v-\Gamma p,\qquad v\in U,$$

with trajectories constrained to X. This represents the maximal-loss
reflected model exactly at the level of admissible state paths. To see this,
take a reflected path and replace its allocation, almost everywhere, by

$$\widetilde v_i=
\begin{cases}
v_i,&p_i<M_i,\\
\min\{v_i,\gamma_iM_i\},&p_i=M_i.
\end{cases}$$

The new input is measurable, nonnegative and no more costly; it satisfies
`p_i'=tilde v_i-gamma_i*p_i`. Conversely, an unreflected admissible path
remaining in X has no positive outward derivative at an upper cap except
possibly on a null set. Applying upper reflection therefore preserves that
path. The lower endpoint needs no reflection because controls are
nonnegative and proportional loss vanishes there.

Write `V=Viab(R)` for this maximal-loss system. Then robust finite cold
entry into indefinite readiness is equivalent to

$$0\in\operatorname{Capt}(X,V). \tag{1}$$

The forward implication takes the admissible simultaneous maximal-loss
history of a robust policy. After its finite warmup its continuation proves
membership in V. For the reverse implication, concatenate the finite capture
path with a viable path. Run its measurable allocations as a predetermined
normal schedule. Under every smaller admissible loss, scalar comparison,
including upper reflection, keeps the actual state at least the virtual
maximal-loss state. Upward closure of R proves the deadline guarantee at
every subsequent request time. This is an exact reduction for the existence
question; it is not a theorem that arbitrary feedback policies have identical
paths under different losses.

Similarly, robust finite domination of some minimum is equivalent to

$$0\in\operatorname{Capt}(X,A). \tag{2}$$

Indeed, maximal loss gives necessity. A finite maximal-loss capture path
gives a robust schedule by comparison. On reaching a state above `k in K`,
the constant allocation `v_i=gamma_i*k_i` has total cost s and preserves
domination for every loss history. Thus `A` is contained in V, and (2)
always implies (1).

The pass-15 statements now have a precise standard-language form:

- In the stated two-module, finite-cold-exit domain, (1) implies (2).
- The three-module instance has (1) and fails (2), even though K is a singleton.

Neither statement asserts `V=A` or equality of their capture basins for all
initial states. The reduction packages the question; it does not solve the
schedule-dependent membership test.

## 3. Primary-source results actually inspected

### Aubin and Catté: the general set-theoretic framework

Jean-Pierre Aubin and Francine Catté, *Bilateral Fixed-Points and Algebraic
Properties of Viability Kernels and Capture Basins of Sets*, Set-Valued
Analysis 10(4), 379–416 (2002),
[DOI 10.1023/A:1020667819804](https://doi.org/10.1023/A:1020667819804).
Inspected the [author-uploaded full manuscript](https://www.researchgate.net/publication/226141319_Bilateral_Fixed-Points_and_Algebraic_Properties_of_Viability_Kernels_and_Capture_Basins_of_Sets):
Section 2.1, Lemma 2.2 and Proposition 2.3 with proof; Sections 3.1–3.3,
Definitions 3.1–3.2, Theorem 3.3 with complete proof, and Lemma 3.4 with
complete proof (manuscript pages 5–7 and 11–15).

The framework assumes solution families with initial-state, translation and
concatenation properties. It distinguishes indefinite viability from finite
capture. Theorem 3.3 characterizes viability/capture maps by bilateral fixed
points; its proof uses translation for continued viability and concatenation
for capture closure. Lemma 3.4 expresses finite capture through a trajectory
and a finite hitting time. These results apply to the normal solution family
above. They justify its vocabulary and closure operations, not a finite-time
arrival conclusion from asymptotic convergence. No upkeep, scheduling,
minimizer-concentration or two-versus-three-dimensional hypothesis appears
in this inspected result.

### Broucke and Turriff: finite termination is an additional construction

Mireille E. Broucke and John Turriff, *Viability Kernels for Nonlinear Control
Systems Using Bang Controls* (2010),
[DOI 10.1109/TAC.2010.2042657](https://doi.org/10.1109/TAC.2010.2042657).
Inspected the [author manuscript, revised 28 January 2010](https://www.control.utoronto.ca/~broucke/Webpapers/BroTur10.pdf):
Sections II–III, Assumptions 1, 4 and 7, Lemmas 10 and 13–15, Proposition 12,
and Theorems 17–18 with their complete printed proofs (pages 1–5).

The source constructs finite capture of a selected viability core for smooth
control-affine systems with polyhedral input constraints. Its assumptions
include a smooth safe-set submersion h, relative degree at least two,
continued safety from the target, continuity/closedness of the constructed
set, and a backward tangency condition. Theorem 17 treats bang-bang inputs;
Theorem 18 extends the same construction to measurable inputs. The proofs
establish target capture and backward invariance, checking the boundary
cases and then the convexified input directions. They do not infer finite
arrival at an arbitrary cost-minimizing equilibrium from viability alone.

For S1's direct affine representation, `g=I`. Consequently `L_g h=grad h`
cannot vanish for a smooth submersion, whereas Assumption 1 requires it to
vanish. This explicit hypothesis failure already excludes a direct
application, even on a smooth interior piece of the deadline boundary.
It is not a counterexample to their theorem or an exclusion of every
possible reformulation.
In particular, restricting controls to an always-saturated allocation face
reduces their affine dimension, while adding actuator dynamics can change
relative degree. Neither modification is analyzed here as a reduction of the
full S1 policy class.

### Access and scope limits

The requested PDF endpoint for Aubin's earlier *Viability Kernels and Capture
Basins of Sets Under Differential Inclusions*,
[DOI 10.1137/S036301290036968X](https://doi.org/10.1137/S036301290036968X),
redirected to an abstract/access page. Its full proof was **not** inspected
and no theorem-level nonoverlap claim is made for it. The audit stops at the
two results above rather than treating an inaccessible paper as absent.
No third-party paper was added to the repository.

## 4. A two-module control example with an arbitrary upward region

This is an internal deduction, not a result attributed to either source.
It keeps S1's normal dynamics and positive upkeep but substitutes a prescribed
region for the post-request scheduling contract. It is therefore **not an S1
deadline instance**.

Take

$$s=1,\qquad \Gamma=\operatorname{diag}(2,1/2),\qquad
X=[0,1]\times[0,1/2],$$

and prescribe the closed upward region

$$\widehat R=\{p\in X:p_1+\tfrac14p_2^2\geq\tfrac12\}.$$

Its defining function has nonzero gradient throughout X. Use the same
positive upkeep as the dynamics, `L=2*p_1+p_2/2`. At fixed `p_2`, the
least permissible first coordinate is `1/2-p_2^2/4`, so every member satisfies

$$L(p)\geq1+\frac{p_2-p_2^2}{2}\geq1.$$

Because `0<=p_2<=1/2`, equality requires `p_2=0` and `p_1=1/2`.
Thus the unique minimum is `p^*=(1/2,0)` and its upkeep is exactly s.

No finite normal policy starting cold can robustly dominate this minimum.
On the admissible maximal-loss history, every allocation satisfies

$$\dot p_1\leq1-2p_1,\qquad
p_1(t)\leq\tfrac12(1-e^{-2t})<\tfrac12$$

at every finite time. This argument covers all parallel, preemptive and
adaptive controls; it is not just a failure of the construction below.

Nevertheless finite robust entry into indefinite membership in `R-hat` is
possible. Allocate `(0,1)` for `T_0=2*log(8/7)`. The maximal-loss state
becomes `(0,1/4)`, without touching either upper cap. Thereafter use the
constant allocation `(1,0)`. At elapsed time t the virtual state is

$$p_1(t)=\tfrac12(1-e^{-2t}),\qquad
p_2(t)=\tfrac14e^{-t/2}.$$

It remains inside X and obeys

$$p_1(t)+\tfrac14p_2(t)^2-\tfrac12
=-\tfrac12e^{-2t}+\tfrac1{64}e^{-t}\geq0
\quad\Longleftrightarrow\quad t\geq\log32.$$

After total warmup `2*log(8/7)+log32` it stays in the prescribed region
forever, converges to the unique minimum, and never dominates it in finite
time. Predetermined inputs plus scalar comparison prove the same region
membership for every smaller admissible loss, because the region is upward
closed. No normal capacity release occurs.

This example sharpens the scalar opening: neither positive diagonal
dynamics, a positive linear upkeep linked to the loss coefficients, a
smooth upward constraint, a unique concentrated optimum, nor a shared
source simplex is sufficient for the S1 two-module implication. Its proof
must use restrictions on the region generated by post-request scheduling.
In the S1 companion, the relevant missing restriction is precisely the
coefficient ordering forced on a cold predecessor of a partial optimum.
Here the cold reserve has coefficient `1/2`, smaller than the partial
optimum's coefficient 2; the arbitrary region imposes no scheduling
restriction forbidding it.

## 5. What remains after the reductions

The abstract distinction between viability and finite capture is standard.
The [scalar opening](2026-09-23-pass23-viability-opening.md) independently
shows why critical dissipation and convergence do not remove that distinction.
Likewise, the pass-15 convergence argument uses only bounded-state
dissipation, uniform continuity and a finite minimizing set. Its final
single-point conclusion adds the elementary fact that a continuous path
cannot keep switching among separated neighborhoods while its distance to
their finite union tends to zero. No new general convergence principle
should be claimed.

The unresolved attribution target is therefore narrow: the exact
schedule-generated R, positive linear upkeep tied to the decay coefficients,
and source simplex produce a cold-start implication in two modules that
fails in three. The two inspected results neither imply nor refute that
dimension threshold without doing additional S1 geometry. This is a scoped
nonreduction finding, not evidence sufficient to claim priority or significance.

The three-module construction itself can be recorded as a useful warning:
checking only finite access to cheapest stationary states can miss a feasible
transient readiness policy. Its guaranteed margin tends to zero, and every
fixed positive preparation deficit defeats indefinite readiness at the same
critical source budget. It should remain an ideal exact-model boundary,
not the main operational sales claim.

The control example isolates the dependence on the scheduling-generated
region, but does not establish the importance of that dependence. Before
expanding this into a general viability solver or more coefficient
classifications, assess whether the exact-model warning remains a useful
central contribution once the fixed-positive-deficit limitation is stated.
If it does not, retain it as a boundary finding and return to a defensible
independent-fallback interface and the positive-slack regime. Scientific
priority and operational meaning remain unresolved.
