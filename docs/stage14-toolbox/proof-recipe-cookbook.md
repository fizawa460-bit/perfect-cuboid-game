# Stage14 proof recipe cookbook

This cookbook turns the Stage14 toolbox dependency map into an operational checklist for `14-4` main and `s` work. It records what later stages may legally reuse, where each estimate lives in the quantifier ladder, and where an external theorem contract is required.

## 0. Universal preflight

```text
[ ] SOURCE: every theorem input is merged
[ ] STATUS: PROVED / CONDITIONAL / HEURISTIC is explicit
[ ] INPUT LEVEL: L0..L8 is named
[ ] COUNTED UNIVERSE is named
[ ] CONDITIONING: every fixed packet/direction/coefficient/modulus/sector is named
[ ] SCALE: M-scale and B-scale are not mixed
[ ] TRANSFER: any skipped receiver level has a merged transfer theorem
[ ] COMPLEMENT: sector promotion waits for complementary sectors to close
[ ] OUTPUT LEVEL is stated
[ ] CURRENT LEDGER: terminal CURRENT ledger card is read before exponent claims
```

If an external theorem is used, also complete `external-theorem-import-checklist-template.md`.

## 1. Recipe A — local admissibility to global witness

Input `L0`. Use the five-column local routing, odd local rows, `Q_2` image, and local/global warning cards. Stop at `LOCAL_ADMISSIBLE` unless a merged theorem constructs the global rational witness.

## 2. Recipe B — integral witness to arithmetic or geometry

Input `L2`. Write the integral witness equation, extract the signed kernel packet, and choose either full-radical incidence or fixed-packet genus-one geometry. Coordinate saving is not packet saving; fixed-curve bounds are not moving-family bounds.

## 3. Recipe C — physical compact half-angle routing

Input `L5`. Translate to the compact chamber, form `D_-,D_+,k_-,k_+`, use `QK=X2/kappa`, and route good odd primes through the deterministic gcd cells. Do not replace this by Bernoulli root-sign heuristics.

## 4. Recipe D — fixed fiber to active direction

Use a fixed-fiber `B^o(1)` partner bound only after freezing exactly the theorem variables. Then separately count active directions. Stop if active-direction sparsity has not been proved.

## 5. Recipe E — historical one-cell shared-xi sieve

Status: **PROVED HISTORICAL ARCHITECTURE**.

```text
a=r*s
b=t*j
c=r*t
d=s*j
xi=r*s*t*j
```

Merged s7-08 / 4bw give one selected-cell relative saving `T^(-1/2)` and the historical whole-family checkpoint `18/19`. This recipe remains a valid component but is not the current global ceiling.

## 6. Recipe F — proved 4bx thick reoptimization

Status: **PROVED REUSABLE COMPONENT / HISTORICAL GLOBAL CHECKPOINT**.

Merged 4bx proves

```text
L=H^(4/5)
N_packet << M*H^(-4/5) B^o(1)
```

and, before the two-cell theorem was closed, the whole-family checkpoint `15/16`. The `H^(-4/5)` packet theorem remains an input to the current architecture even though `15/16` is superseded.

## 7. Recipe G — proved adjacent two-cell mixed transform

Status: **PROVED CURRENT ARCHITECTURE**.

The universal detector is

```text
H(R,S)=(1-R^2*S^2)(S^2-R^2)
      =(1-RS)(1+RS)(S-R)(S+R).
```

Merged s7-10 and 4by independently prove, through different external-theorem contracts,

```text
|T_p(h,k)| << p
```

for all required good inert primes and additive frequencies. Hence

```text
N_2cell(R,S) << (RS)^(2/3) B^o(1)
relative saving = (RS)^(-1/3).
```

Combined with the proved 4bx thick input, the exact minimax is

```text
lambda=13/28
nu=11/28
tau=5/56
V(B) << B^(13/14+o(1)).
```

Current ledger:

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=13/14
CURRENT_REMAINING_GAP_TO_SQRT=3/7
```

Merged 4bz / s7-11 show threshold retuning or naive 3-/4-cell enlargement does not improve this square-sieve architecture.

## 8. External theorem import recipe

Status: **MANDATORY FOR LITERATURE INPUTS**.

Use:

```text
external-theorem-import-contract.md
external-theorem-import-checklist-template.md
TB-DICTIONARY-external-theorem-import-status
TB-RECIPE-external-theorem-import-preflight
TB-WARNING-theorem-name-match-not-hypothesis-match
TB-WARNING-rejected-shortcut-must-stay-rejected
TB-WARNING-finite-regression-not-theorem-import
```

State transition:

```text
CANDIDATE -> HYPOTHESIS_MAPPED -> IMPORTED
                             \-> REJECTED
```

For s7-10/4by the live examples are:

```text
Katz 2007 direct nonsingular-polynomial shortcut -> REJECTED
Katz--Laumon stationary-phase specialization     -> IMPORTED
Lei Fu Corollary 0.3 specialization              -> IMPORTED
```

An imported complete-sum theorem still needs the explicit transfer chain:

```text
complete sum -> CRT -> completion -> sieve -> packet/fiber -> sector -> whole family.
```

## 9. Receiver-composition checklist

Before combining two savings:

```text
[ ] SAME UNIVERSE
[ ] SAME CONDITIONING
[ ] LEGAL QUANTIFIER TRANSFER
[ ] EXHAUSTIVE RECOMBINATION
```

If one gate is false, do not multiply savings or promote the exponent.

## 10. New-result maintenance checklist

```text
[ ] verify merged=true and record merge SHA
[ ] classify theorem / conditional / rejected import
[ ] identify receiver input/output levels
[ ] determine whether a CURRENT ledger is superseded
[ ] preserve old cards and add SUPERSEDED_BY
[ ] recompute exact fractions
[ ] update current ledger only for a proved exhaustive whole-family theorem
[ ] record external theorem locator and full hypothesis map when applicable
[ ] keep finite regression separate from theorem proof
[ ] rerun toolbox regression suite
```

## 11. Current boundary at toolbox-am

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=13/14
CURRENT_REMAINING_GAP_TO_SQRT=3/7
CURRENT_SQUARE_ROOT_SQUARE_SIEVE_ARCHITECTURE_BARRIER=13/14
HISTORICAL_4BX_WHOLE_FAMILY_EXPONENT=15/16
HISTORICAL_S7_09_CONDITIONAL_TARGET=16/17
HISTORICAL_4BX_CONDITIONAL_TARGET=13/14
ADJACENT_TWO_CELL_MIXED_FOURIER_OP_BOUND_PROVED=true
SQRT_B_UPPER_BOUND_PROVED=false
```
