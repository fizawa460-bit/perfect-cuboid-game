# E15 (draft) — Tools that see the image curve: Klein intersection, holonomy uniqueness, cone divisors; k = 4 by squaring

Status: **draft research note, zero credit; reading audit PASS (Claude, 2026-11-12, `AUDIT-CLAUDE-E15-20261112.md`).** Written 2026-11-11 as a continuation of E14 (head
`2ac01e841`). Not registered in `STATE.json`. Characteristic 0 only; no mod-p input. Nothing is said about existence
or non-existence of perfect cuboids. Scripts: `e15/` (§8).

Every statement carries one of the labels **[proved]**, **[outline]**, **[computed]**, **[open]**.

- **Result in one line: the open core (E14 §9 item 1) is not closed, and no degree bound is obtained in any open
  configuration.** What is new is listed below; each item is small.
- New, proved:
  - Lemma K (Klein intersection): if the image of (p₁, p₂) is not one of the four Klein graphs, then
    Σ_{v ∈ J} min(e_v(p₁), e_v(p₂)) ≤ 2(a + b); hence **s₁ ≤ b and s₂ ≤ a** when |Ω| ≤ 4.
  - Lemma U (uniqueness): if ρ₂ = gρ₁g⁻¹ on the whole group Π, then P̃₂ = g ∘ P̃₁ and p₂ factors through κ₁. So a
    birational pair with s₁ > 0 has **non-conjugate** holonomies.
  - Lemma D (cone divisors): the pulled-back metrics g_i are determined by their cone-angle functions θ_i; θ₂ ≥ θ₁
    pointwise implies g₂ ≤ g₁; θ₁ = θ₂ implies P̃₂ = g ∘ P̃₁. So a birational pair with s₁ > 0 has θ₁ ≠ θ₂.
  - Lemma Q (k = 4): squaring maps Problem W₄ into the k = 8 setting with the same odd sets, slacks and Ω. Every
    result of E13/E14 that does not use birationality holds for W₄ with (a, b) replaced by (2a, 2b).
  - Lemma M: an explicit slack-0 map f of degree 5 with f(B) ⊂ B, unramified at B (asked for in E14 §4, last remark).
- New, computed: the setting of E14 Theorem A′ with s₁ > 0 is **not realised for b ≤ 3** (§5).
- Addendum §10: the quantitative version of Lemma U was tried. Proved on the way: Theorem E (equal distances for
  short deep pairs of anchors at any slack, radius 4.41 for ℓ = 3.2) and Lemma N (nodal domains of w ≤ number of
  poles). It gives no bound, and §10 says exactly why.
- Addendum §11 (2026-11-12): the component condition of E10 §5 was examined once. It is a non-degeneracy condition on
  label classes (Lemmas C1, C2) and does not separate birational from non-birational pairs (Proposition C′, with
  the degree-5 map of Lemma M). No route to a degree bound; stopped.
- Not obtained: everything in §7.

Notation as in E10–E14. Φ := (p₁, p₂) : V₀ → P¹×P¹; J = label-matched points of O₁ ∩ O₂; K = {t, −t, 1/t, −1/t}.

## 1. Lemma K — intersection with the four Klein graphs [proved]

Γ_g := {y = g(x)}, g ∈ K. The 12 label-matched points of B×B are the points (β, β′) with β, β′ in the same B_χ.
K acts on each B_χ through a quotient of order 2, so **each matched point lies on exactly two of the four Γ_g**:
(0, 0): t, −t; (0, ∞): ±1/t; (1, 1): t, 1/t; (1, −1): −t, −1/t; (i, i): t, −1/t; (i, −i): −t, 1/t.

**Lemma K.** Let p₁, p₂ : V₀ → P¹ have degrees a, b and suppose Φ(V₀) is not one of the Γ_g. Then

  **Σ_{v : Φ(v) matched} min(e_v(p₁), e_v(p₂)) ≤ 2(a + b).**

*Proof.* Γ_g has bidegree (1, 1), so Φ^*Γ_g is an effective divisor of degree a + b on V₀ (the defining section does
not vanish identically because Φ(V₀) ⊄ Γ_g). At v with Φ(v) = (β, gβ), in local coordinates x − β = u^{e₁}·unit,
y − gβ = u^{e₂}·unit, and the local equation of Γ_g is (y − gβ) − c(x − β) + …, c ≠ 0; its order at v is
≥ min(e₁, e₂). Sum over the four g: every matched v is counted twice. □

**Corollary K.** If moreover |Ω| ≤ 4, then s₁ ≤ b and s₂ ≤ a, and (|O₁| + |O₂|)/2 ≤ 2(a + b) + 4.

