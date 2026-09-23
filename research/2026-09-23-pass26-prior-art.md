# Pass 26: common drains, delivery tails and controllable processing

23 September 2026. Bounded primary-source comparison for the
[two-module common-drain theorem](2026-09-23-pass26-common-drain.md).
Read the full local proof, the pass-26 opening, and the earlier
[allocation/deterioration](2026-09-23-pass20-deterioration-prior-art.md)
and [preemptive-scheduling](2026-09-22-pass6-prior-art.md) comparisons.
Two complete relevant primary results were inspected; one older close lead
remains access-limited. No third-party full text is stored in the repository.

The defensible finding is a specific assumption boundary: in this ideal
interface, unequal drains permit a unique two-partial optimum, whereas one
common drain preserves two-module concentration even when its delayed release
can assist later preparation. Delivery tails, controllable initial work,
fixed-deadline allocation and endpoint arguments are established themes.
The inspected results do not directly imply this particular boundary; that
is neither novelty clearance nor a reason to expand the model automatically.

## 1. Exact object requiring comparison

| Item | Pass-26 requirement |
|---|---|
| Controls | Arbitrary measurable divisible preparation, interruption and causal response to bounded loss; maximal-loss replay gives an exact deterministic witness. |
| State and caps | `p_i'=v_i-gamma_i*p_i` before full-state handoff, physical caps `M_i`, initial design caps `U_i<=M_i`. |
| Objective | Minimize `sum gamma_i*x_i + sum h_i*1[x_i>0]`, `h_i>=0`; variable prices equal physical loss coefficients. |
| Deadline | Every immutable drain ends by H; a common duration ell gives every handoff deadline `D=H-ell`. |
| Capacity | `s+sum a_i*1[t>=t_i+ell]`; a tail ending changes other modules' available preparation rate. |
| Conclusion | Existence and **every** minimum having at most one coordinate in `(0,U_i)`, for two modules. |

This is an initial-state optimization statement. It does not prove serial
optimality for each prescribed state, and an algorithm returning one extreme
optimum would not alone establish its every-minimizer quantifier.

## 2. Two primary comparisons and inspection limits

| Feature | Schuurman–Woeginger | Chen–van der Gaast–Zhang, Lemma 4 |
|---|---|---|
| Control | Continuous compression `0<=x_j<=u_j`; nonpreemptive jobs | Fixed job order; choose a discrete mode |
| Work | Fixed shortened duration `p_j-x_j` | Fixed nonnegative integer pairs `(p_ij,q_ij)` |
| Objective | Latest delivery plus `sum c_j*x_j`; fixed-length cost subproblem | Minimum latest delivery |
| Tail and deadline | Resource-free tail `q_j`; length-L test | Resource-free tail; threshold T |
| Capacity | Fixed single machine | Fixed single machine |
| Result inspected | LP rounding and approximation bound | Exact fixed-order deadline test |

