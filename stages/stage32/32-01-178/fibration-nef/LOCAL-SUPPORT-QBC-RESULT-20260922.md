# Local exact boundary: support-qBC, 2026-09-22

This is a new retained research boundary, not hostile-audit acceptance.
Live MAIN is PR #1826, head ac47d459ff4c4611c12f3ffe0634ab8e2a8bc5fd
at startup: certified upper bound 138652739800650593494, 17128 strata.
MAIN/theorem/endpoint/Perfect-Cuboid credit stays zero/unchanged.
No FULL178 run is inspected, cancelled, rerun, or written by this wave.

## Completed exact measurement

Source row 22, g1-d192, b=47, all eligible c,a,e,x4/support/q bins:

| Quantity | Exact value |
| --- | ---: |
| HPADJ22 current mass | 187902185746998436 |
| Parent qBC refined mass | 180167535944018713 |
| Support-qBC refined mass | 176436593457463322 |
| Exact current-to-support reduction | 11465592289535114 |
| Additional support reduction vs parent | 3730942486555391 |

Receipt: `local-support-qbc/row022-b047.json`.
Canonical SHA256 (omit its canonical field before sorted compact JSON hashing):
`2bbc6957864fcb439dc991a26a3ea223d6f3169af7352df8b28966a058a8b47b`.
Execution head a94569a3314a1e59b318355722f5f79111d13218;
authorization-before 4b8922a705405405dda296dd0d804120b22896f2;
worker blob 2c1abfd6d921122d9cf6a67a2f2251b95318e5fd.
Source checkout 4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2.
All transitive production loader checks ran before counting. Each realized
qA current-limit query was checked against the separated current baseline.

Receipt wall 520.4099493000031 s, CPU 483.078125 s. Observed sampled peak
working set 131301376 bytes (not a guaranteed process high-water mark).
Approximate descriptive ROI: 7.93e16 exact reduction/wall-hour;
global reduction 0.0082692865%. These ratios are not mathematical credit.
Supervisor telemetry's last-poll elapsed value is stale; receipt timing is
authoritative. Raw stdout/stderr and telemetry remain under
`C:\CodexWorktrees\stage32-178-local-support`; stderr was empty, exit code 0.

`verify_local_support_qbc_receipt.py` PASS checks canonical hash, immutable
execution worker/key, dependency blobs, cell sums, strict-cell identity,
integer reduction, global reference and credit firewalls. This is structural
and source verification, not independent exhaustive replay/hostile audit.
The completed single-b key is now cold. Reuse its historical arm; do not arm
it again or rerun it to populate coverage.

## Bounded high-degree extension

The same necessary inequality is valid for every even d and g in {0,1}:

    60(qA+qBC)+10*z_min^2+60*p0+12*p1
      <= 15*d^2/2+120*d+240-240*g.

It follows by multiplying the exact Schur energy plus Picard parity lower
bound by 120. Ignoring e-dependent nef caps only relaxes the necessary
condition. No identity requires d=192 or e=32. The generalized worker keeps
all source multiplicities and eligible-e counts, and verifies the row against
the locked manifest. All c=0..d/2 are now retained, including zero reasons.
The original completed worker is unchanged, preserving its source lock.

New worker: `run_hpadj22_support_qbc_local_row_b.py`.
Regression: 4384 exact bounded support/convex-minimizer cases PASS.
Independent collaborator inspected the all-even-d algebra and generalized
loop; this review is not the repository's hostile audit.

Authorized upper envelope: 12 highest-degree source rows, b60..71 then
b47..36, excluding completed (22,47): at most 287 disjoint row,b units.
The key explicitly names every row and b. This is a priority heuristic based
on high-degree mass and the measured b47 ROI, not a predicted exact saving.
Uncomputed units remain at their existing bound, not zero.
The dispatcher stops new work at exact saving >=1386527398006505935 (1%),
after 12 elapsed hours, any failed receipt, or resource limits. Running units
are allowed to finish. No automatic retry, no self-rearming, no next wave.
Stop/pivot earlier if measurements show poor value.

Resource preflight: 6 physical / 12 logical CPUs, 7.82 GiB RAM, about
1.7 GiB available; first worker sampled ~125 MiB, C: >80 GiB free.
Start two workers; allow four only after two successful completions and
available RAM >=1 GiB. Below 512 MiB available stops new dispatch. Each
receipt records wall/CPU and OS peak RSS. Conservative evidence budget64MiB
(measured first receipt43821 bytes); no GitHub artifact upload. Added Actions
concurrency=0. The Actions-specific18-job ceiling is unaffected.

Dispatcher: `run_local_support_qbc_wave.py`; every start needs an exclusive
durable launch sentinel. Atomic status and per-unit receipts survive crashes.
No existing logs/receipts are overwritten. Resume is a separate explicitly
authorized generation after validation, never automatic recovery by rerun.
Use a detached execution worktree to keep the armed head immutable while
retaining later evidence on PR #1821. Monitor only this local process hourly.

## Accounting and promotion

The row,b key is disjoint in the locked HPADJ22 population. A partial consumer
can replace each completed old contribution with its refined contribution and
leave every uncomputed contribution unchanged; require unique coordinates,
matching baseline/source locks, exact cell sums and hostile audit first.
This does NOT prove disjointness from MAIN GRF04 refinements. Never add this
saving to a GRF04 saving: a same-population intersection adapter is required.
1% here means candidate reduction relative to the fixed startup bound, not
an authorized change to current MAIN or a new exact residual identity set.

Next promising route if this relaxed cut saturates: simultaneous b,c,t/support
minimum (rather than max of separate minima), then preserving feasible t holes.
Neither stronger variant is armed or credited by this boundary.
