# Stage29-16 — adversarial audit contract

Audit the residual-receiver compression independently. This stage is bookkeeping-sensitive: a false merge can hide real work, while a false split can make the remaining research look larger than it is.

## 1. Reconstruct the 29-15 authoritative source inventory

Read the merged post-Work 29-15 state, especially:

```text
stages/stage29/29-15/audit-state.json
stages/stage29/29-15/post-work-triage.json
stages/stage29/29-15/post-work-audit.md
```

Independently verify the source census:

```text
TOTAL=46
CLASS1=6
CLASS2=13
CLASS3=11
CLASS4=16
```

Do not trust 29-16's counts before reconstructing them from 29-15.

## 2. Closed Class 1

Verify the six archived Class-1 entries are genuinely discharged and have no unresolved child hidden inside the same receiver:

```text
R29-BEAU2A
R29-KUM-LOC2-2
R29-MOD1C
R29-MOD1D
R29-BEAU1B
R29-BR-LINE9
```

A later dependent receiver may use their result, but the discharged calculation itself must not be counted as active work again.

## 3. Active source-entry accounting

The active source inventory is exactly the 24 Class-2/Class-3 entries.

Class 2:

```text
R29-LG2
R29-LG2-EFF
R29-LG2-MB
R29-CAMP4
R29-KUM5
R29-K3-RULED2
R29-BR0A
R29-BR0B
R29-BR0G
R29-BR2A
R29-BR2B
R29-NF-PHYS2
R29-EXT-CHANG-E
```

Class 3:

```text
R29-PI1-OPEN
R29-CAMP2
R29-BEAU1C
R29-BEAU2
R29-BEAU3
R29-QWEB-CLIFFORD
R29-KUM-LOC3
R29-PESCH-E1
R29-FIB2
R29-EXT-CHANG-C
TERMINAL-P-OVER-M3
```

Verify every one appears in exactly one execution kernel in `active-kernel-ledger.json`. Shared parent-route provenance is allowed; duplicate execution ownership is not.

A PASS requires:

```text
ACTIVE_SOURCE_ENTRY_COUNT=24
ACTIVE_SOURCE_ENTRY_UNMAPPED_COUNT=0
ACTIVE_SOURCE_ENTRY_DUPLICATE_MAPPING_COUNT=0
```

## 4. Challenge the four Class-2 kernel merges

### LOWGENUS-PICARD-PRODUCTION

Verify `LG2`, `LG2-EFF` and `LG2-MB` really form one production program and that none currently has a separate endpoint consequence.

Re-read 29-02c-LG2 and 29-10. If any modest bounded implementation now makes a child tractable with current tools, promote it to Class 1 and execute it on this same PR before PASS. Do not hide a tractable finite task inside a compressed Class-2 label.

### MODULAR-S4-ACTION

Verify `KUM5` is the only remaining active finite modular implementation after audited `MOD1C` and `MOD1D` closure. Confirm action/cocycle identification does not itself eliminate one of the eight marked defects.

### BRAUER-EXPLICIT-CHAIN

This is the most important hostile check.

Verify all eight children belong to one dependency chain rather than independent theorem species:

```text
CAMP4
K3-RULED2
BR0A
BR0B
BR0G
BR2A
BR2B
NF-PHYS2.
```

Re-read 29-02f, 29-11 and the post-Work 29-15 Creutz--Viray/Ford repairs. Confirm:

- `boundary_module_probe.m` is only a preflight until source-locked execution output is committed;
- the K_c ruled model and geometric Br[2] dimension two are already discharged;
- the missing Creutz--Viray `L_{c,E}` / `x-alpha` relation matrix, symbol basis and Q-action are still real finite work;
- the physical-open `UPic/Gersten` and local evaluation work is not replaced by the base seven-line Br[2] calculation;
- Campedelli compatibility genuinely consumes downstream two-primary classes and therefore need not be scheduled independently first.

If an existing repo artifact already materializes one of the claimed missing matrices/classes, execute the remaining bounded step now and repair the compression.

### EXT-E-INTEGRAL-CERTIFICATION

Confirm it is independent of the global Brauer chain and remains only a thin-family certification task.

## 5. Challenge the nine Class-3 kernel merges

For every Class-3 kernel, verify the first missing statement really is theorem-level rather than finite implementation.

### BEAUVILLE-ONE-STEP-DESCENT

This merge requires special care. Verify from the primary-source-checked 29-15 theorem import that on the exact smooth physical open:

```text
ordinary descent = etale-Brauer
iterated descent = ordinary descent.
```

Then verify `BEAU1C`, `BEAU2`, `BEAU3` are alternative/serial ways of solving the same remaining one-step open-twist arithmetic rather than independent stronger obstruction species.

Do not infer a finite twist set from these theorems.

