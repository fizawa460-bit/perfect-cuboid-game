# Reading audit of E15 (Claude, 2026-11-12)

Auditor: Claude (Opus 5.5), owner's local session; the E15 note was written in a separate session. Head audited:
`140a7a993` (branch `claude/inspiring-davinci-327vg8`, PR #1869). Standard: reading audit (owner's rule #1851);
scripts rerun from the repository root with `python -I`. Zero credit; no credit flag changed.

**Verdict: PASS.** No mathematical error found; labels [proved]/[outline]/[computed]/[open] are used correctly
except for one item (S2 below).

| item | check | verdict |
|---|---|---|
| Lemma K | each of the 12 matched points lies on exactly two Klein graphs (checked case by case); Φ^*Γ_g has degree a + b; local order ≥ min(e₁, e₂) | PASS |
| Corollary K | E12 Lemma 0 gives j ≥ 2·deg p_i + 2s_i when \|Ω\| ≤ 4; hence s₁ ≤ b, s₂ ≤ a | PASS |
| Lemma U | Q = 2(cosh d − 1); Δ log Im f = −\|f′\|²/(Im f)²; u = log Q subharmonic with values in [−∞, ∞), interior maximum ⇒ f₁′ = f₂′ = 0 | PASS |
| Lemma D | curvature equation Δw = e^{2w} − 1; w bounded above at cone points under (a); w⁺ subharmonic, removable, constant | PASS |
| Lemma Q | x² ∈ μ₄ ⟺ x ∈ μ₈ with equal local degree; doubled degree at 0, ∞; slack normalisation agrees | PASS |
| Lemma M | degree 5, 8 simple critical points over {0, ∞, ±1}, B fixed and unramified; m = 8a, slack 0 (count checked) | PASS (`lattes5.py` PASS) |
| §5, b ≤ 3 | b = a + s₁ + m/2 and s ≤ 2·deg − 2 leave only (2, 1, 0); the rest is numerical and labelled so | PASS (`aprime_b3.py` PASS) |
| Theorem E | (2) trace gap for products of two elliptic involutions; (3) e^{η(d)}d = arccosh(cosh d + 1); (4) integral argument | PASS (`thme_constants.py` PASS); S1 |
| Lemma N | maximum principle on a nodal domain without a pole; Euler count on V₀ ≅ P¹ for type (1, 1) | PASS |
| Corollary E–N | qualitative Harnack | S2 |
| Lemma C1, C2, Prop. C′ | Kummer group R^⊥; odd locus O₁^χ Δ O₂^ψ; label-differing ⇒ Ω; −B_c = B_c | PASS (`component_check.py` PASS) |

SHOULD FIX (both applied in the audit commit):
- S1. Theorem E(5) used η(d₂) ≥ η(ℓ) without saying why d₂ ≤ ℓ; it follows from the first half of (3).
- S2. Corollary E–N needs γ₁ ∪ γ₂ at distance ≥ 1 from the poles for the Harnack inequality; this is not implied by
  Theorem E(5). Relabelled [outline]. Nothing else in E15 depends on it.

Not checked: statements of E10–E14 that E15 cites (they carry their own audits). The overall conclusion of E15 —
the core E12 §5 is not closed and no degree bound is obtained — is confirmed.