*Proof.* By E12 Lemma 0, j ≥ |O_i| − |Ω| ≥ 2·deg p_i + 2s_i, and j ≤ the left-hand side of Lemma K. □

Remarks.
- The hypothesis is on the image only; birationality is not needed. For a pair of degrees (a, b) mapping k : 1 onto
  its image the bound is the same (pull back).
- It is the k = 8 form of the inequality Σ_{v ∈ J} min(e₁, e₂) ≤ 4(a + b) of E12 §2 (k = 4).
- It is the only place so far where the image curve enters. E14 Proposition F gave s ≤ 2·deg − 2 for a single leg;
  the generic pair (p, −p) (slack 2a − 2 on both sides) violates s₁ ≤ b, consistently: its image is Γ_{−t}.
- **It does not bound the degree**, and it does not exclude the families of E14 §6 numerically: for (p, −p) with
  p = L_n(t² + c), n ≥ 1, one has j = |O| = 2a + 6 ≤ 4a. Those are excluded only because their image is a Klein graph.
- Why no refinement of this kind can work [outline]: an inequality W·T ≥ Σ_p m_p(W)m_p(T) for fixed curves T is
  linear in (a, b) on both sides. With M := Σ m_p(W) ≥ j the best ratio found is the Klein one (6 matched points per
  (1, 1)-curve). Fibres give M ≤ 6·min(a, b); translates of W by K×K give a quadratic inequality that is weaker
  (about (a + s₁)² ≤ 6ab under equidistribution; not checked in detail). At slack 0, j ≈ 2·max(a, b) is far below all
  of these. This is the blind spot of E10 §4 in another form.

## 2. Lemma U — two equivariant holomorphic maps with conjugate holonomy coincide [proved]

Setting: Π = π₁^orb(X_∪) acting cocompactly on H; P̃_i : H → H holomorphic, non-constant, ρ_i-equivariant
(E14 §1, §7), ρ_i : Π → Γ₀.

**Lemma U.** If there is g ∈ PSL₂(R) with ρ₂(γ) = gρ₁(γ)g⁻¹ for all γ ∈ Π, then P̃₂ = g ∘ P̃₁. Then p₂ is constant on
the fibres of κ₁ (E14 Proposition F), so the pair is not birational when deg κ₁ ≥ 2, i.e. when s₁ > 0.

*Proof.* Put f₁ := g ∘ P̃₁, f₂ := P̃₂; both are ρ₂-equivariant. Q := |f₁ − f₂|²/(Im f₁·Im f₂) = 2(cosh d(f₁, f₂) − 1)
is Π-invariant. Suppose f₁ ≢ f₂ and put u := log Q : H → [−∞, ∞), continuous. On {u > −∞},
Δu = |f₁′|²/(Im f₁)² + |f₂′|²/(Im f₂)² ≥ 0, because log|f₁ − f₂|² is harmonic and
Δ log Im f = −|f′|²/(Im f)². By invariance and compactness u has a maximum at some x₀, finite. A subharmonic function
with an interior maximum is constant near it; then Δu = 0 near x₀, so f₁′ = f₂′ = 0 on an open set: contradiction.
So f₁ = f₂. For the last claim: if κ₁(v) = κ₁(v′), lifts x, y satisfy P̃₁(y) = ρ₁(γ)P̃₁(x) = P̃₁(γx) for some γ, hence
P̃₂(y) = P̃₂(γx) and p₂(v′) = p₂(v). □

**Corollary U (what birationality means for the holonomy).** For a birational pair with s₁ > 0 (or s₂ > 0), ρ₁ and ρ₂
are not conjugate in PSL₂(R). In the language of E13 Theorem B / E14 Theorem B′: the cluster groups Π_𝒞 with a common
conjugating element g never generate Π.

- The families of E14 §6 have ρ₂ = Uρ₁U⁻¹ on all of Π. So "ρ₁ ≁ ρ₂" is a property that birational pairs have and the
  known obstruction families do not. The converse is false (a pair (q₁ ∘ κ, q₂ ∘ κ) with a birational (q₁, q₂) of
  positive slack is non-birational with non-conjugate holonomies).
- Local form [proved, same proof]: if S ⊂ V₀ is a compact subsurface and ρ₂ = gρ₁g⁻¹ on the image of π₁^orb(S),
  then d(g ∘ P̃₁, P̃₂), which is then a function on S, takes its maximum on ∂S.
- **This does not give a bound**: it turns birationality into a statement about two representations, but there is no
  quantitative version (a lower bound for d(gP̃₁, P̃₂) somewhere) and Theorem B′ gives ρ₂ = gρ₁g⁻¹ only cluster by
  cluster.

