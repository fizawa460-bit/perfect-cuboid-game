# E16 (draft) — The singularity budget of the image curve: what is forced, why it is not enough, and the target inequality

Status: **draft research note, zero credit; reading audit PASS (Claude, 2026-11-12, `AUDIT-CLAUDE-E16-20261112.md`).** Written 2026-11-12 on main `0b49f73f`. Not registered in
`STATE.json`. Characteristic 0 only; no mod-p input. Nothing is said about existence or non-existence of perfect
cuboids. Script: `e16/sing_budget.py` (§5).

Labels: **[proved]**, **[outline]**, **[computed]**, **[open]**.

- **Result in one line: no degree bound.** The singular points of the image curve W that the parity conditions force
  account for about one sixth of the budget (a − 1)(b − 1) in the balanced case, and the resulting inequality
  (Lemma S) is *implied* by E15 Lemma K together with the fibre bound. It gives nothing new for large degree.
- The count is not new in substance: it is E09 §2 item 2 / E10 §3–§4 read on P¹×P¹ instead of on B (§1, §3).
- §4 states the inequalities that would win, and candidate theorems.

Notation as in E10–E15. Φ = (p₁, p₂) : V₀ = P¹ → P¹×P¹ birational onto W; deg p₁ = a, deg p₂ = b. For a point P,
**m_P := Σ_{v : Φ(v) = P} min(e_v(p₁), e_v(p₂))** (the multiplicity of W at P), δ_P its δ-invariant.
The 12 *matched points* are (β, β′) with β, β′ in the same B_χ. **M := Σ_{P matched} m_P ≥ j.**
δ_cov denotes deg(E → V₀) (called δ in E10), to keep δ_P for δ-invariants.

## 1. Task 1 — was the singularity count used before? Yes, on B; not on P¹×P¹

- **E09 §2 item 2** [audited]: "Hodge index on B only gives C̄² ≤ d²/16, hence ν ≤ δ_int ≤ about d²/32 + d/2. This is
  three times too weak." The criterion there needs ν < d²/96 (case β ≈ d). E09 §3 names the next step: "compute ν,
  or at least δ_int, from the co-image structure".
- **E10 §3** [audited] computes C̄² exactly (for δ_cov = 8: C̄² = 16ab) and **E10 §4** concludes: "E09, with the bound
  ν ≤ δ_int, cannot close the δ = 8, γ = 0 near-balanced family", adding that E09 "could still bite if one proved
  that most singular points of these curves have multiplicity ≥ 4 … Nothing here proves or refutes that."
- **E12 §3** uses p_a only for γ = 1 at bidegrees (2, 2), (2, 3). **E15 §1, last remark** [outline there]: translates
  of W "give a quadratic inequality that is weaker (about (a + s₁)² ≤ 6ab under equidistribution; not checked in
  detail)".
- Not done before: the count directly on W ⊂ P¹×P¹ with Σδ_P = (a − 1)(b − 1), and the question whether the odd-point
  conditions force singular points. That is §2. The relation to E09/E10 is a dictionary (§3): for δ_cov = 8,
  C̄ is the pullback of W, and adjunction on B with C̄² = 16ab is the same statement as p_a(W) = (a − 1)(b − 1).

## 2. Task 2 — Lemma S: what the parity conditions force

**Lemma S (singularity budget) [proved].** For a birational pair,
1. Σ_P δ_P = (a − 1)(b − 1), and δ_P ≥ m_P(m_P − 1)/2.
2. Hence Σ_{P matched} m_P(m_P − 1)/2 ≤ (a − 1)(b − 1), and by convexity over the 12 matched points
   **M(M − 12)/24 ≤ (a − 1)(b − 1).**
3. If |Ω| ≤ 4: M ≥ j ≥ 2·max(a + s₁, b + s₂) (E12 Lemma 0), so with N := max(a + s₁, b + s₂):
   **N(N − 6)/6 ≤ (a − 1)(b − 1).**

*Proof.* (1) W has bidegree (a, b) up to order, so p_a(W) = (a − 1)(b − 1) by adjunction on P¹×P¹, and its
normalization is P¹; p_a − g = Σδ_P. Φ is the normalization, so the branches of W at P are the points v over P, the
branch at v is parametrized by (u^{e₁}·unit, u^{e₂}·unit) and has multiplicity min(e₁, e₂); a germ of multiplicity m
has δ ≥ m(m − 1)/2. (2) Σ m_P² ≥ M²/12. (3) M ≥ 2N ≥ 6 and M(M − 12)/24 is increasing for M ≥ 6. □

