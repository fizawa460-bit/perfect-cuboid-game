# 32R-74 — Audit flags for the char-0 bridge (d = 14 / 16), consolidated

Date: 2026-11-04. Status: research log, local only (no ledger / STATE / credit / audit-master change).
Source: 32R-73 (all computations and directories are listed there). This file only collects, in one place,
every assumption the 32R-73 closures depend on, where it is used, and how it can be discharged.

## 0. What is closed (as of 32R-73, 2026-11-04)

| group | count | closing argument | flags used |
|---|---|---|---|
| d16 h0 = 1 containment (T2) | 1365 | Lemma G 773; h0 argument 386 + 5; remainder-δ 201 | A1, B1, B2, C1 |
| d14 h0 = 1 containment | 62 | Lemma G 22; h0 argument 8 + 7; remainder smooth 7 / δ 18 | A1, B1, B2, C1 |
| d16 pencil low members | 116 | critical scheme reduced (czr) + NC lemma (cnc) | A1, C2, C4, D1 |
| d16 net low members | 92 | types (c)–(e) 75; good-reduction pieces 16; 28246 two-scale 1 | A1–A5, A6, C2–C4, D1 |
| fixfilt (h0 ≥ 2, fixed curve) | 146 | exact char-0 h0 over Q(ζ8): the curve is fixed in char 0 | E1 |
| not closed | — | M3 exact (integer) enumeration at d = 14, 16 (R4); M7 conditional on E03/E04 | — |

## A. Foundations of the reduction arguments

- **A1 Lemma G** (32R-73 §1): g(C_K̄) ≥ Σ g(components of red C). Proof written (stable reduction, resolution of
  indeterminacy, dominant maps do not raise genus). Status: standard; proof in the log. Uses: everywhere.
- **A2 Generalised Lemma G / genus additivity**: for C_0^an decomposed by the specialization map into
  sp⁻¹(closed subsets) and good-reduction pieces glued along ends, g(C_0) = Σ g(pieces) + b₁(graph); disjoint
  affinoids with smooth irreducible reduction of genus h_i give g ≥ Σ h_i. Cite: Bosch–Lütkebohmert (stable
  reduction), Baker–Payne–Rabinoff (skeleta of analytic curves). Uses: R1b nets (27771, 25329, 28246).
- **A3 Singular reduction of a piece**: if the reduction curve of a piece is singular, removing the residue discs
  of its singular points leaves a piece whose genus is at least the geometric genus of the normalization.
  Uses: 28246 at ν = ±1402. Status: follows from A2.
- **A4 Tameness**: p = 10009 does not divide any multiplicity / cover degree used (e ≤ 3, cyclic covers of
  degree 2, 3). Status: immediate.
- **A5 Model over R**: S̃_R (blow-up of the 48 nodes) is smooth over R near every locus used; the nodes reduce
  to 48 distinct A1 nodes mod p (no extra singularities of S_p); the 92 known curves and the 48 exceptional curves
  are defined over Z[ζ8][1/N] with p ∤ N, and p = 10009 ≡ 1 (mod 8) splits in Q(ζ8) (ζ8 ↦ 792).
  Also: the known curves are smooth, including at the nodes (conics; elliptic quartics = CI of two quadrics in
  P³). To discharge: (a) count Sing(S_p) = 48 reduced points (already used: NODES = S + 4×4 minors has degree 48);
  (b) smoothness of each known curve mod p by a Jacobian check. Cheap.
