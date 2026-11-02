# E02 — Check of the F69 receiver premises; the uniform 14-node class has no genus ≤ 1 carrier (2026-11-02)

Status: research note, **unaudited, zero credit**. Round 1 (DeepSeek, reading) gave HOLD at `212bd863`: no must-fix,
five should-fix items. Revision 2 makes the Beauville chain self-contained (§2). It now relies only on the
Freitag–Salvati Manni facts (F1)–(F3), which were read in the primary source, and on Lemma E01′
(`E01-C8-CONGRUENCE-EMPTY-WINDOW.md` §2a).

## 1. Input facts from the primary source

Freitag–Salvati Manni, *Parametrization of the box variety by theta functions*, Michigan Math. J. 65 (2016),
arXiv:1303.6495. Read directly on 2026-11-02.

- **(F1)** The box variety B ⊂ P⁶ is the quotient of X(8) × X(8) by a group G ≅ (Z/2)³ of order 8.
  - Here X(8) = H*/Γ[8] is the compactified modular curve of genus 5.
  - G = Δ(4,8)/(Γ[8]×Γ[8]) acts through the diagonal action of Γ[4] (Introduction; §2, Prop. 2.5).
  - The 48 nodes of B are the images of the points with nontrivial stabilizer. At each of them the local quotient is (C×C)/±1, an A1 node (§2).
- **(F2)** There is an index-2 subgroup G0 = Γ′[4]/Γ[8] ⊂ G acting freely on X(8), hence freely on X(8)×X(8) (§4, Lemma 4.1). The proof of Lemma 4.1 treats every point of the extended upper half plane H* = H ∪ Q ∪ {∞}, cusps included, so the action is free on the *compact* X(8). Then:
  - X := (X(8)×X(8))/G0 is smooth, and P := X(8)×X(8) → X is finite étale Galois of degree 4;
  - q: X → B = X/(G/G0) is the two-fold Galois cover of Beauville. It is unramified outside the 48 nodes and locally C² → C²/±1 at each node (Introduction, §4).
  - §4 also states that "the map X̃ → B̃ is ramified along the exceptional divisors (48 lines)", and that X has the product of two curves of genus > 1 as unramified covering.
- **(F3)** B is a complete intersection of four quadrics in P⁶ (Introduction), so K_B = O_B(1). The resolution S of the 48 nodes is crepant, with exceptional (−2)-curves E_p, K_S = H := pullback of O(1), H² = deg B = 16 and H·E_p = 0.

C8 below means the compact curve X(8). The cusps of the non-compact H/Γ[8] are ordinary points of the compact
Riemann surface X(8). Every map used in E01/E02 — finite étale covers, automorphisms, the product P, the quotients by G0 and G — is a map of compact
curves or surfaces. So E01 may use any uniformization of the compact X(8), in particular the cocompact Γ = PQ¹_B(2).
Nothing below uses Γ[8] or its cusps. (E01 Step 1 identifies the compact genus-5 curve with 192 automorphisms; X(8) is that curve.)

## 2. The Beauville chain, derived here

Let C̄ ⊂ B be an integral curve, Ē its normalization of genus g, and d := K_B·C̄ = deg_{P⁶} C̄ = H·C̃, where C̃ ⊂ S is the strict transform.

**(a) The resolved double cover is branched exactly along the E_p.**

- Locally at a node, X → B is C² → C²/±1.
- Blowing up the origin of C² gives the total space of O(−1) over P¹. The involution −1 acts fibrewise by −1, and the quotient is the total space of O(−2), which is the minimal resolution, with E_p as zero section.
- The quotient map tot O(−1) → tot O(−2) is fibrewise squaring w ↦ w², branched exactly along the zero section.
- So the resolved cover X̃ → S is a double cover branched exactly along ∪E_p, and étale elsewhere.

**(b) The odd-branch rule.**

- Let x ∈ Ē be a normalization point whose image lies on E_p, and let m_x := the local intersection multiplicity of the germ of C̃ at x with E_p. This is the m = min(A, B) of the A1 adapter.
- Near the image point the double cover is w² = f, with f a local equation of E_p. Pulled back to the normalization coordinate τ at x, it becomes w² = τ^{m_x}·(unit).
- Hence the pulled-back double cover is ramified at x iff m_x is odd.

**(B1).**

- Let Y be the normalization of Ē ×_S X̃. Its branch points over Ē are exactly the x with m_x odd. Write r_odd for their number.
- If r_odd > 0, Y is connected (a connected branched double cover).
- Riemann–Hurwitz: 2h − 2 = 2(2g − 2) + r_odd, where h = g(Y).

**(B2).**

- The cover q is quasi-étale: it is unramified in codimension 1. So K_X = q*K_B as Q-Cartier divisors.
- The image of Y in X is q⁻¹(C̄), which is irreducible because Y is connected. It maps birationally from Y, and q_*[Y] = 2[C̄].
- By the projection formula, K_X·Y = K_B·q_*Y = 2d.

**(B4).**

