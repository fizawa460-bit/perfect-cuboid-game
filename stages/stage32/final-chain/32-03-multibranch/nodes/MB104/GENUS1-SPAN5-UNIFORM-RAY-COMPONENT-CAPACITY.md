# Stage32 MB104 genus-one span-five uniform-ray component capacity

Status: **RETAINED FIXED-COMPONENT OBSTRUCTION FOR INCIDENCE 24/20/19 AND ONE INCIDENCE-14 ORBIT / INCIDENCE-16 BALANCED SURVIVORS ISOLATED / SUPPORT-SPAN 5 STILL OPEN / NO DOWNSTREAM CREDIT**

This checkpoint repairs the support-span semantics and uses retained support-hyperplane section components only through exact Picard intersection pairings.

## Scope

The unknown genus-one carrier need not lie in the support hyperplane `H=P^5`. The box-node support `Sigma` merely spans `H`. Section components of `S intersect H` are therefore test curves, not candidate carrier components.

The target is the displayed infinite Picard ray

```text
D_l = 7l H - 4l sum_{i in Sigma} E_i,
l>=1,
|Sigma|=14,
d=112l.
```

## Pairing rule

For a reduced section component `Q`, let

```text
e=H.Q,
n_Q=|Sigma intersect T_Q|.
```

If `Q` meets the corresponding exceptional curves once, then

```text
D_l.Q=l(7e-4n_Q).
```

Thus nonnegative pairing requires `n_Q<=floor(7e/4)`: capacity `3` for a conic and `7` for an elliptic quartic. A negative pairing forces `Q` as a fixed component of every effective member of `D_l`.

## Incidence 24

Eight smooth conics; every section node lies on exactly two conics. For `N>=14`, actual supported incidence is at least `28`, while eight nonnegative conic pairings have capacity only `24`. Hence a negative conic pairing is forced.

## Incidence 20

The exact section is four smooth conics plus two smooth elliptic quartics, and every section node lies on exactly two reduced components. Nonnegative capacity is

```text
4*3+2*7=26,
```

while `N>=14` gives at least `28` supported incidences. A negative section-component pairing is forced.

## Incidence 19

The reduced section support is four smooth conics and every section node lies on at least one. Nonnegative capacity is `4*3=12`, while any `N>=14` support contributes at least `14` conic incidences. A negative conic pairing is forced.

## Incidence 16, size-3 orbit

The section is four smooth elliptic quartics and every section node lies on exactly two quartics. For `N>=15`, total incidence is at least `30>4*7=28`, so a negative pairing is forced.

For `N=14`, nonnegative pairing is possible only in the balanced pattern

```text
(7,7,7,7).
```

Exact enumeration finds exactly `32` such 14-node supports; all retain rank six and span the same support hyperplane.

## Incidence 16, size-24 orbit

The reduced section support is two smooth elliptic quartics with disjoint 8-node supports, each generically doubled scheme-theoretically. For `N>=15`, one quartic contains at least 8 supported nodes and has negative pairing.

For `N=14`, both pairings are nonnegative only for the split `(7,7)`. Exactly `64` such supports occur, and all remain rank-six spanning supports.

## Incidence 14, orbit size 96

Representative support mask

```text
0000185aa566
```

and hyperplane

```text
-a2+a3+b2+b3=0.
```

On this hyperplane,

```text
q1-q3 = 2(a2-b3)(b2+b3).
```

On the branch `a2=b3`, the hyperplane relation gives `b2=-a3`, and `q1=q3=a1^2`. The reduced support therefore has `a1=0`; then `q4-q2=(b1-c)(b1+c)`. This branch consists of two smooth conics, each with generic scheme multiplicity two.

The two conics each contain exactly six of the 14 box nodes on the hyperplane. Since incidence is exactly 14, the only possible `N>=14` support is the full 14-node set itself. Therefore for either conic

```text
D_l.Q = l(7*2-4*6) = -10l < 0.
```

Hence the entire size-96 incidence-14 orbit is irreducibly excluded for the displayed uniform ray.

The complementary branch `b2=-b3` accounts for the remaining section degree; its full component classification is not needed for this fixed-conic obstruction.

## Retained consequence

For the displayed uniform genus-one Picard ray:

```text
incidence 24: closed by forced fixed conic;
incidence 20: closed by forced fixed section component;
incidence 19: closed by forced fixed conic;
incidence 16, orbit size 3: only 32 balanced N=14 supports survive;
incidence 16, orbit size 24: only 64 balanced N=14 supports survive;
incidence 14, orbit size 96: closed by a doubled-conic branch with pairing -10l.
```

This is a genuine support-span statement because it never assumes the carrier lies in the support hyperplane.

It does not close arbitrary Picard classes with unequal exceptional coefficients. The incidence-15 orbit and the remaining four incidence-14 orbits are still open, as are the 96 balanced incidence-16 supports.

## Verification

`verify_mb104_genus1_span5_uniform_ray_component_capacity.py` replays the exact 48-node model, incidence-16 component systems, all 14-of-16 support complements, rank-six span checks, the incidence-14 size-96 representative, and the capacity inequalities.

Local replay:

```text
PASS STAGE32_MB104_GENUS1_SPAN5_UNIFORM_RAY_COMPONENT_CAPACITY_V2
inc24=N>=14_forces_negative_component capacity=24 incidence_at_least=28
inc20=N>=14_forces_negative_component capacity=26 incidence_at_least=28
inc19=N>=14_forces_negative_conic capacity=12 incidence_at_least=14
inc16_orbit3=N>=15_forced;N14_balanced_spanning_survivors=32 counts=7,7,7,7
inc16_orbit24=N>=15_forced;N14_balanced_spanning_survivors=64 counts=7,7
inc14_orbit96=unique_N14_support_forces_double_conic_pairing_minus10l conic_node_counts=6,6
```

No exact-head CI claim is made.

## Next leaf

1. test the 32+64 balanced incidence-16 supports against retained Picard/fibration/effectivity data;
2. attack the incidence-15 orbit and remaining four incidence-14 orbits for analogous test-curve pairings;
3. do not infer carrier degree from support-hyperplane section degree.

## Firewalls

- this result applies to the displayed uniform ray `7lH-4l sum E_i`, not arbitrary divisor classes;
- balanced incidence-16 subsets are survivors, not constructed curves;
- support-span 5 as a whole remains open;
- genus-one span-six and genus-zero full-span remain open;
- no population-wide finite degree window, receiver, theorem, endpoint, Perfect-Cuboid or merge credit.
