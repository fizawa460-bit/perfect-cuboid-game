# Stage24-30 fresh audit

AUDIT_VERDICT=PASS
CHECKPOINT=30
PR=974

## Verdict

Checkpoint30 is accepted.

The literal Stage18 -> Stage19 survivor ratio is exact under the common primitive/canonical physical `R<=B` measure. The frozen interfaces

\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0,
\]

and

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}
\]

legally imply

\[
\frac{N_2(B)}{M_2(B)}\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-5}\to0.
\]

The same whole-family numerator bound combined with the positive directional source asymptotics gives the claimed direction-by-direction quantitative zero-density bounds. No directional limiting constants are inferred.

## Leading-constant audit

Stage15-2b certifies `C_M2=C_a+C_b+C_c` with all chamber constants positive, but explicitly leaves those constants unevaluated. The numerator theorem is an upper bound with an implicit epsilon-dependent constant. Therefore checkpoint30 correctly refuses to manufacture a numerical survivor leading constant.

## Independent Route C audit

The new space-square cover is accepted.

On the dense chart `e=1`, with

\[
x=\frac{2t}{1-t^2},\quad u=\frac{1+t^2}{1-t^2},\quad y=\frac{2s}{1-s^2},
\]

the space radicand is

\[
f=\frac{u^2s^4+(4-2u^2)s^2+u^2}{(1-s^2)^2}.
\]

Writing `z=s^2`, the numerator quadratic has discriminant

\[
16(1-u^2)=-16x^2,
\]

which is generically nonzero. Its two z-roots are distinct and nonzero; hence the quartic numerator has four simple s-roots over the geometric function field and cannot be a square. Since the denominator is already a square, `f` is not a square in the geometric function field. Thus adjoining `sqrt(f)` gives a geometrically integral generically degree-two cover, and its rational image is type-II thin.

The theorem transfer is compatible with the frozen Stage15-2b interface: the base is the same smooth split toric resolution, `R` is the exact anticanonical height, and the required equidistribution/almost-Fano hypotheses are already part of the audited Stage15 contract. Browning-Loughran Theorem 1.2 is the correct theorem species for zero density of a thin subset under these hypotheses. Therefore the independent conclusion

\[
N_2(B)=o(B(\log B)^5),\qquad N_2(B)/M_2(B)\to0
\]

is accepted.

This route is qualitative only. It does not yield a strict sub-square-root upper bound and is not multiplied with the Stage14 half-power saving.

## Discovery audit

The required discovery audit is PASS at checkpoint30 scope.

- Stage15-2b source and directional asymptotics were source-opened.
- Stage19/Stage23 upper-bound history was checked; no certified strict sub-square-root numerator theorem was found.
- The new thin-cover mechanism was independently algebra-checked rather than accepted from the submission summary.
- The external Browning-Loughran theorem contract was checked against the original paper.

```text
DISCOVERY_AUDIT_REQUIRED=true
DISCOVERY_AUDIT_VERDICT=PASS
DISCOVERY_AUDITOR=FRESH_STAGE24_AUDIT
STRONGEST_CERTIFIED_QUANTITATIVE_RATIO_ACCEPTED=true
SPACE_THIN_COVER_GEOMETRICALLY_INTEGRAL_ACCEPTED=true
SPACE_THIN_IMAGE_TYPE_II_ACCEPTED=true
SPACE_THIN_ROUTE_ZERO_DENSITY_ACCEPTED=true
SPACE_THIN_ROUTE_EFFECTIVE_POWER_SAVING=false
INDEPENDENT_ZERO_DENSITY_ROUTES_ACCEPTED=3
LEADING_CONSTANT_SEARCH_ACCEPTED=true
DIRECTIONAL_REFINEMENT_ACCEPTED=true
TRUE_RATIO_EXPONENT_IDENTIFIED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
HALF_POWER_INTRINSIC_PROVED=false
FINITE_DATA_USED_AS_PROOF=false
ADVANCE_ALLOWED=true
NEXT_CHECKPOINT=40
MERGE_ALLOWED=true
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
```
