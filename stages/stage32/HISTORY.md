# Stage32 history and reusable evidence index

Purpose: compactly record what is reusable, superseded, and currently open. Live machine state is always `stages/stage32/controller.json`.

## Current boundary — post-21bl effectivity preflight

Current continuation: PR #1471, branch `stage32-post21bl-effectivity-preflight`, based on merged #1470 / `main@20f5bd1e2e71cf96f8a30e677640666807a71729`.

The former representative state `SAT 0 / UNSAT 55 / UNKNOWN 1` is superseded. The audited current representative state is:

`SAT 1 / UNSAT 55 / UNKNOWN 0`.

The former lone UNKNOWN `g1-d186` was resolved at 21bl by an exact 59D integer SAT witness and fresh replay audit. The witness was then transferred exactly to one retained integral Picard64 class and independently re-audited.

Reusable current facts:

- target: `g1-d186`, genus `1`, degree `186`, `e=266`, `a=592`;
- 21bl witness SHA256: `1a131595c87cf9c5d54ef97dba62261eeb3dda7bb92a5a9fa62c280f46bc4137`;
- 21bl evidence canonical: `ac88fb355252750e6afdc10cbb54abec24babbad57c25090c017f9a55ac93a44`;
- 21bl fresh audit canonical: `4c8ba2456d163963a7ca28d3ce72d3556460e7bee0d46ee676b891e94e9ba264`;
- post-21bl Picard64 adapter canonical: `ef3f21e4166d4bfcacce3503213b0a72afee5f5002ab7145de01fc9c54d47038`;
- post-21bl fresh Picard64 audit canonical: `170611441f83113b27fa1b9b60eeaac31746a10938bb6ee5751f32a450f466d8`;
- Picard-coordinate SHA256: `0fcbe0c9cdf894a95704bcaf55536290fc2daa736387169c891e8262f2c565a7`;
- all140-pairing SHA256: `1968dba54ebe2082c6ed07203ea9e4118460f60c32c60d46292bc73dc6bdf961`;
- all 140 known-curve/exceptional pairings are integral and nonnegative;
- exact self-intersection `C^2=858`;
- `K_S.C=d=186`.

These facts close the representative integer/Picard semantic adapter only. They do **not** prove effectivity or an actual curve.

The exact post-21bl gap is now deliberately split:

1. `FULL178_NUMERICAL_CENSUS = OPEN_SEPARATE`;
2. `EFFECTIVITY_ACTUAL_LOW_GENUS_CURVE = OPEN_PRIMARY`.

`stages/stage32/32-21/post-21bl-effectivity-gap-separation.json` records that the representative already passes the historical Testa–Stoll numerical-effectivity **necessary** filter (nonnegative intersection with all known curves), but no sufficient curve-existence, irreducibility, normalization-genus-one, unibranch, or multibranch certificate is present.

`stages/stage32/32-21/post-21bl-genus-defect-preflight.json` gives the current exact geometric burden:

- adjunction arithmetic genus: `p_a=(858+186)/2+1=523`;
- target normalization genus: `1`;
- required normalization genus defect for a reduced irreducible genus-one realization: `522`;
- exceptional pairing count `48`, sum `266`, min `0`, max `16`, zero count `4`;
- no identity between that exceptional profile and the required delta invariant is claimed.

The next meaningful datum is therefore a source-locked geometric adapter that constructs such an integral low-genus curve or excludes one. Repeating numerical Picard/integrality/nonnegative-pairing filters is not progress.

## Generation map

| Unit | Role | Status | Reuse rule |
|---|---|---|---|
| 32-19 | brute-force scaling limit / hard-tail diagnosis | CLOSED_RETROSPECTIVE | Historical scaling telemetry only; do not revive blind node-ceiling escalation. |
| 32-20 | symbolic prefix compression / exact indexed terminal family | CLOSED_CHECKPOINTED | Exact count/rank/unrank interface remains reusable; do not materialize the full family without a new exact need. |
| 32-21 | numerical Picard / integer-fiber / effectivity boundary | ACTIVE | Reuse only audited locks below; current live problem is effectivity sufficiency, with FULL178 kept separate. |

## 32-19 / 32-20 reusable checkpoints

32-19 established the brute-force scaling wall. Gen38 had 52 continuations from73 inputs and exact finite raw remaining-node upper bound `4555530975806418`.

32-20 replaced blind enumeration by an exact indexed terminal family:

- status `PASS_PREFIX_DFS_REPARAMETERIZED_TO_EXACT_INDEXED_TERMINAL_FAMILY`;
- exact symbolic terminal count `688101306360803751427719294`;
- exact unrank/inverse-rank interface available.

Detailed pre-21ad history: `stages/stage32/controller-history-through-32-21ad.json`.

## 32-21aa through 21ad

Audited reusable package:

- 21aa anti-fixed penalties: 16384 projection classes, 16383 positive, one zero, minimum positive `1/572`;
- 21ab quotient map: free subgroup order128, quotient cosets128;
- 21ac cheap exact anti-fixed coset predicate: 127 positive-minimum cosets, one zero;
- aa→ac fresh audit canonical `5dfd1087d7d1c20baa3475e05e1768edbb9e8f063b20d01ca467a6725b657f1e`;
- 21ad FULL178 census: 178 rows, 2,018,569 prior slices, 679,337 continuous-KKT survivors, **0 additional anti-fixed prunes**;
- 21ad boundary audit canonical `1f2e61ef29cf6000b8cc98906a5dcf3f2a4d15a7b405be2e40ef9c0de3bfab0e`.

Interpretation: 21ac is mathematically valid but numerically dominated on that exact FULL178 population. Do not rerun the same census without a semantic change.

## Post-21ad representative chain

The deterministic56 fixed-projection sample is representative-only, never FULL178 credit.

Important repair/supersession rules:

- 21ba interval upper-search interface is buggy and permanently superseded;
- 21bb/21bc/21bd are reusable only through the independent 21be rescue;
- the first 21bg run with wrong r42 domain is invalid/no credit;
- corrected 21bg and later exact locks are reusable.

Exact coordinate-compression chain:

- 21be restored exact r51;
- 21bf exact r49;
- corrected 21bg exact r42;
- 21bh exact r54;
- 21bi exact r57;
- 21bj exact r56;
- 21bk exact r20.

Every single-coordinate step left all3234 survivor-prism triples open. The finite anti-loop contract then forced 21bl joint integer closure rather than another coordinate. That joint step found the audited integer SAT witness described above. Do not restart the coordinate-compression chain or run the 3234 scaleout merely because it exists.

## Current receiver semantics

Stage29 receiver lock:

`R29-LG2-EFF = EffectiveCurveCertificationForSurvivingNumericalPicardClasses`.

Its parent kernel wall is a symmetry-reduced, effectivity-aware, multibranch Picard-lattice enumeration through the audited genus0 degree<=176 / genus1 degree<=192 window. The current d186 genus1 representative lies inside that window, but numerical Picard survival is not receiver closure.

## Permanent firewalls

- `UNKNOWN != UNSAT`.
- representative sample != FULL178 numerical credit.
- rational SAT != integer SAT.
- fixed-projection UNSAT != slice UNSAT.
- integral Picard class != effective curve existence.
- nonnegative intersections with known curves are a necessary filter, not effectivity sufficiency.
- effectivity/divisor existence != integral low-genus carrier without irreducibility/normalization/branch semantics.
- no theorem, receiver, route, or perfect-cuboid credit without its explicit audited adapter.

For the exact live branch, PR, current item, and next datum, read `stages/stage32/controller.json`.
