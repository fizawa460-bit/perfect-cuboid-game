# Stage27-20-r302an — one fixed-power theorem plus two subpower adapters suffice for the primitive MAIN quadratic form

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302am
SOURCE_STAGE=Stage20

The r302v-am chain fully incorporates the already-audited StructureRadar primitive Fourier/Gauss normalization, including the exact 2-primary local factor, into the coefficient-specific Stage27 receiver.

The resulting closure package has only one source of a new fixed power.

## A. Sole fixed-power input — admissible diagonal product

For each retained packet and gcd stratum,

```text
G_d(b,b)=1_{b in Adm_d}D_d.
```

Let

```text
theta_d
 = (sum_{b in Adm_d}|c_b|^2)
   /(sum_{d|b}|c_b|^2),

c_b=W_hat(b)/q.
```

The only fixed-power theorem required in this package is

```text
(D_d/E_packet) theta_d
 <= B^{-2delta+o(1)}
```

for one fixed `delta>0`, uniformly over all retained packets and gcd strata.

Call this

```text
A = MAINWallPrimitiveInverseFrequencyAdmissibleClassDiagonalEnergyProductDeficit.
```

## B. Zero-loss adapter — joint primitive square-fiber concentration

R302z-am show that the local quadratic phase-label fibers have a singularity weight controlled by odd and 2-primary square-root gcds, and that their weighted Fourier energy is exactly a family of parity-preserving projected physical coset energies.

A sufficient theorem is the joint projected fine-block multiplicity bound

```text
B = MAINWallJointPrimitiveProjectedFineBlockMultiplicitySubpowerAdapter,
```

which asserts the relevant coarse projected blocks contain only `B^o(1)` nonzero base projected blocks uniformly over all odd and 2-primary square-root divisor refinements.

Its consequence is

```text
joint singular weighted Fourier energy
 <= B^o(1) * sum_{b in Adm_d}|c_b|^2.
```

This adapter supplies no independent fixed power.

## C. Zero-loss adapter — joint primitive unit-fiber nonconcentration

Push the same positive amplitude `|A_d|^2 dH_phys^MAIN` to the full primitive inverse-unit coordinate, using both odd and nontrivial 2-primary unit coordinates when present. Let the positive pushforward be `mu_d`, with total mass `D_d` and primitive unit set `U_d`.

A sufficient theorem is

```text
C = MAINWallJointPrimitiveUnitFiberSubpowerNonconcentration:

max_{lambda in U_d} mu_d(lambda)
 <= B^o(1) D_d/|U_d|.
```

This is only relative subpower nonconcentration, not fixed-power equidistribution.

By joint additive Parseval from r302al, the ratio between the full additive coordinate count and `|U_d|` is `B^o(1)`. Combining C with the square-fiber estimate and B gives the **entire** primitive quadratic form bound

```text
Q_d(c)
 <= B^o(1) D_d
    * sum_{b in Adm_d}|c_b|^2.
```

No diagonal/off-diagonal split is needed at this final stage of the estimate; the split was used to discover and verify the normal form, while the positive primitive-unit representation now recombines it without loss.

Finally A yields

```text
Q_d(c)
 <= B^{-2delta+o(1)} E_packet
    * sum_{d|b}|c_b|^2.
```

This is exactly the coefficient-specific quadratic-form deficit required by the audited r302t fallback. Feeding it through the already-audited finite Fourier/Gauss identities returns the same-`H_phys^MAIN` MAIN covariance deficit and hence the r302 high-occupancy route.

## Current frontier

Therefore the current checkpoint40 receiver has been reduced to exactly:

```text
ONE_FIXED_POWER_INPUT=A
ZERO_LOSS_ADAPTER_1=B
ZERO_LOSS_ADAPTER_2=C
```

No independent Kloosterman/Kuznetsov fixed-power theorem is mandatory in this sufficient package. Such machinery remains a possible way to prove A, B, or C, but is no longer itself the canonical theorem statement.

None of A, B, or C is proved in this batch. In particular, no strict sub-square-root saving may be promoted until all three are discharged on the original `H_phys^MAIN` measure.

This is the natural algebraic stopping point. Further progress requires genuinely new same-measure information about the physical diagonal mass, projected physical block multiplicity, or primitive inverse-unit occupancy; another renaming of the Gram/Kloosterman receiver is not progress.

```text
STAGE27_20_R302AN_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
PRIMITIVE_GAUSS_RECOMBINATION_COMPLETE=true
SOLE_FIXED_POWER_INPUT_COUNT=1
ZERO_LOSS_ADAPTER_COUNT=2
SEPARATE_OFFDIAGONAL_FIXED_POWER_REQUIRED=false
FULL_TWO_PRIMARY_LOCAL_FACTOR_RETAINED=true
A_DIAGONAL_PRODUCT_DEFICIT_PROVED=false
B_JOINT_PROJECTED_BLOCK_MULTIPLICITY_SUBPOWER_PROVED=false
C_JOINT_UNIT_FIBER_NONCONCENTRATION_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
WALL_SLAB_AGGREGATE_DEFICIT_THEOREM_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
FREEZE_FOR_STRUCTURE_RADAR=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302ao
NEXT_TARGET=ATTACK_A_OR_DISCHARGE_ZERO_LOSS_ADAPTERS_B_C_WITH_NEW_SAME_MEASURE_INFORMATION
NEXT_BATCH=Stage27-20-r302-main-batch
AUDIT_REQUIRED=true
```