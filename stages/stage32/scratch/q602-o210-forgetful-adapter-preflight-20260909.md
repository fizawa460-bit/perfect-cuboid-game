# Stage32 scratch: Q602 -> O210 forgetful adapter preflight

Status: **SCRATCH / exact-source-bound / unaudited / no authority change**.

## The type issue

The retained values `73,97,235` are formal mod-2 `End(J(C0))` residue labels. They are not themselves geometric carriers. Therefore audited O210 emptiness should **not** be recorded as “the labels 73,97,235 do not exist algebraically”.

The relevant Q602 object is instead an **actual geometric Q602 realization**: a fixed-target O210 carrier/cover together with the common-cover correspondence `T=(f1)_*(f2)^*` and a residue decoration satisfying the retained Q602 predicates.

This distinction is necessary to consume O210 emptiness without falsifying the already-audited survivor statement.

## Source-locked construction

1. `post1484-o210-q4-common-double-cover-cartesian-identity.json` starts with a hypothetical integral carrier `N` and constructs the same `Y` as the normalization of the Beauville/common hyperelliptic pullback through either factor.
2. `post1490-o210-q4-bolza-correspondence-rosati-frontier.json` fixes the O210 correspondence on that `Y` and defines `T=(f1)_*(f2)^*`, with degrees `105` and `81`.
3. `post1505-o210-q4-x8-v4-torsor-plane-retained-f2-4-adapter.json` applies the Q602 pointwise residue predicate to `T` and reduces the retained residue set `28 -> 16`.
4. `post1505-o210-q602-weierstrass-parity-transvection-refinement.json` and its source note derive the actual-correspondence parity/transvection predicate and reduce `16 -> [73,97,235]`.

Thus the Q602 realization data do not define a second independent carrier population. They decorate an underlying member of the exact O210 carrier/cover population.

## Candidate adapter

`S32.ADAPTER.Q602_ADMISSIBLE_TO_O210_POPULATION.V1`

Bridge:

`S32.Q602.ADMISSIBLE_CONFIGURATION -> S32.O210.COVER`

by forgetting `T` / residue / marking decoration and retaining the underlying fixed-target O210 carrier/cover.

The map only needs to be total on actual Q602 realizations. It need not be injective or surjective.

Therefore

`O210 population = empty  =>  Q602 geometric realization population = empty`.

This implication does **not** alter the formal residue-label statement `[73,97,235]`.

## Downstream claim versioning

The population-preserving route must use a new claim core,

`S32.Q602.EXCLUSION.V2`,

with dependencies on:

- `S32.MAIN.CURRENT_TARGET_CONTEXT.V1`
- `S32.Q602.SURVIVORS_73_97_235.V1`
- `S32.O210.EXCLUSION.V3`
- `S32.ADAPTER.Q602_ADMISSIBLE_TO_O210_POPULATION.V1`

Do **not** mutate `S32.Q602.EXCLUSION.V1`: its immutable core does not contain the O210 V3 + forgetful-adapter evidence route.

## Credit firewall

This scratch preflight grants no Q602 exclusion now. Before consumption it still requires:

1. post-sync O210 transition hostile re-audit PASS;
2. retained/versioned adapter package;
3. hostile audit of the typed adapter;
4. separate versioned Q602 V2 claim package and hostile audit;
5. claim-DAG synchronization / active-frontier remap only after PASS.

No O212+, FULL178, Stage32 closure, endpoint, Perfect Cuboid, or merge credit is granted here.

Canonical scratch artifact: `bfd17b6b41e32ab9ce729c2fb735477beb3e70061576433a16d1d0ad30edce69`.
