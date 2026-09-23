# Pass 28: extract the general partial-order theorem

23 September 2026. Completed follow-on; recorded retrospectively with its
outcome. Repository research only.

The pass-26 first-hit advance changes two initial states and reallocates one
module's input to the other. Test whether all other modules can retain their
recorded controls and events when independent drain releases only move
earlier. If valid, derive the exact order and count restriction on interior
partial coordinates for arbitrary finite module count and heterogeneous
drains. Preserve design-cap, support-charge and nominal-precision quantifiers.
Do not infer serial optimality for arbitrary states or control order on
every smaller-loss realization.

Outcome: [the theorem](../../research/2026-09-23-pass28-partial-order.md)
proves that interior partials hand off in strictly decreasing coefficient
order in first-hit maximal-loss witnesses, and a later partial receives no
input before an earlier partial hands off. At most one partial can belong
to each coefficient class. Consequently a common coefficient preserves
every-minimizer concentration for arbitrary independent drains and any finite
module count, including nominal fixed-tolerance minima.

Cold and design-bound coordinates can still interleave. The remaining
three-module common-drain question must address that obstruction explicitly,
not treat the pair theorem as a general seriality result.
