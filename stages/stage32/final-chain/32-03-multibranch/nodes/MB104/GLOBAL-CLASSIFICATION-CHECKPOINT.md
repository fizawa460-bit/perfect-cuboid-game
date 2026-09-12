# Stage32 MB104 global-classification checkpoint

Status: **ACTIVE PRIORITY / GENUS-ONE SPAN-5 AMBIENT AUT QUOTIENT COMPLETE / INCIDENCE >=16 COMPONENT GEOMETRY CLOSED / P6 OPEN / NO CREDIT**

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

The exact support digest is `ba8379b50029db53`. The retained two-prime/Hadamard argument supplies completeness.

## Complete `Aut(S)` quotient

The `1,655` ambient hyperplanes form exactly **12 `Aut(S)` orbits**:

```text
incidence 14: 5 orbits, sizes 96, 192, 192, 384, 384
incidence 15: 1 orbit,  size 256
incidence 16: 2 orbits, sizes 3, 24
incidence 19: 1 orbit,  size 48
incidence 20: 1 orbit,  size 48
incidence 24: 2 orbits, sizes 4, 24
```

This completes the ambient-hyperplane quotient. It does not classify arbitrary support subsets or divisor classes.

## Incidence 24: closed

The two incidence-24 orbits have sizes `4` and `24`. Every section is a union of eight smooth conics. For the uniform ray `D_l=7lH-4l sum E_i` on any support subset of at least 14 section nodes, some conic has negative pairing and is fixed. More strongly for the present span-five component route, every irreducible component of the hyperplane section has genus zero and degree two, so an irreducible genus-one carrier cannot occur in either incidence-24 orbit.

## Incidence 20, 19, 16: exact component classification

`GENUS1-SPAN5-SECTION-COMPONENTS-20-19-16` gives exact representative factorizations and node replay.

### Incidence 20, orbit size 48

Representative:

```text
H20: c=a1+b1,
q4-q2=-2 a1 b1.
```

The section is

```text
4 smooth conics + 2 smooth elliptic quartics,
```

reduced of degree 16. Any irreducible genus-one component therefore has degree exactly 4.

### Incidence 19, orbit size 48

Representative:

```text
H19: c=a3+b1+b2,
q2+q3-q4=2(a3+b1)(a3+b2).
```

The reduced support consists of four smooth conics, each with generic scheme multiplicity two. Hence there is no irreducible genus-one component in this orbit.

### Incidence 16, orbit size 3

Representative:

```text
H16a: b1=0.
```

The section is four smooth elliptic quartics, reduced of degree 16. Any irreducible genus-one component has degree 4.

### Incidence 16, orbit size 24

Representative:

```text
H16b: c=a1+a2+i a3,
q4=-2(a1+i a3)(a2+i a3).
```

The reduced support consists of two smooth elliptic quartics, each with generic scheme multiplicity two. Any irreducible genus-one component again has degree 4.

## Consequence for the hard genus-one span-five sector

If an irreducible curve `C` spans an ambient hyperplane `H=P^5`, then `C` is contained in the one-dimensional section `S intersect H` and hence is one of its reduced irreducible components.

Therefore all incidence `24,20,19,16` ambient orbits are closed for **unbounded** genus-one span-five carriers. Incidence 20 and 16 permit genus-one components only in degree 4; incidence 24 and 19 permit none.

This conclusion does not use the equal-coefficient Picard-ray hypothesis.

## Routes exhausted for priority purposes

Do not spend the next mainbatch on:

- direct `R8<d/4` recombinations without a new external lever;
- fixed finite local jets;
- Picard integrality or bare effectivity of the displayed formal rays;
- re-enumerating the 1,655 ambient span-five hyperplanes;
- recomputing their `Aut(S)` orbit quotient;
- incidence 24/20/19/16 component geometry;
- already-retained Hodge/GFU/Beauville/rank-3 packet tests.

## Next execution leaf

Only lower incidence remains in the genus-one span-five component route:

1. incidence 15 orbit, size 256;
2. incidence 14 orbits, sizes 96, 192, 192, 384, 384.

For each representative, determine the scheme-theoretic hyperplane section. If the section is irreducible of genus greater than one, that directly excludes it as a genus-one carrier. If reducible, classify only enough components to bound or exclude irreducible genus-one members.

Keep genus-zero P6 and genus-one P6 irreducible-low-genus classification open in parallel.

## Firewalls

- the ambient span-five `Aut(S)` quotient is complete, but incidence 15/14 section geometry remains open;
- genus-one span-six and genus-zero full-span remain open;
- no population-wide finite degree window is proved for all MB104 sectors;
- MB104 remains incomplete and MB105 remains gated;
- no receiver/effectivity-final/theorem/endpoint/Perfect-Cuboid credit;
- no merge authorization.
