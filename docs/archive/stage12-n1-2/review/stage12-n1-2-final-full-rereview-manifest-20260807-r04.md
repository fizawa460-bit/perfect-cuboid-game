# Stage12-N1-2 final full re-review manifest R04

> **BUNDLE_ID:** `PC-N1-2-FINAL-FULL-REREVIEW-20260807-R04`
>
> **COMPLETED_THROUGH:** `Stage12-N1-3e`
>
> **SOURCE_SNAPSHOT_COMMIT:** `efe6ba788fa30e2c8f33b9cc98f99006dde34775`
>
> **SOURCE_LEDGER_SHA256:** `9938c98890850d545704128cb5a06c98cbc1422dfa14b0717a87abb1ea414435`
>
> **FINAL_DOCUMENT:** `docs/stage12-n1-2-final-r03.md`
>
> **REVIEW_PAGE:** `review/PC-N1-2-FINAL-FULL-REREVIEW-20260807-R04.html`
>
> **THEOREM_STATUS:** `FULL_ZERO_BASE_REREVIEW_CANDIDATE`

## Mandatory handshake

Before mathematical review, reproduce exactly:

```text
BUNDLE_ID=PC-N1-2-FINAL-FULL-REREVIEW-20260807-R04
COMPLETED_THROUGH=Stage12-N1-3e
SOURCE_SNAPSHOT_COMMIT=efe6ba788fa30e2c8f33b9cc98f99006dde34775
SOURCE_LEDGER_SHA256=9938c98890850d545704128cb5a06c98cbc1422dfa14b0717a87abb1ea414435
FINAL_DOCUMENT=docs/stage12-n1-2-final-r03.md
THEOREM_STATUS=FULL_ZERO_BASE_REREVIEW_CANDIDATE
END_OF_BUNDLE=PC-N1-2-FINAL-FULL-REREVIEW-20260807-R04
```

If any fixed value differs, return `STALE_SOURCE`. If `CHECKPOINT=END_OF_MAIN` or the end marker cannot be read, return `UNREADABLE_SOURCE`.

## Review scope

This is a **full zero-base re-review**, not another limited patch review.

Audit the complete consolidated proof of

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
=
\frac{\eta}{12\pi^2}B(\log B)^3,
\]

for the primitive oriented count defined in the embedded definition sheet.

Do not treat any prior `CLOSED` decision as binding. Recheck every implication needed by the displayed asymptotic. Earlier reviews may be used only to locate historically sensitive steps.

The target does **not** include:

- existence of a perfect cuboid;
- a canonical-count asymptotic;
- an exact-one-face asymptotic;
- an automatic conversion from oriented to canonical counts.

## Immutable source ledger

The consolidated Final R03 is generated from the following exact sources.

| path | Git blob SHA | role |
|---|---|---|
| `docs/stage12-n1-3d-definition-sheet.md` | `b44f76a890363708d6274d14b7f7154894debc7b` | target and counting conventions |
| `docs/stage12-n1-3d-constant-sheet.md` | `3428f220c35c3625589dc44abf55819b48109631` | Euler products and front factors |
| `docs/stage12-n1-3d-selberg-delange-reference-lock.md` | `23f887107b0babaadfcf6d6dc2e4255921c3651d` | analytic theorem input |
| `docs/stage12-n1-2-final-r02.md` | `e343182e82d9ecacf844fa7e508662749d43b55b` | integrated repaired proof through 3d |
| `docs/stage12-n1-3e-local-gap-closure.md` | `a61ba1fe84f49c92e4ccbcd5755ea1e3e0bf5ae5` | outer average and local-factor closure |

The physical R04 page contains the complete generated Final R03 text. The source files are integrity references, not prerequisites for reading.

## Required full-review questions

### A. Object and exact identities

1. Is the admissible parameter set unambiguous, including orientation, parity, height, multiplicity, and primitive conventions?
2. Is the exact global Möbius relation correct at the object level, including floors and endpoints?
3. Is the primitive-first formula with `A_{r,s}(m)` exact in both parity branches?
4. Are all constant `-1` terms and the `m=1` adjustment handled consistently?

### B. Fixed-circle input and outer average

5. Is the finite Euler correction `h_{r,s}` correct and is
   \[
   H_{\rm abs}(n)
   \]
   explicitly and consistently defined?
