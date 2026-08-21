# Stage29-02g — audited modular `M(4,8)` / Q-descent synthesis

```text
STAGE=29-02g
KIND=MODULI_M4_8_Q_DESCENT
STATUS=AUDITED_PASS_AFTER_BOUNDED_REPAIR
PERFECT_CUBOID_CONCLUSION=NONE
```

## Executive result

The endpoint modular route is now cleanly separated from ordinary 8-congruence.

For `K=Q(i)`, Testa--Stoll give

```text
Sbar_K ~= (X(8) x X(8))/Delta G0,
G0 ~= (Z/2)^3,
PSL2(Z/8)/G0 ~= PSL2(Z/4) ~= S4.
```

On the noncuspidal modular locus, a Q-rational endpoint point gives

```text
E/K,
(P1,P2) basis of E[4],
psi:E[8] -> E^sigma[8],
psi(P1)=P1^sigma,
psi(P2)=-P2^sigma.
```

This exact conjugate-self level-4 datum is strictly stronger than ordinary symplectic 8-congruence.

```text
R29_MOD1A=DISCHARGED_GENERIC_MODULI_LOCUS
```

## 1. Ordinary 8-congruence route is RED

Fisher's `Z(8,1)` is the ordinary symplectic 8-congruence surface up to simultaneous quadratic twist. It is rational over Q and Corollary 1.3 gives infinitely many non-isogenous rational pairs.

```text
NAIVE_ORDINARY_8_CONGRUENCE_OBSTRUCTION=RED_AUDITED
```

Any useful endpoint obstruction must use the retained level-4/Q-conjugation information, not bare 8-congruence.

## 2. Generic level-4 quotient

At the function-field/moduli level, forgetting the retained level-4 data enlarges the diagonal quotient group from `G0` to `PSL2(Z/8)`. Therefore the generic quotient has

```text
GENERIC_DEGREE=[PSL2(Z/8):G0]=192/8=24
GENERIC_RESIDUAL_GROUP=S4.
```

The quotient target is birational to Fisher's ordinary `Z(8,1)` surface.

```text
R29_MOD2=DISCHARGED_GENERIC_BIRATIONAL_QUOTIENT
```

Audit scope repair: this is not promoted to an everywhere finite morphism between arbitrary chosen compactifications. Cusps, ramification and extra stabilizers remain

```text
R29-MOD2B=BranchCuspAndStabilizerLedgerForGenericDegree24Quotient.
```

## 3. Finite conjugation-defect compression

Define

```text
kappa=psi^sigma o psi:E[8]->E[8].
```

The exact level-4 sign condition forces `kappa` to fix `E[4]` pointwise. Symplecticity gives

```text
kappa in K8=ker(SL2(Z/8)->SL2(Z/4)) ~= (Z/2)^3.
```

Thus every possible defect lies in an eight-element group. Under ordinary symplectic conjugation, the eight elements split into four classes of sizes

```text
1,3,3,1.
```

The exact checker `defect_orbits.py` reproduces this classification.

```text
R29_MOD1B=DISCHARGED_AS_ABSTRACT_K8_CONJUGACY_CLASSIFICATION
```

Audit scope repair: these four ordinary conjugacy classes are **not yet certified as the exact four arithmetic strata of Q-rational endpoint data**. The retained asymmetric level-4 sign operator and sigma-twisted descent action must still be incorporated.

```text
ARITHMETIC_DEFECT_STRATA_EXACTLY_FOUR_PROVED=false
R29-MOD1C=TwistedSigmaDescentActionAndArithmeticAnalysisOfK8Classes
```

## 4. Remaining exact receivers

```text
R29-MOD1C  TwistedSigmaDescentActionAndArithmeticAnalysisOfK8Classes
R29-MOD1D  CuspStabilizerAndPhysicalOpenRemoval
R29-MOD2B  BranchCuspAndStabilizerLedgerForGenericDegree24Quotient
```

No defect class is globally eliminated yet, no finite set of elliptic curves `E/Q(i)` is obtained, and no endpoint point is constructed or excluded.

## 5. Namespace / routing

02g materially sharpens the already accepted modular foundation `F5`; it is not a genuinely independent new foundation. Therefore it does not consume the `29-02ha` namespace.

PR #1300 / 29-02f is already merged. 02g itself creates no automatic Stage16--28 reentry. The correct next checkpoint is

```text
29-03 FOUNDATION_BACKFLOW_DECISION
```

which decides whether any of the new Stage29 foundations justify targeted old-stage reentry.

```text
AUDIT_REQUIRED=false
AUDIT_VERDICT=PASS
CHECKPOINT29_02G_AUDIT=PASS
BOUNDED_REPAIR=GENERIC_BIRATIONAL_DEGREE24_SCOPE_PLUS_TWISTED_DEFECT_ORBIT_SCOPE
R29_MOD1A=DISCHARGED_GENERIC_MODULI_LOCUS
R29_MOD1B=DISCHARGED_ABSTRACT_K8_CONJUGACY
R29_MOD2=DISCHARGED_GENERIC_BIRATIONAL_QUOTIENT
ORDINARY_8_CONGRUENCE_OBSTRUCTION=RED
GENERIC_DEGREE24=PASS
ARITHMETIC_DEFECT_STRATA_EXACTLY_FOUR_PROVED=false
NEW_HA_GRADE_FOUNDATION_FOUND=false
OLD_GATE_REPLAY=false
BACKFLOW_TO_STAGE16_28=false
REPAIR_REQUIRED=false
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
NEXT_ITEM=29-03
NEXT_EXPECTED_COMMAND=Stage29-main-batch
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
