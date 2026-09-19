# MB104 Z1--Z30 post-conductor re-audit — 2026-09-19

Status: **Z-ONLY PARALLEL RE-AUDIT / POST-CONDUCTOR UPDATE / NO CREDIT**

## Scope

This note updates only the original Z1--Z30 research portfolio.

Later-numbered results are used strictly as input facts when they refine an old Z-route.  No Z31+
route is adopted as the research target.

The current Z1--Z30 priority from the earlier re-audit was:

```text
Tier 1: Z12, Z3
Tier 2: Z21+Z16+Z6+Z11+Z14
Tier 3: Z2, Z4', Z5', Z25
```

The purpose here is to remove routes that are now demonstrably exhausted and identify the true
remaining open theorem interfaces.

## 1. Z3 is exhausted on the balanced uniform hard core

The exact balanced ray

```text
P=7H-4 sum_(i in Sigma)E_i
```

is big and nef, and the complete P-null locus is classified.

The numerical null-lattice/discriminant route is vacuous because P is already an integral class
in Pic(S).  The generalized-Jacobian gluing calculation then gives:

```text
00070b000f0f  excluded by non-torsion cycle holonomy,
0000770000ff  survives; null graph is a forest,
00007b0000ff  survives; null graph is a forest,
000707000f0f  survives; ordinary and all finite formal Picard gluing vanish.
```

Thus no hidden negative curve, hidden null curve, lattice gluing, ordinary Pic0 gluing, or finite
formal Picard obstruction remains on the three surviving balanced orbits.

Disposition:

```text
Z3 = EXHAUSTED on balanced uniform sector.
```

## 2. Z12 remains mathematically open but execution-blocked

The exact ordinary BTVA cubic coefficient at node support size N is

```text
c_N=(144-11N)/108.
```

Hence

```text
c_13=1/108>0,
c_14=-5/54<0.
```

The published BTVA construction is abstractly arbitrary-m but the perfect-cuboid executable
demonstration is m=2.  No source-locked graded family currently supplies all of:

```text
W_m,
local extension maps for general m,
multiplication maps,
support-specific kernel V_m(T),
quotient by the known hyperplane-generated submodule,
primitive cubic Hilbert coefficient.
```

Disposition:

```text
Z12 = OPEN MATHEMATICALLY / BLOCKED BY GENERAL-m GRADED INTERFACE.
```

## 3. Z2 is source-complete no-go on the balanced ray

The clean theorem candidates have now been checked:

- Miyaoka single-curve inequality: strictly satisfied for all l;
- Sabatino open-surface theorem: direct Theorem 1.1(i) substitution is strictly satisfied for all
  l, all exceptional-boundary subsets and all alpha in [0,1], with uniform positive margin;
- Langer normal log-pair BMY: useful coefficient depends on local orbifold terms not determined by
  the current singularity package, while log-canonicity forces alpha=O(1/l), eliminating an
  ambient l-growth contradiction.

Disposition:

```text
Z2 = EXHAUSTED for currently source-valid theorem shapes.
```

## 4. Z4' is genuinely improved by the exact conductor scheme

The old Z4' wall said the quadratic singularity mass had no controlled zero-dimensional
surface-side object.

That is no longer true.

The intrinsic conductor scheme now gives exactly

```text
Z_cond subset smooth interior of S,
length(Z_cond)=delta(C)=168l^2+56l.
```

So Z4' has a true quadratic localization object.

However the natural postulation/vector-bundle continuation does not close the carrier.

### 4a. Natural adjoint system

The conductor scheme imposes exactly delta(C) independent conditions on |K_S+C|.  Thus the
canonical adjoint dimension count is exact equality, not overdetermination.

### 4b. Serre/Reider/Bogomolov preflight

The exact intrinsic Cayley--Bacharach hypothesis needed for Hartshorne--Serre is not currently
source-locked for this surface conductor scheme.

Even granting the strongest favorable CB assumption and constructing

