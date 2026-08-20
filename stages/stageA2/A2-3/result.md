# StageA2 A2-3 — published `-18` equation-(6) restart

## Scope

StageA2 restarts the equation-(6) anchor analysis from the published source after StageA1 was closed for the incorrect `-18 -> -8` source correction.

This task deliberately does **not** inherit any algebra from the quarantined StageA1 `-8` auxiliary curve. It follows the required restart order:

1. source PDF coefficient check;
2. independent transcription of equation (6);
3. exact numerical sanity check at a nondegenerate source parameter point;
4. symbolic anchor derivation from the published `-18` formula;
5. only then reciprocal quotient / reconstruction analysis.

The source is Andrew Bremner, Christian Elsholtz and Maciej Ulas, *There are infinitely many Hilbert cubes of dimension 3 in the set of squares*, arXiv:2604.05459v1, PDF p.13, equation (6).

## 1. Source PDF coefficient check

The published equation (6) gives

```text
a0 = (c^2+d^2)^2 F18(c,d,G,H)^2,
```

with

```text
F18 = -4 c^2 d^4 (c^2-d^2) G^4
      + (c^8-18 c^4 d^4+d^8) G^3 H
      + 8 c^2 d^2 (c^2-d^2)(2 c^2+d^2) G^2 H^2
      - (c^8-18 c^4 d^4+d^8) G H^3
      - 4 c^2 d^4 (c^2-d^2) H^4.
```

The coefficient is exactly

```text
-18 c^4 d^4.
```

The same `-18` coefficient also appears in the immediately preceding displayed `(P,Q)` formula in the source. Therefore StageA1's replacement by `-8` was not a source correction.

```text
SOURCE_PDF_COEFFICIENT_CHECK=PASS_MINUS18
SOURCE_LOCATOR=arXiv:2604.05459v1 PDF p.13 equation (6)
```

## 2. Exact source-parameter sanity check

Use the nondegenerate source parameter point

```text
(c,d,G,H)=(3,1,7,1).
```

Here

```text
c d G H (c^2-d^2)(G^2-H^2) != 0.
```

Direct evaluation of the published equation-(6) polynomials gives

```text
(a0,a1,a2,a3) =
(243180321177600,
 1521303552000000,
 1362949057806336,
 403778845016064).
```

All eight Hilbert-cube subset sums are exact squares:

```text
 a0                         = 15594240^2
 a0+a3                      = 25435392^2
 a0+a2                      = 40076544^2
 a0+a2+a3                   = 44832000^2
 a0+a1                      = 42005760^2
 a0+a1+a3                   = 46564608^2
 a0+a1+a2                   = 55923456^2
 a0+a1+a2+a3                = 59424000^2.
```

As a negative control, changing only `-18` to `-8` in the anchor factor changes only `a0` at this point and leaves exactly one of the eight sums square: the base `a0` itself. The other seven fail exact squareness.

Thus the source coefficient is not a cosmetic normalization; it is arithmetically essential.

```text
SOURCE_SANITY_POINT_CHECK=PASS
MINUS8_NEGATIVE_CONTROL=PASS_BREAKS_7_OF_8
```

## 3. Published anchor equation

For a rational member of this source family with `a0=0`, the factor `c^2+d^2` cannot vanish over `Q` at a nontrivial projective parameter pair. Hence the anchor condition is exactly

```text
F18(c,d,G,H)=0.
```

The basic nondegenerate walls remain

```text
c d G H (c^2-d^2)(G^2-H^2) != 0,
```

with all remaining equation-(6) factors in `a1,a2,a3` to be checked before accepting a reconstructed point.

Away from `dH=0`, set

```text
x = c/d,
r = G/H,
k = x^2,
u = r - 1/r.
```

After division of `F18=0` by `d^8 H^4`, the source anchor becomes

```text
-4 x^2(x^2-1)(r^4+1)
+ (x^8-18x^4+1)(r^3-r)
+ 8 x^2(x^2-1)(2x^2+1)r^2 = 0.
```

Divide by `r^2` and use

```text
r^2+r^(-2)=u^2+2.
```

The result is the exact reciprocal quadratic

```text
4 k(k-1)u^2
- (k^4-18k^2+1)u
- 16k^2(k-1)=0.                         (A2.3.1)
```

This is the published-`-18` anchor receiver.

## 4. First square condition: reciprocal genus-3 curve

Let

```text
A18(k)=k^4-18k^2+1.
```

The discriminant of (A2.3.1) in `u` is

```text
D18(k)=A18(k)^2+256k^3(k-1)^2
      =k^8-36k^6+256k^5-186k^4
       +256k^3-36k^2+1.                  (A2.3.2)
```

Its polynomial discriminant is

