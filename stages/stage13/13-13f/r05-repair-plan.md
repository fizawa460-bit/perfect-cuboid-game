# Stage13-13f — R05 repair / closure plan

> STATUS: `ACTIVE_REPAIR_PLAN_GATES_A_B_C_D_E_F_G_COMPLETE_GATE_H_NEXT`
>
> SOURCE_BUNDLE: `STAGE13-FINAL-SELF-CONTAINED-20260809-R04`
>
> R04_IMMUTABLE: `true`

This plan repairs the Claude `OPEN` and DeepSeek `REPAIRABLE` objections without mutating R04 or presuming final acceptance.

## Gate A — finite discrepancy and q-independence

Status: `[x] COMPLETE — 13-13fa`.

```text
STAGE13_13FA=COMPLETE_Q_INDEPENDENCE_AND_FINITE_DISCREPANCY_AUDIT
FINITE_DATA_CONTRADICTS_THEOREM=false
LEADING_Q_DEPENDENT_ARITHMETIC_FACTOR_FOUND=false
COMMON_THETA_AUDIT=PASS_AT_CURRENT_PROOF_LEVEL
PROVED_EFFECTIVE_CONVERGENCE_RATE=false
FINITE_DISCREPANCY_QUANTITATIVELY_EXPLAINED_BY_PROVED_REMAINDER=false
```

## Gate B — explicit Wiener bound

Status: `[x] COMPLETE — 13-13fb`.

```text
STAGE13_13FB=COMPLETE_EXPLICIT_WIENER_BOUND
WIENER_E_BOUND=17744/243
WIENER_EXACT_CONSTANT=3465625/6561
WIENER_ROUNDED_CONSTANT=529
WIENER_EXPONENT=5/4
P5_EXPLICIT_FINITE_BOUND_LT=432
PHASE_UNIFORM=true
RETAINED_HARMONIC_UNIFORM=true
```

## Gate C — curved-region error ledger

Status: `[x] COMPLETE — 13-13fc`.

```text
STAGE13_13FC=COMPLETE_CURVED_REGION_ERROR_ACCUMULATION
BOX_COUNT=O((log B)^27)
FINITE_REMAINDER_N=64
FINITE_REMAINDER_AFTER_ALL_BOXES=O(B(log B)^-35)
POWER_TAIL_SAVING=exp(-(3/16)(log B)^(1/4))
CURVED_BOUNDARY=O(B(log B)^-5)+lower-order-ledger
MESH_ERROR=O(B(log B)^-5)
```

## Gate D — retained nonzero harmonics

Status: `[x] COMPLETE — 13-13fd`.

```text
STAGE13_13FD=COMPLETE_RETAINED_HARMONIC_CONDUCTOR_BOOKKEEPING
HECKE_STRIP_LEFT=3/4
HECKE_FAMILY_BOUND=S_ell(X)<<X^(1-delta_H)(1+ell)^C_H(log(2X))^D_H_for_all_ell>=1
HARMONIC_POLYLOG_EXPONENT=4*C_H+D_H+6
HARMONIC_STRETCHED_SAVING=exp(-delta_H*(log B)^(1/4))
HARMONIC_CORE=o_A(B(log B)^(-A))_for_every_fixed_A
VAALER_ZERO_MODE_EXCESS=O(B(log B)^-1)
FIXED_A48_REQUIRED=false
GAUSSIAN_HECKE_ZERO_FREE_REGION_REQUIRED=false
WINGS_EXPANDED_HARMONIC_BY_HARMONIC=false
```

## Gate E — complete Stage12 R09 interface

Status: `[x] COMPLETE — 13-13fe`.

The proof-facing interface includes the full `D_B -> G(hrs)-1 -> C_raw -> Mobius/common-scale C_prim` definition chain, the explicit `kappa`/`eta` theorem interface, and the exact objectwise factor-two projection.

