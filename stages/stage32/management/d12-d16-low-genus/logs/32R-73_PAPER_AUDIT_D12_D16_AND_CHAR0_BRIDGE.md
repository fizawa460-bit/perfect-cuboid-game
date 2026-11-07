# 32R-73 — Paper audit of 32-02 d = 12/14/16 (FAIL) and the char-0 bridge (Lemma G)

Date: 2026-11-03. Status: research log, local only (no ledger / STATE / credit change).

## 0. Audit result (8 audits, integrated by ChatGPT): PAPER AUDIT FAIL

Package: AUDIT-PACKAGE-32-02-D12-D16.md. Verdicts: FAIL ×4, HOLD ×4, PASS ×0.
Accepted must-fix items:

| # | item | status after this log |
|---|---|---|
| M1 | T4: "reducible / non-reduced mod p ⇒ not integral in char 0" is false (XY − pZ²) | replaced by Lemma G (§1); recomputed (§3) |
| M1' | same direction error in T2 (containment mod p) and fixfilt (fixed component mod p) | T2: Lemma G (§3); fixfilt: closed by exact char-0 h0 (§4, fix0) |
| M2 | char-0 singular point reducing into a removed locus (base points, nodes) | reformulated: purely a char-p statement (§2) |
| M3 | floating-point y-enumeration at d = 14, 16 (C1) | done: exact rerun identical (32R-74 §H) |
| M4 | T1: do symbolic powers / saturations compute |x|? | answered (§5) |
| M5 | d = 12: certified run vs split enumeration orbit correspondence | answered (§6) |
| M6 | d = 12 reps 1215, 2020 | answered (§6) |
| M7 | 13 nets via μ-filter depend on E03/E04 (C2) | conditional, unchanged |

## 1. Lemma G (genus under specialization) — replaces T4

**Setting.** R a DVR (localization of the ring of integers of a number field at a prime over p), K = Frac R,
k residue field. X/R projective flat (here the model of S̃ / S). C_K ⊂ X_K a geometrically integral curve,
C its flat closure in X, C_k the special fibre, Z_1, ..., Z_r the reduced irreducible components of C_k ⊗ k̄.

**Lemma G.** g(C_K̄) ≥ Σ_i g(Z_i) (geometric genera).

*Proof.* Let N be the normalization of C_K̄; after a finite extension R ⊂ R', N has a semistable model 𝒩
(stable reduction). Replace 𝒩 by a regular model and blow up closed points of the special fibre until the
rational map 𝒩 ⇢ C ⊗ R' is a morphism φ (resolution of indeterminacy on a regular 2-dimensional scheme). The
blow-ups add only rational components. Then g(N) = Σ_v g(W_v) + b₁(dual graph) ≥ Σ_v g(W_v) over the components
W_v of 𝒩_k. φ is proper and dominant, hence surjective, so every Z_i is the image of some W_{v(i)}, with
v(i) ≠ v(j) for i ≠ j. A dominant map of curves does not raise the geometric genus (Riemann–Hurwitz in the
separable case; purely inseparable maps preserve the genus). Hence g(N) ≥ Σ_i g(Z_i). ∎

**Use.** If C_0 is a hypothetical integral char-0 curve in class x, then red(C_0) := C_k is a member of the
char-p system |x|_p. Old T4 only showed "red(C_0) is not integral", which proves nothing. New T4':
**Σ g(components of red(C_0)) ≥ 2 ⇒ g(C_0) ≥ 2.**
Integral case (r = 1) recovers the old direction "g_p ≤ g_0" used in T3.

Implementation note: components come from minAssGTZ over F_p (or F_p(w)). An F_p-component Q that splits into
k conjugate curves of genus g' over F̄_p has Singular genus(Q) = k·g' − k + 1 ≤ k·g', and we count max(0, genus(Q));
so the computed sum is a lower bound of the true Σ g(Z_i). Components of degree ≤ 2 or p_a ≤ 0 are counted 0.

## 2. Removed loci (M2) is a char-p question

