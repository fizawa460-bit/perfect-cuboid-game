# EXP11 — E9: absolute-floor LP applied to φ383 band narrowing (row383, c_Cl ≥ 1)

Date: 2026-11-21. Lab copies only; the repo clone was not modified.
Verifier: the repo's own `verify_spectral383.py`, python-flint 0.9.0
(venv /tmp/flintenv), scipy/HiGHS for the LPs. Every number marked
CERTIFIED is the output of a full verifier run (score/moment asserts
+ `check_exterior` subdivision); LP and float-scan numbers are
labeled diagnostic.

## Headline results (all CERTIFIED)

**The bands move.** EXP06's "band raising is DEAD in this family" was
an artifact of its relative LP form (plus a too-coarse grid) — the
same artifact EXP10 diagnosed on φ384. With the absolute-floor form,
the c_Cl ≥ 1 necessary-zero bands of row383 narrow, at ε = 29/4000:

| cand | Re > band 1 | Re > band 2 | Re > band 3 | score_lower | gap |
|---|---|---|---|---|---|
| row383 baseline | 0.562 | 0.572 | 0.605 | 0.0098858898430937020… | 0.029 |
| K-narrow-d | 0.562 | 0.572 | **0.680** | 0.0081125003351975160… | 0.1156225 |
| K-narrow-d + tail 10⁷ | 0.562 | 0.572 | **0.680** | (same) | **0.120915** |
| K-narrow-a | 0.562 | **0.580** | **0.660** | 0.0080622749120922782… | 0.1103725 |
| K-narrow-a + tail 10⁷ | 0.562 | **0.580** | **0.660** | (same) | **0.115665** |
| K-narrow-b | **0.564** | **0.580** | **0.620** | 0.0079084414604232310… | 0.0946225 |
| K-narrow-f | 0.562 | **0.585** | **0.660** | 0.0074889858190247350… | 0.0473725 |
| K-narrow-c | **0.564** | **0.580** | **0.640** | 0.0070699528550397492… | 0.0549675 |
| K-narrow-e | 0.562 | **0.580** | **0.680** | 0.0072802555229028306… | 0.0263725 |

(|Im| windows unchanged: (0.26, 0.77), (1.03, 1.46), (1.70, 2.12).)

