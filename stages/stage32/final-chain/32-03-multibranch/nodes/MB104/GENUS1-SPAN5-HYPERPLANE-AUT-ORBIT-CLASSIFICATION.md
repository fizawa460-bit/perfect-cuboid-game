# Stage32 MB104 genus-one span-five `Aut(S)` orbit classification

Status: **RETAINED EXACT ORBIT CLASSIFICATION / INCIDENCE-24 COMPONENT GEOMETRY CLOSED / WHOLE SPAN-5 OPEN / NO CREDIT**

This checkpoint continues `MB104-GENUS1-SPAN5-HYPERPLANE-COMPONENT-CLASSIFICATION` under `PRIORITY-OVERRIDE-20260912.json`. It does not reopen the frozen direct `R8<d/4+O(1)` route.

## Input population

The preceding finite-reduction certificate proves that every potentially infinite genus-one support of projective span dimension exactly five lies in one of exactly `1,655` characteristic-zero node-spanned ambient hyperplanes containing at least 14 of the 48 box nodes. Their exact node-incidence distribution is

```text
14: 1248
15:  256
16:   27
19:   48
20:   48
24:   28
```

with exact support digest `ba8379b50029db53`.

## Exact automorphism action

The current verifier rebuilds the same exact 48-node `Q(i)` model and applies the nine coordinate substitutions from the immutable Stoll verification source locked in `AUTS-NODE-ACTION-SOURCE-NOTE.md`.

The induced projective permutations of the 48 nodes generate a group of order

```text
1536,
```

matching `Aut(S)` in the immutable source and the retained MB103 semantic quotient contract.

The verifier re-enumerates the high-incidence hyperplanes over `p=1097`, checks the retained exact-support digest, and then computes their complete orbits under this 48-node action.

## Complete orbit decomposition of the 1,655 ambient P5s

There are exactly **12 `Aut(S)` orbits**:

```text
incidence 14: 5 orbits, sizes 96, 192, 192, 384, 384
incidence 15: 1 orbit,  size 256
incidence 16: 2 orbits, sizes 3, 24
incidence 19: 1 orbit,  size 48
incidence 20: 1 orbit,  size 48
incidence 24: 2 orbits, sizes 4, 24
```

The orbit-size sums reproduce each exact incidence count and total `1,655`.

This is the complete ambient-hyperplane quotient for the hard genus-one span-five sector. It is not yet a classification of all possible support subsets or divisor classes inside each ambient hyperplane.

## Incidence-24 sector: two orbits, not one

The 28 incidence-24 hyperplanes split as

```text
4 + 24.
```

The size-4 orbit contains `c=0`; an equivalent exact representative in the verifier's node ordering is the support of `a1=0`.

The size-24 orbit has exact representative support mask

```text
0x005a5affa5a5
```

and exact hyperplane representative

```text
a1 + a2 - b3 = 0.
```

Thus the earlier possibility that all 28 incidence-24 hyperplanes form one `Aut(S)` orbit is false.

## Component geometry of the size-4 orbit

The retained Stoll/canonical-section source lock used by `GLOBAL-EFFECTIVITY-P5-CONIC-OBSTRUCTION` gives that `c=0` cuts the surface into eight smooth conics, and each `c=0` box node lies on exactly two of those conics.

Automorphism transport therefore gives the same eight-conic section geometry and node-incidence pattern for all four hyperplanes in this orbit.

## Component geometry of the size-24 orbit

Let

```text
H2 : b3 = a1 + a2.
```

Write the surface quadrics as

```text
q1 = a1^2+a2^2-b3^2,
q2 = a2^2+a3^2-b1^2,
q3 = a1^2+a3^2-b2^2,
q4 = a1^2+a2^2+a3^2-c^2.
```

On `H2`,

```text
q1 = -2 a1 a2,
```

so the hyperplane section splits between `a1=0` and `a2=0`.

On `a1=0`, one has

```text
b3=a2,
q3=(a3-b2)(a3+b2),
q4-q2=(b1-c)(b1+c).
```

Hence this half splits into four plane conics indexed by `epsilon,delta in {+1,-1}`:

```text
a1=0,
b3=a2,
b2=epsilon*a3,
c=delta*b1,
b1^2=a2^2+a3^2.
```

