# E06 — Co-images of bidegree (1,1) in R×R carry no ε > 0 carrier (2026-11-02)

Status: research note, **unaudited, zero credit**.

- It answers the "Möbius-type" question in the ChatGPT brainstorming proposal of 2026-11-02 (Directions A-1, A-2 and A-4).
- It uses audited F71–F73, E04, and exact computations: `mobius/mobius_enum.py` (k = 8) and `mobius/mobius_enum_k4.py` (k = 4).

## 0. Setting

- A carrier C̄ ⊂ B has the following data:
  - Z ⊂ C8×C8 its real co-image normalization;
  - S = Stab_G(Z), k = |S|;
  - E = Z/S of genus g ≤ 1;
  - the induced maps ψ_i : E → R = C8/S.
- By F72, ε > 0 forces k ∈ {4, 8}, R ≅ P¹, and A₁ + A₂ > 0. Here A_i is the ramification of the leg f_i, and the deficiency D_i satisfies deg D_i = A_i/k.
- Let W ⊂ R×R be the image of (ψ₁, ψ₂), V₀ its normalization, and (a, b) its bidegree.

## 1. Two facts checked from the proposal

**(A) d ≤ 8(a + b).**

- Z → V₀ has degree kδ, where δ = deg(E → V₀).
- Z is birational onto its image Z̄ ⊂ C8×C8, and Z̄ is a component of the preimage of W under C8×C8 → R×R, a map of degree k².
- Hence kδ ≤ k², i.e. δ ≤ k.
- With n₁ = δa, n₂ = δb and d = 8(n₁ + n₂)/k (F71), this gives d = 8δ(a + b)/k ≤ 8(a + b).

**(K) Marked Kummer conditions.**

- For each quadratic character χ of S, the χ-part of K(Z)/K(E) is K(E)(√q_χ(ψ_i)) for both i.
  - k = 8: q_a = 1 + t², q_b = 1 − t², q_e = t on R = P¹_t. The branch sets are B_a = {±i}, B_b = {±1}, B_e = {0, ∞}.
  - k = 4: q_u = ρ⁴ + 1, q_v = ρ⁴ − 1 on R = P¹_ρ, with r = √2·ρ in the model u² = (r⁴+4)/4, v² = (r⁴−4)/4. The branch sets are B_u = the primitive 8th roots of unity and B_v = μ₄.
- Hence q_χ(ψ₁)/q_χ(ψ₂) ∈ K(E)^{×2} for each χ, kept separately (not multiplied together).
- If K(E)/K(V₀) has odd degree, these classes are already squares in K(V₀) (Kummer descent).

## 2. Theorem E06

**Theorem.** If W has bidegree (1,1), i.e. ψ₂ = T∘ψ₁ for a Möbius map T, then ε = 0. Hence, by E04, C̄ is one of the 80 known single-branch curves, and no MB101 carrier has a co-image of bidegree (1,1).

*Proof.*

- **The Kummer condition gives a bound on Δ(T).**
  - Put Δ(T) = ∪_χ (B_χ △ T⁻¹B_χ). The function q_χ∘T / q_χ on P¹ has odd order exactly at the points of B_χ △ T⁻¹B_χ: the pole orders at ∞ are even, and the factor (γt + δ)² or (γt + δ)⁴ is a square.
  - By (K), ψ₁* of it is a square. So every point of E over Δ(T) has even ψ₁-local degree.
  - Riemann–Hurwitz for ψ₁ (degree n) gives (n/2)|Δ| ≤ 2n + 2g − 2, i.e. |Δ(T)| ≤ 4 + 4(g − 1)/n.
- **Counting.**
  - Let j be the number of points of B sent by T to a point of B with the same label, and h the number sent to a point of B with a different label. Then |Δ| = 2|B| − 2j − h.
  - So |Δ| ≤ 4 forces T to send at least three points of B into B. These T are finite in number.
- **Exact enumeration.**
  - k = 8, over Q(i): 1080 candidates. |Δ| ≤ 4 holds for exactly 16 of them: 4 with Δ = ∅ (the label-preserving maps t ↦ ±t, ±1/t) and 12 with |Δ| = 4. No |Δ| ∈ {1, 2, 3} occurs.
  - k = 4, over Q(ζ₈): 8976 candidates. |Δ| ≤ 4 holds only for the 8 label-preserving maps (Δ = ∅).
  - The counting identity is checked for every candidate.
- **Case Δ = ∅.**
  - T preserves every marked branch set, so it lifts to an automorphism σ of C8 normalizing S. Indeed, q_χ∘T/q_χ is a constant times a square.
  - Then f₂ and σ∘f₁ lie over the same map Z → R, so f₂ = gσ∘f₁ for a fixed g ∈ S. Hence Ram f₂ = Ram f₁.
  - F73 Lemma 3.1 then makes both legs étale. In fact Z is the graph of gσ. So ε = 0 by F72 Lemma 3.1.
- **Case |Δ| = 4** (k = 8 only).
  - Then g = 1 and Riemann–Hurwitz is an equality. So ψ₁ is unramified off Δ(T), and every point over Δ(T) has local degree exactly 2.
  - The computation shows Δ(T) ⊂ B and T(Δ(T)) ⊂ B. Since ψ₂ = T∘ψ₁, ψ₂ ramifies only over T(Δ(T)), again with local degree 2.
  - By F72 (4), points over B with local degree ≤ 2 add nothing to D_i, and there is no ramification off B. So D₁ = D₂ = 0, hence A₁ = A₂ = 0, and ε = 0 by F72 Lemma 3.1.
- **Genus 0.** Riemann–Hurwitz gives |Δ| ≤ 3, so only Δ = ∅ remains. □

## 3. Consequences and what remains

- Every MB104 carrier with ε > 0 has a co-image W ⊂ P¹×P¹ of bidegree (a, b) ≠ (1, 1), and d ≤ 8(a + b).
- **Next step (sketch, not proved here): bidegree (1, b).** Then ψ₂ = φ∘ψ₁ with deg φ = b.
  - The same Kummer argument bounds the number of points where q_χ∘φ / q_χ has odd order by 4. So all but at most 10 points of φ⁻¹(B) carry odd ramification only at label-matching points of B.
  - Riemann–Hurwitz for φ then gives −2 ≥ −2b + 3b − 5, so b ≤ 3 (k = 8).
  - This reduces bidegree (1, b) to φ of degree ≤ 3, but φ may ramify freely off B, so it is not yet a finite list. To be done.
- **General (a, b).** The parity conditions on V₀ give a ≤ O/2 + 2g(V₀) − 2, where O is the number of label-matching odd points over B. O grows with the number of node branches, so no uniform bound follows yet. This is the core question of the brainstorming proposal.

## 4. Reproduction

From the repository root:

```
python -I -O stages/stage32/32-03-multibranch/MB104/route-E/mobius/mobius_enum.py
python -I -O stages/stage32/32-03-multibranch/MB104/route-E/mobius/mobius_enum_k4.py
```

The first takes seconds and the second about 7 minutes. Each ends with `PASS`, exit code 0. All checks are fail-closed.

## 5. Audit points

1. The odd-order statement for q_χ∘T / q_χ, including the points at ∞ and the denominators.
2. The equality case of Riemann–Hurwitz, and D_i = 0 ⇒ A_i = 0, which uses deg D_i = A_i/k from F72 (5).
3. The lifting of label-preserving T, and f₂ = gσ∘f₁.
4. The k = 4 model (S = ⟨u ↦ −u, v ↦ −v⟩) as the representative of the three conjugate k = 4 subgroups.
5. The code: Möbius maps through three points, the exact fields, and the counting identity.
