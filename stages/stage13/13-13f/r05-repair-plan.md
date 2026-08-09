# Stage13-13f — R05 repair / closure plan

> STATUS: `R05_REPAIR_GATES_A_THROUGH_H_AND_IMMUTABLE_BUNDLE_COMPLETE_FRESH_REVIEW_NEXT`
>
> SOURCE_BUNDLE: `STAGE13-FINAL-SELF-CONTAINED-20260809-R04`
>
> R04_IMMUTABLE: `true`

This plan was opened because Claude returned `OPEN` and DeepSeek returned `REPAIRABLE` on R04. It does not mutate R04 and it does not treat an internal repair as an external-review verdict.

## Gate A — finite discrepancy and q-independence

Status: `[x] COMPLETE — 13-13fa`.

```text
STAGE13_13FA=COMPLETE_Q_INDEPENDENCE_AND_FINITE_DISCREPANCY_AUDIT
FINITE_DATA_CONTRADICTS_THEOREM=false
LEADING_Q_DEPENDENT_ARITHMETIC_FACTOR_FOUND=false
COMMON_THETA_AUDIT=PASS_AT_CURRENT_PROOF_LEVEL
PROVED_EFFECTIVE_CONVERGENCE_RATE=false
FINITE_DISCREPANCY_QUANTITATIVELY_EXPLAINED_BY_PROVED_REMAINDER=false
NEXT=13-13fb
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
NEXT=13-13fc
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
NEXT=13-13fd
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
NEXT=13-13fe
```

## Gate E — complete Stage12 R09 interface

Status: `[x] COMPLETE — 13-13fe`.

The full Stage12 counting object, primitive definition, explicit `kappa`, `eta=pi*kappa`, exact cutoff, orientation convention and two-element Stage13 projection fiber are copied into the proof-facing interface.

```text
STAGE13_13FE=COMPLETE_STAGE12_COUNTING_INTERFACE
STAGE12_COUNTING_TARGET=PRIMITIVE_ORIENTED_DISTINGUISHED_FACE_RECORDS
STAGE12_PRIMITIVE_DEFINITION=MOBIUS_COMMON_SCALE
STAGE12_CUTOFF=d<=B
STAGE12_THEOREM=C_prim(B)~kappa/(12*pi)B(log B)^3
KAPPA_EULER_PRODUCT_EXPLICIT=true
ETA_EQUALS_PI_KAPPA=true
STAGE13_PROJECTION_FIBER=2
PROJECTION_FIBER_REASON=TWO_ORDERS_OF_DISTINGUISHED_FACE_LEGS
STAGE12_REOPENED=false
NEXT=13-13ff
```

## Gate F — exact external theorem contracts

Status: `[x] COMPLETE — 13-13ff`.