## 3. Lemma D — the cone divisor decides, and a monotonicity principle [proved]

g_i := P̃_i^*(hyperbolic metric) is a conformal metric of curvature −1 on V₀ with cone angle
θ_i(v) = π·e_v(p_i) if p_i(v) ∈ B and 2π·e_v(p_i) otherwise (Lemma S(b): the local degree of P̃_i in an orbifold
chart). Area(g_i) = 2π·deg p_i.

**Lemma D.** (a) If θ₂(v) ≥ θ₁(v) for all v, then g₂ ≤ g₁ (so b ≤ a). (b) If θ₁ = θ₂, then g₁ = g₂ and
P̃₂ = g ∘ P̃₁ for an orientation-preserving isometry g; then Lemma U's conclusion holds.

*Proof.* Write g₂ = e^{2w}g₁. Away from the cone points Δ_{g₁}w = e^{2w} − 1. In a local coordinate ζ at v,
g_i = |ζ|^{2(θ_i/2π − 1)}·(positive continuous), so w = ((θ₂ − θ₁)/2π)·log|ζ| + O(1): under (a), w is bounded above
near every cone point. w⁺ := max(w, 0) is subharmonic away from the cone points and bounded above, so it extends as a
subharmonic function to the compact surface V₀ and is constant; a constant c > 0 contradicts Δw = e^{2c} − 1 > 0.
So w ≤ 0. (b) Apply (a) both ways; two developing maps of one hyperbolic cone structure differ by an isometry,
orientation-preserving because both are holomorphic. □

- (a) contains Schwarz–Pick for E14 §3 (g_p ≤ g_X) and is the reason E14 Theorem A′ needs the slack-0 leg to have
  the larger odd set: only then θ₂ ≤ θ₁ everywhere.
- **Corollary D.** A birational pair with positive slack has θ₁ ≠ θ₂. In the reduced case O₁ = O₂ the two angle
  functions agree on all standard points; they differ only at the ≤ s₁ + s₂ non-standard points. The families of
  E14 §6 have θ₁ = θ₂.
- In every open configuration neither θ dominates the other, so (a) gives no inequality between a and b beyond
  Gauss–Bonnet. [No progress on the bound.]

## 4. Lemma Q — k = 4 reduces to k = 8 by squaring, for everything that ignores the image [proved]

Let (p₁, p₂) be a pair for Problem W₄ (branch set μ₈, labels u = primitive 8th roots, v = μ₄; E12 §2), of degrees
(a, b), with odd sets O_i⁽⁴⁾, slacks s_i⁽⁴⁾ = (|O_i⁽⁴⁾| − 4·deg p_i − 4)/2 and Ω⁽⁴⁾.

**Lemma Q.** The pair (p₁², p₂²), of degrees (2a, 2b), has, in the k = 8 sense: O_i = O_i⁽⁴⁾, s_i = s_i⁽⁴⁾,
Ω = Ω⁽⁴⁾, labels u ↦ a, v ↦ b, and no odd point of label e.

*Proof.* p²(v) ∈ {±1, ±i} iff p(v) ∈ μ₈, with e_v(p²) = e_v(p); p²(v) ∈ {0, ∞} iff p(v) ∈ {0, ∞}, with
e_v(p²) = 2e_v(p) even. So the odd sets agree and s = (|O| − 2·2n − 4)/2. h_a(x², y²) = h_u, h_b(x², y²) = h_v and
h_e(x², y²) = (xy)² is a square, so the odd loci agree. □

**Consequences for W₄ [proved, given the cited statements].**
- E14 Lemma S, Propositions F and L hold for each leg (with Γ₀⁽⁴⁾ := π₁^orb(P¹; 2⁸) ⊂ Γ₀ of index 2, so E13 Lemma 1
  — the trace gap — holds verbatim for its elliptic involutions).
- E14 Theorem A⁺: there is no W₄ pair with s₁ = s₂ = 0 and O₁ ⊊ O₂.
- E14 Theorem A′: if s₂ = 0 and O₁ ⊂ O₂, then 2a + s₁ ≤ 2935.2·s₁ + c_m.
- E13 Theorem B (slack (0, 0), O₁ ≠ O₂) applies to (p₁², p₂²).
- **Not transferred:** anything using birationality, because (p₁², p₂²) need not be birational even if (p₁, p₂) is.
  So E14 §9 item 6 is answered for the non-birational tools, and the open core for k = 4 is the same as for k = 8.

## 5. E14 §9 items 4–5: Theorem A′ at small degree, and the Lattès map [computed / proved]

