# Stage14-t-batch — t109 through t111

## Batch status

Runs the canonical `Stage14-t-batch` contract from latest merged main

```text
BATCH_START_MAIN_SHA=eb93b1c3ca28637c2d3dd3ffead4271cb3e56478
```

with merged Stage14-t108 and the completed merged Stage14-tH28 negative applicability certificate as the parent-route boundary.

Three substantive stages are completed:

- `t109`: fixes one primitive Gaussian cofactor ray and proves the full moving `ell` dependence factors exactly to the endpoint projective selector; every other physical selector on the ray is `ell`-independent.
- `t110`: lifts one projective class to an exact `B^o(1)` union of invertible Gaussian residue classes modulo the endpoint conductor `d=B^o(1)`.
- `t111`: proves that localization into one of only `B^o(1)` projective prime classes cannot itself support a fixed-power density deficit uniformly over all moving packet/classes, and isolates the only remaining possible gain as the joint correlation between the primitive physical cofactor core, its selected projective class, and dominant-prime occupancy in the cofactor-dependent interval.

The receiver therefore changes materially at t111 from generic projected primitive norm-form support to

```text
SharedUPrimitiveGaussianCofactorPhysicalCoreSelectedProjectivePrimeClassCorrelation.
```

This is not a positive saving.  The particular class selected by each physical cofactor is not proved heavily occupied, and a joint cofactor/class/prime correlation may still be thin.  The standalone endpoint class density is merely discharged as an independent fixed-power factor.

Merged tH26 already certifies that generic Hecke large-sieve/BV/BDH machinery does not control the full nonmultiplicative cofactor coefficient, and merged tH28 certifies that the unseparated projected support has no applicable off-the-shelf fixed-power theorem.  The new receiver must therefore be opened internally before another theorem audit is useful.

Publication recheck found main unchanged at

```text
BATCH_PUBLICATION_MAIN_SHA=eb93b1c3ca28637c2d3dd3ffead4271cb3e56478.
```

The merged mainline 4eb--4ef and merged sH71 results do not provide a fixed-U-to-whole-family cross-promotion and do not change the t108/tH28 fixed-U theorem boundary.

```text
STAGE14_T_BATCH=COMPLETE
BATCH_START_MAIN_SHA=eb93b1c3ca28637c2d3dd3ffead4271cb3e56478
BATCH_PUBLICATION_MAIN_SHA=eb93b1c3ca28637c2d3dd3ffead4271cb3e56478
BATCH_FIRST_STAGE=Stage14-t109
BATCH_LAST_STAGE=Stage14-t111
BATCH_SUBSTANTIVE_STAGE_COUNT=3
BATCH_STOP_REASON=receiver_change
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
CURRENT_T_RECEIVER=SharedUPrimitiveGaussianCofactorPhysicalCoreSelectedProjectivePrimeClassCorrelation
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
NEXT=Stage14-t112
```

Next internal target:

```text
PrimitiveGaussianCofactorPhysicalCoreDensityPlusSelectedClassCenteredCorrelation
```
