# Stage12-N1-2 final full re-review manifest R05

> **BUNDLE_ID:** `PC-N1-2-FINAL-FULL-REREVIEW-20260807-R05`
>
> **COMPLETED_THROUGH:** `Stage12-N1-3f`
>
> **SOURCE_SNAPSHOT_COMMIT:** `b0208ce33204a3c5f5a52afec146b08a313203f1`
>
> **SOURCE_LEDGER_SHA256:** `f758808bc7f36307b9abcb2b6038ce497735619382fc7bc3056c65cc246cf16f`
>
> **FINAL_DOCUMENT:** `docs/stage12-n1-2-final-r04.md`
>
> **REVIEW_PAGE:** `review/PC-N1-2-FINAL-FULL-REREVIEW-20260807-R05.html`
>
> **THEOREM_STATUS:** `FULL_ZERO_BASE_REREVIEW_CANDIDATE_AFTER_R04_REPAIR`

## Mandatory handshake

Before mathematical review, reproduce exactly:

```text
BUNDLE_ID=PC-N1-2-FINAL-FULL-REREVIEW-20260807-R05
COMPLETED_THROUGH=Stage12-N1-3f
SOURCE_SNAPSHOT_COMMIT=b0208ce33204a3c5f5a52afec146b08a313203f1
SOURCE_LEDGER_SHA256=f758808bc7f36307b9abcb2b6038ce497735619382fc7bc3056c65cc246cf16f
FINAL_DOCUMENT=docs/stage12-n1-2-final-r04.md
THEOREM_STATUS=FULL_ZERO_BASE_REREVIEW_CANDIDATE_AFTER_R04_REPAIR
END_OF_BUNDLE=PC-N1-2-FINAL-FULL-REREVIEW-20260807-R05
```

If any fixed value differs, return `STALE_SOURCE`. If `CHECKPOINT=END_OF_MAIN` or the end marker cannot be read, return `UNREADABLE_SOURCE`.

## Scope and precedence

This is a **full zero-base re-review** of the complete theorem candidate, not a review limited to the R04 finding.

Audit

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
=
\frac{\eta}{12\pi^2}B(\log B)^3
\]

for the primitive oriented count defined in the embedded definition sheet.

Do not treat prior `CLOSED` findings as binding. Earlier audits may be used only to identify sensitive points.

One explicit source-precedence rule is necessary because the bundle retains historical sources for integrity:

```text
SUPERSEDED:
retained boxes satisfy min(R,S) >= S0

ACTIVE REPLACEMENT:
core boxes are defined by R,S >= S0;
the r-wing and s-wing are bounded directly by Stage12-N1-3f
```

Do not reject the bundle merely because the superseded historical sentence remains visible. Instead, verify that the active 3f replacement is mathematically sufficient and that no later argument still relies on the false implication.

The target excludes perfect-cuboid existence, canonical counting, exact-one-face counting, and any automatic conversion from oriented to canonical counts.

## Immutable source ledger

| path | Git blob SHA | role |
|---|---|---|
| `docs/stage12-n1-3d-definition-sheet.md` | `b44f76a890363708d6274d14b7f7154894debc7b` | target and counting conventions |
| `docs/stage12-n1-3d-constant-sheet.md` | `3428f220c35c3625589dc44abf55819b48109631` | Euler products and front factors |
| `docs/stage12-n1-3d-selberg-delange-reference-lock.md` | `23f887107b0babaadfcf6d6dc2e4255921c3651d` | analytic theorem input |
| `docs/stage12-n1-2-final-r02.md` | `e343182e82d9ecacf844fa7e508662749d43b55b` | integrated proof through 3d |
| `docs/stage12-n1-3e-local-gap-closure.md` | `a61ba1fe84f49c92e4ccbcd5755ea1e3e0bf5ae5` | outer average and local factors |
| `docs/stage12-n1-3f-small-coordinate-wing.md` | `e2c77dc23744cb0b9866b40e7a4c0646b0994dd6` | R04 small-coordinate wing repair |

The R05 physical page contains the complete generated Final R04 text. The source files are integrity references, not prerequisites for reading.

## Required full-review questions

### A. Object and exact identities

1. Is the admissible parameter set unambiguous, including orientation, parity, height, multiplicity, and primitive conventions?
2. Is the exact global Möbius relation correct at object level, including floors and endpoints?
3. Is the primitive-first formula exact in both parity branches?
4. Are the `m=1` and constant `-1` terms handled consistently?

