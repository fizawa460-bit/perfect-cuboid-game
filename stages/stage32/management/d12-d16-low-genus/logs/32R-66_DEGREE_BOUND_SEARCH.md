# 32R-66 Is there an a-priori degree bound for genus <= 1 curves on S? (2026-10-25)

Question (user): is d = 48 the last degree? Answer: not proven for all curves.

1. Garcia-Fritz–Urzúa (arXiv 1804.07671, Thm 1.2/3.1/Cor 3.3): for C ⊂ S with strict transform C', if
   -deg C + E.C' + 4g - 4 < 0 then C is ω-integral (ω the (2,2)-twisted symmetric differential). Hence every
   non-ω-integral curve has d <= e + 4g - 4 (e = E.C' = Σ m_j). Smooth at the nodes => e <= 48 => d <= 4g + 44.
   Our Hurwitz bound e >= 2 max(n1, n2) + 4 - 4g >= d + 4 - 4g already contains this. No bound when e is large
   (curves through nodes with m_j >= 2).
2. Miyaoka, Publ. RIMS 44 (2008) 403-417: Thm 1.1 (effective Bogomolov–McQuillan) needs K² > c2; on S~ K² = 16,
   c2 = 80, so no bound. Thm 1.3(ii) (C not ≅ P1, CK > 3g - 3): 2(CK - 3g + 3)² <= (3c2 - K²)(C² + 3CK - 6g + 6)
   with 3c2 - K² = 224 on S~: always satisfiable here (x² <= d²/16 - Σm²/2).
3. Orbifold heuristic: on S̄ (48 A1 points) e_orb = e(S̄) - 48(1 - 1/2) = 32 - 24 = 8 < K² = 16. An orbifold
   version of Thm 1.3(ii) with 3 c2_orb - K² = 8 and C̄² = y² <= d²/16 would give, for g = 1, 2d² <= 8(d²/16 + 3d),
   i.e. d <= 16 — but only without the local correction terms at the nodes the curve passes through.
   Plan: Langer, "Logarithmic orbifold Euler numbers of surfaces with applications", Proc. LMS 86 (2003):
   (K + αC)² <= 3 e_orb(X, αC) with local orbifold Euler numbers at the A1 points; estimate the local terms in
   terms of the germ of C at the node (m_j, branches) and see whether a bound d <= f(g) survives.

4. Langer applied (stoll/langer_filter.py). X = S̄, D = αC, e_top(S̄) = 32, e_orb(A1, not on C) = 1/2; at a node on C
   the preimage germ C' ⊂ C² has multiplicity exactly m_j (the double cover Bl_0 C² -> S~ is branched along E',
   π_*E' = E, so C'·E' = C~·E = m_j). Local terms (0.2.3): smooth point of X with mult m, r branches:
   α r - α m + α² m²/4; node: α r_j - α m_j/2 + α² m_j²/8. Necessary condition (unknown singularities bounded by
   Σ_T m²/4 <= p_a - g, r <= m, α = 1/(max multiplicity) for lc):
     16 + 2αd + α²(x² + Σm²/2) <= 24 - 6α(1-g) + 3α²(p_a - g) + Σ_j (3α m_j/2 + 3α² m_j²/8).
   Sanity: no known curve violates it. Effect: kills 0 of 2029 (d = 12) and 0 of 1487 (d = 14) reps.
   Reason: every passage through a node adds ~ (3/2)α to the right side, so with e >= d the inequality is far
   from tight (asymptotically it only gives e >~ 2d/3, weaker than Hurwitz e >= d + 4 - 4g).
   Conclusion: neither GFU nor Miyaoka/Langer gives an a-priori degree bound for curves through the nodes with
   e large; the general case seems open. A bound would need a new idea (e.g. use of both fibrations / the
   symmetric differentials of GFU with the m_j >= 2 local analysis).

5. CORRECTION (Stage29 records, stages/stage29/29-02-work-import/audit.md, 29-02c-LG2/): Freitag–Salvati Manni,
   Theorem 3.1: a curve whose normalization map is bijective (globally unibranch, singularities allowed, also at
   the nodes) has d <= 176 + 16g; with even degrees: g = 0 -> d <= 176, g = 1 -> d <= 192. Stage29 status:
   FSM_THEOREM_3_1_AUDIT=PASS_EXACT, MULTIBRANCH_RESIDUAL_OPEN=true (receiver R29-LG2-MB). So "finite" holds for
   unibranch curves; the open case is curves with >= 2 branches at some point (at a node or elsewhere).
   Items 1-4 above remain correct for what they say, but the "no bound for curves singular at the nodes" remark
   must read: no bound known for MULTIBRANCH curves; unibranch ones are capped at 176/192 by FSM.
