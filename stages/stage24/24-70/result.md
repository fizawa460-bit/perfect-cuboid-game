# Stage24-70 — bounded maximal synthesis / closeout candidate

EVIDENCE_LEVEL=PROVED_BOUNDED_SYNTHESIS_FROM_AUDITED_CHECKPOINTS
CHECKPOINT=70
STATUS=SUBMITTED_FOR_FRESH_AUDIT
TRANSITION=Stage18 -> Stage19

## Executive synthesis

Stage24 studies the literal subset transition from primitive canonical exactly-two-face cuboids without a space requirement to the same population with integral space diagonal, under the exact common cutoff

\[
R=\sqrt{a^2+b^2+c^2}\le B.
\]

With `M2(B)` for the Stage18 source and `N2(B)` for the Stage19 target, the audited theorem stack is

\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0,
\]

\[
\sqrt{\log B}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon},
\]

and therefore

\[
\boxed{
B^{-1}(\log B)^{-9/2}
\ll
\frac{N_2(B)}{M_2(B)}
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-5}
}
\]

with

\[
\boxed{N_2(B)/M_2(B)\to0}
\]

and simultaneously

\[
\boxed{N_2(B)\to\infty}.
\]

Thus the strongest bounded classification is

```text
STAGE24_CLASS=THIN_BUT_INFINITE
GLOBAL_ZERO_DENSITY_PROVED=true
TARGET_UNBOUNDEDNESS_PROVED=true
POSITIVE_POWER_TARGET_LOWER_BOUND_PROVED=false
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
```

## KNOWN_RESULTS

1. Exact transition contract: Stage19 equals Stage18 intersect `{R integral}` with identical primitive/canonical population, physical cutoff and multiplicity.
2. Exact matched finite census through `B=1,000,000`, with `M2(10^6)=13,817,725`, `N2(10^6)=255`; finite data are diagnostic only.
3. Quantitative upper ratio:
   `N2/M2 <<_epsilon B^(-1/2+epsilon)(log B)^(-5)`.
4. Three independent zero-density routes exist at different strength:
   - quotient of the Stage19 half-power upper by the Stage18 asymptotic;
   - fixed-prime squareclass/local sieve, qualitative only;
   - geometrically integral degree-two space-square thin cover, qualitative only.
5. Fixed physical rational curves cannot explain square-root saturation: the physical `M·C=4` mechanism is absent, so every fixed rational curve has individual exponent at most `2/5+o(1)`; any fixed finite collection is strict sub-square-root.
6. Whole-family strict sub-square-root remains unproved because growing moving-family uniformity is missing.
7. Mixed-parity quartic family
   `p^4+q^4=17Z^2`
   produces infinitely many primitive canonical exactly-two Stage19 objects and gives
   `N2(B)>>sqrt(log B)`.
8. Historical odd/odd specialization of the same algebraic formula remains space-dead modulo 16; the broader formula is revived by mixed parity.
9. Intrinsic ambient space-diagonal baseline from Stage16S is `~ const/B`.
10. Stage21 proves one-face conditioning changes that ambient space cost by a positive `(log B)^2` enhancement while retaining polynomial order `B^-1`.
11. For the two-face host, current Stage24 bounds straddle the ambient-neutral scale, so the global interaction sign is unresolved.
12. The Stage22/Stage23 second-order cross-ratio also straddles 1, so the effect of prior space integrality on acquisition of a second face is unresolved.
13. Post-Stage24 Stage23 reinvestigation proves the named integral-space pair-overlap channel
    `A_ac,bc(B)>>sqrt(log B)`
    while the frozen Stage17 overlap theorem gives
    `A_ac,bc(B)=o(B(log B)^3)`.

## ADDITIONAL_DEDUCTIONS

### D70-01: explicit lower ratio from the infinite family

From `N2(B)>>sqrt(log B)` and `M2(B)~C_M2 B(log B)^5`,

\[
\boxed{
\frac{N_2(B)}{M_2(B)}
\gg B^{-1}(\log B)^{-9/2}.
}
\]

This is a true asymptotic lower inequality, not a finite-census extrapolation.

### D70-02: zero density does not mean finite target

Combining the lower theorem with any of the audited zero-density routes yields the logically stronger qualitative description

\[
N_2(B)\to\infty,
\qquad
N_2(B)=o(M_2(B)).
\]

Thus the integral-space condition removes asymptotically almost all Stage18 objects while leaving infinitely many primitive exactly-two survivors.