**Lemma M [proved; exact check].** α := −1 + 2i, f(x) := x(x² + α)²/(αx² + 1)². Then f has degree 5, all its 8
critical points are simple with critical values in {0, ∞, ±1}, f fixes every point of B, and f is unramified at B.
Hence for every slack-0 map p₁, p₂ := f ∘ p₁ has slack 0, O₁ ⊂ O₂, b = 5a and m = |O₂ ∖ O₁| = 8a.

*Proof.* f − 1 = (x − 1)(x² + ux + 1)²/(αx² + 1)² and f + 1 = (x + 1)(x² − ux + 1)²/(αx² + 1)² with u = (1 − α²)/2;
the four quadratics are square-free, pairwise coprime and have no root in B (`e15/lattes5.py`, exact in Q(i)[x]).
The critical points of f ∘ p₁ are those of p₁ (over B, index 2, and f is unramified at B with f(B) ⊂ B) and the
preimages of those of f (p₁ is unramified outside p₁⁻¹(B)). □

- This is the x-coordinate of an endomorphism of norm 5 of y² = x³ − x. It answers the last remark of E14 §4:
  **for unrestricted m the nested slack-0 case has unbounded degree with a = m/8**, so a bound that is linear in m
  is of the right order. It says nothing for m ≤ 4 (Theorem A⁺).

**Small degrees [computed].** In the setting of E14 §4 (s₂ = 0, O₁ ⊂ O₂, s₁ > 0, m ≤ 4), b = a + s₁ + m/2.
- b ≤ 2: impossible (a = 1 forces s₁ = 0).
- b = 3: the only numerical possibility is (a, s₁, m) = (2, 1, 0): p₁ of degree 2 with exactly one critical value in
  B and O₁ = O₂. Then O₂ is invariant under the deck involution σ of p₁, σ acts freely on O₂, and the five σ-orbits
  together with the image of one fixed point of σ form a Möbius image of B. `e15/aprime_b3.py` (double precision)
  lists, for the 60 slack-0 cubics, all Möbius involutions preserving O₂ (79 in total; rejected candidates have
  error ≥ 1.0·10⁻², accepted < 10⁻⁶) and finds octahedral defect ≥ 0.9255 for every quotient configuration
  (a planted example is detected with defect 1.7·10⁻¹⁵). **So the setting of Theorem A′ with s₁ > 0 is empty for
  b ≤ 3.** Numerical, not a certificate.
- b ≥ 4: [open]. b = 4 needs the list of slack-0 maps of degree 4 (not available; E11 §5). The question
  a ≤ b/2 + O(1) is [open]; b = 3 with a = 2 would have been the first test and does not occur.

## 6. Verdict by item

| item (as asked) | verdict | reason |
|---|---|---|
| 1. both slacks positive, birational | **not closed; no bound** | Lemmas K, U, D are proved and use the image / birationality, but none is quantitative in the degree. |
| 2. mixed slack-(0, 0) types | **no progress** | at slack 0 Lemma K is far from sharp (j ≈ 2·max(a, b) ≤ 2(a + b)); Lemmas U, D only say ρ₁ ≁ ρ₂, θ₁ ≠ θ₂, which is clear there (O₁ ≠ O₂). |
| 3. s₂ = 0, O₂ ⊊ O₁, s₁ > 0 | **no progress** | θ₁ < θ₂ at the points of O₁ ∖ O₂ with e = 1 and θ₁ ≥ θ₂ elsewhere: no domination, so no contraction (Lemma D). Only s₁ ≤ b from Corollary K. |
| 4. a ≤ b/2 + O(1); is A′ ever non-vacuous | **partial** | empty for b ≤ 3 [computed]; unrestricted m: unbounded examples (Lemma M) [proved]; m ≤ 4, b ≥ 4 open. |
| 5. k = 4 | **partial (closed for the non-birational tools)** | Lemma Q. |

## 7. Where it is stuck, and what to try next

Stuck: all three new lemmas describe *that* a birational pair differs from the obstruction families (image not a
Klein graph; ρ₁ ≁ ρ₂; θ₁ ≠ θ₂) but give no lower bound for *how much*, and a degree bound needs exactly that.

Next, in order of expected value:
1. **A quantitative Lemma U.** In the reduced case O₁ = O₂, θ₁ − θ₂ is supported on ≤ s₁ + s₂ points with integer
   weights. w = ½·log(g₂/g₁) solves Δ_{g₁}w = e^{2w} − 1 with prescribed logarithmic poles there. A lower bound for
   |w| at distance r from the poles (Green function of Δ − 2 on a surface of area 2πa) combined with the trace gap
   at pairs of anchors (which forces the anchor distances in g₁ and g₂ to be *equal* in deep clusters, E14 §7) would
   contradict each other if the decay of w is slower than the rate at which the gap forces equality. This is the one
   idea here that has not been tested. Risk: w decays like e^{−√… r}, the same rate as in Lemma 2, and then nothing
   is gained.
