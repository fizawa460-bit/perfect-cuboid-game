# E13 — Trace-gap rigidity: verification and open gaps (2026-11-11)

Status: research note, **not audited, zero credit**. Continues E12 §5 (the open core: a uniform degree bound for Problem W). Route-E notation as in E10–E12.

This note records the hostile verification of the E13 draft ("Trace-gap rigidity"), a corrected sketch of Theorem B, an improvement of the packing constant via the distance spectrum, an analysis of mixed slack-0 types with a quantitative bound on the symmetric difference, an outline for positive slack, and computational data on when subsets of involutions span D_B. No statement is made about the existence or non-existence of perfect cuboids.

## 1. Hostile check of Theorem A

All five steps hold under the stated hypotheses of the draft:

- (a) G ⊂ PQ¹ / PQ¹(2), so that Γ₀ = PQ¹(𝕎²).
- (b) trd(𝕎) ⊂ √2 · ℤ[√2], and both traces compared in Theorem A are traces of level-≥3 elements of conjugates of Γ₀.
- (c) The lifted map G : ℍ → ℍ is a branched covering branched exactly over the lifts of O₂ ∖ O₁, so a holomorphic section F exists on a disc avoiding them.
- (d) Strictness T₁ < T₂, including the case where the two lifts have the same image.
- (e) Isolation and packing count in part 2 (original N ≈ 840, a ≤ 5863).

**Computation (Python, quaternion algebra mod 2).** Reproduced the filtration of Q_B / 2Q_B:
- |P^k / 2Q_B| = 64 / 16 / 4 / 1,
- exact level counts 64 / 24 / 4 / 3 / 1,
- 7 involutions at level ≥2,
- the (ℤ/2)³ subgroup.

The original packing bound of Theorem A part 2 is reproduced (ℓ* ≈ 3.045, R(ℓ*) ≈ 5.4838, N ≈ 840, a ≤ 5863).

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

In the unit group of the Bolza order, elements g with g² = ±1 were enumerated (12 such elements). The K-span of their pairwise products (66 products) has full rank 8.

**Subset experiment (20 random subsets each):**
- Size 4: ranks range 2–6, never full (0/20).
- Size 6: ranks mostly 8, occasionally 6–7 (17/20 full).
- Size 8: always full rank 8 (20/20).

Thus spanning becomes reliable once at least 6–8 involutions remain. This supports setting A₀ so that 2a − 4 ≥ 8, i.e. A₀ ≥ 6, or treating a ≤ 6 by direct means and using the density argument only for larger a.

### 2.4 What is still open

- A rigorous (non-computational) proof that the products of the remaining involutions span D_B for all a large enough, or a genericity statement that covers the arithmetic case.
- Explicit verification for the boundary cases around the transition (a = 4, 5, 6).

## 3. Distance spectrum of order-2 points and improved packing

The same enumeration of the 12 involutions yields the reduced traces of their products. The distinct positive hyperbolic distances between the corresponding order-2 points begin at

\[ d_{\min} \approx 1.528571. \]

Using balls of radius \(d_{\min}/2\) improves the packing constant in the ball of radius \(R(\ell^*)\approx 5.4838\):

- original N ≈ 840,
- improved N ≈ 389.

Provisional degree bound a ≤ 2710. This is a computed improvement, not yet folded into a fully rewritten proof of Theorem A.

## 4. Mixed slack-0 types

For slack-0 maps |O_i| = 2 deg p_i + 4. Mixed types have O_1 ≠ O_2.

**Double-cover reduction.** The double cover branched at O_1 Δ O_2 makes both pulled-back maps have the same odd set. Degree doubles.

**Quantitative bound for small bidegrees.** |O_1 Δ O_2| ≤ 8 for all bidegrees (a,b) with a,b ≤ 4 and both slacks 0. For these the packing argument already bounds the degree.

**Still open.** A uniform bound on |O_1 Δ O_2| valid for all degrees.

## 5. Positive slack (Variant A′) — outline only

When s_i > 0 the map p_i factors as an arithmetic covering followed by a π_1-surjective map of degree ≥ 2. The excess is expected to be controlled by the slack. No explicit bound is written.

## 6. What remains open (research, not bookkeeping)

1. Rigorous spanning (or genericity) for sufficiently large a in Theorem B. Computational threshold is around 6–8 remaining involutions.
2. Explicit treatment of a ≤ A₀ (suggested A₀ = 6).
3. Full incorporation of the distance spectrum into a rewritten packing argument.
4. Mixed slack-0: a uniform bound on |O_1 Δ O_2| valid for all degrees.
5. Positive-slack case: an explicit bound on the excess degree in terms of the slack.
6. Carry-over of Lemma 1 to k = 4 (Problem W₄).

Characteristic 0 only.

## 7. Reproduction

All computations (filtration, packing, full and subset involution-product ranks, distance spectrum) are reproducible in Python from the Bolza generators α, β and the multiplication table of D_B = (-3, √2).
