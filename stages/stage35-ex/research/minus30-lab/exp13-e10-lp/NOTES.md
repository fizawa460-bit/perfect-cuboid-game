# EXP13 — E10 full experiment: LP redesign in new length families

Date: 2026-11-21. Status: DONE. **Verdict: NEGATIVE — E10 is closed.**
No (lengths, weights) pair in the families searched restores exterior
positivity while keeping the depth shallower than the counting budget
allows. The LP frontier is mapped and the shortfall is quantified
below. −30 is NOT closed; no exclusion; no credit. All LP/float
numbers are diagnostics; the only verifier-grade numbers are the
score/moment values computed by verify_average384.py's own code
(§2, §4) — no new certificate was produced, because no candidate
passed the LP screen.

## 0. Trap-B check line (ledger rule)

Finite claim = "either certify a 7-char-average test function
satisfying BOTH exterior positivity (full verifier) AND the depth
criterion −min_R Re φ < G_7/4, or map the LP frontier showing no such
function exists in the families searched"; the certified numbers that
must move = depth min Re φ and the exterior min g; stop condition =
frontier mapped or criterion met. → Outcome: frontier mapped (§3–§5);
the second branch of the claim is what happened. Not a rephrasing:
EXP12 left exactly one live path (LP redesign in new length
families); this experiment walked it to the end.

## 1. Question and setup

EXP07 §5: the 7-char counting argument gains a second orbit only if
−min_R Re φ < G_7/4, G_7 = 7·(105·S − ε·M). EXP05 base: G_7/4 =
10.674 vs depth 19.92. EXP12 (float scout): shortening the spline
lengths shallows the depth (×0.85 → −9.47 at inherited weights) but
breaks exterior positivity at the band-1 top edge (0.5, 0.77).
Question: can an EXP10-style absolute-floor LP weight redesign, run
inside each new length family, restore positivity AND keep the
depth above −G_7/4 for the redesigned function's own G_7?

