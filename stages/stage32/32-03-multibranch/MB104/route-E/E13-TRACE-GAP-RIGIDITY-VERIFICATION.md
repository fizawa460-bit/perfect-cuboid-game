# E13 — Trace-gap rigidity: verification and open gaps (2026-11-11)

Status: research note, **not audited, zero credit**. Continues E12 §5 (the open core: a uniform degree bound for Problem W). Route-E notation as in E10–E12.

This note records the hostile verification of the E13 draft ("Trace-gap rigidity"), a corrected sketch of Theorem B, an improvement of the packing constant via the distance spectrum, and a first analysis of mixed slack-0 types. No statement is made about the existence or non-existence of perfect cuboids.

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

In the unit group of the Bolza order, elements g with g² = ±1 were enumerated (12 such elements). The K-span of their pairwise products (66 products) has full rank 8. Thus products of involutions can span D_B when sufficiently many are present. With only two remaining involutions the single product cannot span; with four or more, spanning is plausible.

### 2.4 What is still open

- A rigorous (non-computational) proof that the products of the remaining involutions span D_B for all a > A₀, or a genericity statement that covers the arithmetic case.
- Explicit verification for the boundary cases a = 3, 4 if A₀ is lowered.

## 3. Distance spectrum of order-2 points and improved packing

The same enumeration of the 12 involutions yields the reduced traces of their products. The distinct positive hyperbolic distances between the corresponding order-2 points begin at

\[ d_{\min} \approx 1.528571. \]

(The full list of observed distances starts 1.528571, 2.448452, 2.914035, ….)

Using balls of radius \(d_{\min}/2\) instead of the coarser packing radius of the original argument improves the packing constant in the ball of radius \(R(\ell^*)\approx 5.4838\):

- original N ≈ 840,
- improved N ≈ 389.

The resulting degree bound scales by the same factor, giving a provisional a ≤ 2710 (exact constant depends on the precise relation between N and a in the original derivation). This is a computed improvement, not yet folded into a fully rewritten proof of Theorem A.

## 4. Mixed slack-0 types

For slack-0 maps one has |O_i| = 2 deg p_i + 4 (E11 Lemma 1). Mixed types are those in which s_1 = s_2 = 0 but O_1 ≠ O_2 (so the odd sets differ). The four combinatorial types (1,1), (2,2), (3,1), (1,3) refer to the possible local patterns of how the differing points sit relative to the fibres.

**Obstruction to a global contraction.** There is no single element of Comm(Γ₀) that conjugates the two developing maps on the whole of V₀, because the branch data O_1 and O_2 are different. Theorem B still applies locally: outside a bounded neighbourhood of the symmetric difference O_1 Δ O_2 the two maps are conjugate by an element of the commensurator.

**Double-cover reduction (suggested in the draft).** Let π : V' → V₀ be the double cover branched exactly at O_1 Δ O_2. Then both pulled-back maps p_i' = p_i ∘ π have the same odd set (the preimage of O_1 ∩ O_2 together with the new ramification points of equal multiplicity) and the same slack pair (m_2, m_1), where m_i is half the number of points of O_j that are not in O_i. On V' the two maps therefore satisfy the hypotheses of the equal-odd-set case of Theorem B. The degree of each p_i' is twice the original degree, so a bound on the degree of the pulled-back maps yields a bound on the original degrees.

**What is proved in outline.** The reduction is valid whenever |O_1 Δ O_2| is finite (which it always is for algebraic maps) and the double cover is irreducible. The local conjugacy outside a bounded set then lifts to the cover. The spanning hypothesis of §2 must be checked on the cover; because the number of remaining involutions grows with the degree, the same computational evidence applies for large degree.

**Precise obstruction for small symmetric difference.** If |O_1 Δ O_2| ≤ 4 the neighbourhood N of Theorem B already contains all differing points, so the conjugacy holds on a cofinite set and the degree is bounded by the packing of Theorem A (or its improvement in §3). For larger symmetric differences the double-cover reduction reduces the problem to the equal-odd-set case already treated by Theorem B, at the cost of doubling the degree.

**Still open.** An explicit bound on |O_1 Δ O_2| in terms of the bidegree (coming from the Riemann–Hurwitz relation and the label-matching conditions of E10–E12) would turn the reduction into a uniform degree bound. No such bound is written here.

## 5. What remains open (research, not bookkeeping)

1. Rigorous spanning (or genericity) for the large-a case of Theorem B.
2. Explicit treatment of a ≤ A₀.
3. Full incorporation of the distance spectrum into a rewritten packing argument.
4. Mixed slack-0: an explicit bound on |O_1 Δ O_2| that makes the double-cover reduction effective.
5. Positive-slack case (Variant A′): each p_i factors as an arithmetic covering followed by a π_1-surjective map of degree ≥ 2; a bound in terms of the slack is not yet proved.
6. Carry-over of Lemma 1 to k = 4 (Problem W₄).

Characteristic 0 only.

## 6. Reproduction

Filtration, packing, involution-product rank, and distance-spectrum computations are reproducible in Python from the Bolza generators α, β and the multiplication table of D_B = (-3, √2). The minimal distance is obtained from the reduced traces of products of elements satisfying g² = ±1.
