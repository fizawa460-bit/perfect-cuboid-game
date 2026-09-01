# Stage34-02 — audited Route D with StageA2 successive factor-cover descent

Status: `ACTIVE_D2_STAGEA2_FACTOR_COVER_DESCENT`.

## Locked foundation

- Stage34-01 exact object/global population: hostile-audited CLOSED.
- Stage34-02 Route-D algebraic reduction: hostile-audited PASS on `d54ee6f0eda2814781301cc80ff11a47f92a8c24`.
- Exact direct cover, fourteen `d=1,2` split quartics, their seven common Jacobians, full MW bases, fourteen global Q-isomorphisms and exact receiver-x pullbacks remain locked.
- Earlier four-prime and fixed-quotient MW panels are retained as exact nonclosing diagnostics.

## StageA2 method import

Closed/audited StageA2 A2-4/A2-5 supplies an applicable method, not a family-specific theorem import:

```text
factor square condition
 -> finite exact squareclass covers
 -> elementary/local branch obstructions
 -> remaining reconstruction square as a genus-one quartic
 -> binary-quartic invariants / Jacobian
 -> complete pullback only when the auxiliary point set is complete.
```

StageA2's concrete rank-zero `15.a5` result is **not** imported.

## Common four-factor reconstruction template

For `q=a/b`, set

```text
A = aU+bV,
B = bU+aV.
```

For d=1:

```text
U=T^2-S^2,
V=2TS.
```

For d=2:

```text
U=2T^2-S^2,
V=2T^2-4TS+S^2.
```

The remaining matching-x square condition is

```text
U*V*A*B = square.
```

Writing

```text
U=delta1 R^2,
V=delta2 S^2,
A=delta3 M^2,
B=delta4 N^2
```

reduces the infinite problem to finitely many exact squareclass branches. Odd squareclass support is confined to primes dividing `2ab(a^2-b^2)`; the 2-adic pattern is separately locked.

Evidence:

- `d2-stageA2-weapon-applicability-lock.json`
- `d2-stageA2-style-reconstruction-factor-lock.json`
- `d2-stageA2-odd-squareclass-support-lock.json`
- `d2-stageA2-two-adic-pattern-lock.json`

## Exact branch pruning

The safe factor-branch over-approximation contains

```text
29,952 branches.
```

Generation-1 exact good-prime projective local sieve:

```text
29,952 -> 1,946.
```

Run `33509140780`, job `99860360478`, artifact `9800873356`, digest `sha256:c25de400dacadde13ae62028f4ee05d792c4a2f32338a4eed263db3ecc57cc34`.

An elementary d=2 support-prime obstruction was then proved: for odd `p|ab` with `(2/p)=-1`, neither d=2 form `U` nor `V` has a nontrivial projective zero mod p, so p cannot occur in a genuine branch. Generation-2 replay gives

```text
1,946 -> 1,214,
```

with d=2 alone reduced `802 -> 82`. Run `33509939369`, job `99862944274`, artifact `9801199356`, digest `sha256:2b01eca419247b078f9e5656197148e7eba61fc6b27ebc9abb7138f7d83e01d8`.

## Reconstruction genus-one quartic

A genuine factor branch must additionally reconstruct `(T,S)`.

For d=1:

```text
U^2+V^2=(T^2+S^2)^2
=> W^2=delta1^2 R^4+delta2^2 S^4.
```

For d=2:

```text
2(U^2+V^2)=4(S^2-2ST+2T^2)^2
=> W^2=2(delta1^2 R^4+delta2^2 S^4).
```

These diagonal genus-one quartics have `J=0` and reduce, after rational scaling, to finitely many j=1728 congruent-number twists. Eighteen required twist species were run through proof-capable `eclib/mwrank`, requiring the explicit unconditional full-MW-basis success marker and independently bounding rational torsion by good reduction.

Rank-zero species are exactly

```text
1, 2, 10, 26, 66, 195,
```

all with torsion order 4.

Only rank-zero species with an explicit four-point trivial set receive elimination credit. This gives

```text
1,214 -> 1,024.
```

Run `33510649458`, job `99865272250`, artifact `9801489713`, digest `sha256:ad2c4e8750544cd7cf48c463c2948a0964c2c653da850608ed780100d8dd2c93`.

The d=2 side is now almost closed:

```text
20/21 : 16 branches
after all current filters
24/7  : 4 branches
all five other q : 0 branches
```

All twenty surviving d=2 branches have the single reconstruction squareclass species `abs(sf(delta1*delta2))=7`.

The d=1 side has `1,004` positive-rank reconstruction branches remaining.

## Current exact leaf

```text
D2_STAGEA2_CLOSE_20_REMAINING_D2_E7_RECONSTRUCTION_TORSORS_THEN_COMPRESS_D1_POSITIVE_RANK_FACTOR_COVERS
```

The next task is to exploit the common `e=7` reconstruction cover for the twenty d=2 branches, including the remaining `A,B` square conditions and exact pullback. Only after that should the 1,004 d=1 branches be grouped by their much smaller `(q, squareclass/twist species)` data and sent to further cover/MW/Chabauty analysis.

## Credit boundary

```text
D1_LOCAL_CLASSIFICATION_COMPLETE=true
D2_COMMON_JACOBIAN_RANKS_CERTIFIED=true
D2_EXPLICIT_BIRATIONAL_MAPS_COMPLETE=true
D2_EXCEPTIONAL_LOCI_COMPLETE=true
D2_SPLIT_TO_RECEIVER_PULLBACK_COMPLETE=true
D2_STAGEA2_GOOD_PRIME_LOCAL_SIEVE_COMPLETE=true
D2_STAGEA2_SUPPORT_PRIME_REFINEMENT_COMPLETE=true
D2_STAGEA2_RANK_ZERO_RECONSTRUCTION_PRUNING_COMPLETE=true
D2_ALL_FACTOR_BRANCHES_CLOSED=false
DIRECT_COVER_RATIONAL_POINTS_COMPLETE=false
ALL_MULTIPLES_CLOSED=false
R29_EXT_CHANG_C_closed=false
PARENT_ROUTE_CLOSED=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
