# Pass 15: what the proportional-loss concentration theorem can mean

22 September 2026, continuing from
`bb1e34f41338745c88ae486d493a053c658fb3d1`. This is an internal operational
and assumption audit of the focused theorem candidate. It is not a deployment
validation, a new physical model, or an external referee report. The full
pass-6 interface, pass-8 pipeline, pass-11 concentration, and pass-12 frontier
notes were read for this assessment.

## 1. Assessment

The proportional law need not be justified by random data updates. A
deterministically leaky activation reserve supplies a coherent ideal
interpretation: several independent receivers need a threshold amount of
preparation before taking over their respective essential loads; a common
source maintains the reserves and can accelerate preparation after a removal
request. Each completed takeover releases source capacity.

The mathematical information is then concrete. Among all readiness vectors
that permit every receiver to take over by a specified deadline, **every
minimum-maintenance vector has at most one partly prepared receiver**, even
when leakage coefficients differ. Every other receiver is fully prepared or
cold. Unequal leakage can make a cold receiver worth activating before the
partly prepared one. These are statements about allocating standby resources,
not merely the observation that maintenance consumes capacity.

This supports a focused paper about an ideal scheduling and readiness class.
It does not establish that the model is an exact description of replicated
software, practical power generation, or arbitrary controller withdrawal.
The scalar loss law is credible as an idealization; the stronger unresolved
engineering burden is the complete threshold-to-autonomy interface. A paper
can state that interface as its model, explain the consequences and boundaries,
and assess novelty within it without inventing a requirement for a large
simulation or an equipment demonstration.

## 2. A deterministic reserve interpretation

Consider a receiver with a lumped thermal activation reserve. Let its heat
capacity be `c_i>0`, its fixed ambient temperature be `T_0`, and its thermal
conductance to that ambient be `k_i>0`. Suppose the ideal preactivation heat
balance is

$$c_i\dot T_i=\eta_i v_i-k_i(T_i-T_0),\qquad \eta_i>0,$$

where `v_i` is electrical heating power and `eta_i` is a constant conversion
factor. Define preparation in equivalent source-energy units,

$$p_i=\frac{c_i(T_i-T_0)}{\eta_i},\qquad
\gamma_i=\frac{k_i}{c_i},\qquad
M_i=\frac{c_i(T_i^*-T_0)}{\eta_i}.$$

For `0<=p_i<=M_i`, the balance becomes exactly

$$\dot p_i=v_i-\gamma_i p_i.                              \tag{1}$$

This is an algebraic deduction from the displayed ideal heat balance.
Different heat capacities, conductances, and efficiencies are compatible
with the theorem's unequal coefficients and common input budget. The
maintenance power at a target `p_i` is `gamma_i*p_i`.

Constant ambient conditions, a scalar temperature state, constant coefficients,
and the displayed heat-transfer law are assumptions. Radiation, spatial
temperature gradients, coupled cooling, temperature-dependent conversion,
and thermal ramp limits need not satisfy them. Equation (1) is not presented
as an exact empirical law for all equipment. The linear leaky-stock equation
itself is established storage modeling: Flatley, MacKay, and Waterson use it
in their continuous-time storage model, with explicitly separate input and
conversion accounting [1].

To obtain S1's service interpretation, more than (1) is required. An ideal
receiver must, on reaching `T_i^*`, be able to begin independently sustained
operation. For example, activation could enable a separately fuelled process
whose own operation supports subsequent thermal losses. The preparation loss
does **not** have to physically vanish after takeover: it must cease to demand
the removable source's resource. The receiver's fuel, auxiliaries, controls,
actuation, and continuing supply must be separately provisioned for the
essential-service horizon. A finite warm reserve alone does not provide
indefinite essential service.

Thermally self-sustaining fuel-cell operation is an existence example for the
distinction between activation and subsequent heat supply [2]. The material
inspected does not validate our linear preactivation equation, a single exact
activation threshold, negligible startup delay, or the shared-resource
architecture below. It is a physical motivation for investigating the
interface, not a claimed instantiation of the theorem.

