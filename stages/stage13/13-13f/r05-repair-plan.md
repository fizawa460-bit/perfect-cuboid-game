# Stage13-13f — R05 repair / closure plan

> STATUS: `ACTIVE_REPAIR_PLAN_GATES_A_B_C_D_E_COMPLETE_GATE_F_NEXT`
>
> SOURCE_BUNDLE: `STAGE13-FINAL-SELF-CONTAINED-20260809-R04`
>
> R04_IMMUTABLE: `true`

This plan repairs the Claude `OPEN` and DeepSeek `REPAIRABLE` objections without mutating R04 or presuming the theorem survives.

## Gate A — finite discrepancy and q-independence

Status: `[x] COMPLETE — 13-13fa`.

Finite exact-one data through `B=5m` do not contradict the claimed asymptotic vector; no surviving leading q-dependent arithmetic factor was found. No effective convergence rate is claimed.

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
||E|| <= (17744/243) rho^2
(17744/243)*(5/3)*(25/12)^2 = 3465625/6561 < 529
||C_{ell,p}-1||_(5/8) <= 529 p^(-5/4), p>=13
||C_{ell,5}-1||_(5/8) < 432
```

```text
STAGE13_13FB=COMPLETE_EXPLICIT_WIENER_BOUND
WIENER_EXPONENT=5/4
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

uniformly for every `X>=2`, `ell>=1`. The retained restriction `ell<=floor((log B)^4)` is imposed only at mode summation.

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

Artifacts:

```text
stages/stage13/13-13fe/stage12-counting-interface.md
stages/stage13/13-13fe/result.md
stages/stage13/scripts/13-13fe/stage12_interface_audit.py
stages/stage13/data/13-13fe/stage12_interface_audit.json
.github/workflows/stage13-13fe-stage12-interface.yml
```

The repaired proof-facing interface now includes the exact frozen Stage12 definitions:

```text
D_B -> G(hrs)-1 -> C_raw(B) -> Mobius/common-scale C_prim(B)
```

with Stage12 orientation `r<s`, retained distinguished-face construction, and no full edge-permutation quotient.

The frozen theorem is copied with the complete constant interface:

```text
C_prim(B) ~ kappa/(12*pi) B(log B)^3
          = eta/(12*pi^2) B(log B)^3
eta=pi*kappa
KAPPA_EULER_PRODUCT_EXPLICIT=true
```

The exact Stage12-to-Stage13 object map is also explicit. Forget the order of the two distinguished face legs, canonically sort the three edges, and retain which canonical face contains that distinguished pair. For each raw canonical incidence the fiber consists exactly of the two leg orders `(x,y)` and `(y,x)`:

```text
C_prim,q^proj(B)=2 A_q(B)
C_prim(B)=2 sum_q A_q(B)
```

The outer Pythagorean parameter already has `r<s`, repeated-side contribution is zero, and the factor two holds separately in the OE/EE strata. Multi-face objects do not alter it because raw incidence retains the distinguished face.

```text
STAGE13_13FE=COMPLETE_STAGE12_COUNTING_INTERFACE
STAGE12_R09_BUNDLE=PC-N1-2-FINAL-SELF-CONTAINED-20260807-R09
STAGE12_R09_CONTENT_SHA256=0da06c78bbb546039dbe8d423dcc6ed403fe1af90d777488c2393c0c77c16848
STAGE12_COUNTING_TARGET=PRIMITIVE_ORIENTED_DISTINGUISHED_FACE_RECORDS
STAGE12_PRIMITIVE_DEFINITION=MOBIUS_COMMON_SCALE
STAGE12_CUTOFF=d<=B
STAGE12_THEOREM=C_prim(B)~kappa/(12*pi)B(log B)^3
ETA_EQUALS_PI_KAPPA=true
STAGE13_PROJECTION_FIBER=2
PROJECTION_FIBER_REASON=TWO_ORDERS_OF_DISTINGUISHED_FACE_LEGS
PROJECTION_PARITY_STRATIFIED=true
EXTRA_2ADIC_PROJECTION_FACTOR=false
MULTI_FACE_FACTOR_TWO_EXACT=true
STAGE12_REOPENED=false
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
```

Gate E closes the R04/DeepSeek objection that `C_prim`, its orientation, `kappa`, and the factor-two bridge were not fully visible inside the review-facing proof.

## Gate F — exact external theorem contracts

Status: `[>] NEXT — 13-13ff`.

State proof-facing imported versions of:

- Dirichlet/Gaussian-Hecke analytic continuation and functional equation;
- polynomial vertical/angular-conductor growth on the fixed strip needed by Gate D, sufficient to imply fixed `delta_H,C_H,D_H` for all `ell>=1`;
- holomorphy/no pole for nonzero angular index;
- Vaaler periodic interval majorant/minorant, including constant-term excess and nonzero coefficient bounds.

The hypotheses and conclusions actually used must be visible inside R05.

## Gate G — fixed inert-prime transfer

Status: `[ ] Pending Gate F`.

Expand the fixed-`S` overlap proposition: finite character decomposition, principal multiplier `prod lambda_p`, nonprincipal lower order, fixed-conductor control of mixed factors, and the order `fix S -> B->infinity -> |S|->infinity`.

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
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R05_REQUIRED_IF_THEOREM_SURVIVES_AUDIT=true
R05_FRESH_REVIEW_REQUIRED=true
PROMOTE_TO_13_13G=false
NEXT=13-13ff
```
