# Stage33-05 J2 named-representative repair roadmap

Purpose: define the finite repair ladder and successful exit contract for the hostile reopen of Stage33-05 without duplicating current status or historical evidence.

This file is **planning/exit-contract only**.

Use:

```text
current human status  -> stages/stage33/CURRENT.md
current machine state -> stages/stage33/controller.json
current R5 math state -> stages/stage33/33-05/j2-representative-repair-state.json
history/evidence      -> stages/stage33/HISTORY.md and 33-05/33-12 certificates/results
stable rules          -> stages/stage33/RULES.md
```

Do not add mutable Stage33 progress, current leaf, attempt counters, or live-route ledgers here.

## Scope

This repair concerns the named J2 representative/descent path for Stage33-05. It does not by itself revoke the abstract geometric statement `Br(Kc_bar)[2] ~= (F2)^2` or the abstract class label J2.

Stage33-12 files may provide evidence used by this repair, but Stage33-12 is not a second independent roadmap for the same J2 calculation.

## Finite repair ladder

| Leaf | Question | Exact exit |
|---|---|---|
| R0 | Was the old promoted representative valid? | Full geometric CV quotient regression |
| R1 | Is abstract J2 genuinely nonzero? | Independent quotient/presentation check |
| R2 | Is there a correct concrete geometric representative? | Corrected `(f2,1)` nonzero in `L^*/(K^*L^{*2})` |
| R3 | What is its generic-fiber cohomology class? | Explicit CV `E[2]` cocycle |
| R4 | Which marked Brauer functional is it? | Twisted kernel/lattice fingerprint |
| R5 | Does corrected geometric J2 descend arithmetically over Q? | Actual surface `mu2` lift -> Pic/2 defect -> integral lift -> HS `d2` -> Q-Brauer verdict |

Closed leaves are frozen unless a source-lock contradiction is found. Their current DONE/OPEN status belongs in CURRENT/state, not this roadmap.

## R5 arithmetic ladder

The R5 repair is decomposed as:

| Step | Exact object |
|---|---|
| R5a | Independent hostile replay of corrected R1-R4 geometry |
| R5b | Corrected finite smooth support on marked Kc / `CsK[22]` |
| R5c | Genuine `lambda_D in H^2_et(Kc_bar,mu_2)` via explicit Cech/Gysin construction |
| R5d | Generic cc/ct defect splittings, q-fiber support, normalized ct rank-2 splitting module |
| R5e | Actual local Cech rank-2 lattices and overlap transitions; actual cc/ct classes in `Pic(Kc_bar)/2` |
| R5f | Integral Pic lifts and Bockstein/Hochschild-Serre `d2` 2-cocycle/class |
| R5g | Q-defined Brauer preimage and arithmetic unramifiedness, restricting back to corrected `J2=(f2,1)` |

The exact current substep is read from CURRENT/controller/repair-state.

## R5e acceptance

R5e is complete only after the actual compactified Cech extension is represented by local rank-two lattices and overlap transition matrices at every required divisor/resolution exceptional and these data determine the actual cc/ct Picard-mod-2 defect classes.

Generic splitting matrices or the determinant parity of a standard auxiliary compactification are not substitutes for the actual chosen extension.

## R5f acceptance

R5f is complete only after integral Picard lifts are chosen and the resulting Bockstein/Hochschild-Serre `d2` 2-cocycle and its cohomology class are explicitly computed without assuming zero.

Geometric Galois fixedness alone does not imply `d2=0`.

## R5g acceptance

If the exact HS `d2` class is zero, R5g must materialize a Q-defined Brauer preimage, prove the required arithmetic unramifiedness, and verify that geometric restriction is the corrected nonzero `J2=(f2,1)` rather than the revoked historical representative.

If the exact HS `d2` class is nonzero, record the arithmetic no-go and rebuild the dependency chain; do not force successful reclosure.

## Successful R5 exit contract

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

Only after successful full R5 exit may the transition/audit/reclosure sequence defined by CURRENT/controller/RULES and the repair-band/closure contract proceed.

## Evidence and retired routes

Closed-leaf certificates, current post-R5 certificates, revoked representatives, tombstoned producers, and retired route families are indexed by:

`stages/stage33/HISTORY.md`

and retained in the relevant `33-05/` / `33-12/` result, audit, certificate, verifier, and Git history.

Do not delete failed/revoked evidence merely to simplify navigation, and do not resurrect retired credit because an older file name matches the current object.
