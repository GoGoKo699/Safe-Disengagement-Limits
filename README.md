# Safe Disengagement Limits

**How much useful operation must a system give up to keep its controller safely removable?**

Theory-first research on cooperative, bounded-time handover to an independent fallback. The controller obeys the removal request; the difficulty is keeping essential service running after it leaves. This project studies resource accounting, not an agent's incentive to resist shutdown.

**Research status:** two analytical checkpoints with reproducible finite checks. The active-readiness model has a matching lower bound and construction under explicit restrictions. Publication novelty, a concrete engineering instantiation, and external proof review are **not established**. See [STATUS.md](STATUS.md).

## Start here

| Reading goal | Entry point |
|---|---|
| Understand the current candidate result | [Active readiness: definitions and proofs, sections 1–6](checkpoints/active-2026-09-22/NOTE.md) |
| See the assumption that changes the conclusion | [Proportional-invalidation countermodel, section 8](checkpoints/active-2026-09-22/NOTE.md#8-assumption-stress-test-a-smooth-alternative-removes-the-staircase) |
| Check overlap with established research | [Active source comparison](checkpoints/active-2026-09-22/LITERATURE.md) and [passive source comparison](checkpoints/passive-2026-09-22/LITERATURE.md) |
| Understand the earlier benchmark | [Passive commitments](checkpoints/passive-2026-09-22/NOTE.md) |
| Reproduce the finite checks | Run `python verify.py` from the repository root |
| Continue the investigation | [Current work order](work_orders/CURRENT.md) and [agent instructions](AGENTS.md) |

A first reading can stop after sections 1–6 of the active note and its source comparison. The earlier passive model is useful context, not a prerequisite.

## The current model in one paragraph

There are `n` identical, independently switchable services. While primary-controlled, each uses resource rate `a`. After this prescribed normal load, spare capacity `s` is shared between optional throughput and preparing current handover state. Full preparation requires work `M`; any positive preparation may become outdated at rate up to `d`. On a removal request, optional work stops. A fully prepared service transfers immediately to a separately provisioned fallback, releasing rate `a` for the remaining transfers. Essential service is uninterrupted, and all dependence on the primary must end within deadline `H`.

For `k` fully prepared services and an otherwise unprepared system, the exact worst-case exit time is

$$
T_k=M\sum_{j=k}^{n-1}\frac{1}{s+ja-d},
$$

when `k<n` and `s+ka>d`. Otherwise `T_k` is infinite; `T_n=0`. Define `k_H` as the smallest `k` with `T_k<=H`.

The exact maximum guaranteed long-run **optional** throughput is

$$
u^*(H)=s-dk_H,
$$

provided `dk_H<=s`. When `dk_H>s`, indefinitely maintaining that deadline is infeasible under the prescribed normal load. Keeping exactly `k_H` services fully prepared attains the bound after paid initialization. A potential argument and an averaging inequality cover parallel, preemptive, partial, and rotating preparations—not only the attaining schedule.

This does not say that full normal service has throughput `u*`: the mandatory normal load `na` is still delivered. It also does not guarantee a cold start or survival of a sudden primary failure during the cooperative grace period.

## The boundary matters

The fixed-rate invalidation assumption is load-bearing. A one-service proportional-invalidation model gives a **continuous** maintenance frontier instead of the staircase above. The staircase is not a universal law of dependence.

The independent fallback, its essential-service capability, and a sufficient handover interface are assumed, not created by copying data. Services have no shared-state cutover barriers; cutover has zero latency; receiver resources are provisioned separately. These restrictions and excluded alternatives are explicit in the [active model](checkpoints/active-2026-09-22/NOTE.md).

The earlier passive model concerns noncancellable, fixed demand profiles and independent supply plus stored reserve. Its stationary frontier overlaps directly with network calculus. It remains a benchmark, not the main publication claim. The two models must not be merged by notation alone.

## Reproduce locally

Python 3.10 or newer; standard library only:

```sh
python verify.py
```

The root runner checks checkpoint hashes, runs both original verifiers in temporary directories, and compares their complete reports with the archived reports. It writes `build/verification.json` without modifying the checkpoints. It refuses optimized Python because the original verifiers use assertions.

The active checkpoint includes 65,100 local maintenance-inequality cases, 27,992 transition-inequality cases, and 3,360 parameter curves. The passive checkpoint includes 9,720 frontier cases. These categories are not independent experiments, and the finite tests do not prove continuous-time claims, validate an application, or establish novelty. See [the bootstrap reproduction record](results/bootstrap-verification.json).

No large simulations, model training, external datasets, or network access are needed for these checks.

## Provenance and license

The research question was inspired by the science-fiction setting of Ruge Lin's *Falling* (《坠落》). The mathematical models are explicit research formulations, not claims that the fiction's mechanisms are physically established. The story and third-party papers are not redistributed here.

The two checkpoint directories preserve the supplied research packages byte-for-byte. Their historical statements about having no repository refer to their creation time; current repository status and licensing are given here. See [PROVENANCE.md](PROVENANCE.md).

[MIT License](LICENSE), Copyright (c) 2026 Ruge Lin. The repository's original license is preserved unchanged.
