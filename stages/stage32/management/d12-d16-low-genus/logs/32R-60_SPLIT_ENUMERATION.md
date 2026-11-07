# 32R-60 Split enumeration (2026-10-24) — breakthrough candidate

Idea: x ∈ Pic(S~) ↔ (y, m), y = π_L(x) = x + Σ (x.E_j/2) E_j ∈ Λ (rank 16, det -1, i.e. odd unimodular I_{1,15}),
m = (x.E_j) ∈ Z^48_{>=0}. Lifts of y differ by Sat = Pic ∩ span(E) (E-span has index 2^10 in Sat), so
m ∈ m~ + M0, M0 = {v : v mod 2 ∈ D}, D = 10-dim binary code (RREF information set of 10 positions fixes the parity
of the other 38). Constraints: x.q >= 0 for the 92 non-exceptional curves <=> Σ μ_j(q) m_j <= b_q (packing, small
right-hand sides); x^2 = y^2 - Σ m^2/2 >= c2min. Hurwitz e >= d+4-4g and Σm^2 >= e give y^2 >= -d/2.
Pipeline (split/): yenum.c = Fincke-Pohst in the rank-15 kernel of K on Λ with radius d^2/16 + d/2 and the b_q >= 0
filter at the leaves; msearch.c = DFS over m (10 free-parity positions first, then 38 with forced parity, packing
slack, Σm^2 bound); split_run.py reconstructs x, applies the same inventory rule as the certified runs.
Validation (exact class sets):
- d = 8 : 1830 classes, identical to the certified d8 leaf (old method ~6 h on 11 threads) — new ~8 s.
- d = 10: 256 classes, identical to classes_d10.json (old ~1 day) — new ~3 min.
Research prototype: floating Fincke-Pohst with margins (to be certified like certified_enum), exact recheck of x.
Note: the new method returns the FULL class set (no symmetry reduction); the certified runs returned orbit reps.
- d = 12: y-stage 136 s (3.0e8 nodes, 8.4e6 y), m-stage 2846 s, total ~50 min: 1,917,312 classes in the inventory
  (full set). All 29,400 classes found so far by the certified production run are contained (missing 0).
  Next: orbits (split/orbits.py), base-locus sweep on geometric reps, final cross-check when production finishes.
- d = 12 decisions (stoll/f12_*): 2029 geometric orbit reps (lattice orbits 778; class set closed under both groups).
  C² < 0 (1999 reps): 1917 h0 = 0; 82 h0 = 1: 81 residuals of degree 12 with genus >= 3 (char p, P3 projection:
  genus 3 ×6, 4 ×3, 5 ×48, 6 ×16, smooth p_a 5/6 ×8); rep 1215 residual degree 14 contains no known curve, hence no
  degree-12 component (the complement would be a conic, and all conics are known) -> no curve.
  No class with C² = -14 (smooth rational) exists at d = 12.
  Open: 30 reps with C² = 0 (pencils, h0 = 2). 21 of them: K - x = two disjoint conics + 12 exceptional (residual
  pencil of hyperplanes through the span of two conics); 9 others to classify.
- C² = 0 (30 reps): 28 reps have (n1,e) = (6,12): balanced equality g = 1 (g = 0 needs e >= 16) -> excluded by the
  32R-39/42 lemma (slice 6|12 was already dropped in production). Remaining 1959 (6,16) and 2020 (4,16): g = 1 only.
  Both are base-point-free pencils |x| (h0 = 2) of genus-7 curves on S~. A genus-1 member needs δ = 6.
  * Exc: all m_j <= 1 -> no singular point of any member on an exceptional curve.
  * Critical points of the pencil (char 10009, 5x5 minors of [grad S_i ; F1 grad F0 - F0 grad F1], saturated by base
    locus and nodes), with three decompositions D, D', D'' of 2K - x so that every known curve with x.Γ >= 2 is avoided
    by some decomposition; the triple intersections of dangerous curves (6 triples) are empty off the nodes; vertical
    curves (x.Γ = 0) cannot meet an irreducible fibre.
    2020: no critical point at all (all three decompositions) -> every non-known fibre is smooth (genus 7).
    1959: exactly 8 reduced critical points (on curves 54, 56), over 4 values of t (u^4+3478u^3-...), 2 per fibre ->
    those fibres have δ = 2 (genus 5 if integral); all other non-known fibres are smooth.
  => no genus <= 1 curve in these classes. d = 12 is resolved at research level (no curve of degree 12 with genus <= 1).
  Caveats: char-p computations (a char-0 critical point could in principle reduce into the removed loci mod p),
  floating y-enumeration (to be certified), the production cross-check still running.
