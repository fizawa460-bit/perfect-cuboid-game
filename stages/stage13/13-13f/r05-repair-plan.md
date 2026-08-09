# Stage13-13f — R05 repair / closure plan

> STATUS: `ACTIVE_REPAIR_PLAN_GATES_A_B_C_D_COMPLETE_GATE_E_NEXT`
>
> SOURCE_BUNDLE: `STAGE13-FINAL-SELF-CONTAINED-20260809-R04`
>
> R04_IMMUTABLE: `true`

This plan repairs the Claude `OPEN` and DeepSeek `REPAIRABLE` objections without mutating R04 or presuming the theorem survives.

## Gate A — finite discrepancy and q-independence

Status: `[x] COMPLETE — 13-13fa`.

Artifacts: `stages/stage13/13-13fa/` plus dedicated script/data/CI.

Result: finite exact-one data through `B=5m` do not contradict the claimed asymptotic vector; no surviving leading q-dependent arithmetic factor was found. The theorem still has no effective convergence rate.

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

Artifacts: `stages/stage13/13-13fb/` plus dedicated script/data/CI.

The phase-uniform coefficientwise calculation gives

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

Artifacts: `stages/stage13/13-13fc/` plus dedicated script/data/CI.

The formerly unspecified global accumulation is explicit:

```text
BOX_COUNT=O((log B)^27)
FINITE_REMAINDER_N=64
FINITE_REMAINDER_AFTER_ALL_BOXES=O(B(log B)^-35)
POWER_TAIL_SAVING=exp(-(3/16)(log B)^(1/4))
CURVED_BOUNDARY=O(B(log B)^-5)+lower-order-ledger
MESH_ERROR=O(B(log B)^-5)
```

The small-height, small-coordinate and mixed-shift terms remain respectively `O(B log^(9/4) B)`, `O(B log^(5/2) B)` and `O(B log^2 B)`.

## Gate D — retained nonzero harmonics

Status: `[x] COMPLETE — 13-13fd`.

Artifacts:

```text
stages/stage13/13-13fd/harmonic-conductor-lemma.md
stages/stage13/13-13fd/result.md
stages/stage13/scripts/13-13fd/harmonic_conductor_audit.py
stages/stage13/data/13-13fd/harmonic_conductor_audit.json
.github/workflows/stage13-13fd-harmonic-conductor.yml
```

The old `A=48` bookkeeping is no longer a logical premise. Gate D exposes the conductor loss itself. On the fixed strip `Re s>=3/4`, use fixed constants `delta_H>0`, `C_H,D_H>=0` with

```text
S_ell(X) << X^(1-delta_H) (1+ell)^C_H (log(2X))^D_H
```

uniformly for **all** `X>=2` and `ell>=1`. This all-ell formulation is necessary because at the core lower cutoff `X=H0`, the global retained range `ell<=floor((log B)^4)` is not contained in `ell<=(log X)^4`.

On `h>=H0=exp((log B)^(1/4))`, partial summation gives the scale saving

```text
(1+ell)^C_H (log B)^D_H exp(-delta_H*(log B)^(1/4)).
```

The two base channels cost `+2` logarithmic powers. Summing `ell<=L=(log B)^4` costs `4*C_H+4`, hence

```text
HARMONIC_POLYLOG_EXPONENT=4*C_H+D_H+6
HARMONIC_STRETCHED_SAVING=exp(-delta_H*(log B)^(1/4))
HARMONIC_CORE=o_A(B(log B)^(-A))_for_every_fixed_A
```

The wings are removed by the positive Gate C bound **before** harmonic expansion, so no factor `L` is charged to them. The Vaaler constant-term excess is `O(B(log B)^-1)`.

```text
STAGE13_13FD=COMPLETE_RETAINED_HARMONIC_CONDUCTOR_BOOKKEEPING
HECKE_STRIP_LEFT=3/4
HECKE_FAMILY_BOUND=S_ell(X)<<X^(1-delta_H)(1+ell)^C_H(log(2X))^D_H_for_all_ell>=1
RETAINED_HARMONICS=ell<=floor((log B)^4)
FIXED_A48_REQUIRED=false
GAUSSIAN_HECKE_ZERO_FREE_REGION_REQUIRED=false
WINGS_EXPANDED_HARMONIC_BY_HARMONIC=false
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
```

Gate D closes the conductor/log-bookkeeping objection. Gate F still has to expose the exact imported Hecke and Vaaler theorem statements; Gate D does not substitute for that external-contract audit.

## Gate E — complete Stage12 interface

Status: `[>] NEXT — 13-13fe`.

Copy into the repaired proof the exact frozen Stage12 R09 interface:

- definition of `C_prim(B)`;
- orientation/counting convention;
- definition/provenance interface for `kappa`;
- exact projection from Stage12 oriented objects to Stage13 canonical triples;
- proof of the factor-two multiplicity;
- explicit statement that Stage12 supplies the total asymptotic but no directional proportionality.

## Gate F — exact external theorem contracts

Status: `[ ] Pending Gate E`.

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

- propagate `vartheta` for local angular phase;
- define `C_{ell,p}` substitutions at first use;
- keep deterministic `PASS` explicitly limited to reproducibility/consistency;
- synthesize Gates A–G into the repaired canonical proof and decide whether immutable R05 can be generated.

## Promotion rule

If any later repair finds a genuine theorem-level defect, reopen the theorem contract. Otherwise, after A–H create a new immutable R05 bundle and obtain fresh independent reviews. R04 verdicts do not automatically count toward R05 freeze.

```text
R04_IMMUTABLE=true
STAGE13_13FA=COMPLETE_Q_INDEPENDENCE_AND_FINITE_DISCREPANCY_AUDIT
STAGE13_13FB=COMPLETE_EXPLICIT_WIENER_BOUND
STAGE13_13FC=COMPLETE_CURVED_REGION_ERROR_ACCUMULATION
STAGE13_13FD=COMPLETE_RETAINED_HARMONIC_CONDUCTOR_BOOKKEEPING
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R05_REQUIRED_IF_THEOREM_SURVIVES_AUDIT=true
R05_FRESH_REVIEW_REQUIRED=true
PROMOTE_TO_13_13G=false
NEXT=13-13fe
```
