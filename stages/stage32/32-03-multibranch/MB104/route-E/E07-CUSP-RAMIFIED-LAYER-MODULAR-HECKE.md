# E07 — The cusp-ramified layer: correspondences ramified only over cusps carry no ε > 0 carrier (2026-11-02)

Status: research note, **unaudited, zero credit**.

- It answers "Proposition A" of the Claude brainstorming proposal of 2026-11-02, which uses the second arithmetic structure of X(8).
- It uses audited E01/E04 and F70–F73, and an exact computation: `modular/run_e07.py` driving `modular/modhecke.py`.

## 0. The second uniformization

C8 = X(8) has two arithmetic uniformizations:

- **(B)** the cocompact one, H/PQ¹_B(2) with PQ¹_B(2) ◁ Δ(2,3,8), used in E01–E04;
- **(M)** the cusped one, Y(8) = H/Γ(8) ⊂ X(8) with Γ(8) ◁ PSL₂(Z). Aut(X(8)) = PSL₂(Z/8) has order 192.

The box group is G = Γ(4)/Γ(8) ⊂ PSL₂(Z/8) (FSM). It is checked in `run_e07.py`:

- the 24 cusps of X(8) are the primitive vectors mod 8 up to sign;
- the nontrivial elements of G fix 8, 8, 8, 0, 0, 0, 0 cusps;
- no element of G is the image of an elliptic element of PSL₂(Z), so G has no interior fixed points.

Hence **the 24 singular fixed points of G on C8 are exactly the 24 cusps of X(8)**, consistent with FSM Prop 2.5 (nodes = pairs of cusps of the same type).

## 1. Theorem E07

Let C̄ be an integral non-exceptional curve on B of geometric genus g ≤ 1. Let Z ⊂ C8×C8 be its co-image normalization, with legs f₁, f₂ : Z → X(8), S = Stab_G(Z) and k = |S|. Assume:

- **(i)** every ramification point of f₁ and of f₂ lies over a cusp of X(8);
- **(ii)** f₁⁻¹(cusps) = f₂⁻¹(cusps), i.e. Z meets the Satake boundary only at pairs of cusps.

Then C̄ is one of the 80 curves of E04, so ε = 0 and C̄ is single-branch. **In particular, no MB104 carrier satisfies (i) and (ii).**

*Proof.*

1. **Étale over Y(8).**
   - Put Z° = Z ∖ f₁⁻¹(cusps), which equals Z ∖ f₂⁻¹(cusps) by (ii).
   - Each f_i : Z° → Y(8) is proper. By (i) it is unramified, so it is a finite covering.
   - Γ(8) is torsion-free, so Z° = H/K′ with K′ ⊂ Γ(8) of finite index n = deg f₁.
2. **Hecke.**
   - f₂ lifts to an isometry a of H with aK′a⁻¹ ⊂ Γ(8). So a ∈ Comm(Γ(8)) = PGL₂(Q)⁺ (classical).
   - Z is birational onto its image, so K′ = Γ(8) ∩ a⁻¹Γ(8)a, as in E01 Step 2.
   - Scale a to a primitive integral matrix. Its Smith form gives a = γ·diag(N,1)·γ′ with γ, γ′ ∈ SL₂(Z).
   - Up to a diagonal automorphism of X(8)×X(8), which normalizes G and so descends to B, Z is the twist Z_σ = (1×σ)·T_N, σ ∈ PSL₂(Z/8), of the Hecke curve T_N = {(Γ(8)z, Γ(8)·diag(N,1)z)}.
3. **Congruence and the degree bound.**
   - The diagonal S lifts to L ⊃ K′ with [L : K′] = k and Z/S = H/L, with cusps filled.
   - L ⊂ PSL₂(Z), and L ⊇ Γ(8N), so L is a congruence subgroup of PSL₂(Z).
   - Selberg (1965) gives λ₁(L) ≥ 3/16. LMR Thm 4.4 (Zograf) applies to every finite-coarea Fuchsian group, cusps included.
   - With genus ≤ 1 these give Area(H/L) = (192n/k)·π/3 < 256π/3. So n < 4k/3, i.e. n ≤ 10.
   - The index is n = [Γ(8) : Γ(8) ∩ Γ⁰-level 8N] = 2^{v₂(N)}·ψ(N_odd). So n ≤ 10 exactly for N ∈ {1, …, 8}: n = 1, 2, 4, 4, 6, 8, 8, 8.
