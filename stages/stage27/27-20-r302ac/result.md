# Stage27-20-r302ac — reduce projected singular coset energy to twisted fine-block multiplicity

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302ab
SOURCE_STAGE=Stage20

R302ab preserves the exact primitive admissibility class by writing

```text
M_0=d L_d,
b_0=d beta_d (mod M_0),
```

and, for every odd `r|m_*`,

```text
M_r=M_0 r,
b_r=b_0 (mod M_0),
b_r=0   (mod d r).
```

It defines the projected physical coset energy

```text
C_{M,b}(W)
 = sum_{t mod q/M}
     |sum_{j=0}^{M-1}
        W(t+j q/M) e_M(-b j)|^2.
```

Define the base twisted fine-block sums

```text
S_0(t)
 = sum_{j=0}^{M_0-1}
     W(t+j q/M_0)e_{M_0}(-b_0 j),
t mod q/M_0.
```

Then

```text
C_{M_0,b_0}(W)=sum_t |S_0(t)|^2.
```

For `r|m_*`, put `N_r=q/M_r`. Since `M_r=M_0 r` and `b_r=b_0 (mod M_0)`, grouping an index in the coarse projected sum as

```text
j=k+r ell,
0<=k<r,
0<=ell<M_0,
```

gives the exact identity

```text
sum_{j=0}^{M_r-1}
 W(t+j N_r)e_{M_r}(-b_r j)
 = sum_{k=0}^{r-1}
     e_{M_r}(-b_r k) S_0(t+k N_r).
```

Thus the coarse projected block is a unit-phase sum of exactly `r` base projected blocks. No primitive parity class has been enlarged and no coefficient energy has been changed.

Let `M_d^proj(r)` be the maximum, over `t mod N_r`, of the number of nonzero terms among

```text
S_0(t+k N_r), 0<=k<r.
```

Cauchy inside each coarse block gives

```text
C_{M_r,b_r}(W)
 <= M_d^proj(r) C_{M_0,b_0}(W).
```

The sets of base indices occurring as `t+kN_r` partition `Z/(q/M_0)Z`, so there is no extra multiplicity in the outer summation.

Therefore the r302ab projected singular-collision adapter follows from the subpolynomial block-multiplicity theorem

```text
M_d^proj(r) <= B^o(1)
```

uniformly for every `r|m_*`. Indeed,

```text
sum_{r|m_*} (phi(r)/r) C_{M_r,b_r}(W)
 <= B^o(1) C_{M_0,b_0}(W)
```

because `phi(r)/r<=1` and `tau(m_*)=B^o(1)`.

This is only a zero-fixed-power-loss adapter: the actual fixed power still comes from the r302w diagonal product. Its role is to prevent singular square collisions from consuming that power while preserving the exact admissible Fourier class.

The old reverse-reciprocal divisor multiplicity is not automatically identified with `M_d^proj(r)`. Such reuse requires an exact adapter from these twisted MAIN block sums to the audited reconstruction fibers.

```text
FIRST_MISSING_LEMMA=
MAINWallPhysicalProjectedFourierFineBlockMultiplicitySubpowerAdapter

STAGE27_20_R302AC_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
PROJECTED_COARSE_FINE_COSET_IDENTITY_PROVED=true
PRIMITIVE_PARITY_CLASS_RETAINED=true
PROJECTED_COSET_ENERGY_BLOCK_MULTIPLICITY_BOUND_PROVED=true
SUBPOWER_PROJECTED_BLOCK_MULTIPLICITY_SUFFICIENT=true
EXISTING_DIVISOR_MULTIPLICITY_CROSS_PROMOTED=false
PROJECTED_FINE_BLOCK_MULTIPLICITY_SUBPOWER_PROVED=false
INVERSE_A_DISCREPANCY_DEFICIT_PROVED=false
DIAGONAL_PRODUCT_DEFICIT_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302ad
NEXT_BATCH=Stage27-20-r302-main-batch
```