2. **Slack-0 maps of degree 4** (monodromy enumeration plus the normal forms of E11 §9), to extend §5 to b = 4 and to
   test a ≤ b/2 + O(1) on (a, s₁, m) ∈ {(3, 1, 0), (2, 2, 0), (2, 1, 2)}.
3. **Use the component condition of E10 §5** (Stab(Z) ⊇ S), which Problem W ignores. Proposition C of E14 and Lemma U
   suggest that the conditions of Problem W alone may be too weak; the actual carrier condition has not been used in
   E13–E15 at all.
   **Done in §11: gives no bound.**
4. Exact certification of §5 (b = 3) in the style of E11 §9, if the statement is to be used.

## 8. Reproduction

From the repository root (outputs stored as `*.out`):

```
python3 -I stages/stage32/32-03-multibranch/MB104/route-E/e15/lattes5.py
python3 -I stages/stage32/32-03-multibranch/MB104/route-E/e15/aprime_b3.py
python3 -I stages/stage32/32-03-multibranch/MB104/route-E/e15/component_check.py
```

- `lattes5.py`: Lemma M, exact in Q(i)[x] (uses `e14/gq.py`). Ends `PASS`.
- `aprime_b3.py`: §5, b = 3 (needs numpy; a few seconds). Two controls; ends `PASS (test valid)`.
- Lemmas K, U, D, Q have written proofs and no script.

## 9. Audit points

1. Lemma K: each matched point on exactly two Klein graphs; the local order ≥ min(e₁, e₂), including points at ∞.
2. Corollary K: the use of E12 Lemma 0 (j ≥ |O_i| − |Ω|).
3. Lemma U: Δ log Im f = −|f′|²/(Im f)²; the maximum principle at a point where Q may vanish elsewhere; the descent
   to "p₂ factors through κ₁".
4. Lemma D: the cone angles θ_i; the local form of w; removability of the cone points for the bounded-above
   subharmonic function w⁺.
5. Lemma Q: the odd sets, the slack normalisation of E12 §2, and h_e becoming a square; that each transferred theorem
   of E13/E14 really does not use birationality or the label e.
6. §5: completeness of the reduction for b = 3 (the only case is (2, 1, 0)); numerical margins.

## 10. Addendum (same day): the quantitative version of Lemma U was tried — Theorem E, Lemma N, and why it stops

This is §7 item 1, carried out. **Outcome: no degree bound.** The expected contradiction does not occur, for a
reason that can be stated exactly (end of this section). Two statements are proved on the way.

Notation. X := X_∪ = (V₀; O₁ ∪ O₂) with hyperbolic metric g_X; H̃ its universal orbifold cover with group Π;
g_i = P̃_i^*(hyp) ≤ g_X; **v_i := ½·log(g_X/g_i) ≥ 0** (the "defect potential" of leg i) and
**w := ½·log(g₂/g₁) = v₁ − v₂**. So w ≤ v₁ and −w ≤ v₂. By E14 Proposition L(b), v_i ≤ −log tanh(R/2) at every point
that is R-deep for P̃_i. A *pole* of w is a point with θ₁ ≠ θ₂ (Lemma D); w → +∞ where θ₂ < θ₁ and −∞ where θ₂ > θ₁.

**Theorem E (pairs of anchors) [proved].** Let x̃ ≠ ỹ ∈ H̃ be lifts of anchors (points of O₁ ∩ O₂), d_i :=
d(P̃_i x̃, P̃_i ỹ), and η(d) := log(arccosh(cosh d + 1)/d) (decreasing in d; `e15/thme_constants.py`).
1. For every path γ from x̃ to ỹ: d₁ ≤ ∫_γ ds₁ and d₂ ≤ ∫_γ ds₂ = ∫_γ e^w ds₁.
2. Either d₁ = d₂ or |2cosh d₁ − 2cosh d₂| ≥ 2.
3. If the geodesic [P̃₁x̃, P̃₁ỹ] has a P̃₁-lift γ₁ from x̃ to ỹ and w < η(d₁) on γ₁, then d₂ ≤ d₁. Symmetrically with
   γ₂ and −w < η(d₂): d₁ ≤ d₂.
4. If both hold, then d₁ = d₂ and **min_{γ₂} w ≤ 0 ≤ max_{γ₁} w**: w is not of one sign on γ₁ ∪ γ₂.
5. In particular, if d₁ ≤ ℓ and every point of γ₁ is R-deep for P̃₁, and likewise for γ₂, P̃₂, with
   R > R_E(ℓ) := 2·artanh(e^{−η(ℓ)}), then d₁ = d₂. Values: R_E(ℓ_min) = 2.23, R_E(3.2) = 4.41, R_E(6.4) = 8.26.

