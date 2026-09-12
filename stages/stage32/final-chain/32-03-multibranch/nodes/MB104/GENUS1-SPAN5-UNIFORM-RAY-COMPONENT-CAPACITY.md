# Stage32 MB104 genus-one span-five uniform-ray component capacity

Status: **RETAINED FIXED-COMPONENT OBSTRUCTION FOR INCIDENCE 24/20/19 / INCIDENCE-16 BALANCED SURVIVORS ISOLATED / SUPPORT-SPAN 5 STILL OPEN / NO DOWNSTREAM CREDIT**

This checkpoint repairs the support-span semantics and uses the retained hyperplane-section components only through exact Picard intersection pairings.

## Scope

The unknown genus-one carrier need not lie in the support hyperplane `H=P^5`. The box-node support `Sigma` merely spans `H`. Therefore section components of `S intersect H` are used as test curves, not as candidate carrier components.

The target here is the displayed infinite Picard ray from `FORMAL-INFINITE-FAMILY-PICARD-REALIZABILITY`:

```text
D_l = 7l H - 4l sum_{i in Sigma} E_i,
l>=1,
|Sigma|=14,
d=H.D_l=112l.
```

More generally the same capacity argument applies to support size `N>=14` with these uniform exceptional coefficients.

## Pairing rule

Let `Q` be a reduced component of the support-hyperplane section. If

```text
e = H.Q,
n_Q = number of supported box nodes of Sigma lying on Q,
```

and `Q` meets each corresponding exceptional curve once, then

```text
D_l.Q = 7l e - 4l n_Q
      = l(7e-4n_Q).
```

Hence nonnegative pairing requires

```text
n_Q <= floor(7e/4).
```

For a conic (`e=2`) the capacity is `3` supported nodes. For an elliptic quartic (`e=4`) the capacity is `7`.

If any component has negative pairing, every effective divisor in `|D_l|` contains that component, so an irreducible effective representative of the ray is impossible.

## Incidence 24: forced fixed conic

The retained incidence-24 classification gives eight smooth conics and every section node lies on exactly two conics.

For any support of size `N>=14`, total supported node/component incidence is at least

```text
2N >= 28.
```

But eight nonnegative conic pairings can carry at most

```text
8*3 = 24
```

supported incidences. Therefore at least one conic has `n_Q>=4`, so `D_l.Q<0`.

Thus every incidence-24 support configuration on the uniform ray has a fixed conic component.

## Incidence 20: forced fixed section component

The exact section is

```text
4 smooth conics + 2 smooth elliptic quartics,
```

and every one of its 20 nodes lies on exactly two reduced components.

If all component pairings were nonnegative, the total supported incidence capacity would be

```text
4*3 + 2*7 = 26.
```

For `N>=14`, actual supported incidence is at least `2N>=28`. Contradiction.

Hence every incidence-20 support configuration on the uniform ray forces a negative-pairing section component and has no irreducible effective representative.

## Incidence 19: forced fixed conic

The reduced support is four smooth conics. Every one of the 19 section nodes lies on at least one reduced conic.

Four nonnegative conic pairings have total support capacity

```text
4*3 = 12.
```

Any `N>=14` support contributes at least 14 conic incidences, so some conic has `n_Q>=4` and negative pairing.

Thus every incidence-19 support configuration on the uniform ray is irreducibly excluded.

## Incidence 16, size-3 orbit: finite balanced survivors

The section is four smooth elliptic quartics, every section node lies on exactly two quartics, and each quartic can contain at most seven supported nodes without negative pairing.

For `N>=15`, total supported incidence is at least `30`, exceeding the nonnegative capacity

```text
4*7 = 28.
```

So all `N>=15` supports are excluded.

For `N=14`, nonnegative pairing is possible only in the exact balanced pattern

```text
(7,7,7,7).
```

Exact enumeration of the 120 two-node complements of the 16-node section finds exactly

```text
32
```

balanced 14-node supports. All 32 retain rank six over the good prime `p=1097`, hence still span the same support hyperplane.

Therefore this orbit reduces from arbitrary 14-node subsets to 32 explicit balanced support subsets.

## Incidence 16, size-24 orbit: finite balanced survivors

The reduced section support consists of two smooth elliptic quartics with disjoint 8-node supports; each has scheme multiplicity two.

For `N>=15`, one quartic contains at least 8 supported nodes, giving negative pairing.

For `N=14`, both pairings are nonnegative only for the balanced split

```text
(7,7).
```

Equivalently one omitted node must be chosen from each 8-node quartic. There are exactly

```text
8*8 = 64
```

such 14-node supports, and exact rank replay shows all 64 still span the same support hyperplane.

## Retained consequence

Within the displayed uniform genus-one Picard ray:

```text
incidence 24: closed by forced fixed conic;
incidence 20: closed by forced fixed section component;
incidence 19: closed by forced fixed conic;
incidence 16, orbit size 3: only 32 balanced N=14 supports survive;
incidence 16, orbit size 24: only 64 balanced N=14 supports survive.
```

This is a genuine support-span statement because it never assumes the unknown carrier lies in the support hyperplane.

It does **not** close arbitrary Picard classes with unequal exceptional coefficients, and it does not yet handle incidence 15 or 14 ambient orbits.

## Verification

`verify_mb104_genus1_span5_uniform_ray_component_capacity.py` replays the exact 48-node model, the two incidence-16 component systems, all 14-of-16 support complements, rank-six span checks, and the component-capacity inequalities.

Local replay:

```text
PASS STAGE32_MB104_GENUS1_SPAN5_UNIFORM_RAY_COMPONENT_CAPACITY_V1
inc24=N>=14_forces_negative_component capacity=24 incidence_at_least=28
inc20=N>=14_forces_negative_component capacity=26 incidence_at_least=28
inc19=N>=14_forces_negative_conic capacity=12 incidence_at_least=14
inc16_orbit3=N>=15_forced;N14_balanced_spanning_survivors=32 counts=7,7,7,7
inc16_orbit24=N>=15_forced;N14_balanced_spanning_survivors=64 counts=7,7
```

No exact-head CI claim is made.

## Next leaf

1. test the 32+64 balanced incidence-16 support subsets against the retained rank-3/fibration/Picard/effectivity data;
2. classify incidence-15 and incidence-14 support-hyperplane sections only far enough to obtain analogous test-curve capacity inequalities;
3. do not infer carrier degree from support-hyperplane section degree.

## Firewalls

- this result applies to the displayed uniform ray `7lH-4l sum E_i` and the same uniform coefficient pattern, not arbitrary divisor classes;
- balanced incidence-16 subsets are survivors, not constructed curves;
- support-span 5 as a whole remains open;
- genus-one span-six and genus-zero full-span remain open;
- no population-wide finite degree window, receiver, theorem, endpoint, Perfect-Cuboid or merge credit.
