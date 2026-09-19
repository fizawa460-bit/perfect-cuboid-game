# Stage32 32-03 — revived-Z deepening pass 2 — 2026-09-19

Status: **USER-DIRECTED DEEPENING / PRE-AUDIT / NO MATHEMATICAL CREDIT**

## Scope

Deepen only routes whose previous HARD/conditional diagnosis was materially changed by the post-Z30 work:

- Z16: Miyaoka canonical-degree inequality on the smooth resolution;
- Z6 as a newly revived **auxiliary** product-cover branch-count inequality;
- Z14: fixed A1 landing directions / collision lower bounds;
- Z25: local lct as an equality/collision detector;
- Z7: Seshadri route recheck after contact mass became linear in degree;
- Z9/Z30: Miyaoka aggregate/orbifold variants rechecked through the fixed product cover and Z2.

This pass is deliberately not a Z1-Z30 rescan.

Retained notation:

```
S = smooth minimal resolution of the box surface,
H=K_S, H^2=16, c2(S)=80,
D = strict transform of an integral nonexceptional carrier,
d=H.D>0,
g=geometric genus of normalization in {0,1},
M_i=D.E_i, M=sum M_i,
N=#{i:M_i>0}.
```

From Z21:

```
D^2 + (1/2) sum M_i^2 <= d^2/16.             (H)
```

From the retained multibranch differential/product interfaces:

```
g=1: M>=d,
g=0: M>=d+4.
```

The main new result of this pass is that Z16 and Z21 compose into a stronger exact partial finite-window theorem.

---

## 1. Z16 genuinely revives when composed with Z21

### Source correction

Miyaoka, *The Orbibundle Miyaoka-Yau-Sakai Inequality and an Effective Bogomolov-McQuillan Theorem*, PRIMS 44 (2008), Theorem 1.3, applies to an irreducible curve of **geometric genus** on a smooth surface of nonnegative Kodaira dimension. The curve need not itself be nonsingular for Theorem 1.3(i)/(ii).

The two source inequalities needed here are:

```
(i)
alpha^2/2 * (D^2+3d-6g+6)
 -2 alpha*(d-3g+3)
 +(3c2(S)-K_S^2) >=0,

(ii), when D is not P1 and d>3g-3:
2(d-3g+3)^2
 <= (3c2(S)-K_S^2)(D^2+3d-6g+6).
```

For the cuboid resolution,

```
3c2(S)-K_S^2 = 240-16 = 224.
```

The previously noted failure of Miyaoka Theorem 1.1 remains true because `K^2>c2` fails, but Theorem 1.3 still supplies useful lower bounds on `D^2`. This is the point missed in the earlier HARD classification.

### 1.1 Genus one

Since `g=1`, `D` is not rational and `d>0=3g-3`. Theorem 1.3(ii) gives

```
2d^2 <=224(D^2+3d),
D^2 >= d^2/112 - 3d.                         (M1)
```

Combine (M1) with (H):

```
sum M_i^2
 <= 2[d^2/16-(d^2/112-3d)]
 = 3d(d+56)/28.                              (M1H)
```

Cauchy and `M>=d` give

```
d^2/N <= sum M_i^2 <=3d(d+56)/28.
```

For `d>0` and `N<28/3`,

```
d <= 168N/(28-3N).                           (G1-N)
```

Therefore:

```
N=8 => d<=336,
N=9 => d<=1512.
```

For `N<=7`, the old Z21 bounds remain stronger where applicable; in particular `N=7 => d<=112`.

Hence every **unbounded** genus-one sequence must now have

```
N>=10.
```

### 1.2 Genus zero

If `Delta_total=0`, then the integral rational curve `D` is nonsingular. Miyaoka Remark A gives directly

```
d <= 3c2(S)-K_S^2-5 = 219.
```

Now assume `Delta_total>=1`. Adjunction gives `D^2>=-d`, so

```
A := D^2+3d+6 >=2d+6.
```

