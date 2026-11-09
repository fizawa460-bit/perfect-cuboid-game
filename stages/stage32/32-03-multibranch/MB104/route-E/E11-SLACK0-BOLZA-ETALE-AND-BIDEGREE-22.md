# E11 — Problem W at slack 0: étale covers of the Bolza curve, the link to E07, and bidegrees (2, 2), (2, 3), (3, 3) (2026-11-03)

Status: research note, **reading audit round 1 (2026-11-07, two auditors): Lemmas 1–3, the search reductions and the
search sizes PASS; the exclusions of §4 and §4b were numerically verified (revision 2, §8). Revision 3 (2026-11-09,
§9): exact certificates for §4 and §4b (exact number-field arithmetic for (2, 2); finite-field exhaustion with a
characteristic-zero lifting argument for (2, 3), (3, 3)), re-run locally; reading + executing audit by Claude PASS
(slack0/exact-20261109/AUDIT-CLAUDE-20261109.md)**, zero credit.

- It builds on E10 (audit round 2 PASS), whose §5 states that Problem W is a finite search exactly at slack 0.
- It gives three things:
  - a structural description of slack 0 (§1–§2);
  - a translation of E07's hypotheses at slack 0 (§3);
  - **numerically verified** exclusions in Problem W for bidegrees (2, 2), (2, 3) and (3, 3) with both slacks 0
    (§4, §4b). Coincidences of points are decided in floating point with a large separation gap; exact (algebraic or
    interval) certification is pending, so these are not yet theorems.

Setting and notation as in E10:

- k = 8, R = P¹_t, B = {0, ∞, ±1, ±i}, with B_a = {±i}, B_b = {±1}, B_e = {0, ∞};
- the co-image W ⊂ P¹×P¹ has rational normalization V₀ (γ = 0), with p₁, p₂ : V₀ → P¹ of degrees a and b, and (p₁, p₂) : V₀ → W birational;
- O_i = {v : p_i(v) ∈ B with odd local degree};
- slack s_i = (|O_i| − 2·deg p_i − 4)/2;
- P_i := p_i⁻¹(B) as a set.

## 1. Slack 0: ramification over B, of index 2

**Lemma 1.** s_i = 0 holds iff every ramification point of p_i lies over B with local degree 2. Then O_i is the set of points over B with local degree 1, |O_i| = 2·deg p_i + 4 and |P_i| = 4·deg p_i + 2.

*Proof.*

- Put n = deg p_i, and let o(y) be the number of odd-degree points over y.
- Over y ∈ B the ramification is at least (n − o(y))/2. Summing gives at least (6n − |O_i|)/2 = 2n − 2 − s_i.
- The total ramification is 2n − 2. So the ramification outside B (plus any excess over B) is at most s_i.
- At s_i = 0 equality holds fibrewise: points of even degree have degree 2, points of odd degree have degree 1, and there is nothing outside B.
- |P_i| = Σ_y (o(y) + (n − o(y))/2) = (|O_i| + 6n)/2. □

This is the finiteness statement of E10 §5: for fixed n, slack-0 maps are finitely many up to Möbius maps of the source (Riemann existence, fixed branch data).

## 2. Slack 0 as an étale cover of the Bolza curve

Let H : y² = r(t) with r = t(t⁴ − 1) be the Bolza curve. Its six Weierstrass points are exactly B; ∞ is a branch point because deg r = 5 is odd. Let V′_i be the normalization of V₀ ×_{P¹} H via p_i.

**Lemma 2.** V′_i → V₀ is the double cover branched exactly at O_i, and V′_i has genus deg p_i + 1 + s_i. The induced degree-n map V′_i → H is **étale iff s_i = 0**.

*Proof.*