- **A6 R-lattice of the linear system**: the equation of C_0 can be scaled into the R-lattice of degree-m forms
  of |x| and reduces to a member of |x|_p; h0_K ≤ h0_k by semicontinuity. Where the argument picks a basis of
  the lattice (nets: C_0 = F_M + τ B_λ; 28246: C_0 = M_0 + τB* + τ'B3) it needs the saturated sub-lattices; for
  28246 the char-0 dimensions were computed exactly (net h0 = 3, the B* subspace dim 2, as mod p).

## B. The h0 = 1 argument (T2, d14/d16 low members with all components known)

- **B1 M_0 ∈ |x| in char 0**: the divisor M_0 = Σ mult·K_{i,0} (+ E's) is linearly equivalent to x. Current
  justification: equality of classes in the 64-lattice + Pic(S̃_K̄) torsion-free and equal to that lattice.
  **Can be removed by computation**: exhibit, over Q(ζ8), a degree-m form vanishing on D + M_0 (h0_0(D + M_0) ≥ 1,
  same machinery as stoll/fix0). Then M_0 is cut out by a form and no Pic statement is needed.
- **B2 Semicontinuity** h0_0(x) ≤ h0_p(x) = 1 for O(x) on S̃_R (line bundle defined over R). Standard.

## C. Local singularity / δ arguments

- **C1 Remainder δ (cgp, cgp14)**: Sing(R) ⊆ Sing(member) = S + NN + 5×5 minors; tangent-space test; local δ from a
  generic plane projection (an upper bound for δ_R when the fibre length is 1; 28711 used the plane δ = 3 as an
  upper bound). All char-p computations; Σg ≥ p_a − δ is exact algebra. No extra flag.
- **C2 δ semicontinuity at a reduced crossing** (net type (d), e = 1, x·E = 1: contribution ≤ 1). Standard but
  to be cited / proved.
- **C3 Type (e) double E**: b′ ≠ 0 at the crossing points on E (the net member containing E does not pass
  through them). **To verify by computation** (per net low member with type (e)).
- **C4 NC lemma** (no singular point of C_0 in the residue disc of a normal-crossing point of M_p with
  multiplicities prime to p and b(Q̄) ≠ 0). Proof sketch in 32R-73; write out.

## D. Computational conventions

- **D1 Generic order oG at nodes** was computed from ONE random member FL[1] (ordP(FL[1], P)). If FL[1] happened
  to be special at some node, e and x·E would be off. **To verify**: oG = min over the basis FL[1..h].
- **D2 genus()** over F_p of an F_p-component that splits over F̄_p is ≤ the true sum (lower bound; counted
  max(0, ·)). Conservative.
- **D3** cnn "OFFNODE base point on multiple comp" tested one member only; reinterpreted (moving point) in 32R-73.
- **D4** baddir printed t = −1/kq (the bad member is FL2 + (1/t)·FL3); only equality of directions was used.
- **D5** All Singular runs mod p = 10009 except fix0 and c28/h0c (exact over Q(ζ8)).

## E. fixfilt

- **E1** Exact h0 over Q(ζ8) with the same component ideals as fasth0/precompute_v2 (curve saturations, symbolic
  powers saturated at the nodes, node powers). 146 reps: h0_0(D) = h0_p(D), and h0_0(D + Γ) = h0_0(D) for all 396
  fixed curves. No reduction argument involved. Remaining dependency: correctness of the ideal description of
  |x| (32R-73 §5, M4).

## F. Cheap discharge plan (local, no heavy compute)

1. B1: char-0 form for every M_0 used by the h0 argument (406 members: d16 386 + 5, d14 8 + 7).
2. D1: recompute oG as the minimum over the basis for all net / pencil members used in R1b.
3. C3: check b′ ≠ 0 at the crossing points for the type-(e) loci.
4. A5: Jacobian smoothness of the 92 known curves mod p, and Sing(S_p) = 48 reduced points.
Items C2, C4, A2, A3 are write-ups / citations, not computations.

## G. Discharged by computation (2026-11-04)

- **B1 + B2 (h0 = 1 argument), stoll/pic0** — exact over Q(ζ8), same component ideals as fix0. For each of the 406
  members (d16: 386 low members with all components known (cgk KCOMP lists) + 5 "residual not a curve";
  d14: 8 low (cgk) + 7 ALLKNOWN (cgq14 CONTAINS lists)):
  - h0_0(D) = 1 in all 406 (equal to h0_p);
  - 401 (component lists): h0_0(D + Σ K_i) = 1 — the unique char-0 member contains every listed known curve;
  - 5 (27991, 27992, 27994, 28339, 28425; all 140 single additions tried): the unique char-0 member contains extra
    D-curve / node multiplicity (e.g. 27991: curves 34, 40, 44 and nodes 113, 115, 119, 120, 122).
  Hence |x|_0 consists of one reducible member (x is not the class of a single known curve or E), and no integral
  char-0 curve of class x exists. This uses neither Pic(S̃) (B1) nor semicontinuity (B2), nor the reduction M_0 ≡ M_p.
  Total 5282 s CPU, max 234 s. (Job list had 1275 twice; 406 distinct.)
- **A5 (model), stoll/a5** — mod p: Sing(S_p) = S + 4×4 minors has degree 48 and is reduced (radical degree 48), so
  S_p has exactly 48 A1 nodes (Tjurina number 1), the reductions of the 48 char-0 nodes. All 92 known curves are
  1-dimensional and smooth mod p (Jacobian 5×5 minors, saturated: empty), including at the nodes; hence smooth in
  char 0 with smooth R-models.
- Tally correction: in the 206 cg1 timeouts there was no "all-known" case (5 not a curve + 201 remainders); the
  earlier "1 all-known" was the test job 1275, which belongs to the 386.
Remaining flags: A2, A3, C2, C4 (write-ups / citations), C3 and D1 (cheap computations), M3 (R4), M7.

## H. R4, D1, C3 (2026-11-04)

- **R4 / M3 — exact enumeration (split/splitenum9x.c, split/gen_exact.py, split/x14.sh, split/x16.sh).**
  splitenum9 with the y-stage made exact: the LDL^T data of the rank-15 form are recomputed from the lattice with
  rationals (gen_exact.py; denominators: lcm(U) = 24, lcm(D) = 12; deviation from the float input ≤ 1.1e-9 = the
  old R margin), the Fincke–Pohst ranges use Rem = DD·L²·rem (int64) and an exact isqrt, and the CS prune is the exact
  test "V < 0 and V² > nr·σ²" with V, nr, σ² rational (__int128). No floating point decides any branch.
  Results (same modes as the production runs, outputs compared as sets of 64-vectors):
  d = 12: 2029 reps, identical to r12_out (diff 0);  d = 14: 1487 reps, identical (diff 0, 135 s);
  d = 16 (SPLIT_UB + SPLIT_SYMFILE, 480 shards): 71,697 reps, identical to /root/s16sym/all.txt (diff 0, 462 s,
  no shard error). **Caveat C1 / M3 is discharged for d = 14 and d = 16** (modulo correctness of the C code).
- **D1 (stoll/d1)**: in all 208 pencil (116) and net (92) scripts, ordP(generic) used (F0 + 7F1 resp. FL[1]) equals
  the minimum of ordP over the basis NFL at every node. 0 mismatches.
- **C3 (stoll/c3)**: FAILS. At most e = 2, x·E = 0 nodes the bad-direction member B contains a component through the
  node (locint = ∞), so b′ vanishes at those crossing points. 61 net members have such a node; 58 of them were among
  the 75 "closed by types (c)–(e)" (the other 3, 28246 dm_1_0 and 25329 ×2, were closed by other means).
  → The type-(e) bound "δ ≤ 3" is NOT justified for these 58.
- **Re-closure of the 58 without δ (stoll/gph, gph2/analyze.py → analysis.txt / analysis.json).**
  Same decomposition as for 28246: sheets = components with x·Γ > 0 (all of multiplicity 1 here), specials =
  connected x-trivial configurations Z (B|_Z is a constant, so Z is bad for exactly one direction), sheet–sheet
  crossings (bad where B(Q) = 0; for base-point crossings, where B is tangent to a branch: xy + τ(αx + βy) is an
  annulus of modulus |τ|² when αβ ≢ 0); E-sheet/curve-sheet crossings are always counted as bad. Then
  g(C_0) = Σ_sheets g + Σ_specials (g(Y_s) − c_s) + N − S + 1, with good Z: G_Z − 1 (G_Z = genera of the pieces —
  cyclic covers for multiple components — plus b₁ of the internal graph), good crossing: −1, bad: −(number of ends).
  For every direction (each distinct bad direction and the generic one) the bound was evaluated.
  Result: all 58 have g(C_0) ≥ 2 for every direction (minimum 2 for 34761 r_0_19/r_0_20, 3 or 6 otherwise).
  Sanity: with every special good the bound equals p_a(x) (11, or 12 for 27882 / 28255 where x² = 6), except
  34761 r_0_19/20 (9, because of the always-bad E-sheet crossings).
  Flags used: A2 (genus additivity), C4 (NC lemma, incl. multiplicities 2 / 3 and the base-point annulus), no δ.
- Net tally after this section: 92 = 17 (closed earlier by pieces / Lemma G, 32R-73) + 58 (re-closed here) +
  17 (types (c)/(d) only, no e = 2 node: their 32R-73 closure does not use C3).
Remaining flags: A2, A3, C2 (type (d) only, for the 17 nets without e = 2 nodes), C4 — write-ups / citations;
M7 (E03/E04).

## I. Proof of C2 (and of the reduced case of C4)

Setting. R complete DVR (after finite extension), m its maximal ideal, Q̄ a closed point of the special fibre of
the smooth R-surface S̃_R, x, y ∈ Ô_{S̃_R, Q̄} formal coordinates (so Ô = R[[x, y]]). C_0 has local equation
f = F_M + τ B ∈ R[[x, y]], where F_M is the equation of the char-0 member M_0 and τ ∈ m. M_0 is reduced at Q̄ with
two smooth transversal branches (known curves / exceptional curves, smooth over R by A5); take x, y to be local
equations of these branches. Then F_M = unit·xy exactly, and after replacing x by unit·x: f = xy + g with
g = τ·(unit·B) ∈ τ·R[[x, y]] ⊂ m·R[[x, y]]. The residue disc of Q̄ is the open unit bidisc D = {|x| < 1, |y| < 1}.

**Lemma C2.** C_0 ∩ D has at most one singular point, and it is an ordinary node. In particular δ(C_0 ∩ D) ≤ 1.

*Proof.* A singular point P ∈ D satisfies f_x = y + g_x = 0, f_y = x + g_y = 0. The map Φ(x, y) = (−g_y, −g_x)
sends D into itself and is a contraction for the sup-norm with constant ≤ |π| < 1, because every coefficient of
g lies in m (so the coefficients of the partial derivatives of g_x, g_y do too). By the fixed-point theorem
(equivalently multivariate Hensel: the Jacobian of (f_x, f_y) is ≡ [[0, 1], [1, 0]] mod m, hence invertible) there
is exactly one critical point P_0 of f in D, and it is defined over R. The Hessian of f at P_0 is ≡ [[0, 1], [1, 0]]
mod m, with determinant ≡ −1, a unit; so if f(P_0) = 0 then P_0 is an ordinary double point (δ = 1), and if
f(P_0) ≠ 0 there is no singular point in D. ∎

**Corollary C4 (reduced crossing).** If moreover B(Q̄) ≠ 0 (so v(g(P)) = v(τ) for all P ∈ D), then f(P_0) ≠ 0
(since |P_0 x-coordinate · y-coordinate| = |g_x g_y| ≤ |π|·|τ| < |τ| = |g(P_0)|): no singular point, and
C_0 ∩ D = {xy = −g} is an open annulus {|x||y| = |τ|·const}.
**C4 with multiplicities** (f = x^a y^b·unit + τ(b_0 + …), p ∤ a, b, b_0 a unit): at a singular point,
a x^{a−1} y^b·unit = −τ ∂_x(…) gives |x^{a−1} y^b| ≤ |τ| (if a ≥ 1), hence |x^a y^b| < |τ| and |f| = |τ| ≠ 0:
no singular point. (Same with y.) The tube is gcd(a, b) open annuli.
**Base-point crossing** (B(Q̄) = 0 for all members, f = xy + τ(αx + βy) + τ·O(2), αβ ≢ 0 mod m): the critical
point is P_0 ≈ (−τβ, −τα) with f(P_0) ≈ −τ²αβ + O(τ³) ≠ 0: no singular point; the tube is an annulus of
modulus |τ|².
Use of C2 in 32R-73 type (d) (e_E = 1, x·E = 1, M_p reduced along E): b_λ̄ has one zero on E; in residue discs of
smooth points of (M_p) f_x or f_y is a unit (no singular point); at a crossing point Lemma C2 gives δ ≤ 1. Hence the
type-(d) contribution is ≤ 1, as used. C2 is now a proved lemma, not an assumption.

## J. Write-up of A2 and A3

References: [BPR] M. Baker, S. Payne, J. Rabinoff, "On the structure of non-archimedean analytic curves",
Contemp. Math. 605 (2013) (semistable vertex sets, skeleta, genus formula); [BL] S. Bosch, W. Lütkebohmert, "Stable
reduction and uniformization of abelian varieties I", Math. Ann. 270 (1985); Berkovich, "Spectral theory ...".

Setting. K a complete discretely valued field of residue characteristic p (after a finite extension, which does
not change genera), X = C_0^ν the normalization of C_0, a smooth projective connected curve over K, X^an its
Berkovich analytification. For a type-2 point x let g(x) be the genus of its residue curve.

**Fact 1 (genus formula, [BPR] Thm 4.22 / Cor. 4.23).** For any skeleton Γ of X^an (the skeleton of a semistable
vertex set), g(X) = b₁(Γ) + Σ_{x ∈ Γ type 2} g(x), and g(x) = 0 for all type-2 points outside Γ.

**A2 (additivity over a decomposition).** Let X^an = (⊔_i U_i) ∪ (⊔_j A_j), where the U_i are pairwise disjoint
connected analytic domains and the A_j open annuli, each A_j adjacent to (at most) two of the U_i at its two ends,
and such that the union is a disjoint union of sets. Put G = the graph with vertices U_i and edges A_j, and
g(U) := b₁(Γ ∩ U) + Σ_{x ∈ U} g(x) (computed with any skeleton Γ containing the skeleta of the annuli).
Then g(X) = Σ_i g(U_i) + b₁(G) ≥ Σ_i g(U_i) + b₁(G).
*Proof.* Enlarge a semistable vertex set so that it contains the boundary points of all U_i and the skeleta of
all A_j (always possible, [BPR] §5). Then Γ is the union of the subgraphs Γ ∩ U_i and the edges Γ ∩ A_j (the
skeleton of an open annulus is an open segment), and b₁(Γ) = Σ b₁(Γ ∩ U_i) + b₁(G) because contracting each
connected Γ ∩ U_i to a point yields G (homotopy invariance of b₁ for contractions of connected subgraphs; the
contracted subgraphs are connected because U_i is connected). Fact 1 then gives the formula; genera of type-2
points are counted in exactly one U_i. ∎
In the uses (32R-73: 27771, 25329, 28246; 32R-74 §H) the U_i are the tubes sp⁻¹(Z) of closed subsets Z of the
special fibre of the flat closure 𝒞 of C_0 (pulled back to X), and the A_j are tubes of crossing points (annuli by
§I) or the pieces of good reduction between them; a tube over a connected closed subset need not be connected,
which is why the formula is written with the number c_Z of its components, and only the inequality
"g(Y_Z) − c_Z ≥ −(number of ends)" (each component has an end since X is connected) is used for bad specials.

**A3 (pieces with smooth or singular reduction).** Let U ⊂ X^an be an affinoid domain with a formal model 𝒰 =
Spf A, A = R⟨…⟩/(f), whose special fibre Ū is reduced and irreducible. Then A is the ring of power-bounded
functions of A_K (reduced special fibre), so Ū is the canonical reduction and U has a unique Shilov boundary
point x, whose residue field is the function field of Ū. Hence g(U) ≥ g(x) = genus of the normalization of the
projective completion of Ū (= geometric genus). In particular:
 - smooth irreducible Ū with completion of genus h (the cyclic-cover pieces of 32R-73/74): g(U) ≥ h;
 - singular Ū (28246, r = 3, ν = ±1402): g(U) ≥ geometric genus of Ū (computed by genus() in normal.lib).
And by A2, disjoint pieces add: g(X) ≥ Σ g(U_i). This also re-proves the "generalised Lemma G" of 32R-73.
The reduction curves were computed in characteristic p from the char-p data (limits λ → 0 of the scaled
equations), which is legitimate because Ū depends only on f mod m after the scaling.

## K. M2 paper check of the d = 12 / 14 pencils, and a new gap class (2026-11-04)

Paper check. For a pencil, a hypothetical C_0 reduces to a char-p member M. (i) If M is reduced, every singular
point of M is a critical point of the pencil (outside the base points, which are simple) and its Milnor number is the
length of the critical scheme there; δ ≤ μ for reduced curve germs, so Σδ(M) is bounded by the per-fibre critical
counts summed over the decompositions (hidden-set check). Then Σ g(components) = p_a − δ(M) + r − 1 ≥ p_a − Σδ, and
Lemma G gives g(C_0) ≥ p_a − Σδ. So the 32R-60/69 bounds (1959: ≥ 3; 1309, 1382, 1384: ≥ 3; 1480: ≥ 6; 2020: stage 2
genus 5) remain valid for reducible reduced members. (ii) Non-reduced members are NOT covered by (i): their multiple
component may be an exceptional curve E (e ≥ 2 at a node) or a known curve, which the node-saturated critical scheme
does not see. The old text treated them as "not integral" (the M1 error).
Scan (fasth0, mod p): h0_p(D + 2Γ) over the 140 curves / nodes (and direct Singular for the cap cases, m2b):
non-reduced members exist in all six pencils — 1959: 2 (e = 2 at nodes 112, 116), 2020: 4 (nodes 111, 112, 119,
120), 1309: 1 (node 120), 1382: 1 (2·K3, the critical conic), 1384: 1 (2·K6), 1480: 3 (nodes 119, 126, 135); all have
Σ g ≤ 1 (stoll/m2b). Closure (stoll/m2c, same decomposition as §H; in a pencil the second member B is fixed, and B
cannot vanish on an x-trivial configuration Z, otherwise Z would be a fixed component): every special is good, and
g(C_0) ≥ 7 (1959, 2020), 9 (1309, 1382, 1384), 8 (1480) — equal to p_a in every case. **d = 12 / 14 pencils closed.**
New gap class at d = 16. The same non-reduced members (2E at a node with x·E = 0, or a known curve doubled) occur in
the d = 16 pencils and nets and were invisible to the 32R-69 pipeline (node_jobs.py only treats nodes with x·E ≥ 2).
Scan over the 288 d = 16 h0 ≥ 2 reps (m2/scan16.json): ~200 reps have such members; 1390 single members (stoll/m16,
running) and 14 one-parameter families (nets 27685, 27769 (8 nodes), 28244, 28246, 28255; m16/families.json).

## L. d = 16 non-reduced members: status (2026-11-04, stoll/m16, m16u, fam; analyzer m16/an2.py, m16/web.py)

Analyzer v2 (an2.py): g(C_0) ≥ 1 + Σ_{certified pieces} g + #certified annuli − #certified pieces (bad tubes
contribute ≥ 0; A2). Pieces of multiple components are cyclic covers (split covers counted with their number of
components); for a multiple sheet the zeros of B|_Γ are placed worst-case. Checked: identical to §H on all 58
re-closed nets; additionally closes 25329 (≥ 7) and the 27771 double-conic family (≥ 5) automatically.
For webs (h0 = 4) the bad set of a locus is a point / line in the P² of directions; all intersection points of
bad lines, generic points of each line, and a generic point are tested (web.py).
Single members found by the scan (1390 jobs):
  Lemma G 294; analyzer OK 608 (pencils / nets) + 56 (webs); no member (cap cases) 390;
  timeouts 5 → closed by containment + smooth remainder (m16u: remainder smooth, p_a 5 ⇒ Σg ≥ 5);
  28246 (3 jobs) = the dm_1_0 member, closed in 32R-73 by the E17 regime analysis;
  OPEN (bad-direction cases with an e = 3 node of type (2,2,1,1)): net 28255 (curves 5, 6 doubled; 2 jobs),
  net 28760 (4 jobs), web 27769 (two members, 16 jobs), web 28244 (two members, 12 jobs). In webs the low value
  occurs at the intersection of the bad lines of two configurations, each containing an e = 3 node.
One-parameter families (17: 14 from the scan + 3 cap cases 27523_121, 27685_94, 28244_117): the generic member
has Σg ≥ 5 (a moving curve of genus 5 or 8; stoll/fam); the finitely many special members are still to be found.
Bug note: the m16 tail defines an int `b1`, which shadows the ring variable b1 in code written after it. Checked:
no polynomial literal uses b1 after that line in tail.sing / tail_web.sing (m16 results unaffected); the first
m16u run was affected (spurious "CONTAINS 33–36") and was redone with `kill b1;`.

## M. e = 3 nodes in the bad direction: 28255 and 28760 closed (2026-11-04, stoll/c55)

Tool c55/gen.py (generalises c28): for a member M, its bad configuration Z and an e = 3 node P of type (2,2,1,1):
W = members vanishing on Z (x-sense), W2 = W with excess 2 at P; B* ∈ W \ ⟨NN⟩; chart P + λu; limit curves of
F_M + τB* + τ'B3 in the regimes of r = v(τ')/v(τ); components of the limit that are rulings of the tangent cone
(fixed D-curves through P) are discarded; genus of the genuine piece; discriminant of the critical regime and the
genus (or, over F_p², the singular-point count) of its special fibres. Bound used: g(C_0) ≥ (analyzer value in
that direction) + g(Y_Z), and g(Y_Z) ≥ g(E-piece) + b₁ (loops through the E-piece inside Y_Z).
Local facts used (proved as in §I): at a crossing of a multiplicity-1 component of Z with the e = 3 curve E, with
B* = y·w^k·unit (k = excess), the tube is an annulus (critical regime) or a sphere with 3 or 4 holes (degenerate
regimes) joining the pieces of the different scales.
- 28255 (net, Zb = {K5², K6², G31, G32, E19, E21 (e = 3), E27..E30}, analyzer 0 in the bad direction):
  W = W2 (dim 2 incl. NN) mod p AND over Q(ζ8) (c55/h0c.sing: net 3, W 2, W2 2), so B*_0 has excess 2 at E21
  (no w-term). β2 = B*|_E21 has the four simple zeros ξ_K5, ξ_K6, ξ_G31, ξ_G32 (B* = K5 + K6 + Y_8 (genus 5,
  not through the node) + G31 + G32 + …). Regimes: r < 3: v³a + c, genus 2; r = 3: genus 2, at ν = ±1021 genus 1,
  plus the loop E21-piece – G31 – E19 – G32 ⇒ g(Y) ≥ 2; r > 3: double cover of genus 1 + two loops through the
  pants at ξ_G31, ξ_G32 ⇒ g(Y) ≥ 3. Hence g(C_0) ≥ 2 in every regime. **Closed.**
