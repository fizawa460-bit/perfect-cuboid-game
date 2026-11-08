# E12 — Problem W at small bidegrees (k = 8 and k = 4, all rows), rigidity per degree, and the single open core (2026-11-08)

Status: research note, **not audited, zero credit**. STATE is not changed. Working logs: `stage32_research/32R-91` …
`32R-95` (local). Code: `problemw/` (research code, paths relative to its own folder).

- It extends E10/E11 in four directions:
  - an exact (mod p) search for Problem W of bidegree (2, 2), k = 8, at every slack (§1), replacing the floating-point
    search of E11 §4 for (2, 2);
  - the k = 4 version of Problem W ("W₄", §2) and its bidegree (2, 2);
  - the γ = 1 row and the genus-0 row that E10 §5 left out (§3);
  - a rigidity lemma (§4) that reduces everything open in route E to **one** statement (§5).
- By user decision of 2026-11-08 the core (§5) is parked: further attempts only with a new tool or idea.

Notation as in E10 (k = 8: B = {0, ∞} ∪ {±1} ∪ {±i} with labels e, b, a) and E06/E08 (k = 4: B = μ₈, labels
u = primitive 8th roots, v = μ₄). W ⊂ P¹×P¹ of bidegree (a, b), V₀ its normalization of genus γ, Σo_i, j, h, Ω,
slack s_i, S = s₁ + s₂, δ = deg(E → V₀).

## 0. A lemma used throughout (sharpens E10 §2)
**Lemma 0.** O_i \ Ω ⊆ J. Hence j ≥ max(Σo₁, Σo₂) − |Ω| and |Σo₁ − Σo₂| ≤ |Ω|.
*Proof.* v ∈ O₁ with label χ means "p₁(v) ∈ B_χ with odd local degree". If v ∉ Ω, the same statement holds for p₂
and the same χ, so v ∈ O₂ with the same label. Also j ≤ |O₁ ∩ O₂| ≤ min Σo_i. □

## 1. k = 8, bidegree (2, 2): exact search mod p, all slacks (`problemw/w22`)
Passing through a point of B×B is linear in the 9 coefficients of W, so the conditions of E10 §2 with Lemma 0 become
linear-plus-discriminant problems. Arithmetic mod p = 10009 (i = 6706) and p = 30089 (i = 8086); every count below
is identical at both primes.
- **≥ 8 points of B×B** (`w22.c`): 2,483,637 rank-8 curves, 66 with |Ω| ≤ 4 and no fibre line, all products of two
  (1, 1) curves. 143,874 pencils through ≥ 8 points; 32,886 coprime; |Ω| evaluated at every event value of the
  pencil parameter (an extra point: linear; a fibre discriminant: quadratic, roots in F_p or F_p²), at ∞ and at a
  generic value: 240 irreducible members with |Ω| ≤ 4, all with |Ω| = 4 and **smooth**, so γ = 1 and
  g = 1 + δ ≥ 3 (E10 §2 RH).
- **Node of W at a point of B×B** (`w22g.c`, two orbits under the 96 label-compatible pairs): 25,611 curves and
  2,818 families per case; 5 hits, all reducible; family hits none irreducible.
- **Slack 1** (`slack1.py`, `netchk.py`): exactly 7 label-matched points; 768 pencils (816 hits, none irreducible),
  24 nets (each with a common component: 6 of the points lie on one Klein graph Γ, W·Γ = 4 < 6).
- **Slack 0** (`slack0.py`, `mkdec.py`, `s0C_eval.py`, `nnetchk.py`): 7 points with j ≥ 5 (231,072 pencils), 6
  matched points (920 nets: common zeros of two x- and two y-discriminants, minAssGTZ, 8,616 primes, all
  F_p-rational), node + 4 matched points (320 pencils). Irreducible hits: 48, all smooth (g ≥ 3). Families of
  higher dimension (10,502): all with a common component.
