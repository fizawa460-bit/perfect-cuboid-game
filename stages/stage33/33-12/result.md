# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_J2_SEMANTIC_KC_PICARD_COORDINATE_MATERIALIZED_4_OF_5`

Stage33-12 remains open. Stage33-07 remains open. Stage33-13 is not released.

## Authoritative receiver state

- `P=Br(Sbar)[2]^{G_Q}`: exact F2 dimension `10`.
- `H^1(V4,Pic(Sbar)/2)`: exact F2 dimension `75`.
- Future finite-V4 Kummer matrix: `75 x 10`, materialized columns `0/10`.
- Finite obstruction cosets: `0/26`.
- Stage33-11 localization connecting map: audited exact zero on `26/26` directions.

## Named J2 geometry retained

`E_J2 = 2*infinity_minus - P_plus - P_minus`, with `div(ell_J2)=2E_J2`.

Pinned Stoll Kc coordinates are `(A1,A2,A3,B1,B2,B3)=(e,x,y,z,q,p)`. The named branch is exactly `CsK[22]`, and

```text
P_plus_K  = [-1:1:i:0:0:sqrt(2)]
P_minus_K = [-1:1:i:0:0:-sqrt(2)]
P_inf_K   = [1:0:0:0:-1:-1]
```

`P_inf_K` is an A1 singularity. The J2 strict transform meets its exceptional conic at `[a:b:c]=[1:i:0]`.

Important firewall: the support points of `E_J2` live on the branch normalization; they are not K3 divisors and are never inserted directly into `PicK`.

## New exact progress: order-independent semantic PicK basis

The Magma `ptsK` enumeration order is no longer load-bearing.

Using the pinned Stoll source lock

```text
MichaelStollBayreuth/Verification
commit 51233ed5ef2bf228fac9416c66db9adc0ebcaadd
Cuboids/cuboids.magma
```

and its exact assertion

```text
sub<PicK | [qPicK(BigK.j) : j in indlistK]> eq PicK
```

we keep the same 17 curve slots from `indlistK` and replace its three order-dependent exceptional slots by the semantic exceptionals

```text
A1_B2-1_B3-1 = [1:0:0:0:-1:-1]   (= P_inf_K)
A2_B1-1_B3-1 = [0:1:0:-1:0:-1]
A3_B1-1_B2-1 = [0:0:1:-1:-1:0].
```

The exact `17 x 17` curve Gram and `17 x 12` curve/exceptional incidence table are committed in `j2-semantic-kc-picard-basis.json`. Exhausting all `C(12,3)=220` exceptional triples gives determinant distribution

```text
0      : 120
-32    : 64
-128   : 32
-512   : 4
```

so every nondegenerate triple has absolute determinant at least `32`. The chosen semantic triple has determinant `-32`. Since the pinned Stoll `indlistK` triple generates `PicK`, while the semantic 20-class lattice is a sublattice of `PicK`, the index/discriminant formula forces

```text
|disc PicK| = 32
[PicK : L_semantic] = 1.
```

Thus the semantic 20 classes are an exact integral basis of `PicK`, with no Smith recomputation and no `ptsK` ordering dependency.

In this basis:

```text
[CsK[22]] = e8 = [CsK[21]] in PicK
[E_{P_inf}] = e18
```

where `E_{P_inf}` is the exceptional divisor over `P_inf_K`. This is the required explicit Kc marked coordinate for the J2 branch carrier and infinity exceptional.

Certificate: `j2-semantic-kc-picard-basis.json`, canonical SHA256 `c17439c877de3d1cdebd716f4ba2571fb67ec9f07e30d944eafc39ae534380c0`.
Verifier: `certify_j2_semantic_kc_picard_basis.py` (network-free exact Bareiss replay over all 220 triples).

The former remote Magma materializer is now optional cross-check only; it is not needed for Stage33-12 progress.

## Visible progress

```text
1/5 named J2 half-divisor and CV support adapter                         DONE
2/5 pinned Stoll branch/support identification                          DONE
3/5 infinity exceptional geometric attachment                           DONE
4/5 explicit marked PicK coordinate for J2 carrier + infinity exceptional DONE
5/5 branch-Jacobian 2-torsion -> Kc discriminant Kummer glue            OPEN
```

## Current exit state

```text
J2_NAMED_HALF_DIVISOR_MATERIALIZED=true
J2_CV_TO_RULED_SUPPORT_ADAPTER_MATERIALIZED=true
J2_BRANCH_IDENTIFIED_WITH_STOLL_CSK22=true
J2_INFINITY_EXCEPTIONAL_GEOMETRIC_ATTACHMENT_MATERIALIZED=true
J2_PTSK_ORDER_DEPENDENCY=ELIMINATED
J2_SEMANTIC_PICARD_BASIS_MATERIALIZED=true
J2_CSK22_PICARD_COORDINATE=e8
J2_INFINITY_EXCEPTIONAL_PICARD_COORDINATE=e18
J2_BRANCH_JACOBIAN_TO_DISCRIMINANT_KUMMER_GLUE_MATERIALIZED=false
J2_KC_DISCRIMINANT_COORDINATE_MATERIALIZED=false
FINITE_V4_KUMMER_DEFECT_COLUMNS_MATERIALIZED=0
ARITHMETIC_HS_D2_COMPUTED=false
STAGE33_07_HOSTILE_REAUDIT=NOT_RUN
STAGE33_12_CLOSED=false
```

Next exact leaf: `BRANCH_JACOBIAN_2TORSION_TO_KC_PICARD_DISCRIMINANT_KUMMER_GLUE`.

No 33-13 release, theorem/receiver/endpoint credit, or perfect-cuboid existence/nonexistence claim is granted by this checkpoint.
