# CURRENT RESEARCH STATUS

```text
CURRENT_STAGE=Stage15-8
STAGE12_STATUS=FROZEN_R09
STAGE13_STATUS=CLOSED_R07
STAGE14_STATUS=CLOSED_R06
STAGE15_STATUS=FINAL_REVIEW_ACTIVE
STAGE15_6_STATUS=CLOSED
STAGE15_7_STATUS=R01_MERGED_AUDIT_STATUS_NOT_CANONICALLY_RECORDED
STAGE15_8_TARGET=SELF_CONTAINED_HTML_HOSTILE_REVIEW_AND_FREEZE
SELF_CONTAINED_REVIEW_STANDARD=docs/self-contained-review-standard.md
```

## Canonical completed-stage sources

| Stage | Final source | Active external review | Manifest |
|---|---|---|---|
| 12 | `stages/stage12/final.md` | `review/PC-N1-2-FINAL-SELF-CONTAINED-20260807-R09.html` | `stages/stage12/manifest-r09.md` |
| 13 | `stages/stage13/final.md` | `review/STAGE13-FINAL-SELF-CONTAINED-20260810-R07.html` | `stages/stage13/manifest-r07.md` |
| 14 | `stages/stage14/final.md` | `review/STAGE14-FINAL-SELF-CONTAINED-20260813-R06.html` | `stages/stage14/manifest-r06.md` |

Historical task results, superseded reviews, working roadmaps, and completed
workflows are archive-only provenance under the corresponding stage.

## Project-wide self-contained review rule

The authoritative definition is:

`docs/self-contained-review-standard.md`

Future final review artifacts must use the Stage12 R09 / Stage13 R07 / Stage14 R06
standard: internal load-bearing mathematics is embedded in proof-complete form;
published external theorems may remain external only with an exact working contract,
hypothesis map, measure/height adapter, and quantifier limitations.

A repository path is provenance, not a substitute for a load-bearing proof.

The top-level `review/` directory is reserved for active rendered review artifacts;
the reusable standard/template remains under `docs/`.

## Stage14 interfaces protected for Stage15

```text
docs/stage14-arsenal.md
docs/stage14-arsenal-index.md
docs/stage14-arsenal-stage15-map.md
```

Stage14 data, scripts, and literature keep stable paths. Historical task-result
citations in the arsenal point to `stages/stage14/archive/tasks/`.

## Stage15-6 closed result

Stage15-6 is closed after its audited final closeout.

Its independent causal theorem is

N_2(B)/M_2(B) -> 0,

proved from the fixed-prime local Gaussian-squareclass sieve on the same
primitive/canonical exactly-two `R<=B` physical measure.

Stage15-6 did **not** prove an internal fixed `delta>0` or `sigma>0`. Effective
growing-modulus adelic/local sieving and stronger global quantitative mechanisms
are classified as external future gates, not unfinished Stage15-6 routes.

Canonical Stage15-6 closeout: `stages/stage15/15-6-final.md`.

## Stage15-7 audit-status provenance

PR #887 merged the Stage15 R01 synthesis bundle. However the canonical R01 files
still explicitly record the pre-audit state:

- `stages/stage15/final.md`: `Status: fresh-audit candidate`;
- `stages/stage15/manifest-r01.md`: `Status: candidate pending fresh Stage15-7-audit`.

No canonical Stage15-7 audit record or controller closeout was committed with that
merge. Therefore repository state must **not** describe R01 as canonically audited
or Stage15-7 as `CLOSED_R01`.

Stage15-8 does not repair this by inventing a retrospective Stage15-7 closeout.
Instead it treats the merged R01 synthesis as a source candidate and performs its
own fresh hostile audit of the proof-facing R02 HTML against the immediate
canonical mathematical sources. This provenance correction opens no new
Stage15-7 mathematical route and does not reopen Stage15-6.

## Active operation

Stage15-8 is the active presentation/preservation gate: build and hostile-review
one offline self-contained HTML representation of the Stage15 theorem content
without changing the mathematics and without assuming an unrecorded Stage15-7
`AUDITED/CLOSED_R01` state.

The active Stage15-8 review repair uses
`SELF_CONTAINED_REVIEW_STANDARD_V1`; a fresh Stage15-8 audit is required before
merge/freeze.
