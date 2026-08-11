# Stage14-Work-buX33 — outer physical support versus fixed-residue prime occupancy

## Status

`COMPLETE_OUTER_SUPPORT_EXISTENCE_VERSUS_FIXED_RESIDUE_PRIME_OCCUPANCY_ADAPTER_NOGO`

Starts from latest merged main

```text
eb2d64f771ebff9ce1c1a829ecbf032a7a4cbac4
```

and consumes only merged theorem sources:

- merged `Stage14-Work-btX32`;
- merged mainline through `Stage14-4fp`;
- merged s-route through `Stage14-s7-98`;
- merged fixed-U t-route through `Stage14-t136`, including completed merged `Stage14-tH30`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Gate

The normal Work-btX32 revisit condition was approximately

```text
4fp + s7-98 + t135.
```

All three are merged, and fixed-U has advanced further through `t136+tH30`. Therefore

```text
STAGE14_WORK_TOOLBOX_X=RUN
RUN_TRIGGER=normal_revisit_plus_material_tH30_receiver_change
```

This run is `Stage14-Work-buX33`.

## 2. Global/main and s: inner unitary multiplicity is exhausted

Merged `4fn..4fp` proves that on both complementary-dilation scales the short unitary-divisor witness fiber over one outer point has size only `B^o(1)`.

For fixed complementary dilation `E=E0`, define

```text
A_E0(m)=1
```

iff at least one unitary divisor witness `u||m` lies in the transported short physical interval and satisfies the retained canonical/reverse physical predicate.

The weighted incidence and accepted outer support are exponent-equivalent:

```text
I_E0 = B^o(1) * #{m : A_E0(m)=1}
```

in the fixed-power ledger sense.

For polynomial `E`, define analogously

```text
A_poly(E,m)=1
```

iff at least one physical unitary-divisor witness exists. Then the full inner witness multiplicity again contributes only `B^o(1)` per outer pair `(E,m)`.

Hence the mainline heavy receiver is exactly

```text
FixedComplementaryDilationOuterSupportOfPhysicalShortUnitaryDivisorExistence
OR
PolynomialComplementaryDilationOuterPairSupportOfPhysicalShortUnitaryDivisorExistence.
```

Merged `s7-96..98` is a same-packet refinement of this receiver:

- fixed `E`: short unitary-divisor incidence weighted by the canonical/reverse completion Boolean;
- polynomial `E`, subpolynomial primitive product `m`: exact `(m,u)` freezes and all polynomial entropy lies in outer `E`;
- polynomial `E`, polynomial `m`: both `(E,m)` stay polynomial and the witness predicate remains correlated.

These s branches do not multiply the mainline count. They refine how the same outer physical-existence support can be realized.

```text
GLOBAL_S_INNER_UNITARY_MULTIPLICITY_POLYNOMIAL_OBSTRUCTION_EXHAUSTED=true
GLOBAL_S_OUTER_PHYSICAL_EXISTENCE_SUPPORT_RECEIVER_PROVED=true
GLOBAL_S_MAIN_S_COUNTS_MULTIPLICABLE=false
GLOBAL_S_FIXED_E_OUTER_COORDINATE=m
GLOBAL_S_POLYNOMIAL_E_OUTER_COORDINATE=(E,m)
```

## 3. Fixed-U: the cofactor-weight obstruction is exhausted

Work-btX32 recorded a weight-location asymmetry because fixed-U still used an outer scalar norm weight `W_c(n)` against a projective prime selector.

Merged `t133..t135` opens that weight completely:

1. freeze one D4 normalization state;
2. freeze one exact Gaussian cofactor residue `rho_* (mod d)`;
3. freeze one exact Gaussian prime residue `beta_* (mod d)`;
4. unfold the scalar norm weight back to actual primitive Gaussian cofactors in one fixed open sector.

The frozen t135 object is therefore an explicit primitive Gaussian cofactor × Gaussian-prime reciprocal hyperbola with ordinary fixed residue classes.

Completed `tH30` independently audits this exact snapshot and proves the previous tH29 opaque-cofactor / Type-I--II obstruction is no longer the active issue. It nevertheless finds no unconditional theorem for the full family because two prime-side problems remain:

- arbitrary endpoint-short prime intervals;
- individual `d=B^o(1)` fixed Gaussian residue classes in long headroom, including possible exceptional real-character bias.

Merged `t136` consumes this audit and reduces the receiver to

```text
EndpointShortFixedGaussianResiduePrimeOccupancyDeficit
OR
LongHeadroomIndividualSubpolynomialModulusFixedGaussianResiduePrimeOccupancyBias.
```

Thus the earlier Work-btX32 physical-weight-location asymmetry is superseded as the fixed-U final obstruction.

```text
FIXED_U_OPAQUE_COFACTOR_WEIGHT_OBSTRUCTION_EXHAUSTED=true
FIXED_U_TYPE_I_II_COFACTOR_ADAPTER_OBSTRUCTION_EXHAUSTED=true
FIXED_U_RECEIVER_RELOCATED_TO_PRIME_SIDE_ONLY=true
TH30_COMPLETE_CONSUMED=true
TH30_DIRECT_FULL_TARGET_THEOREM_APPLICABLE=false
```

## 4. Common support/occupancy language

After these reductions, both sides can be written abstractly as a charged outer family plus an inner arithmetic witness selector.

