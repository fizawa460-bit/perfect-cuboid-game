# Stage12-N1-2b〜2k adversarial review manifest

> **DOCUMENT_ID:** `PC-N1-REVIEW-2B-2K-20260806-1545-JST`
>
> **COMPLETED_THROUGH:** `Stage12-N1-2k`
>
> **SOURCE_SNAPSHOT_COMMIT:** `5ae4057e8a83a23d7accee5b5145290e2a65e198`
>
> **LAST_SOURCE_DOCUMENT:** `docs/stage12-n1-2k-final-remainder.md`
>
> **SERIES_STATUS:** `Derivation stopped after 2k; adversarial review pending`
>
> **CREATED_AT_JST:** `2026-08-06 15:45`

## Mandatory handshake before review

Before performing any mathematical assessment, output these four lines exactly as read from this document:

```text
DOCUMENT_ID=PC-N1-REVIEW-2B-2K-20260806-1545-JST
COMPLETED_THROUGH=Stage12-N1-2k
SOURCE_SNAPSHOT_COMMIT=5ae4057e8a83a23d7accee5b5145290e2a65e198
LAST_SOURCE_DOCUMENT=docs/stage12-n1-2k-final-remainder.md
```

If you cannot reproduce them exactly, stop. You are reading a stale or different document and your review must not be used.

## Review target

Review the complete logical chain from Stage12-N1-2b through Stage12-N1-2k. Do not assess only the final 2k memo. Check definitions, reindexing, local factors, parity restrictions, Möbius inversion, lattice-point estimates, exponent budgets, smoothing, endpoint terms, pole orders, Euler-product identities, and the exact scope of the counted object.

The current candidate conclusion is

```text
C_prim(B) ~ (kappa/(12*pi)) * B * (log B)^3.
```

The review must determine whether this conclusion is fully supported by the cited standard theorems and the preceding reductions. It must not infer anything about existence or nonexistence of a perfect cuboid.

## Immutable source documents

All links below are pinned to the same immutable snapshot commit.

1. [Stage12-N1-2b: multiplicative-weight shared-prime correction](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/5ae4057e8a83a23d7accee5b5145290e2a65e198/docs/stage12-n1-2b-average.md)
2. [Stage12-N1-2c: Gao–Zhao compatibility audit](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/5ae4057e8a83a23d7accee5b5145290e2a65e198/docs/stage12-n1-2c-gao-zhao.md)
3. [Stage12-N1-2d: modular hyperbola audit](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/5ae4057e8a83a23d7accee5b5145290e2a65e198/docs/stage12-n1-2d-modular-hyperbola.md)
4. [Stage12-N1-2e: divisor/dyadic expansion](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/5ae4057e8a83a23d7accee5b5145290e2a65e198/docs/stage12-n1-2e-divisor-dyadic.md)
5. [Stage12-N1-2f: formal main term and local densities](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/5ae4057e8a83a23d7accee5b5145290e2a65e198/docs/stage12-n1-2f-main-term.md)
6. [Stage12-N1-2g: uniform lattice-error audit](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/5ae4057e8a83a23d7accee5b5145290e2a65e198/docs/stage12-n1-2g-uniform-error.md)
7. [Stage12-N1-2h: Poisson and modulus split](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/5ae4057e8a83a23d7accee5b5145290e2a65e198/docs/stage12-n1-2h-poisson-split.md)
8. [Stage12-N1-2i: Ramanujan/exponent-pair budget](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/5ae4057e8a83a23d7accee5b5145290e2a65e198/docs/stage12-n1-2i-exponent-budget.md)
9. [Stage12-N1-2j: primitive-first boundary layers](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/5ae4057e8a83a23d7accee5b5145290e2a65e198/docs/stage12-n1-2j-boundary-layers.md)
10. [Stage12-N1-2k: final averaged remainder and Euler constant](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/5ae4057e8a83a23d7accee5b5145290e2a65e198/docs/stage12-n1-2k-final-remainder.md)

## Audit artifacts

Each stage has a sibling JSON report and deterministic audit script in the same snapshot. A reviewer disputing a finite identity or numerical diagnostic should inspect the corresponding `data/*.json` and `scripts/audit_*.py` files rather than relying only on prose.

The final artifacts are:

- [2k JSON report](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/5ae4057e8a83a23d7accee5b5145290e2a65e198/data/final_remainder_stage12_n1_2k_report.json)
- [2k audit script](https://github.com/fizawa460-bit/perfect-cuboid-game/blob/5ae4057e8a83a23d7accee5b5145290e2a65e198/scripts/audit_final_remainder_stage12_n1_2k.py)

## Required adversarial questions

1. Does every reindexing preserve parity, coprimality, orientation, and multiplicity exactly?
2. Is the primitive-first convolution formula valid at all endpoints, including the `m=1` correction?
3. Does the cited fixed-domain primitive lattice-point theorem imply the exact parity-restricted estimate used in 2k, with the stated remainder after finite Euler correction?
4. Is the average of `G(rs)H_abs(rs)` genuinely bounded with the claimed pole order and sufficient uniformity?
5. Are the core/wing estimates in 2i transferred to the beta weights without losing a logarithmic degree?
6. Does the multiple-sum theorem apply to the precise nonrectangular ordered domain and smoothing used here?
7. Are all shallow, boundary, axis-frequency, large-divisor, smoothing, and endpoint contributions `o(B(log B)^3)` after the final primitive-first formulation?
8. Is `eta=pi*kappa` correct prime by prime, including the archimedean and 2-adic factors?
9. Is the final counted object exactly the Stage12-N1-2 primitive oriented count, with repeated-side contribution zero, and not a stronger exact-multiplicity claim?
10. Identify the earliest unsupported implication. Do not merely say that the argument is plausible.

## Review output format

Return one of:

- `CLOSED`: no material gap found; list all theorem hypotheses checked.
- `REPAIRABLE`: one or more explicit gaps found that appear repairable; give the exact lemma required.
- `OPEN`: a central step is unsupported or false; identify the earliest failing stage.
- `STALE_SOURCE`: the mandatory handshake did not match.

A generic response such as “the approach looks correct” is not a completed review.

## Legacy memo warning

`docs/face-ratio-geometry-research.md` begins with an older date and contains earlier project-wide material. It may remain useful as background, but it is not sufficient as the sole source for reviewing Stage12-N1-2b〜2k. Use this versioned manifest and its commit-pinned links.