The exact fixed-conductor Hecke/Dirichlet contracts, polynomial strip/angular growth deduction, explicit Riesz/Perron smoothing, and Vaaler sawtooth-to-interval coefficient bounds are exposed.

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
VAALER_ZERO_MODE_EXCESS=1/(L+1)
VAALER_NONZERO_COEFFICIENT_BOUND_LT=1
GAUSSIAN_HECKE_ZERO_FREE_REGION_REQUIRED=false
GENERAL_SELBERG_DELANGE_REQUIRED=false
GROWING_MODULUS_THEOREM_USED=false
NEXT=13-13fg
```

## Gate G — fixed inert-prime transfer

Status: `[x] COMPLETE — 13-13fg`.

The proof separates p-adic strata from unit residue predicates, expands the latter by finite character orthogonality and CRT, groups all aliasing-compatible leading tuples into the principal pole sector, and proves pole loss for every sector outside it.

```text
STAGE13_13FG=COMPLETE_FIXED_INERT_PRIME_TRANSFER
INERT_LOCAL_STATES=U_Rb_Sc_ONLY
INERT_LAMBDA=(p+5)/(2(p+1))
FIXED_RESIDUE_TRANSFER=FINITE_CHARACTER_ORTHOGONALITY_PLUS_CRT
PRINCIPAL_POLE_SECTOR_MULTIPLIER=product_{p_in_S}_lambda_p
AUXILIARY_CHARACTER_ALIASING_INCLUDED=true
MIXED_CORRECTION_REMAINS_HOLOMORPHIC=true
NONPRINCIPAL_POLE_SECTOR_LOSS_AT_LEAST_ONE=true
NONPRINCIPAL_TOTAL=o_S(B(log B)^3)
LIMIT_ORDER=FIX_S_THEN_B_TO_INFINITY_THEN_ENLARGE_S
GROWING_MODULUS_THEOREM_USED=false
PAIR_OVERLAP=o(B(log B)^3)
TRIPLE_OVERLAP=o(B(log B)^3)
NEXT=13-13fh
```

## Gate H — notation / audit scope / canonical synthesis / R05 readiness

Status: `[x] COMPLETE — 13-13fh`.

New canonical proof candidate:

```text
stages/stage13/13-13fh/stage13-r05-canonical-proof.md
```

Gate H performs the last presentation and synthesis repairs:

1. `theta` is reserved for the geometric spherical angle and Gaussian phase is `vartheta`;
2. `C_{ell,p}(s_h,s_r,s_s)=C_vartheta(p^-s_h,p^-s_r,p^-s_s)` is defined at first use;
3. deterministic `PASS` is explicitly limited to reproducibility/consistency evidence;
4. Gates A--G are synthesized into one theorem-order proof instead of a repair-chain reading path;
5. the finite `100k -> 5m` discrepancy is disclosed together with the exact nonclaim of an effective convergence rate;
6. the future R05 proof uses the repaired Gate-G principal pole sector rather than the compressed R04 transfer.

```text
STAGE13_13FH=COMPLETE_R05_SYNTHESIS_READINESS
R05_CANONICAL_PROOF=stages/stage13/13-13fh/stage13-r05-canonical-proof.md
R05_CANONICAL_PROOF_SINGLE_ENTRYPOINT=true
NOTATION_THETA_GEOMETRIC_ONLY=true
NOTATION_VARTTHETA_GAUSSIAN_PHASE=true
C_ELL_P_SUBSTITUTION_DEFINED_AT_FIRST_USE=true
DETERMINISTIC_AUDIT_SCOPE=REPRODUCIBILITY_AND_CONSISTENCY_ONLY
REPAIR_GATES_A_THROUGH_H_COMPLETE=true
R04_OBJECTIONS_REPAIRED_IN_R05_CANDIDATE=true
R04_VERDICTS_CARRY_FORWARD_TO_R05=false
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R05_SYNTHESIS_READY=true
R05_BUNDLE_CREATED=false
R05_FRESH_EXTERNAL_REVIEW_REQUIRED=true
NEXT=13-13fi
```

## R04 objection crosswalk

```text
Claude finite ratio / possible hidden q-factor   -> A + H
529 derivation                                  -> B
box-count / curved uniformity                   -> C
nonzero harmonic conductor bookkeeping          -> D + F
Stage12 object / orientation / factor two        -> E
Hecke / Dirichlet / Vaaler interfaces            -> F
fixed-prime principal/nonprincipal transfer      -> G
notation collision / audit PASS presentation     -> H
```

The statement `R04_OBJECTIONS_REPAIRED_IN_R05_CANDIDATE=true` means the repair candidate contains explicit responses to every recorded R04 objection. It is **not** an external `CLOSED` verdict.

## 13-13fi — immutable R05 review bundle

Status: `[x] COMPLETE`.

```text
STAGE13_13FI=COMPLETE_R05_REVIEW_BUNDLE
BUNDLE_ID=STAGE13-FINAL-SELF-CONTAINED-20260809-R05
SOURCE_SNAPSHOT_COMMIT=79f03341b67dd49a8c128cfbeba3f756c91de6f6
CONTENT_SHA256=4214a6e3621b52ce39373799b48fc8325351f650514e732d6e2244d28d475458
BUNDLE_PATH=review/STAGE13-FINAL-SELF-CONTAINED-20260809-R05.html
R05_IMMUTABLE=true
R04_IMMUTABLE=true
R03_IMMUTABLE=true
THEOREM_CHANGED=false
R05_FRESH_EXTERNAL_REVIEW_REQUIRED=true
R04_VERDICTS_CARRY_FORWARD_TO_R05=false
DETERMINISTIC_AUDIT_SCOPE=REPRODUCIBILITY_AND_CONSISTENCY_ONLY
NEXT=13-13fj
```

R05 is built deterministically from the fixed merged Gate-H snapshot and is now the only review target for the next external-review round. Any substantive defect creates R06 or later; R05 is never edited.

## Next: 13-13fj — fresh R05 external review

Start a new reviewer ledger for `STAGE13-FINAL-SELF-CONTAINED-20260809-R05` with zero inherited votes.

```text
R05_INDEPENDENT_CLOSED_VERDICTS=0
R05_UNRESOLVED_THEOREM_LEVEL_OBJECTIONS=0
R05_FRESH_EXTERNAL_REVIEW_REQUIRED=true
R04_VERDICTS_CARRY_FORWARD_TO_R05=false
```

Fresh reviewer text must be stored against the R05 bundle ID/hash. Final Stage13 freeze is forbidden until the final immutable bundle has

```text
INDEPENDENT_CLOSED_VERDICTS>=2
UNRESOLVED_THEOREM_LEVEL_OBJECTIONS=0
```

If a substantive R05 defect appears, preserve R05 and create R06 or later.

## Promotion rule

Current parent lock:

```text
R03_IMMUTABLE=true
R04_IMMUTABLE=true
R05_IMMUTABLE=true
REPAIR_GATES_A_THROUGH_H_COMPLETE=true
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R05_SYNTHESIS_READY=true
R05_BUNDLE_CREATED=true
R05_FRESH_REVIEW_REQUIRED=true
R05_INDEPENDENT_CLOSED_VERDICTS=0
R05_UNRESOLVED_THEOREM_LEVEL_OBJECTIONS=0
PROMOTE_TO_13_13G=false
NEXT=13-13fj
```