6. Does the pointwise estimate
   \[
   R_{r,s}(X)
   \ll G(rs)H_{\rm abs}(rs)X^{1/2}
   \]
   follow without the previously invalid extraction of `omega(X)`?
7. Is the Euler factorization for
   \[
   W(n)=G(n)H_{\rm abs}(n)
   \]
   correct and sufficient for
   \[
   \sum_{n\le T}W(n)\ll T\log(2T)?
   \]
8. Does the dyadic shell argument rigorously yield
   \[
   O\!\left(BX_0^{-1/2}(\log B)^2\right)?
   \]

### C. Selberg--Delange and rectangle asymptotics

9. Do the locked `z=1` and `z=2` Selberg--Delange uses satisfy the hypotheses of the cited theorem in the exact forms used?
10. Is arbitrary fixed log-power saving sufficient after every dyadic, partial-summation, and boundary loss?
11. Is the two-variable coprime rectangle factorization exact and uniform in the required ranges?
12. Is the corrected rectangular error
    \[
    R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}
    \]
    transferred with a genuinely lower-order total contribution?

### D. Local factors and constants

13. For odd primes, is
    \[
    D_{\lambda,p}(s_1,s_2)=1+U_p(s_1)+U_p(s_2)
    \]
    the exact coprime local factor?
14. Is the 2-adic factor exactly
    \[
    D_{\lambda,2}(s_1,s_2)
    =2+\frac{x}{1-x}+\frac{y}{1-y},
    \]
    and does its normalized value at `(1,1)` equal `1`?
15. Are the `p congruent 3 mod 4` and `q congruent 1 mod 4` factors correct prime by prime?
16. Does the full product give
    \[
    C_\lambda^{(0)}=\frac8{\pi^2}\eta?
    \]
17. Are the definitions of `kappa` and `eta`, and the exact identity
    \[
    \eta=\pi\kappa,
    \]
    independently recomputable from the displayed local factors?

### E. Coupled radial transfer

18. Is the passage from rectangle asymptotics to the radial Stieltjes integral justified without assuming the superseded fixed-`(b,c)` anisotropic kernel lemma?
19. Is
    \[
    \iint_{x^2+y^2\le B}
    \frac{\log x\log y}{x^2+y^2}\,dx\,dy
    =\frac\pi{48}(\log B)^3+O((\log B)^2)
    \]
    correct with the actual lower limits and boundary treatment?
20. Are orientation, parity, odd--odd cutoff `2B`, diagonal, arc-crossing boxes, shallow boxes, and annular differences all accounted for at lower order?
21. Does the complete factor ledger produce exactly
    \[
    \frac{1}{12}
    \]
    and no missing factor of `2`, `pi`, or orientation multiplicity?

### F. Final error budget and theorem status

22. Are every floor, endpoint, shallow, annulus, diagonal, fixed-height, and lower-log term collectively
    \[
    o\!\left(B(\log B)^3\right)?
    \]
23. Is any statement marked superseded still used implicitly?
24. Does the final conclusion prove exactly the stated primitive oriented asymptotic and nothing stronger?

## Required output

Classify each material finding as `FATAL`, `MAJOR`, `MINOR`, or `CLARIFICATION`, and return one of:

- `CLOSED`: the complete displayed theorem is supported by the consolidated proof;
- `REPAIRABLE`: a local, explicitly repairable gap remains;
- `OPEN`: a central implication is false or unsupported;
- `STALE_SOURCE`;
- `UNREADABLE_SOURCE`.

Use this machine-readable summary:

```text
VERDICT=
FATAL=
MAJOR=
MINOR=
CLARIFICATION=
COUNTING_DEFINITION=
PRIMITIVE_FIRST_IDENTITY=
FIXED_CIRCLE_AND_OUTER_AVERAGE=
SELBERG_DELANGE_INPUTS=
RECTANGLE_ASYMPTOTIC=
LOCAL_FACTOR_IDENTITY=
RADIAL_TRANSFER=
FINAL_ERROR_BUDGET=
CONSTANT_NORMALIZATION=
SUPERSEDED_LEMMA_USED=
NEW_CENTRAL_GAP=
THEOREM_STATUS=
```

A generic plausibility statement or a review of only the two R03 local items is not a completed review.