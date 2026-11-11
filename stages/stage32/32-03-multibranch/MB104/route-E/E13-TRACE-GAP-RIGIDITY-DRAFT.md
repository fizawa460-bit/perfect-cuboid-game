# E13 (draft) — Trace-gap rigidity: a uniform degree bound for nested slack-0 pairs, and localization of the rest

Status: **draft research note, not audited, zero credit.** Written 2026-11-11 as a continuation of E12 §5 (the open
core). Not registered in `STATE.json`. Scripts: `e13/filt.py`, `e13/traces.py`, `e13/bound.py`.

- It gives a new tool for Problem W (E10 §5): the arithmetic group has a *trace gap*, and the two pulled-back
  hyperbolic structures are exponentially close away from the points where they differ. Together these give exact
  statements.
- **Theorem A:** in the slack-(0, 0) case with O₁ ⊂ O₂ (or O₂ ⊂ O₁), the degree is bounded by an explicit absolute
  constant. This is the first bound in route E that is uniform in the bidegree and is not the equality face.
- **Theorem B:** in every slack-(0, 0) case, W agrees exactly with a Hecke correspondence outside a region of bounded
  size around the points of O₁ Δ O₂, and all four points of Ω lie in that one region.
- It does **not** close the core. Open: the mixed slack-0 types, and positive slack (§6).

Notation as in E10–E12: k = 8, γ = 0, p₁, p₂ : V₀ ≅ P¹ → P¹ of degrees a, b; B = {0, ∞, ±1, ±i};
O_i = points over B with odd local degree; slack s_i; Ω; h = number of label-differing points.

## 0. Setting at slack 0

- Γ₀ := π₁^orb(P¹; 2⁶), the group with C8/G = H/Γ₀. It contains PQ¹_B(2) (E01) with quotient G.
- At slack 0, p_i is an orbifold covering (E10 §5, E11 Lemma 1). So X_i := (V₀; O_i) = H/Λ_i with Λ_i a subgroup of
  index deg p_i in a conjugate of Γ₀, and |O_i| = 2·deg p_i + 4.
- X₁ and X₂ have the same underlying Riemann surface V₀. They differ only in the cone points:
  |O₁ Δ O₂| = |Ω| − h ∈ {0, 2, 4} (from E10 §2: |Ω| = Σo₁ + Σo₂ − 2j − h and |O₁ ∩ O₂| = j + h).
- **Types.** (m₁, m₂) := (|O₁ ∖ O₂|, |O₂ ∖ O₁|), with b − a = (m₂ − m₁)/2.
  - (0, 0): both legs étale, the equality face (E03/E04). This also settles the case left open in E11 §5.
  - *nested*: (2, 0), (0, 2), (4, 0), (0, 4);
  - *mixed*: (1, 1), (2, 2), (3, 1), (1, 3).

## 1. Lemma 1 — the arithmetic of Γ₀

Let 𝔓 be the two-sided prime of the Bolza order Q_B over √2 (so 𝔓² = √2·Q_B and 2Q_B = 𝔓⁴), and
PQ¹(𝔓^k) = {x ∈ Q¹ : x ≡ ±1 mod 𝔓^k}/±1.

**(a)** Γ₀ = PQ¹(𝔓²), the Bolza group is PQ¹(𝔓³), and C8 = H/PQ¹(𝔓⁴).

- *Check (`filt.py`, exact, in Q_B/2Q_B):* the image of Q¹ has order 96; the radical filtration has
  |𝔓^k/2Q_B| = 64, 16, 4, 1; the numbers of group elements at level exactly 0, 1, 2, 3, 4 are 64, 24, 4, 3, 1.
  The group has exactly 7 involutions, and they form its only subgroup ≅ (Z/2)³: the level-≥2 subgroup. Its only
  normal subgroup of order 4 is the level-≥3 subgroup.
- G is elementary abelian of order 8 and lies in PQ¹/PQ¹(2): a singular involution is the fourth power of an order-8
  element of Δ(2,3,8), and squares lie in the index-2 subgroup Δ(3,3,4) = PQ¹. So G is the level-≥2 subgroup, and the
  free subgroup G₀ (C8/G₀ = Bolza) is the level-≥3 subgroup.
- The four elements at level exactly 2 are the three singular involutions (one orbit) and s_a s_b s_e.

