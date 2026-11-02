# E04 — The Beauville equality face is exactly the 32 + 48 known curves (2026-11-02)

Status: research note, **unaudited, zero credit**. It uses E02 §1–§2 (FSM facts, the Beauville chain), Lemma E01′,
and an exact finite computation (`hecke/hecke.py`, `hecke/run_face.py`, built on `hecke/qalg.py` and `hecke/deltagrp.py`).

## 1. Claim

**Lemma E04.** Let C̄ ⊂ B be an integral curve on the box variety (non-exceptional on S) of geometric genus g ≤ 1
that lies on the Beauville equality face r = d − 4g + 4. Then C̄ is one of:

- the **32 smooth rational curves of degree 2**, `w = Mz + k` (FSM Prop 2.6). For these, g = 0, d = 2, e = 4, |Stab| = 8;
- the **48 non-boundary elliptic curves of degree 4**, the Δ(1,2)-orbit of `w = z + 1` (FSM Prop 2.9). For these, g = 1, d = 4, e = 2, |Stab| = 4.

All of them are graphs of automorphisms of C8, i.e. leg degree n = 1. No genuine Hecke correspondence (n > 1) gives a
curve of genus ≤ 1.

Combined with E03, every genus-≤1 curve of B other than these 80 satisfies **r ≥ d − 4g + 5**, in every degree.

## 2. Proof

**Step 1. Reduction to Hecke correspondences.**

- On the equality face, a component Z of the pullback to C8×C8 is the normalization of an integral curve with étale legs of degree n = ed/8 (E02 §2(E),(S)). Here e ∈ {1, 2, 4} and |Stab_G(Z)| = 2e.
- With the compact uniformization C8 = H/Γ, Γ = PQ¹_B(2) (E01), Z = H/K with K = Γ ∩ a⁻¹Γa for some a ∈ Comm(Γ) = PD_B^×₊, and n = [Γ : K] (E01 Step 2).
- Lemma E01′ with A = Stab_G(Z) gives n < 16·2e/3 ≤ 128/3, so n ≤ 42.

**Step 2. Which double cosets have index ≤ 42.**

- The index [Γ : Γ ∩ a⁻¹Γa] is the product of the local indices.
- At the ramified prime (√2), D_B is a division algebra, so every local element normalizes O_2 and 2O_2, hence normalizes Γ locally. Local index 1.
- At a prime 𝔭 ∤ 2 (split for D_B), an element at distance k in the Bruhat–Tits tree has local index (N𝔭+1)·N𝔭^{k−1}.
- Since N𝔭 ≥ 7 for 𝔭 ∤ 2 in Z[√2], index ≤ 42 forces:
  - either a ∈ N(Γ) = Δ(2,3,8) (n = 1, graphs of automorphisms);
  - or a is primitive of distance 1 at a single prime with N𝔭 + 1 ≤ 42.

  Two primes give at least 8·8 = 64, and k = 2 gives N(N+1) ≥ 56.
- The primes with N𝔭 ≤ 41 are:
  - split: 3 ± √2 (N = 7), 5 ± 2√2 (17), 5 ± √2 (23), 7 ± 3√2 (31), 7 ± 2√2 (41);
  - inert: 3 (N = 9) and 5 (N = 25).

  That gives 12 primes.

**Step 3. The twists.**

- Up to the diagonal action of Aut(C8) = Δ/Γ, which normalizes G and so descends to automorphisms of B, every such curve is Z_σ = (1×σ)·{(Γz, Γaz)} with σ ∈ Δ/Γ (192 twists).
- Its G-stabilizer is S(σ) = {g ∈ G : σφ(g)σ⁻¹ = g}, where φ is conjugation by a on Δ/Γ.
- Z_σ/S(σ) = H/L with L = {ℓ ∈ Δ ∩ a⁻¹Δa : ℓΓ ∈ S(σ)}.

**Step 4. Computation.** The computation is exact, over Q(√2) and residue fields.

- Δ(2,3,8) = ⟨x, y⟩ with y = α and x = −1 + α + β ∈ Q_B. Here nrd x = 2 + √2, x² is central, and (xy)⁸ is central.
- Δ/Γ is built from mod-2 coset keys. It has 192 elements, and x, y, xy have orders 2, 3, 8.
- G is the normal (Z/2)³ in Δ/Γ. Three of its elements have 8 fixed points each, and four are free. G0 is the free subgroup of order 4.
- For each prime, Δ ∩ a⁻¹Δa is the stabilizer of the left ideal (Q_B/𝔭)·ā among the N𝔭 + 1 minimal left ideals. φ is computed 2-adically.
- The genus of H/L is computed by Riemann–Hurwitz from the cycle types of x, y, xy on Δ/L.
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

- The equality face contributes only the 80 known curves above. MB104's multibranch population is the rest.
- So the open part of MB104 is exactly the genus-≤1 curves with r ≥ d − 4g + 5 (strictly off the face) in every degree, together with the boundary/known curves already classified.
- The off-face case (μ > d − 4g + 4, ramified legs) is still the open core. A finite window needs a new idea there.

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

It takes about 1 minute. The script prints g(Z) for every prime, the counts, and finally `distinct curves: genus 0 32  genus 1 48` and `PASS`, with exit code 0. All checks are fail-closed: no `assert`, so `-O` cannot disable them. It writes `face_results.json`, the per-twist table, which is not committed.
