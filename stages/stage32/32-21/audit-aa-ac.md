# Stage32-21aa-ac fresh boundary audit

Status: `PASS`

Verdict: `PASS_STAGE32_21AA_AC_FRESH_BOUNDARY_AUDIT`

This audit is the meaningful boundary review for the coherent PR #1465 work package:

`32-21aa anti-fixed penalty -> 32-21ab exact quotient adapter -> 32-21ac cheap exact pruning predicate`.

## Load-bearing chain

1. 32-21aa fixes the exact Reynolds projection state. For every canonical residue `r in im(N) mod 64`, exact slice-kernel dual norms give a safe lower bound `lambda(r) <= -q^2` for the anti-fixed component.
2. 32-21ab uses the identical exact fixed-image basis `B` and the unimodular projected Smith transform `T`. Thus a Smith affine state `y=(y0,y1,y2,u,v)` maps exactly to `r=(B*T*y) mod 64`.
3. Integer `(u,v)` move residues in an exact 128-element subgroup. The 16384 residues therefore partition into 128 exact cosets.
4. 32-21ac sets `lambda_C=min_{r in C} lambda(r)`. Hence every lift in the slice obeys `x^2 <= p^2-lambda_C`. Reusing the exact rank-2 integer concave-QP exhaustion against the raised rational threshold is therefore a safe pruning decision.

## Independent rederivation

The audit did not accept the package certificates merely because their CI was green. It independently rebuilt and checked:

- `B*T mod 64`;
- the complete 16384-element projection image from both the original fixed basis and Smith coordinates;
- the free `(u,v)` subgroup, order `128`;
- the exact partition into `128` cosets;
- all `16384` coordinate-Cauchy penalties from the retained dual norms;
- all `128` coset minima;
- `127` positive-minimum cosets and exactly `1` zero-minimum coset;
- minimum positive coset lower bound `1/572`.

A fresh 81-case synthetic Smith-coordinate panel also checked implementation monotonicity and witnesses:

- old exact rank-2 false -> new true: `0`;
- old exact rank-2 true -> new false: `1`;
- zero-penalty coset reduces exactly to the old rank-2 decision on exercised cases;
- every surviving new witness was directly checked against fixed halfspaces and the raised exact rational threshold.

The one additional panel prune is a regression demonstration only, not FULL178 numerical credit.

## Execution evidence

Package CI:
- run `33308996594`;
- job `99250520551`;
- artifact `9731412581`, `3008` bytes;
- 32-21ab SHA256 `07bf0aff16a344ad68fe7179ff797057fca562fd6bafbdaf418155ba0995c8b4`;
- 32-21ac SHA256 `2c227d773aaf6a6543ae89419c468d85fd4ebd42422eb6f4c8ac60b2e7227c8e`.

Fresh audit:
- initial audit attempt failed only in the audit harness at the final witness panel because `quad` was not imported (`NameError`); no PASS/credit was assigned;
- repaired audit run `33309333080`, job `99251414877`;
- audit artifact `9731500315`, `1343` bytes, ZIP SHA256 `520f7f458d71b5b89ec42ed4abf36e1288c312313d284ab988ae6b7a26168b3b`;
- canonical audit SHA256 `5dfd1087d7d1c20baa3475e05e1768edbb9e8f063b20d01ca467a6725b657f1e`.

## Operational audit

During package and audit synchronizations, the historical pairing-prefix workflow could still receive an outer event because of cumulative PR paths. Its cheap authorization job ran, but the compute job was skipped because no fresh dedicated run-key generation was present. No Stage32 heavy production was re-armed.

## Firewalls and release

- FULL178 census: not run;
- legacy prefix DFS: not re-armed;
- 59D anti-fixed CVP: not run;
- 27-digit terminal family: not materialized;
- UNKNOWN != UNSAT;
- numerical row completion: false;
- theorem credit: false;
- receiver credit: false;
- route credit: false;
- perfect-cuboid existence claim: false;
- perfect-cuboid nonexistence claim: false.

Audit release is deliberately narrow: the aa->ab->ac evaluator package is an audited checkpoint. `32-21ad FULL178_COMPRESSED_NUMERICAL_CENSUS` may be planned only after #1465 is merged into the authoritative base; this audit does not arm that production and does not authorize automatic merge.
