# EXP10 — E8 combination: EXP06 redesign machinery applied to φ384 (row384 / EXP05 averaging)

Date: 2026-11-21. Lab copies only; the repo clone was not modified.
Verifier: the repo's own `verify_average384.py` (7-char lab copy from
EXP05; original 3-char copy from repo row384), python-flint 0.9.0,
scipy/HiGHS for the LPs. Every number below marked CERTIFIED is the
output of a full verifier run (score/moment asserts + `check_exterior`
subdivision); LP and float-scan numbers are labeled diagnostic.

## Headline results (all CERTIFIED)

**7-char average (c_Cl ≥ 3), EXP05's problem.** EXP05 certified, with
the baseline weights: score ≥ 0.0911527542420397790…, bands
Re > 0.64 / 0.68, gap 9/20 = 0.45 (ε = thr = 9/100, M_thr = 100).

- Same bands, much bigger gap: **gap 234983/40000 = 5.874575**
  (candH: ε = 13/400, score 0.0868448982333700496…), and with EXP09's
  extended tail composed (see §5) **gap 58983/10000 = 5.8983**.
  At ε = 3/50 the redesigned weights even raise the score above
  baseline: 0.1053145701385321485…, gap 101787/20000 = 5.08935 (candE).
- Strictly narrower bands (Pareto frontier, all at ε = 3/50,
  M_thr = 9919/100): Re > **0.65 / 0.70** (gap 2.5326), 0.65/0.71
  (2.22285), 0.65/0.72 (1.8816), 0.65/0.73 (1.51935), 0.65/0.74
  (1.13085; **1.17465** with the extended tail), 0.65/0.76 (0.3066),
  0.655/0.70 (1.4406), 0.655/0.71 (1.1466), 0.66/0.70 (0.33285).
  So the Re φ < 0 patch that capped EXP05 is NOT immovable: it was a
  property of the baseline weights, not of the fixture family.

**3-char average (c_Cl ≥ 2), row384's original problem.** row384
certified score ≥ 0.0523946411808995256…, Ω2 = Re > 0.63/0.63,
gap 7/10 (ε = 7/200, thr = 1/25, M_thr = 100).

- Same bands: score **0.0709356122343433040…**, **gap
  39571/10000 = 3.9571** (candR3, ε = 7/200); with extended tail
  **79653/20000 = 3.98265**.
- Narrowed Ω2: Re > **0.64 / 0.66** (candS3, gap 4053/2500 = 1.6212)
  and Re > **0.64 / 0.68** (candT3, gap 26649/20000 = 1.33245;
  **13653/10000 = 1.3653** with extended tail), both at ε = 9/200.

This sharpens the necessary conditions only. −30 is NOT closed; no
exclusion is claimed; ZF2-type zero-freeness in the (now smaller)
regions is still the missing input, and per EXP03 literature regions
reach only Re ≈ 0.99986 at these heights. The hard core c_Cl ∈ {1, 2}
is untouched in kind — but the c_Cl = 2 necessary region is now
Ω2′ = {Re > 0.64, |Im| ∈ (0.26, 0.77)} ∪ {Re > 0.68, |Im| ∈ (1.03, 1.46)}.

## Method

Pipeline as in EXP06, rebuilt for φ384 (lengths 91/10, 23/10, 23/10,
7/20, 7/20; 21 shifts 0, 1/40, 2/5, …, 4; σ = 7/5; tail_height 12):

1. **Affine score.** score(b) = C + Σ g_j b_j with C =
   0.11074897511696911, extracted with the verifier's own interval
   arithmetic (unit modulation per shift). cc=7: g_0 = +0.16799,
   g_1 = +0.15875 (both positive, unlike row383; g_1 − g_0 ≈ −0.0092,
   so the (0, 1/40) pair is a nearly score-free dial), g_2…g_20 from
   −1.267 to −3.452. Affine reconstruction of the certified baseline
   score matched to 7e-14 (cc=7) and 8e-14 (cc=3); tail-ratio formula
   ratio = K·Σ|b_j|/(12−a_j)^10, K = 2267688.800850699, matched to
   1e-16 (baseline ratio 0.0003518820231463842 — never binding).
   Moment is weight-independent: 99.186384435239… at LIMIT = 1982760.
