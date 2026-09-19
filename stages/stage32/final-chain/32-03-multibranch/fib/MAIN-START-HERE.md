# Stage32 MB-FIB startup

This is the single startup contract for the short operator command `stage32mb-fib`.

MB-FIB is an auxiliary producer for 32-03 multibranch / MB104. It is not the ordinary MB controller. Its purpose is to run bounded fibration/Picard64 work in parallel without moving, freezing, or auditing the `stage32mb-mainbatch` active leaf.

## Command modes

Use only the short base command:

- `stage32mb-fib` — ordinary producer research / bounded computation;
- `stage32mb-fib 監査` — exact-head hostile audit of the dedicated MB-FIB surface.

There is intentionally no separate canonical `stage32mb-fib-audit` command.

Audit intent never changes mathematical authority. If the dedicated STATE is not frozen to one exact audit head, audit mode fails closed instead of guessing a target.

## Ordinary startup

Read only, in this order:

1. `AGENTS.md`;
2. this file;
3. current `stages/stage32/MAIN-STATE.json`;
4. current `stages/stage32/proof/CROSS-LANE-DEMANDS.json`, restricted to demands involving lane `MB-FIB`;
5. `stages/stage32/final-chain/32-03-multibranch/fib/STATE.json`;
6. only the exact source/evidence paths named by the active MB-FIB leaf.

Do not preload the ordinary MB STATE or MB history. Read the MB lane only when the MB-FIB STATE names an exact consumer handoff/source lock that requires it.

## Ownership boundary

MB-FIB owns only the auxiliary fibration/Picard64 producer route selected by its own STATE. It may import exact mathematics or source-locked code from archived MB or 32-01 assets, but it does not inherit their operational authority.

MB-FIB does not own:

- the `stage32mb-mainbatch` active leaf;
- MB104 completion;
- MAIN authority or promotion;
- theorem / endpoint / Perfect-Cuboid credit;
- ordinary MB audit state.

An MB-FIB audit failure, heavy timeout, or runkey freeze does not freeze ordinary MB mainbatch by itself. MB is affected only when it explicitly consumes a frozen/audited MB-FIB handoff or when a shared Stage32 authority/safety gate independently fails.

## Current producer route

The bootstrap route is the size768 fibration-improvement shell package imported from archived PR #1825.

Support: `000707000f0f`

Compact exceptional indices: `[0,1,2,3,8,9,10,11,24,25,26,32,33,34]`

Candidate shells:

- degree 10: `(P.F,M)=(30,10),(34,9),(38,8)`, H-perp norm 400;
- degree 12: `(P.F,M)=(36,12)`, H-perp norm 144.

The producer first performs exact Picard64 candidate enumeration using the source-locked MB-native H-perp/CloseVectors machinery. Zero candidates is only a producer result. MB must separately compose it with the retained degree reduction / degree-8 classification before claiming a global fibration optimum. Surviving candidates go to the degree-10 residual-sextic or degree-12 `QA+QB+degree4` geometry.

Do not drift to the late Z55+ analytic chain merely because this producer is blocked.

## Heavy execution

The command itself never arms heavy compute. Before execution, the dedicated runkey must be semantically advanced and armed on the dedicated MB-FIB research PR, with pilot-first, resume-first partitioning, bounded Stage32 heavy concurrency, compact certificates, storage preflight, and exact source locks.

## Handoff to MB

MB-FIB outputs are producer evidence only. A result becomes consumable by MB only through an exact audited handoff containing producer PR/head, certificate identity, population semantics, and result scope.

The consumer MB lane decides whether and how the result closes an MB obligation. MB-FIB never self-promotes that handoff to MAIN/theorem/endpoint credit.

## Merge

Do not merge a research/audit PR without explicit user authorization.