*Proof.* (1) P̃_i is a local isometry from g_i to H, so the image of γ is a path of the same length joining the two
image points. (2) ρ_i(e_x̃), ρ_i(e_ỹ) are elliptic involutions of Γ₀ fixing the image points (a loop around an odd
point maps to an odd power of the local generator), so 2cosh d_i is the trace of a product of two elliptic
involutions of Γ₀, or 2; E13 Lemma 1(b), (b′). (3) By (1), d₂ ≤ e^{max w}·d₁ < e^{η(d₁)}d₁ = arccosh(cosh d₁ + 1),
so 2cosh d₂ < 2cosh d₁ + 2 and (2) gives d₂ ≤ d₁. (4) d₁ ≤ ∫_{γ₂} e^{−w} ds₂ and d₁ = d₂ = ∫_{γ₂} ds₂ give
∫_{γ₂}(e^{−w} − 1) ds₂ ≥ 0; likewise ∫_{γ₁}(e^{w} − 1) ds₁ ≥ 0. (5) w ≤ v₁ ≤ −log tanh(R/2) < η(ℓ) ≤ η(d₁), so d₂ ≤ d₁ ≤ ℓ by (3); hence η(d₂) ≥ η(ℓ) > v₂ ≥ −w and
(3) also gives d₁ ≤ d₂. □

- This is E13 Lemma B1 **at any slack, with a complete proof**, and with a smaller radius (the pair statement of the
  outline Theorem B′ of E14 §7). It does not replace Lemmas B2–B6.
- E14 Theorem A′(1)–(2) is the case v₂ ≡ 0: then w = v₁ > 0, so (4) is impossible and every short pair of anchors
  is near a defect of leg 1.

**Lemma N (nodal domains) [proved].** Every connected component of {w > 0} contains a pole with w = +∞, and every
component of {w < 0} a pole with w = −∞. So {w ≠ 0} has at most #poles components: ≤ s₁ + s₂ in the reduced case
O₁ = O₂, and ≤ |O₁ Δ O₂| ≤ 4 at slack (0, 0) (exactly two for type (1, 1), so there {w = 0} is one simple closed
analytic curve).

*Proof.* On a component D of {w > 0} without such a pole, w is finite and continuous on the closure, 0 on ∂D, and
Δ_{g₁}w = e^{2w} − 1 > 0 away from the common cone points, where w is bounded (removable). The maximum principle
gives w ≤ 0 on D. For type (1, 1): the zero set of a real-analytic solution is a graph with all vertices of even
valence ≥ 4 or none; with two faces on the sphere, Euler's formula leaves only one simple closed curve. □

**Corollary E–N (balance) [outline: Harnack constant not computed; the hypothesis that γ₁ ∪ γ₂ stays at distance ≥ 1
from the poles is assumed, not implied by Theorem E(5)].** v_i > 0 solves
Δ_X v_i = 1 − e^{−2v_i} = c_i(x)·v_i with 0 < c_i ≤ 2 away from its poles, so v_i satisfies a Harnack inequality
with a constant H(r) on balls of radius r at distance ≥ 1 from the poles. With Theorem E(4): for every pair of
anchors as in (5), **H⁻² ≤ v₁/v₂ ≤ H²** on γ₁ ∪ γ₂. The two legs' defect potentials are comparable at every short
deep pair of anchors; if one leg has no defects (v ≡ 0) there are no such pairs (Theorem A′).

**Why this does not bound the degree (the precise point where it stops).**
- Idea tested: "w decays away from its poles, while the trace gap forces exact equalities; exact equalities should
  force w = 0." The second half is false. The trace gap forces d₁ = d₂ for pairs of anchors (Theorem E), and that is
  **equivalent** to: h := g⁻¹ ∘ P̃₂ ∘ (P̃₁)⁻¹ fixes the anchors. A holomorphic map fixing a discrete set of points is
  not the identity, and w = log|h′|_hyp need not vanish; it only cannot have one sign along the edge (E(4)).
- So the decay rate of w never enters a contradiction. The threshold in Theorem E is the fixed number η(ℓ), not a
  quantity that shrinks with the distance to the poles.
- Balance does not help either: v_i behaves like Σ_{poles q} e^{−2d(·, q)}, and on a surface of area 2πa most points
  are at distance log a + O(1) from any given point, so "v₁ ≍ v₂" holds on a positive proportion of the surface for
  generic positions of the poles. [heuristic, not proved]
