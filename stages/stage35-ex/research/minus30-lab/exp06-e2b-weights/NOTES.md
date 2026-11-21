# EXP06 — E2(b) full: positivity-constrained weight re-optimization + joint ε / threshold redesign (2026-11-21)

Lab copies of row383 only; the repo clone was not modified. Verifier:
the repo's own `verify_spectral383.py`, python-flint 0.9.0 (venv
/tmp/flintenv, recreated 2026-11-21). Scripts: `extract_gradient.py`,
`phi_float.py`, `validate_phi.py`, `build_grid.py`, `build_grid2.py`,
`lp_search.py`, `rationalize.py`. Candidate dirs `cand*/` each hold the
full verifier copy, the redesigned fixture, `result.json` (pass) or
`err.txt` (fail).

## Headline result (CERTIFIED by the full rigorous verifier)

**candG-eps00725** passes every check of `verify_spectral383.py`:

- score_lower = **0.0103597391213032410352…** (baseline 0.0098858898430937020…; +4.8%)
- moment_upper = 99.1863844352390573… (unchanged — moment does not depend on the weights)
- tail ratio = 0.0045479166478727… < ε = 29/4000 = 0.00725
- **contradiction_gap = 140749/400000 = 0.3518725** (baseline 29/1000 = 0.029; **×12.1**)
- necessary bands IDENTICAL to baseline (Re > 281/500, 143/250, 121/200
  on the same three |Im| windows); 7 rectangles certified, max depth 18.

What the gap is and is not: it is the slack in the certificate's
contradiction (N·score_threshold − ε·moment_threshold). A bigger gap
makes the row383 certificate strictly more robust; it does NOT narrow
the bands, does NOT close −30, and claims no new exclusion. Gap
decomposition vs baseline: +0.0420 from the higher score threshold
(0.0098 → 0.0102), +0.2809 from the ε·moment term (1.0 → 0.7191275).

## Why ε and the thresholds are legitimate knobs (checked in PROOF.md §4)

ε is a free constant of the proof ("次に ε=1/100 と置く"): outside the
bands one needs Re φ + εW > 0, for t ≥ 8 the ratio bound < ε, and the
contradiction needs ε·Mχ < N·Bχ. The verifier encodes exactly these
three conditions (asserts on score/moment, `N*low_score > eps*upper_
moment`, `ratio < eps`, and the exterior subdivision). Likewise
`moment_threshold` is just a certified upper bound for the moment:
99.1863844352390573… < 9919/100 = 99.19, so replacing the round 100 by
9919/100 is the same kind of statement, only tighter. σ stays 7/5
(EXP02a: σ is exhausted), lengths/shifts/bands stay the baseline ones.

## Method

1. **Exact affine structure.** Score, prime term, arch term and tail
   ratio are linear in the weights; the moment is weight-independent.
   Per-shift coefficients g_j = prime_j − arch_j were extracted with
   the verifier's own interval arithmetic (`extract_gradient.py`):
   score(b) = C + Σ g_j b_j, C = 0.11074897511696911, all g_j < 0,
   g_0 = −0.078163449552 the shallowest, g_19 = −3.444090751150 the
   steepest. Affine reconstruction of the baseline score matched the
   certified value to 7e-17; the tail-ratio formula
   ratio = K·Σ|b_j|/(8−a_j)^12, K = 12097251.890555464, matched to
   1e-18. So score-only optimization is an LP objective, not a search.
2. **Float φ evaluator** (`phi_float.py`): Re φ(u,t) = Σ b_j R_j(u,t)
   with φ0(z) = Π sinc(i z ℓ/2)²/norm (flint sinc = sin w/w — the
   π-normalized convention fails; corrected after a first mismatch).
   Validated against the verifier's `phi0_series` at 18 points, worst
   error 1.8e-15.
3. **LP** (scipy/HiGHS): maximize the affine score over b_1..b_19
   (b_0 = 1 − Σb_j), baseline sign pattern fixed, subject to
   (i) positivity on a grid of the required region in the
   pointwise-relative form g_new(p) ≥ g_base(p; ε) − slack with floor
   (baseline min g is only 1.36e-4, at the (u→1/2, t=8) corner, so an
   absolute margin is impossible even for the baseline itself);
   (ii) dominance margin ≥ 0.001; (iii) Σ|b_j| ≤ baseline (not binding);
   (iv) tail ratio ≤ 0.95ε.
4. **Rationalize** to a 1e-6 grid (b_0 absorbs rounding, Σb = 1 exact),
   set score_threshold just below the predicted score, run the FULL
   verifier. The verifier is the only judge; ~13–15 s per run.

## Grid flaw found and fixed (methodological record)

