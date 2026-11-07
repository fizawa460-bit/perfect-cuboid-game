# 32R-69 Fast exact h0 and the saturation bug in the base-locus tool (2026-10-27)

## Fast h0 (stoll/fasth0/)
(I(D))_m = ∩ (I_comp)_m for homogeneous ideals; degree-m parts (m = 1..3) of all component ideals are precomputed
once, h0 = N_m - rank(stacked annihilators) - dim S_m (N_m = 7, 28, 84; dim S_m = 0, 4, 28). Validation against
the Singular sweep with the same (v1) ideals: d = 16, 71,625 / 71,625 identical.

## Bug found in the v1 component ideals (baselocus.py since 32R-38, and precompute.sing v1)
1. Curve multiplicity c >= 2: sat(S + G^c, S + (a1 a2 a3 b1 b2 b3 c)) saturates by the whole union of the
   coordinate-hyperplane curves, not by the 48 nodes. For every known curve lying in a coordinate hyperplane the
   result is the unit ideal (88 of the 92 curves at c = 2..4) -> the multiplicity condition is dropped -> h0
   OVER-estimated (h0 = 0 claims stay valid; h0 >= 1 results and the "member contains Γ again" test were wrong;
   the 2,037 extra exclusions of 32R-69b are void).
2. Node powers c >= 2: S + m_p^c is not saturated by the irrelevant ideal; its low-degree parts are too small
   (e.g. N93_2 in degree 1: 0 instead of 3 linear forms; N93_3 in degree 2: 4 instead of 19) -> h0
   UNDER-estimated -> some h0 = 0 claims were false.
Fix (spaces_v2.txt, precompute_v2.sing, fasth0v2.py): curves sat by the ideal of the 48 node points and by the
irrelevant ideal (multiplicities 1..4), nodes sat by the irrelevant ideal (powers 1..3). Curve ideals with c = 1
and S were already saturated (checked).
Theory: for an A1 point ord_E(π* f) equals the m_{S,p}-adic order of f, so π*F >= c E <=> F lies in the
saturated ideal of S + m_p^c; known curves are smooth, so the saturation of S + I_Γ^c by the nodes and the
irrelevant ideal is the c-th symbolic power.

