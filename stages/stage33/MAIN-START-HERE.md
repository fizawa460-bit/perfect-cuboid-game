# Stage33 MAIN startup

Ordinary `Stage33-main-batch` reads `AGENTS.md`, then `stages/stage33/MAIN-STATE.json`, then only the files in `current_leaf_working_set`.

## Stage33 repository-read discipline

For ordinary research/navigation use:

`controller -> active roadmap -> Arsenal index/card -> exact referenced files`

The current branch-local roadmap is `stages/stage33/ROADMAP-33-12-V71-J1-TORSOR.md`. Older roadmaps remain historical planning checkpoints.

Use known paths directly. Repository discovery is search-first. A search miss never proves repository absence or mathematical nonexistence.

**Stage33 MAIN hard ban:** do not request, fetch, or dump a full/recursive repository tree, including GitHub recursive `git/trees` reads or equivalent whole-branch tree enumeration. Navigate only by exact-path fetches, targeted filename/code searches, and explicit controller/roadmap/Arsenal/source-lock references.

V58 remains the operational routing authority: Arsenal first, then repeatable bounded search only when each repeat has a materially new mathematical signal. Unbounded/open-ended search remains forbidden.

## Current exact frontier: V85

- V61-V64 fix the B1 source basis, literal `lambda_A={f_A,g22}`, `kappa_A=J1`, `kappa_D=J2`, and retained J2 geometry.
- V71/V73 retain the literal J1 E[2] cocycle and semilinear quartic; V77 proves J1 is zero in the geometric Brauer/Ogg-Shafarevich quotient.
- V79 closes the full B1 Gysin matrix with masks `[0,25,0,25]`, rank `1`, image `{0,25}`; e3 proper14 mask `20` is not in that image.
- V84 descends the exact coordinate automorphism generators (`swap12`, `swap13`, seven coordinate signs) to proper14 and computes the orbit of mask25.
- V85 certifies `orbit(mask25)={25}` under all nine generators. Hence the coordinate-conjugate B1/B2/B3 sign-quotient Gysin family has image `{0,25}` and **cannot realize mask20**.
- V85 freezes exactly that coordinate-conjugate route family. It does **not** prove global nonexistence of an e3 `H2(mu2)` lift; arbitrary full-surface Cech/Gersten representatives remain open.

The inherited `controller.json` remains the global/firewall authority. No global credit is changed.

## Current leaf

`STOP` means **leaf gate only, not algorithm exhaustion**. `Stage33-main-batch` remains allowed.

CURRENT:

`NON_COORDINATE_CONJUGATE_FULL_SURFACE_CECH_OR_ACTUAL_GERSTEN_DATUM_WITH_EXACT_PROPER14_BRAUER_IMAGE_MASK20`

Required next object:

`CONSTRUCT_NON_COORDINATE_CONJUGATE_FULL_SURFACE_CECH_OR_ACTUAL_GERSTEN_DATUM_WITH_EXACT_PROPER14_BRAUER_IMAGE_MASK20`

Acceptance requires one independently source-locked full-surface object outside the frozen coordinate-conjugate sign-quotient family:

- literal Cech/function/divisor/transition data, or actual Gersten height-one support/residue data;
- exact marked Brauer image equal to proper14 mask20;
- source binding to the V41 e3 class;
- all residue/resolution/adapter hypotheses required by the selected route.

The retained J2 `{f2,g22}` object is a method/example only and must not be relabelled as e3.

Do not reopen B1/B2/B3 coordinate-conjugate Gysin membership after V85, and do not promote this route-family failure to global `H2(mu2)` nonexistence.

## Arsenal-first routing

Read `docs/arsenal/index.json`, then only:

- `S33-PW04` for exact marked-source / Picard-adjoint binding;
- `S33-PW07` for literal Cech/torsor/Brauer-layer construction patterns;
- `S33-PW08` conditionally for an actual Gersten construction, with height-one valuation attachment and residue hypotheses checked exactly.

Cards are PROVISIONAL routing aids; live Stage33 source locks override them.

## Historical correction retained

V77 remains exact: J1 is zero in the geometric Brauer/Ogg-Shafarevich quotient. The V71 E[2] cocycle and V73 quartic remain valid historical objects; only the old nonzero-Brauer interpretation was superseded.

Do not reopen the historical 4/12 minimum-norm discriminator and do not choose identity versus shear from that gate.

## Release and verification

Stage33 remains `6/11`. Stage33-12 is not closed. Stage33-13 is not released. No receiver, endpoint, theorem, existence/nonexistence, or merge credit is granted.

After writes run at minimum:

- `python stages/stage33/33-12/verify_e3_coordinate_conjugate_sign_quotient_route_freeze_v85.py`
- `python stages/stage33/33-12/verify_stage33_v85_frontier_state_v86.py`
- `python stages/stage33/sync_main_state.py --check`
- `git diff --check`

Commit and push the same branch. Do not merge without explicit authorization.