```text
0 -> O_S -> V -> I_Zcond(C) -> 0,
```

we get

```text
c1(V)^2=336l^2,
c2(V)=168l^2+56l,
4c2-c1^2=336l^2+224l>0.
```

Therefore Bogomolov instability is not forced.

Disposition:

```text
Z4' = ACTIVE ONLY IF a stronger conductor postulation/regularity theorem is found.
Natural adjoint and Serre/Bogomolov continuations are exhausted.
```

## 5. Z5' has no remaining independent invariant in the tested architecture

The e=4 packet on 000707000f0f has exact data:

```text
two saturated factor fibers,
support-hyperplane factorization,
common labelled G-cover,
exact Kummer square classes,
exact Abel class of the different.
```

The distinguished half-fiber ratio descends as a rational function on the box surface, so its
conductor/first-jet compatibility is automatic.

The three Kummer square-class equalities are exactly the function-field encoding of the already
known common character subcovers; they add no fourth Abel--Jacobi constraint.

Disposition:

```text
Z5' = EXHAUSTED for the current common-G / half-fiber / Kummer architecture.
```

A revival requires genuinely new marked divisor data not recoverable from the existing common
G-cover.

## 6. The Z21+Z16+Z6+Z11+Z14 equality engine does not consume the conductor scheme

The current exact equality packet is

```text
M=R=O=d,
every supported exceptional contact has m=1.
```

Z21 is saturated on the hostile balanced ray.  Z6 and Z11 are saturated.  Z14 controls
non-diagonal exceptional collision data.

The new conductor scheme is supported in the smooth interior and is disjoint from the exceptional
contact locus.  Therefore it does not change:

```text
the supported-node multiplicities,
M,
R,
O,
the exceptional collision term,
the Z21 root-lattice equality.
```

Hence it supplies no strictness to the current inequality engine.

Disposition:

```text
Z21+Z16+Z6+Z11+Z14 remain load-bearing helpers,
but no new equality-breaking term is obtained from Z_cond.
```

## 7. Updated Z1--Z30 hierarchy

### Still mathematically live

```text
Z12
  needs a source-complete general-m support-specific graded differential module.

Z4'
  needs a stronger theorem on intrinsic conductor postulation/regularity/support,
  beyond length and natural adjoint equality.
```

### Live only if a genuinely new theorem appears

```text
Z25
  requires a collision/tangency theorem stronger than ordinary simple-contact equality.

Z5'
  requires a new marked-packet invariant outside the tested common-G/Kummer architecture.
```

### Exact helper package, not independent closer

```text
Z6 Z11 Z14 Z16 Z21
```

### Exhausted / absorbed as independent closers on the current balanced hard core

```text
Z1 Z2 Z3 Z4 Z5 Z7 Z8 Z9 Z10
Z13 Z15 Z17 Z18 Z19 Z20
Z22 Z23 Z24 Z26 Z27 Z28 Z29 Z30
```

## 8. Recommended next Z-only research

The only two routes worth a deep allocation are now:

```text
A. Z12:
   recover/build a general-m support-specific graded interface,
   or prove a Hilbert-series coefficient directly without full module construction.

B. Z4':
   locate a theorem on intrinsic conductor ideals/schemes of Cartier curves on surfaces
   that controls regularity, generators, or support strongly enough to beat the exact adjoint
   equality.
```

Everything else should remain shallow until one of these produces new strictness.

## Firewalls

```text
Z1_Z30_post_conductor_reaudited=true
Z3_balanced_uniform_exhausted=true
Z12_general_m_interface_missing=true
Z2_source_valid_shapes_exhausted=true
Z4P_quadratic_conductor_scheme_exact=true
Z4P_natural_serre_bogomolov_closer=false
Z5P_current_architecture_exhausted=true
composition_engine_strictness_from_conductor=false
finite_degree_window_proved=false
whole_uniform_ray_closed=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