The pencil / net arguments only need: every char-p member M of |x|_p that could be red(C_0) is excluded.
By Lemma G, red(C_0) is either integral with g ≥ g(C_0)... i.e. δ(red C_0) ≥ δ(C_0) ≥ p_a − 1, or
non-integral with Σ g ≤ g(C_0) ≤ 1. Both are statements about char-p members. So the critical-point count,
base-point and node analysis must hold **for all char-p members over F̄_p**; no char-0 point needs to be
followed into the removed loci. Remaining paper check: each base-point / node argument in 32R-60/69/71/72 is a
statement about all char-p members (it is: local intersection number 1 at simple base points is a char-p
computation on the char-p system; node charts are char-p computations).

## 3. Recomputation with Lemma G (2026-11-03)

Script: tail after `minAssGTZ(Bp)`: per 1-dim component degree, p_a, genus(); `GENUS-SUM`.
Dirs: stoll/cg (pencils), stoll/cg1 (d16 h0 = 1 containment), stoll/cg14 (d14 containment).

| group | jobs | Σg ≥ 2 | low (Σg = 1) | not finished |
|---|---|---|---|---|
| d16 pencils, scx (OPEN → reducible/non-reduced) | 565 | 477 | 85 | 3 (28761, minAss heavy) |
| d16 pencils, sx "contains a D-curve" | 164 | 130 | 31 | 3 |
| d16 h0 = 1 containment (T2) | 1365 | 773 | 386 (all known curves → h0 argument) | 206 → all closed (cgq/cgp, §4) |
| d14 containment | 62 (v2 ∪ fullf lists) | 22 (of 33 finished) | 8 (all known → h0 argument) | 3 timeouts + 29 not run → all closed (cgq14/cgp14, §4) |
| d16 nets (r_, rl_, dm/dm_, dm/rd_ reducible verdicts) | 270 | 178 | 92 | 0 |

Net low cases are mostly unions of 4–8 conics (Σg = 0), some conics + an elliptic quartic.
Check (stoll/cgk/k_27940_0_42): the 8 conic components are exactly the known curves 21–30 (ideal equality mod p).
So the low members are reductions of explicit char-0 members M_0 = D + Σ a_i K_i.

The low cases all have the shape *k conics + one elliptic quartic* (k = 4..6), in 27 reps
(24755, 41026, 58648, 38463, 38711, 46960, 68496, 9381, 15031, 17619, 28761, 29236, 38725, 41493, 41506, 46971,
58431, 5867, 68835, 15044, 17633, 47334, 59873, 60412, 67315, 67803, 8214, ...). Lemma G gives only g(C_0) ≥ 1
there (g = 0 is excluded, g = 1 is not). Needs a char-0 argument (§4).

## 4. Still open after this log

- R1: low members (Σg ≤ 1). The components are reductions of known char-0 curves, so M_0 = D + Σ a_i K_i is a
  char-0 member reducing to M_p. Route ("occupied critical points"):
  1. Let Z ⊂ (parameter space × S̃) over R be the critical scheme {(t, P) : member_t singular at P}.
     For a finite R-scheme, length of the generic fibre ≤ length of the special fibre (torsion-free rank).
  2. Singular points of a hypothetical C_0 specialize to singular points of red(C_0) = M_p.
  3. If every singular point of M_p (outside the loci handled by the char-p base/node analysis) is an isolated
     REDUCED point of Z_k, it can receive at most one char-0 critical point, and M_0's own singular point
     (which reduces there: transverse intersections K_i·K_j are counted with the same total in both
     characteristics) already takes it. C_0 ≠ M_0 is a different member, so its singular points have nowhere
     to go: contradiction.
  Pencils: Z is finite; reducedness at an ordinary node of a reduced fibre = Morse point (computable).
  Nets: Z is 1-dimensional; use Z_N = {(q, P_1, ..., P_N)} with N = number of nodes needed, finite; check
  independence of the "singular at P_i" conditions (tangent space rank) at the configuration point.
  Needed per low member: components = known curves (ideal test), M_p reduced, all singular points ordinary
  nodes, local reducedness of Z_k there.
