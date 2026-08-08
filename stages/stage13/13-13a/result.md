# Stage13-13a — result

> STATUS: `STAGE13_13A_COMPLETE_CLAIM_DEPENDENCY_LEDGER`
>
> NEXT: `13-13b`

## Result

Stage13 R03 plus the post-review `13-12ag` supplement have been decomposed into a 30-entry claim/dependency ledger before any canonical rewrite.

The audit freezes the theorem to be reproduced by `13-13c`:

\[
N_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\qquad q\in\{ab,ac,bc\},
\]

\[
N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3,
\]

with

\[
I_{ab}+I_{ac}+I_{bc}=\frac{\pi^2}{8},
\qquad
J_q=\frac{2I_q}{\pi},
\qquad
P_q=\frac{8I_q}{\pi^2}.
\]

The exact inert-prime overlap multiplier is frozen as

\[
\lambda_p=\frac{p+5}{2(p+1)},
\]

and the overlap conclusions remain

\[
O_{qr}(B)=o(B(\log B)^3),
\qquad
T(B)=o(B(\log B)^3).
\]

No perfect-cuboid nonexistence assumption is used.

## Dependency boundary

Every active dependency is now classified as one of:

```text
INTERNAL_PROOF
FROZEN_STAGE12_INPUT
STANDARD_EXTERNAL_THEOREM
FINITE_CHECK
REVIEW_RECORD
```

The Stage12 dependency is limited to its frozen R09 primitive-oriented theorem interface, in particular

\[
C_{\rm prim}(B)\sim\frac{\kappa}{12\pi}B(\log B)^3.
\]

The external theorem categories have all been located. Their precise source/hypothesis verification is intentionally the next token, `13-13b`.

## Supersession result

The active theorem chain does **not** require the superseded Stage13-7jb or Stage13-7jf arguments, R01/R02 proof bundles, categorywise numerical `D_q/K_q` equality, finite-field enumeration as proof, or finite directional fits as proof.

```text
HISTORICAL_SUPERSEDED_ARGUMENT_REQUIRED=false
```

## Drift found

No theorem-level contradiction was found. Five documentation/provenance drifts were isolated:

1. the immutable R03 header still says `PENDING_EXTERNAL_R03`, although later records contain Grok/Qwen `CLOSED`;
2. older wording around `J_q=2I_q/pi` gives too much prominence to numerical checking; `13-12ag` now contains the explicit derivation;
3. `13-12ab` has a soft `lambda_p=1/2+O(1/p)` bound superseded by the exact `13-12ae` formula;
4. `13-12ag` expands the R03 unit-state character calculation without changing its result;
5. exact publication-grade theorem/source/hypothesis mapping for the external analytic inputs remains to be completed in `13-13b`.

R03 remains immutable; these are not repaired by rewriting the old bundle.

## Locks

```text
STAGE13_13A=COMPLETE_CLAIM_DEPENDENCY_LEDGER
CLAIM_COUNT=30
THEOREM_STATEMENT_FROZEN_FOR_RESYNTHESIS=true
THEOREM_LEVEL_DEFECT_FOUND=false
HISTORICAL_SUPERSEDED_ARGUMENT_REQUIRED=false
EXTERNAL_DEPENDENCY_CATEGORIES_IDENTIFIED=true
FULL_EXTERNAL_HYPOTHESIS_AUDIT_DEFERRED_TO_13_13B=true
R03_IMMUTABLE=true
STAGE12_R09_REOPENED=false
NEXT=13-13b
```

Canonical artifacts:

```text
stages/stage13/13-13a/claim-dependency-ledger.md
stages/stage13/13-13a/result.md
stages/stage13/data/13-13a/claim-dependency-ledger.json
```