```text
STAGE13_13FE=COMPLETE_STAGE12_COUNTING_INTERFACE
STAGE12_R09_BUNDLE=PC-N1-2-FINAL-SELF-CONTAINED-20260807-R09
STAGE12_R09_CONTENT_SHA256=0da06c78bbb546039dbe8d423dcc6ed403fe1af90d777488c2393c0c77c16848
STAGE12_COUNTING_TARGET=PRIMITIVE_ORIENTED_DISTINGUISHED_FACE_RECORDS
STAGE12_PRIMITIVE_DEFINITION=MOBIUS_COMMON_SCALE
STAGE12_CUTOFF=d<=B
STAGE12_THEOREM=C_prim(B)~kappa/(12*pi)B(log B)^3
KAPPA_EULER_PRODUCT_EXPLICIT=true
ETA_EQUALS_PI_KAPPA=true
STAGE13_PROJECTION_FIBER=2
PROJECTION_FIBER_REASON=TWO_ORDERS_OF_DISTINGUISHED_FACE_LEGS
PROJECTION_PARITY_STRATIFIED=true
EXTRA_2ADIC_PROJECTION_FACTOR=false
MULTI_FACE_FACTOR_TWO_EXACT=true
STAGE12_REOPENED=false
```

## Gate F — exact external theorem contracts

Status: `[x] COMPLETE — 13-13ff`.

Gate F exposes the exact fixed-conductor Hecke/Dirichlet contracts, derives polynomial strip/angular growth, inserts explicit Riesz/Perron smoothing before ordinary partial sums, and reduces the Vaaler import to the sawtooth theorem with interval polynomials derived internally.

```text
STAGE13_13FF=COMPLETE_EXACT_EXTERNAL_THEOREM_CONTRACTS
HECKE_NONZERO_ENTIRE=true
HECKE_NONZERO_FUNCTIONAL_EQUATION=true
HECKE_NONZERO_POLE_AT_1=false
FIXED_RESIDUE_CONDUCTOR=true
NONTRIVIAL_HECKE_TWIST_HOLOMORPHIC_AT_1=true
L_CHI4_HOLOMORPHIC_AT_1=true
POLYNOMIAL_STRIP_GROWTH_DERIVED=true
POLYNOMIAL_ANGULAR_GROWTH_DERIVED=true
RIESZ_PERRON_SMOOTHING_EXPLICIT=true
HECKE_FAMILY_SUMMATORY_INTERFACE_DERIVED=true
VAALER_IMPORTED_OBJECT=SAWTOOTH_APPROXIMATION
VAALER_INTERVAL_MAJORANT_DERIVED_INTERNALLY=true
VAALER_ZERO_MODE_EXCESS=1/(L+1)
VAALER_NONZERO_COEFFICIENT_BOUND_LT=1
GAUSSIAN_HECKE_ZERO_FREE_REGION_REQUIRED=false
GENERAL_SELBERG_DELANGE_REQUIRED=false
GROWING_MODULUS_THEOREM_USED=false
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
NEXT=13-13fg
```

The `NEXT=13-13fg` line above is retained as the historical Gate F completion lock used by its deterministic CI.

## Gate G — fixed inert-prime transfer

Status: `[x] COMPLETE — 13-13fg`.

Artifacts:

```text
stages/stage13/13-13fg/fixed-inert-transfer.md
stages/stage13/13-13fg/result.md
stages/stage13/scripts/13-13fg/fixed_inert_transfer_audit.py
stages/stage13/data/13-13fg/fixed_inert_transfer_audit.json
.github/workflows/stage13-13fg-fixed-inert-transfer.yml
```

The repaired transfer separates p-adic valuation strata from unit residue predicates. Unit predicates are expanded by finite character orthogonality and CRT.

The leading terms are grouped by **principal pole sector** rather than by a single literally all-trivial auxiliary character tuple. The principal pole sector contains every tuple whose induced characters on all pole-producing channels are principal; this safely includes any auxiliary-character aliasing from algebraic coordinate relations. Its complete finite Fourier sum is exactly the product of local acceptance factors.