- 32R-62 streaming version split/splitenum.c + split_stream.py (y-stage, exact y^2, m-stage in one pass; shards;
  vectorised chunked reconstruction, output split_d{d}.npy): d = 10 in 21 s, d = 12 stream stage 463 s on 2 shards,
  identical class sets (256; 1,917,312). d = 14 started 2026-10-24 (2 shards).
- FINAL CROSS-CHECK d = 12 (split/crosscheck_d12.py): certified production run complete (statuses COMPLETE 748,
  CONGRUENCE_EMPTY 16185, NO_BVECTOR 62, no errors), 33,147 classes. Split set restricted to the production
  inventory rules: 1,274,512 classes in 519 lattice orbits. production ⊆ split (0 missing) and every lattice orbit
  contains a production class (0 orbits missed) -> the two independent methods agree exactly up to the symmetry group.
- d = 14 (2026-10-24): streaming split, 12 shards, stream stage 4474 s: 7,483,360 solutions, 2,068,736 classes in
  the inventory (split/split_d14.npy). orbits.py rewritten (void-view searchsorted + scipy connected components,
  166 s): class set closed under both groups; 560 lattice orbits, 1487 geometric reps
  (C²: -10 ×6, -8 ×151, -6 ×290, -4 ×522, -2 ×352, 0 ×161, 2 ×5). No C² = -14 / -12 class: every d = 14 candidate
  would be a singular curve. All 1487 reps have a decomposition of mK - x (m <= 3); sweep stoll/f14/ running.
  C² >= 0 (stoll/c2nonneg_d14.py), (C², n1, n2, e): Hurwitz e >= 18 - 4g; balanced lemma kills equality n = 7.
    (0,7,7,14) ×112 and (2,7,7,14) ×2: g = 1 equality, g = 0 impossible -> excluded.
    (0,7,7,18) ×30: g = 0 equality excluded, g = 1 open. (0,7,7,16) ×16, (2,7,7,16) ×3: g = 1 only, open.
    (0,7,7,22) ×2: g = 0, 1 open. (0,5,9,18) ×1: g = 1 only (equality, unbalanced), open.  -> 52 reps open.
- d = 14 sweep done (stoll/f14/, summary.json): h0 = 0 ×1318, h0 = 1 ×161, h0 = 2 ×8 (5 runs timed out at 3000 s:
  69, 1062, 1066, 1204, 1270, all h0 = 1). Note: for d = 14, χ(x) = 8 + (C² - 14)/2, so C² = 0 gives χ = 1
  (unique member, not a pencil as at d = 12); C² = 2 gives pencils.
  h0 = 1 with residual degree < 14 (8, 10, 12; 17 reps): the unique member contains a known curve -> reducible ->
  no irreducible curve. (7,7,14) h0 = 1 reps (48 + 5): lemma. Genus jobs (char p, P3 projection) f14/g14_*: 96
  (residual degree 14 ×85, degree 16 ×6, timed-out ×5).
  h0 = 2: 1179, 1244 (C² 2), 1314, 1345 (C² 0) are (7,7,14) -> lemma. Open pencils: 1309, 1382, 1384 (C² 2,
  (7,7,16)), 1480 (C² 0, (5,9,18)); base locus outside D empty; critical-point runs stoll/c14/crit_*.
  (The first C² >= 0 crit batch assumed pencils for all 52; stopped, superseded by the sweep.)
- d = 14 pencils (stoll/c14/fib_*): critical scheme of F0/F1 (char p), fibre distribution via u = F0/F1 on a chart
  (no critical point at F1 = 0 or on the chart hyperplane). Second/third decompositions cover every D-curve with
  x.Γ >= 2 (c14/mkalt.py, mkalt2.py); pairwise intersections of hidden curves (c14/pairs.sing, char 0): 1309 has
  points on 67∩92, 68∩90, 1384 on 51∩59, 52∩57 -> third decomposition avoiding all four.
  1309 (3 decomps), 1382 (2), 1384 (3): all critical points reduced (ordinary nodes, μ = 1), at most 2 per fibre
  in each decomposition -> δ <= 6 < 8 needed for g = 1 (p_a = 9). Caveat: the 2 base points (x² = 2) are removed
  by the saturation; a member singular at a base point needs a tangential base point (not yet checked).
  1480 (C² 0, base-point free, 2 decomps): 36 reduced critical points, 1 per fibre -> δ <= 2 < 7. All 4 pencils
  have no genus <= 1 member (modulo the base-point caveat for the three C² = 2 ones).
  Triples (c14/triples14.sing, char 0): the pair points of 1309/1384 avoid every hidden curve of the third
  decomposition -> every point off the nodes is visible in some decomposition. Base-point caveat closed: base points
  lie on D-curves in every decomposition (base locus outside D empty); a member singular at p meets each
  non-component curve through p with multiplicity >= 2, so p would lie only on hidden curves (x.Γ >= 2) of every
  decomposition (or on Exc with m_j <= 1, impossible) -> empty by the pair/triple checks.
  => the 4 d = 14 pencils contain no member of geometric genus <= 1.
