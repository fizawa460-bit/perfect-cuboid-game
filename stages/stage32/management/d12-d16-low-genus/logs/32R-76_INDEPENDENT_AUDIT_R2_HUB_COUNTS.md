# 32R-76 — Independent audit of R2 (HOLD): hub lemma, counts, scope

Date: 2026-11-05. Status: research log, local only (no ledger / STATE / credit / audit-master change).
Audit received: "Stage32 / 32-02 R2 独立監査", PAPER AUDIT HOLD. Items: (1) hub lemma graph argument MUST FIX;
(2) A3 OPEN; (3) M7 OPEN; (4) C5 scope; (5) counts MUST CHECK.

## 1. Hub lemma (MUST FIX) — the audit is right
R2 App. C.4 claimed: modelling sp⁻¹(H°) (H of multiplicity m in a bad configuration) by ONE vertex "lowers b₁".
False: identifying c vertices of a graph that lie in k connected components changes b₁ by +(c − k) ≥ 0, i.e. merging
can only create cycles (audit example H1–X1–Y–X2–H2). The loop lemma (LOOP in an2.py) merges in the same way.

Valid replacement (Riemann–Hurwitz form). For a subgraph Γ′ of certified pieces/annuli:
g(C_0) ≥ Σ_{v∈Γ′} g_v + b₁(Γ′) ≥ 1 + ½ Σ_{v∈Γ′} (2g_v − 2 + n′_v)  (n′_v = edges of Γ′ at v).
Let U = sp⁻¹(H°) ∩ C_0 = U_1 ⊔ … ⊔ U_c, finite flat of degree m over the H°-tube (genus g_H, n holes), tame
(p ∤ m). Glue discs over the end annuli (Kummer z ↦ z^d extends) and apply Riemann–Hurwitz to the complete curves:
Σ_i (2g_i − 2 + n_i) = m(2g_H − 2 + n) + R, R ≥ 0, n_i = ends of U_i, Σ_i n_i = Σ_Q e_Q, e_Q ≤ m.
With h = number of certified ends (connector edges to multiplicity-1 neighbours, one per incidence):
½ Σ_i (2g_i − 2 + n′_i) ≥ ½[m(2g_H − 2 + n) − Σ_Q (e_Q) + h] ≥ m(g_H − 1) + h/2.
So the hub cluster is a vertex of weight m(g_H − 1) (not −1), joined to its h certified edges; no connectivity
pattern is assumed. (A connector component with j ≥ 2 ends on the H-side only increases the bound.)
Implementation: `m16/an2.py` HUBRH = True (hub vertex = (m, g_H)), LOOP = False. Old file `m16/an2_pre_hubfix.py`.

Re-evaluation (`famg/recheck_hub.py` → `famg/recheck_hub.out`; configurations old / safe (no hub, no loop) / new):
- 965 entries = 881 distinct members + 84 duplicates: the m16/m_* outputs of the 84 web reps (27769 ×24,
  27986 ×16, 28244 ×12, 28386 ×32) are in the old net format and are superseded by m16/w_* (web.py). The 32R-75
  statement "965 members re-evaluated" should read 881 distinct members (the collision result is unchanged).
- **72 members fall below 2 under the corrected model** (old ≥ 2):
  m16 nets 28246_29/30/118, 28255_5/6, 28760_3/13/93/102 (9); webs w_27769 ×15, w_28244 ×12 (27);
  famc s_27769_1xx ×16, s_28244_1xx ×12, s_28246_121_8232, s_28255_122_461 (30); famg s1_28246_*_461 ×3,
  s1_28255_0_0_8232 (4); gph g_gn_dm_28246_1_0 (1, = App. E).
  Values (old, safe, new): (3,1,1) ×43, (2,−1,1) ×16, (2,1,1) ×8, (4,0,0) ×4, (3,−3,−1) ×1.
- These are exactly the cases closed in R2 only through the hub/loop model, plus the App. E/F cases (28246, 28255,
  28760) whose explicit multi-scale computations depend on A3.
Status at that point: T7 not certified for these 72.

