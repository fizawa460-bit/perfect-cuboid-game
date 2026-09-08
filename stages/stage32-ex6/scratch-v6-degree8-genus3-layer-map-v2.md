# Stage32EX6 scratch — V6 degree-8 genus-3 layer map V2

Status: `SCRATCH_SUPERSEDES_48_ONLY_LAYER_MAP_96_SINGULAR_CLOSED_240_SMOOTH_OPEN`.

Scratch only. This note does not update `MAIN-STATE`, exclude O266, authorize O264 descent, create hostile-audit credit, advance Stage32 MAIN, or merge anything.

## 1. Superseded statement

This note supersedes only the live interpretation of `scratch-v6-degree8-genus3-nef-reentry-adapter-wall.md` that treated `C4s (32) + C5s (16) = 48` as the next explicit degree-8 genus-3 layer. That 48-count is a genuine explicit subset in the pinned Testa--Stoll verification source, but it is not the full explicit degree-8 genus-3 inventory relevant to the next D1 sign scan.

## 2. Current D1 input

For the current V6 class `C`, let

`D1 = C - K - (R17+R21+R24+R25+R26+R28+R30+R31)`.

The previous exact scratch replay proved `D1 >= 0` on the source-locked classical 140 curves only. Global nefness was and remains unproved.

## 3. Degree-8 genus-3 inventory from the source

The Testa--Stoll manuscript/source distinguishes at least the following explicit degree-8 genus-3 families on the cuboid resolution:

1. **96 singular hyperelliptic fibers** from the last four rank-4 quadrics: eight resolved fibrations, each with twelve hyperelliptic genus-3 fibers having two nodes at surface singularities. The source states that these 96 form one `Aut(Sbar)` orbit.
2. **32 smooth hyperelliptic curves** in the octahedral family. The verification source's `C4s` gives these 32 explicit curves.
3. **192 further smooth hyperelliptic curves**, obtained from rational quartics on the coordinate K3 quotient and the analogous coordinate quotients.
4. **16 smooth nonhyperelliptic genus-3 curves**, the Fermat-quartic family. The verification source's `C5s` gives these 16 explicit curves.

Thus after the singular 96 family, the currently source-visible smooth explicit layer is at least

`32 + 192 + 16 = 240` curves.

The old `C4s + C5s = 48` statement therefore omitted the 192 smooth K3-pullback family.

This is an explicit-source inventory, not a theorem that every degree-8 negative curve on the surface occurs in these families.

## 4. Singular 96 family is now closed against D1 negativity

The tracked scratch decision is

`stages/stage32-ex6/scratch-v6-degree8-hyperelliptic-superset-decision.json`.

The exact reconstruction scans the necessary-condition lattice superset

`R = F_fib - E_p - E_q`

for each of the eight last-four rank-4 fibrations. The actual 96 two-node fibers are contained in this superset. The scan produced:

- 8 fibration classes;
- 156 candidate pairs per class;
- 1248 candidate numerical classes total;
- `negative_D1_candidate_total = 0`;
- `zero_D1_candidate_total = 0`;
- global candidate range `29 <= D1.R <= 97`.

Therefore every actual member of the source's 96-fiber orbit has `D1.R > 0`. Exact identification of the twelve geometric node pairs in each fibration is unnecessary for this sign conclusion because the whole necessary-condition superset is strictly positive.

Green replay:

- workflow `Stage32 EX6 scratch degree8 hyperelliptic reconstruction`;
- run `34286760507`;
- job `102264021521`;
- scratch source head before this note `e54706cc1b62bb0d2a953aec9e4e841e89996756`.

Firewalls: this closes only the singular two-node degree-8 hyperelliptic family against D1 negativity. It does not prove global nefness, O266 exclusion, O264 descent, or Stage32 MAIN progress.

## 5. Existing Kc adapter assets discovered

The old wall's wording `NEW_MAGMA_OR_EQUIVALENT_EXACT_PICARD_COMPUTATION_REQUIRED = true` is also too strong as a discovery statement.

Existing Stage33-07 assets already include:

