# Stage19-10 — population contract

Status: **SUBMITTED_FOR_FRESH_AUDIT**

Stage19 studies the primitive canonical exactly-two-face population after imposing an integral space diagonal.

## 1. Physical population

A Stage19 object is a positive integer edge triple
\[
0<a<b<c,\qquad \gcd(a,b,c)=1,
\]
with geometric space-diagonal length
\[
R=\sqrt{a^2+b^2+c^2}.
\]
Let `I_ab,I_ac,I_bc` denote the three face-square predicates. The target population is
\[
\mathcal A_2(B)
=
\{(a,b,c):R\le B,\ I_{ab}+I_{ac}+I_{bc}=2,\ R\in\mathbf Z\}.
\]
Define
\[
N_2(B)=\#\mathcal A_2(B).
\]

Thus Stage19 requires **exactly two** integral face diagonals and an integral space diagonal. Exactly-three-face cuboids are excluded by the population contract.

## 2. Exact Stage15 interface

This is literally the numerator population from Stage15:

```text
UPSTREAM_STAGE=Stage15
UPSTREAM_OBJECT=numerator exactly-two population A_2(B)
UPSTREAM_THEOREM_SCOPE=primitive canonical exactly-two cuboids with integral space diagonal
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
MEASURE_ADAPTER_REQUIRED=false
QUANTIFIER_ADAPTER_REQUIRED=false
IDENTITY=Stage19 target = Stage15 A_2(B)
```

On the target population write
\[
d=R\in\mathbf Z.
\]
Then exactly
\[
R\le B\iff d\le B.
\]
Hence the Stage15/Stage14 integral-space cutoff and the Stage19 geometric cutoff agree without a constant-factor height adapter.

Each canonical physical cuboid is counted once. The unique shared edge of the two successful faces may be used as a parametrization coordinate, but it introduces no additional object multiplicity.

## 3. Relation to Stage18 and the transition stages

Stage18 is the same primitive/canonical exactly-two population without requiring `R` integral. Therefore
\[
\boxed{\text{Stage19}=\text{Stage18}\cap\{R\in\mathbf Z\}}.
\]
Equivalently, under the common roadmap conventions,
\[
\text{Stage19}=\text{Stage18}\cap\text{SPACE\_AT\_LEAST}.
\]

This checkpoint does not yet quantify the survival ratio. The conditional transition

```text
Stage18 -> Stage19
```

belongs to Stage24. The transition `Stage17 -> Stage19` belongs to Stage23, and the combined `Stage16 -> Stage19` comparison belongs to Stage25.

## 4. Frozen quantitative provenance, not yet promoted

Stage15 records the matched numerator bound
\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}
\]
from Stage14 and the zero-density comparison
\[
N_2(B)/M_2(B)\to0.
\]
These are frozen provenance for later Stage19 checkpoints. Checkpoint10 does **not** self-award checkpoint30, checkpoint40, or an intrinsic exponent claim.

In particular, no matching lower bound and no asymptotic
\[
N_2(B)\sim C B^{1/2}
\]
is claimed here. Whether the current half-power upper exponent is intrinsic is a later Stage19 question.

## 5. Non-claims

- no perfect-cuboid existence or nonexistence conclusion;
- no claim that the space-diagonal condition is independent of the two face conditions;
- no claim that exponent `1/2` is sharp;
- no new finite-data claim;
- no Stage23/24/25 transition result is promoted at checkpoint10.

```text
EVIDENCE_LEVEL=PROVED
PARENT_STAGE=Stage19
PARENT_CLASS=population_state
TARGET_POPULATION=A_2(B)
COUNT=N_2(B)
EXACT_FACE_MULTIPLICITY=2
SPACE_DIAGONAL_REQUIRED=true
CUTOFF=R<=B
INTEGRAL_CUTOFF_ADAPTER=d=R; R<=B iff d<=B
STAGE15_INTERFACE=LITERAL_MATCH
STAGE18_RELATION=Stage19 = Stage18 intersect {R integral}
AUDIT_REQUIRED=true
NEXT_CHECKPOINT_AFTER_PASS=20
CODEX_REQUIRED=false
CODEX_REASON=Exact population/interface freeze; no implementation task is required.
```