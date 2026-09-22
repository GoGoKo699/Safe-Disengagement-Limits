# Pass 16 recovery: execution checks on the preserved sources

22 September 2026. This check starts from the freshly recovered repository at
`16dca7e14950e13e4a292600ee39b2a3aeca9ec1`. The pre-interruption checkout and
its missing new report are unavailable. This note records new execution of
the preserved sources, not identity with every pre-interruption local byte.

## Recovery integrity

Before source edits, all 19 entries of
`results/recovery-source-inventory.json` matched both their recorded byte
counts and independently calculated canonical Git blob SHA-1 values. The
inventory deliberately excludes itself. The check establishes that the fresh
checkout contains the source bytes recorded by the recovery commit; it does
not recover an unavailable earlier filesystem snapshot.

`LICENSE` remains blob `e17a781bf47c4aadf18b68fc593846a1193b86c1`.
The license and both complete checkpoint directories have no diff against
either the recovery commit or the preceding research commit
`bb1e34f41338745c88ae486d493a053c658fb3d1`. The root verifier also validated
the checkpoint manifests, ran the historical programs in temporary copies,
and reproduced both historical reports byte for byte.

## Executed suites

Runtime: Python 3.12.14 on Linux x86-64. All commands below exited zero.

| Command | Result |
| --- | --- |
| `python verify.py` | Both immutable checkpoints reproduced unchanged. |
| `python -B analysis/verify_heterogeneous.py` | Report identical to the existing result. |
| `python -B analysis/verify_state_dependent.py` | Report identical to the existing result. |
| `python -B analysis/verify_handoff.py` | Report identical to the existing result. |
| `python -B analysis/verify_partial_states.py` | Report identical to the existing result. |
| `python -B analysis/verify_proportional.py` | Report identical to the existing result. |
| `python -B analysis/verify_unequal_proportional.py` | Report identical to the existing result. |
| `python -B analysis/verify_critical_viability.py` | New report generated and inspected. |

The six pre-existing research reports were compared as complete byte strings,
not only by their status fields. The new critical-viability report was then
generated a second time to a separate build path. The two new outputs were
byte-identical. The inspected bytes were saved as
`results/critical-viability-verification.json` (2,960 bytes; SHA-256
`2963d70fc8259cd07208363b5fc82892325f30b22b3393acbc584ec102cd2cef`).
No comparison with the unavailable pre-interruption report is claimed.

## New report: what is actually checked

The recovered verifier was read in full. Its rational arithmetic checks four
global-cost case groups supporting the written concentration-based argument,
300 sampled target-obstruction state/allocation combinations, two phase
identity groups, an interval certificate, and 18 rational path samples.
The interval certificate uses the exact endpoint inequality
`108/128 + 63/128^3 < 1` and nonnegative polynomial coefficients. The written
fourth-root concavity argument turns that certificate into a statement for
every real `0 < x <= 1/128`; the rational samples are not the all-time proof.

The report separately identifies 18 floating schedule replays and one
floating frontier check. The latter returns upkeep
`1.0000000000000004`, within the stated tolerance `2e-9`. The largest sampled
schedule/formula difference is about `3.33e-16`; all sampled replay times
are below the deadline, with the closest gap about `5.32e-6`.
These are numerical consistency checks, not certified deadline decisions or
an optimization proof. The universal-policy obstruction, unique global
minimum, and robust indefinite-readiness claims remain written theorems in
the pass-15 notes and manuscript.

The new verifier rejects `-O`, `-OO`, and `PYTHONOPTIMIZE=1` with exit code 2
and creates no requested output. A requested output under the immutable
checkpoint directory is also rejected with exit code 2, before any file is
created. The checkpoint trees remain unchanged after these guard checks.

## Remaining gate

This note covers recovered-source execution and report regeneration.
PDF compilation and rendered-page inspection are recorded separately by the
manuscript task. Before publication, the parent task must commit the complete
intended checkpoint, execute the suites and report comparisons from an
archive of that exact commit, reconcile concurrent remote work, and verify
the published tree. These checks do not certify novelty, physical validity,
external peer review, or submission readiness.
