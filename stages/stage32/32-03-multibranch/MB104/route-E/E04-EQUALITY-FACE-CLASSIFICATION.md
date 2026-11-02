# E04 — The Beauville equality face is exactly the 32 + 48 known curves (2026-11-02)

Status: research note, **unaudited, zero credit**. It uses E02 §1–§2 (FSM facts, the Beauville chain), Lemma E01′,
and an exact finite computation (`hecke/hecke.py`, `hecke/run_face.py`, built on `hecke/qalg.py` and `hecke/deltagrp.py`).

## 1. Claim

**Lemma E04.** Let C̄ ⊂ B be an integral curve on the box variety (non-exceptional on S) of geometric genus g ≤ 1
that lies on the Beauville equality face r = d − 4g + 4. Then C̄ is one of:

- the **32 rational curves of degree 2**: the images of the graphs of the 32 elements σ of the centralizer C(G) of G in Aut(C8). For these, g = 0, d = 2, e = 4, |Stab| = 8. Their number matches the 32 non-exceptional rational curves of Stoll–Testa / FSM Prop 2.6. The literal FSM formula `w = Mz + k`, M ∈ Γ[4]/Γ[8], k ∈ {0,2,4,6}, only yields 16 distinct automorphisms, because z ↦ z + 4 lies in G. So the identification is by count, not by that formula.
- the **48 elliptic curves of degree 4**: the images of the graphs of the 96 automorphisms σ whose centralizer in G has order 4 and contains exactly one singular involution s_i, taken up to G-conjugacy (48 classes). For these, g = 1, d = 4, e = 2, |Stab| = 4. Their number matches the 48 non-boundary elliptic curves of FSM Prop 2.9.

All of them are graphs of automorphisms of C8, i.e. leg degree n = 1. No genuine Hecke correspondence (n > 1) gives a
curve of genus ≤ 1.

Combined with E03, every genus-≤1 curve of B other than these 80 satisfies **r ≥ d − 4g + 5**, in every degree.

## 2. Proof

**Step 1. Reduction to Hecke correspondences.**

- On the equality face, a component Z of the pullback to C8×C8 is the normalization of an integral curve with étale legs of degree n = ed/8 (E02 §2(E),(S)). Here e ∈ {1, 2, 4} and |Stab_G(Z)| = 2e.
- With the compact uniformization C8 = H/Γ, Γ = PQ¹_B(2) (E01), Z = H/K with K = Γ ∩ a⁻¹Γa for some a ∈ Comm(Γ) = PD_B^×₊, and n = [Γ : K] (E01 Step 2).
- Lemma E01′ with A = Stab_G(Z) gives n < 16·2e/3 ≤ 128/3, so n ≤ 42.

**Step 2. Which double cosets have index ≤ 42 (completeness, written out after audit round 1).**

- (2a) *Which elements occur.*
  - Γ is arithmetic, so Comm(Γ) is the image of D_B^× in PGL₂(R) under the split real place (Borel).
  - A correspondence of compact Riemann surfaces needs a holomorphic action on H. So a has positive reduced norm at the split real place.
  - At the ramified real place, nrd is positive definite, hence positive there too.
  - Therefore nrd(a) is totally positive. Elements with negative norm at the split place act anti-holomorphically, or swap the upper and lower half planes, and give no holomorphic correspondence.
- (2b) *Local–global.* By strong approximation for the norm-one group of D_B (indefinite at one real place), [Γ : Γ ∩ a⁻¹Γa] = ∏_𝔭 [Γ_𝔭 : Γ_𝔭 ∩ a⁻¹Γ_𝔭 a]. Here Γ_𝔭 is the closure of Γ, with Γ_𝔭 = O¹_𝔭(2O_𝔭) at 𝔭 = (√2) and Γ_𝔭 = O¹_𝔭 ≅ SL₂(O_𝔭) at 𝔭 ∤ 2.
- (2c) *At (√2) the local index is 1.*
  - D_B ⊗ K_(√2) is a division algebra (KKSV §5). Its valuation ring O_2 is the unique maximal order, and every one-sided ideal of O_2 is a power of the unique maximal ideal P, hence two-sided.
  - So every local a satisfies a·O_2·a⁻¹ = O_2 and a·2O_2·a⁻¹ = 2O_2.
  - Hence a normalizes Γ_2 = O¹_2(2O_2), and the local index is 1.
- (2d) *At 𝔭 ∤ 2.* D_B splits at 𝔭, and Γ_𝔭 = SL₂(O_𝔭) is the stabilizer of a vertex of the Bruhat–Tits tree.
  - For a at tree distance k from that vertex, the local index is the size of the SL₂(O_𝔭)-orbit of a vertex at distance k, which is (N𝔭+1)·N𝔭^(k−1) (k ≥ 1), and 1 for k = 0.
  - The smallest norm of a prime 𝔭 ∤ 2 of Z[√2] is 7. Rational primes ≡ ±1 mod 8 split, the smallest being 7; inert primes have norm p² ≥ 9.
