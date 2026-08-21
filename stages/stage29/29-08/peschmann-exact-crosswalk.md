# Stage29-08 — exact Peschmann / Stage28 / joint-V4 crosswalk

```text
RECEIVER=R29-PESCH1
STATUS=PROPOSED_DISCHARGED_PENDING_FRESH_AUDIT
SOURCES=arXiv:2604.09328, arXiv:2604.28072, arXiv:2605.00573
```

## 1. Same two-face host

Use Peschmann's two primitive Euclid triples

```text
U1=a^2-b^2, V1=2ab, W1=a^2+b^2
U2=m^2-n^2, V2=2mn, W2=m^2+n^2
```

and edges

```text
e = U1*U2
x = V1*U2
y = U1*V2.
```

Then

```text
p=W1*U2, q=U1*W2
```

satisfy identically

```text
e^2+x^2=p^2
e^2+y^2=q^2.
```

Thus Peschmann's Euclid-pair chart lands on the exact Stage29-07 two-face canonical model

```text
T2bar={e^2+x^2=p^2, e^2+y^2=q^2} subset P4,
```

whose resolution is the Stage28 base `Y=Bl_4(P1xP1)`.

On `e!=0`, put

```text
t1=x/e=V1/U1
t2=y/e=V2/U2.
```

## 2. The two residual Peschmann square conditions are literally the Stage28 radicands

Peschmann's Master condition is

```text
M=(V1*U2)^2+(U1*V2)^2.
```

Therefore

```text
M/e^2 = (V1/U1)^2+(V2/U2)^2
      = t1^2+t2^2
      = f_face.
```

Peschmann's `H-total` / space-diagonal norm is

```text
H=(W1*U2)^2+(U1*V2)^2.
```

Using `W1^2=U1^2+V1^2`,

```text
H/e^2 = (W1/U1)^2+(V2/U2)^2
      = 1+(V1/U1)^2+(V2/U2)^2
      = 1+t1^2+t2^2
      = f_sp.
```

Hence the exact same residual two roots are being adjoined:

```text
sqrt(M)/e = sqrt(f_face)  # third face
sqrt(H)/e = sqrt(f_sp)    # space diagonal.
```

This is an equation-level identity on the same physical chart, not a similarity of patterns.

```text
PESCHMANN_PROVEN_F2_ADAPTER=true
PESCHMANN_INDEPENDENT_FOUNDATION=false
R29-PESCH1=DISCHARGED_PENDING_AUDIT
```

## 3. Meaning of the genus-3 reduction

The genus-3 family

```text
C_A: w^2=lambda^8+A lambda^4+1
```

is obtained only after fixing one Euclid ratio and reparametrizing/eliminating part of the same two-root problem. It is therefore a curve-level/fibration chart inside the already-audited two-face/joint-V4 architecture, not a new endpoint surface.

The 2026 source itself preserves a specialization firewall: a perfect cuboid gives a nondegenerate rational point on `C_A`; a converse at specialized rational parameters requires additional square-factor control and is not used globally.

## 4. Peschmann's May elliptic fibration

For fixed `(m,n)`, arXiv:2605.00573 writes the Master equation as

```text
H_mn: s^2=V2^2*t^4+(4*U2^2-2*V2^2)*t^2+V2^2,
```

with `t=a/b`, and gives a Weierstrass normalization `E_mn` plus a rational function `tau` with

```text
tau(P)=t^2.
```

Because `H_mn` is exactly the Master/third-face equation above, this is an elliptic fibration chart on the Euler-brick / Stage20 marginal, not a new full-endpoint foundation. The remaining space-diagonal test is still `f_sp`.

New bounded downstream receiver:

```text
R29-PESCH2=MasterHitEllipticFibrationToStage20EulerK3FibrationClassAndPhysicalPolarizationAdapter
PRIMARY_OWNER=J12-PARAMETRIC
```

## 5. Population firewall

The exact equation crosswalk does not make finite Peschmann databases into Stage16--20 population theorems. No asymptotic, density or height saving is imported from the finite 1,072-fiber or million-brick computations.

```text
FINITE_DATABASE_IS_GLOBAL_COVERAGE=false
FINITE_BLOCKER_VERIFICATION_IS_THEOREM=false
HEIGHT_COUNT_TRANSFER_AUTOMATIC=false
ASYMPTOTIC_TRANSFER=false
PERFECT_CUBOID_CONCLUSION=false
```
