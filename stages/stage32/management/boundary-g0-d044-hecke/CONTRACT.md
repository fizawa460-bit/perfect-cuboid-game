# Stage32 BOUNDARY-G0-D044-HECKE — the rational boundary stratum g0-d044 is empty (proof sketch, research cycle 32R-17)

```text
CLAIM: No integral unibranch rational curve C on S (not a fibre component) reaches equality in 2ν = e + d − 4g + 4 with d = 44, e = ν = 48.
       So the boundary stratum g0-d044 is empty. It has 17 compressed terminals in V52.
STATUS: External hostile audit PASS (2026-10-17, head c96ba0ff), together with the arithmetic bridge in §3a, which was added after the audit. See EXTERNAL-AUDIT-RECEIPT.md. The arithmetic enumeration is checked by `verify_boundary_g0_d044_hecke.py`.
SCOPE: This excludes the geometric g0-d044 boundary stratum. It is not an audit of the formal count of 17 terminals, and it does not change MAIN.
OPEN: g1-d048. Hecke candidates remain at the primes P | 7 (h=8) and P | 23 (h=24); they need finer analysis.
```

## 0. Notation
- FSM / post1648al:
  - X(8) has genus 5. H ≅ (Z/2)² acts freely on it, and Y := X(8)/H has genus 2.
  - X := (X(8)×X(8))/H (diagonal action) is smooth.
  - π: X → B̄ is a double cover ramified only at the 48 nodes.
  - X → Y×Y is étale of degree 4.
  - The two factor fibrations of B̄ are X → Y → Y/σ = X(4) ≅ P¹, where σ is the hyperelliptic involution.
- Y → X(4) is branched exactly at the 6 cusps of X(4) (the vertices of an octahedron, {0, ∞, ±1, ±i}). Hence Y ≅ the **Bolza curve** w² = x⁵ − x, for both factors.
- The Bolza curve is Y = 𝔥/Γ_Y, where Γ_Y is torsion-free and cocompact, and is a normal subgroup of index 48 in the (2,3,8) triangle group Δ, with Δ/Γ_Y ≅ Aut⁺(Y), of order 48.
  - Δ is arithmetic (Takeuchi): the field is Q(√2), and the quaternion algebra is ramified only at (√2) and one real place.
  - Δ is maximal (Singerman), so N(Γ_Y) = N(Δ) = Δ.

## 1. Reduction to two étale maps (from 32R-09/15)
Suppose C exists, with C̃ ≅ P¹. Let D̄ be the normalisation of π⁻¹(C̄) ⊂ X.
- Every m_j = 1 is odd, so D̄ is a double cover of C̃ ramified at 48 points: hyperelliptic of genus 23.
- The equality case gives n_1 = n_2 = 22, and both composites f_i : D̄ → X → Y are **étale of degree 22** (equality in r ≥ 2n_i + 4 − 4g).
- D̄ → π⁻¹(C̄) is birational, and X → Y×Y has degree 4. So the map (f1, f2): D̄ → Y×Y has degree **at most 4** onto its image Z.
- f2 ≠ α∘f1 for every α ∈ Aut(Y). Otherwise φ2 = ᾱ∘φ1, and C̃ would map with degree 22 onto the graph of ᾱ in X(4)². But C̄ maps to its image with degree at most deg(B̄ → X(4)²) = 8.

