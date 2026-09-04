# Stage33 MAIN startup

Ordinary `Stage33-main-batch` reads `AGENTS.md`, then `stages/stage33/MAIN-STATE.json`, then only the files in `current_leaf_working_set`.

## Stage33 repository-read discipline

For ordinary research/navigation use:

`controller -> active roadmap -> Arsenal index/card -> exact referenced files`

The current branch-local roadmap is `stages/stage33/ROADMAP-33-12-V65-J1-DISCRIMINATOR.md`. The older `ROADMAP-33-12-MICROGOALS.md` is retained as the historical V60 planning checkpoint.

Use known paths directly. Repository discovery is search-first. A search miss never proves repository absence or mathematical nonexistence.

**Stage33 MAIN hard ban:** do not request, fetch, or dump a full/recursive repository tree, including GitHub recursive `git/trees` reads or equivalent whole-branch tree enumeration. Do not use a recursive tree as a convenience fallback after a search miss. Navigate only by exact-path fetches, targeted filename/code searches, and explicit controller/roadmap/Arsenal/source-lock references. If a future leaf genuinely requires exhaustive repository enumeration, that requirement must first be made explicit in the Stage33 roadmap/controller; it is not implicitly authorized by `Stage33-main-batch`.

Do not use branch-history archaeology as ordinary discovery.

## Current exact frontier: V65

The branch exact certificate chain has advanced beyond the inherited controller current-leaf text:

- V61 fixes `[kappa_A,kappa_D]` on `Pic0(C22_tilde)[2]`.
- V62 fixes the full B1 ordered basis `[cc(kappa_A),cc(kappa_D),kappa_A,kappa_D]`.
- V63 materializes the literal Cech/surface `mu2` lift for `kappa_A` as B1 column 3, but not its marked proper14 coordinate.
- V64 identifies `kappa_A=J1`, `kappa_D=J2`, fixes `J2 -> u1=[1,0]`, and reduces J1 to exactly `{u2=[0,1],u1+u2=[1,1]}`.
- V65 freezes that one-bit gate. The fixed marked target fingerprints distinguish the candidates by minimum norm `4` versus `12`, but no independent source-locked J1 fingerprint or exact second transport column is yet materialized.

The inherited `controller.json` remains the global/firewall authority. Its pre-V61 current-leaf fields are not the branch frontier; `MAIN-STATE.json` and V65 explicitly record this temporary branch-local current-leaf supersession. No global credit is changed.

## STOP semantics

`STOP` at V65 means **leaf gate only, not algorithm exhaustion**. `Stage33-main-batch` remains allowed. Continue by constructing one exact discriminator; do not promote column 3 by guess.

Admissible next witnesses:

1. exact second column of the named CV/contact -> fixed marked Kc transport;
2. independent source-locked J1 fingerprint, preferably a J1-specific twisted-kernel minimum norm;
3. exact source and fixed-marked-Kc automorphism actions plus an equivariance proof.

Historical contact bits are not marked Kc coordinates. An arbitrary GL2(F2) complement is forbidden. The J2-specific twisted kernel cannot be relabelled as J1. A source elliptic automorphism without an exact target action is insufficient.

## Arsenal-first routing

Read `docs/arsenal/index.json`, then only:
- `S33-PW04` for exact marked-source / Picard-interface transport;
- `S33-PW07` for torsor/Brauer/integral-kernel construction.

These cards are PROVISIONAL routing aids; live Stage33 source locks override them. V58 still permits repeatable bounded searches when each repeat has a materially new mathematical signal. There is no fixed per-object count cap. Unbounded/open-ended search remains forbidden.

## Release and verification

Stage33 remains `6/11`. Stage33-12 is not closed. Stage33-13 is not released. No receiver, endpoint, theorem, existence/nonexistence, or merge credit is granted.

After writes run at minimum:

- `python stages/stage33/33-12/verify_e3_b1_c22_pic0_2_basis_v61.py`
- `python stages/stage33/33-12/verify_e3_b1_full_domain_basis_v62.py`
- `python stages/stage33/33-12/verify_e3_b1_c22_kappa_a_literal_cech_lift_v63.py`
- `python stages/stage33/33-12/verify_e3_b1_c22_named_torsion_normalization_bridge_v64.py`
- `python stages/stage33/33-12/verify_e3_b1_j1_marked_kc_discriminator_gate_v65.py`
- `python stages/stage33/33-12/verify_stage33_v65_frontier_state_v66.py`
- `python stages/stage33/sync_main_state.py --check`
- `git diff --check`

Commit and push the same branch. Do not merge without explicit authorization.