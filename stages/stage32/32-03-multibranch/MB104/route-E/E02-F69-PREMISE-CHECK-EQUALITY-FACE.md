# E02 — Check of the F69 receiver premises; the Beauville equality face is empty (2026-11-02)

Status: research note, **unaudited, zero credit**. It builds on E01 (`E01-C8-CONGRUENCE-EMPTY-WINDOW.md`) and on the
predecessor-archive Beauville notes listed in §4. Those notes are not hostile-audited at the current head.

## 1. Where the F69 premises come from

F69 §3 assumes:

- a minimal Z ⊂ C8×C8 (the normalization of an integral curve);
- étale legs of equal degree;
- a diagonal finite group H;
- E = Z/H of genus ≤ 1.

These premises are not new. They are exactly the output of the predecessor note
`GENUS1-P5-BEAUVILLE-EQUALITY-RIGIDITY.md`, whose framework is `BEAUVILLE-ODD-BRANCH-COVER-WALL.md`. The current STATE
inherits that output: the e=2 chain cites it as "the retained equality-rigidity geometry gives deg = n = 28l, g(E) = 1,
f_i étale" (blob `d4e5c3b9`, locked in `retained_frontier.e2_unique_pair_etale_immersion_orbifold_bmy`).

The framework is the following.

- **Beauville cover.** Freitag–Salvati Manni, *Parametrization of the box variety by theta functions*, §4: a double cover q: X → B of the box variety B. Locally it is C²→C²/±1 at the 48 nodes; it is quasi-étale, so K_X = q*K_B.
  - X has a finite étale Galois cover P = C8×C8 → X with group G0 ≅ (Z/2)², which acts freely.
  - P → B is Galois with group G = Γ[4]/Γ[8] ≅ (Z/2)³, acting diagonally.
- **Odd branches.** For a carrier C̄ ⊂ B with normalization of genus g and canonical degree d = K_B·C̄, let r_odd be the number of normalization branches through nodes with odd m = min(A, B) (A1 adapter, blob `512fcc70`). Let Y be the normalized double cover of the carrier's normalization. Then:
  - (B1) 2h(Y) − 2 = 4g − 4 + r_odd;
  - (B2) K_X·Y = 2d.
- **Product inequality.** Let Z be a component of the normalized pullback of Y to P, with Z → Y étale of degree e ∈ {1, 2, 4}. Riemann–Hurwitz for the two projections gives K_P·Z ≤ 2(2g(Z) − 2). Hence r_odd ≥ d − 4g + 4 (B4).
- **Equality.** If r_odd = d − 4g + 4, then both projections are finite étale of degree ed/8 (equality-rigidity note, (E3)–(E4)).

## 2. Premise-by-premise check for the uniform class

Take the uniform class D_l = 7l·H − 4l·Σ_{p∈Σ} E_p with |Σ| = 14 (MB104 support `000707000f0f`), l ≥ 1. On the resolved
surface S we have K_S = H, H² = 16, E_p² = −2 and H·E_p = 0. Then:

- d = K·D_l = 7l·16 = **112l**;
- the strict transform meets each exceptional curve with C̃·E_p = −4l·E_p² = **8l**;
- every normalization branch through p meets E_p at least once, so the number of branches through p is ≤ 8l;
- hence the total number of node branches is M ≤ 14·8l = 112l = d.

| F69 premise | Status for the uniform class |
|---|---|
| (P0) Equality face r_odd = d − 4g + 4 | **Forced.** For g = 1: r_odd ≥ d by (B4), and r_odd ≤ M ≤ d, so r_odd = M = d = 112l. For g = 0, (B4) gives r_odd ≥ d + 4 > M, which is impossible, so genus 0 is excluded by counting alone. |
| (P1) Z is the normalization of an integral curve in C8×C8 (minimality / birational onto image) | **Automatic.** Z is a component of the normalized pullback of the reduced curve C̄ under the generically étale map P → B. |
| (P2) Both legs finite étale | **Follows from (P0)** by the equality-rigidity argument. Leg degree n = ed/8 = 14el. |
| (P3) A finite group acting on Z through Aut(C8) with quotient of genus ≤ 1 | **Automatic.** Z/Stab_G(Z) = normalization of C̄, of genus 1. Here \|Stab_G(Z)\| = 2e, and G acts diagonally. |
| (P4) d = 56m | **Not needed.** E01 only needs n/\|Stab\| ≥ 16/3, and here n/\|Stab\| = 14el/(2e) = 7l ≥ 7. |

