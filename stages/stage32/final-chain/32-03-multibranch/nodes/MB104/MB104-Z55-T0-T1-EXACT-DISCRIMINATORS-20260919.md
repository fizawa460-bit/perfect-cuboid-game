# MB104 Z55 — exact equivalent discriminators for the T0/T1 tangent bit — 2026-09-19

Status: **PRE-AUDIT EXACT ONE-BIT RECEIVER / ACTUAL BIT NOT YET EVALUATED / NO CREDIT**

## Input

Z54 reduces the projectivized tangent cone of the size48 canonical-cover germ to exactly two
projective equivalence classes

```
T0 = V(x^2, yz),
T1 = V(x^2, yz+xw)
```

in P3_[x:y:z:w].

Both have reduced support the same two distinct intersecting lines

```
L1={x=y=0},
L2={x=z=0},
P0=L1 cap L2=[0:0:0:1].
```

The purpose of Z55 is to turn the remaining choice into several exact, bounded tests.

## 1. Rank-four-quadric discriminator

For T0 the pencil is

```
a x^2 + b yz.
```

Every member has rank at most three because w is absent.

For T1 the pencil is

```
a x^2 + b(yz+xw).
```

For b != 0 the symmetric matrix has nonzero determinant, hence rank four.

Therefore

```
T0 <=> every tangent quadric is singular,
T1 <=> the tangent pencil contains a nonsingular quadric.
```

This is coordinate-independent.

## 2. Local embedding-dimension discriminator at P0

Work in the affine chart w=1.

### T0

```
O_(T0,P0) ~= C[[x,y,z]]/(x^2,yz).
```

Both relations have order at least two, so the Zariski tangent space has dimension three:

```
embdim_P0(T0)=3.
```

### T1

```
O_(T1,P0) ~= C[[x,y,z]]/(x^2,yz+x).
```

The second equation has linear term x.  Eliminate x=-yz to obtain

```
O_(T1,P0) ~= C[[y,z]]/(y^2 z^2).
```

Hence

```
embdim_P0(T1)=2.
```

Thus

```
T0 <=> embdim at the line-intersection point is 3,
T1 <=> embdim at that point is 2.
```

## 3. Pencil determinant discriminator

Represent a tangent quadric by its symmetric 4x4 matrix.

For T0,

```
det(a Q_x2 + b Q_yz) == 0
```

identically in [a:b].

For T1,

```
det(a Q_x2 + b Q_(yz+xw))
```

is a nonzero scalar multiple of b^4.

Therefore the pencil determinant is

```
identically zero  <=> T0,
nonzero quartic    <=> T1.
```

This is the cheapest symbolic test once two quadratic initial relations are available.

## 4. Actual cuboid local input isolated

For the size-48 supports the ambient incidence-16 hyperplane is

```
b1=0.
```

The cuboid surface equations include

```
a2^2+a3^2-b1^2=0,
a1^2+a2^2+a3^2-c^2=0.
```

Their difference gives the exact local rank-three quadric

```
a1^2+b1^2-c^2=0.
```

At either omitted b1=0 box node, the two zero elliptic quartics in one Q-E-Q fiber are the two
branches

```
b1=0,
a1-c=0
```

and

```
b1=0,
a1+c=0.
```

Thus the original A1 plumbing coordinate system is source-explicit.

What is still missing is not the base A1 equation.  It is the map from these cuboid/A1 coordinates
through

```
A1 resolution
 -> index-three canonical cover
 -> two A2 resolutions
 -> maximal-ideal generators of the contracted Gorenstein cover
 -> m/m^2
```

far enough to recover one quadratic pencil determinant.

This is the exact adapter that Z55 now isolates.

## 5. Symmetry check

The size-48 support is preserved by sign-change automorphisms such as

```
c -> -c
```

which swaps the two elliptic branches at an omitted node, and

```
b1 -> -b1
```

which fixes each branch and reverses the transverse A1 coordinate.

These symmetries descend through the contraction and lift to the unique canonical cover.

However, without the induced character representation on `m/m^2`, they do not distinguish T0
from T1: both normal forms admit line-swapping and line-preserving involutions.

Therefore symmetry alone is not promoted to a bit value.

## 6. Bounded next computation

The remaining calculation can be stated without ambiguity.

Choose one omitted node, for example P31 in the canonical b1=0 section.  In an analytic chart
eliminate the three smooth directions from the four cuboid quadrics and use

```
X=a1,
Y=b1,
Z=c,
X^2+Y^2-Z^2=0
```

as the A1 germ.

Track the two branches X=+Z and X=-Z through the explicit resolution and the cyclic cover with
local equations

```
u=t^3,
uv=s^3
```

at smooth/crossing charts.  Construct four generators of the maximal ideal of the contracted cover
with divisor at least

```
F=(1,2,2,2,2,2,1).
```

Then compute the two relations modulo m^3.  The single required output is

```
DET_PENCIL_IDENTICALLY_ZERO
```

or

```
DET_PENCIL_NONZERO.
```

No higher-order ICIS normal form is needed for this gate.

## Decision

The actual T0/T1 bit is **not** asserted yet.

Z55 converts the problem to one exact binary receiver with three interchangeable verification
interfaces:

```
rank-four quadric,
embedding dimension at P0,
pencil determinant.
```

## Firewalls

```
actual_tangent_type_selected=false
symmetry_promoted_to_bit=false
maximal_ideal_generators_materialized=false
equivariant_smoothing_known=false
downstairs_local_correction_computed=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
