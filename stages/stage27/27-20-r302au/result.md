# Stage27-20-r302au — deterministic effective-support criterion for the singularity-weighted root receiver

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302at
SOURCE_STAGE=Stage20

The root-energy target can be reduced to one transparent spread statistic of the actual physical coefficient.

For `E_all(W)>0`, define

```text
P_inf(W) = max_{f mod q}|W(f)|^2,
N_eff(W) = E_all(W)/P_inf(W).
```

`N_eff(W)` is the effective `L2` residue support. Since

```text
E_root(W;C)
 <= R_q(C) * P_inf(W),
```

r302as gives

```text
R_q(C) * rho_root(W;C)
 <= R_q(C)^2 / N_eff(W).
```

Using r302at,

```text
R_q(C)^2
 <= B^{o(1)} s_q(C)^2.
```

Therefore the following single inequality is sufficient for one fixed power:

```text
N_eff(W)
 >= B^{2delta-o(1)} s_q(C)^2.
```

Equivalently,

```text
s_q(C)^2 / N_eff(W)
 <= B^{-2delta+o(1)}.
```

This is a deterministic reduction, not a probabilistic heuristic. It makes the competition explicit:

- singular square divisibility of `C` increases the possible root multiplicity through `s_q(C)`;
- spread of the actual physical residue coefficient increases `N_eff(W)`;
- a fixed power appears exactly when physical residue support dominates the squared singular-root scale by a polynomial factor.

On the regular branch `(C,q)=1`, `s_q(C)=1`, so it is enough that `N_eff(W)` be a positive power of `B`. On singular packets the required effective support grows with the explicit local singularity.

Neither a positive-power lower bound for `N_eff(W)` nor an exceptional-mass statement for packets where it is small is proved here.

```text
FIRST_MISSING_LEMMA=
MAINWallPhysicalResidueEffectiveSupportVersusQuadraticSingularityDeficit

STAGE27_20_R302AU_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
EFFECTIVE_L2_RESIDUE_SUPPORT_DEFINED=true
ROOT_ENERGY_BY_PEAK_BOUND_PROVED=true
SINGULARITY_WEIGHTED_EFFECTIVE_SUPPORT_CRITERION_PROVED=true
REGULAR_BRANCH_REQUIRES_ONLY_POLYNOMIAL_EFFECTIVE_SUPPORT=true
EFFECTIVE_SUPPORT_FIXED_POWER_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
CURRENT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302av
NEXT_BATCH=Stage27-20-r302-main-batch
```