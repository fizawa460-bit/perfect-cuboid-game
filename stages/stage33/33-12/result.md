# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_J2_INDEPENDENT_ELLIPTIC_2TORSION_OBSERVATION_AND_CM_TRANSPORT_REDUCTION_4_OF_5`

Stage33-12 remains open. Stage33-07 remains open. Stage33-13 is not released.

## Authoritative receiver state

- `P=Br(Sbar)[2]^{G_Q}`: exact F2 dimension `10`.
- `H^1(V4,Pic(Sbar)/2)`: exact F2 dimension `75`.
- Future finite-V4 Kummer matrix: `75 x 10`, materialized columns `0/10`.
- Stage33-11 localization connecting map: audited exact zero on `26/26` directions.

## Retained named J2 / marked Brauer state

```text
E_J2 = 2*infinity_minus - P_plus - P_minus
T(Kc) = <4> direct_sum <8>
Br(Kc)[2] = Hom(T,Z/2) = (1/2 T*)/T*
beta1 = t1/8 -> [1,0]
beta2 = t2/16 -> [0,1]
```

The named nonzero J2 Brauer class remains one of `[1,0]`, `[0,1]`, `[1,1]`.

The three nonzero functionals have pairwise non-isometric index-two kernel lattices:

```text
[1,0] -> diag(8,16),        minimum norm 8
[0,1] -> diag(4,32),        minimum norm 4
[1,1] -> [[12,-4],[-4,12]], minimum norm 12
```

Certificate: `j2-brauer-kernel-lattice-fingerprints.json`.
Canonical SHA256: `572ad201ca859c5970507dbc598ac0489fdd90d10ee74ffc58f5e2f3fba7927e`.

Per `LOOP-GUARD.md`, this three-to-three dictionary is comparison infrastructure, not candidate reduction.

## Independent J2-side observation

The Stage33-05 normalization is

```text
C: z^2=t^4-6t^2+1
```

with binary-quartic invariants `I=48`, `J=0`, so its Jacobian has `j=1728` and CM field `Q(i)`.

There is an explicit degree-two map

```text
phi:C -> E'
X=t^2
Y=t z
E': Y^2=X(X^2-6X+1).
```

The named supports map as

```text
P_plus  -> (3+2sqrt(2),0)
P_minus -> (3-2sqrt(2),0),
```

and the two images sum to the remaining rational nonzero 2-torsion point. Hence

```text
phi_*(E_J2)=(0,0) in E'[2].
```

This is a genuine named-J2 observation and does not assume a marked Brauer candidate.

Certificate: `j2-normalization-2isogeny-rational-torsion.json`.
Canonical SHA256: `81097b3eab3b9f17de5a802b88324c74a7ab80e09c70dc179d4c5af4abd04571`.
Network-free verifier: `certify_j2_normalization_2isogeny_rational_torsion.py`.

## Exact rejection of the naive Shioda-Mitani factor shortcut

For `T(Kc)=diag(4,8)`, the Shioda-Mitani quadratic form is

```text
(a,b,c)=(2,0,4), D=-32,
tau=i*sqrt(2),
a*tau+b=2*i*sqrt(2).
```

Thus the two elliptic factors in the canonical Shioda-Mitani abelian surface have CM field

```text
Q(sqrt(-2)).
```

The J2 normalization has `j=1728`, hence CM field `Q(i)`, and its explicit elliptic quotient `E'` is isogenous to it, so `E'` also has rational endomorphism algebra `Q(i)`.

Complex-isogenous elliptic curves have isomorphic rational endomorphism algebras. Since

```text
Q(i) != Q(sqrt(-2)),
```

there is no elliptic isogeny identifying the J2 normalization or `E'` with either Shioda-Mitani elliptic factor of `Kc`.

Therefore

```text
NAIVE_SHIODA_MITANI_ELLIPTIC_FACTOR_TRANSPORT=REJECTED_EXACTLY.
```

This does not rule out a genuinely K3-level Shioda-Inose correspondence; it only kills the tempting direct elliptic-factor shortcut.

Certificate: `j2-naive-shioda-mitani-factor-transport-rejection.json`.
Canonical SHA256: `1713ce4b2a88250e0110fc5b3863836f3b108e752e0911939b3687fc0540ab2b`.
Network-free verifier: `certify_j2_naive_shioda_mitani_factor_transport_rejection.py`.

