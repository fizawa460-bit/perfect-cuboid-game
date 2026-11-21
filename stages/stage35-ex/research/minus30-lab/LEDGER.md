# −30 lab ledger — tried / untried / results (started 2026-11-21)

Purpose (user, 2026-11-21): try small things against the −30 wall, failure
expected, and RECORD each attempt so the same thing is never retried as new.
This ledger is the do-not-repeat list. Entries: date, what was tried, exact
setup, result, verdict. No E1/endpoint credit is claimed by anything here.

## Ground facts (from repo, audited)
- Target: c_Cl = 0 for K (deg 105, sig (7,49), root disc ≈ 44.5), or rank
  J(Q) ≤ 9. Sel2 dim = 9 + c_Cl; −30 source forces rank ≥ 10.
- row381: c_Cl = 0 under quadratic Hecke GRH (conditional, kept conditional).
- row383: Gal(L/Q) = S_105 certified; unramified quadratic E/K ⇒ E∩L = K,
  Gal(EL/Q) = W(D_105). Unconditional explicit formula: c_Cl ≥ 1 ⇒ some
  nontrivial quadratic Hecke χ has an L-zero in 3 bands (Re > 0.562/0.572/
  0.605, |Im| < 2.12). Score ≈ +0.009886 vs threshold 49/5000, gap 29/1000.
- row384: c_Cl ≥ 2 ⇒ among χ1, χ2, χ1χ2 one has a zero in Ω2 (Re > 0.63,
  |Im| ∈ (0.26,0.77) ∪ (1.03,1.46)). Open obligations stated by the repo
  itself: ZF2 (zero-freeness in Ω2) and δ★ Sel4 non-lift. "次は ZF2 と
  δ★ の4リフトを具体的に検査する" (row384 PROOF §, final paragraph).

## Already tried (do not redo as new)
- T1. Prime-ideal-by-prime-ideal killing of Cl/2 (R3 rows 370–393):
  878 small primes (norm ≤ 6768), formal residual 181. Generation
  certificate needs all primes < 2^94. DEAD as a finishing method.
- T2. Odlyzko/discriminant comparison, unconditional: root disc 44.5 vs
  unconditional bound ≈ 23.9 for this signature. DEAD (gap ~2x in constant).
- T3. Analytic score method under "uniform nonnegativity, no extra lower
  bound for unknown terms" (04-minus30 barrier): score stays < −0.000142
  even with 800k primes, in THAT normalization. (Different normalizations
  are E2/E5 below, not this.)
- T4. Single-character explicit formula (row382 rectangle → row383 three
  bands, cosine modulation, 20 weights, lengths 229/25 + 397/200×2 +
  56/125×3, support T = 7237/500, Hadamard at σ = 7/5, ε = 1/100).
- T5. Three-character average (row384: χ1, χ2, χ1χ2; odd-power uniform
  bound −1/3 at undetermined primes). Gave Ω2 for c_Cl ≥ 2.
- T6. Galois-closure genus constraint (row383 §5): consumed, output was
  the W(D_105) restriction, not c_Cl = 0.
- T7. Class-group computation algorithms (Biasse–Fieker etc.): output
  would be GRH/heuristic-conditional = same status as row381, and
  |disc| ≈ 10^173 is out of practical range. Scouted 2026-11-21, DEAD.

## Untried experiment queue
- E1. Baseline replay of row383 certificate in this environment. DONE
  (see log). Purpose: working harness for E2/E5/E6.
- E2. Test-function variations on the row383 harness: (a) Hadamard point
  σ ∈ {6/5, 8/5} instead of 7/5 — DONE, dead (EXP02a); (b) numerical
  re-optimization of the 20 cosine weights — DONE in full (EXP02b
  single-weight scout + EXP06 positivity-constrained LP with joint
  ε/threshold redesign, 2026-11-21): certified score 0.0098858898… →
  0.0103597391…, contradiction gap 29/1000 → 0.3518725 (×12.1), bands
  unchanged; ε ≲ 0.007 and band raising are dead in this family
  [the band-raising clause is SUPERSEDED by EXP11 (E9): it was an
  artifact of EXP06's relative LP form; the absolute-floor form
  certifies raised bands — see the EXP11 log entry. The ε ≲ 0.007
  clause is likewise relative-form-specific: EXP11 certifies
  ε = 1/500 at the original bands]. Do
  not retry weight re-optimization at these shifts/lengths; (c)
  different length splits at the same support — DONE (EXP08,
  2026-11-21): length multiset is essentially rigid; only a ×1.001
  support rescale helps (certified score 0.0099193768789228958…,
  gap 0.0476 in the baseline-weight configuration), the one
  score-positive split (E4) is positivity-dead with an LP frontier
  below candG at every ε, and the moment is exactly
  lengths-independent in this verifier. Nothing beats EXP06's
  candG gap 0.3518725. E2 is now FULLY DONE (a)+(b)+(c); do not
  retry length splits at these shifts/support.
