# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_J2_KUMMER_EXTENSION_ADAPTER_OPEN_4_OF_5`

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

## Prior exact reductions retained

The Stage33-05 `q1` HS/Bockstein odd test parity cannot be used as the missing J2 orientation bit: every semantic discriminant numerator lies in `rad(G mod 2)` and pairs evenly with integral PicK. The shortcut remains `REJECTED_EXACTLY`.

Historical Smith `V` is reproducible but does not contain the named `[J2,q1] -> discriminant` change of basis. A classical Kummer `(16_6)` marking is also unavailable in the pinned 12-node Kc model and is not imported.

## New exact reduction: lattice Galois connecting also cannot select J2

The pinned Stoll definition gives `ct: sqrt(2)->-sqrt(2), i fixed`. In the exact curve enumeration:

```text
CsK[1..26]  ct-fixed
CsK[47] <-> CsK[49]
CsK[52] <-> CsK[54]
```

The semantic half-lattice numerators have supports

```text
u1 : semantic positions [1,2,5,6,14,15]
     curve slots        [2,4,9,10,47,49]

u2 : semantic positions [16,17]
     curve slots        [52,54]
```

Hence `u1` and `u2` are each fixed exactly as integral divisor sums by `ct`; therefore `u1/2`, `u2/2`, and `(u1+u2)/2` all admit an exactly `ct`-fixed dual-lattice representative. The connecting cocycle from the bare lattice sequence `PicK -> PicK^* -> A_PicK` is therefore zero on all three candidates.

By contrast, the hostile-audited Creutz--Viray presentation has

```text
ct(J2)-J2 = 0
ct(q1)-q1 = J1 != 0 in the presentation relation module.
```

Therefore the bare Picard-discriminant Galois connecting map is **not** the CV/Kummer extension connecting map and cannot identify the named J2 coordinate.

Certificate: `j2-picard-discriminant-galois-functional-rejection.json`
Canonical SHA256: `ae980dae7e33ecf58e35d697dde1c1be20c98c170bde6b6b9591e9b1f8680e54`.
Network-free verifier: `certify_j2_picard_discriminant_galois_functional_rejection.py`.

This agrees with the already retained `full-surface-pic2-kummer-target.json` information boundary: Picard action is known, but the **Kummer extension class is missing**. The remaining interface is therefore not another action matrix or parity functional; it is the genuine CV `x-alpha` / Kummer extension-class adapter into the semantic PicK discriminant frame.

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
    bare Picard-discriminant Galois connecting shortcut                    EXACTLY_REJECTED
    genuine CV/Kummer extension-class adapter                              OPEN
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
J2_PICARD_DISCRIMINANT_GALOIS_CONNECTING_SHORTCUT=REJECTED_EXACTLY
J2_GENUINE_CV_KUMMER_EXTENSION_ADAPTER_MATERIALIZED=false
J2_BRANCH_JACOBIAN_TO_DISCRIMINANT_KUMMER_GLUE_MATERIALIZED=false
J2_KC_DISCRIMINANT_COORDINATE_MATERIALIZED=false
FINITE_V4_KUMMER_DEFECT_COLUMNS_MATERIALIZED=0
ARITHMETIC_HS_D2_COMPUTED=false
STAGE33_07_HOSTILE_REAUDIT=NOT_RUN
STAGE33_12_CLOSED=false
```

Next exact leaf: `CONSTRUCT_GENUINE_CV_XALPHA_KUMMER_EXTENSION_CLASS_ADAPTER_TO_SEMANTIC_PICARD_DISCRIMINANT_AND_EVALUATE_J2`.

No 33-13 release, theorem/receiver/endpoint credit, or perfect-cuboid existence/nonexistence claim is granted by this checkpoint.
