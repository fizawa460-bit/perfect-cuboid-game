# Stage30 roadmap audit contract

Audit target: the Stage30 roadmap/controller/Codex handoff design itself, before Stage30-01 execution begins.

## Fresh-read requirements

Audit must fresh-read:

```text
stages/stage30/ROADMAP.md
stages/stage30/controller.json
stages/stage30/codex-handoff-contract.md
```

and independently compare them against the merged Stage29 records:

```text
stages/stage29/29-02g/*
stages/stage29/29-02ha/*
stages/stage29/29-11/*
stages/stage29/29-15/*
stages/stage29/29-16/active-kernel-ledger.json
stages/stage29/29-17/final-handoff.json
```

## Hard questions

1. Is Stage30 attacking exactly `K16-C2-MODULAR-S4-ACTION / R29-KUM5`, without reopening discharged `MOD1C` or `MOD1D` work?
2. Does the roadmap preserve the distinction between the concrete arrangement action and the modular residual action?
3. Does it preserve the Q versus Q(i) field-of-definition split?
4. Does it avoid treating `PSL2(Z/4) ~= S4` as the desired adapter?
5. Does it avoid treating the four ordinary K8 conjugacy classes `1,3,3,1` as already-certified arithmetic endpoint strata?
6. Is the Stage29-15 result `sigma acts trivially on K8` consumed correctly without overclaiming that `R29-KUM5` is therefore closed?
7. Does the targeted Arsenal requirement improve anti-miss coverage without reopening the entire Stage14/StructureRadar loop?
8. Are all Codex-owned tasks finite/exact enough to delegate safely?
9. Are the mathematically semantic steps (QI adapter, Q descent cocycle, physical endpoint adapter) retained under ChatGPT/audit ownership rather than outsourced blindly?
10. Can the roadmap reclassify a newly exposed leaf to Class 3 if a new theorem is actually required?
11. Is there any hidden Class-1 finite task that should be executed before the proposed Codex sequence?
12. Are the two user-facing commands sufficient to represent every controller state, including waiting for Codex output?

## Roadmap repair policy

Bounded corrections should be applied on the same roadmap PR.  If audit finds that the core target is not actually a Class-2 finite/action adapter problem, mark the roadmap `FAIL_RECLASSIFY_REQUIRED` rather than cosmetically repairing the sequence.

## PASS hard gates

```text
TARGET_KERNEL_EXACT=true
DISCHARGED_RECEIVER_REPLAY_COUNT=0
ABSTRACT_S4_SHORTCUT_ALLOWED=false
Q_QI_FIELD_SPLIT_PRESERVED=true
ORDINARY_K8_ORBIT_OVERCLAIM=false
CODEX_PROMPT_GENERATION_INCLUDED=true
CODEX_OUTPUT_AUTO_CREDIT=false
TARGETED_ARSENAL_READ_INCLUDED=true
FULL_ARSENAL_REPLAY_REQUIRED=false
USER_COMMAND_COUNT=2
RECURSIVE_1234_RECLASSIFICATION_ENABLED=true
HIDDEN_CLASS1_CARRY_FORWARD_ALLOWED=false
```

## Required audit status block

```text
AUDIT_VERDICT=PASS|PASS_AFTER_REPAIR|FAIL
TARGET_KERNEL=K16-C2-MODULAR-S4-ACTION
TARGET_RECEIVER=R29-KUM5
ROADMAP_SUBSTAGE_COUNT=<integer>
CHATGPT_OWNED_UNIT_COUNT=<integer>
CODEX_OWNED_UNIT_COUNT=<integer>
CODEX_PROMPT_GENERATION_STAGE_COUNT=<integer>
USER_COMMAND_COUNT=<integer>
TARGETED_ARSENAL_READ_REQUIRED=true|false
FULL_ARSENAL_REPLAY_REQUIRED=true|false
DISCHARGED_RECEIVER_REPLAY_COUNT=<integer>
HIDDEN_CLASS1_PENDING_COUNT=<integer>
NEW_THEOREM_ASSUMED=false
MERGE_ALLOWED=true|false
ADVANCE_ALLOWED=true|false
NEXT_ITEM=<item>
NEXT_EXPECTED_COMMAND=<command>
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

If PASS, next item is

```text
30-01_SOURCE_LOCK_AND_ACTION_OBJECT_FREEZE
```

and the next command is

```text
Stage30-main-batch
```