### D70-03: a named direction is infinite

On the physical C17 cone the canonical ordering is `(a,b,c)=(x,y,e)`, and the guaranteed integral faces are `ac` and `bc`. Therefore the shared-edge-`c` directional target satisfies

\[
\boxed{N_{2,c}(B)\gg\sqrt{\log B}}.
\]

This gives a proved directional infinitude statement, but not a directional asymptotic or limiting survivor ratio.

### D70-04: named source-host overlap is thin but infinite

Every C17 box lies in the Stage17 `ac,bc` pair-overlap channel, so

\[
\boxed{A_{ac,bc}(B)\gg\sqrt{\log B}}.
\]

Together with the frozen Stage17 overlap theorem,

\[
\boxed{
\sqrt{\log B}\ll A_{ac,bc}(B)=o(B(\log B)^3).
}
\]

Hence a specific causal channel behind the Stage23 target is now known to be infinite but lower order.

## CAUSAL_SYNTHESIS

The Stage24 added condition is literally the new space-square predicate on the Stage18 shared-edge double-Pythagorean host. It can be represented equivalently as a rational lift to

\[
w^2=e^2+x^2+y^2,
\]

or in the paired-Gaussian normal form by the squareclass equality `sf(A)=sf(B)`.

The audited evidence establishes three different layers:

- **geometric rarity:** the space-square lift is a genuine degree-two geometrically integral cover, so its rational image is thin and zero-density;
- **local arithmetic rarity:** split-prime valuation parity gives an independent qualitative zero-density sieve;
- **global quantitative ceiling:** the inherited Stage14/19 theorem gives `N2<<B^(1/2+epsilon)`.

These layers are not multiplied together. Neither the thin-set theorem nor the fixed-prime local sieve has been proved to supply the half-power rate.

The lower side is arithmetically heterogeneous. The historical odd/odd Stage15-2 slice has no space lifts modulo 16, whereas the mixed-parity C17 slice contains infinitely many space lifts. Therefore a single ambient two-face algebraic formula can contain both completely dead and infinite arithmetic strata.

The exact mechanism that determines the whole-population exponent remains unresolved.

## LOWER_STAGE_REINTERPRETATIONS

The following are later supersessions, not revocations of historical audits:

1. Stage19 historical statements saying unboundedness and an infinite primitive construction were unproved are superseded by Stage24 checkpoint50. The materialized record is `stages/stage19/post-stage24-50-supersession.md`.
2. Stage23's odd/odd modulo-16 death certificate remains valid under its stated parity hypothesis, but any broader claim that the underlying formula is globally dead is superseded by the mixed-parity C17 family.
3. Post-Stage24 Stage23 reinvestigation is audited and merged. It upgrades the adjacent-stratum ratio to a two-sided bound and proves the `A_ac,bc` named overlap channel is infinite.
4. Historical Stage19 and Stage23 PASS verdicts remain valid for the claims available at their audit times.

No foundational lower-stage population, cutoff, canonicalization or multiplicity contract was invalidated, so no lower-stage recomputation is required.

## REFINEMENT_CANDIDATES

1. Prove uniform bounds for moving/growing curve families; fixed-curve bounds alone cannot control the whole family.
2. Improve the moving-Jacobi/Q06 receiver with a uniform height/count theorem.
3. Obtain growing-modulus or averaged squareclass-sieve uniformity strong enough to produce a genuine power saving.
4. Improve the C17-family counting from `sqrt(log B)` toward a positive power of `B`, or find a denser independent family.
5. Prove a strict whole-family sub-square-root upper bound.
6. Evaluate the Stage18 Peyre/Tamagawa constant `C_M2` numerically/closed-form if a later comparison needs it.
7. Determine directional Stage19 asymptotics or at least compare `N2,a,N2,b,N2,c` beyond finite diagnostics.
8. Determine whether the half-power ceiling is intrinsic or merely a current proof limit.

## NEW_HEURISTICS

The frozen matched census shows a decreasing survivor ratio through `B=10^6`, but effective slopes change materially between scale ranges. This is evidence against promoting a finite fitted exponent. Directional survivor rates at `10^6` are ordered `a>b>c`, but no limiting directional ordering is claimed.

No heuristic is used in any Stage24 theorem.

## OPEN_GATES

