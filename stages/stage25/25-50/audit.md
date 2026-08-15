# Stage25-50 hostile fresh audit

Status: **PASS — positive-power lower accepted**

## Scope

This is a hostile audit of the theorem-class-changing checkpoint50 claim

\[
N_2(B)\gg B^{1/4}.
\]

The audit independently attacked the exact homogeneous identities, physical cone/canonical ordering, primitive reduction, exactly-two preservation, squarefreeness/genus of the missing-face curve, qualitative Faltings use, reduced rational-parameter count, height conversion, bounded similarity multiplicity, and cross-stage backflow.

## Accepted theorem

For the homogenized Meskhishvili first NPC parametrization, on `7/2<t<4` we have `0<B<C<A`. After primitive reduction by `g=gcd(A,B,C)`,

\[
(a,b,c)=(B/g,C/g,A/g).
\]

The exact identities preserve two integer face diagonals plus the integer space diagonal. The guaranteed canonical faces are `ab` and `bc`, sharing edge `b`.

The remaining raw face is square only on `w^2=P(t)` with squarefree degree-16 polynomial `P`. The hostile-audit verifier derives its mod-5 `Q` directly from the submitted `P` coefficients, checks the Bezout certificate for `Q,Q'`, and thereby certifies squarefreeness. The smooth projective curve has genus 7, so Faltings leaves only finitely many rational third-face exceptions.

Reduced parameters occur with count `gg T^2`, space height is `O(T^8)`, and the similarity invariant has fibers of size at most 8. Thus

\[
\boxed{N_2(B)\gg B^{1/4}}.
\]

Together with the existing upper,

\[
\boxed{B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}}.
\]

For Stage25,

\[
\boxed{N_2/M_1\gg B^{-7/4}(\log B)^{-1}}.
\]

## Backflow accepted

The numerator lower gives

\[
N_2/M_2\gg B^{-3/4}(\log B)^{-5},
\qquad
N_2/N_1\gg B^{-3/4}(\log B)^{-3}.
\]

Hence

\[
J_2\gg B^{1/4}(\log B)^{-5}\to\infty,
\qquad
I\gg B^{1/4}(\log B)^{-7}\to\infty.
\]

Both previously unresolved interaction signs are now positive/divergent.

The family also proves

\[
\boxed{N_{2,b}(B)\gg B^{1/4}},
\qquad
\boxed{A_{ab,bc}(B)\gg B^{1/4}}.
\]

No Stage25 directional endpoint ratio is inferred because checkpoint30's source-channel denominator adapter remains open.

Backflow records are materialized at:

- `stages/stage19/post-stage25-50-supersession.md`;
- `stages/stage23/post-stage25-r01/result.md`;
- `stages/stage24/post-stage25-r01/result.md`.

## Hostile-audit hardening executed

1. The mod-5 verifier is mechanically bound to the submitted missing-face polynomial rather than an independent hard-coded `Q`.
2. Checkpoint40's exact `upper_provenance` artifact path is restored in the Stage25 controller.
3. The verifier is audit-state aware and distinguishes pre-audit candidate markers from post-audit certified markers.

Final audited-head CI:

```text
Stage25-10 contract audit       run 31865209630  SUCCESS
Stage25-20 matched-grid replay  run 31865209709  SUCCESS
Stage25-30 ratio consistency    run 31865209660  SUCCESS
Stage25-40 upper provenance     run 31865209656  SUCCESS
Stage25-50 parametric lower     run 31865209648  SUCCESS
```

## Nonclaims preserved

```text
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
LOWER_EXPONENT_GREATER_THAN_ONE_QUARTER_PROVED=false
STRICT_SUB_SQRT_WHOLE_FAMILY_UPPER_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
HALF_POWER_INTRINSIC_PROVED=false
PERFECT_CUBOID_CONCLUSION=false
FINITE_DATA_USED_AS_PROOF=false
```

## Audit footer

```text
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
HOSTILE_AUDIT=true
PRIMARY_SOURCE_PROVENANCE_CHECK=PASS
EXACT_STAGE19_ADAPTER_CHECK=PASS
EXACTLY_TWO_MASK_CHECK=PASS
SQUAREFREE_GENUS7_CHECK=PASS
FALTINGS_FINITE_EXCEPTION_CHECK=PASS
PARAMETER_COUNT_CHECK=PASS
HEIGHT_CONVERSION_CHECK=PASS
BOUNDED_MULTIPLICITY_CHECK=PASS
POSITIVE_POWER_LOWER_BOUND_PROVED=true
POSITIVE_POWER_EXPONENT=1/4
STAGE25_RATIO_LOWER_ACCEPTED=true
CROSS_STAGE_BACKFLOW_REQUIRED=true
CROSS_STAGE_BACKFLOW_EXECUTED=true
ADVANCE_ALLOWED=true
NEXT_CHECKPOINT=60
MERGE_ALLOWED=true
COUNTS_RECOMPUTE_REQUIRED=false
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
FINITE_DATA_USED_AS_PROOF=false
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
NEXT_EXPECTED_COMMAND=merge PR #984; then Stage25-main-batch
```
