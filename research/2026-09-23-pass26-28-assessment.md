# Passes 26–28: a unified concentration boundary

23 September 2026. Repository research only. The earlier manuscript and all
historical records remain unchanged. This assessment follows the full
pass-17 resource/authority audit and the new drain proofs; it does not turn
an ideal scheduling theorem into a universal cost of controller removal.

## 1. The surviving mathematical question

The coherent question is now: **when does minimum recurring upkeep concentrate
preparation, and which forms of heterogeneity can require it to be distributed?**
The variable upkeep price is the same positive coefficient that governs
proportional preparation loss. Preparation competes for a specified common
source resource. Ownership handoff ends preparation demand; an independent
immutable drain may retain the old source reservation before releasing it.

The new results fit one structural argument, rather than independent scheduling
variants:

| Assumptions | Proved preparation structure |
|---|---|
| Instantaneous handoffs/releases, any number of modules and unequal positive coefficients | Every minimum has at most one partial coordinate (existing theorem). |
| Two modules, common positive drain, unequal positive coefficients | Every minimum has at most one partial coordinate, including when released capacity assists later preparation (pass 26). |
| Any finite number of modules, arbitrary positive drains, common positive coefficient | Every minimum has at most one partial coordinate (pass 28). |
| Any finite number, arbitrary positive drains and coefficients | At most one interior partial per distinct coefficient; in normalized maximal-loss witnesses those partials hand off in strictly decreasing coefficient order (pass 28). |
| Two modules, unequal coefficients and unequal drains | A unique two-partial minimum can exist with positive upkeep slack and positive request-time tolerance (passes 25 and 27). |

The preserving statements also hold for the corresponding nominal minimizers
under the specified fixed positive request-time deficit contract. With reduced
design caps, “interior” refers to those caps, not to physical full preparation.
Support charges in the proof encode that precision contract; they do not turn
arbitrary independent investment prices into physical upkeep prices.

Thus joint coefficient and drain heterogeneity is necessary for a two-partial
failure **in the two-module model**, and is sufficient in an explicit example.
For three or more modules with unequal coefficients and a common drain,
concentration remains unresolved. The table is not an all-dimensional
characterization by two yes/no heterogeneity flags.

## 2. Why the all-policy argument matters

The [two-module proof](2026-09-23-pass26-common-drain.md) derives scheduling
structure only at a hypothetical minimum with two interior preparations. It
does not assume or prove serial optimality for every prescribed initial state.
The existing fixed-loss drain counterexamples remain intact.

Its crucial perturbation advances the first full-state handoff of one partial
module, shifts the freed preparation input to another, and offsets both changes
in their initial preparation. If the first module's decay coefficient is no
larger, upkeep strictly decreases. Earlier independent drain completion can
only increase available resource. Other modules can keep their recorded
inputs and handoff times unchanged.

That last observation gives the [general partial-order theorem](2026-09-23-pass28-partial-order.md).
Equal coefficients cannot occur in two interior partials at a minimum.
For unequal coefficients, a separate discounted input exchange prevents a
later partial from receiving input before an earlier partial has handed off.
Cold modules and coordinates on design bounds may still be interleaved.
This does not produce a general serial scheduler or an explicit upkeep oracle.

In the two-module common-drain case, the remaining first-handoff time has
a genuine two-sided feasible variation while the last handoff remains at
the common deadline. A smooth stationary point is a strict maximum and the
release transition has a downward derivative jump. Unequal handoff deadlines
can block that variation, which is exactly what the counterexample uses.

## 3. Small mismatch is a nonuniform boundary, not a fixed robustness margin

The [pass-27 family](2026-09-23-pass27-small-drain-mismatch.md) fixes source
capacity, sizes, coefficients, removal deadline and release rates, varying
only the two drain durations. For any positive absolute mismatch bound there
is a smaller positive mismatch whose unique upkeep minimum is two-partial,
including at some positive preparation tolerance.

