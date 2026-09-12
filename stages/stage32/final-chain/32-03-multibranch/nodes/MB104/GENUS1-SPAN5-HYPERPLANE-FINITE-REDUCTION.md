# Stage32 MB104 genus-one span-five hyperplane finite reduction

Status: **RETAINED FINITE AMBIENT-HYPERPLANE REDUCTION / SPAN-5 NOT CLOSED / MB104 INCOMPLETE / NO CREDIT**

This note is read under `PRIORITY-OVERRIDE-20260912.json`. It addresses the reprioritized global-classification route and does not reopen the frozen direct `R8<d/4+O(1)` route.

## Scope bridge

The retained BTVA low-support theorem gives

```text
potentially infinite genus-0/1 multibranch population => N>=14,
```

where `N` counts distinct box nodes met by the curve. The retained span reduction says the only genus-one hard sectors are support-span dimensions `5` and `6`.

If a genus-one support `Sigma` has projective span dimension exactly `5`, then `Span(Sigma)` is a unique projective hyperplane `P^5` in the ambient `P^6`. Since the potentially infinite sector has `N>=14`, that ambient hyperplane contains at least 14 of the 48 box nodes.

Thus the span-five problem first reduces to the exact finite question:

> Which hyperplanes in `P^6` contain at least 14 of the 48 box nodes?

The answer below is exact and finite: **1,655 ambient hyperplanes**.

## Exact 48-node model

Coordinates are ordered as

```text
[a1,a2,a3,b1,b2,b3,c].
```

The verifier builds the 48 nodes over `Q(i)` in two canonical families.

Type A (`c=1`, 24 nodes): choose one index `j`; set `a_j=+-1`, the other two `a` coordinates to zero, `b_j=0`, and the other two `b` coordinates independently to `+-1`.

Type B (`c=0`, 24 nodes): choose one zero pair `a_j=b_j=0`; on the remaining two indices normalize the first nonzero `a` coordinate to `1`, the second to `+-i`, and choose independently the two signs in the corresponding `b=+-i*a` relations.

The displayed `F1-P5` support from the earlier formal-family certificate lies in the Type-B hyperplane `c=0`.

## Exhaustive two-prime enumeration

For each of the two good primes

```text
p1=1097, i=341 mod p1,
p2=1153, i=140 mod p2,
```

the verifier enumerates all

```text
C(48,6)=12,271,512
```

six-node subsets. Whenever the six rows have rank six, it computes the unique projective kernel normal, normalizes it canonically, and deduplicates the resulting hyperplanes.

Both primes independently give exactly `593,735` distinct modular hyperplanes and the same node-incidence distribution:

```text
6:  372608
7:  114624
8:   61440
9:   32256
10:   8736
12:   1648
13:    768
14:   1248
15:    256
16:     27
19:     48
20:     48
24:     28
```

Hence the modular high-incidence count is

```text
1248+256+27+48+48+28 = 1655.
```

The low-incidence totals are diagnostic only; the load-bearing object for this leaf is the `>=14` sector.

## Exact `Q(i)` replay

Every modular candidate with at least 14 nodes is replayed exactly. From the stored six-node basis, the verifier forms the seven Gaussian-integer cofactors of the `6x7` matrix, obtaining an exact normal in `Z[i]^7`, and evaluates that normal on all 48 exact nodes.

For all 1,655 high-incidence candidates at both primes:

- the exact normal is nonzero;
- exact support equals modular support;
- no duplicate exact support remains;
- the exact support set obtained from `p1` is identical to that obtained from `p2`.

The exact high-incidence distribution is therefore

```text
14: 1248
15:  256
16:   27
19:   48
20:   48
24:   28
```

and the stable FNV64 digest of the sorted exact 48-bit support masks is

```text
ba8379b50029db53.
```

In particular `c=0`, containing exactly the 24 Type-B nodes, is one of the 28 incidence-24 hyperplanes.

## Completeness over characteristic zero

A true span-five support has six independent box nodes. Choose six such nodes and a nonzero `6x6` minor `Delta` of their Gaussian matrix. All entries have complex norm at most one, so Hadamard gives

```text
|Delta| <= 6^(6/2) = 216,
N_Q(i)/Q(Delta) <= 216^2 = 46,656.
```

If this exact rank-six basis dropped rank modulo both chosen primes, then both rational primes would divide the Gaussian norm of `Delta`. But

```text
1097*1153 = 1,264,841 > 46,656,
```

which is impossible for nonzero `Delta`.

Therefore every characteristic-zero node-spanned hyperplane is detected by at least one of the two finite-field enumerations. If it contains at least 14 box nodes it enters the high-incidence replay, where all candidates were verified exactly and the two exact sets coincide.

Thus the list of 1,655 ambient hyperplanes is complete over `Q(i)`.

## Retained reduction

Combining the BTVA inputs with the exact enumeration gives

```text
potentially infinite genus-one span-5 carrier
=> N>=14
=> its node support spans a unique P5 hyperplane
=> that P5 contains >=14 box nodes
=> that P5 is one of exactly 1,655 exact ambient hyperplanes.
```

This is a finite global classification reduction. It is **not** yet a classification of all possible support subsets inside those hyperplanes. An actual support may be a spanning subset of the node set of one of the 1,655 ambient `P^5`s.

## Relation to the displayed `c=0` ray

The retained `GLOBAL-EFFECTIVITY-P5-CONIC-OBSTRUCTION` already excludes the displayed `F1-P5-PIC` ray from having an irreducible effective member: in the `c=0` section at least three of the eight conics occur as forced fixed components for that class.

The present finite reduction places that example inside a complete finite ambient list: `c=0` is one of the 28 incidence-24 candidates. No transport of the conic argument to the other 27 candidates is claimed here.

## Next load-bearing leaf

Classify the 1,655 ambient hyperplanes by exact `Aut(S)` orbit and by the component geometry of the corresponding surface section. The first target is the 28 incidence-24 candidates: determine whether they form one or more `Aut(S)` orbits and whether the `c=0` fixed-component argument transports orbitwise. Then descend through incidences 20, 19, 16, 15, and 14.

## Verification

`verify_mb104_genus1_span5_hyperplane_finite_reduction.cpp` performs the exhaustive two-prime enumeration and exact Gaussian replay. The Python wrapper source-locks the current MB101, BTVA low-support, BTVA span, P5 conic obstruction, and C++ verifier blobs before compiling and running it.

Local replay result:

```text
PASS STAGE32_MB104_GENUS1_SPAN5_HYPERPLANE_FINITE_REDUCTION_V1
nodes=48 p1=1097 i1=341 p2=1153 i2=140
distinct_mod_hyperplanes_per_prime=593735 exact_high_incidence_hyperplanes=1655
high_distribution=14:1248,15:256,16:27,19:48,20:48,24:28
exact_support_fnv64=ba8379b50029db53 hadamard_norm_bound=46656 prime_product=1264841
scope=genus1_span5_N_ge_14_supports_finitely_reduced_not_closed
```

No exact-head CI claim is made by this note.

## Firewalls

- the whole genus-one span-five sector is **not** closed;
- 1,655 counts ambient hyperplanes, not all support subsets;
- no claim is made that the 28 incidence-24 hyperplanes form one automorphism orbit;
- no genus-one span-six or genus-zero full-span closure is claimed;
- no finite population-wide degree window is proved;
- MB104 remains incomplete and MB105 remains gated;
- no receiver/effectivity-final/theorem/endpoint/Perfect-Cuboid credit;
- no merge authorization.