**(b) Trace gap.** If x ∈ Γ₀ has level ≥ 3 (for example a product of two elliptic involutions of Γ₀), then
tr x ∈ ±(2 + 2·Z[√2]) and |σ(tr x)| ≤ 2 for the non-trivial conjugation σ. Hence two such traces with different
absolute values differ in absolute value by **at least 2**.

- *Proof.* x = ±(1 + y) with y ∈ 𝔓³ = √2·𝔓, and trd(𝔓) ⊂ √2·Z[√2], so trd(y) ∈ 2·Z[√2]. D_B is ramified at
  one real place, so |σ(tr x)| ≤ 2. The difference of two absolute values is 2Δ′ with Δ′ ∈ Z[√2] ∖ {0} and
  |σ(Δ′)| ≤ 2. If |Δ′| < 1 then |N(Δ′)| < 2, so Δ′ is a unit ±(1 + √2)^k with k ≤ −1, and then |σ(Δ′)| ≥ 1 + √2 > 2.
  So |Δ′| ≥ 1. □
- *Check (`traces.py`):* among 87 elements of Γ₀ (words of length ≤ 9), no conjugate trace exceeds 2; the 16
  involutions found are all at level 2; the traces of products of two involutions start 2 + 2√2, 6 + 4√2, 10 + 6√2, …;
  the smallest gap seen is 2.
- Consequence: two distinct order-2 points of Γ₀ are at distance ≥ ℓ_min := arccosh(1 + √2) ≈ 1.5286.

**(c) Level is conjugation-invariant.** If x ∈ Γ₀, g ∈ D_B^× and g x g⁻¹ ∈ Γ₀, then x and g x g⁻¹ have the same level.

- *Proof.* 𝔓^k = {y ∈ Q_B : w(y) ≥ k} for the valuation w of the division algebra D_B ⊗ K_{√2}, and
  w(g y g⁻¹) = w(y). □
- In particular the parity character θ : Γ₀ → Γ₀/PQ¹(𝔓³) = Z/2 (θ = 1 on every elliptic involution) satisfies
  θ(g x g⁻¹) = θ(x).

## 2. Lemma 2 — two-point Schwarz–Pick on a disc

Let D ⊂ H be the hyperbolic disc of radius R about c, and F : D → H holomorphic. For x ∈ D at distance ℓ < R from c,

  2cosh d(F(c), F(x)) ≤ 2cosh ℓ + 2·sinh²ℓ / (cosh R − cosh ℓ).

*Proof.* Schwarz–Pick for the Poincaré metric of D: d(Fc, Fx) ≤ d_D(c, x) = 2·artanh(tanh(ℓ/2)/tanh(R/2)), and
cosh(2·artanh u) = (1 + u²)/(1 − u²). □

## 3. Theorem A — nested slack-0 pairs have bounded degree

**Theorem A.** Let s₁ = s₂ = 0 and O₁ ⊊ O₂. Put R(ℓ) := arccosh(cosh ℓ + sinh²ℓ). Then:

1. for any two distinct lifts c̃, c̃′ ∈ H of cone points of X₁, at distance ℓ, some lift of a point of O₂ ∖ O₁ lies
   within distance R(ℓ) of c̃;
2. consequently a is bounded by an absolute constant. A non-optimized count gives a ≤ 5,863 (a ≤ 2,928 when
   |O₂ ∖ O₁| = 2).

*Proof of 1.*

- The identity of V₀ is an orbifold map X₂ → X₁ (it forgets the cone points O₂ ∖ O₁). It lifts to a holomorphic
  G : H → H, equivariant for a surjection π : Λ₂ → Λ₁. G is the quotient by the normal closure of the involutions at
  O₂ ∖ O₁; it is branched exactly over the lifts 𝒬 of O₂ ∖ O₁, and it is not an isometry.
- Let D be the disc of radius R about c̃, with R > ℓ, and suppose D ∩ 𝒬 = ∅. Then G has a holomorphic section
  F : D → H. The points ĉ = F(c̃), ĉ′ = F(c̃′) are fixed points of involutions ε, ε′ ∈ Λ₂, and π(ε), π(ε′) are the
  involutions of Λ₁ at c̃, c̃′.
- T₂ := |tr(εε′)| = 2cosh d(ĉ, ĉ′) and T₁ := |tr(π(ε)π(ε′))| = 2cosh ℓ. Both are traces of products of two
  involutions in conjugates of Γ₀.
