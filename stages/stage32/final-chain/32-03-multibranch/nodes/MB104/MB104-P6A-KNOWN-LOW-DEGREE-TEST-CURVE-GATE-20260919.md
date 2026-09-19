# MB104 P6A — genus-one full-span known low-degree test-curve gate — 2026-09-19

Status: **PRE-AUDIT EXACT FINITE GEOMETRY / NO CREDIT**

## Purpose

After parking span-five simple-contact / primitive-Hilbert work, return to the genus-one full-span `P^6` sector.

The historical hostile family retained an explicit 14-node full-span support `S_P6` and the infinite Picard ray

```
D_l = 7l H - 4l sum_{i in S_P6} E_i,  l>=1.
```

Historical Riemann--Roch proves this class is effective for every `l>=1`. What remained open was irreducibility / actual low-genus carrier existence.

This checkpoint reuses the retained low-degree test-curve library:

- 32 known smooth plane conics;
- 12 retained smooth elliptic quartics.

No uniform exceptional-coefficient statement is promoted to the whole P6 population.

## Exact old hostile support

In the retained 48-node ordering the historical `S_P6` support is

```
mask = 03c003818383
nodes = {0,1,7,8,9,15,16,23,24,25,38,39,40,41}.
```

It spans `P^6`.

The exact 32-conic replay gives supported-node incidence distribution

```
0 nodes: 4 conics
1 node : 11 conics
2 nodes: 8 conics
3 nodes: 8 conics
5 nodes: 1 conic
```

The unique five-node conic in the chosen representative has

```
conic support = {1,7,9,15,41,46}
carrier support intersection = {1,7,9,15,41}.
```

For the strict transform `Q` of a known conic,

```
H.Q=2,
E_i.Q=1 when node i lies on Q.
```

Therefore

```
D_l.Q = 14l - 4l*5 = -6l < 0.
```

Every effective divisor in this displayed P6 class contains `Q` as a fixed component. Since `H.D_l=112l>2=H.Q`, the divisor cannot equal `Q`.

Hence the historical displayed `F1-P6-PIC` ray has **no irreducible effective member**.

The exact Aut(S) orbit of this 14-node support has size `1536`. By automorphism transport the same fixed-conic obstruction closes the full support orbit.

This is stronger than the historical checkpoint, which had proved effectivity but left the displayed P6 ray open.

## This does not close all P6 supports

An exact finite search over the same 48-node configuration produces a different 14-node support

```
mask = 0000093f442e
nodes = {1,2,3,5,10,14,16,17,18,19,20,21,24,27}.
```

The seven rows

```
{1,2,3,5,10,14,16}
```

have determinant `-16`, so this support spans `P^6`.

Against all 32 known conics its incidence distribution is

```
0:4, 1:8, 2:12, 3:8,
max = 3.
```

Against all 12 retained elliptic quartics its incidence distribution is

```
1:5, 2:2, 3:2, 4:2, 5:1,
max = 5.
```

Thus for the analogous uniform ray

```
D'_l = 7lH - 4l sum_{i in S'} E_i
```

all retained low-degree test curves have strictly positive pairing:

```
known conic:       D'_l.Q >= 14l-12l = 2l > 0,
elliptic quartic:  D'_l.E >= 28l-20l = 8l > 0.
```

The Riemann--Roch effectivity argument depends only on the 14 orthogonal exceptional classes and therefore applies to `D'_l` as well:

```
D'^2 = 336l^2,
H.D' = 112l,
chi(O(D')) = 168l^2-56l+8 > 0,
H.(K-D') = 16-112l < 0.
```

Hence `D'_l` is effective for every `l>=1`.

This is a **hostile survivor class**, not a constructed irreducible genus-one curve. The exact result is only that the retained 32-conic + 12-quartic test library does not force a fixed low-degree component on this support.

## Route consequence

The old explicit P6 hostile ray is closed as an irreducible-carrier candidate, but P6 itself remains open.

Therefore:

```
historical F1-P6 support orbit: CLOSED_BY_KNOWN_CONIC
all 14-node full-span uniform rays: OPEN
retained 44 low-degree test curves: INSUFFICIENT POPULATION-WIDE
```

A useful next P6 gate must attack the new full-span survivor by information not contained in this 44-curve library:

- a larger exact effective/test-curve cone;
- a support-specific symmetric-differential/global incidence obstruction;
- a global singularity/conductor restriction;
- or another population-wide invariant.

Do not infer existence from Riemann--Roch effectivity.

## Source locks

Historical archive exact head:

```
ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11
```

Load-bearing blobs:

- formal family certificate `8ec4a403d2485dbf061b8b16182aa06c62193c43`;
- formal Picard certificate `32a01bc272f14eca3e8ba3229f021f4140ab7260`;
- global effectivity certificate `7bef88be7a8a81bbcf022ef9fea4834c2dc2da39`;
- known-conic certificate `b425ba24932632d28752899c6ad11cd530c7de6c`;
- Aut(S) node-action source note `cbe21fdbacb975a726d0c2c8a1ab8fd3b21d0693`;
- section-component certificate `9c36555e495df0d8d6b816f1c0dc7d4c35b55848`;
- known-conic/balanced quotient certificate `f63d08b9005762a02935a727f35e6581ae52aaab`.

## Credit firewall

```
finite_degree_window_proved=false
MB104_complete=false
R29_LG2_MB_discharged=false
receiver_credit=false
effectivity_final_milestone_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
