# E13 — Trace-gap rigidity: verification and open gaps (2026-11-11)

Status: research note, **not audited, zero credit**. Continues E12 §5 (the open core: a uniform degree bound for Problem W). Route-E notation as in E10–E12.

This note records the hostile verification of the E13 draft ("Trace-gap rigidity") and the corrected conditions required for Theorem B. No statement is made about the existence or non-existence of perfect cuboids.

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

## 2. Theorem B: Zariski density — gaps and corrected conditions

The outline of Theorem B requires an explicit justification that ρ₁(π₁^orb(W)) is Zariski-dense in the algebraic group G of Γ₀ (so that Skolem–Noether applies to the conjugating element g).

### 2.1 Errors in the first explicit version

- Involutions alone do **not** generate a Zariski-dense subgroup. They are level-2 elements and generate a finite group ≈ (ℤ/2)³ whose Zariski closure is 0-dimensional. Density is carried by their products (level ≥3 elements).
- π₁^orb(W) is not a finite-index subgroup of Λ₁, so the standard fact “finite-index subgroups of arithmetic groups are Zariski-dense” does not apply directly.
- For small a the number of remaining involutions may be too small for their products to span D_B.

### 2.2 Corrected applicability conditions

**Case distinction.**
- If a ≤ A₀ (suggested A₀ = 4), treat separately by the packing of Theorem A or by direct monodromy computation. The conclusion is then bounded by an absolute constant.
- If a > A₀, proceed as follows.

**Large-a case.**
- N is a neighbourhood of radius an absolute constant R₀ of O₁ Δ O₂, so at most 4 cone points are removed. W therefore contains at least 2a − 4 involutions of O₁.
- Products of two such involutions yield level-≥3 elements whose reduced traces lie in 2 + 2ℤ[√2].
- These products must be shown to K-span D_B (equivalently, to span the Lie algebra sl_1(D_B)). With that spanning, a Borel-density argument yields that the Zariski closure of the image is the full G = D_B^	imes / K^	imes.
- The isometry g normalises this image, hence normalises D_B, and Skolem–Noether supplies g ∈ D_B^	imes · ℝ^	imes.

**Still open for a complete proof of Theorem B.**
1. Explicit construction (or genericity argument) that the products of the remaining involutions span D_B when a > A₀.
2. Clean separation of the small-a case.

## 3. What remains open (research, not bookkeeping)

1. Explicit spanning of D_B by products of remaining involutions (large-a case of Theorem B).
2. Case distinction and separate treatment for small a.
3. Sharpened packing bound using the exact distance spectrum of order-2 points in hyperbolic balls (instead of the pure packing estimate).
4. Mixed slack-0 types (1,1), (2,2), (3,1), (1,3) and the positive-slack case (Variant A′).
5. Whether Lemma 1 carries over to k = 4 (Problem W₄).

Characteristic 0 only. All computations referenced above are local to this verification.

## 4. Reproduction

The filtration and packing computations were performed in a Python environment with an explicit quaternion multiplication table for the Bolza order modulo 2. Scripts can be supplied on request.
