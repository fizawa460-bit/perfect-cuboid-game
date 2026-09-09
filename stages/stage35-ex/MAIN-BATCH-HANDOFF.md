# Stage35-EX MAIN batch handoff — Goal4BT source-known bridge reservoir reopen

Mathematical authority remains **V74 / Goal4AK** (hostile review `5142248509`). Goal4BS remains the independently audited intermediate checkpoint (review `5151846948`, audited head `d6f5151c9d95304afe7081c92f40f1d25cc4aa3b`). No E1, Stage35, endpoint, or Perfect Cuboid credit is promoted.

Audited checkpoint receipt:

- review: `5151846948`
- audited exact head: `d6f5151c9d95304afe7081c92f40f1d25cc4aa3b`

Retained Goal4BS receipt markers (historical checkpoint state, not the post-BT current route):

```text
PARKING_AUDIT_COMPLETE=true
ROUTE_STATUS=PARKED_AUDITED_REOPEN_GATED
GLOBAL_RATIONAL_REALIZATION_WITH_HEIGHT_CONTROL
NEW_SOURCE_FIXED_E1_INVARIANT
QUANTITATIVE_HEIGHT_DISCRIMINANT_ADAPTER
```

## Reopen from audited parking

Goal4BS had

```text
ROUTE_STATUS=PARKED_AUDITED_REOPEN_GATED
```

with reopen gate B:

```text
NEW_SOURCE_FIXED_E1_INVARIANT
```

Goal4BT identifies such an invariant by correcting the historical classification of the bridge reservoir.

For every Master-Hit,

```text
M=(V1*U2)^2+(U1*V2)^2=S^2,
h=c*q,
H=S/(c*q),
e=gcd(c,H).
```

`H` is the primitive Master hypotenuse and is source-computable before any E1-failure assumption. Hence `e` is source-computable too.

Historical 35EX-10 treated `e` as not source-known. Its branch-specific bridge residue conditions therefore upgrade to source-only E1 kill predicates:

```text
Branch L: odd ell|e requires (p*q/ell)=+1.
Branch R: odd ell|e requires (2*p*q/ell)=+1.
```

This channel is nonredundant with the old cross/T split-prime channels. Regression witnesses are retained in the Goal4BT artifact for both 2-adic branches.

## Current provisional leaf

```text
unit=35EX-35_GOAL4BT_MASTER_HYPOTENUSE_BRIDGE_RESERVOIR_SOURCE_RECLASSIFICATION
status=PROVISIONAL_EXACT_REOPEN_GATE_B_SOURCE_KNOWN_BRIDGE_SIEVE_NO_E1_CREDIT
REOPEN_GATE_B_TRIGGERED=true
NEW_SOURCE_FIXED_E1_INVARIANT=SOURCE_KNOWN_BRIDGE_RESERVOIR_RESIDUE_PROFILE
```

Files:

- `stages/stage35-ex/35ex-35/goal4bt-master-hypotenuse-bridge-reservoir-source-reclassification-source-lock.md`
- `stages/stage35-ex/35ex-35/goal4bt-master-hypotenuse-bridge-reservoir-source-reclassification.json`
- `stages/stage35-ex/verify_stage35_ex_35_goal4bt_bridge_reservoir_source_reclassification.py`
- `.github/workflows/stage35-ex-goal4bt-bridge-reservoir-source-reclassification.yml`

MAIN-STATE is intentionally unchanged at V74 / Goal4AK. Goal4BT has no hostile-audit or promotion credit.

## Next leaf

```text
35EX-35_GOAL4BU_THREE_SOURCE_RESERVOIR_RECIPROCITY_COUPLING_PREFLIGHT
```

Question: after correcting `e` to source-known, can the pairwise-coprime source-known triple

```text
cross reservoir, T, e
```

be coupled by a global Jacobi/reciprocity relation or universal bad-prime condition beyond the separate 35EX-10/11 primewise predicates?

Do not recharge the already-tested Gaussian/ray/Brauer/height routes unless Goal4BU exposes a genuinely new adapter.

No merge.
