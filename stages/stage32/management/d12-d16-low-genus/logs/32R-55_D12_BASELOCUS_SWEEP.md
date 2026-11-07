# 32R-55 d = 12 base-locus sweep on the classes found so far (2026-10-23, research)

- Classes found so far (results.jsonl, results_wide*.jsonl): 9584 -> closure under the 6144 lattice group 637824
  -> 628 orbits of the geometric group (stoll/d12_reps.py, d12_reps.json).
- BUG FOUND AND FIXED in stoll/baselocus.py: Singular 4.3+ returns an ideal from sat(), so `sat(...)[1]` took only the
  first generator for curves of multiplicity >= 2 in D (and the residual saturation). Fixed (handles list/ideal,
  checks S ⊂ G^c-ideal) + a second h0 computation via Hilbert functions (kbase). All earlier outputs moved to
  stoll/old_buggy/; everything re-run. d = 8 / d = 10 reproduction unchanged (h0 and residuals identical).
- d = 12 (628 orbits, m = 1 for 542, m = 2 for 86; char 0 and char p agree; both h0 computations agree):
  617 orbits h0 = 0 (no curve); 10 orbits h0 = 1 with an integral residual of degree 12; 1 orbit C² = 0 with h0 = 2.
- The 10 residuals (stoll/g12_*.out, gg12_*.out, char p = 10009, generic projection to P^3, degree preserved):
  510, 511 smooth, p_a = 6 -> genus 6; 607 genus 6; 595 genus 6; 581, 585, 591..594 genus 5.
  (char-0 geometric genus >= char-p geometric genus; Hilbert polynomials agree in char 0 and p.)
  These are curves on S of degree 12 and genus 5/6 not among the 140 known curves (if the char-0 residual is integral).
- Open: the C² = 0 orbit (idx 603, h0 = 2, pencil) needs the fibration argument; the run is still going, more classes
  will come (rerun d12_reps.py + sweep12.py on the final results).
