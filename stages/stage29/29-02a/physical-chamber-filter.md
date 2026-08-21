# Stage29-02a — positive physical chamber filter for low-degree curves

This note combines the Testa--Stoll low-degree classification with the Stage29 physical endpoint chamber.  It is an elementary applicability adapter, not a new external theorem.

## Source classification

Testa--Stoll Definition 6 defines the known low-degree set `G=G0 union G1 union G2 union G3`:

- `G0`: exceptional curves above the 48 singular points;
- `G1`: conics in `a1=0`, `a2=0`, `a3=0`, or long diagonal `c=0`;
- `G2`: genus-one curves in `b1=0`, `b2=0`, or `b3=0`, where the `b_i` are face diagonals;
- `G3`: genus-one curves in hyperplanes `a_j=±a_{j+1}` or `a_j=± i c`.

Corollary 18 identifies `G` with all integral curves of canonical degree at most 6 on the minimal desingularization; Theorem 17 separately states there are no integral degree-6 curves on the projective cuboid surface.

## Physical filter

A Stage29 physical endpoint point has positive rational side lengths, positive rational face diagonals, and positive rational long diagonal.

### G1

`a_j=0` gives a zero side.  `c=0` gives zero long diagonal.  Hence `G1` has no positive nondegenerate physical endpoint point.

### G2

`b_j=0` means a face diagonal is zero.  Over the positive real chamber this forces both sides of that face to vanish.  Hence `G2` has no positive nondegenerate physical endpoint point.

### G3: equal-side components

If `a_j=±a_{j+1}` with nonzero rational sides, the corresponding face diagonal satisfies

```text
b_k^2 = a_j^2+a_{j+1}^2 = 2 a_j^2.
```

For rational nonzero `a_j`, rational `b_k` would imply `sqrt(2)` rational.  Therefore there is no nonzero rational physical endpoint point on these components.

### G3: imaginary long-diagonal components

`a_j=± i c` has no point in the positive real chamber with `a_j,c>0`.

### G0

`G0` lies over the singular locus of the projective canonical model.  These are not positive nondegenerate rational-box points; the positive physical endpoint lies in the smooth nondegenerate locus used by Stage29.

## Consequence

Every integral curve of canonical/projective degree at most 6 on the full cuboid surface is excluded from carrying a positive nondegenerate rational-box family.

Equivalently, any integral curve on the full endpoint surface that genuinely carries positive nondegenerate physical endpoint points and is not confined to a finite exceptional intersection must lie outside the complete degree-<=6 classification.  Since the source also rules out odd-degree curves in this setting, the first possible canonical degree for such a curve-family route is at least 8.

```text
POSITIVE_NONDEGENERATE_ENDPOINT_CURVE_DEGREE_LE_6=ABSENT
FIRST_POSSIBLE_CANONICAL_CURVE_DEGREE_FOR_PHYSICAL_FAMILY>=8
PERFECT_CUBOID_POINT_NONEXISTENCE_PROVED=false
```

## Firewall

This is a statement about **curve-family carriers**, not isolated rational points.  It does not say that a hypothetical perfect cuboid cannot be an isolated rational point or lie on higher-degree curves.  It also does not identify Stage20 `M_face` degree with full-endpoint canonical degree.
