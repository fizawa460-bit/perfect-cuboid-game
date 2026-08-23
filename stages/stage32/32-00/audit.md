# Stage32-00 hostile audit — roadmap and source lock

AUDIT_VERDICT = PASS_AFTER_BOUNDED_RECEIVER_SEMANTICS_REPAIR

## What was independently checked

- Stage31 is closed on main with post-Stage31 frontier `active=11, Class2=2, Class3=9`.
- The selected kernel matches the frozen Stage29-16 entry: `K16-C2-LOWGENUS-PICARD-PRODUCTION`, children `R29-LG2`, `R29-LG2-EFF`, `R29-LG2-MB`, parent `G10-LOWGENUS-PICARD`.
- The Stage29 finite-search contract really is restricted to integral nonexceptional curves whose normalization maps bijectively to the singular image; therefore the `d<=176/192` caps are unibranch-only and a separate multibranch ledger is mandatory.
- The upstream Stoll repository/commit/blob exist. The frozen `cuboids.magma` constructs the 48 singular points, the rank-64 known-curve lattice, `PicL`, `HinPicL`, automorphism/Galois actions, K3 quotient/lifts, and the degree-6 lift helper. The lift kernel has rank 44, and the code estimates close-vector volume using `bound^(Dimension/2)`, hence exponent 22.
- The upstream code itself explicitly says the known curves have rank 64 and conditions full generation on the separate theorem input; Stage32 preserves that attribution firewall.

## Bounded semantic repair

The submitted roadmap said that `32-01` could set `R29_LG2=DISCHARGED` after the numerical orbit census alone. That is too strong relative to the frozen Stage29 `finite-search-contract.md`: its completion criterion for `R29-LG2` also requires every numerical survivor to be disposed by effectivity/boundary/explicit-carrier evidence.

Therefore the authoritative Stage32 execution semantics are:

```text
32-01:
  FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=true
  R29_LG2_NUMERICAL_COMPONENT=COMPLETE
  R29_LG2=NOT_YET_DISCHARGED

32-02, after UNKNOWN_EFFECTIVITY_SURVIVOR_COUNT=0:
  R29_LG2=DISCHARGED
  R29_LG2_EFF=DISCHARGED
```

This changes only the intermediate closure label, not the mathematics, windows, execution order, or final kernel close condition.

## Roadmap verdict

The large checkpointed-unit strategy is accepted. A raw monolithic `CloseVectors` sweep is not authorized. Runtime, memory, missing CAS, or an unimplemented pruning method remain Class-2/tool walls; Class 3 requires an exact missing theorem after finite work is exhausted.

The following firewalls remain mandatory:

```text
NUMERICAL_SURVIVOR != EFFECTIVE_CURVE
UNIBRANCH_CENSUS != MULTIBRANCH_CENSUS
LOWGENUS_CARRIER_CENSUS != ENDPOINT_NONEXISTENCE
ISOLATED_RATIONAL_POINTS_EXCLUDED=false
G10_LOWGENUS_PICARD=AMBER
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

Final state:

```text
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS_AFTER_BOUNDED_RECEIVER_SEMANTICS_REPAIR
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=32-01_PRODUCTION_ENUMERATOR_AND_COMPLETE_UNIBRANCH_NUMERICAL_CENSUS
NEXT_EXPECTED_COMMAND=Stage32-main-batch
```
