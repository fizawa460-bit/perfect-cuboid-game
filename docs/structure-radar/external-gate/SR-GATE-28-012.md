# StructureRadar external-gate closure 28 — SR-STR-012

BATCH_ID=SR-BATCH-EXTERNAL_GATE_CLOSURE-28-R01
PHASE=EXTERNAL_GATE_CLOSURE
STRUCTURE=SR-STR-012
GATE_BEFORE=EXTERNAL_GATE
GATE_AFTER=ACTIVE_PENDING_AUDIT
EXTERNAL_GATE_COUNT_BEFORE=14
EXTERNAL_GATE_COUNT_AFTER=13

## Receiver

The receiver is the Stage14 elliptic fiber

```text
E_t: Y^2 = X(X-1)(X+t^2),
r = X_1/(H_1+S_1),
t = 2r/(1-r^2).
```

The search ledger left one gate: prove a uniform polynomial comparison from the physical cutoff `d<=B` to both the elliptic model/curve height and the point exponential height required by Dujella's bounded-height theorem.

## Gate discharge

This adapter is already proved in the audited Stage14 canonical proof and was therefore a registry reconciliation gap, not a genuinely missing theorem. `stages/stage14/final.md`, Lemma 3.2, proves uniformly over every active face that:

- every nonsingular physical specialization has rational exact 2-torsion `(0,0)`;
- clearing the denominator of `t` produces a Weierstrass model with coefficients given by fixed-degree polynomials in the rational-circle data;
- `d<=B` gives `H_1<B` and the second-face Euclid parameter `v=O(sqrt(B))`;
- the quartic-to-Weierstrass maps have fixed degree, so one absolute `C_0` gives model height and image-point height at most `B^C_0`;
- Dujella over the fixed field `Q`, with torsion order `2`, then yields `exp(O(log B/log log B))=B^o(1)` points uniformly in the active fiber.

The same argument is independently materialized in `stages/stage14/archive/stage14-4ag-kummer-rank-jump.md`, Section 5, and is registered as ACTIVE weapon `AR-005` in `docs/stage14-arsenal.md`.

Thus the exact smallest transfer test recorded by `SR-SEARCH-02.md` is satisfied on the card's own Stage14 receiver. No new external theorem is being inferred and no fixed-curve theorem is extrapolated to a different family.

## Firewalls

- Promotion is only for the exact Stage14 physical integral-space-diagonal fiber and its audited fixed-degree height maps.
- This does not transfer to Stage15 ambient `B2`, a different moving elliptic family, or a different height without a fresh adapter.
- The resulting `B^o(1)` is multiplicity control only, not a fixed-power saving.
- The whole-family physical exponent remains `1/2`; no strict sub-square-root improvement is claimed.
- No perfect-cuboid existence/nonexistence statement is made.

```text
GATE_DISCHARGE=PROVED_FROM_EXISTING_AUDITED_REPO_ADAPTER_PLUS_DUJELLA
SR_STR_012_ARSENAL_DECISION=ACTIVE_PENDING_INDEPENDENT_AUDIT
SEARCH_STATUS=SEARCHED
NOVELTY_BY_SEARCH_ABSENCE=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=StructureRadar-audit
```
