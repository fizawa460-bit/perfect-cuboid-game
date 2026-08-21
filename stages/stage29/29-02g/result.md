# Stage29-02g — modular `M(4,8)` / exact Q-descent synthesis

```text
STAGE=29-02g
KIND=MODULI_M4_8_Q_DESCENT
STATUS=SUBMITTED_FOR_FRESH_AUDIT
PERFECT_CUBOID_CONCLUSION=NONE
```

## Executive result

The endpoint modular route is now sharply separated from ordinary 8-congruence.

For `K=Q(i)`, the endpoint surface has the exact presentation

```text
Sbar_K ~= (X(8) x X(8))/Delta G0,
G0 ~= (Z/2)^3,
PSL2(Z/8)/G0 ~= PSL2(Z/4) ~= S4.
```

A Q-rational endpoint point gives an elliptic curve `E/K`, a level-4 basis `(P1,P2)`, and a symplectic 8-torsion isomorphism

```text
psi:E[8] -> E^sigma[8]
psi(P1)=P1^sigma
psi(P2)=-P2^sigma.
```

This is the exact arithmetic receiver. Bare 8-congruence is insufficient.

## 1. Ordinary 8-congruence route is RED

Fisher's ordinary symplectic 8-congruence surface `Z(8,1)` is rational over Q and carries infinitely many non-isogenous rational pairs. Therefore an endpoint argument cannot be based on the rarity of ordinary 8-congruence.

```text
NAIVE_ORDINARY_8_CONGRUENCE_OBSTRUCTION=RED
```

## 2. Exact level-4 cover

Forgetting the retained level-4 structure enlarges the diagonal quotient group from `G0` to `PSL2(Z/8)`. Thus, generically away from cusps/stabilizers,

```text
Sbar_K -> Z(8,1)_K
```

is a degree-24 cover with residual group `S4`.

```text
R29-MOD2=EndpointAsLevel4S4CoverOfOrdinarySymplectic8CongruenceSurface
STATUS=PASS_CANDIDATE
```

This explains why the ordinary congruence surface can be rational while the endpoint surface is of general type: the endpoint lives on the much more restrictive level-4-retaining cover.

## 3. Finite conjugation-defect stratification

For a compatible `psi`, define

```text
kappa=psi^sigma o psi.
```

The exact level-4 sign condition forces `kappa` to fix `E[4]` pointwise. Symplecticity places it in

```text
K8=ker(SL2(Z/8)->SL2(Z/4)) ~= (Z/2)^3.
```

Hence the discrete defect has only eight elements. Under compatible basis change the eight elements fall into four conjugacy types, with orbit sizes

```text
1,3,3,1.
```

The exact dependency-free checker `defect_orbits.py` reproduces this split.

```text
R29-MOD1B=EightTorsionConjugationDefectStratification
STATUS=PASS_CANDIDATE
```

This is a finite stratification of one descent datum; it is not a finite enumeration of endpoint points.

## 4. Residual exact receivers

The modular route is compressed to

```text
R29-MOD1A  ExactConjugateSelfLevel4ModuliAdapter
R29-MOD1B  EightTorsionConjugationDefectStratification
R29-MOD1C  ArithmeticAnalysisOfTheFourDefectOrbits
R29-MOD1D  CuspStabilizerAndPhysicalOpenRemoval
R29-MOD2    EndpointAsLevel4S4CoverOfOrdinarySymplectic8CongruenceSurface
R29-MOD2B   BranchAndStabilizerLedgerForTheDegree24ForgetfulCover
```

The first two and the generic degree-24 structure are submitted as PASS candidates. The arithmetic exclusion/survival of the four defect types and special-locus bookkeeping remain open.

Potential future inputs for `R29-MOD1C` include local mod-8 Galois-image restrictions over `Q(i)`, explicit equations for `X_E(8,1)`, and compatibility with the physical open. None is assumed here to cover all endpoint points.

## 5. What has not been proved

- no defect type is eliminated globally;
- no finite set of elliptic curves `E/Q(i)` is obtained;
- no endpoint rational point is constructed;
- no endpoint rational point is excluded;
- `kappa=1` does not imply that `E` descends to Q;
- cusps and extra-automorphism stabilizers are not yet fully removed;
- the degree-24 statement is generic, not a claim of an everywhere-etale cover.

## 6. Relation to the 29-02 extension namespace

This suffix materially strengthens the already accepted modular foundation `F5`; it does not expose a genuinely independent new foundation. Therefore it does **not** earn `29-02ha` merely by subdivision.

After a fresh audit PASS, the intended mainline move is

```text
29-03 FOUNDATION_BACKFLOW_DECISION
```

while the `29-02ha, hb, ...` namespace remains available later if a materially new theorem/model/adapter/invariant/obstruction is discovered.

```text
NEW_HA_GRADE_FOUNDATION_FOUND_IN_02G=false
OLD_GATE_REPLAY=false
BACKFLOW_TO_STAGE16_28=false
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_ITEM_AFTER_PASS=29-03
NEXT_EXPECTED_COMMAND=Stage29-audit
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