- 28760 (net, Z1 = {K1², K3, E13, E16, E32 (e = 3), E46}, analyzer 1 in the bad direction): W dim 2, W2 dim 1, so
  B* has excess exactly 1 at E32 (automatic in char 0: excess cannot drop under reduction). Local equation
  a w³ + τ γ w + τ' c with γ vanishing at ξ_K1, ξ_K3. Regimes (critical r = 3/2): r < 3/2: genus 2; r = 3/2:
  a v³ + γ v + ν, generic genus 2, special ν with ν² = 4981 or 1818 (over F_p²): exactly one new affine singular
  point of length 1 (ordinary node), singularities at infinity unchanged ⇒ genus ≥ 1; r > 3/2: a v² + γ = 0 is a
  connected genus-0 double cover with two points over ξ_K3, both joined to the 4-holed local piece at ξ_K3 ⇒ a loop.
  Hence g(C_0) ≥ 1 + 1 = 2 in every regime. **Closed.**
Remaining: webs 27769 (2 members) and 28244 (2 members) — there W/⟨NN⟩ is 2-dimensional and W2 ≠ W, so all four
Newton-polygon points (μ, γ, β, a) can be active; and the 17 one-parameter families.

## N. Loop and hub lemmas; all single non-reduced members closed (2026-11-04, m16/an2.py, m16/web.py)

