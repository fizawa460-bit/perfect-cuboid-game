# Stage13-13f — R05 repair / closure plan

> STATUS: `ACTIVE_REPAIR_PLAN_GATES_A_B_C_D_E_F_COMPLETE_GATE_G_NEXT`
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

The remaining wing/shift bounds are `O(B log^(9/4)B)`, `O(B log^(5/2)B)`, and `O(B log^2 B)`.

## Gate D — retained nonzero harmonics

Status: `[x] COMPLETE — 13-13fd`.

On `Re s>=3/4`, the proof-facing family interface is

```text
S_ell(X) << X^(1-delta_H)(1+ell)^C_H(log(2X))^D_H
```

uniformly for every `X>=2`, `ell>=1`.

```text
STAGE13_13FD=COMPLETE_RETAINED_HARMONIC_CONDUCTOR_BOOKKEEPING
HECKE_STRIP_LEFT=3/4
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

Artifacts: `stages/stage13/13-13fe/` plus deterministic script/data/CI.

The repaired proof-facing interface contains

```text
D_B -> G(hrs)-1 -> C_raw(B) -> Mobius/common-scale C_prim(B)
C_prim(B) ~ kappa/(12*pi) B(log B)^3
          = eta/(12*pi^2) B(log B)^3
eta=pi*kappa
C_prim,q^proj(B)=2 A_q(B)
C_prim(B)=2 sum_q A_q(B)
```

The projection fiber is exactly the two orders of the distinguished face legs and remains exact in OE/EE strata and on multi-face raw incidences.

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

Artifacts:

```text
stages/stage13/13-13ff/external-theorem-contracts.md
stages/stage13/13-13ff/result.md
stages/stage13/scripts/13-13ff/external_contract_audit.py
stages/stage13/data/13-13ff/external_contract_audit.json
.github/workflows/stage13-13ff-external-contracts.yml
```

The R05-facing external boundary is now explicit:

- nonzero Gaussian angular Hecke `L`-functions: entire continuation, completed functional equation, no pole at `s=1`;
- fixed finite residue twists: fixed-conductor Hecke characters, with only the trivial character allowed a pole at `s=1`;
- `L(s,chi_4)`: nonprincipal Dirichlet `L`-function, holomorphic at `s=1` with the classical functional equation;
- polynomial strip/angular growth derived from right-boundary absolute convergence, the functional equation, Stirling and Phragmen--Lindelof;
- Gate D ordinary summatory estimate derived through an explicit high-order Riesz/Perron smoothing and finite differencing, rather than an unexplained unsmoothed contour shortcut;
- Vaaler black-box reduced to the sawtooth approximation; interval majorants/minorants are derived internally with exact zero-mode excess `1/(L+1)` and nonzero coefficient bound `<1`.

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
```

Gate F closes the DeepSeek objection that the Hecke and Vaaler hypotheses/conclusions were not visible at the precision actually consumed by the proof.

## Gate G — fixed inert-prime transfer

Status: `[>] NEXT — 13-13fg`.

Expand the fixed-`S` overlap proposition into a proof-facing lemma:

1. finite residue-state decomposition and character orthogonality;
2. principal tuple multiplies the raw top coefficient by `prod_{p in S} lambda_p`;
3. each nonprincipal tuple removes at least one principal pole and contributes `o(B(log B)^3)` for fixed `S`;
4. the Gate F fixed-conductor contracts control all twisted factors and Gate B controls the mixed Euler correction;
5. the order `fix S -> B to infinity -> |S| to infinity` is explicit.

## Gate H — notation and audit scope / R05 synthesis readiness

Status: `[ ] Pending Gate G`.

Propagate `vartheta`, define `C_{ell,p}` substitutions at first use, keep deterministic `PASS` limited to reproducibility/consistency, synthesize Gates A-G into the repaired canonical proof, and decide whether immutable R05 can be generated.

## Promotion rule

If any repair finds a genuine theorem-level defect, reopen the theorem contract. Otherwise, after A-H create a new immutable R05 bundle and obtain fresh independent reviews. R04 verdicts do not automatically count toward R05 freeze.

```text
R04_IMMUTABLE=true
STAGE13_13FA=COMPLETE_Q_INDEPENDENCE_AND_FINITE_DISCREPANCY_AUDIT
STAGE13_13FB=COMPLETE_EXPLICIT_WIENER_BOUND
STAGE13_13FC=COMPLETE_CURVED_REGION_ERROR_ACCUMULATION
STAGE13_13FD=COMPLETE_RETAINED_HARMONIC_CONDUCTOR_BOOKKEEPING
STAGE13_13FE=COMPLETE_STAGE12_COUNTING_INTERFACE
STAGE13_13FF=COMPLETE_EXACT_EXTERNAL_THEOREM_CONTRACTS
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R05_REQUIRED_IF_THEOREM_SURVIVES_AUDIT=true
R05_FRESH_REVIEW_REQUIRED=true
PROMOTE_TO_13_13G=false
NEXT=13-13fg
```
