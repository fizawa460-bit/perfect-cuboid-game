# E13 (draft) — Trace-gap rigidity: a uniform degree bound for nested slack-0 pairs, and localization of the rest

Status: **draft research note, not audited, zero credit.** Written 2026-11-11 as a continuation of E12 §5 (the open
core). Not registered in `STATE.json`. Scripts: `e13/filt.py`, `e13/traces.py`, `e13/bound.py`.

- It gives a new tool for Problem W (E10 §5): the arithmetic group has a *trace gap*, and the two pulled-back
  hyperbolic structures are exponentially close away from the points where they differ. Together these give exact
  statements.
- **Theorem A:** in the slack-(0, 0) case with O₁ ⊂ O₂ (or O₂ ⊂ O₁), the degree is bounded by an explicit absolute
  constant. This is the first bound in route E that is uniform in the bidegree and is not the equality face.
- **Theorem B** (complete proof, revision 3): in every slack-(0, 0) case, each non-collinear cluster of common cone
  points far from O₁ Δ O₂ (distance ≥ 10.78) determines a commensurator element g with ρ₂ = gρ₁g⁻¹ on the cluster
  group and the second leg equal to g∘(first leg) at the cone points; parity and label constraints follow, and for
  δ = 8 all of Ω lies on one side of such a cluster. (Revisions 1–2 said "W agrees exactly with a Hecke
  correspondence"; that was an overstatement and is withdrawn, §4.)
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
- The four elements at level exactly 2 are the three singular involutions (one orbit) and s_a s_b s_e. These four
  form **one coset**: the quotient (level ≥ 2)/(level ≥ 3) = Γ₀/PQ¹(𝔓³) has order 8/4 = 2, not 4. The level-≥3
  subgroup is G₀ = {1, s_a s_b, s_a s_e, s_b s_e}; in particular s_a s_b is free, not the third singular involution.
- Notation: G = Γ₀/PQ¹(𝔓⁴) is the box group of FSM (C8/G = H/Γ₀), identified with the level-≥2 subgroup of
  PQ¹/PQ¹(2). This identification holds because Γ₀ = PQ¹(𝔓²).
- *Cross-check (`e13/check_lemma1.py`):* the multiplication table of Q_B used in `filt.py` / `traces.py` equals the
  table of E01's `bolza_mod2.py` on all 16 basis products.

**(b) Trace gap.** If x ∈ Γ₀ has level ≥ 3, then tr x ∈ ±(2 + 2·Z[√2]) and |σ(tr x)| ≤ 2 for the non-trivial
conjugation σ. Hence two such traces with different absolute values differ in absolute value by **at least 2**.

**(b′) Products of two elliptic involutions have level ≥ 3.** Let ε, ε′ be elliptic elements of order 2 of Γ₀ (or of
one conjugate hΓ₀h⁻¹, h ∈ PSL₂(R)). Then εε′ has level ≥ 3, so (b) applies to tr(εε′).

- *Proof.* PQ¹(𝔓³) is the Bolza surface group, which is torsion free, so an elliptic element of Γ₀ is not in it:
  ε and ε′ have level exactly 2. Γ₀/PQ¹(𝔓³) has order 2 by (a), so εε′ ∈ PQ¹(𝔓³). For a conjugate hΓ₀h⁻¹ apply this
  to h⁻¹εh, h⁻¹ε′h and use tr(h x h⁻¹) = tr x. □
- *Check (`e13/check_lemma1.py`):* the 16 elliptic involutions found by `traces.py` all have level 2, and all 120
  products of two distinct ones have level 3 (85) or 4 (35).

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

*Proof.* The Poincaré distance of D is d_D(c, x) = 2·artanh(tanh(ℓ/2)/tanh(R/2)), and cosh(2·artanh u) =
(1 + u²)/(1 − u²) gives the **identity** cosh d_D(c, x) = cosh ℓ + sinh²ℓ/(cosh R − cosh ℓ). The inequality comes only
from Schwarz–Pick, d(Fc, Fx) ≤ d_D(c, x). □

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
  By Lemma 1(b′) both εε′ and π(ε)π(ε′) have level ≥ 3, so Lemma 1(b) gives T₂ ≥ T₁ + 2.
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

## 4. Theorem B — anchored clusters are Hecke-rigid (complete proof, revision 3)

*Corrections to the outline of revision 1–2.* (i) The outline said that W "agrees exactly with a Hecke
correspondence" outside a bounded region. That is not what the argument gives and is withdrawn: what holds is
equality at the common cone points and conjugacy of the holonomy on a subgroup (Theorem B (1)–(2)). (ii) The outline
assumed that every region far from O₁ Δ O₂ contains enough cone points. X_i can have large cone-free regions, so the
statements are now made on *anchored clusters*. (iii) The outline did not exclude a mirror-image matching of the cone
points; Lemma B3 does. (iv) "Zariski dense" is replaced by the elementary fact that a quaternion division algebra has no
non-commutative proper subalgebra.

### 4.0 Setting and constants

- s₁ = s₂ = 0 and O₁ ≠ O₂. Put U := V₀ ∖ (O₁ Δ O₂), an orbifold whose cone points are the *anchors*
  A := O₁ ∩ O₂ (order 2). Let Ũ be its universal orbifold cover and π := π₁^orb(U), acting on Ũ.
- U is open in X₁ and in X₂. Let dev_i : Ũ → H be the developing maps and ρ_i : π → Λ_i the holonomies. Since p_i is
  an orbifold covering of H/Γ₀, we normalize so that **Λ_i ⊂ Γ₀**. dev_i is ρ_i-equivariant and is a covering map
  onto H ∖ 𝒬_i, where 𝒬_i is the set of lifts, in the X_i-picture, of the points of O₁ Δ O₂.
- A lift x̃ of an anchor has stabilizer {1, e_x̃} in π, and ρ_i(e_x̃) is an elliptic involution of Γ₀ fixing dev_i(x̃).
- x̃ is **R-deep** if B(dev_i x̃, R) ∩ 𝒬_i = ∅ for i = 1, 2, i.e. the anchor is at distance ≥ R from O₁ Δ O₂ in both
  X₁ and X₂. For R-deep x̃ let s_i : B(dev_i x̃, R) → Ũ be the inverse branch of dev_i with s_i(dev_i x̃) = x̃, and put
  F := dev₂ ∘ s₁ : B(dev₁ x̃, R) → H and G := dev₁ ∘ s₂. Then G ∘ F = id near dev₁ x̃.
- The **L-star** St_L(x̃) is the set of anchor lifts ỹ ≠ x̃ with dev₁ ỹ ∈ B(dev₁ x̃, L) and s₁(dev₁ ỹ) = ỹ (the
  anchors on the sheet of x̃ within L); for those, dev₂ ỹ = F(dev₁ ỹ).
- Constants (all elementary functions; `e13/thmb_constants.py`). For R > L > 0, t := tanh(R/2), u := tanh(L/2):
  - λ(R, L) := t(1 − u²)/(t² − u²) (the largest ratio of the Poincaré metric of B(c, R) to that of H on B(c, L));
  - Δ(R, L) := max(2cosh(2λ₁L) − 2cosh(2L), 2cosh(2λ₂L̂) − 2cosh(2L̂)), with λ₁ = λ(R, L), L̂ = λ₁L, λ₂ = λ(R, L̂);
  - ε(R, L) := 2E/(1 − (u + E)²), where s = u/t, η = 1 − t², E = sη(1 + s)/(1 − s) + u(1 − t)/t;
  - w_min(L) := the least width (min over geodesics L′ of the largest distance of a vertex to L′) of a
    non-degenerate triangle whose sides d₁, d₂ ≤ L and d₃ ≤ 2L all satisfy 2cosh d ∈ 2 + 2Z[√2] with conjugate in
    [−2, 2]. These are finitely many shapes; degeneracy is decided exactly in Q(√2).
  - **Certified width bound (revision 4).** For each shape put p₁ at the origin and n(t, φ) = (sinh t, cosh t cos φ,
    cosh t sin φ); the width is asinh(min_n M(n)), M(n) = max_j |⟨P_j, n⟩|. Since |⟨P₁, n⟩| = |sinh t|, the bound
    M ≥ sinh w holds automatically for |t| ≥ w, and on |t| ≤ w each |⟨P_j, n⟩| is Lipschitz with
    |∂_t| ≤ cosh(d_j + w), |∂_φ| ≤ cosh(w) sinh d_j. A branch-and-bound over the strip |t| ≤ w then proves
    M ≥ sinh w. For L = 3.2 this proves **width ≥ 0.03 for all 2,500 non-degenerate shapes** (`thmb_constants.py 3.2
    0.03`; 160,424 cells; floating point, with margins far above rounding). Negative control: on the thinnest shape
    (numerical width 0.03774) the same procedure proves 0.037 and fails for 0.0385 and 0.040.
  - R_B(L) := the least R with Δ(R, L) < 2 and ε(R, L) < 2·w_min(L).
- Values (`thmb_constants.py`; floating point, the width by numerical minimization):

  | L | sides ≤ L | shapes | degenerate | w_min(L) | R_B(L) | ε(R_B, L) |
  |---|---|---|---|---|---|---|
  | 1.6 | 1 | 7 | 1 | 0.2515 | 5.49 | 0.2567 |
  | 2.0 | 2 | 32 | 2 | 0.1109 | 6.80 | 0.1427 |
  | 2.5 | 4 | 229 | 4 | 0.0834 | 8.46 | 0.0690 |
  | 3.2 | 8 | 2510 | 10 | 0.0377 | 10.78 | 0.0261 |

  In each case Δ < 2 is the binding condition; the width condition then holds with a factor ≥ 2.0 to spare. Theorem B
  uses L = 2ℓ₀; with the smallest admissible ℓ₀ = 1.6 > ℓ_min this is L = 3.2 and **R = 10.78**. There the width
  condition is used only through the certified bound: ε(10.78, 3.2) = 0.0261 < 2 × 0.03.

### 4.1 Lemma B1 — equal distances in a star

Let x̃ be R-deep with Δ(R, L) < 2, and ỹ, z̃ ∈ St_L(x̃) ∪ {x̃} distinct. Then
d(dev₂ ỹ, dev₂ z̃) = d(dev₁ ỹ, dev₁ z̃).

*Proof.* Put c = dev₁ x̃, d₁ = d(dev₁ ỹ, dev₁ z̃) ≤ 2L, d₂ = d(dev₂ ỹ, dev₂ z̃).
- The geodesic from dev₁ ỹ to dev₁ z̃ lies in B(c, L). By Schwarz–Pick for the Poincaré metric of B(c, R) and the
  definition of λ, d₂ = d(F dev₁ ỹ, F dev₁ z̃) ≤ λ₁ d₁. Also F(B(c, L)) ⊂ B(dev₂ x̃, L̂).
- The path s₁([c, dev₁ ỹ]) from x̃ to ỹ is mapped by dev₂ into B(dev₂ x̃, L̂) ⊂ B(dev₂ x̃, R) (Δ < ∞ forces L̂ < R),
  so it is the s₂-lift of its image and s₂(dev₂ ỹ) = ỹ; likewise for z̃. The same argument with G gives d₁ ≤ λ₂ d₂.
- T_i := 2cosh d_i = |tr(ρ_i(e_ỹ)ρ_i(e_z̃))| (two involutions with fixed points at distance d_i). By Lemma 1(b′)
  both are traces of level-≥3 elements of Γ₀.
- T₂ − T₁ ≤ 2cosh(λ₁d₁) − 2cosh d₁ and T₁ − T₂ ≤ 2cosh(λ₂d₂) − 2cosh d₂; both are increasing in d_i (λ ≥ 1), so
  |T₁ − T₂| ≤ Δ(R, L) < 2. By Lemma 1(b), T₁ = T₂, so d₁ = d₂. □

### 4.2 Lemma B2 — F is close to an orientation-preserving isometry

Let x̃ be R-deep. There is an orientation-preserving isometry g̃ of H with d(F(p), g̃(p)) ≤ ε(R, L) for all
p ∈ B(dev₁ x̃, L).

*Proof.* In the unit-disc model, move dev₁ x̃ and dev₂ x̃ to 0. Then B(dev₁ x̃, R) = {|z| < t} and F becomes
φ : {|z| < t} → D, φ(0) = 0.
- By Schwarz–Pick for B(dev₁ x̃, R), |φ′(0)| ≤ 1/t. By Schwarz–Pick for G on B(dev₂ x̃, R) and G ∘ F = id,
  |φ′(0)| ≥ t.
- ψ(w) := φ(tw) maps D to D, ψ(0) = 0, |ψ′(0)| ∈ [t², 1]. Write ψ(w) = wχ(w) with χ : D → D̄ and c₀ = χ(0),
  1 − |c₀| ≤ η = 1 − t². Schwarz–Pick for χ gives |χ(w) − c₀| ≤ s(1 − |c₀|²)/(1 − s) ≤ 2sη/(1 − s) for |w| ≤ s.
  Hence |ψ(w) − e^{iθ}w| ≤ sη(1 + s)/(1 − s), e^{iθ} = c₀/|c₀|.
- For |z| ≤ u (that is, p ∈ B(dev₁ x̃, L)), w = z/t and |φ(z) − e^{iθ}z| ≤ E. Both points lie in |·| ≤ u + E, where
  the hyperbolic metric is at most 2/(1 − (u + E)²) times the Euclidean one. Take g̃ = the rotation z ↦ e^{iθ}z
  composed with the two normalizing isometries. □

### 4.3 Lemma B3 — one orientation-preserving isometry for each star

Let x̃ be R-deep with R ≥ R_B(L) and St_L(x̃) ≠ ∅. There is a unique orientation-preserving isometry g_x̃ of H with
g_x̃(dev₁ ỹ) = dev₂ ỹ for all ỹ ∈ St_L(x̃) ∪ {x̃}.

*Proof.* Fix ỹ ∈ St_L(x̃) and let g be the orientation-preserving isometry with
(dev₁ x̃, dev₁ ỹ) ↦ (dev₂ x̃, dev₂ ỹ); it exists and is unique by Lemma B1. Let z̃ ∈ St_L(x̃) and p₁, p₂, p₃ the
dev₁-images of x̃, ỹ, z̃.
- By Lemma B1 the triangles (p_j) and (dev₂ of the same points) have equal sides, so some isometry h maps one onto the
  other.
- If p₁, p₂, p₃ are collinear, h may be taken orientation-preserving, and then h = g.
- Otherwise the side lengths are values d with 2cosh d ∈ 2 + 2Z[√2], conjugate in [−2, 2] (Lemma 1(b), (b′)), with
  d(p₁, p₂), d(p₁, p₃) ≤ L, so the triangle is one of the shapes in the definition of w_min(L): its width is
  ≥ w_min(L). Suppose h reverses orientation. Then σ := g̃⁻¹h (g̃ from Lemma B2) reverses orientation and moves each
  p_j by d(g̃ p_j, F(p_j)) ≤ ε. An orientation-reversing isometry with axis L′ and translation τ satisfies
  cosh d(p, σp) = cosh τ·cosh²δ + sinh²δ ≥ cosh 2δ, δ = d(p, L′) (Fermi coordinates). So every p_j lies within ε/2
  of L′, the width is ≤ ε/2 < w_min(L): a contradiction. So h is orientation-preserving, and h = g (two points).
- Hence g maps every point of the star correctly; uniqueness holds because the star has ≥ 2 points. □

### 4.4 Clusters, the conjugating isometry, and its arithmetic

Fix ℓ₀ ≥ ℓ_min, put L := 2ℓ₀, and fix R ≥ R_B(L) with R > L.
- **Edges.** For R-deep anchor lifts x̃, ỹ, put an edge [x̃, ỹ] := s₁ of the geodesic segment [dev₁ x̃, dev₁ ỹ] when
  this segment has length ≤ ℓ₀ and ỹ ∈ St_{ℓ₀}(x̃). The relation is symmetric and π-invariant (𝒬_i and the
  deepness are ρ_i(π)-invariant).
- **Clusters.** 𝒮 ⊂ Ũ is the union of all edges. A *cluster* 𝒞 is a connected component of 𝒮 (as a subset of Ũ, so
  two crossing edges lie in the same cluster) with at least one edge. Π_𝒞 := {γ ∈ π : γ𝒞 = 𝒞}. Translates of a
  cluster are clusters, and two of them are equal or disjoint.
- **Lemma B4.** All g_x̃ (x̃ a vertex of 𝒞, Lemma B3 with stars of radius L) are equal; call it g = g_𝒞. So
  dev₂ = g ∘ dev₁ on every anchor lift lying on 𝒞 or in the L-star of a vertex of 𝒞.
  *Proof.* Along an edge [x̃, ỹ], g_x̃ and g_ỹ are orientation-preserving and agree on the two points dev₁ x̃, dev₁ ỹ.
  At a crossing of [x̃, ỹ] and [z̃, w̃], the points z̃, w̃ lie within ℓ₀ + ℓ₀ = L of x̃ on the sheet of x̃, so they are
  in St_L(x̃); then g_x̃ and g_z̃ agree on dev₁ z̃, dev₁ w̃. □
- **Lemma B5 (conjugacy).** ρ₂(γ) = g·ρ₁(γ)·g⁻¹ for every γ ∈ Π_𝒞. Π_𝒞 contains e_x̃ for every anchor lift x̃ on 𝒞,
  and the image of π₁^orb(W_𝒞) for W_𝒞 := the projection to V₀ of a thin regular neighbourhood of 𝒞 (thin enough to
  contain no cone point other than the anchors on 𝒞).
  *Proof.* For a vertex ỹ: g ρ₁(γ) dev₁ ỹ = g dev₁(γỹ) = dev₂(γỹ) = ρ₂(γ) g dev₁ ỹ. The orientation-preserving
  isometries gρ₁(γ) and ρ₂(γ)g agree on ≥ 2 points, so they are equal. e_x̃ fixes x̃ ∈ 𝒞, so e_x̃𝒞 meets 𝒞 and equals it.
  The preimage of the projection of 𝒞 is ∪_γ γ𝒞, a locally finite union of pairwise disjoint closed sets. A loop in
  W_𝒞 deforms into the projection of 𝒞, and its lift from a point of 𝒞 is a connected path in that union, hence stays
  in 𝒞; its endpoint is γ·(start) with γ the class of the loop, so γ ∈ Π_𝒞. □
- **Lemma B6 (arithmetic of g).** If dev₁ of the vertices of 𝒞 is not contained in one geodesic, then g lies in
  Comm(Γ₀) = D_B^×/K^× (image in PGL₂(R)⁺), and ρ₁(γ), ρ₂(γ) have the same level for every γ ∈ Π_𝒞.
  *Proof.* Take three non-collinear vertices x̃, ỹ, z̃. The hyperbolic elements ρ₁(e_x̃ e_ỹ), ρ₁(e_x̃ e_z̃) have
  different axes, so they do not commute. Let A_i ⊂ D_B be the K-span of the lifts ±ρ̃_i(Π_𝒞) ⊂ Q¹. A_i is a
  non-commutative K-subalgebra of the quaternion division algebra D_B, so A_i = D_B (its proper subalgebras are
  fields). Conjugation by a lift ĝ ∈ GL₂(R)⁺ is R-linear and maps ±ρ̃₁(Π_𝒞) onto ±ρ̃₂(Π_𝒞), so it restricts to a
  K-algebra automorphism of D_B. By Skolem–Noether it is conjugation by some u ∈ D_B^×; as D_B spans M₂(R),
  ĝ ∈ R^×·u. The levels agree by Lemma 1(c). □

### 4.5 Theorem B

**Theorem B.** Let s₁ = s₂ = 0, O₁ ≠ O₂, ℓ₀ ≥ ℓ_min, L = 2ℓ₀, R ≥ R_B(L), R > L, and let 𝒞 be a cluster whose vertices
are not dev₁-collinear, with g = g_𝒞. Then:

1. **(anchors)** dev₂ = g ∘ dev₁ on every anchor lift on 𝒞; in particular (p₁(c), p₂(c)) lies on the Hecke curve
   T_g = {(Γ₀z, Γ₀gz)} ⊂ P¹×P¹ for every anchor c on the projection of 𝒞, and F is within ε(R, L) of g on the
   L-stars of the vertices (Lemma B2);
2. **(holonomy)** ρ₂ = gρ₁g⁻¹ on Π_𝒞, with g ∈ Comm(Γ₀);
3. **(parity)** for every simple closed curve ∂ ⊂ W_𝒞 and either disc D ⊂ V₀ bounded by ∂,
   |(O₁ Δ O₂) ∩ D| is even;
4. **(labels)** let φ_g be the automorphism of G induced by g (below). If 𝒞 carries matched anchors of two different
   labels, then φ_g = id, every anchor on 𝒞 is matched, and the E-monodromy μ is trivial on loops in W_𝒞. If
   moreover δ = 8 (then the curve has genus 1 and |Ω| = 4, E10 §2), all four points of Ω lie in **one** component of V₀ ∖ W_𝒞.

*Proof.*
- (1), (2): Lemmas B4–B6.
- (3): Let θ : Γ₀ → Γ₀/PQ¹(𝔓³) ≅ Z/2 (Lemma 1(c)); θ = 1 on elliptic involutions. In X_i, ∂ is homotopic to the
  product of loops around the cone points of X_i in D, so θ(ρ_i(∂)) ≡ |O_i ∩ D| mod 2. ∂ ∈ Π_𝒞 (Lemma B5) and θ∘ρ₂ =
  θ∘ρ₁ on Π_𝒞 (Lemma B6). O₁ and O₂ agree outside O₁ Δ O₂.
- (4), φ_g: conjugation by g ∈ D_B^× preserves the valuation at √2, hence the local maximal order and every 𝔓^k. It
  induces an automorphism φ_g of (Q_B/2Q_B)^× preserving levels, with r(gxg⁻¹) = φ_g(r(x)) whenever x, gxg⁻¹ ∈ Γ₀
  (r = reduction mod 2Q_B = 𝔓⁴). φ_g carries conjugation orbits of (Q_B/2Q_B)^× to conjugation orbits. On the four
  level-2 classes these orbits are {s_a, s_b, s_e} and {s_a s_b s_e} (`e13/check_lemma1.py`), so φ_g fixes s_a s_b s_e
  and permutes the three singular involutions.
- (4), labels: label_i(c) = r(ρ_i(e_c)). For an anchor on 𝒞, label₂ = φ_g(label₁). Matched anchors of two different
  labels give two fixed singular involutions, so φ_g fixes all three, which generate G (their product
  s_a s_b s_e ≠ 1): φ_g = id. Then every anchor on 𝒞 is matched and, for a loop γ in W_𝒞,
  μ(γ) = r(ρ₁γ)·r(ρ₂γ)⁻¹ = r(ρ₁γ)·φ_g(r(ρ₁γ))⁻¹ = 1 (μ as in E10 §1: the monodromy of E → V₀ is
  (r∘ρ₁)(r∘ρ₂)⁻¹ into (G×G)/ΔG ≅ G).
- (4), δ = 8: W_𝒞 is a regular neighbourhood of a connected finite graph, so V₀ ∖ W_𝒞 is a union of discs D_j, each
  bounded by a loop ∂_j in W_𝒞. Ω ∩ W_𝒞 = ∅ (the points of O₁ Δ O₂ are at distance ≥ R − ℓ₀ > 0 from 𝒞, and the
  anchors on 𝒞 are matched). So the local monodromies μ_v (v ∈ Ω) multiply to μ(∂_j) = 1 over each D_j. A disc with
  one point of Ω is impossible (μ_v ≠ 1). A split 2 + 2 makes the two monodromies in each disc equal, so the image of
  μ, which is generated by the μ_v (V₀ = P¹), has order ≤ 4, contradicting δ = 8. So all of Ω lies in one D_j. □

**What Theorem B does not say.** It does not say that W coincides with T_g on any open set (F ≠ g in general; they
agree at the anchors), and it does not bound the degree. It is a constraint on mixed slack-0 solutions: the defects
cannot be separated from each other by a non-collinear cluster with two matched labels, and every such cluster
determines a commensurator element g.

## 5. What is proved, and at what level

- Lemma 1(a): verified by exact computation (`filt.py`); the identification of G uses the uniqueness of (Z/2)³.
- Lemma 1(b), (c), Lemma 2, Theorem A part 1: complete proofs above. Theorem A part 2: the counting is elementary;
  the numerical constant is from `bound.py` and is not optimized.
- Theorem B: complete proof (§4, revision 3). Its constants are explicit; for L = 3.2 the width condition is proved by
  the certified bound width ≥ 0.03 (branch and bound with Lipschitz constants, revision 4), not by the numerical
  minimum. Floating point is used throughout; no interval arithmetic.
- Variant A′: outline only.
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
5. Theorem B (§4): Lemma B1 (two-sided Schwarz–Pick and λ); Lemma B2 (the normalized Schwarz-lemma estimate);
   Lemma B3 (the candidate-spectrum reduction to finitely many triangle shapes, the Fermi-coordinate inequality, and
   the numerical widths); Lemma B4 (constancy of g across edges and crossings, L = 2ℓ₀); Lemma B5 (the cluster group
   and W_𝒞); Lemma B6 (non-commutative subalgebra = D_B, Skolem–Noether); (3) and (4), including φ_g and the
   conjugation orbits.
6. Scope: slack (0, 0) only for Theorems A and B; k = 8, γ = 0.

## 8. Reproduction

From the repository root:

```
python3 -I stages/stage32/32-03-multibranch/MB104/route-E/e13/filt.py
python3 -I stages/stage32/32-03-multibranch/MB104/route-E/e13/traces.py 9
python3 -I stages/stage32/32-03-multibranch/MB104/route-E/e13/bound.py
python3 -I stages/stage32/32-03-multibranch/MB104/route-E/e13/check_lemma1.py
python3 -I stages/stage32/32-03-multibranch/MB104/route-E/e13/thmb_constants.py 3.2 0.03
```

- `filt.py`: exact arithmetic in Q_B/2Q_B (Lemma 1(a)); a few seconds.
- `traces.py 9`: exact arithmetic over Z[√2] on words of length ≤ 9 in α^{±1}, β^{±1} (Lemma 1(b) check; a finite
  sample, not a proof); a few seconds.
- `bound.py`: the numerical constants of Theorem A part 2 (floating point).
- `check_lemma1.py`: Lemma 1(b′) on the sample, the quotient order 2, the table comparison with E01, and the
  conjugation orbits {s_a, s_b, s_e}, {s_a s_b s_e} of the level-2 classes (used in Theorem B (4)).
- `thmb_constants.py L [w]`: the candidate spectrum, the triangle shapes and the numerical w_min(L), Δ, ε and R_B(L);
  with a second argument w, the certified proof that every non-degenerate shape has width ≥ w (about 4 minutes in
  total for L = 3.2 and w = 0.03; seconds for L ≤ 2.5).

## 9. History

- 2026-11-11, revision 4 (Claude): the width condition of Lemma B3 made rigorous (certified width ≥ 0.03 at L = 3.2).
  Prompted by a reading audit of revision 3 that could not open the repository (HOLD for lack of access). Its other
  points are answered in the text: the two normalizations Λ_i ⊂ Γ₀ are independent and need no compatibility (§4.0);
  λ(R, L) ≥ 1 is a ratio of metrics, not a contraction factor (B1); the traces in B1 are products of exactly two
  elliptic involutions, so Lemma 1(b′) applies; φ_g needs only the local maximal order at √2, which every
  g ∈ D_B^× preserves (§4.5 (4)).

- 2026-11-11, revision 3 (Claude): Theorem B rewritten as a complete proof (§4). Corrections to the outline: the
  "exactly Hecke" overstatement withdrawn; statements restricted to anchored clusters (X_i can have large cone-free
  regions); mirror matchings excluded (Lemma B3); "Zariski dense" replaced by the subalgebra argument (Lemma B6); the
  label step needs that φ_g fixes s_a s_b s_e, which holds by the conjugation-orbit sizes (checked). Constants:
  R_B(3.2) = 10.78.

- 2026-11-11, reading audits of Theorem A with Lemmas 1–2 (two independent auditors, head `dd451568e`):
  - auditor 1: **PASS** on all six items;
  - auditor 2: **FAIL**, on one claim: that Γ₀/PQ¹(𝔓³) has order 4, so that a product of two singular involutions
    is "the third singular involution, still at level 2". This is incorrect: the four elements at level exactly 2 form
    one coset of a subgroup of index 2 (8/4 = 2), and s_a s_b ∈ G₀ is free. Answered by the new Lemma 1(b′) with its
    proof and `e13/check_lemma1.py`. Its other items: MUST CHECK on the multiplication table vs E01 (now checked
    exactly); SHOULD FIX on the symbol G and on the wording of Lemma 2 (both applied). Its N ≈ 850 "by hand" vs 840:
    `check_lemma1.py` prints N = 840.02.
  - Theorem A's statement and constants are unchanged.

- 2026-11-11: draft written (Claude). A first reading check by another reviewer reproduced Lemma 1, Lemma 2 and
  Theorem A; Theorem B was confirmed to be an outline only.
- PR #1868 (another session) is not a verification of this draft: it does not contain the draft, and its
  "12 involutions model" and "trace exclusion of a bad subset" are not valid arguments (there are infinitely many
  order-2 points; every involution has reduced trace 0). Nothing from it is used here.
