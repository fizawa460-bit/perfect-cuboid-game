# Stage27-20-r302k — exact same-measure correlation target inside the MAIN physical host

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302j
SOURCE_STAGE=Stage20

For each wall fiber x=(P,U), let A_x be the indicator that a physical-host tuple survives the frozen nested-divisor and simultaneous two-root MAIN constraints. Then rho_x is exactly the H_x-normalized average of A_x.

A legal fixed-power theorem must therefore show that high averages of A_x are rare in H_x-mass. Equivalently, for some fixed alpha,beta>0,

  sum_{x: rho_x>B^{-alpha}} H_x <= B^{-beta+o(1)} sum_x H_x.

This is a correlation theorem between the MAIN arithmetic constraints and the already-charged physical host. It cannot be replaced by unweighted residue-class counts, outer-U cardinality, fixed witness moments, or the exponent-neutral row-CRT repackaging.

The theorem may be attacked either directly on A_x or through a common physical refinement that dominates H_x with only B^{o(1)} loss. Any transfer from another route must preserve this same-measure fixed power.

STAGE27_20_R302K_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
SAME_MEASURE_MAIN_ARITHMETIC_HOST_CORRELATION_TARGET_DERIVED=true
UNWEIGHTED_CLASS_COUNT_SUFFICIENT=false
ROW_CRT_AS_NEW_SAVING_SUFFICIENT=false
OUTER_U_CARDINALITY_AS_NEW_SAVING_SUFFICIENT=false
MAIN_HIGH_OCCUPANCY_PHYSICAL_MASS_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302l
