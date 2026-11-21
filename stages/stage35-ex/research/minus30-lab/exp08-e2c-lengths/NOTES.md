# EXP08 — E2(c): length-splitting variants of the row383 test function (2026-11-21)

Lab copies of row383 only; the repo clone was not modified. Judge: the
repo's own `verify_spectral383.py`, FULL runs (score + moment +
`check_exterior`), python-flint 0.9.0 (venv /tmp/flintenv, recreated).
Scripts: `harness_float.py` (float screen, validated below),
`scan.py`, `screen_pos.py`, `eval_arb.py`, `lp_e4.py`, `lp_e4b.py`,
`lp_frontier.py`, `lp_a4_combined.py`, `lp_a4_v2.py`, `lp_a4_v3.py`,
`make_candidates.py`. Candidate dirs `cand*/` hold full verifier
copies + fixtures + `result.json` (pass) or `err.txt` (fail).
Best certified fixture/result at this level: `fixture383-A4.json`,
`result-A4.json`.

## Headline

- **One small CERTIFIED improvement, from a uniform length rescale
  ×1.001 (variant A4), baseline weights**: score_lower
  0.0098858898430937020… → **0.0099193768789228958…** (+3.35e-5),
  same bands, full verifier PASS. With thresholds (99/10000, 9919/100)
  at ε=1/100 the contradiction gap is **119/2500 = 0.0476**, vs
  0.0371 for baseline lengths at the same tightened thresholds (and
  0.029 for the original row383 thresholds). The length-attributable
  part is exactly the score_threshold step 0.0098 → 0.0099 that the
  higher certified score unlocks.
- **Nothing beats EXP06's candG** (gap 0.3518725, score
  0.0103597391213032410…, ε=29/4000). The only length split with a
  higher raw score (E4, split one mid component) has its gain eaten
  by a positivity dip; its LP frontier stays below the candG-beating
  score at every ε (table below), and the transplanted-weight full
  run fails `check_exterior`. A4 lengths + LP weights at ε=29/4000
  predict score ≈0.01043–0.01046 but are NOT certifiable: two full
  runs fail at the same u→1/2 sliver (t≈4.18–4.19, [2.12,8] gap).
- **Premise correction**: in this verifier the moment does NOT depend
  on the lengths at all (see §1). Length moves cannot improve the
  moment margin, and cannot rescue EXP02a's σ moves; σ∈{6/5, 8/5}
  joint moves are also gap-dominated arithmetically (§5).

## 1. How lengths enter the verifier; the moment is lengths-independent

Reading `verify_spectral383.py`: the score is
γ + log(8π) + π/30 − logdisc/N − arch + prime. Lengths enter through
the test function values `f.value` (prime term), the knot data
(arch term), φ0 (positivity), and `tail_constant` / the exponent
2n = 2·len(lengths) (tail ratio). The moment is
logdisc/2 + (7/2)((σ/2)ψ − log π) + 49(σψ − log 2π) + deriv, where
`prime_bounds`' `log_deriv` never touches `f` — it depends only on σ
and the prime splitting data. Empirical confirmation: the certified
`moment_upper_expression` is the IDENTICAL arb string
99.1863844352390573896576084911412625701974938363473864… for the
baseline lengths (n=6), the E3 lengths (n=12) and the A4 lengths —
three different length multisets at σ=7/5. Consequence: E2(c)'s only
levers are score, positivity and tail ratio; "lower moment via
lengths" does not exist in this harness, and a σ change changes the
moment by exactly EXP02a's amounts regardless of lengths.

Support constraint: `prime_bounds` asserts exp(T) < LIMIT = 1982760,
i.e. T < 14.49984…; baseline T = 7237/500 = 14.474 leaves room for a
×1.001 rescale (T = 14.488474) but not ×1.002 (T = 14.5029…).

## 2. Screening harness (float, validated)

