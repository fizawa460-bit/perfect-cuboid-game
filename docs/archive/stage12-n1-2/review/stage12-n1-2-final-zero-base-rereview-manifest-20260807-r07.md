# Stage12-N1-2 physical zero-base full re-review manifest R07

> **BUNDLE_ID:** `PC-N1-2-FINAL-ZERO-BASE-REREVIEW-20260807-R07`
>
> **COMPLETED_THROUGH:** `Stage12-N1-3h`
>
> **SOURCE_SNAPSHOT_COMMIT:** `1cc47f22be84e2924671294c88f2613d7cbafcd4`
>
> **SOURCE_LEDGER_SHA256:** `9e8fe78faca3e30f9bfa9db9ef5cfd7b5c33187e94889c46aa3ab83b011c6f98`
>
> **HISTORICAL_PROVENANCE_COMMIT:** `8d6910e8e68145e474f92716460a1cc6f384ecf1`
>
> **FINAL_DOCUMENT:** `docs/stage12-n1-2-final-r06-zero-base.md`
>
> **REVIEW_PAGE:** `review/PC-N1-2-FINAL-ZERO-BASE-REREVIEW-20260807-R07.html`
>
> **THEOREM_STATUS:** `FULL_ZERO_BASE_REREVIEW_CANDIDATE_WITH_PROVENANCE`

## Mandatory source check

Confirm that the physical page contains `CHECKPOINT=START_OF_MAIN`, all eight embedded sources, `CHECKPOINT=END_OF_MAIN`, and the exact end marker. If not, return `UNREADABLE_SOURCE`. If any fixed value differs, return `STALE_SOURCE`.

```text
BUNDLE_ID=PC-N1-2-FINAL-ZERO-BASE-REREVIEW-20260807-R07
COMPLETED_THROUGH=Stage12-N1-3h
SOURCE_SNAPSHOT_COMMIT=1cc47f22be84e2924671294c88f2613d7cbafcd4
SOURCE_LEDGER_SHA256=9e8fe78faca3e30f9bfa9db9ef5cfd7b5c33187e94889c46aa3ab83b011c6f98
HISTORICAL_PROVENANCE_COMMIT=8d6910e8e68145e474f92716460a1cc6f384ecf1
FINAL_DOCUMENT=docs/stage12-n1-2-final-r06-zero-base.md
THEOREM_STATUS=FULL_ZERO_BASE_REREVIEW_CANDIDATE_WITH_PROVENANCE
END_OF_BUNDLE=PC-N1-2-FINAL-ZERO-BASE-REREVIEW-20260807-R07
```

The identifier check is only an integrity check. Mathematical closure must be based on the proof content.

## Review target

Audit from zero the displayed asymptotic for the primitive oriented count:

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
=
\frac{\eta}{12\pi^2}B(\log B)^3.
\]

The physical page now includes:

1. the active proof through Stage12-N1-3g;
2. the complete Stage12-N1-3a rectangle-error derivation;
3. historical derivations of `G`, its divisor expansion, `kappa`, primitive-first `A_{r,s}`, `beta`, `gamma`, and `eta`;
4. Stage12-N1-3h, which supplies the vertical-growth and radial lower-boundary calculations.

Do not rely on external repository files or previous review decisions.

## Precedence rules that must be audited

```text
ACTIVE_CURRENT_PROOF=docs/stage12-n1-2-final-r05.md
ACTIVE_RECTANGLE_DERIVATION=Stage12-N1-3a Lemma 3a.1
ACTIVE_VERTICAL_AND_RADIAL_BOUNDARY=Stage12-N1-3h
2F_FORMAL_RAW_ASYMPTOTIC=PROVENANCE_ONLY
2K_OLD_FIXED_CIRCLE_REMAINDER=SUPERSEDED_BY_3B_AND_3E
2K_OLD_SHALLOW_BOUND=SUPERSEDED_BY_3G
3A_OLD_RETAINED_MIN_RS_APPLICATION=SUPERSEDED_BY_3F
SUPERSEDED_FIXED_BC_KERNEL=NOT_USED
```

A historical derivation may be used for identities and local factors only where it has not been superseded. Treat any silent reuse of an explicitly superseded estimate as a material error.

## Required full-review questions

### A. Object, multiplicity and primitive-first identities

1. Does the embedded 2b source derive the raw parameter sum and multiplicity `G(hrs)-1` consistently with the current definition sheet?
2. Does the embedded 2e source give the exact divisor expansion of `G`, including the pairwise-coprime allocation of prime powers?
3. Are orientation, parity, height, coprimality, floors and the global Möbius relation exact?
4. Does the embedded 2j source derive `A_{r,s}(m)`, its nonnegative formula, and `beta`, `gamma`, `g` without an omitted case?

### B. Provenance and supersession

