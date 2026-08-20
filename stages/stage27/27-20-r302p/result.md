# Stage27-20-r302p — primitive Gauss completion removes oscillatory diagonal saving

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302o
SOURCE_STAGE=Stage20
STRUCTURE_RADAR_SOURCE=SR-GATE-33A-169,SR-GATE-34-169,SR-GATE-36A-169,SR-GATE-37A-169

The repaired r302o leaves a mandatory diagonal obligation

```text
sup_b G_d(b,b)
 <= B^{-2delta_1+o(1)} E_packet.
```

The StructureRadar Gauss completion gives a further structural reduction of this branch. On a gcd stratum `d=(a,q)`, nonzero frequencies satisfy `d|b` and the exact descent is

```text
G_q(a,b)=d G_{q/d}(a/d,b/d).
```

With the pre-existing `1/q` normalization this becomes the primitive normalized kernel at `q'=q/d`. On each coprime odd local factor, completion of the square gives

```text
G_{q'}(a',b')
 = G_{q'}(a',0) * unit_phase(a',b'),
```

and the primitive Gauss magnitude is square-root size. The 2-primary primitive factor is likewise explicit: inadmissible parity frequencies vanish and admissible ones have square-root local magnitude up to an absolute factor.

Therefore, once a frequency `b` is admissible, the inverse-frequency oscillation that may drive off-diagonal cancellation is absent from its Gram diagonal:

```text
G_d(b,b)=||K_d(.,b)||^2_{H_phys^MAIN}.
```

Any unit-modulus inverse phase disappears in `|K_d(x,b)|^2`. Consequently a Kloosterman-fraction, Kuznetsov, or other phase-cancellation estimate cannot by itself prove the mandatory diagonal deficit. The fixed power must come from the exact single-frequency physical energy: normalization, amplitude, admissible support, or another already-unpaid physical restriction retained inside `K_d`.

This does not prove that the diagonal is full size. It proves only that oscillatory cancellation is not a legal source of its saving.

The diagonal branch is therefore narrowed to

```text
FIRST_MISSING_LEMMA=MAINWallPrimitiveInverseFrequencySingleFrequencyPhysicalEnergyDeficit
```

namely: prove one fixed `delta_diag>0`, uniformly over every retained packet, gcd stratum, and admissible frequency, such that

```text
||K_d(.,b)||^2_{H_phys^MAIN}
 <= B^{-2delta_diag+o(1)} E_packet.
```

The same charged measure, gcd-descent factor, common-parent allocation, physical masks, and quantifier order must be retained.

STAGE27_20_R302P_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
STRUCTURE_RADAR_GAUSS_COMPLETION_IMPORTED=true
SINGLE_FREQUENCY_TEST_REQUIRED=true
INVERSE_PHASE_DIAGONAL_CANCELLATION_AVAILABLE=false
DIAGONAL_SAVING_MUST_BE_PHYSICAL_OR_NORMALIZATION=true
SINGLE_FREQUENCY_PHYSICAL_ENERGY_DEFICIT_PROVED=false
OFFDIAGONAL_REMAINDER_OPERATOR_DEFICIT_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302q
NEXT_BATCH=Stage27-20-r302-main-batch
