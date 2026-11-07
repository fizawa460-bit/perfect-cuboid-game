# 32R-71 — fibre matching across decompositions (2026-10-29)

## Extension-field members: where the time goes
- d=16 sx jobs: degree-1 members 2,114 jobs, avg 21 s (12.6 h); extension members 627 jobs, degree 2..16,
  avg 350 s (deg 2) .. 5,700 s (deg 14), 156.5 h in all.  All 627 ended g >= 2 (FASTGENUS lower bounds 5..11).
- Profile of sx_15031_0_2 (degree 2, 469 s): sat(B, Dc) 132 s, slocus(C3) 327 s; the rest about 3 s.
- Tried: member step over F_p with ww as an extra variable plus minpoly (sxfast/var_*.sing) -- slower (> 660 s for the
  sat step alone, killed).  Singular GF(q) needs q < 2^16, so not usable at p = 10009.

## Exact Moebius maps between decompositions (p16/mob2)
- For a pencil with decompositions t = 0..nD-1 the residual curves are the members of the same |x|, so the pencil maps
  differ by a Moebius map.  mkmob.py: constants (a,b,c,d) with F0t (c G0 + d G1) - F1t (a G0 + b G1) = 0 mod std(S)
  (degree-0 syzygies of the four products).  155 pencils (all decompositions ok, nD >= 2, some heavy fibre):
  exactly one Moebius map for every decomposition, about 80 s per pencil.
- match.py: maps every printed fibre factor (per fibre >= 2) to dec-0 coordinates, sums L_t over decompositions
  (L_t = 1 if the mapped fibre is not printed in dec t but dec t has an unprinted factor of that degree, else 0).
  A fibre needs a member job only if sum >= p_a - 1 (same argument as stage2.py, sharper sum).
- Result on d=16: 720 heavy fibre classes; 115 excluded by the sum (107 degree 1, 8 extension); 605 need one member
  (475 degree 1, 130 extension).  Classes are mostly the same fibre seen in all decompositions.
  sx time: 169.1 h -> 38.6 h (one job per needed class, taking the slowest finished job of the class).
- Consistency with the finished sx results: no class contains a low-genus result; FASTGENUS differs inside some classes
  (e.g. 10 vs 8) -- these are lower bounds, so this is expected.  41 excluded classes had only 'other' (fast tail
  failed) results -- they are now closed by the sum.

## Faster critical step and member tail (2026-10-30)
- p16/crit_tail_v2.sing: slack loop. length_f >= deg f * mult_f(eliminant) = LB_f; slack = vZU - sum LB.  Exact length
  only if LB + slack >= 2 deg; otherwise prints "critical length at most ... per fibre at most 1 (bound)".
  "FIBRE-LOOP-DONE" marks a complete run (stage2m.py also accepts sum of lengths = vZU).
- p16/crit_tail_v4.sing: if dim(Z1) <= 1, node saturation sat(std(Z1), NODES) is skipped (it was 523 of 539 s in
  c_1009308_0).  Lengths are then upper bounds (nodes included), so the heavy-fibre set can only grow (conservative).
  Guard: F1=0 / chart-hyperplane points allowed only at nodes (reduce(NODES, std(radical(Z1+F1))) == 0).
  Tests (old -> new s): 15031_0 86->28, 28589_0 444->58, 661172_0 445->49, 664830_0 481->57, 312679_0 537->88,
  323569_0 463->75, 1009308_1 550->79.  Old heavy factors kept, extra inflated fibres appear.
- Tried and dropped: chart-wise node saturation (v3, 15031: 86 -> 426 s).
- gfast/tail_fast_v2.sing: slocus(C3) replaced by JP = C3 + pi1^*(Sing f1) + pi2^*(Sing f2) for two generic plane
  projections (a superset of Sing C3).  53 validation jobs: identical genus bounds.  Avg s old -> new: h0=1 d18 85->17,
  h0=1 d16 22.4->7.35, sx degree 1 82->10, sx extension 469->183.

## d=18 sample with the fast pipeline (stoll/p18s4)
- Same 32 pencils / 64 decompositions as p18s (prep.py seed 71, 40 drawn, 8 fixed), plan.json and Moebius maps
  (m_*.out, unique map for all 32, about 17 s each) copied from p18s.
- c (v4): 64 jobs, all complete, total 14,658 s, avg 229 s, max 1,107 s (old p18s: avg 808 s, one 14,401 s timeout).
- stage2m (DIR=p18s4): 50 member jobs, all degree 1 (old: 5).  sx (tail_fast_v2): total 592 s, avg 12 s, max 25 s.
  16 MEMBER-REDUCIBLE, 21 FASTGENUS >= 2 (3..9), 13 with bound <= 1.  The 13 gx (plane factorize) jobs: all reducible
  (5..9 factors), total 167 s.  Conclusion as in p18s: no irreducible low-genus member in the sample.
- Not run on the sample: n/nt/hp/bp/sb/scx/sc stages (scaled from d=16 in the estimate); no extension-field member
  appeared in the sample; nets (h0=3: 204, h0=4: 1) not sampled.
