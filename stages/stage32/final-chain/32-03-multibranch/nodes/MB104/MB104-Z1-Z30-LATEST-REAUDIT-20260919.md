# MB104 Z1--Z30 latest re-audit — 2026-09-19

Status: **Z-ONLY RE-AUDIT USING N>=14 / Z33 EQUALITY / CURRENT NULL-LOCUS INPUT / NO CREDIT**

## Scope

This note re-evaluates only the original population-wide Z1--Z30 routes.

Later Z31--Z33 results are used only as new input facts. They are not treated as replacement route labels.
W-routes and P6 subroutes are likewise used only when they materially settle a Z-route's proposed mechanism.

Current compact branch head observed before write:
`ac772b7e45ea87138298d80e307e7ec3868bcf15`.

## New global facts since the original Z1--Z30 breadth scan

The re-audit uses these later exact/pre-audit inputs:

1. BTVA support threshold:
   ```text
   unbounded genus <=1 family => N>=14.
   ```
   Ordinary BTVA is positive through N<=13 and fails exactly at N=14.

2. Z33 span-five genus-one equality:
   ```text
   M=R=O=d,
   every branch has m=1,
   div(nu^*h)=B_node reduced.
   ```

3. For the uniform balanced incidence-16 ray, the archived finite quotient leaves four support orbits:
   ```text
   0000770000ff  48
   00007b0000ff  48
   000707000f0f 768
   00070b000f0f 768
   ```

4. Local zero-quartic landing avoidance does not close those orbits: the diagonal lambda locus remains infinite.

5. The zero-pairing elliptic-quartic restriction is exactly trivial:
   ```text
   P|_Q ~= O_Q.
   ```
   Hence there is no torsion/divisibility obstruction from restriction alone.

6. Negative expected dimension / equigeneric isolation does not imply emptiness.

These facts materially change the old Z portfolio.

## Reclassification key

- **ACTIVE-HIGH**: concrete next exact object exists and directly addresses the current N14 wall.
- **ACTIVE-SPECIFIC**: alive only on a specific support/cone/packet sector, not population-wide by itself.
- **PROVED-HELPER**: exact/pre-audit inequality now feeds the live route but cannot close alone.
- **CONDITIONAL**: needs a missing theorem/adapter before another exact computation is useful.
- **HARD/ABSORBED**: tested architecture is dead or subsumed by another Z route.

## Z1--Z10

### Z1 smooth Bogomolov / big cotangent
**HARD.**
The smooth resolution has negative Segre input; later N14 information does not change the sign gate.

### Z2 orbifold canonical-degree
**CONDITIONAL-HIGH.**
Still the cleanest population-wide theorem shape. The singular canonical model has favorable orbifold invariants, but no source-valid theorem currently handles arbitrary multibranch passage through the 48 A1 points with coefficient strong enough to beat the exact equality packet.

Later P6 Miyaoka/log-BMY checks do not prove this orbifold theorem; they instead show the obvious smooth or correction-term substitutions are insufficient.

### Z3 effective cone / stable base
**ACTIVE-SPECIFIC.**
Not useful as generic effectivity: the rays are effective. But for the four balanced incidence-16 support orbits, current Z33 null-locus work is precisely the strong version of Z3: determine whether the primitive ray is compatible with the complete null lattice / cone.

Z33E kills the simplest restriction-torsion version, but does not yet kill discriminant/gluing or a complete cone obstruction.

### Z4 aggregate delta inequalities
**HARD standalone.**

### Z4' localization / collision refinement
**ACTIVE-SPECIFIC / NARROWED.**
The later equality package removes higher contact in the span-five genus-one tail: all m=1. Local finite landing exclusion is now known insufficient. A useful Z4' must therefore be genuinely cross-node/global: force repeated lambda/jet relations or localize the quadratic defect into analytically controlled singularities.

### Z5 generic product-cover boundedness
**HARD.**

### Z5' packet-sensitive arithmetic product
**CONDITIONAL / DEMOTED.**
Later common-cover/Kummer/Nielsen work shows the natural labelled G-cover and square-class constraints are largely tautological or presentation-dependent. A revival needs new exact branch-value/marked-divisor data, not more generic correspondence theory.

### Z6 generic product hyperbolicity
**HARD as closer; PROVED-HELPER as branch-count input.**
The revived exact consequence
```text
O >= d-4g+4
```
is now essential. In the genus-one span-five equality sector it combines with M<=d to force
```text
M=R=O=d.
```
Do not discard Z6; discard only its standalone finite-window claim.

### Z7 Seshadri
**HARD.**
Canonical Seshadri price vanishes along the (-2) exceptional locus where the contact lives.

### Z8 generic syzygy rank
**HARD.**
The 7-dimensional ambient subsystem remains too incomplete.

### Z9 smooth Miyaoka elliptic-degree aggregate
**ABSORBED BY Z2/Z16.**

### Z10 stable-map negative virtual dimension
**HARD as emptiness route.**
Later equigeneric isolation confirms the same point: isolated obstructed carriers are allowed.

## Z11--Z20

### Z11 García-Fritz / Vojta differential inequality
**PROVED-HELPER / STRUCTURAL.**
The exact inequality
```text
d <= M + 4g - 4
```
is one of the load-bearing inputs. In the genus-one span-five N14 equality sector, Z33 supplies M<=d, so Z11 is saturated:
```text
M=d.
```
It diagnoses the wall but does not close it.

### Z12 adaptive higher symmetric differentials
**ACTIVE-HIGH.**
This is stronger now than at the original Z30 comparison.

