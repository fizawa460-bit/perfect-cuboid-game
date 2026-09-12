# Stage32 MB104 genus-one span-five section components: incidence 20, 19, 16

Status: **RETAINED EXACT COMPONENT CLASSIFICATION FOR INCIDENCE 20/19/16 / HIGH-DEGREE GENUS-ONE CARRIERS CLOSED ON THESE ORBITS / SPAN-5 STILL OPEN / NO DOWNSTREAM CREDIT**

This checkpoint continues `MB104-GENUS1-SPAN5-SECTION-COMPONENTS-INC20-DOWN` from the exact 12-orbit ambient-hyperplane classification. The direct `R8<d/4+O(1)` route remains frozen by `PRIORITY-OVERRIDE-20260912.json`.

## Surface model

Use homogeneous coordinates

```text
(a1,a2,a3,b1,b2,b3,c)
```

and the four cuboid quadrics

```text
q1 = a1^2+a2^2-b3^2,
q2 = a2^2+a3^2-b1^2,
q3 = a1^2+a3^2-b2^2,
q4 = a1^2+a2^2+a3^2-c^2.
```

The retained ambient quotient has one incidence-20 orbit, one incidence-19 orbit, and two incidence-16 orbits of sizes `3` and `24`. Exact representatives are recovered from the retained 48-node `Q(i)` model and checked against the orbit support masks.

## Incidence 20: one orbit of size 48

Representative support mask:

```text
0000ff33330f
```

Representative hyperplane:

```text
H20: c=a1+b1.
```

On `H20`,

```text
q4-q2 = -2 a1 b1.
```

Hence the section splits into the `a1=0` and `b1=0` branches.

On `a1=0`, one has `c=b1` and

```text
q1=(a2-b3)(a2+b3),
q3=(a3-b2)(a3+b2),
q4=q2.
```

This gives four smooth conics

```text
a1=0,
c=b1,
b3=epsilon a2,
b2=delta a3,
b1^2=a2^2+a3^2,
```

for `epsilon,delta in {+1,-1}`.

On `b1=0`, one has `c=a1` and

```text
q2=(a2+i a3)(a2-i a3),
q4=q2.
```

For each sign `a2=+/- i a3`, the remaining equations are projectively equivalent to

```text
x^2-y^2-w^2=0,
x^2+y^2-z^2=0
```

in `P^3`. The associated pencil has four distinct singular members, so each complete intersection is a smooth genus-one quartic.

Therefore

```text
S intersect H20
= 4 smooth conics + 2 smooth elliptic quartics,
```

all reduced, with total degree `4*2+2*4=16`.

Exact node replay gives six nodes on each conic, eight nodes on each elliptic quartic, and every one of the 20 section nodes lies on exactly two reduced components.

## Incidence 19: one orbit of size 48

Representative support mask:

```text
003c3c163333
```

Representative hyperplane:

```text
H19: c=a3+b1+b2.
```

On `H19`,

```text
q2+q3-q4 = 2(a3+b1)(a3+b2).
```

On the branch `a3+b1=0`, one has `c=b2` and

```text
q2=a2^2,
q4=q2+q3.
```

The reduced support has `a2=0`, and then

```text
q1=(a1-b3)(a1+b3).
```

Thus this branch consists of two smooth conics, each with generic scheme multiplicity two coming from `a2^2`.

Similarly, on `a3+b2=0`, one has `c=b1`, `q3=a1^2`, and the reduced support `a1=0` splits through

```text
q1=(a2-b3)(a2+b3),
```

again giving two smooth conics, each with generic scheme multiplicity two.

Therefore the full section has reduced support equal to four smooth conics, each doubled scheme-theoretically:

```text
S intersect H19 = 2 Q1 + 2 Q2 + 2 Q3 + 2 Q4,
```

with total degree `4*(2*2)=16`.

The 19 box nodes on the section meet the reduced conics with incidence distribution

```text
16 nodes on 1 reduced component,
2 nodes on 2 reduced components,
1 node on all 4 reduced components.
```

There is no irreducible genus-one component in this orbit.

## Incidence 16, size-3 orbit

Representative support mask:

```text
0000ff0000ff
```

Representative hyperplane:

```text
H16a: b1=0.
```

Then

```text
q2=(a2+i a3)(a2-i a3),
q4-q2=(a1-c)(a1+c).
```

Choosing one factor from each product yields four components

