# Stage32 MAIN scratch — EX1 audited terminal to MAIN V6 scope adapter

Status: scratch only / unaudited / no MAIN promotion.

## Audited input

Stage32EX1 PR #1728 has hostile-audit PASS at exact head

`e3c4a04d5010e6dca9428722e334890e2614297a`

review `5147627146`.

The audit's strongest supported result is

`FULL_TARGET_CLOSURE / ALL_V6_GENUS1_CARRIERS_EXCLUDED`

for the exact Stage32EX1 population.

The corresponding immutable claim core is

`S32.EX1.ALL_V6_GENUS1_CARRIERS_EXCLUDED_CANDIDATE.V2`

with claim-core SHA256

`84e7a4b6990d7c687eebe341fbea296fad1da2cae4785cb87580a0d84572437a`.

The PASS receipt may advance that same EX1 V2 core from PROVISIONAL to AUDITED only through claim-DAG synchronization. This scratch leaf does not perform that registry write and therefore does not treat the EX1 result as consumable MAIN authority yet.

## Exact population comparison

EX1's registered lane target is the decision problem for integral irreducible V6 carriers of geometric genus 1. Its fixed target records:

- Picard class V6;
- integral = true;
- irreducible = true;
- geometric genus = 1;
- V6^2 = 758;
- K.V6 = 186;
- geometric analysis field C.

The current MAIN negative V6 goal

`S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V1`

is also population-wide over:

- row `g1-d186`;
- Picard class V6;
- integral = true;
- irreducible = true;
- geometric genus = 1.

MAIN-STATE independently records the same V6 numerical invariants `V6^2=758` and `K.V6=186`.

Thus the mathematical object predicate attacked by EX1 and the object predicate quantified by the current MAIN negative V6 goal coincide at the current target. EX1 is not merely a finite searched subfamily: the hostile audit accepted its terminal outcome as `ALL_V6_GENUS1_CARRIERS_EXCLUDED` under the lane's full-target closure contract.

This gives the candidate concrete scope adapter

`S32.ADAPTER.EX1_V6_TERMINAL_TO_MAIN_V6_NO_MEMBER.V1`

with bridge

`S32.EX1.V6_CARRIER -> S32.MAIN.V6_CARRIER`.

The adapter is still scratch/unaudited. It must be retained with exact source locks and hostile-audited before MAIN may consume it.

## Claim-version consequence

The existing active-frontier goal `S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V1` cannot simply be relabelled AUDITED from the new EX1 evidence. Its immutable core does not contain the EX1 terminal claim or this concrete scope adapter.

Therefore a retained promotion must create a new versioned MAIN claim, expected to be

`S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V2`,

whose immutable core explicitly depends on the audited EX1 V2 claim and the concrete EX1->MAIN adapter.

After that replacement itself becomes audited and the active frontier is remapped, the old normalization-location branches are no longer needed to decide the current V6 carrier population.

## Downstream consequences are separate adapters

Only after audited MAIN V6 population nonexistence exists may MAIN consider:

1. `V6 empty -> O210 empty`, because the current O210 carrier/cover population is a typed subpopulation of the same V6 carrier population;
2. `V6 empty -> Q602 empty`, as a population-preserving obstruction, not as residue-by-residue arithmetic on 73/97/235.

Both transfers require their own explicit adapters and versioned target claims. This leaf grants neither O210 nor Q602 exclusion.

Stage32 FINAL-CHECK remains not ready. No merge is authorized.