**Proposition S′ (it is implied by known bounds) [proved].** For every pair whose image is not a Klein graph,
M ≤ min(2(a + b), 6a, 6b) (E15 Lemma K; fibres x = β: Σ_{v over β} e_v(p₁) = a). These bounds alone give
M(M − 12)/24 ≤ (a − 1)(b − 1). So **Lemma S (2)–(3) exclude no triple (a, b, M) that Lemma K and the fibre bound
allow.**

*Proof.* Let a ≤ b; the left side increases with M for M ≥ 6 and is negative for M < 12. If b ≥ 2a, use M ≤ 6a:
(3/2)a² − 3a ≤ 2a² − 3a + 1 ≤ (a − 1)(b − 1). If a ≤ b ≤ 2a, use M ≤ 2(a + b):
(a + b)²/6 − (a + b) ≤ ab − (a + b) + 1 because (a + b)² ≤ 6ab for b/a ≤ 2 + √3. □

**Why nothing more is forced [proved for the listed sources; "no other source" is open].**
- Odd points: a point of J is a branch with e₁, e₂ odd through a matched point. That is all the parity conditions
  say; they give M ≥ j and nothing about the distribution over the 12 points or about tangency of branches.
- Even points (e₁ = 2 over B): the parity of h_χ is even there whatever p₂(v) is. No condition, no forced singularity.
  (The branch is smooth and tangent to the fibre x = β.)
- Size: in the balanced slack-0 case j ≈ 2a, forced Σδ_P ≈ a²/6, budget ≈ a². About 5/6 of the singular points of W
  are free. With slack the forced part is ≈ N²/6 against ab, and Lemma K (a + b ≥ N) keeps it below the budget.
- The control pairs (f_n, −f_n) of E15 Proposition C′ have M = 6a and Σ C(m_P, 2) = 60, 1800 against budgets 16,
  576: they violate (1). So Lemma S does see non-birationality there — but only because all 6a fibre points sit at
  matched points, which is the statement "the image is a Klein graph", already in Lemma K.

**Check [computed, exact].** `e16/sing_budget.py`: seven birational pairs (certified birational; degrees up to
(25, 25); m_P up to 6) satisfy (1) at all 36 points of B×B, Lemma K and the fibre bound; the two controls are
detected as non-birational and violate (1). Known answers used: the Möbius pair (x, ix) of E10 §2 (δ = 0); the
degree-5 map f of E15 Lemma M and its iterate; L_n of E14 §6. Ends `PASS`. The check tests the inequality, not its
sharpness: no genuine solution of Problem W of large degree is known to test against.

Verdict for Task 2: **tried; failed.** A lower bound "δ ≥ c·ab" does come out, but with c ≈ 1/6 < 1, and it is not
independent of Lemma K.

## 3. Dictionary with E09 (case δ_cov = 8, all matched branches with e₁ = e₂ = 1) [outline]

The quotient map B → P¹×P¹ has degree 8, branched along the 12 lines x ∈ B, y ∈ B; the 48 nodes of B lie over the 12
matched points, four over each. Then d = 8(a + b) and
- a branch of W through a matched point lifts to two contact-1 branches at each of the 4 nodes: m_p = 2m_P,
  Σ_p m_p = 8M, **σ = Σ_p m_p² = 16·Σ_P m_P²**, β = 8M, λ := β/d = M/(a + b) ≥ 1;
- a singular point of W off the 12 lines gives 8 interior singular points of C̄ of the same type; an even point
  gives 4 ordinary double points; so **ν = 8·δ_off + O(a + b)** when the singular points off the lines are ordinary
  double points (δ_off := Σ δ_P over P off the 12 lines).

E09's criterion (2 − (3/2)λ)² > 32(ν − σ/8)/d² becomes

  **4·δ_off − Σ_{P matched} m_P² < (2 − (3/2)λ)²·(a + b)².**

With Lemma S (1), δ_off ≤ (a − 1)(b − 1) − Σ C(m_P, 2), a sufficient condition is (leading terms)

  **(T1)  3·Σ_{P matched} m_P² > 4ab − (2 − (3/2)λ)²·(a + b)².**

Balanced slack-0 case (a = b, λ = 1): (T1) asks Σ m_P² > a², while equidistribution gives (2a)²/12 = a²/3. This is
E09's "three times too weak", now in the variables of W. For λ ≥ 4/3 (slack ≥ about (a + b)/6) the left side of the
criterion vanishes and (T1) cannot be met at all. *Not checked: the O(a + b) terms and the log-canonical range of α.*

## 4. Task 3 — what would win

