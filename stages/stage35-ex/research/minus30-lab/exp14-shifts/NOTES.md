# EXP14 — E11: new SHIFT SETS for φ384 (7-char / 3-char) and φ383

Date: 2026-11-21. Lab copies only; the repo clone was not modified.
Verifiers: the repo's own `verify_average384.py` / `verify_spectral383.py`
(tail-10⁷ copies from EXP10/EXP11, LIMIT = 10⁷, M_thr = 9846/100),
python-flint 0.9.0, scipy/HiGHS for the LPs. Every number marked
CERTIFIED is the output of a full verifier run; LP/float numbers are
labeled diagnostic.

## Trap-B line (ledger gate, stated before the runs)

Finite claim: either certify, by full verifier runs, a band/gap
strictly stronger than the EXP10/EXP11 frontiers using a new shift
set, or map the shift-axis frontier tightly enough to close it.
Certified numbers that must move: the φ384 7-char/3-char bands and
gaps, and the φ383 bands/gap. Stop condition: frontier mapped across
the shift families below. **Outcome: the first alternative holds —
every target was beaten and certified (see table). E11 is DONE.**

## How shifts enter the verifier (code evidence)

`fixture["cosine_weights"]` is a list of [a_j, b_j] pairs;
`TestFunction.shifts` reads them directly. Constraints, all from
asserts in `verify_average384.py` (the 383 verifier is identical in
structure):

- Σ b_j = 1 exactly; a_0 = 0; all other a_j > 0 (distinctness is NOT
  asserted — duplicates would just merge); dominance
  b_0 > Σ_{j≥1} |b_j|; all a_j < tail_height (12 for φ384, 8 for
  φ383, via `high > max(a)` in check_exterior); d_upper > 0.
- Shifts are therefore **not verifier-locked**: any rational shift
  set satisfying the above is a legal fixture. E11 is live, not void.
- Where shifts act: (i) the test function values
  f.value(x) = spline(x)·Σ b_j cos(a_j x), hence the prime term of
  the score; (ii) the archimedean term, via phases e^{i·a_knot·a_j}
  and via d_upper = K0 + Σ_j |b_j| a_j² in its tail bound;
  (iii) Re φ(u,t) = Σ_j b_j Re[(φ0(u,t−a_j) + φ0(u,t+a_j))/2] (j ≥ 1),
  the exterior-positivity function; (iv) the tail ratio
  K·Σ_j |b_j|/(high − a_j)^{2·len(lengths)}.
- The **moment does not depend on the shifts at all** (nor on the
  weights or lengths): prime_bounds' log_deriv never touches f.
  With the 10⁷ tail it is 98.4550015213825703… for every fixture
  here, so M_thr = 9846/100 composes unchanged.

**Exact affine score model** (the one new piece of machinery):
score(b) = C + Σ_j h_j b_j − C_tail·(K0 + Σ_j |b_j| a_j²), with
h_j = prime_j − rowpart_j extracted per shift by unit modulation in
the verifier's own interval arithmetic, d_upper monkeypatched to the
lengths-only constant K0 during extraction so the arch tail is
separated exactly. C_tail = (16/15)/(2·(1024−1/2)²) = 32/62853135
≈ 5.091234e-07 (the correction EXP13 identified); K0 = +0.071548128650
(φ384 lengths) / +0.079169205031 (φ383 lengths). Since
K0 > 0, the d_upper > 0 assert is automatic for any weights.
Validation: the model reproduces the certified EXP05/row384 baseline
scores to −2.8e-17 / −8.3e-17 and candH's certified score to
+1.4e-17 (conventions.py); per-family assembly (unit modulations vs
one full-modulation computation) agrees to ≤ 8e-17 (φ384) and 0.0
(φ383); the F0 control extraction reproduces EXP10's stored gradient
to 4.4e-16 after the convention correction.

## Shift families (one-line justification each)

Baseline φ384 shifts (21): 0, 1/40, 2/5, 3/5, 4/5, 1, 7/5, 8/5, 9/5,
2, 43/20, 49/20, 51/20, 27/10, 57/20, 3, 16/5, 17/5, 18/5, 19/5, 4 —
irregular, hand-tuned (cluster at 2.15–3.0, the 1/40 near-zero dial).

- **F0-base** — control: baseline shifts through the new free-sign LP.
- **F1-fine** — step 1/10 on [0, 4], 41 shifts: maximal translate
  dictionary on the baseline range; the LP selects.
- **F2-uniform** — step 1/5 on [0, 4], 21 shifts: same count as
  baseline, regularized — tests whether the hand-tuning matters.
- **F3-extended** — baseline ∪ {22/5, 24/5, 26/5, 28/5, 6}, 26
  shifts: longer translates bring smooth far copies (tail-ratio and
  d_upper costs are quantified and small).
