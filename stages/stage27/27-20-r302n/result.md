# Stage27-20-r302n — isolate diagonal versus genuine two-frequency burden

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302m
SOURCE_STAGE=Stage20

R302m imports the exact same-`H_phys^MAIN` quadratic-form receiver for the completed primitive inverse-frequency operator. The next reduction is to identify which part of that positive semidefinite quadratic form can carry the required fixed-power deficit.

For one retained MAIN packet and gcd stratum `d`, write the Gram form as

```text
Q_d(c)=sum_{b,b'} c_b conj(c_{b'}) G_d(b,b')
      =sum_b |c_b|^2 G_d(b,b)
       +sum_{b!=b'} c_b conj(c_{b'})G_d(b,b').
```

Because `G_d=T_d^*T_d` is positive semidefinite, the diagonal cannot be cancelled away by an optimistic off-diagonal estimate. Therefore any theorem proving

```text
Q_d(c) <= B^{-2delta+o(1)} E_packet ||c||_2^2
```

must either:

1. place the diagonal itself below the target envelope uniformly on the retained physical packets; or
2. renormalize `E_packet` so that the diagonal is already part of the admissible baseline and then prove a strict spectral deficit for the nontrivial modes relative to that exact baseline.

A proof that only shows cancellation for `b!=b'` while leaving a diagonal of full `E_packet` size does not yield the required operator saving. Conversely, an absolute Schur row bound remains unnecessary if a spectral inequality controls the full positive quadratic form.

Thus the live burden splits into two exact subreceivers on the same charged measure:

```text
MAINWallPrimitiveInverseFrequencyDiagonalEnergyDeficitOrBaselineIdentification
MAINWallPrimitiveInverseFrequencyNontrivialSpectralGap
```

The first must decide whether the Gram diagonal is genuinely smaller than the host energy or merely the normalization baseline. The second must supply the uniform positive-power gap for the remaining spectrum without changing modulus family, common-parent weights, masks, or quantifier order.

No diagonal saving or spectral gap is proved here.

STAGE27_20_R302N_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
GRAM_DIAGONAL_CANNOT_BE_IGNORED=true
OFFDIAGONAL_CANCELLATION_ALONE_SUFFICIENT=false
DIAGONAL_DEFICIT_PROVED=false
NONTRIVIAL_SPECTRAL_GAP_PROVED=false
SAME_MEASURE_QUADRATIC_FORM_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302o
NEXT_BATCH=Stage27-20-r302-main-batch
