# Stage32 MB104 global-classification checkpoint

Status: **ACTIVE PRIORITY / SUPPORT-SPAN SEMANTICS REPAIRED / UNIFORM P5 RAY REDUCED TO FOUR BALANCED INC16 SUPPORT ORBITS / STATIC LANDING ROUTE DOMINATED / P6 OPEN / NO CREDIT**

Read this checkpoint under `PRIORITY-OVERRIDE-20260912.json`. Direct pursuit of `R8<d/4+O(1)` remains frozen until a genuinely new lever appears.

The most recent hostile-audited retained boundary is exact head

```text
39a56d2a9abda0c051145172ff61d67eef0bdb14
```

with `HOSTILE AUDIT: PASS`. The present continuation is newer retained work and has not yet been hostile-audited.

## Hard sectors and span semantics

```text
g=0: box-node support spans P^6;
g=1: box-node support span dimension 5 or 6;
potentially infinite sector: N>=14.
```

`span` refers to the box-node support, not the unknown carrier curve. The carrier need not lie in its support hyperplane.

## Displayed uniform genus-one P5 ray

The retained ray is

```text
D_l=7lH-4l sum_{i in Sigma}E_i,
|Sigma|=14,
d=112l,
l>=1.
```

For a retained test curve `Q` of degree `e=H.Q` meeting `n_Q` supported nodes,

```text
D_l.Q=l(7e-4n_Q).
```

Thus a conic becomes negative at `n_Q>=4` and an elliptic quartic becomes negative at `n_Q>=8`.

## Complete ambient reduction

Support-span five is reduced to exactly 1,655 node-spanned `P^5` hyperplanes:

```text
14:1248, 15:256, 16:27, 19:48, 20:48, 24:28.
```

The complete `Aut(S)` quotient has 12 ambient orbits:

```text
14: sizes 96,192,192,384,384
15: size 256
16: sizes 3,24
19: size 48
20: size 48
24: sizes 4,24.
```

## Uniform-ray closures

Retained fixed-component arguments now give

```text
incidence 24: CLOSED
incidence 20: CLOSED
incidence 19: CLOSED
incidence 15: CLOSED
incidence 14: ALL FIVE AMBIENT ORBITS CLOSED
```

The incidence-15 and complete incidence-14 closure uses the 32 known smooth conics. Each incidence-14 representative has two known conics through six supported nodes, hence pairing `-10l`. The incidence-15 representative has three six-node conics; every rank-six 14-node omission has negative-conic incidences `[6,6,5]`. Automorphism transport closes the full ambient orbits.

Evidence:

- `GENUS1-SPAN5-KNOWN-CONIC-BALANCED-QUOTIENT.md`
- `GENUS1-SPAN5-KNOWN-CONIC-BALANCED-QUOTIENT-CERTIFICATE.json`
- `verify_mb104_genus1_span5_known_conic_balanced_quotient.py`

## Incidence-16 hard core

The only surviving supports for the displayed uniform ray are balanced `N=14` supports.

On representative ambient hyperplanes:

```text
size-3 ambient orbit: 32 supports, pattern (7,7,7,7)
size-24 ambient orbit: 64 supports, pattern (7,7)
```

Every support has rank six and therefore a unique support hyperplane. Globally this gives

```text
3*32 + 24*64 = 1632
```

supports. Their exact `Aut(S)` quotient has only four orbits:

```text
canonical support mask   orbit size
0000770000ff                48
00007b0000ff                48
000707000f0f               768
00070b000f0f               768
```

For all 96 representative balanced supports:

```text
max incidence on any of the 32 known conics = 2,
max incidence on any of the 12 retained elliptic quartics = 7.
```

Therefore the retained low-degree test-curve library has no negative pairing on this hard core.

## Zero-pairing quartics and the static-landing wall

The four support orbits do have zero-pairing elliptic quartics:

```text
orbit sizes 48,48: 4 zero quartics; every supported node lies on 2;
orbit sizes 768,768: 2 zero quartics; every supported node lies on 1.
```

An irreducible effective carrier would have to be disjoint from those quartics on the resolution, hence avoid their exceptional landing points at shared box nodes.

However the retained formal packet has `k=4l`, `M_i=2k=8l`, all branches FSM-minimal with multiplicity one, and pairwise distinct nonzero landing keys. Static zero-quartic avoidance forbids at most two landing points per node. Over the infinite characteristic-zero geometric field this leaves infinitely many local choices, so `8l` distinct admissible landing values can still be chosen for every finite `l`.

Thus **landing value alone is not the missing obstruction**. See:

- `BALANCED16-STATIC-LANDING-AVOIDANCE-WALL.md`
- `BALANCED16-STATIC-LANDING-AVOIDANCE-CERTIFICATE.json`
- `verify_mb104_balanced16_static_landing_wall.py`

The next useful lever must couple global tangent/first-jet data, simultaneous algebraic gluing, or stronger Picard/effective-cone geometry.

## Remaining open work

For support-span five:

- the displayed uniform ray is reduced to four balanced incidence-16 support orbits, but those four are not closed;
- arbitrary Picard classes with unequal exceptional coefficients remain open.

In parallel:

- genus-one support-span `P^6` remains open;
- genus-zero full-span `P^6` remains open.

## Next execution leaf

`MB104-GENUS1-SPAN5-BALANCED16-FIRST-JET-GLOBAL-COMPATIBILITY`:

1. work only on the four balanced support orbits `48,48,768,768` for the displayed uniform ray;
2. do not retry static landing-value exclusion;
3. test whether the required low-genus/global cuboid equations force tangent or first-jet coincidence with a zero-pairing elliptic quartic, or otherwise obstruct simultaneous local choices;
4. if that route is still free, look for a stronger Picard/effective-cone wall;
5. keep P6 hard sectors active in parallel.

## Firewalls

- support-span five is not closed;
- the displayed uniform P5 ray is not fully closed because four balanced support orbits survive;
- arbitrary unequal exceptional coefficients are not covered;
- no population-wide finite degree window is proved;
- MB104 remains incomplete and finite Picard enumeration is unreleased;
- no receiver/effectivity-final/theorem/endpoint/Perfect-Cuboid credit;
- no merge authorization.
