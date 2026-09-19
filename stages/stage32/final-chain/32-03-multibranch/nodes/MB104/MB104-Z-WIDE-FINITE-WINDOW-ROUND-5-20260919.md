# Stage32 32-03 — Z-wide population finite-window scan, Round 5 (Z21-Z25) — 2026-09-19

Status: **USER-DIRECTED BREADTH SCAN / WHOLE R29-LG2-MB POPULATION / NO MATHEMATICAL CREDIT**

## Scope

Target remains the whole multibranch low-genus receiver

```text
R29-LG2-MB
g(normalization) in {0,1}
=> population-wide finite degree/intersection window.
```

Balanced `000707` is only a hostile test sector. Z2/Z12/W16-H are not deepened.

Before this round, archive-semantic replay was used to reject rediscoveries of the old W1 Bogomolov/Reider, W19 Wronskian/Pluecker, W26 equisingular-T-smoothness, and related W1-W31 mechanisms.

---

## Z21 — exceptional A1 root-lattice orthogonal projection + Hodge index

**Result: SOFT-PARK / PARTIAL POSITIVE WINDOW / structurally sharp on balanced 000707.**

Let `D` be the strict transform on the smooth minimal resolution `S`. Retain the MB101 quantities

```text
d = H.D,  H=K_S, H^2=16,
M_i = D.E_i,
M = sum_i M_i,
N = #{i : M_i>0},
E_i^2=-2, E_i.E_j=0 (i!=j), H.E_i=0.
```

Define the rational orthogonal projection away from the 48 A1 roots

```text
D# = D + (1/2) sum_i M_i E_i.
```

Then `D#.E_i=0`, `H.D#=d`, and exactly

```text
(D#)^2 = D^2 + (1/2) sum_i M_i^2.
```

Hodge index against `H` gives the population-wide inequality

```text
D^2 + (1/2) sum_i M_i^2 <= d^2/16.
```

Cauchy on the `N` met nodes gives the weaker scalar form

```text
D^2 + M^2/(2N) <= d^2/16.                 (Z21)
```

Combine with Z11, `d <= M + 4g - 4`, and MB102 adjunction.

For `g=1`,

```text
M >= d,
D^2 >= -d,
-d + d^2/(2N) <= d^2/16.
```

Hence, whenever `N<8`,

```text
d <= 16N/(8-N).
```

In particular `N=7 => d<=112`; smaller support gives a stronger bound.

For `g=0`,

```text
M >= d+4,
D^2 >= -d-2,
-d-2 + (d+4)^2/(2N) <= d^2/16.
```

This is impossible for positive `d` when `N<=4`, and gives

```text
N=5: d <= 6
N=6: d <= 17
N=7: d <= 49.
```

Thus Z21 is a genuine population subwindow theorem: any unbounded low-genus sequence must meet at least eight box nodes.

Hostile balanced test is exactly sharp. There

```text
N=14,
M=d=112l,
D^2=336l^2,
M_i=8l on each of the 14 met nodes,
D#=7lH.
```

Therefore both Cauchy and Hodge are equalities:

```text
D^2 + M^2/(2N)
=336l^2+448l^2
=784l^2
=d^2/16.
```

So Z21 cannot by itself cut the balanced tail. Any improvement must break this equality geometry, for example by proving non-uniform contact, an additional Picard direction, or a strict inequality from packet geometry.

Disposition:

```text
full population closure = NO
new finite subwindow N<=7 = YES
classification = SOFT-PARK / PARTIAL-POSITIVE
```

---

## Z22 — Serrano low-gonality pencil extension after embedded resolution

**Result: HARD.**

A normalization of genus zero or one has gonality at most two. Serrano's extension theorem is therefore a natural candidate: for a smooth curve `C'` on a smooth surface, a degree-`q` pencil extends to the surface when `(C')^2` is sufficiently large (in particular `(C')^2>(q+1)^2`).

For a singular carrier `D subset S`, resolve its curve singularities by successive blowups and let `D_tilde` be the smooth strict transform, which is the normalization. If the multiplicities at all proper and infinitely-near centers are `m_p`, then the plane-curve delta formula and adjunction give

```text
2 Delta = sum_p m_p(m_p-1),
D^2 + d = 2g-2 + 2Delta,
D_tilde^2 = D^2 - sum_p m_p^2
          = 2g-2-d-sum_p m_p.
