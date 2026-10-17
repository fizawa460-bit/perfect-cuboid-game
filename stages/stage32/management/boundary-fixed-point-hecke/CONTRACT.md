# Stage32 BOUNDARY-FIXED-POINT-HECKE — both boundary strata g0-d044 and g1-d048 are empty (proof sketch, research cycle 32R-18)

```text
CLAIM: No integral unibranch curve C on S (not a fibre component) of geometric genus g ∈ {0,1} attains equality in
       2ν = e + d − 4g + 4 with ν = e = 48, i.e. (g,d) = (0,44) or (1,48).
       g1-d048 is new; for g0-d044 this is a second, simpler proof (the first is #1842).
STATUS: Proof sketch, needs hostile audit. Arithmetic and finite-group facts checked by `verify_boundary_fixed_point_hecke.py`.
BUILDS ON: #1842 CONTRACT §0–§3a (FSM structure, Bolza curve, Δ(2,3,8) = normalizer of the Bolza maximal order,
           the Hecke product formula, strong approximation for 𝒪¹). Those facts were audited there.
```

## 1. Setting (same as #1842)
- In the equality case, every multiplicity m_j is 1. So D̄, the normalisation of π⁻¹(C̄) ⊂ X, is a connected double cover of C̃ branched at exactly 48 points (the node points).
- Hence the deck involution ι of D̄ → C̃ has **exactly 48 fixed points**.
- 2g(D̄) − 2 = 2(2g − 2) + 48. Both f_i : D̄ → X → Y (Bolza) are **étale of degree n = d/2** (22 or 24), by the equality case of r ≥ 2n_i + 4 − 4g.
- The involution τ of X → B̄ induces the hyperelliptic involution σ on each factor Y. This is because each factor fibration of B̄ goes to X(4) = Y/σ. Hence **f_i ∘ ι = σ ∘ f_i** for i = 1, 2.
- f2 ≠ α∘f1 for every α ∈ Aut(Y), as in #1842 §1: otherwise C̃ would map with degree n ≥ 22 > 8 onto a graph in X(4)².

## 2. Group-theoretic translation
- Write Y = 𝔥/Γ_Y with Γ_Y ◁ Δ = Δ(2,3,8) and Δ/Γ_Y ≅ GL₂(F₃). Write D̄ = 𝔥/Γ_D with Γ_D ⊂ Γ_Y of index n, and lift f2 to g with gΓ_Dg⁻¹ ⊂ Γ_Y.
  - Then g ∈ Comm(Δ). If g ∈ Δ = N(Γ_Y), then f2 = α∘f1, which is excluded. So **g ∉ Δ**.
- Let K = Δ ∩ g⁻¹Δg and h = [Δ : K] = Π N(P)^{k−1}(N(P)+1) (#1842 §3a). Let ω be the number of primes in the support. Then h ≥ 8^ω, because N(P) ≥ 7 for every unramified P.
- **Lift of ι.** ι lifts to ι̃ ∈ PSL₂(ℝ) normalising Γ_D.
  - f1∘ι = σ∘f1 means that ι̃ normalises Γ_Y and induces σ, so ι̃ ∈ σ̃Γ_Y ⊂ Δ.
  - f2∘ι = σ∘f2 gives, in the same way, gι̃g⁻¹ ∈ Δ.
  - Hence **ι̃ ∈ K**. Γ'' := Γ_Y ∩ K is normal in K (Γ_Y ◁ Δ), and Γ_D ⊂ Γ''.

## 3. Fixed-point count
Let Y'' = 𝔥/Γ''. The coverings D̄ → Y'' → Y are ι-, ι''- and σ-equivariant.
1. A fixed point of ι on D̄ maps to a fixed point of ι'' on Y'', which maps to a fixed point of σ on Y. σ has **6** fixed points (the Weierstrass points).
2. **Fibre of Y'' → Y over a Weierstrass point y.**
   - Γ_Y acts transitively on Δ/K. Indeed, the image of 𝒪¹ in the congruence quotient at the support of g is Π SL₂(O/P^k)/±, which is perfect because every residue field has size ≥ 7. Δ/Γ_Y is solvable, so the image of Γ_Y contains this perfect group.
   - Hence the fibre is identified with Δ/K, which has h points: Γ''γ ↦ γ⁻¹x₀.
   - Let e ∈ σ̃Γ_Y be the elliptic element of order 2 fixing a lift z₀ of y.
   - ι'' fixes [γz₀] iff γeγ⁻¹ ∈ K ∩ σ̃Γ_Y = ι̃Γ''. That holds iff e fixes the point γ⁻¹x₀ of Δ/K.
3. **Fixed points of e on Δ/K.**
   - Locally, Δ/K = Π_P {vertices at distance k_P from v₀ in the Bruhat–Tits tree of PGL₂(k_P)}.
   - e ∈ Stab(v₀) is a semisimple involution. Its eigenvalue difference is a P-adic unit, since P is odd. So its fixed set in the tree is:
     - either the geodesic through v₀ (split case): 2 vertices at each distance k ≥ 1;
     - or {v₀} alone (non-split case): 0 vertices.
   - Hence e has at most 2^ω fixed points on Δ/K.
   - For k = 1 this is the statement that an involution of PGL₂(F_N) fixes 0 or 2 points of P¹(F_N), which was checked by computer for N = 7 and 23.
   - So **#Fix(ι'') ≤ 6·2^ω**.
4. Each fibre of D̄ → Y'' has [Γ'' : Γ_D] = n/h points (Γ_Y transitive, so [Γ_Y : Γ''] = h), and ι fixes at most that many of them.
5. Therefore
   **48 = #Fix(ι) ≤ 6·2^ω·n/h ≤ 6·n·(2/8)^ω ≤ 6n/4**, which is 33 for n = 22 and 36 for n = 24. Contradiction. ∎

## 4. Remarks
- This argument does not need the index restriction or the degree bound onto the image used in #1842. Only g ∉ Δ, the Hecke formula, transitivity, and the fixed-point bound are used. It is therefore a second proof for g0-d044 and the first proof for g1-d048.
- Both boundary strata (35 compressed terminals in V52) are excluded geometrically. MAIN is unchanged, since this is not an audit of the formal counts.

## 5. Points to audit
1. f_i∘ι = σ∘f_i: τ induces σ on both Y factors, and ι is the restriction of τ.
2. ι̃ ∈ K: the lift of ι lies in Δ and in g⁻¹Δg.
3. Transitivity of Γ_Y on Δ/K for a general support (products of primes and prime powers): perfectness of Π SL₂(O/P^k).
4. The fixed set of an involution in the Bruhat–Tits tree, and the bound of at most 2 fixed vertices at each distance k.
5. The fibre identification Γ''\Γ_Y ≅ Δ/K and the fixed-point criterion.
6. The count "exactly 48 fixed points": the branch points of D̄ → C̃ are exactly the 48 node points with odd m.
