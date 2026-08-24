# Stage33-08 — BR2B explicit endpoint representatives — hostile-audited BLOCKED_NEW_KERNEL

Hostile-audit verdict:

```text
PASS_BLOCKED_NEW_KERNEL_AFTER_NARROWING_REAUDIT_TO_STAGE33_07_GLOBAL_Q_LIFT_AND_ROLLING_PROGRESS_BACK_TO_6_OF_11
```

```text
STAGE33_UNIT=33-08
PR=1375
UNIT_STATUS=BLOCKED_NEW_KERNEL
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
BR2B=BLOCKED_NEW_KERNEL
CLOSURE_CRITERIA_TOTAL=10
CLOSURE_CRITERIA_SATISFIED=0
UNRESOLVED_UNKNOWN_IN_SCOPE=1
NEW_KERNEL_ID=R33-BR0G-BR2A-GLOBAL-RESIDUE-LIFT-ARITHMETIC-HS-DESCENT
BLOCKED_BY_PREDECESSOR=33-07
STAGE33_PROGRESS=6/11
STAGE33_09_RELEASED=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Accepted exact direct prefix

The following Stage33-08 work is independent of the unsupported global-Q Gersten lift and remains exact:

```text
FULL_U_D_EXPLICIT_Q_RATIONAL_BASIS_RANK=14
FULL_U_D_SMITH=1^14
FULL_U_D_BASIS_UNIMODULAR=true
BR0B_LEFT_FILTRATION_EXPLICIT_PARAMETRIC_REPRESENTATIVES=true
U44_EXPLICIT_Q_DEFINED_QUATERNION_REPRESENTATIVES=44/44
U44_PHYSICAL_OPEN_DOMAIN=ALL_PHYSICAL_OPEN
J2_Q_DEFINED_GENERIC_CORESTRICTION_CSA=true
J2_FULL_PHYSICAL_OPEN_PATCH_COVER=false
SEVEN_LINE_ENDPOINT_BLOCK=0
```

The low-degree Q-rational scan produced 57/57 boundary-supported sections and 56 usable ratios. Their coordinate matrix has rank 14 and Smith diagonal `1^14`; the selected 14x14 basis has determinant absolute value one. Thus it is exactly the full audited `U_D ~= Z^14`, not a finite-index sublattice.

The 44 `U01..U44` generators are direct quaternion symbols `(u_i,u_j)_2` in this saturated Q-rational unit basis. Since both slots are units on the physical open `U=S-D`, all 44 are evaluable on the entire physical open.

The exact Q-defined Stage33-05 `J2` corestriction CSA is retained on its current dense evaluation patch. No full patch cover is claimed.

## The theorem-scope regression is real

Stage33-07 treated Panin--Zainoulline finite-coefficient Gersten exactness as global surjectivity from compatible residue data on the entire smooth proper cuboid surface to global Brauer lifts over Q.

Direct source verification shows Theorem 1.1 is semi-local: it is stated for

```text
U = Spec O_{X,x}
```

for a finite set of points. For a global surface, the Bloch--Ogus Gersten resolution leaves a possible middle `H^1_Zar(S,H^2)` obstruction after taking global sections. The cited theorem alone therefore did not justify the Stage33-07 global-Q lift step.

The geometric part is repairable. The cuboid minimal resolution is simply connected; consequently `H^1_et(Sbar,Z/n)=0`, and Poincare duality gives `H^3_et(Sbar,mu_n^2)=0`. Hence the compatible finite residue tuples globally lift over `Qbar`.

What remains unresolved is arithmetic descent of those geometric lifts to Q. Since `b2=78` and `rank Pic(Sbar)=64`, the proper transcendental l-adic rank is 14, so this descent ambiguity is genuinely nonzero and cannot be ignored.

## Correct predecessor scope after hostile audit

Stage33-04 remains `CLOSED`.

Its audited scope is the physical-boundary residue adapter, and its own firewall explicitly said that it was **not** a complete Q-defined Brauer-class list. Its exact boundary modules remain valid.

The unit that must be reopened is Stage33-07, because its closure contract explicitly requires a complete relevant Q-defined global class list. Until arithmetic Hochschild--Serre descent is computed, that gate is false.

Effective Stage33-07 state:

```text
UNIT_STATUS=BLOCKED_NEW_KERNEL
UNIT_CLOSED=false
BR2A=BLOCKED_NEW_KERNEL
UNRESOLVED_UNKNOWN_IN_SCOPE=1
NEW_KERNEL_ID=R33-BR0G-BR2A-GLOBAL-RESIDUE-LIFT-ARITHMETIC-HS-DESCENT
```

Retained from Stage33-07:

```text
BR0B all-primary inventory and full boundary injection
J2 Q-defined, endpoint-nonzero, proper-transcendental, Q2-nonconstant
seven-line endpoint contribution = 0
Stage33-04 BR0G boundary-residue presentation as boundary data
```

Pending/revoked until HS descent is exact:

```text
complete Q-defined global BR0G class inventory
Q-defined global constant-character complement lifts
Q-defined global R17/O12 residue lifts
noncanonical finite Gersten splitting over Q
global direct-sum presentation and duplicate quotient using those unknown lifts
```

Because blocked units do not count as complete under the Stage33 closure contract, effective progress is `6/11`, not `7/11`.

## Current kernel and next work

```text
R33-BR0G-BR2A-GLOBAL-RESIDUE-LIFT-ARITHMETIC-HS-DESCENT
```

Required next work:

```text
- compute G_Q / Hochschild--Serre descent for the geometric BR0G residue lifts;
- include interaction with the proper geometric Brauer module;
- determine exactly which boundary residue classes admit Q-defined global Brauer lifts;
- rebuild the Stage33-07 global inventory only from those descended classes;
- then reuse the retained Stage33-08 U_D/U44/J2 direct prefix.
```

This is an exact `NEW_KERNEL_EXPOSED` checkpoint, not a negative verdict on the Brauer route.

```text
NEXT_EXACT_LEAF=L33-07-REPAIR-COMPUTE-ARITHMETIC-HS-DESCENT-OF-BR0G-RESIDUE-LIFTS
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```

No Brauer--Manin emptiness, endpoint emptiness, or Perfect Cuboid existence/nonexistence conclusion is claimed.
