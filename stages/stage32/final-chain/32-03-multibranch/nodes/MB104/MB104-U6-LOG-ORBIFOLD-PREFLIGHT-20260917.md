# Stage32 MB104 — U6 log/orbifold preflight — 2026-09-17

Status: **U6 BLOCKED AS STANDALONE UNIFORM-CLOSURE ROUTE / NO CREDIT**

## Scope

This note tests restart candidate U6: use a log/orbifold surface inequality on the exact balanced genus-one ray

```text
D_l = 7l H - 4l sum_(p in Sigma) E_p,
|Sigma|=14,
l>=1,
D_l^2=336l^2,
K_S.D_l=112l,
g=1.
```

It does not reopen conductor-sheet recovery, Armstrong H1, or counting-only RH routes.

## 1. Standard Miyaoka 2008 route is archived-equivalent

The archived PR #1791 already proves that Miyaoka's one-curve orbibundle inequality becomes

```text
168 l(l+1) alpha^2 - 224 l alpha + 224 >= 0
```

and its minimum is strictly positive for every `l>=1`. Therefore this part of U6 is `EQUIVALENT/BLOCKED`, not a new route.

Archived source:

```text
old head ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11
MIYAOKA2008-ORBIBUNDLE-GENUS1-WALL.md
```

## 2. Sabatino open-surface boundary with all 48 exceptionals

Let

```text
B = sum_(i=1)^48 E_i.
```

The 48 exceptional `(-2)`-curves are pairwise disjoint, `K_S.E_i=0`, and `c2(S)=80`. Hence

```text
B^2=-96,
(K_S+B)^2=16-96=-80,
e(S\B)=80-48*2=-16,
3e(S\B)-(K_S+B)^2=32.
```

For the balanced packet, only 14 exceptionals meet the carrier and each contributes `8l` normalization preimages/intersection points, so

```text
(K_S+B).D_l = 112l + 14*8l = 224l,
e_(D_l\B) = -112l.
```

Sabatino's BMY-type inequality therefore specializes exactly to

```text
168 l(l+1) alpha^2 - 112 l alpha + 32 >= 0.
```

The minimum on `[0,1]` occurs at

```text
alpha_l = 1/(3(l+1))
```

and equals

```text
32 - (56/3)*l/(l+1)
= (40l+96)/(3(l+1))
> 40/3.
```

Thus even the full exceptional boundary remains uniformly on the allowed side; it gives no all-`l` contradiction and no large-`l` cutoff.

Published input: Pietro Sabatino, *An Explicit Bound for the Log-Canonical Degree of Curves on Open Surfaces*, PRIMS 58 (2022), Theorem 1.1.

## 3. Zero-pairing elliptic quartics make the defect worse

The balanced hard core has retained elliptic quartics `Q` with

```text
D_l.Q=0,
K_S.Q=4,
Q^2=-4,
```

and each such quartic meets eight exceptional curves. Starting from `B=sum E_i`, add one such quartic to the reduced boundary.

Because `Q` is elliptic and meets the old boundary in eight points,

```text
e(Q\B) = -8,
```

so removing `Q\B` raises the open Euler number by `8`, contributing `+24` to `3e`. Meanwhile

```text
(K_S+B+Q)^2-(K_S+B)^2
 = 2(K_S+B).Q+Q^2
 = 2(4+8)-4
 = 20.
```

Therefore

```text
[3e-(K+D)^2] : 32 -> 36.
```

Since `D_l.Q=0`, neither the relative canonical degree nor the puncture count of the carrier improves. Adding a zero-pairing elliptic quartic strictly weakens this inequality.

## 4. Langer local-orbifold enhancement does not force a quadratic charge

A possible rescue would be to use local orbifold Euler numbers for an ordinary high-multiplicity singularity. That is not uniform on the MB104 receiver.

The archived A1 resolution geometry permits minimal branches over a box node to have pairwise distinct landing parameters on the exceptional line. In that realization the `8l` branches over one downstairs box node are separated on the smooth resolution `S`; they need not form one `8l`-fold singular point of the strict transform. The retained finite-jet wall likewise permits arbitrarily many branches with distinct or repeated finite jets without forcing the needed global collision.

Consequently a Langer-style local charge that grows quadratically with the number of coincident branches is not forced by the current exact MB104 receiver. Any such use would require a genuinely new **global collision theorem** proving that sufficiently many branches must meet at the same resolved point or otherwise create an equivalent local orbifold contribution.

Archived source boundaries:

```text
R8-BOUND-ROUTE-LEDGER.md
FINITE-JET-MULTIPLICITY-SATURATION-WALL.md
```

## Verdict

```text
U6_STANDARD_MIYAOKA = EQUIVALENT/BLOCKED
U6_SABATINO_FULL_EXCEPTIONAL_BOUNDARY = BLOCKED
U6_ZERO_PAIRING_QUARTIC_AUGMENTATION = BLOCKED
U6_LANGER_LOCAL_MULTIBRANCH_CHARGE = BLOCKED_UNLESS_NEW_GLOBAL_COLLISION_INPUT
```

U6 remains useful only if a new exact global theorem forces branch collisions/tangencies that the retained local model currently allows one to avoid. Without that new input it is not a replacement theorem for MB104.

No finite `l` window, receiver credit, effectivity credit, theorem credit, endpoint credit, merge authorization, or Perfect-Cuboid claim is produced.
