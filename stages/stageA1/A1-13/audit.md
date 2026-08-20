# StageA1 independent audit — A1-13

```text
AUDIT_VERDICT=PASS_WITH_CONTROLLER_REPAIR
AUDITED_TASK=STAGEA1-A1-13-R01
AUDITED_SUBMISSION_HEAD=0a0172e0e507810a0971b4320d793d87c814b9d2
BASE_MAIN_AUDIT=PASS
BASE_MAIN=ffb718eb2cb15cb91e36360dca41f703624d2e52
BASE_MAIN_IS_A1_12_MERGE=PASS
TRUE_DELTA1_RECEIVER_FIREWALL_AUDIT=PASS
P7_GOOD_REDUCTION_INHERITED_AUDIT=PASS
FORMAL_PARAMETER_AUDIT=PASS_t=-x/y
P9_EXACT_MULTIPLE_AUDIT=PASS
V7_T_9P_AUDIT=PASS_1
T_9P_OVER_7_MOD7_AUDIT=PASS_2
P63_FORMAL_DEPTH_AUDIT=PASS_V7_2
ORD_P_MOD7_AUDIT=PASS_9
ORD_P_MOD49_AUDIT=PASS_63
Z_POLE_AT_O_AUDIT=PASS_SIMPLE
Z_POLE_AT_P_AUDIT=PASS_SIMPLE
Z_MINUS_2_ZERO_AT_2P_AUDIT=PASS_SIMPLE
Z_MINUS_2_ZERO_AT_MINUS_P_AUDIT=PASS_SIMPLE_AFTER_CANCELLATION
FIRST_ORDER_VALUATION_TABLE_AUDIT=PASS
ALLOWED_MOD63_AUDIT=PASS_0_1_2_MINUS1
A1_12_CRT_RECOMPUTATION_AUDIT=PASS_384_MOD_3416490
A1_13_CRT_FILTER_AUDIT=PASS_256_MOD_3416490
A1_13_SURVIVING_CLASS_SHA256_AUDIT=PASS
A1_13_INVOLUTION_SYMMETRY_AUDIT=PASS
STRICT_RECEIVER_NARROWING_AUDIT=PASS
COMPLETE_DELTA1_CLOSURE=false
CONTROLLER_HISTORY_PRESERVATION_AUDIT=FAIL_THEN_REPAIRED
CONTROLLER_REGRESSION=historical audited fields were dropped while routing A1-13
AUDIT_REPAIR_SCOPE=controller-only historical-ledger restoration plus audit lifecycle transition
FAMILY_SPECIFIC_ONLY_FIREWALL_AUDIT=PASS
UNIVERSAL_REVERSE_MAP_AUDIT=NOT_PROVED
NEW_ARBITRARY_CUBE_CONSTRAINT_AUDIT=NOT_PROVED
PERFECT_CUBOID_FOUND=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
EXACT_HEAD_STAGEA1_CI=NOT_CONFIGURED
INDEPENDENT_VERIFY_RECOMPUTATION=PASS
REPAIR_REQUIRED=false
READY_TRANSITION=COMPLETED
NEXT_TARGET=A1-14_DELTA1_DEEPER_7ADIC_OR_DENOMINATOR_RECURRENCE
NEXT_EXPECTED_COMMAND=StageA1-main-batch
AUDITED_AT=2026-08-20T11:21+09:00
```

## Audit notes

The A1-13 mathematics is accepted. Independent exact rational group-law recomputation reproduces the submitted `9P`, gives `v_7(t(9P))=1`, `(t(9P)/7) mod 7 = 2`, and `v_7(t(63P))=2`. Hence the order of `P` grows from 9 modulo 7 to 63 modulo 49.

The divisor analysis is also sound: `z` has simple poles at `O` and `P`; `z-2` has simple zeros at `2P` and `-P`, with the latter obtained after the single cancellation in the displayed line identity. The six noncentral lifts in each old class modulo 9 therefore have odd 7-adic valuation in at least one required square function. This gives the safe necessary condition `n mod 63 in {0,1,2,-1}`.

The A1-12 CRT set was independently recomputed as 384 classes modulo 3416490. Filtering by the new mod-63 condition gives exactly 256 classes and reproduces SHA-256 `f08de28f142bf79dd88bbee5725e87c4dd0692091d0e85a645275dc1bfca6fc0`; the set remains invariant under `n -> 1-n`.

One non-mathematical regression was found in `controller.json`: the A1-13 routing rewrite dropped several already-audited historical ledger fields from A1-8/A1-11/A1-12. Those facts are still valid and are restored by the audit repair. No A1-13 theorem statement requires correction.
