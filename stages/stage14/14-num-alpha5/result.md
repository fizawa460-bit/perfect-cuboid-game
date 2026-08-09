# Stage14-num-α5 — safe primitive diagonal / pair sieve

> STATUS: `STAGE14_NUM_ALPHA5=PENDING_GITHUB_ACTIONS_FINAL_LOCK`
>
> CLASSIFICATION: exact finite-enumeration engineering theorem/audit; no asymptotic claim.

## Goal

Prove which diagonal and pair-level filters can be applied *before* expensive Gaussian representation/collision work while preserving every primitive Stage14 object with at least two integral face diagonals.

No historical perfect-cuboid-only mod-11/mod-19 pruning is imported.

## 1. Primitive diagonal support theorem

Take any Stage14 object with an integral face diagonal `F=sqrt(b^2+c^2)` and space diagonal

```text
d^2 = a^2 + F^2.
```

### Excluding `2 | d`

If `d` is even, then `d^2 = 0 (mod 4)`. Since squares mod 4 are only 0 or 1, `a^2+F^2=0 (mod 4)` forces both `a` and `F` even. Then `F^2=b^2+c^2=0 (mod 4)` forces both `b,c` even. Hence all three edges are even, contradicting primitiveness.

Therefore every primitive Stage14 object has `d` odd.

### Excluding primes `p == 3 (mod 4)`

If `p == 3 (mod 4)` divides `d`, then

```text
a^2 + F^2 == 0 (mod p).
```

Because `-1` is not a quadratic residue mod such `p`, this forces `p|a` and `p|F`. Applying the same fact to `F^2=b^2+c^2` gives `p|b,c`. Again the box is nonprimitive.

Therefore no prime `3 mod 4` divides the primitive space diagonal.

Combining the two statements:

```text
primitive Stage14 diagonal d > 1
=> every prime divisor of d is 1 mod 4
=> d == 1 mod 4.
```

This is stronger than merely checking `d mod 4` and is safe for the full exactly-two-or-three-face census.

## 2. Exact representation-count sieve

For an all-split diagonal

```text
d = product_i p_i^e_i,  p_i == 1 (mod 4),
```

the classical two-squares count gives

```text
r_2(d^2) = 4 product_i (2e_i+1).
```

After removing the four axis representations and quotienting by the eight sign/order symmetries of every positive nontrivial unordered pair,

```text
#Rep_+(d^2) = ( product_i(2e_i+1) - 1 ) / 2.
```

The alpha collision construction needs two *distinct* nontrivial representations of the same `d^2`; using both orientations of only one representation yields zero residual. Hence diagonals with `#Rep_+(d^2)<2` can be discarded before Gaussian synthesis.

In particular a single split prime `d=p` has only one such representation and cannot contribute.

## 3. Safe pair common-divisor sieve

For a compressed collision candidate with edge roles `x,y`,

```text
c^2 = d^2 - x^2 - y^2.
```

If a prime `p` divides `gcd(d,x,y)` and `c^2` is a square, then `p^2` divides the right-hand side, so `p|c`. Thus the reconstructed edge triple has a common factor `p` and is nonprimitive.

Therefore

```text
gcd(d,x,y) > 1
```

is a safe pre-square-test rejection.

The existing Stage14 canonical semantics also require strict edge inequalities, so an `x==y` candidate may be rejected before `isqrt` rather than after reconstruction.

## 4. Physical-height semantics

Stage14's physical cutoff is already exactly `d<=B`. Alpha5 does not rescale or replace the diagonal: it only discards diagonals that cannot support a *primitive* accepted object. A nonprimitive object removed at diagonal `d` reduces to its primitive representative at a strictly smaller diagonal and is generated there independently if it lies in the cutoff.

Thus the pruning does not alter the Stage14 physical-height contract.

## Acceptance gates

Dedicated CI requires:

1. At `B=200,000`, exact object-set equality between the merged alpha4 stream and the alpha5-pruned stream.
2. For every kept all-split diagonal in the audit, the Gaussian representation-set size equals the exact formula above.
3. At frozen `B=2,000,000`, exact counts, graph counts, and all four Stage14-num1 SHA-256 locks.
4. Record the exact outer-sieve rejection counts and pre-`isqrt` pair rejection counts.

The expected purely factorization-level outer candidate count at B=2m is about 97k rather than 2m; the committed result is taken only from Actions, not from this expectation.

## Boundary

Alpha5 proves and measures safe pruning, but still does **not** claim a meaningful end-to-end crossover against the ordinary rolling num engine. That decision remains alpha7 after alpha6 locks a broader equality matrix.

```text
HISTORICAL_MOD11_MOD19_PRUNING_IMPORTED=false
MEANINGFUL_END_TO_END_SPEEDUP_PROVED=false
NEXT_AFTER_SUCCESS=Stage14-num-alpha6
```
