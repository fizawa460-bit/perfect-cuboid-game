# Stage14-Work-btX32 — physical-weight location split and direct weighted-selector adapter no-go

## Status

`COMPLETE_PHYSICAL_WEIGHT_LOCATION_SPLIT_AND_DIRECT_ADAPTER_NOGO`

This integrated Work run consumes only merged theorem sources from latest main at branch start:

- merged `Stage14-Work-bsX31`;
- merged mainline `Stage14-4fk..4fm`;
- merged s-route `Stage14-s7-93..95`;
- merged fixed-U `Stage14-t132`;
- merged q14 and completed tH29 only as their existing routing/negative-theorem boundaries.

The Work gate is **RUN**. Mainline and s each accumulated three substantive merged stages. Fixed-U accumulated only `t132`, but `t132` is an early material trigger: it supersedes the moving-selected-class / real-nonreal cofactor-side receiver by a fixed cofactor class and fixed inverse prime class.

```text
TOOLBOX_COMPONENT_COMPLETE=true
X_COMPONENT_COMPLETE=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Global/s: one exact weighted unitary-divisor incidence

Merged `s7-95` writes the heavy packet exactly as

```text
I_unit
 = sum_n
   sum_{q|n}
   sum_{u||q, u in U_phys(n,q)}
     W_unit(n,q,u),

E=n/q,
```

where

```text
W_unit(n,q,u)
 = 1_{gcd(sqf(E),K_Z)=1}
   * w_res(n,u,q/u,E).
```

The changes from primitive ratio to `(n,q,u)` are bijective on accepted candidates. Thus mainline and s are still the identical charged global heavy packet, not two independent counts.

Merged `4fm` is an exact refinement of this same incidence by the scale of the complementary dilation `E=n/q`:

```text
(A) E=B^o(1),
(B) E=B^(epsilon+o(1)), epsilon>0.
```

On (A), freeze one exact `E=E0` at `B^o(1)` cost and put `m=n/E0`. Then

```text
m=uv,
gcd(u,v)=1,
u||m,
u^2/m in the transported short interval.
```

The local complementary mask at fixed `E0` is constant on a surviving cell and cannot be recharged. The remaining canonical/reverse Boolean still depends on the inner unitary-divisor coordinates.

On (B), polynomial `E` is a genuine outer variable coupled to the short unitary-divisor selector and its canonical/reverse weight.

Therefore:

```text
GLOBAL_S_WEIGHTED_UNITARY_DIVISOR_INCIDENCE_IDENTIFIED=true
MAINLINE_4FM_E_SCALE_SPLIT_APPLIES_TO_SAME_S7_95_PACKET=true
GLOBAL_S_WEIGHTED_UNITARY_COUNTS_MULTIPLICABLE=false
FIXED_E_LOCAL_COMPLEMENTARY_MASK_RECHARGE_ALLOWED=false
POLYNOMIAL_E_REMAINS_GENUINE_OUTER_CORRELATION=true
```

## 2. fixed-U: t132 moves the physical cofactor weight completely outside the prime selector

Merged `t132` freezes one exact projective cofactor class `c_*` at only `B^o(1)` cost and hence one fixed inverse projective prime class

```text
q_* = c_*^(-1) [a]^(-1).
```

The localized count and principal baseline are

```text
T_* = sum_n W_{c_*}(n) K_n(q_*),

