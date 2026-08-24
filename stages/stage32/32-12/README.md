# Stage32-12 — e8/a36 full-parent numerical orbit census

This stage is a consolidation boundary after the Stage32-11 exact high-mass tail run and its timeout-shard repair.

It does **not** change solver semantics. It source-locks and combines:

- the exact `<=65536` 44-cell predecessor tier;
- the eight directly completed high-mass e8/a36 cells from Stage32-11;
- the four-way exact repair aggregate for timeout cell 39;
- the audited 53-cell materialization profile;
- the source-locked Picard core and full Aut(S) action.

The first verifier requires exact coverage of all 53 immutable e8/a36 signature cells and all 1,783,951 materialized branches, with no UNKNOWN/node-budget exhaustion, and emits one compact parent census manifest.

The second verifier independently closes the source-locked Aut(S) group to order 1536, partitions every parent numerical survivor into its full Aut(S) orbit in the injective 140-intersection representation, recovers every orbit member integrally in the Picard basis, and checks that every orbit member returning to the a=36 slice is present in the completed parent. The previously audited square-0 orbit of size 6 and square-(-4) orbit of size 192 are retained as regressions.

Scope is numerical Picard classes only. No effectivity or actual-curve existence is asserted.

Firewalls remain:

- `THEOREM_CREDIT=false`
- `RECEIVER_CREDIT=false`
- `FULL_D8_G0_ROW_COMPLETE=false`
- `FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false`
- `R29_LG2_NUMERICAL_COMPONENT_COMPLETE=false`
- `R29_LG2=NOT_DISCHARGED`
- `R29_LG2_EFF=NOT_DISCHARGED`
- `R29_LG2_MB=NOT_DISCHARGED`
- `G10_LOWGENUS_PICARD=AMBER`

If this workflow passes, Stage32 stops for hostile audit before any further e10 giant-cell computation or effectivity interpretation.
