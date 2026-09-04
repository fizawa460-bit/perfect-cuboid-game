# Stage33 MAIN startup

Ordinary `Stage33-main-batch` reads `AGENTS.md`, then `stages/stage33/MAIN-STATE.json`, then only the files in `current_leaf_working_set`.

## Stage33 repository-read discipline

For ordinary research/navigation use:

`controller -> active roadmap -> Arsenal index/card -> exact referenced files`

The current branch-local roadmap is `stages/stage33/ROADMAP-33-12-V71-J1-TORSOR.md`. Older roadmaps remain historical planning checkpoints.

Use known paths directly. Repository discovery is search-first. A search miss never proves repository absence or mathematical nonexistence.

**Stage33 MAIN hard ban:** do not request, fetch, or dump a full/recursive repository tree, including GitHub recursive `git/trees` reads or equivalent whole-branch tree enumeration. Do not use a recursive tree as a convenience fallback after a search miss. Navigate only by exact-path fetches, targeted filename/code searches, and explicit controller/roadmap/Arsenal/source-lock references. If a future leaf genuinely requires exhaustive repository enumeration, that requirement must first be made explicit in the Stage33 roadmap/controller; it is not implicitly authorized by `Stage33-main-batch`.

Do not use branch-history archaeology as ordinary discovery.

## Current exact frontier: V71

- V61-V64 fix the B1 source basis, literal `lambda_A`, named `J1/J2`, and `J2 -> u1=[1,0]`.
- V65 reduces J1 to `u2=[0,1]` versus `u1+u2=[1,1]`; the target fingerprints are minimum norm `4` versus `12`.
- V67 shows the #1529 U/S-to-Stoll-word adapter does not supply the missing J1 transport/equivariance datum.
- V68-V69 reduce the remaining transport to exactly identity versus the unique shear fixing `u1`; one bit remains. V70 replays this reduction immutably.
- V71 constructs the J1-specific Creutz--Viray E[2] cocycle from the retained `(f1,1)` representative: splitting field `Kgeom(sqrt(f1))`, fixed translation value `rho_f1 -> Tr`. This is not a relabelled J2 class or kernel.

The inherited `controller.json` remains the global/firewall authority. Its pre-V61 current-leaf fields are not the branch frontier; `MAIN-STATE.json` records this branch-local current-leaf supersession. No global credit is changed.

## Current leaf

`STOP` means **leaf gate only, not algorithm exhaustion**. `Stage33-main-batch` remains allowed.

The next constructive leaf is D2.1: materialize the J1 translation torsor from the V71 cocycle with `d=f1`, using `S33-PW07` as the method route. Then D2.2 computes the J1-specific twisted-kernel minimum norm. Only `4` or `12` can close the remaining bit; `4` selects `u2`, `12` selects `u1+u2`.

Historical contact/Weil pairing data have already been reevaluated at the V69 one-bit frontier and do not distinguish identity from shear. Do not reopen them without materially new target-side data.

## Arsenal-first routing

Read `docs/arsenal/index.json`, then only:
- `S33-PW07` for the active cocycle -> translation torsor -> integral/twisted-kernel construction;
- `S33-PW04` for exact marked-source transport/firewall once an independent fingerprint is available.

Cards are PROVISIONAL routing aids; live Stage33 source locks override them. V58 permits repeatable bounded search only when each repeat has a materially new mathematical signal. Unbounded/open-ended search remains forbidden.

## Release and verification

Stage33 remains `6/11`. Stage33-12 is not closed. Stage33-13 is not released. No receiver, endpoint, theorem, existence/nonexistence, or merge credit is granted.

After writes run at minimum:

- `python stages/stage33/33-12/verify_e3_b1_j1_marked_kc_discriminator_gate_v65.py`
- `python stages/stage33/33-12/verify_e3_b1_j1_post1529_equivariance_scope_gate_v67.py`
- `python stages/stage33/33-12/verify_e3_b1_c22_j1_transport_gates_v70.py`
- `python stages/stage33/33-12/verify_e3_b1_c22_j1_cv_e2_cocycle_v71.py`
- `python stages/stage33/33-12/verify_stage33_v71_frontier_state_v72.py`
- `python stages/stage33/sync_main_state.py --check`
- `git diff --check`

Commit and push the same branch. Do not merge without explicit authorization.