2. **Float φ evaluator** (`phi_float384.py`): Re φ = Σ b_j R_j with
   φ0(z) = Π sinc(i z ℓ/2)²/norm, norm = 0.09678649236566852.
   Validated against the verifier's `transform_series` at 20 points
   (including the patch (0.5, 0.435): −19.919871709796, matching
   EXP07): worst error 3.3e-14.
3. **Grid** (`build_grid384.py`): the verifier's required region —
   gaps u ∈ [0, 1/2] over t ∈ [0.1, 0.26] ∪ [0.77, 1.03] ∪ [1.46, 12],
   bands u ∈ [0, c] over their t-ranges — 164,322 points after the
   densification forced by candF's failure (§4): t-step 0.01 to
   t = 6 in gap C, u-step 0.002 for u ∈ [0.4, 0.5], a surgical patch
   at (u ∈ [0.44, 0.5], t ∈ [2.40, 2.76]), band refinement u-step
   0.001 / t-step 0.0025 around both patches.
4. **Two LP forms** (variables b_1…b_20, b_0 = 1 − Σb_j, baseline
   sign pattern fixed; dominance ≥ 0.001; Σ|b| ≤ cap; tail ratio
   ≤ ε/2; maximize the affine score):
   - *Relative form* (EXP06-style): g_new(p) ≥ max(FLOOR,
     g_base(p; ε) − SLACK) on band points, g_base − SLACK on gap
     points, SLACK = 2e-4.
   - *Absolute form*: g_new(p) ≥ FLOOR everywhere on the required
     region. This is the form that unlocked everything: EXP05's
     weights were chosen for ε = 7/200 at bands (0.13, 0.13), so the
     relative form's ~44k near-baseline constraints chained the LP
     to them; the baseline's own min g on the region is only
     5.6e-4 (the (1/2, 12) corner, where g ≈ εW is
     weight-independent), so an absolute FLOOR = 2e-4 is honest and
     far less restrictive. FLOOR > 0 everywhere honors EXP08's
     warning (no pure-relative form is used for any certified
     candidate's binding region in the relative ladder either:
     FLOOR = 5e-4–2e-3 there).
5. **Rationalize** to a 1e-6 grid (b_0 absorbs rounding, Σb = 1
   exact, dominance > 0 as rationals), score_threshold = largest
   multiple of 1/20000 ≤ score_rat − 1.5e-4, M_thr = 9919/100
   (or 9846/100 with the extended tail), run the FULL verifier.
   Scripts: `lp384.py`, `ladder384.py`, `ladder384_cc3.py`.

## Certified ladder — 7-char, bands (0.64, 0.68) fixed

| cand | form | ε | score_lower | gap |
|---|---|---|---|---|
| EXP05 cand6 | — | 9/100 | 0.0911527542420397790… | 0.45 |
| threshold-only | — | 9/100 | (same weights) | 399/625 = 0.6384 |
| A | rel, FLOOR 2e-3 | 17/200 | 0.0917895993315136435… | 1.18685 |
| B | rel, FLOOR 2e-3 | 41/500 | 0.0917693764254253096… | 1.48442 |
| C | rel, FLOOR 5e-4 | 2/25 | 0.0917906473924825513… | 1.6828 |
| D | rel, FLOOR 5e-4 | 79/1000 | 0.0915256796856751032… | 1.75574 |
| E | abs, FLOOR 2e-4, cap 7.75 | 3/50 | 0.1053145701385321485… | 5.08935 |
| F2 | abs, cap 10 | 9/200 | 0.0953452879343421846… | 5.5272 |
| G | abs, cap 10 | 7/200 | 0.0887335826832529251… | 5.8261 |
| H | abs, cap 10 | 13/400 | 0.0868448982333700496… | **5.874575** |
| H + tail 10⁷ | M_thr 9846/100 | 13/400 | (same) | **5.8983** |