- Lemma N bounds the *number* of nodal domains, not the length of {w = 0}; a long curve can pass through every edge.

**What the attempt leaves as the sharpest formulation of the core.** In every open configuration (after the double
cover): two positive potentials v₁, v₂ on X with different pole sets, each of total mass
∫_X (1 − e^{−2v_i}) = 2π·cost_i, such that for every short deep pair of anchors the map h fixes both anchors. A
bound needs a rigidity statement for holomorphic h : B(c, R) → H commuting with the involutions at ~30–70 anchors in
the disc (h is ε(R, L)-close to the identity by E13 Lemma B2) — i.e. a lower bound for |h − id| in terms of w at the
poles. None was found. **Stuck here.**

Updated verdicts: item 1 unchanged (not closed); item 3 unchanged; E14 Theorem B′'s first step (equal distances) is
now proved at any slack (Theorem E). Reproduction: `python3 -I …/e15/thme_constants.py` (ends `PASS`).

Audit points for §10: (i) Theorem E(2): ρ_i(e) is an elliptic involution for every anchor, also non-standard ones;
(ii) E(3): the existence of γ₁ is a hypothesis, not a claim; (iii) Lemma N: boundedness of w at common cone points
with equal angles, and the Euler count; (iv) the Harnack statement is qualitative.

## 11. Addendum (2026-11-12): the component condition of E10 §5 was examined once — no route to a degree bound

This is §7 item 3, carried out once, as asked. **Outcome: no degree bound, and no line of argument towards one.**
The condition is translated exactly (Lemma C1), shown to be a non-degeneracy condition carrying a bounded amount of
information (Lemma C2), and shown not to separate birational from non-birational pairs (Proposition C′). Stopped here.

Notation. Ĝ ≅ subsets of {a, b, e}: χ ↔ S_χ, q_χ = ∏_{c ∈ S_χ} q_c. For a leg p_i put
**O_i^c** := points of O_i with label c, and **O_i^χ** := ∪_{c ∈ S_χ} O_i^c (O_i^1 = ∅).

**Lemma C1 (the condition, exactly) [proved].** Let R := {(χ, ψ) ∈ Ĝ×Ĝ : q_χ(p₁)·q_ψ(p₂) is a square in K(V₀)}.
For a birational pair, with Z a component of the preimage of W in C8×C8:
Stab(Z) ⊇ ΔG ⟺ R ⊂ {(χ, χ)} ⟺ **O₁^χ ≠ O₂^ψ for all χ ≠ ψ**.

*Proof.* K(Z) = L = K(V₀)(√q_χ(p₁), √q_ψ(p₂)) (E10 §1), a Kummer extension with group H = R^⊥ ⊂ G×G; G×G is
abelian, so H is the stabilizer of every component. H ⊇ ΔG ⟺ R ⊂ (ΔG)^⊥ = {(χ, χ)}. The divisor of q_c on P¹_t is
odd exactly on B_c, and the sets B_c are disjoint, so the odd locus of q_χ(p₁)·q_ψ(p₂) on V₀ is O₁^χ Δ O₂^ψ; on
V₀ ≅ P¹ a function is a square iff its divisor is even. □

- R ∩ {(χ, χ)} = Q (E10 §1), so the condition says [L : K(V₀)] = 8δ, the value E10 §1 uses.
- Special case ψ = 1: no q_c(p_i) is a square, i.e. **no label class O_i^c is empty**, i.e. p_i does not factor
  through the double cover of P¹ branched at B_c.
- For a non-birational pair the middle statement still makes sense; call it condition (C).

**Lemma C2 (when it can fail) [proved].** If O₁^χ = O₂^ψ with χ ≠ ψ, then for every label c ∈ S_χ Δ S_ψ all
label-c points of O₁ ∪ O₂ lie in Ω; so |O₁^c ∪ O₂^c| ≤ |Ω| ≤ 4 and J has no point of label c.
Conversely, **if every label occurs in J, the condition holds.** In particular it holds if o₁^c ≥ 5 for all c.

*Proof.* Let c ∈ S_χ ∖ S_ψ. A label-c point of O₁ lies in O₁^χ = O₂^ψ, so it is in O₂ with a label ≠ c: a
label-differing point, hence in Ω (E10 §2). A label-c point of O₂ is not in O₂^ψ = O₁^χ, so it is not in O₁ with
label c: it is in O₂ ∖ O₁ ⊂ Ω or label-differing. The case c ∈ S_ψ ∖ S_χ is symmetric. For the converse: a matched
point of label c lies in O₁^χ Δ O₂^ψ whenever c ∈ S_χ Δ S_ψ; and a label-c point of O₁ outside Ω is matched. □

