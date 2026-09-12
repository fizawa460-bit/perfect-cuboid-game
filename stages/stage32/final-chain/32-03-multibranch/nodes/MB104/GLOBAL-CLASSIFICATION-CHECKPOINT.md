# Stage32 MB104 global-classification checkpoint

Status: **ACTIVE PRIORITY / SUPPORT-SPAN SEMANTICS REPAIRED / UNIFORM P5 RAY REDUCED TO FOUR BALANCED INC16 SUPPORT ORBITS / ZERO-QUARTIC PIC^0 ROUTE EXHAUSTED / P6 OPEN / NO CREDIT**

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

A conic becomes negative at `n_Q>=4`; an elliptic quartic becomes negative at `n_Q>=8`.

## Complete ambient reduction and uniform-ray closures

Support-span five is reduced to exactly 1,655 node-spanned `P^5` hyperplanes with incidence distribution

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

Retained fixed-component arguments close, for the displayed uniform ray,

```text
incidence 24: CLOSED
incidence 20: CLOSED
incidence 19: CLOSED
incidence 15: CLOSED
incidence 14: ALL FIVE AMBIENT ORBITS CLOSED.
```

The complete incidence-14/15 closure uses the 32 known smooth conics and is retained in `GENUS1-SPAN5-KNOWN-CONIC-BALANCED-QUOTIENT-*`.

## Incidence-16 hard core

The only surviving supports for the displayed uniform ray are balanced `N=14` supports.

On representative ambient hyperplanes:

```text
size-3 ambient orbit: 32 supports, pattern (7,7,7,7)
size-24 ambient orbit: 64 supports, pattern (7,7).
```

Globally this gives

```text
3*32 + 24*64 = 1632
```

supports. Their complete `Aut(S)` quotient has exactly four orbits:

```text
0000770000ff   size 48
00007b0000ff   size 48
000707000f0f   size 768
00070b000f0f   size 768.
```

Across all representative balanced supports,

```text
max incidence on any of the 32 known conics = 2,
max incidence on any of the 12 retained elliptic quartics = 7.
```

Thus no retained conic/quartic has negative pairing on this hard core.

## Zero-pairing quartics: static landing values are insufficient

The four support orbits have zero-pairing elliptic quartics:

```text
orbit sizes 48,48: 4 zero quartics; each supported node lies on 2;
orbit sizes 768,768: 2 zero quartics; each supported node lies on 1.
```

The formal packet has `M_i=8l` multiplicity-one branches with pairwise distinct nonzero exceptional landing keys. A zero quartic forbids at most one landing point, so at most two static points are forbidden at a supported node. Over the infinite characteristic-zero geometric field this cannot close the packet. This negative route is retained in `BALANCED16-STATIC-LANDING-AVOIDANCE-*`.

## New exact wall: the hidden Pic^0 obstruction is also absent

For the representative elliptic quartic

```text
Q: z^2=x^2+y^2,
   w^2=x^2-y^2,
```

the eight box nodes split as the two degree-four hyperplane sections `x=0` and `y=0`. Therefore

```text
B_Q ~ 2H_Q.
```

The 12 retained elliptic quartics, together with their eight box nodes each, give `12*8=96` incident pairs `(Q,P)`. Exact `Aut(S)` replay shows these 96 pairs form a single orbit.

At the representative point

```text
P=[0:1:1:-i],
```

the plane

```text
-2y+z+i w=0
```

cuts `Q` as `4P`; equivalently

```text
H_Q ~ 4P.
```

Projective-linear automorphism transport gives this relation for every box node on every retained elliptic quartic.

For a zero-pairing quartic of a balanced support, exactly one of its eight box nodes is omitted, so

```text
Sigma cap Q = B_Q-P.
```

For the primitive uniform-ray class `A=7H-4 sum E_i`,

```text
A|_Q
 ~ 7H_Q-4(B_Q-P)
 ~ 4P-H_Q
 ~ 0.
```

Hence

```text
O_Q(D_l) ~= O_Q
```

for every `l>=1` and every zero-pairing quartic in all four balanced support orbits.

Therefore the tempting route

```text
D_l.Q=0 but O_Q(D_l) is nontrivial degree zero,
forcing Q into every effective divisor
```

is false. There is no hidden `Pic^0` obstruction.

Evidence:

- `GENUS1-SPAN5-BALANCED16-ZERO-QUARTIC-PIC0-WALL.md`
- `GENUS1-SPAN5-BALANCED16-ZERO-QUARTIC-PIC0-CERTIFICATE.json`
- `verify_mb104_balanced16_zero_quartic_pic0.py`.

This still does **not** prove that the restriction map

```text
H^0(S,O(D_l)) -> H^0(Q,O_Q)
```

is nonzero. Thus a zero quartic may still be a fixed component for a different global reason; that question is now isolated cleanly.

## Remaining open work

For support-span five:

- the displayed uniform ray is reduced to four balanced incidence-16 support orbits;
- static landing-value exclusion is exhausted;
- nontrivial degree-zero/Pic^0 restriction is exhausted;
- the global restriction-map/fixed-locus question is open;
- simultaneous algebraic gluing of the required multibranch jets is open;
- arbitrary Picard classes with unequal exceptional coefficients remain open.

In parallel:

- genus-one support-span `P^6` remains open;
- genus-zero full-span `P^6` remains open.

## Next execution leaf

`MB104-GENUS1-SPAN5-BALANCED16-RESTRICTION-MAP-AND-GLUING`:

1. determine whether `H^0(S,O(D_l))->H^0(Q,O_Q)` is zero or surjective for the four support orbits;
2. if nonzero, test simultaneous multibranch jet gluing across all fourteen exceptional curves;
3. if the restriction map is identically zero, identify the actual fixed-locus mechanism;
4. if neither route closes, seek a stronger nef/effective-cone wall;
5. keep the P6 hard sectors active in parallel.

## Firewalls

- support-span five is not closed;
- the displayed uniform P5 ray is not fully closed because four balanced support orbits survive;
- arbitrary unequal exceptional coefficients are not covered;
- restriction-map nonzero/surjective is not proved;
- no population-wide finite degree window is proved;
- MB104 remains incomplete and finite Picard enumeration is unreleased;
- no receiver/effectivity-final/theorem/endpoint/Perfect-Cuboid credit;
- no merge authorization.
