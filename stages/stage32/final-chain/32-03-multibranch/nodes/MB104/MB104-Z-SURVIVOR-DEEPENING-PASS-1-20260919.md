# Stage32 32-03 — non-HARD Z survivor deepening, pass 1 — 2026-09-19

Status: **USER-DIRECTED DEEPENING / NO MATHEMATICAL CREDIT**

## Scope

Revisit every retained non-HARD Z route after the Z1-Z30 breadth scan:

- Z2 canonical-orbifold canonical-degree,
- Z3 strong stable-base/effective-cone,
- Z4' global singularity localization/collision,
- Z5' packet-sensitive arithmetic,
- Z12 adaptive/higher-order symmetric differentials,
- Z21 exceptional-root-lattice Hodge,
- Z16' conditional bounded-gonality canonical-degree blueprint.

The purpose is not to relabel the portfolio. It is to identify exact theorem gaps or executable next gates toward a population-wide finite degree/intersection window for R29-LG2-MB.

Balanced 000707 remains a hostile test only.

---

## 1. Z2 + Z16' — source correction and exact ambient-singularity gap

### 1.1 Correction to the earlier Z16 shallow description

Miyaoka, *The Orbibundle Miyaoka–Yau–Sakai Inequality and an Effective Bogomolov–McQuillan Theorem*, PRIMS 44 (2008), Theorem 1.1, is stated for an **irreducible curve of geometric genus g** on a smooth minimal projective surface of general type. The curve is not required to be nonsingular for Theorem 1.1.

The smoothness of the curve enters a later asymptotic estimate, not the main uniform canonical-degree theorem.

Thus the old shallow wording "smooth-curve theorem does not apply because the carrier is multibranch/singular" was too strong and is superseded by this note.

The actual obstruction is the **ambient surface**:

```
smooth resolution S:
K_S^2 = 16,
c2(S) = 80,
K_S^2 > c2(S) is false.
```

So Miyaoka 2008 does not give the required bound on S.

Langer, *Logarithmic orbifold Euler numbers of surfaces with applications*, PLMS 86 (2003), Theorem 10.1, likewise gives effective canonical-degree bounds on a smooth surface when either `c1^2>2c2` for arbitrary curve singularities or `c1^2>c2` under an ordinary-singularity hypothesis. Neither numerical condition holds on S.

### 1.2 Singular ambient BMY exists, but the lc coefficient collapses with contact mass

Langer 2003 Theorem 0.1 does apply to a normal projective surface with boundary:

```
(X, alpha C) log canonical,
K_X + alpha C Q-effective
=> (K_X + alpha C)^2 <= 3 e_orb(X, alpha C).
```

This is genuinely relevant because the canonical cuboid surface X has A1 quotient singularities.

However, the MB101 A1 branch adapter gives an exact obstruction to using a fixed positive alpha on an unbounded multibranch sequence.

At one A1 point, use the local uniformizing double cover

```
C^2_(p,q) -> {xz=y^2},
x=p^2, y=pq, z=q^2.
```

For an MB101 branch with invariant exponents (A,B), A+B even, put m=min(A,B).

- if A,B are odd, the lifted irreducible branch has plane multiplicity m;
- if A,B are even, the pullback splits into two conjugate branches of multiplicity m/2 each.

Therefore the total multiplicity of the pulled-back divisor over node i is exactly

```
mult_0(pi^* C) = sum_j m_ij = M_i.
```

If `(X,alpha C)` is log canonical, its quasi-etale local pullback is log canonical. The first blow-up on the smooth cover gives the necessary condition

```
alpha M_i <= 2.
```

Hence

```
alpha <= 2/max_i M_i.
```

From Z11,

```
g=1: M>=d,
g=0: M>=d+4,
```

and there are only 48 box nodes. Thus on any unbounded sequence,

```
max_i M_i >= M/48,
alpha <= 96/M = O(1/d).
```

Consequently a Langer log-pair application necessarily uses `alpha=O(1/d)`. Since

```
C_X^2 = (D#)^2 <= d^2/16
```

by Hodge, both `alpha d` and `alpha^2 C_X^2` remain O(1). The left side `(K_X+alpha C)^2` therefore has no term growing with d that could force a uniform degree cutoff.

**Conclusion for Z2-A1:** the existing singular-pair BMY technology does not by itself close 32-03; the lc coefficient is forced to collapse with the exceptional contact mass.

The exact remaining Z2 theorem gap is now much narrower:

> a singular-ambient analogue of Miyaoka's orbibundle/G-nef argument that handles arbitrary curve contact through A1 points without requiring the pair `(X,alpha C)` to remain lc at a fixed alpha, and whose Chern term is the quotient/orbifold Chern term rather than `c2(S)=80`.

