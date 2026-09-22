# Pass 2: ordering simplification and prior-art reduction

22 September 2026. **Completed.** This pass followed the serial-dominance and
exact-upkeep results of pass 1.

Question: can the subset recurrence be replaced by a universal ordering rule,
and which parts are consequences of established scheduling/control?

Outcomes: exact two-job capacity reversal, three-job preference cycle, and
failure of the locally exact zero-loss greedy index. Common-loss/common-release
clearing reduces to an established preemptive scheduling theorem. Recurring
averaging is a bounded-storage dissipativity argument.

Evidence is in `research/2026-09-22-ordering-limits.md`, the current literature
audit, and `research/2026-09-22-dissipativity.md`. No hardness or novelty claim
follows. The next question chosen was whether the fully-ready attaining
construction hides a startup obstruction.