```text
disc(D18) = -2^80 * 3^3 * 5^2 != 0.
```

Hence

```text
C18: v^2=D18(k)
```

is a smooth hyperelliptic curve of genus `3`.

The points `k=0` and `k=1` lie on excluded source-parameter walls (`c=0` and `c^2=d^2`).

## 5. Reciprocal quotient: the correct genus-1 quartic

For `k != 0`, put

```text
z=k+1/k,
Y=v/k^2.
```

Since

```text
D18(k)/k^4
=(k^4+k^-4)-36(k^2+k^-2)+256(k+k^-1)-186,
```

and

```text
k^2+k^-2=z^2-2,
k^4+k^-4=z^4-4z^2+2,
```

we obtain

```text
E18: Y^2=z^4-40z^2+256z-112.             (A2.3.3)
```

The quartic discriminant is

```text
disc(z^4-40z^2+256z-112)
 = -2^32 * 3 * 5 != 0.
```

Thus (A2.3.3) is nonsingular of genus `1`.

At `k=1` one gets

```text
(z,Y)=(2,+/-16),
```

which is the excluded wall `c^2=d^2`, not a nondegenerate anchored cube.

This quartic, and **not** the StageA1 auxiliary quartic `Y^2=z^4-20z^2+256z-412`, is the canonical StageA2 equation-(6) quotient.

## 6. Exact reconstruction tower

A rational point on `E18` is only a necessary condition for a genuine anchored source point. A nondegenerate reconstruction must pass all of:

1. Recover `k` from

   ```text
   k+1/k=z,
   ```

   so `z^2-4` must be a rational square.

2. Recover `x=c/d` from `k=x^2`, so `k` itself must be a rational square.

3. Put `v=k^2Y` and recover

   ```text
   u=(A18(k)+/-v)/(8k(k-1)).
   ```

4. Recover `r=G/H` from `u=r-1/r`, so `u^2+4` must be a rational square and

   ```text
   r=(u+/-sqrt(u^2+4))/2.
   ```

5. Check all excluded source factors and require `a1,a2,a3` to be nonzero; positivity may be restored only through symmetries explicitly allowed by the source.

If all steps pass, the published equation (6) supplies a rational anchored Hilbert cube; clearing denominators by a common square yields an integer perfect cuboid.

No surviving nondegenerate point is claimed in A2-3.

## 7. Coverage firewall

Equation (6) is a two-projective-parameter family, with parameter ratios

```text
[c:d] in P^1,
[G:H] in P^1.
```

Its image in `[a0:a1:a2:a3]` has dimension at most `2`; imposing the nontrivial anchor `a0=0` cuts the parameter locus to dimension at most `1`.

The general anchored Hilbert-cube root variety is not known to be dominated by this one-dimensional source boundary. Therefore A2-3 proves no reverse map from an arbitrary perfect cuboid into equation (6).

The following remain forbidden:

- promoting any A2 family-specific obstruction to arbitrary perfect cuboids;
- citing A1-3 through A1-14 `-8` arithmetic as a restriction on the published family;
- treating the source family's existence or nonexistence as equivalent to the full perfect-cuboid problem.

## 8. A2-3 routing

A2-3 has rebuilt the canonical receiver from the published source and verified it against an exact nondegenerate source point. No Mordell-Weil rank, descent, or rational-point closure is imported from the quarantined A1 curve.

The next admissible task is a fresh analysis of the **correct** quartic (A2.3.3) and its exact reconstruction covers.

```text
A2_3_STATUS=SUBMITTED_FOR_AUDIT
A2_3_SOURCE_COEFFICIENT=-18
A2_3_SOURCE_PDF_CHECK=PASS
A2_3_NUMERICAL_SANITY_CHECK=PASS
A2_3_MINUS8_NEGATIVE_CONTROL=PASS_BREAKS_7_OF_8
A2_3_RECIPROCAL_QUADRATIC_PROVED=true
A2_3_GENUS3_CURVE=D18
A2_3_GENUS1_QUARTIC=Y^2=z^4-40z^2+256z-112
A2_3_RECONSTRUCTION_SQUARE_COVERS=3
A2_3_GENERAL_COVERAGE_PROVED=false
A2_3_NEW_ARBITRARY_CUBE_CONSTRAINT=false
A2_3_PERFECT_CUBOID_FOUND=false
A2_3_PERFECT_CUBOID_NONEXISTENCE_PROVED=false
A1_MINUS8_RESULTS_IMPORTED=false
AUDIT_REQUIRED=true
NEXT=A2-4_PUBLISHED_MINUS18_QUARTIC_AND_EXACT_COVERS
NEXT_EXPECTED_COMMAND=StageA2-audit
```
