# 32R-67 Unibranch / multibranch split of the split-enumeration classes (2026-10-25)

## Link to the Stage32 structure (repo stages/stage32)
- 32-01 (AUDITED_COMPLETE): FULL178 numerical census of the UNIBRANCH g <= 1 population (FSM Thm 3.1 scope).
  Current certified upper bound 726,240,487 compressed N220 terminals in 530 strata (MAIN-STATE.json,
  management/fixed-direction-certificates/RESULT.json). Count semantics: compressed prefixes, NOT Picard classes.
  Per-row data: g0 d = 8..44, g1 d = 8..48, nothing above (d=16: g0 337,445, g1 734,124 terminals).
- The degree cap 44/48 comes from management/unibranch-node-hurwitz (hostile-audited proposition):
  unibranch, g in {0,1}, not a fibre component  =>  nu >= e/2 + max(n1,n2) - 2g + 2, nu = #{j : m_j > 0}.
  Multibranch curves only satisfy the weaker 2B >= e + d - 4g + 4 (B = #points of C~ on Exc), which is what our
  inventory (Hurwitz e >= 2 max + 4 - 4g) uses.
- 32-02 effectivity (ACTIVE) and 32-03 multibranch (ACTIVE, no finite degree window proved) are open.
=> Our split enumeration covers BOTH populations degree by degree. Unibranch part is finite (d <= 48);
   multibranch part has no known degree bound.

## Split of the geometric reps (split/ub_split.py)
| d | reps | unibranch-compatible | multibranch-only |
|---|------|----------------------|------------------|
| 12 | 2029 | 219 | 1810 |
| 14 | 1487 | 739 | 748 |
| 16 | 1,737,363 | 71,697 | 1,665,666 (96%) |
d = 16 full run (split_reps.py, 32R-65): 2,484,463,444 classes, stream stage 12,336 s, Σ orbits = #inventory.
Note: the inventory's g1 cap e <= 2M+3 is a slicing rule only; per-genus unibranch tests must use the genuine
conditions (first C version used it and undercounted: 101 vs 219 reps at d = 12; fixed).

## Enumerator updates (splitenum.c)
- SPLIT_UB=1 (needs invmode): unibranch mode. Necessary score Σ_j (2[m_j>0] - m_j) = 2nu - e >= d used as a
  prune in the parity DFS (parity-1 positions add <= 1, parity-0 <= 0) and in the value DFS; exact per-genus test
  at the leaf. d = 12: 145,328 classes / 219 reps; d = 14: 1,024,768 classes / 739 reps (= ub_split). The prune
  is weak at these d (time almost unchanged).
- bitdfs with precomputed per-bit lists: d = 14 shard 62 s -> 47 s, identical sorted output.
- parity re-basis (greedy choice of new parity coordinates so that columns are determined early;
  SPLIT_NOREBASIS disables): 47 s -> 29 s, identical sorted output (normal and UB mode).
- Large d (towards 48) will need a different method: the y-ellipsoid (radius ~ d²/16) is far too big;
  packing constraints must enter the y-search.

## d = 16 judging
- reps_d16.json = the 71,697 unibranch-compatible reps (with orbit sizes, C²); stoll/judge.py 16 plan in 10
  parallel chunks, then base-locus sweep. Multibranch-only reps (1,665,666) are set aside for 32-03.

## 32R-68 (2026-10-25 evening)
- y-stage CS pruning in splitenum.c (cs_ok, only at levels <= slev so sharding is unchanged): d = 14 shard nodes
  150M -> 54M, identical sorted output; y-stage ~25% faster. 95% of FP leaves fail b_q >= 0 (d = 14).
- d = 16 sweep switched to char p (stoll/f16/*_p.sing; ~7-35x faster). Justification: reduction of the char-0
  ideal lies in the char-p ideal, so h0_p >= h0_0; Hilbert function of S equal in both (7, 24, 56, 104 for
  m = 1..4). h0_p = 0 => h0 = 0. First 8,637 results: h0_p = 0 x8617, 1 x20. Rep 50489 has no decomposition with
  m <= 3 (to do: m = 4).
- judge.py: chunked plan (d plan lo cnt), summary falls back to f{d}_{i}_p.out.
- Unattended chain run_chain_d16_d18.sh (log chain_d16_d18.log): wait for the sweep -> judge summary -> genus /
  conic jobs (grun, 2 h timeout) -> judge final (f16/final.log) -> d = 18 unibranch enumeration
  (split/reps_d18_ub.log, SPLIT_UB=1, CS binary /root/splitenum md5 992e4f98...).
  Open after the chain: char-0 recheck of h0_p >= 1 reps, pencils (h0 >= 2) by hand (c14 method), rep 50489.
- 32R-68b incident (2026-10-26 morning): the *_p.sing sweep scripts also contain the char-p genus tail (plane image,
  normal.lib); for h0 >= 1 reps each job took ~1.5 GB, 11 in parallel exhausted WSL RAM (11.8 GB) + swap ->
  thrashing (~300 jobs/h). Stopped (wsl --shutdown), incomplete outputs removed (marker "base locus outside D's
  curves"), remaining 12,095 jobs rerun with short scripts *_s.sing (cut before the genus tail) at -P 8:
  ~15 jobs/s, RAM ~0.6 GB. Genus jobs now -P 5. Chain restarted (run_chain_d16_d18.sh).
  Results before the restart: h0_p = 0 x58,748, 1 x488, 2 x21.
- 32R-68c (2026-10-26): d = 16 summary of the 71,697 unibranch-compatible reps (char-p sweep):
  h0 = 0 x67,767; reducible (residual degree < 16) x565; genus-type x2,882; conic-type (residual 18) x32;
  pencils (h0 >= 2) x438; residual 2,20 x10; misc x3 (10050 h0 = 1 no residual, 28425 residual -1, 50489 no
  decomposition m <= 3).
  Genus jobs (normal.lib, P3 image) are too slow (57 in 5.7 h at -P 5). Among the finished ones, 23 had char-p
  geometric genus <= 1 (values 1, -1, -3, -5): all 23 residuals contain known curves (conics / elliptic curves)
  -> the unique member is reducible -> excluded. New order (finalize16.py, run_chain2.sh, log chain2.log):
  known-curve containment test first (fast), genus only for residuals with no known curve, then d = 18 UB split.
  Open by hand afterwards: 438 pencils (c14 method needs automation), residual 2,20, the 3 misc reps,
  char-0 recheck of anything decided only by char-p h0 >= 1 data.
- 32R-68d (2026-10-26 15:20): containment tests done (2,879): 788 more reps have a known curve inside the residual
  -> reducible; 16 conic-type with no known curve (excluded as d12 rep 1215); 16 conic-type WITH a known curve
  (open); 23 containment pending (no c16 output?); 2,082 residuals without known curves need genus.
  normal.lib genus is hopeless (~1 h each); stopped. Plan: replace by a δ upper bound = singular points of the
  divisor {F = 0} ∩ S off D-curves and nodes (5x5 minors of [grad S_i; grad F], as for the pencils), with
  alternative decompositions to see points on D-curves; δ <= (4/3)τ per point, need δ >= p_a(C~) - 1.
  d = 18 UB enumeration (started 11:46 by the old chain, 12 shards, /root/splitenum CS+UB) still running;
  output split/reps_d18_ub.log / reps_d18_ub.json.
- 32R-68e (2026-10-26 18:30): the first d = 18 UB run finished but every shard output on /mnt/c lost chunks
  (shard 0: 80,188 lines vs 89,460 reported reps; one merged line per file) — writes from WSL to the Windows
  filesystem dropped data during the WSL timeouts. Moved to split/bad_d18/ (do not use). split_reps.py now
  writes to /root/splitout (WSL native), checks line counts = reported reps, copies, re-checks. d = 12 retest OK.
  d = 12/14/16 were already verified (reps count and Σ orbits = inventory), unaffected.
  Reported (lossy-run) d = 18 UB totals: inventory ≈ 2.0e9 classes, reps 1,401,351 — rerun started 18:35.
- 32R-69 fast exact h0 (stoll/fasth0/): degree-m parts (m = 1..3) of all component ideals precomputed once in
  char p (precompute.sing, 1 min 39 s: S, curves 1..92 with multiplicity 1..3 (saturated by the nodes as in
  baselocus.py), nodes with power 1..3) -> spaces.txt. (I(D))_m = ∩ (I_comp)_m, so h0 = N_m - rank(stacked
  annihilators) - dim S_m (dim S_m = 0, 4, 28). Validation on all d = 16 sweep reps: 71,625 / 71,625 identical h0
  (h0 = 0 x67,696, 1 x3,491, 2 x407, 3 x27, 4 x4; 71 skipped: node powers > 3 in the old decompositions);
  ~6 ms per rep under full load. Decomposition: MILP with bounds <= 3 and mip_rel_gap = 1: 0.125 s (14x faster).
  judge_fast.py (multiprocessing) tested on 300 d = 16 reps with fresh decompositions: 300/300 agree.
  Chained after the d = 18 UB rerun: fasth0/d18_h0.json, log fasth0/d18_judge.log.
- CORRECTION 32R-68e cause (19:30): a second d = 18 UB run was alive — run_chain2.sh continued to its d = 18 step
  after its genus jobs were killed (~15:15), and TaskStop of the chain did not stop its python/WSL children.
  Two runs wrote the same /mnt/c output files r18_ub_out_* -> the lost/merged lines. The stray run (12 procs,
  etimes > 8000 s) was killed at 19:25; only the 18:28 rerun (native /root/splitout + line-count checks) remains.
  Lesson: after stopping a chain, kill its WSL children explicitly; never share output names between runs.
- d = 18 UB rerun OK (2026-10-27 03:20): 2,127,398,048 classes, 1,391,809 geometric reps, Σ orbits = inventory,
  native/copied line counts verified. C² from -20 to 10, peak -2.
- d = 18 fast judging (fasth0/judge_fast.py, 10 procs, 26,492 s): h0_p = 0 x1,336,403 (96.0%), 1 x49,824,
  2 x5,099, 3 x228, 4 x2, no decomposition with m <= 3 and multiplicities <= 3 x253. Output fasth0/d18_h0.json.
  Next: fast known-curve containment for h0 = 1 (the unique form F lies in the saturated (c_Γ+1)-th order space
  of Γ <=> the member contains Γ -> reducible), δ bound for the rest, pencil automation, and the 253 with larger
  bounds.
