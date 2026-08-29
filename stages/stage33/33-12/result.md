# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_J2_MARKED_TRANSCENDENTAL_CYCLE_OPEN_4_OF_5`

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

No named J2 candidate is selected yet.

## Exact CV/discriminant interface reduction

The Creutz--Viray ruled-surface presentation supplies an exact two-dimensional quotient with named basis `[J2,q1]`, while the semantic Picard computation supplies the two-dimensional discriminant 2-torsion target. The retained data still do not canonically identify those two marked F2 spaces; the adapter remains a `GL(2,F2)` torsor before additional transcendental marking data are used.

Certificate: `j2-cv-to-discriminant-marking-obstruction.json`, canonical SHA256 `1366726812db7828e14a6f5c40d862e16b08856ba8278c9c1781f0a3d40eb5dd`.

## New exact reduction: T(Kc) is fixed up to isometry

Because `rho(Kc)=20`, the K3 transcendental lattice has rank two. The semantic Picard lattice has determinant `-32` and discriminant group `Z/4 direct_sum Z/8`. For a primitive Neron--Severi lattice inside the even unimodular K3 lattice, `A_T` and `A_NS` have opposite discriminant quadratic forms.

An exhaustive Gauss-reduced enumeration of positive definite even rank-two lattices of determinant `32` gives only

```text
[[2,0],[0,16]]      A = Z/2 + Z/16
[[4,0],[0,8]]       A = Z/4 + Z/8
[[6,-2],[-2,6]]     A = Z/2 + Z/16
[[6,2],[2,6]]       A = Z/2 + Z/16
```

so the transcendental lattice is fixed up to isometry as

```text
T(Kc) ~= <4> direct_sum <8>.
```

The certificate also materializes an explicit anti-isometry witness from the discriminant generators `t1/4, t2/8` to the semantic NS discriminant: the two NS images have orders `4,8`, quadratic values `7/4,15/8`, cross-pairing `0 mod Z`, and generate all `32` discriminant classes. Thus this is stronger than a determinant-only classification.

Certificate: `j2-kc-transcendental-lattice-isometry.json`.
Canonical SHA256: `b7f2bcfa29c01731ea2f10d22db898ad57317f140b547f91e3d3a27a0faf1010`.
Network-free verifier: `certify_j2_kc_transcendental_lattice_isometry.py`.

This does **not** mark the basis `(t1,t2)` by the named CV basis `[J2,q1]`. Therefore the J2 coordinate is still one of three nonzero mod-2 functionals; the unique-isotropic guess remains forbidden.

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
    transcendental lattice isometry T(Kc)=diag(4,8)                        DONE
    explicit NS/T discriminant anti-isometry witness                       DONE
    named J2 evaluation on one marked transcendental cycle                 OPEN
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
KC_TRANSCENDENTAL_LATTICE_ISOMETRY_MATERIALIZED=true
KC_TRANSCENDENTAL_LATTICE_GRAM=[[4,0],[0,8]]
KC_NS_T_DISCRIMINANT_ANTI_ISOMETRY_WITNESS_MATERIALIZED=true
J2_NAMED_TRANSCENDENTAL_FUNCTIONAL_MATERIALIZED=false
J2_BRANCH_JACOBIAN_TO_DISCRIMINANT_KUMMER_GLUE_MATERIALIZED=false
J2_KC_DISCRIMINANT_COORDINATE_MATERIALIZED=false
FINITE_V4_KUMMER_DEFECT_COLUMNS_MATERIALIZED=0
ARITHMETIC_HS_D2_COMPUTED=false
STAGE33_07_HOSTILE_REAUDIT=NOT_RUN
STAGE33_12_CLOSED=false
```

Next exact leaf: `EVALUATE_NAMED_CV_J2_ON_ONE_MARKED_TRANSCENDENTAL_CYCLE_IN_T_DIAG_4_8_OR_PROVE_A_COMPATIBLE_BFIELD_QUADRATIC_INVARIANT`.

No 33-13 release, theorem/receiver/endpoint credit, or perfect-cuboid existence/nonexistence claim is granted by this checkpoint.
