# Stage33 MAIN — START HERE

Purpose: keep ordinary `Stage33-main-batch` context small enough to reach the current exact computation. This file is the default MAIN interface, not a hostile-audit record.

## Mandatory read order for ordinary MAIN

Read only:

1. `AGENTS.md`
2. `stages/stage33/controller.json`
3. this file
4. the files named under **Current leaf working set** below

Do **not** reconstruct Stage33 history by default. Do not read old PR diffs, old workflow logs, full ancestor result trees, or old certificates merely for reassurance. Hostile audit may expand history separately.

Expand an ancestor only when the current proof genuinely needs an internal matrix/representative not exposed by the audited handoff, a source lock mismatches, a certificate contradicts the current interface, or the user explicitly requests audit/history. State the named reason before expanding.

## Current work area

- PR: `#1460`
- branch: `stage33-12-arithmetic-hs-bootstrap`
- active repair child: `Stage33-12 — ARITHMETIC-HS-CLOSURE-AND-33-07-RECERTIFICATION`
- Stage33 big-task progress remains `6/11`; repair children do not increment that denominator.
- Stage33-07 is still open; Stage33-08 and Stage33-40 remain blocked.

## Audited opaque inputs — trust these interfaces in MAIN

- Stage33-09: Picard-equivariant transport `CLOSED_EXACT`.
- Stage33-10: absolute receiver `X_Q^5 direct_sum X_Q(i)^3 direct_sum E_L`, with the non-split `E_L` filtration preserved; hostile-audit PASS.
- Stage33-11: localization connecting map `COMPUTED_EXACT_ZERO_MAP`, exact `26/26`; hostile-audit PASS. Certificate SHA256: `233be042e92010be169206df1193f25375ee9fd768f7fb3eebb9eb696389632e`.

Important: Stage33-11 zero connecting map does **not** imply the full arithmetic Hochschild–Serre `d2` is zero.

## Current exact Stage33-12 state

- Known Q-defined blocks have exact HS image zero.
- Odd-primary global residue-lift obligation is exact-complete.
- `P = Br(Sbar)[2]^{G_Q}` has exact F2 dimension `10`.
- `H^1(V4, Pic(Sbar)/2)` has exact F2 dimension `75`.
- Missing finite Kummer restriction is a literal `75 x 10` matrix; materialized columns remain `0/10`.
- Finite obstruction cosets remain `0/26` materialized.
- Remaining obstruction blocks are the two-primary constant-character cokernel and the finite 26-direction block.

Named J2 progress already materialized:

- `E_J2 = 2*infinity_minus - P_plus - P_minus`, with `div(ell_J2)=2E_J2`.
- CV branch is pinned to Stoll `CsK[22]` on `K_c`.
- three support images are materialized.
- the infinity branch meets the resolved exceptional conic in tangent direction `[1:i:0]`.
- the pinned Stoll `ptsK` order index and corresponding `qPicK` exceptional coordinate are **not yet certified**.
- branch-Jacobian 2-torsion -> Kc Picard discriminant/Brauer glue is **not yet materialized**.
- J2/q1 adapter is not unique.

## Current exact leaf

First, materialize the pinned Stoll exceptional index and `qPicK` coordinate for J2 infinity using the already-written narrow extractor. Then use that resolved marked-curve datum together with `CsK[22]` and `E_J2` to construct the genuine Kummer/Picard-transcendental glue from the branch Jacobian 2-torsion to the Kc discriminant/Brauer 2-torsion coordinate.

Do not replace this with a giant SymPy Smith recomputation.

### Current leaf working set

Normally read only these Stage33 files in addition to the mandatory three files above:

- `stages/stage33/33-12/result.md` — current checkpoint/interface
- `stages/stage33/33-12/extract_j2_infinity_kc_exceptional_order.py` — immediate leaf
- `stages/stage33/33-12/j2-named-kummer-glue-input.json` — exact named J2 half-divisor/glue input

After the extractor succeeds, its generated certificate `stages/stage33/33-12/j2-infinity-kc-exceptional-order.json` becomes part of the working set. Read additional source only if the next glue computation actually requires it.

## MAIN behavior

Advance the exact next leaf. Do not spend a MAIN batch re-auditing already audited inputs. Preserve exact/audited state separately from MAIN working progress; unresolved adapter/glue data must remain explicit rather than guessed.

Before Actions/artifact/heavy compute, read `docs/research-os/policies/actions-storage-and-evidence-safety.md`. Before claim promotion, closure, or downstream release, read `docs/research-os/policies/research-credit-and-promotion-firewalls.md`.

At the end of every MAIN batch with repository writes, synchronize `controller.json`, `33-12/result.md`, and this file if the exact next leaf or working set changed. Keep this file short; replace obsolete current-leaf detail instead of appending history.

## Firewalls

Until explicitly audited/released:

- `ARITHMETIC_HS_D2_COMPUTED=false`
- `GLOBAL_Q_BR0G_RESIDUE_LIFTS_COMPLETE=false`
- `COMPLETE_RELEVANT_Q_DEFINED_CLASS_LIST_FOR_STAGE33_BRAUER_SCOPE=false`
- `STAGE33_07_HOSTILE_REAUDIT=NOT_RUN`
- `STAGE33_12_CLOSED=false`
- Stage33-08 unreleased
- Stage33-40 unreleased
- theorem credit=false
- receiver/endpoint credit=false
- perfect-cuboid existence/nonexistence claim=false
