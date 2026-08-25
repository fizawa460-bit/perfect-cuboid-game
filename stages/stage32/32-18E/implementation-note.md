# Exact branch-pruning proof note

For each selected scout3 breaker there is an actual element `g` of the source-locked order-1536 automorphism group and an exact integer linear form

`ell_g(z) = score(g.v(z)) - score(v(z))`.

Every full-orbit score minimum satisfies `ell_g(z) >= 0` for every selected `g`. The exact certifier rewrites `ell_g` in the same exact LDL coordinates used for the norm ball. At a partial DFS prefix, if the assigned exact center is negative and its square exceeds `remaining_norm_budget * dual_norm_of_remaining_linear_form`, exact Cauchy--Schwarz proves that no completion can reach `ell_g >= 0`; only then is the branch rejected.

`long double` values are used solely as a scheduling hint for whether to attempt that exact proof. They never authorize rejection. Therefore round-trip drift can only suppress an optional prune and increase runtime; it cannot remove a valid branch. Every surviving leaf is still checked by exact integer breaker evaluation and then canonicalized against all 1536 group elements.

The implementation is intentionally locked to the deterministic 256-breaker bundle reconstructed by `build_prefix_breaker_bundle.py`, canonical bundle SHA `26a6cc35d44029341818b77c0599b6112dc7551da794f6e5d73218f84115995e`.