### 1.1 Repair (same day)
(a) Hub cluster weight −min(m, h) (g_H = 0) / ≥ 0 (g_H ≥ 1): components of U without a certified edge are left out of
the subgraph; each remaining component has genus ≥ g_H. (`an2.py` HUBRH = 'MINMH'.) Alone: still 72 low.
(b) b₁ = E − V + k(Γ′) with k = number of connected components of the certified subgraph (the old formula used k = 1;
the loop lemma had been compensating for that). Splitting a vertex never lowers k. (`an2.py` KCOMP = True.)
With (a)+(b): 24 low (`famg/recheck_hub3.out`): 28244 ×16 (webs w_ ×12 + famc ×4), 28246 ×8 (m16 ×3, famc ×1,
famg ×3, gph ×1). In all 24 the low directions contain an e = 3 hub E with two multiplicity-1 neighbours (in Z);
treating exactly those hubs as one component gives ≥ 2 (`famg/hubwhat.py`).
(c) e = 3 hub lemma (`e3h/`): data mod p (`e3h/gen.py` → `h_*.out`): for all four 28244 configurations (E17, E19,
E21, E22) and both 28246 members: E = conic u1² + u4² = u7² (in its chart), connectors at L = 0 (L = u7 or u1),
multiplicity-2 crossings at M = 0, ā/c̄ ∝ L M², β̄′/c̄ ∝ L M (W2), γ̄/c̄ ∝ L (W \ W2; 0 for 28246, W = W2),
dims W / W2 / W3 = 3 / 2 / 1 (28244), 2 / 2 / 1 (28246). Face polynomials containing the constant term, after x = l·M:
(L/M)·x(s₃x² + s₂x + s₁) + s₀ — fibre product of φ = L/M (degree 2, branch values ≠ 0, ∞) with
g = −s₀/(x(s₃x² + s₂x + s₁)): irreducible (deg g = 3: odd fibre multiplicity; deg g ≤ 2: 0 is a critical value of g but
not a branch value of φ). The pole roots at Q₁, Q₂ (joined to the connectors) are on the last segment, hence on one
component ⇒ hub weight −1. Shapes over R are forced (index 1: vanishing on the R-points Q₁, Q₂; index 2: only the
excess-2 direction reaches the hull) — no char-0 dimension check needed.
Same-member groups by equality of component ideals (`e3h/id/`): famc s_28244_{3733, 2537, 4491, 7779} = w_28244_{3,
118, 123, 27}; famc s_28246_121_8232, famg s1_28246_{0_1, 2_1}_461 = m_28246_{29, 30, 118}; gph dm_28246_1_0 =
famg s1_28246_1_0_461 (computed directly).
Final (`e3h/final.py`): all 24 ≥ 2, certified hubs = exactly the e = 3 hubs in their low directions. **All 881
analyzer members ≥ 2.** App. E / F are no longer needed for any closure (their regime genera agree: {0,3} genus 2,
{0,2} genus 1), so the A3 item for their singular limit curves is moot.

## 2. Counts (MUST CHECK) — all explained, no missing case
- d = 12, C² < 0: 1999 = 1917 (h⁰ = 0) + 82 (h⁰ = 1 under the round-1 v1 ideals) = 1917 + 81 + rep 1215, where
  1215 has h⁰ = 0 under the v2 ideals. Correct split: h⁰_v2 = 0 ×1918 (incl. 1215), h⁰ = 1 ×81.
- d = 14: 1487 = 1320 (h⁰_v2 = 0) + 141 (genus ≥ 3) + 19 (reducible) + 7 (pencils) (`f14v2/f14v2_final.json`).
  The "62 containment" jobs (cg14: c14f ×35, c14v ×27, 62 distinct reps) = the 19 reducible + 18 of the 141
  (1314, 1321, 1322, 1343, 1344, 1346, 1347, 1385, 1386, 1402, 1414, 1460, 1461, 1482, 743, 759, 943, 944)
  + 25 of the 1320 (from the round-1 fullf list: 1011, 1016, 1025, 1104, 1133, 1154, 118, 119, 120, 1236, 1237,
  129, 24, 272, 418, 513, 514, 586, 620, 621, 742, 744, 760, 816, 817) — 43 redundant extra closures.
- d = 16 pencil stage 2: 2746 jobs = 2012 + 164 + 565 + 5 duplicate jobs (32R-69, sx line).

## 3. Scope (C5)
32-02 at d = 16 covers the unibranch-compatible reps only (71,697 of 1,737,363); multibranch is stage 32-03
(open). The R2 title must say so (d = 12, 14: all reps).
