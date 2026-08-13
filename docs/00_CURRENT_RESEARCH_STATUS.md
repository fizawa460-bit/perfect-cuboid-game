# CURRENT RESEARCH STATUS

```text
CURRENT_STAGE=Stage18-20-SUBMITTED
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
STAGE17_STATUS=CLOSED_R01_AUDIT_PASS
STAGE17_CONTROLLER=stages/stage17/17-controller.json
STAGE17_CURRENT_RESULT=stages/stage17/17-70/result.md
STAGE17_CURRENT_AUDIT=stages/stage17/17-70/audit.md
STAGE17_FINAL_BUNDLE=stages/stage17/final.md
STAGE17_MANIFEST=stages/stage17/manifest-r01.md
STAGE17_CURRENT_DATA=stages/stage17/17-20/counts.csv
STAGE17_CURRENT_ENUMERATOR=stages/stage17/17-20/enumerate.py
STAGE17_AUDIT_PERSISTENCE=COMMITTED
STAGE17_NEXT_CHECKPOINT=
STAGE17_NEXT_STAGE=Stage18
STAGE18_STATUS=OPEN_CHECKPOINT_20_SUBMITTED
STAGE18_CONTROLLER=stages/stage18/18-controller.json
STAGE18_CURRENT_RESULT=stages/stage18/18-20/result.md
STAGE18_CURRENT_AUDIT=stages/stage18/18-10/audit.md
STAGE18_CURRENT_DATA=stages/stage18/18-20/counts.csv
STAGE18_CURRENT_ENUMERATOR=stages/stage18/18-20/enumerate.py
STAGE18_AUDIT_PERSISTENCE=PENDING
STAGE18_NEXT_CHECKPOINT=30
NEXT_EXPECTED_COMMAND=Stage18-audit
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
| 17 | `stages/stage17/final.md` | none required beyond the fresh Stage17 audit lane | `stages/stage17/manifest-r01.md` |

Historical task results, superseded reviews, working roadmaps, and completed workflows remain stage-local/archive provenance.

## Project-wide self-contained review rule

The authoritative definition is:

`docs/self-contained-review-standard.md`

Future final review artifacts must use the Stage12 R09 / Stage13 R07 / Stage14 R06 / Stage15 R02 standard: internal load-bearing mathematics is embedded in proof-complete form; published external theorems may remain external only with an exact working contract, hypothesis map, measure/height adapter, and quantifier limitations.

A completed earlier stage may be imported as a frozen theorem interface when population, cutoff, multiplicity, measure and quantifiers match; any new adapter must be proved in the receiving stage.

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

## Stage17 frozen closeout

Stage17 checkpoint 70 and the repaired R01 self-contained interface bundle passed fresh re-audit. The canonical audit record is:

- `stages/stage17/17-70/audit.md`

The frozen Stage17 population theorem is
\[
N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3.
\]
With the frozen Stage16 source law,
\[
\frac{N_1(B)}{M_1(B)}\asymp\frac{(\log B)^2}{B}\to0.
\]
No leading constant is claimed for this ratio because Stage16 has no certified leading constant for `M_1(B)`.

If `H_{1,d}(B)` counts the same primitive canonical integral-space-diagonal population with at least one integral face, Stage13 pair-overlap control yields
\[
H_{1,d}(B)\sim N_1(B),
\qquad
\frac{N_1(B)}{H_{1,d}(B)}\to1.
\]
Thus exactly-one is asymptotically dominant among integral-space cuboids having at least one integral face. This does not assume perfect-cuboid nonexistence.

The Stage16-to-Stage17 structural restriction is the second Pythagorean extension

```text
x^2+y^2=p^2
p^2+z^2=d^2
```

with shared face diagonal `p`. This identifies the new arithmetic predicate but does not assert probabilistic independence.

The final bundle explicitly certifies both frozen upstream interfaces under `SELF_CONTAINED_REVIEW_STANDARD_V1`. In particular the Stage16 denominator interface records population, cutoff, multiplicity, measure and quantifier compatibility, and the bundle lock records `UPSTREAM_INTERFACES_EXACT=true`.

Stage16S remains the separate ambient control for deciding intrinsic/independent/correlated/interaction-dependent space-diagonal cost at Stage21. Stage16S is parallel and does not block Stage17 closure.

The prior Stage17-70 BLOCKED audit is retained as historical provenance inside the canonical audit record; the repaired re-audit PASS supersedes it.

```text
STAGE_STATUS=CLOSED
AUDIT_VERDICT=PASS
AUDIT_PERSISTENCE_STATUS=COMMITTED
ADVANCE_ALLOWED=true
MERGE_ALLOWED=true
NEXT_STAGE=Stage18
SELF_CONTAINED_BUNDLE_REQUIRED=YES
SELF_CONTAINED_BUNDLE=stages/stage17/final.md
ARSENAL_PROMOTION_REQUIRED=NO
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
```

## Current operation

Stage18-10 population contract has passed fresh audit. Stage18-20 now freezes an exact finite census for that same population.

The deterministic shared-edge enumerator gives

```text
B:   50  100  200  400  800  1200  1600  2000
M2:  16   56  172  494  1347 2350  3536  4812
```

The optimized shared-edge construction and an independent direct canonical-triple brute-force enumerator agree as sets through `B=200`. The frozen `counts.csv` SHA-256 is `7873368267bbc21e5fd9ec6437d30e84a646ec4ddb14a50746575f59ac932e5a`.

These counts are `COMPUTED` evidence only. They neither prove nor modify the frozen Stage15 theorem `M_2(B) ~ C_{M_2} B(log B)^5`. No ratio, causal, independence, Stage16->Stage18 transition, or perfect-cuboid claim is added at checkpoint20.

Canonical Stage18-20 submission:

- `stages/stage18/18-20/result.md`
- `stages/stage18/18-20/counts.csv`
- `stages/stage18/18-20/enumerate.py`
- `stages/stage18/18-controller.json`

```text
AUDIT_STATUS=PENDING
AUDIT_PERSISTENCE_STATUS=PENDING
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
NEXT_CHECKPOINT=30
NEXT_EXPECTED_COMMAND=Stage18-audit
```
