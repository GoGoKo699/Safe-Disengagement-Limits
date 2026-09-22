# Pass 7: finite-update readiness reduces to a sporadic deadline task

22 September 2026. This audit concerns the one-record, immediately observed,
whole-version reset model in the [finite-update note](2026-09-22-pass7-finite-updates.md).
It does not settle the separate coupled serial-reduction question from
[pass 6](2026-09-22-pass6-prior-art.md). The conclusion is a positive reduction,
not an inference from failing to find a paper with the same terminology.

## 1. Conclusion and novelty boundary

After deriving the exact post-request exit value, **the entire normal-operation
readiness constraint is equivalent to meeting the deadlines of one
constrained-deadline sporadic task**. The equivalence includes the rising
preparation threshold, not merely its average utilization. The task's execution
requirement, relative deadline, and minimum inter-arrival time are

$$C=2L-H,\qquad D=\Delta+L-H,\qquad T=\Delta,$$

where `L=M/s` and `L<=H<=2L`. Its latest feasible full-speed execution interval
starts at age `D-C=Delta-L`. The preparation cost `(2M-sH)/Delta` is `s` times
the task's ordinary utilization `C/T`.

Consequently the average frontier, per-update workload bound, and delayed ramp
are not defensible as independent scheduling contributions. The derivation of
the post-request value and its conversion into this deadline task are useful
interface calculations. This pass does not identify a primary source already
printing that particular two-copy exit formula, nor does it establish the
formula's novelty. Its short adversarial proof and exact reduction provide no
present basis for selecting it as the central result of a research paper.

The age-dependent state distinction and the failure of substituting mean reset
traffic for a pointwise erosion envelope remain worthwhile negative findings.
They explain an abstraction boundary; they do not by themselves certify a
publication contribution.

## 2. Primary source inspected and access limits

