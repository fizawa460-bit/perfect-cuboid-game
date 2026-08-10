# Stage14 toolbox — two-quadrics and genus-one geometry

## 1. Two genus-one models currently in active reuse

Stage14 now has at least two distinct reusable genus-one presentations. They must be named before a theorem is imported.

### A. Fixed global-witness packet curve

For a primitive oriented Pythagorean base `S^2+X^2=H^2` and fixed nonzero signed kernels `(d0,d1,d2)`, the global witness equations are

```text
Q1=d0*u0^2-d1*u1^2-S^2*D^2=0,
Q2=d2*u2^2-d0*u0^2-X^2*D^2=0.
```

Thus

```text
C_sigma={Q1=Q2=0} subset P^3_[u0:u1:u2:D].
```

The pencil determinant is

```text
d0*d1*d2*lambda*mu*(lambda-mu)*(lambda*S^2+mu*X^2),
```

with four distinct singular parameters

```text
[0:1], [1:0], [1:1], [-X^2:S^2].
```

Direct Jacobian analysis proves `C_sigma` smooth. As a smooth `(2,2)` complete intersection in `P^3`, it has degree four and genus one.

The coordinate boundary `u0*u1*u2*D=0` is zero-dimensional; no accumulating line or conic is hidden there.

Eliminating `u0` gives

```text
d2*u2^2-d1*u1^2=H^2*D^2,
```

a smooth conic, while

```text
d0*u0^2=d1*u1^2+S^2*D^2
```

recovers a degree-two square lift branched at four geometric points.

### B. 4bq diagonal-pair moving-slope quartic

In the normalized good-cell residual,

```text
F=(q12^2*a0*d0)^2-(q21^2*b0*c0)^2,
G=(q22^2*b0*d0)^2-(q11^2*a0*c0)^2,
F*G=square>0.
```

Define

```text
U=q11*q22,
V=q12*q21,
UV=Q<=B.
```

Fixing `(q12,q21)` and the core, the moving pair `(x,y)=(q11,q22)` with reduced slope `t=x/y` lies on

```text
W^2=F0*((b0*d0)^2-(a0*c0)^2*t^4).
```

Fixing the other diagonal gives symmetrically

```text
W^2=G0*((a0*d0)^2*t^4-(b0*c0)^2).
```

These are smooth genus-one quartics. Pairwise coprimality makes the reduced slope injective back to the integer pair.

## 2. Geometry-to-count transfer checklist

Before converting a genus-one statement into a Stage14 count, verify all four layers:

```text
GEOMETRY
  smooth genus-one model identified

HEIGHT
  the relevant rational points lie in the bounded-height window required by the imported theorem

RECOVERY
  rational parameter/point recovers the original integer variables with controlled multiplicity

FAMILY SUM
  the remaining fixed parameters can be summed without losing the claimed exponent
```

For the fixed witness curve, the first layer is closed but a generic per-fixed-curve black box alone does not solve the moving packet-existence count.

For 4bq, all layers are supplied: fixed core + one diagonal gives `B^o(1)` possibilities for the other diagonal, coprime reduced slope gives injection, and `UV<=B` gives `min(U,V)<=B^(1/2)`. Therefore

```text
E_good-res(B)<<B^(3/7+1/2+o(1))=B^(13/14+o(1)).
```

## 3. Current main exponent ledger

Merged 4bq recombines

```text
small partner leg : 20/21 = 120/126
cross branch      : 61/63 = 122/126
good residual     : 13/14 = 117/126
```

so

```text
V(B)<<B^(61/63+o(1)).
```

Compared with the prior `41/42=123/126`, the first full direct post-local saving is

```text
1/126.
```

The current remaining gap to square-root scale is

```text
61/63-1/2=59/126.
```

Historical `10/21` thresholds remain valid inside stages that froze them relative to the old `41/42` checkpoint, but `10/21` is no longer the current remaining whole-family gap.

## 4. Fast dispatch

Use the witness two-quadrics cards when the variables are

```text
(u0,u1,u2,D; d0,d1,d2; S,X,H).
```

Use the diagonal-pair cards when the variables are

```text
(q11,q12,q21,q22; a0,b0,c0,d0; F,G; U,V).
```

If the argument says only “genus one” without specifying which model and which fixed/moving variables, stop and identify the quantifiers before importing any count.

## 5. Canonical cards

```text
TB-FORMULA-fixed-packet-two-quadrics
TB-FORMULA-two-quadric-pencil
TB-LEMMA-fixed-packet-smooth-genus-one
TB-LEMMA-coordinate-boundary-finite
TB-FORMULA-conic-square-lift
TB-LEMMA-diagonal-pair-genus-one-slope
TB-BOUND-diagonal-pair-genus-one-count
TB-WARNING-genus-one-quantifier-and-model-boundary
TB-LEDGER-current-main-after-4bq
```
