# Stage27-20-r302aj — strong intermediate three-input package after primitive Gauss normalization

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302ai
SOURCE_STAGE=Stage20

The audited r302p-u frontier asked for a diagonal fixed power plus an actual-coefficient off-diagonal same-measure fixed power. The r302v-ai continuation already weakens that architecture substantially. This card records a strong sufficient package before the further weakening in r302ak; it is not claimed minimal.

## 1. Fixed-power input A — one scalar/admissible diagonal product

Primitive Gauss completion makes the Gram diagonal frequency-flat on the exact admissible local class:

```text
G_d(b,b)=1_{b in Adm_d}D_d.
```

Hence, with

```text
theta_d
 = (sum_{b in Adm_d}|c_b|^2)
   /(sum_{d|b}|c_b|^2),
```

the coefficient-specific diagonal theorem is

```text
(D_d/E_packet) theta_d
 <= B^{-2 delta_diag+o(1)}.
```

## 2. Zero-fixed-power-loss input B — projected singular square-fiber concentration

R302z-ab give

```text
deg_m(u)<=B^o(1)gcd(u,m_*),
```

and the exact parity-preserving identity

```text
sum_{u in Adm_d} gcd(u,m_*)|c_{du}|^2
 = (1/(q d L_d))
   sum_{r|m_*}(phi(r)/r) C_{M_r,b_r}(W).
```

Thus a sufficient subpolynomial adapter is

```text
sum_{r|m_*}(phi(r)/r) C_{M_r,b_r}(W)
 <= B^o(1) C_{M_0,b_0}(W).
```

R302ac reduces this further to the projected fine-block multiplicity condition `M_d^proj(r)<=B^o(1)`. This input is not an independent saving.

## 3. Strong off-diagonal route C_strong

R302af-ai expose the odd primitive inverse-`a'` unit pushforward

```text
mu_d(lambda)=D_d/phi(m)+nu_d(lambda).
```

The uniform unit component is the Ramanujan matrix, and r302ag bounds its whole quadratic form by `B^o(1)` times the same singular weighted energy from B.

A strong sufficient theorem for the remaining discrepancy is

```text
max_lambda
 |mu_d(lambda)-D_d/phi(m)|
 <= B^{-eta+o(1)}D_d/phi(m).
```

R302ah proves that B plus this hypothesis gives a fixed-power discrepancy bound. R302ai records the exact nonprincipal character-moment route as an alternative architecture.

This `B^{-eta}` discrepancy theorem is sufficient but, as r302ak shows next, **not necessary** once A is already the fixed-power source. It must not be frozen as the minimal restart point.

```text
STAGE27_20_R302AJ_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
PRIMITIVE_GAUSS_FRONTIER_REDUCED=true
STRONG_INTERMEDIATE_PACKAGE_ONLY=true
FIXED_POWER_DISCREPANCY_ROUTE_SUFFICIENT=true
FIXED_POWER_DISCREPANCY_ROUTE_MINIMAL=false
RAMANUJAN_MAIN_TERM_INDEPENDENT_FIXED_POWER_REQUIRED=false
PROJECTED_PARITY_CLASS_PRESERVED=true
DIAGONAL_PRODUCT_DEFICIT_PROVED=false
PROJECTED_FINE_BLOCK_MULTIPLICITY_SUBPOWER_PROVED=false
INVERSE_A_DISCREPANCY_DEFICIT_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
WALL_SLAB_AGGREGATE_DEFICIT_THEOREM_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
FREEZE_FOR_STRUCTURE_RADAR=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302ak
NEXT_TARGET=WEAKEN_OFFDIAGONAL_FIXED_POWER_TO_ZERO_LOSS_NONCONCENTRATION
NEXT_BATCH=Stage27-20-r302-main-batch
AUDIT_REQUIRED=true
```