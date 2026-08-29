# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_J2_LOOP_GUARD_ACTIVE_DIRECT_BFIELD_EVALUATION_PREFERRED_4_OF_5`

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

The exact transcendental lattice and geometric 2-torsion Brauer target remain

```text
T(Kc) = <4> direct_sum <8>
Br(Kc)[2] = Hom(T,Z/2) = (1/2 T*)/T*
beta1 = t1/8 -> [1,0]
beta2 = t2/16 -> [0,1]
```

The named nonzero J2 class is still one of `[1,0]`, `[0,1]`, `[1,1]` in this marked half-dual basis.

## New exact route reduction: branch cohomology is not a new marking adapter

The loop-guard preferred route was tested against the double-cover cohomological description of the Brauer group. Skorobogatov's natural map

```text
Phi : Pic(C)[2] -> Br(X)[2]
```

with its exact sequence through the branch curve canonically constructs branch-origin 2-torsion Brauer classes. This confirms that the branch/Jacobian viewpoint is mathematically legitimate.

However, for the current receiver it does not add the missing marked coordinate: Creutz--Viray's retained `gamma` / CSA presentation already materializes the same named branch-origin J2 Brauer class abstractly. The unresolved step is still the comparison of that named Brauer class with the fixed basis of `Hom(T(Kc),Z/2)`.

Therefore the route is classified

```text
BRANCH_COHOMOLOGICAL_MAP=EQUIVALENT_FOR_CURRENT_MARKED_RECEIVER
```

and is archived rather than retried.

Certificate: `j2-branch-cohomology-route-reduction.json`.
Canonical SHA256: `c3f16d2712888b853e40ca8aaef69a3ed8e6f6409d13ffc47e83e33217ae6b41`.
Network-free verifier: `certify_j2_branch_cohomology_route_reduction.py`.

## Anti-loop / wrong-weapon guard

```text
LOOP_GUARD_ACTIVE=true
LOOP_STAGNATION_COUNT=0
LOOP_ACTIVE_RECEIVER=named CV J2 -> Br(Kc)[2]=Hom(T(Kc),Z/2)
LOOP_ACTIVE_MISSING_INTERFACE=compare named J2 Brauer class with fixed marked t1/t2 half-dual basis
LOOP_NEW_EXACT_INFORMATION=branch-cohomology route classified equivalent and archived
LOOP_CANDIDATES_REMOVED_THIS_BATCH=1
LOOP_EXHAUSTIVE_VIEW_AUDIT_REQUIRED=false
LOOP_BLIND_REDISCOVERY_REQUIRED=false
```

The candidate ledger is now

```text
BRANCH_COHOMOLOGICAL_MAP                 EQUIVALENT / ARCHIVED
DIRECT_TOPOLOGICAL_OR_BFIELD_EVALUATION LIVE / PREFERRED
SHIODA_INOSE_OR_CM_MODEL_MARKING         UNTESTED
GOOD_REDUCTION_ETALE_SPECIALIZATION      UNTESTED
```

Because the live candidate count decreased, this batch is not a stagnation batch under `LOOP-GUARD.md`.

## Retained rejected shortcut families

- HS-d2 parity as a Picard-discriminant orientation bit: `REJECTED_EXACTLY`.
- Unsupported classical Kummer `(16_6)` transfer: `REJECTED_EXACTLY`.
- Historical Smith frame alone: `INSUFFICIENT_EXACTLY`.
- Picard-discriminant Galois fixedness selector: `REJECTED_EXACTLY`.
- Kc automorphism/signature selector: `REJECTED_EXACTLY`.
- Unique-isotropic discriminant-vector guess as a Brauer selector: `REJECTED_EXACTLY_WRONG_QUOTIENT`.

## Visible progress

```text
1/5 named J2 half-divisor and CV support adapter                           DONE
2/5 pinned Stoll branch/support identification                            DONE
3/5 infinity exceptional geometric attachment                             DONE
4/5 explicit marked PicK coordinate for J2 carrier + infinity exceptional DONE
5/5 branch-Jacobian 2-torsion -> Kc discriminant Kummer glue              IN_PROGRESS
    semantic PicK / discriminant data                                      DONE
    T(Kc)=diag(4,8) and NS/T anti-isometry                                 DONE
    marked Br(Kc)[2] half-dual target                                      DONE
    branch cohomology alternative                                          EQUIVALENT / ARCHIVED
    direct named CV J2 CSA/B-field evaluation on marked t1/t2              OPEN / PREFERRED
```

## Current exit state

```text
J2_NAMED_TRANSCENDENTAL_FUNCTIONAL_MATERIALIZED=false
J2_BRANCH_JACOBIAN_TO_DISCRIMINANT_KUMMER_GLUE_MATERIALIZED=false
J2_KC_DISCRIMINANT_COORDINATE_MATERIALIZED=false
BRANCH_COHOMOLOGY_ROUTE_REDUCTION_MATERIALIZED=true
BRANCH_COHOMOLOGICAL_MAP_ROUTE_STATUS=EQUIVALENT_FOR_CURRENT_MARKED_RECEIVER
FINITE_V4_KUMMER_DEFECT_COLUMNS_MATERIALIZED=0
ARITHMETIC_HS_D2_COMPUTED=false
STAGE33_07_HOSTILE_REAUDIT=NOT_RUN
STAGE33_12_CLOSED=false
```

Next exact leaf: `EVALUATE_NAMED_CV_J2_CSA_OR_BFIELD_ON_MARKED_T1_OR_T2_CYCLE_IN_FIXED_HALFDUAL_TARGET`.

No 33-13 release, theorem/receiver/endpoint credit, or perfect-cuboid existence/nonexistence claim is granted by this checkpoint.