J.-J. Chen, N. Bansal, S. Chakraborty, G. von der Brüggen,
*Packing Sporadic Real-Time Tasks on Identical Multiprocessor Systems*,
ISAAC 2018; [author manuscript, arXiv:1809.04355v1](https://arxiv.org/pdf/1809.04355v1)
([HTML rendering](https://arxiv.org/html/1809.04355v1)).

**Inspected:** the introduction's task definitions and complete sections
2.1–2.3, including equation (1) and the following exact EDF feasibility-test
statement. These sections define execution `C`, relative deadline `D`, minimum
inter-arrival time `T`, utilization `C/T`, and constrained deadlines `D<=T`.
Equation (1) gives the demand bound function

$$\operatorname{dbf}(t)=C\max\left\{0,
\left\lfloor\frac{t-D}{T}\right\rfloor+1\right\}.$$

The feasibility statement requires total demand to fit every interval. The
paper attributes that result to Baruah, Mok, and Rosier (1990); it does not
reprove it in these sections. Its later multiprocessor approximation theorems
are not used. The primary manuscript is sufficient to verify the exact model
mapping; the one-task consequence is proved directly below.

S. K. Baruah, A. K. Mok, L. E. Rosier,
*Preemptively scheduling hard-real-time sporadic tasks on one processor*,
RTSS 1990, pp. 182–190,
[DOI 10.1109/REAL.1990.128746](https://doi.org/10.1109/REAL.1990.128746).

**Access limitation:** the publisher PDF endpoint failed, the author publication
page timed out, and the
[author-uploaded ResearchGate record](https://www.researchgate.net/publication/3506549_Preemptively_scheduling_hard-real-time_sporadic_tasks_on_one_processor)
exposed its abstract and bibliography but not the manuscript's model or proofs.
The page's “full text” label is not treated as evidence that the full text was
read. The original theorem is therefore not claimed as independently audited.
The 1990 conference date and DOI are confirmed by the
[institutional publication record](https://profiles.wustl.edu/en/publications/preemptively-scheduling-hard-real-time-sporadic-tasks-on-one-proc-2/);
some indexing records display 1991. Further generic retrieval was stopped once
the accessible primary manuscript supplied the exact model needed here.

## 3. Exact equivalence, including intermediate ages

This section is our mathematical reduction, not a quotation or theorem
attributed to the papers above. Assume the finite-update note's exit theorem.
For `L<=H<=2L`, put

$$K=sC=2M-sH,\qquad D=\Delta+L-H.$$

Then `0<=C<=L<Delta`, `C<D<=Delta`, and `D-C=Delta-L`.
The readiness barrier has the equivalent form

$$p_H(a)
=\max\{0,M-s\max(\Delta-a,H-L)\}
=\min\{K,\max\{0,s(a-(D-C))\}\}.$$

Each update at time `t_j` releases one task instance with work `K`, deadline
`t_j+D`, and physical service rate at most `s`. Consecutive releases are
separated by at least `T=Delta`. Jobs cannot overlap their next release because
`D<=T`. Progress is durable between releases. We count only the first `K`
units of copying after each release; extra copying is unnecessary to satisfy
this readiness requirement.

**Readiness implies deadline completion.** On a continuation with no intervening
update, the age-`D` barrier is `K`, so the job must have received at least `K`
work by its deadline. Such a continuation is always admissible. If `D=T` and
the next update occurs exactly at the deadline, the same conclusion follows
from readiness at all earlier ages and continuity up to the update's left
limit.

**Deadline completion implies readiness throughout the interval.** For any
`0<=a<D`, no update can occur before the job deadline. A trajectory which
completes `K` by that deadline and has rate at most `s` satisfies

$$p(t_j+a)\ \geq\ \max\{0,K-s(D-a)\}.$$

Otherwise the remaining time cannot supply enough work. This is precisely the
ramp in `p_H(a)`. For `a>=D`, completed work is retained until the next reset,
so `p>=K`, the plateau. At a reset both preparation and the new age-dependent
barrier return to zero. These statements cover every interval and every
admissible release sequence. Thus policies feasible for the deadline task and
uniformly ready policies describe the same necessary useful work constraints.

This is a reduction at the level of all admissible trajectories under a rate
bound. Fractional allocation or preemption does not add a missing quantifier:
normal optional work can be viewed as background service on the same unit
processor after dividing physical copying rate by `s`.

## 4. What follows without a new scheduling theorem

For one task with `C<=D<=T`, the demand bound condition is immediate. If an
interval contains `n>=1` complete job windows, its length is at least
`D+(n-1)T`, whereas required normalized work is `nC`. Since `D>=C` and `T>=C`,
the demand fits. The concrete policy waiting until age `D-C` and then serving
the job continuously for `C` time units establishes feasibility directly.

Periodic releases spaced by exactly `T` require `K` work per period, giving
the lower bound `K/T` on worst-case long-run copying cost. Conversely, complete
each released job using exactly `K` work. Any interval `[0,t]` contains at
most `floor(t/T)+1` releases, so its copying work is at most
`K(floor(t/T)+1)`. This gives the matching worst-case average, including finite
release sequences. Subtracting from shared capacity gives optional throughput
`s-K/T`. These are the finite-update theorem's recurring-cost arguments written
in standard task coordinates.

Utilization alone should not replace the deadline constraint: it describes
long-run cost, while `D` specifies when each version's preparation is needed.
In any future multi-record variant, a sum-of-utilizations inequality alone
would generally omit short-interval deadline demand. Neither the existing
one-record exit proof nor the present reduction proves a multi-record
handoff theorem; a shared exit resource would require a new readiness analysis
before introducing several derived tasks.

## 5. Hypotheses that make the reduction exact

| Finite-update assumption | Role in the task reduction |
|---|---|
| Updates are observed immediately and their age is known | Each task release time and relative deadline are available causally. |
| Every update invalidates the whole previous copy | Each release starts a fresh workload; useful work cannot be carried over to the next version. |
| Progress is durable between updates | A completed preparation job remains completed until the next release. |
| A certified lower spacing `Delta>L` | The next reset cannot precede the preparation deadline, and a full copy after an interrupted exit finishes before another possible reset. |
| Fluid copy rate is bounded by `s` | Remaining-work feasibility gives the exact linear ramp, and processor-time normalization is valid. |
| Immediate post-request access to the full spare rate | The exit calculation underlying the derived deadline is valid. |
| An instantaneous fence with the stated completion-first tie convention | Completing the requested copy ends exposure to later resets; equality cases in the exit formula are meaningful. |

For `H=L`, `C=L` and `D=T`; deadline completion immediately before the reset
is understood through the left limit. The requested handover's simultaneous
completion/update ordering remains a separate modeling convention, as the
finite-update note specifies. At `H=2L`, `C=K=0` and the task is vacuous. For
`H<L`, the reset state itself cannot satisfy readiness, so no deadline-task
scheduling choice repairs the interface. For `H>2L`, zero preparation remains
sufficient; the displayed three-parameter mapping is only used on `[L,2L]`.

Positive detection delay, useful retained blocks, delayed ownership fencing,
or a burst constraint without minimum event separation change the derivation.
The exact scheduling reduction does not remove the operational limitations
recorded in [the pass-6 interface note](2026-09-22-pass6-interface.md). Those
must be accounted for before presenting this benchmark as a service guarantee.

## 6. Research decision

Retain the finite-update theorem as an analytically solved benchmark and retain
this reduction alongside it. Do not promote its linear cost frontier to an
unmatched theorem. A justified next pass should address one existing operational
gap or resolve the coupled-decay serial-reduction literature gate; adding
records, deadlines, or reset parameters solely to escape the one-task mapping
would not establish significance or novelty.