5. Are the identities imported from 2b, 2e, 2f, 2j and 2k sufficient to remove the previously external origins of `G`, `beta`, `eta`, and `kappa`?
6. Is every obsolete error estimate in 2k actually replaced by 3b/3e/3g in the active proof?
7. Is 2f used only for its local-factor and formal-main-term derivations, not as an unsupported raw asymptotic theorem?
8. Is the old `retained => min(R,S)>=S0` application in 3a inactive, with radial application performed only by 3f's defined core?

### C. Rectangle asymptotic

9. In Stage12-N1-3a Lemma 3a.1, is the convolution formula with the coprime cross coefficients exact?
10. Does the four-region coefficient split, together with the weighted absolute norm, rigorously give
    \[
    R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}?
    \]
11. Are the small-coefficient Selberg--Delange remainders uniform in the exact ranges used?
12. When applied only on the 3f core, does the corrected rectangle error sum to `o((log B)^3)` after kernel partial summation?

### D. Fixed-height retained and shallow sectors

13. Is the corrected fixed-circle remainder obtained without the invalid extraction of `omega(X)`?
14. Does the `W` outer average close the retained contribution?
15. Does 3g derive, rather than merely assert,
    \[
    \mathcal S_{\rm sh}(B)\ll B(\log B)^{5/2}=o(B(\log B)^3)?
    \]
16. Are the fixed-height retained/shallow split and radial core/wing split kept logically distinct?

### E. Selberg--Delange hypotheses

17. Are the `z=1` and `z=2` factorizations correct?
18. Is `J_beta` locally uniformly absolutely convergent and bounded in the required closed subregions?
19. Does Stage12-N1-3h correctly obtain polynomial vertical growth for `L(s,chi_4)` from absolute convergence, the functional equation, Stirling and Phragmen--Lindelof?
20. Is the resulting vertical growth of `H_beta=L(s,chi_4)J_beta(s)` sufficient for the precise finite-order Selberg--Delange form used?

### F. Local factors and constants

21. Does the embedded 2f source correctly derive the three-variable local factor and `kappa` from the multiplicity expansion?
22. Do 2j/2k correctly derive the two-variable weights and `eta`, after excluding superseded error claims?
23. Is the active coprime local-factor calculation exact for odd primes and at 2, with
    \[
    D_{\lambda,2}(s_1,s_2)
    =2+\frac{x}{1-x}+\frac{y}{1-y}?
    \]
24. Does the active calculation give
    \[
    C_\lambda^{(0)}=\frac8{\pi^2}\eta,
    \qquad
    \eta=\pi\kappa?
    \]

### G. Radial transfer and lower limits

25. Is the Stieltjes/partial-summation passage from rectangles to the radial region valid without the superseded fixed-`(b,c)` lemma?
26. Does Stage12-N1-3h correctly describe the exact angular interval imposed by `x,y>=1`?
27. Is the removed angular mass bounded by `O((log t)^2/t)`, so that its radial integral is `O(1)`?
28. Do the full-angle cross terms contribute at most `O((log B)^2)` and hence preserve
    \[
    I(B)=\frac\pi{48}(\log B)^3+O((\log B)^2)?
    \]
29. Are the discrete and continuous small-coordinate wings lower order?
30. Are parity, orientation, the odd--odd annulus, diagonal, arc and all boundaries included without a missing factor?

### H. Final error budget and scope

31. Are all retained, shallow, rectangle, wing, floor, endpoint, annulus, diagonal and lower-log terms collectively `o(B(log B)^3)`?
32. Does the complete factor ledger produce exactly `1/12`?
33. Is any superseded statement still used implicitly?
34. Does the theorem concern only the defined primitive oriented count and nothing stronger?
35. Is this physical bundle now sufficient for a zero-base review without following an external source reference?

## Required output

Classify findings as `FATAL`, `MAJOR`, `MINOR`, or `CLARIFICATION`, and return one of:

- `CLOSED`
- `REPAIRABLE`
- `OPEN`
- `STALE_SOURCE`
- `UNREADABLE_SOURCE`

```text
VERDICT=
FATAL=
MAJOR=
MINOR=
CLARIFICATION=
PHYSICAL_SELF_CONTAINMENT=
PROVENANCE_SOURCES=
COUNTING_DEFINITION=
PRIMITIVE_FIRST_IDENTITY=
RECTANGLE_DERIVATION=
RECTANGLE_CORE_APPLICATION=
FIXED_CIRCLE_RETAINED=
FIXED_HEIGHT_SHALLOW=
SELBERG_DELANGE_INPUTS=
VERTICAL_GROWTH=
LOCAL_FACTOR_IDENTITY=
RADIAL_LOWER_LIMIT=
SMALL_COORDINATE_WING=
RADIAL_TRANSFER=
FINAL_ERROR_BUDGET=
CONSTANT_NORMALIZATION=
SUPERSEDED_STATEMENT_USED=
NEW_CENTRAL_GAP=
THEOREM_STATUS=
```

A review that checks only the newly added material is not a completed R07 review. The complete chain must be reconsidered from zero.