M_* = 1/|G| sum_n W_{c_*}(n) |P_n|,
```

with

```text
0 <= W_{c_*}(n) <= B^o(1).
```

At this current level, all cofactor-side physical multiplicity is therefore an **outer scalar-norm weight**. Once `(n,c_*)` is fixed, the inner object is the count of primes in one fixed projective class up to reciprocal cutoff `X_U/n`.

This does not prove multiplicativity or regularity of `W_{c_*}(n)`. It only proves the exact location of the weight.

```text
FIXED_U_FIXED_PROJECTIVE_CLASS_LOCALIZED=true
FIXED_U_FIXED_INVERSE_PRIME_CLASS_LOCALIZED=true
FIXED_U_PHYSICAL_COFACTOR_WEIGHT_OUTER_N_ONLY=true
FIXED_U_INNER_PROJECTIVE_PRIME_SELECTOR_SEPARATED_FROM_COFACTOR_FIBER=true
```

## 3. Common template and the new obstruction

Both sides now fit the broad nonnegative weighted reciprocal-selector template

```text
sum_{outer x} sum_{inner y in S(x)} weight(x,y),
```

with polynomial outer support and reciprocal dependence of the inner selector on the outer variable.

But the **weight location is different**.

### global/s

```text
outer n (and, on polynomial-E branch, outer E),
inner q|n and u||q in a short interval,
weight W_unit(n,q,u) retains canonical/reverse dependence on the inner candidate.
```

### fixed-U

```text
outer n,
outer physical weight W_{c_*}(n),
inner prime count K_n(q_*) in one fixed projective class.
```

Thus a direct adapter would have to do at least one of the following while preserving the charged physical measure and quantifier order:

1. factor the global/s canonical/reverse Boolean from `W_unit(n,q,u)` to an outer-only function of `n` (and possibly `E`); or
2. produce an equivalent inner-dependent physical weight on the fixed-U prime selector; or
3. give a finite-fiber arithmetic map from unitary divisors in a short interval to primes in one fixed projective class, with baselines preserved.

No merged theorem supplies any of these.

```text
COMMON_NONNEGATIVE_WEIGHTED_RECIPROCAL_SELECTOR_TEMPLATE_PROVED=true
PHYSICAL_WEIGHT_LOCATION_ASYMMETRY_PROVED=true
GLOBAL_S_INNER_DEPENDENT_PHYSICAL_WEIGHT_REMAINS=true
FIXED_U_OUTER_ONLY_COFACTOR_WEIGHT_PROVED=true
DIRECT_WEIGHTED_UNITARY_TO_FIXED_PROJECTIVE_PRIME_ADAPTER_NOGO_AT_CURRENT_LEVEL=true
COMMON_PHYSICAL_WEIGHT_ADAPTER_PROVED=false
COMMON_ARITHMETIC_INNER_SELECTOR_ADAPTER_PROVED=false
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
```

This is a current-level direct no-go, not a proof that no future arithmetic adapter can exist after the two weights are opened further.

## 4. q14 / tH29 routing remains separated

On the global/s fixed-`E` branch, q14's Ford divisor-in-an-interval architecture is geometrically close, but merged `4fm` still has

```text
Q14_STEP3_CHARGED_PHYSICAL_MEASURE_BOUNDED_DISTORTION=NOT_PROVED
FORD_TRANSFER_FIXED_POWER_SAVING_PROVED=false.
```

The unitary-divisor restriction and canonical/reverse inner Boolean remain exactly the missing weight-preserving transfer issue.

On fixed-U, completed tH29 remains the negative theorem boundary for the reciprocal fixed-projective-prime family. The new t132 localization does not itself supply the distribution theorem; it makes the target sharper by fixing both projective classes.

No q14/Ford saving is cross-promoted to fixed-U, and no tH29 negative conclusion is used as a theorem about global unitary divisors.

```text
Q14_GLOBAL_S_ONLY_ROUTING_RETAINED=true
TH29_FIXED_U_NEGATIVE_BOUNDARY_RETAINED=true
Q14_TO_FIXED_U_CROSS_PROMOTION_PROVED=false
TH29_TO_GLOBAL_UNITARY_DIVISOR_CROSS_PROMOTION_PROVED=false
```

## 5. Receivers and H decisions

The integrated current receivers are

```text
CURRENT_GLOBAL_RECEIVER=
  FixedComplementaryDilationInteriorShortUnitaryDivisorCanonicalReversePhysicalIncidence
  OR
  PolynomialComplementaryDilationInteriorShortUnitaryDivisorCanonicalReversePhysicalCorrelation
  OR existing non-heavy mainline receivers

CURRENT_S_RECEIVER=
  same global heavy weighted-unitary-divisor packet after consuming the merged 4fm E-scale split
  OR existing non-heavy s/global receivers

CURRENT_FIXED_U_RECEIVER=
  SharedUFixedProjectiveCofactorClassScalarNormWeightAgainstReciprocalFixedProjectivePrimeClassDepletion
```

No new heavy/main, sH, or tH theorem request is ready yet. The two exposed physical weights must be opened internally first.

```text
MAINLINE_H_NEEDED=true
NEW_HEAVY_MAIN_H_NEEDED=false
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=false
TH30_NEEDED=false
WHOLE_MAINLINE_BLOCKED_BY_H=false
```

`MAINLINE_H_NEEDED=true` refers only to the already-existing non-heavy three-divisor / mover / diffuse H targets; the current heavy weighted-unitary branch is not H-blocked.

## 6. Next integrated target

The next useful common test is whether further arithmetic opening moves the two routes toward the same outer/inner weight factorization, or proves the separation stable:

```text
NEXT_INTEGRATED_TARGET=OuterInnerPhysicalWeightFactorizationAdapterOrNoGo
```

Normal revisit condition:

```text
NEXT_REVISIT_CONDITION=approximately merged 4fp plus s7-98 plus t135, or earlier material weight-factorization/adapter/H/exponent trigger
```

Earlier RUN is justified by any of:

- global/s canonical/reverse weight factors to outer-only data at `B^o(1)` cost;
- fixed-U `W_{c_*}(n)` opens into theorem-ready multiplicative/Type-I/Type-II data;
- a direct unitary-divisor/projective-prime arithmetic adapter appears;
- a new H target becomes theorem-ready;
- a receiver or whole-family exponent is materially superseded.

## Boundary locks

```text
STAGE14_WORK_BTX32=COMPLETE
TOOLBOX_COMPONENT_COMPLETE=true
X_COMPONENT_COMPLETE=true
GLOBAL_S_WEIGHTED_UNITARY_DIVISOR_INCIDENCE_IDENTIFIED=true
MAINLINE_4FM_E_SCALE_SPLIT_APPLIES_TO_SAME_S7_95_PACKET=true
COMMON_NONNEGATIVE_WEIGHTED_RECIPROCAL_SELECTOR_TEMPLATE_PROVED=true
PHYSICAL_WEIGHT_LOCATION_ASYMMETRY_PROVED=true
FIXED_U_PHYSICAL_COFACTOR_WEIGHT_OUTER_N_ONLY=true
DIRECT_WEIGHTED_UNITARY_TO_FIXED_PROJECTIVE_PRIME_ADAPTER_NOGO_AT_CURRENT_LEVEL=true
COMMON_PHYSICAL_WEIGHT_ADAPTER_PROVED=false
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=true
NEW_HEAVY_MAIN_H_NEEDED=false
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=false
TH30_NEEDED=false
NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false
NEXT_INTEGRATED_TARGET=OuterInnerPhysicalWeightFactorizationAdapterOrNoGo
NEXT_REVISIT_CONDITION=approximately merged 4fp plus s7-98 plus t135, or earlier material weight-factorization/adapter/H/exponent trigger
```