The klt/Q-Chern Miyaoka-Yau theorem of Greb-Kebekus-Peternell-Taji controls the ambient Q-Chern classes, but does not itself supply this curve-degree inequality.

No established theorem matching all of these hypotheses was located in this pass.

### Z2 / Z16' disposition

```
Z2 = OPEN, theorem gap sharply identified
Z16' = CONDITIONAL BLUEPRINT only
Miyaoka-2008 curve-singularity objection = RETRACTED
smooth-ambient Chern-number obstruction = RETAINED
Langer normal-pair fixed-alpha route = BLOCKED by alpha M_i <= 2
```

---

## 2. Z21 — strengthen the real partial theorem at the N=8 boundary

Retain

```
D^2 + (1/2) sum_i M_i^2 <= d^2/16.
```

For N active nodes write

```
V_N = sum_i (M_i - M/N)^2 >= 0,
sum_i M_i^2 = M^2/N + V_N.
```

The previous pass proved a finite window for N<=7. At the first unbounded boundary N=8 one can say substantially more.

### g=1, N=8

Use `M>=d` and `D^2>=-d`. Then

```
M^2 - d^2 + 8V_8 <= 16d.
```

Write `u=M-d>=0`:

```
2du + u^2 + 8V_8 <= 16d.          (Z21-8E)
```

In particular:

```
u>=8 is impossible,
so M-d <= 7.
```

Moreover

```
V_8 <= 2d
```

when u=0, with a smaller allowance as u grows.

Thus any unbounded genus-one N=8 sequence is forced into a very narrow near-equality tube:

```
d <= M <= d+7,
sum_i (M_i-M/8)^2 = O(d).
```

The node masses therefore become asymptotically equal up to O(sqrt(d)) deviations rather than O(d) deviations.

### g=0, N=8

Use `M>=d+4` and `D^2>=-d-2`. Write

```
u = M-(d+4) >= 0.
```

Then

```
2(u-4)d + (u+4)^2 + 8V_8 <= 32.   (Z21-8R)
```

Hence

```
u>=4 is impossible,
so d+4 <= M <= d+7
```

for every positive-degree candidate satisfying the gate.

This is a genuine strengthening of the retained Z21 partial window: N=8 is not finite, but any unbounded tail is asymptotically forced toward uniform exceptional contact.

### Z21 disposition

```
N<=7 = finite degree window already proved
N=8 = new near-equality tube
N>=9 = still open; quadratic Hodge slack remains
```

No receiver credit is claimed.

---

## 3. Z4' — turn "localization" into a quantitative target

Z4' only becomes useful if it produces a **quadratic** lower bound on delta/contact concentration. Pure branch counts remain insufficient because MB101 permits distinct landing parameters.

The Z21 inequality and adjunction give, for g=1,

```
Delta_total
 <= d/2 + d^2/32 - (1/4)sum_i M_i^2.    (Z4-HODGE-UPPER)
```

Therefore any packet theorem forcing

```
Delta_total
 >= d/2 + d^2/32 - (1/4)sum_i M_i^2 + epsilon*d^2
```

for some fixed epsilon>0 on all sufficiently large survivors would immediately contradict Z21.

This is the correct strength target. A merely linear collision bound cannot close the N>8 tail.

For the minimal-branch sector `r_i=M_i`, if the branches at node i were forced into at most `q_i` resolved landing points, ordinary pairwise intersection alone would give

```
Delta_i_exc >= (r_i^2/q_i - r_i)/2.
```

This exposes an exact adapter target: a uniform/sublinear bound on effective landing capacity would convert packet data into the required quadratic delta. MB101 currently allows `q_i=r_i`, so no such result is available yet.

### Z4' disposition

```
OPEN only as a quadratic localization theorem
linear localization/counting = insufficient
best composition target = Z21 Hodge upper bound
```

---

## 4. Z12 — higher-order differential route is now computational, not merely qualitative

The order-two active-support computation remains exhausted: the 13-dimensional BTVA space has stacked principal-part rank 12 on the active 14 nodes and its only common regular line is the retained support-hyperplane form.

New literature does improve the *machinery* for going beyond order two:

- Bruin-Ilten-Xu, *Local Euler characteristics of A_n-singularities and their application to hyperbolicity* (2025), gives explicit quasi-polynomial local Euler characteristics for symmetric powers at A_n singularities and uses explicit symmetric differentials to exclude genus 0/1 curves on concrete highly singular surfaces.
- Asega-De Oliveira-Weiss, *Surface quotient singularities and bigness of the cotangent bundle*, Parts I-II (2025), gives exact A_n local asymptotics and extension results for symmetric differentials on resolutions.