Relative-form frontier: LP infeasible at ε ≤ 0.0785 with FLOOR
5e-4; the binding point is the band-1 top edge (u = 0.140,
t = 0.652) — candC's weights give g = −0.000947 there at ε = 0.078.
Absolute-form frontier at fixed bands: LP infeasible at ε = 0.030
(FLOOR 2e-4 exceeds εW ≈ 1.85e-4 at the (1/2, 12) corner and Re φ
there cannot compensate); Σ|b| cap saturates at ≈ 10.62 (score gain
from cap 7.75 → 12 is only +0.0004).

## Certified narrowings — 7-char (all absolute form, ε = 3/50)

| cand | Re > band 1 | Re > band 2 | score_lower | gap |
|---|---|---|---|---|
| I | 0.65 | 0.70 | 0.0809853402153557264… | 2.5326 |
| J | 0.65 | 0.71 | 0.0780426086460922117… | 2.22285 |
| L | 0.65 | 0.72 | 0.0747734103857591131… | 1.8816 |
| N | 0.65 | 0.73 | 0.0713010519774564418… | 1.51935 |
| P | 0.65 | 0.74 | 0.0676380087610141290… | 1.13085 |
| P + tail 10⁷ | 0.65 | 0.74 | (same) | **1.17465** |
| Q | 0.65 | 0.76 | 0.0597584127561295693… | 0.3066 |
| K | 0.655 | 0.70 | 0.0705978317440849167… | 1.4406 |
| O | 0.655 | 0.71 | 0.0677965353864395439… | 1.1466 |
| M | 0.66 | 0.70 | 0.0600124249324879445… | 0.33285 |

LP diagnostics (not certificates): band 1 caps at c1 ≈ 0.16–0.165
((0.17, ·) has LP score below the ε-viability line at both ε = 0.06
and ε = 0.09; (0.16, 0.21) LP gap is only 0.0425 — not pursued);
band 2 reaches c2 = 0.26 at c1 = 0.15 with score to spare.

## Certified — 3-char (absolute form; row384's original fixture)

| cand | ε | Re > bands | score_lower | gap |
|---|---|---|---|---|
| row384 | 7/200 | 0.63 / 0.63 | 0.0523946411808995256… | 0.7 |
| R3 | 7/200 | 0.63 / 0.63 | 0.0709356122343433040… | 3.9571 |
| R3 + tail 10⁷ | 7/200 | 0.63 / 0.63 | (same) | **3.98265** |
| S3 | 9/200 | 0.64 / 0.66 | 0.0581099534412508669… | 1.6212 |
| T3 | 9/200 | 0.64 / 0.68 | 0.0553661986583767691… | 1.33245 |
| T3 + tail 10⁷ | 9/200 | 0.64 / 0.68 | (same) | **1.3653** |

## §5. Extended tail composition

The average verifier's `load_primes` / `prime_bounds` log-derivative
code is identical to row383's, so EXP09's extension composes with
exactly the same four edits EXP09 used (LIMIT = 10⁷; len/sum asserts
663909 / 664336; pinned SHA of tail_roots_independent.csv →
e5c2e2be…; the extended CSV in place). Validation run (EXP05
narrowed fixture, baseline weights): score identical to the last
digit (0.0911527542420397790…), moment 99.186384435239… →
**98.4550015213825703…** — digit-for-digit EXP09's row383 value, as
expected since the score sum only involves log p < support (all
already tabulated) and the moment's log_deriv is f- and
character-count-independent. No new proof obligations: the table is
EXP09's, byte-validated there against the stored original on its
whole range. Gains are the small M_thr effect only (9919/100 →
9846/100): +0.024 (candH), +0.044 (candP), +0.026 (R3), +0.033 (T3).

## Failures and dead ends (recorded with the same care)

