# Stage33-08 — BR2B explicit endpoint representatives — BLOCKED_NEW_KERNEL

```text
STAGE33_UNIT=33-08
PR=1375
UNIT_STATUS=BLOCKED_NEW_KERNEL
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
BR2B=BLOCKED_NEW_KERNEL
CLOSURE_CRITERIA_TOTAL=10
CLOSURE_CRITERIA_SATISFIED=2
UNRESOLVED_UNKNOWN_IN_SCOPE=1
NEW_KERNEL_ID=R33-BR0G-BR2A-GLOBAL-RESIDUE-LIFT-ARITHMETIC-HS-DESCENT
PREDECESSOR_REAUDIT_REQUIRED=true
STAGE33_PROGRESS_FORMAL_PENDING_REAUDIT=7/11
STAGE33_09_RELEASED=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Exact completed prefix

The direct representative work completed before the new kernel remains valid:

```text
FULL_U_D_EXPLICIT_Q_RATIONAL_BASIS_RANK=14
FULL_U_D_SMITH=1^14
BR0B_LEFT_FILTRATION_EXPLICIT_PARAMETRIC_REPRESENTATIVES=true
U44_EXPLICIT_Q_DEFINED_QUATERNION_REPRESENTATIVES=44/44
U44_PHYSICAL_OPEN_DOMAIN=ALL_PHYSICAL_OPEN
J2_Q_DEFINED_GENERIC_CORESTRICTION_CSA=true
SEVEN_LINE_ENDPOINT_BLOCK=0
```

The old missing-Q-unit kernel was discharged by a 57-section low-degree Q-rational scan.  The resulting coordinate matrix has rank 14 and Smith diagonal `1^14`.

## Theorem-scope regression found by Stage33-08

Stage33-07 used Panin--Zainoulline/Bloch--Ogus finite-coefficient Gersten exactness as a global-surjectivity input on the whole smooth cuboid surface.  Direct source verification shows that Panin--Zainoulline Theorem 1.1 is stated for a semi-local scheme

```text
U = Spec O_{X,x}
```

at a finite set of points.  For a global smooth surface, the Bloch--Ogus Gersten resolution is a flasque resolution; taking global sections leaves a possible middle cohomology / global obstruction.  Therefore the cited theorem alone does not certify that every compatible global residue tuple has a Q-defined Brauer lift.

This does not destroy the geometric residue calculation.  Enriquez--Jarossay--Saettone--Svoray prove that the cuboid surface and its minimal resolution are simply connected.  Consequently for every finite `n` in characteristic zero,

```text
H^1_et(Sbar,Z/n)=0,
H^3_et(Sbar,mu_n^2)=0
```

by Poincare duality, so the compatible finite residue tuples do lift geometrically over `Qbar`.

The remaining issue is arithmetic descent of those geometric lifts to `Q`.  Horie--Yamauchi's H^2 decomposition exhibits a 14-dimensional proper transcendental l-adic part, so this descent correction is not vacuous.

## New exact kernel

```text
R33-BR0G-BR2A-GLOBAL-RESIDUE-LIFT-ARITHMETIC-HS-DESCENT
```

Required next work:

```text
- compute the G_Q / Hochschild--Serre descent obstruction for the BR0G geometric residue lifts;
- include the interaction with the 14-dimensional proper transcendental Brauer module;
- revalidate the claimed Q-defined constant-character and R17/O12 families;
- only after that construct/evaluate their global CSA or crossed-product representatives.
```

Until that is done, Stage33-04/07 Q-defined BR0G lift credit requires predecessor hostile re-audit.  This main-batch does not silently mutate an already hostile-audited predecessor; it freezes the regression and prevents Stage33-09 release.

```text
NEXT_EXACT_LEAF=L33-REPAIR-COMPUTE-ARITHMETIC-HS-DESCENT-OF-BR0G-RESIDUE-LIFTS
NEXT_EXPECTED_COMMAND=Stage33-audit #1375
```
