# CERTLIFT-01 — fixed-exceptional-mass profile

Status: **L1 audited separator candidate only**. This is not a symbolic obstruction lemma and carries no MAIN/theorem/closure credit.

The read-only CUT193..CUT198 source scope contains 1,530 disjoint `g1-d008/e8` blocks (172,890 terminals). The audited split is 1,433 closed blocks and 97 residual controls. Reconstructing only the source-locked pre-solve e8 prefix signature gives the following table for `M10 = fixed_exceptional_mass`:

| M10 | closed | residual |
|---:|---:|---:|
| 2 | 0 | 2 |
| 3 | 0 | 15 |
| 4 | 14 | 37 |
| 5 | 103 | 30 |
| 6 | 267 | 13 |
| 7 | 443 | 0 |
| 8 | 606 | 0 |

Therefore the exact audited-scope predicate `M10 >= 7` selects **1,049 / 1,433 closed blocks** and **0 / 97 residual controls**. It succeeds independently in every source wave: CUT193 148, CUT194 155, CUT195 156, CUT196 180, CUT197 208, CUT198 202. The next weaker monotone threshold `M10 >= 6` already hits 13 residual controls, so 7 is the minimal threshold of this one-parameter monotone form on the audited scope.

Interpretation: this is a compact pre-solve signature worth lifting. It does **not** yet prove `M10 >= 7 => Picard64 completion infeasible`; the next CERTLIFT task is to derive that implication from the source-locked mod-2 finite-ring/HNF equations, or produce a deterministic counterexample outside the bounded audited waves. No CP-SAT/Z3 rerun is used by `certificate_profile.py`; it reconstructs the six wave scopes and the prefix mass profile from the deterministic e8 adapter plus the frozen residual-control ledger.

Artifacts: `CERTIFICATE-LEDGER.json` freezes exact source heads, audit/result canonicals, wave scopes, and residual controls. `certificate_profile.py --self-check` replays the profile and rejects any source-manifest, scope, residual, or MASS7 drift.
