# 32R-91 — 32-03 theory start: our model is E10; Problem W; a small lemma; literature (2026-11-07)

Zero credit, working note (no unibranch assumption).

## 1. Our Kummer model is route-E E10 §1 (audited)
- 32R-88 §3 / 32R-90 §1 (k(B) = k(s1,s2)(√(s1s2), √((s1²−1)(s2²−1)), √((s1²+1)(s2²+1)))) is E10 §1:
  K(E) = K(V₀)(√h_a, √h_b, √h_e), h_χ = q_χ(p₁)q_χ(p₂), q_a = 1 + t², q_b = 1 − t², q_e = t (audit round 2 PASS).
  Our coordinates differ by a scaling of t (cusps {0, ∞, ±1, ±i} in both).
- New in 32R-88/90 only: the explicit formulas on B ⊂ P⁶ (s1, s2, w1, w2, w3 and the inverse map) and the reading of
  E04's 80 curves as graphs of the 16 octahedral rotations of order ≠ 3 (consistent with E04/E06/E07).
- The plane-curve conditions of 32R-90 §2 are E10 §2 (RH equality 2g − 2 = δ(2γ − 2) + (δ/2)|Ω|).

## 2. The open core (status map §3, E05–E11)
- ε > 0, co-image W ⊂ P¹×P¹ of bidegree (a, b) with a, b ≥ 2 (E06, E08), not covered by E07's hypotheses.
- k = 8: Problem W (E10 §5). Finite only at slack 0 (E11: (2,2), (2,3), (3,3) numerically excluded). For slack ≥ 1
  the maps move in families. k = 4, γ = 1, and genus 0 are not reformulated yet.

## 3. A small lemma (sharpens E10 §2)
**Lemma.** O_i \ Ω ⊆ J (J = label-matched points of O₁ ∩ O₂). Hence j ≥ max(|O₁|, |O₂|) − |Ω|.
*Proof.* v ∈ O₁ with label χ means "p₁(v) ∈ B_χ with odd local degree". If v ∉ Ω, the statement for p₂ and the same
χ is also true, so v ∈ O₂ with the same label. □
- g = 1, γ = 0 (|Ω| = 4): j ≥ max(2a + 2s₁, 2b + 2s₂) (E10 had j ≥ a + b). g = 0: j ≥ 2·max(a + s₁, b + s₂) + 1.
- Use: pruning of slack-0 searches (E11 used j ≥ 5 for (2,3); the lemma gives j ≥ 6). It does not bound a + b:
  intersecting W with the four Klein graphs (each through 6 of the 12 label-matched points, each such point on two of
  them) only gives Σ_{v∈J} min(e₁, e₂) ≤ 2(a + b).

## 4. Literature
- Bakker–Tsimerman, *p-torsion monodromy representations of elliptic curves over geometric function fields*, Ann. of
  Math. 184 (2016), arXiv:1403.7168: over a base curve of gonality < N, two non-isotrivial elliptic families with
  isomorphic p-torsion local systems are isogenous for primes p > M_N. M_N is not explicit; p is prime; the method is
  Riemann–Hurwitz against volume/multiplicity bounds (Hwang–To) using the injectivity radius ≈ 2 log p of X(p).
  Our problem is the level-8, (Z/2)³-twisted, genus ≤ 1 case of exactly this question ("function-field Frey–Mazur").
  The theorem does not cover it (level 8 is small and not prime); the method is the family of E09.
- Chen, *Families of elliptic curves with the same mod 8 representations*, arXiv:1405.6385: twists X_E^r(8) (genus 5),
  infinitely many non-isogenous 8-congruent pairs over Q. Pointwise, not one-parameter families.
- Kani–Schanz, *Modular diagonal quotient surfaces*, Math. Z. 227 (1998): Enriques–Kodaira type of Z_{N,ε}
  (general type iff p_g ≥ 3). The N = 8 row was not read (PDF text not extractable here).

## 5. Assessment
- The full 32-03 exclusion (equivalently the target theorem "genus ≤ 1 ⇒ fibre curve or one of the 16 graphs") is a
  small-level case of the function-field Frey–Mazur question. General methods are ineffective at small level; no
  published classification for level 8 was found.
- Concrete steps that are finite: (a) certify E11 exactly; (b) slack-0 searches for larger bidegrees with the lemma's
  pruning. Neither closes slack ≥ 1.
- A closing argument needs a new idea for slack ≥ 1 (families of almost-orbifold coverings with matching), e.g. a
  rigidity statement: the matching conditions cut every positive-dimensional Hurwitz family to finitely many members,
  and those have bounded degree.
