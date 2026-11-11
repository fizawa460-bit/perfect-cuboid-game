# E14 (draft) — Positive slack: factorization, localization, a linear bound for one configuration, and the obstruction for the rest

Status: **draft research note, not audited, zero credit.** Not registered in `STATE.json`. Written 2026-11-11 as a
continuation of E13 (head `ff096e46c`). Scripts and their outputs: `e14/` (§10). Characteristic 0 only; no
mod-p input is used anywhere. Nothing is said about existence or non-existence of perfect cuboids.

Every statement carries one of the labels **[proved]**, **[outline]**, **[computed]**, **[open]**.

- **What is new.**
  - Lemma S: an exact formula for the slack (E11 Lemma 1's "at most" is an equality with explicit weights). [proved]
  - Proposition F: the factorization p_i = (covering) ∘ κ_i, and "s_i > 0 iff deg κ_i ≥ 2" (E13 §6.2). [proved]
  - Proposition L: the area deficit is exactly 2πs_i and it localizes: outside a set of area ≤ 2π(2cosh R − 1) per
    unit of slack, the comparison is within the factor tanh(R/2) = 1 − O(e^{−R}) of an isometry. [proved]
  - **Theorem A′:** if p₂ has slack 0 and O₁ ⊂ O₂, then a + s₁ ≤ 2936·s₁ + 5869. The bound is **linear** in the
    slack (E13 §3 guessed C(1 + s₁)²). [proved; constants computed]
  - **Theorem A⁺ (slack 0, a by-product):** the nested slack-(0, 0) case of E13 Theorem A does not occur at all.
    Types (2, 0), (0, 2) are excluded by a triangle count; types (4, 0), (0, 4) force a Lattès map and then
    (a, b) = (1, 3), which is excluded by an exact computation over Q(i). [proved, with one exact computation]
  - Theorem B′: Theorem B of E13 holds at positive slack with "R-deep" read sheet-wise. [outline]
  - **Proposition C (the obstruction):** when neither leg is an arithmetic source for the other, the hypotheses the
    method can see do not bound the degree: there are explicit pairs with O₁ = O₂, Ω = ∅, slack (0, 0) or (1, 1)
    (the latter with a free parameter) in every degree 2ⁿ. They are not birational. So any bound in those
    configurations must use birationality, which the metric comparison cannot see. [proved; checked exactly]
- **What it does not do.** No degree bound when both slacks are positive, when the slack-0 leg has the smaller odd
  set, or for the mixed types. The open core of E12 §5 is not closed.
- **Nothing in E10–E13 was found to be false.** Two statements are sharpened: E11 Lemma 1 (equality, Lemma S) and
  E13 Theorem A (emptiness, Theorem A⁺). E13 §6.2's count "defect set ≤ 4 + s₁ + s₂" is correct (§1).

Notation as in E10–E13: k = 8, γ = 0, p₁, p₂ : V₀ ≅ P¹ → P¹ of degrees a, b; B = {0, ∞, ±1, ±i};
O_i, s_i, Ω; Γ₀ = π₁^orb(P¹; 2⁶) = PQ¹(𝔓²); ℓ_min = arccosh(1 + √2). Additional notation:
m := |O₂ ∖ O₁| when O₁ ⊂ O₂. By E12 Lemma 0, O₁ Δ O₂ ⊂ Ω, so |O₁ Δ O₂| ≤ 4 for every solution of Problem W.

## 1. Lemma S — the slack is an orbifold Riemann–Hurwitz defect [proved]

Let p : V₀ → P¹ have degree n, odd set O and slack s. Put X := (V₀; O) (cone order 2 at O).

**(a)** p is an orbifold map X → P¹(2⁶), and O is the smallest cone set with this property. So p lifts to a
holomorphic P̃ : H → H, equivariant for a homomorphism ρ : π₁^orb(X) → Γ₀.

**(b)** For v ∈ V₀ with e = e_v(p), the local degree of P̃ at a lift of v is
ν_v = e if v ∈ O; e/2 if p(v) ∈ B and e is even; e if p(v) ∉ B. With m_v = 2 on O and 1 elsewhere,

  **s = Σ_v (ν_v − 1)/m_v = Σ_{p(v) ∉ B} (e − 1) + Σ_{p(v) ∈ B, e even} (e/2 − 1) + Σ_{v ∈ O} (e − 1)/2.**

**(c)** Every point with a non-zero term ("non-standard point") contributes at least 1. So there are at most s
non-standard points, and s = 0 iff P̃ is an isometry iff p is an orbifold covering.

*Proof.* (a) An orbifold map needs 2 | e_v·m_v whenever p(v) ∈ B; this holds iff m_v = 2 at every odd point.
(b) In local coordinates w^{m_v} = z upstairs, u^μ = y downstairs (μ = 2 over B), y = z^e gives u = w^{e·m_v/μ}.
Let N_ev be the number of even points over B. Then Σ_{over B} e = 6n and the total ramification is 2n − 2, so the
right-hand side is (2n − 2 − (6n − |O| − N_ev)) + (3n − N_ev − |O|/2) = |O|/2 − n − 2 = s. (c) The three kinds of
terms are ≥ 1 when non-zero (e ≥ 2; e ≥ 4; e ≥ 3). □

- E11 Lemma 1 says the non-standard ramification is "at most s_i"; (b) is the equality.
- In X_∪ := (V₀; O₁ ∪ O₂) the leg p_i has the additional critical points O_{3−i} ∖ O_i, each of cost ≥ 1/2. The
  total cost of leg i in X_∪ is σ_i := s_i + |O_{3−i} ∖ O_i|/2 (same computation). The number of critical points of
  both legs together is ≤ 4 + s₁ + s₂, as stated in E13 §6.2.

## 2. Proposition F — factorization (starting point 1) [proved]

Let Λ := ρ(π₁^orb(X)) ⊂ Γ₀.

1. Λ has finite index m₀ in Γ₀, and p = c ∘ κ with c : Y := H/Λ → P¹(2⁶) the orbifold covering of degree m₀ and
   κ : X → Y a holomorphic orbifold map of degree k = n/m₀, surjective on π₁^orb. Y has genus 0 and 2m₀ + 4 cone
   points.
2. **s > 0 iff deg κ ≥ 2.** Moreover s equals the orbifold Riemann–Hurwitz defect of κ, and 0 ≤ s ≤ 2k − 2.
3. Conversely, for a slack-0 map c with odd set O_c and *any* rational map κ, the map c ∘ κ has odd set
   {v : κ(v) ∈ O_c, e_v(κ) odd} and slack equal to the defect of κ with respect to O_c.

*Proof.* (1) P̃ descends to a non-constant holomorphic map X → H/Λ. Its image is open and compact, so H/Λ is
compact; the covering H/Λ → H/Γ₀ of a compact surface by a compact surface has finite degree. (2) If k = 1, κ is
an isomorphism of Riemann surfaces and p = c ∘ κ has only index-2 ramification over B, so s = 0. If s = 0, P̃ is an
isometry (Lemma S), ρ is injective and κ is an isomorphism. The defect formula is Lemma S applied to κ (the covering
c contributes nothing). Each cone point of Y has at most k odd preimages, so |O| ≤ k(2m₀ + 4) = 2n + 4k. (3) Same
computation. □

**Consequence.** A single leg has no rigidity at positive slack: slack 2n − 2 is the generic map, and slack 1
occurs in unbounded degree with a free parameter (§6). Any bound has to come from the pair.

## 3. Proposition L — area deficit and localization (starting point 2) [proved]

Let p, X, P̃, s be as in §1, or more generally let X′ = (V₀; O′) with O′ ⊃ O and total cost σ (σ = s if O′ = O).
Write g_X for the hyperbolic metric of X′ and g_p := P̃^*(hyperbolic metric), so g_p ≤ g_X (Schwarz–Pick).

**(a) Deficit.** Area(g_X) − Area(g_p) = 2πσ. In particular Area(X) = 2π(n + s) and the deficit is exactly 2πs.

**(b) Sheet-deep points.** Call x ∈ H **R-deep (for P̃)** if the germ of P̃⁻¹ at P̃(x) with value x extends to a
holomorphic section F_x on the disc B(P̃x, R). Then:
- if x is R-deep, |dP̃(x)| ≥ tanh(R/2), and B_X(x, R) ⊂ F_x(B(P̃x, R)); P̃ is injective on that set;
- if x is not R-deep, there is a critical point q̂ of P̃ with d(P̃q̂, P̃x) < R such that x is the endpoint of one of
  the ν_q̂ lifts, starting at q̂, of the geodesic from P̃q̂ to P̃x.

**(c) Size of the non-deep set.** The non-R-deep set has g_p-area ≤ 2π(cosh R − 1)·2σ and g_X-area
≤ 2πσ(2cosh R − 1). The number of points v ∈ O whose lifts are not R-deep is ≤ 2σ·N₀(R), where
N₀(R) := (cosh(R + ℓ_min/2) − 1)/(cosh(ℓ_min/2) − 1) bounds the number of order-2 points of Γ₀ in a closed disc of
radius R.

*Proof.* (a) Gauss–Bonnet: Area(X′) = 2π(−2 + |O′|/2), Area(g_p) = 2πn, and the difference is 2πσ by §1.

(b) Let K := ker ρ. P̃ factors as H → H/K → H. The second map P̄ is equivariant for the group Λ ≅ π₁^orb/K, which
acts properly and cocompactly on both sides; hence P̄ is proper, i.e. a finite branched covering (of degree
deg κ). If x is R-deep, F_x maps B(P̃x, R) into H, so |F_x′| ≤ 1/tanh(R/2) at the centre (Schwarz–Pick for the
disc), which is the first claim. The geodesic from x to y ∈ B_X(x, R) is mapped by P̃ into B(P̃x, R); the set of
parameters where F_x ∘ P̃ = id on it is closed, and open because P̃ is locally injective at points of the image of
F_x. If x is not R-deep, let R₀ < R be the supremum of the radii to which the germ extends, and F the section on
B(P̃x, R₀). If F extended near every point of the boundary circle it would extend to a larger disc. So there is a
boundary point z₁ near which it does not. Along the radius to z₁, the path F̄ in H/K accumulates, by properness
and finiteness of the fibre, at one point q′ over z₁, and q′ is a branch point of P̄ or a cone point of H/K (else F
would extend). The path F in H then converges to a lift q̂ of q′, a critical point of P̃; reversing the radius gives
the lift described.

(c) For a critical point q̂ and each of its ν lifted germs, the endpoints form a set on which P̃ is injective with
image in B(P̃q̂, R); its g_p-area is ≤ 2π(cosh R − 1). The stabilizer of q̂ (order m_q) permutes the germs freely
(a rotation by π fixes no direction). So modulo the group the non-deep set has g_p-area
≤ 2π(cosh R − 1)·Σ_q ν_q/m_q, and Σ_q ν_q/m_q ≤ 2Σ_q (ν_q − 1)/m_q = 2σ: in each of the five cases of Lemma S
(and for q ∈ O′ ∖ O) one checks ν/m ≤ 2(ν − 1)/m. The g_X-area exceeds the g_p-area by at most the total deficit
2πσ. For the count: P̃ of a lift of v ∈ O is an order-2 point of Γ₀, and the lift is determined by q̂, the germ and
that point. Open discs of radius ℓ_min/2 about order-2 points are disjoint (E13 Lemma 1), which gives N₀. □

**Answer to starting point 2.** Yes, with "away from the defects" read on the sheet: the comparison is within
tanh(R/2) = 1 − 2e^{−R} + … of an isometry outside a set of area ≤ 2π(2cosh R − 1) per unit of cost.
The fraction of X that is not R-deep is ≤ σ(2cosh R − 1)/(n + σ). **So the localization has content only when
σ·e^R is small compared with n.** For σ comparable to n (e.g. the generic map, σ = 2n − 2) the defects are
everywhere and there is no deep region at all; this is not an artefact of the proof (`e14/constants.py` prints the
numbers for R = 5, 5.49, 10.78).

## 4. Theorem A′ — one leg of slack 0 with the larger odd set (starting point 3) [proved]

**Setting.** s₂ = 0 and O₁ ⊂ O₂; s₁ ≥ 0 arbitrary; m := |O₂ ∖ O₁|. Then b = a + s₁ + m/2 (compare |O₂| = 2b + 4
with |O₁| + m), and (s₁, m) ≠ (0, 0) is assumed. No label, no Ω and no birationality is used; for solutions of
Problem W, m ∈ {0, 2, 4}.

- X₂ = (V₀; O₂) = H/Λ₂ with Λ₂ ⊂ Γ₀ of index b. The identity X₂ → X₁ followed by P̃₁ lifts to a holomorphic
  **G : H → H**, equivariant for φ : Λ₂ → Γ₀. Its total cost is b − a = s₁ + m/2 > 0, so G is not an isometry and
  d(Gx, Gy) < d(x, y) for all x ≠ y.
- For c ∈ O₁ with lift ĉ and involution ε ∈ Λ₂, φ(ε) is an elliptic involution of Γ₀ fixing G(ĉ) (the loop around
  c maps to an odd power of the generator at p₁(c)).

**Theorem A′.**
1. For two distinct lifts ĉ, ĉ′ of points of O₁, T₂ := 2cosh d(ĉ, ĉ′) and T₁ := 2cosh d(Gĉ, Gĉ′) satisfy
   **T₂ ≥ T₁ + 2**.
2. If moreover d(ĉ, ĉ′) = ℓ, then ĉ is not R-deep for G for any R > R(ℓ) = arccosh(cosh ℓ + sinh²ℓ).
3. Consequently, with θ := 1/(cosh(ℓ*/2) − 1) < 1 and N := N₀(R(ℓ*)),

   **2a + 4 + 2s₁ ≤ 2bθ + N·(2s₁ + m), i.e. a + s₁ ≤ [N(2s₁ + m) + θm − 4] / (2(1 − θ)).**

   With ℓ* = 3.048: N = 844.89, θ = 0.7122, so **a + s₁ ≤ 2935.2·s₁ + c_m** with c₀ = −6.9, c₂ = 2930.7,
   c₄ = 5868.4 (`e14/constants.py`; floating point, margins far above rounding).
4. Equivalent form: a non-covering holomorphic orbifold map between two genus-0 coverings of P¹(2⁶) loses a definite
   fraction of the area: b − a ≥ (b(1 − θ) + 2)/(N + 1), with (1 − θ)/(N + 1) = 3.4·10⁻⁴.

*Proof.* (1) εε′ ∈ Λ₂ and φ(ε)φ(ε′) are products of two elliptic involutions in (a conjugate of) Γ₀, or the
identity. By E13 Lemma 1(b′), (b) both traces lie in the gap set, and T₁ < T₂ by strict contraction.

(2) Suppose ĉ is R-deep with R > R(ℓ), with section F on D := B(Gĉ, R). By Proposition L(b), ĉ′ ∈ F(D) and
F(Gĉ′) = ĉ′; put d₁ := d(Gĉ, Gĉ′) ≤ ℓ. E13 Lemma 2 for F gives T₂ ≤ T₁ + 2sinh²d₁/(cosh R − cosh d₁). With (1),
cosh R ≤ cosh d₁ + sinh²d₁ ≤ cosh ℓ + sinh²ℓ: contradiction.

(3) Call c ∈ O₁ *isolated* if no other lift of a point of O₁ is within ℓ* of a lift of c. Isolated points have
disjoint embedded cone-discs of radius ℓ*/2 in X₂ (area 2πb), so there are at most 2bθ of them. A non-isolated
point is not R-deep for every R > R(ℓ*), hence (the critical points being discrete) is attached to a critical point
as in Proposition L(b) with distance ≤ R(ℓ*); by Proposition L(c) there are at most N·Σ_q ν_q/m_q ≤ N·2(b − a)
such points. (4) Use |O₁| = 2b + 4 − m and m ≤ 2(b − a). □

Remarks.
- The slack-0 leg must have the larger odd set, because the source of G has to be arithmetic. With s₂ = 0 and
  O₂ ⊊ O₁, or with both slacks positive, there are two contractions out of a non-arithmetic X_∪ and no inequality
  between T₁ and T₂ (§6, §8).
- Since b = a + s₁ + m/2, the theorem says: in this configuration the slack is at least a/2936 − 2. It is a bound
  of type (a), a + b ≤ C·(1 + s₁), with no smallness assumption.
- γ = 1 with one slack-0 leg (there O₁ = O₂): the same proof with Area(X₂) = 2πb and |O| = 2b gives
  b ≤ N·s₁/(1 − θ). [outline: the genus-1 bookkeeping is not written out]
- Whether the linear form is sharp for m ≤ 4 is [open]. For unrestricted m it is the right order if there is a
  slack-0 map f with f(B) ⊂ B unramified at B (then p₂ = f ∘ p₁ has b = a·deg f); such an f was not looked for.

## 5. Theorem A⁺ — the nested slack-(0, 0) case does not occur [proved, with an exact computation]

This sharpens E13 Theorem A (a ≤ 5,863) to emptiness. It uses only: strict contraction, the two smallest distances
between order-2 points of Γ₀, and an area count. It is the s₁ = 0 end of §4.

**The triangulation.** The three circles R ∪ {∞}, iR ∪ {∞}, |t| = 1 are fixed by anti-holomorphic symmetries of
(P¹; B), hence geodesic in P¹(2⁶). They cut it into 8 equilateral triangles with angles π/4, area π/4, side ℓ_min
(cosh side = (cos A + cos²A)/sin²A = 1 + √2) and altitude h, sinh h = sinh ℓ_min·sin(π/4), cosh 2h = 3 + 2√2.
Their lifts tile H; the vertices are exactly the order-2 points of Γ₀, with 8 triangles at each.

**Lemma T (distances) [proved].** Two distinct order-2 points of Γ₀ are at distance ℓ_min (iff adjacent in the
tiling) or at distance ≥ 2h; distance 2h occurs for the two apexes of two triangles with a common edge (a
*rhombus*, area π/2). A closed chain v₁v₂v₃v₄ of tiling edges with four distinct vertices is the boundary of a
rhombus.

*Proof.* The star of v is bounded by the 8 edges opposite to v, at distance h. If w is not adjacent to v, the
geodesic vw leaves the star of v at a point x of an edge not containing w; x is not in the open star of w, so
d(v, w) ≥ h + h. For the chain: v₂, v₄ are the two points at distance ℓ_min from v₁ and v₃, mirror images in the
line v₁v₃. If v₁, v₃ are adjacent, their common neighbours are the two apexes. Otherwise v₁, v₃ are neighbours of
v₂ at angle jπ/4, j ≥ 2; j = 2 is the rhombus; j = 3 would give a quadrilateral with angles 3π/4 at v₂, v₄, hence
< π/4 at v₁, impossible for two tiling edges; j = 4 gives v₄ = v₂. □

**Theorem A⁺.** There is no pair (p₁, p₂) with s₁ = s₂ = 0 and O₁ ⊊ O₂ (and none with O₂ ⊊ O₁). No label, Ω or
birationality is used.

*Proof.* Let 𝒯₂ be the lifted triangulation of X₂ (8b triangles; a point of O₂ lies in exactly 4 of them, the other
vertices in 8). G : X̃₂ → X̃₁ covers the identity of V₀ and is a strict contraction (m > 0).

*Step 1 (at most one point of O₁ per triangle).* If c ≠ c′ ∈ O₁ are vertices of one triangle, they have lifts at
distance ℓ_min, and Gĉ ≠ Gĉ′ are distinct order-2 points of (a conjugate of) Γ₀ at distance < ℓ_min: impossible.
Counting incidences, 4(2a + 4) ≤ 8b = 8a + 4m, so **m ≥ 4**. Types (2, 0) and (0, 2) are excluded.

*Step 2 (m = 4 forces a Lattès map).* Now every triangle has exactly one vertex in O₁. Crossing an edge at such
a vertex keeps it; crossing the opposite edge leads to the triangle over the adjacent face, whose third vertex lies
over the antipode β* of β = p₂(c). By connectedness all of O₁ lies over one antipodal pair {β, β*}, and every
point over β, β* is in O₁. So p₂ is unramified over β, β*, O₁ = p₂⁻¹{β, β*} (2b points), and over
Q := B ∖ {β, β*} it has 4 simple points D = O₂ ∖ O₁ and index 2 elsewhere: p₂ is a covering of (2, 2, 2, 2)
orbifolds (V₀; D) → (P¹; Q). The stars of the points of O₁ are 2b "squares" tiling X₂; their corners are D
(two squares each) and the 2b − 2 even vertices E (four squares each).

*Step 3 (a ≤ 1).* For each of the 4b sides of the squares, the two centres c, c′ (over β and β*, so c ≠ c′) have
lifts at distance 2h. Then Gĉ ≠ Gĉ′ are at distance < 2h, hence adjacent (Lemma T): the dual arc cc′ is homotopic
in X₁ to an edge of the triangulation 𝒯₁ of X₁. The dual arcs form a cell decomposition of V₀ with vertex set O₁
(all cone points of X₁) and one face for each corner. Lift it to X̃₁ and define an equivariant map f̃ : identity
on vertices, each arc to its geodesic, each face to a filling of its boundary chain. f̃ is equivariantly homotopic
to the identity, so the induced f : V₀ → V₀ has degree 1 and is onto. The boundary chain of a face is: two equal
edges (corner in D); or a closed 4-chain of tiling edges (corner in E), which is either degenerate (filling inside
a tree, area 0) or a rhombus of area π/2 (Lemma T). Hence 2πa = Area(X₁) ≤ (2b − 2)·π/2. With b = a + 2 this is
4a ≤ 2a + 2, so **a = 1, b = 3**.

*Step 4 (a = 1, b = 3, exact).* Then p₁ is a Möbius map and f := p₂ ∘ p₁⁻¹ is a cubic with f⁻¹{β, β*} = B and
four simple critical points with critical values Q. After an octahedral rotation of the target and a Möbius change
of the source, f = c·∏(t − b_j)/∏(t − b′_j) for a splitting of a Möbius image B′ of B into 3 + 3 points, with
critical values {±1, ±i}. Then the critical values v₁, …, v₄ of f/c are c⁻¹·{±1, ±i}, so their power sums p₁, p₂,
p₃ vanish. `e14/residual_exact.py` computes them exactly in Q(i) for all 20 splittings (traces of powers of the
multiplication by P/Q on Q(i)[t]/(P′Q − PQ′)): 12 splittings have four simple critical points, and all of them
have p₂ ≠ 0; the other 8 have a multiple critical point. □

Checks [computed].
- `e14/nested_check.py` (double precision): (1) for the 12 cubics of Step 4, the fibre over the antipodal pair has
  octahedral defect ≥ 1.0068 (0 for an octahedral set; control 1.9·10⁻¹⁶); (2) a falsification test of the theorem
  for a = 1: for all 15 slack-0 maps of degree 2 and all 60 of degree 3, no 6-subset of O₂ is octahedral (smallest
  defect 0.83 and 0.82; distinct points separated by ≥ 0.37, double roots split by ≤ 5·10⁻⁷).
- For a = 1, b = 2 the theorem can also be seen by hand: the 8 points of O₂ carry 8 or 10 lifted edges and no 6 of
  them are pairwise non-adjacent.

**Consequences.**
- In the slack-(0, 0) case only type (0, 0) (the equality face) and the mixed types (1, 1), (2, 2), (3, 1), (1, 3)
  remain. E13 Theorem B and its §6.1 are unaffected.
- The same two steps at positive slack (setting of §4) give [proved]: two points of O₁ on a common triangle of 𝒯₂
  have the same image under P̃₁ (their lifts in that triangle are identified by G), and two points of O₁ at the
  apexes of a rhombus have equal or adjacent images. With t_j := the number of triangles of 𝒯₂ with exactly j
  vertices in O₁, t₂ + 2t₃ − t₀ = 16 − 4m. If every triangle has exactly one vertex in O₁, Steps 2–3 give m = 4,
  p₂ Lattès, and 2a ≤ b − 1, i.e. s₁ ≥ a − 1.
- Whether a ≤ b/2 + O(1) holds in the whole setting of §4 is [open]; it would replace the constant 2936 by about 1.
  The missing step is the area count when triangles with no vertex in O₁ are present.

## 6. Proposition C — the obstruction, with explicit families [proved; checked exactly]

**The maps.** L(x) := (x² − 1)/(2ix). It is the x-coordinate of the endomorphism of degree 2 of y² = x³ − x (up to
a unit). Its critical points are ±i with critical values ±1, L(±1) = 0, L(0) = L(∞) = ∞, and L(−x) = −L(x).
Put L_n := L ∘ … ∘ L (n times), of degree 2ⁿ.

1. **L_n has slack 0 for every n** [proved]. All critical values of L_n lie in {±1, 0, ∞} and all critical points
   have index 2: a critical point of L_n is a point x with L_j(x) = ±i for one j < n (the orbit ±i ↦ ±1 ↦ 0 ↦ ∞ ↦ ∞
   never returns to ±i, so only one factor is critical along it). So slack-0 maps exist in every degree 2ⁿ
   (and, by the same argument with other isogenies onto y² = x³ − x, in every degree; not written out).
2. **p_{n,c} := L_n(t² + c) has slack 1** for all c outside a finite set, degree 2ⁿ⁺¹, and depends on the free
   parameter c [proved]. By Proposition F(3) the slack is the defect of κ = t² + c with respect to O_{L_n}: the
   critical point ∞ lies over the cone point ∞ ∈ O_{L_n} with index 2 (cost 0), and t = 0 lies over c ∉ O_{L_n}
   (cost 1). For n = 0 this is the example t² + c of E10 §5.
3. **The pairs (p, −p)**, p = L_n or p = p_{n,c}: since −B_χ = B_χ for each label, O₁ = O₂ with equal labels, so
   **Ω = ∅**, j = |O_i|, h = 0, and all parity conditions of Problem W (E10 §2 with |Ω| ≤ 4) hold. The slacks are
   (0, 0), resp. (1, 1); the degrees (2ⁿ, 2ⁿ), resp. (2ⁿ⁺¹, 2ⁿ⁺¹), are unbounded; for slack (1, 1) there is a
   one-parameter family in each degree. The image of (p, −p) is the graph y = −x: **the pair is not birational**
   onto a curve of bidegree (a, b), so it is not a solution of Problem W.

*Exact check* (`e14/lattes_family.py`, arithmetic in Q(i)[t], no floating point): slack 0 for L_n, n ≤ 5 (degree
≤ 32), and slack 1 for p_{n,c}, n ≤ 4, c ∈ {2, 1/3 + i/2, −5 + i}; all multiplicities over B are certified ≤ 2.

**Proposition C.** Let 𝓗 be the set of pairs (p₁, p₂) of maps V₀ → P¹ with |O₁ Δ O₂| ≤ 4 and |Ω| ≤ 4, with
birationality dropped.
- (i) If O₁ = O₂ with equal labels (so Ω = ∅), then (p₁ ∘ κ, p₂ ∘ κ) has the same property for *every* rational
  map κ. So this part of 𝓗 is closed under composition on the source.
- (ii) Hence 𝓗 contains pairs of unbounded degree with (s₁, s₂) = (0, 0) and with (s₁, s₂) = (1, 1), the latter
  in positive-dimensional families. **So no inequality a + b ≤ C·f(s₁ + s₂) holds on 𝓗.**
- (iii) Every argument that uses only the two orbifold maps X_∪ → P¹(2⁶), their holonomies and metrics, the sets
  O_i and the labels — this includes Schwarz–Pick, the trace gap and Theorem B/B′ — is valid on 𝓗. Therefore, in
  the configurations where 𝓗 has unbounded degree, **a degree bound must use birationality of (p₁, p₂)**.
- (iv) In the setting of §4 the pairs (p, U ∘ p) are excluded by the hypothesis itself: they have s₁ = s₂ and
  O₁ = O₂, so G is an isometry. That is why §4 needs no birationality, and why its proof cannot be transported to
  the case s₁, s₂ > 0.

*Proof.* (i) The odd set and labels of p_i ∘ κ are determined by those of p_i and by κ (Proposition F(3)); equal
data for p₁, p₂ give equal data after composition. (ii) items 1–3. (iii), (iv) by inspection. □

**Remark (how birationality enters at slack 0; not checked here).** For type (0, 0), p₂ = "g ∘ p₁" with
g ∈ Comm(Γ₀) and Λ₁ ⊂ Γ₀ ∩ g⁻¹Γ₀g; the pair is birational iff equality holds, i.e. iff Λ₁ is a *congruence*
subgroup. Genus-0 congruence subgroups have bounded index by a spectral gap (λ₁ ≥ 3/16 via Jacquet–Langlands and
Gelbart–Jacquet, with Zograf's inequality); non-congruence ones (e.g. the L_n above) do not. This is cited, not
proved, and is used nowhere. At positive slack there is no group whose congruence property expresses
birationality; that is the precise gap.

**Remark (the reduction of all remaining cases to one).** Let π : V₁ → V₀ be the double cover branched at
O₁ Δ O₂ (2 or 4 points; genus 0 or 1), m₁ := |O₁ ∖ O₂|, m₂ := |O₂ ∖ O₁|. Then p_i ∘ π have the **same** odd set
π⁻¹(O₁ ∩ O₂) and slacks s₁′ = 2s₁ + m₂, s₂′ = 2s₂ + m₁ [proved: count |O′| = 2|O₁ ∩ O₂| and apply the genus-γ′
form of the slack]. So every case is an "equal odd sets" case; §4 is exactly the case s₂′ = 0; everything else is
"equal odd sets, both slacks positive", which is where the families of this section live.

## 7. Theorem B′ — anchored clusters at positive slack [outline]

**Statement.** Let s₁, s₂ be arbitrary, X_∪ = (V₀; O₁ ∪ O₂) with group Π, P̃_i : H → H and ρ_i : Π → Γ₀. Call a
lift x̃ of an anchor (a point of O₁ ∩ O₂) R-deep if it is R-deep for P̃₁ and for P̃₂ (Proposition L(b)). Define
stars, edges, clusters and Π_𝒞 as in E13 §4 with dev_i := P̃_i and s_i := the sections F_x̃. Then E13 Theorem B
(1)–(4) holds verbatim for every non-collinear cluster, with the same constants (L = 3.2, R = 10.78).

**Why (the changes to E13 §4).** Lemmas B1–B3 use only F = P̃₂ ∘ s₁ and G = P̃₁ ∘ s₂ on the discs, G ∘ F = id near
the centre, and the fact that a path through s_i(disc) is the s_i-lift of its image; the last point is
Proposition L(b). Lemmas B4–B6 are statements about Π_𝒞 and ρ_i(Π_𝒞) ⊂ Γ₀ and do not use that dev_i is a covering.
In (3), a loop around a non-standard point or a point of O_{3−i} ∖ O_i has trivial or even image under ρ_i, so
θ(ρ_i(∂)) ≡ |O_i ∩ D| still holds. Not re-audited line by line; hence "outline".

**When it has content (goal (b)).** By Proposition L(c) at most 2(σ₁ + σ₂)·N₀(10.78) ≤ 336,582·(s₁ + s₂ + 2)
anchors fail to be deep. So deep anchors exist once

  |O₁ ∩ O₂| ≥ 2·max(a, b) > 336,582·(s₁ + s₂ + 2),

i.e. when **the slack is below about (degree)/1.7·10⁵**. Above that threshold the theorem may be empty. As at slack
0, it constrains but does not bound: the pairs of §6 satisfy it with g = the lift of U on every cluster.

## 8. Summary by configuration (goals (a)–(c))

| configuration | result | level |
|---|---|---|
| s₁ = s₂ = 0, nested | does not occur (Theorem A⁺) | proved (+ exact computation) |
| s₂ = 0, O₁ ⊂ O₂, s₁ > 0 | a + s₁ ≤ 2935.2·s₁ + c_m (Theorem A′) | proved |
| γ = 1, one leg of slack 0 | b ≤ N s₁/(1 − θ) | outline |
| s₂ = 0, O₂ ⊊ O₁, s₁ > 0 | only Theorem B′; no bound | open |
| s₁, s₂ > 0, any O₁, O₂ | only Theorem B′; on 𝓗 no bound exists (Prop. C) | obstruction proved |
| mixed, slack (0, 0) | E13 Theorem B; no bound | open (as in E13) |

- (a) holds, linearly in the slack and without any smallness condition, exactly when one leg is an arithmetic
  source for the other.
- (b) In all other configurations the method gives rigidity statements only on the deep part, which is non-empty
  when the slack is below about a/1.7·10⁵ (for the Theorem B′ radius) and covers a fraction
  ≥ 1 − σ(2cosh R − 1)/(a + σ) of the surface. When the slack is comparable to the degree nothing is deep.
- (c) The obstruction is birationality: Proposition C with the families (L_n, −L_n) and (L_n(t² + c), −L_n(t² + c)).

## 9. What remains open, and audit points

Open.
1. Both slacks positive with a birational pair: any bound. By §6 this is the single remaining case (after the
   double cover), and it needs an input that distinguishes a birational pair from a composite one.
2. s₂ = 0 with O₂ ⊊ O₁ and s₁ > 0.
3. Mixed slack-(0, 0) types (E13 §6.1), unchanged.
4. Whether a ≤ b/2 + O(1) in the setting of §4 (end of §5).
5. Whether Theorem A′ is ever non-vacuous for m ≤ 4: no example with s₂ = 0, O₁ ⊂ O₂, s₁ > 0 is known.
6. k = 4: not checked (the triangulation there has 8 branch values and a different triangle).

Audit points.
1. Lemma S: the three local degrees and the bookkeeping identity.
2. Proposition L(b): properness of H/K → H, and the limit argument producing the critical point; (c): the free
   action of the stabilizer on germs and ν/m ≤ 2(ν − 1)/m in every case.
3. Theorem A′: φ(ε) is an involution for c ∈ O₁; the embeddedness of the discs when only O₁-lifts are excluded
   (other cone points may lie inside); the count modulo Λ₂.
4. Theorem A⁺: Lemma T (the star argument and the 4-chains); Step 2 (antipode under crossing the opposite edge;
   connectedness); Step 3 (the degree-1 argument and the area of fillings; the number 2b − 2 of even vertices);
   Step 4 (the reduction to power sums; the 8 splittings with a multiple critical point are irrelevant because
   slack 0 requires four simple critical points).
5. §6: the orbit argument for L_n; that −B_χ = B_χ.
6. Theorem B′ is an outline.
7. Scope: k = 8, γ = 0 throughout (γ = 1 only in the remark of §4).

## 10. Reproduction

From the repository root (outputs are stored next to the scripts as `*.out`):

```
python3 -I stages/stage32/32-03-multibranch/MB104/route-E/e14/constants.py
python3 -I stages/stage32/32-03-multibranch/MB104/route-E/e14/residual_exact.py
python3 -I stages/stage32/32-03-multibranch/MB104/route-E/e14/lattes_family.py
python3 -I stages/stage32/32-03-multibranch/MB104/route-E/e14/nested_check.py
```

- `constants.py`: ℓ_min, h, cosh 2h = 3 + 2√2; ℓ*, N, θ and the constants of Theorem A′; the numbers of
  Proposition L and Theorem B′. Floating point, elementary functions.
- `residual_exact.py`: Theorem A⁺ Step 4, exact in Q(i) (`gq.py`: Gaussian rationals and polynomials). Ends `PASS`.
- `lattes_family.py`: §6 items 1–2, exact in Q(i)[t]. About 10 seconds. Ends `PASS`.
- `nested_check.py`: the two numerical checks of §5 (needs numpy). Ends `PASS`. Not part of any proof.

## 11. Changes relative to E13

- **Changed:** E13 Theorem A (nested slack 0: a ≤ 5,863) becomes "no such pair" (Theorem A⁺). Variant A′ of E13 §3
  is now a theorem, with a linear instead of a quadratic bound. E13 §6.2 is confirmed and made precise
  (Lemma S, Proposition F). "R-deep" is redefined sheet-wise so that it makes sense at positive slack.
- **Proved:** Lemma S; Proposition F; Proposition L; Theorem A′; Lemma T and Theorem A⁺ (Step 4 by an exact
  computation); the families and Proposition C; the double-cover reduction.
- **Outline:** Theorem B′; the γ = 1 remark; "slack-0 maps in every degree" beyond 2ⁿ; the congruence remark (cited
  only).
- **Computed:** all constants (`constants.py`); the exact checks; the numerical falsification test.
- **Open:** §9 items 1–6. In particular the core of E12 §5 remains open, now reduced to: a birational pair with
  equal odd sets and both slacks positive.
