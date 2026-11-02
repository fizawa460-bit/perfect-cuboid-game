# E05 — Structure of the small-ε layers, and the μ filter for degree-by-degree searches (2026-11-02)

Status: research note, **unaudited, zero credit**. It uses E03/E04 and the audited F71–F73 identities. No new exclusion
of MB104 carriers is claimed. §1 is a corollary of E03/E04; §2 and §3 are bookkeeping of necessary conditions.

Notation as in `MB104-STATUS-MAP-20261102.md` §0:

- d = H·C̃, M = μ = Σ_p C̃·E_p;
- r = the number of odd-contact branches;
- ε = M − d − 4(1 − g);
- k = |Stab_G(Z)|, with legs f_i : Z → C8 of degree n_i and ramification A_i;
- ψ_i : E → R = C8/S;
- D_i = (1/k)·p_*Ram(f_i).

## 1. The μ filter (corollary of E03 + E04)

**Corollary E05.1.** Let C̃ be an integral, non-exceptional curve on S of geometric genus g ≤ 1 and degree d. Then:

- g = 1 and d even ⇒ μ ≥ d + 2;
- g = 1 and d odd ⇒ μ ≥ d + 1;
- g = 0 ⇒ μ ≥ d + 6 for d even, and μ ≥ d + 5 for d odd,

unless C̃ is one of the 80 curves of E04 (degrees 2 and 4).

*Proof.*

- E03 gives r ≥ d − 4g + 4. By E04, equality holds only for the 80 curves.
- r is even, by (B1) of E02.
- Finally r ≤ M ≤ μ. □

**Application (degree 16, local computation, not in this repository).** The 71,697 unibranch-compatible d = 16
representatives of the 32R lane were checked:

- μ ranges over 16..32;
- 2,293 representatives have μ < 18 and contain no genus-≤1 curve;
- among the 23 open net classes (h0 = 3, 4), 13 have μ = 16 and are excluded. The remaining 10 have μ ∈ {18, 20} and only g = 1 is possible.

The pairing used is x·E_p = x Gn E_p, over the 48 lattice vectors of square −2 and H-degree 0.

The per-node-type parity "Σ_{p of type s} C̃·E_p is even" (F72 §6) holds automatically. The class Σ_{type s} E_p is
divisible by 2 in Pic, which was checked against all 140 generators. So it gives no filter.

## 2. The layer ε = 2

Assume ε = 2. Then:

- **From F73** (ε = 2(M − r) + L + 2c_off with L ≥ 1, and L even here): L = 2, M = r and c_off = 0.
  - Every exceptional contact is 1, so M = r = B_o = d + 6 − 4g.
  - D₁ and D₂ have disjoint supports, and deg D₁ + deg D₂ = 2.
  - At each node branch the local degree of Z → E is 2, and at least one leg is unramified there.
- **From F72 (5):** deg D_i = 2g − 2 + B_o/2 − 8n_i/k = d/2 + 1 − 8n_i/k. So:
  - k = 8: n₁ + n₂ = d and {deg D₁, deg D₂} = {d/2 + 1 − n₁, d/2 + 1 − n₂}. Hence (n₁, n₂) ∈ {(d/2 + 1, d/2 − 1), (d/2, d/2), (d/2 − 1, d/2 + 1)}.
  - k = 4: n₁ + n₂ = d/2, with 2n_i ∈ {d/2 + 1, d/2, d/2 − 1}, subject to parity.
- **Type rule.** If node branches occur at nodes of all three types, the inertia subgroup I is G, so k = 8.
- **Genus of Z.** 2g(Z) − 2 = k(2g − 2) + (k/2)·B_o.
- **One leg étale (deg D₁ = 0).**
  - ψ₁ is an orbifold covering of R = (P¹; 2⁶) (k = 8) or (P¹; 2⁸) (k = 4) of degree n₁. Only the fixed cone points carry branching, with local degree ≤ 2.
  - For **fixed d**, the Riemann existence theorem gives finitely many (E, ψ₁): finitely many transitive involution tuples in S_{n₁} with product 1 and Σ(transpositions) fixed by genus g.
  - For **varying d** there is no finiteness: genus-≤1 subgroups of Γ_G of large index exist, and they need not be congruence. So E01's method does not extend.
- **Example (d = 16, g = 1, all three types present, as for the classes 27882, 28255, 28261).** Then k = 8, g(Z) = 37, B_o = 18, A₁ + A₂ = 16 and (n₁, n₂) ∈ {(9,7), (8,8), (7,9)}. In the (9,7) and (7,9) cases, E carries a degree-9 orbifold covering of (P¹; 2⁶): a finite Hurwitz problem.

## 3. The layer ε = 4 (brief)

- F73 gives M − r ≤ 1: at most one contact of multiplicity 2, all other contacts 1.
- Also L ∈ {2, 4} with c_off = (4 − L − 2(M − r))/2 ≥ 0.
- Same bookkeeping as §2 with deg D₁ + deg D₂ = 4 − (M − B_o).

## 4. Why the remaining core is not reached (for the record)

- E01's congruence argument needs both legs étale, so that K = Γ ∩ a⁻¹Γa. With a ramified leg, Z is not uniformized by a subgroup of Γ.
- Turning the branch values into cone points does not close up. The orbifold orders must satisfy μ_z·e₁(z) = m(f₁z) and μ_z·e₂(z) = m(f₂z) at every z. Through the correspondence, this constraint propagates beyond any finite set of points unless all ramification sits over special points.
- If all leg ramification lay over the 24 singular fixed points, the relevant orbifolds would be (2,3,8m)-type. There, Margulis (non-arithmetic, finite commensurator) or Takeuchi (arithmetic m = 2, 3) would apply. This special case is not shown to be forced.

## 5. Status

- MB104 stays OPEN.
- The next step needs a new idea for ramified, high-genus co-image correspondences (see the status map §3), or large computations on the F75 windows.
