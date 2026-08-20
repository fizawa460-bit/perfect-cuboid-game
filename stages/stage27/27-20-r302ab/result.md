# Stage27-20-r302ab — exact Fourier-subgroup identity for singular collision energy

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302aa
SOURCE_STAGE=Stage20

R302aa reduces the unresolved odd square-collision contribution to

```text
sum_u gcd(u,m_*) |c_{du}|^2,
c_b=W_hat(b)/q.
```

This weighted Fourier quantity has an exact residue-space representation.

For any divisor `R|q`, define the physical coset-energy functional

```text
C_R(W)
 = sum_{t mod q/R}
     | sum_{j=0}^{R-1} W(t+j q/R) |^2.
```

Finite Fourier orthogonality gives exactly

```text
sum_{b mod q : R|b} |c_b|^2
 = C_R(W)/(q R).
```

In particular, the gcd stratum energy is

```text
sum_{d|b}|c_b|^2 = C_d(W)/(q d),
```

and for every `r|m_*`,

```text
sum_{dr|b}|c_b|^2 = C_{dr}(W)/(q d r).
```

Now use the exact divisor identity

```text
gcd(u,m_*)
 = sum_{r | gcd(u,m_*)} phi(r).
```

Therefore

```text
sum_u gcd(u,m_*) |c_{du}|^2
 = (1/(q d))
   sum_{r|m_*} (phi(r)/r) C_{dr}(W).
```

Relative to the original restricted Fourier energy, the singularity multiplier is exactly

```text
[sum_{r|m_*} (phi(r)/r) C_{dr}(W)] / C_d(W).
```

Thus the singular collision problem is not an abstract Fourier-tail question. It is a nested physical residue-coset concentration problem for the **same original coefficient `W`**.

A sufficient subpower adapter is

```text
sum_{r|m_*} (phi(r)/r) C_{dr}(W)
 <= B^o(1) C_d(W).
```

If this holds, the entire odd square-collision contribution is absorbed by the same coefficient-specific diagonal fixed-power deficit with only `B^o(1)` loss. No such coset-energy theorem is proved here.

```text
FIRST_MISSING_LEMMA=
MAINWallPhysicalNestedResidueCosetEnergySubpowerConcentration

STAGE27_20_R302AB_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
FOURIER_SUBGROUP_ENERGY_IDENTITY_PROVED=true
SINGULAR_GCD_WEIGHT_DIVISOR_EXPANSION_PROVED=true
SINGULAR_COLLISION_REDUCED_TO_PHYSICAL_COSET_ENERGY=true
NESTED_COSET_ENERGY_SUBPOWER_CONCENTRATION_PROVED=false
NONZERO_SQUARED_FREQUENCY_DEFICIT_PROVED=false
DIAGONAL_PRODUCT_DEFICIT_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302ac
NEXT_BATCH=Stage27-20-r302-main-batch
```