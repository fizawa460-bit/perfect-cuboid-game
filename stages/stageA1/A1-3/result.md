# StageA1 A1-3 — general published anchor-boundary geometry

## Scope

This task takes the two-parameter projective Hilbert-cube family displayed as equation (6) in Bremner–Elsholtz–Ulas, *There are infinitely many Hilbert cubes of dimension 3 in the set of squares*, arXiv:2604.05459v1 (2026), and imposes the perfect-cuboid anchor condition `a0=0` before any one-parameter specialization.

This is **not** assumed to parametrize every Hilbert cube. Coverage is audited separately below.

## Audit correction of the source coefficient

The first draft accidentally copied the coefficient `-18 c^4 d^4` from the preceding `(P,Q)` formula into equation (6). The actual equation-(6) anchor factor has coefficient **`-8 c^4 d^4`**. All downstream curve equations in this file use the corrected source coefficient.

## 1. Exact anchor polynomial from equation (6)

Up to the common projective scaling used in equation (6), the source gives

```text
a0 = (c^2+d^2)^2 F(c,d,G,H)^2,
```

where

```text
F = -4 c^2 d^4 (c^2-d^2) G^4
    + (c^8-8 c^4 d^4+d^8) G^3 H
    + 8 c^2 d^2 (c^2-d^2)(2 c^2+d^2) G^2 H^2
    - (c^8-8 c^4 d^4+d^8) G H^3
    - 4 c^2 d^4 (c^2-d^2) H^4.
```

Over `Q`, `c^2+d^2=0` forces `c=d=0`, which is not a projective parameter pair. Hence every rational anchored member of this family satisfies

```text
F(c,d,G,H)=0.
```

For a nondegenerate cube we exclude the parameter walls

```text
c d G H (c^2-d^2)(G^2-H^2)=0,
```

because equation (6) then forces at least one displayed increment to vanish or the construction normalization becomes invalid. Any eventual point must also be checked against all remaining zero factors of `a1,a2,a3` and against positivity after the paper's finite symmetry action.

## 2. Projective normalization and reciprocal reduction

Equation (6) is bihomogeneous of degree 20 in `(c,d)` and degree 8 in `(G,H)`. Away from the already-degenerate walls `dH=0`, put

```text
x = c/d,
r = G/H,
k = x^2,
u = r - 1/r.
```

After division by `d^8 H^4`, the corrected anchor equation is

```text
-4 x^2(x^2-1)(r^4+1)
+ (x^8-8x^4+1)(r^3-r)
+ 8 x^2(x^2-1)(2x^2+1)r^2 = 0.
```

Divide by `r^2` and use

```text
r^2+r^(-2)=u^2+2.
```

The constant terms cancel exactly, leaving

```text
4 k(k-1)u^2
- (k^4-8k^2+1)u
- 16k^2(k-1)=0.                       (A1.3.1)
```

Thus the quartic equation in `r` reduces exactly to a quadratic in the reciprocal invariant `u=r-1/r`.

## 3. First square condition: genus-3 reciprocal curve

Set

```text
A(k)=k^4-8k^2+1.
```

The discriminant of (A1.3.1) is

```text
D(k)=A(k)^2+256k^3(k-1)^2
    =k^8-16k^6+256k^5-446k^4+256k^3-16k^2+1.   (A1.3.2)
```

Therefore every rational nondegenerate boundary point maps to

```text
C: v^2=D(k).
```

The polynomial `D` is reciprocal of degree 8. Its discriminant is

```text
-2^58 * 3^2 * 5^4 * 13 * 19^3 != 0,
```

so it is squarefree. Hence the smooth hyperelliptic model `C` has genus 3.

The points arising from `k=0` or `k=1` lie on excluded parameter walls (`c=0` or `c^2=d^2`).

## 4. Reciprocal quotient: a genus-1 quartic

For `k != 0`, put

```text
z=k+1/k,
Y=v/k^2.
```

Since

```text
D(k)/k^4
=(k^4+k^-4)-16(k^2+k^-2)+256(k+k^-1)-446,
```

and

```text
k^2+k^-2=z^2-2,
k^4+k^-4=z^4-4z^2+2,
```

we obtain the quotient

```text
E: Y^2=z^4-20z^2+256z-412.             (A1.3.3)
```

The quartic discriminant is

```text
-2^27 * 5^2 * 19 != 0,
```

so (A1.3.3) is a nonsingular genus-1 curve. It has the obvious rational points

```text
(z,Y)=(2,+/-6),
```

which correspond to `k=1` and hence to the excluded wall `c^2=d^2`.

This corrected genus-1 quotient is the principal family-specific structural output of A1-3.

## 5. Exact reconstruction tower

