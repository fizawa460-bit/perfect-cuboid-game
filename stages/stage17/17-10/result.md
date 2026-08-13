# Stage17-10 — population contract

Status: **SUBMITTED_FOR_FRESH_AUDIT**

## Stage object

Stage17 counts the Stage16 exactly-one-face population after adding an integral space diagonal. No face-multiplicity convention changes.

Let
\[
R(a,b,c)=\sqrt{a^2+b^2+c^2}.
\]
The frozen Stage16 source population is
\[
\mathcal B_1(B)=\{0<a<b<c:\gcd(a,b,c)=1,\ R\le B,\ \text{exactly one of }a^2+b^2,a^2+c^2,b^2+c^2\text{ is a square}\}.
\]
Its count is `M_1(B)`.

Define the Stage17 population
\[
\mathcal B_{1,d}(B)=\{(a,b,c)\in\mathcal B_1(B):R(a,b,c)\in\mathbb Z\},
\qquad
N_1(B)=\#\mathcal B_{1,d}(B).
\]
If `d=R(a,b,c)` on this population, then
\[
d^2=a^2+b^2+c^2,
\qquad d=R>0.
\]
Hence
\[
R\le B\iff d\le B
\]
exactly. No asymptotic cutoff conversion or multiplicative loss is present.

## Contract lock

```text
PARENT_STAGE=Stage17
PARENT_CLASS=population_state
STAGE_OBJECT=primitive canonical cuboids with exactly one integral face diagonal and integral space diagonal
SOURCE_POPULATION=Stage16 exact-one population B_1(B)
TARGET_POPULATION=B_{1,d}(B) subset of B_1(B) with R integral
SOURCE_COUNT=M_1(B)
TARGET_COUNT=N_1(B)
CANONICAL_EDGES=0<a<b<c
PRIMITIVE=gcd(a,b,c)=1
EXACT_FACE_MULTIPLICITY=1
SPACE_DIAGONAL_INTEGRALITY=REQUIRED
COMMON_HEIGHT=R=sqrt(a^2+b^2+c^2)
COMMON_CUTOFF=R<=B
SPACE_DIAGONAL=d=R exactly on target
CUTOFF_EQUIVALENCE=R<=B iff d<=B
COMPARISON_ADAPTER_REQUIRED=NO
POPULATION_CONTRACT_CHANGED=NO
FINITE_DATA_USED_AS_PROOF=false
EVIDENCE_LEVEL=PROVED_DEFINITIONAL_CONTRACT
```

`exactly one` is inherited literally from Stage16. Objects with exactly two or exactly three integral face diagonals are not Stage17 objects even when the space diagonal is integral.

## Frozen upstream interface

The Stage16 R01 bundle and its checkpoint-70 fresh audit are frozen upstream inputs:

```text
UPSTREAM_STAGE=Stage16
UPSTREAM_THEOREM=M_1(B) ASYM B^2 log B
UPSTREAM_POPULATION_MATCH=true
UPSTREAM_CUTOFF_MATCH=true
UPSTREAM_MULTIPLICITY_MATCH=true
UPSTREAM_AUDIT=stages/stage16/16-70/audit.md
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
```

The Stage16 theorem is not yet used to infer any Stage17 asymptotic. It is recorded only so later checkpoints can compare counts without population drift.

## Stage21 boundary

Stage17 freezes and studies the target population itself. Stage21 is the dedicated later transition object `16 -> 17` and will own the final cross-stage thinning synthesis. Stage17 must therefore keep the exact subset relation
\[
\mathcal B_{1,d}(B)\subseteq\mathcal B_1(B),
\qquad N_1(B)\le M_1(B),
\]
without changing cutoff, canonicalization, primitivity, or face multiplicity.

## Reuse boundary

- AR-001 supplies the primitive/canonical physical convention.
- AR-002 supplies primitive Euclid face decomposition when later counting work needs it.
- AR-039 is a known narrower exactly-one family with integral space diagonal and is parked for the Stage17 lower-bound/construction ledger. It is not used at checkpoint 10 to infer a growth law.

No Stage14/15 exactly-two theorem is imported into this population contract.

## Nonclaims

Checkpoint 10 does **not** claim:

- an asymptotic order for `N_1(B)`;
- a limit or rate for `N_1(B)/M_1(B)`;
- zero density or positive density inside Stage16;
- an upper or lower exponent for Stage17;
- independence of the one-face and space-diagonal conditions;
- any perfect-cuboid existence or nonexistence conclusion.

Checkpoint 20 will require a deterministic finite-data baseline under this audited contract. The main lane stops here because that census must not become canonical before the new Stage17 population definition receives independent audit.

```text
MAIN_BATCH_STATUS=SUBMITTED
CURRENT_STAGE=Stage17
CURRENT_CHECKPOINT=10
CHECKPOINTS_ATTEMPTED=10
CHECKPOINTS_SUBMITTED=10
NEW_CLAIMS=Stage17 population/cutoff/subset contract only; no counting law
REUSED_WEAPONS=AR-001,AR-002; AR-039 parked for checkpoint 50
CODEX_REQUIRED=false
CODEX_REASON=Checkpoint 10 is a compact population/cutoff contract with no repository-heavy implementation.
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=Stage17-audit
MERGE_ALLOWED=false
```
