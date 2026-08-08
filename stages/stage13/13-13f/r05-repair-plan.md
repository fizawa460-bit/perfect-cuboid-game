# Stage13-13f — R05 repair / closure plan

> STATUS: `ACTIVE_REPAIR_PLAN_GATE_A_COMPLETE_GATE_B_NEXT`
>
> SOURCE_BUNDLE: `STAGE13-FINAL-SELF-CONTAINED-20260809-R04`
>
> R04_IMMUTABLE: `true`

This plan combines the unresolved Claude `OPEN` objection and DeepSeek `REPAIRABLE` objections. It is a repair/audit plan, not a presumption that the theorem statement is correct.

## Gate A — finite directional discrepancy and q-independence

Status: `[x] COMPLETE — 13-13fa`.

Artifacts:

```text
stages/stage13/13-13fa/result.md
stages/stage13/scripts/13-13fa/q_independence_finite_audit.py
stages/stage13/data/13-13fa/q_independence_finite_audit.json
.github/workflows/stage13-13fa-q-independence.yml
```

Result:

- every retained exact-one cutoff available from the historical PR #89 fixture and active 100k..5m scaling reports was normalized against both `2:1:1` and `8 I_q/pi^2`;
- from `B=100000` to `B=5000000`, L1 distance from exact `2:1:1` grows from `0.0155150866` to `0.0237058175`, while L1 distance to the claimed vector falls from `0.0679146211` to `0.0618745005`;
- the trajectory is not monotone at every cutoff, so no monotonicity or effective secondary asymptotic is claimed;
- the common-`Theta` chain was retraced from the primitive `j=0` local coefficient through the mixed correction, parity factors, curved zero mode and only then Stage12 calibration;
- no surviving q-dependent leading arithmetic factor was found at the current proof level;
- the theorem supplies only a little-`o` remainder, not an effective convergence rate capable of numerically explaining the `B<=5m` discrepancy.

Locks:

```text
STAGE13_13FA=COMPLETE_Q_INDEPENDENCE_AND_FINITE_DISCREPANCY_AUDIT
FINITE_DATA_CONTRADICTS_THEOREM=false
LEADING_Q_DEPENDENT_ARITHMETIC_FACTOR_FOUND=false
COMMON_THETA_AUDIT=PASS_AT_CURRENT_PROOF_LEVEL
PROVED_EFFECTIVE_CONVERGENCE_RATE=false
FINITE_DISCREPANCY_QUANTITATIVELY_EXPLAINED_BY_PROVED_REMAINDER=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R04_IMMUTABLE=true
R05_REQUIRED=true
```

Gate A closes the finite-contradiction and missing-leading-q-factor components of the Claude objection at the current theorem level. It does **not** claim an effective rate, and it does not repair DeepSeek's proof-explicitness objections.

## Gate B — explicit Wiener bound

Status: `[>] NEXT — 13-13fb`.

Expose a line-by-line lemma proving or replacing

```text
||C_{ell,p}-1||_{5/8} <= 529 p^(-5/4), p>=13.
```

The proof must state the local rational functions, support cancellation of pure axes, weighted Wiener estimates for numerator/denominator inverses, the origin of the constant, treatment of `p=5`, and uniformity in the retained angular phase.

## Gate C — curved-region error ledger

Status: `[ ] Pending Gate B`.

Write explicit lemmas for:

- small height;
- small coordinate;
- multiplicative core boxes;
- rectangle Perron tails;
- boxes meeting the curved boundary;
- accumulation over `O((log B)^C)` boxes.

All exponents must be substituted with

```text
H0=U=exp((log B)^(1/4))
eta=(log B)^(-8)
```

so the final `o(B(log B)^3)` conclusion is mechanically auditable.

## Gate D — retained nonzero harmonics

Status: `[ ] Pending Gate C`.

State an explicit Hecke-family lemma on the exact strip used, with conductor dependence sufficient for

```text
1 <= ell <= (log B)^4.
```

Show algebraically how `(1+ell)^C`, Vaaler coefficients, the number of modes, and the chosen finite cancellation order combine to the final harmonic error. Avoid hiding unknown fixed powers behind an unqualified choice such as `A=48`; either prove 48 dominates the actual exponent or choose the cancellation order as an explicit function of the imported polynomial-growth exponent.

## Gate E — complete Stage12 interface

Status: `[ ] Pending Gate D`.

Copy into the repaired proof the exact interface needed from Stage12 R09:

- definition of `C_prim(B)`;
- orientation/counting convention;
- definition/provenance interface for `kappa`;
- exact projection map to the Stage13 canonical triples;
- proof of the finite factor-two multiplicity;
- statement of what Stage12 does and does not supply about directionality.

## Gate F — exact external theorem contracts

Status: `[ ] Pending Gate E`.

State the proof-facing imported versions of:

- Dirichlet/Gaussian-Hecke analytic continuation, functional equation and strip/conductor growth;
- holomorphy at `s=1` for nonzero angular index;
- Vaaler periodic interval majorant/minorant, including zero-mode excess and nonzero Fourier coefficient bounds.

The bundle may cite these theorems externally, but the hypotheses and conclusions actually used must be visible inside the bundle.

## Gate G — fixed inert-prime transfer

Status: `[ ] Pending Gate F`.

Expand §13 into a formal fixed-`S` proposition. It must show:

1. finite residue-state decomposition and character orthogonality;
2. the principal tuple multiplies the raw top coefficient by `prod_{p in S} lambda_p`;
3. nonprincipal tuples remove at least one principal pole and contribute `o(B(log B)^3)` for each fixed `S`;
4. mixed correction/local Euler factors remain absolutely controlled under the fixed conductor restrictions;
5. the order `fix S -> B to infinity -> |S| to infinity` is explicit.

## Gate H — notation and audit scope

Status: `[ ] Pending Gate G`.

- Rename the local angular phase so it is not confused with the spherical-coordinate `theta`.
- Define `C_{ell,p}` with its substitutions `x=p^{-s_h}`, `y=p^{-s_r}`, `z=p^{-s_s}` at first use.
- Reword deterministic audit status so `PASS` means reproducibility/consistency only, never proof validation.

## Promotion rule

After Gates A-H:

- if a leading q-dependent defect is found, reopen the theorem contract and do **not** generate R05 as a cosmetic repair;
- if the theorem survives unchanged, produce a new immutable R05 bundle containing all repairs;
- obtain fresh independent reviews on R05;
- do not count R04 `CLOSED` verdicts toward final R05 freeze unless the reviewer explicitly re-reviews R05.

```text
R04_IMMUTABLE=true
STAGE13_13FA=COMPLETE_Q_INDEPENDENCE_AND_FINITE_DISCREPANCY_AUDIT
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R05_REQUIRED_IF_THEOREM_SURVIVES_AUDIT=true
R05_FRESH_REVIEW_REQUIRED=true
PROMOTE_TO_13_13G=false
NEXT=13-13fb
```