- G is a strict contraction (Schwarz–Pick, G not an automorphism), so ℓ = d(Gĉ, Gĉ′) < d(ĉ, ĉ′), i.e. T₁ < T₂.
  By Lemma 1(b), T₂ ≥ T₁ + 2.
- By Lemma 2 applied to F, T₂ ≤ T₁ + 2·sinh²ℓ/(cosh R − cosh ℓ).
- So cosh R ≤ cosh ℓ + sinh²ℓ, i.e. R ≤ R(ℓ). □

*Proof of 2.* Fix ℓ* with cosh(ℓ*/2) > 2. Call a cone point of X₁ *isolated* if no other lift of a cone point is
within ℓ* of one of its lifts.

- Isolated cone points have disjoint embedded cone-discs of radius ℓ*/2, each of area π(cosh(ℓ*/2) − 1), inside X₁
  of area 2πa. So there are at most 2a/(cosh(ℓ*/2) − 1) of them.
- By part 1, a non-isolated cone point is within R(ℓ*) of a point of O₂ ∖ O₁. The cone points of X₁ are ≥ ℓ_min apart
  (Lemma 1), so at most N := (cosh(R(ℓ*) + ℓ_min/2) − 1)/(cosh(ℓ_min/2) − 1) of them lie within R(ℓ*) of a given point.
- Hence 2a + 4 ≤ 2a/(cosh(ℓ*/2) − 1) + |O₂ ∖ O₁|·N. With ℓ* = 3.045: R(ℓ*) ≈ 5.48, N ≈ 840 (`bound.py`). □

Remarks.

- No label, no Ω and no genus condition is used: the statement is about two finite-index subgroups of Γ₀ whose
  quotients become isomorphic after forgetting cone points of one of them.
- The constant is crude (packing bound, one threshold). Using the exact distance spectrum of the order-2 points
  should lower it substantially.
- **Variant A′ (sketch, not checked in detail).** If only p₂ has slack 0 and O₁ ⊂ O₂, the same G exists
  (G = τ₁ ∘ τ₂⁻¹ is single-valued on H), and the argument gives a ≤ C·(1 + s₁)² with the non-standard ramification
  points of p₁ counted as additional defects. In particular γ = 1 (where O₁ = O₂ always) with one slack-0 leg.

## 4. Theorem B — every slack-0 pair is exactly Hecke outside a bounded region

**Theorem B.** Let s₁ = s₂ = 0 and O₁ ≠ O₂. There is an absolute constant R₀ such that, outside the R₀-neighbourhood
N of O₁ Δ O₂ (in either metric), the following hold on each connected component W of V₀ ∖ N:

1. for cone points c, c′ ∈ W joined by a geodesic of length ≤ ℓ₀ (a fixed threshold), the distances in X₁ and X₂ are
   **equal**;
2. there is g ∈ Comm(Γ₀) = D_B^×/K^× with ρ₂ = g·ρ₁·g⁻¹ on π₁^orb(W) (ρ_i the holonomy of X_i), and the developing maps
   satisfy τ₂(c̃) = g·τ₁(c̃) at every cone point of W;
3. for each boundary circle ∂ of W, the numbers of points of O₁ and of O₂ enclosed by ∂ have the same parity;
4. if δ = 8 and cone points of at least two labels occur in W, then g preserves labels, the label-differing points of
   Ω are not in W, and **all of Ω lies in one component of N**.

*Proof (outline).*

- 1: apply Lemma 2 in both directions (F = τ₂∘τ₁⁻¹ on a disc free of O₂ ∖ O₁, and its analogue for τ₁∘τ₂⁻¹). The two
  traces then differ by less than 2, so they are equal by Lemma 1(b).
- 2: equal pairwise distances for ≥ 3 cone points in a ball determine an isometry g_x with τ₂ = g_x τ₁ on those
  points; overlapping balls give the same g_x, and following F around a loop gives the conjugacy. The subgroup
  ρ₁(π₁^orb(W)) is Zariski dense in Γ₀, so g normalizes the K-algebra it spans, which is D_B; by Skolem–Noether
  g ∈ D_B^×·R^×.
- 3: ρ_i(∂) is the product of the involutions at the enclosed points of O_i. The two products are conjugate by g,
  so they have the same parity by Lemma 1(c).
