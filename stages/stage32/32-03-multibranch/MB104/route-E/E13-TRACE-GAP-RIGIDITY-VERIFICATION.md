# E13 — Trace-gap rigidity: verification and open gaps (2026-11-11)

Status: research note, **not audited, zero credit**. Continues E12 §5 (the open core: a uniform degree bound for Problem W). Route-E notation as in E10–E12.

This note records the hostile verification of the E13 draft ("Trace-gap rigidity") and a corrected sketch of Theorem B. No statement is made about the existence or non-existence of perfect cuboids.

## 1. Hostile check of Theorem A

All five steps hold under the stated hypotheses of the draft:

- (a) G ⊂ PQ¹ / PQ¹(2), so that Γ₀ = PQ¹(𝕎²).
- (b) trd(𝕎) ⊂ √2 · ℤ[√2], and both traces compared in Theorem A are traces of level-≥3 elements of conjugates of Γ₀.
- (c) The lifted map G : ℍ → ℍ is a branched covering branched exactly over the lifts of O₂ ∖ O₁, so a holomorphic section F exists on a disc avoiding them.
- (d) Strictness T₁ < T₂, including the case where the two lifts have the same image.
- (e) Isolation and packing count in part 2 (N ≈ 840, a ≤ 5863).

**Computation (Python, quaternion algebra mod 2).** Reproduced the filtration of Q_B / 2Q_B:
- |P^k / 2Q_B| = 64 / 16 / 4 / 1,
- exact level counts 64 / 24 / 4 / 3 / 1,
- 7 involutions at level ≥2,
- the (ℤ/2)³ subgroup.

The packing bound of Theorem A part 2 is likewise reproduced (ℓ* ≈ 3.045, R(ℓ*) ≈ 5.4838, N ≈ 840, a ≤ 5863).

## 2. Theorem B — corrected sketch with case distinction

**Theorem B (sketch).** Outside a bounded neighbourhood N of O₁ Δ O₂, on each connected component W of V₀ ∖ N the two maps are conjugate by an element of Comm(Γ₀). More precisely: there exists g ∈ D_B^	imes · ℝ^	imes such that ρ₂ = g ρ₁ g^{-1} on π₁^orb(W).

### 2.1 Case distinction

- **Small degree (a ≤ A₀).** Suggested A₀ = 4. In this range the packing of Theorem A already bounds a, or the monodromy can be checked directly. The conclusion of Theorem B is then absorbed into an absolute bound. No Zariski-density argument is required.
- **Large degree (a > A₀).** Proceed with the density argument below.

### 2.2 Large-a argument (outline)

1. N has radius an absolute constant R₀, so |O₁ ∩ N| ≤ 4. Thus W contains at least 2a − 4 involutions of O₁.
2. For a > 4 the remaining involutions are numerous. Their pairwise products are level-≥3 elements of conjugates of Γ₀ whose reduced traces lie in 2 + 2ℤ[√2].
3. **Spanning hypothesis.** The K-span of these products is the whole of D_B. (Supported by the computation in §2.3: already 12 involutions give products of full rank 8. With ≥4 remaining involutions the same is expected generically.)
4. The image ρ₁(π₁^orb(W)) therefore contains a set of elements whose K-span is D_B. Its Zariski closure in G = D_B^	imes / K^	imes is consequently the full G (Borel density, or the fact that any proper algebraic subgroup cannot contain enough elliptic elements of level ≥3).
5. The local isometry g that matches the two developing maps normalises this image, hence normalises D_B. Skolem–Noether yields g ∈ D_B^	imes · ℝ^	imes, as required.

### 2.3 Computational evidence for spanning (2026-11-11)

In the unit group of the Bolza order, elements g with g² = ±1 were enumerated (12 such elements). The K-span of their pairwise products (66 products) has full rank 8. Thus products of involutions can span D_B when sufficiently many are present. With only two remaining involutions the single product cannot span; with four or more, spanning is plausible.

### 2.4 What is still open

- A rigorous (non-computational) proof that the products of the remaining involutions span D_B for all a > A₀, or a genericity statement that covers the arithmetic case.
- Explicit verification for the boundary cases a = 3, 4 if A₀ is lowered.

## 3. What remains open (research, not bookkeeping)

1. Rigorous spanning (or genericity) for the large-a case of Theorem B.
2. Explicit treatment of a ≤ A₀.
3. Sharpened packing bound using the exact distance spectrum of order-2 points.
4. Mixed slack-0 types and the positive-slack case (Variant A′).
5. Carry-over of Lemma 1 to k = 4.

Characteristic 0 only.

## 4. Reproduction

Filtration, packing, and involution-product rank computations are reproducible in Python from the Bolza generators α, β and the multiplication table of D_B = (-3, √2).