Global/s:

```text
outer x = m or (E,m),
accept x iff exists a physically admissible short unitary-divisor witness u.
```

Fixed-U:

```text
outer x = primitive Gaussian cofactor gamma,
acceptance/deficit is measured by primes pi in one fixed residue class
inside the reciprocal cutoff N(gamma)N(pi)<=X_U.
```

This yields a legitimate common structural statement:

```text
COMMON_OUTER_FAMILY_INNER_ARITHMETIC_WITNESS_LANGUAGE_PROVED=true
COMMON_POLYNOMIAL_OBSTRUCTION_RELOCATED_AWAY_FROM_SUBPOLYNOMIAL_INNER_FIBER=true
```

But the selectors are not the same arithmetic object.

Global/s is an existential unitary-divisor event on an integer factorization with a correlated canonical/reverse Boolean. Fixed-U is a prime occupancy discrepancy in one ordinary Gaussian residue class with endpoint/long-headroom prime-distribution issues.

The baselines, measures, inner witness species, and quantifier orders remain different.

Therefore

```text
DIRECT_OUTER_SUPPORT_EXISTENCE_TO_FIXED_RESIDUE_PRIME_OCCUPANCY_ADAPTER_NOGO_AT_CURRENT_LEVEL=true
COMMON_ARITHMETIC_INNER_SELECTOR_ADAPTER_PROVED=false
COMMON_PHYSICAL_MEASURE_ADAPTER_PROVED=false
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
GLOBAL_FIXED_U_SAVING_CROSS_PROMOTED=false
```

## 5. Supersession ledger

Work-btX32 target:

```text
OuterInnerPhysicalWeightFactorizationAdapterOrNoGo
```

is now resolved asymmetrically:

- global/s: physical weight remains inside an existential physical witness predicate, but inner multiplicity is exhausted and the receiver is outer support;
- fixed-U: cofactor-side weight is explicitly unfolded and no longer an obstruction; the receiver is prime-side occupancy only.

Hence

```text
BTX32_WEIGHT_LOCATION_AS_FINAL_COMMON_OBSTRUCTION_SUPERSEDED=true
COMMON_WEIGHT_LOCATION_ADAPTER_NO_LONGER_THE_MINIMAL_CROSS_ROUTE_QUESTION=true
```

The new minimal cross-route question is whether an outer physical-existence support deficit can be related, with charged measure preserved, to a fixed-residue prime occupancy deficit. No such bridge is merged.

## 6. H decisions

Global/main heavy and s routes still require internal opening of the existential physical predicate before a stable new weighted-unitary/Ford theorem request exists.

Fixed-U has just consumed `tH30`; its remaining two mechanisms are exactly the negative boundary exposed by that audit, so a new `tH31` is premature before `t137+` materially changes one of them.

```text
MAINLINE_H_NEEDED=true
NEW_HEAVY_MAIN_H_NEEDED=false
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=false
TH30_COMPLETE_CONSUMED=true
TH31_NEEDED=false
WHOLE_MAINLINE_BLOCKED_BY_H=false
```

`MAINLINE_H_NEEDED=true` refers only to already-open non-heavy mainline theorem gates and is not a new heavy H request.

## 7. Locks

```text
TOOLBOX_COMPONENT_COMPLETE=true
X_COMPONENT_COMPLETE=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_GLOBAL_RECEIVER=FixedComplementaryDilationOuterSupportOfPhysicalShortUnitaryDivisorExistence_OR_PolynomialComplementaryDilationOuterPairSupportOfPhysicalShortUnitaryDivisorExistence
CURRENT_FIXED_U_RECEIVER=SharedUEndpointShortFixedGaussianResiduePrimeOccupancyDeficit_OR_LongHeadroomIndividualSubpolynomialModulusFixedGaussianResiduePrimeOccupancyBias
GLOBAL_S_INNER_UNITARY_MULTIPLICITY_POLYNOMIAL_OBSTRUCTION_EXHAUSTED=true
GLOBAL_S_OUTER_PHYSICAL_EXISTENCE_SUPPORT_RECEIVER_PROVED=true
FIXED_U_OPAQUE_COFACTOR_WEIGHT_OBSTRUCTION_EXHAUSTED=true
FIXED_U_RECEIVER_RELOCATED_TO_PRIME_SIDE_ONLY=true
COMMON_OUTER_FAMILY_INNER_ARITHMETIC_WITNESS_LANGUAGE_PROVED=true
BTX32_WEIGHT_LOCATION_AS_FINAL_COMMON_OBSTRUCTION_SUPERSEDED=true
DIRECT_OUTER_SUPPORT_EXISTENCE_TO_FIXED_RESIDUE_PRIME_OCCUPANCY_ADAPTER_NOGO_AT_CURRENT_LEVEL=true
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
MAINLINE_H_NEEDED=true
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=false
TH31_NEEDED=false
NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false
NEXT_REVISIT_CONDITION=merged 4fs+s7-101+t139 approximately, or earlier material theorem/adapter/exponent/receiver/H trigger
```

## 8. Next integrated target

```text
PhysicalExistenceSupportVersusFixedResiduePrimeOccupancyTheoremIntersectionOrNoGo
```

Normal revisit is approximately

```text
4fs + s7-101 + t139
```

with early RUN allowed for a material theorem, adapter, exponent, receiver, or H change.
