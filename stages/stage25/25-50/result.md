# Stage25-50 — deep lower/construction checkpoint

EVIDENCE_LEVEL=PROVED_CANDIDATE_REQUIRING_FRESH_AUDIT
CHECKPOINT=50
STATUS=PROVED_SUBMITTED_FOR_FRESH_AUDIT
STAGE=Stage25
TRANSITION=Stage16->Stage19

## 1. Main candidate result

The audited entering lower was

\[
N_2(B)\gg\sqrt{\log B}.
\]

Deep sublane `Stage25-r501` opens a different construction mechanism: a one-rational-parameter nearly-perfect-cuboid family, homogenized into the exact primitive/canonical Stage19 population and counted by rational parameter height.

Subject to fresh audit, it proves

\[
\boxed{N_2(B)\gg B^{1/4}.}
\]

This is a strict positive-power lower bound and supersedes the logarithmic lower.

Combined with the audited upper,

\[
\boxed{B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.}
\]

No matching half-power lower or true exponent is claimed.

## 2. Stage25 endpoint ratio

The audited Stage21 source interface is

\[
M_1(B)\sim \frac{3}{4\pi^2}B^2\log B.
\]

Therefore the new lower candidate gives

\[
\boxed{
\frac{N_2(B)}{M_1(B)}
\gg B^{-7/4}(\log B)^{-1}.
}
\]

Together with the audited checkpoint40 upper,

\[
\boxed{
B^{-7/4}(\log B)^{-1}
\ll \frac{N_2(B)}{M_1(B)}
\ll_\varepsilon B^{-3/2+\varepsilon}(\log B)^{-1}.
}
\]

The ratio still tends to zero, while the target grows by a positive power.

## 3. Construction mechanism in plain form

For coprime positive `m,n`, one homogeneous degree-eight family is

\[
A=16m^2n^2(m^4-9n^4),
\]
\[
B=(m^4-10m^2n^2+9n^4)(m^4+2m^2n^2+9n^4),
\]
\[
C=4mn(m^2+3n^2)(m^4-10m^2n^2+9n^4).
\]

It has exact integer diagonals

\[
D_{AC}=4mn(m^2+3n^2)(m^4-2m^2n^2+9n^4),
\]
\[
D_{BC}=(m^4-n^4)(m^4-81n^4),
\]
\[
D=m^8+46m^4n^4+81n^8,
\]

with

\[
A^2+C^2=D_{AC}^2,
\quad B^2+C^2=D_{BC}^2,
\quad A^2+B^2+C^2=D^2.
\]

On the fixed cone

\[
\frac72<\frac mn<4
\]

one has `0<B<C<A`, so canonicalization is fixed.

Primitive reduction by `g=gcd(A,B,C)` preserves all three displayed integer diagonals because `g` divides each corresponding square root prime-by-prime.

## 4. Exactly-two mask

The remaining face `(A,B)` is square only on

\[
w^2=P(t),\qquad t=m/n,
\]

where

\[
P(t)=t^{16}-16t^{14}+316t^{12}-112t^{10}-3290t^8
-1008t^6+25596t^4-11664t^2+6561.
\]

The committed mod-5 Bezout certificate proves `P` squarefree over `Q`; hence the smooth projective curve has genus seven. Faltings therefore leaves only finitely many rational `t` for which the third face is rational.

Removing this finite set leaves exactly-two-face Stage19 boxes.

## 5. Counting mechanism

Choose

\[
m=4n-k,\qquad 1\le k<n/2,\qquad \gcd(k,n)=1.
\]

Then `7/2<m/n<4` and `gcd(m,n)=1`. For each `n>2` there are `phi(n)/2` admissible `k`, so reduced rational parameters with numerator/denominator size at most `T` number `gg T^2`.

The space diagonal satisfies

\[
D\le128T^8.
\]

The similarity map has bounded fibers: the invariant

\[
A/D=16t^2(t^4-9)/(t^8+46t^4+81)
\]

has degree at most eight, so one primitive canonical box receives at most eight parameter values.

Thus `gg T^2` parameters below height `O(T^8)` give

\[
N_2(B)\gg B^{2/8}=B^{1/4}.
\]

Full proof ledger: `r501-parametric-positive-power.md`.

## 6. Immediate backflow consequences if fresh audit passes

These consequences are algebraic corollaries of the new numerator lower and existing audited denominator asymptotics. They are recorded now but should not rewrite frozen upstream files until fresh audit accepts the construction.

### Stage24 lower ratio upgrade

Since

\[
M_2(B)\sim C_{M_2}B(\log B)^5,
\]

we get

\[
\boxed{
\frac{N_2}{M_2}\gg B^{-3/4}(\log B)^{-5}.
}
\]

This supersedes the previous logarithmic-family lower scale.

### Stage23 lower ratio upgrade

Since

\[
N_1(B)\sim \frac{\kappa}{24\pi}B(\log B)^3,
\]

we get

