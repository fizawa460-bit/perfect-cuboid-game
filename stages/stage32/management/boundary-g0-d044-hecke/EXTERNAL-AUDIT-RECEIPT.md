# External hostile audit receipt — BOUNDARY-G0-D044-HECKE

```text
HOSTILE AUDIT: PASS (with the arithmetic bridge supplied by the auditor)
DATE: 2026-10-17
AUDITED HEAD: PR #1842, c96ba0ff705061867be9e4162b9723de932c9004
REPRODUCTION: verify_boundary_g0_d044_hecke.py, Python 3.12.14, exit 0. An independent prime-ideal enumeration gives the same list
  {242, 264, 440, 594, 770, 858, 968, 1034}: each is supported on one prime ideal with k = 1.
SCOPE: exclusion of the geometric g0-d044 boundary stratum. This is not an audit of the formal count of 17 terminals; MAIN is unchanged.
NOT INCLUDED: g1-d048, curve nonexistence elsewhere, perfect cuboids, merge permission.
```

## Item verdicts

| # | Item | Verdict | Auditor's basis |
|---|---|---|---|
| 1 | Reading of the FSM structure | PASS | FSM Lemma 4.1 (the free H-action) gives the same Y = X(8)/H for both factors. X → Y×Y is étale of degree 4 via (H×H)/H_diag. From FSM's θ-relations, Y is w² = t(1−t⁴) up to scalars, which is Bolza. This is consistent with the factor fibrations. |
| 2 | Étaleness from equality | PASS | Unibranch with all 48 multiplicities 1 gives a connected double cover branched at 48 points, so 2g(D̄)−2 = 44. With n₁+n₂ = 44 and 44 ≥ 2nᵢ, both nᵢ = 22 and the ramification is 0. The auditor checked this derivation itself, not only the numbers. |
| 3 | Δ data, maximality, index 48 | PASS | Consistent with the Bolza-order literature (Γ_Y ◁ Δ with quotient GL₂(F₃)). Maximality also follows from area: π/12 compared with the minimal orbifold area π/21. |
| 4 | Index lemma and Hecke degrees | PASS (with bridge) | t = (h/r)·s with r, s \| 48 is correct. The product formula needs the identification of Δ with the normalizer of the Bolza maximal order; this was missing from the contract. |
| 5 | Strong approximation and perfectness | PASS | It applies to the norm-one group 𝒪¹, with reduction PSL₂(F_N). Since Δ/Γ_Y is solvable, Γ_Y is transitive on P¹(F_N) (see also the Bolza-order paper, Cor. 14.2). |

## Requested fixes and their resolution

| Class | Finding | Resolution |
|---|---|---|
| must fix | Add the maximal-order/normalizer identification and the derivation of the product formula. | Added as `CONTRACT.md` §3a: 𝒪 = O_k[α,β], P𝒪¹ = Δ(3,3,4), q = α+β−1 with q² = −(2+√2), qα = βq, qβ = αq; Δ is the normalizer; tree local factors; ramified factor 1. |
| must fix | Strong approximation applies to 𝒪¹, not to Δ. | §3a and the transitivity step now say this explicitly. |
| note | The script's "étale" PASS line is only a numerical consistency check. | Messages and docstring reworded to "numerical consistency only; the geometric derivation is in CONTRACT.md §1". The check logic is unchanged. |
| note | "Single prime" means the support count; each rational prime splits, so there are two choices of prime ideal. | Reworded in `CONTRACT.md` §4 and in the script messages. |

After the audited head, the following changed:
- `CONTRACT.md`: §3a added; status, scope and wording updated.
- This receipt (new).
- Message and docstring text in `verify_boundary_g0_d044_hecke.py`. The check logic and expected values are unchanged.

`RESULT.json` is byte-identical.
