# Stage32 32-03 — Z-wide population finite-window scan, Round 3 (Z11-Z15) — 2026-09-19

Status: **USER-DIRECTED BREADTH SCAN / WHOLE R29-LG2-MB POPULATION / NO MATHEMATICAL CREDIT**

## Scope

This round stays above the balanced `000707` subtree and does not deepen W16-H.

Target:

```text
all multibranch nonexceptional integral carriers
g(normalization) in {0,1}
=> population-wide finite degree/intersection window
```

The balanced `000707` family is used only as a hostile test case.

---

## Z11 — García-Fritz / Vojta symmetric-differential main inequality

**Result: HARD standalone, but STRUCTURAL DIAGNOSTIC.**

For the cuboid surface itself, García-Fritz Theorem 6.48 gives for a curve `C` with strict transform `C'` on the minimal resolution:

```text
deg pulled-back symmetric-differential line
 = -d + (E.C') + 2(2g-2),
E = sum_(48 nodes) E_i.
```

Therefore, unless the strict transform is one of the explicitly classified integral curves for the chosen symmetric differential,

```text
d <= M + 4g - 4,
M := E.C'.
```

This explains the 32-03 firewall exactly. In a unibranch/smooth-at-node situation, `M` is bounded by the finite node set and this gives a degree bound. For the multibranch population, `M` can grow with degree. The hostile balanced ray has

```text
g=1,
M=d=112l,
```

so the inequality is exactly saturated and gives no cutoff.

Thus the existing perfect-cuboid-specific differential inequality is not the missing finite-window theorem. It reduces the missing input to a strict improvement over the raw exceptional-contact term, or to an independent upper bound on `M` strong enough to beat `d`.

Source:
Natalia García-Fritz, *Curves of low genus on surfaces and applications to Diophantine problems* (2015), Theorem 6.48.

---

## Z12 — adaptive / higher-order symmetric differentials

**Result: SOFT-PARK / DISTINCT HIGHER-ORDER DIRECTION.**

Known order-two symmetric-differential methods already constrain low-genus curves on the cuboid surface. Bruin--Thomas--Várilly-Alvarado show that rational curves outside known exceptions must meet many singularities and genus-one curves at least two; later retained Stage32 work also isolates finite-node-support regimes.

However the current whole-population obstruction is multiplicity, not only support cardinality. A fixed finite-order form can become saturated at a supported node while arbitrarily many branches continue to land there. The hostile `000707` order-two replay already found the unique common regular line equal to the support-hyperplane architecture.

A genuinely new route would require one of:

```text
order m increasing with contact complexity,
or
a fixed high-order family whose local vanishing/contact charge grows strongly enough with branch multiplicity,
or
a cuboid-specific jet-differential theorem converting 48 A1 singularities into a strict coefficient improvement in Z11.
```

No such population-wide theorem is currently retained. Unlike Z1, the broader higher-order direction is not numerically disproved.

Disposition:

```text
tested fixed/order-two architecture = HARD
broader adaptive higher-order direction = SOFT-PARK
```

---

## Z13 — irregular product cover + Albanese-defective curve bound

**Result: HARD as a population-wide route; useful only for a bounded-lift-genus subpopulation.**

The fixed product cover has irregular surface

```text
Y = X(8) x X(8),
q(Y)=10,
K_Y^2 = 128.
```

Mendes Lopes--Pardini prove that on a minimal irregular surface of general type, curves of geometric genus `g <= q-2` satisfy

```text
K_Y.C <= K_Y^2,
```

with a related bound for `g=q-1`.

This would give a strong fixed bound if every low-genus cuboid carrier lifted to a curve of bounded genus on `Y`.

But quotient branching at the 48 A1 points makes the lifted normalization genus grow with the branch packet. The retained hostile product family has

```text
projection degree n=28l,
g(Z)=4n+1,
```

so `g(Z)` is unbounded with `l`.

Therefore low coarse genus downstairs does not place the lifted curve in the `g<=9` Albanese regime. The theorem can bound small-branch/small-lift-genus pieces, but cannot close the full multibranch population.

---

## Z14 — finite-node pigeonhole / forced branch collision

**Result: HARD generic; absorbed into the Z4 global-localization refinement.**

A tempting population argument is:

```text
only 48 box nodes
+ very large degree
=> many normalization branches over the same nodes
=> many pairwise collisions
=> quadratic delta
=> contradiction.
```

MB101/MB102 show exactly why this fails. At one A1 node, arbitrarily many minimal branches may have distinct exceptional landing parameters `lambda` on the exceptional `P^1`. Distinct landing points contribute no pairwise local delta on the resolution.

Hence finite support does not imply finite landing capacity, and raw pigeonhole counting cannot force quadratic local singularity charge.

A revival would require a new cuboid-specific theorem saying that allowed landing parameters/finite jets lie in a finite or sufficiently low-capacity subset. That is precisely the stronger global localization/collision input already preserved as Z4'.

---

## Z15 — complete-intersection / Castelnuovo-Halphen genus-degree bounds

**Result: HARD for the 32-03 receiver.**

The cuboid surface is a complete intersection of four quadrics in `P^6`, and there are strong projective genus-degree bounds for curves on complete-intersection surfaces or under flag conditions.

But these control the **arithmetic genus** or speciality/projective Hilbert data of the image curve. Stage32 fixes the **geometric genus of the normalization**:

```text
g in {0,1},
p_a(C) = g + Delta_total.
```

The multibranch receiver permits `Delta_total` to grow quadratically. The balanced hostile ray already has

```text
p_a = 1 + 168l^2 + 56l,
g = 1.
```

So large projective/arithmetic genus is not contradictory; it is exactly how a high-degree curve can keep normalization genus one.

Therefore generic complete-intersection genus bounds do not produce a finite window unless supplemented by a new theorem controlling the singularity defect `Delta_total`, which returns to Z4/Z11-type input.

---

## Round-3 portfolio update

```text
PROMISING:
  Z2  canonical-orbifold canonical-degree inequality

SOFT-PARK:
  Z3   strong effective-cone/fixed-component theorem
  Z4'  global singularity localization/collision theorem
  Z5'  packet-sensitive arithmetic product theorem
  Z12  adaptive/higher-order symmetric differentials

HARD / ABSORBED AS TESTED:
  Z1 Z4 Z5 Z6 Z7 Z8 Z9 Z10
  Z11 Z13 Z14 Z15
```

Important structural conclusion from Z11:

```text
existing cuboid-specific differential method already gives
d <= M + 4g - 4,
so the multibranch finite-window wall is precisely the growing
exceptional-contact/branch-complexity term M.
```

This is a diagnosis, not a closure theorem.

Next breadth batch:

```text
Z16-Z20
```

Do not deepen Z2 or Z12 before the planned breadth scan is complete.

## Firewalls

```text
finite_degree_window_proved=false
MB104_complete=false
R29_LG2_MB_discharged=false
finite_picard_enumeration_released=false
receiver_credit=false
effectivity_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
