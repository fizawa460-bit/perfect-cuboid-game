# Audit package R2 — Stage32 / 32-02: no curve of degree 12, 14 (all classes) or 16 (unibranch-compatible classes) with geometric genus ≤ 1 (research level, revised)

Compiled 2026-11-04, revised 2026-11-05. Supersedes, for re-audit, `AUDIT-PACKAGE-32-02-D12-D16.md` (round 1, PAPER
AUDIT FAIL; that file is kept unchanged as the audit master of round 1). **This is the single file for the re-audit**:
it contains the response to round 1 and to the round-2 reading audit (§R below); the former cover letter
`AUDIT-RESPONSE-32-02-D12-D16.md` is merged into it.
Sources: research logs 32R-38 … 32R-80 (local, `claudework/stage32_research/`); code paths are relative to
`stage32_research/stoll/` unless stated otherwise.

- **Status:** research level, zero credit. No ledger / STATE / credit change. Merged predecessors: d = 8 (#1844),
  d = 10 (#1845), both audited.
- **Audit standard (owner decision, 2026-11-06).** The goal is to check that nothing is wrong. A reading audit that
  checks the arguments, and what each computation decides, is sufficient. Re-executing the computations is optional,
  not a condition for acceptance. Under this standard the fifth audit (§R.6, PASS with should-fix items only, all
  answered) is a PASS for this package.
- **This package is for a paper (reading) audit.** It is meant to be readable without the logs: every argument that
  replaced a round-1 tool is stated with its proof (Appendices A–D), and the representative computations are
  described in enough detail to judge what they decide (Appendices E–G).
- **What is not closed** (§5, §7): M7 (13 nets via the μ filter). Its argument is now written out and recomputed here
  (Appendix J); it rests on route-E E02 / E04 (executing audit PASS) and on E03 (1), whose revision 2 is reproduced with proof in
  Appendix K **for re-audit together with this package**.
  The item found
  while compiling this package (§4.7: the "2Γ-families" of the d = 16 net D-check, closed in round 1 by "the
  residual is reducible", the M1 error) has been redone with Lemma G and the Appendix G procedure (§4.7, 32R-75).

Arithmetic: mod p = 10009 (p ≡ 1 mod 8, ζ8 ↦ 792) unless "exact over Q(ζ8)" (Singular ring (0,z), minpoly z⁴ + 1) is
stated.

---

## R. Response to the audits

### R.1 Round 1 (8 audits, PAPER AUDIT FAIL): must-fix items

| # | must-fix item | status | where |
|---|---|---|---|
| M1 | T4 "reducible / non-reduced mod p ⇒ not integral in char 0" is false | **replaced** by Lemma G and the pieces/loops bound T7; every use recomputed; in addition the non-reduced members invisible to the round-1 pipeline were found and closed | §2.2, §2.6, §3, §4, App. A–D |
| M1′ | same direction error in T2 (containment) and fixfilt (fixed component) | **fixed** by exact h⁰ over Q(ζ8) | §2.3, §4.2 |
| M2 | char-0 singular points reducing into removed loci | **reformulated** as statements about all char-p members | §2.5, §3 |
| M3 | floating-point y-enumeration at d = 14, 16 (C1) | **fixed**: exact integer re-run, identical output | §1 |
| M4 | does T1 compute \|x\|? | answered | §2.1 |
| M5, M6 | d = 12 orbit correspondence; reps 1215, 2020 | answered | §1 (M5), §3 (M6) |
| M7 | 13 nets excluded by the μ filter depend on route-E E03/E04 (C2) | **closes with App. J–K**: corollary proved, 13 nets recomputed (J), E03 (1) reproduced with proof for re-audit (K) | §4.4, §5, App. J, K |
| (new) | 2Γ-families of the d = 16 net D-check and the 27988 P0 member, closed in round 1 by "residual reducible" (the M1 error); found while compiling this package | **redone** (Lemma G + App. G; extension-field fibres by a direct singularity check over F_p(α)) | §4.7, App. G |
| (new) | round-1 "type (e)" bound δ ≤ 3 (flag C3) failed for 61 net members | **repaired** by T7 | §6 |

### R.2 Round-2 reading audit (HOLD): must-fix and must-check items

| item | answer | where |
|---|---|---|
| A2 citation and decomposition (sp is anti-continuous; tubes of closed vs. open sets) | citation corrected to [BPR] Remark 4.18, formula (4.18.1) ([BL85] Thm 4.6) and Remark 4.17; base change to C_p; decomposition into closed tubes of open strata and open tubes of points, limit boundary [BPR] Lemma 3.2; τ-saturation U_i = τ⁻¹(Γ ∩ U_i); subgraph lower bound | App. B |
| A3 needs geometric reducedness | added as a hypothesis; satisfied by every piece the analyzer uses (Kummer covers); geometric irreducibility is not needed (A3 revised after the third audit, R.4); App. E–F (singular limit curves) are no longer used for any closure (§R.3) | App. B, E, F |
| bad tubes in the analyzer (adjacent annuli) | an edge is counted only if both ends are certified pieces, i.e. bad tubes are dropped together with all adjacent annuli (the valid rule) | App. D |
| connector lemma: hypotheses | written out, (i)–(v) | App. C.4 |
| web strata (isolated bad points, bad points on lines, extension-field points) | `web.py` tests the generic point, every bad point, a generic point per bad line and all pairwise intersections; all bad loci are F_p-linear | App. D |
| zero collisions on multiple sheets (good strata) | not covered before; fixed (all partitions of the free zeros); all analyzer members re-evaluated (881 distinct; the earlier count 965 included 84 superseded duplicates of web members): no bound changed by this item | App. D |
| the lift M_0 needs all components known | conics (6559, all known) and degree-4 genus-1 components (211 in 190 members), all identified with known curves by ideal equality, 0 unknown | App. D |
| positive-dimensional critical loci not discarded | none discarded (no critical curve outside a fibre; the only non-linear critical-curve fibre polynomial, 27523_121, splits over F_p) | App. G |
| h⁰ = 2 in representation 2, per family | checked for every family (17 in §4.6, 22 in §4.7) | §4.6, §4.7 |
| §4.7, M7 | §4.7 redone; M7 → App. J–K | §4.7, §5, App. J |

### R.3 Independent audit of R2 (HOLD, 2026-11-05)

| item | answer | where |
|---|---|---|
| 1. hub lemma: merging the components over a multiple curve H into one vertex can create cycles (MUST FIX) | **agreed — the merged model was invalid**, and so was the "loop lemma" (same merging). Replaced by (a) the hub-cluster bound: each component of the cover over H° has genus ≥ g(H), components carrying no certified edge are left out, so the cluster contributes ≥ −min(m, h) (g(H) = 0) or ≥ 0 (g(H) ≥ 1), h = number of certified connector edges; (b) b₁ = E − V + (number of connected components) instead of E − V + 1 (splitting a vertex never lowers the component count); (c) for the 24 members where (a) is not enough, a proof that all connector edges of the e = 3 hub lie on one component (fibre-product argument, App. C.4). Loop lemma removed. Result: all 881 analyzer members ≥ 2 | App. C.4, D; 32R-76 |
| 2. A3 (geometric reducedness of limit curves) | no closure depends on App. E–F any more: their members are closed by the corrected analyzer (App. D); App. E–F are kept as independent consistency checks (their regime genera agree with the hub computation) | App. B, D |
| 3. M7 | the μ-filter corollary (route-E E05.1, unaudited there) is proved in full in App. J, and μ is recomputed for all 23 nets (exactly 13 have μ = 16). The status of the cited route-E results (GitHub STATE): E02 and E04 executing audit PASS; E03 audit FAIL on one wording item, fixed in revision 2, **re-audit pending**. the part of E03 rev 2 that is used, E03 (1), is reproduced with its proof in App. K for re-audit with this package; M7 closes if J–K pass | §5, App. J, K |
| 4. C5 scope | the title now states the scope: d = 12, 14 all classes; d = 16 unibranch-compatible classes (71,697 of 1,737,363); multibranch is stage 32-03 | title, §4 |
| 5. counts | all reconciled at ID level, no missing case: d = 12 (rep 1215 has h⁰ = 1 under the v1 ideals, 0 under v2); d = 14 (43 reps processed twice: 18 of the 141 and 25 of the 1320 also appear in the 62 containment jobs); d = 16 pencil stage 2 (5 duplicate jobs) | §3, §4.3 |

---

### R.4 Third audit (independent PAPER AUDIT, HOLD, 2026-11-05)

| item | answer | where |
|---|---|---|
| 3. A3: separable ⇒ geometrically reduced, but not geometrically irreducible (MUST FIX) | **agreed**: irreducibility was claimed without proof. It is not needed. A3 is restated for a reduced reduction with s irreducible components over k̄ (one Shilov point each): Σ over connected components of (g − 1) ≥ Σ_j (h_j − 1) (A3.1), and for a cyclic cover Σ_j (2h_j − 2) is the Riemann–Hurwitz sum of the whole cover (A3.2), whatever the splitting. The analyzer uses only this product (`tot += c·(g′ − 1)`), and the component count k is taken on the model graph (splitting never lowers k). So no bound changes, and no re-run is needed | App. B (A3), D |
| 4. e = 3 hub connectedness (MUST CHECK) | deg g = 1 / 2 / 3 now separated (deg 1: g is an automorphism, so the fibre product ≅ E). The coefficient shapes are checked on the data for all 16 hub computations (`e3h/shapes.py`: BE = L·M·c, AA = κ·L·M²·c, GA = κ′·L·c or 0; Q₁ ≠ Q₂; M has two distinct zeros; no common zero of L and M; zeros of c only at crossings): all OK. 28246 has no l¹ term, so deg g ∈ {2, 3}. 28244 is also excluded by the μ filter | App. C.4(c) |
| 5. history mixed with current proof (DOCUMENT FIX) | App. D now states the v4 rules as the only rules used; v1–v3 (constant 1, hub weight −1, loop lemma) are marked "History (not used)"; the round-2 answer in App. D point 1 is marked superseded; §4.4 (28246 dm_1_0) and §4.5 now cite the analyzer v4, and App. E–F are headed "consistency check only" | §2.6, §4.4, §4.5, App. D, E, F |
| M7 | logic PASS (given E04); the μ values of the 13 reps are reproducible with `stoll/mu_nets.py` (exact integers) | App. J |
| 881 results | not re-executed by the auditor; reproduction: `famg/recheck_hub.py` (857), `e3h/final.py` (24) | App. D |

### R.5 Fourth audit (independent PAPER AUDIT, HOLD, 2026-11-05)

| item | answer | where |
|---|---|---|
| A3 (Kummer splitting), e = 3 fibre product (degrees 1, 2, 3), withdrawal of the old hub / loop lemmas | PASS (auditor) | — |
| 28246: c ∝ u₁ vanishes at the connectors Q₁, Q₂, but connector hypothesis (iii) needs c(Q) ≠ 0 (MUST FIX) | **two different c's**: the data c is the coefficient of the *form* (the system is given as forms vanishing on a fixed curve D); (iii) is about the *moving part* c′ = c / (trace of D on E). Computed for all 16 hub files: zeros of c = trace of D on E exactly (`e3h/tr/`, TRACEMATCH 1 ×16). For 28246 (3 files) the two D-curves through the node pass through Q₁, Q₂ (they are the connectors C₃, C₄, D-curves with excess 1). So c′ is a nonzero constant and (iii) holds. Ratios, normal form and (ii) are unchanged for the moving part | App. C.4(c) "Which c" |
| reproducibility of the 881 results | not re-executed by the auditor; scripts: `famg/recheck_hub.py`, `e3h/final.py`, `e3h/shapes.py`, `e3h/tr/`, `mu_nets.py` | App. D, J |

### R.6 Fifth audit (reading audit of R2, PASS — conditional, 2026-11-06)

| should-fix | answer | where |
|---|---|---|
| 1. stale wording: App. D "Bad directions", §2.6 "tubes of closed subsets", §7 Q3, Q5 | rewritten to match App. D item 2 and A2 (revised) | §2.6, §7, App. D |
| 2. App. B "how it is used" bound has +1, analyzer has +k | stated with k(G′) = number of connected components (b₁ = E − V + k); +1 remains a weaker valid bound | App. B |
| 3. App. C.4 last item (e = 3 crossing tubes) rests on App. F | marked "not used by the analyzer v4 certificate" | App. C.4 |
| 4. δ ≤ μ in char p | Deligne, SGA 7 XVI: μ ≥ 2δ − r + 1, with δ ≥ r − 1 | §2.5(i) |

The auditor also withdrew their round-2 acceptance of the one-vertex hub model (agreeing with the withdrawal in R.3).
Not re-executed by the auditor: logs 32R-75…79 and the scripts listed in R.5.

## 0. Setting and notation (unchanged)

- S ⊂ P⁶ the cuboid surface: a₁² + a₂² = b₃², a₂² + a₃² = b₁², a₁² + a₃² = b₂², a₁² + a₂² + a₃² = c². 48 A₁ nodes N_k;
  S̃ the minimal resolution, exceptional curves E_j.
- 92 known curves G_k (Stoll's list; contains all conics). All are smooth, also at the nodes, in char 0 and mod p
  (checked, §5 A5).
- A class x ∈ Pic(S̃): d = K·x, x² = C², m_j = x·E_j. Goal for d ∈ {12, 14, 16}: no class of degree d carries an
  integral curve of geometric genus ≤ 1 apart from the known curves.
- p_a = p_a(x). A member of |x| is written M; for a decomposition mK − x = D, members ↔ forms of degree m in I(D).
- **Char-0 / char-p setup used throughout.** R = a DVR of a number field over p (enlarged by finite extensions when
  needed), K = Frac R, k = residue field. S̃_R = blow-up of the 48 nodes over R (smooth over R near every locus used,
  A5). A hypothetical integral curve C_0 ⊂ S̃_K of class x and genus ≤ 1 has a flat closure whose special fibre
  M_p = red(C_0) is a member of |x|_p ("the reduction").

---

## 1. Enumeration of candidate classes (C1 / M3 resolved)

The split method of round 1 (x = (y, m), y ∈ Λ rank-16 odd unimodular, m ∈ Z⁴⁸_{≥0} with the parity code, packing
x·G_k ≥ 0, x² ≥ c2min; Fincke–Pohst for y in the ball of radius d²/16 + d/2, DFS for m; orbit reps under the group of
order 1536) is unchanged, **except that the y-stage is now exact** (`split/splitenum9x.c`, `split/gen_exact.py`,
`split/x14.sh`, `split/x16.sh`):

- the LDLᵀ data of the rank-15 form are recomputed from the lattice with rationals (lcm of denominators: U 24, D 12);
- Fincke–Pohst ranges use Rem = DD·L²·rem in int64 and an exact integer square root;
- the Cauchy–Schwarz prune is the exact test "V < 0 and V² > nr·σ²" with V, nr, σ² rational (__int128).

No floating-point comparison decides any branch. Outputs compared as sets of 64-vectors with the round-1 production
runs:

| d | geometric reps (round 1) | exact re-run | used here |
|---|---|---|---|
| 12 | 2029 | 2029, identical | all |
| 14 | 1487 | 1487, identical | all |
| 16 | 71,697 unibranch-compatible (of 1,737,363) | 71,697, identical (480 shards, SPLIT_UB + SPLIT_SYMFILE) | unibranch-compatible only (C5) |

d = 12 cross-check with the certified production run (M5): 33,147 production classes; the split set restricted to
the production inventory rules has 1,274,512 classes in 519 lattice orbits; production ⊆ split and every orbit
contains a production class. The full split set (778 lattice orbits, 2029 reps) is a superset and only adds
candidates.

**Remaining dependency:** correctness of the C code (reading audit of `splitenum9x.c` welcome).

---

## 2. Tools (revised)

| round 1 | status | round 2 replacement |
|---|---|---|
| T1 h⁰ via I(D) | kept; M4 answered (§2.1) | — |
| T2 known-curve containment mod p | **wrong direction (M1′)** | Lemma G on the reduction (T4′), or exact h⁰ over Q(ζ8) (T2′) |
| T3 fast genus bound | kept, only for members that are integral mod p | justified by Lemma G with one component |
| T4 reducible / non-reduced mod p ⇒ not integral | **false (M1)** | Lemma G (T4′) + pieces / loops (T7) |
| T5 balanced lemma | kept | — |
| T6 pencils / nets | kept for reduced members, reformulated (M2, §2.5) | non-reduced members by T7 (§4.5–4.6) |
| fixfilt (fixed curve mod p) | **wrong direction (M1′)** | exact h⁰ over Q(ζ8) (T2′) |

### 2.1 T1 — does the ideal compute |x|? (M4)
S is a complete intersection, so H⁰(S, O(m)) = (k[a,b,c]/I_S)_m = H⁰(S̃, π*O(m)). Members of |π*O(m) − D| are the
forms F with ord_{Γ̃}(π*F) ≥ c_Γ and ord_{E_j}(π*F) ≥ c_j.
- Curves: ord_{Γ̃} ≥ c is the symbolic power Γ^{(c)}; Γ is locally principal at smooth points of S, so I_Γ^c has
  embedded components only at the nodes; saturating by the node points and the irrelevant ideal gives Γ^{(c)}.
- Nodes (A₁): m_P·O_S̃ = O(−E) and m_P^c is integrally closed (rational singularity; Lipman), so
  {ord_E(π*F) ≥ c} = m_P^c; its saturation by the irrelevant ideal is the homogeneous ideal.
- The intersection of the ideals is the conjunction. Implementation `fasth0/fasth0v2.py` (mod p), the same ideals
  exact over Q(ζ8) in `fix0/`, `pic0/`. The v1 → v2 bug history of round 1 is unchanged.
- Char-p direction: h⁰_p ≥ h⁰_0 (semicontinuity), so h⁰_p = 0 ⇒ h⁰_0 = 0. This is the only char-p use of T1.

### 2.2 T4′ — Lemma G (replaces T4). Statement; proof in Appendix A.
**Lemma G.** g(C_0) ≥ Σ_i g(Z_i), the Z_i the reduced irreducible components of M_p ⊗ k̄ (geometric genera).

Use: **Σ g(components of M_p) ≥ 2 ⇒ g(C_0) ≥ 2.** Implementation: minAssGTZ over F_p; an F_p-component splitting
into k conjugate curves of genus g′ has Singular genus k·g′ − k + 1 ≤ k·g′, counted as max(0, ·): a lower bound.
With one component (M_p integral) this is "g_p ≤ g_0", the direction already used by T3.

### 2.3 T2′ — exact h⁰ over Q(ζ8) (replaces T2 where Lemma G is not enough, and fixfilt)
- **fixfilt** (d = 16, 146 reps with a curve Γ fixed in |x|_p): h⁰_0(D) and h⁰_0(D + Γ) computed exactly with the
  same component ideals: h⁰_0(D) = h⁰_p(D) in all 146, and h⁰_0(D + Γ) = h⁰_0(D) for all 396 fixed curves (`fix0/`).
  So Γ is fixed in char 0 and |x|_0 has no integral member (x is not the class of Γ). No reduction argument.
- **h⁰ = 1 with all components known** (406 members: d = 16 386 + 5, d = 14 8 + 7): exactly over Q(ζ8), h⁰_0(D) = 1
  and the unique char-0 member contains every listed known curve (401) or extra D-curve / node multiplicity (5)
  (`pic0/`). Hence |x|_0 = {one reducible member}. Needs neither Pic(S̃) nor semicontinuity.

### 2.4 T3 (kept)
Fast genus bound g ≥ p_a − Σ deltaLoc over a superset JP of the singular locus of a birational space model
(`gfast/tail_fast_v2.sing`). δ of a germ ≤ δ of its birational image, so the bound is valid for the char-p curve.
**Used only when M_p is integral**; then Lemma G (one component) gives g(C_0) ≥ g(M_p) ≥ bound.

### 2.5 T6 — pencils and nets: the char-p formulation (M2)
The argument has to exclude every char-p member M ∈ |x|_p that can be red(C_0); no char-0 point is followed into a
removed locus. By Lemma G, red(C_0) is either
- (i) **reduced**: then Σ g(components) = p_a − δ(M) + r − 1 ≥ p_a − δ(M), so g(C_0) ≤ 1 forces δ(M) ≥ p_a − 1.
  Every singular point of M off the base locus is a critical point of the system, with Milnor number = local length
  of the critical scheme, and δ ≤ μ for reduced germs. (In char p: Deligne, SGA 7 II, Exp. XVI ("La formule de Milnor") gives
  μ ≥ 2δ − r + 1 for a reduced plane germ with r branches, and δ ≥ r − 1, so μ ≥ 2δ − (δ + 1) + 1 = δ.) Base points are simple (local intersection number 1: every
  member is smooth there; a char-p computation on the char-p system). Nodes with m_k ≥ 2 are treated in blow-up
  charts (char p). The visible-length / hidden-set / threshold argument of round 1 (several decompositions; hidden
  set empty or treated directly) therefore bounds δ(M) for **all reduced char-p members**, reducible or not.
- (ii) **non-reduced**: δ is not defined usefully, and (i) gives nothing. These members were invisible to the
  round-1 pipeline (§4.5) and are treated by T7.

### 2.6 T7 — pieces and loops (generalised Lemma G). Statements; proofs in Appendices B–D.
For C_0 with reduction M_p, decompose C_0^an by the specialization map along a stratification of M_p (Appendix B,
A2): closed tubes U_i = sp⁻¹(Z_i°) of the open strata and open tubes sp⁻¹(Q_j) of the points — good-reduction
pieces and open annuli. Then (Appendix B, A2)

  g(C_0) = Σ g(pieces) + b₁(graph of pieces and annuli).

Pieces over multiple components are cyclic covers (v^m = −c/a, read off from char-p data), possibly singular and
possibly split over k̄. By Appendix B, A3 (revised), such a piece contributes at least
½(Riemann–Hurwitz sum of its normalised cover), however the cover splits. The local lemmas that identify the
tubes over special points (Appendix C):

| lemma | statement |
|---|---|
| C2 | at a reduced normal crossing of M_p, C_0 has at most one singular point, an ordinary node (δ ≤ 1) |
| C4 / NC lemma | x^a y^b·unit + τ(b₀ + …), b₀ a unit, p ∤ a, b: no singular point; the tube is gcd(a, b) open annuli |
| base-point crossing | xy + τ(αx + βy) + τ·O(2), αβ ≢ 0: no singular point; the tube is one annulus of modulus \|τ\|² |
| mult-1 × mult-1 in Z; mult-1 in Z × sheet | annuli |
| connector | X mult 1 meeting H of mult m ≥ 2 in a bad configuration: the tube contains a component adjacent to both sides |
| hub (corrected, R.3) | the tube over H° is finite flat of degree m over the tube of H° (Weierstrass); its components carrying certified edges contribute ≥ −min(m, h) (g(H) = 0); for the e = 3 hubs of 28244 / 28246 all connector edges lie on one component |

The automatic lower bound (`m16/an2.py`, `m16/web.py`; Appendix D):

  g(C_0) ≥ k + Σ_{certified pieces} (g − 1) + #certified annuli   (k = number of connected components of the certified subgraph),

evaluated for every direction from which C_0 can approach M_p (finitely many bad directions per member, computed by
linear algebra; generic direction in addition).

### 2.7 T5 balanced lemma — unchanged (from audited #1842 §3a, #1843 §6): (6, 6, 12) at d = 12, (7, 7, 14) at d = 14.

---

## 3. d = 12 and d = 14

**d = 12** (2029 reps):
- C² < 0 (1999): h⁰ = 0 ×1918 (T1, safe direction; v2 ideals), h⁰ = 1 ×81: integral residuals with genus ≥ 3
  (T3 + Lemma G). (Rep 1215 had h⁰ = 1 under the round-1 v1 ideals — the round-1 package counted 1917 + 82 — and has
  h⁰ = 0 under the v2 ideals; M6.)
- C² = 0 (30): 28 by the balanced lemma; **1959** (Σδ ≤ 4 < 6 for reduced members, §2.5(i)); **2020** (reduced
  members: the two conjugate heavy members form one F_p-component of degree 24 with fast bound 9; if it splits into k
  geometric components, Σ g ≥ (8 + k)/2 ≥ 5 per member; Lemma G ⇒ g(C_0) ≥ 5).
- **Non-reduced members of the two pencils** (§4.5): 1959: 2 (2E at nodes 112, 116), 2020: 4 (nodes 111, 112, 119,
  120); all Σg ≤ 1; closed by T7 with g(C_0) ≥ 7 = p_a (`m2b/`, `m2c/`).

**d = 14** (1487 reps):

| outcome | reps | round-2 argument |
|---|---|---|
| h⁰ = 0 | 1320 | T1 (safe direction) |
| h⁰ ≥ 1, integral, genus ≥ 3 | 141 | T3 + Lemma G |
| h⁰ = 1 "containment" (round-1 T2) | 62 | Lemma G 22; exact h⁰ (T2′) 8 + 7; remainder R smooth 7 (Σg ≥ 3); R singular only at S-nodes with δ = 1, 18 (Σg ≥ 3 or 5) (`cg14/`, `cgq14/`, `cgp14/`) |
| pencils | 7 | 1179, 1244, 1345: balanced lemma; 1309, 1382, 1384, 1480: §2.5(i) for reduced members (≥ 3, ≥ 3, ≥ 3, ≥ 6); non-reduced members: 1309: 1, 1382: 1 (2·K3, the critical conic), 1384: 1 (2·K6), 1480: 3 — closed by T7 with g(C_0) ≥ 9, 9, 9, 8 (= p_a) |
| balanced lemma (7, 7, 14) | 57 (overlapping) | unchanged |

Partition (`f14v2/f14v2_final.json`): 1487 = 1320 (h⁰ = 0) + 141 (integral, genus ≥ 3) + 19 (unique member contains a
known curve) + 7 (pencils). The 62 containment jobs (`cg14/`: c14f ×35, c14v ×27) = the 19 + 43 reps that are also in
another row (18 of the 141: 743, 759, 943, 944, 1314, 1321, 1322, 1343, 1344, 1346, 1347, 1385, 1386, 1402, 1414, 1460,
1461, 1482; 25 of the 1320: 24, 118, 119, 120, 129, 272, 418, 513, 514, 586, 620, 621, 742, 744, 760, 816, 817, 1011,
1016, 1025, 1104, 1133, 1154, 1236, 1237), processed twice from the round-1 lists; both closures hold.

In a pencil the second generator B is fixed; it cannot vanish on an x-trivial configuration Z (Z would be a fixed
component), so every special is good and T7 gives exactly p_a in all 12 non-reduced members.

---

## 4. d = 16 (71,697 unibranch-compatible reps)

h⁰ (T1): 0 ×67,769; 1 ×3,493; 2 ×406; 3 ×24; 4 ×4; rep 50489 (no m ≤ 3 decomposition): m = 4 gives h⁰ = 0.

### 4.1 h⁰ = 1 (3,493)
| sub-group | count | argument |
|---|---|---|
| member integral mod p, fast bound ≥ 2 | 2128 | T3 + Lemma G |
| round-1 "containment" (T2) | 1365 | Lemma G 773 (Σg ≥ 2); exact h⁰ (T2′) 386 + 5; 201 with an unknown remainder R (degree 12, p_a(R_red) = 6): Sing(R) ⊆ Sing(member), Zariski tangent-space test at every point: 98 R smooth, 103 R singular only at 1–2 S-node points with δ = 1 (generic plane projection with fibre length 1; 28711: fibre length 2, plane δ = 3 used as an upper bound) ⇒ Σg ≥ 5 (`cgq/`, `cgp/`) |

### 4.2 h⁰ ≥ 2 with a fixed curve (146): T2′ (§2.3).

### 4.3 Pencils (265)
Round-1 stage 2 (2746 member jobs = 2012 + 164 + 565 + 5 duplicate jobs, 32R-69): integral members with g ≥ 2 ×2012
(T3 + Lemma G). The 565 "OPEN → non-integral"
and 164 "contains a D-curve" members were recomputed with Lemma G (`cg/`): Σg ≥ 2 ×607; low (Σg ≤ 1) ×116;
not finished ×6.
- **116 low members:** every component is a known curve (ideal equality), so M_0 = D + Σ a_i K_i is a char-0 member
  reducing to M_p. Normal-crossings check (`cnc/`, 116/116 OK): off the nodes pairwise transverse, no triple points,
  the second generator B̃ avoids crossings and multiple components; at the nodes distinct tangent directions, and
  where x·E > 0 B̃ meets every component with local length 1. Base points simple. By the NC lemma (Appendix C.3) C_0
  has no singular point, so g(C_0) = p_a ≥ 2. (Includes 9 members that are non-reduced on S: double conics.)
- **6 timeouts** (`cgp16/`): containment against the 92 known curves leaves R of degree 10 / 12, p_a(R_red) = 5, R
  smooth (tangent-space test; plane δ = 0 as cross-check) ⇒ Σg ≥ 5.
- Reduced members not listed by stage 2: §2.5(i) (the round-1 visibility argument, now read as a statement on all
  reduced char-p members).

### 4.4 Nets and webs (h⁰ = 3, 4; 23 reps)
- **13 nets with μ = 16: μ filter (Appendix J) → M7**, with E03 (1) proved in Appendix K.
- **10 nets with μ = 18, 20 (28 decomposition jobs):** round-1 net candidates, D-check members and the 27988
  cross-decomposition (package round 1 §4b). Round-2 status of the members that round 1 called "reducible":
  - 270 member verdicts (r_, rl_, dm/dm_, dm/rd_) recomputed with Lemma G: Σg ≥ 2 ×178; low ×92.
  - **92 low members** (unions of 4–8 known conics, some with an elliptic quartic; double E's at nodes): all closed
    by T7. 17 by good-reduction pieces / Lemma G (27771 family ×12: two double conics with ≥ 4 branch points each;
    25329 ×2; 34761 dm_0_4 and 27988 dm_1_2: excess elliptic D-curves, Σg = 3; 28246 dm_1_0: analyzer v4 with the e = 3 hub, App. C.4(c), D; App. E is a consistency check only);
    58 re-closed by the pieces/loops analyzer after the C3 failure (§6); 17 by the local types (c)/(d) with C2
    (no e = 2 node). Minimum g(C_0) ≥ 2.
  - **2Γ-families of the D-check: see §4.7 (redone).**

### 4.5 Non-reduced members (a gap found in the revision; part of M1)
Members of |x|_p containing an exceptional curve E with x·E = 0 or a known curve with multiplicity ≥ 2 were never
listed by round 1 (critical schemes saturated by the nodes and the base locus) and were implicitly treated as "not
integral". Scan: h⁰_p(D + 2Γ) over the 140 curves / nodes for every h⁰ ≥ 2 rep (`m2/scan16.py`, `m2b/` for cap cases).
- d = 12, 14: 12 members (§3).
- d = 16 single members (1390 scan jobs): Lemma G 294; analyzer OK 617 (pencils, nets) + 84 (webs, P² of
  directions); no member 390; timeouts 5 (containment + smooth remainder, p_a 5 ⇒ Σg ≥ 5; `m16u/`).
  The members with an e = 3 node in a bad direction (28255, 28760, 28246) are closed by analyzer v4 (App. C.4(a)–(c),
  D). *History:* they were first closed by explicit multi-scale computations (Appendices E–F; `c55/`, `c28/`), which
  are kept only as consistency checks and are not used for any closure.

### 4.6 One-parameter families of non-reduced members (17)
Pencils P ⊂ |x| inside nets / webs whose members all contain 2E or 2K: M_s = Fix + Y_s, generic Y_s irreducible of
genus 5 (genus 8 for the eight 27769 families) ⇒ generic members closed by Lemma G. Special members: procedure of
Appendix G (two representations, hidden points, node charts, base points). All special members closed: 339 over F_p
(Lemma G, analyzer, or identification with a closed member), the hidden-point member 28244_124 (Y = G77 + G79,
Σg = 2), extension-field fibres of 28244_117 by the genus of the union of conjugates (G = 9, 21 ⇒ Σg ≥ 5 per member).

### 4.7 The 2Γ-families of the net D-check (found while compiling this package; redone, 32R-75)
Round 1 (32R-72) found, in 16 D-check jobs of the classes 27882, 27988, 28246, 28255, 28261, 34761 (+ 27988_0
G40/G44), one-parameter families of net members containing (m + 1)Γ for a D-curve Γ of multiplicity m in D
(checked as an identity, `n16/fam/mkfam2.py`, `h_*.out`). They were closed by "the residual R ⊇ Γ is reducible".
**That was the M1 error**: such a member is reduced (R = Γ + R′_q) and can be red(C_0) unless Σ g ≥ 2.
Likewise the single member singular at P0 in the 27988 cross-decomposition argument ("contains a further D-curve").
(27685s_0 is a μ = 16 class and falls under M7.) Redone as follows (`stoll/famg/`, 32R-75):
- **P0 member** (27988_0): components four elliptic quartics, Σg = 4 ⇒ Lemma G.
- **22 (job, line) families**, each the pencil {members of |x| in I(D_t + Γ)} (dimension 2 in all 22), M_s = Fix +
  Y_s, y = x − Fix. Five are identical to §4.6 families (same basis and critical values: 28246_0_0 = 2_0, 28255_0_1 =
  1_0 = 2_0); two (27988_0_0 = 1_0) have the elliptic quartics G40, G42 in Fix ⇒ Σg ≥ 2 for every member. Remaining
  15 jobs (6 pencils).
- **Representation 2**: MILP decomposition D2 of 2K − y sharing no curve with D_t ∪ Fix; h⁰_p(D2) = 2 in all 22, so
  |y| is the family {Y_s}. **Base points**: y² = 0 except 28255_0_0 (y² = 2: two simple base points on E_18, local
  length 1 in both representations, every member smooth there).
- **Generic member**: Y_s irreducible of genus 7 (8 for 28255), plus elliptic fixed curves where present ⇒ Σg ≥ 5.
- **Special F_p members** (Appendix G lists: critical lengths ≥ 2 in either representation, critical-curve fibres,
  members containing E_P, node-critical fibres, hidden points (all F_p-rational)): 695 jobs. Σg ≥ 2 for 647; the 24
  low rep-1 members (unions of known conics, one elliptic quartic in 34761) are closed by T7 (worst bound 3, …, 11);
  each of the 24 low rep-2 members is the Y-part of one of these (same pencil, componentwise). Every other F_p fibre
  has δ(Y_s) ≤ 2 ≤ g(Y) + g(Fix) − 2.
- **Extension-field fibres** (155 irreducible factors of degree ≥ 2 of the special-fibre polynomials, both
  representations; 34761 by the length bound): **direct check over F_p(α)**, h(α) = 0 (`famg/mksx.py`, `sx*_`):
  Y_α = (S + (F0 − αF1)) saturated by D_t ∪ Fix and the irrelevant ideal (degree 12 = generic in all 155); singular
  locus off the nodes by the Jacobian criterion on S (5-minors of [dS; dg], g ∈ generators of Y_α), on each E_P in the
  blow-up charts (strict transform, chart surface written as a local complete intersection: three of the S_i/l and
  (Σc_iS_i)/l² for the linear relation c of the tangent forms). Result: **139 factors Y_α smooth** ⇒ Σg ≥ g(Y) ≥ 7;
  **16 factors singular scheme of length 2 off the nodes** (28246, 28255) ⇒ δ ≤ 2 (a point of multiplicity ≥ 3 has
  Tjurina length ≥ 3, and a double point A_k with τ = k has δ ≤ k) ⇒ Σg ≥ g(Y) − 2 ≥ 5. A member containing E_P
  beyond the generic order is impossible for α ∉ F_p (it needs r0 = α r1 with r0, r1 defined over F_p), so the class
  of Ỹ_α is y and p_a = g(Y). Checks: positive controls (an F_p fibre with known δ = 2 gives length 2; a constructed
  curve with a node on E_P is detected); and the genus of the union of conjugates (§4.6 method) for the 63 factors
  where it finished agrees in every case (smooth ⇔ G = 2g(Y) − 1; for 28255 the factors with G = 11 are exactly the
  four with singular length 2, g = 6).
**Closed** (Lemma G for every member).

---

## 5. Global caveats and flags — status

| code | round-1 caveat / flag | status |
|---|---|---|
| C1 / M3 | floating y-enumeration | **resolved**: exact re-run identical (§1) |
| C2 / M7 | μ filter depends on E03/E04 | **closes with App. J–K** (E02, E04 audited PASS; E03 (1) re-audited here, App. K) |
| C3 / M1, M1′, M2 | char-p directions | T4, T2, fixfilt replaced (§2); every remaining char-p use is h⁰_p ≥ h⁰_0, g_p ≤ g_0 (Lemma G), or a statement about all char-p members (§2.5); §4.7 redone |
| C4 | randomness | unchanged: random bases / fields / projections; failures detected (birationality checks) or conservative |
| C5 | d = 16 scope | unibranch-compatible reps only (stated in the title; multibranch = stage 32-03) |
| hub (independent audit) | merged hub vertex / loop lemma | **invalid, replaced** (App. C.4, D; R.3) |
| A1 | Lemma G | proved (Appendix A) |
| A2, A3 | genus additivity; affinoid with singular reduction | stated and proved from [BPR] (Appendix B) |
| A4 | tameness | p = 10009 divides no multiplicity / cover degree used (≤ 3) |
| A5 | model over R | checked mod p (`a5/`): Sing(S_p) = 48 reduced points (A₁, Tjurina 1); all 92 known curves smooth mod p incl. at the nodes |
| A6 | R-lattice of the linear system | exact char-0 dimensions computed where a basis is chosen (28246, 28255) |
| D1 | generic order at nodes from one member | checked: = min over the basis in all 208 scripts (`d1/`) |
| C3 (32R-74) | "type (e)" bound δ ≤ 3 | **failed** for 61 members; repaired (§6) |

---

## 6. A failed assumption, found and repaired (32R-74 C3)
The round-1 net closure used a bound δ ≤ 3 at double exceptional curves (e = 2, x·E = 0), which needed the
bad-direction member not to pass through the crossing points on E. Checked (`c3/`): false for 61 net members (the bad
member contains the components through the node). 58 had been counted as closed by this bound. All 58 were re-closed
by T7 without any δ bound (`gph/`, `gph2/analyze.py`): minimum g(C_0) ≥ 2 (34761 r_0_19/20), 3 or 6 otherwise.
Sanity: with every special good the bound equals p_a(x) (11; 12 for 27882 / 28255 where x² = 6).

---

## 7. Questions for the auditors
1. §1: is the exact y-stage (`splitenum9x.c`, `gen_exact.py`) a faithful exact version of the round-1 enumeration?
2. Lemma G (Appendix A) and the char-p formulation of pencils / nets (§2.5): valid?
3. Genus additivity over the specialization decomposition (Appendix B, A2/A3): correctly stated and correctly cited
   for the decomposition into closed tubes of open strata and open tubes of points (A2, revised)?
4. Local lemmas (Appendix C), in particular the connector and hub lemmas: "every component of the tube over H° is
   adjacent to the tube of every point of H \ H°".
5. Bad-direction bookkeeping (Appendix D): can C_0 approach M_p only along the directions tested (pencils: the
   second generator; nets: every bad point of P¹ and a generic point; webs: a generic point of P², every bad
   point (isolated or on a bad line), a generic point of each bad line, every intersection of two bad lines)?
6. Families (Appendix G): does the two-representation + hidden-set + node-chart + base-point procedure find all
   special members?
7. Is anything still decided in char p in the unsafe direction (in particular in §4.7, the direct singularity check
   over F_p(α) for the extension-field fibres)?
8. M7 (Appendices J–K): Lemma K (= route-E E03 (1), revision 2) with its standing hypothesis; are the hypotheses
   met by an integral member C_0 of |x|, and is r ≤ μ justified?

---

# Appendices

## Appendix A. Lemma G — proof

**Setting.** R a DVR, K = Frac R, k residue field. X/R projective flat (the model of S̃). C_K ⊂ X_K a geometrically
integral curve, C its flat closure, Z_1, …, Z_r the reduced irreducible components of C_k ⊗ k̄.

**Lemma G.** g(C_K̄) ≥ Σ_i g(Z_i).

*Proof.* Let N be the normalization of C_K̄; after a finite extension R ⊂ R′, N has a semistable model 𝒩. Replace 𝒩
by a regular model and blow up closed points of the special fibre until the rational map 𝒩 ⇢ C ⊗ R′ is a morphism φ
(resolution of indeterminacy on a regular 2-dimensional scheme); the blow-ups add only rational components. Then
g(N) = Σ_v g(W_v) + b₁(dual graph) ≥ Σ_v g(W_v) over the components W_v of 𝒩_k. φ is proper and dominant, hence
surjective, so each Z_i is the image of some component W_{v(i)}, with v(i) ≠ v(j) for i ≠ j. A dominant map of curves
does not raise the geometric genus (Riemann–Hurwitz if separable; purely inseparable maps preserve the genus). ∎

## Appendix B. Genus additivity (A2) and pieces (A3)

References: [BPR] M. Baker, S. Payne, J. Rabinoff, "On the structure of non-archimedean analytic curves", in
Tropical and Non-Archimedean Geometry, Contemp. Math. 605 (2013), arXiv:1404.0279; [BL85] S. Bosch, W. Lütkebohmert,
"Stable reduction and uniformization of abelian varieties I", Math. Ann. 270 (1985); [Ber] V. Berkovich, "Spectral
theory and analytic geometry over non-archimedean fields" (1990).

Setting (revised after the round-2 reading audit). [BPR] works over an algebraically closed complete field. We
therefore base change from K to C_p (the completion of an algebraic closure of K); the geometric genus of X and the
genera of residue curves do not change, and the special fibre of a model only changes by the base change k → k̄.
X = normalization of C_0 ⊗ C_p, X^an its analytification, g(x) the genus of the residue curve of a type-2 point x,
τ: X^an → Γ the retraction to a skeleton.

**Fact 1 ([BPR] Remark 4.18, formula (4.18.1), citing [BL85] Thm 4.6).** For a semistable vertex set V with skeleton
Σ(X, V): g(X) = Σ_{x ∈ V} g(x) + b₁(Σ(X, V)). By [BPR] Remark 4.17 every type-2 point of positive genus lies in V.
(The round-1 / first R2 draft cited Thm 4.22 / Cor 4.23, which are the stable reduction theorem and the uniqueness
of the minimal skeleton; corrected.)

**A2 (decomposition; revised).** The specialization map sp is anti-continuous (preimages of closed sets are open), so
the decomposition is taken along a *stratification* of the special fibre M̄ (of the flat closure, pulled back to the
model of X): finitely many closed points Q_j (crossings, special points of the analysis) and the open strata
Z_i° = (union of components) \ {Q_j}. Then, as sets,

  X^an = ⊔_i U_i ⊔ ⊔_j sp⁻¹(Q_j),   U_i := sp⁻¹(Z_i°) (closed analytic domains; affinoid for affine Z_i°),
                                    sp⁻¹(Q_j) open (residue classes).

Each sp⁻¹(Q_j) is a finite disjoint union of open pieces; where the local lemmas (Appendix C) apply they are open
annuli ("edges"), each with two ends at limit-boundary points of the adjacent U_i ([BPR] Lemma 3.2). Choose V so that
Σ(X, V) contains the Shilov boundary points of all U_i and the skeleta of all annuli, and so that each U_i is
τ-saturated: U_i = τ⁻¹(Γ ∩ U_i). (This can always be arranged by enlarging V, [BPR] §5; it guarantees that Γ ∩ U_i is
connected for every connected component of U_i.) Let G be the graph with one vertex per connected component of the
U_i and of the non-annulus pieces, and one edge per annulus. Then

  g(X) = Σ_v g(v) + b₁(G),   g(v) := b₁(Γ ∩ v) + Σ_{x ∈ v} g(x) ≥ 0.

*Proof.* Γ is the union of the connected subgraphs Γ ∩ v and the open segments Γ ∩ A_j; contracting each Γ ∩ v gives
G, so b₁(Γ) = Σ_v b₁(Γ ∩ v) + b₁(G). Fact 1 gives the formula; each type-2 point lies in exactly one piece. ∎
**How it is used (lower bound).** For any set 𝒱 of vertices that are certified (genus and number of components known
from Appendix C / A3) and any set ℰ of annuli joining two certified vertices, the subgraph G′ = (𝒱, ℰ) satisfies
b₁(G) ≥ b₁(G′) = |ℰ| − |𝒱| + k(G′), k(G′) = number of connected components of G′ (≥ 1), and all other vertices
contribute g(v) ≥ 0. Hence

  g(X) ≥ k(G′) + Σ_{v ∈ 𝒱} g(v) + |ℰ| − |𝒱|   (≥ 1 + … ; the analyzer v4 uses k(G′), Appendix D).

Uncertified ("bad") tubes are dropped *together with all annuli adjacent to them*; no edge is ever counted whose end
lies in a dropped tube (this is the rule implemented in `an2.py`, see Appendix D). Equivalently, a bad tube with c_Z
components and e ends could be kept with weight g − c_Z ≥ −e; dropping it is never better than that and is valid.

**A3 (revised after the third audit: no irreducibility is used).** Let U ⊂ X^an be an affinoid with formal model
Spf A, A = R⟨…⟩/(f), whose special fibre Ū is **geometrically reduced** (reduced after k → k̄). Let Ū ⊗ k̄ have
irreducible components Ū_1, …, Ū_s, with smooth complete models of genus h_1, …, h_s. Then A ⊗ C_p° is the ring of
power-bounded functions, Ū ⊗ k̄ is the canonical reduction, and the Shilov boundary of U is {x_1, …, x_s}, one
type-2 point per irreducible component, with g(x_j) = h_j ([Ber] 2.4.4; [BPR] Thm 4.6(1)). Let U^(1), …, U^(t) be the
connected components of U; each contains at least one x_j, so t ≤ s, and g(U^(i)) ≥ Σ_{x_j ∈ U^(i)} h_j (A2:
g(v) = b₁(Γ ∩ v) + Σ_{x∈v} g(x)). Hence

  Σ_i (g(U^(i)) − 1) ≥ Σ_j h_j − t ≥ Σ_j (h_j − 1).                                              (A3.1)

The right-hand side does **not** depend on how Ū ⊗ k̄ splits. The auditor's example v² = a (a a non-square in k) is
irreducible over k and splits over k̄; (A3.1) is applied over k̄ and counts its two components.

*Cyclic-cover pieces.* For the tube of Z° = Γ \ {crossings} over a sheet Γ of multiplicity m (p ∤ m) the reduction is
v^m = f with f ≠ 0 on Z°, hence separable, hence geometrically reduced. Over k̄ its normalised complete model is the
(possibly disconnected) cyclic cover Y → Γ, and Riemann–Hurwitz for the whole cover gives

  Σ_j (2h_j − 2) = m(2g(Γ) − 2) + Σ_{Q ∈ Γ} (m − gcd(m, ord_Q f)),                                 (A3.2)

whatever the number of components is (also when f is a constant times an m-th power, or when div f is divisible by
some c | m without f being a c-th power on a genus-1 Γ). The analyzer (`an2.py`, `cover(m, g, ords)`) returns a
component count c = gcd(m, ords) and a genus g′ with c·(g′ − 1) equal to half the right-hand side of (A3.2).
**Only the product c·(g′ − 1) enters the bound** (`tot += vv[0]*vv[1] − vv[0]`); the count c is not used elsewhere.
In the graph the sheet piece is one model vertex for the component count k (App. C.4(b): splitting a vertex never
lowers k). So by (A3.1)–(A3.2) the vertex weight is a valid lower bound for Σ_i (g(U^(i)) − 1) in every case,
whether the cover splits over k̄ or not. Multiplicity-1 pieces are tubes of known curves, which are smooth and
geometrically irreducible over R (A5).

The limit curves of Appendices E–F (28246, 28255, 28760) are not used: those members are closed by the corrected
analyzer (App. D, R.3), and App. E–F remain only as consistency checks.

## Appendix C. Local lemmas — proofs

Setting: Q̄ a closed point of the special fibre of the smooth R-surface S̃_R, Ô = R[[x, y]], C_0 with local equation
f = F_M + τB, τ ∈ m. The residue disc of Q̄ is D = {|x| < 1, |y| < 1}.

**C.1 Lemma C2.** If M_0 is reduced at Q̄ with two smooth transversal branches (known / exceptional curves, smooth
over R by A5), take x, y their local equations: f = xy + g, g ∈ τ·R[[x, y]]. Then C_0 ∩ D has at most one singular
point, an ordinary node.
*Proof.* Singular points satisfy y = −g_x, x = −g_y. Φ(x, y) = (−g_y, −g_x) maps D into itself and is a sup-norm
contraction with constant ≤ |π| (all coefficients of g in m), so f has exactly one critical point P_0 in D (fixed-point
theorem; equivalently Hensel, the Jacobian of (f_x, f_y) is ≡ [[0,1],[1,0]] mod m). Its Hessian has determinant
≡ −1: if f(P_0) = 0 it is an ordinary node, otherwise there is no singular point. ∎

**C.2 Corollaries.** (a) If B(Q̄) ≠ 0: |x(P_0) y(P_0)| = |g_x g_y| ≤ |π||τ| < |τ| = |g(P_0)|, so f(P_0) ≠ 0: no
singular point; the tube is the open annulus |xy| = |τ|.
(b) Multiplicities: f = x^a y^b·unit + τ(b₀ + …), p ∤ a, b, b₀ a unit. At a singular point
a x^{a−1} y^b·unit = −τ ∂_x(…) gives |x^{a−1} y^b| ≤ |τ|, hence |x^a y^b| < |τ| and |f| = |τ| ≠ 0. No singular point;
the tube is gcd(a, b) open annuli.
(c) Base-point crossing: f = xy + τ(αx + βy) + τ·O(2), αβ ≢ 0 mod m: P_0 ≈ (−τβ, −τα), f(P_0) ≈ −τ²αβ ≠ 0; the tube
is an annulus of modulus |τ|².

**C.3 NC lemma (pencils).** If Q̄ is not a base point (B(Q̄) ≠ 0), members near Q̄ are level sets {A = −τ} of
A = F_M/B. If M_p is a normal-crossings divisor at Q̄ whose components are reductions of components of M_0, with
multiplicities prime to p, then A = u^α v^β ε over R (ε a unit), and a singular point Q of {A = −τ} in the residue disc
needs α ε + u ε_u = 0 at Q — impossible since it is a unit (α a unit, u(Q) ∈ m). So no singular point of C_0
specializes to Q̄.

**C.4 Bad configurations.** Setting: a direction bad for an x-trivial connected configuration Z, C_0 = M_0 + ΔB,
ΔB = μ·B3 + (W-part), W = members vanishing on Z, μ ≠ 0 (C_0 integral).
- mult-1 × mult-1 inside Z, Q = K ∩ K′: W-part ∈ (xy), f = xy(1 + h) + μc: annulus.
- mult-1 in Z × sheet X of multiplicity 1: W-part ∈ (y), f = y(x + h) + μc: annulus (coordinate x′ = x + h).
- **Hypotheses used in all items of C.4** (stated explicitly after the round-2 reading audit): (i) the local
  equations of the components through Q̄ are part of a regular system of parameters over R (smooth components, A5);
  (ii) the W-part is τ·w with τ ∈ m and w vanishing on every component of Z through Q̄ to the order prescribed by Z
  (x-sense), so w ∈ (y) (resp. (xy)) for the components y = 0 (resp. x = 0, y = 0) of Z, with coefficients in R;
  (iii) c = B3 is a unit at Q̄ (Q̄ is not a base point: `basept 0` in the CROSS data; base-point crossings use C.2(c));
  (iv) μ ∈ m \ {0} (C_0 is integral, so it is not the member containing Z), and h := τw/y ∈ m·R[[x, y]];
  (v) p ∤ m. Under (i)–(v) the claims below follow by solving the local equation for one variable (Hensel /
  Weierstrass, as in C.1).
- **Connector:** X of mult 1, H ∈ Z of mult m ≥ 2, local M = x y^m: f = y(x y^{m−1} u + h) + μc; solving for x, the
  tube sp⁻¹(Q) contains a connected component (the outer annulus in the y-disc) adjacent to both the X-piece and the
  H-region; other components touch only the H-region.
- **Hub (corrected after the independent audit, 32R-76).** U := C_0 ∩ sp⁻¹(H°) is finite flat of degree m over the
  tube of H° (Weierstrass preparation; F_M = a·w^m, a a unit on H°). The round-1/R2 statement "modelling U by ONE
  vertex gives a lower bound for b₁" is **false** (identifying c vertices lying in k components raises b₁ by c − k;
  example H₁–X₁–Y–X₂–H₂), and so is the loop lemma built on it; both are withdrawn. Replacement:
  (a) *Cluster bound.* Write U = U₁ ⊔ … ⊔ U_c. Each U_i is finite over the H°-tube, so g(U_i) ≥ g(H) (glue discs over
  the ends: a finite map of complete curves). Each connector edge (C.4 "Connector") ends on exactly one U_i. Keep in
  the subgraph only the U_i carrying a certified edge (≤ min(m, h) of them, h = number of connector edges): their
  contribution Σ(g(U_i) − 1) is ≥ −min(m, h) if g(H) = 0 and ≥ 0 if g(H) ≥ 1.
  (b) *Components.* g(C_0) ≥ Σ g_v + b₁(Γ′) with b₁ = E − V + k(Γ′), k = number of connected components of the
  certified subgraph Γ′. Splitting a model vertex into the actual components never lowers k, so k computed on the
  model graph (hub = one vertex) is a valid lower bound.
  (c) *e = 3 hubs (28244, 28246; the 24 members not settled by (a)+(b)).* H = E (e = 3, type (2,2,1,1)), the two
  multiplicity-1 neighbours C, C′ (in Z) meet E at Q₁, Q₂. On the E°-tube the equation of C_0 is
  a l³ + T₂ l² + T₁ l + μc (l = equation of E; oG removed). Computed mod p (`e3h/gen.py`, all 4 configurations of
  28244 and both members of 28246): with L, M the linear forms on the conic E vanishing at {Q₁, Q₂} resp. at the two
  multiplicity-2 crossings, ā/c̄ ∝ L M², (l²-coefficient of W2)/c̄ ∝ L M, (l¹-coefficient of W \ W2)/c̄ ∝ L, and
  dim W2/⟨M⟩ ≤ 1. Over R the reduced face coefficients are forced into these shapes: index 1 — a section of degree 2
  over E_R vanishing on the R-points Q₁, Q₂ (C, C′ ⊂ Z), hence ∝ L; index 2 — on the lower hull only when an excess-2
  direction dominates, hence ∝ the char-p W2 coefficient; contributions of B3 never reach the hull at indices 1, 2.
  At Q_i exactly one root has a pole (the last Newton segment, the one containing the constant term), and that root
  is the one joined to C (resp. C′). Every face polynomial containing the constant term has, after x = l·M, the form
  (L/M)·x(s₃x² + s₂x + s₁) + s₀ = 0 (s₀ ≠ 0), i.e. the fibre product of φ = L/M: E → P¹ (degree 2, branch values
  ≠ 0, ∞) and g(x) = −s₀/(x(s₃x² + s₂x + s₁)). It is irreducible over k̄ (third audit: degrees 1 and 2 separated):
  · deg g = 3 (s₃ ≠ 0): k̄(x)/k̄(t) has odd degree 3, so it contains no quadratic subextension, and the double cover
    φ does not split over it.
  · deg g = 2 (s₃ = 0, s₂ ≠ 0): g = −s₀/(x(s₂x + s₁)) has a double zero at x = ∞, so 0 is a branch value of g. It is
    not a branch value of φ, so the two double covers are not isomorphic and the fibre product is irreducible.
  · deg g = 1 (s₃ = s₂ = 0, s₁ ≠ 0): g is an automorphism of P¹, and the fibre product is isomorphic to E itself.
  For 28246 there is no l¹ term (W = W2, so GA = 0), so only deg g ∈ {2, 3} occurs there. deg g = 1 can occur only for
  28244, which the μ filter also excludes independently (μ = 16, App. J).
  Since the coefficients are units on E°, the Newton factorisation holds on the whole E°-tube, and an irreducible
  reduction gives a connected cover.
  *Data check* (`e3h/shapes.py` → `e3h/shapes.out`; all 16 `h_*.out`, i.e. the 4 configurations of 28244 and the 4
  computed members of 28246; the other 4 members of 28246 are the same M_0 by ideal equality, `e3h/id/`). Over GF(p),
  on the conic E, with L the line through the two connector points:
  · BE = L·M·c, AA = κ₁·L·M²·c (κ₁ ≠ 0), and GA = κ₂·L·c (28244) or GA = 0 (28246);
  · Q₁ ≠ Q₂; the two zeros of M on E are distinct; L and M have no common zero on E (so φ = L/M has degree 2 and
    branch values ≠ 0, ∞);
  · the zeros of c lie in {L = 0} ∪ {M = 0}, i.e. at crossings, outside E°.
  All 16: OK. For 28246: L = u₁, M = u₇, E: u₁² + u₄² = u₇², c ∝ u₁ (3 members) or c constant (1 member).
  *Which c (fourth audit).* The linear systems are given as forms vanishing on a fixed curve D = Σ D_j (each D_j a
  known curve, multiplicity 1; `DL` in the scripts). The data c, AA, BE, GA are coefficients of these **forms**, so
  they contain the trace of D on E. Hypothesis (iii) of C.4 concerns the **moving part** (the member of |x| on S̃),
  whose coefficients are c′ = c / t_D, a′ = AA / t_D, … with t_D the local equation of the trace of D on E.
  Check (`e3h/tr/t_*.sing` → `t_*.out`, all 16): the zero scheme of c on E equals the trace of D on E
  (`TRACEMATCH 1` in all 16, by equality of the saturated ideals). In the 3 members of 28246 with c ∝ u₁, the two
  D-curves through the node meet E exactly at Q₁ = (u₁ = 0, u₄ = −u₇) and Q₂ = (u₁ = 0, u₄ = u₇). (These are the
  connector components C₃, C₄; they are D-curves with excess 1, `COMP 3 2 1 1`, so they have moving multiplicity 1.)
  So c′ is a nonzero constant on all of E, including Q₁ and Q₂. Hypothesis (iii) holds for the moving part. In the
  other files c is constant (no D-curve through the node) or vanishes exactly on the D-trace (28244 E19: 4 D-curves,
  c ∝ L M; E21: 2 D-curves, c ∝ L). The ratios ā/c̄, β̄′/c̄, γ̄/c̄ are unchanged by removing t_D, so the normal form
  and the fibre-product argument apply verbatim to the moving part. The W-part of the moving part is
  w′ = w / t_D. Since w vanishes on each D-curve of Z to order DM + 1 (x-sense, `gpow(QL, DM + 1)`), w′ still
  vanishes to the order required in (ii). Hence both connector edges lie on one component and
  the hub contributes ≥ −1 (`e3h/final.py`: all 24 members ≥ 2, the certified hubs are exactly the e = 3 hubs
  occurring in their low directions; same-member groups verified by equality of component ideals, `e3h/id/`).
- e = 3 node P (type (2,2,1,1)) in the bad direction: at a crossing of a multiplicity-1 component of Z with the e = 3
  curve E, with B* = y·w^k·unit (k = excess), the tube is an annulus (critical regime) or a sphere with 3 or 4 holes
  (degenerate regimes) joining the pieces of different scales (Appendix F). *Not used by the analyzer v4
  certificate:* this item rests on Appendix F, which is a consistency check only. In analyzer v4 such a crossing
  is never certified by the regime analysis of Appendix F. The Z-component is bad in this direction, so
  `ok_edge_dir` is False. The crossing therefore enters the bound in only two ways: by the REFINE rule (both
  multiplicities 1; B_lead vanishes on Z only, so b = μ ≠ 0), or as a connector edge of a hub (items (a) and (c)
  above).

## Appendix D. The analyzer (`gph2/analyze.py` → `m16/an2.py`, `m16/web.py`)

Input per member M_p: components (minAssGTZ of the member off D, plus D-curves with excess multiplicity, plus E's with
e = ord_P(member) − ord_P(generic) > 0), multiplicities, pairwise crossings, generic orders at nodes (min over the basis,
D1), and the restriction of the system to each locus.
- **Sheets** = components with x·Γ > 0; **specials** = connected x-trivial configurations Z (the restriction of the
  system to Z is constant, so Z is bad for exactly one direction: the one in which the moving member vanishes on Z).
- **Bad directions** of each locus by linear algebra: members vanishing on Z in the x-sense (G^{(DM+1)} for D-curves,
  saturated ideals); node incidences BADN: B|_C vanishing at P beyond the generic order
  (G^{(DM+1)} + G^{(DM)}·m_P^k, saturated). Pencils: the direction is fixed; nets: points of P¹; webs: points / lines
  of P² — tested: a generic point, every bad point (isolated or on a bad line), a generic point of each bad line,
  and every intersection of two bad lines (item 2 below).
- **Bound (current rules, analyzer v4; the only rules used for any closure).** For each tested direction,
  g(C_0) ≥ k + Σ_v w(v) + #certified annuli, where:
  · k = number of connected components of the certified subgraph (model graph: one vertex per piece / hub);
  · w(v) = ½(Riemann–Hurwitz sum) for a cyclic-cover piece (App. B, A3.1–A3.2; zeros of B|_Γ on multiple sheets
    placed worst-case, collisions included), and g − 1 for a multiplicity-1 piece;
  · a hub H of multiplicity m with h certified connector edges: w = −min(m, h) if g(H) = 0, w ≥ 0 if g(H) ≥ 1
    (App. C.4(a)); w = −1 for the certified e = 3 hubs (App. C.4(c));
  · annuli from Appendix C, counted only if both ends are certified; bad tubes and their annuli are dropped.
  `an2.py` flags: `HUB = True`, `HUBRH = 'MINMH'`, `KCOMP = True`, `LOOP = False`, `COLLIDE = True`.
  *History (not used):* v1–v3 had the constant 1 in place of k, a hub weight of −1 for every hub, and the loop lemma
  (v3 = max(old model, hub model)). All three were withdrawn after the independent audit (32R-76). Re-evaluation of all 881 analyzer members
  (`famg/recheck_hub.py`, `e3h/final.py`): with (a)+(b) 857 are ≥ 2 at once, the remaining 24 (28244 ×16, 28246 ×8)
  become ≥ 2 with (c). Minimum 2. The 28255 / 28760 members of App. F and the 28246 member of App. E are among those
  closed this way.
- **Checks:** with every special good the bound equals p_a(x); on the 58 re-closed nets identical to the hand
  analysis; the 92 net members never decrease between versions (62 increase); 28255, 28760 agree with Appendix F.
- **Points raised by the round-2 reading audit (answered 2026-11-04, 32R-75):**
  1. *Bad tubes.* The bound is the subgraph bound of Appendix B (A2, "how it is used"): a bad vertex is set to None
     and an annulus is counted only if **both** ends are certified vertices (`an2.py`: `if vert[u] and vert[w] and
     ok_edge_dir(...)`); only the hub's edges to certified multiplicity-1 neighbours are counted (at most one per
     neighbour incidence). The hub weight is that of the "Bound" item above. *(The round-2 answer — hub weight −1
     and a loop-lemma term — described v3 and is superseded.)*
  2. *Web strata.* `web.py` tests: a generic point of P², **every** bad point (isolated, or lying on a bad line), a
     generic point of each bad line, and every intersection of two bad lines. All bad loci are kernels of F_p-linear
     maps (BADC / BADE / BADN / BADX are linear conditions on the net), hence F_p-rational linear subspaces, and their
     intersections are F_p-points; no bad stratum is defined only over an extension field. Nets (P¹): every bad point +
     a generic point.
  3. *Zero collisions on multiple sheets (good strata).* The worst case over the zeros of B|_Γ on a multiple sheet
     enumerated distributions over the incidence points but treated the remaining ("free") zeros as distinct simple
     zeros, so collisions of free zeros were not covered. Fixed (`COLLIDE = True`: all partitions of the free zeros).
     Re-evaluation of every member closed by the analyzer (965 members: m16 nets/pencils/webs, m16u, m2c, famc, famd,
     famg, gph): **no bound changed**, none below 2.
  4. *The lift M_0.* The analyzer is used only for members all of whose components are known curves (or E's), so
     that M_0 lifts componentwise over R. Components of the analyzed members: conics (6559 occurrences; all conics are
     known) and degree-4 genus-1 curves (211 occurrences in 190 members), **all identified** with known curves by ideal
     equality (`famg/kq/`, 32R-75; 0 unknown).

## Appendix E. 28246 dm_1_0 (net, x² = 4; `c28/`) — consistency check only, not used for any closure

M_0 = 2K30 + 2K29 + K8 + K7 + K31 + K32 + E7 + E8 + E9 + E10 + E13 + E14 + 3E17 + E19 + E21 + E22 + 2E23. x·Γ = 0
except E9, E10, E13, E14 (x·E = 1). x-trivial part: Z1 = K29 ∪ K30 ∪ K7 ∪ K8 ∪ E7 ∪ E8 ∪ E17 ∪ E22 ∪ E23,
Z2 = K31 ∪ K32 ∪ E19 ∪ E21; E9, E14 (E10, E13) join K29 (K30) to K31 (K32).
- Char 0 (`c28/h0c.sing`, exact over Q(ζ8)): net h⁰ = 3; members containing K29, K30 with excess at nodes 7, 8, 22, 23
  (1) and 17 (2): dimension 2, as mod p. So net_R = R·M_0 ⊕ R·B* ⊕ R·B3, C_0 = M_0 + τB* + τ′B3, Z1-bad ⇔ v(τ′) > v(τ),
  r = v(τ′)/v(τ) > 1.
- Decomposition: Y1 = sp⁻¹(Z1), Y2 = sp⁻¹(Z2), 4 edges sp⁻¹(E_i°). g(C_0) = g(Y1) + g(Y2) + 5 − c1 − c2.
- Y2: M_p reduced along Z2, B* a nonzero constant on K31, K32, E19, E21 ⇒ 8 annuli, cycle K31–E19–K32–E21: c2 = 1,
  g(Y2) = 1. So g(C_0) ≥ g(Y1) + 1.
- Y1 contains the E17 piece (e = 3, B* excess 2, B3(P17) ≠ 0). Newton polygon of a w³ + τβ₂w² + τ′c₃: r < 3:
  ā v³ + c̄ = 0, genus 2; r > 3: β̄₂ v² + c̄ = 0, genus 1; r = 3: singular only for ν = ±1402 (discriminant
  n⁴ − 3840 n²), genus 1 there, 2 otherwise. So g(Y1) ≥ 1, g(C_0) ≥ 2. Other directions: the E17 piece is the good
  triple cover (genus 2).

## Appendix F. e = 3 nodes in the bad direction: 28255 and 28760 (`c55/gen.py`) — consistency check only, not used for any closure

Tool: W = members vanishing on Z (x-sense), W2 = W with excess 2 at P; B* ∈ W \ ⟨M⟩; chart P + λu; limit curves of
F_M + τB* + τ′B3 in the regimes of r = v(τ′)/v(τ); rulings of the tangent cone (fixed D-curves through P) discarded;
genus of the genuine piece; discriminant of the critical regime and genus (or singular-point count over F_p²) of its
special fibres. Bound: g(C_0) ≥ (analyzer value in that direction) + g(Y_Z), g(Y_Z) ≥ g(E-piece) + loops.
- **28255** (Zb = {K5², K6², G31, G32, E19, E21 (e = 3), E27..E30}; analyzer 0 in the bad direction): W = W2 (dim 2
  incl. M) mod p and exactly over Q(ζ8) (`c55/h0c.sing`: net 3, W 2, W2 2), so B*_0 has excess 2 at E21. β₂ = B*|_E21
  has four simple zeros. r < 3: v³a + c, genus 2; r = 3: genus 2 except ν = ±1021 (discriminant n⁴ − 1505 n²) genus 1,
  plus the loop E21-piece – G31 – E19 – G32 ⇒ g(Y) ≥ 2; r > 3: double cover of genus 1 + two loops ⇒ g(Y) ≥ 3.
  g(C_0) ≥ 2 in every regime.
- **28760** (Z1 = {K1², K3, E13, E16, E32 (e = 3), E46}; analyzer 1): W dim 2, W2 dim 1, B* excess exactly 1 at E32
  (excess cannot drop under reduction). a w³ + τγw + τ′c, critical r = 3/2. r < 3/2: genus 2; r = 3/2: a v³ + γv + ν,
  generic genus 2, special ν (discriminant n⁶ + 3210 n⁴ − 2687 n²; ν² = 4981 or 1818, over F_p²): one new ordinary
  node, singularities at infinity unchanged ⇒ genus ≥ 1; r > 3/2: connected genus-0 double cover with two points over
  ξ_K3, both joined to the 4-holed local piece ⇒ a loop. g(C_0) ≥ 1 + 1 = 2 in every regime.

## Appendix G. One-parameter families: procedure (`fam/`, `famc/`, `famd/`)

Family = pencil P ⊂ |x| with M_s = Fix + Y_s. Lemma G needs Σ g(components of Y_s) ≥ 2 (or the analyzer on M_s).
1. **Representation 1** (P in |x|, base locus D ∪ Fix): critical scheme off base locus and nodes (`famc/c_*`).
2. **Representation 2**: Y_s ∈ |y|, y = x − Fix, with a decomposition D2 of m·K − y (MILP, `famd/milp.py`) sharing no
   curve with D ∪ Fix (all 17 at m = 2, h⁰ = 2); critical scheme again (`famd/r_*`). Points hidden in both
   ((D ∪ Fix curves) ∩ (D2 curves) off the nodes, 146 pairs): members with Y_s singular there solved directly
   (`famd/h_*`).
3. **Nodes:** blow-up charts (6 per node), critical points of the strict-transform pencil on E_P, and members
   containing E_P beyond the generic order (`famd/n_*`, `n2_*`; members divided by l^{oG} modulo the surface
   equations). Per special fibre the critical length on E_P is compared with g(Y) − 2; fibres above the bound are
   decomposed directly.
4. **Base points:** by intersection numbers. If y² = 0, two members of |y| are disjoint on S̃, so there is no base
   point. y² ≠ 0 only for the eight 27769 families of §4.6 (y² = 2; two simple base points on the E_P, found in
   representation 2, `famd/bq2_*`) and for 28255_0_0 of §4.7 (y² = 2; two simple base points on E_18, local length 1
   in both representations, `famg/nb1_`, `nb2_`); since their total length equals y², these are all, and every
   member is smooth there. (The round-1-revision jobs `famd/b_*` had a script error and produced no data; they are not
   used.)
5. **Extension-field fibres** above the bound: either the genus G of the union of the conjugate Y's over F_p, giving
   Σg ≥ (G + #conj − 1)/#conj per member (§4.6), or
6. **direct check over F_p(α)** (§4.7; `famg/mksx.py`): ring with the parameter α and minimal polynomial h(α);
   Y_α = (S + (F0 − αF1)) saturated by D ∪ Fix and the irrelevant ideal; singular locus by the Jacobian criterion on
   S off the nodes, and on E_P in the blow-up charts (strict transform; chart surface as a local complete intersection).
   Smooth ⇒ Σg ≥ g(Y); singular scheme of length λ ⇒ δ ≤ λ (Tjurina length bounds δ for the double points that can
   occur; multiplicity ≥ 3 forces length ≥ 3, examined separately if it occurs; it did not). E_P-excess cannot occur
   for α ∉ F_p.
Results §4.6: rep-1 specials over F_p 37 + 136 = 173, all closed (Lemma G 121 + 29 found earlier; analyzer 52 + 8); rep-2 specials 166: Σg ≥ 2 for 106,
the 60 with Σg = 0 (unions of known conics) matched by the linear condition "contains these conics" to closed rep-1
members; 27523: critical fibres split over F_p (4 members, closed); 28244_117: G = 9 / 21 ⇒ Σg ≥ 5.
Results §4.7: see §4.7 (695 F_p specials; 155 extension-field factors: 139 smooth, 16 with δ ≤ 2).

## Appendix H. Implementation errors found in the revision (all fixed, results re-checked)
- an integer `b1` shadowing a ring variable (first `m16u` run; redone);
- unsaturated QL + m_P^k in a membership test, and D-curves treated as ordinary curves (BADN; redone);
- polynomial division by l^{oG} in the node charts (wrong for oG ≥ 2; replaced by division modulo the surface
  equations; all 34 node runs redone, no change in the conclusion; the 28244_117 "4 nodes" were artifacts);
- embedded points first read as isolated base points (rechecked in representation 2);
- Singular name clashes (`res`, `sres`) and ring-scope errors (caught by errors, redone).
- `famd/b_*` (representation-2 base points): a generator inserted a line into a statement, no data; replaced by the
  y² argument (App. G 4).
- §4.7: `y2.py` ignored its argument (fixed); e-jobs lost a declaration (`int k`, rerun); the known-curve check
  `famg/kq` first reported 102 "unknown" because of the `b1` shadowing above (rerun with `kill b1`: 0 unknown);
  a union genus G = 11 for 28255 was first misread as "smooth" (it means δ = 2, g = 6; Σg still ≥ 5).

## Appendix I. File index
- Logs: `32R-80` (fifth audit: wording, k, δ ≤ μ); `32R-79` (fourth audit: c of forms vs moving part); `32R-78` (third audit: A3, e = 3 shapes); `32R-77` (M7, App. J–K); `32R-60` (enumeration), `32R-69` (v2 h⁰, pencils), `32R-71/72` (pencils stage 2, nets, D-check),
  `32R-73` (audit result, Lemma G, recomputation), `32R-74` (flags, proofs, closures), `32R-75` (§4.7 families,
  round-2 reading audit).
- Code: `split/` (enumeration), `stoll/fasth0`, `fix0`, `pic0` (h⁰), `cg*`, `cgk`, `cgq*`, `cgp*` (Lemma G and
  remainders), `cnc`, `czr` (pencil NC), `cbd*`, `c28`, `c55`, `gph*`, `m2*`, `m16*` (pieces / analyzer), `fam*`
  (families; `famg/` for §4.7, direct check `famg/mksx.py`, `sx*_`), `a5`, `d1`, `c3` (flags).

## Appendix J. The μ filter (M7; route-E E05.1, proved here)
Notation: S̃ the minimal resolution of S, E_p (p = 1..48) the exceptional curves (E_p² = −2, H·E_p = 0); for a
class x, d = H·x and μ(x) = Σ_p x·E_p. For an integral curve C̃ ⊂ S̃ other than an E_p, r = number of branches of C̃
with odd contact with some E_p (as in route-E E02/E03), M = Σ_p C̃·E_p.

**Cited (32-03, GitHub `stages/stage32/32-03-multibranch/MB104/route-E/`; status from its STATE.json):**
- E02 (B1): r is even. [executing audit PASS]
- E03: for an integral curve C̄ ⊂ B (non-exceptional on S, d ≥ 1) of geometric genus g ≤ 1: r ≥ d − 4g + 4.
  [round 1 PASS; round 2 FAIL on one must-fix, the missing hypothesis "C̄ ⊂ B, d ≥ 1" (E_p are counterexamples to
  the old wording); fixed in revision 2; the re-audit of revision 2 is pending on the route-E side, so the part used
  here is reproduced with its proof in **Appendix K**]
- E04: equality r = d − 4g + 4 holds only for 80 curves, all of degree 2 or 4. [executing audit PASS]

**Corollary J.1.** Let x be a class with d = 16 and μ(x) < 18. Then |x| has no integral member of geometric genus ≤ 1.

*Proof.* Let C_0 ∈ |x| be integral with g ≤ 1, C̃ its strict transform (class x). C̃ is not an E_p, since
d = 16 ≥ 1, so E03 applies; since d ∉ {2, 4}, C̃ is not one of the 80 curves of E04, so r ≥ d − 4g + 5; r is even
and d is even, so r ≥ d − 4g + 6 ≥ 18 (g = 1) or ≥ 22 (g = 0). Each odd-contact branch meets some E_p with local
intersection ≥ 1, and C̃·E_p ≥ 0 for all p (C̃ ≠ E_p), so r ≤ M = Σ_p C̃·E_p = Σ_p x·E_p = μ(x). Hence μ ≥ 18. □

**Application** (`stoll/mu_nets.py` → `mu_nets.out`, exact integer arithmetic on the lattice Gn; the 48 E_p are
identified as the classes of square −2 and H-degree 0 among the 140 known curves; checks d = 16, C² and
x·E_p ≥ 0; prints PASS). The 23 nets / webs of §4.4 (`n16/plan.json`):

| μ | reps |
|---|---|
| 16 (excluded by J.1) | 9379, 25329, 27523, 27685, 27769, 27986, 28244, 28386, 28525, 28760, 28997, 46958, 58647 (13) |
| 18 | 27882, 28255, 28261 (g = 0 also excluded by J.1's argument: μ < 22) |
| 20 | 27740, 27771, 27940, 27988, 28246, 28445, 34761 (g = 0 excluded) |

The 10 reps with μ = 18, 20 are closed without the μ filter (§4.4). Some members of μ = 16 reps were also run
through the analyzer (App. D: 27769, 27986, 28244, 28386, 28760) and are all ≥ 2 there, but these runs are not
claimed to cover every direction of those nets; M7 rests on J.1.

## Appendix K. Route-E E03 (1) for the μ filter — full proof, for re-audit together with this package
Route-E E03 revision 2 (GitHub `stages/stage32/32-03-multibranch/MB104/route-E/E03-*.md`) is in state "audit FAIL
fixed, re-audit pending". Corollary J.1 uses only E03 (1) (d = 16 ≤ 85, so E03 (2), (3) are not used; the equality
case is E04). This appendix reproduces E03 (1) with its proof, so that **auditing Appendices J–K re-audits the part of
E03 revision 2 used here**. The proof is E02 §2–§3 (route E, executing audit PASS) applied to an arbitrary class.

**Input facts** (Freitag–Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J.
65 (2016), arXiv:1303.6495):
- (F1) B ⊂ P⁶ is (C8 × C8)/G, C8 = X(8) (compact, genus 5), G ≅ (Z/2)³ acting diagonally; its 48 nodes are A1.
- (F2) An index-2 subgroup G0 ⊂ G acts freely on C8 × C8; X := (C8 × C8)/G0 is smooth, π: P := C8 × C8 → X is
  finite étale of degree 4, and q: X → B is a double cover unramified outside the 48 nodes, locally C² → C²/±1.
- (F3) B is a complete intersection of four quadrics, K_B = O_B(1); S → B is crepant with (−2)-curves E_p,
  K_S = H, H·E_p = 0.

**Standing hypothesis** (the revision-2 fix). C̃ ⊂ S is integral and **not** an E_p; equivalently C̄ ⊂ B is an
integral curve, and d := H·C̃ = K_B·C̄ ≥ 1. (For C̃ = E_p, which has d = 0, μ = −2 and genus 0, the inequality is
false. That was the round-2 must-fix.) Ē is the normalization of C̃, g = g(Ē); r = number of points x ∈ Ē over ∪E_p
with odd local intersection m_x of the germ with E_p.

**Lemma K (= E03 (1)).** Under the standing hypothesis, if g ≤ 1, then r > 0, r is even, and r ≥ d − 4g + 4.

*Proof.*
1. *Double cover.* Blowing up the node of C² → C²/±1 gives tot O(−1) → tot O(−2), fibrewise w ↦ w², so the
   resolved cover X̃ → S is a double cover branched exactly along ∪E_p. Since C̃ ⊄ ∪E_p (standing hypothesis), the
   pullback to Ē is generically w² = (unit); at x over E_p it is w² = τ^{m_x}·(unit), ramified iff m_x is odd.
   Let Y be the normalization of Ē ×_S X̃; Y → Ē is branched exactly at the r points.
2. *r > 0.* If r = 0, every component of Y is étale over Ē, so has genus ≤ 1, and so does every component Z of its
   pullback along the étale π. But Z ⊂ C8 × C8 has a nonconstant projection to C8, so g(Z) ≥ 5. Contradiction.
3. *Parity and Riemann–Hurwitz.* Y is a connected double cover branched at r points: r is even and
   2h − 2 = 2(2g − 2) + r, h = g(Y).
4. *Degree.* q is quasi-étale, so K_X = q*K_B; Y maps birationally onto q⁻¹(C̄) and q_*[Y] = 2[C̄], so
   K_X·Y = 2d. Let Z be a component of the normalized pullback of Y to P, e = deg(Z → Y) (étale). Then
   2g(Z) − 2 = e(2h − 2) and K_P·Z = 2ed. With K_P = pr₁*K_{C8} + pr₂*K_{C8} and n_i = deg(pr_i|Z),
   K_P·Z = 8(n₁ + n₂), and Riemann–Hurwitz gives 8n_i ≤ 2g(Z) − 2 for a nonconstant projection (0 for a constant one).
   So 2ed ≤ 2e(2h − 2), i.e. d ≤ 2h − 2 = 4g − 4 + r. □

Nothing in 1–4 depends on the class of C̃; the only hypothesis on C̃ is the standing one, used in step 1
(C̃ ⊄ branch locus) and to have d ≥ 1.

**Cited without reproduction:** E04 (equality face r = d − 4g + 4 ⇒ one of 80 curves of degree 2 or 4; executing
audit PASS; it uses E01′ and E02 §2 (E), (S)). For d = 16 only its degree statement is used.

**Status consequence.** If Appendices J–K pass in this audit, M7 is closed, and the result can be recorded on the
route-E side as a re-audit of E03 revision 2, part (1) (STATE change on GitHub: user's decision).
