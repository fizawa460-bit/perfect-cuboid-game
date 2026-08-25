# Stage32-18A — certify d16 Hperp traversal and stable Aut provenance

This is the first main-batch unit after the audited route switch to the d16 Aut-compression path. It does not resume the d8 `e20/a0` 7.8-billion materialized-branch route.

The merged Stage32-18 implementation already has exact rank-63 `H^perp` coordinates, an exact order-1536 geometric Aut group, 64 deterministic score breakers, and exact full-group leaf canonicalization. Its b6 regression is `17,833` baseline cap survivors, `232` survivors after the 64 breaker inequalities, and `37` exact Aut-canonical representatives including zero. Hostile audit #1380 accepted that architecture but blocked numerical credit because the DFS radius and dual-reach pruning used uncertified `long double` arithmetic.

Stage32-18A therefore adds an independent certificate path for b6. The certifier reconstructs an exact rational LDL decomposition of the 63x63 positive-definite integer Gram matrix and checks `L D L^T = Q` exactly. Every DFS coordinate interval is an exact rational superset of the remaining norm ball, and every candidate coordinate is retained only after an exact rational norm-budget comparison. No floating-point value participates in any traversal-pruning decision. The 140 cap tests, 64 symmetry inequalities, and full-1536 leaf canonicalization remain exact integer checks.

The certificate must reproduce all three locked b6 levels exactly:

```text
complete norm-ball + 140 caps       = 17,833
+ 64 exact Aut score breakers       =    232
+ full order-1536 canonicalization  =     37 (36 nonzero)
```

The exact canonical set is then compared record-for-record as a set against the existing fast implementation, whose output is independently checked under the reconstructed full group.

The second audit defect is fixed without rewriting historical evidence. `magma_elapsed_seconds` and the legacy runtime-dependent canonical field are excluded from the mathematical Aut content hash. The required stable content SHA-256 is the hostile-audit lock:

`7aa6c9be4a91a25549950e1e45c2349146c6ea4cd035ff9133b41e9de3032bc3`.

Scope firewall:

```text
AUDIT_STATUS=PENDING
D16_B6_TRAVERSAL_CERTIFICATION_GATE_ONLY=true
FULL_D16_G0_ROW_COMPLETE=false
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false
R29_LG2_NUMERICAL_COMPONENT_COMPLETE=false
R29_LG2=NOT_DISCHARGED
G10_LOWGENUS_PICARD=AMBER
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
```

If this unit passes CI, stop for hostile `Stage32-audit`. Only after audit PASS may the controller advance to `32-18B-D16-AUT-CANONICAL-BOUNDED-PRODUCTION`.
