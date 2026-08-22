# Stage30 — MODULAR-S4-ACTION roadmap

Status: ROADMAP_SUBMISSION_PENDING_AUDIT

## Objective

Stage30 attacks the post-Stage29 Class-2 kernel

```text
K16-C2-MODULAR-S4-ACTION
child: R29-KUM5
parent route: Q11-MODULAR
```

The goal is **not** to prove a new abstract `S4 ~= S4` statement.  The goal is to construct and certify the exact action-level adapter between the seven-line arrangement symmetry and the modular residual symmetry, including the marked arithmetic data and the `Q(i)/Q` descent cocycle needed by the physical endpoint.

Target close state:

```text
MODULAR_S4_ACTION_ADAPTER=VERIFIED
QI_EQUIVARIANCE=VERIFIED
Q_GALOIS_COCYCLE_COMPATIBILITY=VERIFIED
MARKED_DEFECT_MAPPING=COMPLETE
PHYSICAL_ADAPTER=VERIFIED
R29_KUM5=DISCHARGED_ACTION_LEVEL_S4_Q_DESCENT_ADAPTER
```

This is a support/computational kernel.  Completion does not by itself prove perfect-cuboid existence or nonexistence.

## Frozen audited starting facts

Do not re-prove these unless audit finds a contradiction.

1. The seven-line base arrangement has

```text
Aut_P2(D) ~= S4.
```

The exact arithmetic lift split is already audited:

```text
Q-liftable base subgroup = S3, order 6
Q(i)-liftable base group = S4, order 24
Q line orbits = 3+3+1
Q(i) line orbits = 4+3
```

2. On the modular side, after forgetting the retained level-4 data, the generic residual group is

```text
PSL2(Z/4) ~= S4,
generic degree = 24.
```

3. For the conjugation defect

```text
kappa = psi^sigma o psi,
```

the defect lies in

```text
K8 = ker(SL2(Z/8) -> SL2(Z/4)) ~= (Z/2)^3,
```

so the abstract defect set has exactly 8 elements.  Ordinary symplectic conjugation gives class sizes `1,3,3,1`, but this ordinary orbit split is not automatically the arithmetic endpoint stratification.

4. Stage29-15 discharged the bounded sigma-action subproblem:

```text
R29-MOD1C=DISCHARGED_TRIVIAL_SIGMA_ACTION_ON_K8
MARKED_ARITHMETIC_DEFECT_CLASS_COUNT=8
R29-MOD1D=DISCHARGED_PHYSICAL_OPEN_NONCUSP_STABILIZER_FREE
```

5. The unresolved wall remains:

```text
R29-KUM5=OPEN_ACTION_LEVEL_S4_Q_DESCENT_ADAPTER
```

An abstract isomorphism of the two `S4` groups is insufficient.  The adapter must respect the concrete actions, marked data, and descent/Galois structure.

## Mandatory source read before execution

Every Stage30 execution PR must first fresh-read the relevant merged records, not rely on memory:

```text
stages/stage29/29-02g/*
stages/stage29/29-02ha/*
stages/stage29/29-11/*
stages/stage29/29-15/*
stages/stage29/29-16/active-kernel-ledger.json
stages/stage29/29-17/final-handoff.json
```

### Arsenal policy

Yes: Stage30 must explicitly consult the Arsenal, but **only as a targeted rematch**, not as a full Stage14/StructureRadar replay.

Search the indexed Arsenal/StructureRadar material for exact hits on terms and adapters involving:

```text
S4
modular
M(4,8)
Q(i)
Kummer
K8
descent
cocycle
Galois action
marked orbit
```

Consume only items whose hypotheses and action data match the Stage30 objects exactly.  Do not grant theorem/adapter credit from a name-level or abstract-group match.  If the targeted Arsenal rematch finds a material shortcut, record it before starting new computation.

## Two-command operating model

The user-facing command surface remains exactly:

```text
Stage30-main-batch
Stage30-audit
```

No third `Stage30-codex-*` command is required.

`Stage30-main-batch` reads the controller and executes the next eligible unit.  When the next unit belongs to Codex, ChatGPT must generate a complete copy/paste-ready Codex task file under `stages/stage30/handoffs/`, set the controller to `WAITING_EXTERNAL_CODEX_RESULT`, and stop the mathematical advance there.

After Codex has placed its result in the repository, `Stage30-main-batch` resumes from that result.  `Stage30-audit` performs a fresh hostile audit of the current Stage30 PR/result and repairs the same PR where bounded repair is possible.