- ord_v(r∘p_i) = e_v(p_i)·ord_{p_i(v)}(r).
- This is odd exactly when p_i(v) ∈ B (r has simple zeros at 0, ±1, ±i, and a pole of order 5 at ∞) and e_v(p_i) is odd.
- So the branch locus is O_i, and the genus is (|O_i| − 2)/2 = n + 1 + s_i.
- Riemann–Hurwitz for V′_i → H gives 2(n + 1 + s_i) − 2 = n·2 + R, so R = 2s_i. □

So slack-0 maps of degree n correspond to étale degree-n covers of the Bolza curve compatible with the hyperelliptic involution, with rational quotient.

- The Bolza curve is the quotient C8/G₀ by the free subgroup G₀ (E10 §3).
- It is arithmetic, being uniformized by a subgroup of the (2,3,8) triangle group. This points to a Hecke-type treatment (§5), which is not carried out here.

## 3. E07's hypotheses at slack 0

E07 assumes:

- (i) the legs f_i : Z → X(8) ramify only over cusps;
- (ii) f₁⁻¹(cusps) = f₂⁻¹(cusps).

The cusps are the 24 singular fixed points of G (E07 §0). Their images in R form B.

**Lemma 3** (k = 8, γ = 0, s₁ = s₂ = 0).

- (i) holds iff Ω ⊆ P₁ ∩ P₂.
- (ii) holds iff P₁ = P₂. In particular (ii) forces a = b, by Lemma 1.

*Proof.*

- Let z ∈ Z, with images x = π(z) ∈ E and v = ρ(x) ∈ V₀. Here E = Z/G and ρ : E → V₀ is branched exactly over Ω with index 2 (E10 §2).
- A nontrivial g ∈ G fixing z fixes f₁(z) and f₂(z). So π : Z → E is unramified at every z with f_i(z) not a cusp.
- C8 → R is branched exactly at the cusps. So for f_i(z) not a cusp: e_z(f_i) = e_x(ψ_i) = e_x(ρ)·e_v(p_i).
- f_i(z) is not a cusp iff p_i(v) ∉ B. There e_v(p_i) = 1 by Lemma 1.
- So f_i is ramified at z iff v ∈ Ω. Hence (i) ⇔ no point of Ω lies outside P₁ ∩ P₂.
- (ii) says that f₁(z) is a cusp iff f₂(z) is, i.e. p₁(v) ∈ B ⇔ p₂(v) ∈ B. □

**Corollary.**

- By E07, a slack-0 solution with Ω ⊆ P₁ ∩ P₂ and P₁ = P₂ is one of the 80 curves of E04, so ε = 0.
- A slack-0 MB104 carrier therefore has an Ω-point outside P₁ ∩ P₂ (interior ramification of a leg), or P₁ ≠ P₂ (one-sided cusp contact).

## 4. Bidegree (2, 2) with both slacks 0 (numerically verified; exactly certified in §9)

**Proposition (numerically verified; exact certification pending).** There is no k = 8, γ = 0 configuration (g ≤ 1) whose co-image W has bidegree (2, 2) with s₁ = s₂ = 0 and |Ω| ≤ 4.

This uses the necessary conditions of E10 §2: |Ω| = 4 for g = 1 and δ ≥ 2; |Ω| ≤ 3 for g = 0.

*Proof (exact reduction plus enumeration, `slack0/e11_w22.py`).*

1. **The slack-0 maps of degree 2.** These are q = M(t²) whose two critical values y₁, y₂ lie in B. There are 15 choices of {y₁, y₂}. For each choice the map is unique up to source Möbius maps.
2. **Setup.** Take p₁ = q_i for a fixed representative, and p₂ = q_j∘T with T a Möbius map.
   - |O₁| = |O₂| = 8. The identity |Ω| = 16 − 2j − h and |Ω| ≤ 4 give 2j + h ≥ 12.
   - h ≤ |Ω| (E10 §2) gives j ≥ 4.
   - So T maps a label-matched triple of O₁ into O_{q_j}, with the same labels. A triple determines T.
   - All (i, j, triple, image triple) are enumerated: 157,824 Möbius maps T.
