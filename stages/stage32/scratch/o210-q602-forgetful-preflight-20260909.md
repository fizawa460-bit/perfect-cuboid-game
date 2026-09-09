# Stage32 scratch — O210-empty to Q602-empty forgetful preflight

Status: scratch only. No claim-DAG sync, no MAIN authority mutation, no hostile-audit credit, no merge.

## Exact current boundary

Base exact head is PR #1730 repair head `ceeac85cb70b7765380dd31b210f0b38423fa86c`. The post-#1728 active-frontier remap is still awaiting hostile re-audit PASS, so this note must not be consumed as authority yet.

The current Q602 goal `S32.Q602.EXCLUSION.V1` has exact scope `g1-d186 / O=210 / Q=602 / survivors [73,97,235]`. Its statement explicitly permits either residue-specific arithmetic or an equally exact population-preserving obstruction.

## Existing stronger O210 input

PR #1714 already contains hostile-audited MAIN claim `S32.O210.EXCLUSION.V3`, immutable core `7003e228cbb0273e1ac6352bd9535a5f10ca5964bc6d4072130d20012aaec824`, hostile PASS review `5147304889` at exact head `040dfb6c7e1dc40573866bb10f62e93419121711`.

That claim rests on the separately audited EX3 terminal and EX3-to-MAIN population identity adapter V3. Its exact population is `g1-d186 / V6 / O=210 / qprime=4` and is population-wide.

PR #1714 has not been merged into current main, and MAIN routing has not consumed that O210 credit. This scratch preflight therefore treats O210 V3 only as an audited external handoff candidate.

## Forgetful population map

The EX3-09 terminal artifact fixes one hypothetical integral irreducible genus-one V6 carrier with `O=210`, `qprime=4`, `Q=602`, and marked survivors `[73,97,235]`. Its terminal chain derives the Q602 spectrum from the same common-cover correspondence attached to that carrier, and explicitly states that the Q602 survivors are obstruction evidence rather than a population filter.

Therefore every actual configuration counted by the current Q602 admissibility population has an underlying O210 carrier/cover configuration obtained by forgetting the Q602 marking/residue/correspondence arithmetic.

This gives the typed total map

`Q602-admissible configurations -> O210 carrier/cover configurations`.

Consequently, once audited O210 V3 is consumed as current MAIN routing authority,

`O210 population = empty  =>  Q602 admissible population = empty`.

This is a population-emptiness obstruction, not three independent residue-specific contradictions.

## Claim-versioning consequence

Do not mutate `S32.Q602.EXCLUSION.V1` in place. Adding audited O210 dependency plus the forgetful-population semantics changes immutable claim-core fields (`requires` and proof statement). The retained promotion candidate should instead use:

- adapter candidate: `S32.ADAPTER.O210_EMPTY_TO_Q602_ADMISSIBLE_EMPTY.V1`;
- Q602 claim candidate: `S32.Q602.EXCLUSION.V2`.

The historical audited survivor claim `S32.Q602.SURVIVORS_73_97_235.V1` is not revoked. `[73,97,235]` remains the correct audited arithmetic survivor set under the former hypothetical-carrier frontier; the new route would show that no actual admissible carrier exists on which any of those residues can be realized.

## Required order before promotion

1. PR #1730 post-#1728 remap hostile re-audit PASS.
2. MAIN consumes already-audited `S32.O210.EXCLUSION.V3` from PR #1714 into current routing/active frontier.
3. Retain the typed forgetful adapter as a versioned provisional claim with exact source locks.
4. Hostile-audit the adapter / Q602 V2 candidate.
5. Only after PASS + claim sync may MAIN set `Q602_excluded=true` and retire EX3/EX4 Q602 fallback work.

FULL178 and Stage32 closure remain independent and open.
