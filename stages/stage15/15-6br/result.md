# Stage15-6br — Huang geometric-sieve large-prime audit

Base: Stage15-6bq. Audit verdict: BLOCK for fixed-power thinning.

Huang v3 Theorem 1.5 gives, for a fixed codimension-at-least-two reduction locus and primes p>=N, a bound of shape

\[
\ll B(\log B)^{r-1}/(N\log N)+B(\log B)^{r-2}\log\log B.
\]

The common-core prime condition is codimension two after the S/O orientation union, so this theorem is the correct species for the branch where the actual core q has a large prime factor. But the second term is still B times a logarithmic saving only. Taking N=B^theta therefore does not certify a polynomial B-saving.

Moreover a large squarefree q may be smooth, so a largest-prime split alone cannot cover the high-core population.

```text
STAGE15_6_SUBSTAGE=6br
STAGE15_6BR_AUDIT_VERDICT=BLOCK
STAGE15_6BR_GEOMETRIC_SIEVE_SPECIES_MATCH=true
STAGE15_6BR_LARGE_PRIME_POLYNOMIAL_SAVING=false
STAGE15_6BR_SMOOTH_LARGE_CORE_UNCOVERED=true
STAGE15_6BR_EXIT=CODIMENSION_TWO_MULTIPLICATIVE_SIEVE_GATE_READY
```