\[
\boxed{
\frac{N_2}{N_1}\gg B^{-3/4}(\log B)^{-3}.
}
\]

### Stage24 ambient-space interaction sign

The Stage16S ambient space-survival baseline is

\[
S_0(B)=N_S^{all}(B)/U(B)\asymp B^{-1}.
\]

With

\[
S_2(B)=N_2(B)/M_2(B)\gg B^{-3/4}(\log B)^{-5},
\]

one obtains

\[
\boxed{
J_2(B)=S_2(B)/S_0(B)\gg B^{1/4}(\log B)^{-5}\to\infty.
}
\]

Thus the previously unresolved global interaction sign would become rigorously positive.

### Cross-ratio / order-of-conditions sign

The audited one-face space-survival law is

\[
S_1(B)=N_1(B)/M_1(B)\asymp B^{-1}(\log B)^2.
\]

Hence

\[
\boxed{
I(B)=\frac{S_2(B)}{S_1(B)}
\gg B^{1/4}(\log B)^{-7}\to\infty.
}
\]

So the second-order interaction sign, previously unresolved, would also become positive. Full causal interpretation remains checkpoint60 work; checkpoint50 records only the forced algebraic consequence.

## 7. Deep-search lane status

This checkpoint was intentionally run deeper than the minimum required lower reuse.

```text
LOWER_LANE_A=Meskhishvili_first_parametrization_positive_power:BREAKTHROUGH_CANDIDATE
LOWER_LANE_B=Meskhishvili_third_parametrization_same_degree8:IDENTIFIED_NO_EXPONENT_GAIN_YET
LOWER_LANE_C=Meskhishvili_second_parametrization_degree12:WEAKER_HEIGHT_EXPONENT
LOWER_LANE_D=Yoshida_face_cuboid_elliptic_surface:OPEN_FOR_POSSIBLE_HIGHER_DIMENSION_COUNT
LOWER_LANE_E=Stage24_symmetric_multiplier_k_family:OPEN_FOR_RANK_UNIFORMITY_OR_MULTI_K_AGGREGATION
LOWER_LANE_F=common_squarefree_core_slices:OPEN_NO_NEW_GLOBAL_COUNT_YET
```

Because lane A already changes the theorem class from logarithmic to positive-power, checkpoint50 is submitted for fresh audit before attempting to stack unreviewed stronger claims. If audit accepts it, later work can continue the open lanes without needing to redo lane A.

## 8. Numerical/reuse policy

No census extension is used.

```text
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R02,NUM-R03
NUM_POPULATION_MATCH=ADAPTER_PROVED
NUM_EVIDENCE_LEVEL=REGRESSION_ONLY_FOR_NEW_PARAMETRIC_FAMILY
NUM_NEW_COMPUTATION_JUSTIFIED=TARGETED_EXACT_IDENTITY_AND_SQUAREFREE_CERTIFICATE_ONLY
FINITE_DATA_USED_AS_PROOF=false
```

## 9. Literature boundary

Meskhishvili 2015 supplies the rational formula provenance, and Yoshida 2026 independently confirms the broad elliptic-curve structure and infinitude of rational face-cuboid similarity classes. Neither is used as a substitute for the exact Stage19 adapter, primitive reduction, exactly-two mask, height count, or bounded multiplicity proof.

No mathematical novelty claim is made for rational face cuboids or the one-parameter NPC formulas.

## 10. Exit

```text
DISCOVERY_CHECKPOINT=Stage25-50
DEEP_RESEARCH_MODE=true
C17_LOWER_REUSED=true
STAGE25_SPECIFIC_LOWER_UPGRADE_SEARCH=BREAKTHROUGH_CANDIDATE
OLD_LOWER=N2(B)>>sqrt(log B)
NEW_LOWER_CANDIDATE=N2(B)>>B^(1/4)
POSITIVE_POWER_LOWER_BOUND_CANDIDATE=true
POSITIVE_POWER_EXPONENT_CANDIDATE=1/4
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
STAGE25_RATIO_LOWER_CANDIDATE=B^(-7/4)(log B)^(-1)
STAGE24_RATIO_LOWER_BACKFLOW_CANDIDATE=B^(-3/4)(log B)^(-5)
STAGE23_RATIO_LOWER_BACKFLOW_CANDIDATE=B^(-3/4)(log B)^(-3)
AMBIENT_INTERACTION_SIGN_BACKFLOW_CANDIDATE=POSITIVE_DIVERGENT
CROSS_RATIO_SIGN_BACKFLOW_CANDIDATE=POSITIVE_DIVERGENT
HISTORY_SUPERSESSION_BACKFLOW_REQUIRED_AFTER_AUDIT_PASS=true
FORMULA_SUBSTITUTION_ONLY=false
FINITE_DATA_USED_AS_PROOF=false
EXPLORATION_EVIDENCE_COMPLETE=true
AUDIT_REQUIRED=true
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=50
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage25-audit
CODEX_REQUIRED=false
```