- R1 data (2026-11-03, stoll/cgk, czr, csv):
  - all 216 low members (pencils 116, nets 92, d14 8): every component is a known curve (ideal equality) →
    M_0 exists in char 0. 191 reduced, 25 non-reduced on S (reps d14 760; d16 584, 17633, 38725, 58431,
    28246, 25329, 27771).
  - pencil decompositions of the 33 low reps (p16/c_*.out): 159/165 have a reduced finite critical scheme
    (with multiplicity = distinct); 35 of them also have a critical curve (a fibre with a multiple component);
    6 have non-reduced points (5905_0, 58600_0/4, 69324_1/2, ...) → per-fibre check czr/:
    116/116 low pencil members: FIBRE-CRIT-REDUCED (critical scheme reduced at the low fibre; done 2026-11-03).
    The 9 pencil members that are non-reduced on S still need R1b.
  - nets: the low members (unions of conics) have ALL singular points at S-nodes (csv/: visible 0, on
    D-curves 0). On S̃ (rep 27940 cand. 42): 8 conics with K̃_i² = −4, pairwise disjoint, plus exceptional
    curves e_j = 1 (E109, 110, 115, 116, 118, 120, 121, 123, 135, 136) and e_j = 2 (E139, E140).
    So red(C_0) on S̃ is non-reduced along E139, E140: local δ semicontinuity gives no bound there, and the
    "occupied critical point" route does not apply directly. Needs a separate argument (R1b).
- R1-h0=1 (T2 containment, cg1 low 386; 2026-11-04, cgk/k_c1_*): all components of all 386 low members are
  known curves (308 reduced, 78 non-reduced). For h0_p(x) = 1 this closes the case WITHOUT critical points:
  M_0 := Σ (mult) K_{i,0} is a char-0 member of |x| (class equality in Pic, specialization of Pic is
  injective — flag: needs Pic(S̃_K̄) torsion-free and = the 64-lattice); a hypothetical integral C_0 ≠ M_0 would
  give h0_0(x) ≥ 2 > h0_p(x) = 1, contradicting semicontinuity. Non-reducedness is irrelevant here.
  The same applies to d14 h0 = 1 low members. 206 cg1 timeouts (stoll/cgq, cgp): containment against the 92
  known curves + iterated saturation (no minAssGTZ): 5 "residual not a curve" (member = D-curves only, closed by
  the h0 argument), 201 leave an unknown remainder R (degree 12, p_a(R_red) = 6, F_p-
  irreducible plane projection). genus() on R times out (> 30 min). Instead: Sing(R) ⊆ Sing(member) =
  S + NN0 + 5-minors of Jac(S, NN0); at every such point test the Zariski tangent space of R (len O/(I_R + m²) =
  2·[k(P):k] ⇔ smooth). If R is smooth: Σ g(components) = p_a(R) + r − 1 ≥ 6, so g(C_0) ≥ 6 by Lemma G.
  Result (all 201): 98 R smooth (p_a 5–7). 103 R singular only at S-nodes (1 or 2 rational points); local δ
  via a generic plane projection (fibre over the image point of length 1 = local isomorphism) and deltaLoc:
  every such point has δ = 1 (78 × one point, 24 × two points). One case (28711, embedding dim 3 at the point)
  has fibre length 2; the plane δ = 3 bounds δ_R(P) from above (finite birational map). Then
  Σ g(components of R) = p_a(R) − δ(R) + r − 1 ≥ p_a(R) − δ(R) ≥ 5 in all 201 cases ⇒ g(C_0) ≥ 5 by Lemma G.
  **d16 h0 = 1 containment (1365): all closed** (773 by Lemma G directly, 386 + 5 by the h0 argument, 201 here; correction 2026-11-04: the "1 all-known" was the test job 1275, which is one of the 386).
- R1b local lemma (pencils; paper, 2026-11-04). On the regular model S̃_R, let Γ be a component of M_0 with
  multiplicity 2 (Γ = E_j or a conic), s a local equation of Γ over R. Near Γ the pencil is F_τ = a s² + τ b
  (M_0 = {a s² = 0}, b = the other generator, τ ∈ m_R for members reducing to M_p). Let Q be a singular
  K̄-point of F_τ (τ ≠ 0) specializing to Q̄ ∈ Γ_k, u a coordinate along Γ.
  (i) b(Q̄) ≠ 0: with G = F/b = a' s² + τ, dG = s(s da' + 2a' ds) and s(Q) ≠ 0, so s ∂_s a' + 2a' = 0 and
      ∂_u a' = 0; reducing (p ≠ 2): a'(Q̄) = 0 and ∂_u a'(Q̄) = 0, i.e. (a/b)|_Γ has a multiple zero at Q̄.
  (ii) b(Q̄) = 0, a(Q̄) ≠ 0, b|_Γ simple zero: coordinates (s, v = b): ∂_s F = s(2a + s a_s) forces s = 0, then
      F = τ v = 0 forces v = 0 and ∂_v F = τ ≠ 0: no singular point.
  So if on Γ_k the zeros of a|_Γ and of b|_Γ are simple and disjoint ("clean double component"), no singular
  point of C_0 specializes into Γ. The remaining singular points go to isolated points of Z_k off Γ, where the
  occupied-point argument applies; with all of them occupied by M_0, C_0 is smooth, g(C_0) = p_a(x) ≥ 2.
  For Γ = E_j with x·E_j = 0, b|_E is a nonzero constant (E not a base component), so only (i) matters:
  the residual R = M_p − 2E must meet E in 4 distinct points.
  Nets: the condition must hold for every direction b_λ = b_1 + λ b_2 (λ̄ ∈ P¹(k̄)); for Γ = E the direction with
  b_λ|_E ≡ 0 (member containing E) needs a second-order analysis. Open.
  Data: pencil non-reduced members (584, 17633, 38725, 58431, ...) are double conics on S (RADICAL 10 vs scheme
  12 in csv/); net ones are double E on S̃. Clean-condition check: to compute.
