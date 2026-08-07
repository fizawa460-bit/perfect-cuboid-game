# Stage12 archive index

This index answers two questions for the frozen Stage12 history:

1. **which task used this script/data?** — encoded by the directory name;
2. **what does the file do?** — encoded by the short filename.

## Mathematical/audit scripts and reports

| Task | Script(s) | Data | Role |
|---|---|---|---|
| N1b | `scripts/n1b/audit_primitive_joint.py`, `scripts/n1b/update_memo.py` | `data/n1b/primitive_joint_report.json` | primitive-compatible shared-`p` joint count |
| N1c | `scripts/n1c/audit_global_mobius.py`, `scripts/n1c/update_memo.py` | `data/n1c/global_mobius_report.json` | global Möbius consistency |
| N1d | `scripts/n1d/audit_analytic_exit.py`, `scripts/n1d/update_memo.py` | `data/n1d/analytic_exit_report.json` | analytic-exit audit |
| 2 | `scripts/2/audit_hyperbola.py`, `scripts/2/update_memo.py` | `data/2/hyperbola_report.json` | shared-`p` hyperbola coordinates |
| 2b | `scripts/2b/audit_average.py`, `scripts/2b/update_memo.py` | `data/2b/average_report.json` | multiplicative-weight average |
| 2c | `scripts/2c/audit_gao_zhao.py` | `data/2c/gao_zhao_report.json` | Gao--Zhao compatibility |
| 2d | `scripts/2d/audit_modular_hyperbola.py` | `data/2d/modular_hyperbola_report.json` | modular-hyperbola compatibility |
| 2e | `scripts/2e/audit_divisor_dyadic.py` | `data/2e/divisor_dyadic_report.json` | divisor expansion / dyadic ranges |
| 2f | `scripts/2f/audit_main_term.py` | `data/2f/main_term_report.json` | formal main term and local density |
| 2g | `scripts/2g/audit_uniform_error.py` | `data/2g/uniform_error_report.json` | uniform lattice error |
| 2h | `scripts/2h/audit_poisson_split.py` | `data/2h/poisson_split_report.json` | Poisson / modulus split |
| 2i | `scripts/2i/audit_exponent_budget.py` | `data/2i/exponent_budget_report.json` | exponent budget |
| 2j | `scripts/2j/audit_boundary_layers.py` | `data/2j/boundary_layers_report.json` | primitive-first boundary layers |
| 2k | `scripts/2k/audit_final_remainder.py` | `data/2k/final_remainder_report.json` | final average remainder / Euler constants |
| 2l | `scripts/2l/audit_dlb_hypotheses.py` | `data/2l/dlb_hypotheses_report.json` | de la Bretèche hypothesis audit |
| 2m | `scripts/2m/audit_iterated_selberg_delange.py` | `data/2m/iterated_selberg_delange_report.json` | iterated Selberg--Delange route |
| 2n | `scripts/2n/audit_coupled_region.py` | `data/2n/coupled_region_report.json` | coupled radial/height region |
| 2o | `scripts/2o/audit_analytic_closure.py` | `data/2o/analytic_closure_report.json` | analytic closure lemmas |
| 2p | `scripts/2p/audit_final_bookkeeping.py` | `data/2p/final_bookkeeping_report.json` | final bookkeeping audit |

## Review/bundle builders

Historical review tooling is grouped under `scripts/review/`:

```text
build_r01_page.py
build_r02_page.py
build_legacy_review_bundle.py
build_legacy_r05_bundle.py
build_2j_2p_review_html.py
build_r03_limited_rereview.py
build_r04_full_rereview.py
build_r05_full_rereview.py
build_r06_full_rereview.py
build_r07_zero_base.py
build_r08_self_contained.py
build_r09_self_contained.py
verify_manifest.py
```

These are archive assets, not active CI.

## Historical documents and review artifacts

- `docs/` preserves the original Stage12 derivation/repair documents and superseded finals.
- `review/manifests/` preserves old audit/re-review manifests.
- `review/html/` preserves old generated review pages.
- `workflows/` preserves disabled historical GitHub Actions files and trigger markers.

No archive relocation changes the mathematical content of the frozen R09 proof.
