# 32R-41 Literature check + sign-group structure (2026-10-22, research)

## Literature
- Stoll–Testa, arXiv 1009.0388: all integral curves of degree <= 6 classified; conjecture: the 92 known curves are all
  curves of genus <= 1.
- Garcia-Fritz–Urzúa, arXiv 1804.07671 (§ "The surface of cuboids", from Garcia's 2015 Queen's thesis):
  (a) every genus <= 1 curve passes through >= 2 nodes; (b) deg C <= 4g + 44 if C is smooth at the nodes (also Kani);
  (c) a rational curve other than exceptional / components of x0x1x2x3 = 0 has C·E >= 8 (indeed C·E_i' >= 4 for 4 subsets).
  Method: symmetric differentials ω = F dx dw pulled back; for our setting this is equivalent to Riemann–Hurwitz
  bookkeeping and is weaker than our §1 bound e >= 2n - 4g + 4.
- Horie–Yamauchi, arXiv 2512.22520: L-function and Galois structure of Pic; no curve classification.
=> Our merged d = 8, 10 results (#1844, #1845) go beyond the published classification (degree <= 6). Not peer reviewed.

## Sign group (Z/2)^6 on Pic (stoll/sign_rep.py)
- Pic ⊗ Q splits into 37 characters: one of dim 7 (invariants, = plane quotient), 21 of dim 2, 15 of dim 1.
- S -> P^2, (a1²:a2²:a3²), degree 64, branched along 7 lines u_i, u_i+u_j, u1+u2+u3 (6 triple points, 3 double points).
- A rational C with stabiliser of order 2^k maps to a rational plane curve of degree 24/2^k with k <= 2
  (an elementary abelian 2-cover of P^1 is rational only for <= 3 branch points). k = 0 is the original problem
  (degree-12 polynomial parametrisation of S); k = 1, 2 give plane curves of degree 12 / 6 with all 7 line restrictions
  = (<= 2 roots) × square — small algebraic systems.
- Tried and dropped: x·σx >= x·R_σ for involutions (identity, no rationality content; weak as a cut).