- Positive control: bidegree (1, 1) with the same |Ω| count gives exactly the 16 octahedral graphs of E06.
- **Result (k = 8, (2, 2)): no W with γ = 0 satisfying E10 §2 at any slack, at two primes.**
- Caveats: (i) reduction mod p is assumed good for the unknown field of definition; (ii) discarding a candidate
  because it is reducible mod p is not by itself a characteristic-0 statement (the R2 audit's M1 point). Exact
  certification of the reducible rank-8 hits over Q(ζ₈) is not done yet.

## 2. k = 4: Problem W₄ and bidegree (2, 2) (`problemw/w4`)
- K(E) = K(V₀)(√h_u, √h_v), h_u = (1 + x⁴)(1 + y⁴), h_v = (1 − x⁴)(1 − y⁴); δ ∈ {1, 2, 4}; the same RH equality
  2g − 2 = δ(2γ − 2) + (δ/2)|Ω| and the same identity |Ω| = Σo₁ + Σo₂ − 2j − h.
- **Riemann–Hurwitz on (P¹; 2⁸)**: Σo_i ≥ 4·deg p_i + 4 − 4γ (8 branch values instead of 6).
- Consequences (γ = 0, g = 1): j ≥ 4·max(a, b) + 2·max(s_i) (every unit of slack forces 2 more points);
  |2(a − b) + (s₁ − s₂)| ≤ 2; and from the 8 label-preserving graphs ρ ↦ ζρ, ζ/ρ (ζ ∈ μ₄), each of the 32
  label-matched points lying on exactly two of them: Σ_{v ∈ J} min(e₁, e₂) ≤ 4(a + b).
- **(2, 2), mod p = 10009 (ζ₈ = 792):** W through ≥ 8 matched points covers every row (g = 0, 1; γ = 0, 1; all
  slacks). 2,658,092 rank-8 curves → 28 hits, all reducible over F_p²; 196,116 pencils → 9,072 hits, **8
  irreducible**; node at a matched point (one orbit): 9,913 curves → 1 hit (reducible), 3,568 pencils → 12 hits
  (none irreducible).
- **The 8 irreducible hits** are smooth, |Ω| = 0, and are exactly the pullbacks under (x, y) ↦ (x², y²) of the 8
  E06 Möbius graphs with |Δ| = 4 whose pullback is irreducible (`w4_ctrl.py`). Their preimage in C8×C8
  (u² = ρ⁴ + 1, v² = ρ⁴ − 1) has 8 components of degree 2 over V₀, hence of degree 4 = deg(C8 → P¹) over each
  factor: **graphs of automorphisms of C8** (genus 5 checked), with stabilizer an order-4 subgroup **different from S**
  (`w4_lift.sing`). So they are not k = 4 carriers for S; in their own model they are E04/E07 graphs.
- **Result: Problem W₄ of bidegree (2, 2) has no solution with stabilizer S** (one prime; caveats as in §1).
- (2, 3): rank-11 curves through ≥ 12 matched points: 6,481,696, none with |Ω| ≤ 4 (`w4_23.c`). The 438,916 pencils
  and 5,096 nets are not analysed yet (fibre-discriminant events of degree 4 in the parameter).

## 3. The γ = 1 row and the genus-0 row (k = 8)
- **γ = 1:** RH gives g = 1 and Ω = ∅. With Lemma 0: O₁ = O₂ = J, h = 0, j = Σo₁ = Σo₂ = 2·deg p_i + 2s_i.
- **(2, 2), exact (Q(i), sympy).** W is smooth (p_a = 1). Block lemma: an unramified p₁-fibre over β ∈ B_χ has two
  odd points, both in J, with distinct y-values in B_χ, i.e. {β} × B_χ; symmetrically for p₂. So J is a union of
  label blocks B_χ × B_χ, j ∈ {4, 8, 12}.
  - j = 4 (J = {0, ∞}²): W = a x²y + b xy² + c xy + d x + e y; ramification over ±1, ±i on both sides forces W = 0.
  - j = 8 (J = {0, ∞}² ∪ {±1}²): W = a y(x² − 1) + b x(y² − 1), ramification over ±i forces a = ±b, and then
    W = b(x + y)(xy − 1) or −b(x − y)(xy + 1): reducible.
  - j = 12: the j = 8 family through (i, ±i) forces W = 0.
  - **No solution.** (Exact; no reduction mod p; no assumption on the stabilizer.)
- **(2, 3) and (3, 2)** (`problemw/gamma1`). p_a = 2, so W has one singular point (δ = 1). On the cubic side an odd
  point over b ∈ B_χ has x ∈ B_χ (2 values), so three odd points over b need the singular point: o_b = 3 for at most
  one b, s₂ ∈ {0, 1}. With the block lemma on the quadratic side: 8 cases with j = 6 (one block per label) and 48 with
  j = 8 (singular point at (β₀, b₀), β₀ ∈ B_χ(b₀)). All conditions are homogeneous in the 12 coefficients over
  Z[i, 1/6]. **All 56 systems are projectively empty mod 10009** (`g1_23_p.out`). A solution over Q̄ would reduce to a
  nonzero solution mod a prime above p (primitive scaling; both embeddings of i permute the case list), so **there is
  no solution in characteristic 0**. This is the valid direction (existence descends), unlike §1 caveat (ii).
- **Genus 0:** γ = 0 and |Ω| ≤ 3 (δ ∈ {1, 2, 4}). The point conditions are stronger than for g = 1, γ = 0 (2j + h
  larger, j ≥ 2·max(a, b) + 4 − |Ω|), so every search that keeps |Ω| ≤ 4 already contains them: §1, E11 §4b, §2.
- (3, 3) with γ = 1 is not done.

## 4. Rigidity per degree
**Lemma R.** For fixed d, the integral curves C̄ ⊂ B of geometric genus ≤ 1 are finitely many.
*Proof.* S (minimal resolution) is minimal of general type (K_S² = 16 > 0, K_B ample, E09 §0). Curves of degree d form
a finite-type Hilbert scheme. A positive-dimensional family of curves of geometric genus ≤ 1 would sweep out S, so S
would be dominated by a surface fibred over a curve in curves of genus ≤ 1, of Kodaira dimension ≤ 1; but a dominant
generically finite map Y → S gives κ(Y) ≥ κ(S) = 2. Hence the locus is zero-dimensional, hence finite. □
- **For Problem W:** at fixed (a, b), the genuine solutions (W with a preimage component Z with Stab(Z) ⊇ S, giving a
  curve of genus ≤ 1 of degree d = 8δ(a + b)/k) are finitely many. So the slack ≥ 1 families of E10 §5 are cut down to
  finitely many members by the matching conditions (in the per-bidegree sense asked in E10 §5). Positive-dimensional
  solution sets of the *necessary* conditions can only consist of artifacts with a smaller stabilizer (as the 8 hits of
  §2).
- It does not bound (a, b).

## 5. The single open core
- With Lemma R, everything open in route E is **one statement: a uniform degree bound for multibranch curves of
  geometric genus ≤ 1 on B** (equivalently a bound on the bidegree in Problem W, W₄). Below such a bound every case is
  a finite computation of the kind in §1–§3.
- This is FSM Thm 3.1 (d ≤ 176 + 16g, audited W29-A) without its hypothesis "bijective normalization". Stage29 already
  recorded `MULTIBRANCH_RESIDUAL_OPEN=true`.
- Why the known tools stop (all recorded before): in Langer's orbifold BMY (E09) the node term
  (3/2)α Σ_p Σ_j (2 − c_j) is bounded for unibranch curves (≤ 2·48) but is ≈ r ≥ d for multibranch ones (E03), which
  is E09's (R2); E10 §4 shows the δ = 8 near-balanced curves sit in the blind spot. Bogomolov's finiteness needs
  c₁² > c₂, and S has 16 < 80; on the orbifold B (16 > 8) the symmetric differentials acquire poles at the odd-contact
  branches (E09 §2.3). Literature: the level-8, (Z/2)³-twisted case of the function-field Frey–Mazur question;
  Bakker–Tsimerman (Ann. Math. 2016) need large prime level and are ineffective.
- **Assessment (user rule):** every reformulation returns here; no tool found; computation cannot bound the degree.
  Parked by user decision, 2026-11-08.

## 6. What is still finite and open (not the core)
1. k = 4, (2, 3): the 438,916 pencils and 5,096 nets (§2).
2. γ = 1, (3, 3), k = 8.
3. Exact certification of the reducible rank-8 hits (§1, §2) over Q(ζ₈), and a second prime for §2.
4. k = 8, (2, 3) at all slacks (exact search with the h ≥ 2 refinement for the six-point reps: in progress locally).

## 7. Reproduction (research code)
- `problemw/w22/`: `gcc -O2 w22.c -o w22 && ./w22` (about 4 min); the family / slack scripts take the `w22`/`w22g`
  output as input (usage lines at the top of each file).
- `problemw/w4/`: `w4_22.c` (about 3 min), `pw4fam.py 10009 792 0 w4_22.out` (about 1.5 h), `w4node.py`,
  `w4node_eval.py`, `w4nodefam.py`, `w4_ctrl.py`, `w4_lift.sing`; `w4_23.c` (about 1 h).
- `problemw/gamma1/`: `python g1_23_mk.py` writes the Singular file; the mod-p version is the same file with the
  field changed to 10009 and I ↦ 6706 (`g1_23_p.out` is its output: 56 lines, all `dim 0`).
