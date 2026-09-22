# Local support-conditioned Picard refinement

Startup authority: MAIN PR #1826 at `ac47d459ff4c4611c12f3ffe0634ab8e2a8bc5fd`;
repository main `da573f048a82a63e459be1343fb002e663b60875` is the merged baseline,
not the live controller. Both retain the certified upper bound
138652739800650593494 on 17128 strata, not an exact residual identity set.
The exact 1% target is ceil(bound/100) = 1386527398006505935.
No OPEN cross-lane demand preempts lane 178. Research branch origin:
`2e910d74e723ca7de0de1f483f618ed0b457afe0` on PR #1821.
Most recent independent hostile-audit PASS: head
`0597e0aef4dd824e4b106d19f4215fe6e983823c`, review 5272494027.
This new computation remains unaudited and zero credit.

## Candidate selection

The earlier e32 256-key measurement pilot gave exact tightening zero;
it measures receipt size but does not justify filling its 989 remaining units.
The top16 e192 refinement gives 61600343972619, only about 0.0000444%
of the live bound. Both results remain retained unchanged.

The active route applies a common Picard energy condition to all eligible e.
The existing support-qBC band4 code is executing on the 178 Actions surface;
this local worker refuses b=48..59. It never runs the MAIN GRF04/HPADJ22
parent or c-shard worker. The two routes can address overlapping mathematical
candidate populations, so their savings must never be added without an exact
intersection adapter. No disjointness from the MAIN refinement is claimed.

Band3 (b=36..47) contains 35641966335542218797 across all 178 rows,
versus 24348355963238288318 for band5. This is a priority heuristic,
not a prediction of the g1-d192 row's saving. Begin with one b=47 exact
job, retaining every c contribution. Extend only using measured reduction
and runtime. A long job is valuable only if its mass/reduction merits it.

## Necessary inequality and accounting

For g1-d192, write q=qA+qBC and t=x0+x1+x6+x9. The locked signature
factorization has energy q/2+(d/2-2*x4-t)^2/12. Picard parity implies a
residual penalty of at least p0/2+p1/10, where p0=(b+c) mod 2 and p1=a mod 2.
Thus a necessary condition is

    60*q + 10*z_min^2 + 60*p0 + 12*p1 <= 15*d^2/2 + 120*d + 240 - 240*g.

The support-conditioned interval is a relaxation of the possible t values
at fixed b,c,qBC and H support. Squared distance to that interval lower-bounds
the actual squared z. Filling interval holes can only weaken rejection.
Current HPADJ22 histogram multiplicities, x4 capacity and eligible-e counts
are preserved. No statistical independence or min-of-counts saving is used.
Each realized qA bin replays the existing separated baseline rule exactly.
Different b receipts are disjoint within this route; uncomputed b/cells stay
at their current bound. A numeric replacement still requires independent
hostile audit and a MAIN consumer. No MAIN state is changed.

## Execution and reproducibility

`run_hpadj22_zero_center_support_qbc_local_b.py` is an execution-only extension
of the support-qBC worker at the branch origin. It restricts computation to
one b, keeps g1-d192 fixed, emits c progress, and writes a canonical receipt
atomically only after the full b completes. It checks a fresh committed
runkey generation, exact worker blob, authorized b, and execution HEAD before
loading expensive dependencies. Existing receipt paths fail closed.

Run from an LF checkout with Python and SymPy, with the locked HPADJ22 source
checkout at `4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2`:

    python run_hpadj22_zero_center_support_qbc_local_b.py --repo-root ROOT --source-root SOURCE --b 47 --before COLD_COMMIT --head ARM_COMMIT --output RECEIPT

Local concurrency is one because available RAM was approximately 1.8 GiB.
No GitHub compute is authorized or dispatched by this local runkey.
Durable receipts and logs live outside the repository; budget is 8 MiB.
Every completed b must be validated before reuse. Partial b output has no
reusable exact credit. Record wall/CPU times; do not infer zero pruning from
timeout. No workflow/runkey on PR #1826 is changed.

## Candidate ledger

- LIVE: support-conditioned qBC interval across high-mass b, first g1-d192.
- UNTESTED: simultaneous exact minimum for b,c,t,H-support, stronger than the
  maximum of separate support and b,c,t minima; needs independent regression.
- UNTESTED: preserve feasible t holes rather than their parity hull.
- UNTESTED: extend the integer necessary condition to other even-d rows after
  exact baseline/source checks. All-row band mass is not row-level ROI.
- BLOCKED_FOR_PRIORITY: sequential low-e receipt filling, observed pilot
  tightening zero; reopen on a source-locked high-mass/high-reduction selector.

CYCLE_ROUTE_STATUS=PASS_NEXT_GATE_UNCHANGED
CYCLE_ACTIVE_RECEIVER=SAME_POPULATION_SUPPORT_QBC_PICARD_NECESSARY_CONDITION
CYCLE_LIVE_CANDIDATES=1
CYCLE_UNTESTED_CANDIDATES=3
CYCLE_EXHAUSTIVE_VIEW_AUDIT=false
CYCLE_BLIND_REDISCOVERY=false
CYCLE_SPLIT_TRIGGERED=false
CYCLE_PARKING_AUDIT_COMPLETE=false
