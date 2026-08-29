# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_J2_INDEPENDENT_ELLIPTIC_2TORSION_OBSERVATION_MATERIALIZED_4_OF_5`

Stage33-12 remains open. Stage33-07 remains open. Stage33-13 is not released.

## Authoritative receiver state

- `P=Br(Sbar)[2]^{G_Q}`: exact F2 dimension `10`.
- `H^1(V4,Pic(Sbar)/2)`: exact F2 dimension `75`.
- Future finite-V4 Kummer matrix: `75 x 10`, materialized columns `0/10`.
- Stage33-11 localization connecting map: audited exact zero on `26/26` directions.

## Retained named J2 / semantic PicK state

`E_J2 = 2*infinity_minus - P_plus - P_minus`, with `div(ell_J2)=2E_J2`.
The named Stoll branch is exactly `CsK[22]`; `P_inf_K=[1:0:0:0:-1:-1]` is the attached A1 exceptional point.

The exact transcendental lattice and geometric 2-torsion Brauer target remain

```text
T(Kc) = <4> direct_sum <8>
Br(Kc)[2] = Hom(T,Z/2) = (1/2 T*)/T*
beta1 = t1/8 -> [1,0]
beta2 = t2/16 -> [0,1]
```

The named nonzero J2 Brauer class is still one of `[1,0]`, `[0,1]`, `[1,1]` in this marked half-dual basis.

## Retained route reductions

The branch-cohomological map is exact but equivalent for the current marked receiver:

```text
BRANCH_COHOMOLOGICAL_MAP=EQUIVALENT_FOR_CURRENT_MARKED_RECEIVER
```

Certificate: `j2-branch-cohomology-route-reduction.json`.
Canonical SHA256: `c3f16d2712888b853e40ca8aaef69a3ed8e6f6409d13ffc47e83e33217ae6b41`.

The three nonzero Brauer functionals have pairwise non-isometric index-two kernel lattices:

```text
[1,0] -> diag(8,16),              minimum norm 8
[0,1] -> diag(4,32),              minimum norm 4
[1,1] -> [[12,-4],[-4,12]],       minimum norm 12
```

Certificate: `j2-brauer-kernel-lattice-fingerprints.json`.
Canonical SHA256: `572ad201ca859c5970507dbc598ac0489fdd90d10ee74ffc58f5e2f3fba7927e`.

Per the tightened loop guard, this three-to-three fingerprint dictionary is structural preparation and does not by itself count as receiver reduction.

## New independent J2-side observation

The retained Stage33-05 normalization is the genus-one quartic

```text
C: z^2 = t^4 - 6 t^2 + 1.
```

Its binary-quartic invariants are `I=48`, `J=0`, hence its Jacobian has `j=1728`.

There is an explicit degree-two map

```text
phi : C -> E'
X = t^2
Y = t z
E' : Y^2 = X (X^2 - 6 X + 1).
```

Both quartic points at infinity map to the identity `O` of `E'`. The two finite points occurring in the named J2 half-divisor satisfy

```text
P_plus  : t=1+sqrt(2), z=0  -> T_plus  =(3+2sqrt(2),0)
P_minus : t=1-sqrt(2), z=0  -> T_minus =(3-2sqrt(2),0).
```

The three nonzero points of `E'[2]` are

```text
(0,0), (3+2sqrt(2),0), (3-2sqrt(2),0),
```

so `T_plus + T_minus = (0,0)`. Therefore the named divisor class has the exact pushforward

```text
phi_*(E_J2) = (0,0) in E'[2].
```

This is a genuine J2-side observation: it was computed from the named J2 normalization/support and does not assume any of the three possible marked Brauer coordinates.

Certificate: `j2-normalization-2isogeny-rational-torsion.json`.
Canonical SHA256: `81097b3eab3b9f17de5a802b88324c74a7ab80e09c70dc179d4c5af4abd04571`.
Network-free verifier: `certify_j2_normalization_2isogeny_rational_torsion.py`.

Semantic firewall: this does **not** yet identify `[1,0]`, `[0,1]`, or `[1,1]`. A proved transport from this rational elliptic 2-torsion datum to the fixed K3 transcendental marking is still required.

