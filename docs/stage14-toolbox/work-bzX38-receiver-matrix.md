# Stage14-Work-bzX38 — receiver / supersession matrix

## Integrated boundary

```text
LATEST_MERGED_WORK=Stage14-Work-byX37
LATEST_MERGED_Q=Stage14-q16
MAIN_BOUNDARY=Stage14-4ge
S_BOUNDARY=Stage14-s7-113
FIXED_U_BOUNDARY=Stage14-t149
```

## Common charged-once language

```text
COMMON_SUPPORT_EXISTENCE_AFTER_MULTIPLICITY_EXHAUSTION_LANGUAGE_PROVED=true
BOUNDED_WITNESS_MULTIPLICITY_DOES_NOT_IMPLY_EXISTENCE_DENSITY=true
SUBPOLYNOMIAL_EXTENSION_FIBER_CANNOT_CLOSE_EXISTENTIAL_SUPPORT_DEFICIT=true
EXISTENCE_AND_MULTIPLICITY_MUST_REMAIN_SEPARATE=true
```

## Route matrix

| Route | Ambient / baseline | First remaining support layer | Final remaining support layer | B^o(1) multiplicity status | Current external theorem state |
|---|---|---|---|---|---|
| main fixed-E two-sided | principal primitive pair rectangle `R_prim` | reciprocal divisor/CRT support `T_rec` | residual root/canonical/reverse/post-column physical support | reciprocal candidate fiber `B^o(1)`, charged once | q17 DIRECT=0; 4gf direct construction first |
| s fixed-E endpoint | charged 1D candidate support | deterministic reconstructed prefilter | existential reverse/post-column extension | reverse extension fiber `B^o(1)`, multiplicity only | internal equations not theorem-ready |
| s fixed-E two-sided | full-exponent fixed-E pair support | deterministic reconstructed prefilter | existential reverse/post-column extension | reverse extension fiber `B^o(1)`, multiplicity only | main reciprocal-CRT refinement not cross-promoted |
| s polynomial-E fixed product | charged 1D E support | deterministic reconstructed prefilter | existential reverse/post-column extension | reverse extension fiber `B^o(1)`, multiplicity only | internal equations not theorem-ready |
| s polynomial-E polynomial product | full-exponent fibered product support | deterministic reconstructed prefilter | existential reverse/post-column extension | reverse extension fiber `B^o(1)`, multiplicity only | internal equations not theorem-ready |
| fixed-U sparse endpoint | one actual cofactor interval | fixed Gaussian residue-class prime occupancy | physical selected prime occupancy | residue denominator `d^2 B^o(1)` already charged | tH32 only on safe near-full range |
| fixed-U many endpoint | host/residue-normalized cofactor annulus | fixed Gaussian residue-class prime occupancy | physical selected prime occupancy | host and `d^2` denominator already charged | no new theorem-ready family |
| fixed-U long headroom | reciprocal hyperbola | fixed Gaussian residue-class prime occupancy bias | physical selected prime occupancy | hosted modulus already charged | beyond-Mitsui individual-modulus obstruction remains |

## Main/s relation

The exact common relation is the quantifier split

```text
ambient
 -> precompletion support
 -> existential completion support.
```

Only the main fixed-E two-sided realization has merged equations refining the precompletion layer to

```text
FixedAgreementPairRadialLinearTwoLevelDivisorCRTReciprocalSolvabilitySupport.
```

```text
GLOBAL_S_TWO_LEVEL_COMPLETION_QUANTIFIER_LANGUAGE_PROVED=true
MAIN_FIXED_E_RECIPROCAL_CRT_REFINEMENT_CROSS_PROMOTED_TO_ALL_S=false
S_EXTENSION_MULTIPLICITY_AS_EXISTENCE_DENSITY_RECHARGED=false
```

## fixed-U separation

The fixed-U receiver has an analogous nested-support vocabulary but a different arithmetic witness species and baseline:

```text
Gaussian prime in one fixed residue/projective class
```

rather than

```text
integer reciprocal divisor/CRT witness or reverse/post-column extension.
```

No measure-preserving map between these is merged.

```text
COMMON_COMPLETION_TO_GAUSSIAN_PRIME_OCCUPANCY_ADAPTER_PROVED=false
COMMON_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
```

## q17 ledger

```text
Q_COMPONENT=COMPLETE
Q_TRIGGER_STAGE=Stage14-4gd+Stage14-4ge
EXACT_Q_OBSTRUCTION=FixedAgreementPairRadialLinearTwoLevelDivisorCRTReciprocalSolvabilitySupport
Q_LEDGER_BASELINE=Stage14-q16
Q_RESULT_IMPORTED_BACK_TO_X=true
Q17_DIRECT_FULL_OBSTRUCTION_THEOREM_COUNT=0
Q17_RECIPROCAL_CRT_SUPPORT_DIRECT_THEOREM_FOUND=false
Q17_PRIMARY_HANDOFF=Q17_EXPLICIT_RECIPROCAL_SELECTOR_CONSTRUCTION_OR_MOMENT_SUPPORT_TRANSFER_TEST
```

q17 supersedes q16 only as the active fixed-E literature target. It does not invalidate q16's completed ambient product-capacity conclusion.

```text
Q16_AMBIENT_PRODUCT_CAPACITY_RESULT_REMAINS_VALID=true
Q16_AS_CURRENT_FIXED_E_LITERATURE_TARGET_SUPERSEDED=true
Q17_POST_MASK_SEARCHED=false
Q17_FIXED_U_SEARCHED=false
```

## Exponent and H locks

The broad mainline H ledger retains the three pre-existing non-heavy targets. The current heavy reciprocal-completion branch opens no new H yet; Stage14-4gf must first test explicit divisor-choice/CRT constructions.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_INTEGRATED_WHOLE_FAMILY_POWER_SAVING_PROVED=false
MAINLINE_H_NEEDED=true
MAINLINE_H_TARGET=CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity_OR_FixedPolynomialCommonCoreCanonicalAllocationOffDiagonalProjectiveCollisionDispersion_OR_DiffusePolynomialComplementaryGaussianFactorCanonicalAllocationBilinearCorrelation
NEW_HEAVY_MAIN_H_NEEDED=false
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=false
TH33_NEEDED=false
WHOLE_MAINLINE_BLOCKED_BY_H=false
```

## Current receivers

```text
CURRENT_GLOBAL_RECEIVER=
  PrecompletionSupportDeficit
  OR ExistentialReversePostColumnCompletionDeficit
  with FixedETwoSidedReciprocalDivisorCRTSubreceiver

CURRENT_FIXED_U_RECEIVER=
  SharedUResidueNormalizedSingleInterval
  OR ResidueHostNormalizedManyEndpoint
  OR BeyondMitsuiLongBias
```

## Next integrated target

```text
ReciprocalCRTAndExistentialCompletionSupportVersusResidueNormalizedPrimeOccupancyOrNoGo
```

Normal revisit:

```text
4gh + s7-116 + t152
```

or earlier on a material reciprocal-CRT construction result, reverse/post-column theorem target, new fixed-U H target, common adapter, receiver change or exponent change.
