# Stage12-N1-2 final full re-review manifest R06

> **BUNDLE_ID:** `PC-N1-2-FINAL-FULL-REREVIEW-20260807-R06`
>
> **COMPLETED_THROUGH:** `Stage12-N1-3g`
>
> **SOURCE_SNAPSHOT_COMMIT:** `c9a91650bece7a2173af4f495212faf1a1054aeb`
>
> **SOURCE_LEDGER_SHA256:** `511a055bd243e0b4f40d554c949e5c1c52db1cc412bcadae55eb8b99e6de2e49`
>
> **FINAL_DOCUMENT:** `docs/stage12-n1-2-final-r05.md`
>
> **REVIEW_PAGE:** `review/PC-N1-2-FINAL-FULL-REREVIEW-20260807-R06.html`
>
> **THEOREM_STATUS:** `FULL_ZERO_BASE_REREVIEW_CANDIDATE_AFTER_R05_REPAIR`

## Mandatory handshake

Before mathematical review, reproduce exactly:

```text
BUNDLE_ID=PC-N1-2-FINAL-FULL-REREVIEW-20260807-R06
COMPLETED_THROUGH=Stage12-N1-3g
SOURCE_SNAPSHOT_COMMIT=c9a91650bece7a2173af4f495212faf1a1054aeb
SOURCE_LEDGER_SHA256=511a055bd243e0b4f40d554c949e5c1c52db1cc412bcadae55eb8b99e6de2e49
FINAL_DOCUMENT=docs/stage12-n1-2-final-r05.md
THEOREM_STATUS=FULL_ZERO_BASE_REREVIEW_CANDIDATE_AFTER_R05_REPAIR
END_OF_BUNDLE=PC-N1-2-FINAL-FULL-REREVIEW-20260807-R06
```

If any fixed value differs, return `STALE_SOURCE`. If `CHECKPOINT=END_OF_MAIN` or the end marker cannot be read, return `UNREADABLE_SOURCE`.

## Review scope

This is a **complete zero-base re-review**, not a limited review of Stage12-N1-3g.

Audit the complete consolidated proof of

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
=
\frac{\eta}{12\pi^2}B(\log B)^3
\]

for the primitive oriented count defined in the embedded proof.

Do not treat any prior `CLOSED` decision as binding. Recheck every implication needed by the displayed asymptotic. Earlier audits may be used to locate sensitive steps only.

The target does **not** include:

- existence of a perfect cuboid;
- a canonical-count asymptotic;
- an exact-one-face asymptotic;
- an automatic conversion from oriented to canonical counts.

## Active supersession rules

The following historical statements are not active proof steps:

```text
retained boxes satisfy min(R,S) >= S0
shallow fixed-height sector: o(BL^3) by nonnegative rectangle upper bounds
```

The active replacements are:

```text
radial core boxes are defined by R,S >= S0 and the complementary wings are bounded by Stage12-N1-3f
fixed-height shallow sector is bounded directly by Stage12-N1-3g as O(BL^(5/2))
```

The fixed-height retained/shallow split and the radial core/wing split must be checked as distinct decompositions.

## Immutable source ledger

| path | Git blob SHA | role |
|---|---|---|
| `docs/stage12-n1-2-final-r04.md` | `f6eaf4eca8e58c686a69b530161c9b213f774df5` | complete consolidated proof through Stage12-N1-3f |
| `docs/stage12-n1-3g-fixed-height-shallow-sector.md` | `c7024e1422b90c71a62906af83314f25b847bc4f` | explicit fixed-height shallow-sector closure |

The physical R06 page contains the complete generated Final R05 text. The source files are integrity references, not prerequisites for reading.

## Required full-review questions

### A. Object and exact identities

1. Is the admissible parameter set unambiguous, including orientation, parity, height, multiplicity, and primitive conventions?
2. Is the exact global Möbius relation correct at the object level, including floors and endpoints?
3. Is the primitive-first formula with `A_{r,s}(m)` exact in both parity branches?
4. Are `A_{r,s}(1)=G(rs)-1`, the constant `-1`, and the positive version handled consistently?

### B. Fixed-circle retained input

5. Is the finite Euler correction and its absolute `1/2`-norm correct?
6. Does
   \[
   R_{r,s}(X)\ll G(rs)H_{\rm abs}(rs)X^{1/2}
   \]
   follow without the invalid extraction of `omega(X)`?
7. Is the Euler factorization for `W(n)=G(n)H_abs(n)` correct and sufficient for
   \[
   \sum_{n\le T}W(n)\ll T\log(2T)?
   \]
8. Does the retained shell argument yield
   \[
   O(BX_0^{-1/2}(\log B)^2)?
   \]

### C. Fixed-height shallow sector — Stage12-N1-3g

