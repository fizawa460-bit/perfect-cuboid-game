# Stage14-t73 — consumption of completed parallel tH19 audit

The parallel tH19 audit supplied during Stage14-t73 completed with

```text
STAGE14_TH19=COMPLETE_INDEPENDENT_PELL_SMOOTH_ENERGY_AUDIT
PRIMITIVE_DIVISOR_LUCAS_PELL_APPLICABLE_PARTIALLY=true
PRIMITIVE_DIVISOR_FORCES_CANONICAL_LPF=false
PRIMITIVE_DIVISOR_FORCES_V_ELL_ONE=false
PRIMITIVE_DIVISOR_FORCES_2C_LT_ELL=false
FIXED_S_SUNIT_SMOOTH_THEOREMS_AVAILABLE=true
MOVING_KAPPA_MOVING_S_UNIFORM_QUANTITATIVE_SAVING_AVAILABLE=false
PELL_UNIT_ORBIT_POLYNOMIAL_COST_EXPECTED=false
PELL_UNIT_ORBIT_COST=Bo1_COMPATIBLE
MOVING_CLASS_NUMBER_REGULATOR_UNIFORM_AVERAGE_SUFFICIENTLY_STRONG=false
SHARP_ELL_DELTA_HYPERBOLA_MUST_BE_RETAINED=true
DISTINGUISHED_LARGEST_PRIME_FILTER_MUST_BE_RETAINED=true
EXPONENT_ONE_FILTER_MUST_BE_RETAINED=true
SMOOTH_COMPANION_FILTER_MUST_BE_RETAINED=true
OFF_THE_SHELF_UNIFORM_FIXED_POWER_SAVING_PROVED=false
GENERIC_PELL_COUNT_IS_NOT_MINIMAL_RECEIVER=true
PREFERRED_RECEIVER=SmallOddKappaCanonicalLargestPrimePellSmoothEnergy
NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false
CURRENT_SHARED_WHOLE_FAMILY_EXPONENT=5/8
```

## Relation to t73

tH19 and t73 agree that a bare Pell count is not the minimal receiver.  tH19 already found the unit-orbit cost compatible with `B^o(1)`.  t73 makes that fixed-norm statement exact and uniform by avoiding class-number averaging altogether:

```text
# fixed norm fibers
<= (# ideal divisors of (n)) * (# unit translates in the height box)
<= tau(n)^2 * O(log B)
= B^o(1).
```

Thus the tH19 negative finding

```text
MOVING_CLASS_NUMBER_REGULATOR_UNIFORM_AVERAGE_SUFFICIENTLY_STRONG=false
```

does not obstruct a fixed norm value; class number never enters that fiber count.  It remains relevant only as evidence that one should not expect an off-the-shelf theorem to average the entire moving family automatically.

The primitive-divisor / Lucas-Pell mechanism is likewise retained only as a possible tool for the **moving value** average.  tH19 correctly shows that primitive divisors by themselves do not force any of

```text
ell = LPF_odd(P+P-),
v_ell(P-)=1,
2c<ell.
```

Therefore those filters, together with the sharp `ell*delta` hyperbola and the smooth companion, remain mandatory.

## Post-t73 preferred receiver

The tH19 preferred receiver is narrowed from

```text
SmallOddKappaCanonicalLargestPrimePellSmoothEnergy
```

to

```text
SmallOddKappaMovingCanonicalLargestPrimeSmoothNormValueEnergy.
```

The word `Pell` is intentionally removed from the minimal name: fixed-norm Pell orbit multiplicity is now proved `B^o(1)`.  The remaining issue is the average over moving physical norm values after fixed `(kappa,beta)` conditioning.

```text
TH19_PARALLEL_AUDIT_CONSUMED=true
TH19_PREFERRED_RECEIVER_PRE_T73=SmallOddKappaCanonicalLargestPrimePellSmoothEnergy
TH19_PREFERRED_RECEIVER_POST_T73=SmallOddKappaMovingCanonicalLargestPrimeSmoothNormValueEnergy
TH19_FIXED_NORM_PELL_ORBIT_SUBPROBLEM_SUPERSEDED=true
TH19_CLASS_NUMBER_FIXED_NORM_SUBPROBLEM_SUPERSEDED=true
TH19_UNIT_ORBIT_FIXED_NORM_SUBPROBLEM_SUPERSEDED=true
TH19_PRIMITIVE_DIVISOR_MECHANISM_RETAINED_FOR_MOVING_VALUES=true
TH19_LARGEST_PRIME_FILTER_RETAINED=true
TH19_EXPONENT_ONE_FILTER_RETAINED=true
TH19_SMOOTH_COMPANION_FILTER_RETAINED=true
TH19_SHARP_ELL_DELTA_HYPERBOLA_RETAINED=true
T_ROUTE_BLOCKED_WAITING_FOR_TH19=false
```
