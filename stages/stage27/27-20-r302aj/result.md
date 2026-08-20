# Stage27-20-r302aj — reduced three-input closure package after primitive Gauss normalization

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302ai
SOURCE_STAGE=Stage20

The audited r302p-u frontier asked for a diagonal fixed power plus an actual-coefficient off-diagonal same-measure fixed power. The r302v-ai continuation uses the already-imported StructureRadar Fourier/Gauss algebra to reduce that package further without claiming either missing theorem.

## 1. Fixed-power input A — one scalar/admissible diagonal product

Primitive Gauss completion makes the Gram diagonal frequency-flat on the exact admissible local class:

```text
G_d(b,b)=1_{b in Adm_d}D_d.
```

Hence the actual coefficient diagonal is exactly

```text
D_d * sum_{b in Adm_d}|c_b|^2.
```

With

```text
theta_d
 = (sum_{b in Adm_d}|c_b|^2)
   /(sum_{d|b}|c_b|^2),
```

the required coefficient-specific diagonal saving is the single product theorem

```text
(D_d/E_packet) theta_d
 <= B^{-2 delta_diag+o(1)}.
```

This is the first genuine fixed-power input still missing.

## 2. Zero-fixed-power-loss input B — projected singular square-fiber concentration

The odd square-map collision degree is

```text
deg_m(u)
 <= B^o(1) gcd(u,m_*),

m_* = product_{p^k||m} p^floor(k/2).
```

The singular weighted admissible Fourier energy has an exact parity-preserving physical representation. With the r302ab progressions `(M_r,b_r)`,

```text
sum_{u in Adm_d} gcd(u,m_*)|c_{du}|^2
 = (1/(q d L_d))
   sum_{r|m_*}(phi(r)/r) C_{M_r,b_r}(W).
```

A sufficient **subpolynomial**, not fixed-power, adapter is

```text
sum_{r|m_*}(phi(r)/r) C_{M_r,b_r}(W)
 <= B^o(1) C_{M_0,b_0}(W).
```

R302ac further reduces this to a projected fine-block multiplicity condition

```text
M_d^proj(r)<=B^o(1)
```

uniformly for `r|m_*`. This input only preserves the fixed power supplied elsewhere; it is not charged as a second saving.

## 3. Fixed-power input C — inverse-a primitive unit discrepancy

After primitive normalization the positive same-MAIN inverse-`a'` pushforward on the odd unit group is

```text
mu_d(lambda)=D_d/phi(m)+nu_d(lambda),
sum_lambda nu_d(lambda)=0.
```

The uniform unit component is the Ramanujan matrix. R302ag proves that its entire quadratic form, including nonzero squared-frequency differences, is bounded by `B^o(1)` times the same singular weighted Fourier energy from input B. Thus it requires no independent fixed-power theorem.

The only genuinely new odd off-diagonal power is carried by `nu_d`. One strong sufficient theorem is the pointwise relative equidistribution estimate

```text
max_{lambda in (Z/mZ)^x}
 |mu_d(lambda)-D_d/phi(m)|
 <= B^{-eta+o(1)} D_d/phi(m)
```

for one fixed `eta>0`, uniformly on retained packets and gcd strata. R302ah shows that, together with input B, this gives a fixed-power discrepancy quadratic-form bound for the actual coefficient vector.

R302ai records an alternative exact route through nonprincipal unit-group character moments. That route is not combined with the pointwise theorem as an independent saving; either one may discharge input C.

## 4. Closure implication

If A, B, and C hold, then:

1. the actual coefficient diagonal has a fixed-power deficit by A;
2. the uniform primitive unit/Ramanujan off-diagonal contribution costs only `B^o(1)` times the same admissible diagonal energy by B and r302ag;
3. the zero-mass inverse-`a'` discrepancy has a fixed-power deficit by B+C;
4. the exact primitive 2-primary admissibility and local phase data remain inside the same coefficient class and are not dropped;
5. therefore the actual `c_b=W_hat(b)/q` quadratic form has a fixed-power deficit on the original `H_phys^MAIN` packet.

Feeding this back through audited r302t, r302m, and the earlier same-measure r302h/i/b/r301u transfers would close `UniformWallSlabMAINArithmeticHostCorrelationPowerDeficit` and yield a strict sub-square-root upper saving **only after** A and C are actually proved and B is actually supplied. None is promoted here.

## 5. Natural stopping point

The remaining frontier is no longer generic “large sieve/Kloosterman cancellation”. It consists of exactly:

```text
A = MAINWallPrimitiveInverseFrequencyAdmissibleClassDiagonalEnergyProductDeficit
B = MAINWallPhysicalProjectedFourierFineBlockMultiplicitySubpowerAdapter
C = MAINWallInverseAUnitPushforwardDiscrepancyAgainstActualShearedCoefficientClass
```

with the strong sufficient replacement

```text
C_strong = MAINWallInverseAUnitFiberPointwiseRelativeEquidistribution
```

or the alternative character route

```text
C_char = MAINWallPrimitiveACharacterMomentSameMeasureLargeSieveAdapter.
```

Further renaming without new information on A, B, or C would be non-progress. The route remains unfrozen, but the next batch must attack at least one of these concrete inputs rather than restating the same quadratic-form gate.

```text
STAGE27_20_R302AJ_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
PRIMITIVE_GAUSS_FRONTIER_REDUCED=true
DIAGONAL_FIXED_POWER_INPUT_COUNT=1
ZERO_POWER_LOSS_ADAPTER_COUNT=1
OFFDIAGONAL_FIXED_POWER_INPUT_COUNT=1
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
NEXT_TARGET=PROVE_A_OR_B_OR_C_WITH_NEW_SAME_MEASURE_INFORMATION
NEXT_BATCH=Stage27-20-r302-main-batch
AUDIT_REQUIRED=true
```