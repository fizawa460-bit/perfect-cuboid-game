# Stage32-18B — d16 Aut-canonical bounded production

This unit starts the audited production phase of the promoted `d=16` rank-63 `H^perp` route. The old d8 `e20/a0` 7.8-billion materialized-branch route remains paused and restartable at its audited `<=114186` checkpoint.

The first new meaningful norm wall after audited `b6` is `b8` (the lattice norm is even, so `b7` adds no new norm shell). Stage32-18B therefore credits no extrapolation from b6. It directly runs b8 twice:

1. the fast 64-breaker Aut-canonical implementation, to measure production cost;
2. an exact-rational traversal derived mechanically from the hostile-audited Stage32-18A certifier, with every actual cap branch rejection certified by exact Cauchy–Schwarz.

Both runs use the same rank-63 Hperp input and stable order-1536 Aut bundle. Both emitted canonical sets are independently checked under the full group and must be byte-identical before b8 receives numerical credit.

The audited Stage32-18A source blob is locked as `cb1b7b47c7a03c8bab243e867cb5fecac38643b3`; `build_exact_bound_certifier.py` only removes the explicit `bound==6` guard and changes the output schema. It refuses any unexpected source shape.

Firewalls remain:

```text
AUDIT_STATUS=PENDING
FAST_TRAVERSAL_GLOBAL_COMPLETENESS_CERTIFIED=false
D16_PRODUCTION_EXACT_OR_CROSS_CERTIFICATE_REQUIRED=true
FULL_D16_G0_ROW_COMPLETE=false
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false
R29_LG2_NUMERICAL_COMPONENT_COMPLETE=false
R29_LG2=NOT_DISCHARGED
G10_LOWGENUS_PICARD=AMBER
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
```

If b8 completes and cross-certifies, stop for hostile `Stage32-audit`; do not infer any larger-bound count or global fast-traversal completeness from b8.
