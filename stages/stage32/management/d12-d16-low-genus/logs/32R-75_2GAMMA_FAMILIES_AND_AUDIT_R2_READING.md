# 32R-75 — The 2Γ-families of the d = 16 net D-check (Lemma G redo) and the round-2 reading audit of R2

Date: 2026-11-04. Status: research log, local only (no ledger / STATE / credit / audit-master change).
Code: `stoll/famg/` (gen.py, milp2.py, hgen.py, nodegen*.py, collect.py, mkmem.py, mkext.py, tally.py, y2.py,
recheck_collide.py, mkkq.py; outputs *.out). Analyzer change: `stoll/m16/an2.py` (COLLIDE).

## 1. The gap (R2 package §4.7)
32R-72 closed the D-check "2Γ-families" (members containing (m+1)Γ for a D-curve Γ) by "the residual R ⊇ Γ is
reducible" — the M1 error. Also the 27988 cross-decomposition member singular at P0 ("contains a further D-curve").

## 2. P0 member (27988_0, q = (−3811 : −3427 : 1)) — closed
`famg/p_27988_P0`: components = four elliptic quartics (genus 1 each), Σg = 4 ⇒ g(C_0) ≥ 4 by Lemma G.

## 3. The families
22 (job, line Q) families from `n16/fam/h_*.out` (27685s excluded: μ = 16, M7). Each is the pencil
{members of |x| in I(D_t + Γ)} (MEMBERDIM 2 in all 22), M_s = Fix + Y_s.
- Fixed part (`famg/x_*`; FIXC curves, FIXE exceptional curves). Same Fix ⇒ same pencil |x − Fix| + Fix
  (h⁰(y) = 2, below). Distinct pencils: 9.
- Generic member (`famg/f_*`): Σg = 5 … 8 (moving Y of genus 5, 7, 8 + elliptic fixed curves) ⇒ Lemma G.
- Identical to §O families (same basis, same critical values): 28246_0_0 = 28246_2_0 = §O 28246_121;
  28255_0_1 = 28255_1_0 = 28255_2_0 = §O 28255_122 (Fix identical). Closed in 32R-74 §O.
- 27988_0_0 = 27988_1_0: Fix contains the elliptic quartics G40 and G42 ⇒ every member has Σg ≥ 2. Closed.
- Remaining 15 jobs (6 pencils: 27882 ×2, 27988 (G44), 28246 (G31/32), 28255 (G7/8), 28261 ×2, 34761).

### 3.1 Representation 2 (`famg/milp2.py`)
y = x − Fix; D2 = MILP decomposition of mK − y avoiding every curve of D_t ∪ Fix; all 22: m = 2, h⁰_p(D2) = 2
(`pencil h0 2` in every r_ job), so |y| is the family {Y_s}.

### 3.2 Base points (`famg/y2.py`)
y² = 0 for 21 of 22 ⇒ |y| has no base point on S̃ (two members are disjoint). 28255_0_0: y² = 2; Y_0 ∩ Y_1 on S lies
only at nodes (`bb3`); on S̃ (node charts, both representations, `nb1_`, `nb2_`): two simple base points on E_18
(local length 1 each) — total 2 = y², so these are all; every member is smooth there.
Side result for 32R-74 §O: the representation-2 base-point jobs `famd/b_*` had a script error (generator inserted a
line into a statement) and produced no data. Not needed: y² = 0 for all §O families except the eight 27769 ones
(y² = 2), whose two simple base points (famd/bq2_) exhaust y². §O's conclusion is unchanged; the log statement
"no isolated base points in either representation (b_*, b1_*)" is replaced by this y² argument.

### 3.3 Where singular points of Y_s can be
- off D_t ∪ Fix ∪ nodes: rep-1 critical scheme (`famg/c_*`);
- on D_t ∪ Fix, off D2 ∪ nodes: rep-2 critical scheme (`famg/r_*`);
- (D_t ∪ Fix) ∩ D2, off nodes: hidden points, members singular there solved directly (`famg/h_*`);
- on the E_P: node charts in both representations (`famg/n_*`, `n2_*`; NODEEXC = members containing E_P);
- base points: §3.2.
- positive-dimensional critical loci (non-reduced fibres): "critical curve fibre values", all over F_p.
Special F_p members (`famg/collect.py` → special.json): fibres with rep-1 or rep-2 length ≥ 2 per fibre, critical
curve fibres, NODEEXC, node-critical fibres, hidden-point members. Any other F_p fibre has δ(Y_s) ≤ 1 + 1 = 2 ≤
(allowed drop ≥ 4), so Σg ≥ 2.

### 3.4 Special F_p members (695 jobs, `famg/s1_*`, `s2_*`, tally.py)
- Σg ≥ 2 (rep 1 member, or rep 2 Y + g(Fix)): 647.
- Σg ≤ 1: 48 (24 rep 1 + 24 rep 2), all unions of known conics (+ one elliptic quartic in 34761).
  - The 24 rep-1 members (net members of |x|): analyzer (an2.py, net mode) worst bound 3, 4, 8, 9, 10, 11 ⇒
    g(C_0) ≥ 3.
  - The 24 rep-2 members: each matched to exactly one rep-1 low member of the same pencil (components of Y_s ⊆
    components of the rep-1 member ∪ curves of D_t; `famg/ks*`). Hence already closed.

