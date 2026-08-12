# Stage15-6-cycle — 6bp through 6bs

Base: merged PR #853.

```text
6bp  Huang moving polynomial window              BLOCK
6bq  maximal direct Huang level certificate      PASS
6br  geometric-sieve large-prime route           BLOCK
6bs  multiplicative codimension-two sieve gate   NEW_GATE
```

Theorem 1.4 gives neighbourhood-complexity exponent 10 for the Stage15 toric surface, so direct moving-modulus equidistribution reaches only q<=log(B)^(1/24-o(1)), not q=B^theta. Theorem 1.5 handles existence of a large bad prime but leaves a B times logarithmic remainder and does not cover smooth large squarefree q.

Thus the next legal global-charge theorem must aggregate the primewise p^-2 local conditions multiplicatively before the effective-equidistribution error is paid.

```text
STAGE15_6_CYCLE_START=6bp
STAGE15_6_CYCLE_END=6bs
STAGE15_6_CYCLE_AUDIT_LEDGER=BLOCK,PASS,BLOCK,NEW_GATE
STAGE15_6_CYCLE_HUANG_POLYNOMIAL_WINDOW=false
STAGE15_6_CYCLE_MAX_DIRECT_HUANG_LEVEL=log(B)^(1/24-o(1))
STAGE15_6_CYCLE_GEOMETRIC_SIEVE_FIXED_POWER=false
STAGE15_6_CYCLE_REQUIRED_GLOBAL_OBJECT=CODIMENSION_TWO_MULTIPLICATIVE_SIEVE
STAGE15_6_CYCLE_CAUSAL_THREE_QUARTERS_PROVED=false
STAGE15_6_CYCLE_CAUSAL_HALF_POWER_REDERIVED=false
STAGE15_6_CYCLE_EXIT=DIMENSION_TWO_SIEVE_OR_UNIVERSAL_TORSOR_CONGRUENCE_THEOREM_GATE
```
