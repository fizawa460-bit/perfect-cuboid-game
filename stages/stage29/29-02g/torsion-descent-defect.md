# Stage29-02g — finite 8-torsion conjugation-defect stratification

```text
ROLE=EIGHT_TORSION_CONJUGATION_DEFECT_STRATIFICATION
STATUS=DERIVED_PENDING_FRESH_AUDIT
```

Let `K=Q(i)` with nontrivial automorphism `sigma`. On the generic fine-moduli locus, choose the Testa--Stoll datum

```text
(E/K, P1,P2 in E[4], psi:E[8] -> E^sigma[8])
```

with

```text
psi(P1)=P1^sigma,
psi(P2)=-P2^sigma.
```

Conjugate `psi` and compose:

```text
kappa = psi^sigma o psi : E[8] -> E[8].
```

On `E[4]`, the displayed sign rules give

```text
kappa(P1)=P1,
kappa(P2)=P2.
```

Since the level-8 correspondence is symplectic, `kappa` is symplectic and fixes `E[4]` pointwise. Hence, after a symplectic level-8 basis,

```text
kappa in K8 := ker(SL2(Z/8Z) -> SL2(Z/4Z)).
```

Every element of `K8` is uniquely

```text
I + 4A  (mod 8),
A in sl2(F2),
```

so

```text
K8 ~= (Z/2Z)^3,
|K8|=8.
```

This is the linear version of the Testa--Stoll kernel `G0`.

## Basis-change orbits

Changing the compatible level basis conjugates `A`. The conjugation action factors through

```text
SL2(F2) ~= S3
```

because only the basis matrix modulo 2 acts on `A`. The eight trace-zero `2x2` matrices over `F2` split into four orbits:

```text
size 1: A=0
size 3: A nonzero, det(A)=0
size 3: det(A)=1, A!=I
size 1: A=I.
```

Thus the generic compatible Q-descent data are partitioned by a finite four-type defect ledger.

```text
R29-MOD1B=EightTorsionConjugationDefectStratification
DEFECT_ELEMENTS=8
DEFECT_BASIS_CHANGE_ORBITS=4
ORBIT_SIZES=1,3,3,1
```

## What this does and does not mean

This does **not** say that there are only four endpoint points or four elliptic curves. It only compresses one discrete part of the Q-descent condition.

Also,

```text
kappa=1
```

does not imply that `E` itself descends to an elliptic curve over Q: `psi` is an isomorphism of 8-torsion modules, not an isomorphism `E -> E^sigma`.

At cusps or points with extra automorphisms the fine-moduli uniqueness can fail, so those loci remain in `R29-MOD1D`.

The next arithmetic receiver is to test the four defect types against local Galois images, physical-open constraints and any available 2-adic image classification without assuming generic coverage.

```text
R29_MOD1B=PASS_CANDIDATE
R29_MOD1C=OPEN
R29_MOD1D=OPEN
ELLIPTIC_CURVE_DESCENT_PROVED=false
ENDPOINT_NONEXISTENCE_PROVED=false
```
