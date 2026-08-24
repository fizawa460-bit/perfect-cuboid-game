# Stage33-02 — BR0A integral Picard / saturation production result

```text
STAGE33_UNIT=33-02
UNIT_STATUS=AUDIT_REQUIRED
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
PREREQUISITE_UNITS=[33-01]
PREREQUISITES_ALL_CLOSED=true
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Exact production result

The initial direct Magma-online materializer reached the full 72-component boundary map but failed only on a backend-specific `Invariants(ModTupRng)` print call. No mathematical credit was taken from that failed run.

The production repair uses the already-audited Stage32 primitive Picard core through the explicit adapter in `cross-stage-picard-adapter.md`. The source identity is exact: the Stage32 core and frozen Stage29 BR0A receiver both use the same pinned Testa--Stoll source and the same unreordered class indices. The physical boundary is exactly rows

```text
1..24, 93..140
```

of the 140 known classes.

Run `32685802105` reconstructs the exact `72 x 64` map

```text
Div_D -> Pic(Sbar)
```

and independently performs exact integer Smith/Hermite computations. The run completed successfully with

```text
BOUNDARY_COMPONENT_COUNT = 72
PIC_RANK                 = 64
BOUNDARY_IMAGE_RANK      = 58
UNIT_KERNEL_RANK         = 14
PICARD_OPEN_FREE_RANK    = 6
SATURATION_INDEX         = 4
COKERNEL_TORSION         = [2,2]
```

Thus, before hostile audit, the exact computed quotient has abstract abelian-group shape

```text
Pic(Sbar) / im(Div_D)  ~=  Z^6  +  Z/2  +  Z/2.
```

This is an integral statement; no rational-rank substitute is used.

## Exact maps and certificates

The adapter reconstructs and checks:

```text
M              = 72 x 64 boundary-to-Picard matrix
M*G            = boundary restriction/pairing against the primitive Picard basis
M*G*M^T        = complete 72 x 72 boundary intersection matrix
ker_Z(M)       = exact rank-14 unit divisor-relation lattice
SNF(M)         = exact saturation / quotient torsion certificate
```

The direct Stage32 raw pairings are independently required to match `M*G` on all 72 selected boundary rows.

CI evidence:

```text
workflow_run             = 32685802105
workflow_conclusion      = success
certificate_sha256       = 2e365c273f2aae44adb7a871c864fa55d19a95336686b13a5eef245175f8bcd1
artifact_id              = 9505606017
artifact_zip_sha256      = ad4c4a2b041540aeb5ffaf5d511c9e866291d500acc8dfca0c1a9d2d8dccb40e
```

## Gate state

All finite production data required by BR0A are now materialized, but the strict Stage33 contract does not allow downstream release before hostile audit.

```text
EXACT_DIVISOR_LATTICE_CERTIFIED=true
INTEGRAL_SATURATION_CERTIFIED=true
INTERSECTION_MAPS_CERTIFIED=true
RESTRICTION_MAPS_REQUIRED_DOWNSTREAM_CERTIFIED=true
REPRODUCIBLE_CAS_MANIFEST=true
UNRESOLVED_UNKNOWN_IN_SCOPE=0
BR0A=CLAIMED_DISCHARGED_PENDING_HOSTILE_AUDIT
HOSTILE_AUDIT=PENDING
UNIT_STATUS=AUDIT_REQUIRED
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
STAGE33_PROGRESS=1/11
```

`STAGE33_PROGRESS=1/11` counts the already audited/merged `33-01` only. Stage33-02 itself does not increment the progress numerator until audit PASS.

If hostile audit passes, `33-02` becomes CLOSED and releases `33-03` and `33-04`.

```text
NEXT_EXPECTED_COMMAND=Stage33-audit
```
