# CURRENT RESEARCH STATUS

```text
CURRENT_STAGE=Stage17-60-AUDIT-PASS
STAGE12_STATUS=FROZEN_R09
STAGE13_STATUS=CLOSED_R07
STAGE14_STATUS=CLOSED_R06
STAGE15_STATUS=CLOSED_R02_REVIEW_FROZEN
STAGE15_6_STATUS=CLOSED
STAGE15_7_STATUS=R01_MERGED_AUDIT_STATUS_NOT_CANONICALLY_RECORDED
STAGE15_8_STATUS=CLOSED_R02
STAGE15_FINAL_REVIEW=review/STAGE15-FINAL-SELF-CONTAINED-20260813-R02.html
STAGE16_STATUS=CLOSED_R01_AUDIT_PASS
STAGE16_CONTROLLER=stages/stage16/16-controller.json
STAGE16_FINAL_BUNDLE=stages/stage16/final.md
STAGE16_MANIFEST=stages/stage16/manifest-r01.md
STAGE16_FINAL_AUDIT=stages/stage16/16-70/audit.md
STAGE16_SUPPORTING_DATA=stages/stage16/16-20/counts.csv
STAGE17_STATUS=OPEN_CHECKPOINT_60_AUDIT_PASS
STAGE17_CONTROLLER=stages/stage17/17-controller.json
STAGE17_CURRENT_RESULT=stages/stage17/17-60/result.md
STAGE17_CURRENT_AUDIT=stages/stage17/17-60/audit.md
STAGE17_CURRENT_DATA=stages/stage17/17-20/counts.csv
STAGE17_CURRENT_ENUMERATOR=stages/stage17/17-20/enumerate.py
STAGE17_NEXT_CHECKPOINT=70
NEXT_EXPECTED_COMMAND=Stage17-main-batch
NEXT_RESEARCH_PROGRAM=docs/stage16-28-population-roadmap.md
STAGE16_28_EXECUTION_TEMPLATE=docs/stage16-28-execution-controller-template.md
STAGE16_28_WRITE_POLICY=docs/stage16-28-github-write-policy.md
SELF_CONTAINED_REVIEW_STANDARD=docs/self-contained-review-standard.md
```

## Canonical completed-stage sources

| Stage | Final source | Active external review | Manifest |
|---|---|---|---|
| 12 | `stages/stage12/final.md` | `review/PC-N1-2-FINAL-SELF-CONTAINED-20260807-R09.html` | `stages/stage12/manifest-r09.md` |
| 13 | `stages/stage13/final.md` | `review/STAGE13-FINAL-SELF-CONTAINED-20260810-R07.html` | `stages/stage13/manifest-r07.md` |
| 14 | `stages/stage14/final.md` | `review/STAGE14-FINAL-SELF-CONTAINED-20260813-R06.html` | `stages/stage14/manifest-r06.md` |
| 15 | `stages/stage15/final.md` (merged R01 synthesis; pre-audit status preserved) | `review/STAGE15-FINAL-SELF-CONTAINED-20260813-R02.html` | `stages/stage15/15-8-manifest-r02.md` |
| 16 | `stages/stage16/final.md` | none required beyond the fresh Stage16 audit lane | `stages/stage16/manifest-r01.md` |

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

## Stage16 frozen closeout

Stage16 checkpoint 70 and the repaired R01 self-contained bundle passed fresh audit. The canonical audit record is:

- `stages/stage16/16-70/audit.md`

The frozen Stage16 population law is
\[
M_1(B)\asymp B^2\log B,
\qquad
U(B)=\frac{\pi}{36\zeta(3)}B^3+O(B^2),
\qquad
\frac{M_1(B)}{U(B)}\asymp\frac{\log B}{B}\to0.
\]
For the same primitive canonical `R<=B` population with at least one integral face,
\[
H_1(B)\asymp M_1(B)\asymp B^2\log B.
\]
The polynomial exponent `2` and logarithmic power `1` are intrinsic at the proved Theta resolution. No leading constant, overlap little-o theorem, directional limiting law, Stage16-to-Stage17 survival law, or perfect-cuboid conclusion is included in Stage16.

## Current operation

Stage17-60 has passed fresh audit. The Stage17 population remains the same primitive canonical exactly-one population with integral space diagonal and common cutoff `R<=B`; on target objects `R=d` exactly.

For the unique integral face write

`x^2+y^2=p^2`.

The new Stage17 requirement that the space diagonal be integral is exactly

`p^2+z^2=d^2`

for the complementary edge `z`. Thus the audited structural mechanism is a second Pythagorean extension sharing the face diagonal `p`.

The audited laws

`M_1(B) asymp B^2 log B`

and

`N_1(B) ~ (kappa/(24*pi)) B(log B)^3`

give the net survival law

`N_1(B)/M_1(B) asymp (log B)^2/B`.

At theorem scale this is one lost polynomial power of `B`, with `(log B)^2` net compensation. The logarithms are not split into independent probabilistic costs.

Canonical ordering, global primitivity, exactly-one multiplicity and `R<=B` are already charged in Stage16. The identity `d=R` is not a new cost. Stage13's extra-face overlap theorem is lower order, so exactly-one subtraction is not the leading Stage17 mechanism. AR-039 remains an explicit survivor family rather than the source of the full asymptotic.

Stage16S remains the separate ambient control for space-diagonal integrality. Stage17-60 does not decide whether the observed cost is intrinsic, independent, correlated, or interaction-dependent; that comparison is reserved for Stage21 once the necessary Stage16S baseline is audited.

Canonical Stage17-60 records:

- `stages/stage17/17-60/result.md`
- `stages/stage17/17-60/audit.md`
- `stages/stage17/17-controller.json`

Checkpoint 60 is merge-allowed. The next unresolved checkpoint is `Stage17-70` (bounded maximal synthesis / intrinsic-status closeout), entered through `Stage17-main-batch` after this audited checkpoint is merged.
