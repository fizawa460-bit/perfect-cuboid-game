# Stage29 num1 mainline integration

```text
TASK=Stage29-num1-mainline-integration
SOURCE_PR=1289
SOURCE_STATUS=MERGED_MAIN
ROLE=IMPORT_EXACT_FINITE_NUMERICAL_RESULT_INTO_STAGE29_MAINLINE
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
PERFECT_CUBOID_CONCLUSION=NONE
```

## Imported facts

The merged Stage29-num1 track supplies an exact finite census of the primitive canonical Euler-cuboid population `M3(B)` under the same physical Euclidean cutoff used by the Stage20/28/29 program.

The mainline now records the exact checkpoints

```text
B=1e6   M3=219
B=5e6   M3=480
B=1e7   M3=656
B=5e7   M3=1298
B=1e8   M3=1757
B=2e8   M3=2339
B=5e8   M3=3331
```

and the exact finite endpoint observation

```text
P(B)=0 for B<=5e8
```

under the matching primitive/canonical physical contract.

The census is complete for the requested checkpoints, uses exact integer arithmetic, and has an independent exhaustive-table cross-check over 3556 aligned Resta/Helenius OEIS records.

## Mainline interpretation

This integration deliberately changes no asymptotic theorem and no Stage29 endpoint conclusion.

The finite ledger is now a first-class Stage29 input for coverage/regression work, especially `29-08`, and for later endpoint-family diagnostics. It is not used to infer the true exponent of `M3`, eventual ordering of `M3/N2`, or perfect-cuboid nonexistence.

Canonical mainline entry points:

- `stages/stage29/numerical-ledger.md`
- `stages/stage29/numerical-ledger.json`
- source result `stages/stage29/num1/result.md`
- source manifest `stages/stage29/num1/data/m3_census_manifest.json`

```text
STAGE29_NUM1_MAINLINE_IMPORTED=true
M3_5E8=3331
P_FINITE_ZERO_THROUGH_B=500000000
FINITE_DATA_IS_NOT_ASYMPTOTIC_THEOREM=true
P_GLOBAL_ZERO_THEOREM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
NEXT_EXPECTED_COMMAND=Stage29-audit
```
