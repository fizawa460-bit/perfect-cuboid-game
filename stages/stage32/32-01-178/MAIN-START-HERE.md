# Stage32 32-01-178 retained startup boundary

Status: **PARKED / RETAINED after audited 32-01 completion**.

This is not an ordinary operator entrypoint. `stage32mainbatch` must not enter this surface unless current MAIN explicitly reopens a concrete 32-01 obligation or a verified regression invalidates the retained numerical-census claim.

## Reopen-only read order

If MAIN explicitly reopens 178 work:

1. current `stages/stage32/MAIN-STATE.json`;
2. this file;
3. the exact reopen reason / regression boundary;
4. the selected current 178 node/state;
5. only retained evidence named by that node;
6. cross-lane demands only if the reopened node has a concrete dependency.

`MISSION.json`, Generation-1 states, old roadmaps, and audit receipts are retained history, not startup authority.

178 never self-promotes to MAIN credit. Heavy execution remains separately authorized. No merge without explicit authorization.
