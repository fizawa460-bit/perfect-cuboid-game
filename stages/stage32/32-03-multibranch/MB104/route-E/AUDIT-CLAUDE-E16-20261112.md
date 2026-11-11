# Reading audit of E16 (Claude, 2026-11-12)

Auditor: Claude (Opus 5.5), owner's local session; E16 was written in a separate session. Base: main `0b49f73f`.
Standard: reading audit (owner's rule #1851); `e16/sing_budget.py` rerun from the repository root with `python -I`
(ends `PASS`). Zero credit; no credit flag changed.

**Verdict: PASS.** No mathematical error found.

| item | check | verdict |
|---|---|---|
| §1 quotations | "three times too weak" (E09), "cannot close the δ = 8, γ = 0 near-balanced family" and "could still bite" (E10) found verbatim | PASS |
| Lemma S (1) | p_a = (a − 1)(b − 1), normalization P¹; branch multiplicity min(e₁, e₂); δ_P ≥ m_P(m_P − 1)/2 for the whole germ | PASS |
| Lemma S (2), (3) | Σ m_P² ≥ M²/12; j ≥ 2(deg + s) when \|Ω\| ≤ 4 | PASS; S1 |
| Proposition S′ | fibre bound M ≤ 6a (two matched points per fibre value β); the two cases b ≥ 2a and a ≤ b ≤ 2a; (a + b)² ≤ 6ab for b/a ≤ 2 + √3 | PASS |
| "nothing more is forced" | parity gives only M ≥ j; even points carry no condition; controls violate (1) | PASS (labels correct) |
| §3, §4 | marked [outline] / [heuristic] / [open]; dimension count 2(a + b) − 1 checked; literature statements flagged as quoted from memory | PASS (not used for any claim) |

SHOULD FIX (applied): S1. Lemma S (3) used that M(M − 12)/24 is increasing without saying M ≥ 2N ≥ 6.

Confirmed conclusion: the singularity count gives no degree bound; the core E12 §5 remains open.