## 3. Conclusion (Lemma E02)

**Lemma E02.** Assume the Beauville framework of §1, i.e. the source facts in §4. Then for every l ≥ 1 and every
14-node support Σ, the uniform class D_l = 7lH − 4lΣE_p on the box surface contains no integral curve whose
normalization has genus ≤ 1.

*Proof.*

- Genus 0 is excluded by counting (§2, P0).
- Suppose the genus is 1. By §2, a component Z of the pullback to C8×C8 is a minimal étale correspondence with legs of degree n = 14el.
- Z/Stab_G(Z) = Ē has genus 1, and |Stab_G(Z)| = 2e.
- Apply E01 with h = 2e. Its proof works verbatim for h ∈ {1, 2, 4, 8}, because the diagonal group only enters through [L : K] = h.
  - Equivalently: the orbifold area is Area(H/L) = Area(Z)/(2e) = 2π·e·d/(2e) = πd = 112πl.
  - L ⊇ K = Γ ∩ a⁻¹Γa is congruence, because Γ = PQ¹_B(2).
  - LMR Thm 4.3 gives λ₁(L) ≥ 3/16. Zograf (LMR Thm 4.4) with g = 1 and area ≥ 64π gives λ₁(L) < 16π/(112πl) = 1/(7l) ≤ 1/7.
- But 1/7 < 3/16, a contradiction. □

General form: on the equality face, the area of Ē is π(4g − 4 + r_odd), which equals πd for g ≤ 1. So any genus-≤1 carrier on the equality face with d ≥ 86 is excluded.

This covers the whole current e=2 frontier: the rational-core and coreless branches, the m=1 energy band and the balanced bulk. It also covers e = 1 and e = 4. All of these live inside the uniform class on the equality face.

## 4. What this relies on (must be audited)

1. **Beauville framework** (predecessor archive, not in current STATE locks; the predecessor branch's last re-audit was FAIL):
   - `BEAUVILLE-ODD-BRANCH-COVER-WALL.md`, blob `1afa8398`: (B1), (B2), quasi-étaleness, the product cover.
   - `GENUS1-P5-BEAUVILLE-EQUALITY-RIGIDITY.md`, blob `a2054708`: (E1)–(E4).
   - `GENUS1-P5-FULL-DECK-STABILIZER-RIGIDITY.md`, blob `cb05a7a1`: P/G0 = X, P/G = B, G = Γ[4]/Γ[8], G0 free.
   - Primary source: Freitag–Salvati Manni (Michigan Math. J. 65 (2016), arXiv:1303.6495), checked directly on 2026-11-02 (arXiv PDF text):
     - Introduction: the box variety is the quotient of H/Γ[8] × H/Γ[8] by a group of order 8 coming from the diagonal action of Γ[4].
     - §2, Prop. 2.5 and the following lines: G = Δ(4,8)/(Γ[8]×Γ[8]) ≅ (Z/2)³ is the Galois group, and the 48 nodes are images of fixed points of G.
     - Introduction and §4: Beauville's smooth two-fold Galois cover X is unramified outside the 48 nodes, and Γ'[4]/Γ[8] acts freely on H/Γ[8].
     - The exact statements of (B1)/(B2) and the A1 adapter are still to be audited.
2. **A1 branch adapter** m = min(A, B) and the "ramified exactly on odd branches" statement (blob `512fcc70`).
3. **Identification of the FSM product-cover curve with C8.** That curve is X(8) = H*/Γ[8], compactified. It must be the genus-5 curve uniformized by PQ¹_B(2) in E01. The Wiman curve is unique, so this holds once the FSM curve is known to be the compact X(8) with its full automorphism group.
4. **E01 itself.** Round-2 executing audit: PASS.
5. **Scope.**
   - Only the *uniform* class 7lH − 4lΣE with |Σ| = 14 is covered.
   - Unequal Picard coefficients, other node counts, P6 sectors and carriers off this class are untouched.
   - Route A's 864 balanced supports are covered only insofar as their carrier classes have this uniform shape. This must be checked against the A-route definitions.
   - No credit, frontier change or MB104 closure is claimed.

## 5. Arithmetic check

`e02_counts.py` checks the following exactly:

- d = 112l and C̃·E_p = 8l;
- M ≤ d;
- n = 14el;
- n/|Stab| = 7l;
- area(Ē) = 112πl versus 256π/3;
- the 1/7 < 3/16 comparison.

These are checked for l = 1..1000 and e ∈ {1, 2, 4}.
