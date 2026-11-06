# E08 — Co-images of bidegree (1, b) or (b, 1) with b ≥ 2 do not occur (2026-11-03)

Status: research note, **audit round 1 PASS (two auditors, head 5e199e66; should-fixes applied here), zero credit**.

- It continues E06 (bidegree (1, 1)), and replaces the withdrawn "b ≤ 3" sketch of E06 §3 by a proof.
- It uses audited F72 and E06 §1 (the marked Kummer conditions (K)), and exact computations in `bidegree/`.

## 0. Setting

Notation as in E06 §0:

- Z ⊂ C8×C8 is the co-image normalization of an integral non-exceptional curve C̄ ⊂ B of geometric genus g ≤ 1.
- S = Stab_G(Z), k = |S|, E = Z/S, and ψ_i : E → R = C8/S.
- We assume k ∈ {4, 8}, so R ≅ P¹. By F72, every carrier with ε > 0 satisfies this.
- The branch set B ⊂ R is labelled by the basis characters χ:
  - k = 8: B_a = {±i}, B_b = {±1}, B_e = {0, ∞} on P¹_t, so |B| = 6;
  - k = 4: B_u = the primitive 8th roots of unity, B_v = μ₄ on P¹_ρ, so |B| = 8.
- W ⊂ R×R is the image of (ψ₁, ψ₂), of bidegree (a, b) with a = deg(pr₁|W) and b = deg(pr₂|W).

Bidegree (1, b) means that W is the graph of a map φ : R → R of degree b, i.e. ψ₂ = φ∘ψ₁. Bidegree (b, 1) is the same with the legs swapped.

## 1. Theorem E08

**Theorem.** Under §0, the co-image W never has bidegree (1, b) or (b, 1) with b ≥ 2. The theorem does not use ε, so it holds for every curve C̄ with k ∈ {4, 8}.

**Corollary.** Together with E06: every MB104 carrier with ε > 0 has a co-image of bidegree (a, b) with a ≥ 2 and b ≥ 2.

## 2. Proof

By symmetry of the two legs it suffices to treat (1, b), so ψ₂ = φ∘ψ₁ with deg φ = b ≥ 2. Write n = deg ψ₁.

**Step 1. The odd locus Ω.**

- For each basis character χ put F_χ = (q_χ∘φ)/q_χ, a function on R.
- By (K), q_χ(ψ₁)/q_χ(ψ₂) = ψ₁*(1/F_χ) is a square in K(E). So at every point of E over a point where F_χ has odd order, ψ₁ has even local degree.
- Let Ω be the union over χ of the odd-order loci of F_χ.
- Riemann–Hurwitz for ψ₁ gives (n/2)|Ω| ≤ 2n + 2g − 2. So **|Ω| ≤ 4 + 4(g − 1)/n ≤ 4** (and ≤ 3 if g = 0).

**Step 2. The shape of Ω.**

- As in E06 §2, div(q_χ) ≡ [B_χ] (mod 2), with ∞ ∈ B_e for k = 8. Pulling back along φ gives div(q_χ∘φ) ≡ φ*[B_χ] (mod 2).
- So x ∈ R lies in the odd locus of F_χ exactly when the two statements "φ(x) ∈ B_χ and the local degree e_x(φ) is odd" and "x ∈ B_χ" have different truth values.
- Define:
  - o(y) = the number of points of φ⁻¹(y) with odd local degree, and Σo = Σ_{y∈B} o(y);
  - j = the number of x ∈ B with e_x odd and φ(x) ∈ B carrying the same label as x;
  - h = the number of x ∈ B with e_x odd and φ(x) ∈ B carrying a different label.
- Then **|Ω| = Σo + |B| − 2j − h**. Indeed, Ω is the union of the odd-degree points over B and the points of B, minus the j label-matched points. The two sets overlap in exactly the j + h points of B that are odd-degree points over B.

**Step 3. Riemann–Hurwitz for φ.**

- Over y ∈ B, every point of even local degree has e ≥ 2. So the ramification of φ over y is at least (b − o(y))/2.
- The total ramification of φ is 2b − 2. Hence Σ_{y∈B} (b − o(y))/2 ≤ 2b − 2, i.e. **Σo ≥ (|B| − 4)·b + 4**.

**Step 4. The bound on b.**

- From Steps 1–3: 2j + h = Σo + |B| − |Ω| ≥ (|B| − 4)b + |B|.
- Also 2j + h ≤ j + |B| ≤ 2|B|. Hence (|B| − 4)b ≤ |B|.
- So **b ≤ 3 for k = 8, and b ≤ 2 for k = 4.**
- The remaining cases are pinned down further:
  - **k = 8, b = 2:** 2j + h ≥ Σo + 2 ≥ 10, so at least five points of B land in B.
  - **k = 8, b = 3:** 2j + h ≥ Σo + 2 ≥ 12, so j = 6, h = 0 and Σo = 10.
    - All six points of B land label-preservingly in B.
    - Σo = 10 means that exactly four values y ∈ B have o(y) = 1. Their ramification is then at least 4 = 2b − 2, so each fiber has type (2, 1) and φ has no other ramification.
    - So φ has exactly four critical values, all in B, each simple.
  - **k = 4, b = 2:** 2j + h ≥ Σo + 4 ≥ 16, so j = 8: all eight points of B land label-preservingly in B.

