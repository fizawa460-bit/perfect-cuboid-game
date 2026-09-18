# Stage32 MB104 — SOFT-PARK second-depth screening Round 1 — 2026-09-18

Status: **ROUND 1 COMPLETE / W4,W16 ADVANCE FOR THIRD-DEPTH / W13 RESERVE / W26,W31 PARK / NO MATHEMATICAL CREDIT**

## Purpose

The W1--W31 wide scan has already sampled the major top-level mechanisms.  This phase does not manufacture W32+ variants.  It revisits selected SOFT-PARK directions one level deeper and asks whether each has a concrete route to one of the only two MB104 success shapes:

1. all-`l` exclusion of the exact balanced ray; or
2. explicit large-`l` exclusion leaving a finite exact backend.

Round 1 screens

```
W4   K3 quotient / full lattice wall
W13  stable base locus / effective cone
W16  nontrivial Cayley--Bacharach subcluster
W26  equisingular T-smoothness / Severi regularity
W31  non-tautological Lazarsfeld--Mukai / coherent systems
```

The active numerical ray remains

```
D_l = 7l H - 4l sum_(p in Sigma) E_p,
|Sigma|=14,
D_l^2=336l^2,
K.D_l=112l,
Delta=168l^2+56l.
```

No result below is theorem/receiver/endpoint credit.

## W4 — K3 quotient full root-wall test

### What the previous shallow tests killed

For the seven coordinate-sign K3 quotients, the pushdown classes have degree `112l` and square

```
a1  1344 l^2
a2  1344 l^2
a3  1376 l^2
b1  1152 l^2
b2  1152 l^2
b3   736 l^2
c   1312 l^2.
```

Parity, Hodge index, and the sampled elliptic-fibration intersections are all compatible.  The published degree-2/4 curve classification does not touch degree `112l`.

### Second-depth correction

Pure K3 **effectivity** is not the right target.  Each primitive pushdown `P` has `P^2>0` and positive hyperplane degree.  On a K3 surface, Riemann--Roch makes non-effectivity of such a positive class an implausible closure target.

The useful exact target is instead a **root wall**.

For a coordinate involution `sigma`, the active support is not `sigma`-invariant.  Hence a hypothetical integral carrier cannot be invariant under that involution; its restriction to the degree-two quotient is generically degree one.  Its image is therefore an integral genus-one curve in class `lP`.

If the rank-20 K3 lattice contains an effective `(-2)` root `R` with

```
P.R < 0,
```

then every effective member of `|lP|` contains `R` for every `l>=1`.  An integral image of positive square cannot equal that `(-2)` curve, so this gives an all-`l` contradiction.

Thus W4 now has a concrete exact gate:

```
for each of the seven primitive pushdown rays P:
    decide P.R >= 0 for every effective (-2)-root R.
```

One negative root closes the corresponding quotient uniformly.  If every primitive ray is nef against the complete root system, this W4 architecture is genuinely exhausted.

The Stoll--Testa verification code already constructs the quotient Picard lattice of rank 20, its intersection pairing, automorphism action, and known curve/fibration data, so the missing step is a bounded lattice/root-wall computation rather than a new branch-lift adapter.

**Disposition: ADVANCE_FOR_THIRD_DEPTH.**

## W13 — stable base locus / effective-cone route

Because `D_l=lD_1`, any genuine fixed divisorial component forced by the primitive ray propagates uniformly to every positive multiple.

A negative effective curve `R` with

```
D_1.R < 0
```

would be an immediate all-`l` obstruction to an integral carrier.  If no negative wall exists, a complete W13 proof would still have to determine every effective class in the null locus

```
D_1.R=0
```

and prove that at least one is fixed in every `|lD_1|`.

The known zero-pairing elliptic quartics do **not** do this: retained primitive-rank work proves them nonfixed for all `l`.

The difficulty is source-completeness.  On the original cuboid surface the Picard rank is 64.  Existing low-degree curve inventories are not a complete effective/nef cone at the active degree, and the historical Stoll--Testa analysis explicitly notes that the large Picard rank obstructs extending their lattice enumeration to high degree.

W13 therefore has a valid all-`l` closure shape, but its next gate is much larger than W4:

```
source-complete D_1-negative/null effective-curve inventory on Pic(S), rank 64.
```

**Disposition: RESERVE.**  Revisit if W4 produces reusable cone/root machinery or a new source-complete negative-curve theorem appears.

## W16 — nontrivial canonical Cayley--Bacharach subcluster

This is the strongest conceptual survivor in Round 1.

The full genus-defect cluster is too large for the standard Serre/Bogomolov instability package.  The previously tested obvious linear-size cluster `C intersect B_E` is also useless because its Serre bundle splits tautologically.