Every tuple outside the principal pole sector makes at least one pole-producing channel nonprincipal. Gate F makes the corresponding fixed-conductor Dirichlet/Hecke factor holomorphic at `s=1`; Gate B keeps the mixed Euler correction holomorphic and unable to restore the pole.

```text
STAGE13_13FG=COMPLETE_FIXED_INERT_PRIME_TRANSFER
INERT_LOCAL_STATES=U_Rb_Sc_ONLY
INERT_H_VALUATION_ZERO=true
INERT_POSITIVE_VALUATION_FRACTION=2/(p+1)
INERT_UNIT_ACCEPTANCE=(p+1)/(2(p-1))
INERT_LAMBDA=(p+5)/(2(p+1))
INERT_LAMBDA_LE_3_OVER_4_FOR_P_GE_7=true
FIXED_RESIDUE_TRANSFER=FINITE_CHARACTER_ORTHOGONALITY_PLUS_CRT
PRINCIPAL_POLE_SECTOR_MULTIPLIER=product_{p_in_S}_lambda_p
AUXILIARY_CHARACTER_ALIASING_INCLUDED=true
MIXED_CORRECTION_REMAINS_HOLOMORPHIC=true
NONPRINCIPAL_POLE_SECTOR_LOSS_AT_LEAST_ONE=true
NONPRINCIPAL_TOTAL=o_S(B(log B)^3)
FIXED_S_CONSTANTS_MAY_DEPEND_ON_S=true
LIMIT_ORDER=FIX_S_THEN_B_TO_INFINITY_THEN_ENLARGE_S
GROWING_MODULUS_THEOREM_USED=false
PAIR_OVERLAP=o(B(log B)^3)
TRIPLE_OVERLAP=o(B(log B)^3)
PERFECT_CUBOID_NONEXISTENCE_ASSUMED=false
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
NEXT=13-13fh
```

Gate G closes the DeepSeek objection that the fixed-prime transfer did not expose character decomposition, principal leading mass, mixed-correction compatibility, nonprincipal pole loss, and limit order.

## Gate H — notation / audit scope / repaired-proof synthesis / R05 readiness

Status: `[>] NEXT — 13-13fh`.

Gate H must:

1. rename the Gaussian angular phase to `vartheta` where it conflicts with spherical `theta`;
2. define the substitutions entering `C_{ell,p}` at first use;
3. label deterministic `PASS` only as reproducibility/consistency evidence;
4. synthesize Gates A–G into one repaired canonical proof rather than leaving a repair-chain reading requirement;
5. verify all R04 objections have explicit closures and no theorem-level defect was found;
6. decide whether an immutable R05 bundle can be generated for fresh independent review.

## Promotion rule

If any repair finds a genuine theorem-level defect, reopen the theorem contract. Otherwise Gate H authorizes a new immutable R05 review bundle. R04 verdicts do not count automatically toward R05 freeze.

```text
R04_IMMUTABLE=true
STAGE13_13FA=COMPLETE_Q_INDEPENDENCE_AND_FINITE_DISCREPANCY_AUDIT
STAGE13_13FB=COMPLETE_EXPLICIT_WIENER_BOUND
STAGE13_13FC=COMPLETE_CURVED_REGION_ERROR_ACCUMULATION
STAGE13_13FD=COMPLETE_RETAINED_HARMONIC_CONDUCTOR_BOOKKEEPING
STAGE13_13FE=COMPLETE_STAGE12_COUNTING_INTERFACE
STAGE13_13FF=COMPLETE_EXACT_EXTERNAL_THEOREM_CONTRACTS
STAGE13_13FG=COMPLETE_FIXED_INERT_PRIME_TRANSFER
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R05_REQUIRED_IF_THEOREM_SURVIVES_AUDIT=true
R05_FRESH_REVIEW_REQUIRED=true
PROMOTE_TO_13_13G=false
NEXT=13-13fh
```