In Theorem 1.3(i), the minimizing value

```
alpha_* = 2(d+3)/A
```

lies in `[0,1]`. Evaluating the quadratic at its minimum gives

```
D^2 >= (d+3)^2/112 -3d-6.                   (M0)
```

Combine with (H):

```
sum M_i^2
 <= 3(2d^2+110d+221)/56.                    (M0H)
```

Using `M>=d+4` and Cauchy:

```
(d+4)^2/N
 <=3(2d^2+110d+221)/56.
```

This yields the exact finite bounds

```
N=8:
d <= 137+2 sqrt(4830) <276,
hence integer d<=275.

N=9:
d <= (1261+3 sqrt(177807))/2 <1264,
hence integer d<=1263.
```

Together with the existing stronger `N<=7` Z21 bounds and the smooth-rational `d<=219` case:

```
every unbounded genus-zero sequence also has N>=10.
```

### Z16/Z21 conclusion

This is a genuine upgrade:

```
OLD:
unbounded low-genus sequence => N>=8.

NEW, PRE-AUDIT:
unbounded low-genus sequence => N>=10.
```

Z16 is therefore no longer merely a conjectural blueprint. The bounded-gonality/Vojta form remains conjectural, but **Miyaoka 1.3 itself is an unconditional auxiliary theorem that materially strengthens Z21**.

No theorem/receiver credit is promoted by this pre-audit research note.

---

## 2. Z6 revives as an auxiliary branch-count theorem

The generic product-hyperbolicity route remains unable to close the balanced tail, but its exact product-cover geometry carries more information than the scalar inequality used in the old HARD test.

Let

```
O = number of normalization branches over the 48 box nodes
    whose exceptional contact multiplicity m is odd.
```

The resolved Beauville double cover is branched along the exceptional divisor. Pulling it back to the normalization `N_D` of the carrier gives a double cover ramified exactly at these `O` odd-contact branches.

If `O=0`, every connected component of this pullback has genus at most one for `g<=1`; further etale pullback to the fixed product cover also has genus at most one. A nonconstant map from such a curve to `X(8)` of genus five is impossible by Riemann-Hurwitz, while positive canonical degree forces at least one product projection to be nonconstant. Therefore `O>0`, and the double cover is connected.

Let `q' in {1,2,4}` be the degree of a connected component after the etale V4 product-cover pullback. If `Z` is its normalization, then

```
2g(Z)-2 = q'(4g-4+O).
```

Let `n1,n2` be the two projection degrees to `X(8)`, which has genus five. Projection formula and the canonical product divisor give

```
n1+n2 = q'd/4.
```

Riemann-Hurwitz for each nonconstant projection gives

```
2g(Z)-2 >=8n_i.
```

Using `max(n1,n2)>=(n1+n2)/2`:

```
q'(4g-4+O)
 >= 8 max(n1,n2)
 >= 4(n1+n2)
 = q'd.
```

Hence the population-wide necessary condition

```
O >= d-4g+4.                                 (Z6-AUX)
```

So:

```
g=1: O>=d,
g=0: O>=d+4.
```

This has the same scalar consequence `M>=d` / `M>=d+4`, but is structurally stronger because `O` counts **distinct normalization branches**, not contact mass.

Disposition:

```
Z6 standalone closure = still HARD/equality-saturated,
Z6 as branch-count auxiliary = REVIVED / PRE-AUDIT.
```

---

## 3. Z14 revives quantitatively: non-diagonal branches must collide at two fixed landings

The A1 branch adapter contains more information than the earlier "lambda can vary" diagnosis.

For a branch with exponents `A,B`:

```
A<B -> fixed distinguished landing on E_i,
A>B -> the other fixed distinguished landing on E_i,
A=B -> free nonzero lambda in C*.
```

The two fixed landings are exactly the two Satake-boundary intersection directions on that exceptional `P1`.

Let at node `i`

