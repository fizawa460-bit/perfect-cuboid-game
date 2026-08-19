# StageA1 A1-3 — general published anchor-boundary geometry

## Scope

This task takes the two-parameter projective Hilbert-cube family displayed as equation (6) in Bremner–Elsholtz–Ulas, *There are infinitely many Hilbert cubes of dimension 3 in the set of squares*, arXiv:2604.05459v1 (2026), and imposes the perfect-cuboid anchor condition `a0=0` before any one-parameter specialization.

This is **not** assumed to parametrize every Hilbert cube. Coverage is audited separately below.

## 1. Exact anchor polynomial from equation (6)

The paper gives

```text
a0 = (c^2+d^2)^2 F(c,d,G,H)^2,
```

where

```text
F = -4 c^2 d^4 (c^2-d^2) G^4
    + (c^8-18 c^4 d^4+d^8) G^3 H
    + 8 c^2 d^2 (c^2-d^2)(2 c^2+d^2) G^2 H^2
    - (c^8-18 c^4 d^4+d^8) G H^3
    - 4 c^2 d^4 (c^2-d^2) H^4.
```

Over `Q`, `c^2+d^2=0` forces `c=d=0`, which is not a projective parameter pair. Hence every rational anchored member of this family satisfies exactly

```text
F(c,d,G,H)=0.
```

For a nondegenerate cube we in particular exclude the obvious parameter walls

```text
c d G H (c^2-d^2)(G^2-H^2)=0,
```

because the displayed equation-(6) increments contain these factors and/or the construction denominators become invalid. Any eventual rational point must also be checked against every remaining zero factor of `a1,a2,a3` and against positivity/order after applying the paper's finite symmetry group.

## 2. Projective normalization and reciprocal reduction

Equation (6) is homogeneous of degree 20 in `(c,d)` and degree 8 in `(G,H)`. Therefore, away from `dH=0`, write

```text
x = c/d,
r = G/H,
k = x^2,
u = r - 1/r.
```

After dividing the anchor equation by `d^8 H^4`, the exact equation is

```text
-4 x^2(x^2-1)(r^4+1)
+ (x^8-18x^4+1)(r^3-r)
+ 8 x^2(x^2-1)(2x^2+1)r^2 = 0.
```

Dividing by `r^2` and using

```text
r^2+r^(-2) = u^2+2
```

gives the quadratic equation

```text
4 k(k-1) u^2
- (k^4-18k^2+1) u
- 16 k^2(k-1) = 0.                    (A1.3.1)
```

Thus the quartic equation in `r` has been reduced, without approximation, to a quadratic equation in the reciprocal invariant `u=r-1/r`.

## 3. First square condition: genus-3 hyperelliptic quotient

Let

```text
A(k) = k^4-18k^2+1.
```

The discriminant of (A1.3.1) is

```text
D(k) = A(k)^2 + 256 k^3(k-1)^2
     = (k^4-8k^3+30k^2-8k+1)
       (k^4+8k^3-2k^2+8k+1).          (A1.3.2)
```

Hence a rational nondegenerate boundary point maps to a rational point on

```text
C : v^2 = D(k).
```

The two quartic factors in (A1.3.2) are coprime and squarefree over `Q` (their resultant is `2^24`; their discriminants are respectively `1769472` and `-1638400`). Thus `D` is squarefree of degree 8 and the smooth hyperelliptic model `C` has genus 3.

The obvious points `k=0` and `k=1` come from excluded/degenerate parameter walls (`c=0` or `c^2=d^2`).

## 4. Second reciprocal quotient: an elliptic quartic

Both quartic factors in `D(k)` are reciprocal. For `k != 0`, put

```text
z = k + 1/k,
Y = v/k^2.
```

Then

```text
(k^4-8k^3+30k^2-8k+1)/k^2 = z^2-8z+28,
(k^4+8k^3-2k^2+8k+1)/k^2  = z^2+8z-4.
```

Therefore every rational nondegenerate boundary point maps to

```text
E : Y^2 = (z^2-8z+28)(z^2+8z-4)
          = z^4-40z^2+256z-112.       (A1.3.3)
```

The quartic on the right has discriminant

```text
-15 * 2^32 != 0,
```

so (A1.3.3) is a nonsingular genus-1 curve. It has the rational points

```text
(z,Y)=(2,+/-16),
```

