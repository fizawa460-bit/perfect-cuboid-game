# Stage32 MB104 global-classification checkpoint

Status: **ACTIVE PRIORITY / DISPLAYED P5 RAY IRREDUCIBLY CLOSED / GENUS-ONE SPAN-5 FINITELY REDUCED TO 1,655 AMBIENT P5S / P6 OPEN / NO CREDIT**

This checkpoint is read under `PRIORITY-OVERRIDE-20260912.json`. It supersedes the older MB104 checkpoint only for research ordering. The retained direct inequality

```text
d <= 16g-16+4R8
```

remains mathematically valid, but direct pursuit of `R8<d/4+O(1)` remains frozen until a genuinely new lever appears.

## Hard sectors

The priority population remains

```text
g=0: node support spans P^6;
g=1: node-support span dimension 5 or 6;
potentially infinite sector: N>=14.
```

## Formal-family and Picard status

The retained formal packet families are

```text
F0-P6: d=28k-4,
F1-P5: d=28k,
F1-P6: d=28k,
N=14, R=R8=M=r_odd=28k.
```

Integral Picard subsequences exist:

```text
F0-P6-PIC: k=4l+3, D=(7l+5)H-(4l+3)sum_{S_P6}E_i;
F1-P5-PIC: k=4l,   D=7l H-4l sum_{S_P5}E_i;
F1-P6-PIC: k=4l,   D=7l H-4l sum_{S_P6}E_i.
```

The global effectivity checkpoint strengthened this further: Riemann--Roch with `K=H`, `chi(O_S)=8`, and `H` big and nef shows that **all three displayed Picard rays are effective** on their retained parameter ranges. Thus Picard integrality and bare effectivity are not the obstruction.

The adjunction defects remain

```text
F0: Delta_total=(21k^2+14k-1)/2,
F1: Delta_total=(21k^2+28k)/2.
```

so the open issue is irreducible low-genus carrier realization, not existence of an effective divisor class.

## Displayed genus-one P5 ray: irreducible effectivity closed

For the explicit `F1-P5-PIC` support in `c=0`, the canonical section `c=0` is a union of eight smooth conics. The exact node/conic incidence gives at least three conics `Q` with

```text
D.Q < 0.
```

Every effective divisor in this displayed class therefore contains those conics as fixed components. Hence this infinite P5 Picard ray has **no irreducible effective member**.

This closes the displayed P5 formal ray only; it does not by itself close all genus-one span-five supports.

## Entire genus-one span-five sector: finite ambient reduction

`GENUS1-SPAN5-HYPERPLANE-FINITE-REDUCTION` gives a complete characteristic-zero enumeration of node-spanned ambient `P^5` hyperplanes that can contain a potentially infinite genus-one span-five support.

Using two primes (`1097`, `1153`) plus exact Gaussian replay, the exact high-incidence distribution is

```text
14: 1248
15:  256
16:   27
19:   48
20:   48
24:   28
```

for a total of exactly

```text
1,655 ambient hyperplanes containing >=14 box nodes.
```

The two exact high-support sets agree and have digest

```text
ba8379b50029db53.
```

A Hadamard norm bound on a nonzero six-node minor, together with `1097*1153 > 216^2`, proves that no characteristic-zero rank-six hyperplane can evade both finite-field enumerations.

Therefore every potentially infinite genus-one span-five support lies inside one of these 1,655 exact ambient `P^5`s. This is an ambient-hyperplane reduction, not a claim that there are only 1,655 possible support subsets.

The `c=0` example is one of the 28 incidence-24 candidates.

## Routes exhausted for priority purposes

Do not spend the next mainbatch on:

- direct `R8<d/4` recombinations without a new external lever;
- fixed finite local jets;
- Picard integrality of the displayed formal rays;
- bare effectivity of those rays;
- already-retained Hodge/GFU/Beauville/rank-3 packet tests.

They remain valid inputs but do not close the surviving P6 sectors or the full span-five population.

## Next execution leaf

Priority is now the **finite global classification** of the 1,655 genus-one span-five ambient hyperplanes:

1. compute exact `Aut(S)` orbits of the 1,655 candidates;
2. start with the 28 incidence-24 hyperplanes and determine whether the `c=0` conic-section/fixed-component obstruction transports orbitwise;
3. classify surface-section components for the remaining incidence classes 20, 19, 16, 15, and 14;
4. for each ambient hyperplane, classify spanning support subsets only as far as needed to force reducibility, geometric genus `>=2`, or another finite obstruction;
5. in parallel, keep the genus-zero P6 and genus-one P6 irreducible-low-genus problem open.

A successful orbitwise component obstruction may close a positive fraction of the whole span-five sector at once. Do not assert a single incidence-24 orbit until independently verified on the current branch.

## Firewalls

- all three displayed Picard rays are effective, but only the displayed `c=0` P5 ray is currently proved to have no irreducible member;
- the whole genus-one span-five sector is not closed;
- the 1,655 count is for ambient hyperplanes, not support subsets;
- genus-one span-six and genus-zero full-span remain open;
- no finite population-wide degree window is proved;
- MB104 remains incomplete and MB105 remains gated;
- no receiver/effectivity-final/theorem/endpoint/Perfect-Cuboid credit;
- no merge authorization.
