# Stage32 MB104 global-classification checkpoint

Status: **ACTIVE PRIORITY / GENUS-ONE SPAN-5 AMBIENT AUT QUOTIENT COMPLETE / INCIDENCE-24 COMPONENT GEOMETRY CLOSED / P6 OPEN / NO CREDIT**

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

## Formal-family / Picard / effectivity status

The retained formal packet families are

```text
F0-P6: d=28k-4,
F1-P5: d=28k,
F1-P6: d=28k,
N=14, R=R8=M=r_odd=28k.
```

Integral Picard subsequences exist, and Riemann--Roch with `K=H`, `chi(O_S)=8`, and `H` big and nef shows all three displayed Picard rays are effective. Therefore Picard integrality and bare effectivity are not the obstruction.

The displayed `c=0` genus-one P5 ray remains irreducibly excluded by conic fixed components.

## Genus-one span-five ambient reduction

The potentially infinite span-five sector was reduced exactly to `1,655` characteristic-zero node-spanned ambient `P^5` hyperplanes containing at least 14 of the 48 box nodes:

```text
14: 1248
15:  256
16:   27
19:   48
20:   48
24:   28
```

The exact support digest is

```text
ba8379b50029db53.
```

The two-prime/Hadamard argument in `GENUS1-SPAN5-HYPERPLANE-FINITE-REDUCTION` remains the completeness firewall.

## New: complete `Aut(S)` quotient of all 1,655 ambient P5s

`GENUS1-SPAN5-HYPERPLANE-AUT-ORBIT-CLASSIFICATION` rebuilds the exact 48-node action from the nine immutable Stoll automorphism substitutions and verifies that the generated node-permutation group has order `1536`.

The `1,655` ambient hyperplanes form exactly **12 `Aut(S)` orbits**:

```text
incidence 14: 5 orbits, sizes 96, 192, 192, 384, 384
incidence 15: 1 orbit,  size 256
incidence 16: 2 orbits, sizes 3, 24
incidence 19: 1 orbit,  size 48
incidence 20: 1 orbit,  size 48
incidence 24: 2 orbits, sizes 4, 24
```

This completes the **ambient-hyperplane** quotient. It does not classify all support subsets or divisor classes inside those hyperplanes.

## Incidence-24 component geometry: closed

The 28 incidence-24 hyperplanes do **not** form one automorphism orbit. They split as

```text
4 + 24.
```

The size-4 orbit contains `c=0`, whose section is the retained union of eight smooth conics.

A size-24 representative is

```text
a1+a2-b3=0.
```

On this hyperplane the first surface quadric becomes `-2a1a2`, and direct factorization splits the section into four smooth conics in `a1=0` and four smooth conics in `a2=0`. Exact node replay shows each conic contains six of the 24 section nodes and every section node lies on exactly two conics.

Automorphism transport therefore proves:

```text
all 28 incidence-24 hyperplane sections
= unions of eight smooth conics,
each of the 24 box nodes lying on exactly two section conics.
```

## Uniform incidence-24 rays: irreducibly excluded

For any incidence-24 hyperplane, any support subset `S` of at least 14 of its nodes, and the uniform ray

```text
D_l = 7l H - 4l sum_{i in S} E_i, l>=1,
```

the eight-conic incidence gives some conic through at least four supported nodes. Hence

```text
D_l.Q = 14l - 4l*n_Q <= -2l < 0.
```

Every effective member therefore has a conic fixed component and cannot be irreducible.

This strictly generalizes the one displayed `c=0` example, but it does not cover arbitrary Picard classes or unequal exceptional coefficients and does not close the whole genus-one span-five sector.

## Routes exhausted for priority purposes

Do not spend the next mainbatch on:

- direct `R8<d/4` recombinations without a new external lever;
- fixed finite local jets;
- Picard integrality or bare effectivity of the displayed formal rays;
- re-enumerating the 1,655 ambient span-five hyperplanes;
- recomputing their `Aut(S)` orbit quotient;
- already-retained Hodge/GFU/Beauville/rank-3 packet tests.

## Next execution leaf

The ambient quotient is complete. Continue the **surface-section component classification** in descending incidence:

1. incidence 20 orbit (size 48);
2. incidence 19 orbit (size 48);
3. incidence 16 orbits (sizes 3 and 24);
4. incidence 15 orbit (size 256);
5. the five incidence-14 orbits.

For each representative, determine the scheme-theoretic component geometry of `S intersect H`, then test whether the section yields a support/multiplicity obstruction for irreducible genus-one carriers. Only classify support subsets as far as needed for a genuine reducibility/genus/finite obstruction.

Keep genus-zero P6 and genus-one P6 irreducible-low-genus classification open in parallel.

## Firewalls

- the ambient span-five `Aut(S)` quotient is complete, but support-subset/divisor-class classification is not;
- incidence-24 component geometry is closed, but the whole genus-one span-five sector is not;
- the uniform-ray obstruction does not cover arbitrary Picard classes or unequal node multiplicities;
- genus-one span-six and genus-zero full-span remain open;
- no finite population-wide degree window is proved;
- MB104 remains incomplete and MB105 remains gated;
- no receiver/effectivity-final/theorem/endpoint/Perfect-Cuboid credit;
- no merge authorization.