- R1b refined (2026-11-04) — "normal-crossings lemma" (pencils). Let Q̄ ∈ M_p be a point that is not a base
  point, so b(Q̄) ≠ 0 and members near Q̄ are the level sets {A = −τ} of A := F_M / B, a function on the regular
  R-scheme S̃_R near Q̄. Suppose M_p is a normal-crossings divisor at Q̄ whose components are reductions of the
  components of M_0, with multiplicities prime to p. Then over R, A = u^α v^β ε (u, v, ϖ regular parameters,
  ε a unit; β = 0 allowed). A singular K̄-point Q of {A = −τ}, τ ≠ 0, in the residue disc of Q̄ is a critical
  point of A with u(Q) v(Q) ≠ 0; ∂_u A = u^{α−1} v^β (α ε + u ε_u) = 0 needs α ε + u ε_u = 0, but this is a unit
  at Q (α a unit in R, u(Q) ∈ m). Contradiction. So C_0 has no singular point specializing to Q̄.
  Consequence: if M_p is normal crossings (multiplicities prime to p) at every non-base point, and the base points
  are simple (all members smooth there), then C_0 is smooth, g(C_0) = p_a(x) ≥ 2. This replaces both the
  "occupied critical point" step (reduced nodes: A = uv) and the clean-double-component lemma (A = u² ε, A = w²s²).
- Data for the 9 non-reduced pencil members (cdb/, cdn/): off the S-nodes, the double conic Γ meets the rest
  only at simple points (584: 1 point; others: none), b ≠ 0 on Γ off nodes. All of Γ's other contacts are at
  6 S-nodes on Γ, where M̃ has E-coefficient e = ord_P(NN) − c_P ∈ {1, 2} and up to 2 other conics pass
  through. Normal crossings there = distinct tangent directions at P (+ b ≠ 0 at those points of E): needs a
  node-chart computation on S̃ (to do). Rep 584 (cd_) also contains a D-curve with excess multiplicity.
- NC check, all 116 pencil low members (stoll/cnc, 2026-11-04): **116/116 NC-OK**. Checked on S:
  components of M̃ = minAss(Bp) + D-curves with excess multiplicity (cd_ cases); off the S-nodes: pairwise
  intersections reduced (transverse), no triple points, B̃ avoids crossings and multiple components; at each node P
  on M̃: e = ord_P(NN) − ord_P(generic member), x·E = −2e + Σ mult of components through P (never < 0),
  pairwise local length 1 at P (distinct tangent directions ⇒ strict transforms meet E at distinct points),
  and where x·E > 0 the moving member B̃ has local length 1 with every component through P (its point on E is
  not a special point of M̃). Points where M̃ is smooth and reduced need nothing (dF_M(Q̄) ≠ 0 ⇒ F_τ smooth).
  Assumptions to flag: components (known conics / elliptic quartics) are smooth, also at the nodes; "local
  length 1 at an A1 point ⇔ distinct tangent directions" for smooth branches; base points simple (32R-69).
  ⇒ With the NC lemma: all pencil low members are excluded in char 0 (including the 9 non-reduced ones).
