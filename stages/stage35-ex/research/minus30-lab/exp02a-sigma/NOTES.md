# EXP02a — Hadamard point σ variation on the row383 fixture (2026-11-21)

Change: fixture383.json "hadamard_real_abscissa" only.
Baseline σ=7/5: score_lower 0.0098858898430937020… (threshold 49/5000),
moment_upper 99.186384435239… < 100.

- σ=6/5: verifier aborts (assertion at the moment bound). Moment upper
  bound becomes 133.2333448343481425486… > 100. No score/bands are
  produced. DEAD as a drop-in variant.
- σ=8/5: same abort. Moment upper bound 107.9495764860553089217… > 100.
  DEAD as a drop-in variant (smaller deterioration than 6/5).

Observation: at σ=7/5 the moment margin is only 0.81, and both
neighbours break the certificate, so 7/5 sits at a local optimum of the
moment bound for this fixture. The threshold 100 is paired with
ε=1/100 (the contradiction needs −ε·Mχ > −1), so it cannot simply be
raised; rescuing either variant requires redesigning ε and the bands
together — that is a separate experiment, not a variant of this one.
Verdict: the σ direction, as a single-field change, is exhausted.