```text
b1=0,
a2=epsilon i a3,
c=delta a1,
q1=q3=0,
```

with `epsilon,delta in {+1,-1}`.

Each is projectively equivalent to the same smooth `(2,2)` complete intersection in `P^3` used above, hence is a smooth genus-one quartic. Thus

```text
S intersect H16a = 4 smooth elliptic quartics
```

and the section is reduced of total degree `4*4=16`. Each quartic contains eight of the 16 section nodes, and every section node lies on exactly two components.

## Incidence 16, size-24 orbit

Representative support mask:

```text
000f0f000f0f
```

Representative hyperplane:

```text
H16b: c=a1+a2+i a3.
```

On `H16b`,

```text
q4 = -2(a1+i a3)(a2+i a3).
```

On `a1+i a3=0`, one has `c=a2` and

```text
q3=-b2^2.
```

The reduced support is `b2=0`, and the remaining `q1,q2` form a smooth elliptic quartic. The square `b2^2` gives generic scheme multiplicity two.

On `a2+i a3=0`, one has `c=a1` and

```text
q2=-b1^2,
```

and the reduced support `b1=0` is another smooth elliptic quartic, again with generic scheme multiplicity two.

Therefore

```text
S intersect H16b = 2 E1 + 2 E2,
```

where `E1,E2` are smooth elliptic quartics. Total degree is `2*(2*4)=16`. The 16 section nodes split as eight on `E1` and eight on `E2`.

## Consequence for genus-one span-five carriers

Let `C` be an irreducible curve on the cuboid surface whose projective span is one of these ambient `P^5` hyperplanes. Since `C` is contained in the one-dimensional hyperplane section `S intersect H`, it must be one of the reduced irreducible section components.

Hence, on every incidence-20, incidence-19, or incidence-16 ambient orbit:

```text
any irreducible genus-one component has degree 4,
```

and the incidence-19 orbit has no genus-one component at all.

Therefore these four ambient orbits cannot support the unbounded genus-one span-five families under investigation. This conclusion is stronger than the earlier uniform-ray fixed-component obstruction: it does not assume equal exceptional coefficients or a particular Picard ray.

Combined with the retained incidence-24 classification, all ambient orbits of incidence `>=16` are now closed for the potentially infinite genus-one span-five sector.

## Exact verifier

`verify_mb104_genus1_span5_sections_20_19_16.py` checks:

- the exact factor identities above over `Z[i]`;
- the four retained representative support masks on the exact 48-node model;
- conic/quartic component node incidences;
- smoothness of the elliptic quartic normal form via four distinct singular members in its quadric pencil;
- scheme multiplicity-two branches for incidence 19 and the size-24 incidence-16 orbit;
- degree-16 accounting for every section.

Local replay:

```text
PASS STAGE32_MB104_GENUS1_SPAN5_SECTIONS_20_19_16_V1
inc20=4_smooth_conics_plus_2_smooth_elliptic_quartics reduced degree16 node_component_mult=2
inc19=4_smooth_conics_each_scheme_multiplicity2 degree16 reduced_node_incidence=16x1,2x2,1x4
inc16_orbit3=4_smooth_elliptic_quartics degree16 node_component_mult=2
inc16_orbit24=2_smooth_elliptic_quartics_each_scheme_multiplicity2 degree16 nodes_split_8_plus_8
irreducible_genus1_component_degree_cap=4 for incidence 20,19,16 ambient orbits
```

No exact-head CI claim is made for this local verifier.

## Next load-bearing leaf

Only the lower-incidence ambient orbits remain in the genus-one span-five component route:

1. incidence 15 orbit, size 256;
2. incidence 14 orbits, sizes 96, 192, 192, 384, 384.

Classify their scheme-theoretic hyperplane sections. If they are irreducible canonical sections of genus greater than one, that alone excludes them as genus-one carriers; if reducible, classify only enough components to bound or exclude irreducible genus-one members.

Keep genus-one span-six and genus-zero full-span routes open in parallel.

## Firewalls

- this closes only incidence 20/19/16 ambient orbits for irreducible genus-one span-five carriers;
- incidence 15 and 14 remain open;
- no claim is made about arbitrary reducible divisors inside the same hyperplanes;
- no population-wide finite degree window for all MB104 sectors is proved;
- MB104 remains incomplete and MB105 remains gated;
- no receiver/effectivity-final/theorem/endpoint/Perfect-Cuboid credit;
- no merge authorization.
