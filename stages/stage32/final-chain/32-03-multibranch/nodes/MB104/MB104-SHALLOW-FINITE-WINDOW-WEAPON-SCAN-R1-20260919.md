# MB104 — shallow finite-window weapon scan R1 — 2026-09-19

Status: **PRE-AUDIT SHALLOW PORTFOLIO SCAN / NO ROUTE DEEPENED / NO CREDIT**

## Governing rule

The sole dangerous equality-packet frontier is the size-768 support

```
000707000f0f.
```

This pass tests three weapon shapes at equal shallow depth.  It does not deepen the best-looking
route merely because the other two fail.

The target is always one of

```
l <= L
```

or direct exclusion of the 000707 dangerous packet.

## A. Intrinsic conductor postulation / regularity

Exact available input:

```
Z_cond subset S_smooth,
length(Z_cond)=168l^2+56l.
```

This is the correct quadratic scale.

Academic search again returns Eisenbud--Ulrich, *The Regularity of the Conductor*, as the closest
direct regularity theorem.  Its theorem controls conductor schemes for plane curves and more
generally certain projectively Gorenstein varieties.

The retained MB104 carrier is an integral Cartier divisor on the smooth cuboid resolution, but
there is no uniform proof that its P6 homogeneous coordinate ring is arithmetically Gorenstein or
arithmetically Cohen--Macaulay.  This is exactly the hypothesis wall already isolated in Z48B.

No new source found in this shallow pass supplies the missing intrinsic-surface theorem.

Disposition:

```
HIGH UPSIDE,
NO NEW ADAPTER FOUND,
DO NOT DEEPEN IN R1.
```

## B. Primitive Hilbert / symmetric-differential shortcut

Z12 needs a support-specific improvement over the ordinary BTVA N=14 cubic coefficient

```
-5/54.
```

The shallow literature search found general asymptotic results on Hilbert coefficients and syzygy
growth over complete intersections, but not a theorem computing the primitive support quotient of
the BTVA symmetric-differential module from coarse Hilbert data alone.

In particular, nothing found bypasses all of

```
general-m module,
support local-extension map,
known hyperplane-generated submodule,
primitive quotient.
```

Disposition:

```
HIGH UPSIDE,
MULTI-INTERFACE BUILD STILL REQUIRED,
NO SHORTCUT FOUND,
DO NOT DEEPEN IN R1.
```

## C. Collision / tangency strictness from delta or conductor mass

The shallow search finds useful local delta formulas for curves on rational surface singularities,
delta-constant collision theory for plane-curve singularities, and tangency formulas for unibranch
plane curves.

These do not match the current required shape.

The MB104 conductor scheme lies in the smooth interior of S, while the equality packet

```
M=R=O=d,
all supported exceptional contacts m=1
```

is carried by the fourteen A1 exceptional packets.  A useful theorem must couple these two
geographically disjoint pieces and produce strictness in the global equality engine.

No source located in R1 supplies that coupling.

Disposition:

```
NEW-THEOREM SHAPE ONLY,
NO EXECUTABLE ADAPTER FOUND,
DO NOT DEEPEN IN R1.
```

## R1 comparison

```
A conductor postulation      : nearest theorem shape, hypothesis mismatch
B primitive Hilbert shortcut : direct finite-window shape, too many missing interfaces
C collision strictness       : no theorem coupling smooth conductor to exceptional packet
```

No R1 route has earned a deep allocation.

## New shallow weapon family for R2

Rotate rather than deepen.

The most interesting fresh top-down observation is the scale comparison

```
C^2=336l^2,
K.C=112l,
delta(C)=168l^2+56l.
```

For a big linear system |lP|, Riemann--Roch has leading dimension approximately

```
(1/2)C.(C-K) = 168l^2-56l
```

before lower-order surface terms, while the equigeneric defect required to force normalization
genus one is

```
delta = 168l^2+56l.
```

The leading quadratic terms tie exactly, but the linear terms differ by 112l.

This suggests a genuinely top-down weapon:

```
Severi / equigeneric codimension / deformation-theoretic strictness.
```

If the genus-one locus has codimension at least delta (or delta minus a uniformly bounded defect)
inside |lP| on this surface, the linear mismatch could force a finite l window.

This is not yet a theorem claim.  It is a new shallow-search direction.

R2 should compare at least three fresh shapes:

1. equigeneric/Severi expected-codimension theorems for integral Cartier curves on smooth surfaces;
2. jet-ampleness / k-very-ampleness criteria for lP after accounting for the complete P-null locus;
3. deformation-theoretic conductor/Tjurina bounds that control the superabundance of the equigeneric
   locus.

Do not return to A/B/C unless a new theorem is found.

## Firewalls

```
R1_route_A_closed=false
R1_route_B_closed=false
R1_route_C_closed=false
R1_deep_route_selected=false
finite_degree_window_proved=false
dangerous_000707_excluded=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
