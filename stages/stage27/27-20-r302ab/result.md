# Stage27-20-r302ab — exact progression-projected Fourier identity for singular collision energy

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302aa
SOURCE_STAGE=Stage20

R302aa reduces the unresolved odd square-collision contribution, on the actual primitive admissible coefficient class, to

```text
sum_{u in Adm_d} gcd(u,m_*) |c_{du}|^2,
c_b=W_hat(b)/q.
```

The 2-primary primitive completion makes `Adm_d` either all odd-component lifts (`q'_2=1`) or one exact parity class in `u=b/d`. Encode this by

```text
L_d in {1,2},
u = beta_d (mod L_d).
```

This local admissibility must be retained; replacing it by all `d|b` frequencies can lose a possible coefficient-specific diagonal saving.

## Exact arithmetic-progression Fourier energy

For any divisor `M|q` and residue `b0 mod M`, define

```text
C_{M,b0}(W)
 = sum_{t mod q/M}
     | sum_{j=0}^{M-1}
         W(t+j q/M) e_M(-b0 j) |^2.
```

Finite Fourier orthogonality gives the exact identity

```text
sum_{b mod q : b=b0 (mod M)} |c_b|^2
 = C_{M,b0}(W)/(q M).
```

The earlier divisibility-only formula is the special case `b0=0`.

For each odd divisor `r|m_*`, CRT gives a unique residue `beta_{d,r} mod L_d r` satisfying

```text
beta_{d,r}=beta_d (mod L_d),
beta_{d,r}=0      (mod r).
```

Put

```text
M_r=d L_d r,
b_r=d beta_{d,r} (mod M_r).
```

Then

```text
b=d u,
u in Adm_d,
r|u
```

is exactly the progression

```text
b=b_r (mod M_r).
```

Hence

```text
sum_{u in Adm_d, r|u}|c_{du}|^2
 = C_{M_r,b_r}(W)/(q d L_d r).
```

For `r=1`, this is the exact admissible-class energy.

Now use

```text
gcd(u,m_*)
 = sum_{r|gcd(u,m_*)} phi(r).
```

to obtain

```text
sum_{u in Adm_d} gcd(u,m_*) |c_{du}|^2
 = (1/(q d L_d))
   sum_{r|m_*} (phi(r)/r) C_{M_r,b_r}(W).
```

Relative to the exact admissible Fourier energy, the singularity multiplier is therefore

```text
[sum_{r|m_*}(phi(r)/r) C_{M_r,b_r}(W)]
/
C_{M_1,b_1}(W).
```

A sufficient zero-fixed-power-loss adapter is

```text
sum_{r|m_*}(phi(r)/r) C_{M_r,b_r}(W)
 <= B^o(1) C_{M_1,b_1}(W).
```

If this holds, singular odd square collisions cost only `B^o(1)` times the **same admissible-class Fourier energy** that appears in the r302w diagonal product, so a diagonal saving coming through `theta_d` is preserved rather than washed out.

No such projected coset-energy theorem is proved here.

```text
FIRST_MISSING_LEMMA=
MAINWallPhysicalNestedProjectedResidueCosetEnergySubpowerConcentration

STAGE27_20_R302AB_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
FOURIER_PROGRESSION_ENERGY_IDENTITY_PROVED=true
PRIMITIVE_PARITY_CLASS_RETAINED=true
SINGULAR_GCD_WEIGHT_DIVISOR_EXPANSION_PROVED=true
SINGULAR_COLLISION_REDUCED_TO_PROJECTED_PHYSICAL_COSET_ENERGY=true
NESTED_PROJECTED_COSET_ENERGY_SUBPOWER_PROVED=false
INVERSE_A_DISCREPANCY_DEFICIT_PROVED=false
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