# CURRENT RESEARCH STATUS

> **DOCUMENT_ID:** `PC-N1-CURRENT-20260806-1645-JST`
>
> **COMPLETED_THROUGH:** `Stage12-N1-2k`
>
> **SOURCE_SNAPSHOT_COMMIT:** `8d6910e8e68145e474f92716460a1cc6f384ecf1`
>
> **SERIES_STATUS:** `Stage12-N1-2 derivation stopped; adversarial proof-chain review pending`
>
> **LATEST_SELF_CONTAINED_REVIEW_PAGE:** `review/PC-N1-2-PROOF-REVIEW-20260806-R02.html`
>
> **LATEST_BUNDLE_ID:** `PC-N1-2-PROOF-REVIEW-20260806-1645-R02`

## Review source rule

Use the uniquely named, self-contained HTML review page above. It embeds all of the following in one page:

- Stage12-N1-2 and Stage12-N1-2b through 2k research documents
- all corresponding deterministic JSON reports
- all corresponding audit scripts
- the mandatory adversarial-review protocol

R01 remains an immutable historical artifact. It contained the full source payload, but some AI readability extractors retained only the HTML `<main>` element and therefore omitted the R01 handshake that was placed in outer `<header>` and `<footer>` elements. R02 keeps the same embedded research payload and repeats the complete handshake four times inside `<main>`.

The earlier link-only manifest also remains a historical version record, but it is superseded for actual review because some external AI browsers cannot follow its immutable GitHub links.

## Mandatory handshake

A reviewer must not begin the mathematical review until it has repeated these values from the R02 review page:

```text
BUNDLE_ID=PC-N1-2-PROOF-REVIEW-20260806-1645-R02
COMPLETED_THROUGH=Stage12-N1-2k
SOURCE_SNAPSHOT_COMMIT=8d6910e8e68145e474f92716460a1cc6f384ecf1
CONTENT_SHA256=201cad458d172e0939e5508b78e6e06abe894d908390f0c1b54c51a16e63d586
LAST_SOURCE_DOCUMENT=docs/stage12-n1-2k-final-remainder.md
END_OF_BUNDLE=PC-N1-2-PROOF-REVIEW-20260806-1645-R02
```

The reviewer should also see:

```text
PAGE_STRUCTURE=ALL_HANDSHAKES_INSIDE_MAIN_R02
CHECKPOINT=START_OF_MAIN
CHECKPOINT=END_OF_MAIN
```

If the values differ, neither checkpoint is visible, or the final embedded Stage12-N1-2k audit script is unavailable, the reviewer must return `UNREADABLE_SOURCE` and must not review from memory, cached summaries, or external search snippets.

## Current conclusion level

The Stage12-N1-2 series has reached the candidate leading asymptotic

```text
C_prim(B) ~ (kappa/(12*pi)) * B * (log B)^3
```

at the standard-theorem-application level. This is not yet described as an independently peer-reviewed publication proof. The immediate next action is adversarial review of the included Stage12-N1-2 through 2k proof chain, not automatic continuation to Stage12-N1-2l and not yet a whole-project consistency review.

## Version policy

- Do not overwrite or reuse a review-page filename.
- Do not give reviewers a mutable branch URL as the sole source.
- For every material correction or delivery-structure correction, create a new page filename and new `BUNDLE_ID`.
- `CONTENT_SHA256` identifies the embedded canonical research payload; it remains unchanged in R02 because the mathematical documents, JSON reports, and audit scripts are unchanged from R01.
- The GitHub Pages URL for each versioned file is intended to remain content-stable after merge.