- E3. ZF2 reality check: collect the best EXPLICIT zero-free regions for
  Hecke/Dedekind L-functions at log-conductor ≈ 400 (literature), compute
  the exact Re they reach at height ≤ 2.12, record the gap to 0.63.
  Expected outcome: negative (gap huge) — recorded so nobody retries.
- E4. δ★ 4-lift, place by place: SUPERSEDED by EXP04 (see log and
  exp04-delta-lift/NOTES.md). No single place can witness non-lift:
  the lift is a global Cassels–Tate condition, reduced by row385 to
  one class q★ ∈ Cl(O_K)/2Cl(O_K). Do not run place-by-place checks.
- E5. More-character averaging: generalize row384 from 3 characters
  (−1/3) to 7 characters of a (Z/2)^2 subgroup... note: for c_Cl ≥ 3 use
  the 7 nontrivial characters of (Z/2)^3, odd-power bound −1/7 at
  undetermined primes. Expected: narrower necessary-zero bands for the
  c_Cl ≥ 3 case. Does not close −30 alone; shrinks the hard core to
  c_Cl ∈ {1, 2}. DONE (see log, EXP05): score 0.0524 → 0.0912, region
  narrowed to Re > 0.64 / 0.68 per band.
- E6. Deuring–Heilbronn repulsion variant: assume one χ HAS a band zero;
  derive widened zero-free regions for the others and feed back into the
  row384 average. DONE, NEGATIVE (EXP07, 2026-11-21): no repulsion is
  available from the row383/row384 test functions — the average couples
  characters only through one scalar budget (cannot localize the
  others' zeros), one deep zero orbit supplies 1.9x–2000x the whole
  budget (counting fails), and the classical full-group channel is
  vacuous (pole term 2φ(1/2) ≈ +90.7 > group budget ≈ 36.6). Do not
  retry with these test functions; the exact criterion a future
  depth-capped test function would need is recorded in EXP07 §5.
- E7. Tail extension: recompute first-degree prime counts for p up to
  10^7 (repo tail stops at 1,982,760) and re-run E2 with the longer tail;
  measures how much of the score is tail-limited. (Compute-heavy; the
  row383 verifier's --recount style path recounts only the stored range,
  so this needs new counting code: factor f mod p for ~664k primes.)
  DONE (EXP09, 2026-11-21): counting code reproduced the stored table
  byte-identically, extension to 10^7 counted (516,851 primes), and the
  gain is moment-only: moment 99.186384435239… → 98.455001521382…,
  score/bands exactly unchanged (structurally: score primes satisfy
  log p < support, all already tabulated). Via threshold redesign the
  certified gaps become base 0.029 → 0.039 and candG 0.3518725 →
  0.357165. The direction is within ≈0.248 of its absolute ceiling
  (LIMIT < B² caps the residual Chebyshev term at ≥ 0.5594); do not
  extend further.
- E8. Combination: apply EXP06's redesign machinery (LP weight
  re-optimization + ε/threshold redesign) to the row384/EXP05
  averaging test function φ384, 7-char first, then the original
  3-char fixture; compose EXP09's extended tail if clean. DONE
  (EXP10, 2026-11-21): certified on both targets — 7-char gap
  0.45 → 5.8983 at EXP05's bands and bands narrowed to
  0.65/0.76 (Pareto frontier); 3-char gap 0.7 → 3.98265 and Ω2
  narrowed to Re > 0.64/0.68. The EXP05 "genuine patch" was
  weight-dependent, not family-intrinsic. Do not re-run this LP
  family at these shifts/lengths: ε-frontier, Σ|b| saturation
  and the band-1 cap (c1 ≈ 0.16) are all mapped in EXP10.
- E9. φ383 band narrowing via EXP10's absolute-floor LP (the
  c_Cl ≥ 1 case; EXP06's relative form declared band raising
  dead — the verdict EXP10's φ384 finding reopened). DONE
  (EXP11, 2026-11-21): certified narrowings — band 3 threshold
  0.605 → 0.680, band 2 0.572 → 0.580 (0.585 in one point),
  band 1 0.562 → 0.564, joint points (0.562, 0.580, 0.680) and
  (0.564, 0.580, 0.640); at the original bands the gap rises to
  0.51708 (tail composed) at ε = 1/500, at a LOWER score than
  candG (0.006967 vs 0.010360 — same bands, more slack, not a
  stronger statement). Frontier mapped (band 1 caps c1 ≈
  0.066–0.067 at the deep patch; band 2 ≈ 0.09–0.095 alone;
  band 3 ≈ 0.18–0.20 alone; fixed-band ε-ladder plateaus at
  ε ≈ 0.0015–0.002, collapses at 0.001 under the tail-ratio
  cap; Σ|b| saturation ≈ 1.70). Do not re-run this LP family
  at these shifts/lengths.

