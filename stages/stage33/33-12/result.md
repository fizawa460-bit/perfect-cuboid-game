# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_J2_LOOP_GUARD_ACTIVE_KERNEL_LATTICE_FINGERPRINTS_MATERIALIZED_4_OF_5`

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

## Branch cohomology route reduction retained

The double-cover branch map `Pic(C)[2] -> Br(X)[2]` is mathematically valid but does not supply the missing marked `Hom(T,Z/2)` coordinate beyond the already retained Creutz--Viray named CSA presentation. It remains archived as

```text
BRANCH_COHOMOLOGICAL_MAP=EQUIVALENT_FOR_CURRENT_MARKED_RECEIVER
```

Certificate: `j2-branch-cohomology-route-reduction.json`.
Canonical SHA256: `c3f16d2712888b853e40ca8aaef69a3ed8e6f6409d13ffc47e83e33217ae6b41`.

## New exact kernel-lattice fingerprint reduction

For any order-two Brauer class `alpha`, the B-field functional `alpha:T(Kc)->Z/2` determines the index-two kernel lattice `T(Kc,alpha)=ker(alpha)`. In the fixed marked lattice `T(Kc)=diag(4,8)`, the three nonzero candidates have pairwise non-isometric kernel lattices:

```text
alpha=[1,0]: kernel Gram ~= diag(8,16), determinant 128, minimum norm 8
alpha=[0,1]: kernel Gram  = diag(4,32), determinant 128, minimum norm 4
alpha=[1,1]: kernel Gram  = [[12,-4],[-4,12]], determinant 128, minimum norm 12
```

Thus a single exact fingerprint of the named J2 twisted transcendental kernel -- in particular its minimum norm -- selects the marked Brauer functional uniquely:

```text
minimum norm 4  -> J2=[0,1]
minimum norm 8  -> J2=[1,0]
minimum norm 12 -> J2=[1,1]
```

This is a genuine new comparison interface: direct integration on both marked cycles is no longer the only possible route. Any exact construction identifying `T(Kc,J2)` up to isometry suffices.

Certificate: `j2-brauer-kernel-lattice-fingerprints.json`.
Canonical SHA256: `572ad201ca859c5970507dbc598ac0489fdd90d10ee74ffc58f5e2f3fba7927e`.
Network-free verifier: `certify_j2_brauer_kernel_lattice_fingerprints.py`.

## Anti-loop / wrong-weapon guard

```text
LOOP_GUARD_ACTIVE=true
LOOP_STAGNATION_COUNT=0
LOOP_ACTIVE_RECEIVER=named CV J2 -> Br(Kc)[2]=Hom(T(Kc),Z/2)
LOOP_ACTIVE_MISSING_INTERFACE=identify T(Kc,J2) kernel lattice or equivalently evaluate named J2 on marked t1/t2
LOOP_NEW_EXACT_INFORMATION=three Brauer candidates now have pairwise non-isometric index-two kernel lattice fingerprints
LOOP_CANDIDATES_REMOVED_THIS_BATCH=0
LOOP_EXHAUSTIVE_VIEW_AUDIT_REQUIRED=false
LOOP_BLIND_REDISCOVERY_REQUIRED=false
```

The candidate ledger is now

```text
BRANCH_COHOMOLOGICAL_MAP                 EQUIVALENT / ARCHIVED
KERNEL_LATTICE_FINGERPRINT_IDENTIFICATION LIVE / PREFERRED
DIRECT_TOPOLOGICAL_OR_BFIELD_EVALUATION LIVE / PARALLEL FALLBACK
SHIODA_INOSE_OR_CM_MODEL_MARKING         UNTESTED / NATURAL INPUT TO KERNEL FINGERPRINT
GOOD_REDUCTION_ETALE_SPECIALIZATION      UNTESTED
```

This batch is not stagnation: the receiver is unchanged but the comparison interface gained a new load-bearing invariant which distinguishes all three candidates.

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
    T(Kc)=diag(4,8) and marked Br(Kc)[2]                                   DONE
    branch cohomology alternative                                          EQUIVALENT / ARCHIVED
    three candidate twisted-kernel lattice fingerprints                    DONE / PAIRWISE DISTINCT
    identify named J2 twisted kernel or direct t1/t2 evaluation             OPEN
```

## Current exit state

```text
J2_NAMED_TRANSCENDENTAL_FUNCTIONAL_MATERIALIZED=false
J2_TWISTED_TRANSCENDENTAL_KERNEL_IDENTIFIED=false
J2_BRANCH_JACOBIAN_TO_DISCRIMINANT_KUMMER_GLUE_MATERIALIZED=false
J2_KC_DISCRIMINANT_COORDINATE_MATERIALIZED=false
BRAUER_KERNEL_LATTICE_FINGERPRINTS_MATERIALIZED=true
BRAUER_KERNEL_LATTICE_MINIMUM_NORMS=[4,8,12]
FINITE_V4_KUMMER_DEFECT_COLUMNS_MATERIALIZED=0
ARITHMETIC_HS_D2_COMPUTED=false
STAGE33_07_HOSTILE_REAUDIT=NOT_RUN
STAGE33_12_CLOSED=false
```

Next exact leaf: `IDENTIFY_NAMED_CV_J2_TWISTED_TRANSCENDENTAL_KERNEL_LATTICE_UP_TO_ISOMETRY_OR_DIRECTLY_EVALUATE_ONE_MARKED_T_CYCLE`.

No 33-13 release, theorem/receiver/endpoint credit, or perfect-cuboid existence/nonexistence claim is granted by this checkpoint.
