# Stage27-20-r302o — repaired diagonal-plus-remainder continuation receiver

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302n
SOURCE_STAGE=Stage20

The continuation policy remains unchanged: unresolved external theorems do not freeze the checkpoint40 reduction chain, but they do block promotion to checkpoint50.

R302m requires the same-`H_phys^MAIN` full quadratic-form deficit for every coefficient vector. The repaired r302n shows, by the basis-vector test `c=e_b`, that a fixed-power Gram-diagonal deficit is a necessary consequence of that theorem. Therefore the previous `exact baseline subtraction + nontrivial subspace gap` escape is deleted unless a separate adapter first proves that the original all-`c` receiver has been replaced by a genuinely smaller coefficient space. No such adapter is currently proved.

The next honest sufficient receiver is:

`MAINWallPrimitiveInverseFrequencyDiagonalAndRemainderOperatorDeficitTheorem`.

Uniformly over every retained MAIN wall packet and gcd stratum, on the exact already-charged `H_phys^MAIN` measure, write

```text
G_d = D_d + R_d,
D_d = diag(G_d),
R_d = G_d-D_d.
```

Prove fixed `delta_1,delta_2>0` such that

```text
sup_b G_d(b,b)
 <= B^{-2delta_1+o(1)} E_packet,

||R_d||op
 <= B^{-2delta_2+o(1)} E_packet.
```

The correlated modulus, common-parent divisor weights, gcd-descent factor, primitive/chamber/parity masks, physical masks, and quantifier order must remain unchanged, and packet summation may lose only `B^{o(1)}`.

Then

```text
||G_d||op
 <= B^{-2 min(delta_1,delta_2)+o(1)} E_packet,
```

so the r302m full quadratic-form receiver follows rigorously. This theorem is only a sufficient decomposition; a direct full operator estimate remains admissible.

A different-measure theorem, a pure off-diagonal cancellation estimate with an uncontrolled diagonal, or a spectral theorem after subtracting an unproved baseline does not discharge r302m.

STAGE27_20_R302O_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
AUDIT_REPAIR_APPLIED=true
ADVANCEMENT_POLICY=CONTINUE_THROUGH_EXTERNAL_GATE_REDUCTIONS
FREEZE_FOR_STRUCTURE_RADAR=false
NEXT_THEOREM=MAINWallPrimitiveInverseFrequencyDiagonalAndRemainderOperatorDeficitTheorem
BASIS_VECTOR_DIAGONAL_NECESSITY_PROVED=true
BASELINE_SUBTRACTION_ADAPTER_PROVED=false
DIAGONAL_DEFICIT_PROVED=false
OFFDIAGONAL_REMAINDER_OPERATOR_DEFICIT_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
WALL_SLAB_AGGREGATE_DEFICIT_THEOREM_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302p
NEXT_BATCH=Stage27-20-r302-main-batch
AUDIT_REQUIRED=true
