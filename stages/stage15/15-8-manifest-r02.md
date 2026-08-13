# Stage15-8 self-contained review manifest R02

```text
REVIEW_BUNDLE_ID=STAGE15-FINAL-SELF-CONTAINED-20260813-R02
SOURCE_STAGE15_BUNDLE=STAGE15-FINAL-SELF-CONTAINED-20260813-R01
HTML_PATH=stages/stage15/stage15-final-self-contained.html
HTML_GIT_BLOB_SHA=5ebfd8e9e3b37c91a5cce509bfca708c1c34c618
SELF_CONTAINMENT_STANDARD=SELF_CONTAINED_REVIEW_STANDARD_V1
SELF_CONTAINMENT_STANDARD_PATH=docs/self-contained-review-standard.md
SELF_CONTAINMENT_STANDARD_GIT_BLOB_SHA=1b7c6fcb3a982dc81f0fa78e2deda01c0d95cb45
STATUS=AUDIT_CANDIDATE
NEW_MATHEMATICS=false
STAGE15_6_REOPENED=false
SUMMARY_ONLY=false
INTERNAL_LOAD_BEARING_PROOFS_EMBEDDED=true
EXTERNAL_THEOREM_WORKING_FORMS_STATED=true
EXTERNAL_HYPOTHESES_MAPPED=true
REMOTE_REQUIRED_ASSETS=false
FRESH_AUDIT_REQUIRED=true
MERGE_ALLOWED=false
```

## Repair boundary

R02 repairs the R01 presentation-level self-containment defect identified by comparison with the active Stage12 R09, Stage13 R07, and Stage14 R06 review bundles. It changes no Stage15 theorem, exponent, population, cutoff, route status, or literature claim.

The repair transcribes the already-certified internal load-bearing arguments that R01 had compressed to assertions or repository provenance:

- Stage15-2a shared-edge surface, four `A1` singularities, `Bl_4(P1 x P1)` toric resolution, Picard rank, and anticanonical morphism;
- Stage15-2b exact `R` anticanonical height, full shared-edge toric count, incidence identity, geometrically integral degree-two third-face cover, thin-set subtraction, and `M_2(B)` asymptotic;
- Stage15-4 primitive normalization `G`, multiplicity-one inverse toric reconstruction, `G^2 R^2=4AB`, and squareclass equivalence;
- Stage15-6dy split-prime divisor geometry, residue-class ledger, p-adic parity probabilities, and exact `rho_p`;
- Stage15-6dz fixed-prime and fixed-finite-set same-measure refinement, CRT/Tamagawa tensor, and ordered-limit zero-density implication.

The completed Stage14 numerator theorem remains a frozen upstream theorem interface and is not re-proved. Published external theorems remain external at the stated theorem level, but R02 prints their working forms, hypothesis maps, and uniformity limits.

## Source ledger

| Role | Path | R02 treatment |
|---|---|---|
| geometry | `stages/stage15/15-2a/result.md` | proof-complete transcription of load-bearing steps |
| ambient theorem | `stages/stage15/15-2b/result.md` | proof-complete transcription of load-bearing steps |
| finite evidence | `stages/stage15/15-3/result.md` | diagnostic summary only |
| survivor normal form | `stages/stage15/15-4/result.md` | proof-complete transcription of load-bearing steps |
| upstream quantitative theorem | `stages/stage14/final.md` | frozen exact interface |
| quantitative comparison | `stages/stage15/15-5/result.md` | direct ratio implication |
| local acceptance | `stages/stage15/15-6dy/result.md` | proof-complete transcription |
| fixed-S refinement | `stages/stage15/15-6dz/result.md` | proof-complete transcription |
| causal closeout | `stages/stage15/15-6-final.md` | theorem boundary and non-claims |
| final Stage15 synthesis | `stages/stage15/final.md`, `stages/stage15/manifest-r01.md` | theorem-species and provenance lock |
| review standard | `docs/self-contained-review-standard.md` | project-wide authoritative definition |

## External theorem boundary

External proofs are intentionally not embedded:

1. Batyrev–Tschinkel toric anticanonical counting;
2. Huang fixed adelic-neighbourhood Manin–Peyre equidistribution/counting;
3. Browning–Loughran thin-subset zero density.

R02 embeds the object identification, exact height/measure adapter, hypothesis checks, local restrictions, and quantifier limitations needed to apply those results.

## Audit gate

A fresh `Stage15-8-audit` must treat `docs/self-contained-review-standard.md` as part of the audit contract and verify that R02 satisfies it. Deterministic CI checks structure and offline constraints only.