## Experiment log
- 2026-11-21 EXP01 (E1): copied row383 to exp01-baseline/, decompressed
  row378_exact.json + tail CSV, ran verify_spectral383.py with
  python-flint 0.9.0 (venv /tmp/flintenv). Runtime 13 s. Result: replay
  output matches spectral383.json EXACTLY on all 14 certified values
  (score_lower 0.0098858898430937020…, moment 99.186384435239…, bands,
  rectangles). tail_recounted=false (stored tail table used, hashes
  checked by the harness). Verdict: harness works locally; E2/E5/E6
  variations can be run and compared against this baseline.
- 2026-11-21 EXP03 (E3): ZF2 reality check against published explicit
  zero-free regions (full write-up: exp03-zfr/ZFR-CHECK.md). Applied the
  best Dedekind-zeta regions to ζ_E (E/K unramified quadratic, n_E = 210,
  log d_E = 797.05; zeros of L(s,χ) are zeros of ζ_E). Best source:
  Das–Gaba–Lee–Savalia–Wong 2025 (arXiv:2506.19319), Thm 1.2 (small
  ordinate, A = 11.51910) and Thm 1.1 (C = 12.21124, 9.54177, −11.59548,
  4.57803); Kadiri 2012 and Lee 2020 are slightly weaker at these
  parameters. Result: literature boundary at band heights is only
  Re s ≥ 0.99986–0.99989 (deficit ≈ 1.1–1.4×10⁻⁴), vs ZF2's required
  Re s > 0.63 (Ω2) / 0.562 (row383 weakest band). Gap ≈ 0.370 in Re;
  deficit shortfall factor ≈ 2.7×10³–4.0×10³. Even the conditional
  Deuring–Heilbronn region (Das Thm 1.3) reaches only 0.99931, and
  Kadiri's Dirichlet R = 5.60 generously misapplied reaches only
  0.99955–0.99978. Exceptional-zero caveat checked and immaterial: the
  allowed exceptional zero is real (Im = 0), all band points have
  |Im| ≥ 0.26, and non-real small-ordinate zeros are excluded outright
  down to the computed boundary. Verdict: ZF2-from-literature is DEAD;
  do not retry unless constants improve by orders of magnitude.
- 2026-11-21 EXP02a (E2a): Hadamard point σ varied, everything else in
  fixture383.json identical to baseline (σ = 7/5: score_lower
  0.0098858898430937020…, moment 99.186384435239… < 100, bands Re >
  281/500, 143/250, 121/200). Copies in exp02a-sigma65/ and
  exp02a-sigma85/; only "hadamard_real_abscissa" edited; runtime ~9 s
  each.
  - σ = 6/5: verifier ABORTS, exit 1, no output JSON. AssertionError at
    verify_spectral383.py line 267: certified moment upper bound
    133.2333448343481425486… exceeds the fixture moment_threshold 100.
    Score and bands are never computed. Verdict: certificate breaks —
    σ = 6/5 badly worsens the Hadamard moment bound (99.19 → 133.23);
    dead as a drop-in variant.
  - σ = 8/5: verifier ABORTS the same way, exit 1, no output JSON.
    Moment upper bound 107.9495764860553089217… > 100. Verdict:
    certificate breaks — σ = 8/5 also worsens the moment bound
    (99.19 → 107.95), though less than 6/5; dead as a drop-in variant.
  - Note: baseline σ = 7/5 passes the moment threshold with only
    0.81 to spare, and BOTH neighbours fail, so 7/5 is at/near a local
    optimum of the moment bound in this fixture; the σ direction of E2
    is exhausted for single-field changes. (The threshold 100 is not a
    free knob: it pairs with ε = 1/100 in the contradiction
    −ε·Mχ > −1, so rescuing a variant would mean redesigning ε and the
    band rectangles together — that would be a different experiment,
    not E2a.)
