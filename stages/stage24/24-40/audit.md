# Stage24-40 fresh audit

AUDIT_VERDICT=FAIL
CHECKPOINT=40
PR=975

## Accepted

The checkpoint40 upper-side reopening is substantive and source-level. The following parts are accepted:

- Stage14-4ah gives exact physical height `H_M=d=R`, fixed-curve exponent `2/(M.C)`, and `M.C>=4` for every fixed physical rational curve.
- Stage14-4ai reduces the extremal `M.C=4` fixed rational-curve mechanism to the final split singular-anticanonical case.
- Stage14-4ak closes that final case by the exact anti-invariant parity-coset void, so `PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTS=false`.
- Therefore every fixed physical rational curve has integer `M.C>=5`, and each individually has polynomial height exponent at most `2/5`.
- Any one fixed finite collection of such curves is strict sub-square-root.
- Stage14-4dj directly proves the principal-density deficit localization: for `omega(c)=B^(-delta+o(1))`, the charged stratum is `B^(1/2-delta+o(1))`; square-root saturation can only remain in `omega(c)=B^(-o(1))` cells.
- The Q06/Jacobi and Stage15 genus-one rechecks correctly leave a moving-family / first-small-point / transverse-incidence gate.
- The split-prime local tensor `rho_p=1-4/p+O(p^-2)` remains logarithmic even under a hypothetical polynomial prime window, so it does not by itself produce a fixed-power saving.
- No whole-family strict sub-square-root theorem is proved; the strongest certified bound remains `N2(B)<<_epsilon B^(1/2+epsilon)`.

## FAIL reason — nonuniform moving-family summation

Checkpoint40 goes one step beyond the source theorem when it writes, for a `B`-dependent collection of `K(B)` fixed rational strata of degree at least five,

`N_curves(B) << K(B) B^(2/5+o(1))`

and then infers the necessary proliferation lower bound

`K(B) >= B^(1/10-o(1))`

for square-root saturation.

Stage14-4ah certifies the exponent `2/(M.C)` for **one fixed curve**. It does not provide a height-count estimate whose implied constant and `o(1)` are uniform over a family of curves that itself varies with `B`.

A fixed finite collection is safe because its finitely many constants can be absorbed. A growing collection `K(B)` is different: summing the pointwise fixed-curve estimates requires a uniform family bound controlling the constants/height normalization as the curve varies. No such uniformity is proved in Stage14-4ah/4ak, Stage23 Q06, or checkpoint40. Indeed, uniform control over a moving family is one of the very gates checkpoint40 correctly records as still open.

Therefore the following checkpoint40 claims are not yet rigorous:

- `N_curves << K(B)B^(2/5+o(1))` for a `B`-dependent family;
- `K(B)>=B^(1/10-o(1))` as a necessary proliferation condition.

This does **not** invalidate the fixed-curve degree-four void, the finite-union sub-square-root statement, the Stage14-4dj occupancy localization, the local-sieve boundary, or the conclusion that no whole-family strict sub-square-root theorem has been obtained.

## Minimal repair

Choose one of two repairs:

1. Preferred: remove/downgrade the `K(B)` summation and `B^(1/10)` proliferation claim. Retain only:
   - every individual fixed rational curve has exponent at most `2/5`;
   - every genuinely fixed finite collection is strict sub-square-root;
   - passing from fixed curves to a growing/moving collection requires a new uniform family theorem.

2. Alternatively, prove a uniform bounded-height estimate over the relevant degree-at-least-five physical curve family strong enough to justify the displayed `K(B)` summation. This would itself be meaningful new moving-family input.

No recomputation is required. Do not reopen the accepted M4 parity-coset computation, Stage14-4dj, checkpoint30, or the finite census.

```text
DISCOVERY_AUDIT_REQUIRED=true
DISCOVERY_AUDIT_VERDICT=FAIL
FIXED_M4_SQRT_MECHANISM_ELIMINATED_ACCEPTED=true
FIXED_CURVE_SINGLE_EXPONENT_2_5_ACCEPTED=true
FIXED_FINITE_COLLECTION_SUBSQRT_ACCEPTED=true
PRINCIPAL_DENSITY_LOCALIZATION_ACCEPTED=true
Q06_MOVING_FAMILY_BOUNDARY_ACCEPTED=true
GROWING_MODULUS_RECHECK_ACCEPTED=true
STRICT_SUB_SQRT_WHOLE_FAMILY_PROVED=false
NONUNIFORM_KB_SUMMATION_REJECTED=true
B_ONE_TENTH_PROLIFERATION_CLAIM_REJECTED=true
REPAIR_SCOPE=REMOVE_OR_UNIFORMLY_PROVE_GROWING_CURVE_FAMILY_SUMMATION_ONLY
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=40
MERGE_ALLOWED=false
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
```
