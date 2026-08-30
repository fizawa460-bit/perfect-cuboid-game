# Stage33-05 J2 named-representative repair roadmap

Purpose: keep the hostile reopen of Stage33-05 finite, current, and non-duplicative. This file is a navigation/exit-contract document. Closed proofs live in their certificates; current machine state lives in `stages/stage33/33-05/j2-representative-repair-state.json`.

## Authority and scope

Current authoritative runtime sources:

```text
controller: stages/stage33/controller.json
repair state: stages/stage33/33-05/j2-representative-repair-state.json
post-R5 compact state: stages/stage33/33-05/j2-post-r5-hs-d2-state.json
audit state: stages/stage33/33-05/audit-state.json
```

This repair does not revoke the abstract geometric statement `Br(Kc_bar)[2] ~= (F2)^2` or the abstract class label `J2`. It revoked the old promoted Q-defined representative because that representative is zero in the full geometric CV quotient.

Stage33-12 files used below are evidence for this repair. They are not a second independent roadmap for the same J2 calculation.

## Current dashboard

```text
R0 = DONE: old promoted ell_J2 is zero in the geometric CV quotient
R1 = DONE: abstract J2 independently nonzero
R2 = DONE: corrected geometric representative J2=(f2,1) nonzero
R3 = DONE: corrected CV E[2] cocycle xi(rho)=Tr
R4 = DONE: twisted kernel <8>+<16>, min norm 8, marked J2=[1,0]
R5 geometric hostile replay = PASS
R5 arithmetic descent = OPEN
Stage33 progress = 5/11
Stage33-05 reclosed = false
Stage33-12 exact closure = false
Stage33-13 release = false
```

## Finite repair ladder

| Leaf | Question | Exact exit | State |
|---|---|---|---|
| R0 | Was the old promoted representative valid? | Full geometric CV quotient regression | DONE: ZERO |
| R1 | Is abstract J2 genuinely nonzero? | Independent quotient/presentation check | DONE |
| R2 | Is there a correct concrete geometric representative? | Corrected `(f2,1)` nonzero in `L^*/(K^*L^{*2})` | DONE |
| R3 | What is its generic-fiber cohomology class? | Explicit CV `E[2]` cocycle | DONE |
| R4 | Which marked Brauer functional is it? | Twisted kernel/lattice fingerprint | DONE: `[1,0]` |
| R5 | Does corrected geometric J2 descend arithmetically over Q? | Actual surface `mu2` lift -> Pic/2 defect -> integral lift -> HS `d2` -> Q-Brauer verdict | OPEN |

R0-R4 are frozen unless a source-lock contradiction is found. Do not re-prove them during ordinary MAIN.

## R5 expanded roadmap

The original R5 wording only required hostile replay of R1-R4. That replay passed, but a fresh hostile audit then found an unjustified inference:

```text
geometric Galois fixedness  !=>  Hochschild-Serre d2 = 0
```

R5 therefore has the following post-replay arithmetic substeps.

| Step | Exact object | State |
|---|---|---|
| R5a | Independent hostile replay of corrected R1-R4 geometry | DONE |
| R5b | Corrected finite smooth support on marked Kc / CsK[22] | DONE |
| R5c | Genuine `lambda_D in H^2_et(Kc_bar,mu_2)` via explicit Cech/Gysin construction | DONE |
| R5d | Generic cc/ct defect splittings, q-fiber support, normalized ct rank-2 splitting module | DONE |
| R5e | Actual local Cech rank-2 lattices and overlap transitions; actual cc/ct classes in `Pic(Kc_bar)/2` | OPEN / CURRENT |
| R5f | Integral Pic lifts and Bockstein/Hochschild-Serre `d2` 2-cocycle/class | OPEN |
| R5g | Q-defined Brauer preimage and arithmetic unramifiedness, restricting back to corrected `J2=(f2,1)` | OPEN |

### Current exact leaf

```text
MATERIALIZE_ACTUAL_CECH_LOCAL_RANK2_LATTICES_AND_OVERLAP_TRANSITION_MATRICES_FOR_LAMBDA_D_AT_T0_TINF_SINF_C21_C22_AND_RESOLUTION_EXCEPTIONALS_THEN_COMPARE_CC_CT_NULLHOMOTOPIES_AND_COMPUTE_MARKED_PIC_MOD2_AND_HS_D2
```

Required next checks:

1. Materialize the actual local rank-two lattices and overlap transition matrices for the chosen Cech extension of `lambda_D` at `t=0`, `t=infinity`, `s=infinity`, `C21`, `C22`, and every resolution exceptional.
2. Compare the actual cc/ct nullhomotopies with the standard auxiliary q-cover module. The even determinant of the standard module does not determine the actual compactified defect.
3. Compute the actual cc/ct defect classes in `Pic(Kc_bar)/2`.
4. Choose integral Pic lifts.
5. Compute the Bockstein/Hochschild-Serre `d2` 2-cocycle and its cohomology class without assuming zero.
6. Only if the class is zero, use HS kernel=image to recover Q-defined Brauer credit.
7. Verify the arithmetic lift restricts to the corrected nonzero `J2=(f2,1)`, never the revoked old `ell_J2`.
8. Verify arithmetic unramifiedness before restoring Stage33-05/12 credit.

## R5 exit contract

Successful R5 repair exit requires all of:

```text
ACTUAL_CC_CT_PIC_MOD2_DEFECT_MATERIALIZED=true
INTEGRAL_PIC_LIFTS_MATERIALIZED=true
HS_D2_2COCYCLE_MATERIALIZED=true
HS_D2_CLASS_ZERO=true
Q_DEFINED_CORRECTED_J2_BRAUER_PREIMAGE=true
ARITHMETIC_UNRAMIFIEDNESS=true
RESTRICTS_TO_CORRECTED_J2_F2_1=true
R5_FULL_REPAIR_EXIT_REACHED=true
```

If `HS_D2_CLASS_ZERO=false`, that is an exact arithmetic no-go for this corrected geometric J2 descent route. It is a mathematical verdict, but it is not a successful reclosure. In that case the dependency chain must be explicitly rebuilt; do not force `Stage33-05` or `Stage33-12` closed.

After successful full R5 exit only:

```text
1. transition to a new PR as required by the repair state
2. run mandatory super-hostile audit
3. if audit PASS, re-close Stage33-05
4. re-evaluate and close Stage33-12 only from corrected evidence
5. release Stage33-13 only after Stage33-12 exact closure
```

## Closed-leaf evidence index

```text
R0: stages/stage33/33-12/j2-cv-lclass-zero-regression.json
R1: stages/stage33/33-05/j2-abstract-nonzero-reaudit.json
R2: stages/stage33/33-05/j2-corrected-full-l-representative.json
R3: stages/stage33/33-05/j2-corrected-cv-e2-cocycle.json
R4: stages/stage33/33-05/j2-r4-hostile-torsor-brauer-kernel-verification.json
R5 geometric replay: stages/stage33/33-05/j2-r5-hostile-replay.json
```

Current post-R5 evidence:

```text
pre-Kummer cochain: stages/stage33/33-05/j2-corrected-pre-kummer-descent-cochain.json
corrected Kc support: stages/stage33/33-12/j2-corrected-kc-branch-support.json
surface mu2 adapter: stages/stage33/33-12/j2-corrected-branch-surface-mu2-adapter.json
explicit Cech mu2 lift: stages/stage33/33-12/j2-corrected-explicit-cech-mu2-lift.json
ct norm Picard support: stages/stage33/33-12/j2-corrected-ct-norm-picard-support.json
ct norm splitting module: stages/stage33/33-12/j2-corrected-ct-norm-splitting-module.json
surface boundary contract: stages/stage33/33-12/j2-full-surface-mu2-zero-defect-contract.json
```

## Retired routes and forbidden shortcuts

```text
old Q-defined ell_J2 / historical CSA = REVOKED
historical named Kummer glue producer for old representative = TOMBSTONED
old infinity/exceptional support dependency for corrected D = NOT REQUIRED
single degree-two quotient image (0,0) = NOT the full E[2] cocycle or surface Kummer class
geometric Galois fixedness => HS d2=0 = FORBIDDEN
standard auxiliary q-cover determinant parity => actual compactified defect parity = FORBIDDEN
```

The corrected divisor uses finite smooth Kc support on `CsK[22]`; do not resurrect the old infinity/ptsK/qPicK route merely because older Stage33-12 notes still mention it.

## MAIN startup and reporting

Ordinary `Stage33-main-batch` in this repair reads only:

```text
1. AGENTS.md
2. stages/stage33/controller.json
3. this roadmap
4. stages/stage33/33-05/j2-representative-repair-state.json
5. stages/stage33/33-05/j2-post-r5-hs-d2-state.json
6. immediate certificates named by the current leaf
```

User-visible status format:

```text
33-05 repair: post-R5 | current arithmetic substep | exact new information | unknown count | next exit test
```

Two consecutive batches with no change in leaf, invariant, candidate set, or missing interface trigger a route audit rather than another same-form attempt.

## Firewalls

Until successful R5 full exit and mandatory super-hostile audit PASS:

```text
Q_DEFINED_DESCENT_CREDIT=false
STAGE33_05_RECLOSED=false
STAGE33_12_CLOSED_EXACT=false
STAGE33_13_RELEASED=false
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