4. **Exact computation.** For N = 1..8 and all 192 twists σ, `modhecke.py` computes everything exactly in SL₂(Z/8N):
   - L_σ = { ℓ ∈ Γ₀(N) : ℓ mod 8 ∈ G and (aℓa⁻¹) mod 8 = σ⁻¹(ℓ mod 8)σ }, projectively. This is the full group of lifts of diagonal G-elements preserving Z_σ;
   - S(σ), its image in G;
   - the genus of H/L_σ, by Riemann–Hurwitz from the cycles of S = [[0,−1],[1,0]], U = ST and T on the cosets.

   This is valid with or without torsion, since it computes the underlying genus. Results:

   | N | n | (k, genus) over the twists | twists of genus ≤ 1 |
   |---|---|---|---|
   | 1 | 1 | (8,0)×32, (4,1)×96, (2,3)×64 | 128 twists (see note below) |
   | 2 | 2 | (4,5)×64, (2,9)×128 | 0 |
   | 3 | 4 | (8,3)×32, (4,9)×96, (2,21)×64 | 0 |
   | 4 | 4 | (4,9)×64, (2,21)×128 | 0 |
   | 5 | 6 | (8,7)×32, (4,17)×96, (2,37)×64 | 0 |
   | 6 | 8 | (4,25)×64, (2,49)×128 | 0 |
   | 7 | 8 | (8,11)×32, (4,25)×96, (2,53)×64 | 0 |
   | 8 | 8 | (4,25)×64, (2,49)×128 | 0 |

   *Note on N = 1 (revision 2, audit S1).* The 128 genus-≤1 twists are 128 graphs of automorphisms, not 128 distinct curves on B. Different twists can give the same curve on B. The count of distinct curves, 32 + 48 = 80, is not recomputed here; it is inherited from E04's G-conjugacy count. The code checks only that the (k, genus) pattern of the twists matches (8,0)×32 and (4,1)×96.

   So genus ≤ 1 occurs only for N = 1, the automorphism graphs, i.e. E04's curves. □

Cross-checks:

- N = 1 reproduces E04 independently of the Bolza computation.
- N = 3, 5, 7 agree with the brainstorming estimate (minimal genus 3, 7, 11).

## 2. What this removes, and what remains

- E05 §4 left a case open: all leg ramification sitting over the 24 special points, where (2,3,8m)-type orbifolds and Margulis/Takeuchi might have applied. Under (ii), that case is closed.
  - The cusped uniformization absorbs any ramification index over a cusp. So (2,3,∞) dominates every (2,3,8m).
- Remaining ε > 0 carriers violate (i) or (ii). That is:
  - some leg ramifies at a point over an interior (non-cusp) point of X(8) (ε_int > 0); or
  - Z meets the one-dimensional part of the Satake boundary, i.e. one leg hits a cusp while the other does not (β > 0).
- Together with E06, the open core is ε > 0 with co-image bidegree ≠ (1,1), and with interior ramification or boundary contact.

## 3. Reproduction

From the repository root:

```
python -I -O stages/stage32/32-03-multibranch/MB104/route-E/modular/run_e07.py
```

It takes about a minute and ends with `PASS`, exit code 0. Outputs go to the temporary directory.

## 4. Audit points

1. "Singular fixed points = cusps" (checked in code), and its compatibility with the coordinates of E02/FSM.
2. Step 1: properness and étaleness of f_i on Z° under (i) and (ii). Also the treatment of points of Z over cusps where one leg is unramified and the other ramified. (i) allows this; such points are removed from Z°.
3. Step 2: Comm(Γ(8)) = PGL₂(Q)⁺, the reduction to a = diag(N,1) plus twists, and the descent of the diagonal automorphism to B.
4. Step 3: Selberg 3/16 for congruence subgroups of PSL₂(Z), and Zograf for cusped groups (LMR Thm 4.4 as quoted). Also the area convention Area(H/PSL₂(Z)) = π/3, and the index formula.
5. Step 4: the definition of L_σ, i.e. exact lifts rather than a necessary condition, and the coset/genus computation.

## 5. Audit history

- **Round 1: Claude (executing), PASS (scoped) at `656798f2`.** The script gave PASS. The theorem holds under (i) and (ii) only.
  - Should-fix S1: the 128 twists versus the 80 distinct curves. → §1 Step 4 now has a note; the count 80 is inherited from E04.
  - Hardening in `run_e07.py`: the child runs with `-I -O`; for every twist, μ·k = 192·n is checked; the full (k, genus) table above is checked for every N.