```
t_i^- = number of A<B branches,
t_i^+ = number of A>B branches,
T = sum_i(t_i^-+t_i^+).
```

Distinct branches landing at the same resolved point have pairwise intersection multiplicity at least one. Therefore

```
Delta_exc
 >= sum_i [binom(t_i^-,2)+binom(t_i^+,2)].
```

There are `2N` fixed landing bins. Cauchy gives the universal lower bound

```
Delta_exc >= T^2/(4N)-T/2.                  (Z14-COLL)
```

This is the first population-wide quantitative use of the old Z14 idea that survives the free-lambda wall.

It still cannot control the diagonal `A=B` branches, which may choose arbitrary nonzero `lambda`. Thus Z14 is revived as a helper, not as a standalone closure theorem.

---

## 4. N=10 is now reduced to a large FSM-minimal free-lambda sector

The first possible unbounded support size is now `N=10`. Combine Z16/Z21, Z6-AUX and Z14-COLL.

### 4.1 Genus one, N=10

From (M1H):

```
M^2 <=10 sum M_i^2
     <=15 d(d+56)/14.
```

Since `R>=O>=d`, the number `S1` of contact-one branches satisfies

```
S1 >=2R-M
   >=2d-sqrt(15d(d+56)/14).                 (S1-1)
```

Adjunction plus Hodge and `M>=d` give

```
Delta_total <= d^2/160+d/2.
```

Using Z14-COLL with `N=10`:

```
T <=10 + (1/2)sqrt(d^2+80d+400).            (T1)
```

Every contact-one branch not counted by `T` has `A=B=1`, i.e. it is the unique FSM-minimal local type. Hence the number `F` of FSM-minimal `(1,1)` branches obeys

```
F >= 2d
     -sqrt(15d(d+56)/14)
     -10-(1/2)sqrt(d^2+80d+400).             (F1)
```

The right side is positive from `d>=117`, and asymptotically

```
F/d >= 3/2-sqrt(15/14)+o(1)
     = 0.4649016609...+o(1).
```

### 4.2 Genus zero, N=10

For an unbounded tail the `Delta=0` case is already bounded, so use (M0H):

```
M^2 <=15(2d^2+110d+221)/28.
```

Z6-AUX gives `R>=O>=d+4`, hence

```
S1 >=2(d+4)-sqrt(15(2d^2+110d+221)/28).     (S1-0)
```

Hodge/adjunction gives

```
Delta_total <= d^2/160+3d/10+3/5.
```

Thus

```
T <=10+(1/2)sqrt(d^2+48d+496).              (T0)
```

and the FSM-minimal count satisfies

```
F >=2(d+4)
    -sqrt(15(2d^2+110d+221)/28)
    -10-(1/2)sqrt(d^2+48d+496).              (F0)
```

The right side is positive from `d>=85` and has the same leading coefficient

```
3/2-sqrt(15/14)=0.4649016609...
```

relative to `d`.

### N=10 diagnosis

Therefore an unbounded `N=10` sequence cannot be an arbitrary multibranch configuration. It must contain linearly many FSM-minimal branches

```
(A,B)=(1,1), m=1, lambda in C*,
```

whose landing parameters avoid the two fixed boundary directions.

This is a much narrower obstruction than the old generic "lambda is free" wall.

The retained residual inertia acts

```
lambda -> -lambda,
```

but the existing source-locked tangent preflight already proves that a finite subset of `C*` can avoid opposite pairs. Therefore involution+pigeonhole alone still does not close N=10.

The next genuinely missing datum is now precise:

> a global member-level restriction on the set of free landing values/first jets for these linearly many FSM-minimal branches.

---

## 5. Z25 survives only as an equality/collision detector

On the A1 uniformizing cover, an FSM-minimal branch `(1,1)` lifts to a smooth line through the origin with slope determined by `lambda`.

