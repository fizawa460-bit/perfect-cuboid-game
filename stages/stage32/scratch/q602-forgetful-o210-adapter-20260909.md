# Stage32 MAIN scratch — Q602 → O210 forgetful population adapter

Status: **SCRATCH / exact / unaudited / no MAIN authority**.

## Point

The current Q602 frontier is not a population independent of O210. Its registered scope is
`row=g1-d186, O=210, Q=602`, with audited survivor residues `[73,97,235]`.
The retained post1623 artifact has the same fixed target, including `q'=4`.

The already-audited O210 V3 package is population-wide on
`g1-d186 / V6 / O=210 / q'=4`. Its retained derivation explicitly treats the
Q602 survivor orbit as obstruction evidence, not as a carrier-population filter.

Therefore the relevant map is a forgetful map:

`Q602-admissible decorated configuration -> underlying O210 carrier/cover`

obtained by forgetting the Q602 residue / retained W-line arithmetic decoration
and changing none of row, V6 class, O, q', or the underlying carrier/cover object.

This supports only the implication

`O210 population empty -> current O210-bound Q602 admissible population empty`.

It does not reverse the implication and does not apply to a differently scoped
Q602 problem.

## Claim versioning

Do **not** mutate `S32.Q602.EXCLUSION.V1`. Adding audited O210 V3 plus a new
cross-scope adapter changes immutable `requires` / proof semantics.

Scratch proposed IDs:

- `S32.ADAPTER.O210_TO_Q602_FORGETFUL.V1`
- `S32.Q602.EXCLUSION.V2`

The exact proposed immutable cores are stored in the adjacent JSON artifact.

## Promotion order

1. First consume O210 V3 into MAIN after the pending hostile pre-sync audit PASS.
2. Retain and hostile-audit the forgetful adapter.
3. Register Q602 V2 as a new authority-neutral claim core.
4. Hostile-audit Q602 V2.
5. Only then set `Q602_excluded=true`.

No O212+, FULL178, Stage32, endpoint, or Perfect Cuboid credit follows from this
scratch result.