- **F4-sparse** — step 2/5 on [0, 4], 11 shifts: the lower edge —
  how much dictionary is actually needed.
- **F5-fineext** — step 1/5 on [0, 6], 31 shifts: density × range in
  one moderate dictionary.
- **G5-fineext383** — the F5 pattern transplanted to φ383 (step 1/5
  on [0, 6], 31 shifts < 8 = φ383's tail_height).

LP form: EXP10's absolute floor (g ≥ FLOOR on the whole required
region), but **free-sign** (auxiliary |b| variables; a new shift set
has no inherited sign pattern), dominance ≥ 0.002, Σ|b| ≤ 12,
tail ratio ≤ ε/2 (φ384) / 0.95ε (φ383). Weights rationalized to a
1e-7 grid (EXP11's lesson), b_0 absorbing, Σb = 1 exact.

## Certified results (full verifier; all with the 10⁷ tail)

**φ384, 7-char (c_Cl ≥ 3):**

| cand | family | bands Re > | ε | score_lower | gap | previous record |
|---|---|---|---|---|---|---|
| T5-7fix | F5 | 0.64 / 0.68 | 13/400 | 0.0898783530560583442… | **124371/20000 = 6.21855** | 5.8983 (EXP10 candH) |
| T1-7fix | F1 | 0.64 / 0.68 | 13/400 | 0.0890537296984959192… | **122691/20000 = 6.13455** | 5.8983 |
| T5-7n74 | F5 | 0.65 / 0.74 | 3/50 | 0.0742214837690979428… | **37353/20000 = 1.86765** | 1.17465 (EXP10 candP) |
| T5-7n76 | F5 | 0.65 / 0.76 | 3/50 | 0.0668258431731213265… | **21813/20000 = 1.09065** | 0.3066 (EXP10 candQ) |
| T5-7n70 | F5 | 0.66 / 0.70 | 3/50 | 0.0644063425747719029… | **16773/20000 = 0.83865** | 0.33285 (EXP10 candM) |

**φ384, 3-char (c_Cl ≥ 2):**

| cand | family | bands Re > | ε | score_lower | gap | previous record |
|---|---|---|---|---|---|---|
| T5-3fix | F5 | 0.63 / 0.63 | 7/200 | 0.0731051205933053291… | **84273/20000 = 4.21365** | 3.98265 (EXP10 candR3) |
| T3-3fix | F3 | 0.63 / 0.63 | 7/200 | 0.0723866732530560653… | **41349/10000 = 4.13490** | 3.98265 |
| T5-3nar | F5 | 0.64 / 0.68 | 9/200 | 0.0587597273905633421… | **17223/10000 = 1.72230** | 1.3653 (EXP10 candT3) |

**φ383 (c_Cl ≥ 1), family G5:**

| cand | bands Re > | ε | score_lower | gap | previous record |
|---|---|---|---|---|---|
| G383-fix | 0.562 / 0.572 / 0.605 | 1/500 | 0.0071055083602527473… | **53283/100000 = 0.53283** | 0.51708 (EXP11 K-fixed-a, at a lower score 0.006967 — this one is stronger on both metrics) |
| G383-nd | 0.562 / 0.572 / 0.680 | 29/4000 | 0.0083897301464463955… | **29433/200000 = 0.147165** | 0.120915 (EXP11 K-narrow-d) |

So the c_Cl ≥ 3 necessary region keeps EXP10's narrowest bands with
3.6× the gap at (0.65, 0.76); the c_Cl ≥ 2 region keeps Ω2′ =
(0.64, 0.68) with gap 1.7223; the c_Cl ≥ 1 fixed-band slack rises to
0.53283. This sharpens necessary conditions only. −30 is NOT
closed; no exclusion; the bite still needs ZF-type zero-freeness in
the regions (EXP03: literature reaches Re ≈ 0.99986, unchanged).

## LP frontier per family (diagnostic, full grid, FLOOR 2e-4)

gap_pred with M_thr 9846/100, SCORE_SAFE 3e-4 (scan14b.json):

| target | F0 ctrl | F1 | F2 | F3 | F5 | F4 |
|---|---|---|---|---|---|---|
| cc7 fixed (0.64/0.68), ε=0.0325 | 5.9841 | 6.1113 | 6.0257 | 6.0572 | **6.1935** | dead |
| cc7 (0.65, 0.76), ε=0.06 | 0.6654 | 0.9748 | 0.8308 | 0.8086 | **1.1388** | — |
| cc7 (0.66, 0.70), ε=0.06 | 0.4803 | 0.6165 | 0.5437 | 0.6996 | **0.8837** | — |
| cc7 (0.65, 0.74), ε=0.06 | 1.4535 | 1.7241 | 1.6054 | 1.6097 | **1.9161** | — |
| cc3 fixed (0.63/0.63), ε=0.035 | 3.9731 | 4.0384 | 3.9778 | 4.1120 | **4.1871** | — |
| cc3 (0.64, 0.68), ε=0.045 | 1.4461 | 1.5714 | 1.4927 | 1.5875 | **1.7375** | — |

Reading: (1) every new family beats the baseline-shift control under
the *same* free-sign LP, so the gain is genuinely the shift axis,
not the formulation; (2) F5 (density × range) wins every target,
with remarkably small Σ|b| ≈ 1.7–1.9 (the baseline-shift LP needed
Σ|b| ≈ 10–12, cap-bound) — a richer translate dictionary repairs the
Re φ patch with far less weight mass, which also keeps the
verifier's subdivision shallow; (3) F4-sparse is decisively dead:
max positivity-feasible score ≈ −0.445 at (0.64, 0.68) — 11
translates at 0.4 spacing cannot repair the patch at any score;
(4) ε = 0.030 is LP-infeasible in every family (the (1/2, 12)
corner: εW ≈ 1.85e-4 < FLOOR 2e-4, shift-independent), so the
fixed-band ε-frontier does not move with shifts; (5) past-frontier
points stay past: (0.67, 0.72) and (0.66, 0.76) have negative LP
gaps in all families (best −0.84, F5), and for φ383 the joint point
(0.564, 0.585, 0.680) is LP-negative (−0.152) for G5 — band 2 at
0.585 remains the φ383 obstruction, as in EXP11.

## Failures and lessons (recorded with the same care)

- **First ladder batch (S5-*) mostly failed, two distinct causes.**
  (a) S5-7fix / S5-3fix / S5-3nar / S1-7fix / S3-3fix were
  LP-infeasible at FLOOR 3e-4: at ε ≤ 0.045 the (1/2, 12) corner
  caps the floor at εW ≈ 2.0e-4–2.8e-4. Floors must be chosen
  per-ε (1.8e-4 at ε ≤ 0.035, 2.5e-4 at 0.045, 3e-4 at 0.06).
  (b) S5-7n76 / S5-7n70 / S5-7n74 died in check_exterior at depth
  42, u → 1/2, t ≈ 6.99. Diagnosis with the float evaluator on a
  fine mesh: a genuine g dip to −4.6e-3 / −6.9e-3 at (0.5, t ≈ 6.21)
  for those weights. **Cause: the LP point thinning inherited from
  EXP10's lp384.py** (for t > 6 it kept only integer-t lattice
  points) discarded the grid's dense gap-C coverage (t-step 0.005
  near u = 1/2) — safe for the baseline shift family, whose
  candidates EXP10 certified, but unsound for new shift sets whose
  large-t superpositions differ. Fix: no thinning (full 164,322
  points); F5's LP gaps dropped by 0.03–0.13 under the full grid
  and all re-laddered candidates then passed. The failed S-*
  candidate dirs and their err.txt are kept as evidence.
