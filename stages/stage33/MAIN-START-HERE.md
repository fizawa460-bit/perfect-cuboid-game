# Stage33 MAIN startup

Ordinary `Stage33-main-batch` reads `AGENTS.md`, then `stages/stage33/MAIN-STATE.json`, then only the files in `current_leaf_working_set`.

## Stage33 repository-read discipline

For ordinary research/navigation use:

`controller -> active roadmap -> Arsenal index/card -> exact referenced files`

The current branch-local roadmap is `stages/stage33/ROADMAP-33-12-V71-J1-TORSOR.md`. Older roadmaps remain historical planning checkpoints.

Use known paths directly. Repository discovery is search-first. A search miss never proves repository absence or mathematical nonexistence.

**Stage33 MAIN hard ban:** do not request, fetch, or dump a full/recursive repository tree, including GitHub recursive `git/trees` reads or equivalent whole-branch tree enumeration. Do not use a recursive tree as a convenience fallback after a search miss. Navigate only by exact-path fetches, targeted filename/code searches, and explicit controller/roadmap/Arsenal/source-lock references. If a future leaf genuinely requires exhaustive repository enumeration, that requirement must first be made explicit in the Stage33 roadmap/controller; it is not implicitly authorized by `Stage33-main-batch`.

Do not use branch-history archaeology as ordinary discovery.

## Current exact frontier: V75

- V61-V64 fix the B1 source basis, literal `lambda_A`, named `J1/J2`, and `J2 -> u1=[1,0]`.
- V65 reduces J1 to `u2=[0,1]` versus `u1+u2=[1,1]`; the target fingerprints are minimum norm `4` versus `12`.
- V68-V69 reduce the remaining transport to exactly identity versus the unique shear fixing `u1`; one bit remains. V70 replays this reduction immutably.
- V71 constructs the J1-specific Creutz--Viray E[2] cocycle from `(f1,1)`: splitting field `Kgeom(sqrt(f1))`, fixed translation value `rho_f1 -> Tr`.
- V73 applies S33-PW07 to that same J1 cocycle and materializes the direct semilinear translation torsor
  `d*V^2=N^4-2*a*d*N^2*Z^2+d^2*q^2*Z^4` with `d=f1`.
  Its Jacobian is the original `E: y^2=x*(x^2+a*x+b)`, and its genus-0 bisection is split over the `r1,r4` double cover.
- V75 replays the degree-two quotient `X=n^2/d`, `Y=-n*v/d` and proves that `d` cancels, giving the same generic target
  `E'_Tr: Y^2=X*(X^2-2*a*X+q^2)` as in J2.
- Consequently the generic quotient alone is **not** a 4-vs-12 discriminator. Transplanting the J2 R4 lattice conclusion would force the J2 fingerprint `8 -> u1`, which is excluded by the locked V65 J1 gate. V75 therefore fail-closes that shortcut; it does not revoke V65 or V73 and does not select a J1 minimum norm.

The inherited `controller.json` remains the global/firewall authority. Its pre-V61 current-leaf fields are not the branch frontier; `MAIN-STATE.json` records this branch-local current-leaf supersession. No global credit is changed.

## Current leaf

`STOP` means **leaf gate only, not algorithm exhaustion**. `Stage33-main-batch` remains allowed.

D2.1 is PASS at V73. D2.2 remains CURRENT after V75. The exact missing interface is now:

`J1_SPECIFIC_COMPACTIFIED_SURFACE_INTEGRAL_KERNEL_OR_PRIMITIVE_PULLBACK_IDENTIFICATION`

Admissible witnesses are an exact J1 NS/component-glue computation for the V73 compactified torsor, an equivalent integral transcendental-kernel computation tied to `lambda_A/J1`, an exact surface-level pullback/index computation including bad-fiber compactification data, or an independent marked transport witness.

Only two final fingerprint outcomes remain admissible:
- `4` => `J1 -> u2` => shear transport;
- `12` => `J1 -> u1+u2` => identity transport.

Do not reuse the retained J2 minimum norm `8`, and do not infer the J1 integral kernel from the `d`-independent generic quotient alone.

Historical contact/Weil pairing data have already been reevaluated at the V69 one-bit frontier and do not distinguish identity from shear. Do not reopen them without materially new target-side data.

## Arsenal-first routing

Read `docs/arsenal/index.json`, then only:
- `S33-PW07` for the active torsor -> compactified NS/component glue -> integral/twisted-kernel construction;
- `S33-PW04` for exact marked-source transport/firewall once an independent fingerprint is available.

Cards are PROVISIONAL routing aids; live Stage33 source locks override them. V58 permits repeatable bounded search only when each repeat has a materially new mathematical signal. Unbounded/open-ended search remains forbidden.

## Release and verification

Stage33 remains `6/11`. Stage33-12 is not closed. Stage33-13 is not released. No receiver, endpoint, theorem, existence/nonexistence, or merge credit is granted.

After writes run at minimum:

- `python stages/stage33/33-12/verify_e3_b1_c22_j1_translation_torsor_v73.py`
- `python stages/stage33/33-12/verify_e3_b1_c22_j1_generic_quotient_discriminator_rejection_v75.py`
- `python stages/stage33/33-12/verify_stage33_v75_frontier_state_v76.py`
- `python stages/stage33/sync_main_state.py --check`
- `git diff --check`

Commit and push the same branch. Do not merge without explicit authorization.
