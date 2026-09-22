# Primary-source comparison

**Checked 22 September 2026.** This is targeted screening, not a complete review.
The exact model in `NOTE.md` is our formulation. No source below has been
verified to state that complete theorem with identical quantifiers.

## Direct mathematical overlap

**J.-Y. Le Boudec and P. Thiran, Network Calculus: A Theory of Deterministic
Queuing Systems for the Internet** (Springer, 2001; author-hosted corrected
edition dated August 2022).
https://leboudec.github.io/netcal/latex/netCalBook.pdf

Theorem 1.4.1 (p.22) bounds backlog by `sup(alpha-beta)`. Equation (1.34)
(p.54) gives equivalent capacity `sup_s(alpha(s)-buffer)/s`. Setting
`alpha=lambda Q_H` and `beta(s)=B*s` reproduces our stationary frontier.
Our all-history throughput upper bound additionally uses the averaging lemma.
The operational meanings differ: our physical demand must be served on time,
whereas a queue stores unserved work.

## High-performance operation and degraded-mode safety

**Maxime Gariel and Eric Feron, Graceful Degradation of Air Traffic Operations**
(arXiv:0801.4750, 2008).
https://arxiv.org/abs/0801.4750
https://arxiv.org/html/0801.4750v1

The introduction distinguishes analysis of degradation sensitivity from designing
traffic configurations that keep sensitivity below a threshold. It studies
separation after loss of high-performance surveillance. This is a close
precedent for increased operational capability making degraded operation harder,
not a theorem about our stock/rate/commitment-kernel model.

## Noncancellable accepted work

**Lin Chen, Franziska Eberle, Nicole Megow, Kevin Schewior, Cliff Stein,
A general framework for handling commitment in online throughput maximization**
(arXiv:1811.08238, 2018 preprint).
https://arxiv.org/abs/1811.08238
https://arxiv.org/html/1811.08238v1

The model requires completion of accepted jobs, including commitment upon
admission or before a specified fraction of remaining slack. Its competitive
analysis concerns online scheduling. This establishes that noncancellable
admission is not a new modeling ingredient; it does not by itself resolve our
uniform retirement-resource question.

## Clearing time is already a queueing observable

**Sergey Foss and Peter W. Glynn, On Recurrence of the Infinite Server Queue**,
Queueing Systems 110, article 11 (published 28 January 2026).
https://doi.org/10.1007/s11134-026-09972-7

The opening defines virtual workload as time needed to drain the system if
arrivals stop, and studies the maximum-dater recursion for infinite-server
queues. This concerns clearing time, not the total reserve consumed by our
fixed timed-demand model. A tail or drain-time distinction alone should not be
claimed to originate in S1.

## Prior control baseline remains relevant

**Dung T. Phan et al., Neural Simplex Architecture** (arXiv:1908.00528).
https://arxiv.org/abs/1908.00528
https://arxiv.org/html/1908.00528v2

Its recoverable-region requirement preserves safety under a baseline controller,
with a decision module switching before recovery becomes impossible. S1 must not
claim that preserving safe fallback reachability is new.

## Decisions

* Retain the passive-commitment theorem and checks as an exact benchmark.
* Do not submit the stationary reserve formula as a new general theory.
* Do not call the entire all-history theorem previously published without an
  exact match; that stronger conclusion has not been established either.
* Investigate active conversion of commitments only after specifying a real
  operational mechanism and auditing its scheduling/control precedents.
* A manuscript, application claim, and GitHub repository are premature at this
  checkpoint. No external proof audit has been performed.
