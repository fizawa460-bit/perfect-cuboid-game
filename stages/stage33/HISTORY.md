# Stage33 history and evidence index

This file is an index of past Stage33 decisions, route changes, revocations, and evidence locations. It is not current-state authority and it is not a proof certificate.

For ordinary current startup use `MAIN-START-HERE.md` / `MAIN-STATE.json`.
For detailed machine state use `controller.json`; for stable rules use `RULES.md`.

## Structural history

### Initial Stage33 execution plan

Stage33 began as the 11-big-task `BRAUER-EXPLICIT-DAG` execution program for the frozen Stage29 physical-open Brauer kernel. The original plan and task descriptions remain in `ROADMAP.md`.

The original roadmap also accumulated execution policy and a mutable status header; those are now treated as historical/plan text rather than current authority. Stable policy is routed through `RULES.md`, compact startup state through generated `MAIN-STATE.json`, and detailed live state through `controller.json`.

### Stage33-07 repair band

Stage33-07 was reopened and repair children 33-09 through 33-12 were introduced. Their historical development and child-level evidence remain in:

- `ROADMAP-33-07-REPAIR-BAND.md`
- `33-09/` through `33-12/`
- `33-00/unit-closure-contract.md`

The repair children do not independently increment the 11-task Stage33 progress denominator.

## Reusable Stage33 achievement index

Use this section as the first lookup table when a later Stage33 leaf needs an already-computed object, basis, map, residue calculation, descent datum, certificate, or negative result. It is a navigation layer only: current mathematical authority remains `controller.json` / active state, and exact credit remains in the cited certificate/result/audit files.

### Fast lookup by mathematical object

| Need / object | Reuse first | What is already available | Important scope / warning |
|---|---|---|---|
| Stage29 Brauer source/dependency reconstruction | `33-01/result.md` | frozen dependency DAG; 72 physical-boundary components; Ford line source dim 9; Kc geometric Br[2] dim 2; all-primary BR0B scope firewall | reconnaissance facts only where explicitly marked preview |
| full-surface retained Picard / boundary map | `33-02/result.md`, `33-02/cross-stage-picard-adapter.md` | exact `72 x 64` boundary-to-Picard map; rank 58; unit kernel rank 14; open Picard free rank 6; saturation index 4; quotient torsion `(Z/2)^2`; exact Gram/restriction data | prefer exact integral adapter; do not replace with rational-rank reasoning |
| absolute UPic / open algebraic Brauer module | `33-03/result.md` | `U_D ~= Z^14`; `Pic(Ubar) ~= Z^6 + (Z/2)^2`; exact V4 cohomology; hidden extension data; five free `d2_11=0`; all-primary inventory structure | filtration extension is exact but not asserted split |
| physical-boundary residues / Gersten | `33-04/result.md` | 72 components, 144 crossings; exact residue/incidence data; `(Z/2)^49 + (Z/4)^12` finite ramified two-primary module; odd-primary character factors; exponent-two residual data | Stage33-04 does not itself provide final duplicate-integrated Q-defined class inventory |
| corrected K3 J2 / q1 geometric invariant block | `33-05/result.md`, `33-05/j2-representative-repair-state.json` | corrected `J2=(f2,1)`; invariant basis `{J2,q1}`; exact HS d2 classification; exact zero Q-survival; hostile replay certificate | historical `ell_J2` / `ell_Q` Q-defined witness is revoked; corrected J2 has no Q-defined Brauer preimage |
| seven-line/Ford source at endpoint | `33-06/result.md` | exact 9D source basis and exact zero endpoint pullback because all ambient Ford symbols become squares | zero is specific to the seven-line source; any stale references in older result text to a surviving J2 are superseded by current 33-05/controller state |
| integrated Stage33 class inventory / relation-symbol layer | `33-07/`, `ROADMAP-33-07-REPAIR-BAND.md` | historical integration work plus the repair obligations that led to 33-09..33-12 | 33-07 is currently blocked on repair child 33-12; never treat an old closed-looking artifact as current closure authority |
| explicit endpoint representatives | `33-08/` | historical BR2B representative work | currently blocked by 33-07; reuse formulas only after checking current inventory identity |
| Picard-equivariant transport repair | `33-09/` | exact closed Picard-equivariant transport interface | current controller records `CLOSED_EXACT`; canonical digest is in controller |
| absolute H1 receiver repair | `33-10/` | exact closed absolute H1 receiver | current controller records `CLOSED_EXACT`; canonical digest is in controller |
| arithmetic localization connecting map | `33-11/` | exact zero connecting map, all 26/26 columns audited | current controller records hostile-audit PASS and zero unresolved columns |
| current arithmetic HS / finite-V4 Kummer repair | `MAIN-STATE.json`, `33-12/`, `controller.json` | corrected J2 surface mu2 lift; cc=0; six ct Kc supports; fullPic64 pullbacks; retained weight-15 75D H1 target; exact named orientation `u1=[1,0]`; exact full-surface `A_T[2]` coordinate; retained 10D basis | OPEN. Minimal missing datum is the corrected Kc Brauer functional pullback/evaluation coordinate in the current full-surface proper-Br2 14D dual basis, followed by deterministic retained-10D placement; do not copy `A_T[2]` coefficients or promote parent 33-07 closure |