A rational point on `E` is only a necessary condition. To reconstruct a genuine rational point of the original anchor boundary one must pass all of the following.

1. Recover `k` from

   ```text
   k+1/k=z.
   ```

   Hence `z^2-4` must be a rational square.

2. Recover `x=c/d` from `k=x^2`; hence `k` itself must be a rational square.

3. Put `v=k^2Y` and recover `u` from

   ```text
   u=(A(k)+/-v)/(8k(k-1)).
   ```

4. Recover `r=G/H` from `u=r-1/r`; hence `u^2+4` must be a rational square and

   ```text
   r=(u+/-sqrt(u^2+4))/2.
   ```

5. Check every excluded equation-(6) factor and require the resulting `a1,a2,a3` to be nonzero and, after allowed symmetries, positive.

If all five steps hold, equation (6) gives a rational anchored Hilbert cube. Clearing denominators by a common square then yields an integer perfect cuboid. Thus one nondegenerate rational point surviving the tower would solve the existence problem. No such point is claimed here.

## 6. Coverage audit: equation (6) is not a universal reverse map

The source family has two projective parameter ratios

```text
[c:d] in P^1,
[G:H] in P^1.
```

Its projective image `[a0:a1:a2:a3]` therefore has dimension at most 2, and the nontrivial anchor equation `a0=0` cuts the parameter space to dimension at most 1.

For comparison, write the eight square roots of a general dimension-3 Hilbert cube as

```text
p^2=a0,
q^2=a0+a1,
r^2=a0+a2,
s^2=a0+a1+a2,
P^2=a0+a3,
Q^2=a0+a1+a3,
R^2=a0+a2+a3,
S^2=a0+a1+a2+a3.
```

After eliminating the `ai`, the projective root variety in `P^7` is cut out by four quadrics, for example

```text
q^2+r^2=p^2+s^2,
q^2+P^2=p^2+Q^2,
r^2+P^2=p^2+R^2,
s^2+P^2=p^2+S^2.
```

On the anchor hyperplane `p=0`, this is a subvariety of `P^6` cut out by four equations. Hence every irreducible component has dimension at least 2. Generically the passage from square roots to the increments has only finite sign ambiguity.

Consequently a one-dimensional equation-(6) anchor boundary cannot algebraically dominate the full anchored-cube variety. No reverse map from an arbitrary perfect cuboid to this published family is proved.

This does not rule out the logically separate possibility that all positive integral anchored points lie on a smaller locus; proving such concentration would require a new theorem not supplied here.

## 7. A1-3 go/no-go verdict after audit repair

A1-3 does **not** establish general coverage and does not derive a new necessary condition for every perfect cuboid.

It does, however, leave an unresolved exact boundary problem rather than merely excluding another specialization:

```text
published equation-(6) anchor boundary
    -> corrected genus-3 reciprocal curve C
    -> corrected genus-1 quartic E
    -> three square-cover tests
    -> original nondegenerate boundary.
```

Because a surviving rational point would directly construct a perfect cuboid, the hard-stop rule is interpreted narrowly enough to permit **one bounded A1-4 rational-point closure attempt on this exact corrected tower**. This is not an expansion to new families and is not evidence of general coverage.

A1-4 anti-loop limit:

- work only on the corrected quartic `Y^2=z^4-20z^2+256z-412` and its exact square-cover tower;
- do not rotate to unrelated Hilbert-cube families or literature;
- first obtain a Weierstrass model and bounded rank/descent information, then impose `z^2-4`, `k`, and `u^2+4` square conditions;
- if that bounded direct attempt does not produce a nondegenerate rational point or a complete family-specific rational-point closure, terminate StageA1;
- no family-specific nonexistence statement may be promoted to arbitrary perfect cuboids without a new coverage theorem.

```text
A1_3_STATUS=COMPLETE_WITH_AUDIT_REPAIR
A1_3_SOURCE_COEFFICIENT_CORRECTED=true
A1_3_ANCHOR_FACTOR=F(c,d,G,H)
A1_3_RECIPROCAL_QUADRATIC_PROVED=true
A1_3_GENUS3_QUOTIENT_PROVED=true
A1_3_GENUS1_QUOTIENT_PROVED=true
A1_3_RECONSTRUCTION_SQUARE_COVERS=3
A1_3_GENERAL_COVERAGE_PROVED=false
A1_3_ARBITRARY_CUBE_NEW_INVARIANT=false
A1_3_PERFECT_CUBOID_FOUND=false
A1_3_PERFECT_CUBOID_NONEXISTENCE_PROVED=false
A1_3_VERDICT=GO_LIMITED_A1_4
NEXT=A1-4_BOUNDED_ONLY
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=StageA1-audit
```
