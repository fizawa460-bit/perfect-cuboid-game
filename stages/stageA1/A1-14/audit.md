# StageA1 independent audit — A1-14

```text
AUDIT_VERDICT=PASS
AUDITED_TASK=STAGEA1-A1-14-R01
AUDITED_SUBMISSION_HEAD=e82191a1fa2f448ab158e4277722d651ea6a2105
BASE_MAIN_AUDIT=PASS
BASE_MAIN=949e201993ad9008d12117087bd67b91c51a24d8
BASE_MAIN_IS_A1_13_MERGE=PASS
TRUE_DELTA1_RECEIVER_FIREWALL_AUDIT=PASS
P7_GOOD_REDUCTION_INHERITED_AUDIT=PASS
FORMAL_PARAMETER_AUDIT=PASS_tau=-x/y
V7_TAU_63P_AUDIT=PASS_2
TAU_63P_OVER_49_MOD7_AUDIT=PASS_2
V7_TAU_441P_AUDIT=PASS_3
SECOND_DEPTH_FORMAL_GROUP_SCALING_AUDIT=PASS
ALL_24_NONCENTRAL_LIFTS_DIRECT_AUDIT=PASS
CENTER_0_ALLOWED_K_AUDIT=PASS_0_1_2_4
CENTER_1_ALLOWED_K_AUDIT=PASS_0_3_5_6
CENTER_2_ALLOWED_K_AUDIT=PASS_0_3_5_6
CENTER_MINUS1_ALLOWED_K_AUDIT=PASS_0_1_2_4
ALLOWED_MOD441_AUDIT=PASS_16_CLASSES
ALLOWED_MOD441_INVOLUTION_AUDIT=PASS_N_TO_1_MINUS_N
DEPTH3_K0_CLASSES_RETAINED_CONSERVATIVELY=true
ALLOWED_MOD441_INTERPRETATION=SAFE_NECESSARY_SIEVE_NOT_EXACT_LOCAL_SOLUBILITY_CLASSIFICATION
A1_13_CRT_RECOMPUTATION_AUDIT=PASS_256_MOD_3416490
A1_14_GLOBAL_MODULUS_AUDIT=PASS_23915430
A1_14_PRETEST_LIFTS_AUDIT=PASS_1792
A1_14_SURVIVING_CLASS_COUNT_AUDIT=PASS_1024
A1_14_DENSITY_MULTIPLIER_AUDIT=PASS_4_OVER_7
A1_14_SURVIVING_CLASS_SHA256_AUDIT=PASS
STRICT_RECEIVER_NARROWING_AUDIT=PASS
CONTROLLER_HISTORY_PRESERVATION_AUDIT=PASS
COMPLETE_DELTA1_CLOSURE=false
FAMILY_SPECIFIC_ONLY_FIREWALL_AUDIT=PASS
UNIVERSAL_REVERSE_MAP_AUDIT=NOT_PROVED
NEW_ARBITRARY_CUBE_CONSTRAINT_AUDIT=NOT_PROVED
PERFECT_CUBOID_FOUND=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
EXACT_HEAD_STAGEA1_CI=NOT_CONFIGURED
INDEPENDENT_VERIFY_RECOMPUTATION=PASS
REPAIR_REQUIRED=false
READY_TRANSITION=COMPLETED
AUDIT_PERSISTENCE_STATUS=COMMITTED
MERGE_ALLOWED=true
NEXT_TARGET=A1-15_DELTA1_THIRD_7ADIC_OR_DENOMINATOR_RECURRENCE
NEXT_EXPECTED_COMMAND=StageA1-main-batch
AUDITED_AT=2026-08-20T11:32+09:00
```

## Audit notes

The A1-14 mathematics is accepted. Independent exact rational group-law recomputation reproduces `v_7(tau(63P))=2`, `(tau(63P)/49) mod 7 = 2`, and `v_7(tau(441P))=3`.

The four center computations were also checked directly rather than relying only on the submitted formal-group scaling argument. For every noncentral second-depth lift `n=center+63k`, `k=1,...,6`, the exact rational values of `z+2` and `z-2` reproduce the claimed valuation/unit pattern. The resulting retained lift sets are `{0,1,2,4}`, `{0,3,5,6}`, `{0,3,5,6}`, `{0,1,2,4}` at centers `0,1,2,-1` respectively.

The `k=0` classes are deliberately retained because they lie one 7-adic level deeper. Accordingly, the 16 classes modulo 441 are the exact output of this safe necessary-condition sieve, not a claim that all 16 are locally or globally soluble.

The global arithmetic was independently recomputed: the audited A1-13 set has 256 classes modulo 3416490; lifting to `lcm(3416490,441)=23915430` gives 1792 classes before the new test; 1024 survive, a density factor `4/7`. The sorted-set SHA-256 is `ca2472c7077bac47b0cced38211ea26aa20223dd65e7f2c548d78cca93117251`, and the set is invariant under `n -> 1-n`.

No A1-14-specific GitHub Actions workflow is configured on the audited submission head, so CI is recorded as not configured rather than inferred from unrelated workflows.