### Fast lookup by reusable interface

```text
BOUNDARY -> FULL PICARD 64D
  33-02
  exact integral 72x64 map, Gram/restriction data, SNF/saturation

OPEN ALGEBRAIC / UPic / ABSOLUTE GALOIS
  33-03
  exact U_D, Pic(Ubar), V4 H1/H2, d2, hidden extension

PHYSICAL BOUNDARY / RESIDUES / GERSTEN
  33-04
  exact incidence, residue modules, odd-primary characters, 2-primary order-4 block

K3 GEOMETRIC Br[2] -> ARITHMETIC HS
  33-05
  corrected J2 and q1; exact d2 rank 2; Q-surviving dimension 0

SEVEN-LINE SOURCE -> ENDPOINT
  33-06
  exact pullback zero

PICARD-EQUIVARIANT TRANSPORT
  33-09
  closed exact adapter

ABSOLUTE H1 RECEIVER
  33-10
  closed exact receiver

LOCALIZATION CONNECTING MAP
  33-11
  exact zero map, 26/26 audited

FINITE-V4 KUMMER / FULL-SURFACE HS
  33-12
  current live repair; reuse all already-materialized J2 surface/Picard/H1 data,
  orientation and full-surface A_T[2] coordinate are exact;
  the proper-Br2 dual functional placement remains open
```

### Current high-value Stage33-12 reusable assets

The current controller already records the following as materialized and reusable inside Stage33-12 without reopening their derivation unless an audit contradiction appears:

- corrected J2 surface `mu2` lift;
- corrected J2 ct defect on marked Kc Pic/2 with semantic BigK support `[26,35,42,47,49,52]`;
- corrected J2 cc defect with integral Pic class zero and fullPic64 mod-2 zero;
- exact actual-Cech cc certificate;
- retained full-surface marked-basis numeric matrix;
- six corrected-J2 ct Kc-support pullbacks to fullPic64;
- retained 75D finite-V4 H1 named J2 target, nonzero of weight 15;
- exact named CV semantic orientation `u1=[1,0]`;
- exact semantic-u1 full-surface `A_T[2]` coordinate `[0,0,0,0,0,0,0,1,0,1,0,1,1,0]` from pinned rows and literal retained Magma Smith `V`;
- exact rejection of copying those `A_T[2]` coefficients into the ordered proper-Br2 dual basis (nonzero cc-invariance defect);
- deterministic proper-Br2 `14D -> retained 10D` solve once the source coordinate is known.

Do not redo the historical search for a full `Kc20 -> fullPic64` matrix merely to obtain the first Kummer column: the current controller explicitly records that the six required rows and Smith transform are already exact. The named semantic orientation and full-surface `A_T[2]` element are exact. The active missing datum is narrower: materialize the corrected Kc Brauer functional's pullback/evaluations in the full-surface proper-Br2 14D dual basis, solve its retained 10D coordinate, then place the already-locked 75D target.

### Reuse protocol for future Stage33 batches

Before launching a new derivation for an object that sounds familiar:

1. search this index by object/interface name;
2. check `controller.json` / active state for whether the cited result is still authoritative, superseded, revoked, or only historical;
3. open only the indicated unit result/state and the exact certificate needed for the current leaf;
4. reuse a closed exact adapter directly when its source/target identities match;
5. if identities differ, build an explicit adapter instead of silently transferring credit;
6. only return to broad Git history/repo search when this index has no matching reusable object or when the indexed artifact fails identity checks.

This protocol is intended to reduce repeated repository scans and token use without weakening hostile-audit traceability.

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

Add entries here when a route is materially retired/revoked, a major promotion is rolled back, a new repair generation supersedes an old one, or a historical checklist becomes non-authoritative. Also update the reusable achievement index when a newly closed interface is likely to be consumed again by another Stage33 unit. Do not duplicate every batch or every certificate; link to unit results and Git history instead.