- 2026-11-21 EXP04 (E4): δ★ 4-lift inspection. Full details:
  exp04-delta-lift/NOTES.md. (1) Replayed verify_four_lift_target384.py:
  output matches four_lift_target384.json EXACTLY (δ★ mask
  0x4125e122ae5103, local code 0x44b88774c94772d6bc5c8f05827, real
  signature 0x1e, dyadic obstruction 0, NOT_DETERMINED). (2) E4's
  premise is VOID: no single place can witness non-lift. The
  Bockstein obstruction ∂_v vanishes on local Kummer classes at
  every v, and b_v ∘ κ_{4,v} = κ_{2,v} implies every local
  Selmer-2 class lifts to a local Selmer-4 class; row385 §6 indeed
  proves the global H^1(Q, J[4]) lift of δ★ exists unconditionally.
  Place-by-place lift checks should NOT be run. (3) The decision is
  purely global (row385, audit PASS_SCOPED_DEPENDENT per row386):
  CT pairing b has rad(b) = im(Sel4 → Sel2), b ≡ 0 on the 9-dim
  unit Selmer 𝒰, and lift ⟺ q★ = 0 for a single class
  q★ ∈ Cl(O_K)/2Cl(O_K) defined by χ(q★) = (−1)^{b(δ★, η_χ)}.
  Non-lift would give rank ≤ 7 + c_Cl (−30 ⇒ c_Cl ≥ 3).
  (4) Independent check done here: row385 §3's finite certificate
  recomputed from scratch — alternating forms on F_2^9 (36 comps),
  radical conditions from the 8 known classes (cf, a1, 49, 0e, a8,
  6b, f6, 51) have rank 36, only solution b = 0; rank(known) = 8,
  rank(known + δ★) = 9. Confirms b|_𝒰 = 0. (5) Exact blocker
  (row385 §7's own programme, not yet done): construct q★'s
  representative ideal 𝔞★ from the CT functional λ★ (needs an
  explicit cocycle for the H^1(J[4]) lift + local corrections),
  then test [𝔞★] in the recorded relation lattice. Asymmetry: the
  lattice can only PROVE q★ = 0 (δ★ lifts, route closes with no
  gain); proving q★ ≠ 0 needs an explicit unramified class
  η ∈ ℋ_nr with b(δ★, η) = 1, i.e. the dual of T1's generation
  wall. Obligation NOT discharged; no credit claimed.
- 2026-11-21 EXP05 (E5): row384 averaging generalized from 3 characters
  to 7 (c_Cl ≥ 3 case). Full write-up: exp05-avg7/NOTES.md. Baseline
  row384 replayed byte-identical (45 s, --recount-tail 4). Change: only
  the fixture field number_of_nontrivial_characters_in_average 3 → 7
  and the verifier's assert (lab copy only); the odd-power bound at
  undetermined primes improves −1/3 → −1/7 (if the F2³ pattern w ≠ 0,
  exactly 3 of the 7 nontrivial characters give +1 and 4 give −1).
  New certified score ≥ 0.0911527542420397790… (was
  0.0523946411808995256…), prime term ≥ 0.4079279534386562419…, moment
  unchanged 99.186384435239… < 100. Narrowing (6 candidates): uniform
  Re raises c = 3/20, 17/100, 1/5, 1/4 all FAIL in band 1 (subdivision
  depth 42 near u → c, t ≈ 0.71–0.75); pointwise diagnostic (not a
  certificate) shows a genuine Re φ < 0 patch at t ≈ 0.55–0.65 for
  u ≥ 0.15, so band 1 caps at c = 7/50 and band 2 at c = 9/50 for this
  test function. Mixed candidates PASS: cand6 certifies, for c_Cl ≥ 3,
  at least one of the 7 characters has a zero with Re > 16/25 = 0.64 on
  |Im| ∈ (13/50, 77/100) or Re > 17/25 = 0.68 on |Im| ∈ (103/100, 73/50)
  (threshold and ε raised to 9/100, contradiction gap 9/20; outputs
  exp05-avg7/avg7_result.json, fixture_avg7_narrowed.json). |Im| bands
  unmoved — shrinking them is blocked by the same φ patch. Verdict:
  real but modest sharpening of the c_Cl ≥ 3 necessary condition;
  −30 NOT closed, no exclusion; hard core remains c_Cl ∈ {1, 2} plus
  ZF-type zero-freeness in every case.
- 2026-11-21 EXP02b (E2b): cosine-weight re-optimization scout. Full
  write-up: exp02b-weights/NOTES.md. Harness reproduced the baseline
  exactly (score 0.009885889843093703, moment 99.186384435239). Findings:
  (1) the score is affine in the weights (dscore(+delta) = -dscore(-delta)
  exactly in every tested move), so score-only optimization is degenerate
  -- it points toward killing the modulation (w0 -> 1); the weights are
  chosen against exterior positivity, not score. (2) Dominance margin
  w0 - sum|b_i| = 0.001998 at baseline, so +0.01 on any positive weight
  breaks the verifier's dominance assert. (3) Best score candidate
  (shift 51/20, delta=-1/50, score-only 0.066658) passed score/moment in
  the FULL verifier but FAILED check_exterior at depth 42, u->1/2,
  t~=1.70 (top of the gap below band 3). Uniform scaling x0.9 / x0.8
  raised the score only +0.00227 / +0.00454; x1.1 / x1.2 break dominance.
  Coverage: single moves delta in {+-1/100, +-1/50} for idx 1-11 only
  (scout killed by 280 s timeout before idx 12-19). Verdict: single-weight
  direction EXHAUSTED, do not retry; a positivity-constrained
  optimization remains unattempted and is a different experiment.
- 2026-11-21 EXP06 (E2b, full): positivity-constrained LP re-optimization
  of the row383 weights + joint ε / threshold redesign. Full write-up:
  exp06-e2b-weights/NOTES.md. Method: exact affine gradient extracted
  with the verifier's own interval arithmetic (score = C + Σ g_j b_j,
  all g_j < 0; affine recon matched certified score to 7e-17); float
  φ evaluator validated vs phi0_series (worst err 1.8e-15); LP
  (HiGHS) maximizing score subject to pointwise-relative positivity
  vs baseline-at-ε, dominance ≥ 0.001, tail ratio ≤ 0.95ε; candidates
  rationalized to 1e-6 and judged ONLY by the full rigorous verifier.
  CERTIFIED PASSES (bands unchanged in all): candC (ε=9/1000) gap
  0.13629, candC2 gap 0.14679, candD (ε=17/2000) 0.191135, candD2
  0.201635, candE (ε=1/125) 0.24598, candF (ε=3/400) 0.306075, candF2
  0.316575, candG (ε=29/4000, score_thr 51/5000, moment_thr 9919/100)
  score_lower 0.0103597391213032410…, gap 140749/400000 = 0.3518725
  (baseline 0.029, ×12.1). ε and moment_threshold are legitimate
  redesign knobs (PROOF §4: ε is a free constant policed by exactly
  the verifier's asserts; 99.1863844352390… < 9919/100). FAILURES:
  candA/candB (grid-v1 LP, ε=0.0075/0.007) died in check_exterior at
  depth 42, band-1 top edge u→0.062, t≈0.687–0.689 — grid v1 never
  sampled u=0.062 (flaw found and fixed in grid v2); candH (ε=0.007,
  v2, slack 8e-4) died at u→1/2, t≈3.3077 in the [2.12,8] gap
  rectangle. LP frontier (v2): ε=0.007 infeasible at slack ≤4e-4,
  ε=0.0075 needs slack ≥4e-4. BAND RAISING DEAD: float scan goes
  negative immediately past each u_max (cliff at t≈0.68/1.37/2.01),
  and LP with all bands +0.01 is infeasible at slack 5e-5 and 2e-4.
  Verdict: E2(b) DONE with a real certified improvement (score +4.8%,
  gap ×12.1, same bands); the remaining headroom in this fixture
  family is negligible (float score ceiling ≈0.0104 under rigorous-
  plausible positivity). −30 NOT closed; no exclusion; hard core
  unchanged. [SUPERSEDED IN PART by EXP11 (E9, 2026-11-21): the
  "BAND RAISING DEAD" verdict above and the ≈0.0104 ceiling were
  artifacts of the relative LP form + grid v2 resolution. The
  absolute-floor form on a 742,597-point grid certifies raised
  bands (0.562/0.572/0.605 → up to 0.562/0.572/0.680 and
  0.564/0.580/0.640) and a fixed-band gap of 0.51708 at ε = 1/500.
  See the EXP11 log entry and exp11-phi383-bands/NOTES.md.]
- 2026-11-21 EXP07 (E6): Deuring–Heilbronn repulsion variant. Full
  write-up: exp07-e6-repulsion/NOTES.md. The assumed zero can only
  enter through the derived budget Σ_{χ∈X} Z_in(χ) ≤ −G_N (the
  verifier has no slot for it). Certified budgets G_N: row383 per-char
  0.046155 (baseline) / 0.368671 (candG); row384 G_3 = 6.089742;
  EXP05 7-char G_7 = 42.696610 (base ε=7/200) / 4.509852 (cand6).
  Three obstructions, all quantified. (1) STRUCTURAL: one scalar
  budget cannot localize the other characters' zeros — for any proper
  subregion R' with inf Re φ < 0 outside it, unbounded multiplicities
  at one deep point satisfy the budget with the others zerofree in R';
  the only localization the formalism gives is the positivity region,
  which is assumption-independent. φ383/φ384 negative patches coincide
  (both minima at (u,t)→(0.5,0.44)), so two functions do not rescue
  it. (2) COUNTING FAILS: min Re φ over the band regions (arb point
  evaluations, verifier's own phi0; rigorous at sampled points) is
  −19.920 for φ384 on Ω2 (at u=0.5, t=0.435; band 2 only −1.742) and
  −24.191/−24.203 for φ383 baseline/candG, so one zero orbit supplies
  c_max = 79.68 (φ384) / 96.8 (φ383) of negativity vs budgets above:
  ratios G/c_max = 0.0005 (383 base), 0.0038 (candG), 0.076 (row384),
  0.536 (EXP05 base — closest), 0.057 (cand6), all < 1. Assumed-zero
  shift c1 = −4 Re φ(ρ1) ranges over [−18.9, +79.7] on Ω2 and never
  localizes. (3) CLASSICAL DH CHANNEL VACUOUS: full-group average
  {1,χ1,χ2,χ1χ2} (odd bound −1/3 → 0, diagnostic with repo prime
  machinery, arch/moment stand-ins flagged) gives S_G ≈ 0.120221,
  G_group ≈ 36.6, but the ζ_K pole term 2φ384(1/2) ≈ +90.7 exceeds
  it: the group inequality forces Σ Z_in ≤ +54.1, i.e. nothing; and
  Z_in(ζ_K) has no available lower bound anyway (EXP03). Criterion
  for any future attempt: −min_R Re φ < G_N/4 (EXP05 config would
  need min > −10.67 vs actual −19.92). Verdict: E6 DONE, negative;
  do not retry with these test functions. −30 NOT closed; no
  exclusion; no credit.
- 2026-11-21 EXP08 (E2c): length-splitting variants of the row383
  test function. Full write-up: exp08-e2c-lengths/NOTES.md.
  Baselines (original fixture; EXP06 candG) replayed EXACTLY.
  Structural finding first: in verify_spectral383.py the moment is
  EXACTLY lengths-independent (prime_bounds' log_deriv never touches
  f; the certified moment string 99.1863844352390573896… is identical
  for n=6, n=12 and rescaled length sets at σ=7/5), so lengths move
  only score / positivity / tail ratio, and σ retries cannot be
  rescued by lengths (σ=8/5 / 6/5 joint gaps ≤ 0.2568 / 0.0735 at
  the best certified score — dominated, not run). Float screen
  (validated to 1e-10 on both baselines; its n=12 arch value is a
  cancellation artifact — arb gives E3 score −0.334114128000016…)
  over 19 variants: splitting or shrinking the big component
  (229/25), merging smalls, redistributing, equalizing, n=2/3/12
  are all ≤ baseline or strongly negative; tiny components
  (≤0.115) explode the tail ratio (D4: 22.69, F1: 1.618). Only two
  non-negative directions. (1) E4 = split one mid component
  (397/200 → 397/400×2, n=7): float score 0.010653 (base w) /
  0.010987 (candG w), but positivity screen min g = −0.0294 at
  (0.5, ~2.52) and the FULL verifier with candG weights FAILS
  check_exterior at depth 42, u→1/2, t≈4.0878 ([2.12,8] gap).
  Absolute-LP frontier (grid, slack 0) vs the candG-beating score:
  ε=0.00725: 0.009578 vs 0.010200; 0.0075: 0.009751 vs 0.010436;
  0.008: 0.010094 vs 0.010908; 0.009: 0.010775 vs 0.011853; 0.01:
  0.011447 vs 0.012810 — shortfall grows with ε; relative-form
  feasibility needs slack s* = 0.00292. E4 DEAD. (2) A4 = uniform
  rescale ×1.001 (T = 14.488474 < log LIMIT): CERTIFIED PASS with
  baseline weights (candA4base2/; fixture383-A4.json,
  result-A4.json): score_lower 0.0099193768789228958… (+3.35e-5
  over baseline), tail ratio 0.0077811469051161555… < 1/100,
  moment identical, bands identical; gap 119/2500 = 0.0476 at
  thresholds (99/10000, 9919/100), ε=1/100 (0.0371 at
  (49/5000, 9919/100)). A4 + LP weights at ε=29/4000: predicted
  0.010431–0.010462 but grid min g ≈ 0 along the u=1/2 edge in
  [2.12,8]; FULL verifier FAILS twice at depth 42, u→1/2,
  t≈4.1786 and t≈4.1918 (grids up to 823,776 pts with surgical
  patch). Also recorded: the pure relative LP form without
  EXP06's floor is unsound at ε<1/100 (min g −5.0e-4 at slack
  1e-4). Verdict: E2(c) DONE — one small certified improvement
  (A4 rescale, baseline-weight configuration only), no variant
  beats candG's 0.3518725, lengths are rigid at these
  shifts/support. E2 fully exhausted. −30 NOT closed; no
  exclusion; no credit.
- 2026-11-21 EXP09 (E7): tail extension to 10^7. Full write-up:
  exp09-e7-tail/NOTES.md. Semantics: c(p) = deg gcd(f mod p,
  x^p − x) = # distinct roots of the degree-105 stem polynomial
  in F_p, for primes 5003 < p ≤ LIMIT (row382_inputs
  .degree_one_count = original row379 C++ roots379.cpp).
  VALIDATION: new counting code (count_roots.py, python-flint)
  reproduced the stored table on all 147,058 primes
  BYTE-IDENTICALLY (sha256 572183b2…, sum 147,527; 28.4 s,
  3 workers). EXTENSION: 516,851 primes in (1982760, 10^7] in
  8 checkpointed chunks (124 s), sum 516,809; assembled
  tail_roots_10m.csv: 663,909 rows, sum 664,336, 6,551,781
  bytes, sha256 e5c2e2bed583ed3ac20c4ceb956a2a62438e558a679746aada89889c61735644.
  CERTIFIED (full verifier, lab copies with LIMIT = 10^7):
  score_lower IDENTICAL in both fixtures (base
  0.0098858898430937020…, candG 0.0103597391213032410…) —
  structurally forced, since score primes need log p < 7237/500
  (p ≲ 1.93·10^6), all already tabulated; bands, rectangles,
  tail ratio identical. moment_upper 99.1863844352390574… →
  98.4550015213825703… (Δ = 0.7313829138564871, both fixtures):
  Chebyshev cutoff term 1.5424274344666490 → 0.8074447222926290
  minus the exact sum over newly covered primes
  0.0035997983175329. Gap is threshold-defined, so as-is it is
  unchanged; with EXP06-style threshold redesign, extra FULL
  runs certify base (moment_thr 99) gap 39/1000 = 0.039 and
  candG (moment_thr 9846/100) gap 71433/200000 = 0.357165.
  CEILING: residual Chebyshev term at 10^7 is 0.8074447222926290
  and LIMIT < B² = 25,030,009 caps it below at 0.5594076547027249,
  so ≤ ≈0.248 more moment is ever buyable this way. Verdict:
  E7 DONE — a real but one-dimensional (moment-only) gain;
  the whole E-queue is now exhausted. −30 NOT closed; no
  exclusion; no credit.
- 2026-11-21 EXP10 (E8): EXP06 machinery (affine gradient + float φ
  evaluator + LP + rationalize + full-verifier adjudication) applied
  to φ384. Full write-up: exp10-combo/NOTES.md. Baselines replayed
  exactly (7-char score 0.0911527542420397790…, 3-char
  0.0523946411808995256…). Gradient cc=7: g_0 = +0.168, g_1 = +0.159
  (the (0, 1/40) pair is a near-free dial, g_1 − g_0 ≈ −0.009);
  float evaluator validated vs transform_series to 3.3e-14. KEY
  METHOD FINDING: EXP06's relative LP form chains the LP to the
  baseline weights (~44k near-baseline constraints) and cannot
  raise bands at all (even c1 = 0.145 infeasible); the ABSOLUTE
  form (g_new ≥ FLOOR = 2e-4 on the whole required region — honest
  because baseline min g is 5.6e-4 at the weight-independent
  (1/2, 12) corner) unlocks the family. CERTIFIED, 7-char
  (c_Cl ≥ 3): threshold-only redesign at baseline weights already
  gives gap 0.6384 (thr 911/10000, M_thr 9919/100); relative ladder
  A–D gaps 1.18685 / 1.48442 / 1.6828 / 1.75574 (ε 0.085 → 0.079,
  frontier set by the (0.140, 0.652) band-1 edge, LP-infeasible
  ≤ 0.0785 at FLOOR 5e-4); absolute ladder at bands (0.64, 0.68):
  candE (ε=0.06) score 0.1053145701385321485… gap 5.08935, candH
  (ε=13/400) gap 234983/40000 = 5.874575, +EXP09 tail (moment
  98.4550015213825703…, M_thr 9846/100) gap 58983/10000 = 5.8983.
  CERTIFIED narrowings (ε=0.06, Pareto): (0.65, 0.70) 2.5326,
  (0.65, 0.71) 2.22285, (0.65, 0.72) 1.8816, (0.65, 0.73) 1.51935,
  (0.65, 0.74) 1.13085 → 1.17465 with tail, (0.65, 0.76) 0.3066,
  (0.655, 0.70) 1.4406, (0.655, 0.71) 1.1466, (0.66, 0.70) 0.33285.
  CERTIFIED, 3-char (c_Cl ≥ 2): candR3 (ε=7/200, bands 0.63/0.63)
  score 0.0709356122343433040… gap 3.9571 → 3.98265 with tail;
  candS3 (0.64, 0.66) gap 1.6212; candT3 (0.64, 0.68) gap
  1.33245 → 1.3653 with tail. FAILURES: candF (coarse grid) died
  at depth 42, (u→1/2, t≈2.5788) — grid hole, fixed by
  densification to 164,322 pts (candF weights show min gap
  g = −5.7e-6 at (0.5, 2.575) on the dense grid); first LP version
  falsely infeasible (equality-tight capped-floor rows; HiGHS) —
  every recorded infeasibility was cross-checked. FRONTIERS:
  fixed-band ε ≥ 0.0325 at FLOOR 2e-4 (ε=0.030 LP-infeasible:
  corner εW < FLOOR); Σ|b| saturates ≈ 10.62; band-1 c1 caps
  ≈ 0.16–0.165 at any ε. Verdict: E8 DONE with certified gains
  on both averages; −30 NOT closed, no exclusion, no credit;
  the bite still needs ZF-type zero-freeness (EXP03 gap ≈ 0.37
  in Re from literature).
- 2026-11-21 EXP11 (E9): EXP10's absolute-floor LP form applied to
  φ383 band narrowing (c_Cl ≥ 1). Full write-up:
  exp11-phi383-bands/NOTES.md. Pipeline as EXP06/EXP10 (affine
  gradient from EXP06, float evaluator revalidated to 1.8e-15,
  baselines replayed exactly); LP form is ABSOLUTE (g_new ≥ FLOOR
  on the whole required region; FLOOR capped by the (1/2, 8)
  corner, εW = 0.01373ε there) on a tagged grid built out to
  u = 0.22/0.24/0.30 in the bands. CERTIFIED narrowings (all
  ε = 29/4000 except candC at 27/4000; |Im| windows unchanged):
  K-narrow-d bands (0.562, 0.572, 0.680) score
  0.0081125003351975160… gap 46249/400000 = 0.1156225, with
  EXP09 tail (moment 98.4550015213825703…, M_thr 9846/100) gap
  24183/200000 = 0.120915; K-narrow-a (0.562, 0.580, 0.660)
  score 0.0080622749120922782… gap 0.1103725 → 0.115665 with
  tail; K-narrow-b (0.564, 0.580, 0.620) gap 0.0946225;
  K-narrow-f (0.562, 0.585, 0.660) gap 0.0473725; K-narrow-c
  (0.564, 0.580, 0.640) gap 0.0549675; K-narrow-e (0.562,
  0.580, 0.680) gap 0.0263725. CERTIFIED fixed-band: K-fixed-a
  (ε = 1/500, FLOOR 6e-6) score 0.0069670144039762558… gap
  25781/50000 = 0.51562 → 12927/25000 = 0.51708 with tail —
  above candG's 0.3518725/0.357165 on the gap metric, but at a
  LOWER score (0.006967 vs 0.010360): same bands, more slack,
  not a stronger statement. FRONTIER (LP diagnostics, viability
  = gap > 0, cross-checked at ≥ 2 ε): band 1 caps at c1 ≈
  0.066–0.067 (score falls ~0.0014 per +0.002 near the cap; the
  deep patch at (0.5, 0.44) is the obstruction); band 2 caps
  ≈ 0.09–0.095 alone, ≈ 0.085 combined; band 3 caps ≈ 0.18–0.20
  alone; joint points (0.062, 0.09, 0.16) and (0.066, 0.08,
  0.12) are past the frontier (LP gap < 0 at ε = 0.00725).
  Fixed-band ε-ladder (LP): gap rises to a plateau ≈ 0.51 over
  ε ∈ [0.0015, 0.002] and collapses at ε = 0.001 (score
  −0.0266); at ε ≤ 0.0065 the tail-ratio cap 0.95ε is the
  binding constraint. Σ|b| saturation ≈ 1.70 (= baseline total;
  cap ∈ {1.7, 2.5, 4.0} identical at ε ≥ 0.0065 — unlike
  φ384's ≈ 10.62). FAILURES: K-fixed-a died at depth 42 three
  times before passing — (i) 1e-6 rationalization (rounding
  moved g by −1.7e-5 at the (0.5, 3.295) dip, swamping FLOOR
  6e-6; fixed by a 1e-7 grid), (ii) grid v1 (141,975 pts):
  continuum dip at (0.5, t ≈ 2.4586) between t-step-0.01 edge
  samples, (iii) grid v2 (268,200 pts): band-1 top edge dip
  −1.79e-5 at (0.062, 0.686), ~0.002 wide in t (EXP06 candA/B's
  site; cliff |g″| ≈ 31 ⇒ sag ≈ 31h²/8). Grid v3 (742,597 pts,
  cliff windows at t-step 0.0005) passes everything. Verdict:
  E9 DONE — EXP06's "band raising is dead" is superseded (it
  was the relative form + grid resolution, exactly as EXP10's
  φ384 finding predicted); the c_Cl ≥ 1 necessary region is
  now as small as (0.562, 0.572, 0.680) / (0.564, 0.580,
  0.640) on the certified Pareto frontier. −30 NOT closed; no
  exclusion; no credit; the bite still needs zero-freeness in
  the narrowed bands (EXP03: literature reaches Re ≈ 0.99986,
  deficit shortfall ~3×10³, unchanged).