- (2e) *Conclusion.*
  - Index ≤ 42 allows nontrivial distance at no more than one prime (two primes give at least 8·8 = 64), and there only k = 1 (k = 2 gives N(N+1) ≥ 56).
  - If the distance is 0 everywhere, a normalizes Γ locally everywhere. By (2b), a ∈ N(Γ), which is Δ(2,3,8) because Δ(2,3,8) is a maximal Fuchsian group (F69 §4, LMR) containing Γ as a normal subgroup.
  - So n ∈ {1} ∪ {N𝔭 + 1 : N𝔭 ≤ 41}. The primes are:
    - split: 3 ± √2 (N = 7), 5 ± 2√2 (17), 5 ± √2 (23), 7 ± 3√2 (31), 7 ± 2√2 (41);
    - inert: 3 (N = 9) and 5 (N = 25).

    That gives 12 primes.

**Step 3. The twists.**

- *Every distance-1 element is a twist of a fixed one.* Let a′ be another element at distance 1 at 𝔭.
  - Γ is dense in SL₂(O_𝔭), so it acts transitively on the neighbours of the base vertex. Choose γ ∈ Γ with γ·a′ and a at the same neighbour.
  - Then a(γa′)⁻¹ normalizes every local order, so it lies in N(Q_B)₊ = Δ. Hence T_{a′} = (1 × δ̄)·T_a for some δ̄ ∈ Δ/Γ.
  - A twist on the first factor reduces to the second: (σ × 1)T = (σ × σ)(1 × σ⁻¹)T. Swapping the factors gives T_{a⁻¹}, which is in the same family.
- *The computed S is an upper bound for the true stabilizer.* Equality of the curves (g × g)Z_σ = Z_σ forces, 2-adically, g = σφ(g)σ⁻¹. So the code's S(σ) contains the true stabilizer, and the computed genus is at most the true genus. For the exclusion of genus ≤ 1 this is the right direction. For n = 1 (graphs) S is exact.

- Up to the diagonal action of Aut(C8) = Δ/Γ, which normalizes G and so descends to automorphisms of B, every such curve is Z_σ = (1×σ)·{(Γz, Γaz)} with σ ∈ Δ/Γ (192 twists).
- Its G-stabilizer is S(σ) = {g ∈ G : σφ(g)σ⁻¹ = g}, where φ is conjugation by a on Δ/Γ.
- Z_σ/S(σ) = H/L with L = {ℓ ∈ Δ ∩ a⁻¹Δa : ℓΓ ∈ S(σ)}.

**Step 4. Computation.** The computation is exact, over Q(√2) and residue fields.

- Δ(2,3,8) = ⟨x, y⟩ with y = α and x = −1 + α + β ∈ Q_B. Here nrd x = 2 + √2, x² is central, and (xy)⁸ is central.
- Δ/Γ is built from mod-2 coset keys. It has 192 elements, and x, y, xy have orders 2, 3, 8.
- G is the normal (Z/2)³ in Δ/Γ. Three of its elements have 8 fixed points each, and four are free. G0 is the free subgroup of order 4.
  - *Identification with FSM* (round 1, must-fix 3). FSM's G = Γ[4]/Γ[8] is a normal subgroup of Aut(X(8)) of order 8 consisting of the identity and involutions. FSM's G0 = Γ′[4]/Γ[8] is a subgroup of order 4 acting freely (FSM Lemma 4.1).
  - `run_face.py` checks that the 192-element group has **exactly one** normal subgroup of order 8 made of the identity and involutions, and that this G has **exactly one** subgroup of order 4 acting freely.
  - So the code's G and G0 are FSM's, independently of how Aut(C8) ≅ Δ/Γ is identified.
- For each prime, Δ ∩ a⁻¹Δa is the stabilizer of the left ideal (Q_B/𝔭)·ā among the N𝔭 + 1 minimal left ideals. φ is computed 2-adically.
  - *Lift independence of φ* (round 1, must-fix 4). Fix a. For two lifts ℓ, ℓγ (γ ∈ Γ) of h ∈ Δ/Γ we have aℓγa⁻¹ = (aℓa⁻¹)(aγa⁻¹). Write γ = 1 + 2t with t ∈ O_2. Then aγa⁻¹ = 1 + 2·ata⁻¹ ∈ 1 + 2O_2, because a normalizes O_2 (Step 2c). So the 2-adic key of aℓa⁻¹, hence φ(h), does not depend on the lift.
  - Changing a within its double coset only composes Z with automorphisms of the factors. Those are covered by enumerating all 192 twists σ (Step 3).
  - `run_face.py` also checks this numerically: φ recomputed with 8 nontrivial Γ elements (Schreier generators) agrees, for every prime.