## Roadmap

### Stage30-01 — SOURCE_LOCK_AND_ACTION_OBJECT_FREEZE

Owner: ChatGPT

Tasks:

- fresh-read the mandatory Stage29 sources;
- targeted Arsenal rematch;
- enumerate the exact arrangement-side objects acted on by `S4`;
- enumerate the exact modular-side objects acted on by residual `S4`;
- freeze generator conventions, labels, base fields, marked subsets and the physical receiver;
- identify which existing exact checkers/data files can be reused;
- produce a machine-readable input manifest.

Hard close condition:

```text
ARRANGEMENT_ACTION_OBJECTS_FROZEN=true
MODULAR_ACTION_OBJECTS_FROZEN=true
GENERATOR_CONVENTIONS_FROZEN=true
MARKED_DATA_FROZEN=true
BASE_FIELD_LEDGER_FROZEN=true
ARSENAL_TARGETED_REMATCH_COMPLETE=true
```

If the exact action objects cannot be defined from current sources, classify the missing item before proceeding.

### Stage30-02P — CREATE_CODEX_TASK_A

Owner: ChatGPT

Create `handoffs/codex-task-A-s4-action-extraction.md`.

The task must instruct Codex to reuse repository code before writing new code and to produce exact finite certificates for:

- arrangement `S4` generators and permutation representation;
- modular residual `S4` generators and permutation representation;
- group-order/relation verification;
- orbit and stabilizer tables;
- explicit labels linking every permutation point to the Stage30-01 manifest;
- deterministic machine-readable output and a standalone checker.

The prompt must prohibit replacing the concrete action with an abstract `S4` isomorphism.

Controller state after prompt creation:

```text
WAITING_EXTERNAL_CODEX_RESULT=A
```

### Stage30-02C — CODEX_TASK_A_EXECUTION

Owner: Codex

Expected output:

```text
ACTION_TABLE_ARRANGEMENT
ACTION_TABLE_MODULAR
GENERATOR_RELATIONS_CERTIFICATE
ORBIT_STABILIZER_MANIFEST
VERIFY_ACTIONS
```

No mathematical adapter credit is granted until Stage30-03 audit.

### Stage30-03 — ACTION_TABLE_AUDIT_AND_RECLASSIFICATION

Owner: ChatGPT

- independently check Codex output against source definitions;
- verify no compactification/generic-locus/physical-open scope was silently changed;
- verify all generator conventions and field-of-definition labels;
- reapply the recursive classes 1/2/3/4 to every newly exposed leaf.

If an immediate finite leaf is Class 1, execute it before advancing.

### Stage30-04P — CREATE_CODEX_TASK_B

Owner: ChatGPT

Create `handoffs/codex-task-B-equivariant-identification.md` from the audited action tables.

Codex task B must exhaustively search/certify candidate equivariant identifications subject to the **actual marked structure**, not only the group law.  Required checks include

```text
f(g.x) = phi(g).f(x)
```

for the frozen generators and every relevant marked object, plus compatibility with the 8 K8 defects and any retained level-4 sign datum.

Controller state:

```text
WAITING_EXTERNAL_CODEX_RESULT=B
```

### Stage30-04C — CODEX_TASK_B_EXECUTION

Owner: Codex

Expected output:

- complete candidate list or proof that no candidate survives the frozen constraints;
- exact witness for every surviving candidate;
- rejected-candidate reasons;
- marked-orbit/stabilizer compatibility table;
- standalone exhaustive checker.

### Stage30-05 — QI_EQUIVARIANT_ADAPTER

Owner: ChatGPT

Using the audited finite action results, construct the mathematical `Q(i)`-level adapter.

Required distinction:

```text
abstract residual S4
!=
concrete arrangement S4 action
!=
a Q(i)-equivariant identification of the relevant marked structures.
```

If no compatible identification exists, record that as a mathematically meaningful negative result for `R29-KUM5`; do not invent a replacement.

### Stage30-06 — QI_OVER_Q_DESCENT_COCYCLE_DERIVATION

Owner: ChatGPT

Derive the exact `Gal(Q(i)/Q)` action on the selected adapter and the cocycle/semilinear compatibility relation required to descend the modular identification to the Q-defined endpoint data.

This is the main semantic danger point.  The cocycle definition and the objects it acts on must be fixed mathematically before any brute-force checker is delegated.

