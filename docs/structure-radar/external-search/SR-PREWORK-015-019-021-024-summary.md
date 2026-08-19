# StructureRadar ChatGPT pre-Work follow-up — SR-STR-015 / 019 / 021 / 024

Date: 2026-08-19

This bundle records four targeted ChatGPT primary-source searches performed after the canonical StructureRadar literature pass and before spending Work credits.

## Global verdict

```text
TARGET_COUNT=4
DIRECT_FULL_TARGET_THEOREM_COUNT=0
CHATGPT_ESCALATE_TO_WORK_COUNT=4
ARSENAL_PROMOTION_COUNT=0
CARD_STATUS_CHANGE_COUNT=0
WORK_REQUESTS_NARROWED=true
NOVELTY_BY_SEARCH_ABSENCE=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT_UNCHANGED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## Narrowed gaps

| Structure | New useful literature lead | Remaining exact gap |
|---|---|---|
| SR-STR-015 | Daw–Orr on `E x CM` unlikely intersections in `A_2`; Gaudron–Rémond isogeny-height bounds | Either reduce the 2D R504 exceptional locus to finitely many curves where Daw–Orr applies, or control rational typical intersections of the 2D Prym-moduli surface with fixed-CM-factor Hecke curves, with height transfer |
| SR-STR-019 | Zehavi joint equidistribution of pairs of polynomial-congruence roots; Irving pointwise smooth-modulus divisor AP | Preserve **joint roots + nested divisors + every-principal-cell uniformity** in one published pointwise first-moment theorem/adapter |
| SR-STR-021 | Merikoski combines finite Gaussian characters with angular Hecke characters and primary-generator residue handling | Transfer a single-class-scale short-interval PNT argument to `L(s, xi_k chi)` at `N(q)=X^{o(1)}`, with sector Fourier modes and exceptional-zero handling |
| SR-STR-024 | Nguyen 2024 gives individual-composite-modulus variance for standard `tau_k` | `ConditionedFilteredTau3IndividualModulusVarianceAdapter` preserving the StructureRadar filtered witness, common-core/factor-pair masks, and scalar/pair charged measure |

## Files

- `SR-STR-015-chatgpt-prework.md`
- `SR-STR-019-chatgpt-prework.md`
- `SR-STR-021-chatgpt-prework.md`
- `SR-STR-024-chatgpt-prework.md`

## Lifecycle / audit firewall

This PR is a literature-evidence bundle, not a theorem promotion.

- Existing `EXTERNAL_GATE` decisions remain unchanged.
- No `ACTIVE` promotion is made.
- No whole-family exponent is improved.
- The focused Work requests are escalation targets only if independent audit accepts the literature/applicability narrowing.
- Work is not a merge blocker for unrelated StructureRadar batches.

```text
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=StructureRadar-audit
```