Grid v1 sampled band u in 0.005 steps from 0, landing on 0.060 — the
band-1 top edge u_max = 0.062 itself was never a constraint point. The
first two aggressive candidates (candA, candB) both failed the rigorous
exterior check exactly in that sliver (u → 0.062, t ≈ 0.687–0.689).
Grid v2 (34,195 points) adds u step 0.002 plus the exact u_max, t step
0.005 in bands, and a refinement patch around (u∈[0.04,0.062],
t∈[0.64,0.74]). On v2, ε ≤ 0.008 at slack ≤ 5e-5 is honestly
INFEASIBLE — part of v1's apparent low-ε headroom was the artifact.

## Certified candidates (all full-verifier PASS, bands unchanged)

| cand | ε | score_thr | M_thr | certified score_lower | gap |
|---|---|---|---|---|---|
| baseline | 1/100 | 49/5000 | 100 | 0.0098858898430937020… | 0.029 |
| candC-eps009-safe | 9/1000 | 49/5000 | 9919/100 | 0.0099800337851204592… | 0.13629 |
| candC2 | 9/1000 | 99/10000 | 9919/100 | (same weights) | 0.14679 |
| candD-eps0085 | 17/2000 | 197/20000 | 9919/100 | 0.0100105940902923258… | 0.191135 |
| candD2 | 17/2000 | 199/20000 | 9919/100 | (same weights) | 0.201635 |
| candE-eps008 | 1/125 | 99/10000 | 9919/100 | 0.0100662211617958437… | 0.24598 |
| candF-eps0075 | 3/400 | 1/100 | 9919/100 | 0.0101889412464146487… | 0.306075 |
| candF2 | 3/400 | 101/10000 | 9919/100 | (same weights) | 0.316575 |
| **candG-eps00725** | **29/4000** | **51/5000** | **9919/100** | **0.0103597391213032410…** | **0.3518725** |

candG weights (shifts unchanged; the shift-4 weight went to exactly 0):
λ = 421289/500000, 57389/250000, −148181/1000000, 4569/40000,
−14223/250000, 39851/1000000, −46319/1000000, 21899/500000,
−33091/1000000, 19869/1000000, −10543/1000000, 2797/200000,
−7977/250000, 526/15625, −13743/1000000, 4189/1000000, −667/500000,
181/500000, −33/500000, 0. Dominance margin 0.001002.

## Failures (recorded with the same care)

- candA (ε=0.0075, LP on grid v1, slack 2e-4): exterior check hit
  depth 42 at u∈[0.06199999, 0.062], t≈0.68677 (band-1 top edge).
- candB (ε=0.007, v1, slack 2e-4): same failure, t≈0.68936.
- candH (ε=0.007, grid v2, slack 8e-4): exterior check hit depth 42 at
  u∈[0.499999, 0.5], t≈3.3077 (the [2.12, 8] gap rectangle). ε=0.007
  is rigorously out of reach for this weight family.
- LP infeasibility frontier (grid v2): ε=0.0075 needs slack ≥ 4e-4;
  ε=0.007 needs slack > 8e-4 in LP and fails rigorously at 8e-4.

## Band raising is DEAD in this family

- Float scan with candG/candD weights: every band's min g goes
  negative immediately past its current u_max (band 1: −0.022 at
  u_max+0.01; band 2: −0.0025; band 3: −0.0004) — the u_max values sit
  exactly on the positivity cliff, at t≈0.68 / 1.37 / 2.01.
- LP with all three bands raised by +0.01 as hard constraints
  (ε=0.0085, slack 5e-5 and 2e-4): INFEASIBLE both times.
So no wider necessary-zero bands from weight/ε redesign at the same
shifts and lengths. (Different length splits are E2(c), still open;
different shifts are a different fixture family entirely.)

## Verdict on E2(b)

The direction had REAL headroom, now harvested: within the row383
fixture family (same lengths, shifts, σ=7/5, bands), the certified
score rose 0.0098858898… → 0.0103597391… (+4.8%; LP diagnostics put
the positivity-constrained float ceiling at ≈0.0104, and even slack
2e-3 only reaches 0.0125 vs the no-modulation limit C+g_0 = 0.0326 —
positivity, not score, is what the modulation buys), and the
contradiction gap rose 0.029 → 0.3518725 (×12.1), mostly via the
joint ε (1/100 → 29/4000) and moment_threshold (100 → 9919/100)
redesign that the re-optimized weights make possible. ε ≲ 0.007 and
band raising are certified/LP-dead ends in this family. E2(b) is
DONE; do not retry weight re-optimization at these shifts/lengths.
No E1/endpoint credit; −30 is not closed; the hard core (c_Cl ∈ {1,2},
ZF-type zero-freeness) is unchanged.
