# Stage14-q8 — compact summary

## Why q8 reopened

q7 parked the literature route until a live proof track exposed a stable named obstruction. Two such triggers now exist:

- `Stage14-s5m`: the unresolved analytic boundary has been reduced to a one-small-variable complementary-divisor Jacobi operator with a physical quadratic character;
- `Stage14-t23`: the active-direction second moment has split into rank and torsion branches, with the torsion branch reduced to two explicit quartic squareclass packets.

So q8 is a focused transfer pass, not a broad literature sweep.

## Strongest s-side transfer

**Cameron Wilson 2025, Hooley-neutraliser quadratic large sieve — `NEAR_HIGH_PRIORITY`.**

The theorem is designed for hyper-skewed quadratic-character bilinear forms and retains a multiplicative-weight logarithmic saving. This geometry matches the s5m divisor-switched boundary much better than the older symmetric/interior large-sieve tools.

The missing compatibility lemma is exact: s5n must rewrite each switched physical monomial into a finite combination of

```text
sum A_k B_v f(v) (k/v),   k << v,
```

with the remaining physical character/local state absorbed into bounded one-variable coefficients and a multiplicative `f(v)` satisfying Wilson's prime-average hypothesis.

Old Wilson hyperbolic-region Jacobi bounds remain blocked as the direct boundary solution because they avoid the axes, whereas s5m has isolated a near-axis strip deliberately.

## Strongest t-side transfer

For

```text
F_plus  = m^4+6m^2n^2+n^4,
F_minus = m^4+n^4,
```

t23 squareclass collisions satisfy

```text
core(F(u))=core(F(v))  <=>  F(u)F(v) is a square.
```

The key q8 observation is that square-sieve prime correlations factor exactly:

```text
chi_p(F(u)F(v)) = chi_p(F(u)) chi_p(F(v)).
```

Therefore t24 should first use **square sieve + binary-quartic character sums**, rather than immediately forcing the collision into a generic nonseparable four-variable polynomial sieve.

Exact algebra checks:

```text
disc(x^4+1)=2^8,
disc(x^4+6x^2+1)=2^14.
```

Both quartics are separable at every odd prime, and their degree-four homogeneity makes the squareclass projective in the reduced direction `[m:n]`.

Pierce–Xu Burgess bounds at forms are a high-priority `NEAR` building block for the binary-quartic sums; the exact admissibility/modulus hypotheses still need a t24 check.

## What did not become a shortcut

- generic Bonolis–Pierce nonseparable polynomial-sieve machinery: reserve only; the naive pair cover has special branch geometry and the Stage14 prime correlation already separates;
- modern 2-Selmer distribution results: do not answer the rank-active least-small-physical-point frequency problem;
- new K3/Shimada scan: no new geometric trigger; 14-4 should import s5n first;
- spectral/Kloosterman escalation: defer until an actual Kloosterman kernel is produced.

## Routing

```text
STAGE14_Q8=COMPLETE_TRIGGERED_CROSS_DOMAIN_TRANSFER_RADAR
DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0
S5N_WILSON2025_NEUTRALISER_TRANSFER=NEAR_HIGH_PRIORITY
T24_SQUARE_SIEVE_PRIME_CORRELATION_FACTORIZES=true
T24_PIERCE_XU_BINARY_QUARTIC_TRANSFER=NEAR_HIGH_PRIORITY
Q3_LE_BOUDEC_HEIGHT_TRANSFER_REMAINS_PRIMARY=true
MAIN_14_4_IMPORT_S5N_FIRST=true
HANDOFF_S=Stage14-s5n
HANDOFF_T=Stage14-t24
NEXT_Q_STAGE=NONE_UNTIL_TRANSFER_TEST_FAILURE_OR_NEW_TRIGGER
```

No Stage14 power-saving theorem is claimed by q8 itself.