9. Does the exact formula imply, for every `m>=1`,
   \[
   0\le A_{r,s}(m)\le G(rs)2^{\omega(m)}?
   \]
10. Is
    \[
    2^{\omega(m)}=\sum_{d\mid m}\mu^2(d)
    \]
    used correctly to obtain
    \[
    \sum_{m\le X}2^{\omega(m)}\ll X\log(2X)?
    \]
11. Is the factorization
    \[
    \sum_{n\ge1}\frac{G(n)}{n^s}
    =\zeta(s)^2L(s,\chi_4)
    (1-2^{-s})\prod_{p\text{ odd}}(1-p^{-2s})
    \]
    correct prime by prime and sufficient for
    \[
    \sum_{n\le Y}G(n)\ll Y\log(2Y)?
    \]
12. Does the square majorization rigorously give
    \[
    \sum_{Q<r^2+s^2\le2Q}G(r)G(s)
    \ll Q(\log(2Q))^2?
    \]
13. Does `1<=X_{r,s}<X0` imply the common annulus
    \[
    B/X_0<r^2+s^2\le2B
    \]
    uniformly in both parity branches?
14. Is that annulus covered by `O(log X0)` dyadic radial shells, and does the resulting harmonic weighted sum satisfy
    \[
    \sum_{\rm shallow}
    \frac{\lambda(r,s)G(rs)}{r^2+s^2}
    \ll L^2\log(2X_0)?
    \]
15. Does the complete exact shallow contribution satisfy
    \[
    \mathcal S_{\rm sh}(B)
    \ll BL^2\{\log(2X_0)\}^2
    \ll BL^{5/2}
    =o(BL^3)?
    \]
16. Are orientation, coprimality, and parity removed only in the direction of a valid nonnegative upper bound?

### D. Selberg--Delange and rectangle asymptotics

17. Do the locked `z=1` and `z=2` Selberg--Delange uses satisfy the hypotheses of the cited theorem in the exact forms used?
18. Is arbitrary fixed log-power saving sufficient after all dyadic, partial-summation, and boundary losses?
19. Is the two-variable coprime rectangle factorization exact and uniform in the required ranges?
20. Is the corrected rectangular error
    \[
    R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}
    \]
    transferred with a genuinely lower-order total contribution on the radial core?

### E. Local factors and constants

21. For odd primes, is
    \[
    D_{\lambda,p}(s_1,s_2)=1+U_p(s_1)+U_p(s_2)
    \]
    the exact coprime local factor?
22. Is the 2-adic factor exactly
    \[
    D_{\lambda,2}(s_1,s_2)
    =2+\frac{x}{1-x}+\frac{y}{1-y},
    \]
    and does its normalized value at `(1,1)` equal `1`?
23. Are the `p congruent 3 mod 4` and `q congruent 1 mod 4` factors correct prime by prime?
24. Does the full product give
    \[
    C_\lambda^{(0)}=\frac8{\pi^2}\eta?
    \]
25. Are the definitions of `kappa` and `eta`, and the identity
    \[
    \eta=\pi\kappa,
    \]
    independently recomputable from the displayed local factors?

### F. Coupled radial transfer and small-coordinate wings

26. Is the passage from rectangle asymptotics to the radial Stieltjes integral justified without the superseded fixed-`(b,c)` anisotropic kernel lemma?
27. Is
    \[
    \iint_{x^2+y^2\le B}
    \frac{\log x\log y}{x^2+y^2}\,dx\,dy
    =\frac\pi{48}(\log B)^3+O((\log B)^2)
    \]
    correct with the actual lower limits and boundary treatment?
28. Is the Stage12-N1-3f bound
    \[
    \sum_{\min(r,s)<U}
    \frac{\lambda(r,s)g(r)g(s)}{r^2+s^2}
    =O((\log U)^3)=o(L^3)
    \]
    valid for the complete discrete wings?
29. Is the continuous leading-density wing also `O((log U)^3)` so that the core main integral recovers the full radial leading coefficient?
30. Are orientation, parity, odd--odd cutoff `2B`, diagonal, arc-crossing boxes, annular differences, and artificial core boundaries all lower order?
31. Does the factor ledger produce exactly `1/12`, with no missing factor of `2`, `pi`, or orientation multiplicity?

### G. Final error budget and theorem status

32. Are the retained fixed-height remainder, the explicit shallow bound, radial core errors, radial wings, floor, endpoint, annulus, diagonal, and lower-log terms collectively
    \[
    o(B(\log B)^3)?
    \]
33. Is any superseded statement or lemma still used implicitly?
34. Does the final conclusion prove exactly the primitive oriented asymptotic and nothing stronger?

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
FIXED_CIRCLE_RETAINED=
FIXED_HEIGHT_SHALLOW=
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

A generic plausibility statement or a review only of Stage12-N1-3g is not a completed review.
