# F-01 — slack-0 mismatch spectrum (measured, 2026-11-12)

Status: **floating-point measurement, not a theorem.** Zero credit. Script `f01_mismatch_spectrum.py`, output `f01.out`
(about 27 minutes on this PC). Setting: route-E E10 §2 / E11 (k = 8, γ = 0, s₁ = s₂ = 0).

## What was measured

- p₁ runs over all slack-0 maps of degree a, and p₂ = q∘T over all slack-0 maps q of degree b.
- T runs over **every** Möbius map with at least 3 coincidences between O₁ and T⁻¹(O_q), with any labels.
  - E11 used only label-matched triples, which was enough for |Ω| ≤ 4.
  - Each T is counted once, with weight 1/C(c,3) for c coincidences.
- A T with ≤ 2 coincidences has |Ω| ≥ |O₁| + |O₂| − 4.
- |Ω| = |O₁| + |O₂| − 2j − h (E10 §2), where j counts label-agreeing coincidences and h label-differing ones.
- Birationality uses the E11 two-fibre test. It is automatic when gcd(a, b) = 1.

## Result

| (a,b) | \|O₁\|+\|O₂\| | ω_min over birational pairs | (j, h) at the minimum | max 2j+h (birational) | # extremal T | trivial value | non-birational \|Ω\| below ω_min |
|---|---|---|---|---|---|---|---|
| (1,1) | 12 | 0 (Klein graphs), then 4 | (6,0); (2,4) | 12 | 4; 12 | 8 | — |
| (1,2) | 14 | **6** | (4,0) | 8 | 96 | 10 | — |
| (1,3) | 16 | **8** | (4,0) | 8 | 96 | 12 | — |
| (2,2) | 16 | **6** | (4,2) | 10 | 192 | 12 | 0, 4 (bidegree (1,1)) |
| (2,3) | 18 | **10** | — (min of the histogram; all pairs birational) | 8 | 1152 | 14 | — |
| (3,3) | 20 | **10** | (4,2), (5,0) | 10 | 384 | 16 | 0, 4, 6, 8 (p₂ = M∘p₁) |

Checks:
- The (1,1) control reproduces E11 ({0: 4, 4: 12}).
- (2,2), (2,3) and (3,3) are consistent with E11: there is no birational configuration with |Ω| ≤ 4.
- Separation gap: the largest accepted coincidence is 4.7·10⁻¹²; the smallest rejected distance is 1.9·10⁻⁶ (at (3,3)).

## Reading

1. **ω_min grows with the degree.** For a ≥ 1, b ≥ 2 the data fit ω_min = 2(a+b) when a ≠ b and 2(a+b) − 2 when
   a = b. That is five points, all exact on the fit [estimate: pattern only].
2. The reason is that **the number of coincidences does not grow.** Over birational pairs, 2j + h ≤ 10 and j ≤ 5 at
   every measured bidegree. Lemma K (T0 with c₀ = 2) allows j up to 2(a+b) = 12 at (3,3).
3. Problem W needs |Ω| ≤ 4, i.e. 2j + h ≥ |O₁| + |O₂| − 4 = 2(a+b) + 4. If "2j + h ≤ 10 for all slack-0 birational
   pairs" held uniformly, slack 0 would be closed for a + b ≥ 4. That is goal G4.
   - Under plan F4, a uniform ω_min bound is a restatement of the goal, not a tool spec. What is new is the measured
     shape: the coincidence count stays bounded, far below the c₀ = 2 line.
4. The extremal counts are multiples of 96 (or 4 and 12 at (1,1)). This suggests the extra coincidences come from
   symmetries of (P¹, B) [heuristic, not checked].

## Next (per plan F3, row 1 of the decision table)

F-02: build the slack-0 maps of degree 4 and measure (2,4), (3,4) and (4,4). This tests the fit.
- Degree 4 allows fibres of type (2,2) over B. The degree-3 construction must be extended (E11 §5).
- Work: construction code first; running time to be estimated before any run over 3 days (plan F5).