3. **Birationality.** (p₁, p₂) : V₀ → W is birational unless p₁ and p₂ factor through a common degree-2 map. Since p₁ = q_i, this means p₂ is invariant under the deck involution t ↦ −t of q_i. In that case W = (p₁, p₂)(V₀) has bidegree (1, 1); that case is E06.
4. **Result.**
   - 57 configurations with |Ω| ≤ 4 (distinct after rounding the coordinates of T, i.e. distinct as numerical keys;
     this count is a diagnostic, not a count of exact equivalence classes). All are non-birational, i.e. bidegree
     (1, 1), by the numerical test of item 3.
   - **No birational configuration with |Ω| ≤ 4 was found** (numerical decision of every coincidence, see Numerics).
     □

**Positive control.** For (a, b) = (1, 1) (p₁ = id, p₂ = T; only j ≥ 2 holds, so no label pruning), the same code finds 16 Möbius maps with |Ω| ≤ 4:

- four with |Ω| = 0, the Klein group {t, −t, 1/t, −1/t};
- twelve with |Ω| = 4, for example t ↦ it, the example from the E10 round-1 audit.

**Numerics.**

- Coincidence of points is decided in complex double precision by chordal distance < 10⁻⁸.
- The run checks a separation gap. Every accepted coincidence has distance < 10⁻¹¹ (measured 7.6·10⁻¹⁵). Every non-coincidence has distance > 10⁻⁴ (measured 1.8·10⁻³).
- This is a numerical separation diagnostic with a gap of about 11 orders of magnitude, not a certificate: the errors
  of the computed points against their exact algebraic values are not bounded rigorously, and the root lists and local
  multiplicities that define O_i are also obtained numerically.

## 4b. Bidegrees (2, 3) and (3, 3) with both slacks 0 (numerically verified; exactly certified in §9)

**Proposition (numerically verified; exact certification pending).** There is no k = 8, γ = 0 configuration (g ≤ 1) whose co-image W has bidegree (2, 3), (3, 2) or (3, 3) with s₁ = s₂ = 0 and |Ω| ≤ 4.

(3, 2) is (2, 3) with the legs swapped.

*Proof (`slack0/e11_slack0_small.py`, about 4 minutes).*

1. **The slack-0 maps of degree 3.**
   - By Lemma 1, they have exactly four simple critical points, with distinct critical values y₁, …, y₄ ∈ B. There are 15 choices of the four values.
   - Normalize the critical points over y₁, y₂, y₃ to 0, ∞, 1, and let λ be the critical point over y₄. The conditions "p(c) = y, p′(c) = 0" are linear in the coefficients of P and Q (p = P/Q). So λ is a root of an 8×8 determinant D(λ), computed exactly over Q(i).
   - In every case D has degree 4 after removing the spurious roots λ = 0, 1. Each of the 4 roots gives a one-dimensional kernel and a genuine cubic (nonzero resultant).
   - Total 15 × 4 = **60 maps**. This matches the Hurwitz number 4 for degree-3 covers of P¹ with four simple branch points. Each cover is counted once, because the critical points are labelled by their distinct critical values.
2. **Search**, as in §4 but in homogeneous coordinates and vectorized:
   - **(2, 3):** |O| = 8, 10, so j ≥ 5. All (15 × 60 maps, label-matched triples among the first 6 points of O₁) are enumerated: 468,096 maps T. (p₁, p₂) is automatically birational, since gcd(2, 3) = 1.
   - **(3, 3):** |O| = 10, 10, so j ≥ 6. Triples among the first 7 points of O₁ are enumerated: 3,287,808 maps T.
     - Birationality fails exactly when p₂ = M∘p₁ for a Möbius M. This is tested by constancy of p₂ on two generic fibres of p₁. In that case W is of bidegree (1, 1).
