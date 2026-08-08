# Literature radar — cross-track

Use this file only when one theorem or artifact has a concrete hook in at least two active Stage14 tracks.

## DIRECT / NEAR

### Shimada level-4 computational package
- Link: https://home.hiroshima-u.ac.jp/ichiro-shimada/ComputationData.html
- Gives: the exact rank-20 NS coordinate system, `fsigma`, 40 distinguished `(-2)` curves, chamber data, `AutX0f`, torsion translations and `Galmu` for the Stage14 level-4 modular K3.
- Stage14 hook: primarily `14-4`; any explicit `M`-degree-4 bisection classification immediately feeds `14-s` and reactivates `14-t`.
- Fit: NEAR -> computationally actionable.
- Missing: express the physical class `M` in Shimada's fixed `S0` basis, then run `C^2=-2`, `fsigma.C=2`, `M.C=4` with chamber/orbit/Galois checks.
- Checked: 2026-08-09

### Least-point height pipeline: Petsche -> Naccarato -> Stage14-s
- Link: Petsche `math/0508160`; Naccarato DOI `10.4171/RLM/945`
- Gives: an explicit non-torsion canonical-height lower bound in terms of minimal discriminant and Szpiro ratio, followed by a worked point-counting use of that lower bound.
- Stage14 hook: if the Stage14 conductor/discriminant calculation gives controlled Szpiro ratio, this becomes a concrete arithmetic comparison with the s3 physical upper window; resulting exceptional small-point classes should be compared with 14-4 bisections.
- Fit: NEAR
- Missing: prime-by-prime minimal-model/conductor analysis for `W^2=Z(Z-S^2)(Z+X^2)`.
- Checked: 2026-08-09

### Le Boudec large-prime-factor + complete-2-descent architecture
- Link: https://arxiv.org/abs/1802.07136
- Gives: Lemma 1 preserves a quantitatively large parameter set after imposing a uniquely identifiable large prime factor; Lemma 2 uses complete 2-descent to bound parameters carrying an anomalously small non-torsion point.
- Stage14 hook: compare directly with the Stage14-s1 split covering equations. A successful transplant would give an arithmetic small-point filter independent of the K3 lattice route; a failure will identify the precise structural obstruction.
- Fit: NEAR / high-priority method transfer.
- Missing: replace squarefree twist parameter `d=mp` by the primitive Pythagorean base and show the large-prime condition survives with enough density in the physical-height variable.
- Checked: 2026-08-09

## BLOCKED

_None recorded._

## INBOX

_Next cross-track handoff triggers: (1) `M` identified in Shimada coordinates -> notify 14-4 immediately and send resulting bisection orbits to 14-s/14-t; (2) Stage14 Szpiro ratio controlled -> notify 14-s; (3) Le Boudec Lemma 2 matches the s1 split covering variables -> open a dedicated arithmetic proof task rather than continuing broad literature search._