**Step 5. Exact enumeration.** Write φ = P/Q with binary forms P, Q of degree b. "φ(x) = y" is a linear condition on the coefficients of P and Q. A solution counts only if P and Q have no common factor ("genuine").

- **Uniqueness for b = 2.** Two genuine degree-2 maps that agree at five points coincide, because P Q′ − P′ Q is a binary quartic with five zeros.
  - So for five prescribed points and images, a genuine solution exists only if the solution space is one-dimensional. If it had dimension ≥ 2 and contained one genuine member, then (coprimality being an open condition) the genuine members would form a nonempty open subset of the projectivized space, i.e. infinitely many distinct maps agreeing at five points. So higher-dimensional kernels are discarded.
- **k = 8, b = 2** (`bidegree/e08_k8_b2.py`, exact in Q(i)):
  - all 6·6⁵ = 46,656 choices of five points of B and their images in B;
  - 26,370 distinct one-dimensional solutions, of which 810 are not genuine;
  - the exact necessary filter 2j + h ≥ 10 leaves 216 genuine maps;
  - all 216 have |Ω| = 8. **None has |Ω| ≤ 4.**
- **k = 8, b = 3** (`bidegree/e08_k8_b3.py`, exact over Q(i) with sympy):
  - all 64 label-preserving assignments of the six points of B;
  - the solution space V has dimension 2 in 60 cases and 3 in 4 cases;
  - in the 4 three-dimensional cases every member has a common factor (checked on the generic member with symbolic parameters), so none is genuine. The script reports this as `DEGENERATE` once for each of the 15 choices of four critical values, hence the count 60 = 4 × 15 in its output; this 60 is unrelated to the 60 two-dimensional kernels;
  - in the 60 two-dimensional cases, the condition "branch form ∝ product of four chosen points of B" (15 choices) has no genuine solution. The discriminant condition only locates candidates; a candidate counts only after a separate coprimality check of P and Q;
  - a positive control finds the known map t(t² + 3)/(3t² + 1).
  - **No map exists.**
- **k = 4, b = 2** (`bidegree/e08_k4_b2.py`, exact over Q(ζ₈)):
  - solve on the first five points, label-preservingly, and check the other three;
  - 1,016 one-dimensional solutions on the first five points; 32 genuine label-preserving maps on all eight points;
  - all have |Ω| = 8. **None has |Ω| ≤ 4.**

So no admissible φ exists for b ≥ 2. □

## 3. What remains

- The open core of MB104 is now: ε > 0, co-image bidegree (a, b) with **a ≥ 2 and b ≥ 2**, and (by E07) interior ramification or one-sided cusp contact.
- For a, b ≥ 2, W is a genuine correspondence on P¹ and is not the graph of a map. The parity method of Steps 1–3 needs the normalization V₀ of W and its two projections. This is the next question; nothing is claimed here.
- The bound d ≤ 8(a + b) of E06 (A) still holds.

## 4. Reproduction

From the repository root:

```
python -I -O stages/stage32/32-03-multibranch/MB104/route-E/bidegree/e08_k8_b2.py
python -I -O stages/stage32/32-03-multibranch/MB104/route-E/bidegree/e08_k8_b3.py
python -I -O stages/stage32/32-03-multibranch/MB104/route-E/bidegree/e08_k4_b2.py
```

Each ends with `PASS`, exit code 0. All checks are fail-closed against the exact counts above. Measured runtimes depend on the machine and load: about 2–7, 6–12 and 15–31 minutes respectively.

## 5. Audit points

1. Step 1: (K) applied to ψ₂ = φ∘ψ₁, and the Riemann–Hurwitz bound |Ω| ≤ 4.
2. Step 2: the odd-locus description, with ∞ ∈ B_e, and the identity |Ω| = Σo + |B| − 2j − h.
3. Step 3: Σo ≥ (|B| − 4)b + 4.
4. Step 4: the bound on b, and the fiber-type analysis for k = 8, b = 3.
5. Step 5: the uniqueness lemma for b = 2, the treatment of non-genuine solutions, and the completeness of the enumeration (the fields used contain B).
6. Scope: the theorem needs k ∈ {4, 8}. It does not cover bidegrees with a, b ≥ 2.

## 6. Audit history

- **Round 1** (two auditors, head 5e199e66): PASS on the mathematics, no must-fix.
  - Auditor A (Claude, executing from the repository root): all three scripts PASS, exit 0; Steps 1–4 re-derived by hand; encoding of the scripts read and checked.
  - Auditor B: independent exact enumerator over Q(ζ₈) for k = 4, b = 2 (1,016 one-dimensional kernels, 32 maps, all |Ω| = 8), and reproductions of the k = 8 scripts (from reconstructed copies, not byte-identical, so not a source-locked run).
  - Should-fixes applied: the `DEGENERATE` 60 count explained; the reason for discarding higher-dimensional kernels stated; the role of the discriminant vs the coprimality check stated; runtimes given as ranges.
  - Not yet done: an independent re-implementation of the k = 8 enumerations.
