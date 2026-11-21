# EXP12 — E10 scout: depth-capped fixture family by changing lengths (float only)

Date: 2026-11-21. Scout only — no full-verifier run, no certified claim,
no repo change. Lab copies only.

## Question

E10 (proposed 2026-11-21, pending the user's call) retries repulsion (E6)
with a different fixture family: change support/degree so the test
function meets EXP07 §5's criterion — in-band depth shallow enough that
one zero orbit cannot eat the whole budget, i.e. −min_R Re φ < G_N/4
(EXP05 7-char config: min Re φ > −10.67, actual −19.92, misses by 1.87×).
This scout asks the cheap version of that question: with the weights
inherited (EXP05 cand6 and EXP10 candH), does any length change shallow
the depth while keeping the bands and exterior positivity?

## Method (float, diagnostic only)

- Float φ evaluator adapted from EXP10's `phi_float384.py`
  (`scout_depth.py`, `scout_positivity.py` in this dir): same 21 shifts,
  same weights, only the `lengths` list changes; norm recomputed per
  family. Validated by reproduction: baseline lengths
  [9.1, 2.3, 2.3, 0.35, 0.35] give band-1 depth −19.920 with EXP05
  weights (EXP07's −19.92 exactly) and exterior min g = +0.000557 at
  ε = 9/100 (EXP10's "baseline min g 5.6e-4").
- Depth: min Re φ over Ω2, u ∈ [c, 0.5] × t ∈ band ranges
  (band 1: c = 0.14, t ∈ (0.26, 0.77); band 2: c = 0.18, t ∈ (1.03, 1.46)),
  grid step 0.005.
- Positivity: min g = Re φ + εW over the verifier's required exterior
  region (gaps u ∈ [0, 0.5] over t ∈ [0.1, 0.26] ∪ [0.77, 1.03] ∪
  [1.46, 12]; bands u ∈ [0, c] over their t-ranges), candH weights at
  ε = 13/400. Required: min g > 0.

## Result: the cheap path is dead — depth and positivity trade one-for-one

| lengths | support T | band-1 depth | band-2 depth | min g (exterior) |
|---|---|---|---|---|
| base [9.1, 2.3, 2.3, .35, .35] | 14.40 | −19.92 (exp05) / −20.33 (candH) | −1.74 / −1.67 | +0.0002 |
| ×0.95 | 13.68 | −15.89 | −1.36 | −0.078 at (u=0.28, t=0.77) |
| ×0.90 | 12.96 | −12.32 | −1.07 | −0.61 at (0.38, 0.77) |
| ×0.85 | 12.24 | −9.47 | −0.82 | −1.78 at (0.50, 0.77) |
| ×0.80 | 11.52 | −7.20 | −0.60 | −3.08 at (0.50, 0.77) |
| ×0.60 | 8.64 | −1.94 | −1.25 | −2.05 at (0.50, 0.835) |
| big 8.5 [8.5, 2.3, 2.3, .35, .35] | 13.90 | −15.14 | −1.15 | −0.15 at (0.295, 0.77) |
| big 7 | 12.30 | −6.81 | −0.37 | −2.63 at (0.50, 0.77) |
| big 5 | 10.30 | −1.86 | −0.79 | −1.85 at (0.50, 0.78) |
| redistributed [4, 4, 3, 2, 1.4], same T | 14.40 | −2.91 | −0.13 | −2.00 at (0.50, 0.77) |
| drop smalls [9.1, 2.3, 2.3] | 13.70 | −20.23 | −1.70 | (not run — depth unchanged) |

Reading:

- Shortening the lengths DOES shallow the depth, and it is the longest
  length that sets it (dropping the 0.35 components changes nothing;
  redistributing at fixed T shallows to −2.9). Scale ×0.85 already
  passes the −10.67 depth criterion on paper.
- But every variant that shallows the depth also breaks exterior
  positivity, always at the same place: the band-1 top edge t ≈ 0.77,
  i.e. the gap just above band 1. Shortening the support widens the
  negative lobe in t, so it spills out of the band into the gap.
  Even ×0.95 — depth still −15.9, failing the criterion — already
  has min g = −0.078. There is no scale at which both conditions hold
  with inherited weights.
- Band 2 is never the binding constraint (depth ≥ −1.74 everywhere).

## Verdict (scout-level, not a full-experiment verdict)

- E10's cheap version — change lengths, keep weights — is DEAD.
  Do not run the full verifier on any of these length variants with
  inherited weights; check_exterior would fail at t ≈ 0.77.
- The only live E10 path is a full LP redesign inside a new length
  family (new affine gradient + absolute-floor LP, EXP10/EXP11-scale
  work): the LP would have to repair a −0.08…−3 positivity deficit
  at the band-1 top edge while keeping the shallower depth. Whether
  that is possible is unknown — the LP rescued band-raising in
  EXP10/EXP11, but there the deficit was a grid/floor artifact, while
  here the widening of the negative lobe is structural in the
  fixture family. Expected value stays low; cost is one EXP10-sized
  experiment. Needs the user's call before starting.
- Caveat: the −10.67 criterion uses EXP05's G_N = 42.7; a new
  family's own G_N (score-dependent) would move the threshold. That
  does not affect this scout's verdict, which rests on positivity
  alone — a candidate must pass check_exterior at any score.
- −30 NOT closed; no exclusion; no credit. GRH not assumed anywhere.
  All numbers above are float diagnostics, not certified values.
