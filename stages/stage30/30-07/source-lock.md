# Stage30-07 — source lock for eight marked K8 defects

```text
ROLE=EIGHT_MARKED_K8_DEFECT_TRANSPORT_SOURCE_LOCK
STATUS=SUBMITTED_PENDING_AUDIT
```

## Audited inputs

This stage uses only already-audited repository inputs.

1. `stages/stage29/29-02g/exact-q-moduli-adapter.md`

```text
K8 = ker(SL2(Z/8) -> SL2(Z/4))
kappa = psi^sigma o psi in K8
```

2. `stages/stage29/29-15/bounded-execution.md`

```text
K8={I+4A mod 8 : A in sl2(F2)}
|K8|=8
SIGMA_ACTION_ON_K8=TRIVIAL
MARKED_ARITHMETIC_DEFECT_CLASS_COUNT=8
ordinary unmarked conjugacy sizes=1,3,3,1
```

The Stage29 label `identity` in the ordinary `A in sl2(F2)` classification refers to `A=I`; the corresponding K8 element is `I+4I=5I mod 8`, not the identity element of K8.  Stage30-07 keeps this distinction explicit.

3. `stages/stage30/30-06/source-action-lift-audit-repair.md`

On one source-derived `X(8)` factor,

```text
S: u -> i*v, v -> i*u, w -> w
T: u -> zeta_8*u, v -> i*w, w -> i*v
```

and on the common quotient

```text
U=u1*u2=2*b1
V=v1*v2=2*b2
W=w1*w2=2*b3.
```

4. `stages/stage30/30-06C/audit.md` and `semilinear-certificate.json`

```text
PSL2(Z/4) order=24
SEMILINEAR_ALL24_VERIFIED=true
THETA_FIXES_V_MOD_POINTWISE=true
c_sigma=delta_a3
```

No Stage30-06C output classified or eliminated a K8 defect.

## Exact K8 -> G0 sign-deck adapter

Write

```text
A = [[a,b],[c,a]] in sl2(F2)
kappa(A)=I+4A mod 8.
```

The source-derived one-factor action determines the natural `K8 ~= G0` sign-deck identification as follows.

### Basis E12

The standard level-8 translation satisfies

```text
T^4 = I+4*E12 mod 8.
```

From the source `X(8)` action,

```text
T^4: u -> -u, v -> v, w -> w.
```

Hence

```text
E12 -> flip u.
```

### Basis E21

Residual `S` conjugation interchanges `E12` and `E21` modulo 2.  The source action interchanges the `u` and `v` sign coordinates.  Therefore

```text
E21 -> flip v.
```

### Central basis I

`A=I` is the unique nonzero element of `sl2(F2)` fixed by the full residual `SL2(F2) ~= S3` conjugation action.  In the three-bit sign module on `(u,v,w)`, the unique nonzero vector fixed by all permutations is `(1,1,1)`.  Therefore

```text
I -> flip {u,v,w}.
```

By linearity the exact adapter is

```text
phi([[a,b],[c,a]]) = (a+b, a+c, a) in F2^3_(u,v,w).
```

Using `U=2b1`, `V=2b2`, `W=2b3`, this becomes the endpoint sign-deck representative

```text
(a+b, a+c, a) on (b1,b2,b3).
```

The committed builder and independent verifier check equivariance under the residual generators and all 24 residual elements.

## Ordinary versus marked equivalence

Residual `S4=PSL2(Z/4)` conjugation on K8 factors through reduction to `SL2(F2)=S3`.  Under `phi`, this is exactly permutation of the three sign bits.  Thus the ordinary unmarked orbit sizes are the Hamming-weight layers

```text
weight 0: 1
weight 1: 3
weight 2: 3
weight 3: 1.
```

This is not the marked arithmetic quotient.  The audited sigma action on K8 is trivial and K8 is abelian, so the marked twisted relation remains equality.  Therefore all eight defects remain eight distinct marked Q-descent classes.

## Scope firewalls

```text
K8_EQUALS_V_MOD=false
COORDINATE_COCYCLE_C_SIGMA_EQUALS_KAPPA=false
ORDINARY_S4_ORBIT_EQUALS_MARKED_ARITHMETIC_CLASS=false
MARKED_Q_DESCENT_CLASS_COUNT=8
DEFECT_ELIMINATION_COUNT=0
PHYSICAL_ENDPOINT_EXCLUSION_PROVED=false
R29_KUM5_DISCHARGED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