```text
OPEN_GATE_01=TRUE_TARGET_POLYNOMIAL_EXPONENT_UNKNOWN
OPEN_GATE_02=POSITIVE_POWER_LOWER_BOUND_UNKNOWN
OPEN_GATE_03=MATCHING_HALF_POWER_LOWER_BOUND_UNKNOWN
OPEN_GATE_04=STRICT_SUB_SQRT_WHOLE_FAMILY_UPPER_UNKNOWN
OPEN_GATE_05=HALF_POWER_CAUSAL_MECHANISM_UNKNOWN
OPEN_GATE_06=MOVING_FAMILY_UNIFORMITY_UNKNOWN
OPEN_GATE_07=GROWING_MODULUS_SIEVE_UNIFORMITY_UNKNOWN
OPEN_GATE_08=STAGE24_GLOBAL_INTERACTION_SIGN_UNKNOWN
OPEN_GATE_09=SECOND_ORDER_STAGE22_STAGE23_INTERACTION_SIGN_UNKNOWN
OPEN_GATE_10=SURVIVOR_RATIO_LEADING_CONSTANT_UNKNOWN
OPEN_GATE_11=DIRECTIONAL_STAGE19_ASYMPTOTICS_UNKNOWN
```

## NEXT_STAGE_QUESTIONS

- Stage25 (`Stage16 -> Stage19`) should consume the current infinite lower interface rather than the historical constant floor.
- Stage26 (`Stage18 -> Stage20`) must keep the Stage24 space-square cost distinct from the new third-face condition.
- Stage27 (`Stage16 -> Stage20`) should not compose Stage22 and Stage26 losses multiplicatively without an explicit interaction theorem.
- Stage28 should use the Stage24 cross-ratio and arithmetic-stratum heterogeneity as interaction evidence, while preserving the unresolved global sign.
- Any future perfect-cuboid endpoint remains outside Stage24 and is not decided here.

## Arsenal and bundle decisions

```text
SELF_CONTAINED_BUNDLE_REQUIRED=true
SELF_CONTAINED_BUNDLE_DECISION=YES
SELF_CONTAINED_BUNDLE_MATERIALIZED=true
SELF_CONTAINED_BUNDLE_PATH=stages/stage24/final.md
ARSENAL_PROMOTION_REQUIRED=true
ARSENAL_PROMOTION_DECISION=YES
ARSENAL_PROMOTION_MATERIALIZED=true
ARSENAL_PROMOTION_PATH=docs/stage24-arsenal-promotion.md
AGGRESSIVE_SEARCH_LEDGER_REQUIRED=true
AGGRESSIVE_SEARCH_LEDGER_MATERIALIZED=true
AGGRESSIVE_SEARCH_LEDGER_PATH=stages/stage24/24-70/aggressive-search-ledger.md
```

The arsenal promotion is justified because Stage24 introduces reusable material not present at the historical Stage19 closeout: the mixed-parity C17 infinite construction, the current two-sided `M2 -> N2` survivor interface, and the degree-two space-square thin-cover route with an explicit non-square proof.

## SYNTHESIS_STOP_REASON

All bounded deductions available from the audited checkpoint10-60 stack and the audited Stage23 post-Stage24 backflow have been taken. Improving the polynomial exponent, proving a positive-power lower bound, finding a strict sub-square-root whole-family upper, resolving the interaction sign, or identifying the half-power mechanism would require a substantially new theorem or a new research sublane rather than further algebraic synthesis.

```text
KNOWN_RESULTS=COMPLETE_THROUGH_AUDITED_CHECKPOINT60_PLUS_AUDITED_STAGE23_BACKFLOW
ADDITIONAL_DEDUCTIONS=FOUR_MATERIALIZED
CAUSAL_SYNTHESIS=MATERIALIZED
LOWER_STAGE_REINTERPRETATIONS=MATERIALIZED_WITHOUT_AUDIT_REVOCATION
REFINEMENT_CANDIDATES=MATERIALIZED
NEW_HEURISTICS=FINITE_ONLY_NOT_PROMOTED
OPEN_GATES=MATERIALIZED
NEXT_STAGE_QUESTIONS=MATERIALIZED
SYNTHESIS_STOP_REASON=FURTHER_PROGRESS_REQUIRES_NEW_THEOREM_OR_NEW_RESEARCH_SUBLANE
SYNTHESIS_STOP_RULE_SATISFIED=YES
FINITE_DATA_USED_AS_ASYMPTOTIC_PROOF=false
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_REQUIRED=true
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage24-audit
```
