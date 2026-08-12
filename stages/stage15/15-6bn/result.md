# Stage15-6bn — effective toric equidistribution audit

Base: Stage15-6bm. This is a literature/theorem-interface audit.

Primary source audited: Zhizhong Huang, `Equidistribution of rational points and the geometric sieve for toric varieties`, arXiv:2111.01509v3 (2026 revision). Huang proves effective Manin--Peyre equidistribution for smooth proper split toric varieties, including arbitrary standard adelic neighbourhoods, with explicit polynomial dependence on the finite-neighbourhood covering exponent.

This is the correct theorem species for 6bm: fixed congruence classes on the Stage15 toric surface are not a measure mismatch.

However, Stage15 needs more than fixed-`q` equidistribution. The actual core `q` is point-generated and can grow polynomially with `B`. To obtain a causal global bound one must extract the exact error dependence for the specific two-coordinate residue neighbourhood, verify uniformity through the required `q`-range, and then sum over actual squarefree cores/orientations without replacing the full-core condition by arbitrary divisibility.

The present audit does not certify that Huang's general polynomial error is small enough through the balancing range `q≈B^(1/4)`. Therefore no `q^{-2}` global main term is promoted yet.

Verdict: the theorem species matches, but the required quantitative window has not been verified.

```text
STAGE15_6_SUBSTAGE=6bn
STAGE15_6BN_AUDIT_VERDICT=BLOCK
STAGE15_6BN_PRIMARY_SOURCE=HUANG_ARXIV_2111_01509_V3
STAGE15_6BN_THEOREM_SPECIES_MATCH=true
STAGE15_6BN_FIXED_ADELIC_NEIGHBOURHOOD_EFFECTIVE=true
STAGE15_6BN_MOVING_q_POLYNOMIAL_WINDOW_CERTIFIED=false
STAGE15_6BN_FULL_CORE_NOT_ARBITRARY_DIVISOR_FIREWALL=true
STAGE15_6BN_CAUSAL_POWER_SAVING_PROMOTED=false
STAGE15_6BN_EXIT=EXACT_UNIFORM_q_WINDOW_REQUIRED
```