**Fixed bands, bigger gap — with a caveat.** At the baseline bands,
the absolute form at ε = 1/500 certifies **gap 25781/50000 =
0.51562** (K-fixed-a; **12927/25000 = 0.51708** with EXP09's tail),
above candG's 0.3518725 (0.357165 with tail). Caveat, stated
plainly: this is the lab's gap metric N·thr − ε·M_thr, and the
low-ε point buys it by trading score for ε — its certified score
0.0069670144039762558… is BELOW candG's 0.0103597391213032410….
The necessary condition proved is identical (same bands); only the
contradiction slack differs. It is a new best on the metric EXP06
itself optimized, not a stronger theorem.

This sharpens a necessary condition only. −30 is NOT closed; no
exclusion is claimed. The narrowed region is where a c_Cl ≥ 1
character's zero must now lie; excluding it still needs
zero-freeness there, which per EXP03 is at Re ≈ 0.99986 in the
literature — a deficit shortfall of ~3×10³, unchanged.

## Method

Pipeline as in EXP06/EXP10, rebuilt for φ383 (lengths 229/25,
397/200 ×2, 56/125 ×3; 20 shifts 0, 1/4, …, 4; σ = 7/5;
tail_height 8):

1. **Affine score** (EXP06's `gradient.json`, the verifier's own
   interval arithmetic): score(b) = C + Σ g_j b_j, C =
   0.11074897511696911, all g_j < 0; moment weight-independent
   (99.186384435239… at LIMIT = 1982760, 98.4550015213825703… at
   10⁷). Tail ratio = K·Σ|b_j|/(8−a_j)¹², K = 12097251.890555464.
2. **Float φ evaluator** (EXP06's `phi_float.py`): revalidated here
   against `phi0_series`, worst err 1.8e-15.
3. **Grid** (`build_grid383.py`): tagged (0 gap, 1/2/3 bands), band
   grids built out to u = 0.22 / 0.24 / 0.30. Three generations —
   v1 141,975 pts, v2 268,200, v3 **742,597** — each forced by a
   verifier death (§Failures). v3 adds: cliff windows at t-step
   0.0005 / u-step 0.0005 (band 1: u∈[0.045,0.22], t∈[0.63,0.74];
   band 2: [0.055,0.24]×[1.31,1.43]; band 3: [0.085,0.30]×
   [1.95,2.09]) and gap-edge strips at t-step 0.001–0.002.
   Sag arithmetic: near the band-1 cliff |g″| ≈ 31, so grid step h
   undershoots the continuum by ≈ 31h²/8 — h = 0.0025 sags 2.4e-5
   (the whole low-ε floor), h = 0.0005 sags ~1e-6.
4. **LP** (`lp383.py`): ABSOLUTE form — g_new(p) ≥ FLOOR on the
   whole required region (gaps + bands out to the candidate
   (c1, c2, c3)); dominance ≥ 0.001; Σ|b| ≤ cap (scanned, never the
   frontier — see §Frontier); tail ratio ≤ 0.95ε; baseline sign
   pattern; maximize the affine score. The floor is capped by the
   (u=1/2, t=8) corner, where W = 0.013730 and Re φ ≈ −8.8e-7:
   FLOOR must stay below ε·0.01373; the runs use FLOOR/(εW_corner)
   ≈ 0.22 (K-fixed-a) to ≈ 0.55 (narrowed runs).
5. **Rationalize** (`ladder383.py`) to a **1e-7** grid (b_0 absorbs
   rounding; Σb = 1 and dominance > 0 as exact rationals),
   score_threshold = largest multiple of 1/20000 ≤ score_rat −
   1.5e-4, M_thr = 9919/100 (9846/100 with tail), post-rationalization
   min-g check on grid + gap-C edge strip, then the FULL verifier.
   Baselines replayed exactly first (row383: all 14 certified
   values; candG: score/moment/gap strings identical).

## Frontier map (LP diagnostics unless stated; viability = gap > 0)

- **Band 1 is the stiff one.** Single-band: c1 = 0.064 viable at
  every ε tried (best gap 0.2044 at ε = 0.00725, FLOOR 4e-5);
  c1 = 0.066 barely (gap 0.0576 at ε = 0.00725; 0.0300 at 0.008);
  c1 = 0.068 not viable at ε ∈ {0.00725, 0.008, 0.0085} (gap ≤
  −0.089). Combined with c2/c3 raises, c1 = 0.064 costs most of the
  gap (K-narrow-b/c). The strip u ∈ [0.062, 0.07] × t ∈ [0.26, 0.77]
  contains the deep patch (EXP07: min Re φ383 = −24.2 at
  (0.5, 0.44) for baseline weights); repairing it is what eats the
  score (score falls ~0.0014 per +0.002 of c1 near the cap).
- **Band 2 is moderate.** Single: c2 = 0.09 viable (gap 0.0890 at
  ε = 0.0085; 0.0334 at ε = 0.01), c2 = 0.095 thin (0.0688 at
  ε = 0.00725), c2 = 0.10 not viable at ε ∈ {0.0085, 0.01}.
  Combined cap ≈ 0.085 at useful gaps (K-narrow-f).
- **Band 3 is the roomy one.** Single: c3 = 0.18 viable (gap
  0.1022 at ε = 0.00725; 0.0573 at ε = 0.0085), c3 = 0.20 not
  viable at ε ∈ {0.0085, 0.01}. Combined: (0.08, 0.18) still
  positive (K-narrow-e, gap 0.0264); (0.09, 0.16) and
  (0.066, 0.08, 0.12) are past the joint frontier (LP gap < 0 at
  ε = 0.00725).
- **ε frontier at fixed bands (LP):** predicted gap rises as ε
  falls — 0.3439 (ε = 0.00725, FLOOR 5e-5) → 0.3748 (0.0065) →
  0.4462 (0.00425) → plateau ≈ 0.51 over ε ∈ [0.0015, 0.002] —
  then collapses at ε = 0.001 (LP score −0.0266: the ratio cap
  0.95ε strangles the modulation Σ|b| → ~1.2 while positivity
  still needs it). Certified at the plateau: ε = 0.002, gap
  0.51562. At low ε the binding constraint is the tail ratio
  (active, ratio = 0.95ε, in every solve ε ≤ 0.0065), not the
  floor and not Σ|b|.
- **Σ|b| saturation ≈ 1.70** (the baseline's own total): at
  ε ≥ 0.0065 the LP optimum is identical for cap ∈ {1.7, 2.5, 4.0}
  — unlike φ384 (EXP10: saturation ≈ 10.62), this family does not
  spend modulation. At ε ≤ 0.0065 the ratio constraint forces
  Σ|b| DOWN (1.43 at ε = 0.00325, 1.19 at ε = 0.00175).
- **FLOOR sensitivity is small** once the grid resolves the cliffs:
  at ε = 0.00725, FLOOR 3e-5 vs 5e-5 moves the LP score by
  ~1e-4 (0.010489 vs 0.010424). No LP infeasibility occurred
  anywhere in EXP11 — every cap above is a score-viability cap,
  each cross-checked at ≥ 2 values of ε (the two joint-frontier
  points at ε = 0.00725 only, labeled as such).

## Failures (recorded with the same care)

All three are the same candidate (K-fixed-a: ε = 1/500, FLOOR 6e-6,
baseline bands) dying in `check_exterior` at depth 42, each at a
finer grid generation — the EXP10 candF lesson, twice more:

- **1e-6 rationalization** (dir `cand-K-fixed-a-1e6grid/`): died at
  u → 1/2, t ≈ 3.3113 (gap C). The LP solution met FLOOR = 6e-6 on
  the grid, but rounding the weights to 1e-6 moved g by −1.7e-5 at
  the dip (0.5, 3.295) — the dip is real and narrow (g < 2e-5 over
  t ∈ [3.2685, 3.3225] at u = 1/2, min −1.14e-5 after rounding).
  Fix: rationalize at 1e-7. (EXP06/EXP10 never saw this: their
  floors were ≥ 2e-4 ≫ rounding swing.)
- **Grid v1** (141,975 pts, 1e-7): died at u → 1/2, t ≈ 2.4586
  (gap C) — a continuum dip between v1's t-step-0.01 edge samples.
  Fix: v2 edge strips (t-step 0.002).
- **Grid v2** (268,200 pts): died at the band-1 top edge,
  u → 0.062, t ∈ [0.68730, 0.68736] — EXP06 candA/B's exact death
  site. The dip at (0.062, 0.686) is −1.79e-5, ~0.002 wide in t,
  between the patch's t-step-0.0025 samples. Fix: v3 cliff windows
  at t-step 0.0005. On v3 the same configuration PASSES
  (min_g_rat = +4.0e-6 on grid + edge strip).

## Reproduction

Each `cand-*/` dir is self-contained (verifier + inputs + redesigned
`fixture383.json` + `result.json` or `err.txt`); run
`/tmp/flintenv/bin/python verify_spectral383.py` inside it
(~15–17 s). Tail variants are the `cand-*-tail10m/` dirs (LIMIT =
10⁷ verifier copy in `tail-src/`, EXP09's table). Champion fixtures
are also copied to the top level: `fixture_K-fixed-a10m.json`
(fixed bands, gap 0.51708, tail), `fixture_K-narrow-d10m.json`
(0.562/0.572/0.680, gap 0.120915, tail), `fixture_K-narrow-a10m.json`
(0.562/0.580/0.660, gap 0.115665, tail), `fixture_K-narrow-b.json`
(0.564/0.580/0.620), `fixture_K-narrow-c.json` (0.564/0.580/0.640),
`fixture_K-narrow-e.json` (0.562/0.580/0.680),
`fixture_K-narrow-f.json` (0.562/0.585/0.660), with matching
`result_*.json`. Scripts: `build_grid383.py`, `lp383.py`,
`ladder383.py`, scans in `scan_bands.py` / `scan2.py` / `scan3.py`
(+ `.json` outputs; those ran on grid v2 — frontier diagnostics,
superseded in resolution but not in shape by the v3 ladder runs).

## Verdict on E9

EXP10's method finding transplants cleanly: the absolute-floor LP
raises φ383's bands, which the relative form could not do at all.
Certified: band 3's threshold rises 0.605 → 0.680, band 2's
0.572 → 0.580 (0.585 in one Pareto point), band 1's 0.562 → 0.564,
with joint points (0.562, 0.580, 0.680) and (0.564, 0.580, 0.640)
on the frontier; and at the original bands the contradiction gap
rises to 0.51708 (tail composed) on the lab's metric, at a lower
score. The frontier is mapped: band 1 caps at c1 ≈ 0.066–0.067
(the deep patch), band 2 at ≈ 0.09–0.095 alone / ≈ 0.085 combined,
band 3 at ≈ 0.18–0.20 alone; the fixed-band ε-ladder plateaus at
ε ≈ 0.0015–0.002 and collapses at 0.001 under the tail-ratio cap.
Do not re-run this LP family at these shifts/lengths expecting
more. E9 is DONE. −30 NOT closed; no exclusion; no credit; the
bite still needs zero-freeness in the narrowed bands (EXP03).