## Anti-loop / wrong-weapon guard

`stages/stage33/LOOP-GUARD.md` now explicitly forbids resetting stagnation merely by relabelling the same three Brauer candidates. This batch remains non-stagnant because it both produced an independent named-J2 observation and permanently removed a materially distinct naive transport route.

```text
LOOP_GUARD_ACTIVE=true
LOOP_STAGNATION_COUNT=0
LOOP_ACTIVE_RECEIVER=named CV J2 -> Br(Kc)[2]=Hom(T(Kc),Z/2)
LOOP_ACTIVE_MISSING_INTERFACE=transport named J2 data to fixed marked t1/t2 Brauer basis
LOOP_NEW_EXACT_INFORMATION=phi_*(E_J2)=(0,0) plus exact CM-field mismatch for naive Shioda-Mitani factor transport
LOOP_J2_INDEPENDENT_OBSERVATION=phi_*(E_J2)=(0,0) in E'[2]
LOOP_CANDIDATES_REMOVED_THIS_BATCH=0
LOOP_ROUTES_REMOVED_THIS_BATCH=1
LOOP_EXHAUSTIVE_VIEW_AUDIT_REQUIRED=false
LOOP_BLIND_REDISCOVERY_REQUIRED=false
```

Current route ledger:

```text
BRANCH_COHOMOLOGICAL_MAP                    EQUIVALENT / ARCHIVED
KERNEL_LATTICE_FINGERPRINT_IDENTIFICATION   LIVE / COMPARISON DICTIONARY
NAIVE_SHIODA_MITANI_ELLIPTIC_FACTOR_ROUTE  REJECTED_EXACTLY
K3_LEVEL_SHIODA_INOSE_CORRESPONDENCE        UNTESTED / HIGHER-COST
DIRECT_TOPOLOGICAL_OR_BFIELD_EVALUATION     LIVE / PREFERRED
GOOD_REDUCTION_ETALE_SPECIALIZATION         UNTESTED
```

## Visible progress

```text
1/5 named J2 half-divisor and CV support adapter                           DONE
2/5 pinned Stoll branch/support identification                            DONE
3/5 infinity exceptional geometric attachment                             DONE
4/5 explicit marked PicK coordinate for J2 carrier + infinity exceptional DONE
5/5 branch-Jacobian 2-torsion -> Kc marked Brauer/Kummer glue             IN_PROGRESS
    T(Kc)=diag(4,8) and marked Br(Kc)[2]                                  DONE
    three candidate kernel fingerprints                                   DONE / COMPARISON ONLY
    named J2 elliptic quotient 2-torsion image                            DONE: (0,0)
    naive Shioda-Mitani factor transport                                  EXACTLY REJECTED
    one direct marked t1/t2 value or genuine K3-level transport           OPEN
```

## Current exit state

```text
J2_NAMED_ELLIPTIC_QUOTIENT_2TORSION_IMAGE=(0,0)
J2_INDEPENDENT_OBSERVATION_MATERIALIZED=true
NAIVE_SHIODA_MITANI_ELLIPTIC_FACTOR_TRANSPORT=REJECTED_EXACTLY
J2_NAMED_TRANSCENDENTAL_FUNCTIONAL_MATERIALIZED=false
J2_TWISTED_TRANSCENDENTAL_KERNEL_IDENTIFIED=false
J2_KC_DISCRIMINANT_COORDINATE_MATERIALIZED=false
FINITE_V4_KUMMER_DEFECT_COLUMNS_MATERIALIZED=0
ARITHMETIC_HS_D2_COMPUTED=false
STAGE33_07_HOSTILE_REAUDIT=NOT_RUN
STAGE33_12_CLOSED=false
```

Next exact leaf: `EVALUATE_ONE_NAMED_CV_J2_BFIELD_OR_CSA_VALUE_ON_MARKED_T1_OR_T2; IF_NO_INDEPENDENT_BIT_IS_OBTAINED, INCREMENT_LOOP_STAGNATION_AND_SWITCH_TO_K3_LEVEL_CORRESPONDENCE_OR_SPECIALIZATION`.

No 33-13 release, theorem/receiver/endpoint credit, or perfect-cuboid existence/nonexistence claim is granted by this checkpoint.
