# Stage32 MB104 global-classification checkpoint

Status: **ACTIVE PRIORITY / SUPPORT-SPAN SEMANTICS REPAIRED / GENUS-ONE SPAN-5 AMBIENT AUT QUOTIENT COMPLETE / UNIFORM-RAY FIXED-COMPONENT PROGRESS / P6 OPEN / NO CREDIT**

Read this checkpoint under `PRIORITY-OVERRIDE-20260912.json`. Direct pursuit of `R8<d/4+O(1)` remains frozen until a genuinely new lever appears.

## Hard sectors and span semantics

```text
g=0: box-node support spans P^6;
g=1: box-node support span dimension 5 or 6;
potentially infinite sector: N>=14.
```

`span` refers to the box-node support, not the unknown carrier curve. The carrier need not lie in its support hyperplane.

## Formal/Picard status

The retained formal families `F0-P6`, `F1-P5`, `F1-P6` survive the older packet inequalities. The displayed genus-one P5 Picard ray is

```text
D_l=7lH-4l sum_{i in Sigma}E_i,
|Sigma|=14,
d=112l.
```

Bare Picard integrality and effectivity do not close it; irreducibility is the issue.

## Exact support-hyperplane reduction

The support-span-five sector is reduced to exactly `1,655` node-spanned `P^5` hyperplanes:

```text
14:1248, 15:256, 16:27, 19:48, 20:48, 24:28.
```

Stable support digest: `ba8379b50029db53`.

The complete `Aut(S)` quotient has 12 orbits:

```text
14: sizes 96,192,192,384,384
15: size 256
16: sizes 3,24
19: size 48
20: size 48
24: sizes 4,24.
```

## Semantic repair

The previous provisional inference that section-component degree bounds carrier degree is revoked. Exact section decompositions remain retained only as test-curve geometry for explicit intersection/fixed-component arguments.

Retained section geometry includes:

- incidence 24: eight smooth conics;
- incidence 20: four smooth conics plus two smooth elliptic quartics;
- incidence 19: four smooth conics, each generically doubled;
- incidence 16 size-3: four smooth elliptic quartics;
- incidence 16 size-24: two smooth elliptic quartics, each generically doubled.

## Uniform-ray pairing interface

For a reduced section component `Q` of degree `e=H.Q` meeting `n_Q` supported nodes,

```text
D_l.Q=l(7e-4n_Q).
```

Hence a conic has nonnegative support capacity `3`, and an elliptic quartic capacity `7`. Negative pairing forces a fixed component and excludes an irreducible effective representative of the displayed ray.

## Current valid closures/reductions for the uniform ray

```text
incidence 24: closed by forced fixed conic;
incidence 20: closed by forced fixed section component;
incidence 19: closed by forced fixed conic;
incidence 16 size-3: N>=15 closed; N=14 leaves exactly 32 balanced (7,7,7,7) spanning supports;
incidence 16 size-24: N>=15 closed; N=14 leaves exactly 64 balanced (7,7) spanning supports.
```

### New: incidence-14 orbit size 96 closed

Representative:

```text
-a2+a3+b2+b3=0,
support mask 0000185aa566.
```

On this hyperplane

```text
q1-q3=2(a2-b3)(b2+b3).
```

The `a2=b3` branch contains two smooth conics, each generically doubled, and each conic contains 6 of the 14 box nodes. Since incidence is exactly 14, the only possible `N>=14` support is the full node set, giving

```text
D_l.Q=l(14-24)=-10l<0.
```

Thus the full size-96 incidence-14 orbit is irreducibly excluded for the displayed uniform ray.

## Remaining open support-span-five work

For the displayed uniform ray:

- 96 balanced incidence-16 supports remain;
- incidence-15 orbit size 256 remains open;
- four incidence-14 orbits remain open: sizes `192,192,384,384`.

Arbitrary Picard classes with unequal exceptional coefficients are not covered by the uniform-ray capacity argument. Genus-one support-span six and genus-zero full-span also remain open.

## Next execution leaf

`MB104-GENUS1-SPAN5-BALANCED16-AND-LOWER-INCIDENCE`:

1. test the 32+64 balanced incidence-16 supports against retained global constraints;
2. attack incidence 15 and the remaining four incidence-14 orbits for valid test-curve pairings/capacity obstructions;
3. keep genus-one support-span P6 and genus-zero full-span active in parallel;
4. never infer carrier degree from support-hyperplane section degree.

## Firewalls

- support-span five is not closed;
- the uniform-ray result does not cover arbitrary unequal exceptional coefficients;
- no population-wide finite degree window is proved;
- MB104 remains incomplete and MB105 remains gated;
- no receiver/effectivity-final/theorem/endpoint/Perfect-Cuboid credit;
- no merge authorization.
