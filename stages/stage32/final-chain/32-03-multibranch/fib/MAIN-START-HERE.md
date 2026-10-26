# Stage32 MB-FIB internal startup

MB-FIB is an MB-local auxiliary producer for 32-03. It is not a Stage32 claim-DAG lane and is not an operator entrypoint.

## Entry condition

Open this surface only when the current MB STATE or an exact retained MB handoff explicitly requires MB-FIB work.

Read:

1. current Stage32 MAIN authority;
2. current MB STATE/consumer handoff that selected MB-FIB;
3. this file;
4. `stages/stage32/final-chain/32-03-multibranch/fib/STATE.json`;
5. only source/evidence named by the active FIB leaf;
6. cross-lane demand state only when the selected leaf has a concrete dependency.

Do not preload unrelated MB history or old fibration routes.

## Boundary

MB-FIB owns only its bounded fibration/Picard64 producer work. It does not own MB completion, MAIN promotion, theorem/endpoint credit, Stage32 closure, or merge authority.

Its timeout, freeze, or audit failure does not automatically freeze ordinary MB work unless MB explicitly depends on that frozen handoff or a shared Stage32 safety gate fails.

Heavy execution remains runkey-gated, resume-first, source-locked, and subject to the Stage32 concurrency/storage limits.

A result becomes consumable only through an exact MB handoff recording producer identity, certificate identity, population semantics, and scope. MB-FIB never self-promotes.