3. **Result.**
   - (2, 3): no configuration with |Ω| ≤ 4 was found.
   - (3, 3): every configuration found with |Ω| ≤ 4 is non-birational by the numerical two-fibre test (raw counts
     {0: 8400, 4: 496}). **No birational one was found.** □
   - In exact arithmetic the two-fibre test is valid: if p₂ is constant on two distinct regular fibres of p₁ (degree 3),
     the numerators of p₂ − c₁ and p₂ − c₂ are proportional to those of p₁ − c′₁ and p₁ − c′₂, so p₂ = M∘p₁ for a
     Möbius M (audit round 1). The implementation tests constancy numerically.

**Why only label-matched triples are needed.** If j ≥ 3, at most |O₁| − j points of O₁ are not label-matched coincidences. So any |O₁| − j_min + 3 points of O₁ contain a label-matched coincident triple, which determines T. For (1, 1) only j ≥ 2 holds, so the control runs without label pruning.

**Cross-check.** The new implementation (homogeneous coordinates) reproduces:
- §4 for (2, 2): no birational configuration; non-birational raw counts {0: 4200, 4: 408};
- the (1, 1) control: 16 maps, {0: 4, 4: 12}.

**Numerical separation.**

| Bidegree | Largest accepted coincidence | Smallest rejected distance |
|---|---|---|
| (2, 2) | 1.0·10⁻¹⁴ | 3.7·10⁻³ |
| (2, 3) | 1.2·10⁻¹³ | 1.4·10⁻⁵ |
| (3, 3) | 2.4·10⁻¹² | 1.9·10⁻⁶ |

- The script requires < 10⁻¹⁰ and > 10⁻⁶.
- For (3, 3) the margin is about 6 orders of magnitude, which is the weakest in the table. This is a numerical separation diagnostic, not a certificate (see §4 Numerics).
- The inputs are computed to 50–60 digits; the search itself runs in double precision.

## 5. Open and next

- **Larger bidegrees at slack 0.** E10 §2 gives |a − b| ≤ 2 at slack 0. The next cases are (2, 4), (3, 4), (4, 4), (3, 5), …
  - Degree 4 allows fibres of type (2, 2) over B, so the parametrization of §4b needs extending.
  - A uniform argument, rather than case-by-case search, would need the Hecke direction below.
- **The Hecke direction.** If O₁ = O₂ (the Bolza character in Q), then V′₁ = V′₂ carries two étale maps to H, i.e. an étale correspondence on an arithmetic curve. A commensurator argument as in E01/E07 would make this a Hecke problem. What is missing is a degree bound; in E07 it came from genus(E) ≤ 1.
- **Positive slack** is not addressed (E10 §5: families of dimension up to s).

## 6. Reproduction

```
python -I -O stages/stage32/32-03-multibranch/MB104/route-E/slack0/e11_w22.py
python -I -O stages/stage32/32-03-multibranch/MB104/route-E/slack0/e11_slack0_small.py
```

- The first covers §4 (about 10 seconds). The second is an independent re-implementation covering §4 and §4b (about 4 minutes).
- Both end with `PASS`, exit code 0. The second checks the expected counts {(1,1): 2400 maps T and {0: 4, 4: 12}; (2,2): 98,352; (2,3): 468,096; (3,3): 3,287,808}, the 60 degree-3 maps and the numerical gap.
- The first fails closed against the expected counts: 15 maps, the control {0: 4, 4: 12}, 157,824 maps T, 57 non-birational configurations, 0 birational ones, and the numerical gap.

## 7. Audit points

1. Lemma 1 and Lemma 2. Lemma 1 restates the slack bookkeeping of E10 §5 (audited); Lemma 2 adds the branch behaviour at ∞.
2. Lemma 3: π : Z → E is unramified over non-cusps, and the translation of E07 (i) and (ii).
3. §4 and §4b:
   - completeness of the 60 degree-3 maps (determinant method, Hurwitz number 4);
   - the birationality test for (3, 3);
   - completeness of the 15 degree-2 maps;
   - the reduction to label-matched triples (j ≥ 4);
   - the birationality criterion;
   - the numerical gap argument.
