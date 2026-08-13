# Stage14-t-batch — t129 through t131

## Status

`COMPLETE_ENDPOINT_REAL_NONREAL_SCALAR_NORM_OUTER_REDUCTION`

This batch starts from latest merged main

```text
d519dcccee5bedb4844dbcee5cb4b5171600c0bf
```

and consumes merged `Stage14-t128`, completed merged `Stage14-tH29`, and merged `Stage14-Work-brX30`.

## Work unit 1 — Stage14-t129

The endpoint-headroom branch is transposed exactly to the reciprocal-hyperbola corner wedge

```text
0<u<=v<theta,
ell=L_B*B^u,
n=N_max*B^(-v).
```

For fixed `theta>0`, neither the scalar cofactor projection nor the prime projection is fixed-power small under the merged hypotheses. Endpoint geometry alone therefore gives no saving.

## Work unit 2 — Stage14-t130

For every real/order-two projective character,

```text
chi([conj z])=chi([z]).
```

Hence generic split-prime orientation bits disappear exactly. After freezing the exceptional label,

```text
chi([gamma])
 = chi([gamma_E]) xi_chi(n_G),
```

where `xi_chi` is a scalar completely multiplicative `{+1,-1}` phase on the generic split-prime norm support. The real branch becomes a real Hecke prime cumulative bias against the scalar physical norm weight `W_phys(n) xi_chi(n_G)`.

## Work unit 3 — Stage14-t131

For a nonreal character, define the exact norm-fiber coefficient

```text
A_chi(n)
 := sum_{gamma in Omega_nb,long, N(gamma)=n} chi([gamma]),
|A_chi(n)|<=B^o(1).
```

Then

```text
D_chi,long
 = chi([a]) sum_n A_chi(n) P_chi(X_U/n).
```

The inner Gaussian orientation dependence is compressed to the finite subset-product coefficient `A_chi(n)`; the polynomial outer variable is the scalar cofactor norm `n`.

This materially changes the full fixed-U receiver. All three surviving branches now have the same polynomial outer coordinate `n=N(gamma)`, though their arithmetic weights remain inequivalent:

```text
(A) endpoint corner-wedge projective prime depletion;
(B) long real Hecke bias against W_phys(n) xi_chi(n_G);
(C) long nonreal Hecke correlation against A_chi(n).
```

Merged Work-brX30 permits only a common reciprocal-window geometric language; no global/s arithmetic measure is imported and no saving is cross-promoted.

No new tH is opened. Completed tH29 already gives the relevant negative theorem boundary, and the newly exposed scalar weights still require internal arithmetic decomposition before a materially new theorem request exists.

```text
STAGE14_T_BATCH=COMPLETE
BATCH_START_MAIN_SHA=d519dcccee5bedb4844dbcee5cb4b5171600c0bf
BATCH_PUBLICATION_MAIN_SHA=d519dcccee5bedb4844dbcee5cb4b5171600c0bf
BATCH_FIRST_STAGE=Stage14-t129
BATCH_LAST_STAGE=Stage14-t131
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3
BATCH_SUBSTANTIVE_STAGE_COUNT=3
BATCH_INTEGRATED_H_UNITS=NONE
BATCH_STOP_REASON=receiver_change
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_T_RECEIVER=SharedUScalarNormOuterEndpointCornerWedgeProjectivePrimeDepletionOrLongRealHeckeBiasAgainstPhysicalNormWeightOrLongNonrealHeckeCorrelationAgainstNormFiberOrientationCoefficient
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
NEXT=Stage14-t132
```
