# 32R-70 — enumeration symmetry breaking and GLPK type sorting (2026-10-29)

## Enumeration (split/splitenum9.c + split/symz.txt)
- The order-1536 group acts on the lattice part z by integral 16x16 matrices A_g (split/symz.py, checked integral and
  span-invariant). splitenum9 keeps only y-leaves whose z is lex-max in its orbit; the final pe test runs over Stab(z).
- d=16: 71,697 reps, orbit set equal to the old run (cmp_orbits.py).
- d=18: 542 s (old 16,020 s), 1,391,809 reps; orbit sets equal to the old run, checked with the C canonicalizer
  split/canon.c (pe lex-max over G, 128-bit hash; split/cmpc.sh): SAME_SETS.
- d=20: 1,887 s (xargs -P 9, split/full20sym.sh), 25,103,605 reps in /root/s20sym/out_*.txt (WSL; 4.2 GB, not on C:).

## Type sorting (stoll/fasth0/decglpk.c + h0stream.py + judge_glpk.sh)
- The scipy/HiGHS 1.2 MILP (about 96 % of judge_fast time) is replaced by GLPK 5.0 (WSL libglpk.so.40, prototypes
  declared in the source) called in-process: warm-started dual simplex as LP filter, then glp_intopt with
  depth-first backtracking, most-fractional branching, no preprocessing, zero objective (flags "0 2848").
  Every returned c is re-checked (c.Cm = mK - x, 0 <= c <= 3). Smallest m in 1..3 as before; h0 by fasth0v2.
- Tried and dropped: lattice/kernel local search (latdec.py, 4/539 found), pure DFS with bound propagation
  (decomp.c, all UNK), own LP dive (slower than glp_intopt), HiGHS options (no effect in 1.2).
- d=16: 71,697 reps, 188 s (11 parallel); (m, h0) equal to d16v2f_h0.json for every rep.
- d=18: 1,391,809 reps, 5,794 s (old 26,492 s); (m, h0) equal to the old d18_h0.json m and d18_h0_v2.json h0 for
  every rep (matched by orbit hash, fasth0/cmp18.py). 0 UNK. Distribution (m, h0):
  (2,0) 59,320, (2,1) 11,632, (2,2) 2,186, (2,3) 152, (2,4) 1, (3,0) 1,278,850, (3,1) 36,765, (3,2) 2,598, (3,3) 52,
  no decomposition 253.  So d=18: h0=1 48,397, h0=2 4,784, h0=3 204, h0=4 1.
- d=20 done 2026-10-31 (/root/j20, 240 shards, 9 empty; resumed twice after app/PC restarts with judge_glpk_resume.sh,
  last resume 63 shards 64,708 s).  25,103,605 lines = all reps, 0 UNK.  Distribution (m, h0):
  (2,0) 33,142, (2,1) 14,272, (2,2) 5,307, (2,3) 1,056, (2,4) 117, (2,5) 6, (3,0) 23,837,137, (3,1) 802,992,
  (3,2) 114,009, (3,3) 7,988, (3,4) 299, (3,5) 2, no decomposition (m <= 3) 287,278.
  So d=20: h0=0 23,870,279, h0=1 817,264, h0=2 119,316, h0=3 9,044, h0=4 416, h0=5 8.
  Extracted (WSL): /root/x20_h1.txt (946,048 lines: shard TAB rep TAB judge, s20sym ls order), /root/x20_none.txt.
  Open: the 287,278 no-decomposition reps need m = 4 (as d18 253 and d16 rep 50489).

## Notes for the detailed survey
- Cheap numeric tests do not separate outcomes: no d=16 rep has x.Γ < 0 for any of the 140 generators (the
  enumeration already enforces it), so the d=16 containment cases are not visible numerically (fasth0/numpred.py).
- d=16 pencil survey cost (core hours): sx 169 (of which about 158 in the ~630 members over extension fields),
  c 61, others about 30.  Idea: pick a prime where the heavy fibre factor has a root, so the member is defined
  over F_p' (degree-1 job, about 20 s).
- Net prototype n16/d_9379_0 (net 9379, dec 0): discriminant degree 32 = 6 lines + 4 conics + 2 quartics + 1 of
  degree 10; 20,415 s (node saturation 16,700 s). Variant d_9379_0b (node saturation skipped; node lines to be
  divided out afterwards) running.
