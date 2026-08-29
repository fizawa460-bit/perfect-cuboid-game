# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_J2_ORIENTATION_INVARIANT_REDUCED_4_OF_5`

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

The Magma `ptsK` enumeration order is no longer load-bearing. The source-locked semantic 20-class basis has determinant `-32`, index one in `PicK`, and canonical certificate SHA256

```text
c17439c877de3d1cdebd716f4ba2571fb67ec9f07e30d944eafc39ae534380c0
```

In this basis `[CsK[22]]=e8=[CsK[21]]` and the infinity exceptional is `e18`.

## Semantic discriminant 2-torsion target

Exact GF(2) reduction of the semantic Gram gives rank `18`, nullity `2`, hence `A_PicK[2]=(F2)^2`. A deterministic half-lattice basis is

```text
u1 = [1,1,0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0]
u2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0]
```

and the three nonzero candidates are exactly `u1/2`, `u2/2`, `(u1+u2)/2`. Their discriminant quadratic values mod 2 are `1,0,1`. This still does not by itself select J2.

Certificate: `j2-semantic-kc-discriminant-2torsion-target.json`, canonical SHA256 `0b5d7dfdefbb0f2b7c37396ada35c0bee462dfeb625eb18262be0e862205d8df`.

## New exact reduction: HS-d2 parity is not the missing orientation bit

The audited Stage33-05 q1 obstruction uses the integral NS lift

```text
D = Cb + E_[0:1:0:-1:0:1]
```

and the ct-invariant test conic

```text
T : A1=0, A2+B3=0, A3-B2=0.
```

Pinned Stoll ordering identifies this test conic exactly as `CsK[2]`, which is semantic basis vector `e1`. The hostile-audited calculation gives `D.T=1` and `[D] != 0` in `H^2(<ct>,Pic)`.

However every numerator of a semantic discriminant 2-torsion class lies in `rad(G mod 2)`. Therefore every one of `u1`, `u2`, `u1+u2` pairs evenly with every integral PicK class, in particular with `T=e1`.

Consequently the odd HS obstruction parity `D.T=1` cannot be identified with a direct parity bit of the semantic discriminant half-lattice numerator. This rigorously rejects the tempting shortcut `q1 HS parity -> choose J2 discriminant candidate`; no candidate is guessed or promoted.

Certificate: `j2-orientation-invariant-reduction.json`, canonical SHA256 `2027fbe407fef0bad64f17d9735790b0c65ff8b158b9cd5c898277dc4851a01f`.

The remaining exact orientation must instead come from the named Jacobian/Kummer geometry itself. The next leaf is to derive one theta-translate / Kummer `(16_6)` incidence bit from the already fixed CV support and pinned Stoll marking and evaluate it on the three semantic half-lattice candidates.

## Visible progress

```text
1/5 named J2 half-divisor and CV support adapter                           DONE
2/5 pinned Stoll branch/support identification                            DONE
3/5 infinity exceptional geometric attachment                             DONE
4/5 explicit marked PicK coordinate for J2 carrier + infinity exceptional DONE
5/5 branch-Jacobian 2-torsion -> Kc discriminant Kummer glue              IN_PROGRESS
    Kc discriminant 2-torsion semantic target                              DONE
    HS-d2 parity shortcut                                                   EXACTLY_REJECTED
    named J2 theta/Kummer incidence orientation                            OPEN
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
J2_HS_PARITY_ORIENTATION_SHORTCUT=REJECTED_EXACTLY
J2_BRANCH_JACOBIAN_TO_DISCRIMINANT_KUMMER_GLUE_MATERIALIZED=false
J2_KC_DISCRIMINANT_COORDINATE_MATERIALIZED=false
FINITE_V4_KUMMER_DEFECT_COLUMNS_MATERIALIZED=0
ARITHMETIC_HS_D2_COMPUTED=false
STAGE33_07_HOSTILE_REAUDIT=NOT_RUN
STAGE33_12_CLOSED=false
```

Next exact leaf: `DERIVE_NAMED_J2_THETA_TRANSLATE_OR_KUMMER_INCIDENCE_BIT_FROM_CV_SUPPORT_AND_STOLL_16_6_GEOMETRY`.

No 33-13 release, theorem/receiver/endpoint credit, or perfect-cuboid existence/nonexistence claim is granted by this checkpoint.