## Recheck of all judged reps with v2 (same decompositions; fasth0/recheck_v2*.py)
| d | old h0 = 0 that are really h0 >= 1 | old h0 >= 1 that are really 0 | skipped (old node power > 3) |
|---|---|---|---|
| 12 | 0 (d = 12 conclusion stands) | 2 | 0 |
| 14 | 4: reps 452, 502, 652, 743 (d = 14 NOT closed) | 7 | 0 |
| 16 | 49 | 72 | 70 |
| 18 | 185 | 1,952 | 0 (+253 without decomposition) |
d = 18 v2 totals: h0 = 0 x1,338,170, 1 x48,397, >= 2 x4,989, no decomposition x253.
d = 8 / d = 10 (merged #1844 / #1845) do not use these ideals (d10: hyperplane residual sat(S ∩ H0, conics));
the `list L = sat(...); L[1]` idiom there is correct in Singular 4.4.1 (checked: L[1] is the whole ideal).
judge_fast.py now uses fasth0v2.

## d = 14 re-judging with correct ideals (running at hand-off, 2026-10-27)
stoll/fasth0/script_v2.py builds Singular scripts with the v2 ideals (h0, residual, known-curve containment,
genus only if no known curve). d = 14: 167 reps with v2 h0 >= 1 (160 with h0 = 1, 7 pencils) ->
stoll/f14v2/v_<idx>.sing, run with xargs -P 6 (stoll/f14v2/jobs.txt, run.sh). Next: read v_*.out, classify
(reducible / genus >= 2 / open), handle the 7 pencils (c14 critical-point method with v2 ideals), then the same
for d = 16 (49 + 70 skipped + all v2 h0 >= 1) and d = 18 (fasth0/d18_h0_v2.json).

## d = 14 re-judging result (2026-10-27 20:26)
stoll/f14v2/f14v2_final.json: of the 167 v2 h0 >= 1 reps, geometric genus >= 3 x141 (3 x12, 5 x4, 6 x29,
7 x50, 8 x46), reducible (known curve inside the unique member) x19, pencils x7 (1179, 1244, 1309, 1345, 1382,
1384, 1480). No genus <= 1. The 4 reps reopened by the bug (452, 502, 652, 743) are all genus >= 2.
Runner note: a second xargs (-P 5, reversed list) was added at 19:25; run.sh changed from `-s` to `-e` so a
started job is never restarted.
Pencils: 1179, 1244, 1345 are (7,7,14) -> balanced lemma. 1309, 1382, 1384, 1480: the c14 fibre analysis
(32R-60) used the old ideals. Every old component ideal is contained in its v2 saturation, so
(I_old(D))_m ⊆ (I_v2(D))_m; fasth0v2 gives h0 = 2 for all 10 decompositions used in c14/fib_*.sing, equal to the
old h0 = 2, so the pencils (the linear spaces of forms) are identical and the critical-point/δ argument carries
over unchanged. => d = 14 is closed again with correct ideals: no class of degree 14 carries an irreducible
curve of geometric genus <= 1 (full d = 14 inventory reps_d14.json; char-p caveats as before).

## 32R-69f fast containment prefilter + empty-space fix (2026-10-27 21:20)
Bug in fasth0v2: a component with no degree-m forms (only m = 1: S, curves at mult >= 3, ...; 185 entries of
spaces_v2.txt) was loaded as "no constraint" instead of (I)_m = 0. Effect: h0 could only be over-counted
(conservative for h0 = 0 exclusions), and member_form returned None at m = 1 (containment silently skipped).
Fixed (ANN = identity; old file fasth0v2_pre69f.py). Rerun: h0 unchanged at d = 14 and d = 16 (0 changes).
stoll/fasth0/contfilt.py: unique member F (h0 = 1) tested against V(Γ, c_Γ + 1) for Γ = 1..92.
Validation d = 14 (d14fullf_*): all 19 Singular "reducible" found; 16 more found (Singular had removed D's own
curves before testing, missing extra multiplicity; it then excluded them by genus 3/5 of the rest) -> consistent.
d = 16 (d16v2f_h0.json, 71,697 reps): h0 = 0 x67,769, 1 x3,493, 2 x406, 3 x24, 4 x4, no decomposition x1.
h0 = 1: reducible by containment x1,365, remaining 2,128 -> stoll/f16v2/v_<idx>.sing (script_v2, genus),
xargs -P 11 (run.sh with -e).

## 32R-69g fast genus lower bound (stoll/gfast/tail_fast.sing), 2026-10-27
Replaces the normal.lib genus() tail. Steps (char p 10009): residual curve C = V(Bp), p_a = 1 - hilbPoly[1];
generic projection to P3 (C3, check deg C3 = deg C: birational); SL = Sing(C3) (finite, else give up);
generic projection P3 -> P2 (plane curve f, check one generator of degree deg C: birational) and image J of SL;
all points of J in the chart w0 = 1 (else give up); Σ deltaLoc(f, P) over the prime components P of J.
Claim: g(C) >= p_a - Σ. Reason: for a birational finite map of reduced curve germs, δ of the image germ >= sum of
δ of the source germs over it (O_image ⊂ O_source ⊂ normalization); singular points of C map into Sing(C3), and
those of C3 into J's points; so Σ_{p in Sing C} δ_p(C) <= Σ_{q in V(J)} δ_q(f), and g = p_a - Σ δ_p(C) when C is
irreducible and reduced (if C is reducible or non-reduced, class x has no irreducible member since h0 = 1, so the
exclusion holds anyway). The A1 nodes of S are covered (non-planar germs are fine: projection only raises δ).
Char p: g_p <= g_0 (32R-69), so a char-p lower bound >= 2 gives g_0 >= 2.
Prototype: d14 rep 452: bound 6 (= genus() 6) in 7 s; rep 943: bound 3 (= 3) in 2 s (genus() ~1 h).
Validation over the 141 d = 14 genus cases running (gfast/val14.txt, t_<idx>.out).
Validation d = 14 (gfast/cmp14.py): 141 genus cases -> bound = genus() x139, bound = genus() - 1 x2 (1211, 1302;
5 vs 6, a non-planar germ whose plane image has larger δ); never above genus(); avg 3.3 s, max 17 s.
d = 16 switched: the slow f16v2 run (11 jobs in 40 min, none finished) was stopped and its partial outputs removed;
stoll/f16fast/t_<idx>.sing (f16v2 scripts with tail_fast), xargs -P 11 one.sh.
d = 16 fast genus result (2026-10-28, f16fast/tally.py -> tally16.json): all 2,128 remaining h0 = 1 reps have
genus lower bound >= 2 (no failure, no timeout; avg 22 s, max 35 s per job). With containment (1,365 reducible),
every d = 16 h0 = 1 rep is excluded. d = 16 open: 434 reps with h0 >= 2 (406 / 24 / 4 for h0 = 2 / 3 / 4) and
1 rep without a bounded decomposition.

## 32R-69h..j d = 16 pencils (2026-10-28, in progress) and a NODE-IDEAL BUG in the old pencil analysis
- fixfilt.py (fixed component: h0(D + Γ) = h0(D) for a known curve or E_k): 146 of the 434 h0 >= 2 reps excluded.
- 50489 (C² = -16, no decomposition with m <= 3): m = 4 decomposition, Singular v2 script: h0 = 0 -> excluded
  (degree-4 forms: Hilbert function 104 = h^0(4K)).
- Remaining: 265 pencils (h0 = 2; 163 with all m_j <= 1, 102 with some m_j >= 2) and 23 nets (h0 = 3, 4).
- BUG (old c14 / d12 crit scripts, copied into p16): `NODES = std(S + ideal(a1*a2*a3*b1*b2*b3*c))` is NOT the
  48 nodes but S ∩ {product = 0}, a curve of degree 112 (checked: dim 2, degree 112; Sing(S) = S + 4x4 minors is
  48 points).  Saturating the critical scheme by it dropped all critical points on those coordinate-section
  curves, so the d = 12 and d = 14 pencil conclusions (32R-60) have a gap whenever such a curve Γ has x.Γ >= 2
  and is not covered otherwise.  Fixed in p16 (NODES = S + minor(jacob(S), 4)); d = 12 / 14 pencils to be redone.
  Also: sat(Z, S + (F0, F1)) replaced by sat(Z, F0) ∩ sat(Z, F1) (same ideal, faster).
- Pencil method: decompositions until no point off the nodes is hidden in all of them (hidden_check.py; after the
  node fix 63 pencils keep finitely many hidden points -> hidden_pts.py: members through them via the moving parts
  R_u = sat(S + (F0 - u F1), D-curves) -> special members for stage 2; 2 pencils have their hidden points at
  moving base points, which are simple (basepts.py) -> no member singular there).
- Base points (basepts.py): i_q = local intersection of any two members; i_q = 1 => no member singular at q.
  259 / 265 all simple or none; 6 with a non-simple base point, none of them hidden (bh_*.out) -> fine.
- Nodes with m_k >= 2 (node_jobs.py): blow-up chart, moving part on E_k, branch values of E_k -> P1 and
  coincidences with fixed points -> special members (330 chart jobs fine, 18 = 9 pencils with every member
  tangent to E_k: direct singular-point version ns_*.sing too heavy so far, open).

## 32R-69k (2026-10-28) refix of the old d=12/d=14 pencils; stage-2b first tally
- refix/ (old scripts with the correct NODES = S + 4x4 minors of jacob(S)):
  * d=12 2020: critical scheme off base locus and nodes is 20 points (old claim "no critical point" was an artefact of
    the degree-112 NODES curve). 1959: 30 points (old: 8). The old crit_ tail eliminates on the affine cone (EL = 0),
    so these give no fibre data. => the d=12 pencil conclusion of 32R-60 is RE-OPENED.
  * d=14 1382, 1384: the critical scheme now contains a conic (dim 2 deg 2 affine) -> old fib tail stops at dim ZU 1.
    1309, 1480: finite, fibre data as listed in refix/fib_*.out (per fibre <= 2). pairs/triples rechecked.
  * refix2/: same prefixes + p16/crit_tail.sing (critical-curve handling, chart elimination). Running.
- stage-2b (p16/sb_*, tally_sb.py -> sb_tally.json) at 382/519: g >= 2 for 318; MEMBER-REDUCIBLE (contains a D-curve)
  31; 31 low/undecided (fast bound <= 1, or P3 singular locus a curve). sc_*.sing: radical + minAssGTZ of the member
  residual: all 31 have >= 2 one-dimensional F_p-components (14 also non-reduced) -> the special member is not integral
  (char-p statement; same char-0 caveat as the rest of the pipeline).
- refix2 results (correct NODES, random pencil basis, chart elimination; all decompositions finite, no point with
  F1 = 0 or on the chart hyperplane):
  * d=14 1309 (p_a 9, 3 decs): max per fibre 2,2,2 -> Σδ <= 6 < 8. 1382 (2 decs): critical conic lies in one fibre
    (that member is singular along it -> non-reduced, not integral); remaining points max 2,2 -> Σδ <= 4 < 8.
    1384 (3 decs): critical conic in one fibre; max 2,2,2 -> 6 < 8. 1480 (p_a 8, 2 decs): 1 per fibre -> 2 < 7.
    Hidden sets (refix/pairs.out, triples14.out with the correct NODES): pair points exist only for 1309 (68∩90) and
    1384 (51∩59, 52∩57); every triple with the third decomposition is empty -> H empty. Base points (C² = 2): x² = 2
    with 2 distinct base points -> both simple (i_q = 1) -> no member singular there (resolves the 32R-60 caveat).
    => d=14 pencil conclusion stands (with the corrected computation).
  * d=12 1959 (p_a 7, 2 decs): 30 reduced points, max 2 per fibre in both decs -> Σδ <= 4 < 6: excluded.
    2020 (2 decs): 20 points (12 distinct), two degree-2 fibre factors with 3 per fibre in each dec -> 3 + 3 = 6
    reaches the threshold; stage-2 (refix2/s2_r2_crit_2020*: union of the 2 conjugate members, radical/minAss +
    fast genus) running.
  * 2020 stage-2 result: all 4 heavy fibre pairs (2 per decomposition): union of the 2 conjugate members is reduced,
    one F_p-component of degree 24, fast bound B = 29 - 20 = 9 -> g >= (9 + 1)/2 = 5. => 2020 excluded; d=12 pencil
    conclusion RE-CLOSED with the corrected computation (char-p caveat as before).
- stage-2b COMPLETE (519 special members of 145 pencils): g >= 2 for 423; contains a D-curve 43; the other 53:
  50 have >= 2 one-dimensional F_p-components (27 also non-reduced; p16/sc_*); 3 (k = 2 conjugate pairs, degree 32:
  24755_0, 29018_3, 31696_4) timed out over F_p and were redone over F_p(ww), ww^2 = disc, one member of degree 16
  each (p16/se_*, both conjugates as cross-check): fast bounds 10, 8, 10. => every special member found by the node /
  hidden-point analysis is non-integral or has g >= 2 (char-p caveat).
- 32R-69l speed fix in p16/crit_tail.sing (old copy crit_tail_pre69l.sing): per-factor critical length was
  vdim(ZU + f^(e+8)) (std of a high power; 13 jobs hit the 2 h limit inside this loop, on factors of degree up to 42);
  now vZU - vdim(sat(ZU, f)) (exact for 0-dim ZU, no power). c_28589_0: 7200 s timeout -> 444 s, same lengths for
  every factor printed before. The 13 timeouts (moved to p16/old_timeout/) are rerun; unstarted c_ scripts patched.
- c_ critical runs COMPLETE (820): all finite. 5 long jobs started before 32R-69l were killed and rerun with the new
  tail (57506_0: > 1 h -> 257 s). 60600_1, 67440_2 had a critical point with F1 = 0 -> reseeded basis
  (system("random", 3141) after 2718), now clean. stage2.py: 0 OPEN decompositions.
- 32R-69m p16/stage2x.py replaces the union-of-conjugates jobs: one member F0 - w F1 per heavy factor f, over F_p
  (deg 1) or F_p(w), minpoly f (deg >= 2); conjugate members have equal genus. 2746 jobs (2114 of degree 1;
  ~19 s each), sx_*.sing, running (-P 10).
- heavy members: undecided ones (fast bound <= 1) go to p16/scx_* (radical + minAssGTZ; scx_loop.sh keeps a core busy).
  All finished ones so far: >= 2 F_p-components. Exception: pencil 28761 (decs 0, 2, 4, fibre with 2 critical
  points each, fast bound 1, minAssGTZ > 2 h): p16/gx_28761_*: the birational plane model (degree 16) factors over F_p
  into 4 factors (largest degree 10) -> the member is reducible (not integral). Note: factorize of the plane model is
  much cheaper than minAssGTZ -> use it first for the remaining undecided members.

## 32R-69n — d=16 pencil stage 2x complete (2026-10-29)

- sx (one member per heavy fibre factor, over F_p(ww)): 2746 jobs = 2012 g>=2, 164 reducible, 565 OPEN (488 low bound + 77 other), 5 duplicate. No timeouts (slowest 6412 s, extension degree 14-16).
- Duplicates: for the slow pencils 58600, 67987, 30728, 26665, the pencil maps of the 5 decompositions are related by a Moebius map (fitted mod p on 40 random points of S, rank 3; script p16/mob/check2.py, output mob/check2.out). Heavy degree-14/16 factors were mapped and compared. Same fibre sets: 58600 {1_2,3_2,4_3}, 67987 {1_3,3_3}, 26665 {0_3,2_3,3_3,4_3}; 30728 all distinct. Jobs 58600_3_2, 67987_3_3, 26665_0_3/2_3/3_3 were marked DUPLICATE (a finished member of the same set has g>=8). One.sh timeout was raised to 36000 s for the last jobs.
- All 565 OPEN members are reducible or non-reduced over F_p: 562 by scx (radical + minAssGTZ), 3 (28761_0_0/2_0/4_0) by plane-model factorization (gx_, 4 factors).
- Conclusion (char-p caveat as before): no irreducible member of genus <= 1 in any d=16 h0=2 pencil. Still open for d=16: the 23 nets (h0 = 3, 4).