If several such branches have distinct `lambda`, they form an ordinary multiple point. For an ordinary reduced r-fold point the lct is controlled by the first blowup at scale `2/r`; this is exactly the same scale as the retained necessary condition

```
alpha M_i <=2.
```

Therefore Z25 does not gain anything in the generic distinct-`lambda` regime.

It becomes useful only if the N=10 landing problem forces:

- repeated tangent directions,
- higher-order jet coincidence,
- or concentration stronger than an ordinary multiple point.

Such a result lowers the local threshold below the ordinary `2/M_i` scale and could then feed a stronger Langer/log-BMY inequality.

Disposition:

```
Z25 standalone = still HARD,
Z25 after a Z14/landing collision theorem = REVIVED HELPER.
```

---

## 6. Z7 recheck: not actually revived on the smooth resolution

The apparent reason to revisit Z7 was that contact mass is now known to be linear in degree.

But the landing points all lie on exceptional `(-2)` curves `E_i`, and

```
K_S.E_i=0.
```

For a big and nef canonical divisor on a minimal surface of general type, the canonical Seshadri constant at a point lying on a `(-2)` curve is zero (Bauer-Szemberg, *Seshadri constants on surfaces of general type*).

Thus the canonical Seshadri constant gives no positive local price at the exact points where the multibranch contact lives.

Passing to the singular canonical model removes the exceptional curve but returns to quotient-local positivity and does not presently improve on the exact Z21 root-lattice/Hodge control.

Disposition:

```
Z7 = NOT REVIVED after deep recheck.
```

---

## 7. Z9/Z30 recheck: useful input, but no independent route

Miyaoka 2009 Proposition B gives strong aggregate rational/elliptic-curve bounds on a **smooth canonically embedded** surface when the Chern ratio is favorable. The smooth resolution has

```
sigma=c2/K^2=5,
```

so it does not provide an all-degree low-genus cutoff there.

The fixed product cover `X(8)xX(8)` has favorable Chern ratio `1/2`, but a low-genus multibranch carrier downstairs lifts to a high-genus curve upstairs. Thus the elliptic/rational aggregate theorem does not apply to the lifted curve as a low-genus curve.

The lift does have bounded degree over the downstairs normalization, hence bounded gonality, but the corresponding general bounded-gonality canonical-degree estimate is the Vojta-shaped conjectural direction described by Autissier-Chambert-Loir-Gasbarri, not an available theorem for this noncompact-modular-compactification geometry.

Therefore:

```
Z9/Z30 independent revival = NO,
their useful orbifold/Chern viewpoint remains absorbed into Z2/Z16.
```

---

## 8. Updated revived-Z portfolio

After this deeper pass:

```
ACTUAL NEW PROVED-SHAPE PROGRESS, PRE-AUDIT:
  Z16 + Z21
  -> unbounded low-genus sequence must have N>=10.

NEW AUXILIARY REENTRY, PRE-AUDIT:
  Z6
  -> O >= d-4g+4 distinct odd-contact branches.

REVIVED COMPOSITION TOOL:
  Z14
  -> non-diagonal branches incur Delta_exc >= T^2/(4N)-T/2.

N=10 STRUCTURAL REDUCTION:
  linearly many FSM-minimal (1,1) free-lambda branches are forced.

CONDITIONAL HELPER:
  Z25
  -> useful only if landing/tangent collision is first forced.

RECHECKED AND RETURNED TO HARD:
  Z7.

ABSORBED / NO INDEPENDENT REVIVAL:
  Z9, Z30.
```

The research frontier is no longer "try random orbifold theorem." It is now:

```
N>=10 only,
and at N=10 an unbounded tail must carry a linear population
of minimal free-lambda branches.
```

The next exact attack should target the allowed `lambda`/first-jet set of an actual global cuboid carrier, not raw node counts.

---

## Firewalls

```
revived_z_pass2_pre_audit=true
finite_degree_window_proved_population_wide=false
N_le_9_partial_window_pre_audit=true
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
