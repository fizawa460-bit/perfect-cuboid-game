# Stage30 roadmap — fresh adversarial audit

```text
AUDITED_PR=1327
AUDIT_VERDICT=PASS_AFTER_BOUNDED_ORDERING_REPAIR
TARGET_KERNEL=K16-C2-MODULAR-S4-ACTION
TARGET_RECEIVER=R29-KUM5
```

## 1. Stage29 handoff lock

Fresh read of merged `stages/stage29/29-17/final-handoff.json` confirms that Stage29 is closed as an endpoint-synthesis phase, the perfect-cuboid problem remains open, and `K16-C2-MODULAR-S4-ACTION` is one of exactly four Class-2 post-Stage29 kernels. The authoritative 29-16 ledger gives this kernel exactly one child, `R29-KUM5`, under parent route `Q11-MODULAR`, with wall:

```text
action-level arrangement-to-modular S4 identification
compatible with the audited Q/Q(i) descent cocycles
```

and with the firewall that an abstract `S4` isomorphism does not close the receiver and no marked defect is eliminated merely by identifying the action.

Therefore Stage30 attacks an exact frozen post-Stage29 kernel and is a legitimate new research program rather than Stage29 bookkeeping.

## 2. Frozen modular/arrangement facts

The roadmap's starting facts match the merged Stage29 audits within scope:

```text
Aut_P2(D) ~= S4
Q-liftable base subgroup ~= S3, order 6
Q(i)-liftable base group ~= S4, order 24
Q line orbits = 3+3+1
Q(i) line orbits = 4+3
PSL2(Z/4) ~= S4
generic residual degree = 24
K8 = ker(SL2(Z/8)->SL2(Z/4)), |K8|=8
ordinary unmarked K8 conjugacy sizes = 1,3,3,1
R29-MOD1C=DISCHARGED_TRIVIAL_SIGMA_ACTION_ON_K8
MARKED_ARITHMETIC_DEFECT_CLASS_COUNT=8
R29-MOD1D=DISCHARGED_PHYSICAL_OPEN_NONCUSP_STABILIZER_FREE
R29-KUM5 remains open
```

The roadmap correctly preserves all load-bearing firewalls: generic degree 24 is not an everywhere-finite compactified map; ordinary `1,3,3,1` is not the arithmetic endpoint stratification; bare ordinary 8-congruence is not a rarity theorem; the Q/Q(i) field split remains explicit.

```text
DISCHARGED_RECEIVER_REPLAY_COUNT=0
ABSTRACT_S4_SHORTCUT_ALLOWED=false
Q_QI_FIELD_SPLIT_PRESERVED=true
ORDINARY_K8_ORBIT_OVERCLAIM=false
```

## 3. Targeted Arsenal policy

The required Arsenal/StructureRadar read is correctly targeted to S4/modular/M(4,8)/Q(i)/K8/descent/cocycle/Galois/marked-orbit material. It is not a full Stage14/StructureRadar replay. This is the right anti-miss policy after the Stage29 anti-loop close.

```text
TARGETED_ARSENAL_READ_REQUIRED=true
FULL_ARSENAL_REPLAY_REQUIRED=false
```

## 4. Codex delegation audit

The Codex contract is safe in overall shape:

- user command surface remains `Stage30-main-batch` and `Stage30-audit` only;
- prompts must be self-contained and source-locked;
- finite computation uses exact arithmetic;
- deterministic manifests and independent checkers are mandatory;
- Codex output never receives automatic theorem/adapter credit;
- semantic Q(i), Q-descent and physical-endpoint steps stay under ChatGPT/audit ownership.

The controller has 15 execution units:

```text
ROADMAP_SUBSTAGE_COUNT=15
CHATGPT_OWNED_UNIT_COUNT=10
CODEX_OWNED_UNIT_COUNT=5
CODEX_PROMPT_GENERATION_STAGE_COUNT=4
USER_COMMAND_COUNT=2
```

The two combined prose headings `30-06C / 30-07` and `30-09P / 30-09C` do not reduce the controller unit count.

## 5. Bounded ordering repair

One semantic ordering defect was found in the submitted roadmap.

Submitted Task B asked the pre-descent Q(i)-level equivariant search to check compatibility with the eight `K8` defects before Stage30-06 had derived the exact `Gal(Q(i)/Q)` semilinear/cocycle relation. That can create a circular notion of "compatibility": the arithmetic meaning of defect transport depends on the very descent adapter derived later.

The audited ordering is therefore:

```text
30-04P / 30-04C:
  exhaustive finite Q(i)-level equivariant identification only;
  K8 elements and the retained level-4 datum may be carried as frozen labels;
  no Q-descent or arithmetic-defect compatibility credit yet.

30-05:
  mathematically certify the Q(i)-equivariant adapter.

30-06:
  derive the exact Gal(Q(i)/Q) semilinear/cocycle relation.

30-06C:
  machine-check that exact cocycle/semilinear relation.

30-07:
  only then transport and classify all eight marked K8 defects through the audited adapter.
```

This repair is recorded authoritatively in `controller.json` under `audit_scope_overrides`. It changes no Stage29 theorem or target; it only removes a possible circular dependency.

```text
BOUNDED_REPAIR=SEPARATE_QI_EQUIVARIANT_SEARCH_FROM_Q_DESCENT_DEFECT_COMPATIBILITY_AND_SPLIT_30_06C_FROM_30_07
```

## 6. Hidden-Class-1 challenge

The roadmap itself contains no already-certified hidden Class-1 result that can be promoted immediately without first freezing the exact Stage30 action objects. Existing Stage29 scripts/checkers must be reused at 30-01/30-02A, but the exact cross-action manifest and labels are not yet frozen, so there is no legitimate adapter closure to execute during roadmap audit.

```text
HIDDEN_CLASS1_PENDING_COUNT=0
```

Any finite leaf exposed after 30-01 must still be executed immediately under the recursive 1/2/3/4 rule.

## 7. Final verdict

The roadmap attacks the correct Class-2 kernel, preserves the Stage29 scope firewalls, permits Class-3 reclassification if the finite-adapter hypothesis fails, and has a reproducible two-command/Codex handoff model. After the bounded ordering repair it is safe to begin Stage30-01.

```text
AUDIT_VERDICT=PASS_AFTER_BOUNDED_ORDERING_REPAIR
TARGET_KERNEL=K16-C2-MODULAR-S4-ACTION
TARGET_RECEIVER=R29-KUM5
ROADMAP_SUBSTAGE_COUNT=15
CHATGPT_OWNED_UNIT_COUNT=10
CODEX_OWNED_UNIT_COUNT=5
CODEX_PROMPT_GENERATION_STAGE_COUNT=4
USER_COMMAND_COUNT=2
TARGETED_ARSENAL_READ_REQUIRED=true
FULL_ARSENAL_REPLAY_REQUIRED=false
DISCHARGED_RECEIVER_REPLAY_COUNT=0
HIDDEN_CLASS1_PENDING_COUNT=0
NEW_THEOREM_ASSUMED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=30-01_SOURCE_LOCK_AND_ACTION_OBJECT_FREEZE
NEXT_EXPECTED_COMMAND=Stage30-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