### B. Fixed-circle input and outer average

5. Is `H_abs(n)` explicitly and consistently defined?
6. Does
   \[
   R_{r,s}(X)\ll G(rs)H_{\rm abs}(rs)X^{1/2}
   \]
   follow without extracting the old invalid `omega(X)` factor?
7. Is the Euler factorization for `W(n)=G(n)H_abs(n)` correct and sufficient for
   \[
   \sum_{n\le T}W(n)\ll T\log(2T)?
   \]
8. Does the retained shell argument rigorously give
   \[
   O(BX_0^{-1/2}(\log B)^2)?
   \]
9. Is the fixed-height retained/shallow split kept logically separate from the radial core/wing split?

### C. Selberg--Delange and rectangle asymptotics

10. Do the locked `z=1` and `z=2` Selberg--Delange uses satisfy the cited theorem's hypotheses in the exact forms used?
11. Is arbitrary fixed log-power saving sufficient after every dyadic and partial-summation loss?
12. Is the two-variable coprime rectangle factorization exact and uniform on the core boxes?
13. Is the corrected rectangular power error
    \[
    R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}
    \]
    transferred with a lower-order total contribution when `R,S>=U`?

### D. Small-coordinate wing repair

14. Is the one-variable bound
    \[
    \sum_{n\le X}\frac{g(n)}{u^2+n^2}
    \ll\frac{\log(2u)}u
    \]
    valid uniformly in `u,X` from `G_0(t)<<t log(2t)`?
15. Does partial summation yield
    \[
    \sum_{r<U}\frac{g(r)\log(2r)}r
    \ll(\log(2U))^3?
    \]
16. After dropping coprimality and using `lambda<=2`, is the complete discrete union of the `r`-wing and `s`-wing bounded by
    \[
    O((\log U)^3)=O((\log B)^{3/4})?
    \]
17. Is the analogous continuous leading-density wing integral also `O((log U)^3)`?
18. Does the core/wing decomposition cover the full radial region without omission, with overlap harmlessly overcounted only in an upper bound?
19. Does boxwise partial summation avoid introducing an unhandled artificial boundary at `x=U` or `y=U`?
20. Is the old inference `retained => min(R,S)>=S0` absent from the active proof after applying the supersession rule?

### E. Local factors and constants

21. For odd primes, is
    \[
    D_{\lambda,p}(s_1,s_2)=1+U_p(s_1)+U_p(s_2)
    \]
    exact?
22. Is the 2-adic factor exactly
    \[
    D_{\lambda,2}(s_1,s_2)
    =2+\frac{x}{1-x}+\frac{y}{1-y},
    \]
    with normalized value `1` at `(1,1)`?
23. Do the prime-by-prime products give
    \[
    C_\lambda^{(0)}=\frac8{\pi^2}\eta?
    \]
24. Are `kappa`, `eta`, and
    \[
    \eta=\pi\kappa
    \]
    independently reproducible from the displayed factors?

### F. Coupled radial transfer and final budget

25. Is the full radial leading integral
    \[
    \iint_{x^2+y^2\le B}\frac{\log x\log y}{x^2+y^2}\,dx\,dy
    =\frac\pi{48}(\log B)^3+O((\log B)^2)
    \]
    correct with the actual lower limits?
26. Does core transfer plus the discrete and continuous wing bounds recover the full-quadrant asymptotic with `o((log B)^3)` error?
27. Are orientation, parity, odd--odd cutoff `2B`, diagonal, arc boxes, annulus, floors, endpoint terms, fixed-height errors, and lower rectangle terms all collectively lower order?
28. Does the factor ledger produce exactly `1/12`?
29. Is the superseded fixed-`(b,c)` anisotropic kernel lemma still unused?
30. Does the final result prove exactly the primitive oriented asymptotic and nothing stronger?

## Required output

Classify findings as `FATAL`, `MAJOR`, `MINOR`, or `CLARIFICATION`, and return one of:

- `CLOSED`: the complete displayed theorem is supported;
- `REPAIRABLE`: an explicit local repair remains;
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
SMALL_COORDINATE_WING=
LOCAL_FACTOR_IDENTITY=
RADIAL_TRANSFER=
FINAL_ERROR_BUDGET=
CONSTANT_NORMALIZATION=
SUPERSEDED_LEMMA_USED=
NEW_CENTRAL_GAP=
THEOREM_STATUS=
```

A generic plausibility statement or a review only of Stage12-N1-3f is not a completed review.