If this step reveals a genuinely uniform/infinite theorem requirement rather than a finite adapter computation, split that leaf to Class 3 and stop pretending Stage30 is purely computational.

### Stage30-06P — CREATE_CODEX_TASK_C

Owner: ChatGPT

Create `handoffs/codex-task-C-galois-cocycle-and-defects.md` containing the exact formulas derived in Stage30-06.

Codex must verify, exhaustively and exactly:

- `S4` relations;
- complex-conjugation action;
- cocycle identity/semilinear compatibility;
- commutation/conjugation relations required by the frozen model;
- transport of all 8 marked defects;
- orbit/stabilizer/descent-class table;
- all candidate adapters if more than one survives.

Controller state:

```text
WAITING_EXTERNAL_CODEX_RESULT=C
```

### Stage30-06C / 30-07 — CODEX_COCYCLE_AND_EIGHT_DEFECT_EXECUTION

Owner: Codex

For every one of the 8 marked defect elements, output at least:

```text
defect_id
K8_element
ordinary_conjugacy_class
S4_orbit
stabilizer
sigma_image
QI_representative
Q_descent_class
adapter_image
arithmetic_equivalence_status
```

The output must distinguish a computed classification from an actual arithmetic elimination.  Stage30 is not allowed to claim that a defect is impossible merely because it lies in a particular orbit.

### Stage30-08 — PHYSICAL_ENDPOINT_ADAPTER

Owner: ChatGPT

Prove exactly what the completed modular/action/cocycle calculation says about the physical endpoint open.

Required firewalls:

- generic moduli degree-24 statements are not automatically global compactified morphisms;
- ordinary 8-congruence is not an endpoint rarity obstruction;
- an action-level classification does not automatically eliminate any arithmetic class;
- projective/algebraic endpoint information is not automatically a primitive/canonical population theorem.

Possible outcomes:

```text
A. R29-KUM5 fully discharged and 8 arithmetic states explicitly located;
B. R29-KUM5 discharged but no state eliminated;
C. a smaller residual Class-2 leaf remains;
D. a genuine Class-3 theorem wall is exposed;
E. the proposed action identification is impossible.
```

All are acceptable Stage30 research outcomes if certified.

### Stage30-09P / 30-09C — CERTIFICATE_AND_INDEPENDENT_CHECKER

Prompt owner: ChatGPT
Execution owner: Codex

Generate the final Codex certificate task only after the mathematical adapter has been fixed.

Required final reproducibility surface:

```text
input-manifest.json
action-tables.json
equivariant-map.json
galois-cocycle.json
defect-classification.json
verify_stage30.py
```

Prefer an independent verifier that does not simply call the same functions used to construct the result.

### Stage30-10 — FINAL_HOSTILE_AUDIT_AND_CLOSE

Owner: ChatGPT

Fresh audit must reconstruct the result from the frozen source material and certificates.

PASS is forbidden unless all load-bearing claims are classified exactly.  In particular:

```text
ABSTRACT_S4_ONLY=false
UNVERIFIED_CODEX_OUTPUT_COUNT=0
HIDDEN_CLASS1_PENDING_COUNT=0
FIELD_OF_DEFINITION_AMBIGUITY_COUNT=0
MARKED_OBJECT_UNMAPPED_COUNT=0
COCYCLE_UNVERIFIED_COUNT=0
PHYSICAL_ADAPTER_UNVERIFIED_COUNT=0
```

Final close does **not** require an arithmetic class to be eliminated.  It requires that `R29-KUM5` itself be either discharged or replaced by a smaller, precisely classified residual leaf.

## Recursive execution rule

Every Stage30 substage must reapply the post-Stage29 four-class rule to newly exposed leaves:

```text
1 = finite/bounded, tractable now, and route-enabling -> execute now
2 = current tool/model/CAS/adapter wall -> decompose further
3 = first genuinely new theorem statement -> split out as theorem research
4 = currently non-decisive/non-enabling -> dormant with trigger
```

No hidden Class-1 task may be carried forward merely to preserve the roadmap numbering.

## Stage30 stop conditions

Stage30 may close in either of two forms:

1. `R29-KUM5` fully discharged; or
2. the current Class-2 kernel is rigorously decomposed and the irreducible remainder is reclassified as a smaller Class-2/Class-3 leaf with all finite work completed.

It may not close merely because a large computation is inconvenient.

## Endpoint claim firewall

```text
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
