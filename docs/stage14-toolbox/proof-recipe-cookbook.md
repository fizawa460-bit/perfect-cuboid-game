# Stage14 proof recipe cookbook

This cookbook turns the Stage14 toolbox dependency map into an operational checklist for `14-4` main and `s` work. It records what later stages may legally reuse, where each estimate lives in the quantifier ladder, and where an external theorem contract is required.

## 0. Universal preflight

```text
[ ] SOURCE: every theorem input is merged
[ ] STATUS: PROVED / CONDITIONAL / HEURISTIC is explicit
[ ] INPUT LEVEL: L0..L8 is named
[ ] COUNTED UNIVERSE is named
[ ] CONDITIONING is named
[ ] SCALE: M-scale and B-scale are not mixed
[ ] TRANSFER: any skipped receiver level has a merged theorem
[ ] COMPLEMENT: sector promotion waits for complementary sectors
[ ] OUTPUT LEVEL is stated
[ ] CURRENT LEDGER: terminal CURRENT ledger is read before exponent claims
```

If an external theorem is used, also complete `external-theorem-import-checklist-template.md`.

## 1. Recipe A — local admissibility to global witness

Input `L0`. Use the five-column local routing, odd local rows, `Q_2` image, and local/global warning cards. Stop at `LOCAL_ADMISSIBLE` unless a merged theorem constructs the global rational witness.

## 2. Recipe B — integral witness to arithmetic or geometry

Input `L2`. Write the integral witness equation, extract the signed kernel packet, and choose full-radical incidence or fixed-packet genus-one geometry. Coordinate saving is not packet saving; fixed-curve bounds are not moving-family bounds.

## 3. Recipe C — physical compact half-angle routing

Input `L5`. Translate to the compact chamber, form `D_-,D_+,k_-,k_+`, use `QK=X2/kappa`, and route good odd primes through deterministic gcd cells.

## 4. Recipe D — fixed fiber to active direction

Use a fixed-fiber `B^o(1)` partner bound only after freezing exactly the theorem variables. Then separately count active directions. Stop if active-direction sparsity has not been proved.

## 5. Recipe E — historical one-cell shared-xi sieve

Status: **PROVED HISTORICAL ARCHITECTURE**.

Merged s7-08 / 4bw give one selected-cell relative saving `T^(-1/2)` and the historical whole-family checkpoint `18/19`. This remains a valid component.

## 6. Recipe F — proved 4bx thick reoptimization

Status: **PROVED REUSABLE COMPONENT / HISTORICAL GLOBAL CHECKPOINT**.

```text
L=H^(4/5)
N_packet << M*H^(-4/5) B^o(1)
```

The packet theorem remains live; the historical global checkpoint was `15/16`.

## 7. Recipe G — proved adjacent two-cell mixed transform

Status: **PROVED REUSABLE RECEIVER / HISTORICAL 13/14 GLOBAL CHECKPOINT**.

Universal detector:

```text
H(R,S)=(1-R^2*S^2)(S^2-R^2).
```

Merged s7-10 and 4by independently prove through different external-theorem contracts

```text
|T_p(h,k)| << p
N_2cell(R,S) << (RS)^(2/3) B^o(1)
relative saving=(RS)^(-1/3).
```

Together with the 4bx thick input this gave the historical checkpoint

```text
lambda=13/28
nu=11/28
tau=5/56
V(B) << B^(13/14+o(1)).
```

The two-cell theorem remains a current reusable receiver even though `13/14` is no longer the terminal global exponent.

## 8. Recipe H — current full-coordinate common refinement

Status: **PROVED CURRENT ARCHITECTURE**.

Merged s7-13 refines one short reduced coordinate simultaneously:

```text
P~B^p, Q~B^q
P=a*x^2, Q=b*y^2
alpha=p-2s
beta=q-2t
m=max(alpha,beta).
```

On the same common-refinement block it has two valid upper bounds:

```text
coordinate support <= B^(1/2+m+o(1))
two-cell receiver  <= B^(1-m/3+o(1)).
```

Do not multiply them. Use

```text
min(1/2+m, 1-m/3).
```

The exact worst point is `m=3/8`, hence

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
CURRENT_REMAINING_GAP_TO_SQRT=3/8
FULL_COORDINATE_REFINEMENT_ARCHITECTURE_BARRIER=7/8
```

Critical geometry:

```text
P,Q~B^(1/2)
a,b~B^(3/8)
x,y~B^(1/16)
xi=ab~B^(3/4).
```

## 9. External theorem import recipe

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

Live examples:

```text
Katz 2007 direct nonsingular-polynomial shortcut -> REJECTED
Katz--Laumon stationary-phase specialization     -> IMPORTED
Lei Fu Corollary 0.3 specialization              -> IMPORTED
```

An imported complete-sum theorem still needs

```text
complete sum -> CRT -> completion -> sieve -> packet/fiber -> sector -> whole family.
```

## 10. Receiver-composition checklist

```text
[ ] SAME UNIVERSE
[ ] SAME CONDITIONING
[ ] LEGAL QUANTIFIER TRANSFER
[ ] EXHAUSTIVE RECOMBINATION
```

For two bounds on the same common-refinement block, taking a minimum is legal; multiplying them requires a separate theorem proving independent/joint savings.

## 11. New-result maintenance checklist

```text
[ ] verify merged=true and record merge SHA
[ ] classify theorem / conditional / rejected import
[ ] identify receiver input/output levels
[ ] preserve superseded cards and add SUPERSEDED_BY
[ ] recompute exact fractions
[ ] update current ledger only for a proved exhaustive theorem
[ ] record external theorem locator and full hypothesis map
[ ] keep finite regression separate from theorem proof
[ ] rerun toolbox regression suite
```

## 12. Current boundary at toolbox-am

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8
CURRENT_REMAINING_GAP_TO_SQRT=3/8
FULL_COORDINATE_REFINEMENT_ARCHITECTURE_BARRIER=7/8
HISTORICAL_TWO_CELL_GLOBAL_CHECKPOINT=13/14
HISTORICAL_4BX_WHOLE_FAMILY_EXPONENT=15/16
ADJACENT_TWO_CELL_MIXED_FOURIER_OP_BOUND_PROVED=true
SQRT_B_UPPER_BOUND_PROVED=false
```