- Rationalization at 1e-7 with per-ε floors: all 10 re-laddered
  candidates passed the full verifier on the first attempt.

## Reproduction

Extraction: `extract14.py fam_<F>.json`, `extract383.py
fam_G5-fineext383.json` (gradients in grad_*.json / grad383_*.json,
assembly-validated). R matrices: `build_R14.py` / `build_R383.py`
(rebuild the deleted grid_*.npz, ~1–2 min each; validated vs
transform_series to ≤ 3.8e-15). LP: `lp14.py`, `lp383_14.py`;
scans in scan14.json (thinned — superseded) and scan14b.json (full
grid). Ladders: `ladder14.py`, `ladder383.py`; per-candidate records
in ladder_<tag>.json; each `cand-<tag>/` is self-contained (verifier
+ inputs + fixture + result.json / err.txt). Champion fixtures and
results are copied to the top level: fixture_/result_7char_bestgap_F5,
7char_narrowed_F5 (0.65/0.76), 3char_bestgap_F5, 3char_narrowed_F5,
383_fixed_G5, 383_narrowd_G5.

## Verdict on E11

DONE, positive beyond the brief's targets: the shift axis was real.
One principled family (uniform step 1/5 respread over [0, 6]) beats
every EXP10/EXP11 record on both averages and on φ383, all certified
by full verifier runs. Remaining mapped limits: the fixed-band
ε-frontier (0.0325 at FLOOR 2e-4) is a corner effect and does not
move with shifts; (0.67, 0.72) / (0.66, 0.76) for φ384 and the
φ383 joint point (0.564, 0.585, 0.680) stay past the LP frontier in
every family tried. Do not re-run these shift families expecting
more; a still denser dictionary (step 1/10 on [0, 6]) is the only
obvious untried point on this axis and the F1→F5 trend suggests
diminishing returns. −30 NOT closed; no exclusion; no credit.