- R1b nets (paper sketch + data, 2026-11-04, stoll/cnn).
  Reduction to one pencil: C_0 = F_M + τ_1 B_1 + τ_2 B_2; with τ = the τ_i of least valuation, C_0 lies in the
  R-pencil ⟨F_M, B_λ⟩, B_λ = B_1 + λ B_2 (or λ B_1 + B_2), λ ∈ R; its direction λ̄ ∈ P¹(k̄) is ONE value.
  Local contributions to δ(C_0) (Q̄ a point / E a curve of M̃ on S̃):
  (a) M̃ smooth reduced at Q̄: 0.  (b) M̃ snc at Q̄, b_λ̄(Q̄) ≠ 0: 0 (NC lemma).
  (c) e_E = 1, x·E = 0: b_λ|_E is a constant c(λ); for λ̄ with c(λ̄) ≠ 0, (b) applies; for c(λ̄) = 0 write
      f = μ' + w g (w = local eq of E, μ' ∈ m constant along E, ḡ|_E = residual): critical points need ḡ = ∂_u ḡ = 0
      on E, i.e. a tangency of the residual with E; transverse crossings (local length 1) ⇒ 0.
  (d) e_E = 1, x·E = 1: b_λ̄ has one zero on E; ≤ 1 (δ semicontinuity at a reduced crossing; flag).
  (e) e_E = 2, x·E = 0: f = a w² + τ(μ + w b') near E; away from a = 0: singular points ↔ critical points of
      φ = b'²/a on E ≅ P¹ (degree (x − 2E)·E = 4) with critical value 4μ/τ (≠ 0, since μ = 0 would put E in C_0);
      Riemann–Hurwitz: one fibre carries Σ(e_i − 1) ≤ 3 ⇒ δ ≤ 3. At the poles (a = 0, transverse crossings) with
      b'(Q̄) ≠ 0 a valuation count puts no singular point in the residue disc. (Flag: b' ≠ 0 at the crossing points
      on E, i.e. the net member containing E does not pass through them — to verify.)
  Bound: δ(C_0) ≤ Σ contributions; g(C_0) ≥ p_a(x) − δ.
  Data (92 net low members, all p_a(x) = 11, no off-node crossings by csv/): 75 have only types (c), (d), (e),
  bound ≤ 6, so g(C_0) ≥ 5: **75 closed** (modulo the flags). Remaining 17: 27771 family (12: double conic +
  e = 3 at two nodes), 25329 (2: double conic, base point on it), 28246 (double conic, e = 3), 27988 (double
  conic), 34761 (one off-node triple point). Ideas: local analysis in the
  node charts (x·E139 = x·E140 = 0, so C_0 avoids E139/E140 in char 0); or exact char-0 / p-adic
  computation of the net near q_0 for these ~11 net reps and ~8 pencil reps.
- R2: fixfilt (146 reps, h0 ≥ 2, fixed component mod p): CLOSED 2026-11-04 by exact h0 over Q(ζ8) (see below).
- R3: d16 nets: 45 reducible (dm/rd_), 2Γ-families, 27988 — rerun with the genus-sum tail.
- R4: d = 14, 16 exact (integer) enumeration (M3).

## 5. T1 (M4)

S ⊂ P⁶ is a complete intersection, so H⁰(S, O(m)) = (k[a,b,c]/I_S)_m, and H⁰(S̃, π*O(m)) = H⁰(S, O(m)).
Members of |x| = |π*O(m) − D| ↔ forms F with ord_{Γ̃}(π*F) ≥ c_Γ and ord_{E_j}(π*F) ≥ c_j.
- Curves: ord_{Γ̃} ≥ c is the symbolic power Γ^{(c)} on S. At smooth points of S, Γ is locally principal, so
  I_Γ^c has embedded components only at the nodes; saturating by the node points and the irrelevant ideal gives
  exactly the symbolic power.
- Nodes (A₁): m_P·O_S̃ = O(−E) and m_P^c is integrally closed (rational singularity, Lipman), so
  {ord_E(π*F) ≥ c} = m_P^c; sat(S + m_P^c, irrelevant) is its homogeneous ideal.
- Intersection of the ideals = conjunction of the conditions.

## 6. d = 12 items (M5, M6)

- Enumeration (32R-60 "FINAL CROSS-CHECK"): certified production run complete (no errors), 33,147 classes;
  split set restricted to the production inventory rules: 1,274,512 classes in 519 lattice orbits;
  production ⊆ split (0 missing) and every one of the 519 orbits contains a production class. The full split
  set (1,917,312 classes, 778 lattice orbits, 2,029 geometric reps) is a superset, so it adds candidates only.