Three targets, each sufficient for a degree bound in the stated range. None is proved. [open]

- **(T0) A Klein-type bound with constant below 1:** M ≤ (1 − c)(a + b) + C for birational pairs with |Ω| ≤ 4.
  Then a + b ≤ j ≤ M gives a + b ≤ C/c. Lemma K has constant 2. (T0) is **not to be expected without the leg
  conditions** [heuristic]: rational curves of bidegree (a, b) form a family of dimension 2(a + b) − 1 and "one
  branch through a given point" is one condition, so M ≈ 2(a + b) − 1 is expected for arbitrary rational curves.
  So (T0) must use that the points of J are odd points of *both* legs, i.e. the ramification of p₁, p₂ over B.
- **(T1) Concentration** (§3): Σ m_P² > (4/3)ab − (1/3)(2 − (3/2)λ)²(a + b)². Equivalent in content to E09 (R1).
- **(T2) Few cheap singular points off the lines:** δ_off ≤ (a + b)²/16 + (1/4)Σ m_P² − c(a + b)² (the form of (R1)
  on W for λ = 1), or most of them of multiplicity ≥ 4. E10 §4 already asks for this.

Count of conditions [heuristic]: parameters 2(a + b) − 1; conditions j + (2a − 2 − s₁) + (2b − 2 − s₂) (matched odd
points, ramification over B) ≥ 2(a + b) + 2a + s₁ − s₂ − 4. The excess grows like a: solutions of large degree are
"unlikely intersections" of codimension ≈ a. This is consistent with E12 Lemma R and proves nothing.

Candidate theorems, with the reason each falls short as it stands:

| candidate | what it would give | gap |
|---|---|---|
| Langer's orbifold BMY (E09) | (T1)/(T2) ⇒ bound | needs (T1); factor 3 short (§3) |
| Truncated second main theorem with moving targets over function fields (Yamanoi, Acta Math. 2004), with targets y = β′ (6) and the four Klein graphs | each point of J counted once instead of three times: 2j ≤ (6 + 2ε)a + s₂ + C_ε·a | [outline; statement quoted from memory] needs j > 3a to contradict, but j ≈ 2a in the balanced case: short by the ramification term 2a even with C_ε = 0. No further label-preserving target curves exist (only K) |
| gcd bounds in function fields (Corvaja–Zannier, 2008) | sublinear bound for Σ_v min(ord_v(u − 1), ord_v(w − 1)), u, w multiplicatively independent S-units | p_i − β are S-units only for S ⊃ p_i⁻¹(B), with |S| ≈ 4a; the bound (deg·deg·χ)^{1/3} is then linear in a |
| Hwang–To multiplicity inequalities; Bakker–Tsimerman | m_p ≤ const·d from the injectivity radius | linear (Seshadri-type), like Lemma K; B–T use a level tower, absent here |
| Miyaoka 2008 on S; Bogomolov | only δ_S ≥ d²/224 − d; c₁² < c₂ on S | recorded in E09 §2, E12 §5 |
| Rigidity of hyperbolic correspondences (Mochizuki) | finiteness when both legs are orbifold-étale for the *same* orbifold | applies only to O₁ = O₂ at slack (0, 0), closed in E13 |

**Where it is stuck.** Every count in §2–§4 is a count of incidences with fixed curves or of singular points, and
each is quadratic or linear on both sides with the constant on the wrong side by a factor between 1.5 and 6. No
argument here changes a constant. **Stuck; no further reformulation is proposed.**

## 5. Reproduction and audit points

```
python -I stages/stage32/32-03-multibranch/MB104/route-E/e16/sing_budget.py
```
(exact, about 4 s, output stored as `e16/sing_budget.out`, ends `PASS`).

Audit points: (i) Lemma S (1): the multiplicity of the branch at v is min(e₁, e₂) (primitive parametrization because
Φ is birational); (ii) Proposition S′: the two case estimates; (iii) §3 is an outline: the lift of a branch at a
node, ν versus δ_off, and the lower-order terms; (iv) §4: the Yamanoi and Corvaja–Zannier statements are quoted
from memory and must be checked against the papers before any use; (v) script: the birationality certificate (one
fibre of Φ is a single point) and the treatment of v = ∞.

## 6. Audit history
- 2026-11-12, reading audit by Claude (not the author session) on main `0b49f73f` + this note: **PASS**, no must-fix;
  script rerun, `PASS`; the quotations of E09 §2 and E10 §4 in §1 were checked against the files. One should-fix
  applied: the monotonicity step in Lemma S (3). Details: `AUDIT-CLAUDE-E16-20261112.md`.
