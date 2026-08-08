# Stage13-13f — R05 repair / closure plan

> STATUS: `ACTIVE_REPAIR_PLAN_FROM_R04_EXTERNAL_REVIEWS`
>
> SOURCE_BUNDLE: `STAGE13-FINAL-SELF-CONTAINED-20260809-R04`
>
> R04_IMMUTABLE: `true`

This plan combines the unresolved Claude `OPEN` objection and DeepSeek `REPAIRABLE` objections. It is a repair/audit plan, not a presumption that the theorem statement is correct.

## Gate A — finite directional discrepancy and q-independence

1. Collect every available exact directional cutoff in the repository and normalize the exactly-one vector.
2. Compare the finite vectors with both `2:1:1` and the claimed limit `8 I_q/pi^2`.
3. Fit only descriptive secondary-term diagnostics; do not infer the theorem from finite data.
4. Retrace the top-degree arithmetic coefficient through the primitive local coefficient system, mixed Euler/Wiener correction, parity branches and curved-region assembly.
5. Explicitly prove that no q-dependent leading arithmetic factor survives, or record a theorem-level defect if one is found.
6. State what remainder information is actually proved and whether it is quantitatively strong enough to explain the observed finite discrepancy. If not, say so explicitly rather than claiming empirical confirmation.

## Gate B — explicit Wiener bound

Expose a line-by-line lemma proving or replacing

```text
||C_{ell,p}-1||_{5/8} <= 529 p^(-5/4), p>=13.
```

The proof must state the local rational functions, support cancellation of pure axes, weighted Wiener estimates for numerator/denominator inverses, the origin of the constant, treatment of `p=5`, and uniformity in the retained angular phase.

## Gate C — curved-region error ledger

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

State an explicit Hecke-family lemma on the exact strip used, with conductor dependence sufficient for

```text
1 <= ell <= (log B)^4.
```

Show algebraically how `(1+ell)^C`, Vaaler coefficients, the number of modes, and the chosen finite cancellation order combine to the final harmonic error. Avoid hiding unknown fixed powers behind an unqualified choice such as `A=48`; either prove 48 dominates the actual exponent or choose the cancellation order as an explicit function of the imported polynomial-growth exponent.

## Gate E — complete Stage12 interface

Copy into the repaired proof the exact interface needed from Stage12 R09:

- definition of `C_prim(B)`;
- orientation/counting convention;
- definition/provenance interface for `kappa`;
- exact projection map to the Stage13 canonical triples;
- proof of the finite factor-two multiplicity;
- statement of what Stage12 does and does not supply about directionality.

## Gate F — exact external theorem contracts

State the proof-facing imported versions of:

- Dirichlet/Gaussian-Hecke analytic continuation, functional equation and strip/conductor growth;
- holomorphy at `s=1` for nonzero angular index;
- Vaaler periodic interval majorant/minorant, including zero-mode excess and nonzero Fourier coefficient bounds.

The bundle may cite these theorems externally, but the hypotheses and conclusions actually used must be visible inside the bundle.

## Gate G — fixed inert-prime transfer

Expand §13 into a formal fixed-`S` proposition. It must show:

1. finite residue-state decomposition and character orthogonality;
2. the principal tuple multiplies the raw top coefficient by `prod_{p in S} lambda_p`;
3. nonprincipal tuples remove at least one principal pole and contribute `o(B(log B)^3)` for each fixed `S`;
4. mixed correction/local Euler factors remain absolutely controlled under the fixed conductor restrictions;
5. the order `fix S -> B to infinity -> |S| to infinity` is explicit.

## Gate H — notation and audit scope

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
R05_REQUIRED_IF_THEOREM_SURVIVES_AUDIT=true
R05_FRESH_REVIEW_REQUIRED=true
PROMOTE_TO_13_13G=false
NEXT=13-13f
```
