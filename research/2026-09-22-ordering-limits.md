# Heterogeneous ordering limits

Date: 22 September 2026. Research pass 2. The
[serial-dominance theorem](2026-09-22-heterogeneous-scheduling.md) gives an exact
subset dynamic program. This note records exact obstructions to replacing it
with simple priority rules. These are model-internal counterexamples, not a
publication-novelty or complexity-hardness claim.

## What ordering simplifications fail?

After serial optimality, the next question is whether the subset search reduces
to a context-free job ordering. The following exact counterexamples delimit
that possibility. They do not prove any complexity lower bound.

For two eligible jobs `i,j` at current capacity `b`, define

    L_ij(b) = M_i/(b-d_i) + M_j/(b+a_i-d_j).

Their exact adjacent-interchange difference is

    L_ij(b)-L_ji(b)
      = M_i*a_j/[(b-d_i)(b+a_j-d_i)]
        - M_j*a_i/[(b-d_j)(b+a_i-d_j)].             (1)

**Two-job reversal with changing available capacity.** Take
`A=(M=2,a=4,d=0)` and `B=(M=1,a=1,d=0)`.

| Available capacity | A then B | B then A | Strictly better |
|---:|---:|---:|---|
| `b=1` | `11/5` | `2` | B then A |
| `b=4` | `5/8` | `13/20` | A then B |

Thus a priority depending only on an individual module's fixed parameters,
independent of current capacity, cannot reproduce all optimal two-job orders.

**A three-job preference cycle at one fixed capacity.** At `b=3`, take

| Job | M | a | d |
|---|---:|---:|---:|
| A | 2 | 4 | 2 |
| B | 6 | 5 | 1 |
| C | 5 | 1 | 0 |

Each pair considered alone prefers the order in the second column:

| Pair | Preferred order and time | Reverse order and time |
|---|---|---|
| A, B | A then B: `3` | B then A: `10/3` |
| B, C | B then C: `29/8` | C then B: `11/3` |
| C, A | C then A: `8/3` | A then C: `19/7` |

The strict cycle `A before B before C before A` excludes a scalar priority
depending only on `(b,M_i,a_i,d_i)` that correctly ranks every two-job instance.
It does not exclude policies using the whole remaining set. Nor does it say that
the three comparisons apply at the same capacity in a single three-job schedule.
Two jobs suffice for the preceding context reversal; three are necessarily
required for a strict preference cycle. No claim of minimal integer coefficients
is made.

**Even an exact local pairwise index need not give a globally optimal greedy
rule.** When all losses are zero and all `a_i>0`, (1) says that at fixed `b` the
pairwise comparison is represented by ascending

    I_i(b) = M_i + b*M_i/a_i.

But repeatedly choosing the smallest current index is not globally optimal.
Take `b=1`, and zero-loss jobs `A=(M=3,a=1)`, `B=(M=5,a=4)`,
`C=(M=6,a=6)`. Initially the indices are `6,25/4,7`; the greedy choice is
uniquely A. At `b=2`, B's index is `15/2`, below C's `8`. Greedy therefore uses
A,B,C and takes `13/2`. Enumeration of the six exact serial costs gives the
unique optimum B,C,A, whose time is

    5 + 6/5 + 3/11 = 356/55 < 13/2.

Accordingly, adjacent exchange comparisons alone do not certify an optimal
global ordering, even without invalidation. The exact subset dynamic program
remains the available general algorithm.

## Interpretation for the prior-art audit

The two-job reversal rules out a priority fixed once for all available capacities.
The three-job cycle is narrower and stronger at a fixed capacity: no scalar score
of an individual job and `b` can reproduce all optimal two-job decisions across
instances. The zero-loss greedy example shows why transitive adjacent comparisons
at a given stage do not establish a globally optimal adaptive priority rule.

These witnesses identify what a claimed prior scheduling rule must actually
cover. A theorem limited to equal capacity releases, equal invalidation rates,
fixed total capacity, or two jobs is not contradicted by these examples. A method
that uses the complete remaining set or searches subsets is not excluded. The
examples do not prove that no polynomial-time algorithm exists, and they do not
establish new complexity classifications.

For the literature comparison, ask whether a candidate theorem allows
job-dependent released capacity, job-dependent active loss, and arbitrary
preemptive allocations. Inspect its optimality criterion and whether it handles
all remaining sets, rather than matching only its notation or a pairwise rule.
`analysis/verify_heterogeneous.py` records exact rational assertions and six-order
checks for these examples. Its checks support the arithmetic; the logical scope
of each counterexample is stated above.
