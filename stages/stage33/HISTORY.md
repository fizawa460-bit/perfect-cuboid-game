# Stage33 history and evidence index

This file is an index of past Stage33 decisions, route changes, revocations, and evidence locations. It is not current-state authority and it is not a proof certificate.

For current status use `CURRENT.md` / `controller.json`. For stable rules use `RULES.md`.

## Structural history

### Initial Stage33 execution plan

Stage33 began as the 11-big-task `BRAUER-EXPLICIT-DAG` execution program for the frozen Stage29 physical-open Brauer kernel. The original plan and task descriptions remain in `ROADMAP.md`.

The original roadmap also accumulated execution policy and a mutable status header; those are now treated as historical/plan text rather than current authority. Stable policy is routed through `RULES.md`, while live status is routed through `CURRENT.md` and `controller.json`.

### Stage33-07 repair band

Stage33-07 was reopened and repair children 33-09 through 33-12 were introduced. Their historical development and child-level evidence remain in:

- `ROADMAP-33-07-REPAIR-BAND.md`
- `33-09/` through `33-12/`
- `33-00/unit-closure-contract.md`

The repair children do not independently increment the 11-task Stage33 progress denominator.

## J2 representative repair history

### Historical named representative revoked

The previously promoted Q-defined `ell_J2` / `ell_Q` / CSA route was found to have zero full geometric Creutz--Viray class and cannot serve as the named nonzero J2 witness.

Primary historical evidence includes:

- `33-12/j2-cv-lclass-zero-regression.json`
- `33-05/j2-post-r5-hs-descent-datum.json`

The failed/revoked artifacts remain retained as audit evidence; they must not be silently reused for corrected-J2 credit.

### Corrected geometric representative

The corrected geometric representative was established as `J2=(f2,1)`, with explicit nonzero CV data and marked Brauer coordinate `[1,0]`.

Key evidence:

- `33-05/j2-corrected-full-l-representative.json`
- `33-05/j2-corrected-cv-e2-cocycle.json`
- `33-05/j2-r4-hostile-torsor-brauer-kernel-verification.json`
- `33-05/j2-r5-hostile-replay.json`

Retained geometric facts include `xi(rho)=Tr`, twisted kernel Gram `diag(8,16)`, minimum norm 8, and marked J2 coordinate `[1,0]`, within their declared geometric scope.

### Post-R5 arithmetic descent rollback

An attempted post-R5 Q-descent promotion proved finite-presentation Galois fixedness but did not derive the actual Pic/2 defect, integral Pic lift, or Hochschild--Serre d2. The shortcut

```text
Galois-fixed geometric Brauer class => HS d2 = 0
```

was rejected.

This reopened the arithmetic part of R5 without revoking the retained R0-R4 geometric credit.

### Corrected surface lift progress

The corrected route then materialized:

- half-divisor `D=P_r2-P_r4` and representative-level descent witnesses;
- finite smooth marked-Kc support on `CsK[22]`;
- branch-to-surface `H^2(mu2)` adapter;
- explicit Cech symbol `e_D` and genuine surface mu2 lift `lambda_D`;
- generic cc/ct splitting data;
- ct norm witness and exact generic rank-2 splitting matrices.

Key evidence:

- `33-05/j2-corrected-pre-kummer-descent-cochain.json`
- `33-12/j2-corrected-kc-branch-support.json`
- `33-12/j2-corrected-branch-surface-mu2-adapter.json`
- `33-12/j2-corrected-explicit-cech-mu2-lift.json`
- `33-12/j2-corrected-ct-norm-picard-support.json`
- `33-12/j2-corrected-ct-norm-splitting-module.json`

An explicit elementary-transform comparison showed that the even determinant of the standard auxiliary q-cover does not determine the actual compactified Pic/2 defect. This is why the current route moved to actual local Cech lattices and overlap transitions.

### Retired corrected-J2 subroutes

The historical infinity/ptsK/qPicK/old-Kummer-glue checklist is retired for the corrected J2 route because the corrected support uses finite smooth Kc points and the modern surface-lift path supersedes that checklist.

Historical formulas and certificates may still be used as source material only when their scope is valid; retired credit must not be resurrected by name matching alone.

## Navigation cleanup history

In the August 2026 Stage33 cleanup:

- the J2 repair roadmap was reduced to the current R5a-R5g structure;
- the Stage33-12 roadmap role was separated from the active 33-05 arithmetic repair;
- `controller.json` was compacted around current execution state;
- `controller-post-r5-hs-d2-override.json` became a compatibility shim;
- `33-05/j2-post-r5-hs-d2-state.json` became a compatibility shim;
- `33-05/j2-representative-repair-state.json` became the single authoritative detailed R5 mathematics state;
- `33-12/result.md` was updated to the corrected R5e/R5f/R5g sequence;
- `RULES.md`, `CURRENT.md`, and `HISTORY.md` were introduced to separate stable policy, current state, and historical evidence.

Historical checkpoint PR #1463 was merged, but that checkpoint merge did not itself close Stage33-12 or release Stage33-13.

## Evidence locations by role

```text
Current Stage33 machine state:
  controller.json

Current J2 repair mathematics:
  33-05/j2-representative-repair-state.json

Current human dashboard:
  CURRENT.md

Stable Stage33 rules:
  RULES.md

High-level plan:
  ROADMAP.md
  ROADMAP-33-05-J2-REPRESENTATIVE-REPAIR.md
  ROADMAP-33-07-REPAIR-BAND.md

Per-unit historical summaries:
  33-xx/result.md
  33-xx/audit.md / audit-state.json where present

Exact evidence:
  33-xx/*.json certificates
  certifier/verifier scripts
  Git commit history
```

## Maintenance rule

Add entries here when a route is materially retired/revoked, a major promotion is rolled back, a new repair generation supersedes an old one, or a historical checklist becomes non-authoritative. Do not duplicate every batch or every certificate; link to unit results and Git history instead.
