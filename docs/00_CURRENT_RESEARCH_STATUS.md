# CURRENT RESEARCH STATUS

```text
CURRENT_STAGE=Stage16-50-SUBMITTED
STAGE12_STATUS=FROZEN_R09
STAGE13_STATUS=CLOSED_R07
STAGE14_STATUS=CLOSED_R06
STAGE15_STATUS=CLOSED_R02_REVIEW_FROZEN
STAGE15_6_STATUS=CLOSED
STAGE15_7_STATUS=R01_MERGED_AUDIT_STATUS_NOT_CANONICALLY_RECORDED
STAGE15_8_STATUS=CLOSED_R02
STAGE15_FINAL_REVIEW=review/STAGE15-FINAL-SELF-CONTAINED-20260813-R02.html
STAGE16_STATUS=OPEN_CHECKPOINT_50_SUBMITTED
STAGE16_CONTROLLER=stages/stage16/16-controller.json
STAGE16_CURRENT_RESULT=stages/stage16/16-50/result.md
STAGE16_SUPPORTING_DATA=stages/stage16/16-20/counts.csv
STAGE16_LAST_AUDIT=stages/stage16/16-40/audit.md
STAGE16_NEXT_CHECKPOINT=60
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

The authoritative definition is `docs/self-contained-review-standard.md`.

Future final review artifacts must use the Stage12 R09 / Stage13 R07 / Stage14 R06 / Stage15 R02 standard: internal load-bearing mathematics is embedded in proof-complete form; published external theorems may remain external only with an exact working contract, hypothesis map, measure/height adapter, and quantifier limitations.

A repository path is provenance, not a substitute for a load-bearing proof. The top-level `review/` directory is reserved for active rendered review artifacts; the reusable standard/template remains under `docs/`.

## Stage14 reusable interfaces

```text
docs/stage14-arsenal.md
docs/stage14-arsenal-index.md
docs/stage14-arsenal-stage15-map.md
```

These remain reusable historical interfaces. Stage14 data, scripts, literature, and archive provenance retain their stable paths.

## Stage15 closed status

Stage15 is closed. Its frozen human-facing review is `review/STAGE15-FINAL-SELF-CONTAINED-20260813-R02.html`. Stage15-6 is closed with the independent causal theorem `N_2(B)/M_2(B)->0`, while Stage15-8 independently fresh-audited the R02 proof-facing review. Historical Stage15-7 audit-status wording remains preserved rather than retrospectively rewritten.

## Current operation

Stage16-10 and Stage16-20 are certified. Stage16-30 passed fresh audit and proved
\[
M_1(B)\asymp B^2\log B,
\qquad
U(B)=\frac{\pi}{36\zeta(3)}B^3+O(B^2),
\qquad
\frac{M_1(B)}{U(B)}\asymp\frac{\log B}{B}\to0.
\]

Stage16-40 has now also passed fresh audit. Its canonical audit record is

- `stages/stage16/16-40/audit.md`

and it freezes the sharp upper-bound ledger
\[
M_1(B)\ll B^2\log B.
\]

Stage16-50 now submits the lower-bound / construction ledger. The strongest certified construction is the already-audited Stage16-30 family, which gives
\[
M_1(B)\gg B^2\log B.
\]
It uses a primitive Pythagorean face, harmonic face scale, a positive-density third-edge interval, global coprimality, and deletion of the two accidental-square sets. This is order-sharp against checkpoint 40 and adds no stronger theorem than Stage16-30.

AR-039 is also adapted, but only as a narrower regression subset. Its primitive exactly-one family additionally has integral space diagonal; because `R=d` exactly on that subset, its historical `d<=B` cutoff equals Stage16 `R<=B`. Hence it legally yields the weaker `M_1(B)>>B^(1/2)` lower bound, but it is not used for the Stage16 ambient exponent or sharp lower bound.

Canonical Stage16-50 submission:

- `stages/stage16/16-50/result.md`

Checkpoint 50 is newly submitted, so `ADVANCE_ALLOWED=false` until a fresh `Stage16-audit`. Checkpoint 60 causal decomposition must not be treated as certified before that audit.