- Rep 1215: the package quoted the v1 argument (residual degree 14). Under v2 ideals h0 = 0
  (fasth0/recheck_v2_d12.json: changed [1215, 1 → 0], [41, 1 → 0]); excluded by T1.
- Rep 2020: the two conjugate heavy members (over F_{p²}) form one F_p-component of degree 24 with fast bound 9.
  If it splits into k geometric components (k even, each member holding k/2), the union genus bound gives
  Σ g_i ≥ 9 + k − 1, so each member has Σ g ≥ (8 + k)/2 ≥ 5. By Lemma G, g(C_0) ≥ 5.

### d14 h0 = 1 containment: all 62 closed (2026-11-04, stoll/cgq14, stoll/cgp14)

All 62 d14 containment jobs have h0_p = 1.
- 22: Σg ≥ 2 by Lemma G (cg14).
- 8 low (541, 690, 846, 1011, 1133, 129, 418, 760): all components known curves (cgk) → h0 argument.
- 32 remaining (3 timeouts 1210, v1016, v272 + 29 never run), containment against the 92 known curves (cgq14):
  7 ALLKNOWN (1059, 1274, 1305, 1319, 1320, 1475, 1486) → h0 argument.
  25 leave an unknown remainder R (degree 8 or 12). Tangent-space test on Sing(member) ∩ R (cgp14/s_*):
  7 R smooth (1321, 1322, 1346, 1347, 1482: p_a 3; 1460, 1461: p_a 5) → Σg ≥ 3.
  18 R singular at 1, 2 or 4 rational S-node points; local δ via generic plane projection (cgp14/d_*): every
  point has fibre length 1 and δ = 1. p_a − δ: 6 − 1 = 5 (1210, 1330, v1016, v272), 5 − 2 = 3 (1314, 1343,
  1344, 1348, 1349, 1350, 1385, 1386), 9 − 4 = 5 (1354, 1371, 1402, 1414, 1477, 1478).
  So g(C_0) ≥ 3 in all 25 by Lemma G.
Result: d14 h0 = 1 containment closed (same audit flags as d16: Pic for the h0 argument, δ semicontinuity).

### R1b nets: 16 of the remaining 17 closed by "good-reduction pieces" (2026-11-04, stoll/cbd, cbd2)

Tool (generalised Lemma G; flag: standard stable-reduction fact, cite e.g. Bosch–Lütkebohmert): if X/K is a smooth
projective curve and U_1, ..., U_r ⊂ X^an are pairwise disjoint affinoids whose canonical reductions are irreducible
smooth affine curves with smooth completions of genus h_i, then g(X) ≥ Σ h_i. Lemma G is the case "U_i = tube over
a reduced component of red(C_0)". New pieces come from multiple loci of M̃ (residue char p ≠ 2, 3):
- E with e = 3, x·E = 0, C_0 = F_M + τ B_λ with c_E(λ̄) ≠ 0 (B_λ̄|_E is a nonzero constant): on
  {|a| = 1, |w| = |τ|^{1/3}} the equation f/τ reduces to ā v³ + c̄ = 0, a cyclic triple cover of E ≅ P¹ branched where
  ord(a) ≢ 0 mod 3. With components through E of multiplicities 1, 1, 2, 2 (distinct points, L = 1): genus 2.
- double conic K (mult 2, K̃² = −4, x·K = deg a − 8): on {|a| = 1, |w| = |τ|^{1/2}} the reduction is ā v² + s̄ = 0 with
  s = B_λ̄|_K ∈ H⁰(K, O(x·K)); if s ≢ 0 this is a double cover branched at the odd-order zeros of a·s.
- bad direction of a locus L = the members of net/F_M vanishing on L (or with excess order at the node);
  computed in char p (cbd/b_*: baddir). "NONE" = no direction is bad (restriction net/F_M → H⁰(L) injective).
  (Printed t is −1/kq; the bad member is FL2 + (1/t)·FL3. Only equality/inequality of directions is used.)
