# Stage14-tH32 — independent safe-modulus quarter-scale Gaussian short-interval audit

## Status

`COMPLETE_PARTIAL_NEAR_FULL_POSITIVE_QUARTER_SCALE_NEGATIVE_AUDIT`

This is a clean-room audit of the frozen `Stage14-t142` target only.

```text
AUDITED_THROUGH=Stage14-t142
SOURCE_SNAPSHOT_SHA=744d5b844d9f6b6bcace141497a97fef1945e81b
TARGET_FILE=stages/stage14/14-t142/th32-target.md
TARGET_FROZEN=true
REQUESTED_OBJECT=SafeMitsuiModulusQuarterScaleFixedGaussianResidueShortIntervalPrimeOccupancy
```

No later t-stage conclusion is used.

## 1. Scale conversion

The frozen prime norm lower endpoint is

```text
x:=L_B=2*sqrt(B)=B^(1/2+o(1)).
```

A target additive width

```text
H=B^(lambda+o(1))
```

corresponds to the usual short-interval exponent

```text
H=x^(theta+o(1)),
theta=2*lambda.
```

Thus the Stage14 quarter scale `lambda=1/4` is exactly the norm short-interval scale

```text
H=x^(1/2+o(1)).
```

## 2. Kai/Mitsui retains the growing residue but is cumulative-error limited

Wataru Kai, arXiv:2209.11816, refines Mitsui's prime-element theorem by retaining the possible Siegel secondary term. For a fixed number field and modulus ideal in the pseudopolynomial range

```text
N(q) <= exp(sqrt(log X)/O_K(1)),
```

the weighted prime-element count in congruence classes and admissible convex/annulus-sector regions has an absolute error of the form

```text
O_K(N * exp(-sqrt(log N)/O_K(1))).
```

For `K=Q(i)` and `q=(d)`, the frozen safe range

```text
d <= exp(c_safe*sqrt(log B))
```

can be placed strictly inside this theorem by choosing `c_safe` sufficiently small, exactly as in completed `tH31`.

However, subtracting the cumulative theorem at `x+H` and `x` produces two absolute errors of size

```text
x * exp(-c*sqrt(log x))
```

at norm scale. The expected fixed-residue short-interval main term is only

```text
~ H / phi_K(q)
```

multiplied by the possible exceptional real-character suppression factor.

Since `phi_K(q)=exp(O(sqrt(log x)))` in the safe range and the exceptional suppression is only `x^(-o(1))`, Kai/Mitsui directly yields a lower bound after subtraction only once

```text
H >= x * exp(-c_short*sqrt(log x))
```

for a sufficiently small fixed `c_short>0` after reserving constant margin for the modulus and exceptional factor.

In `B` scale this is

```text
H >= B^(1/2) * exp(-c'_short*sqrt(log B))
  = B^(1/2-o(1)).
```

Therefore Kai/Mitsui does **not** reach any fixed exponent `lambda<1/2` merely by cumulative subtraction, and in particular does not reach `lambda=1/4`.

```text
KAI_MITSUI_GROWING_RESIDUE_COMPATIBLE=true
KAI_MITSUI_CUMULATIVE_SUBTRACTION_QUARTER_SCALE_SUFFICIENT=false
KAI_MITSUI_NEAR_FULL_SHORT_INTERVAL_THRESHOLD=B^(1/2)*exp(-c*sqrt(logB))
```

## 3. Stucky's Gaussian short-sector theorem is still above quarter scale and has no growing ordinary residue

Joshua Stucky, arXiv:2008.11325, Theorem 1.1, proves an asymptotic for Gaussian primes with simultaneous norm-short-interval and angular restrictions when

```text
theta>7/10,
delta*x^theta >= x^(7/10+epsilon).
```

For the frozen broad canonical sector, `delta` is fixed, so the norm width threshold is

```text
H >= x^(7/10+epsilon).
```

Since `x=B^(1/2+o(1))`, this comparator becomes

```text
H >= B^(7/20+epsilon).
```

Thus even after dropping the ordinary residue condition, this theorem does not reach the Stage14 quarter scale `B^(1/4)`.

More importantly for the exact target, Stucky's Hecke characters are the angular conductor-one family. The theorem does not state uniformity for one ordinary Gaussian residue modulo a growing

```text
d <= exp(c_safe*sqrt(log B)).
```

Hence `7/20` is only a useful conductor-one Gaussian-sector benchmark, not a direct certified exponent for the frozen residue target.

```text
STUCKY_CONDUCTOR_ONE_GAUSSIAN_SECTOR_B_EXPONENT=7/20+epsilon
STUCKY_REACHES_QUARTER_SCALE=false
STUCKY_GROWING_ORDINARY_RESIDUE_DIRECTLY_SUPPORTED=false
```

## 4. General Hecke zero-density / Hoheisel technology does not supply the missing exact theorem

