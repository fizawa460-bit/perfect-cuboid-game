# Stage33-08 hostile audit

## Verdict

```text
PASS_BLOCKED_NEW_KERNEL_AFTER_NARROWING_REAUDIT_TO_STAGE33_07_GLOBAL_Q_LIFT_AND_ROLLING_PROGRESS_BACK_TO_6_OF_11
```

PR: `#1375`

Audited pre-audit head:

```text
bb9bfabb7f3352d1891a13c9ad122d599fc6fd96
```

Pre-audit workflow evidence:

```text
workflow_run=32754776316
workflow_run_number=22
workflow_conclusion=success
artifact_id=9530417283
artifact_zip_sha256=15d201718e1d4562ca3645144fdea5f144c62284090433c86864b8dad77539bf
```

The artifact ZIP was independently downloaded and rehashed. All six JSON certificates carrying `canonical_sha256` were independently canonical-rehashed and matched their stored hashes.

## 1. The new theorem-scope regression is real

Stage33-07 used Panin--Zainoulline finite-coefficient Gersten exactness as if it supplied global surjectivity from every compatible codimension-one residue tuple on the complete smooth cuboid surface to a global Brauer lift over Q.

Direct primary-source verification rejects that use. Panin--Zainoulline Theorem 1.1 is formulated for

```text
U = Spec O_{X,x}
```

with `x` a finite set of points; `U` is a semi-local regular scheme of geometric type. It does not by itself assert global-section exactness for the whole projective surface.

For the global Bloch--Ogus Gersten resolution, the middle homology of global sections is a Zariski cohomology group `H^1(S,H^2)`. Thus compatible residue data need not globally lift unless the corresponding global obstruction is shown to vanish.

Accepted regression:

```text
PANIN_ZAINOULLINE_SCOPE_SEMILOCAL=true
STAGE33_07_GLOBAL_Q_SURJECTIVITY_FROM_THAT_THEOREM_UNJUSTIFIED=true
GLOBAL_BLOCH_OGUS_OBSTRUCTION_MUST_BE_CHECKED=true
```

## 2. The geometric Qbar lift is repaired

The 2026 v3 paper of Enriquez--Jarossay--Saettone--Svoray proves that the cuboid surface and its minimal resolution are simply connected.

Over C, simple connectedness gives

```text
H^1_et(Sbar,Z/n)=0
```

for every finite `n`. For the smooth proper surface, Poincare duality then gives

```text
H^3_et(Sbar,mu_n^2)=0.
```

In the Bloch--Ogus spectral sequence the potential `H^1_Zar(Sbar,H^2)` middle obstruction injects into total degree 3; hence it vanishes. Therefore the compatible finite residue tuples do globally lift geometrically over `Qbar`.

Accepted:

```text
GEOMETRIC_GLOBAL_COMPATIBLE_RESIDUE_LIFT_OVER_QBAR=true
```

This is not arithmetic descent to Q.

## 3. The arithmetic Q-descent kernel is genuine and non-vacuous

Horie--Yamauchi compute `rank H^2(S)=78` and `rank Pic(Sbar)=64`. Hence the proper transcendental l-adic rank is

```text
78 - 64 = 14.
```

Thus two geometric lifts of the same residue tuple can differ by a nonzero proper transcendental Brauer class. Galois-invariance of the residue tuple alone therefore does not certify that a Q-defined lift exists.

The exact unresolved dependency is accepted as

```text
R33-BR0G-BR2A-GLOBAL-RESIDUE-LIFT-ARITHMETIC-HS-DESCENT
```

Required repair:

```text
compute the G_Q / Hochschild-Serre descent obstruction for the geometric BR0G residue lifts,
including their torsor/extension interaction with the proper geometric Brauer module;
do not infer Q-defined global classes from invariant residue data alone.
```

## 4. Hostile-audit correction: Stage33-04 remains CLOSED

The production PR over-scoped the predecessor re-audit target by listing Stage33-04 arithmetic Q-defined class completeness.

Stage33-04 did not claim a complete Q-defined global Brauer-class inventory. Its audited contract and result are explicitly the 72-component physical-boundary residue adapter. Its own firewall says

```text
complete_q_defined_brauer_class_list=false.
```

Its exact boundary result remains valid:

```text
72 boundary components
120 arithmetic crossing orbits
odd-primary boundary-character module
Hom_cont(G_Q,Q/Z)_odd^48 direct_sum Hom_cont(G_Q(i),Q/Z)_odd^12
finite two-primary boundary residue module
(Z/2)^49 direct_sum (Z/4)^12
```

Therefore Stage33-04 remains `CLOSED`. No Stage33-04 audit credit is revoked by this regression.

## 5. Stage33-07 global integration credit is revoked/reopened

Stage33-07 closure, unlike Stage33-04, explicitly required

