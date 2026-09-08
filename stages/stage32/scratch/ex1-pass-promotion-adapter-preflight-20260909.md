# Stage32 MAIN scratch — EX1 hostile-PASS promotion adapter preflight

Status: **scratch only / unaudited / no MAIN promotion**.

## New external authority event

PR #1728 received hostile-audit **PASS** at exact head

`e3c4a04d5010e6dca9428722e334890e2614297a`

review `5147627146`.

The audit's strongest supported EX1 result is

`FULL_TARGET_CLOSURE / ALL_V6_GENUS1_CARRIERS_EXCLUDED`

for the exact Stage32EX1 population. The audit also explicitly states that this PASS does not automatically mutate the claim registry or promote EX1 to MAIN. At the audited head the V2 claim core remains `PROVISIONAL`, so the PASS first triggers `AUTHORITY_OR_AUDIT_TRANSITION` synchronization under `CLAIM-SYNC-CONTRACT.md`.

## Promotion must be decomposed into typed adapters

The generic `S32.ADAPTER.EX_TO_MAIN_PROMOTION_BOUNDARY.V2` is only a management boundary. It expressly says it is not a concrete scope equivalence. Therefore the hostile PASS cannot be copied into MAIN by narrative.

The smallest concrete chain is three separate adapters.

### A. EX1 terminal population -> MAIN V6 population

Candidate ID:

`S32.ADAPTER.EX1_V6_TERMINAL_TO_MAIN_V6_NO_MEMBER.V1`

Bridge:

`S32.EX1.V6_CARRIER -> S32.MAIN.V6_CARRIER`

The exact semantic obligation is to prove that EX1's terminal population is the same complete current `g1-d186`, `V6`, integral irreducible geometric-genus-1 carrier population quantified by `S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V1`. Only after this adapter is retained and itself becomes consumable audited authority can the MAIN negative-V6 goal be promoted.

### B. MAIN V6 empty -> O210 empty

Candidate ID:

`S32.ADAPTER.MAIN_V6_EMPTY_TO_O210_EMPTY.V1`

Bridge:

`S32.MAIN.V6_CARRIER -> S32.O210.COVER`

The current O210 goal is explicitly scoped to the same row and Picard class V6. The adapter must certify that its O210 carrier/cover population is a subpopulation of the current V6 carrier population. Then V6 population nonexistence gives O210 exclusion by a population-preserving argument.

This is not an EX3 monodromy proof and must not be described as one.

### C. MAIN V6 empty -> Q602 empty

Candidate ID:

`S32.ADAPTER.MAIN_V6_EMPTY_TO_Q602_EMPTY.V1`

Bridge:

`S32.MAIN.V6_CARRIER -> S32.Q602.ARITHMETIC`

`S32.Q602.EXCLUSION.V1` already permits either residue-specific arithmetic **or an equally exact population-preserving obstruction**. If the exact current V6 carrier population is empty, none of `[73,97,235]` survives as an admissible Q602 component. This would be a vacuous/population obstruction, not an arithmetic proof that 73, 97 and 235 individually fail the old residue predicate.

Consequently the same-member local-to-Q602 identity becomes unnecessary only after the negative V6 claim and the empty-population adapter are themselves consumable.

## Authority gate

At this scratch checkpoint:

- hostile PASS exists;
- the exact V2 claim core is known;
- claim-DAG synchronization of the PASS receipt is still required before EX1 audited authority is consumable;
- none of the three concrete adapters is registered or hostile-audited;
- MAIN V6, O210 and Q602 remain unpromoted;
- Stage32 FINAL-CHECK remains not ready.

This leaf therefore prepares the exact adapter decomposition but grants no mathematical credit.