4. Scope:
   - §4 and §4b cover only (2, 2), (2, 3), (3, 2) and (3, 3) with both slacks 0, and are numerically verified only;
   - nothing is claimed for positive slack or larger bidegrees;
   - no credit.

## 8. Audit history and what certification needs

- **Round 1 (2026-11-07), reading audit, two auditors (ChatGPT, DeepSeek).** Both HOLD.
  - PASS: Lemmas 1–3 (Riemann–Hurwitz, the treatment of ∞, the translation of E07), the 15 degree-2 maps, the
    reduction to label-matched triples (j ≥ 4, 5, 6), the birationality criteria, the use of E10 §2. DeepSeek
    recounted the search sizes 157,824 / 98,352 / 468,096 / 3,287,808 independently: all agree.
  - **Must-fix (DeepSeek E11-1): numerical decisions do not certify exact nonexistence.** Answered by revision 2: §4
    and §4b are now stated as numerically verified, not as theorems. No counterexample was reported.
  - Should-fix (E11-5, E11-6, ChatGPT): the meaning of "57 distinct" and the term "certificate" are corrected above.
- **Open certification items (needed only to turn §4 / §4b into theorems):**
  1. the 60 degree-3 maps: for each of the 15 value sets, the four non-spurious roots of D(λ) are distinct, each has a
     one-dimensional kernel and gives a cubic with nonzero resultant (exact, in Q(i)[λ]/(D)) (E11-2);
  2. the root lists and local multiplicities defining O_i, by exact gcds / discriminants or certified root disks
     (E11-4);
  3. non-coincidences by certified enclosures (disjoint balls), so that every rejected T has certified |Ω| ≥ 5;
  4. for every accepted configuration, the identity p₂ = M∘p₁ (or q_j∘T invariant under t ↦ −t) proved exactly
     (E11-3).

## 9. Exact certification (revision 3, 2026-11-09)

Files: `slack0/exact-20261109/` (README there). Computed by ChatGPT on the user's request, re-run locally by Claude
with identical results. Audit: Claude, reading + executing, PASS, no must-fix (`AUDIT-CLAUDE-20261109.md`).

- **(2, 2)** (`w22/`): the 15 degree-2 maps; all odd points in K = Q(√2, √(−1+i)), [K : Q] = 8; every coincidence
  decided exactly in K. All |Ω| ≤ 4 configurations have a relative Möbius map commuting with t ↦ −t (diagonal or
  antidiagonal), hence are non-birational. This answers certification items 2–4 of §8 for §4.
- **Degree-3 maps** (`w22/degree3_enumeration.py`): every slack-0 cubic is N⁻¹∘F_k with
  F_k(t) = t²((2k − 1)t + 2 − 3k)/(t − k) and H_z(k) = k(3k − 2)³ − z(2k − 1) = 0; for all 15 value sets H_z has degree
  4, simple roots and no spurious root; 60 maps. This answers item 1.
- **(2, 3), (3, 3)** (`w23_33/`, PROOF.md): at p = 874009 all 75 covers and their odd points split with distinct
  simple reductions (disc_k H_z = −2⁴3⁹z²(z − 1)²). The three-point alignment over F_p is exhaustive (j ≥ 6 by
  O_i \ Ω ⊆ J, E12 Lemma 0), and every characteristic-zero candidate reduces to an F_p-candidate with no larger |Ω|.
  (2, 3): no candidate. (3, 3): 8,896 candidate occurrences, each of the form q̄∘M̄ = Ū∘f̄ with Ū ∈ Aut(B); the
  identity lifts to characteristic 0 (Hensel uniqueness of the normal-form parameter and of the marked simple points),
  so every candidate is non-birational. This answers items 2–4 for §4b without certified root disks.
- Consequence: **§4 and §4b hold exactly**: Problem W has no
  solution of bidegree (2, 2), (2, 3), (3, 2), (3, 3) with both slacks 0.
