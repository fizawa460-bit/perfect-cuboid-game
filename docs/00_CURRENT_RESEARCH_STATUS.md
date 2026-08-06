# CURRENT RESEARCH STATUS

> **DOCUMENT_ID:** `PC-N1-CURRENT-20260806-1545-JST`
>
> **COMPLETED_THROUGH:** `Stage12-N1-2k`
>
> **SOURCE_SNAPSHOT_COMMIT:** `5ae4057e8a83a23d7accee5b5145290e2a65e198`
>
> **SERIES_STATUS:** `Stage12-N1-2 derivation stopped; adversarial review pending`
>
> **LATEST_VERSIONED_REVIEW_MEMO:** `docs/review/stage12-n1-2b-to-2k-review-manifest-20260806-1545.md`

## Stale-document rule

An AI or reviewer must not begin the mathematical review until it has repeated the following three values exactly:

```text
DOCUMENT_ID=PC-N1-REVIEW-2B-2K-20260806-1545-JST
COMPLETED_THROUGH=Stage12-N1-2k
SOURCE_SNAPSHOT_COMMIT=5ae4057e8a83a23d7accee5b5145290e2a65e198
```

If any value differs, the reviewer is reading an old branch, an old cached page, or a different memo. Discard that review and reopen the versioned review memo.

## Current conclusion level

The Stage12-N1-2 series has reached the candidate leading asymptotic

```text
C_prim(B) ~ (kappa/(12*pi)) * B * (log B)^3
```

at the standard-theorem-application level. This is not yet described as an independently peer-reviewed publication proof. The next action is adversarial review of the complete chain from Stage12-N1-2b through Stage12-N1-2k, not automatic continuation to Stage12-N1-2l.

## URL policy

- Do not give reviewers a mutable branch URL as the sole source.
- Use the uniquely named review memo.
- The review memo links every source document to the immutable source snapshot commit.
- For every new completed stage or material correction, create a new versioned memo with a new `DOCUMENT_ID`; do not silently reuse the old review URL.
