# Stage16S-30 — fresh audit record

Status: **PASS**

Audited submission: PR #913, head `51a1194853c390b0024bcc80996be802ace3dfd4`.

## Scope checked

- The Stage16S population contract remains the audited primitive/canonical population `0<a<b<c`, `gcd(a,b,c)=1`, `R<=B`, with `SPACE_AT_LEAST` requiring integral `R=d` and `SPACE_ONLY` requiring zero integral face diagonals.
- The primary literature input was checked against Werner Hürlimann, *Exact and Asymptotic Evaluation of the Number of Distinct Primitive Cuboids*, Journal of Integer Sequences 18 (2015), Article 15.2.5. The paper defines the cumulative count `N_3(x)` of distinct primitive nonzero cuboids with odd diagonal and Theorem 7 has leading term `x^2/(32G)`, where `G=L(2,chi_4)` is Catalan's constant.
- The same paper gives the repeated-edge cumulative term `N_2(x;2) ~ sqrt(2) x/(2 pi)`, hence it is `O(x)`.
- The project adapter is valid: primitive Stage16S objects have odd `d`; `gcd(a,b,c)=1` is equivalent to Hürlimann's `gcd(a,b,c,d)=1` on the space-diagonal equation; and strict `a<b<c` removes exactly the repeated-edge family represented by `x^2+2y^2=d^2`. Therefore the strict-canonical correction is lower order and
  `N_S^all(B) ~ B^2/(32G)`.
- Combining with the audited Stage16 ambient law `U(B)=pi/(36 zeta(3)) B^3+O(B^2)` gives
  `N_S^all(B)/U(B) ~ [9 zeta(3)/(8 pi G)] B^-1`.
- For the faceful complement, after marking an integral face, the nested equations `a^2+b^2=e^2`, `e^2+c^2=d^2` give a two-level sum-of-two-squares upper bound. Using `r_2(n)<=4 tau(n)` and the standard divisor bound with the exponent rescaled as needed yields
  `N_S^all(B)-N_S^0(B)=O_epsilon(B^(1+epsilon))` for every `epsilon>0`.
- Consequently
  `N_S^0(B) ~ B^2/(32G)`,
  `N_S^0(B)/N_S^all(B) -> 1`, and
  `N_S^0(B)/U(B) ~ [9 zeta(3)/(8 pi G)] B^-1`.
- Stage16S-20 finite data are used only as diagnostics. No probabilistic independence, causal factorization, sharp faceful-complement asymptotic, or perfect-cuboid conclusion is claimed.
- Stage16S remains an auxiliary parallel lane and checkpoint 40 remains audit-gated until this PASS is merged.

## Evidence classification

The checkpoint is accepted as `LITERATURE_ADAPTED` with a proved project adapter plus an internal divisor-bound proof. No new external or human input is required.

```text
AUDIT_VERDICT=PASS
AUDIT_PERSISTENCE_STATUS=PENDING_CONTROLLER_SYNC
ADVANCE_ALLOWED=true
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
NEXT_CHECKPOINT=40
NEXT_STAGE=
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
MERGE_ALLOWED=true
```
