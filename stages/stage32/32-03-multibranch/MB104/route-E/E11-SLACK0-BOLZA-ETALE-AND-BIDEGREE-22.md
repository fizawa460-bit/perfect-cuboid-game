# E11 — Problem W at slack 0: étale covers of the Bolza curve, the link to E07, and bidegrees (2, 2), (2, 3), (3, 3) (2026-11-03)

Status: research note, **unaudited, zero credit**.

- It builds on E10 (audit round 2 PASS), whose §5 states that Problem W is a finite search exactly at slack 0.
- It gives three things:
  - a structural description of slack 0 (§1–§2);
  - a translation of E07's hypotheses at slack 0 (§3);
  - exclusions in Problem W for bidegrees (2, 2), (2, 3) and (3, 3) with both slacks 0 (§4, §4b).

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

## 4. Bidegree (2, 2) with both slacks 0 does not occur

**Proposition.** There is no k = 8, γ = 0 configuration (g ≤ 1) whose co-image W has bidegree (2, 2) with s₁ = s₂ = 0 and |Ω| ≤ 4.

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
   - 57 distinct configurations have |Ω| ≤ 4. All are non-birational, i.e. bidegree (1, 1).
   - **No birational configuration has |Ω| ≤ 4.** □

**Positive control.** For (a, b) = (1, 1) (p₁ = id, p₂ = T; only j ≥ 2 holds, so no label pruning), the same code finds 16 Möbius maps with |Ω| ≤ 4:

- four with |Ω| = 0, the Klein group {t, −t, 1/t, −1/t};
- twelve with |Ω| = 4, for example t ↦ it, the example from the E10 round-1 audit.

**Numerics.**

- Coincidence of points is decided in complex double precision by chordal distance < 10⁻⁸.
- The run checks a separation gap. Every accepted coincidence has distance < 10⁻¹¹ (measured 7.6·10⁻¹⁵). Every non-coincidence has distance > 10⁻⁴ (measured 1.8·10⁻³).
- This is a numerical certificate with a gap of about 11 orders of magnitude, not interval arithmetic.

## 4b. Bidegrees (2, 3) and (3, 3) with both slacks 0 do not occur

**Proposition.** There is no k = 8, γ = 0 configuration (g ≤ 1) whose co-image W has bidegree (2, 3), (3, 2) or (3, 3) with s₁ = s₂ = 0 and |Ω| ≤ 4.

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
   - (2, 3): no configuration with |Ω| ≤ 4.
   - (3, 3): every configuration with |Ω| ≤ 4 is non-birational (raw counts {0: 8400, 4: 496}). **None is birational.** □

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
- For (3, 3) the margin is about 6 orders of magnitude, which is the weakest in the table. This is a numerical certificate, not interval arithmetic.
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
   - §4 and §4b cover only (2, 2), (2, 3), (3, 2) and (3, 3) with both slacks 0;
   - nothing is claimed for positive slack or larger bidegrees;
   - no credit.