- d = 14 h0 = 1, residual degree 16 (5, 6, 105, 137, 428, 501; f14/k14_*): no known curve inside the residual ->
  as for d12 rep 1215, no degree-14 component (complement would be a degree-2 curve, i.e. a known conic) -> excluded.
  Genus jobs (degree-14 residuals) running: smooth P3 images finish in minutes, singular ones take 45-60+ min in
  normal.lib genus (329, 569: genus 7).
- d = 14 genus jobs complete (f14/genus_results.json, 90 reps incl. the 5 earlier time-outs): geometric genus (char p,
  P3 projection) 2 ×2 (1348, 1349), 6 ×16, 7 ×34, 8 ×8; smooth P3 image with p_a 6 ×1, 7 ×8, 8 ×21. All >= 2
  (char-p geometric genus <= char-0 genus).
  => d = 14 RESOLVED at research level: no curve of degree 14 with geometric genus <= 1 on S (beyond none known).
  Tally of the 1487 geometric reps (exact, each counted once): h0 = 0 ×1318; balanced lemma (7,7,14) ×57;
  reducible unique member (residual degree < 14, not (7,7,14)) ×12; residual degree 16 without known conic ×6;
  genus >= 2 ×90; pencils with too few singular points ×4. Total 1487, nothing open.
  Same caveats as d = 12: char-p computations, floating y-enumeration (to be certified).
- 32R-64 speed-ups for d = 16 (2026-10-24):
  * sharding: the old rule (top-level value mod nshard) left most shards empty at d = 14 (3 shards did ~95% of the
    nodes). splitenum.c now deals the subtrees at level n-1-SPLIT_DEPTH (default 4) round-robin: d = 12 on 12
    shards balanced (23-27M nodes each), stream stage 463 s (2 shards) -> 113-125 s; identical 1,917,312 classes.
  * split_stream.py: block parsing of the shard outputs, int8 dedupe via 64-byte void view, split_d{d}.npy now int8,
    JSON only for d <= 12 or when comparing. Fixed overhead (library setup) ~2 min.
  * d = 14 rerun with the new sharding for timing + identity check against split_d14_v1.npy.
  * d = 14 rerun (balanced sharding): stream stage 4474 s -> 1947 s, identical 2,068,736 classes. Machine has 6
    physical cores (i7-10750H, 12 threads): per-shard speed drops ~3x when 12 shards run.
  * profile (SPLIT_NOM): the m-stage is 97% of the time. Depth profile: the DFS over the 10 free-parity positions
    reaches 88M nodes at depth 10 per 0.73M y-leaves, and 99.98% die at the parity check of the 38 forced positions.
  * parity-first m-search (splitenum.c, 32R-64): DFS over the 10 parity bits first, charging the minimal demand
    (m_j >= parity) of every position as soon as its parity is determined (lastdep), then the value DFS with full
    look-ahead (needq, needs2). Single d = 12 shard 60 s -> 8.6 s with identical output (sorted md5).
    d = 12 stream stage 29.7 s (identical class set); d = 14 stream stage 205 s (was 4474 s), identical classes.
    Old versions kept as splitenum_v2.c (before look-ahead), splitenum_v3.c (look-ahead only, no gain).
  * d = 16 started 2026-10-25 with the parity-first enumerator (12 shards).
- 2026-10-25 incident: the first d = 16 run wrote 68 GB of raw solution text and filled drive C (0 bytes free).
  Stopped, s16_out_* deleted (regenerable), 64 GB free again; logs/memory checked intact.
- 32R-65 in-C reduction (splitenum.c invmode, driver split/split_reps.py d nshards): exact integer reconstruction
  of x (SMinv scaled by its common denominator; non-integral -> abort), inventory filter in C, and a geometric
  orbit-representative test (keep x iff pe = P140.x is lexicographically maximal over the 1536 permutations, the
  group closed from Stoll's 9 generators). Only the reps are written; Python checks Σ orbit sizes = #inventory.
  d = 12: 1,917,312 classes, 2029 reps, Σ orbits OK, 59 s total. d = 14: 2,068,736 classes, 1487 reps, same C²
  distribution, 3 min 24 s total (was 75 min + orbits). d = 16 started with split_reps.py.