but these correspond to `k=1`, hence to the already-excluded wall `c^2=d^2`.

This genus-1 quotient is the principal new structural output of A1-3.

## 5. Exact reconstruction tower

A rational point of `E` is only a **necessary** condition. To reconstruct a genuine rational point of the original anchor boundary one must pass all of the following exact square-cover conditions.

1. Recover `k` from

   ```text
   k + 1/k = z.
   ```

   Thus `z^2-4` must be a rational square.

2. Recover `x=c/d` from `k=x^2`; hence `k` itself must be a rational square.

3. Put `v=k^2 Y` and recover `u` from

   ```text
   u = (A(k) +/- v)/(8 k(k-1)).
   ```

4. Recover `r=G/H` from `u=r-1/r`; hence `u^2+4` must be a rational square and

   ```text
   r = (u +/- sqrt(u^2+4))/2.
   ```

5. Check all excluded equation-(6) factors and require the resulting `a1,a2,a3` to be nonzero and, after allowed symmetries, positive.

If all five steps hold, equation (6) supplies a rational anchored Hilbert cube. Since `a0=0`, the three increments are rational squares and all four remaining subset sums are rational squares. Clearing denominators by a common square then produces an integer perfect cuboid. Thus a single nondegenerate rational point surviving this tower would be a genuine positive solution of the perfect-cuboid problem.

No such point is claimed here.

## 6. Coverage audit: equation (6) is not a universal reverse map

The source family has two projective parameter ratios:

```text
[c:d] in P^1,
[G:H] in P^1.
```

Because every `ai` in (6) is bihomogeneous (degree 20 in `(c,d)`, degree 8 in `(G,H)`), the projective image `[a0:a1:a2:a3]` has dimension at most 2. The anchor equation `a0=0` cuts its nontrivial parameter image to dimension at most 1.

By contrast, write the eight square roots of a general 3-dimensional Hilbert cube as

```text
p^2 = a0,
q^2 = a0+a1,
r^2 = a0+a2,
s^2 = a0+a1+a2,
P^2 = a0+a3,
Q^2 = a0+a1+a3,
R^2 = a0+a2+a3,
S^2 = a0+a1+a2+a3.
```

After eliminating the four `ai`, the projective root variety in `P^7` is cut out by four quadrics, for example

```text
q^2+r^2 = p^2+s^2,
q^2+P^2 = p^2+Q^2,
r^2+P^2 = p^2+R^2,
s^2+P^2 = p^2+S^2.
```

On the anchored hyperplane `p=0`, this becomes a variety in `P^6` cut out by four equations. Every irreducible component therefore has dimension at least 2 (codimension at most 4). Passing from square roots to the `ai` only has finite sign ambiguity generically, so this is the relevant algebraic-moduli dimension.

Consequently the one-dimensional anchor boundary coming from equation (6) cannot algebraically dominate the full anchored-cube variety. There is no justified reverse map from an arbitrary perfect cuboid to this published family.

This does **not** rule out the possibility that all positive integral anchored points happen to lie on a lower-dimensional locus; proving such concentration would itself require a new theorem and is not supplied by the source.

## 7. A1-3 go/no-go verdict

A1-3 does **not** produce general coverage and does not produce a new necessary condition for every perfect cuboid.

However, it does produce a genuinely new, exact and much smaller rational-point target:

```text
published equation-(6) anchor boundary
    -> genus-3 reciprocal curve C
    -> genus-1 quartic E
    -> three explicit square-cover tests
    -> original nondegenerate boundary.
```

This is more than another family-specific discriminant exclusion: the full published two-parameter family has been reduced to a concrete elliptic quotient plus explicit reconstruction conditions. Therefore the reconnaissance receives a **limited GO** to A1-4, solely to determine whether this exact boundary tower has any nondegenerate rational points.

Anti-loop limit for A1-4:

- do not broaden to unrelated Hilbert-cube literature;
- do not introduce a new parametrized family unless it strictly enlarges coverage;
- first determine a Weierstrass model/rank-or-descent information for (A1.3.3), then impose the three square-cover conditions;
- if A1-4 cannot close the rational points after a bounded direct attempt, or if it only proves a family-specific exclusion, StageA1 terminates rather than spawning a refinement chain.

```text
A1_3_STATUS=COMPLETE_GENERAL_PUBLISHED_BOUNDARY_REDUCTION
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
NEXT=A1-4
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=StageA1-audit
```
