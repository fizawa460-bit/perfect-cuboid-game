# Stage33 MAIN startup

Ordinary `Stage33-main-batch` reads `AGENTS.md`, then `stages/stage33/MAIN-STATE.json`, then only the files in `current_leaf_working_set`.

## Stage33 repository-read discipline

For ordinary research/navigation use:

`controller -> active roadmap -> Arsenal index/card -> exact referenced files`

The current branch-local roadmap is `stages/stage33/ROADMAP-33-12-V71-J1-TORSOR.md`. Older roadmaps remain historical planning checkpoints.

Use known paths directly. Repository discovery is search-first. A search miss never proves repository absence or mathematical nonexistence.

**Stage33 MAIN hard ban:** do not request, fetch, or dump a full/recursive repository tree, including GitHub recursive `git/trees` reads or equivalent whole-branch tree enumeration. Do not use a recursive tree as a convenience fallback after a search miss. Navigate only by exact-path fetches, targeted filename/code searches, and explicit controller/roadmap/Arsenal/source-lock references. If a future leaf genuinely requires exhaustive repository enumeration, that requirement must first be made explicit in the Stage33 roadmap/controller; it is not implicitly authorized by `Stage33-main-batch`.

Do not use branch-history archaeology as ordinary discovery.

## Current exact frontier: V77

- V61-V64 fix the B1 source basis, literal `lambda_A={f_A,g22}`, `kappa_A=J1`, `kappa_D=J2`, and retained J2 marked/proper14 data.
- V65/V68/V69 historically treated J1 as one of two nonzero marked-Kc candidates and reduced that conditional transport to identity versus shear.
- V71 constructs the exact nonzero J1 E[2]-valued cocycle `(f1,1)`, splitting over `Kgeom(sqrt(f1))`, with `rho_f1 -> Tr`.
- V73 materializes the direct semilinear quartic torsor from that E[2] cocycle.
- V75 proves the degree-two quotient is independent of `d`.
- V77 wires in the exact historical `xalpha_pair_galois_repair.py`: `J1` is itself an x-alpha relation, and the geometric Brauer quotient has basis `{J2,q1}`. Therefore source J1 is **zero in the geometric Brauer/Ogg-Shafarevich quotient**.
- Thus V71 remains nonzero in `H^1(E[2])`, but its image in `H^1(E)` is zero. The V73 smooth projective torsor is the zero OS class with `T=<4>+<8>`, minimum norm `4`. This `4` is **not** the nonzero `u2` fingerprint.
- The old V65/V69 J1 nonzero marked-Kc gate and V75 4-vs-12 next contract are superseded for J1. J2 -> `u1=[1,0]` remains intact.

The inherited `controller.json` remains the global/firewall authority. Its pre-V61 current-leaf fields are not the branch frontier; `MAIN-STATE.json` records this branch-local supersession. No global credit is changed.

## Current leaf

`STOP` means **leaf gate only, not algorithm exhaustion**. `Stage33-main-batch` remains allowed.

The active repair leaf is now the literal `lambda_A` -> proper14 column-3 binding. V63 already materializes the source-specific H2(mu2) symbol

`lambda_A=alpha({f_A,g22}),  f_A=(t-r1)/(t-r4)`.

V57 defines `Phi_B1:H1(C21_tilde disjoint_union C22_tilde,F2)->Br(Kc_tilde_bar)[2]`. The next atomic check is whether V63 `Phi_B1(kappa_A)` is exactly the same geometric Brauer quotient class called `J1` in the locked x-alpha repair. If that exact same-codomain/source crosswalk holds, column3 is the zero proper14 vector. If not, stop at the missing adapter; name equality alone is insufficient.

Do not reopen the 4/12 minimum-norm discriminator and do not choose identity versus shear.

## Arsenal-first routing

Read `docs/arsenal/index.json`, then only:
- `S33-PW04` for the current marked-source/Picard-adjoint binding and basis firewall;
- `S33-PW07` only for the retained source/cocycle/torsor/Brauer-layer dictionary.

Cards are PROVISIONAL routing aids; live Stage33 source locks override them. V58 permits repeatable bounded search only when each repeat has a materially new mathematical signal. Unbounded/open-ended search remains forbidden.

## Release and verification

Stage33 remains `6/11`. Stage33-12 is not closed. Stage33-13 is not released. No receiver, endpoint, theorem, existence/nonexistence, or merge credit is granted.

After writes run at minimum:

- `python stages/stage33/33-12/verify_e3_b1_c22_j1_xalpha_kernel_correction_v77.py`
- `python stages/stage33/33-12/verify_stage33_v77_frontier_state_v78.py`
- `python stages/stage33/sync_main_state.py --check`
- `git diff --check`

Commit and push the same branch. Do not merge without explicit authorization.
