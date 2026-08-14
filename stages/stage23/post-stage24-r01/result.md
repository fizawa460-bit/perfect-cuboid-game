# Stage23 post-Stage24 reinvestigation R01

```text
LANE=STAGE23_POST_STAGE24_REINVESTIGATION_R01
STATUS=SUBMITTED_FOR_FRESH_AUDIT
HISTORICAL_STAGE23_PASS_REVOKED=false
SOURCE_STAGE=Stage17
TARGET_STAGE=Stage19
UPSTREAM_NEW_INPUT=Stage24 checkpoint50/60 audited PASS
```

## 1. Why Stage23 is being revisited

Historical Stage23 closed correctly with the audited upper-side transition

\[
\frac{N_2(B)}{N_1(B)}\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-3}\to0,
\]

but at that time the only certified target lower statement was a finite constant floor. Stage24 checkpoint50 later proved

\[
\boxed{N_2(B)\gg\sqrt{\log B}},
\]

and checkpoint60 was subsequently audited PASS and merged with the resulting interaction synthesis. This lane does not revoke the historical Stage23 audit. It imports the later theorem and asks what Stage23 can now say that it could not say at closeout.

## 2. Frozen population contract

`N1(B)` counts primitive canonical `0<a<b<c`, `gcd(a,b,c)=1` cuboids with integral space diagonal `d=R<=B` and exactly one integral face diagonal.

`N2(B)` counts the same primitive/canonical/cutoff population with exactly two integral face diagonals.

The strata are disjoint. Therefore `N2/N1` remains an adjacent-stratum population-size ratio, not a literal survival probability for a fixed box.

Stage17 gives

\[
N_1(B)\sim c_1 B(\log B)^3,
\qquad c_1=\frac{\kappa}{24\pi}>0.
\]

## 3. New two-sided Stage23 ratio window

From the audited Stage24 lower theorem and the Stage17 asymptotic,

\[
N_2(B)\gg\sqrt{\log B},
\qquad
N_1(B)\asymp B(\log B)^3,
\]

so

\[
\boxed{
\frac{N_2(B)}{N_1(B)}
\gg B^{-1}(\log B)^{-5/2}.
}
\]

Combining this with the historical audited Stage23 upper bound gives

\[
\boxed{
B^{-1}(\log B)^{-5/2}
\ll
\frac{N_2(B)}{N_1(B)}
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-3}.
}
\]

Consequently Stage23 now has the rigorous qualitative classification

```text
SOURCE_POPULATION=N1(B)~c1*B*(log B)^3
TARGET_ZERO_DENSITY=true
TARGET_UNBOUNDED=true
TRANSITION_CLASS=ZERO_DENSITY_WITH_INFINITE_TARGET
POSITIVE_POWER_TARGET_LOWER_BOUND=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
HALF_POWER_INTRINSIC_STATUS=UNRESOLVED
```

The new lower bound has polynomial exponent zero and does not match the inherited half-power upper.

## 4. A specific source-host overlap channel is now quantitatively unbounded

Stage17's source-host overlap notation includes

\[
A_{ab,ac},\qquad A_{ab,bc},\qquad A_{ac,bc},
\]

with each pair overlap `o(B(log B)^3)`.

The audited mixed-parity `C17` construction from Stage24 has

\[
e=4pq,\qquad x=4p^2-q^2,\qquad y=4q^2-p^2,
\]

and in its physical cone the canonical ordering is

\[
(a,b,c)=(x,y,e),\qquad 0<a<b<c.
\]

Its two guaranteed integral faces are

\[
a^2+c^2=(4p^2+q^2)^2,
\qquad
b^2+c^2=(4q^2+p^2)^2.
\]

After removing the finite genus-five third-face-square exception set, all remaining family members are exactly-two Stage19 objects with the common edge `c`. The Stage24 height argument supplies `gg sqrt(log B)` such objects below `R<=B`. Hence

\[
\boxed{N_{2,c}(B)\gg\sqrt{\log B}},
\]

where `N_{2,c}` denotes the exactly-two target stratum whose integral faces are `ac` and `bc`. In particular,

\[
\boxed{A_{ac,bc}(B)\gg\sqrt{\log B}}.
\]

Together with the frozen Stage17 overlap theorem,

\[
\boxed{
\sqrt{\log B}\ll A_{ac,bc}(B)=o(B(\log B)^3).
}
\]