**What this means for the core.**
- The condition is a list of at most 56 inequations O₁^χ ≠ O₂^ψ, each witnessed by a single point. It **excludes** a
  thin set of solutions of Problem W (some label class of O₁ ∪ O₂ inside Ω) and says nothing about the others. Its
  content does not grow with (a, b). A degree bound needs information that grows with the degree (as the trace gap
  at ~a anchors does); the condition supplies none. [proved, by C1–C2]
- It is not a restriction "almost never": legs with a thin label class exist in every degree 2ⁿ (below). But a
  hypothetical carrier satisfies it by definition, and then C2 only says "each label class meets J or is not
  covered by Ω". Nothing in E13–E15 becomes stronger with this input.

**Proposition C′ (the obstruction of E14 Proposition C survives the component condition) [proved; checked exactly].**
Let f be the degree-5 map of Lemma M and f_n its n-th iterate.
1. f_n has slack 0, degree 5ⁿ, and B ⊂ O_{f_n} with f_n(β) = β (f fixes B pointwise and is unramified there). So
   every label class of f_n is non-empty.
2. f_n(t² + c) has slack 1 for c outside a finite set (E14 Proposition F(3), as in E14 §6 item 2: ∞ ∈ O_{f_n},
   c ∉ O_{f_n}), degree 2·5ⁿ, a free parameter c, and non-empty label classes.
3. The pairs (p, −p), p = f_n or f_n(t² + c), have O₁ = O₂ with equal labels, Ω = ∅, and satisfy (C) (by C1:
   O^χ = O^ψ forces S_χ Δ S_ψ ⊂ {empty classes} = ∅). They are not birational (image y = −x).

So **the set 𝓗 of E14 Proposition C, intersected with condition (C), still has unbounded degree at slacks (0, 0)
and (1, 1), the latter in one-parameter families.** Proposition C (ii)–(iii) hold with (C) added: metric and
holonomy tools plus the component condition cannot bound the degree; birationality itself is still needed.

- Correction to the picture in E14 §6 (not to its statements): the families (L_n, −L_n) and
  (L_n(t² + c), −L_n(t² + c)) **violate** (C). The label class b of L_n is empty for every n (the fibre of L_n over
  ±1 is L_{n−1}⁻¹(±i), entirely of index 2), so q_b(L_n) = 1 − L_n² is a square. E14 Proposition C is correct as
  stated (it concerns Problem W, which ignores (C)), but its example families are not evidence about carriers. The
  f-families above are.
- *Exact check* (`e15/component_check.py`, Q(i)[t], no floating point): label classes e/b/a = 4/0/2ⁿ⁺¹ for L_n
  (n ≤ 4) and 6/0/2ⁿ⁺² for L_n(t² + 2) (n ≤ 3); 2/2/10 for f, 2/2/50 for f∘f, 2/4/20 for f(t² + c)
  (c = 2, 1/3 + i/2), 2/4/100 for f(f(t² + 2)), with slacks 0, 0, 1, 1. Ends `PASS`.

**Why I stop here (as asked: one look, no rephrasing).**
- (C) is the only part of "being a carrier" that Problem W omits (E10 §5). By C1 it is a statement about label
  classes only. It does not see the map Φ = (p₁, p₂) beyond the sets O_i^c, and these are the same for a birational
  pair and for the non-birational pairs of Proposition C′.
- Hence the open core is unchanged: **a degree bound must come from birationality, and E13–E15 contain no tool
  that uses it quantitatively** (Lemma K uses it linearly; Lemmas U, D only qualitatively). No further idea is
  proposed in this section.

Verdict for §7 item 3: **failed** (examined; gives no bound). By-products: Lemma C1, Lemma C2 [proved];
Proposition C′ [proved, checked exactly].

Audit points for §11: (i) C1: H = R^⊥ and that the stabilizer of the image curve Z̄ equals that of the component
of the normalized fibre product (birational case); (ii) C2: the use of "label-differing ⇒ in Ω" and O₁ Δ O₂ ⊂ Ω;
(iii) C′(2): that c avoids O_{f_n} and that t² + c is unramified over the other points of O_{f_n}; (iv) that
−B_c = B_c makes the labels of p and −p equal.

## 12. Audit history
- 2026-11-12, reading audit by Claude (not the author session) at head 140a7a993: **PASS**, no must-fix; all four
  scripts rerun, all `PASS`. Two should-fix items applied in the same commit: Theorem E(5) now states the step
  d₂ ≤ d₁ ≤ ℓ before the symmetric condition; Corollary E–N relabelled [outline] (its distance-to-poles hypothesis is
  an assumption). Details: `AUDIT-CLAUDE-E15-20261112.md`.