```text
COMPLETE_RELEVANT_Q_DEFINED_CLASS_LIST_FOR_STAGE33_BRAUER_SCOPE=true.
```

The arithmetic lift gap invalidates that closure gate and the claimed global direct-sum presentation for the BR0G families.

The following Stage33-07 facts remain exact and are retained:

```text
BR0B full boundary map injective = true
BR0B all-primary inventory = retained
J2 Q-defined proper transcendental endpoint class = retained
J2 Q2 evaluation nonconstant = retained
seven-line endpoint contribution = 0 retained
BR0G boundary residue presentation = retained as boundary data
```

The following Stage33-07 claims are no longer authoritative until HS descent is computed:

```text
complete Q-defined BR0G global class inventory
finite global group (Z/2)^49 direct_sum (Z/4)^12 as Q-defined Brauer lifts
noncanonical finite Gersten splitting over Q
complete odd/two-primary constant-character global lift blocks
full global duplicate quotient involving those unknown lifts
```

Effective Stage33-07 state after this hostile audit:

```text
UNIT_STATUS=BLOCKED_NEW_KERNEL
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
BR2A=BLOCKED_NEW_KERNEL
UNRESOLVED_UNKNOWN_IN_SCOPE=1
NEW_KERNEL_ID=R33-BR0G-BR2A-GLOBAL-RESIDUE-LIFT-ARITHMETIC-HS-DESCENT
```

Under the Stage33 closure contract, blocked units do not count as complete. Therefore effective progress rolls back from `7/11` to `6/11`.

## 6. Stage33-08 exact prefix independently accepted

The new kernel does not invalidate direct constructions that do not use the unsupported global-Q lift step.

The downloaded artifact was independently checked:

```text
57/57 curated low-degree Q-rational sections have boundary-only support
56 usable ratios
coordinate rank = 14
Smith diagonal = 1^14
```

The explicit 14x14 coordinate matrix has determinant `+/-1`, independently confirming that the produced Q-rational unit basis is exactly the full audited `U_D ~= Z^14`, not an index sublattice.

Accepted direct Stage33-08 prefix:

```text
FULL_U_D_EXPLICIT_Q_RATIONAL_BASIS_RANK=14
FULL_U_D_SMITH=1^14
BR0B_LEFT_FILTRATION_EXPLICIT_PARAMETRIC_REPRESENTATIVES=true
```

The 44 audited unit-symbol basis pairs are 44 distinct pairs of this saturated unit basis. Hence the quaternion symbols `(u_i,u_j)_2` are direct Q-defined classes; because both slots are units on `U=S-D`, these 44 representatives are evaluable on the entire physical open.

Accepted:

```text
U44_EXPLICIT_Q_DEFINED_QUATERNION_REPRESENTATIVES=44/44
U44_PHYSICAL_OPEN_DOMAIN=ALL_PHYSICAL_OPEN
```

The exact Stage33-05 J2 corestriction formula is also retained:

```text
Cor_{L(C)/Q(t)(C)}((ell_J2,s-alpha)_2)
```

with its present dense patch explicitly recorded. A full physical-open patch cover is not claimed.

Accepted:

```text
J2_GENERIC_Q_DEFINED_CSA=true
J2_FULL_PHYSICAL_OPEN_PATCH_COVER=false
SEVEN_LINE_ENDPOINT_BLOCK=0
```

## 7. Effective Stage33-08 state

Because Stage33-07 is no longer CLOSED, Stage33-08 cannot satisfy its inheritance gate. Its completed prefix is retained as work product, but no Stage33-08 closure criterion depending on the complete Stage33-07 list can currently be credited.

Effective state:

```text
UNIT_STATUS=BLOCKED_NEW_KERNEL
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
BR2B=BLOCKED_NEW_KERNEL
CLOSURE_CRITERIA_TOTAL=10
CLOSURE_CRITERIA_SATISFIED=0
UNRESOLVED_UNKNOWN_IN_SCOPE=1
BLOCKED_BY_PREDECESSOR=33-07
STAGE33_09_RELEASED=false
```

This is a valid `NEW_KERNEL_EXPOSED` checkpoint, not a failed mathematical route.

## 8. Firewall

Nothing in this audit weakens the exact J2 result: J2 remains Q-defined, proper-transcendental, nonzero at the endpoint, and Q2-nonconstant.

What is lost is the claim that the entire BR0G residue inventory has already been lifted/descent-certified as Q-defined global Brauer classes.

Therefore:

```text
BRAUER_MANIN_SET_EMPTY_NOT_PROVED=true
ENDPOINT_EMPTY_NOT_PROVED=true
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

The next authorized work is the Stage33-07 repair leaf computing arithmetic Hochschild--Serre descent for the geometric BR0G residue lifts. Stage33-08's exact direct prefix should be reused after that repair; it should not be recomputed from scratch.
