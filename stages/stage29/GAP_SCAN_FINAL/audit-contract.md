# Stage29 GAP_SCAN_FINAL — adversarial audit contract

Audit this terminal gap scan independently. Do not trust the submitted 13-kernel claim merely because it matches 29-16.

## 1. Fresh source state

Fresh-read:

- merged 29-16 audit state and active-kernel ledger;
- 29-16 inactive inventory;
- 29-15 post-Work audit state;
- `SR-ARSENAL-24.md`, `SR-ARSENAL-25.md` and `PAUSE_AND_RETURN_STAGE27_2026-08-20.md`;
- Stage29-10/11/12/13/14 route conclusions as needed.

Confirm the starting inventory:

```text
SOURCE_FRONTIER_COUNT=46
CLASS1_CLOSED=6
CLASS2_ACTIVE=13
CLASS3_ACTIVE=11
CLASS4_DORMANT=16
COMPRESSED_KERNEL_COUNT=13
CLASS2_KERNELS=4
CLASS3_KERNELS=9
```

## 2. Hidden Class-1 challenge

PASS is forbidden if any current Class-2/3/4 item is actually finite, tractable now, route-enabling/decisive, and unexecuted.

Rechallenge especially:

- `K16-C2-LOWGENUS-PICARD-PRODUCTION`;
- `K16-C2-MODULAR-S4-ACTION`;
- `K16-C2-BRAUER-EXPLICIT-CHAIN` (dependency DAG, not linear chain);
- `K16-C2-EXT-E-INTEGRAL-CERTIFICATION`.

If a hidden Class-1 task is found, execute it on this same PR, update the inventory, and re-audit. Do not defer it to 29-17.

Required:

```text
HIDDEN_CLASS1_PENDING_COUNT=0
```

for PASS.

## 3. StructureRadar reverse mapping

Independently test the submitted absorption of cards 161,162,163,164,165,166,167,168,169,170,171,173,174,216,222,223.

Do not create a new kernel merely because a card has a distinct historical name. Create/reopen one only if its first missing mathematical statement is genuinely distinct from the 13-kernel surface.

In particular:

- same-measure/selector/Gaussian/reciprocal cards must not be transferred from larger ambient measures to primitive canonical `M3` without the exact conditional adapter;
- moving-fiber cards must not be replaced by fixed-fiber Chabauty/rank calculations;
- `SR-STR-216` remains an exactly-two/no-space-diagonal ambient theorem unless a legal final-host transfer is proved.

## 4. Dormant reactivation challenge

For all 16 Class-4 entries, check whether Ford, Creutz--Viray, exact Beauville squareclasses, descent=etale-Brauer, or 29-16's dependency compression actually satisfies a recorded reactivation trigger.

If yes, reopen the exact receiver and classify it correctly. Otherwise require

```text
DORMANT_REACTIVATED_COUNT=0.
```

## 5. Fresh theorem search

Repeat a narrow current primary-source search through 22 August 2026 for the nine Class-3 theorem species:

```text
ENDPOINT-EFFECTIVE-RATIONAL-POINT
CAMPEDELLI-UNIFORM-TORSOR
BEAUVILLE-ONE-STEP-DESCENT
QWEB-CLIFFORD-OBSTRUCTION
M3-LOCAL-TO-GLOBAL
PESCH-EXPONENT-ONE
MOVING-FIBER-ARITHMETIC
EXT-C-PRIMITIVE-DIVISOR
TERMINAL-P-OVER-M3
```

Search absence is not novelty. If an exact theorem match is found, apply it now and change the frontier.

For Peschmann, inspect the theorem/proof body rather than relying on potentially overcompressed abstract wording. Do not promote finite verified samples to the universal exponent-one theorem.

## 6. External claimed proofs

### Taha Muhammad

Read the latest available 2026 working-paper version. Verify whether the displayed complete-square argument really makes the invalid implication identified by the submission. If a later version supplies a valid missing universal argument, repair the disposition.

### Maximus Shlygin

Attempt to source-lock the full primary manuscript behind the Synapse/Zenodo claim. If successful, audit the actual proof rather than its abstract.

At minimum test:

1. local-model definition and map to the physical endpoint;
2. branch-admission completeness for an arbitrary rational/integral endpoint point;
3. higher-order/local-support completeness beyond degree-three/tangent data;
4. coverage of all endpoint components/branches;
5. compatibility with the known nonempty geometric endpoint surface.

If full text cannot be source-locked, keep it quarantined with no theorem credit. Lack of access is not a mathematical refutation.

## 7. Decision hierarchy firewall

Verify that only `K16-C3-PESCH-EXPONENT-ONE` currently has an already-audited statement of the form

```text
IF THIS EXACT NEW THEOREM IS PROVED -> PERFECT CUBOID NONEXISTENCE.
```

Do not promote:

```text
P/M3 -> 0
```

to nonexistence.

Do not treat a completed finite Brauer computation as endpoint emptiness unless the resulting physical adelic/etale-Brauer set is actually certified empty.

## 8. Required audit output

Create `stages/stage29/GAP_SCAN_FINAL/audit.md` and repair this same PR if needed.

```text
AUDIT_VERDICT=PASS|PASS_AFTER_REPAIR|FAIL
GAP_SCAN_FINAL_COMPLETE=true|false
SOURCE_FRONTIER_COUNT=<integer>
FINAL_ACTIVE_KERNEL_COUNT=<integer>
FINAL_CLASS2_KERNEL_COUNT=<integer>
FINAL_CLASS3_KERNEL_COUNT=<integer>
HIDDEN_CLASS1_FOUND=true|false
HIDDEN_CLASS1_PENDING_COUNT=<integer>
NEW_ACTIVE_RECEIVER_FOUND=true|false
NEW_ACTIVE_KERNEL_FOUND=true|false
NEW_DECISIVE_GLOBAL_THEOREM_FOUND=true|false
DORMANT_REACTIVATED_COUNT=<integer>
PESCH_E1_CURRENTLY_PROVED=true|false
PESCH_E1_IF_PROVED_IMPLIES_NONEXISTENCE=true|false
TAHA_CLAIM_DISPOSITION=<value>
SHLYGIN_CLAIM_DISPOSITION=<value>
ATTACK_ROUTE_COUNT=<integer>
GREEN_ROUTE_COUNT=<integer>
AMBER_ROUTE_COUNT=<integer>
P_OVER_M3_SCALE_KNOWN=true|false
TARGETED_BACKFLOW_REQUIRED=true|false
ROADMAP_REWRITE_REQUIRED=true|false
MERGE_ALLOWED=true|false
ADVANCE_ALLOWED=true|false
NEXT_ITEM=<item or blocker>
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

PASS requires no hidden pending Class-1 task and no unaccounted active theorem/receiver.

If the submitted frontier survives:

```text
NEXT_ITEM=29-17_STAGE29_FINAL_HANDOFF_AND_CLOSE
```

Do not merge during audit.