Results:
- 27771 family (12: r_27771_{0,1,2}_{60,61}, rd_27771_*): double conics K5, K6 with x·K = 1, a-zeros of orders
  3, 3, 1, 1, 1 (deg 9); both "BAD NONE", so s ≢ 0 for every λ̄; branch points ≥ 4 (6 unless the zero of s hits an
  odd zero of a) ⇒ each gives genus ≥ 1, disjoint ⇒ g(C_0) ≥ 2 for every direction. (Also: the two e = 3 nodes have
  different bad directions, so one of them adds a genus-2 piece: g(C_0) ≥ 4.) **Closed.**
- 25329 (2): double conic K3, x·K3 = 1 (a-zeros 1, 2, 1, 1, 2, 1 at nodes + 1 off-node crossing with comp 4), "BAD
  NONE" ⇒ genus ≥ 1 piece; comp 4 is an elliptic quartic of multiplicity 1 (Lemma-G piece, genus 1) ⇒ g(C_0) ≥ 2.
  The cnn flag "OFFNODE base point on multiple comp" tested only ONE generic member (IB = FL[1]); it is a moving
  point, not a base point of the net. **Closed.**
- 34761 dm_0_4 and 27988 dm_1_2: the members contain excess D-curves (G77, G79 resp. G40, G42 (mult 2)), which are
  elliptic quartics; with them red(M_p) has Σ g = 3 (cbd2: genus() of every component). Lemma G ⇒ g(C_0) ≥ 3.
  (The earlier "low" label used only the residual off D.) **Closed.**
- 28246 dm_1_0: OPEN (only in one direction). Components: double conics K1, K2 (x·K = 0), conics K3..K6; e = 3 at
  node 17 (mults 2, 2, 1, 1 → genus-2 piece when good). All loci (E7, E8, E17, E22, E23, K1, K2) have the SAME bad
  direction; the bad member is B4 = K1 + K2 + K3 + K4 + Y + E7 + E8 + 2E17 + E22 + E23, Y irreducible of degree 8,
  genus 5 (cbd2/z_28246). Off the bad direction: closed (E17 piece, g ≥ 2). In the bad direction, with
  μ_L = constant term along L, the K-pieces have genus 1 if v(μ_K) < 2v(τ) but can degenerate (a v² + β v
  reducible) if v(μ_K) > 2v(τ), i.e. C_0 very close to the char-0 pencil ⟨M_0, B4_0⟩. Needs a two-scale argument
  (or the char-0 position of the bad directions λ_L).
Net tally: 92 low members → 75 + 16 closed, 1 open (28246 dm_1_0, bad direction only) → closed below; all 92 closed.

### R2 fixfilt: closed by exact char-0 h0 (2026-11-04, stoll/fix0)

Problem: fixfilt showed h0_p(D + Γ) = h0_p(D) (Γ fixed mod p); semicontinuity alone does not transfer this to
char 0. Fix: compute both dimensions EXACTLY over Q(ζ8) (Singular ring (0,z), minpoly z^4+1; same component ideals
as fasth0/precompute_v2.sing: curves satur(S + I_Γ), symbolic powers satur(satur(S + I_Γ^c, nodes), m), node
powers satur(S + m_P^c)); h0 = rank of the degree-m part of ∩ components − dim S_m (fix0/mk.py → f_<idx>.sing).
Result (146 reps, 396 fixed-curve checks, total 124 s): h0_0(D) = h0_p(D) in all 146, and h0_0(D + Γ) = h0_0(D) for
every Γ in every fixed list. So Γ is a fixed component of |x| in characteristic 0 as well; |x|_0 has no integral
member other than Γ itself, and no char-0 curve C of class x exists. No Lemma G / reduction argument needed.
(Check of d = 14: fasth0/d14_fix.json has no rep with a fixed curve; nothing to do.)

### 28246 dm_1_0: closed (2026-11-04, stoll/c28)

Components (c28/id.sing): M_0 = 2K30 + 2K29 + K8 + K7 + K31 + K32 + E7 + E8 + E9 + E10 + E13 + E14 + 3E17 + E19 + E21 + E22
+ 2E23 (known-curve labels; K31, K32 are the D-curves with excess 1). x·Γ = 0 for every component except E9, E10, E13,
E14 (x·E = 1). The x-trivial part splits into two connected configurations
  Z1 = K29 ∪ K30 ∪ K7 ∪ K8 ∪ E7 ∪ E8 ∪ E17 ∪ E22 ∪ E23,   Z2 = K31 ∪ K32 ∪ E19 ∪ E21,
