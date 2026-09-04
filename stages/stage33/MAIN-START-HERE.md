# Stage33 MAIN startup

Ordinary `Stage33-main-batch` reads `AGENTS.md`, then `stages/stage33/MAIN-STATE.json`, then only the files in `current_leaf_working_set`.

## Stage33 repository-read discipline

For ordinary research/navigation use:

`controller -> active roadmap -> Arsenal index/card -> exact referenced files`

The current branch-local roadmap is `stages/stage33/ROADMAP-33-12-V71-J1-TORSOR.md`. Older roadmaps remain historical planning checkpoints.

Use known paths directly. Repository discovery is search-first. A search miss never proves repository absence or mathematical nonexistence.

**Stage33 MAIN hard ban:** do not request, fetch, or dump a full/recursive repository tree, including GitHub recursive `git/trees` reads or equivalent whole-branch tree enumeration. Navigate only by exact-path fetches, targeted filename/code searches, and explicit controller/roadmap/Arsenal/source-lock references.

V58 remains the operational routing authority: Arsenal first, then repeatable bounded search only when each repeat has a materially new mathematical signal. Unbounded/open-ended search remains forbidden.

## Current exact frontier: V80

- V61-V64 fix the B1 source basis, literal `lambda_A={f_A,g22}`, `kappa_A=J1`, `kappa_D=J2`, and retained J2 geometry.
- V71 constructs the nonzero J1 `H^1(E[2])` cocycle; V73 materializes the direct semilinear quartic torsor.
- V77 wires in the exact x-alpha relation. J1 is zero in the geometric Brauer/Ogg-Shafarevich quotient, so the historical V65/V69 nonzero marked-Kc discriminator is not an active J1 decision gate.
- V79 closes the full B1 Gysin matrix in ordered basis `[cc(kappa_A),cc(kappa_D),kappa_A,kappa_D]` with column masks `[0,25,0,25]`, rank `1`, image `{0,25}`.
- The e3 target is proper14 mask `20`, so `20 notin {0,25}`. Therefore the B1 branch-Gysin route is **exactly frozen for e3**.
- This is only a route-local negative result. It does **not** prove global nonexistence of an e3 `H2(mu2)` lift.
- V80 promotes that boundary and returns CURRENT to the pre-existing V52/V56 source-specific marked-Picard-to-literal-geometry gap outside the frozen B1 route.

The inherited `controller.json` remains the global/firewall authority. No global credit is changed.

## Current leaf

`STOP` means **leaf gate only, not algorithm exhaustion**. `Stage33-main-batch` remains allowed.

CURRENT:

`SOURCE_SPECIFIC_FULL_SURFACE_CECH_H2_MU2_REALIZATION_FOR_E3_MASK20_OUTSIDE_B1_ROUTE`

Exact input already available:

- V41 e3 proper14 mask `20`;
- V53 exact marked Picard-adjoint candidate for mask20;
- V56 exact localization of the missing bridge;
- V79 exact proof that the B1 route image is only `{0,25}` and therefore cannot realize mask20.

Required next object: one source-locked literal Cech/function/divisor/transition datum, or actual Gersten datum with all adapter hypotheses checked, whose exact marked Brauer image is proper14 mask20. The retained J2 `{f2,g22}` object is a method/example only and must not be relabelled as e3.

Do not reopen B1 membership after V79, and do not promote B1 nonmembership to global `H2(mu2)` nonexistence.

## Arsenal-first routing

Read `docs/arsenal/index.json`, then only:

- `S33-PW04` for exact marked-source / Picard-adjoint binding;
- `S33-PW07` for literal Cech/torsor/Brauer-layer construction patterns;
- `S33-PW08` only conditionally if actual Gersten data are constructed and its hypotheses can be checked exactly.

Cards are PROVISIONAL routing aids; live Stage33 source locks override them.

## Historical correction retained

V77 remains exact: J1 is zero in the geometric Brauer/Ogg-Shafarevich quotient. The V71 E[2] cocycle and V73 quartic remain valid historical objects; only the old nonzero-Brauer interpretation was superseded.

Do not reopen the 4/12 minimum-norm discriminator and do not choose identity versus shear from that historical gate.

## Release and verification

Stage33 remains `6/11`. Stage33-12 is not closed. Stage33-13 is not released. No receiver, endpoint, theorem, existence/nonexistence, or merge credit is granted.

After writes run at minimum:

- `python stages/stage33/33-12/verify_e3_b1_full_gysin_matrix_xalpha_correction_v79.py`
- `python stages/stage33/33-12/verify_e3_b1_route_freeze_and_outside_cech_rewire_v80.py`
- `python stages/stage33/sync_main_state.py --check`
- `git diff --check`

Commit and push the same branch. Do not merge without explicit authorization.
