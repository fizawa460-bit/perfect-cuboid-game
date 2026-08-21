# Stage29-02g — audited 8-torsion conjugation-defect compression

```text
ROLE=EIGHT_TORSION_CONJUGATION_DEFECT_COMPRESSION
STATUS=AUDITED_PASS_WITH_ARITHMETIC_ORBIT_SCOPE_REPAIR
```

Let `K=Q(i)` with nontrivial automorphism `sigma`. On the noncuspidal fine-moduli locus, use the Testa--Stoll datum

```text
(E/K, P1,P2 in E[4], psi:E[8] -> E^sigma[8])
psi(P1)=P1^sigma,
psi(P2)=-P2^sigma.
```

Define

```text
kappa=psi^sigma o psi:E[8]->E[8].
```

Conjugating the two level-4 sign identities shows

```text
kappa(P1)=P1,
kappa(P2)=P2.
```

Since the correspondence is symplectic, after choosing a symplectic level-8 basis,

```text
kappa in K8=ker(SL2(Z/8)->SL2(Z/4)).
```

Every element is uniquely

```text
I+4A mod 8,
A in sl2(F2),
```

so

```text
K8 ~= (Z/2)^3,
|K8|=8.
```

## Audited abstract conjugacy classes

Under ordinary conjugation by the full symplectic change-of-level-8-basis group, the action on `A` factors through `SL2(F2)~=S3`. The eight trace-zero matrices split exactly into

```text
size 1: A=0
size 3: A nonzero, det(A)=0
size 3: det(A)=1, A!=I
size 1: A=I.
```

The dependency-free checker `defect_orbits.py` verifies these four ordinary conjugacy classes exactly.

```text
DEFECT_ELEMENTS=8
ABSTRACT_SYMPLECTIC_CONJUGACY_CLASSES=4
ORBIT_SIZES=1,3,3,1
R29_MOD1B=DISCHARGED_AS_ABSTRACT_K8_CONJUGACY_CLASSIFICATION
```

## Audit scope repair

The endpoint arithmetic datum retains the asymmetric level-4 sign condition relative to `sigma`. Therefore one must distinguish:

```text
ordinary symplectic conjugacy of kappa
```

from

```text
actual equivalence of Q-rational endpoint descent data.
```

A basis change preserving a fixed displayed sign normal form is not automatically the entire `SL2(F2)` conjugation action. Equivalently, the sigma-twisted action/cocycle and retained level-4 datum must be included before the four ordinary conjugacy classes can be called the exact four arithmetic endpoint strata.

Thus the correct promotion is finite compression, not a solved arithmetic stratification:

```text
ARITHMETIC_DEFECT_STRATA_EXACTLY_FOUR_PROVED=false
R29_MOD1C=TwistedSigmaDescentActionAndArithmeticAnalysisOfK8Classes
```

This does not weaken the statement that every possible `kappa` lies in an eight-element group, nor the exact `1,3,3,1` abstract conjugacy calculation.

## Firewalls

```text
kappa=1 => E descends to Q                 FALSE_IN_GENERAL
four_K8_classes => four endpoint points    FALSE
four_K8_classes => four arithmetic strata  NOT_YET_PROVED
R29_MOD1D=CuspStabilizerAndPhysicalOpenRemoval
ELLIPTIC_CURVE_DESCENT_PROVED=false
ENDPOINT_NONEXISTENCE_PROVED=false
```
