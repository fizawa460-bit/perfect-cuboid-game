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
  unchanged; ε ≲ 0.007 and band raising are dead in this family. Do
  not retry weight re-optimization at these shifts/lengths; (c)
  different length splits at the same support — still OPEN (the only
  remaining E2 sub-item). Success = strictly narrower bands or larger
  gap than 29/1000, with interval arithmetic.
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
  row384 average. Untried in the materials.
- E7. Tail extension: recompute first-degree prime counts for p up to
  10^7 (repo tail stops at 1,982,760) and re-run E2 with the longer tail;
  measures how much of the score is tail-limited. (Compute-heavy; the
  row383 verifier's --recount style path recounts only the stored range,
  so this needs new counting code: factor f mod p for ~664k primes.)

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
  unchanged.