**Schuurman and Woeginger**, *A PTAS for single machine scheduling with
controllable processing times*, Acta Cybernetica 15 (2001), 369–378.
[Institutional primary PDF](https://acta.bibl.u-szeged.hu/12685/1/cybernetica_015_numb_003_369-378.pdf).
Read Sections 1–2.4 in full, including the Section-2.3 LP and complete
proofs of Lemmas 2.4–2.5 (pp. 376–377); Theorem 2.6 summarizes the result
on p. 378. The LP includes compression caps and tail-dependent interval
eligibility. Rounding enlarges the deadline while controlling compression
cost; this is not an exact every-minimizer concentration theorem.
Parsed mathematics obscures some rounding constants; those constants are
not relied upon here, and no independent certification of the PTAS is claimed.
The volume prints 2001 but its final receipt line says May 2002; the citation
retains the printed volume year without resolving that inconsistency.

**Chen, van der Gaast and Zhang**, *Scheduling Jobs with Multiple Operational
Modes and Tail Times*, [arXiv:2609.16001v1](https://arxiv.org/html/2609.16001v1).
The source-audit agent read Section 3.1, equations (1)–(4), and the complete
Section-3.3 Lemma-4 proof ([retrieved PDF](https://arxiv.org/pdf/2609.16001v1),
pp. 9–10). Its threshold test selects the shortest eligible processing mode;
smaller cumulative processing preserves subsequent feasibility. There is no
preparation-investment objective. Other complexity results are not imported.
The displayed fields are Bo Chen, Jelmer Pier van der Gaast, Xiandong Zhang;
`arXiv:2609.16001v1`; manuscript `July 19, 2026`; submission `24 Jul 2026`.
Those dates conflict with the identifier's month. The root agent's independent
HTML/PDF cross-checks failed. Provenance therefore remains provisional:
successful delegated retrieval is recorded, but this source is not necessary
for the contribution assessment, and no publication chronology is inferred.

**Access-limited predecessor.** S. Zdrzałka, *Scheduling jobs on a single
machine with release dates, delivery times and controllable processing
times: worst-case analysis*, Operations Research Letters 10(9), 519–523
(1991), [DOI 10.1016/0167-6377(91)90071-V](https://doi.org/10.1016/0167-6377(91)90071-V).
The publisher abstract/metadata were accessible; the PDF endpoint failed.
Its complete theorem and proof were not inspected, so no exact exclusion
or priority conclusion is drawn. Previously inaccessible Glazebrook and
Rudek sources were not retried; their recorded limits remain material.

## 3. Positive reductions and the remaining direct-mapping obstruction

The following are deductions about S1, not claims attributed to the sources.
First, the tail/deadline conversion is elementary and exact:

$$t_i+\ell_i\leq H\quad\Longleftrightarrow\quad t_i\leq H-\ell_i.$$

Unequal immutable drains therefore encode module-specific preparation
deadlines. In the pass-25 witness no release occurs soon enough to help
preparation: its failure of concentration is already a different-deadline
effect. A common drain removes that difference. For `ell<=H<=2*ell`,
all required handoffs precede any useful release, recovering the previously
proved zero-release model at `D=H-ell`.

Second, fix the handoff times and hence the capacity history b. Discounting
maximal-loss dynamics gives the ordinary linear allocation equations

$$z_i(t)=x_i+\int_0^t e^{\gamma_i r}v_i(r)\,dr,\qquad
z_i(t_i)=M_i e^{\gamma_i t_i},\qquad \sum_i v_i(t)\leq b(t),$$

with linear intermediate cap constraints. The
[opening note](2026-09-23-pass26-common-drain-opening.md) states this exact
fixed-time problem and a weak-duality certificate. Discounted coordinates,
linear allocation and that certificate are ordinary tools, not a new
scheduling principle. Optimizing the handoff times remains a separate step.

Third, a direct identification of initial preparation with a standalone
processing mode fails even before a capacity jump. At constant capacity
`b>gamma_i*M_i`, suppose a subfull module receives no input before t, then
all b until handoff. Its remaining duration is

$$\delta_i(t,x_i;b)=\frac1{\gamma_i}
\log\frac{b-\gamma_i x_i e^{-\gamma_i t}}{b-\gamma_i M_i}.$$

For positive initial preparation it depends on the start time. Thus x_i
does not merely select a fixed processing duration independent of the
schedule. Moreover, an earlier module's drain can change b during the
next module's preparation. Neither direct comparison table has this
capacity dependence. This identifies missing hypotheses for a direct
substitution; it does not exclude a more elaborate nonlinear reduction.

The all-policy work in pass 26 is correspondingly specific: advancing a
slow-first handoff strictly lowers upkeep after a discounted initial-state
exchange; a putative fast-first two-interior minimum must itself use serial
full-rate inputs. Only then does the ordinary exponential calculation apply.
The common deadline permits two-sided timing variations, and the downward
derivative jump at a delayed release excludes a kink minimum. Caps and
support charges are implementation of the same local argument, not separate
allocation discoveries. Earlier deterioration and allocation comparisons
remain applicable and unresolved where they were previously unresolved.

## 4. Decision for the next research task

Record pass 26 as a proved two-module interface boundary paired with pass 25,
with novelty and operational adequacy still unresolved. The source audit
does not establish an exact prior-art reduction, but its outcome supports
only this narrow residual description. It does not justify claims that
delivery tails, controllable processing or allocation concentration are new.

Do not generalize n merely to accumulate variants. First perform a concise
contribution and operational assessment: identify which real obligation makes
the immutable drain retain the preparation resource, account for independent
receiver service, and say what decision the common-versus-unequal distinction
changes. A higher-dimensional question is justified only if it tests a
specified new obstruction, such as overlapping common drains changing the
minimal concentration boundary. It must not inherit two-module seriality.
If no stronger operational or conceptual meaning survives that assessment,
retain these results as assumption diagnostics and select the next S1
question accordingly. More dimensions alone would not resolve the remaining
novelty or meaning gaps. Manuscript work remains paused.
