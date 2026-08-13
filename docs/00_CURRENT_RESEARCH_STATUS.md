# CURRENT RESEARCH STATUS

```text
CURRENT_STAGE=Stage16-60-SUBMITTED
STAGE12_STATUS=FROZEN_R09
STAGE13_STATUS=CLOSED_R07
STAGE14_STATUS=CLOSED_R06
STAGE15_STATUS=CLOSED_R02_REVIEW_FROZEN
STAGE15_6_STATUS=CLOSED
STAGE15_7_STATUS=R01_MERGED_AUDIT_STATUS_NOT_CANONICALLY_RECORDED
STAGE15_8_STATUS=CLOSED_R02
STAGE15_FINAL_REVIEW=review/STAGE15-FINAL-SELF-CONTAINED-20260813-R02.html
STAGE16_STATUS=OPEN_CHECKPOINT_60_SUBMITTED
STAGE16_CONTROLLER=stages/stage16/16-controller.json
STAGE16_CURRENT_RESULT=stages/stage16/16-60/result.md
STAGE16_SUPPORTING_DATA=stages/stage16/16-20/counts.csv
STAGE16_LAST_AUDIT=stages/stage16/16-50/audit.md
STAGE16_NEXT_CHECKPOINT=70
NEXT_EXPECTED_COMMAND=Stage16-audit
NEXT_RESEARCH_PROGRAM=docs/stage16-28-population-roadmap.md
STAGE16_28_EXECUTION_TEMPLATE=docs/stage16-28-execution-controller-template.md
SELF_CONTAINED_REVIEW_STANDARD=docs/self-contained-review-standard.md
```

## Canonical completed-stage sources

| Stage | Final source | Active external review | Manifest |
|---|---|---|---|
| 12 | `stages/stage12/final.md` | `review/PC-N1-2-FINAL-SELF-CONTAINED-20260807-R09.html` | `stages/stage12/manifest-r09.md` |
| 13 | `stages/stage13/final.md` | `review/STAGE13-FINAL-SELF-CONTAINED-20260810-R07.html` | `stages/stage13/manifest-r07.md` |
| 14 | `stages/stage14/final.md` | `review/STAGE14-FINAL-SELF-CONTAINED-20260813-R06.html` | `stages/stage14/manifest-r06.md` |
| 15 | `stages/stage15/final.md` (merged R01 synthesis; pre-audit status preserved) | `review/STAGE15-FINAL-SELF-CONTAINED-20260813-R02.html` | `stages/stage15/15-8-manifest-r02.md` |

Historical task results, superseded reviews, working roadmaps, and completed workflows remain stage-local/archive provenance.

## Project-wide self-contained review rule

The authoritative definition is:

`docs/self-contained-review-standard.md`

Future final review artifacts must use the Stage12 R09 / Stage13 R07 / Stage14 R06 / Stage15 R02 standard: internal load-bearing mathematics is embedded in proof-complete form; published external theorems may remain external only with an exact working contract, hypothesis map, measure/height adapter, and quantifier limitations.

A repository path is provenance, not a substitute for a load-bearing proof.

The top-level `review/` directory is reserved for active rendered review artifacts; the reusable standard/template remains under `docs/`.

## Stage14 reusable interfaces

```text
docs/stage14-arsenal.md
docs/stage14-arsenal-index.md
docs/stage14-arsenal-stage15-map.md
```

These remain reusable historical interfaces. Stage14 data, scripts, literature, and archive provenance retain their stable paths.

## Stage15-6 closed result

Stage15-6 is closed after its audited final closeout.

Its independent causal theorem is

\[
N_2(B)/M_2(B)\to0,
\]

proved from the fixed-prime local Gaussian-squareclass sieve on the same primitive/canonical exactly-two `R<=B` physical measure.

Stage15-6 did **not** prove an internal fixed `delta>0` or `sigma>0`. Effective growing-modulus adelic/local sieving and stronger global quantitative mechanisms are external future gates, not unfinished Stage15-6 routes.

