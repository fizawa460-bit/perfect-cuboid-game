# External hostile audit receipt — BOUNDARY-FIXED-POINT-HECKE

```text
HOSTILE AUDIT: PASS (limited to the geometric boundary strata g0-d044 and g1-d048)
DATE: 2026-10-17
AUDITED HEAD: PR #1843, 36c481b585885fcb05efe902ee5fce48dda62908
PREREQUISITE: #1842 CONTRACT §0–§3a (audited)
REPRODUCTION: verify_boundary_fixed_point_hecke.py, Python 3.12.14, exit 0. Extra auditor checks: 900 involutions over
  prime-power local rings, and 200 cases over the inert P|3 (residue field F_9, exponents 1 and 2). Every fixed-point count was 0 or 2.
NOT INCLUDED: formal terminal counts, MAIN changes, other strata, perfect cuboids, merge permission
```

## Item verdicts

| # | Item | Verdict | Auditor's basis |
|---|---|---|---|
| 1 | f_i∘ι = σ∘f_i | PASS | τ is the nontrivial element of G/H (G = Γ[4]/Γ[8]) acting diagonally on both factors. On each Y it is the deck transformation of Y → X(4), i.e. σ. |
| 2 | ι̃ ∈ K | PASS | ι̃ lies in the Γ_Y-coset of a lift of σ, and gι̃g⁻¹ does too, so ι̃ ∈ Δ ∩ g⁻¹Δg. ι̃ need not have order 2. |
| 3 | Transitivity and perfectness for a general support | PASS | Simultaneous surjection by strong approximation and CRT. SL₂ over a finite local ring is perfect by the commutator formula, given residue field size ≥ 7. Δ/Γ_Y is solvable. |
| 4 | Fixed set in the tree | PASS | A representative with trace 0 and unit determinant at odd P gives 2 fixed vertices per distance in the split case and only the base vertex in the non-split case. Thick fixed sets are excluded. |
| 5 | Fibre identification and fixed-point criterion | PASS | Γ''γ ↦ γ⁻¹K is a bijection. The criterion reduces to γeγ⁻¹ ∈ ι̃Γ'' = K ∩ σ̃Γ_Y. The directions of conjugation and inversion are correct. |
| 6 | Exactly 48 fixed points | PASS | e = ν = 48 gives multiplicity 1 at every node, so the 48 points are simple branch points and the rest is unramified. |

Conclusion: ω ≥ 1 and h ≥ 8^ω give 48 ≤ 6n(1/4)^ω ≤ 6n/4 ∈ {33, 36}, a contradiction. No logical HOLD remains after the supplements.

## Requested fixes and their resolution

| Finding | Resolution |
|---|---|
| Add the perfectness proof (commutator formula) | `CONTRACT.md` §6 |
| Add the local fixed-point explanation (trace 0, unit determinant) | `CONTRACT.md` §6 |
| Distinguish ι̃ from e | `CONTRACT.md` §2 (notation note) |
| Justify f_i∘ι = σ∘f_i by the diagonal action | `CONTRACT.md` §1 |
| The script does not check generation or perfectness; align the docstring with what it checks | Docstring rewritten. The check logic is unchanged. |
| Tests for ω = 1..11 are not a proof for all ω | `CONTRACT.md` §6: the (1/4)^ω monotonicity gives the general case |

After the audited head, only `CONTRACT.md`, the verifier docstring and this receipt changed. The check logic is unchanged.