`harness_float.py` replicates the score (prime points/coefficients
are f-independent; arch transliterated term-by-term), the tail ratio
and the positivity function g = Re φ + εW in float64. Validation
against both certified baselines: score agrees to 7e-11 (base) /
1e-10 (candG), prime to 4e-12, arch to 8e-11, tail ratio to 1e-15;
positivity screen reproduces EXP06's baseline min g = +1.36e-4 at
(u→1/2, t=8). One failure of the float screen, recorded: for the
n=12 variant E3 the degree-23 arch Horner suffers catastrophic
cancellation and reports score ≈ +972.98 (garbage); the arb
score-only evaluation (`eval_arb.py`, verifier's own functions)
gives the true **−0.3341141280000160158…**. Float rankings are
trustworthy for n ≤ 8 here; E3 is dead on positivity anyway (§3).

## 3. Variant scan (19 variants; float scores, both weight sets)

Baseline lengths L0 = [229/25, 397/200 ×2, 56/125 ×3], T = 14.474.
Reference scores: base weights 0.009886, candG weights 0.010360.

| variant | change | n | score (base w) | score (candG w) | verdict |
|---|---|---|---|---|---|
| A1 ×0.99 | rescale | 6 | 0.008855 | 0.009263 | worse |
| A2 ×0.98 | rescale | 6 | 0.006593 | 0.006948 | worse |
| A3 ×0.95 | rescale | 6 | −0.007069 | −0.006821 | dead |
| **A4 ×1.001** | rescale | 6 | **0.009919** | **0.010401** | **certified (§4)** |
| B1 | split big 9.16→4.58+4.58 | 7 | −0.291811 | −0.291689 | dead |
| B2 | split big →6+3.16 | 7 | −0.234543 | −0.234417 | dead |
| B3 | split big →thirds | 8 | −0.477871 | −0.477756 | dead |
| C1 | merge 3 smalls →1.344 | 4 | 0.006740 | 0.007359 | worse |
| C2 | merge 2 smalls | 5 | 0.008942 | 0.009461 | worse |
| C3 | merge mids+smalls | 3 | −0.030751 | −0.028635 | dead (ratio 0.0201 > ε) |
| D1 | move 1.0 big→smalls | 6 | −0.042366 | −0.042160 | dead |
| D2 | move 1.0 big→mids | 6 | −0.030810 | −0.030514 | dead |
| D3 | all equal T/6 | 6 | −0.504596 | −0.504480 | dead |
| D4 | move 1.0 →big (smalls 0.1147) | 6 | −0.045731 | −0.043834 | dead, tail ratio 22.69 |
| E1 | n=2, T/2 each | 2 | −0.130126 | −0.123662 | dead (ratio 0.285) |
| E2 | n=3, T/3 each | 3 | −0.144151 | −0.143679 | dead |
| E3 | n=12, all halved | 12 | float invalid; arb **−0.334114** | — | dead; positivity −2.76 |
| **E4** | split one mid 1.985→0.9925×2 | 7 | **0.010653** | **0.010987** | raw gain, positivity-dead (§4) |
| F1 | L0 + tiny comp 1/50 | 7 | 0.009885 | 0.010359 | dead, tail ratio 1.618 |

Pattern: the score is extremely sensitive to the length multiset —
almost every perturbation is strongly negative. The baseline's big
component (229/25 ≈ 63% of the support) is load-bearing: splitting
or shrinking it collapses the prime term. Tiny components (≤0.115)
explode `tail_constant`/norm and kill the tail ratio (D4, F1).
Only two directions are non-negative: +0.1% support (A4) and
splitting one mid component (E4).

## 4. The two live candidates

### E4 — split one mid component (n=7): raw gain, positivity-dead

Lengths [229/25, 397/400, 397/400, 397/200, 56/125 ×3]. Float score
0.010653 (base w) / 0.010987 (candG w); tail ratio fine (0.00231 at
candG config). But the positivity screen gives min g = −0.0280
(base w) / −0.0294 (candG w) at (u=0.5, t≈2.52), and the FULL
verifier run with candG weights (`candE4G/`) FAILS
`check_exterior`: depth 42 at u∈[524287/1048576, 1/2], t≈4.0878
([2.12, 8] gap rectangle). LP re-optimization for E4 lengths
(EXP06 machinery; grid 105,346 pts; absolute form, slack 0 — the
max score with grid min g ≥ 0) vs the score needed to beat candG's
gap at the same ε (M_thr 9919/100):

| ε | LP frontier score | score needed | shortfall |
|---|---|---|---|
| 0.00725 | 0.009578 | 0.010200 | −0.000622 |
| 0.0075 | 0.009751 | 0.010436 | −0.000685 |
| 0.008 | 0.010094 | 0.010908 | −0.000814 |
| 0.009 | 0.010775 | 0.011853 | −0.001078 |
| 0.01 | 0.011447 | 0.012810 | −0.001363 |

The shortfall GROWS with ε (frontier slope ≈0.68 < 99.19/105
≈0.945), so no ε rescues E4. (Grid LPs underestimate the continuous
positivity constraints, so certified scores would be ≤ frontier:
the conclusion is conservative.) The relative form needs slack
s* = 0.00292 even for feasibility. E4 is a mapped dead end: its
φ0 shape dips below zero near u=1/2 in the high gap, and no weight
vector at these shifts repairs that while keeping the score.

### A4 — uniform rescale ×1.001 (n=6): small certified win, LP ceiling at candG level

Lengths L0 × 1001/1000, T = 14.488474 (exp(T) ≈ 1.966e6 < LIMIT).

CERTIFIED (full verifier, `candA4base2/`, copied to
`fixture383-A4.json` / `result-A4.json`): baseline weights,
ε = 1/100, thresholds (99/10000, 9919/100):
- score_lower = **0.0099193768789228958725…**
- moment_upper = 99.1863844352390573896… (identical string, §1)
- tail ratio 0.0077811469051161555… < 1/100
- **contradiction_gap = 119/2500 = 0.0476**; bands identical to
  baseline (Re > 281/500, 143/250, 121/200). (At thresholds
  (49/5000, 9919/100) the same run certifies gap 371/10000 =
  0.0371, `candA4base/`.)

With candG weights transplanted, the screen shows min g = −8.1e-5
at the band-1 cliff (u=0.062, t≈0.685) — infeasible as-is. LP
re-optimization for A4 lengths at ε=29/4000 (combined form
g_new ≥ max(g_ref(ε) − slack, 0); grids of 105k, then 759,542,
then 823,776 points with a surgical patch near the failure):
predicted score 0.010431 (slack 1e-3) – 0.010462 (slack 2e-3),
but grid min g ≈ 0 (−7e-8) along the u=1/2 edge in [2.12, 8] —
the LP rides the boundary with no rigorous cushion. FULL verifier
runs FAIL twice at depth 42, u→1/2: t≈4.1786 (`candA4/`, v1 grid)
and t≈4.1918 (`candA4v2/`, v2 grid). Methodological note: the pure
relative LP form (no floor) is unsound at ε<1/100 — it returns
grid min g = −5.0e-4 already at slack 1e-4, because the reference
(baseline weights at ε=29/4000) is itself negative somewhere;
EXP06's "with floor" was load-bearing. Verdict for A4+LP: ceiling
≈ candG's score with zero cushion; not certifiable without an
analytic treatment of the u=1/2 edge. Not pursued further.

## 5. σ joint moves: dominated, not run

The score is σ-independent in this verifier and the moment is
lengths-independent (§1), so for any length set the σ=8/5 moment is
EXP02a's 107.9495764860553089217… and σ=6/5 is
133.2333448343481425486…. Best-case gaps at ε=29/4000 with the best
certified score available (A4, s_thr = 0.0099): σ=8/5 →
105·0.0099 − 0.00725·107.9496 = 0.2568; σ=6/5 → 0.0735. Both
< 0.3518725 (candG at σ=7/5). Even E4's uncertified float score
0.010987 would give only ≈0.362 at σ=8/5 before its (harder, since
W shrinks as centers grow) positivity — a dead combination. No
full runs were spent on σ variants.

## Verdict on E2(c), and on E2 as a whole

Length splitting is DONE. Within the row383 fixture family the
length multiset is essentially rigid: the only non-destructive
moves are a +0.1% support rescale (certified: score +3.35e-5, gap
0.0476 in the baseline-weight configuration — real, and an order
of magnitude below EXP06's candG configuration) and one mid-split
whose gain is exactly cancelled by positivity. No length variant,
with any weights the LP could find, beats candG's certified gap
0.3518725 at the same bands, and none improves the moment (which
lengths cannot move). E2 (a)+(b)+(c) is now fully explored:
(a) σ dead, (b) weights+ε harvested by EXP06, (c) lengths rigid
with the small A4 exception above. Do not retry length splits at
these shifts/support; a different support cap would need a longer
prime tail (that is E7's territory, a different input, not a
fixture variation). No E1/endpoint credit; −30 is not closed; the
hard core (c_Cl ∈ {1,2}, ZF-type zero-freeness) is unchanged.