- `extract_kc_picard_lattice.py`;
- `extract_kc_picard_maps.py`;
- `indlist-to-magma-picard-basis.json`;
- `marked-picard-basis-bridge-certified.json`;
- retained Kc lattice/discriminant material.

`extract_kc_picard_maps.py` is an exact pinned-source producer for

- `pmPicK` (20x20),
- `MatKtoS` (20x64),
- `MatStoK` (64x20),
- the Smith right transform.

A historical successful Stage33-07 run exists:

- run `32790534938` (`Stage33-07 BR2A integration regression`), head `4be96346dd2353ae9ef7d86a7451487cf229f2a6`;
- artifact `9542962724`, digest `sha256:22e9359dbf11340253c14de074d1f154111ec003c56c929a9fafddf4657844b8`;
- that artifact is now expired.

Separately, Stage32 already retained exact pinned Kc/sigma-c replay machinery for the same V6 witness, including commits

- `5af6d5c1aad8ce4f2b7a455e9aea3c210c1a5913` — materialize exact Kc Picard action from pinned source;
- `80202993b3a30622f7a6a9f55e8faf04ab900147` — add pinned Kc Picard replay V6;
- `cada3932d0b2683620bf861591127a622a701b6e` — retain exact Kc replay nonexclusion result.

The retained V6 Kc replay has source-locked full integral Picard64/sigma-c and exceptional-ordering infrastructure. It does not itself retain the full 20x64/64x20 Kc map certificate needed to transport the 192 quartic classes.

Therefore the precise current wall is:

`KC_MAP_PRODUCER_AND_S_TO_K_INFRASTRUCTURE_EXIST_BUT_FULL_KC_MAP_CERTIFICATE_NOT_TRACKED_AND_HISTORICAL_ARTIFACT_EXPIRED`.

A fresh heavy Magma run has not been authorized or started in this EX6 batch.

## 6. Next bounded leaf

Priority order:

1. Recover a non-expired or otherwise retained exact `MatKtoS/MatStoK` certificate if one exists elsewhere in repository history/evidence storage.
2. If recovered, source-lock a representative rational quartic class in `Pic(K_c)`, transport/pull it to `Pic(S)`, generate the source-declared orbit(s), and compute `D1.G` on the 192 smooth K3-pullback curves.
3. Independently adapt the explicit `C4s` 32 and `C5s` 16 seeds to the retained Picard64 basis and orbit-replay their D1 intersections.
4. If any `D1.G < 0`, peel the forced component(s) and replay. If all explicit degree-8 families are nonnegative, retain only explicit-degree8-layer nonnegativity; do not call D1 globally nef without a theorem covering all remaining negative curves.

## 7. Decision ledger

- `D1_CLASSICAL140_ALL_NONNEGATIVE = true`;
- `DEGREE8_SINGULAR_HYPERELLIPTIC_ORBIT_SIZE = 96`;
- `DEGREE8_SINGULAR_HYPERELLIPTIC_D1_STRICTLY_POSITIVE = true`;
- `DEGREE8_SINGULAR_HYPERELLIPTIC_SUPERSET_MIN_D1 = 29`;
- `DEGREE8_SMOOTH_EXPLICIT_SOURCE_VISIBLE_COUNT_AT_LEAST = 240`;
- `DEGREE8_SMOOTH_C4_COUNT = 32`;
- `DEGREE8_SMOOTH_K3_PULLBACK_COUNT = 192`;
- `DEGREE8_SMOOTH_C5_COUNT = 16`;
- `OLD_48_ONLY_LAYER_MAP_SUPERSEDED = true`;
- `KC_EXACT_MAP_PRODUCER_EXISTS = true`;
- `KC_FULL_MAP_CERTIFICATE_TRACKED_IN_CURRENT_INSPECTED_TREE = false`;
- `KC_HISTORICAL_MAP_ARTIFACT_EXPIRED = true`;
- `FRESH_HEAVY_MAGMA_STARTED = false`;
- `D1_GLOBAL_NEF = UNPROVEN`;
- `O266_ENDPOINT_EXCLUDED = false`;
- `O264_DESCENT_AUTHORIZED = false`;
- `STAGE32_MAIN_ADVANCED = false`.