Thus the pair-overlap mechanism used in the original Stage23 causal proof is not merely a formal lower-order container: at least one named overlap channel is provably infinite and quantitatively populated.

This does **not** imply that `A_ac,bc` has order `sqrt(log B)`, nor that the `c`-shared direction dominates the full Stage19 population.

## 5. Updated causal interpretation

Historical Stage23 described the source as an already-space-integral nested Pythagorean chain

\[
x^2+y^2=p^2,\qquad p^2+z^2=d^2,
\]

and the new target requirement as one additional cross-leg relation

\[
x^2+z^2=q^2
\quad\text{or}\quad
y^2+z^2=q^2.
\]

That description remains correct. The new lower theorem strengthens it:

1. the added cross-leg compatibility sends the dominant exactly-one source stratum into lower-order pair-overlap loci, proving zero density;
2. one such pair-overlap channel, `A_ac,bc`, is nevertheless provably infinite;
3. arithmetic subfamilies are heterogeneous: the historical odd/odd Stage15-2 slice has zero space lifts, while the mixed-parity `C17` slice has infinitely many;
4. therefore the transition is not explained by a uniform local impossibility.

```text
SOURCE_HOST_PAIR_OVERLAP_LOWER_ORDER=true
SPECIFIC_PAIR_OVERLAP_CHANNEL_UNBOUNDED=true
SPECIFIC_CHANNEL=A_ac,bc
UNIFORM_LOCAL_DEATH_EXPLANATION=false
ARITHMETIC_STRATUM_HETEROGENEITY_PROVED=true
```

## 6. Stage22 comparison after the lower breakthrough

Stage22, before imposing space integrality, has the sharp adjacent-stratum law

\[
\frac{M_2(B)}{M_1(B)}
\sim C_{22}\frac{(\log B)^4}{B},
\qquad C_{22}>0.
\]

Stage23, after space is already present, now has

\[
B^{-1}(\log B)^{-5/2}
\ll\frac{N_2}{N_1}
\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-3}.
\]

Define the exact second-order interaction cross-ratio

\[
\mathcal I(B)
=
\frac{N_2/N_1}{M_2/M_1}.
\]

Then the audited Stage24-60 algebra gives

\[
\boxed{
(\log B)^{-13/2}
\ll \mathcal I(B)
\ll_\varepsilon B^{1/2+\varepsilon}(\log B)^{-7}.
}
\]

These bounds straddle `1`. Therefore current theorems do not determine whether pre-imposed space integrality globally makes the second-face adjacent-stratum ratio asymptotically larger or smaller than in the no-space host.

```text
SPACE_PRECONDITION_SECOND_FACE_INTERACTION_SIGN=UNRESOLVED
INDEPENDENCE_CLAIMED=false
POSITIVE_INTERACTION_CLAIMED=false
NEGATIVE_INTERACTION_CLAIMED=false
```

## 7. Double-charge firewall

- Space integrality is already present in every Stage17 source object and is not charged again as the new Stage23 condition.
- `N2/N1` and `M2/M1` compare disjoint adjacent strata; neither is a literal objectwise conditional probability.
- The Stage24 `C17` family supplies a target lower witness, not a positive proportion of the target bulk.
- The squareclass sieve and thin-cover arguments are not multiplied into the inherited half-power upper.
- The Stage21 `(log B)^2` one-face space enhancement is not inserted as a factor into the Stage23 ratio.

```text
DOUBLE_CHARGE_CHECK=PASS
```

## 8. Current frontier

The strongest post-Stage24 Stage23 status is

```text
N2_OVER_N1_LOWER=B^-1*(log B)^(-5/2)
N2_OVER_N1_UPPER=B^(-1/2+epsilon)*(log B)^(-3)
TARGET_UNBOUNDEDNESS_PROVED=true
TARGET_ZERO_DENSITY_PROVED=true
SPECIFIC_OVERLAP_LOWER=A_ac,bc(B)>>sqrt(log B)
POSITIVE_POWER_LOWER_BOUND_PROVED=false
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
HALF_POWER_CAUSAL_MECHANISM_IDENTIFIED=false
PERFECT_CUBOID_CONCLUSION=NONE
FINITE_DATA_USED_AS_PROOF=false
```

A sharper Stage23 result now requires either a stronger Stage19 lower theorem, a stronger target upper theorem, or a direct uniform count for the source-host cross-leg compatibility. The historical Stage23 theorem remains valid; this document is a later theorem-strengthening supplement.

```text
AUDIT_REQUIRED=true
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage23-audit
```