This does **not** automatically prove bigness or a degree bound for the cuboid surface. The retained CMS/bulk asymptotic gate is not positive for the cuboid A1 configuration, so simply taking m large and invoking generic asymptotic bigness is not justified.

But it makes the next Z12 test finite and explicit rather than speculative:

```
Z12-C1:
  construct/order the product-generated order-4 space from Sym^2(V_13);
  impose exact A1 extension/principal-part conditions on the active support;
  compute the common regular subspace;
  quotient out forms generated by the known order-2 support-hyperplane line;
  test whether any genuinely new regular order-4 direction survives.
```

A positive result would still need a curvewise vanishing/non-tangency argument. A zero result would close the cheapest higher-order product-generated branch, but not all primitive higher-order forms.

### Z12 disposition

```
OPEN and executable
generic asymptotic bigness = not established
next exact gate = order-4 active-support computation
```

---

## 5. Z3 — stable-base/effective-cone route remains weak after the root-wall audit

The W4 third-depth computation already checked the available primitive coordinate quotient rays against the effective (-2)-root walls and found no negative wall.

The balanced numerical class also has

```
D_l^2 = 336l^2 > 0,
D_l.E_i = 8l on the 14 active exceptional curves,
D_l.E_i = 0 on the other exceptional curves.
```

Thus no known negative intersection forces a fixed component on this ray.

A useful Z3 theorem would have to go beyond the tested root walls and prove that every sufficiently large low-genus irreducible representative acquires a fixed component from the **full** effective/Mori cone. No such theorem specific enough to the cuboid surface was found.

Concrete next test, if Z3 is revisited:

```
determine nefness/semiampleness of the primitive balanced class D_1
against a complete certified cone, not only the seven quotient root systems.
```

If D_1 is nef and the base-point-free hypotheses are met, this would work *against* Z3 in the balanced sector.

### Z3 disposition

```
RESERVE ONLY
no new closure mechanism found
do not spend next deep pass here before Z21/Z12
```

---

## 6. Z5' — arithmeticity gives many correspondences; only a marked-packet stabilizer can save the route

The prior H5/H6 conclusions survive deeper literature search:

- arithmetic Fuchsian curves have a large commensurability/self-correspondence structure;
- Hecke-type correspondences occur in unbounded families;
- generic equal-degree etale correspondence rigidity therefore cannot bound the degree.

The only viable refinement is to prove that the cuboid packet forces the correspondence to preserve a **fixed finite marked divisor / fixed lift datum**, reducing from the full arithmetic commensurator to a much smaller stabilizer.

The current exact e=2 passport does not provide that adapter. H5 already records that the branch data do not canonically assign all branches to a single fixed product lift, and H6 shows the Nielsen/passport population grows with l.

Concrete next test:

```
Z5'-A:
  extract the retained residual/deck data at the eight fixed branch values;
  ask whether it forces preservation of a fixed marked divisor on C8
  (not merely the aggregate branch passport).
```

Without that implication, further generic arithmetic-correspondence theory is unlikely to help.

### Z5' disposition

```
RESERVE / ADAPTER-DEPENDENT
generic arithmetic theorem route remains negative
```

---

## 7. Post-pass comparison

This pass does not declare a winner. It changes what is actually executable:

```
Z21:
  strongest proved progress;
  N<=7 finite, and now N=8 forced into a near-equality tube.

Z2:
  potentially strongest theorem shape;
  exact missing theorem isolated;
  existing Langer singular-pair route loses fixed alpha because alpha M_i<=2.

Z12:
  concrete finite next computation exists at order 4 using modern A_n extension machinery.

Z4':
  useful only if it yields quadratic localization;
  now has an explicit coefficient target from Z21.

Z5':
  requires a new marked-packet adapter before more arithmetic theory.

Z3:
  reserve; no new mechanism.

Z16':
  conditional blueprint; Miyaoka source correction recorded, but no unconditional ambient-singular theorem.
```

Recommended next executable order:

```
1. Z21/Z4'-B1:
   exploit the new N=8 near-equality tube and search for a cuboid-specific
   contact/landing constraint that creates quadratic variance or delta.

2. Z12-C1:
   exact order-4 active-support regularity computation.

3. Z2-A2:
   only if a source supplies the missing singular-ambient Miyaoka orbibundle
   theorem without the fixed-lc-alpha collapse.
```

Do not return automatically to W16-H.

---

## Firewalls

```
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
