# Stage14-t94 — antipodal quotient occupancy reduction

## Status

`COMPLETE_ANTIPODAL_QUOTIENT_OCCUPANCY_REDUCTION`

Consumes merged t93 and merged frozen tH26. No H target is reopened.

Let the generic orientation cube be `Omega_r={+-1}^r`, with antipodal involution `epsilon -> -epsilon`. The t93 survivor is the even part

```text
C_even(epsilon)=(C(epsilon)+C(-epsilon))/2.
```

Hence it descends exactly to

```text
Omega_r/{+-1},
```

which has `2^(r-1)` classes for `r>=1`. Its character group is exactly the even-cardinality Walsh spectrum. Thus the odd spectrum is gone permanently and the live centered spectrum is a character system on the antipodal quotient.

For each antipodal pair define the normalized pair occupancy

```text
omega_pair([epsilon]) = C_even(epsilon)/C_max,
0 <= omega_pair <= 1,
```

where `C_max` is the charged-once complete physical majorant for the fixed packet/cell. The principal cube mean is the quotient average

```text
mu_U = average_[epsilon] omega_pair([epsilon]) * C_max.
```

Therefore any fixed-power occupancy-deficit layer

```text
omega_pair = B^(-delta+o(1)), delta>0,
```

inherits the merged 4dj positive-density estimate and contributes at exponent at most

```text
1/2-delta.
```

Consequently any square-root-saturating t-route sequence must lie in the near-maximal pair-occupancy regime

```text
omega_pair = B^(-o(1)).
```

This is a localization statement, not a uniform strict sub-square-root theorem. The centered even quotient spectrum can still have full degree on the quotient and the near-maximal principal occupancy can remain positive.

```text
ANTIPODAL_QUOTIENT_REDUCTION_PROVED=true
ODD_WALSH_SECTOR_REOPENED=false
EVEN_WALSH_CHARACTERS_DESCEND_TO_QUOTIENT=true
PAIR_OCCUPANCY_DEFICIT_FIXED_POWER_SAVING_PROVED=true
PAIR_OCCUPANCY_DEFICIT_EXPONENT=delta
SQRT_SATURATION_FORCES_NEAR_MAXIMAL_PAIR_OCCUPANCY=true
PRINCIPAL_PAIR_MEAN_ELIMINATED=false
CENTERED_EVEN_QUOTIENT_SPECTRUM_ELIMINATED=false
TH26_COMPLETE_CONSUMED=true
TH27_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT=Stage14-t95
```

Current receiver:

```text
SharedUCanonicalLPFNearMaximalAntipodalPairOccupancyPlusCenteredEvenQuotientOrientationCorrelation
```