- **candF (absolute, ε = 9/200, cap 10, coarse grid)**: full
  verifier FAILED at depth 42, u → 1/2, t ≈ 2.5788 (gap C). Cause:
  the coarse grid (t-step 0.05 above t = 2.5) missed a narrow dip;
  on the densified grid the same weights show min gap g = −5.7e-6
  at (0.5, 2.575). The densified grid (164,322 pts) is now standard;
  candF2 (same ε, dense grid) passes. Lesson recorded: in gap C the
  u = 1/2 edge needs t-step ≤ 0.01 and u-step ≤ 0.002 near the edge.
- **First LP version falsely infeasible everywhere**: the capped
  gap-floor form made thousands of large-t rows equality-tight
  (thr = g_base exactly) and HiGHS reported infeasibility although
  the baseline is feasible in exact arithmetic (max violation
  2e-19). Fixed by the uniform-slack gap form; the episode is why
  every "INFEASIBLE" above was cross-checked against a feasible
  point or a floor/slack scan before being recorded as a frontier.
- **Relative form cannot raise bands at all**: with FLOOR = 0 the
  band threshold max(0, g_base − slack) still demands g_new ≥ 0 on
  the extension strip, and even c1 = 0.145 was LP-infeasible in
  relative form — the ~44k relative constraints elsewhere block the
  strip repair. The absolute form (which drops the relative
  constraints, keeping only FLOOR = 2e-4) is what moves the patch.
  Interpretation: EXP05's "genuine patch" is genuine *for the
  baseline weights*; within the fixture family the patch onset is
  weight-dependent and moves by up to +0.02 (band 1) / +0.08
  (band 2) in u.
- **Slack-funded score is not used**: at ε = 0.078, raising SLACK to
  1e-3 lifts the LP score to 0.0937 — the EXP08 unsoundness
  direction; no certified candidate relies on it (all use
  SLACK = 2e-4 with FLOOR ≥ 2e-4 absolute in the binding regions,
  and the full verifier adjudicated each one).

## Reproduction

Each `cand-*/` dir is self-contained (verifier + inputs + redesigned
`fixture384.json` + `result.json` or `err.txt`); run
`/tmp/flintenv/bin/python verify_average384.py` inside it (~15 s).
`tail10m/` and `tail10m3/` hold the LIMIT = 10⁷ verifier copies and
the composed fixtures (`fixture_H.json`, `fixture_P.json`,
`fixture_R.json`, `fixture_T.json` — copy to `fixture384.json` and
run). Champion fixtures are also copied to the top level:
`fixture_7char_bestgap_10m.json` (candH + tail),
`fixture_7char_narrowed_10m.json` (candP + tail),
`fixture_3char_bestgap_10m.json` (candR3 + tail),
`fixture_3char_narrowed_10m.json` (candT3 + tail), with matching
`result_*_10m.json`. LP scripts: `phi_float384.py`,
`build_grid384.py`, `lp384.py`, `ladder384.py`, `ladder384_cc3.py`,
gradients in `base7/gradient384_cc7.json`,
`base3/gradient384_cc3.json`.

## Verdict on E8

The combination works, on both targets, beyond the brief's success
criteria: for c_Cl ≥ 3 the certified gap at EXP05's bands grows
0.45 → 5.8983 (×13.1) and the bands narrow to 0.65/0.76 at the
extreme (gap 0.3066) with a full Pareto frontier between; for
c_Cl ≥ 2 the gap grows 0.7 → 3.98265 (×5.7) and Ω2 narrows to
0.64/0.68. The remaining obstruction is unchanged in kind: these
are necessary conditions whose bite requires zero-freeness in the
regions (ZF2/ZF3), which per EXP03 is ~0.37 of Re away from
literature. E8 is DONE. Do not re-run this LP family at these
shifts/lengths expecting more: the fixed-band ε-frontier
(0.0325 at FLOOR 2e-4), the Σ|b| saturation (≈10.6), and the band-1
cap (c1 ≈ 0.16) are all mapped.