## 3. The complete conditional service class

A simple ideal service contract is uninterrupted delivery of specified loads
by either the primary or their independent receivers. Suppose the primary
has resource capacity

$$P=s+\sum_i a_i.$$

Until receiver `i` takes over, its essential load consumes the primary's
reserved rate `a_i`. Normal optional use `u` and activation allocations share
the residual budget `s`. When a set `C` has taken over, the same accounting
gives

$$P-\sum_{i\notin C}a_i=s+\sum_{i\in C}a_i=b(C).           \tag{2}$$

For a power illustration, all rates in (2) are power, the optional use is an
auxiliary load, and `p_i` and `M_i` have source-energy units. This avoids mixing
copying bandwidth with electrical power or counting the receiver's fuel as
free primary capacity. A different common resource is possible only with a
similarly explicit accounting identity.

The ideal interface must additionally specify all of the following.

| Interface condition | Role in the theorem |
| --- | --- |
| Preparation is completely summarized by the independent scalar `p_i`; below `M_i` the receiver cannot yet take over under the declared contract. | Defines the state and the completion barrier; hidden ready state or another activation path can invalidate a lower bound. |
| At `M_i`, transfer is instantaneous and maintains the original essential service; the receiver then needs no source resource. | Justifies zero completion tail and the immediate release in (2). |
| The primary continues essential service throughout preparation. | The grace period is cooperative withdrawal, not survival of an immediate primary failure. |
| Before a removal request, ownership remains with the primary; receivers are maintained in standby. | Defines the normal operating problem and prevents prior permanent transfer from changing its recurring objective. |
| Every untransferred receiver can accept the available common preparation rate; there are no additional rate, ramp, switching, or coupling constraints. | Makes the serial dominance proof and its attaining schedules applicable. |
| Independent maximum losses can occur together, or the simultaneous deterministic maximal law is itself an allowed history. | Makes the robust lower bound valid, in addition to comparison-based upper bounds. |
| Initialization and independent receiver operation are paid separately. | Prevents free initial preparation or hidden continuation capacity from being attributed to the source budget. |

Under this interface, loss histories and admissible allocations are precisely
those of passes 9, 11, and 12, and each transfer preserves its corresponding
essential load. Induction over transfers preserves all loads and yields the
capacity identity (2). Completion of all modules therefore permits source
withdrawal with the stated service intact. This is a conditional model
interpretation, not a deduction of the interface from a heat balance.

Normal ownership retention is a policy-domain restriction inherited from
the research problem. It is not a universal engineering fact. If early
permanent activation is desirable and admissible, its operating costs and
service consequences belong in the optimization. A source-maintenance
optimum for standby receivers cannot answer that expanded problem.

## 4. Exactness and conservative use must be separated

Suppose actual preactivation losses satisfy the certified bound

$$0\leq\rho_i(t)\leq\gamma_i p_i(t).$$

With the rest of the interface unchanged, a policy designed for simultaneous
maximal loss gives a guaranteed deadline and a feasible maintenance allocation.
The comparison argument needs no stochastic independence. If simultaneous
maximal loss is also an admissible realization, the matching lower bound is
available and the ideal model's frontier is exact for that uncertainty class.

If instead `gamma_i*p_i` merely bounds a smaller physical loss family, the
concentrated construction is a **sufficient conservative design**. It does not
prove that the equipment's true optimum has at most one partial reserve,
nor that its actual recurring cost must equal `C(H)`. The same distinction
applies when `M_i` is a sufficient safe activation threshold but not a
necessary one. Replacing an exact law or necessary threshold by a convenient
upper bound preserves some guarantees and can destroy optimality claims.

