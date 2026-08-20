# Stage27-20-r302ax — replace the peak-support route by a canonical residue fourth-moment collision index

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302aw
SOURCE_STAGE=Stage20
STRUCTURE_RADAR_SOURCE=SR-STR-173

The effective-support route r302au is useful, but the pointwise peak `P_inf(W)` is not necessary. A softer moment quantity suffices and matches the ACTIVE StructureRadar support/moment architecture more naturally.

For `E_all(W)>0`, define the normalized residue collision index

```text
Lambda(W)
 = [sum_{f mod q}|W(f)|^4]
   / [sum_{f mod q}|W(f)|^2]^2.
```

By Cauchy on the quadratic root set,

```text
E_root(W;C)
 = sum_{f in Root_q(C)}|W(f)|^2
 <= R_q(C)^{1/2}
    * [sum_f |W(f)|^4]^{1/2}.
```

Hence the exact root-energy product from r302as obeys

```text
R_q(C) * rho_root(W;C)
 <= R_q(C)^{3/2} * Lambda(W)^{1/2}.
```

Using r302at,

```text
R_q(C) <= B^o(1) s_q(C),
```

so

```text
R_q(C) * rho_root(W;C)
 <= B^o(1)
    * [ s_q(C)^3 Lambda(W) ]^{1/2}.
```

Define the singularity-normalized residue collision statistic

```text
Z(W,C) = s_q(C)^3 Lambda(W).
```

Then every packet satisfying

```text
Z(W,C) <= B^{-2kappa}
```

has a deterministic local arithmetic deficit

```text
R_q(C) * rho_root(W;C)
 <= B^{-kappa+o(1)}.
```

This is strictly preferable to requiring a pointwise peak adapter: it uses only the second and fourth moments of the **same actual residue coefficient** and keeps the singular local root multiplicity explicit.

It also matches the scope of SR-STR-173: nonnegative witness moments may be converted to support/concentration information only on the same charged measure, with no illegal scalarization. The present identity does not claim that the existing SR-STR-173 moments already equal `Lambda(W)`; an exact identification would still be needed before direct reuse.

The AR-012 peak route from r302aw remains an optional stronger adapter, not a prerequisite.

```text
STAGE27_20_R302AX_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
RESIDUE_L4_COLLISION_INDEX_DEFINED=true
ROOT_ENERGY_L4_CAUCHY_REDUCTION_PROVED=true
SINGULARITY_NORMALIZED_COLLISION_STATISTIC_DEFINED=true
POINTWISE_W_PEAK_REQUIRED=false
AR_012_PEAK_ADAPTER_MANDATORY=false
SR_STR_173_MOMENT_ARCHITECTURE_MATCH_IDENTIFIED=true
SR_STR_173_EXACT_W_MOMENT_IDENTIFICATION_PROVED=false
COLLISION_STATISTIC_FIXED_POWER_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
CURRENT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302ay
NEXT_BATCH=Stage27-20-r302-main-batch
```