However, the family approaches a common drain equal to the entire removal
deadline. Both preparation windows collapse. The exact zero-deficit penalty
for restricting to concentrated preparation is

$$g_B=(y-1)^2(y^2+2y+3),\qquad
\delta=\ell_A-\ell_B=3\log y,\qquad
\frac{g_B}{\delta^2}\longrightarrow\frac23.$$

The certified tolerance and optional operating slack also vanish. No fixed
positive accuracy margin, constant cost advantage, or instability around a
fixed positive preparation window follows. This qualification is essential
to the significance of the small-mismatch result.

## 4. What decision the drain distinction can change

The useful interpretation is a choice of **certified duration bounds**, not a
requirement that physical drain realizations be identical. Suppose independent
immutable drains can take any duration in `[0,ell_i]`, and simultaneous maximum
durations are admissible. The actual robust ready set equals the fixed-duration
model with durations `ell_i`: necessity follows by choosing all maxima;
sufficiency follows by replaying the maximal-duration schedule and ignoring
any earlier release. Shorter drains retain no reservation longer and finish
no later. The same argument applies to common upper bounds. This is an
elementary monotonicity reduction, not a new scheduling theorem.

Using a common conservative bound can therefore support a concentration
guarantee even when actual drain lengths vary. Using tighter individual bounds
can reduce upkeep while making the optimum distributed. In the pass-27 family
this distinction is exactly quantified at zero preparation deficit. Replace
both drain bounds by their larger value `ell_A`, so both handoffs must occur
by `h_A=log y`. The B-first all-policy bound remains

$$G=7-3y^2,$$

attained by full B at the request and rate-four preparation of A until h_A.
In the A-first case the certificate gives

$$L\geq W(h_A,h_A)=4-3y^2+3y=G+3(y-1)>G.$$

Hence the optimum under the common conservative bound is exactly G. The
upkeep price of discarding the tighter individual duration bound is exactly
`G-C=g_B`, the same small penalty computed above. This comparison does not
claim the same formula at positive tolerance.

All resource and service restrictions remain substantive: the receiver must
independently serve new essential work, the old residual obligations must be
immutable, and their retained reservation must be charged. A changing old
obligation cannot be hidden inside the drain. The result does not validate
a physical proportional-loss law, ownership fence or implementation. Free
independent premaintenance and free early permanent transfer still defeat
a universal source-upkeep interpretation, as the
[earlier counterpolicies](2026-09-22-pass17-assumptions.md) prove.

## 5. Prior art and contribution decision

The [bounded source comparison](2026-09-23-pass26-prior-art.md) confirms that
controllable processing, delivery tails and fixed-deadline allocation are
established scheduling themes. Fixed handoff times reduce to discounted linear
allocation, and the scalar exponential calculation is elementary. No novelty
claim attaches to those ingredients, to the common-bound substitution, or
to generic resource depletion.

The inspected direct models do not imply the displayed all-policy structure
after the tested substitutions: useful preparation decays while waiting and
drain completions change later input capacity. This does not exclude more
general reductions or settle priority. One delegated arXiv retrieval has
inconsistent date metadata and could not be independently retrieved by root;
it remains provisional and is unnecessary to this assessment. The accessible
Schuurman–Woeginger model already establishes the conventional framing.

The residual candidate is a precise structural theorem and separation for
upkeep-optimal readiness in the declared leaky preparation class. The common
coefficient theorem and partial-order bound strengthen that candidate; the
small-mismatch family limits how its equality assumptions may be interpreted.
Meaningful publication novelty and a justified physical application remain
unestablished. Manuscript writing is still deferred.

One further dimensional test is justified by a specific obstruction: with
two unequal-rate interior partials and a cold third module, the cold module
can interrupt preparation and release resource, while its zero initial amount
prevents the initial-state decrease used by the local exchange. The pair-order
theorem restricts the partials but does not eliminate that cold work. The next
pass should test this smallest remaining common-drain case over all policies,
including competitors with nonzero initial preparation in the third module.
It should not start a general solver or automatically expand to more modules.
