# E13 — Trace-gap rigidity: verification and open gaps (2026-11-11)

Status: research note, **not audited, zero credit**. Continues E12 §5 (the open core: a uniform degree bound for Problem W). Route-E notation as in E10–E12.

This note records the hostile verification of the E13 draft, a corrected sketch of Theorem B, packing improvements, mixed slack-0 analysis, positive-slack outline, subset-spanning data, and notes on remaining gaps including k=4. No statement is made about the existence or non-existence of perfect cuboids.

## 1. Hostile check of Theorem A

All five steps hold under the stated hypotheses of the draft.

**Computation.** Reproduced filtration counts 64/16/4/1, level counts 64/24/4/3/1, 7 involutions, and the original packing (N ≈ 840, a ≤ 5863).

## 2. Theorem B — corrected sketch

**Theorem B (sketch).** Outside a bounded neighbourhood N of O₁ Δ O₂, on each connected component W the two maps are conjugate by an element of Comm(Γ₀).

### 2.1 Case distinction
- a ≤ A₀ (suggested A₀ = 6): handle by packing or direct computation.
- a > A₀: density argument below.

### 2.2 Large-a outline
Remaining involutions ≥ 2a − 4. For a > 6 this is ≥ 8. Products of these give level-≥3 elements. Spanning hypothesis: their K-span is D_B. Then Zariski closure is full G, and Skolem–Noether applies.

### 2.3 Computational evidence
12 involutions give full rank 8.

Subset ranks (20 samples):
- size 4: never full
- size 6: 17/20 full (occasional rank 7)
- size 8: always full

Non-full size-6 subsets exist and have fewer distinct product traces, consistent with lying in a proper subspace. This supports A₀ = 6 (so that ≥8 involutions remain).

### 2.4 Still open
Rigorous reason that arithmetic configurations with ≥8 remaining involutions cannot lie in a proper subspace.

## 3. Distance spectrum and improved packing

d_min ≈ 1.528571.

Improved packing in the ball of radius R ≈ 5.4838: N ≈ 389 (original 840).

Provisional a ≤ 2715. Full rewrite of the packing argument with this spectrum is still open.

## 4. Mixed slack-0

Double cover branched at O₁ Δ O₂ reduces to equal-odd-set case (degree doubles).

For bidegrees ≤ 4: |O₁ Δ O₂| ≤ 8, so packing already bounds the degree.

Uniform bound for all degrees remains open. No new algebraic relation forcing |O₁ Δ O₂| = O(1) independently of degree was found.

## 5. Positive slack (Variant A′)

Outline: p_i = arithmetic covering composed with π₁-surjective map of degree ≥ 2. Excess degree is expected to be ≤ C·s_i for some absolute C (from the dimension of the moduli of such maps). Once the excess is controlled, the arithmetic factor is bounded by the packing of Theorem A. Explicit C is not computed.

## 6. k = 4 (Problem W₄)

Lemma 1 (filtration counts and 7 involutions) is specific to the Bolza order for k=8. For k=4 the corresponding congruence subgroup and radical filtration differ; the same counts do not automatically carry over. Existing code in problemw/w4/ can be used to check the analogous level structure, but this has not been done here. Carry-over is open.

## 7. What remains open

1. Rigorous spanning for a > 6 (non-degeneracy of arithmetic configurations).
2. Explicit treatment of a ≤ 6.
3. Full packing rewrite using d_min.
4. Uniform bound on |O₁ Δ O₂| for all degrees.
5. Explicit excess bound for positive slack.
6. Lemma 1 carry-over (or replacement) for k=4.

Characteristic 0 only.

## 8. Reproduction

All listed computations are reproducible from the Bolza generators α, β and the multiplication table of D_B = (-3, √2).