But the numerical window for a **non-split canonical proper CB cluster** is very favorable.  Put

```
L_l = D_l-K.
```

Then

```
L_l^2 = 336l^2-224l+16.
```

Suppose every hypothetical MB104 carrier canonically supplies a zero-dimensional lci Cayley--Bacharach subscheme `Z_l` such that the associated Serre extension is non-split and

```
length(Z_l) <= 112l.
```

Its Bogomolov discriminant would satisfy

```
L_l^2 - 4 length(Z_l)
 >= 336l^2-672l+16.
```

Hence

```
l=1:  -320
l>=2: >0.
```

So a source-complete nontrivial CB construction of only linear size would immediately supply the required **large-`l` exclusion with cutoff L=1**, leaving only `l=1` to an exact finite backend.

This is precisely the MB104 success shape that most other SOFT-PARK routes lack.

The missing statement is not numerical.  It is geometric:

```
actual MB104 carrier
 -> canonical proper CB subscheme Z_l of O(l) length
 -> non-split Serre extension
 -> destabilizing divisor constraints
 -> carrier contradiction.
```

The old `C intersect B_E` cluster cannot be reused because it gives the split bundle.  The next third-depth test must therefore search the equisingularity/conductor package for a *proper minimal dependency* or another intrinsic CB scheme, not choose a subcluster ad hoc.

**Disposition: ADVANCE_FOR_THIRD_DEPTH.**

## W26 — equisingular T-smoothness / Severi regularity

The previous problem was not merely that the clean published theorems assume rank one or classes proportional to `K`.  There is also an asymptotic coefficient wall for the standard Bogomolov/T-smoothness architecture.

Using the most favorable ordinary-node model for the missing quadratic defect, the number of nodes has leading term `168l^2`.  In the Keilen-type `gamma_alpha` criterion, an ordinary node contributes `(1+alpha)^2`, while the right side has leading term

```
alpha (D_l-K)^2 ~ 336 alpha l^2.
```

Thus the leading inequality would require

```
168(1+alpha)^2 < 336 alpha
<=> 1+alpha^2 < 0,
```

which is impossible over the reals.

Therefore simply extending the known T-smoothness criterion from Picard rank one to the cuboid lattice with the same local invariant/constants would still not close MB104.  A useful W26 revival would need genuinely packet-specific extra structure that changes the coefficient, not just removal of the Picard-rank hypothesis.

That packet-specific dependency is exactly the kind of input W16 asks for, so W26 is currently dominated by W16 as a research route.

**Disposition: PARK_DOMINATED_BY_W16.**

External reference used for this diagnostic:
Thomas Keilen, *Smoothness of Equisingular Families of Curves*, Trans. AMS 2006 / arXiv:math/0308247.

## W31 — non-tautological Lazarsfeld--Mukai / coherent systems

The retained rank-seven construction from

```
A=O_C(H)
```

is hard-dead because `A` extends from the surface and yields the explicit tautological extension

```
0 -> O_S(D_l-H) -> E -> M_H^vee -> 0.
```

To revive W31 one needs an intrinsic line bundle or coherent subsystem on the normalization/carrier which is canonically produced by **every** MB104 carrier but does not come by restriction from a globally generated bundle on `S`.

The currently retained natural systems do not supply such an all-carrier input:

- the canonical seven-section system is the tautological construction above;
- the product-factor pencils are induced by ambient/fibration geometry;
- the more exotic half-hyperplane data live on the residual double-cover model, are tied to the `e=2` branch, and depend on additional conditional structure.

No source-complete carrier-wide intrinsic coherent system is presently available.  Without one, another instability calculation would only manufacture a different tautology or cover only a subcase.

**Disposition: PARK_NO_CURRENT_INTRINSIC_SYSTEM.**

## Round-1 selection

```
ADVANCE_FOR_THIRD_DEPTH:
  W4   exact rank-20 K3 (-2)-root wall
  W16  canonical non-split O(l)-size CB subcluster

RESERVE:
  W13  rank-64 stable-base / complete null-locus

PARK:
  W26  standard coefficient architecture cannot close; dominated by W16
  W31  no source-complete non-tautological all-carrier coherent system
```

This is a research-priority selection only.  It grants no mathematical closure or downstream credit.

## Next second-depth round

Continue the user-directed SOFT-PARK review with

```
W5   adaptive higher symmetric differentials
W6   coupled two-factor modular relation
W11  special seven-section elliptic linear-series relations
W20  cuboid-specific residue / Abel moment identities
W30  four-quadric-specific Gaussian identities
```

Use the same test: require a source-complete forward adapter and either an all-`l` contradiction or an explicit large-`l` cutoff before advancing a route to third-depth work.
