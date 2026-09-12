# Stage32 MB104 global-classification checkpoint

Status: **ACTIVE PRIORITY / SUPPORT-SPAN SEMANTICS REPAIRED / GENUS-ONE SPAN-5 AMBIENT AUT QUOTIENT COMPLETE / UNIFORM-RAY FIXED-COMPONENT PROGRESS / P6 OPEN / NO CREDIT**

Read this checkpoint under `PRIORITY-OVERRIDE-20260912.json`. The direct inequality

```text
d <= 16g-16+4R8
```

remains valid, but direct pursuit of `R8<d/4+O(1)` is frozen until a genuinely new lever appears.

## Hard sectors

```text
g=0: box-node support spans P^6;
g=1: box-node support span dimension 5 or 6;
potentially infinite sector: N>=14.
```

The word `span` in this route refers to the **box-node support**, not the unknown carrier curve.

## Formal/Picard status

The retained formal families `F0-P6`, `F1-P5`, `F1-P6` survive the older packet inequalities. Infinite integral Picard subsequences also survive. For the genus-one P5 family the displayed ray is

```text
D_l = 7l H - 4l sum_{i in Sigma} E_i,
|Sigma|=14,
d=112l.
```

Bare Picard integrality and effectivity do not close it; irreducibility is the issue.

## Exact finite support-hyperplane reduction

Every potentially infinite genus-one support of span dimension five lies in one of exactly `1,655` node-spanned ambient `P^5` hyperplanes containing at least 14 of the 48 box nodes:

```text
14: 1248
15:  256
16:   27
19:   48
20:   48
24:   28
```

Stable exact-support digest: `ba8379b50029db53`.

The complete `Aut(S)` quotient has 12 support-hyperplane orbits:

```text
14: sizes 96,192,192,384,384
15: size 256
16: sizes 3,24
19: size 48
20: size 48
24: sizes 4,24
```

## Semantic repair

The support hyperplane contains `Sigma`, not necessarily the carrier curve. Therefore:

```text
carrier C need not lie in H=Span(Sigma),
section-component degree does not bound deg(C),
C is not identified with a component of S intersect H.
```

The previous provisional inference closing incidence `>=16` from section-component degrees is revoked. The exact section decompositions themselves remain valid and are retained only as explicit test-curve geometry.

## Retained section geometry

- incidence 24: eight smooth conics;
- incidence 20: four smooth conics plus two smooth elliptic quartics;
- incidence 19: four smooth conics, each generically doubled scheme-theoretically;
- incidence 16, orbit size 3: four smooth elliptic quartics;
- incidence 16, orbit size 24: two smooth elliptic quartics, each generically doubled.

## New valid consequence: uniform-ray component capacity

For a reduced section component `Q` of degree `e=H.Q`, meeting `n_Q` supported nodes, the displayed uniform ray satisfies

```text
D_l.Q = l(7e-4n_Q).
```

Thus a conic can contain at most 3 supported nodes and an elliptic quartic at most 7 if all pairings are to remain nonnegative. Negative pairing forces that section component into every effective member of `D_l`, excluding irreducibility.

Applying the exact node/component incidence data gives:

```text
incidence 24: forced negative conic for every N>=14 support;
incidence 20: forced negative section component for every N>=14 support;
incidence 19: forced negative conic for every N>=14 support;
incidence 16, size-3 orbit: N>=15 forced; N=14 leaves exactly 32 balanced (7,7,7,7) supports;
incidence 16, size-24 orbit: N>=15 forced; N=14 leaves exactly 64 balanced (7,7) supports.
```

All 96 balanced incidence-16 supports retain rank six and genuinely span their support hyperplane.

This is a correct support-span obstruction because it uses `H` only to supply explicit test curves and does not assume the carrier lies in `H`.

## What remains open

The uniform-ray P5 route is not closed: 96 balanced incidence-16 supports survive on the two representative incidence-16 orbits, and incidence 15/14 have not yet been converted into pairing-capacity obstructions. Arbitrary Picard classes with unequal exceptional coefficients are also not covered.

Genus-one support-span six and genus-zero full-span remain open.

## Next execution leaf

`MB104-GENUS1-SPAN5-INC16-BALANCED-PLUS-INC15-14`:

1. test the 32+64 balanced incidence-16 supports against retained Picard/fibration/effectivity constraints;
2. classify incidence-15 and incidence-14 support-hyperplane sections only far enough to derive valid component pairings/capacities;
3. keep genus-one support-span P6 and genus-zero full-span active in parallel;
4. never infer carrier degree from support-hyperplane section degree.

## Firewalls

- support-span five is not closed;
- the uniform-ray result does not cover arbitrary unequal exceptional coefficients;
- no population-wide finite degree window is proved;
- MB104 remains incomplete and MB105 remains gated;
- no receiver/effectivity-final/theorem/endpoint/Perfect-Cuboid credit;
- no merge authorization.
