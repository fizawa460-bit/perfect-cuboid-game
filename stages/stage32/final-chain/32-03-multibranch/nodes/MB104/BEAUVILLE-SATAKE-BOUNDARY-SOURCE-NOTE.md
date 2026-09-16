# Stage32 MB104 source note — Satake boundary components

Status: **EXTERNAL PUBLISHED SOURCE ADAPTER / NO CLOSURE / NO CREDIT**

## Source

Eberhard Freitag and Riccardo Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016), 675--691, DOI `10.1307/mmj/1480734014`, especially Theorem 2.4 and Proposition 2.7.

Only the following published facts are imported here.

## 1. Product modular cover and box coordinates

Over `C`, the box variety is the diagonal modular quotient of

```text
C8 x C8,
C8 = H*/Gamma[8],
G ~= (Z/2)^3.
```

The three face-diagonal coordinates are

```text
Z1 = theta01(z) theta01(w),
Z2 = theta00(z) theta00(w),
Z3 = theta10(z) theta10(w).
```

The Stage32 convention is

```text
(b1,b2,b3)=(Z1,Z2,Z3).
```

## 2. Satake boundary

The Satake boundary is the union of the images of

```text
H* x {a}
and
{a} x H*,
```

for rational cusps `a`.  Freitag--Salvati Manni prove that after passing to the box quotient it consists of exactly twelve smooth elliptic curves.

Each such elliptic boundary component contains exactly

```text
8 singular zero-dimensional cusps
and
8 smooth zero-dimensional cusps.
```

The whole boundary is the zero divisor of

```text
Z1 Z2 Z3.
```

Thus every irreducible elliptic component of one of the divisors

```text
Z1=0, Z2=0, Z3=0
```

is a Satake boundary component.

## 3. Boundary component as one-factor cusp orbit

A boundary component is obtained from the `G`-orbit of a vertical or horizontal boundary line in `C8 x C8` with one factor fixed at a cusp.  If that cusp has singular stabilizer `<s>` of order two, then its `G`-orbit has size four.

For any rank-two subgroup

```text
H=<s,t> <= G
```

containing that singular stabilizer, the same four-cusp `G`-orbit splits into exactly two `H`-orbits, because

```text
|H|/|<s>|=2.
```

Consequently, after quotienting the factor curve by `H`, one box-boundary component can contribute points only over **two** marked factor-quotient values on its fixed-coordinate side.

This last sentence is only elementary orbit counting applied to the published modular-cover description; it does not assert any concentration of different normalization branches at one of the two values.

## Firewalls

- No Stage32 carrier is asserted to lie in a boundary component.
- A carrier meeting a box node on a boundary component need not be tangent to that boundary component.
- The adapter supplies only the location of the underlying product-cover point: its fixed factor coordinate belongs to one of the two `H`-orbits attached to that boundary component.
- No per-node branch-value concentration or divisibility is claimed.
- No receiver/theorem/endpoint/Perfect-Cuboid credit.
- No merge authorization.
