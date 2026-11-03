# E09 — Orbifold BMY on the box variety: an exact inequality, and what it would take to bound d (2026-11-03)

Status: research note, **audit round 2 PASS at f1ceb4b9 (revision 2; round-2 should-fixes applied), zero credit**. No exclusion and no finite window are claimed.

- It records an exact necessary inequality for every curve of the MB101 population, obtained from Langer's logarithmic orbifold BMY inequality on the singular surface B.
- It explains why this and the related Chern-number inequalities (Miyaoka 2008, Bogomolov) do **not** by themselves bound d.
- It isolates two quantities, β and ν (§2), that a uniform degree bound would have to control.
- The algebra and the numerical thresholds are checked in `bmy/e09_check.py`.

## 0. The surface B as an orbifold

- B = (C8×C8)/G, with G ≅ (Z/2)³ acting diagonally. Three involutions s_a, s_b, s_e fix 8 points each on C8; the other four are free.
- Fixed points on P = C8×C8: 3·64 = 192 points, each with stabilizer of order 2, so B has **48 A₁ points** (the nodes p) and no other singularities.
- Numbers:
  - e(B) = (1/8)·(64 + 3·64) = 32;
  - e_orb(B) = e(P)/8 = 8, i.e. e(B) − 48·(1/2);
  - K_B² = K_P²/8 = 128/8 = 16, and K_B is ample.
  - For comparison, on the minimal resolution S: c₂(S) = 32 + 48 = 80 and K_S² = 16.
- For a curve C̄ of the population, d = K_B·C̄. This follows from K_B·C̄ = 8(n₁ + n₂)/k and F71's n₁ + n₂ = kd/8.

The point of working on B: the "Bogomolov" condition K² > e holds for the orbifold (16 > 8) but fails on S (16 < 80). This is why Miyaoka's inequality on S only bounds imbalanced degrees (the old F82 HOLD).

## 1. The exact inequality

**Notation.** Let C̄ ⊂ B be an integral curve with normalization of genus g ≤ 1 and d = K_B·C̄. Define:

- **interior singular points** P (singular points of C̄ in the smooth locus of B): multiplicity m_P, number of branches r_P ≤ m_P, and δ-invariant δ_P;
- **nodes** p on C̄: m_p = C̃·E_p, the total contact. The branches of C̄ at p have contacts c_j ≥ 1, with Σ_j c_j = m_p;
- M = Σ_p m_p;
- δ_E ≥ 0, the δ-invariant of C̃ at points on the exceptional curves.

**Theorem E09.** Let 0 < α < 1 (first α rational; see the last step of the proof) with α·m_P ≤ 1 at every interior singular point and α·m_p ≤ 1 at every node on C̄. Then

(2α − α²)·d ≤ 8 + (3α − α²)(2g − 2) + Σ_P [3α(r_P − m_P) + α²(3m_P²/4 − 2δ_P)] − 2α²δ_E + Σ_p [ (3/2)α Σ_j(2 − c_j) − (α²/8)·m_p² ].

*Proof.*

- **Langer's theorem applies.** The pair (B, αC̄) is log canonical:
  - at an interior point, lct ≥ 1/mult;
  - at a node, the pair is log canonical iff its lift to C² is, and the lifted germ has multiplicity m_p (see below).
- **The positivity hypothesis.** Langer's Thm 0.1 asks only that some multiple of K_B + αC̄ be effective (no nefness). K_B is ample and C̄ is effective, so this holds for rational α.
  - Revision 1 argued nefness from C̄² ≥ 2g − 2 − d instead. That argument was incomplete for g = 0 (it needs (1 − α)d − 2α ≥ 0) and is not needed; it is withdrawn.
- So Langer, Thm 0.1, gives (K_B + αC̄)² ≤ 3·e_orb(B, αC̄) for rational α.
- **Computing e_orb(B, αC̄)** with Langer's definition:
  - e_orb(B, αC̄) = 8 + α(2g − 2) + α·Σ_{P∪p} r + Σ_P (e_P − 1) + Σ_p (e_p − 1/2).
  - At an interior point, Langer (0.2.3) gives e_P ≤ (1 − αm_P/2)².
  - At a node, e_p = e_orb(0; C², α·lift)/2 ≤ (1 − αm_p/2)²/2.
  - **The lifted germ at a node has multiplicity m_p.** Let ρ be the double cover branched along the exceptional curve E′ of the blow-up of C². Then ρ*E = 2E′, so C̃·E = L̃·E′, where L̃ is the strict transform of the lifted germ.