- The genus of H/L is computed by Riemann–Hurwitz from the cycle types of x, y, xy on Δ/L. This is valid for **every** finite-index L, with or without torsion (round 1, must-fix 2, answered):
  - the underlying compact surface of the orbifold H/L is a branched cover of degree N = [Δ : L] of the underlying sphere of H/Δ;
  - it is branched only over the three cone points;
  - over the cone point of type g, its points are the cycles of g on Δ/L, with ramification index equal to the cycle length.

  Riemann–Hurwitz for these underlying surfaces gives 2g(H/L) − 2 = −2N + Σ_g (N − c_g). Elliptic points of L are cycles shorter than ord(g) and are already counted correctly. No orbifold correction enters the *underlying* genus, which is the genus of Ē.
- Sanity check: for every prime, g(Z) = 1 + 4(N𝔭 + 1), as theory predicts (33, 41, 73, 97, 105, 129, 169).

**Results.** All 12 primes and the graphs, 192 twists each, 2496 cases in all:

| n | twists with genus(Z/S) ≤ 1 | distinct curves in B (G-conjugacy classes of σ) |
|---|---|---|
| 1 (graphs) | 32 with \|S\| = 8, e = 4, genus 0; 96 with \|S\| = 4, e = 2, genus 1 | **32 rational, 48 elliptic** |
| 8, 10, 18, 24, 26, 32, 42 | none | none |

The minimal genus of Z_σ/S(σ) over the twists, per prime, is 5 (N = 7), 3 (9), 7 (17), 13 (23), 11 (25), 17 (31) and 19 (41).

The counts 32 and 48 and the degrees (d = 8n/e = 2 and 4) match FSM Prop 2.6 and 2.9 exactly. The 12 Satake-boundary
elliptic curves (FSM Prop 2.7) have r = 8 > d = 4. They are off the face, consistent with the auditor's check in E03 round 2.

## 3. Consequence for MB104

- Conditional on the inputs in §4 (completeness of the double-coset list in Step 2, and the correctness of the code), the equality face contributes only the 80 known curves above. The off-face inequality r ≥ d − 4g + 5 for all other curves is inherited from E03, not proved anew. E04 only classifies the face r = d − 4g + 4. MB104's multibranch population is the rest.
- So the open part of MB104 is exactly the genus-≤1 curves with r ≥ d − 4g + 5 (strictly off the face) in every degree, together with the boundary/known curves already classified.
- The off-face case r > d − 4g + 4 (ramified legs) is still the open core. Since r is even, this means r ≥ d − 4g + 6 when d is even, and r ≥ d − 4g + 5 when d is odd. A finite window needs a new idea there.

## 4. Audit points

1. Step 2: the local index formula and the completeness of the list of double cosets of index ≤ 42, including the claim that there is no index > 1 at (√2), and the prime list.
2. Step 3: the reduction of all curves to (1×σ)·T_a up to diagonal Aut(C8), and the formulas for S(σ) and L.
3. The code:
   - the 2-adic φ;
   - the ideal action I ↦ I·δ⁻¹, and that the stabilizer of (Q_B/𝔭)ā is Δ ∩ a⁻¹Δa;
   - the cycle-based genus;
   - the identification of G and G0.
4. The match with FSM Prop 2.6/2.9 is a check, not a proof input.
5. No credit, frontier change or MB104 closure is claimed.

## 5. Reproduction

From `stages/stage32/32-03-multibranch/MB104/route-E/hecke/`:

```
python -O run_face.py
```

It takes about 1 minute. The script prints g(Z) for every prime, the counts, and finally `distinct curves: genus 0 32  genus 1 48` and `PASS`, with exit code 0. All checks are fail-closed: no `assert`, so `-O` cannot disable them. It writes the per-twist table to `face_results.json` in the system temporary directory, not in the repository.

## 6. Audit history

- **Round 1: DeepSeek (reading), HOLD at `5a10c241`.** Four must-fix items:
  1. Completeness of the double-coset list → Step 2 written out (2a–2e).
  2. The genus formula with torsion → answered: Riemann–Hurwitz on the underlying surfaces, valid for any finite-index L.
  3. Identification of G and G0 → uniqueness checked in code.
  4. Lift independence of φ → proved, and checked in code for all 12 primes.

  Should-fix items:
  1. Execution → `python -O run_face.py` PASS at revision 2.
  2. The off-face inequality is inherited from E03 → §3.
  3. Conditional wording → §3.
- **Round 2: Claude (executing), PASS at `5a10c241`. No must-fix.**
  - Re-ran all scripts with matching hashes.
  - Independent re-implementations:
    - PSL₂(Z/8) (graphs: 32 and 48);
    - a separate Hecke implementation for N = 7 and 9, with the same genus distributions.
  - Should-fix items, addressed in revision 3:
    1. Completeness argument → Step 2 (revision 2), plus the transitivity / N(Q_B)₊ = Δ argument and S as an upper bound in Step 3.
    2. FSM Prop 2.6 identification is by count only → claim restated via C(G).
    3. Fixed-point pattern and normality of G now in the fail-closed check.
    4. The μ/r confusion in §3 → fixed; parity refinement added.
    5. `face_results.json` now written to the temporary directory.
