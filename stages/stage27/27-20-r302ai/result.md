# Stage27-20-r302ai — multiplicative-character expansion of the inverse-a unit discrepancy

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302ah
SOURCE_STAGE=Stage20

R302ah gives a strong sufficient pointwise equidistribution route for the zero-mass unit discrepancy `nu_d`. If pointwise control is unnecessarily strong, there is an exact multiplicative Fourier expansion on the finite unit group.

For every Dirichlet character `chi` on `(Z/mZ)^x`, define

```text
M_d(chi)
 = sum_{lambda in (Z/mZ)^x}
     nu_d(lambda) chi(lambda).
```

Because `sum_lambda nu_d(lambda)=0`,

```text
M_d(chi_0)=0.
```

Unit-group Fourier inversion gives exactly

```text
nu_d(lambda)
 = (1/phi(m))
   sum_{chi != chi_0}
     M_d(chi) conj(chi(lambda)).
```

Since

```text
lambda=inverse(4a') (mod m),
```

the moment `M_d(chi)` is, up to the fixed unit factor from `4`, the same-measure physical character moment in the primitive additive-frequency coordinate `a'`:

```text
chi(lambda)=conj(chi(4a')).
```

Thus no new measure or unrelated modulus family is introduced by passing to multiplicative characters.

For the actual quadratic test function

```text
F_a(lambda)=sum_u a_u e_m(lambda u^2),
```

the discrepancy form becomes

```text
Q_nu(a)
 = (1/phi(m))
   sum_{chi != chi_0}
     M_d(chi) B_a(chi),

B_a(chi)
 = sum_{lambda in (Z/mZ)^x}
     conj(chi(lambda)) |F_a(lambda)|^2.
```

Equivalently, after interchanging sums, `B_a(chi)` is governed by generalized Gauss sums

```text
sum_{lambda in (Z/mZ)^x}
  conj(chi(lambda)) e_m(lambda h),
h=u^2-v^2.
```

For primitive characters and coprime `h` these have the usual square-root Gauss size; imprimitive characters and noncoprime `h` require their exact conductor/gcd descent and are not silently replaced by the primitive formula.

This yields an alternative focused external route:

```text
FIRST_MISSING_LEMMA=
MAINWallPrimitiveACharacterMomentSameMeasureLargeSieveAdapter
```

A successful theorem must control the above paired character moments on the original `H_phys^MAIN` packet, retain the correlated modulus/common-parent masks, and preserve one fixed power. Existing Gaussian/Hecke or ordinary character large-sieve cards are not cross-promoted without an exact identification of this character family and weight.

No character-moment saving is proved here.

```text
STAGE27_20_R302AI_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
UNIT_GROUP_CHARACTER_INVERSION_PROVED=true
PRINCIPAL_CHARACTER_DISCREPANCY_MOMENT_ZERO=true
INVERSE_A_TO_PRIMITIVE_A_CHARACTER_IDENTITY_PROVED=true
IMPRIMITIVE_CONDUCTOR_DESCENT_RETAINED=true
CHARACTER_MOMENT_LARGE_SIEVE_APPLICABILITY_PROVED=false
INVERSE_A_DISCREPANCY_DEFICIT_PROVED=false
DIAGONAL_PRODUCT_DEFICIT_PROVED=false
FINE_BLOCK_MULTIPLICITY_SUBPOWER_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302aj
NEXT_BATCH=Stage27-20-r302-main-batch
```