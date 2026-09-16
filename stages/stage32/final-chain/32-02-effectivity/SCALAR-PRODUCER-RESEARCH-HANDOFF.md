# Stage32 32-02 scalar producer research handoff

This file preserves the research reached on PR #1790 without promoting it into MAIN authority.

## Retained research source

- PR: `#1790` — `[Stage32][32-02] exact selected64 Hperp scalar producer research`
- Retained branch: `stage32-02-scalar-producer-research`
- Retained process head: `de53289859bec2b718f7066326e095f969875da0`
- Exact E2E replay predecessor: `c1e8eaeec0e5f53d99ba32a5d374f828b5729354`
- Exact E2E workflow run: `34902750246` — SUCCESS

The two commits after the replay predecessor restored the shared workflow-inventory verifier to current-main form and retired the temporary automatic scalar E2E workflow. They did not change the retained scalar-producer mathematics or evidence.

## Research reached

The retained 32-02 experiment implements a source-locked selected64-to-`Hperp` scalar producer and connects it to the existing RR consumer boundary.

The scalar relation used by the retained route is

```text
N = m^2 * (d^2/16 - C^2)
```

The producer/protocol path was repaired so that:

- retained dependencies are source-locked before execution/import;
- the producer and protocol use the same `STAGE32_32_02_SCALAR_PRODUCER_V1` schema;
- the E2E verifier exercises producer -> protocol -> independent scalar replay -> existing RR consumer;
- record tampering and dependency drift are rejection cases.

The retained known-curve replay reaches:

```text
d = 2
C^2 = -4
N = 272
```

and the E2E result remains RR-inconclusive because the source is not affirmed for the target effectivity claim.

## Audit / credit boundary

This handoff is a research-memory checkpoint only.

- hostile-audit PASS for the retained final #1790 head: **NO**
- MAIN authority mutation: **NO**
- MAIN pruning credit: **0**
- effectivity/existence credit: **NO**
- integral irreducible carrier credit: **NO**
- FULL178 completion credit: **NO**
- theorem / endpoint credit: **NO**
- Perfect Cuboid existence/nonexistence claim: **NO**
- merge authorization: **NO**

Earlier hostile-audit blockers on lock-before-exec and producer/protocol composition were repaired, and an exact E2E replay succeeded on the predecessor head. This record does not upgrade that research to audited consumable authority.

## Resume rule

32-02 is **PARKED / INCOMPLETE**, not finished.

If the user says `32-02の研究途中から開始して`, `32-02を途中から再開`, or otherwise asks to resume 32-02, treat that as an explicit reopen request. Start from this handoff and inspect PR #1790 / retained head `de53289859bec2b718f7066326e095f969875da0` rather than repeating the scalar-producer work from scratch.

Re-establish current-main freshness and obtain a new exact-head hostile audit before any promotion or MAIN credit. Do not infer that PARKED/INCOMPLETE means authority credit is pending automatically; it only records the research continuation point.