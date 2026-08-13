## Stage14-main-batch — 4fh through 4fj

Starts from latest merged main `d519dcccee5bedb4844dbcee5cb4b5171600c0bf` and follows the shared Stage14 main-batch contract.

### Results
- `4fh`: writes the two root-size constraints as an exact reciprocal `L`-window intersection and proves nonemptiness is equivalent to one radial product window in `n`; pure geometry gives no independent fixed-power saving.
- `4fi`: for a heavy support cell `n=B^(nu+o(1))`, any endpoint strip of thickness `B^-theta` with `theta>nu-mu` contains `o(B^mu)` integers. A surviving packet therefore carries its full exponent on the interior, where the `L`-window has relative width at least `B^(-theta+o(1))`.
- `4fj`: because fixed `n` has only `B^o(1)` admissible `L` candidates, accepted-`n` support and the full physical `(n,L)` incidence count are exponent-equivalent. The residual primitive/canonical/reverse masks remain in one Boolean weight `w_phys(n,L)`.

The heavy receiver materially changes to

`FixedPrimitiveRayFixedAgreementPairInteriorShortReciprocalSquareclassDivisorPhysicalIncidenceWithMassExponentMuAndWindowExponentThetaGreaterThanNuMinusMu`.

No new heavy H is opened yet: `w_phys(n,L)` still bundles the mask-preservation issue, so `4fk` must open that weight before an external theorem target is frozen.

```text
BATCH_SUBSTANTIVE_WORK_UNIT_COUNT=3
BATCH_INTEGRATED_H_UNITS=NONE
BATCH_STOP_REASON=receiver_change
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEXT=Stage14-4fk
```

Includes deterministic algebra/endpoint/incidence audit, previous-mainline and Work-brX30 regressions, publication-main lock, and path-scoped CI.
