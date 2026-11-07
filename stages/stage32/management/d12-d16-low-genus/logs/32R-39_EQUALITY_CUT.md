# 32R-39 Balanced-equality cut for d = 12 (2026-10-22, research, unaudited)

Cost profile of the d = 12 enumeration (32R-33 Knuth estimate, 4.12e12 nodes): 62% sits in the g = 0, n1 = n2 = 6
slices (6|16..22|-14); 6|12|-12 is 7.9%.

Lemma (d8 leaf §3 argument with general n): if n1 = n2 = n and e = 2n - 4g + 4 (equality in the §1 Hurwitz bound for both
rulings), then x, y are unramified off the cusps, the double cover D̄ (via sqrt h(x)) has 2g(D̄) - 2 = 2n and
f1, f2 : D̄ -> Y (Bolza) are étale of degree n. If n < 8 the Hecke step (h >= 8 > n) forces f2 = α∘f1, so C lies over an
octahedral graph and n = 2^r in {1, 2, 4}. Hence n = 6 is impossible.
(To recheck: the #1843 §6 Hecke lemma for an arbitrary étale pair of degree n — already flagged in the d8 CONTRACT §-review list.)

Consequences for d = 12:
- 6|12|-12 (g = 1, e = 12): empty. Saves 3.24e11.
- 6|16|-14: g = 0 is impossible, so c2min -14 -> -12. Knuth: 8.17e11 -> 2.01e11 (ratio 0.246). Script 32R-39_equality_cut.py.
Total 4.12e12 -> ~3.18e12 (-23%).

Next ideas: the defect-2 case (e = 2n - 4g + 6, f_i ramified in total <= 2) for g = 0 — would move 6|18|-14 (20.5%) to
c2min -12; rational curves via explicit parametrisation (x(t), y(t) of degree 6 with every h_j(x)h_j(y) a square).

## 32R-40 addendum
- Defect-2 (e = 2n - 4g + 6) cannot be cut by the same argument: via the double cover, R(f_i) = 4g - 4 + b - 2n with
  b = #odd-order node points, b ≡ e (mod 2), b <= e; b = e gives R = 2 (not étale), and b = e whenever all m_j <= 1.
- If smooth rational curves (C² = -14, p_a = 0) are excluded separately, every slice can run with c2min = -12
  (singular rational curves have p_a >= 1). Knuth (32R-40_no_smooth_rational.py, 18555 jobs): **1.06e12** nodes
  (vs 4.12e12 baseline, 3.18e12 after 32R-39). So the smooth-rational shell costs ~2/3 of the remaining work.
- Reformulation for rational curves: C̃ = P¹ with x(t), y(t) of degree 6; the condition is that for each cusp class
  ({0,∞}, {±1}, {±i}) the set of odd-order points over that class is the same for x and for y. Odd points O >= 16;
  O = 16 means x is rigid (ramified only over the 6 cusps, all indices <= 2).

## 32R-42 check of the general-n Hecke step (closes the open item above)
Lemma. Let C be integral on S̃, not a fibre component, of geometric genus g, with n1 = n2 = n < 8 and e = 2n - 4g + 4.
Then n ∈ {1, 2, 4}.
Proof check (all ingredients already audited in #1842/#1843/#1844):
1. Chain (d8 §1): 2g-2+2n = R_x >= Σ_c (n - k_c) >= 6n - (6n-e)/2 - B >= 3n - e/2. Equality for x and for y (same n, e)
   forces: points on E_c have (C·E_c)_P = 1 and lie on no Exc; node points meet one Exc transversally; B = e;
   x, y unramified off the cusps.
2. D̄ = normalisation of C̃ in C(C̃)(√h(x)) is branched exactly at the e node points (ord h(x) odd there, even at E-points),
   connected (e >= 8 > 0), with 2g(D̄) - 2 = 2(2g-2) + e = 2n. So f1, f2 : D̄ -> Y (degree n) have total ramification 0:
   étale.
3. Hecke: g ∉ Δ gives h = Π N(P)^{k-1}(N(P)+1) >= 8 (N(P) >= 7 for unramified P of Q(√2); #1842 §3a); Γ_Y is transitive
   on Δ/K for any support (#1843 §6, perfectness of Π SL2(O/P^k)); Γ_D ⊂ Γ_Y ∩ K. Hence h = [Γ_Y : Γ_Y ∩ K] <= n < 8,
   contradiction. So g ∈ Δ and f2 = α∘f1.
4. Graph step (d8 §3, verifier E): C is a component over an octahedral graph, n = 2^r with r ∈ {0,1,2}.
For d = 12: n = 6 is impossible. Slice 6|12|-12 holds only g = 1 equality classes (g = 0 needs e >= 16): empty.
Slice 6|16|-14: g = 0 is equality: impossible; g = 1 needs C² = 2p_a - 14 >= -12.