- 4: conjugation by g acts on G through a fixed automorphism; matched points force it to be the identity once two
  labels occur. Then the product of the G-classes around each boundary circle agrees, i.e. the (Z/2)³-cover E → V₀ is
  unramified around each component of N; for δ = 8 this forces a single component. □

Consequence: on W the curve W ⊂ P¹×P¹ is carried, by a conformal map φ of W that fixes every cone point and is
exponentially close to the identity, onto an open piece of the Hecke correspondence T_g. So a mixed slack-0 solution
of large degree is "a Hecke correspondence modified inside one region containing a bounded number of cone points".

## 5. What is proved, and at what level

- Lemma 1(a): verified by exact computation (`filt.py`); the identification of G uses the uniqueness of (Z/2)³.
- Lemma 1(b), (c), Lemma 2, Theorem A part 1: complete proofs above. Theorem A part 2: the counting is elementary;
  the numerical constant is from `bound.py` and is not optimized.
- Theorem B and Variant A′: outlines. The steps "overlapping balls give the same g" and "Zariski dense" need to be
  written out, and R₀, ℓ₀ made explicit.
- Nothing here is audited. No exclusion is claimed below the bound of Theorem A: a finite search for a ≤ 5,863 is
  not feasible by the methods of E11/E12 as they stand.

## 6. What remains open

1. **Mixed slack-0 types** (1, 1), (2, 2), (3, 1), (1, 3). There is no global contraction between X₁ and X₂, so only
   Theorem B applies. The remaining question is local-to-global: can a region with boundedly many cone points be
   replaced so that the result is conformally the same surface with one cone point moved?
   - A reduction that may help: on the double cover of V₀ branched at O₁ Δ O₂ the two maps have the *same* odd set
     and slack (m₂, m₁).
2. **Positive slack.** Every p_i factors as (an arithmetic covering Y_i → P¹(2⁶)) ∘ (a π₁-surjective map
   κ_i : V₀ → Y_i), and s_i > 0 iff deg κ_i ≥ 2. The defect set then has size ≤ 4 + s₁ + s₂, and the method bounds
   the degree only when the slack is small compared with the degree and a strict comparison is available.
3. **k = 4** (Problem W₄): the group is again a subgroup of PQ¹_B, so Lemma 1 should carry over; not checked.
4. Sharpening the constant in Theorem A to a searchable range.

## 7. Audit points

1. Lemma 1(a): G ⊂ PQ¹/PQ¹(2), and the multiplication table of Q_B used in `filt.py` (same relations as E01).
2. Lemma 1(b): trd(𝔓) ⊂ √2·Z[√2] and the unit argument; that both traces in Theorem A are traces of level-≥3
   elements of conjugates of Γ₀.
3. Theorem A: G is a branched covering with branch set 𝒬 (so F exists on D); strictness of T₁ < T₂; the equality
   T₁ = 2cosh ℓ.
4. Theorem A part 2: the isolation/packing count.
5. Theorem B: every step of the outline.
6. Scope: slack (0, 0) only for Theorems A and B; k = 8, γ = 0.

## 8. Reproduction

From the repository root:

```
python3 -I stages/stage32/32-03-multibranch/MB104/route-E/e13/filt.py
python3 -I stages/stage32/32-03-multibranch/MB104/route-E/e13/traces.py 9
python3 -I stages/stage32/32-03-multibranch/MB104/route-E/e13/bound.py
```

- `filt.py`: exact arithmetic in Q_B/2Q_B (Lemma 1(a)); a few seconds.
- `traces.py 9`: exact arithmetic over Z[√2] on words of length ≤ 9 in α^{±1}, β^{±1} (Lemma 1(b) check; a finite
  sample, not a proof); a few seconds.
- `bound.py`: the numerical constants of Theorem A part 2 (floating point).

## 9. History

- 2026-11-11: draft written (Claude). A first reading check by another reviewer reproduced Lemma 1, Lemma 2 and
  Theorem A; Theorem B was confirmed to be an outline only.
- PR #1868 (another session) is not a verification of this draft: it does not contain the draft, and its
  "12 involutions model" and "trace exclusion of a bad subset" are not valid arguments (there are infinitely many
  order-2 points; every involution has reduced trace 0). Nothing from it is used here.