```

Hence for every positive-degree `g<=1` carrier,

```text
D_tilde^2 < 0.
```

The smooth curve to which Serrano applies therefore lies on the wrong side of the required positive-self-intersection hypothesis. Moreover the resolving surface depends on the carrier, so this does not convert into a fixed-surface negative-curve finiteness theorem.

Reference shape: Fernando Serrano, *Extension of Morphisms Defined on a Divisor*, Math. Ann. 277 (1987), 395–414.

Disposition: `HARD`.

---

## Z23 — Lefschetz/Nori fundamental-group generation from a high-degree carrier

**Result: HARD population-wide.**

A possible topological route is to force a sufficiently positive curve to carry/generate the fundamental group of the ambient surface and then use the normalization genus `0/1`.

The shallow gate fails twice.

First, the dangerous balanced classes are not in the standard smooth/general ample Lefschetz regime: retained zero-pairing elliptic quartics satisfy `D_l.Q=0`.

Second, and more decisively, the topological fundamental group of a singular integral curve is not controlled by the genus of its normalization. Gluing several normalization points to one singular image point creates graph loops. At the retained MB101 interface, a node with `r_i` distinct normalization branches can contribute `r_i-1` independent graph cycles without increasing normalization genus. Thus the aggregate branch-excess capacity

```text
R-N = sum_i (r_i-1)
```

may grow with degree. In the balanced hostile packet,

```text
R=d=112l, N=14,
R-N=112l-14.
```

Therefore even a hypothetical ambient-`pi_1` surjectivity statement for the singular image would not turn `g(normalization)<=1` into a degree bound.

Disposition: `HARD`.

---

## Z24 — finite discriminant-form / Picard congruence obstruction

**Result: HARD standalone; possible finite packet filter only.**

The cuboid resolution has a large explicit Picard lattice, so one can ask whether its finite discriminant group, divisibility, or quadratic-form congruences force only finitely many low-genus carrier classes.

A finite congruence obstruction cannot give the required large-degree cutoff on its own. The balanced hostile sector already contains the integral ray

```text
D_l = l D_1,  l>=1.
```

Any condition taking values in a fixed finite quotient of the lattice is periodic in `l`; after multiplying by the exponent of that finite quotient, the same residue class recurs on infinitely many `l`. Such data may exclude residue classes or packets, but cannot bound degree along an integral ray.

To become a finite-window theorem, the lattice route needs an archimedean positivity/effectivity statement rather than a finite discriminant congruence. That returns to Z3 or to the new Z21 Hodge/root-lattice inequality.

Disposition: `HARD standalone / FILTER-ONLY`.

---

## Z25 — local log-canonical threshold / alpha-invariant singularity severity

**Result: HARD standalone; absorbed by Z4' if strengthened by packet localization.**

This route asks whether the quadratic genus defect forced by a high-degree genus-zero/one image must create a sufficiently severe singularity, detectable by a small local log-canonical threshold, so that a global alpha/lct inequality yields a cutoff.

The cheap kill-test is the distinction between **severity** and **count**. Ordinary nodes on a smooth surface have local log-canonical threshold one, yet each contributes delta one. A growing collection of ordinary nodes can therefore make

```text
Delta_total = Theta(d^2)
```

while the minimum local lct remains equal to one. This is exactly compatible with the retained Stage32 ordinary-node witness architecture used to show that aggregate BMY/log inequalities do not localize the defect.

Thus a bound depending only on the worst local lct/multiplicity cannot control the aggregate defect. A successful refinement would need a theorem forcing the cuboid packet to concentrate many branches/jets into fewer singularities, which is the already-retained Z4' global localization/collision direction.

Reference shape: Aprodu–Naie, *Log-canonical threshold for curves on a smooth surface*, arXiv:0707.0783.

Disposition: `HARD standalone / ABSORBED BY Z4' FOR ANY LOCALIZATION REFINEMENT`.

---

## Round-5 portfolio update

```text
PROMISING:
  Z2   canonical-orbifold canonical-degree inequality

SOFT-PARK:
  Z3   strong effective-cone/fixed-component theorem
  Z4'  global singularity localization/collision theorem
  Z5'  packet-sensitive arithmetic product theorem
  Z12  adaptive/higher-order symmetric differentials
  Z21  exceptional-root-lattice Hodge inequality
       (genuine N<=7 finite subwindow; balanced equality wall)

CONDITIONAL-ONLY:
  Z16' Vojta bounded-gonality canonical-degree theorem shape

HARD / ABSORBED AS TESTED:
  Z1 Z4-Z11 Z13-Z20
  Z22 Z23 Z24 Z25
```

## New diagnosis after Z21

Z21 adds a fifth, independent view of the multibranch wall:

```text
unbounded low-genus carriers => N>=8,
and the most hostile balanced packet is an exact Hodge/Cauchy equality case.
```

For balanced `000707`, the equality `D#=7lH` shows that generic intersection theory has no slack at all after orthogonally removing the A1 root directions. Therefore a future full-population argument must exploit information not present in the scalar tuple `(d,D^2,M,N)`: landing distribution, packet arithmetic, higher jets/differentials, or orbifold/canonical structure.

Next breadth batch:

```text
Z26-Z30
```

Do not deepen Z2/Z12/Z21 or return to W16-H before the final breadth round is complete.

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
