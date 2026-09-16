# Stage32 MB104 genus-one span-five section components: incidence 20, 19, 16

Status: **RETAINED EXACT SECTION-COMPONENT CLASSIFICATION / SUPPORT-SPAN SEMANTICS REPAIRED / FIXED-COMPONENT INPUT ONLY / SPAN-5 OPEN / NO CREDIT**

This checkpoint continues `MB104-GENUS1-SPAN5-SECTION-COMPONENTS-INC20-DOWN` from the exact 12-orbit ambient-hyperplane classification.

## Critical scope

Here `span 5` means the **box-node support** `Sigma` of the unknown carrier spans a unique ambient hyperplane `H=P^5`. It does **not** imply that the carrier curve itself lies in `H`.

Therefore the component geometry of `S intersect H` cannot by itself bound the degree of the unknown carrier or identify it with a section component. The valid use of these components is as explicit effective test curves for Picard/intersection/fixed-component arguments.

## Surface model

Coordinates are `(a1,a2,a3,b1,b2,b3,c)` and

```text
q1=a1^2+a2^2-b3^2,
q2=a2^2+a3^2-b1^2,
q3=a1^2+a3^2-b2^2,
q4=a1^2+a2^2+a3^2-c^2.
```

## Incidence 20, orbit size 48

Representative support mask `0000ff33330f`, hyperplane

```text
H20: c=a1+b1.
```

Since `q4-q2=-2 a1 b1`, the section splits into the `a1=0` and `b1=0` branches. Exact factorization gives

```text
S intersect H20 = 4 smooth conics + 2 smooth elliptic quartics,
```

reduced of total degree 16. Exact node replay gives 6 nodes on each conic, 8 on each elliptic quartic, and every one of the 20 section nodes lies on exactly two reduced components.

## Incidence 19, orbit size 48

Representative support mask `003c3c163333`, hyperplane

```text
H19: c=a3+b1+b2.
```

Since

```text
q2+q3-q4=2(a3+b1)(a3+b2),
```

the reduced support consists of four smooth conics, each with generic scheme multiplicity two:

```text
S intersect H19 = 2Q1+2Q2+2Q3+2Q4.
```

The 19 section nodes meet the reduced conics with incidence distribution `16x1, 2x2, 1x4`.

## Incidence 16, size-3 orbit

Representative support mask `0000ff0000ff`, hyperplane

```text
H16a: b1=0.
```

Using

```text
q2=(a2+i a3)(a2-i a3),
q4-q2=(a1-c)(a1+c),
```

the section is four smooth elliptic quartics, reduced of total degree 16. Each quartic contains 8 of the 16 section nodes and every section node lies on exactly two quartics.

## Incidence 16, size-24 orbit

Representative support mask `000f0f000f0f`, hyperplane

```text
H16b: c=a1+a2+i a3.
```

Since

```text
q4=-2(a1+i a3)(a2+i a3),
```

the reduced support consists of two disjoint-node-support smooth elliptic quartics, each with generic scheme multiplicity two:

```text
S intersect H16b = 2E1+2E2.
```

Each reduced elliptic quartic contains exactly 8 of the 16 section nodes.

## Correct retained consequence

These exact section decompositions are retained as **test-curve geometry**. They do not close the corresponding support-span orbits by themselves.

For an integral Picard class

```text
D=aH-sum_i b_i E_i,
```

and a section component `Q` of degree `e=H.Q` meeting supported nodes `T_Q` transversely once, the exact pairing is

```text
D.Q = a e - sum_{i in T_Q} b_i.
```

For the displayed genus-one uniform Picard ray

```text
D_l = 7l H - 4l sum_{i in Sigma} E_i,
```

this becomes

```text
D_l.Q = l(7e-4 n_Q),
```

where `n_Q=|Sigma intersect T_Q|`. A negative pairing forces `Q` as a fixed component and therefore excludes an irreducible effective member of that ray.

The separate `GENUS1-SPAN5-UNIFORM-RAY-COMPONENT-CAPACITY` checkpoint applies this correctly to incidence 24/20/19/16.

## Verification

`verify_mb104_genus1_span5_sections_20_19_16.py` checks the exact Gaussian factor identities, representative support masks, node/component incidences, elliptic-quartic smoothness, multiplicities and degree accounting.

Local replay token:

```text
PASS STAGE32_MB104_GENUS1_SPAN5_SECTIONS_20_19_16_V1
```

No exact-head CI claim is made.

## Firewalls

- support-span `P^5` does not imply the unknown carrier is contained in that `P^5`;
- section-component degree is not a carrier-degree bound;
- the component geometry is valid input only for explicit intersection/fixed-component arguments;
- incidence 15 and 14 section geometry remains open;
- genus-one span-six and genus-zero full-span remain open;
- no population-wide finite degree window, receiver, theorem, endpoint or Perfect-Cuboid credit;
- no merge authorization.
