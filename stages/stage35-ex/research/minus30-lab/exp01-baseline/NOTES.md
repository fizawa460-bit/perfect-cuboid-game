# EXP01 — row383 baseline replay (2026-11-21)

- Copied materials/negative30-mw-selmer/row383/ to a scratch dir,
  decompressed row378_exact.json.gz and tail_roots_independent.csv.gz
  (the verifier expects the decompressed names).
- Ran verify_spectral383.py with python-flint 0.9.0: exit 0, ~13 s.
- Compared the replay JSON against the stored spectral383.json on all
  14 certified values (score_lower 0.0098858898430937020…,
  prime_term_lower 0.2846007880573495856…, arch_upper
  0.3854638733312249949…, moment_upper 99.186384435239…, bands,
  certified rectangles, contradiction_gap 29/1000): EXACT MATCH.
- tail_recounted=false in the replay (stored tail table used; the
  harness checks its hashes). Full tail recount is a separate option.
- Verdict: the row383 certificate reproduces locally; this is the
  baseline for EXP02a / EXP05-style variations.