## Anti-loop / wrong-weapon guard

`stages/stage33/LOOP-GUARD.md` is tightened so that a bijection from the three Brauer candidates to three new labels no longer resets stagnation. Reset now requires candidate reduction, a named-J2 independent observation, an actual semantic adapter, or permanent elimination of a distinct route.

Current state:

```text
LOOP_GUARD_ACTIVE=true
LOOP_STAGNATION_COUNT=0
LOOP_ACTIVE_RECEIVER=named CV J2 -> Br(Kc)[2]=Hom(T(Kc),Z/2)
LOOP_ACTIVE_MISSING_INTERFACE=transport phi_*(E_J2)=(0,0) on the explicit elliptic quotient to the fixed K3 marked transcendental/Brauer basis
LOOP_NEW_EXACT_INFORMATION=named J2 normalization has explicit degree-two elliptic quotient and rational 2-torsion pushforward
LOOP_J2_INDEPENDENT_OBSERVATION=phi_*(E_J2)=(0,0) in E'[2]
LOOP_CANDIDATES_REMOVED_THIS_BATCH=0
LOOP_EXHAUSTIVE_VIEW_AUDIT_REQUIRED=false
LOOP_BLIND_REDISCOVERY_REQUIRED=false
```

The candidate ledger is now

```text
BRANCH_COHOMOLOGICAL_MAP                  EQUIVALENT / ARCHIVED
KERNEL_LATTICE_FINGERPRINT_IDENTIFICATION LIVE / COMPARISON DICTIONARY
SHIODA_INOSE_OR_CM_MODEL_MARKING          LIVE / PREFERRED TRANSPORT ROUTE
DIRECT_TOPOLOGICAL_OR_BFIELD_EVALUATION   LIVE / FALLBACK
GOOD_REDUCTION_ETALE_SPECIALIZATION       UNTESTED
```

## Visible progress

```text
1/5 named J2 half-divisor and CV support adapter                           DONE
2/5 pinned Stoll branch/support identification                            DONE
3/5 infinity exceptional geometric attachment                             DONE
4/5 explicit marked PicK coordinate for J2 carrier + infinity exceptional DONE
5/5 branch-Jacobian 2-torsion -> Kc marked Brauer/Kummer glue             IN_PROGRESS
    T(Kc)=diag(4,8) and marked Br(Kc)[2]                                  DONE
    branch cohomology alternative                                         EQUIVALENT / ARCHIVED
    three candidate twisted-kernel fingerprints                           DONE / COMPARISON ONLY
    named J2 elliptic quotient 2-torsion image                            DONE: (0,0)
    transport named elliptic 2-torsion datum to marked K3 Brauer basis    OPEN
```

## Current exit state

```text
J2_NAMED_ELLIPTIC_QUOTIENT_2TORSION_IMAGE=(0,0)
J2_INDEPENDENT_OBSERVATION_MATERIALIZED=true
J2_NAMED_TRANSCENDENTAL_FUNCTIONAL_MATERIALIZED=false
J2_TWISTED_TRANSCENDENTAL_KERNEL_IDENTIFIED=false
J2_BRANCH_JACOBIAN_TO_DISCRIMINANT_KUMMER_GLUE_MATERIALIZED=false
J2_KC_DISCRIMINANT_COORDINATE_MATERIALIZED=false
FINITE_V4_KUMMER_DEFECT_COLUMNS_MATERIALIZED=0
ARITHMETIC_HS_D2_COMPUTED=false
STAGE33_07_HOSTILE_REAUDIT=NOT_RUN
STAGE33_12_CLOSED=false
```

Next exact leaf: `CONSTRUCT_A_PROVED_SHIODA_INOSE_OR_CM_TRANSPORT_FROM_THE_NAMED_RATIONAL_2TORSION_IMAGE_(0,0)_TO_THE_FIXED_T_KC_DIAG_4_8_BRAUER_MARKING_OR_FALL_BACK_TO_ONE_DIRECT_MARKED_T_CYCLE_EVALUATION`.

No 33-13 release, theorem/receiver/endpoint credit, or perfect-cuboid existence/nonexistence claim is granted by this checkpoint.
