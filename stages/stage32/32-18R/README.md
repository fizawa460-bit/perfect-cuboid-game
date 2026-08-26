# Stage32-18R — rescue-aware exact global b14 integration

This stage is the final exact integration receiver for the current b14 production design. It does not enumerate new search space.

Inputs are fixed by run/artifact identity:

- Stage32-18P bulk251 production: all packet IDs except `0,15,63,64,173`;
- Stage32-18O exact pilot packets `63,64,173` reused without recomputation;
- Stage32-18Q logical hot parents for primary residues `26` and `748`, replacing packets `15` and `0` respectively;
- hostile-audited Stage32-18L b12 aggregate artifact as predecessor lock.

The aggregator requires all 256 logical packet slots, all 1024 `h54 mod 1024` residues exactly once, identical immutable source locks, no duplicate canonical records, exact equality of the complete `norm <= 12` record set with the hostile-audited b12 census, and an independent full order-1536 Aut verification.

Nested-rescue and packet execution counters are not summed into a hypothetical single-run global telemetry total because each execution repeats work above its split coordinate.

This branch intentionally has no run key until 18P and 18Q evidence is complete. Numerical credit remains blocked behind hostile audit.
