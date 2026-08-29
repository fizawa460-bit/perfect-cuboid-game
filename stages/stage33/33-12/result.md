# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_NAMED_J2_KUMMER_GLUE_INPUT_MATERIALIZED`

This checkpoint continues the exact arithmetic Hochschild--Serre assembly after the audited Stage33-11 exit. It does not close Stage33-12 or Stage33-07.

## Exact receiver state

Stage33-11 has already proved the localization connecting map exact zero on all 26 finite directions. Stage33-12 has independently linearized the full-surface finite-V4 Kummer receiver:

* `P=Br(Sbar)[2]^{G_Q}` has exact F2 dimension 10;
* `H^1(V4,Pic(Sbar)/2)` has exact F2 dimension 75;
* the missing finite restriction is therefore a literal `75 x 10` matrix;
* materialized columns remain `0/10` and finite obstruction cosets remain `0/26`.

Known Q-defined blocks, including J2, have exact HS image zero. Odd-primary global residue-lift completion is exact. The two remaining obstruction blocks are still the two-primary constant-character cokernel and the finite 26-direction block.

## J2/q1 adapter state

The named K3 basis is hostile-audited as `[J2,q1]`, with `d2(J2)=0` and `d2(q1)!=0`. The retained ambiguity witness enumerates all six elements of `GL(2,F2)`: all six survive the currently retained named d2 data, and even after the Kc kernel line `<J2>` is fixed exactly two adapters remain because `q1` and `q1+J2` have the same nonzero d2.

Certificate: `j2-q1-kc-adapter-ambiguity-witness.json`, canonical SHA256 `2d41bf2d5961fa16caf162311974a858329f2714ec1fe3838305c58e6da79ffb`.

## New exact progress: named J2 Kummer-glue input

`certify_j2_named_kummer_glue_input.py` source-locks the committed Stage33-05 J2 arithmetic representative, the full-surface zero-defect contract, the Stage33-09 marked Picard bridge, and the pinned Stoll source. It materializes the named geometric input needed by a genuine Kummer-glue reconstruction:

* normalization: `z^2=t^4-6*t^2+1`;
* named squareclass: `f2=(t-r2)/(t-r4)`, with `r2=-(1+sqrt(2))`, `r4=1-sqrt(2)`;
* Q-defined branch representative `ell_J2` from Stage33-05;
* exact geometric divisor `div(ell_J2)=4*infinity_minus-2*P1-2*P2`;
* hence the exact named half-divisor
  `E=2*infinity_minus-P1-P2`, with `div(ell_J2)=2E`.

The pinned Stoll code supplies the rank-20 `PicK`, its 20-element known-curve generating interface, `imageinPicK(C)` from intersection data, and the exact `MatStoK` / `MatKtoS` transport. The missing bridge is now stated narrowly: no committed adapter identifies `infinity_minus` and the two `Dplus` support points (or directly `E`) with Stoll marked divisor classes, and no committed Kummer/Picard-transcendental glue map sends that named data to the Kc discriminant/Brauer coordinate.

This distinction matters: merely putting `E` into `PicK` would not by itself justify assigning a Brauer discriminant coordinate. The Kummer-glue step must be explicit.

Retained certificate: `j2-named-kummer-glue-input.json`, canonical SHA256 `18e320e82c9c975f35413c1fe365889c2fa803f2ac0595609d8c6044aa32f0b5`.

## Current exact gap

The next exact route is now:

1. materialize the images of `infinity_minus` and the two roots of `Dplus`, or directly `E`, in the pinned marked Kc divisor presentation;
2. apply an exact Kummer/Picard-transcendental glue map to the named half-divisor plus the Q-defined corestriction representative;
3. read the resulting nonzero Kc Br[2] line and filter the six adapters;
4. if that construction does not simultaneously identify q1, supply one further named invariant distinguishing `q1` from `q1+J2`.

Until this is done, J2 is not assigned to the original proper-Br2 14 coordinates or the retained P10 basis. The abstract J2 zero-defect continues to imply only the exact rank bound `rank <= 9`; it does not materialize a matrix column or a P10 linear relation.

## Current exit state

```text
ARITHMETIC_HS_D2_COMPUTED=false
GLOBAL_Q_BR0G_RESIDUE_LIFTS_COMPLETE=false
COMPLETE_RELEVANT_Q_DEFINED_CLASS_LIST_FOR_STAGE33_BRAUER_SCOPE=false
J2_Q1_KC_ADAPTER_UNIQUE=false
J2_NAMED_HALF_DIVISOR_MATERIALIZED=true
J2_KC_DISCRIMINANT_COORDINATE_MATERIALIZED=false
FINITE_V4_KUMMER_DEFECT_COLUMNS_MATERIALIZED=0
STAGE33_07_HOSTILE_REAUDIT=NOT_RUN
STAGE33_12_CLOSED=false
```

The next exact leaf is `MATERIALIZE_J2_HALF_DIVISOR_E_IN_STOLL_MARKED_KC_PRESENTATION_AND_KUMMER_GLUE`. The known Q-defined prefix, Stage33-11 zero connecting map, and zero boundary scalar adapter must not be recomputed.

All Stage33-07/08/40, theorem, endpoint, receiver, and perfect-cuboid existence/nonexistence firewalls remain closed.
