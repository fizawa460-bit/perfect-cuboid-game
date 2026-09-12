# Stage32 MB104 global-classification checkpoint

Status: **ACTIVE PRIORITY / PICARD INTEGRALITY SURVIVES / EFFECTIVITY AND ACTUAL CARRIER OPEN / NO CREDIT**

This checkpoint is read under `PRIORITY-OVERRIDE-20260912.json`. It supersedes the older MB104 checkpoint only for research ordering. The retained direct inequality

```text
d <= 16g-16+4R8
```

remains mathematically valid, but direct pursuit of `R8<d/4+O(1)` is frozen until a genuinely new lever appears.

## Hard sectors

The priority population remains

```text
g=0: node support spans P^6;
g=1: node-support span dimension 5 or 6;
potentially infinite sector: N>=14.
```

## Formal-family status

`FORMAL-INFINITE-FAMILY-FEASIBILITY` retained three unbounded packet families satisfying the currently enumerated MB104 local/numerical/global necessary constraints:

```text
F0-P6: d=28k-4,
F1-P5: d=28k,
F1-P6: d=28k,
N=14, R=R8=M=r_odd=28k.
```

Those packets did not claim a Picard class or actual curve.

## Picard-realizability strengthening

`FORMAL-INFINITE-FAMILY-PICARD-REALIZABILITY` now shows that the same degree/contact/support skeleton survives the integral Picard lattice on infinite arithmetic subsequences.

For a retained 14-node support `S14`, use

```text
D=aH-k sum_{i in S14} E_i.
```

Since `H^2=16`, `H.E_i=0`, `E_i^2=-2`, this gives `H.D=16a` and supported exceptional intersections `E_i.D=2k`.

The explicit subsequences are:

```text
F0-P6-PIC:
  k=4l+3, l>=0,
  D=(7l+5)H-(4l+3)sum_{S_P6}E_i,
  d=112l+80.

F1-P5-PIC:
  k=4l, l>=1,
  D=7l H-4l sum_{S_P5}E_i,
  d=112l.

F1-P6-PIC:
  k=4l, l>=1,
  D=7l H-4l sum_{S_P6}E_i,
  d=112l.
```

These are honest integral Picard classes. They are **not** asserted effective.

Fixing the class forces positive strict-transform genus defect by MB102 adjunction:

```text
F0: Delta_total=(21k^2+14k-1)/2,
F1: Delta_total=(21k^2+28k)/2.
```

The older packet's `Delta_total=0` is therefore not carried into the Picard deformation. MB102 permits off-exceptional defect, so the correct unresolved question is whether an actual effective irreducible member can realize this `Theta(k^2)` defect while its normalization has genus `0` or `1`.

## Routes now considered exhausted for priority purposes

Do not spend the next mainbatch on:

- direct `R8<d/4` recombinations without a new external lever;
- fixed finite local jets;
- Picard **integrality** of the displayed formal rays;
- the already-retained Hodge/GFU/Beauville/rank-3 packet tests.

They remain valid inputs, but none excludes the displayed infinite Picard subsequences.

## Next execution leaf

Priority is now:

1. test effectivity / nef-cone or effective-cone obstruction for the displayed classes/rays;
2. test whether an irreducible member with normalization genus `0/1` can realize the required `Delta_total=Theta(k^2)`;
3. use the full 28-fibration/incidence structure or another exact global classification invariant against the fixed P5/P6 14-node supports;
4. if one of the three rays is eliminated, separate the surviving sectors rather than forcing one uniform argument.

A proof that the displayed Picard classes are non-effective (eventually or identically), or that every effective member has geometric genus `>=2`, is load-bearing. Conversely, constructing effective members would also be load-bearing because it would identify a genuine obstruction to the intended low-genus classification strategy.

## Firewalls

- integral Picard classes exist only at the exact formal level asserted by the certificate;
- no effective divisor is produced;
- no irreducible carrier is produced;
- no actual genus-0 or genus-1 curve is produced;
- no finite degree window is proved;
- MB104 remains incomplete and MB105 remains gated;
- no receiver/effectivity/theorem/endpoint/Perfect-Cuboid credit;
- no merge authorization.
