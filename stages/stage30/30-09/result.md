# Stage30-09 — final certificate and independent checker

Status: `SUBMITTED_PENDING_STAGE30_FINAL_HOSTILE_AUDIT`.

This unit consolidates the audited Stage30 modular-action work into one immutable-input reproducibility surface. It does not reopen mathematical search and does not pre-grant Stage30 closure.

## Materialized Stage30-08 audit

PR #1335 received hostile-audit verdict

```text
PASS_R29_KUM5_NONOBSTRUCTIVE_ADAPTER_CLOSURE
```

before merge, but its submitted controller still contained `PENDING` state. Stage30-09 materializes that already-completed audit in:

- `stages/stage30/30-08/audit.md`
- `stages/stage30/30-08/audit-state.json`

No second audit or new theorem credit is introduced.

## Final reproducibility surface

Stage30-09 provides the roadmap-required surface:

```text
input-manifest.json
action-tables.json
equivariant-map.json
galois-cocycle.json
defect-classification.json
final-certificate.json
verify_stage30.py
```

The JSON files are compact final certificates/reference wrappers around immutable audited source artifacts. The final checker does not invoke any earlier Stage30 verifier.

`input-manifest.json` pins immutable mathematical artifacts by Git blob SHA. Mutable `controller.json` is deliberately not pinned, preventing legitimate later state transitions from invalidating the mathematical certificate.

## Independent reconstruction performed by `verify_stage30.py`

The checker independently:

1. verifies all immutable Git-blob pins;
2. reconstructs `SL2(Z/4)` and `PSL2(Z/4)` from matrices, checking orders `48` and `24`;
3. compares the reconstructed 24 modular matrices with the frozen Task-A table;
4. reconstructs `V_mod` as the mod-2 identity kernel and requires exactly `g04,g06,g12,g14`;
5. checks the common-model branch projection has kernel order 4 and image `S3` of order 6;
6. binds the source-derived `c_sigma=delta_a3` specification to the audited all-24 semilinear certificate and checks all 24 certificate rows are PASS plus the 576 multiplication certificate;
7. regenerates all eight `K8` elements from `A in sl2(F2)`, re-derives `kappa=I+4A mod 8` and `phi(A)=(a+b,a+c,a)`, and checks every endpoint sign image;
8. recomputes the Hamming-weight multiplicities `1,3,3,1`, eight singleton marked Q-descent classes, and zero eliminations;
9. checks physical-open noncusp/stabilizer-free scope and the materialized Stage30-08 hostile audit;
10. checks route/firewall state.

Expected terminal output includes:

```text
STAGE30_FINAL_CERTIFICATE=PASS
PSL2_Z4_ORDER=24
V_MOD_ORDER=4
SEMI_LINEAR_24_OF_24=PASS
K8_DEFECT_ROWS=8
MARKED_Q_DESCENT_CLASSES=8
DEFECT_ELIMINATION_COUNT=0
R29_KUM5=DISCHARGED_NONOBSTRUCTIVE
K16_C2_MODULAR_S4_ACTION=CLOSED_PENDING_STAGE30_FINAL_AUDIT
Q11_MODULAR=AMBER
```

## Submitted final mathematical state

```text
R29_KUM5=DISCHARGED_ACTION_COCYCLE_ADAPTER_ZERO_DEFECT_ELIMINATION
K16_C2_MODULAR_S4_ACTION=CLOSED_COMPUTATIONAL_KERNEL
DEFECT_ELIMINATION_COUNT=0
SMALLER_RESIDUAL_CLASS2_LEAF=NONE
NEW_CLASS3_THEOREM_GATE=NONE
Q11_MODULAR=AMBER
ROUTE_COLOR_CHANGED=false
PHYSICAL_ENDPOINT_EXCLUSION_PROVED=false
```

Prospective research-OS delta after final Stage30 audit:

```text
ACTIVE_KERNEL_COUNT=12
CLASS2_KERNEL_COUNT=3
CLASS3_KERNEL_COUNT=9
```

Historical Stage29 handoff artifacts remain unchanged.

## Final gate

Stage30-09 does **not** close Stage30 itself. The final unit is Stage30-10 hostile audit.

```text
AUDIT_REQUIRED=true
AUDIT_VERDICT=PENDING_STAGE30_FINAL_AUDIT
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_ITEM=30-10_FINAL_HOSTILE_AUDIT_AND_CLOSE
NEXT_EXPECTED_COMMAND=Stage30-audit
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