### 3.5 Extension-field fibres
Crude length bound (max over fibres, node charts summed over charts) is not enough for 13 jobs (`extbound.py`).
Therefore: union-of-conjugates genus G per factor (as §O 28244_117), 155 factors in 26 jobs (`famg/e1_*`, `e2_*`),
Σg ≥ (G + k − 1)/k per member, + g(Fix). 34761 ×2: bound OK without this (≤ 2 ≤ 4).
RESULT (first pass, 2 h limit per job): 63 of 155 factors finished: G = 13 (g(Y) = 7, smooth fibres) and, for 28255
(g(Y) = 8), G = 15 (smooth) or G = 11 (each conjugate of genus 6, δ = 2). [Correction 2026-11-05: an earlier version
of this line read G = 11 as "smooth, another Y-class"; it is δ = 2, still Σg = 6.] 92 factors timed out (all of
27882_0_0, 27882_1_0, 28246_0_1, 28246_1_0, 28246_2_1, and all degree ≥ 3 factors); rerun one per job with a 24 h
limit (`famg/xe*_*`, one24.sh) — still running after 9 h, superseded by the direct check below.
(A genus over F_p(α) directly is not available: normal.lib genus "does not yet support extension fields".)

DIRECT CHECK over F_p(α) (`famg/mksx.py` → `sx1_*`, `sx2_*`, `tallysx.py`; 155 jobs, 6 s … 7 min each):
ring (10009, a) with minpoly h(a); Y_α = sat(S + (F0 − αF1); D_t, Fix, irrelevant) (degree 12 = generic in all 155);
off the nodes: Jacobian criterion on S (5-minors of [dS; dg] for each minimal generator g of Y_α), saturated by the
nodes; on E_P (nodes through which Y_α passes): blow-up charts as in `n_*`, chart surface as a local complete
intersection (three S_i/l and (Σc_iS_i)/l², c the linear relation of the tangent forms), strict transform
sat(sbm(Y_α) + XS4, l), Jacobian criterion with l = 0.
- 139 factors: Y_α smooth ⇒ Σg ≥ g(Y).
- 16 factors (28246_0_1, 1_0, 2_1 and 28255_0_0, both representations, 4 each): singular scheme of length 2 off the
  nodes, nothing on the E_P ⇒ δ ≤ 2 (multiplicity ≥ 3 would give Tjurina length ≥ 3; a double point A_k, τ = k, has
  δ = ⌊(k+1)/2⌋ ≤ k) ⇒ Σg ≥ g(Y) − 2 ≥ 5.
- E_P-excess impossible for α ∉ F_p (r0 = α r1 with r0, r1 over F_p forces r0 = r1 = 0), so p_a(Ỹ_α) = g(Y).
- Controls: F_p fibre s = 9827 of 28261_0_0 (s1_ genus 5 = 7 − 2): length 2 found; s = 1365 (node-critical, s1_
  genus 7): smooth; a constructed chart curve with a node on E_P: detected (length 1); the 63 finished union-genus
  factors agree one-to-one (28255: G = 11 ⇔ length 2, G = 15 ⇔ smooth; all others smooth ⇔ G = 13).
⇒ every extension-field fibre has Σg ≥ 5. §4.7 CLOSED.
Note: the node-chart critical lengths are only upper bounds and are loose (e.g. 28261_0_0, s² − 4281s + 2554:
critical points at 8 nodes in the charts, but the union genus is generic); they are not used for the bound.
Hidden points are all F_p-points (414 HIDPT, pdeg 1 in famd and famg), so a member singular at a hidden point is
an F_p-member (a linear condition over F_p) and is in the special list.

## 4. Round-2 reading audit of R2 (HOLD) — answers
1. A2 citation and decomposition: corrected in R2 Appendix B — [BPR] Remark 4.18, (4.18.1) ([BL85] Thm 4.6);
   Remark 4.17; base change to C_p; stratification (closed tubes of open strata, open tubes of points, limit
   boundary [BPR] Lemma 3.2); τ-saturation U_i = τ⁻¹(Γ ∩ U_i); subgraph lower bound.
2. Bad tubes in the analyzer: an edge is counted only if both ends are certified vertices (`an2.py`), i.e. bad tubes
   are dropped with all adjacent annuli — the valid rule.
3. Web strata: web.py tests generic point, every bad point (isolated or on a line), a generic point per bad line,
   all pairwise intersections; all bad loci are F_p-linear.
4. Zero collisions (good strata): the worst-case placement of zeros of B|_Γ on multiple sheets did not let the
   "free" zeros collide. Fixed (all partitions). Re-evaluation of all 965 analyzer members: no change, none < 2.
5. The lift M_0: all analyzed members have only known components: conics, and 211 degree-4 genus-1 components, all
   identified with known curves by ideal equality (`famg/kq/`, 190 members, 0 unknown). (First run of this check
   reported 102 "unknown": the m16 tail's `int b1` shadowed the ring variable in the injected code — the known
   bug of 32R-74 §L; rerun with `kill b1;`.)
6. Positive-dimensional critical loci: none discarded (no CRITCURVE-NOT-IN-FIBRE anywhere; the only non-linear
   critical-curve fibre polynomial, 27523_121, splits over F_p, §O).
7. Remaining check items: A3 geometric reducedness of the limit curves in Appendices E–F (28246, 28255, 28760);
   connector-lemma hypotheses written out (32R-74 §N in the package).