At N=14 ordinary BTVA misses by exactly
```text
5/54 * m^3 + O(m^2).
```
Fixed m, fixed finite jet depth, and proportional support-hyperplane powers cannot repair the cubic sign.

The exact current object is support-specific graded growth
```text
V_m(T)=ker(W_m -> direct_sum Q_(s,m))
```
after removing the known support-hyperplane-generated submodule.

The published BTVA perfect-cuboid ancillary provides a concrete possible general-m implementation surface. This is a real executable research route, not merely a theorem wish.

### Z13 irregular Albanese lift bound
**HARD population-wide.**
Lift genus grows with the packet.

### Z14 finite-node collision
**HARD generic; PROVED-HELPER in refined form.**
The revived non-diagonal collision inequality remains useful:
```text
Delta_exc >= T^2/(4N)-T/2.
```
But Z33D shows finite forbidden landing sets cannot control the surviving diagonal lambda family.

### Z15 projective genus-degree
**HARD.**
Arithmetic genus growth is the mechanism, not a contradiction.

### Z16 Miyaoka/Vojta canonical-degree
**PROVED-HELPER / REVIVED.**
The old breadth classification was too pessimistic. Miyaoka Theorem 1.3 on the smooth resolution combines with Z21 and gives explicit finite bounds for N<=9.

It is no longer merely conjectural, although the stronger Vojta bounded-gonality population theorem remains conditional.

### Z17 negative curves
**HARD population-wide.**
Dangerous rays have positive square.

### Z18 Hilbert/Chow boundedness
**HARD.**
N14 does not force one bounded Hilbert stratum.

### Z19 foliation/web
**ABSORBED BY Z12 unless a fixed independent foliation is produced.**

### Z20 function-field abc
**ABSORBED BY Z11/Z12.**

## Z21--Z30

### Z21 A1 root-lattice Hodge projection
**PROVED-HELPER / MAJOR.**
This remains one of the strongest internal exact mechanisms:
```text
D^2 + 1/2 sum M_i^2 <= d^2/16.
```
Combined with Z16 it gives explicit windows through N<=9.

BTVA then independently moves the unbounded frontier to N>=14.

At the hostile balanced ray, Z21 is exact equality, so it cannot close the tail without an equality-breaking input. Its current role is to convert any nonuniformity/extra contact/global Picard direction into quantitative degree control.

### Z22 Serrano extension
**HARD.**
The resolved normalization has negative self-intersection.

### Z23 fundamental group
**HARD.**
Singular image graph loops grow with branch excess.

### Z24 finite discriminant/Picard congruence
**HARD standalone / FILTER ONLY.**
However, do not confuse this with current Z3-style null-lattice discriminant/gluing. A finite congruence of the whole Picard ray cannot bound l; a support-specific primitive gluing obstruction could still exclude an orbit and belongs under Z3.

### Z25 lct / alpha
**CONDITIONAL HELPER.**
Ordinary distinct-lambda multiple points saturate the ordinary lct scale. It becomes useful only after Z4' forces tangent/jet collisions stronger than the ordinary configuration.

### Z26 fixed orbifold-cover classification
**ABSORBED BY Z5'.**

### Z27 KSBA scaling
**HARD.**

### Z28 Cartan SMT
**ABSORBED BY Z12.**

### Z29 K-stability
**HARD.**

### Z30 smooth aggregate Miyaoka counting
**ABSORBED BY Z2.**

## Current Z-only hierarchy

After N>=14 and the latest Z33D/E information, the old ranking
`Z2 > Z21/Z4' > Z12`
should be replaced by:

### Tier 1 — directly executable now

```text
Z12
  support-specific graded BTVA/Hilbert growth at N=14

Z3
  support-specific complete null-lattice / cone / gluing test
  on the four balanced incidence-16 orbits
```

These have concrete finite/executable next objects.

### Tier 2 — active composition

```text
Z21 + Z16 + Z6 + Z11 + Z14
```

This package already produced:
- explicit N<=9 windows;
- unbounded support pushed to N>=14 after BTVA;
- in span-five genus one, M=R=O=d and all m=1;
- quantitative non-diagonal collision control.

It is not one new theorem route; it is the exact inequality engine to consume any new equality-breaking fact.

### Tier 3 — theorem/adapter dependent

```text
Z2   orbifold canonical-degree theorem
Z4'  cross-node/global landing or singularity localization
Z5'  marked packet-sensitive arithmetic correspondence
Z25  lct only after collision input
```

### Retire as independent closers

```text
Z1 Z4 Z5 Z7 Z8 Z9 Z10
Z13 Z15 Z17 Z18 Z22 Z23 Z27 Z29
```

### Keep only as absorbed views

```text
Z19 Z20 Z24 Z26 Z28 Z30
```

(Z24 remains usable as a finite filter but not a population degree bound.)

## Practical next order

For a Z-only parallel effort that does not follow later AI-generated numbering:

1. **Z3-specific**: finish the four balanced-orbit null-lattice/gluing test.
2. **Z12**: recover the BTVA ancillary and determine whether general-m support-extension Hilbert growth is executable.
3. Feed any strictness from 1 or 2 into the **Z21+Z16+Z6+Z11+Z14** inequality package.
4. Revisit **Z2** only when an actual source-valid orbifold canonical-degree theorem is located.
5. Do not spend a deep allocation on Z5'/Z25 without a new marked-packet/collision adapter.

## Firewalls

```text
Z1_Z30_reaudited=true
N_ge_14_used_as_input=true
Z33_equality_used_as_input=true
Z33D_local_landing_no_go_used=true
Z33E_trivial_restriction_used=true
finite_degree_window_proved_population_wide=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