Families (lengths = EXP05's [9.1, 2.3, 2.3, 0.35, 0.35] rescaled, or
redistributed; T = sum of lengths; shifts and 20 cosine slots
unchanged; bands fixed at EXP05's narrowed c = 0.14 / 0.18):

| family | lengths | T |
|---|---|---|
| fam-base | 91/10, 23/10, 23/10, 7/20, 7/20 | 14.4 |
| fam-s95 | ×19/20 | 13.68 |
| fam-s90 | ×9/10 | 12.96 |
| fam-s85 | ×17/20 | 12.24 |
| fam-s80 | ×4/5 | 11.52 |
| fam-red | 4, 4, 3, 2, 7/5 | 14.4 |

Depth region R = the band rectangles u ∈ [c_j, 1/2] (the counting
argument's region; a zero at u < c_j is outside the narrowed bands
and does not enter). Depth cap D means Re φ ≥ −D on R.

## 2. Machinery, and how it was validated

Per family: a fresh copy of verify_average384.py + inputs; the score
gradient re-extracted at that family's lengths
(extract_gradient384.py, 21 unit-modulation runs); an LP grid =
EXP10's positivity geometry PLUS a densified strip t ∈ [0.74, 0.86]
(u-step 0.0025, t-step 0.00125, all u) and a t ∈ [0.70, 0.84] ×
u ∈ [0.40, 0.5] refinement (183,819 points), and a depth grid over R
(27,692 points, refined near u → 1/2, t ∈ [0.36, 0.52]).

Two exactness points that matter:

- **The d_upper correction.** The verifier's arch bound contains
  tail = C_m·d_upper(b), C_m = (16/15)/(2·(1024−1/2)²) ≈ 5.09e-7,
  d_upper(b) = Σ_j |b_j|·a_j². The stock extractor freezes d_upper
  at the fixture's weights, so the affine score model is exact only
  after folding the correction in:
  score(b) = C + Σ g_j b_j − C_m·(d_upper(b) − d_upper(base)).
  Validation (fam-base): corrected model at EXP10 candH weights
  reproduces candH's certified score 0.0868448982333700496… to
  2.8e-17; at EXP05 weights to 6.9e-17. Without the correction the
  error is ~1e-5 — small, but larger than the margins EXP10/EXP11
  reported, so all EXP13 LP scores use the corrected model.
- **Moment is lengths-independent, verifier-confirmed.** In this
  verifier `log_deriv` never touches f; the diag runs (§4) return
  moment upper 99.186384435239… for every family, identical digits.

Float φ (phi13.py) vs the verifier's arb transform_series at 13
sample points incl. (0.5, 0.435), (0.5, 0.77): worst error 2.8e-14.
Baseline depths reproduce EXP07/EXP12 (fam-base −19.9199 at
(0.5, 0.435); fam-red −2.954).

LP (lp13.py): EXP10's absolute-floor form — maximize corrected
score s.t. g_new ≥ FLOOR = 2e-4 on the required region, dominance
≥ 1e-3, Σ|b| ≤ 10.62, tail ratio ≤ ε/2, baseline sign pattern,
x_1 ∈ [−4.6, 0], |x_j| ≤ 0.8 — PLUS the depth-cap rows
Re φ ≥ −D on R. Scan: ε ∈ {0.09, 0.06, 0.045, 0.035} × D ∈ {None,
12, 11, 10.5, …, 3} per family (76 LPs/family, 456 total; fam-base
supplemented with D ∈ {13,…,20} at ε = 0.09/0.06). Predicted margin
= G_7,pred/4 + min_R Re φ with G_7,pred from score − 2.5e-4
(cushion) and M_thr = 99.19; criterion met ⟺ margin > 0.

Robustness relaxations (freesign13.py): free sign pattern via
p/n splitting (feasible set strictly contains the sign-fixed cone),
and Σ|b| cap raised to 25. End-to-end spot checks (§4) confirm the
LP's predicted scores against the verifier's own arb computation at
three LP optima (agreement ≤ 3.3e-6, the 1e-6 weight
rationalization scale).

## 3. Frontier: best achievable margin per family

Criterion needs margin > 0. Best margin over the whole scan
(sign-fixed cone), with the attaining point:

| family | best margin | at ε, D | score | depth |
|---|---|---|---|---|
| fam-base | **−10.03** | 0.035, none | +0.0887 | −20.20 |
| fam-s95 | −17.96 | 0.035, none | +0.0322 | −17.76 |
| fam-s90 | −36.86 | 0.035, none | −0.0799 | −16.06 |
| fam-s85 | −79.53 | 0.035, none | −0.3474 | −9.57 |
| fam-red | −103.15 | 0.035, none | −0.5183 | −1.80 |
| fam-s80 | −140.65 | 0.035, 3.5 | −0.7131 | −3.50 |

In every family the best point is the unconstrained-depth optimum
(or nearly): tightening D only trades score for depth at a losing
rate — each unit of depth bought costs more than one unit of
G_7/4. The global best, fam-base at −10.03, is still ten margin
units from the criterion region. (For scale: the criterion at the
best certified function the lab has, candH, tolerates depth 10.28;
EXP05 base tolerates 10.674.)

## 4. The two failure modes

**(A) Long lengths (base, s95): score survives, depth is floored.**
Max positivity-feasible scores stay positive (base +0.1256 at
ε=0.09; s95 +0.0686), but under positivity the depth cannot be
lifted: dedicated depth-minimizing LPs (positivity at ε=0.09,
score constrained) give the shallowest achievable depths

| family | score ≥ 0 | score ≥ 0.03 | score ≥ 0.065 |
|---|---|---|---|
| fam-base | −13.76 | −14.94 | −16.40 |
| fam-s95 | −14.64 | −15.95 | −17.57 |

while the criterion at those scores tolerates at most ≈ −5.9
(ε=0.035, S=0.065) and less elsewhere. At fam-base, forcing the
depth to exactly the old criterion value 10.674 (free signs, cap
25, ε=0.035) leaves max score −0.112 (margin −37.46); forcing
D = 14 (free signs, cap 25, ε=0.09) leaves score +0.0063
(margin −28.50). Depth caps below ≈ 5.5–6 are LP-infeasible at
baseline lengths at any ε (positivity alone forbids them).

**(B) Short / redistributed lengths (s90, s85, s80, red): depth is
shallow, positivity repair eats the whole score.** At inherited
(EXP05) weights the verifier's own diag scores are already
negative and falling with support: s95 +0.016588, s90 −0.062245,
s85 −0.143762, s80 −0.226476, red −0.381732 (fam-base +0.091153;
moment 99.186384435239… throughout). After optimal LP repair of
positivity the maxima are worse or barely better: s90 −0.0460,
s85 −0.3140, s80 −0.6876, red −0.4981 (ε=0.09). With max score
< 0 there is no contradiction budget at all — G_7 < 0 — so the
counting question never arises: these families do not even yield
a necessary-zero-region statement. Free signs improve the maxima
only slightly (s85 −0.2625, red −0.4559; cap 25: −0.2619 / −0.4552)
and score ≥ 0 under positivity is LP-infeasible at every depth
for s90/s85/s80/red.

Mechanism: the depth dip at (0.5, ~0.44–0.55) and the exterior
lobe at the band-1 top edge (0.5, 0.77) are the same boundary
layer of φ_0 at u → 1/2, seen from inside and outside the band.
Shortening lengths shallows the inside dip (EXP12) but deepens
the outside lobe by the same token (inherited-weights min g at
(0.5, 0.77): −1.93 for s85, −2.07 for red, vs −0.0016-scale at
baseline lengths). The modulation budget that lifts the lobe is
the same budget the score measures; the LP frontier says the
exchange rate never favors the criterion, in either direction,
in any of the six families. EXP12's "depth and positivity trade
off 1:1 along the scaling path" becomes, with weights free: they
do not trade off usefully at all.

## 5. Verdict and scope

- Q1 (does any pair restore certified positivity with depth
  < G_7/4?): **No.** No LP point in the 456 scan solves + 14
  supplementary sign-fixed solves, the free-sign relaxations, or
  the cap-25 relaxations came within
  10 margin units of the criterion; consequently no candidate
  qualified for a full verify_average384.py certification run,
  and none was run. The LP predictions themselves were verified
  against the verifier's own score/moment code at three optima
  (fam-s85: predicted −0.313979786 vs certified −0.313979812;
  fam-red: −0.498125355 vs −0.498124475; fam-base ε=0.06:
  +0.105529885 vs +0.105526658; diffs = 1e-6-grid rationalization).
- Q2 (counting statement): moot — no function meets the depth
  criterion, so EXP07's counting gains nothing new. (Even if one
  had, EXP07 obstruction #1 stands: the bound would be a global
  ≥2-orbits statement, not per-character localization.)
- Q3 (frontier): mapped above. **E10 is DONE, negative.** The
  remaining sub-case is empty within this design space: 5-length
  spline supports in the ×0.80–×0.95 / redistribution families,
  20-cosine modulation, EXP05 narrowed bands. A different
  test-function *shape* (different spline degree/support pattern,
  different modulation basis, or re-narrowed bands traded against
  depth) would be a new experiment, not an E10 continuation —
  do not re-run E10 variants with new angles (trap-B discipline).

Files: lp13.py (LP + corrected affine score), phi13.py,
build_grid13.py (grid13.npz deleted after the runs — rebuild with
this script, ~15 s/family), scan13.py + scan_fam-*.json/.log (all
LP weights and frontier rows), ceilings13.py, freesign13.py,
check_optimum.py, validate13.py; fam-*/ (verifier copies,
fixture384.json with the family's lengths, gradient384_cc7.json,
extract.log, diag outputs). Candidate dirs from check_optimum.py
were scratch and were removed; their weights are the scan JSONs'
rows (fam-s85 ε=0.09 D=None; fam-red ε=0.09 D=None; fam-base
ε=0.06 D=None).