- Let π: P → X be the étale cover from (F2), and let Z be a component of the normalized pullback of Y, with e := deg(Z → Y).
- Since π is étale, Z → Y is étale. Its Galois group is Stab_{G0}(Z), so e = |Stab_{G0}(Z)| ∈ {1, 2, 4}.
- Hence 2g(Z) − 2 = e(2h − 2) and K_P·Z = e·K_X·Y = 2ed, using K_P = π*K_X.
- Write n_i for the degree of the i-th projection Z → C8. Then K_P = pr₁*K_{C8} + pr₂*K_{C8} gives K_P·Z = 8(n₁ + n₂).
- Riemann–Hurwitz for each nonconstant projection gives 8n_i ≤ 2g(Z) − 2. A constant projection contributes 0.
- Hence 2ed ≤ 2(2g(Z) − 2) = 2e(2h − 2), so d ≤ 2h − 2 = 4g − 4 + r_odd. That is, r_odd ≥ d − 4g + 4.

**(E) Equality rigidity.**

- If r_odd = d − 4g + 4, then 2h − 2 = d, so 2g(Z) − 2 = ed, while 8(n₁ + n₂) = K_P·Z = 2ed.
- Each nonconstant projection has 8n_i ≤ 2g(Z) − 2 = ed, and a constant one has n_i = 0. The sum 8(n₁ + n₂) = 2ed is reached only if 8n₁ = 8n₂ = ed. In particular, neither projection is constant: the other would need 8n_j = 2ed > ed.
- So both Riemann–Hurwitz inequalities are equalities: n₁ = n₂ = ed/8 and Ram = 0, i.e. both projections are finite étale.

**(S) Stabilizer.**

- P → B is Galois with group G (F1), and Z is a component of the normalized pullback of Ē. So Z → Ē is the quotient by Stab_G(Z), of degree deg(Z → Y)·deg(Y → Ē) = 2e. Hence |Stab_G(Z)| = 2e.
- Z is the normalization of an integral curve in P. This is the component of the preimage of C̄, which is reduced because P → B is generically étale. So Z is birational onto its image.

## 3. The uniform class

Let D_l = 7l·H − 4l·Σ_{p∈Σ} E_p, with |Σ| = 14 and l ≥ 1, and let C̃ ∈ |D_l| be integral, with g(Ē) ≤ 1.

- d = H·D_l = 7l·16 = 112l, and C̃·E_p = −4l·E_p² = 8l.
- The local multiplicities m_x ≥ 1 over E_p sum to 8l. So the number of normalization points over E_p is ≤ 8l, and r_odd ≤ M ≤ 14·8l = 112l = d.

**Genus 0.** (B4) gives r_odd ≥ d + 4 > d ≥ r_odd. This is impossible.

**Genus 1.**

- (B4) gives r_odd ≥ d. Together with r_odd ≤ d this forces r_odd = d, so every m_x = 1.
- By (E), Z is a minimal étale correspondence with legs of degree n = 14el.
- By (S), Z/Stab_G(Z) = Ē has genus 1, and |Stab_G(Z)| = 2e.
- Lemma E01′ with A = Stab_G(Z) needs n < 16·2e/3, i.e. 14el < 32e/3, i.e. l < 16/21. This contradicts l ≥ 1.
- Equivalently: Area(Ē) = 16πn/(2e) = πd = 112πl > 256π/3.

**Lemma E02.** Assume (F1)–(F3) and Lemma E01′. Then for every l ≥ 1 and every 14-node set Σ, the class
7lH − 4lΣE_p on the resolved box surface contains no integral curve whose normalization has genus ≤ 1. □

## 4. Scope (round-1 should-fix 4 and 5)

- E02 is a statement about the **uniform class 7lH − 4lΣ_{14}E_p only**.
- It does **not** prove that every curve in the current e=2 frontier of STATE lies in this class. The e=2 records in STATE (degrees n = 28l, the factor class A_ref(l) = π_H*O(7l), the support `000707000f0f`) are formulated for carriers in this class. Matching them to E02 is a bookkeeping check for the auditor; E02 itself makes no claim about the frontier beyond the class.
- Untouched: unequal Picard coefficients, other node counts, P6 sectors, and the relation to route A's 864 supports.
- No credit, frontier change or MB104 closure is claimed.
- `e02_counts.py` is an arithmetic consistency check only: d = 112l, C̃·E_p = 8l, M ≤ d, n = 14el, area = 112πl versus 256π/3, and 1/7 < 3/16, for l = 1..1000 and e ∈ {1, 2, 4}. It does not verify any geometry. The geometry is §1–§3.

## 5. Remaining audit points

1. Statements (F1)–(F3) as read in FSM. Freeness of G0 on the compact X(8) is FSM Lemma 4.1, whose proof covers cusps; re-check it.
2. The local model in §2(a)–(b): crepant A1 resolution and the double cover branched along the zero section.
3. Quasi-étaleness, K_X = q*K_B, and the identity of Y's image with q⁻¹(C̄) in (B2).
4. Lemma E01′ (E01 §2a).

## 6. Audit history

- **Round 1: DeepSeek (reading), HOLD at `212bd863`. No must-fix.** Should-fix items and their responses:
  1. Beauville framework unaudited → re-derived in §2 from (F1)–(F3).
  2. Extension of E01 from h ∈ {4,8} to h = 2e → proved as Lemma E01′ (E01 §2a).
  3. FSM non-compact Γ[8] versus compact X(8) → addressed in §1, including FSM Lemma 4.1 (freeness on H*).
  4. "covers the whole current e=2 frontier" → removed; scope in §4.
  5. The script's role → stated in §4.
- Revision 1 relied on the predecessor-archive Beauville notes (blobs `1afa8398`, `a2054708`, `cb05a7a1`) and on the A1 adapter (blob `512fcc70`). Revision 2 no longer relies on them, but they remain consistent with §2.
