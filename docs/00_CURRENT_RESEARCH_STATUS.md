# CURRENT RESEARCH STATUS

> **DOCUMENT_ID:** `PC-N1-CURRENT-20260806-1612-JST`
>
> **COMPLETED_THROUGH:** `Stage12-N1-2k`
>
> **SOURCE_SNAPSHOT_COMMIT:** `0e8bbc6e745ddf6d1f7c0ba3b21bb328a1fcc4d2`
>
> **SERIES_STATUS:** `Stage12-N1-2 derivation stopped; adversarial proof-chain review pending`
>
> **LATEST_SELF_CONTAINED_REVIEW_PAGE:** `review/PC-N1-2-PROOF-REVIEW-20260806-R01.html`
>
> **LATEST_BUNDLE_ID:** `PC-N1-2-PROOF-REVIEW-20260806-1612-R01`

## Review source rule

Use the uniquely named, self-contained HTML review page above. It embeds all of the following in one page:

- Stage12-N1-2 and Stage12-N1-2b through 2k research documents
- all corresponding deterministic JSON reports
- all corresponding audit scripts
- the mandatory adversarial-review protocol

The earlier link-only manifest remains a historical version record, but it is superseded for actual review because some external AI browsers cannot follow its immutable GitHub links.

## Mandatory handshake

A reviewer must not begin the mathematical review until it has repeated these values from the review page:

```text
BUNDLE_ID=PC-N1-2-PROOF-REVIEW-20260806-1612-R01
COMPLETED_THROUGH=Stage12-N1-2k
SOURCE_SNAPSHOT_COMMIT=0e8bbc6e745ddf6d1f7c0ba3b21bb328a1fcc4d2
CONTENT_SHA256=201cad458d172e0939e5508b78e6e06abe894d908390f0c1b54c51a16e63d586
LAST_SOURCE_DOCUMENT=docs/stage12-n1-2k-final-remainder.md
END_OF_BUNDLE=PC-N1-2-PROOF-REVIEW-20260806-1612-R01
```

If any header value differs, or the footer `END_OF_BUNDLE` is unavailable, the reviewer must return `UNREADABLE_SOURCE` and must not review from memory, cached summaries, or external search snippets.

## Current conclusion level

The Stage12-N1-2 series has reached the candidate leading asymptotic

```text
C_prim(B) ~ (kappa/(12*pi)) * B * (log B)^3
```

at the standard-theorem-application level. This is not yet described as an independently peer-reviewed publication proof. The immediate next action is adversarial review of the included Stage12-N1-2 through 2k proof chain, not automatic continuation to Stage12-N1-2l and not yet a whole-project consistency review.

## Version policy

- Do not overwrite or reuse the current review-page filename.
- Do not give reviewers a mutable branch URL as the sole source.
- For every material correction, create a new page filename, new `BUNDLE_ID`, new `CONTENT_SHA256`, and new source snapshot.
- The GitHub Pages URL for the current file is intended to remain content-stable after merge because this versioned file will not be edited again.
