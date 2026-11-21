# EXP04 — δ★ 4-lift inspection (2026-11-21)

## 0. Baseline reproduced
Ran row384's `verify_four_lift_target384.py` (python-flint 0.9.0,
/tmp/flintenv) on the copied materials: output matches
`four_lift_target384.json` EXACTLY (2.1 s). δ★ is the unit Selmer class
with unit-basis mask 0x4125e122ae5103 (21 of the 55 norm-1 unit
squareclasses), 2-adic local code 0x44b88774c94772d6bc5c8f05827,
dyadic obstruction 0x0, real signature 0x1e, complement coset size 256,
representative norm a positive square, `four_lift_membership:
NOT_DETERMINED`. The local data encode level-2 (Selmer) membership
only: per row381's verify_units381.py, real_signature is the sign
vector of the representative at the 7 real embeddings of K and
real_obstruction = (s_0, s_1⊕s_2, s_3⊕s_4, s_5⊕s_6); the dyadic
obstruction comes from row373's parity masks at 2. There is NO
level-4 local data anywhere in the repo.

## 1. The E4 premise is void: no single place can witness non-lift
The ledger's E4 entry assumed "a single failing place = δ★ non-lift".
That is mathematically impossible, for two independent reasons:

(a) H^1-level obstruction. The obstruction to lifting δ★_v to
H^1(Q_v, J[4]) is the Bockstein ∂_v(δ★_v) ∈ H^2(Q_v, J[2]).
A Selmer class satisfies δ★_v = κ_v(P_v) (local Kummer image), and
Bockstein vanishes on Kummer classes: δ_v(T) = κ_v(T) for
T ∈ J[2](Q_v) under Tate duality, or directly: a Kummer cocycle
σ ↦ σQ − Q (2Q = P_v) is the image under [2]: J[4] → J[2] of the
J[4]-cocycle σ ↦ σR − R with R ∈ J[8], 2R = Q. So ∂_v(δ★_v) = 0
at EVERY place v, including 2 and ∞.

(b) Selmer-level local lift. The local Selmer-4 condition maps to the
local Selmer-2 condition via b_v ∘ κ_{4,v} = κ_{2,v} (functoriality
of Kummer maps for the morphism of exact sequences
[4] → [2] over [2] → id). Hence b_v(im κ_{4,v}) = im κ_{2,v}:
every local Selmer-2 class lifts to a local Selmer-4 class, at
every place. Local lifts always exist; only their global
compatibility can fail.

This is exactly row385 §6, which proves the GLOBAL H^1(Q, J[4])
lift of δ★ exists unconditionally (local Bockstein vanishing +
Brauer–Hasse–Noether injectivity on the J[2]-component via Shapiro's
lemma H^2(Q, μ_2^Δ) ≅ Br(K)[2]). It also explains row384 PROOF's
insistence that local membership ≠ global lift. Conclusion: the
4-lift question is purely global (Cassels–Tate), and a place-by-place
search for a failing place should NOT be run. E4's queue text is
superseded by this note.

