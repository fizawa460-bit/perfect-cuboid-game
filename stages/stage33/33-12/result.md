# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_J2_ORIENTATION_INTERFACE_GAP_PINNED_4_OF_5`

Stage33-12 remains open. Stage33-07 remains open. Stage33-13 is not released.

## Authoritative receiver state

- `P=Br(Sbar)[2]^{G_Q}`: exact F2 dimension `10`.
- `H^1(V4,Pic(Sbar)/2)`: exact F2 dimension `75`.
- Future finite-V4 Kummer matrix: `75 x 10`, materialized columns `0/10`.
- Stage33-11 localization connecting map: audited exact zero on `26/26` directions.

## Retained named J2 / semantic PicK state

`E_J2 = 2*infinity_minus - P_plus - P_minus`, with `div(ell_J2)=2E_J2`.
The named Stoll branch is exactly `CsK[22]`; `P_inf_K=[1:0:0:0:-1:-1]` is the attached A1 exceptional point.

The order-independent semantic PicK basis has determinant `-32`, index one, with `[CsK[22]]=e8` and the infinity exceptional `e18`.
Certificate SHA256:

```text
c17439c877de3d1cdebd716f4ba2571fb67ec9f07e30d944eafc39ae534380c0
```

The semantic discriminant target is exact:

```text
A_PicK[2] = (F2)^2
J2 candidate set = {u1/2, u2/2, (u1+u2)/2}
```

with canonical target SHA256 `0b5d7dfdefbb0f2b7c37396ada35c0bee462dfeb625eb18262be0e862205d8df`. No candidate is selected yet.

## Prior exact reduction retained

The Stage33-05 `q1` HS/Bockstein odd test parity cannot be used as the missing J2 orientation bit: every semantic discriminant numerator lies in `rad(G mod 2)` and pairs evenly with integral PicK. The shortcut remains `REJECTED_EXACTLY`.

## New exact reduction: the missing object is an interface, not another Smith computation

A named COLD expansion was performed because the current leaf lacked the load-bearing presentation/discriminant adapter.

Historical exact generators were recovered:

```text
4be96346dd2353ae9ef7d86a7451487cf229f2a6
  Stage33-07: split Kc Picard maps for HS regression

6c1c2bebec8e973dc6712eb0b9f31cc03335537e
  Stage33-07: derive Kc discriminant action from split shards
```

The first deterministically extracts the Kc Gram, `MatKtoS`, `MatStoK`, and Smith right transform `V`; the Smith type is exactly

```text
[1^18,4,8].
```

The second uses that frame to compute Galois action and the discriminant bilinear data. Crucially, neither generator maps the named Creutz--Viray quotient basis `[J2,q1]` into the Smith/discriminant coordinate frame. The later compact discriminant certificate merely attaches the already audited labels `kernel basis=['J2']` and `nonzero class='q1'` after the coordinate-frame calculation. Therefore regenerating Smith `V` alone cannot choose one of the three semantic J2 candidates.

A second tempting route is also rejected. The pinned Stoll Kc construction has exactly `12` singular nodes (`kc-picard-lattice.json`) and does not provide a classical 16-node/trope `(16_6)` Kummer marking. Importing a classical `(16_6)` theta-incidence marking would therefore be an unsupported semantic transfer.

The exact missing interface is now pinned as

```text
ONE_CV_J2_PRESENTATION_TO_PICARD_DISCRIMINANT_FUNCTIONAL
OR_EQUIVALENT_NAMED_CHANGE_OF_BASIS_BIT
```

Certificate: `j2-kc-orientation-interface-gap.json`
Canonical SHA256: `7b6002e54f2d6d746de7917ec017d35e9e143522869201c1cfad5109a22958fa`.

## Visible progress

```text
1/5 named J2 half-divisor and CV support adapter                           DONE
2/5 pinned Stoll branch/support identification                            DONE
3/5 infinity exceptional geometric attachment                             DONE
4/5 explicit marked PicK coordinate for J2 carrier + infinity exceptional DONE
5/5 branch-Jacobian 2-torsion -> Kc discriminant Kummer glue              IN_PROGRESS
    semantic Kc discriminant 2-torsion target                              DONE
    HS-d2 parity shortcut                                                   EXACTLY_REJECTED
    unsupported classical Kummer (16_6) shortcut                           EXACTLY_REJECTED
    historical Smith-frame-only shortcut                                   INSUFFICIENT_EXACTLY
    CV J2 presentation -> PicK discriminant functional                     OPEN
```

## Current exit state

```text
J2_PTSK_ORDER_DEPENDENCY=ELIMINATED
J2_SEMANTIC_PICARD_BASIS_MATERIALIZED=true
J2_CSK22_PICARD_COORDINATE=e8
J2_INFINITY_EXCEPTIONAL_PICARD_COORDINATE=e18
J2_SEMANTIC_KC_DISCRIMINANT_2TORSION_TARGET_MATERIALIZED=true
J2_SEMANTIC_KC_DISCRIMINANT_2TORSION_CANDIDATES=3
J2_HS_PARITY_ORIENTATION_SHORTCUT=REJECTED_EXACTLY
J2_CLASSICAL_KUMMER_16_6_SHORTCUT=REJECTED_UNSUPPORTED_TRANSFER
J2_HISTORICAL_SMITH_FRAME_REGENERABLE=true
J2_NAMED_PRESENTATION_TO_DISCRIMINANT_ADAPTER_MATERIALIZED=false
J2_BRANCH_JACOBIAN_TO_DISCRIMINANT_KUMMER_GLUE_MATERIALIZED=false
J2_KC_DISCRIMINANT_COORDINATE_MATERIALIZED=false
FINITE_V4_KUMMER_DEFECT_COLUMNS_MATERIALIZED=0
ARITHMETIC_HS_D2_COMPUTED=false
STAGE33_07_HOSTILE_REAUDIT=NOT_RUN
STAGE33_12_CLOSED=false
```

Next exact leaf: `CONSTRUCT_ONE_CV_J2_PRESENTATION_TO_PICARD_DISCRIMINANT_FUNCTIONAL_AND_EVALUATE_ON_THREE_SEMANTIC_CANDIDATES`.

No 33-13 release, theorem/receiver/endpoint credit, or perfect-cuboid existence/nonexistence claim is granted by this checkpoint.
