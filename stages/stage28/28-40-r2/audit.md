# Stage28-40-r2 fresh audit

```text
AUDITED_PR=1277
AUDITED_SUBMISSION_HEAD=c59a9e7028b70599eba3cdacad193940e06e58fa
AUDIT_VERDICT=FAIL_REPAIR_REQUIRED
CHECKPOINT40_R2_AUDIT=FAIL_REPAIR_REQUIRED
REPAIR_REQUIRED=true
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=40
NEXT_EXPECTED_COMMAND=Stage28-audit
```

## Primary blocking defect

The U10 branch-component proof contains a load-bearing algebraic identity written incorrectly.  The submitted file states

\[
F_{\rm sp}/4=
(u_1u_2-iv_1v_2)(u_1u_2+iv_1v_2)
+
(u_1v_2-iu_2v_1)(u_1v_2+iu_2v_1).
\]

That displayed equality is false: the right-hand side is a sum of two quadratic products and does not equal the quartic `F_sp/4` defined immediately above.

The intended identity is the four-factor product

\[
\boxed{
F_{\rm sp}/4=
(u_1u_2-iv_1v_2)(u_1u_2+iv_1v_2)
(u_1v_2-iu_2v_1)(u_1v_2+iu_2v_1).
}
\]

Expanding this product gives exactly

\[
4u_1^2v_1^2u_2^2v_2^2
+(u_1^2-v_1^2)^2u_2^2v_2^2
+(u_2^2-v_2^2)^2u_1^2v_1^2.
\]

With the corrected factorization, the claimed four geometric `(1,1)` components and the downstream branch-profile conclusions are plausible and consistent, but the current submitted proof cannot receive PASS while its factorization line is wrong.

## Audit of the exhaustion claim

The r2 work is materially deeper than the prior U1-U9 batch: it distinguishes the branch component profiles (`4 x genus 0` versus `2 x genus 1`), sharpens the local comparison to an Euler-product bias, matches the explicit Huang thin-cover exponent range, separates the quadratic cover squareclasses, and checks the Kummer-height route.  These are genuinely distinct lanes rather than renamed repetitions.

Subject to repair of the U10 factorization and confirmation that U13 continues to use the corrected branch supports, the final receiver

```text
OPEN_GATE_40_R2=DistinctBranchProfileDoubleCoverMarginalComparison
```

is appropriately narrow and research-request-ready.  No obvious repo-native route omitted by the submitted U1-U14 ledger was found that would legally yield a strict bridge-upper improvement without new global arithmetic input or the deferred perfect-cuboid endpoint.

```text
MATERIALLY_DISTINCT_ROUTES_TOTAL_AUDIT=PASS_14
MAXIMAL_BOUNDED_EXPLORATION_CLAIM_AUDIT=PASS_CONDITIONAL_ON_U10_REPAIR
OPEN_GATE_RESEARCH_REQUEST_READY_AUDIT=PASS_CONDITIONAL_ON_U10_REPAIR
PERFECT_CUBOID_ENDPOINT_FIREWALL_AUDIT=PASS
NUMERIC_BRIDGE_UPPER_IMPROVED=false
SOURCE_TARGET_ASYMPTOTIC_ORDERING_IDENTIFIED=false
```

## Required repair

1. Replace the false `+` identity in `branch-component-decomposition.md` by the exact four-factor product.
2. Re-read U10/U13/result/controller for any text that relies on the erroneous written identity rather than the corrected factorization; no claim change is expected if the intended product was used.
3. Submit the repaired head for fresh `Stage28-audit`.

```text
REPAIR_SCOPE=LOCAL_ALGEBRAIC_FACTORISATION_WRITEUP
EXPECTED_MATHEMATICAL_CLAIM_CHANGE=NONE_IF_CORRECTED_PRODUCT_IS_CONFIRMED
MERGE_ALLOWED=false
ADVANCE_TO_CHECKPOINT50=false
```
