# 32R-49 d = 12 wide run (2026-10-23)

- Literature check (Stoll–Testa arXiv 1009.0388, §Fib, §K3, §Curves): the 12 non-isotrivial genus-5 fibrations with
  doubled conic fibres (found in the lattice: 12 classes × 4 fibres, scripts/32R-48_fibrations.json) only give
  C·(32 exceptional curves) >= 4 - 4g: no cut. The K3 quotient splits Pic into 20 + 20 dims but does not reduce the
  number of candidates. Their degree-6 argument is case-by-case hyperplane geometry: not scalable to 12.
- Near-equality algebra (32R-47, stoll/nearmaps.py): the single-map system (29 unknowns, 1-dim family) did not finish
  in Singular (1 h) and msolve was killed (memory) after 18 min. Theory: if f1*J(Y) = f2*J(Y) then f2 = α∘f1
  (graph case, impossible for n = 6); the other case stays open.
- Decision (user: recommendation): finish d = 12 by computation. The wide run (C^2 >= -14 for the genus-0 slices)
  contains the production run, so production was stopped and the wide run started:
  run_d12_wide.py, 13148 jobs, 1816 identical jobs imported from the production results (same binary faf0fbec,
  same slice code, same key incl. c2min = -12), 11332 to run, producer 2a8b932f. Estimate ~412 h (~17 days) at the
  observed production pace (Knuth ratio 3.17 × 130 h); uncertain.
- Final classes = results_wide.jsonl ∪ imported production records (results.jsonl, matching keys).

## 32R-50 speed variant (restart 2026-10-23)
- certified_enum_mtf.c: same per-k bounds and discard test; constraints visited in an adaptive order (a discarding k
  moves forward). Discard iff some k passes, independent of order -> same visited nodes and leaves. Built with
  -O3 -march=native -ffp-contract=off -fno-fast-math (binary 6cf8bb9e).
- Test on 3+4 completed production jobs (1.05e8..1.65e8 nodes): stdout hash and node counts identical for all variants;
  time 86.6/104.4/158.6 s -> 54.7/71.1/108.8 s (x1.46..1.58). (Plain -O3: x1.35..1.48; two-pass vectorised: x1.2..1.4.)
- Restarted: run_d12_wide.py now builds certified_enum_mtf.c; output results_wide2.jsonl, producer 4840603b;
  2444 jobs imported from results.jsonl + results_wide.jsonl (binaries faf0fbec or 6cf8bb9e), 10704 to run.
  Expected ~17 d / 1.5 ≈ 11 days.

## 32R-51..53 further speedups (2026-10-23)
- Profile (job 4|22|-12|64, 1.05e8 nodes): 46M radius discards, 36M CS discards (2.65 tests on average with mtf),
  23M survivors (each runs all 140 tests) -> survivors dominate; per-call centre recomputation O(n) also costly.
- Active-set variant (drop constraints that cannot fire): slower (few constraints become inactive). Dropped.
- Hybrid (first 8 adaptive tests scalar, then a vectorised full pass): x1.12..1.18 over mtf.
- certified_enum_inc.c = hybrid + incremental outward-rounded suffix sums for the centres (STALE index per level)
  + per-level F2 buffers: original 87.7/106.4/159.7 s -> 30.1/33.8/46.5 s (x2.9..3.4); identical stdout and node
  counts on 5 test jobs (2 with leaves). Binary 45510a43.
- Restarted: results_wide3.jsonl, producer 35a9ab97, 4928 jobs imported (binaries faf0fbec/6cf8bb9e), 8220 to run.
  About 5% of the estimated weight was done; at ~2.9x the original speed the rest is ~135 h (~5.5 days).

## 32R-56 constraint subset (2026-10-24)
- Per-constraint discard counts (ce_kprof): the 12 boundary curves (labels 33..44) never discard (their pairings
  are fixed by the slice); the top 20 constraints make 95.5% of the discards.
- certified_enum_keep.c = inc + optional CE_KEEP subset. Without 33..44: identical nodes and classes, 12-16% faster
  (41.4/36.5/34.4 s -> 36.4/31.0/28.9 s). Top-40 only: same classes but 2-10x slower (rare constraints prune big
  subtrees) - rejected.
- Restarted: results_wide4.jsonl, producer 076721e9 (binary 3810537f, ce_keep), 6499 jobs imported, 6649 to run.

## 32R-57 tuning (2026-10-24)
- Head size T (scalar adaptive tests before the vectorised pass): T=4 36.8->35.4 s (~4% faster), T=12/16 slower;
  PGO (-fprofile-use, trained on 2 jobs) no gain. All identical leaves/nodes.
- Restarted with certified_enum_keep4.c (T=4) and 12 workers: results_wide5.jsonl, producer f470d7ad
  (binary cf2413a1), 7380 imported, 5768 to run.