Setting: direction bad for the configuration Z, C_0 = M_0 + ΔB, ΔB = μ·B3 + (W-part), W = members vanishing on Z,
μ ≠ 0 (C_0 ≠ member containing Z). All local claims are proved like §I (solve the local equation for one variable).
- (mult-1 × mult-1 inside Z) at Q = K ∩ K' (both mult 1, both in Z): W-part ∈ (xy), f = xy(1 + h) + μc: annulus.
- (mult-1 in Z × sheet X of mult 1): W-part ∈ (y), f = y(x + h) + μc: annulus (coordinate change x' = x + h).
- Connector lemma (X of mult 1, H ∈ Z of mult m ≥ 2, local M = x·y^m): f = y(x y^{m−1} u + h) + μc; solving for x,
  the tube sp⁻¹(Q) contains a connected component (the outer annulus in the y-disc) adjacent to both the X-piece and
  the H-region. Other components of sp⁻¹(Q) touch only the H-region.
- Hub lemma: sp⁻¹(H°) is finite flat of degree m over the tube of H° (Weierstrass preparation, F_M = a·w^m with a a
  unit on H°), so every component of it is adjacent to the tube of every point of H \ H°. Modelling all of
  sp⁻¹(H°) by ONE vertex of genus 0 joined to each multiplicity-1 neighbour gives a lower bound for b₁ (merging the
  c components into one vertex lowers b₁ by (c − 1)(deg − 1) ≥ 0; dropping multiple × multiple crossings lowers b₁).
  Loop lemma = special case (two mult-1 neighbours of a hub joined inside Z).
- Analyzer v3 = max(old model, hub model) per direction; also the bad direction of an E-sheet × curve-sheet node
  incidence (BADN: B|_C vanishing at P beyond the generic order, in the x-sense G^{(DM+1)} + G^{(DM)}·m_P^k) is now
  computed instead of always counted as bad. Two bugs found and fixed while doing this: unsaturated QL + m_P^k
  (membership test wrong in degree < k) and D-curves (restriction trivially zero; x-sense condition needed).
Checks: the 92 net members never decrease (62 increase); 28255 and 28760 are now closed automatically, in
agreement with §M.
Result for the 1390-job scan: pencils/nets: Lemma G 294, analyzer OK 617, no member 390, timeouts 5 (closed in
m16u); webs: 84/84 OK. **All single non-reduced members of d = 16 are closed.** Remaining: the 17 one-parameter
families (special members).

## O. The 17 one-parameter families (2026-11-04, stoll/fam, famc, famd)

Each family is a pencil P ⊂ |x| (inside a net or web), M_s = Fix + Y_s; the generic Y_s is irreducible of genus 5
(genus 8 for the eight 27769 families), so generic members are closed by Lemma G. Special members are found as
follows (Lemma G needs Σ g(components of Y_s) ≥ 2, or the analyzer on M_s):
1. Representation 1 (the pencil in |x|, base locus D ∪ Fix): critical scheme off base locus and nodes (famc/c_*).
2. Representation 2: Y_s ∈ |y|, y = x − Fix, with a second decomposition D2 of m·K − y found by MILP that shares no
   curve with D ∪ Fix (famd/milp.py; all 17 at m = 2 with h0 = 2): critical scheme again (famd/r_*).
   Points hidden in both representations: (D ∪ Fix curves) ∩ (D2 curves) off the nodes (146 pairs) — for each such
   point P the members with Y_s singular at P were solved for directly (famd/h_*): only one, 28244_124 (rep 2, u = 1488,
   Y = G77 + G79, Σg = 2).
3. Nodes: blow-up charts at every node (6 charts per node), critical points of the strict-transform pencil on E_P,
   and members containing E_P beyond the generic order (famd/n_*, n2_* for both representations). Singular points
   of Ỹ_s on E_P can only lower the genus by at most the critical length there; per special fibre the total was compared
   with g(Y) − 2; F_p fibres above the bound are decomposed directly.
4. Base points: the families have no isolated base points off the nodes in either representation (famd/b_*, b1_*).
Results: rep-1 special members over F_p: 37 + 136 = 173, all closed (Lemma G 121 + the earlier 29, analyzer 52 + 8);
rep-2 special members over F_p: 134 + 32: Σg ≥ 2 for 82 + 24; the 52 + 8 with Σg = 0 are unions of known conics and
were matched (by the linear condition "contains these conics") to rep-1 members already closed. 27523: the critical
curve fibres split over F_p (4 members, all closed). Extension-field fibres above the δ bound: only 28244_117
(a quadratic and a quintic factor): the union of the conjugate Y's has genus G = 9 resp. 21, so each member has
Σg ≥ (G + #conj − 1)/#conj = 5.
Bug found and fixed in step 3: in the node charts the members were divided by l^{oG} with polynomial division, which
is wrong when oG ≥ 2 (sbm(F) is divisible by l^{oG} only modulo the surface equations). Fixed with
division(sbm(F), XS + (l^{oG})) (no remainder in any case); all 34 node runs redone. After the fix: no new F_p member
and NO extension-field factor above the δ bound (the 28244_117 quadratic / quintic "4 nodes" were artifacts of the
bug — consistent with the exact union genus G = 9 / 21 found before). The c28 / c55 limits used saturation and are
unaffected; the m16 single-member analysis does not use charts.
5. Base points on the E_P (rep 1, corrected charts, famd/nb1_*): non-simple base-point components only for the eight
   27769 families (one node each, 2 points, length 2). They are embedded points on a fixed curve of the family
   (the members contain that fixed curve). In representation 2 (where that curve is not fixed; same chart) the
   point is a simple base point of the Y-pencil (local length 1, every member smooth there, no member singular):
   famd/bq2_*. So Ỹ_s is smooth there for all s.
**All 17 one-parameter families are closed.** With §N: every non-reduced member of d = 16 (the gap of §K) is closed.