and E9, E14 (resp. E10, E13) join K29 (resp. K30) in Z1 to K31 (resp. K32) in Z2. (Geometrically: |x| is a net with
x² = 4; Z1, Z2 are contracted to two points z1 ≠ z2 of P², M = preimage of the line through them.)
Char 0 (c28/h0c.sing, exact over Q(ζ8)): net h0 = 3; members containing K29, K30 and with excess order at nodes 7, 8,
22, 23 (1) and 17 (2): dimension 2 — the same as mod p. So the bad direction of Z1 is a char-0 direction: there is
B*_0 with B*_0 ≡ B4 (mod p), and net_R = R·M_0 ⊕ R·B* ⊕ R·B3. Write C_0 = M_0 + τ B* + τ' B3; Z1-bad ⇔ v(τ') > v(τ);
τ' ≠ 0 since C_0 is integral. Put r = v(τ')/v(τ) > 1.
Decomposition of C_0^an by the specialization map: Y1 = sp⁻¹(Z1), Y2 = sp⁻¹(Z2), and 4 edges sp⁻¹(E_i°) (good
reduction, genus 0, one end in Y1 and one in Y2). Then g(C_0) = g(Y1) + g(Y2) + b1, b1 = 4 − c1 − c2 + 1
(c_i = number of connected components of Y_i; every component has an end since C_0 is connected, so c_i ≤ 4).
- Y2: M_p is reduced along Z2; B4 is a nonzero constant on K31 and on K32 (x·K = 0, K31, K32 not in B4) and on
  E19, E21 (their bad direction −3130 ≠ Z1's). So at all 8 crossing points on K31 ∪ K32 the NC lemma gives open
  annuli (|uv| = |τ|), the pieces K31°, K32°, E19°, E21° have good reduction, and the cycle K31–E19–K32–E21 gives
  c2 = 1, g(Y2) = 1. Hence g(C_0) = g(Y1) + 5 − c1 ≥ g(Y1) + 1.
- Y1 contains the E17 piece (e = 3; B* has excess order 2 at node 17; B3(P17) ≠ 0). Newton polygon of
  a w³ + τ β2 w² + τ' c3 (c28/r3.sing, r3b, r3c; limits computed as λ → 0 in the chart P17 + λu, char p):
  r < 3: ā v³ + c̄ = 0, genus 2.  r > 3 (scale w ~ (τ'/τ)^{1/2}): β̄2 v² + c̄ = 0 on the tangent cone, genus 1
  (elliptic y² = x⁴ − k²).  r = 3: the cone ∩ {u1 u6² + 1081 u1 u6 = 557 ν} — singular only for ν = ±1402
  (discriminant n⁴ − 3840 n², ν = 0 excluded), genus 1 there and 2 otherwise. So g(Y1) ≥ 1 in every regime.
  Therefore g(C_0) ≥ 2 in the Z1-bad direction.
- Any other direction: the E17 piece is the good triple cover (genus 2) ⇒ g(C_0) ≥ 2.
Flags: (i) genus additivity over the sp-decomposition (Berkovich skeleton / stable reduction), (ii) the reduction
of an affinoid piece with singular reduction gives at least the geometric genus of its normalization, (iii) h0 of
the R-lattice = 3 (char 0 = char p, checked). **Closed.** All 92 net low members are now closed.

Audit flags consolidated in 32R-74_AUDIT_FLAGS_D14_D16_CHAR0.md (2026-11-04).

B1 / A5 discharged by computation (2026-11-04, stoll/pic0, stoll/a5): see 32R-74 §G.
C3 check FAILED for the type-(e) bound; the 58 affected nets were re-closed without δ, and R4 (exact enumeration) is done: see 32R-74 §H.

d16 pencil low-check timeouts (6: cd_28169_4_1, cd_28169_4_3, cd_38725_3_0, cg_28761_{0,2,4}_0; stoll/cgp16, 2026-11-04):
containment against the 92 known curves (1–3 conics) leaves a remainder R of degree 10 or 12, p_a(R_red) = 5, and the
tangent-space test finds no singular point (R-SMOOTH); plane-projection δ = 0 as a cross-check. So Σ g ≥ 5 and
g(C_0) ≥ 5 by Lemma G. The "not finished" entries of the §3 table (3 + 3) are closed.