The nonlinear counterexample in
[pass 10, section 9](2026-09-22-pass10-proportional-frontier.md) is material
here: smooth identical losses `g(p)=p^2` admit a cheaper two-partial readiness
state than every concentrated state. Proportionality is a structural
hypothesis, not a harmless numerical fit. Likewise, an unproved small-delay
approximation cannot justify an exact all-request-time endpoint.

## 5. Two tempting interpretations that fail

**Random replica updates.** Uniform update locations can produce proportional
expected invalidation. They do not impose the theorem's pathwise loss bound.
Finite updates can destroy a positive chunk instantly; positive delivery
delay also creates independent in-flight state. The
[pass-6 interface audit](2026-09-22-pass6-interface.md) rules out using that
expectation as a proof of this robust model.

**An already powered independent maintainer.** If the receiver already has
an independent supply capable of maintaining its activation reserve before
handover, and using that supply is admissible without another charged cost,
then source expenditure `gamma_i*p_i` need not be required. The exact
source-cost interpretation fails. A thermal illustration must explain why
the source is needed for preactivation and how independent continuation
becomes possible, or include the alternative supply in its policy class.
Merely declaring it usable only after transfer would not validate a proposed
real application.

The same principle applies to turning off loss through an earlier admissible
action. The
[pass-8 pipeline audit](2026-09-22-pass8-pipeline-policy.md) found that earlier
freeze can remove a copying benchmark's restart cost while preserving its
declared response contract. This warning is about admissible controls, not
only communication delay. Free insulation, independent preheating, early
activation, logging, or service from another path must not be excluded from a
claimed implementation-independent lower bound solely to preserve a formula.

## 6. Consequences for the focused paper

The defensible central claim is a concentration theorem for a specified
class of leaky preparation and capacity-releasing completion systems. Its
explicit unequal-rate frontier and nonlinear failure show what the structure
buys and where it stops. They are stronger and clearer than a universal
claim about the cost of safe controller removal.

An introductory physical-reserve example can explain the state and units,
followed immediately by the full service interface and exactness distinction.
The abstract should not advertise an implemented migration protocol or a
universal shutdown law. The theorem does not require stochastic update
assumptions, a named equipment deployment, or numerical performance evidence
to be mathematically meaningful. The remaining scientific questions are its
distinction from the closest scheduling results and whether the ideal
interface is useful enough to the intended theory audience. This note does
not settle that novelty or venue judgment.

## 7. Source inspection record

1. **Flatley, MacKay, and Waterson (2016), _Optimal strategies for operating
   energy storage in an arbitrage or smoothing market_.**
   [Author-accepted manuscript, Warwick repository](https://wrap.warwick.ac.uk/id/eprint/82131/3/WRAP_8779629-ec-111016-mike_w_storageoperation10c_5.pdf).
   Inspected full section 1.1, equations (1)–(3), printed pp. 3–4, and
   Proposition 2.1 with its proof, printed pp. 5–6. Equation (1) uses
   deterministic linear stock leakage and an additive input rate; input
   conversion costs are separately accounted for. The inspected optimization
   concerns one store, exogenous time horizon and capacity constraints, and a
   cost functional. It supplies precedent for the scalar reserve model, not
   a physical validation or a reduction of our concentration result. No
   absence-of-prior-art conclusion follows from this limited comparison.
2. **Shao et al. (2005), _A thermally self-sustained micro solid-oxide fuel-cell
   stack with high power density_, Nature 435, 795–798,
   doi:10.1038/nature03673.**
   [Publisher record](https://www.nature.com/articles/nature03673),
   [author institutional record](https://authors.library.caltech.edu/records/jnp8z-1eq58).
   Inspected the primary abstract and publisher metadata only. They report
   a fuel-fed device whose reactions maintain operating temperature. The
   publisher's full article was not accessible through this retrieval; the
   institutional file links inspected did not yield the article. This is
   explicitly a limited physical lead. No equation, startup guarantee, or
   deployment claim in this note is attributed to unseen full text.

No measurements, simulations, or third-party implementations were reproduced.
No third-party paper was added to the repository.
