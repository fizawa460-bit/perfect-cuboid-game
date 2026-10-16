# Stage32 HPADJ22-UNIBRANCH — HPADJ22 direct count composed with the unibranch node-Hurwitz support requirement

Status: `RESEARCH_RESULT__HOSTILE_AUDIT_PENDING__MAIN_AUTHORITY_UNCHANGED`.

This is a necessary-condition research result. It does not change MAIN authority (V50, 511353002049). It grants no MAIN, effectivity, receiver, theorem, endpoint, Stage32-closure, Perfect-Cuboid or merge credit.

## Statement

Two counters are combined on the same terminal population:

- **HPADJ22.** The exact direct count consumed in the V44–V47 lineage (`management/hpadj22-fast-global/benchmark_direct_count.py`, blob `e965ab0a`). Its source chain is at HPADJ22 head `4bd68ded`.
- **UNIBRANCH-NODE-HURWITZ** (#1838, consumed as MAIN V50).
  - It proves that a unibranch curve with g ≤ 1, not a fibre component, satisfies `nu >= ceil((d+e)/2) - 2g + 2`.
  - Here `nu` is the number of exceptional curves met.

The two are composed as follows. Inside the HPADJ22 count, the e-eligibility test `eligible_e(counter,d,g,h,a,b,c,support,srem,K)` keeps an `e` only if:

1. it passes the original test; and
2. with `req(e) = max(K, ceil((d+e)/2) - 2g + 2)` and `need = req(e) - support`:
   - either `need <= 0`;
   - or both `srem >= need` and `e - M >= need`, where `M = a + b + c`.

The original test uses the same three quantities, with `qneed = K - support`:

- `support`: the visible support of the ten exceptional prefix coordinates;
- `srem = min(16,d) + component_a + component3`: the hidden-support capacity;
- `e - M`: the hidden mass, since each newly met exceptional curve adds mass at least 1.

The original test requires `qneed <= srem` and `e >= M + qneed`. The composed test replaces `K` by `req(e)`.

- `srem` is an upper bound on the number of hidden exceptional curves with positive intersection.
- It is the N355/N356 special-fibre capacity: 16 + 13 + 9 = 38 hidden exceptional curves.
- So `nu <= support + min(srem, e - M)`.
- Rejecting `support + min(srem, e - M) < req(e)` is therefore exactly the unibranch necessary condition, read with HPADJ's own capacity.

## Result (exact integer arithmetic)

| | count |
|---|---|
| HPADJ22 alone, rows d ≤ 48 | 21,006,100,703,634 |
| **HPADJ22 × UNIBRANCH** | **5,369,214,401** (40 rows) |
| UNIBRANCH-NODE-HURWITZ alone (V50) | 511,353,002,049 |

- Every row is at most the corresponding V50 row, so the per-row MIN against V50 is 5,369,214,401, about V50 / 95.
- Rows with d > 48 are already 0 under V50.
- Boundary rows: g0-d044 = 17 and g1-d048 = 18.

### Count semantics

The counts are **compressed terminals (prefixes)** that survive necessary conditions. They are not Picard classes or curves.

## Checks (`verify_hpadj22_unibranch.py --source-root <checkout of 4bd68ded>`)

1. Every row with d ≤ 48 is recounted with the **unmodified** HPADJ22 direct count. This replay includes the counter's own check against the retained HPADJ08 rejected mass.
2. The modified count is ≤ the unmodified count on every row.
3. The per-row data equal `RESULT.json`. Every nonzero row is ≤ its UNIBRANCH-NODE-HURWITZ row.
4. The totals equal `RESULT.json`, and every credit flag is false.

The run takes about 6 minutes on one core.

## Promotion

Before any MAIN use, three things are required:

1. a hostile audit;
2. a separate MAIN V51 authority sync;
3. owner merge permission.