On `a2=0`, similarly

```text
b3=a1,
q2=(a3-b1)(a3+b1),
q4-q3=(b2-c)(b2+c),
```

and one obtains four plane conics

```text
a2=0,
b3=a1,
b1=epsilon*a3,
c=delta*b2,
b2^2=a1^2+a3^2.
```

All eight are smooth conics. The verifier checks on the exact 48-node model that each of these conics contains exactly six of the 24 nodes on `H2`, and every one of those 24 nodes lies on exactly two of the eight conics.

Automorphism transport gives the same component geometry for the full size-24 orbit.

Therefore **all 28 incidence-24 hyperplane sections are unions of eight smooth conics, with each of their 24 box nodes lying on exactly two section conics**.

## Uniform-ray consequence

This closes a larger class than the single displayed `c=0` example, but not the whole span-five sector.

Let `H` be any of the 28 incidence-24 hyperplanes and let `S` be any subset of at least 14 of its box nodes. For the uniform Picard ray

```text
D_l = 7l H_S - 4l sum_{i in S} E_i,   l>=1,
```

where `H_S` denotes the ambient hyperplane class on the resolution, count support incidences with the eight section conics. Each supported node lies on two conics, so the total incidence is at least `28`. Hence some section conic `Q` contains at least four supported nodes.

Using the retained strict-transform pairings

```text
H_S.Q = 2,
E_i.Q = 1  if node i lies on Q,
```

one gets

```text
D_l.Q = 14l - 4l*n_Q <= -2l < 0.
```

Thus every effective member of this uniform ray contains `Q` as a fixed component and cannot be irreducible.

In particular, the fixed-component obstruction is not special to the one displayed `c=0` support: it excludes every uniform `7lH-4l sum E_i` ray supported on at least 14 nodes inside any incidence-24 hyperplane.

This statement does **not** apply to arbitrary Picard classes, arbitrary unequal exceptional coefficients, or arbitrary genus-one carriers in the same hyperplane.

## Exact verifier output

Local replay:

```text
group=1536
hyp=593735
hi=1655 dist 14:1248 15:256 16:27 19:48 20:48 24:28
orbit_summary
14 count=5 sizes=96,192,192,384,384,
15 count=1 sizes=256,
16 count=2 sizes=3,24,
19 count=1 sizes=48,
20 count=1 sizes=48,
24 count=2 sizes=4,24,
c0_orbit_size=4
inc24_orbits
rep=0000ffffff00 size=4 contains_c0=1
rep=005a5affa5a5 size=24 contains_c0=0
PASS STAGE32_MB104_GENUS1_SPAN5_HYPERPLANE_AUT_ORBITS_V1
aut_group_order=1536 high_hyperplanes=1655 aut_orbits=12
orbit_sizes=14:[96,192,192,384,384];15:[256];16:[3,24];19:[48];20:[48];24:[4,24]
incidence24=two_orbits_4_plus_24 second_rep=a1+a2-b3 eight_conics_each_6_nodes_each_node_on_2
```

No exact-head CI claim is made for this new verifier.

## Next load-bearing leaf

The ambient `Aut(S)` quotient is now complete. Continue the component classification in descending incidence:

1. incidence 20 orbit (size 48);
2. incidence 19 orbit (size 48);
3. incidence 16 orbits (sizes 3 and 24);
4. incidence 15 orbit (size 256);
5. the five incidence-14 orbits.

For each representative, determine the scheme-theoretic component geometry of `S intersect H`, then test whether it yields a support/multiplicity obstruction for irreducible genus-one carriers. Keep the genus-one span-six and genus-zero full-span routes open in parallel.

## Firewalls

- `12` is the number of ambient-hyperplane `Aut(S)` orbits, not support-subset or divisor-class orbits;
- the incidence-24 eight-conic geometry is closed, but the whole span-five sector is not;
- the uniform-ray fixed-component argument does not cover arbitrary Picard classes or unequal node multiplicities;
- no finite population-wide degree window is proved;
- MB104 remains incomplete and MB105 remains gated;
- no receiver/effectivity-final/theorem/endpoint/Perfect-Cuboid credit;
- no merge authorization.
