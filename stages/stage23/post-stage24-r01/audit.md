# Stage23 post-Stage24 reinvestigation R01 — fresh audit

```text
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
HISTORICAL_STAGE23_PASS_REVOKED=false
ADVANCE_ALLOWED=true
MERGE_ALLOWED=true
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
```

## Scope

This audit reviews the later theorem-strengthening lane triggered by audited and merged Stage24 checkpoints 50 and 60. It does not reopen or revoke the historical Stage23 closeout.

## Source-interface checks

- Stage17 remains the exact primitive/canonical integral-space exactly-one-face source under `R=d<=B`, with
  `N1(B) ~ kappa/(24*pi) B(log B)^3`, `kappa>0`.
- Stage17's raw pair-overlap channels satisfy
  `A_ab,ac`, `A_ab,bc`, `A_ac,bc`, `A3 = o(B(log B)^3)`.
- Historical Stage23 still supplies
  `N2/N1 <<_epsilon B^(-1/2+epsilon)(log B)^(-3)`.
- Stage24 checkpoint50 is audited and merged with
  `N2(B) >> sqrt(log B)` and an infinite primitive mixed-parity `C17` exactly-two family.
- Stage24 checkpoint60 is audited and merged with the Stage22/23 cross-ratio bracket and the no-double-charge firewall.

All imported populations, cutoff conventions, and multiplicity semantics match. `N2/N1` remains an adjacent-stratum population-size ratio, not an objectwise survival probability.

## Ratio arithmetic

Dividing the Stage24 lower theorem by the Stage17 asymptotic gives

\[
\frac{N_2(B)}{N_1(B)}\gg B^{-1}(\log B)^{-5/2}.
\]

Together with the historical upper,

\[
B^{-1}(\log B)^{-5/2}
\ll \frac{N_2(B)}{N_1(B)}
\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-3}.
\]

Hence the target is rigorously zero-density relative to the Stage17 source and unbounded:

```text
TRANSITION_CLASS=ZERO_DENSITY_WITH_INFINITE_TARGET
TARGET_UNBOUNDEDNESS_PROVED=true
POSITIVE_POWER_TARGET_LOWER_BOUND_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
HALF_POWER_INTRINSIC_STATUS=UNRESOLVED
```

## Specific overlap-channel audit

For the audited Stage24 `C17` family,

\[
e=4pq,\quad x=4p^2-q^2,\quad y=4q^2-p^2,
\]

and on the audited physical cone

\[
1<q/p<(1+\sqrt2)/2
\]

we have `0<x<y<e`, so the canonical assignment is exactly

\[
(a,b,c)=(x,y,e).
\]

The identities

\[
x^2+e^2=(4p^2+q^2)^2,\qquad
y^2+e^2=(4q^2+p^2)^2
\]

place every such physical member in the `ac,bc` pair-overlap channel. Stage24's quantitative height/equidistribution argument already produces `gg sqrt(log B)` distinct boxes in this cone. Its genus-five third-face exception set is finite, so removing those points preserves the lower count. Therefore

\[
N_{2,c}(B)\gg\sqrt{\log B},\qquad
A_{ac,bc}(B)\gg\sqrt{\log B}.
\]

This is compatible with the frozen Stage17 upper

\[
A_{ac,bc}(B)=o(B(\log B)^3).
\]

Thus a named pair-overlap channel is now proved quantitatively unbounded while remaining lower order.

## Exact CI regression

GitHub Actions run `31852289476`, job `exact-audit`, completed successfully. It verifies the ratio exponent arithmetic and the exact witness

`(a,b,c,d)=(3927,5952,6536,9673)`

including canonical ordering, primitivity, integral `ac` and `bc` faces, non-square `ab`, and integral space diagonal.

The CI witness is regression evidence. The asymptotic lower theorem comes from the already-audited Stage24 elliptic-height argument, not from finite computation.

## Stage22 comparison and double-charge firewall

The exact cross-ratio remains

\[
\mathcal I(B)=\frac{N_2/N_1}{M_2/M_1},
\]

with audited bracket

\[
(\log B)^{-13/2}
\ll \mathcal I(B)
\ll_\varepsilon B^{1/2+\varepsilon}(\log B)^{-7}.
\]

The bounds straddle `1`, so the sign is unresolved. Space integrality is already present in the Stage17 source and is not charged again. The `C17` family is a lower witness, not bulk mass, and no local-sieve/thin-cover saving is multiplied into the inherited half-power upper.

## Final verdict

The reinvestigation is a valid theorem-strengthening supplement. It materially upgrades Stage23 from a zero-density transition with only a historical finite target floor to a zero-density comparison with a rigorously infinite target and a named quantitatively unbounded overlap channel.

```text
AUDIT_VERDICT=PASS
DISCOVERY_AUDIT_VERDICT=PASS
RATIO_LOWER_ACCEPTED=B^-1*(log B)^(-5/2)
RATIO_UPPER_ACCEPTED=B^(-1/2+epsilon)*(log B)^(-3)
TARGET_UNBOUNDEDNESS_PROVED=true
SPECIFIC_TARGET_DIRECTION_LOWER=N2,c(B)>>sqrt(log B)
SPECIFIC_OVERLAP_CHANNEL=A_ac,bc
SPECIFIC_OVERLAP_LOWER=A_ac,bc(B)>>sqrt(log B)
SPECIFIC_OVERLAP_UPPER=A_ac,bc(B)=o(B(log B)^3)
ARITHMETIC_STRATUM_HETEROGENEITY_PROVED=true
SPACE_PRECONDITION_SECOND_FACE_INTERACTION_SIGN=UNRESOLVED
POSITIVE_POWER_TARGET_LOWER_BOUND_PROVED=false
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
HALF_POWER_CAUSAL_MECHANISM_IDENTIFIED=false
PERFECT_CUBOID_CONCLUSION=NONE
FINITE_DATA_USED_AS_PROOF=false
MERGE_ALLOWED=true
```