## 2. Uniformisation
- Take D̄ = 𝔥/Γ_D with Γ_D ⊂ Γ_Y of index 22, so that f1 is induced by the identity.
- The étale map f2 lifts to some g ∈ PSL₂(ℝ) with g Γ_D g⁻¹ ⊂ Γ_Y.
- Then g lies in the commensurator Comm(Γ_Y) = Comm(Δ), and Γ_D ⊂ Γ' := Γ_Y ∩ g⁻¹ Γ_Y g.
- If g ∈ Δ = N(Γ_Y), then f2 = α∘f1, which is excluded. So g ∉ Δ.
- [Γ_Y : Γ'] divides 22, so it is 2, 11 or 22. (Index 1 would mean g ∈ N(Γ_Y) = Δ.)
- The map (f1, f2) is z ↦ ([z], [gz]), which factors through Y' = 𝔥/Γ'. So its degree onto Z is at least [Γ' : Γ_D] = 22 / [Γ_Y : Γ'].

## 3. Index lemma
Let K = Δ ∩ g⁻¹Δg and h = [Δ : K], the Hecke degree.
- Γ_Y is normal in Δ, so the Γ_Y-orbits on Δ/K all have the same size h/r, with r | 48.
- Γ_Y ∩ K and K ∩ g⁻¹Γ_Y g are normal in K, and the quotient by the second embeds into a group of order 48. So [Γ_Y ∩ K : Γ'] divides 48.
- Therefore [Γ_Y : Γ'] = (h/r)·s with r, s | 48.
- For g ∉ Δ, h = Π N(P)^{k−1}(N(P)+1) over the unramified primes P in the support of g. §3a justifies this formula.

## 3a. Arithmetic bridge: the maximal order, its normalizer, and the Hecke product formula (added after the audit)
"Arithmetic and maximal" alone does not give the Hecke product formula. It needs the following identification.
- **Bolza maximal order.** Let k = Q(√2), B the quaternion algebra ramified only at (√2) and one real place, and 𝒪 = O_k[α, β] the Bolza maximal order.
  - Then P𝒪¹ = Δ(3,3,4), the projected norm-one group.
  - The element q = α + β − 1 satisfies q² = −(2+√2), qα = βq and qβ = αq. The auditor checked these identities by exact computation.
  - q normalizes 𝒪. Adding its projective image gives Δ(2,3,8).
  - Since Δ is maximal, Δ is exactly the orientation-preserving projective normalizer of 𝒪.
- **Commensurator.** Comm(Δ) is the image of the positive-norm elements of B^× (Borel).
- **Local factors.**
  - At an unramified P, maximal orders of B_P correspond to vertices of the (N(P)+1)-regular Bruhat–Tits tree. The global maximal order g⁻¹𝒪g lies at some distance k from 𝒪.
  - Strong approximation, applied to **𝒪¹** and not to Δ itself, makes the stabilizer of 𝒪 act simultaneously transitively on the vertices at distance k. Hence the local factor is N(P)^{k−1}(N(P)+1).
  - At the ramified prime (√2) the local maximal order is unique, so the factor is 1.
- Hence [Δ : Δ ∩ g⁻¹Δg] = Π_P N(P)^{k_P−1}(N(P)+1) over the unramified primes in the support of g.
- **Transitivity in §4.** Strong approximation for 𝒪¹ makes the reduction mod P of P𝒪¹ equal to PSL₂(F_N); compare the Bolza-order literature, Cor. 14.2. This group is perfect. Δ/Γ_Y ≅ GL₂(F₃) is solvable, so the image of Γ_Y also contains PSL₂(F_N) and acts transitively on P¹(F_N).

## 4. Conclusion
- [Γ_Y : Γ'] = 2: the degree onto Z is at least 11 > 4. Contradiction with §1.
  - (Also, since h ≥ 8 and Γ_Y is transitive — see below — the orbit size is at least 8, so this case cannot occur at all.)
- [Γ_Y : Γ'] ∈ {11, 22}: 11 does not divide 48, so 11 | h, and h/r ≤ 22 gives h ≤ 1056.
- By computer check, the only such h are {242, 264, 440, 594, 770, 858, 968, 1034}. In each case the support of g is a **single** prime ideal P with k = 1, and N(P) ∈ {241, 263, 439, 593, 769, 857, 967, 1033}. Each of these rational primes splits in k, so P can be either of two prime ideals; the argument is identical for both.
- At such a P, the image of Δ in PGL₂(F_N) contains PSL₂(F_N). This group is perfect and Δ/Γ_Y is solvable, so the image of Γ_Y also contains PSL₂(F_N). Hence Γ_Y is transitive on P¹(F_N): r = 1 and the orbit size is h ≥ 242 > 22. Contradiction.
- So no g exists, and C does not exist. ∎ (sketch)

## 5. Points to audit
1. In FSM: the two factor curves are both Y ≅ Bolza, the projections f_i give exactly the degrees n_i, and X → Y×Y is étale of degree 4.
2. The equality case forces f_i to be étale (post1648al: r ≥ 2n_i + 4 − 4g, with equality).
3. The arithmetic data of Δ(2,3,8) (Takeuchi), maximality (Singerman), and Bolza's Γ_Y being a normal subgroup of index 48.
4. The index lemma (the orbit-size/divisibility argument) and the computation of Hecke degrees, including that the ramified prime contributes nothing.
5. Strong approximation and perfectness (PSL₂(F_N) with N ≥ 241).

## 6. g1-d048 (open)
- Here C̃ has genus 1 and D̄ has genus 25. The f_i are étale of degree 24, so [Γ_Y : Γ'] ∈ {6, 8, 12, 24}, given that the degree onto Z is at most 4.
- The Hecke candidates are h = 8 (P | 7) and h = 24 (P | 23). The index lemma does not exclude them.
- Further conditions are needed: (a) the compatibility of the hyperelliptic involution σ (that ι lifts it, with 48 fixed points), and (b) the lift through X → Y×Y (the H-structure). These require explicit computation in the quaternion order.