- **The left side.**
  - (K_B + αC̄)² = 16 + 2αd + α²C̄².
  - C̄² = C̃² + Σ_p m_p²/2, because π*C̄ = C̃ + Σ(m_p/2)E_p (π : S → B the minimal resolution) and E_p² = −2.
  - C̃² = 2g − 2 − d + 2Σ_P δ_P + 2δ_E, by adjunction on S with K_S·C̃ = d.
- **Collecting terms.**
  - The two node terms combine: 3αr_p − (3/2)αm_p = (3/2)α Σ_j (2 − c_j).
  - The quadratic node term: (3/8)α²m_p² − (1/2)α²m_p² = −(1/8)α²m_p².
  - Collecting everything gives the stated inequality for rational α.
- **Real α.** Both sides are polynomials in α, and the conditions α·m ≤ 1 define a closed interval. Rational α are dense in it, so the inequality holds for all real α in the range. □

**Simplified form.** At an interior point, r_P ≤ m_P and δ_P ≥ m_P(m_P − 1)/2, so the interior term is at most α²·(m_P − m_P²/4). This is 1 for a double point, 3/4 for a triple point, and ≤ 0 for m_P ≥ 4. Put:

- β := Σ_p Σ_j (2 − c_j) = 2R − M, where R is the number of node branches. Each contact-1 branch adds 1, each contact-2 branch adds 0, and higher contacts subtract.
- ν := Σ_P max(0, m_P − m_P²/4), the "cheap singularity count": ordinary double and triple points.
- σ := Σ_p m_p² ≥ M²/48.
- β can be as large as M (all contacts 1). When β ≥ (4/3)d the Corollary below is empty.

Then, dropping δ_E ≥ 0,

**(2α − α²)·d ≤ 8 + (3α − α²)(2g − 2) + (3/2)α·β + α²·(ν − σ/8).**  (E09)

## 2. What (E09) does and does not give

Put α = t/d. For g = 1, (E09) reads

(2 − (3/2)·β/d)·t − ((ν − σ/8)/d²)·t² − t²/d ≤ 8.

**Corollary (conditional degree bound).** Suppose that for some constants λ < 4/3 and κ > 0:

- β ≤ λd;
- ν − σ/8 ≤ κd²;
- (2 − (3/2)λ)² > 32κ;
- the log-canonical condition holds for α = t*/d, with t* = (2 − (3/2)λ)/(2κ).

Then d ≤ t*² / ( (2 − (3/2)λ)²/(4κ) − 8 ). (Similarly for g = 0.)

**Why this does not close MB104 by itself.**

1. **Nodes loosen the inequality (the β term).**
   - Every contact-1 branch through a node adds (3/2)α to the right side. In the orbifold sense, passing through a ½-point makes the curve *more* hyperbolic, not less.
   - Since M ≥ d, a curve with all contacts 1 has β = M ≥ d, so λ ≥ 1. In the boundary case λ = 1 (β = d), only (2 − 3/2)² = 1/4 is left on the left; for λ > 1 even less is left, and for λ ≥ 4/3 nothing.
   - Then the criterion needs **ν − σ/8 < d²/128**. With σ ≥ M²/48 ≥ d²/48, this holds once **ν < d²/96**, i.e. fewer than about d²/96 ordinary double points in the interior.
2. **The cheap interior singularities (the ν term).**
   - Hodge index on B only gives C̄² ≤ d²/16, hence ν ≤ δ_int ≤ about d²/32 + d/2. This is three times too weak.
   - Conversely, Miyaoka's inequality on S (factor 3c₂ − K² = 224) gives δ_S ≥ d²/224 − d for g = 1. So a genus-1 curve of large degree **must** have many singular points.
   - So there is a window, roughly d²/224 ≲ δ ≲ d²/96, in which (E09) would bite, but nothing presently forces ν into it.
