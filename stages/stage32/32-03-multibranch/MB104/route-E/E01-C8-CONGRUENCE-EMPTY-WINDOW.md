# E01 — C8 is a principal congruence quotient; the F69 window becomes empty (2026-11-02)

Status: research note, **unaudited, zero credit**. Conditional on the same receiver hypotheses as MB104-F69 (`../drive-research/research/MB104-F69.md`) §3.
GitHub authority: `stages/stage32/32-03-multibranch/STATE.json` (`route_register.routes.E`). Registered as an unaudited note; not in `retained_frontier`.

## 1. Claim

**Lemma E01.** Let C8 be the genus-5 curve u² = (r⁴+4)/4, v² = (r⁴−4)/4. Let Z be the normalization of an integral
curve in C8×C8 whose two projections are finite étale of the same degree d. Let a group H of order h ∈ {4, 8},
acting diagonally through Aut(C8), preserve the image, and let the underlying curve of E = Z/H have genus ≤ 1.
Then d ≤ 21 if h = 4 and d ≤ 42 if h = 8.

In particular, no such Z exists with d = 56m (m ≥ 1). Under the F69 hypotheses this replaces the conditional window
d ≤ 196416 (m ≤ 3507) by the empty set. The argument does not distinguish rational-core from coreless
correspondences.

## 2. Proof

**Step 1. C8 = H/Γ with Γ = PQ¹_B(2), a principal congruence subgroup.**

- Katz–Katz–Schein–Vishne (arXiv:1405.5454) set up the following.
  - The Bolza order Q_B = O_K⟨1, α, β, αβ⟩, with K = Q(√2), is maximal in D_B = (−3, √2), which is ramified at (√2) and at one real place (Thm 1.4, Thm 7.1, Prop 6.2).
  - `bolza_mod2.py` re-derives the structure constants independently, from the defining formulas α = (1+i)/2, γ = (3+i)(1−(1+√2)j)/6 and β = α(1−(1−√2)γ) in (−3, √2), with exact arithmetic over Q(√2). The checks are: α² = α−1, β² = β−1, βα = (−1−√2)+α+β−αβ, γ² = (1+√2)+γ, nrd α = nrd β = 1, α³ = β³ = (αβ)⁴ = −1.
  - Q¹_B/{±1} ≅ Δ(3,3,4), and this is the index-2 subgroup of Δ(2,3,8) (Lemma 3.2).
- `bolza_mod2.py` computes the image of Q¹_B = ⟨α, β⟩ in (Q_B/2Q_B)^×. The result:
  - The image has order 96. Since −1 ≡ 1 mod 2, [PQ¹_B : PQ¹_B(2)] = 96.
  - The images of α, β, αβ have orders 3, 3, 4. Every torsion element of Δ(3,3,4) is conjugate to a power of α, β or αβ, so PQ¹_B(2) is torsion-free.
- The area is 96 · π/6 = 16π, so H/PQ¹_B(2) has genus 5.
- Δ(2,3,8) normalizes Δ(3,3,4) = PQ¹_B. Hence it normalizes O_K[α, β] = Q_B and 2Q_B, and so it normalizes PQ¹_B(2).
- Therefore Aut(H/PQ¹_B(2)) ⊇ Δ(2,3,8)/PQ¹_B(2), which has order 192.
- The genus-5 curve with 192 automorphisms is unique: the Wiman curve, which is X(8) (Kuribayashi–Kimura; LMFDB 5.192-181.0.2-3-8).
- C8 is that curve: MB104-F69 (`../drive-research/research/MB104-F69.md`) §2 checks the 192-element group on this model and matches Swinarski's genus-5 locus 1.
- Hence C8 ≅ H/Γ with Γ = PQ¹_B(2). Γ contains Γ¹_{Q_B}(2Q_B), so Γ is congruence in the sense of LMR Definition 4.1.

**Step 2. Uniformize the correspondence.** This follows F69 §3.

- Because the projections are étale, Z = H/K with K = Γ ∩ a⁻¹Γa for some a ∈ Comm(Γ), and d = [Γ : K].
- Birationality onto the image in C8×C8 is what makes K equal to this intersection: two lifts with the same image pair differ by an element of Γ ∩ a⁻¹Γa.
- The diagonal H lifts to L ⊃ K with L/K ≅ H, and E = H/L as an orbifold.

**Step 3. L is a congruence arithmetic group.**

- Γ is arithmetic, so Comm(Γ) is the image of D_B^×, and a ∈ D_B^×.
- O′ := a⁻¹Q_B a is a maximal order, and a⁻¹Γa ⊇ PO′¹(2O′).
- Pick a nonzero ideal 𝔫 of O_K with 𝔫Q_B ⊂ 2O′ ∩ 2Q_B. Then Q¹_B(𝔫) ⊂ O′¹(2O′) ∩ Q¹_B(2), so K ⊇ PQ¹_B(𝔫).
- Since L ⊇ K, L is a congruence arithmetic Fuchsian group (LMR Def. 4.1).

**Step 4. Area and spectral bounds.**

- K is torsion-free, so Area(H/K) = d · Area(H/Γ) = 16πd and Area(H/L) = 16πd/h. The genus of L is g(E) ≤ 1.
- LMR Thm 4.3 (Gelbart–Jacquet / Vignéras): λ₁(L) ≥ 3/16.
- LMR Thm 4.4 (Zograf), valid for any Fuchsian group of finite co-area: if A ≥ 32π(g+1), then λ₁ < 8π(g+1)/A.
- With g ≤ 1, either A < 64π, or 3/16 < 16π/A, i.e. A < 256π/3. In both cases A < 256π/3.
- So 16πd/h < 256π/3, i.e. d < 16h/3.
- h = 4: d ≤ 21. h = 8: d ≤ 42. □

## 3. What is still open (audit points)

1. The receiver hypotheses of F69 §3, namely that the real MB104 carrier gives such a minimal Z with étale legs, an H-quotient of genus ≤ 1, and d = 56m. These are HOLD in F69 and are not touched here. F69 §7 also shows that dropping minimality (birationality onto the image) breaks the argument.
2. The structure constants are re-derived in `bolza_mod2.py`. ⟨α, β⟩ is the full norm-one group: by Borel's volume formula, Area(H/PO¹) = 2π·ζ_K(−1)·∏_{𝔭|disc}(N𝔭−1) = 2π·(1/12)·1 = π/6, using ζ_{Q(√2)}(−1) = 1/12. This equals the area of Δ(3,3,4) = ⟨α, β⟩/±1, so the two groups coincide. This is to be re-checked by the auditor, together with the Wiman uniqueness statement.
3. Exact statements of LMR Thm 4.3/4.4. The text was checked on 2026-11-02 from genus0_final.pdf, pp. 465–466. Zograf's theorem as quoted there allows any finite co-area Fuchsian group, so elliptic points are fine.
4. Whether other MB104 branches feed into this receiver. This lemma only closes what F69's receiver covers.

## 4. Files

- `bolza_mod2.py`: exact computation of the mod-2 image, with an associativity check of the structure constants.
- Sources:
  - arXiv:1405.5454 (KKSV)
  - Long–Maclachlan–Reid, Pure Appl. Math. Q. 2 (2006) 459–489, §4
  - LMFDB 5.192-181.0.2-3-8
  - Swinarski genus-5 table
