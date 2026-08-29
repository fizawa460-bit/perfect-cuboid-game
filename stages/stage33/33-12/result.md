# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_J2_DIRECT_CSA_MARKED_CYCLE_EVALUATION_OPEN_4_OF_5`

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

## Transcendental lattice fixed up to isometry

The exact semantic discriminant form fixes

```text
T(Kc) ~= <4> direct_sum <8>.
```

The retained certificate also gives an explicit discriminant anti-isometry witness from `t1/4,t2/8` to the semantic NS discriminant, generating all 32 discriminant classes.

Certificate: `j2-kc-transcendental-lattice-isometry.json`.
Canonical SHA256: `b7f2bcfa29c01731ea2f10d22db898ad57317f140b547f91e3d3a27a0faf1010`.

## Exact marked Brauer half-dual target

The correct target for direct evaluation of the named CV class is now materialized. For the fixed marked lattice

```text
T(Kc) = <t1,t2>,   Gram(T)=diag(4,8),
```

the geometric 2-torsion Brauer group is

```text
Br(Kc)[2] = Hom(T,Z/2) = (1/2 T*)/T*.
```

A deterministic marked basis is therefore

```text
beta1 = t1/8   -> [1,0] on [t1,t2]
beta2 = t2/16  -> [0,1] on [t1,t2].
```

Hence the named nonzero J2 class, once directly evaluated, is exactly one of

```text
[1,0], [0,1], [1,1].
```

This is deliberately distinguished from the discriminant 2-torsion quotient

```text
A_T[2] = (T*/T)[2].
```

The two groups have the same cardinality here but are not the same quotient. In particular the discriminant quadratic values `1,0,1` on the three nonzero `A_T[2]` representatives do not canonically select a class of `Br(Kc)[2]`. The former unique-isotropic shortcut is therefore rejected for an exact structural reason, not merely left unproved.

Certificate: `j2-kc-bfield-halfdual-target.json`.
Canonical SHA256: `28180fae13a24e4d06018703aff574db801486fa6130e83c6b6db215c32b1fdb`.
Network-free verifier: `certify_j2_kc_bfield_halfdual_target.py`.

## Automorphism signatures cannot mark J2

Stoll's `substsK[6]` is `B1 -> -B1`, while the named J2 branch has `B1=0` and all three named support points also have `B1=0`; hence this involution fixes the named J2 carrier/support pointwise.

However this cannot select the J2 functional. For `T(Kc)=diag(4,8)`, the complete integral isometry group is exactly `diag(+/-1,+/-1)`, four elements, and every one reduces to the identity modulo `2`. Therefore every geometric automorphism acts trivially on `Hom(T(Kc),Z/2)=Br(Kc)[2]`.

Certificate: `j2-kc-automorphism-mod2-marking-rejection.json`.
Canonical SHA256: `dfbd85c56c3c9c29238e1da633baec2ed2bd8cc58021c8137e95fb1cf9cd74fb`.

## Full Galois fixedness also cannot mark J2

The previous Galois rejection used only `ct: sqrt(2)->-sqrt(2)`. The remaining generator `cc: i->-i` can be evaluated directly in the semantic PicK frame.

In Stoll's final `C3sK` genus-one block,

```text
[i*B2+e2*B3, i*sqrt(2)*A1+e3*B1],  e3,e2 in [1,-1],
```

complex conjugation permutes the four slots by

```text
CsK[51] <-> CsK[54]
CsK[52] <-> CsK[53].
```

Direct exact evaluation of Stoll's `intersectionK` formula against the 17 semantic curve slots gives

```text
CsK51 : [1,1,1,1,1,1,1,2,2,1,1,1,2,2,0,4,0]
CsK53 : [1,1,1,1,1,1,1,2,2,1,1,1,0,0,2,0,4].
```

Neither curve meets any of the 12 A1 nodes. These are exactly the semantic Gram rows of `CsK[54]` and `CsK[52]`, respectively. Since the semantic 20 classes form an index-one PicK basis with nondegenerate Gram determinant `-32`, this proves

```text
[CsK51]=[CsK54] in PicK
[CsK53]=[CsK52] in PicK.
```

Thus `cc` fixes `u2=[CsK52]+[CsK54]` as a Picard-discriminant class; it also fixes `u1`. Together with the prior exact `ct` result, the full Galois group generated by `cc,ct` fixes all of `A_PicK[2]`. Hence Q-definedness of J2 does not select one of the three nonzero candidates.

Certificate: `j2-full-galois-discriminant-fixedness-rejection.json`.
Canonical SHA256: `c351988141e0d75da27727931b1c6167eeb9e07bb58c240bd5e57a5ad6e26d54`.
Network-free verifier: `certify_j2_full_galois_discriminant_fixedness_rejection.py`.

## Rejected shortcuts retained

- HS-d2 parity as a direct orientation bit: `REJECTED_EXACTLY`.
- Unsupported classical Kummer `(16_6)` transfer: `REJECTED_EXACTLY`.
- Historical Smith frame alone: `INSUFFICIENT_EXACTLY`.
- Bare Picard-discriminant `ct` connecting signature: `REJECTED_EXACTLY`.
- Full Picard-discriminant Galois fixed-line signature: `REJECTED_EXACTLY`.
- Kc automorphism/sign/swap fixed-line signature: `REJECTED_EXACTLY`.
- Unique-isotropic discriminant-vector guess as a Brauer selector: `REJECTED_EXACTLY_WRONG_QUOTIENT`.

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
    marked Br(Kc)[2] half-dual target beta1=t1/8,beta2=t2/16              DONE
    automorphism-signature marking shortcut                                EXACTLY_REJECTED
    full Galois fixed-line marking shortcut                                EXACTLY_REJECTED
    direct named CV J2 CSA evaluation on marked t1/t2 cycle                OPEN
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
KC_BRAUER_2TORSION_HALFDUAL_TARGET_MATERIALIZED=true
KC_BRAUER_2TORSION_MARKED_BASIS=[beta1=t1/8,beta2=t2/16]
KC_BRAUER_2TORSION_NONZERO_FUNCTIONALS=[[1,0],[0,1],[1,1]]
DISCRIMINANT_Q_AS_NAMED_J2_BRAUER_SELECTOR=REJECTED_EXACTLY_WRONG_QUOTIENT
KC_AUTOMORPHISM_MOD2_MARKING_SHORTCUT=REJECTED_EXACTLY
KC_FULL_GALOIS_DISCRIMINANT_FIXED_SUBSPACE_DIMENSION_F2=2
J2_FULL_GALOIS_FIXED_LINE_SHORTCUT=REJECTED_EXACTLY
J2_NAMED_TRANSCENDENTAL_FUNCTIONAL_MATERIALIZED=false
J2_BRANCH_JACOBIAN_TO_DISCRIMINANT_KUMMER_GLUE_MATERIALIZED=false
J2_KC_DISCRIMINANT_COORDINATE_MATERIALIZED=false
FINITE_V4_KUMMER_DEFECT_COLUMNS_MATERIALIZED=0
ARITHMETIC_HS_D2_COMPUTED=false
STAGE33_07_HOSTILE_REAUDIT=NOT_RUN
STAGE33_12_CLOSED=false
```

Next exact leaf: `EVALUATE_NAMED_CV_J2_CSA_ON_MARKED_T1_OR_T2_CYCLE_USING_THE_EXPLICIT_HALFDUAL_BFIELD_TARGET`.

No 33-13 release, theorem/receiver/endpoint credit, or perfect-cuboid existence/nonexistence claim is granted by this checkpoint.
