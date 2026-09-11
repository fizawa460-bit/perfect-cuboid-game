# Stage36 36-09ET — targeted template realization and T6-profile near-miss expansion

## Purpose

36-09ES proved six abstract labelled-Legendre templates `T1..T6`; matching one of them is a global sufficient condition for

```text
dim_F2 Sel^2(E_rho,p/Q)=2.
```

The ET task is not another blind Selmer scan. It first searches only for realizations of the already-proved six templates. If the coarse labelled/mod-8 profile matches a proved template but the directed Legendre bits do not, that row is retained as a finite **near-miss** and only that finite set is evaluated by the exact 36-09EP support matrix.

Entry authority is V272, whose repaired ES promotion replay passed on exact head `b017efc62d7c9a362da52fe0c1b351315ef8c95f`, CI `34360323530 / 102495334858`.

## Exact targeted domain

Scan all ordered primitive positive pairs

```text
1 <= a,b <= 2000,
a != b,
gcd(a,b)=1,
p=a/b.
```

There are exactly `2,433,174` ordered rows.

For each row form the 36-09EP labelled radical datum

```text
R(a,b)=(S_P,S_Q,S_D; q mod 8; epsilon_2; directed Legendre bits).
```

The first-stage realization filter uses only

```text
P/Q/D labels + q mod 8 + epsilon_2,
```

up to the global P/Q swap admitted by 36-09ES. It does **not** compute a Selmer rank.

The 36-09EK positive literal orbit

```text
{p,1/p,|c(p)|,1/|c(p)|},  c(p)=(p+1)/(p-1),
```

is used only as an exact bookkeeping reduction. The complete ordered domain is still the claimed domain.

## Six-template realization result

Exactly 44 ordered rows, forming 11 literal four-point orbits, have the same labelled/mod-8 vertex profile as one of the six ES templates.

Among them, exactly 24 rows are exact `T1..T6` directed-Legendre matches. They are precisely the already-known six four-point orbits. Therefore the `1..2000` box contains

```text
new exact realizations of T1..T6 = 0.
```

The remaining 20 rows form exactly five four-point near-miss orbits. All five have the coarse T6 vertex profile. Their canonical representatives are

```text
1/277,
1/333,
1/1323,
81/317,
134/863.
```

No other near-miss profile occurs in this domain.

## Targeted near-miss rank replay

Only these five near-miss representatives are passed to the already exact-green 36-09EP support matrix. The results are

```text
representative   canonical pattern hash                                               n   rank   Sel2 dim
1/277            de74adf6b206d460c3863a55f9ea306aac136fc36bc9d86bb20cbedb73ff36c7  10  18     2
1/333            f22028ff420881c6bf0379bf2aa4d9f6d0c91bec911f9348c18827b1e4d09921  10  18     2
1/1323           fa0099a7c51111569b06af3a6f74a678e4001ea590b4a88c8007bc73f21232ce  10  16     4
81/317           878b70e2136f234d743f7b79ad9bedcf49994dd0d4c6ebd3368567d4c504ecd1  10  16     4
134/863          1d016b4933622e66e1d3a4d83cb7fd349366d53abe67f72feccf77d86bad481b  10  18     2
```

Thus three new abstract maximal-rank patterns are discovered:

```text
T7 := pattern(1/277),
T8 := pattern(1/333),
T9 := pattern(134/863).
```

Each has an abstract support matrix of rank `18=2n-2`. By the already-proved EP/ES pattern theorem, an arbitrary primitive positive rational parameter matching any of T7, T8, or T9 has rho full-2 Selmer dimension two. This is a global sufficient condition; it is not a claim that T1..T9 exhaust all maximal-rank patterns.

The two rank-16 near-miss patterns are retained as negative controls and receive no Sel2-dimension-two credit.

## EH torsion conditions for the three new realization orbits

For `p=a/b`, put

```text
N=a^2-b^2,
d=ab,
h=N/d.
```

The 36-09EH rational 4-torsion obstruction is absent when neither `8h` nor `-8h` is a rational square. In the cleared integral test this is equivalent here to checking that neither `8Nd` nor `-8Nd` is an integer square.

For the three new representatives:

```text
1/277:   8Nd = -170029248,
1/333:   8Nd = -295405632,
134/863: 8Nd = -672400871568.
```

In each case both signs fail the square test.

For rational 3-torsion use the exact 36-09EH division polynomial. After clearing the parameter denominators as in 36-09EI, all three representatives have the same reduction modulo 5:

```text
psi_3(X) = 3 X^4 + 4 X^2 + 4  (mod 5).
```

Its values at `X=0,1,2,3,4` are

```text
4,1,3,3,1,
```

so it has no root modulo 5 and hence no rational root. Thus all three representatives satisfy the independent EH no-4/no-3 conditions.

By 36-09EK literal equality, the same fixed rho curve / retained-boundary exclusion transfers to every positive member of each four-point orbit. Therefore the new excluded parameter orbits are

```text
O(1/277) = {1/277, 138/139, 139/138, 277},
O(1/333) = {1/333, 166/167, 167/166, 333},
O(134/863) = {134/863, 729/997, 863/134, 997/729}.
```

These 12 parameters are disjoint from the existing exact 24-parameter registry. Hence ET raises the exact fixed-p exclusion registry count from

```text
24 -> 36.
```

## Deterministic scan certificate

The 11 coarse-profile orbit representatives, in increasing representative order, are encoded as

```text
representative,canonical_hash,Sel2_dim,status
```

with status in `T1..T6`, `NEW_MAX`, or `DEF4`. The SHA-256 of that exact newline-terminated table is

```text
a3b974818373c1d22601061f77d2f0c8ef494234849d517b484c624fa999429c.
```

The verifier reconstructs the arithmetic datum and the five near-miss ranks independently; it does not trust a stored list of Selmer answers.

## Next leaf

The five T6-profile near-misses differ only in directed Legendre data, while their ranks split `18,18,16,16,18`. This isolates the next exact problem:

```text
36-09EU_RHO_T6_PROFILE_LEGENDRE_RIGIDITY_PREFLIGHT
```

Determine a symbolic bit/parity criterion on the T6 coarse profile that separates rank 18 from rank 16, potentially replacing individual T6/T7/T8/T9 hashes by one larger arithmetic family.

## Credit firewall

ET proves three additional global sufficient pattern templates and twelve additional fixed-p exclusions. It does **not** prove any of the following:

```text
T1..T9 exhaust all maximal-rank patterns,
uniform Sel2 dimension two for all rational p,
all positive rational p excluded,
candidate parameter set shrunk in the parent receiver,
receiver emptiness,
R29-CAMP2 closure,
Q11-CAMPEDELLI closure,
endpoint closure,
Perfect Cuboid nonexistence.
```