3. **Bogomolov-type symmetric differentials.**
   - For B, the G-invariant symmetric differentials come from the orbifold line (P¹; 2⁶) or (P¹; 2⁸).
   - Pulled back to E, they acquire poles exactly at the points of odd contact. This looks like the F72 deficiency bookkeeping again. That it gives no new information is a heuristic remark, not a proved statement.

## 3. Reduction statement and next step

- For large d, a uniform degree bound for MB104 by this route **needs one of**:
  - **(R1) few cheap interior singular points:** ν ≤ (1/96 − c)·d² for some c > 0 (case β ≈ d), or the corresponding bound from the Corollary for general β;
  - **(R2) few contact-1 node branches:** β ≤ λd with λ < 1. For example, many contacts ≥ 2 — but then ε = (A₁ + A₂)/k + (M − B_o) grows.
- **Next step:** compute ν, or at least δ_int, from the co-image structure of E06–E08 (bidegree (a, b), a, b ≥ 2). The interior singular points of C̄ come from:
  - self-crossings of Z̄ ⊂ C8×C8;
  - Z̄ ∩ gZ̄ for g ∉ S.
- The trade-off between (R1)/(R2) and ε (F71) is open. **Nothing here excludes a curve.**

## 4. Inputs to audit

1. Langer, *Logarithmic orbifold Euler numbers of surfaces with applications*, Proc. LMS 86 (2003), arXiv:math/0012180:
   - Thm 0.1: normal projective surface, boundary coefficients in [0, 1], (X, D) log canonical, and some multiple of K_X + D effective (no nefness needed). One round-1 auditor checked this against the paper; the other did not inspect it;
   - the local bound (0.2.3);
   - the quotient rule e_orb(p; X, D) = e_orb(0; C², lift)/|Γ|.
   These were checked against the paper in audit rounds 1 and 2: Thm 0.1, (0.2.2) (quotient formula, quasi-étale of degree 2 at A₁ points), (0.2.3) = Cor 7.8, Def 3.4. D is a Q-divisor, hence rational α first, then real α by continuity.
2. Miyaoka, PRIMS 44 (2008), Thm 1.3, as recorded in STATE.retained_frontier.e2_unique_pair_miyaoka_energy_bound.
3. The orbifold numbers in §0, and the identity d = K_B·C̄.
4. The lift multiplicity m_p = C̃·E_p at an A₁ point.

## 5. Reproduction

```
python -I -O stages/stage32/32-03-multibranch/MB104/route-E/bmy/e09_check.py
```

It checks the symbolic collection of terms in §1 (the identity is additive in the local terms, so one interior point and one two-branch node represent all cases), the E04 equality-face curves (not Satake boundary curves), and the thresholds 1/128 and 1/96 in §2. It ends with `PASS`.

## 6. Audit history

- **Round 1** (two auditors, head 5e199e66).
  - Auditor A (Claude, executing; checked Langer arXiv:math/0012180): no must-fix. Should-fix: wrong citation "K + D nef" (the paper asks for an effective multiple), unneeded nefness argument with a g = 0 gap, β range, the unproved "no new information" remark, script wording, ρ vs π.
  - Auditor B (did not inspect Langer): HOLD, must-fix M1 = the nefness argument is insufficient for g = 0. Should-fix: coefficient domain (real α), coverage of the term check, and that a symbolic PASS does not certify Langer's hypotheses.
  - Fixed in revision 2: the nefness step is removed and replaced by the effective-multiple hypothesis; α is taken rational, then real α by continuity; the other items are addressed above.
  - Not changed: `e09_check.py` verifies only the algebra. Log canonicity and the applicability of Langer's theorem rest on the cited paper and the arguments in §1.

- **Round 2** (Claude, executing, head f1ceb4b9): PASS. M1 fixed; Langer hypotheses (effective multiple, Q-divisor, normal surface, quotient formula at A₁ points) and the log-canonical conditions confirmed; no new must-fix. Should-fixes applied: stale "to be checked" wording in §4 replaced; λ = 1 made explicit in §2.
