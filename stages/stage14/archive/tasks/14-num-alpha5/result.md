# Stage14-num-α5 — safe primitive diagonal / pair sieve

> STATUS: `STAGE14_NUM_ALPHA5=COMPLETE_SAFE_PRIMITIVE_DIAGONAL_AND_PAIR_SIEVE`
>
> CLASSIFICATION: exact finite-enumeration engineering theorem/audit; no asymptotic claim.

## Goal

Prove which diagonal and pair-level filters can be applied before expensive Gaussian representation/collision work while preserving every primitive Stage14 object with at least two integral face diagonals. No historical perfect-cuboid-only mod-11/mod-19 pruning is imported.

## 1. Primitive diagonal support theorem

Take any Stage14 object with an integral face diagonal `F=sqrt(b^2+c^2)` and space diagonal

```text
d^2 = a^2 + F^2.
```

If `d` is even, squares mod 4 force `a,F` even and then `b,c` even, contradicting primitiveness. If a prime `p==3 (mod 4)` divides `d`, nonresiduosity of `-1` forces `p|a,F` and then `p|b,c`, again contradicting primitiveness. Hence

```text
primitive Stage14 diagonal d>1
=> every prime divisor of d is 1 mod 4
=> d == 1 mod 4.
```

This is safe for the complete exactly-two-or-three-face primitive census.

## 2. Exact representation-count sieve

For

```text
d = product_i p_i^e_i,  p_i == 1 (mod 4),
```

the two-squares formula gives

```text
r_2(d^2) = 4 product_i(2e_i+1),
#Rep_+(d^2) = (product_i(2e_i+1)-1)/2,
```

where `Rep_+` means positive unordered nontrivial representations. Alpha collisions require two distinct representations; a single representation paired with its reversed orientation gives zero residual. Therefore `#Rep_+(d^2)<2` is a safe outer rejection.

## 3. Safe pair common-divisor sieve

For

```text
c^2 = d^2-x^2-y^2,
```

if a prime divides `gcd(d,x,y)` and `c` is integral, it also divides `c`. The reconstructed edge triple is nonprimitive, so `gcd(d,x,y)>1` is a safe pre-square-test rejection. The frozen Stage14 canonical contract also requires strict edge inequalities, so `x==y` can be rejected before `isqrt`.

## 4. Physical-height semantics

The Stage14 physical cutoff remains exactly `d<=B`. Alpha5 does not rescale the search variable; it only rejects diagonals that cannot support a primitive accepted object. Thus the physical-height contract is unchanged.

## Successful Actions audit

Dedicated Actions run `31313019131` completed successfully.

At `B=200,000`, alpha5 reproduced the alpha4 object set exactly:

```text
objects                                  116 / 116
alpha4 streamed seconds                  3.517591608
alpha5 pruned seconds                    1.028535169
alpha4/alpha5 ratio                      3.420001293x
alpha4 isqrt tests                         602,930
alpha5 isqrt tests                         118,103
alpha5 kept diagonals                        9,714
common-divisor rejects before sqrt         161,394
```

The complete outer partition at B=200k was:

```text
even diagonal                            100,000
contains 3 mod 4 prime                    81,308
fewer than two nontrivial reps              8,977
kept                                        9,714
trivial                                         1
```

At frozen `B=2,000,000`:

```text
diagonals scanned                       2,000,000
diagonals kept                             97,169
even rejected                           1,000,000
3 mod 4 factor rejected                   828,414
<2 representation rejected                 74,416
common-divisor pair rejects             2,878,014
isqrt tests                             1,758,993
alpha5 streamed seconds                    13.47029
objects                                       356
N_a^(2),N_b^(2),N_c^(2)                 142,134,80
T                                               0
active faces                                  490
raw edges                                     356
max degree                                      9
```

All four frozen Stage14-num1 SHA-256 ledgers matched. The exact representation-count formula was also checked against the generated Gaussian representation set on every kept diagonal.

The B=200k timing demonstrates a large alpha4-to-alpha5 internal speedup, but it is not yet the formal alpha-vs-ordinary-num crossover. That remains alpha7 after alpha6 broadens the exact equality matrix.

```text
STAGE14_NUM_ALPHA5=COMPLETE_SAFE_PRIMITIVE_DIAGONAL_AND_PAIR_SIEVE
PRUNED_OBJECT_SET_EQUALS_ALPHA4=true
PRUNED_B2M_MATCHES_FROZEN_NUM1=true
B2M_FOUR_HASH_LOCKS_MATCH=true
HISTORICAL_MOD11_MOD19_PRUNING_IMPORTED=false
MEANINGFUL_END_TO_END_SPEEDUP_PROVED=false
NEXT=Stage14-num-alpha6 exact frozen-cutoff equality matrix and independent regression pack
```
