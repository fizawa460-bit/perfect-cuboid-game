# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_J2_TRANSCENDENTAL_MARKING_ADAPTER_OPEN_4_OF_5`

Stage33-12 remains open. Stage33-07 remains open. Stage33-13 is not released.

## Authoritative receiver state

- `P=Br(Sbar)[2]^{G_Q}`: exact F2 dimension `10`.
- `H^1(V4,Pic(Sbar)/2)`: exact F2 dimension `75`.
- Future finite-V4 Kummer matrix: `75 x 10`, materialized columns `0/10`.
- Stage33-11 localization connecting map: audited exact zero on `26/26` directions.

## Retained named J2 / semantic PicK state

`E_J2 = 2*infinity_minus - P_plus - P_minus`, with `div(ell_J2)=2E_J2`.
The named Stoll branch is exactly `CsK[22]`; `P_inf_K=[1:0:0:0:-1:-1]` is the attached A1 exceptional point.

The order-independent semantic PicK basis has determinant `-32`, index one, with `[CsK[22]]=e8` and the infinity exceptional `e18`. The semantic discriminant target is exact:

```text
A_PicK[2] = (F2)^2
J2 candidate set = {u1/2, u2/2, (u1+u2)/2}
```

No candidate is selected yet.

## Exact interface reduction

The Creutz--Viray ruled-surface theorem gives the exact sequence

```text
NS(Kc)/2NS(Kc) --(x-alpha)--> Lc,E --gamma--> Br(Kc)[2] --> 0.
```

Thus the CV side canonically supplies the two-dimensional quotient with named basis `[J2,q1]`. Independently, the semantic Picard computation supplies the two-dimensional target `A_PicK[2]` with basis `[u1/2,u2/2]`.

These are two exact two-dimensional F2 spaces, but the retained data do not yet contain a canonical identification between them. The set of linear identifications is a `GL(2,F2)` torsor of size six, and the possible nonzero image of named `J2` remains exactly the three semantic candidates.

Crucially, the CV theorem itself does not identify `Br(Kc)[2]` with `A_PicK[2]`. The latter identification passes through the transcendental lattice / primitive embedding into the unimodular K3 lattice. Therefore Picard lattice data, its Galois action, the historical Smith frame, and the bare discriminant connecting map cannot manufacture the missing marking.

Certificate: `j2-cv-to-discriminant-marking-obstruction.json`
Canonical SHA256: `1366726812db7828e14a6f5c40d862e16b08856ba8278c9c1781f0a3d40eb5dd`.
Network-free verifier: `certify_j2_cv_to_discriminant_marking_obstruction.py`.

The theorem source is Creutz--Viray, *On Brauer groups of double covers of ruled surfaces*, arXiv:1306.3251, Theorem I / Corollary 5.4 and the proof of Theorem I. The theorem proves the CV quotient presentation; it does **not** provide the missing transcendental marking.

## Rejected shortcuts retained

- HS-d2 parity as a direct orientation bit: `REJECTED_EXACTLY`.
- Unsupported classical Kummer `(16_6)` transfer: `REJECTED_EXACTLY`.
- Historical Smith frame alone: `INSUFFICIENT_EXACTLY`.
- Bare Picard-discriminant Galois connecting signature: `REJECTED_EXACTLY`.
- Unique-isotropic-vector guess: `FORBIDDEN_WITHOUT_CV_SIDE_QUADRATIC/B-FIELD_COMPATIBILITY`.

## Visible progress

```text
1/5 named J2 half-divisor and CV support adapter                           DONE
2/5 pinned Stoll branch/support identification                            DONE
3/5 infinity exceptional geometric attachment                             DONE
4/5 explicit marked PicK coordinate for J2 carrier + infinity exceptional DONE
5/5 branch-Jacobian 2-torsion -> Kc discriminant Kummer glue              IN_PROGRESS
    semantic Kc discriminant 2-torsion target                              DONE
    exact CV quotient presentation                                         DONE
    GL2(F2) marking obstruction isolated                                   DONE
    named J2 B-field/transcendental-cycle evaluation                       OPEN
```

## Current exit state

```text
J2_PTSK_ORDER_DEPENDENCY=ELIMINATED
J2_SEMANTIC_PICARD_BASIS_MATERIALIZED=true
J2_CSK22_PICARD_COORDINATE=e8
J2_INFINITY_EXCEPTIONAL_PICARD_COORDINATE=e18
J2_SEMANTIC_KC_DISCRIMINANT_2TORSION_TARGET_MATERIALIZED=true
J2_SEMANTIC_KC_DISCRIMINANT_2TORSION_CANDIDATES=3
J2_CV_TO_DISCRIMINANT_MARKING_OBSTRUCTION_MATERIALIZED=true
J2_CV_TO_DISCRIMINANT_GL2_ADAPTER_COUNT=6
J2_NAMED_BFIELD_OR_TRANSCENDENTAL_EVALUATION_MATERIALIZED=false
J2_BRANCH_JACOBIAN_TO_DISCRIMINANT_KUMMER_GLUE_MATERIALIZED=false
J2_KC_DISCRIMINANT_COORDINATE_MATERIALIZED=false
FINITE_V4_KUMMER_DEFECT_COLUMNS_MATERIALIZED=0
ARITHMETIC_HS_D2_COMPUTED=false
STAGE33_07_HOSTILE_REAUDIT=NOT_RUN
STAGE33_12_CLOSED=false
```

Next exact leaf: `MATERIALIZE_ONE_NAMED_CV_J2_BFIELD_OR_TRANSCENDENTAL_CYCLE_EVALUATION_THEN_MATCH_THROUGH_K3_UNIMODULAR_DISCRIMINANT_GLUE`.

No 33-13 release, theorem/receiver/endpoint credit, or perfect-cuboid existence/nonexistence claim is granted by this checkpoint.