Canonical Stage15-6 closeout: `stages/stage15/15-6-final.md`.

## Stage15-7 audit-status provenance

PR #887 merged the Stage15 R01 synthesis bundle. The canonical R01 files still explicitly preserve their pre-audit state:

- `stages/stage15/final.md`: `Status: fresh-audit candidate`;
- `stages/stage15/manifest-r01.md`: `Status: candidate pending fresh Stage15-7-audit`.

No canonical Stage15-7 audit/closeout record exists in the repository. Therefore the repository does **not** describe Stage15-7 as `CLOSED_R01` and does not invent a retrospective audit record.

This historical status does not keep Stage15 mathematics open. Stage15-8 independently fresh-audited the R02 proof-facing review against the merged R01 synthesis plus immediate canonical mathematical sources, with `AUDIT_VERDICT=PASS` and `INTERNAL_ROUTE_REMAINS=false`.

## Stage15-8 frozen review closeout

PR #888 merged the R02 self-containment repair as commit

`b83dd74be283dc58b3ce5c6862d21e105a9fa3f9`.

The frozen human-facing review is:

`review/STAGE15-FINAL-SELF-CONTAINED-20260813-R02.html`

It is byte-identical to `stages/stage15/stage15-final-self-contained.html` and follows `SELF_CONTAINED_REVIEW_STANDARD_V1`.

The fresh Stage15-8 audit returned PASS, no internal route remains, Codex audit was not required, and merge was allowed. Stage15-8 is therefore closed. See:

- `stages/stage15/15-8-manifest-r02.md`
- `stages/stage15/15-8-closeout.md`
- `stages/stage15/15-8-controller.json`

## Current operation

Stage15 is closed and must not be reopened merely to strengthen a closed theorem or repair historical audit-status wording.

Stage16-10 and Stage16-20 are certified. Stage16-30 has passed fresh audit and proves

\[
M_1(B)\asymp B^2\log B,
\qquad
U(B)=\frac{\pi}{36\zeta(3)}B^3+O(B^2),
\qquad
\frac{M_1(B)}{U(B)}\asymp\frac{\log B}{B}\to0.
\]

Stage16-40 passed fresh audit and freezes the sharp upper-bound ledger

\[
M_1(B)\ll B^2\log B.
\]

Stage16-50 has now also passed fresh audit. Its canonical audit record is:

- `stages/stage16/16-50/audit.md`

The certified sharp construction gives

\[
M_1(B)\gg B^2\log B.
\]

AR-039 remains a narrower integral-space-diagonal regression subset only; on that subset `R=d` exactly and its weaker `B^{1/2}` lower bound is not used for the Stage16 ambient exponent.

Stage16-60 now submits the causal decomposition. If `H_1(B)` denotes the same primitive canonical `R<=B` population with at least one integral face, then the face-union upper bound and the audited exactly-one lower bound give

\[
H_1(B)\asymp M_1(B)\asymp B^2\log B.
\]

The proved `\log(B)/B` thinning order is assigned to the one-face Pythagorean dimension drop: an unrestricted two-edge pair of order `B^2` is replaced by scaled primitive Pythagorean faces of order `B\log B`, while the third edge remains free at order `B`. The logarithm comes from the harmonic scale sum.

At this resolution, primitivity and canonicalization do not change the power/log order, and the exactly-one mask is order-neutral relative to at-least-one. Stage16-60 does **not** prove a global overlap little-`o` theorem or a limiting ratio between exactly-one and at-least-one populations. Space-diagonal arithmetic is not charged at Stage16, and finite directional `ab/ac/bc` imbalance remains diagnostic only.

Canonical Stage16-60 submission:

- `stages/stage16/16-60/result.md`

Because checkpoint 60 contains a new causal synthesis, `ADVANCE_ALLOWED=false` until a fresh `Stage16-audit`. Checkpoint 70 intrinsic-status / closeout verdict must not be treated as certified before that audit.