### PESCH-EXPONENT-ONE

Reconfirm that the statement remains conjectural and that the audited Master-Hit coverage makes its implication genuinely global:

```text
IF R29-PESCH-E1 is proved as stated -> perfect cuboid nonexistence.
```

Do not grant theorem credit merely because it is narrow or computationally verified on large samples.

### M3-LOCAL-TO-GLOBAL and TERMINAL-P-OVER-M3

Keep these distinct. A legal M3 local-to-global theorem may yield a final-host density estimate, while the terminal ratio is the literal `P/M3` quantity. Neither is allowed to inherit an ambient `P2`/`M2+M3` density statement.

Also preserve the endpoint firewall:

```text
P/M3 -> 0 does not imply P=0.
```

### EXT-C

Confirm the residual all-multiples statement is genuinely a new primitive-divisor theorem after finite windows were exhausted, while its family coverage remains nonglobal.

## 6. Route-portfolio compression

Audit `route-portfolio.json` independently.

The historical colors must remain unless a new theorem changes them:

```text
10 AMBER
1 GREEN
0 RED parent routes.
```

Challenge the two execution merges:

```text
G10-K3-SIGN -> execution owner Q11-BRAUER
J12-JOINT-V4 -> no unique current execution kernel; terminal interaction carried by P/M3 unless a genuinely new joint theorem appears.
```

These are execution-owner merges only. They must not erase provenance, claim a parent route is solved, or reduce `ATTACK_ROUTE_COUNT` below 11.

A PASS requires the claim

```text
INDEPENDENT_EXECUTION_OWNER_ROUTE_COUNT=9
```

to be justified from current live kernels, not from aesthetics.

## 7. Dormant Class 4

Verify all sixteen Class-4 entries are present in `inactive-inventory.json` and every one has a concrete reactivation condition.

If any dormant receiver would now immediately enable an already-available endpoint-decisive theorem because of 29-15's new Ford/Creutz--Viray/descent inputs, reactivate and reclassify it before PASS.

A PASS requires:

```text
DORMANT_RECEIVER_COUNT=16
DORMANT_REACTIVATION_TRIGGER_MISSING_COUNT=0.
```

## 8. Decision-frontier audit

Check `decision-frontier.md` for logical overstatement.

In particular:

- `PESCH-E1` may be called a named theorem target with a direct nonexistence implication, but it is not proved;
- completing a Brauer/descent computation is not guaranteed to produce an obstruction;
- closing low-genus, modular-action, EXT-C or EXT-E work is not global endpoint closure;
- `P/M3->0` is not nonexistence;
- no ranking by probability, novelty or publishability is claimed.

## 9. No hidden Class 1

The 29-15 rule remains active at this compression boundary. If the audit discovers any currently tractable finite task incorrectly buried in a Class-2 kernel, execute it on this same PR and update all counts before PASS.

```text
HIDDEN_CLASS1_PENDING_COUNT must equal 0.
```

## 10. Required audit output

Create `stages/stage29/29-16/audit.md` and repair the same PR if needed.

Required final block:

```text
AUDIT_VERDICT=PASS|PASS_AFTER_REPAIR|FAIL
SOURCE_RECEIVER_OR_TERMINAL_FRONTIER_COUNT=<integer>
SOURCE_CLASS1_CLOSED_COUNT=<integer>
SOURCE_CLASS2_ACTIVE_COUNT=<integer>
SOURCE_CLASS3_ACTIVE_COUNT=<integer>
SOURCE_CLASS4_DORMANT_COUNT=<integer>
ACTIVE_SOURCE_ENTRY_COUNT=<integer>
ACTIVE_SOURCE_ENTRY_UNMAPPED_COUNT=<integer>
ACTIVE_SOURCE_ENTRY_DUPLICATE_MAPPING_COUNT=<integer>
COMPRESSED_ACTIVE_KERNEL_COUNT=<integer>
COMPRESSED_CLASS2_KERNEL_COUNT=<integer>
COMPRESSED_CLASS3_KERNEL_COUNT=<integer>
MIXED_EXECUTION_CLASS_KERNEL_COUNT=<integer>
HIDDEN_CLASS1_PENDING_COUNT=<integer>
DORMANT_RECEIVER_COUNT=<integer>
DORMANT_REACTIVATION_TRIGGER_MISSING_COUNT=<integer>
ATTACK_ROUTE_COUNT=<integer>
INDEPENDENT_EXECUTION_OWNER_ROUTE_COUNT=<integer>
MERGED_SUPPORT_ROUTE_COUNT=<integer>
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

A PASS must have zero unmapped/duplicate active entries, zero mixed-class kernels, zero hidden Class-1 pending tasks and zero missing dormant reactivation triggers.

If the compression survives, advance to `GAP_SCAN_FINAL`.
