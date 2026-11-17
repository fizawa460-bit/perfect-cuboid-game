# Audit of ROUTE-F-PLAN.md (Claude, 2026-11-12, main 95096b00)

Status: reading audit of a plan. Zero credit.

## Verdict: PASS. The owner approved the plan, the registration and the start of F-01 on 2026-11-12.

| Item | Verdict | Note |
|---|---|---|
| Cited lemmas exist | PASS | E15 Lemma K (§1), E12 Lemma 0, E16 Lemma S (§2), E10 "d = δ(a+b)" (k = 8). Code `route-E/slack0/e11_w22.py` and `e11_slack0_small.py` exist. The 32R-96 log exists locally (`stage32_research/32R-96_KNOCK_LOG_CORE_IDEAS.md`). |
| c₀ < 1 suffices | PASS | M ≥ j ≥ 2·max(a+s₁, b+s₂) ≥ a+b, so M ≤ c₀(a+b)+C gives a+b ≤ C/(1−c₀). |
| G3 formula | PASS | 2(a+s₁) ≤ (2−η)(a+b)+C ⇒ s₁ ≤ (1−η/2)b − (η/2)a + C/2. |
| T1 gap = 3 | PASS | Balanced (λ = 1, a = b): need 3Σm² > 4a² − a², i.e. Σm² > a². The 12-point equidistribution gives Σm² ≥ (2a)²/12 = a²/3. |
| T2 gap = 2.5 | PASS | Need δ_off < a²/4 + Σm²/4 ≈ a²/3. Lemma S gives δ_off ≲ a² − Σm²/2 ≈ 5a²/6. |
| Replacing the first task | PASS | At d ≤ 16 we have a+b ≤ 2 for δ = 8, so leading-term comparisons carry no information. Near-miss curves have genus ≥ 2 and are outside Problem W. |
| Rephrasing detector and stop rules | PASS | They are mechanical and refer to fixed numbers. Criterion 2 is one-sided, as the plan states. |

## Notes (not blocking)

1. F-01 is a floating-point measurement. Record its table as "measured", not as a lemma.
2. G3 for k = 4 (W₄) and γ = 1 is not written. The plan lists this itself.
3. G2 at N = 4 is estimated at weeks. The F5 rule (ask before any run over 3 days) covers this.
4. "A few percent or less" is a subjective figure, not a computed probability.
