# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_J2_SEMANTIC_KC_DISCRIMINANT_2TORSION_TARGET_MATERIALIZED_4_OF_5`

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

## Exact order-independent semantic PicK basis

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

Certificate: `j2-semantic-kc-picard-basis.json`, canonical SHA256 `c17439c877de3d1cdebd716f4ba2571fb67ec9f07e30d944eafc39ae534380c0`.
Verifier: `certify_j2_semantic_kc_picard_basis.py`.

## New exact progress inside 5/5: semantic discriminant 2-torsion target

The same semantic `20 x 20` Gram now determines the Kc discriminant 2-torsion target directly, without reconstructing the historical Smith basis.

Exact GF(2) reduction gives

```text
rank(G mod 2)    = 18
nullity(G mod 2) = 2
A_PicK[2]        = (F2)^2.
```

A deterministic semantic half-lattice basis is

```text
u1 = [1,1,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0]
u2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0]
```

where `u/2` denotes the corresponding element of `PicK^*/PicK`; exact replay verifies `G*u` is even. The three nonzero discriminant-2-torsion candidates are therefore exactly `u1/2`, `u2/2`, `(u1+u2)/2`. Their discriminant quadratic values mod `2` are respectively `1,0,1`, and the `u1,u2` cross-pairing is integral.

Certificate: `j2-semantic-kc-discriminant-2torsion-target.json`, canonical SHA256 `0b5d7dfdefbb0f2b7c37396ada35c0bee462dfeb625eb18262be0e862205d8df`.
Verifier: `certify_j2_semantic_kc_discriminant_2torsion_target.py`.

This is a genuine narrowing of the final glue problem: the Kc-side target is now an explicit semantic three-element set with canonical 20-bit representatives. It does **not** select the named J2 element. The remaining exact task is to evaluate one named CV/Kummer orientation invariant against this semantic half-lattice basis; guessing the unique isotropic candidate is forbidden.

The former remote Magma materializer remains optional cross-check only and is not load-bearing.

## Visible progress

```text
1/5 named J2 half-divisor and CV support adapter                           DONE
2/5 pinned Stoll branch/support identification                            DONE
3/5 infinity exceptional geometric attachment                             DONE
4/5 explicit marked PicK coordinate for J2 carrier + infinity exceptional DONE
5/5 branch-Jacobian 2-torsion -> Kc discriminant Kummer glue              IN_PROGRESS
    Kc discriminant 2-torsion semantic target                              DONE
    named J2 orientation among 3 nonzero target classes                    OPEN
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
J2_SEMANTIC_KC_DISCRIMINANT_2TORSION_TARGET_MATERIALIZED=true
J2_SEMANTIC_KC_DISCRIMINANT_2TORSION_CANDIDATES=3
J2_BRANCH_JACOBIAN_TO_DISCRIMINANT_KUMMER_GLUE_MATERIALIZED=false
J2_KC_DISCRIMINANT_COORDINATE_MATERIALIZED=false
FINITE_V4_KUMMER_DEFECT_COLUMNS_MATERIALIZED=0
ARITHMETIC_HS_D2_COMPUTED=false
STAGE33_07_HOSTILE_REAUDIT=NOT_RUN
STAGE33_12_CLOSED=false
```

Next exact leaf: `EVALUATE_ONE_NAMED_J2_KUMMER_ORIENTATION_INVARIANT_AGAINST_SEMANTIC_HALF_LATTICE_BASIS`.

No 33-13 release, theorem/receiver/endpoint credit, or perfect-cuboid existence/nonexistence claim is granted by this checkpoint.
