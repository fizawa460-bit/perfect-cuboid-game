# Stage32 32-03 multibranch internal startup

This is an internal execution contract selected by `stage32mainbatch`. It is not an ordinary operator entrypoint.

## Read order after MAIN dispatch

1. current `stages/stage32/MAIN-STATE.json`;
2. this file;
3. `stages/stage32/final-chain/32-03-multibranch/STATE.json`;
4. only the exact evidence named by the current MB obligation;
5. `CROSS-LANE-DEMANDS.json` only when that obligation has a concrete producer/consumer dependency.

MAIN routing always wins over lane-local history. `STATE.json` is the MB resume/frontier projection inside the selected 32-03 unit.

## Ownership

MB owns the R29-LG2-MB multibranch obligations: normalization/branch profiles, delta/genus accounting, Aut(S) quotient semantics, justified finite restrictions, and downstream Picard/effectivity work released by those restrictions.

MB does not own FULL178 numerical census, historical CUT/178 work, MAIN promotion, theorem/endpoint credit, or merge authority.

MB-FIB is an optional MB-local producer. Open it only when MB STATE explicitly selects or consumes its handoff. Do not preload MB-FIB on every MB dispatch.

## Execution / audit

Internal MB work may checkpoint and resume independently, but it cannot self-promote to MAIN. Heavy work still requires the repository authorization/resume rules.

A frozen MB boundary is audited through the Stage32 audit path or its retained specialist audit mechanism as required by the exact boundary. Audit PASS is not merge authorization.