Log-free zero-density and Deuring--Heilbronn results for Hecke `L`-functions provide the analytic ingredients behind long-range ray-class results, but no audited theorem gives an individual fixed Gaussian residue, one fixed canonical sector, pseudopolynomial modulus, and every interval of norm width `x^(1/2+o(1))` with the required lower ratio.

The available prime-ideal short-interval results under RH/GRH are conditional and are excluded by the target. Mean-value arithmetic-progression results average over moduli and/or interval locations, whereas the Stage14 target is one charged individual packet and cannot spend such averaging.

```text
INDIVIDUAL_PSEUDOPOLY_RESIDUE_HOHEISEL_AT_X_HALF_PROVED=false
MEAN_MODULUS_OR_MEAN_INTERVAL_THEOREM_DIRECTLY_APPLICABLE=false
GRH_SHORT_INTERVAL_RESULTS_ADMISSIBLE=false
```

## 5. Exceptional real character

The possible real Hecke/Siegel zero is not the reason quarter scale fails. In the Kai/Mitsui near-full threshold range, it can be retained exactly as in `tH31`: the secondary term is explicit, and in the suppressing sign its loss is only subpolynomial on the safe modulus range.

Therefore on

```text
H >= B^(1/2)*exp(-c_short*sqrt(log B))
```

the fixed-residue occupancy still satisfies

```text
T_nearfull_safe >= B^(-o(1)) M_nearfull_safe.
```

The failure below this threshold is the cumulative absolute-error / short-interval problem, not an inability to retain the exceptional character.

```text
POSSIBLE_SIEGEL_ZERO_RETAINED=true
SAFE_NEAR_FULL_ENDPOINT_FIXED_POWER_DEPLETION_RULED_OUT=true
```

## 6. Certified verdict

No existing audited unconditional theorem covers the entire frozen quarter-scale target.

For the **exact growing-residue problem**, the strongest direct threshold certified here is the Kai/Mitsui near-full pseudopolynomial defect

```text
H >= B^(1/2)*exp(-c_short*sqrt(log B))
  = B^(1/2-o(1)).
```

There is no certified fixed exponent `lambda<1/2` for the full fixed-sector + individual pseudopolynomial ordinary-residue target from the audited results.

The best Gaussian-sector short-interval comparator after dropping the residue is Stucky's

```text
lambda > 7/20.
```

This remains strictly above `1/4`.

```text
DIRECT_THEOREM_APPLICABLE=PARTIAL_NEAR_FULL_RANGE_ONLY
QUARTER_SCALE_ENDPOINT_COVERED=false
BEST_CERTIFIED_B_WIDTH_EXPONENT_FOR_EXACT_GROWING_RESIDUE_PROBLEM=1/2-o(1)
BEST_CONDUCTOR_ONE_GAUSSIAN_SECTOR_COMPARATOR_B_EXPONENT=7/20+epsilon
POSSIBLE_SIEGEL_ZERO_RETAINED=true
SAFE_NEAR_FULL_ENDPOINT_FIXED_POWER_DEPLETION_RULED_OUT=true
SAFE_ENDPOINT_FIXED_POWER_DEPLETION_RULED_OUT=false
NEXT_H_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## Primary sources checked

```text
Wataru Kai,
Notes on Mitsui's Prime Number Theorem with Siegel zeros,
arXiv:2209.11816v2.

Joshua Stucky,
Gaussian Primes in Narrow Sectors,
arXiv:2008.11325.

Jesse Thorner and Asif Zaman,
Explicit results on the distribution of zeros of Hecke L-functions,
arXiv:1510.08086.

L. Grenie, G. Molteni, A. Perelli,
Primes and prime ideals in short intervals,
arXiv:1602.02906 (conditional RH comparison only).
```

## Frozen boundary

```text
STAGE14_TH32=COMPLETE_PARTIAL_NEAR_FULL_POSITIVE_QUARTER_SCALE_NEGATIVE_AUDIT
AUDITED_THROUGH=Stage14-t142
SOURCE_SNAPSHOT_SHA=744d5b844d9f6b6bcace141497a97fef1945e81b
TARGET_FROZEN=true
DIRECT_THEOREM_APPLICABLE=PARTIAL_NEAR_FULL_RANGE_ONLY
QUARTER_SCALE_ENDPOINT_COVERED=false
BEST_CERTIFIED_B_WIDTH_EXPONENT_FOR_EXACT_GROWING_RESIDUE_PROBLEM=1/2-o(1)
POSSIBLE_SIEGEL_ZERO_RETAINED=true
SAFE_NEAR_FULL_ENDPOINT_FIXED_POWER_DEPLETION_RULED_OUT=true
SAFE_ENDPOINT_FIXED_POWER_DEPLETION_RULED_OUT=false
NEXT_H_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```