## 2. The decision problem in its current sharp form (row385)
Row385 (author replay PASS; independent audit PASS_SCOPED_DEPENDENT
per row386's inheritance note) settles the structure:

- Sel^(2) = 𝒰 ⊕ ℋ_nr, dim 𝒰 = 9 (unit Selmer), dim ℋ_nr = c_Cl,
  ℋ_nr ≅ Hom(Cl(O_K), {±1}) (unramified, totally split Kummer space;
  its 2-localisation is 0 because both primes above 2 in K are
  principal).
- Cassels–Tate pairing b on Sel^(2) (alternating by Poonen–Stoll,
  canonical polarization via the rational half-canonical divisor
  51∞): rad(b) = im(Sel^(4) → Sel^(2)) (kernel-of-CT theorem applied
  to 0 → J[2] → J[4] → J[2] → 0; no finiteness of Sha assumed).
- b ≡ 0 on 𝒰 × 𝒰: b descends to an alternating form on the
  1-dimensional quotient 𝒰/𝒲 (𝒲 = 8 known rational classes), and
  every alternating form on a 1-dim space is 0.
- Hence, with λ★(η) := b(δ★, η) for η ∈ ℋ_nr:
  δ★ ∈ im(Sel^(4) → Sel^(2)) ⟺ λ★ = 0 ⟺ q★ = 0 in
  Cl(O_K)/2Cl(O_K), where q★ is the unique element with
  χ(q★) = (−1)^{b(δ★, η_χ)} for every quadratic class character χ.
- If q★ ≠ 0: rank J(Q) ≤ 7 + c_Cl (row385 §5, sharper than
  row384's 8 + c_Cl), so the −30 source (rank ≥ 10) would force
  c_Cl ≥ 3; non-lift alone plus the known rank ≥ 8 forces c_Cl ≥ 1.
  If c_Cl = 0 then b = 0 and δ★ does lift (also under row381's GRH).

## 3. Independent check performed here (row385 §3 certificate)
Recomputed the finite linear algebra of row385 §3 from scratch
(plain Python, no repo code): alternating forms on F_2^9 have 36
components; imposing "each of the 8 known classes (9-bit coords
cf, a1, 49, 0e, a8, 6b, f6, 51) lies in rad(b)" gives a condition
system of rank 36, whose only solution is b = 0. Also verified
rank(known) = 8 and rank(known + δ★=0x10c) = 9. This confirms the
certificate that b|_{𝒰×𝒰} = 0 and that the pairing matrix has the
block form with all unknowns confined to (λ★, B on ℋ_nr).

## 4. Exact blocker: what is missing to decide q★ = 0
Per row385 §7 (the repo's own statement of remaining work), none of
the following has been done:
(i) Make λ★ explicit: extract the Cassels–Tate functional as
    concrete data from the global H^1(J[4]) lift (whose existence
    §6 proves; no explicit cocycle is constructed) together with
    the corrections aligning the local Kummer conditions.
(ii) From λ★, construct a representative ideal 𝔞★ of q★.
(iii) Test [𝔞★] in Cl(O_K)/2Cl(O_K) using the existing
    principal-relation elimination (4,140 relations; formal
    quotient on 4,964 prime-ideal coordinates, 2,492 known to
    vanish in Cl/2).

Direction-of-proof caveat for step (iii), in the rows' own
discipline: if 𝔞★ is killed inside the recorded lattice by an
identity 𝔞★ = (α)·𝔠² with (α) a recorded principal relation, that
PROVES q★ = 0 (the identity is an identity of ideals), hence δ★
lifts — the outcome that gives NO rank gain, closing the δ★ route
negatively. If 𝔞★ survives the recorded lattice, that does NOT
prove q★ ≠ 0: a killing relation whose support leaves the recorded
prime set (norm ≤ 6768) would be invisible, exactly as the formal
residual 181 is not c_Cl. Proving q★ ≠ 0 equivalently requires one
explicit η ∈ ℋ_nr with b(δ★, η) = 1, i.e. one actual unramified
quadratic extension of K / class character χ with χ(q★) = −1 —
an explicit element of the dual of Cl[2], none of which is known.
That is T1's generation wall (all primes < 2^94) seen from the
dual side.

## 5. Verdict
- What the lift check is: a single global Cassels–Tate value,
  packaged as one class q★ ∈ Cl(O_K)/2Cl(O_K). Not a local
  computation; no cheapest place exists.
- What was computed here: exact replay of the δ★ specification,
  and an independent verification of row385 §3's 36-component
  certificate (b|_𝒰 = 0).
- Result: the obligation is NOT discharged and cannot be
  discharged locally. It is blocked precisely on (i)+(ii) —
  construction of q★'s representative ideal from the CT
  functional — and, for the useful direction q★ ≠ 0, on the
  class-group generation/duality wall already recorded as T1.
  A concrete next step exists (row385 §7's programme: explicit
  cocycle for the H^1(J[4]) lift → λ★ → 𝔞★ → recorded-lattice
  test), but its only lattice-decidable outcome is q★ = 0
  (δ★ lifts, route closes with no gain).
