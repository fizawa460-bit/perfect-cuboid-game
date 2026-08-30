# Stage32-21ad fresh boundary audit

Status: `PASS`

Verdict: `PASS_STAGE32_21AD_FRESH_ZERO_PRUNE_BOUNDARY_AUDIT`

## Audited production boundary

Authoritative production evidence is the exact 16-shard FULL178 census from run `33313814094`, aggregate job `99263722930`.

Locked aggregate:

- FULL178 rows: `178`;
- prior image + unconstrained-quadratic slices: `2018569`;
- continuous-KKT survivors: `679337`;
- 32-21ac anti-fixed-coset additional prunes: `0`;
- survivors after the audited predicate: `679337`;
- exact integer-u probes: `1971035` total, `114` maximum for one slice;
- zeroed e-strata: `0`;
- zeroed rows: `0`;
- artifact `9732838513`, size `5429` bytes;
- artifact ZIP SHA256 `5c2ba19b704f9466ad8bd083a4ad14a2821aad5ab0b5829999dbd9ab3bca98cf`;
- aggregate canonical SHA256 `9bf4aba655a6df81e621e3f78e19b16460f1138410ed118f18e25fcb77bf24ad`.

The evaluator is source-locked to audited 32-21ac certificate SHA256 `2c227d773aaf6a6543ae89419c468d85fd4ebd42422eb6f4c8ac60b2e7227c8e` and FULL178 manifest SHA256 `46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23`.

## Fresh audit method

The audit does not merely trust the production aggregate. It downloads all 16 immutable credited shard artifacts and independently checks:

1. each shard JSON canonical SHA is recomputed from its content;
2. shard indices are exactly `0..15` once each;
3. the deterministic mod-16 row partition is rebuilt from the locked FULL178 manifest;
4. every shard's selected rows exactly match that rebuilt partition;
5. all `178` FULL178 rows occur exactly once across the shard evidence;
6. row-summary prior / continuous / prune / survivor / zero-e totals reconcile with each shard payload;
7. decision-reason, quotient-coset, and penalty population totals each reconcile with the continuous-survivor population;
8. the 32-21ac evaluator is independently rebuilt from retained Picard/marking data, reproducing 128 cosets, 127 positive minima, one zero minimum, and minimum positive bound `1/572`;
9. all shard semantic firewalls remain closed;
10. the independently re-aggregated totals reproduce exactly `2018569 / 679337 / 0 / 679337`.

Fresh audit implementation:

- `stages/stage32/residual-32-01-production/audit_stage32_21ad_boundary.py`
- `.github/workflows/stage32-21ad-boundary-audit.yml`

## Audit evidence

First fresh PASS:

- run `33314674227`;
- job `99265778889`;
- artifact `9733074341`;
- artifact ZIP SHA256 `206cd3fc75f69c95bbc7812467c6d81d12f1ad5a46e6f0508e0f69e36441ddbc`.

The verifier was then hardened so it accepts both the pre-audit result status and the final audited bookkeeping status. A second fresh run confirmed this bookkeeping hardening did not change the mathematical certificate:

- hardened run `33314886424`;
- job `99266357586`;
- artifact `9733137852`;
- size `2142` bytes;
- artifact ZIP SHA256 `15d11651104172a9f89c22c144acdff72f6dfc46e7a7b868a45bf05e9f67efa6`;
- canonical audit SHA256 `1f2e61ef29cf6000b8cc98906a5dcf3f2a4d15a7b405be2e40ef9c0de3bfab0e`.

The canonical audit SHA is identical across the two PASS runs.

## Exact conclusion and non-claims

The audited conclusion is only:

> On this exact FULL178 continuous-KKT population, the audited 32-21ac cheap anti-fixed coset-minimum predicate has zero additional pruning power.

32-21ac is not revoked: its mathematical inequality and safe negative predicate remain valid. What is dominated is using this same cheap bound as another FULL178 pruning pass without a semantic strengthening.

The result does **not** imply `UNSAT`, route impossibility, numerical Picard-row completion, theorem credit, receiver discharge, route-color change, or perfect-cuboid existence/nonexistence. `UNKNOWN != UNSAT` remains in force.

## Operational audit

The credited parallel production used 16 effective heavy jobs, within the Stage32 cap of 18. The earlier one-runner full attempt was canceled before producing a result and was not promoted. On later bookkeeping synchronizations, the parallel heavy shards remain skipped unless the dedicated parallel run-key changes; the old pairing-prefix calibration remains skipped. Both 32-21ad run-keys are consumed and disarmed.

No terminal-family materialization, legacy prefix DFS, or 59-dimensional anti-fixed closest-vector search was executed.

## Release state

`32-21ad` is an audited checkpoint and PR #1466 is checkpoint-merge-ready, but automatic merge is not authorized. No further heavy production is released here.

After an explicitly authorized merge of PR #1466, reread authoritative `main`, `AGENTS.md`, and `stages/stage32/controller.json`, then select a materially stronger post-32-21ad strategy. That next strategy is intentionally not precommitted by this audit.
