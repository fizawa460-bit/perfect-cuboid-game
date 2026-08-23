# Stage32-01 — exact polytail reduction

## Input

The source-locked `picard-core.json` is regenerated from the pinned upstream Testa--Stoll Magma blob.  It contains the rank-64 Picard intersection lattice, 92 known nonexceptional curve classes, 48 exceptional classes, the canonical class `H`, and the 64-class primitive basis selected upstream.

## Exact positive identity

In the dual Picard lattice, direct integer reconstruction gives

```text
19 H^* = sum_{i=1}^{92} D_i^* + 5 sum_{j=1}^{48} E_j^*,
```

or, evaluated on an arbitrary Picard class `x`,

```text
19 (H.x)
 = sum_{i=1}^{92} (D_i.x)
 + 5 sum_{j=1}^{48} (E_j.x).
```

`verify_polytail_reduction.py` checks this coordinatewise using integers only.  It also checks that the 64 upstream primitive basis rows occur exactly among the 140 exported intersection rows and that their Gram determinant is

```text
-268435456 = -2^28 != 0.
```

Hence the 140 intersection forms span the full 64-dimensional rational dual space.

## Consequence for the homogeneous tail

A genuinely new irreducible candidate must satisfy the Stage29 necessary inequalities

```text
D_i.x >= 0,
E_j.x >= 0.
```

If additionally `H.x=0`, the positive identity forces every one of the 140 nonnegative terms to be zero.  Since the selected 64 forms are independent, this forces `x=0`.

Therefore

```text
KNOWN_CURVE_TAIL_INTERSECT_HPERP = {0}
FIXED_POSITIVE_H_DEGREE_SLICE_BOUNDED = true
```

This is an exact certificate and does not require a polyhedral dualization, Normaliz, or rank-63 close-vector enumeration.

## Immediate branch-and-bound bounds

For a candidate of canonical degree `d=H.x>0`, positivity and the same identity imply

```text
0 <= D_i.x <= 19*d,
0 <= E_j.x <= floor(19*d/5).
```

Thus every one of the 183 audited degree/genus rows has an explicit finite intersection-coordinate box before the adjunction/norm, congruence, automorphism, incidence, and known-class filters are applied.

## Scope

This closes only the smaller Class-2 leaf `L32-01-POLYTAIL`.  It does not enumerate the bounded slices and therefore does not set

```text
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=true
R29_LG2_NUMERICAL_COMPONENT_COMPLETE=true
```

The next computational leaf is the exact resumable graded integer/orbit enumerator inside these certified bounded slices.
