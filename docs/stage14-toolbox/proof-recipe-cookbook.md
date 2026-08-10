# Stage14 proof recipe cookbook

This cookbook turns the Stage14 toolbox dependency map into an operational checklist for `14-4` main and `s` work.

The cookbook does not create a theorem. It records what later stages may legally reuse, which quantifier level they occupy, when they must stop, and which missing theorem would be required to continue.

## 0. Universal preflight

```text
[ ] SOURCE: every theorem input is merged
[ ] STATUS: PROVED / CONDITIONAL / HEURISTIC is explicit
[ ] INPUT LEVEL: L0..L8 is named
[ ] COUNTED UNIVERSE: coordinates / packets / fibers / directions / sector / whole family
[ ] CONDITIONING: every fixed packet, direction, coefficient, modulus, or sector is named
[ ] SCALE: M-scale and physical B-scale are not mixed
[ ] TRANSFER: any skipped receiver level has a merged transfer theorem
[ ] COMPLEMENT: sector promotion waits for complementary sectors to close
[ ] OUTPUT LEVEL: exact receiver level reached is stated
[ ] CURRENT LEDGER: terminal CURRENT ledger card is read before exponent claims
```

If any item is unknown, stop at the current receiver level.

## 1. Recipe A — local admissibility to global witness

Input: `L0 local state`.

Use:

```text
TB-DICTIONARY-five-column-local-routing
TB-RECIPE-full-local-character-check
TB-WARNING-local-to-global-shortcut
TB-RECIPE-cookbook-local-global-witness
```

Procedure:

1. Normalize Euclid orientation and five columns.
2. Check all odd selected/unselected local rows.
3. Check the `Q_2` eight-state image.
4. Record only `LOCAL_ADMISSIBLE`.
5. Continue to `L1` only if a merged global theorem constructs the rational witness.

Stop condition:

```text
local admissible but no global witness theorem
```

## 2. Recipe B — integral witness to arithmetic or geometry

Input: `L2 integral witness`.

Use:

```text
TB-FORMULA-integral-witness-equation
TB-LEMMA-witness-pairwise-gcd-support
TB-FORMULA-signed-kernel-edge-packet
TB-LEMMA-full-leg-radical-modulus
TB-RECIPE-radical-incidence-small-D-dichotomy
TB-FORMULA-fixed-packet-two-quadrics
TB-LEMMA-fixed-packet-smooth-genus-one
TB-RECIPE-cookbook-witness-kernel-geometry
```

Procedure:

1. Write `Y^2=G0*G1*G2` with exact factor differences.
2. Extract the signed squarefree edge packet.
3. Choose full-radical incidence or fixed-packet geometry.
4. For incidence, keep coordinate density separate from packet existence.
5. For genus-one geometry, keep the packet fixed unless a moving-family transfer is supplied.

Stop conditions:

```text
coordinate saving without packet/base transfer
fixed-curve point bound without moving-family transfer
```

## 3. Recipe C — physical compact half-angle routing

Input: `L5 physical edge/pair`.

Use:

```text
TB-FORMULA-compact-t0-torsion-translation
TB-FORMULA-dual-compact-half-angle-selectors
TB-FORMULA-dual-denominator-cancellation-product
TB-DICTIONARY-dual-selector-gcd-matrix
TB-RECIPE-cookbook-compact-physical
```

Procedure:

1. Translate into the compact chamber.
2. Form `D_-`, `D_+`, `k_-`, `k_+`.
3. Use `Q=D_+D_-`, `K=k_+k_-`, `QK=X2/kappa`.
4. Route good odd primes deterministically into the four gcd cells.
5. Do not model root signs as independent Bernoulli variables.

## 4. Recipe D — fixed fiber to active direction

Input: `L4 fixed curve/fiber` with controlled partner multiplicity.

Use:

```text
TB-RECIPE-cookbook-fixed-fiber-active-direction
TB-WARNING-fixed-fiber-active-direction
TB-WARNING-fixed-object-moving-family
```

Procedure:

1. Freeze exactly the coordinates required by the fiber theorem.
2. Record partner multiplicity only as a fiber statement.
3. Identify the still-moving active direction/base family.
4. Bound active directions independently before multiplying by fiber multiplicity.

Stop condition:

```text
B^o(1) partners per direction but no active-direction count
```

## 5. Recipe E — proved one-cell shared-xi sieve

Status: **PROVED HISTORICAL ARCHITECTURE**.

Canonical first source: merged s7-08. Independent main rederivation: merged 4bw.

Exact four-cell structure:

```text
a=r*s
b=t*j
c=r*t
d=s*j
xi=r*s*t*j
```

For a selected cell `q~T`, the proved nondegenerate quartic square sieve gives

```text
#solutions << T^(1/2) B^o(1)
```

with relative saving `T^(-1/2)`.

The s7-08/4bw one-cell minimax gives

```text
lambda=9/19
tau=2/19
theta=8/19
V(B) << B^(18/19+o(1)).
```

This remains a valid proved recipe and is the thin-cell ingredient used later by 4bx, but `18/19` is no longer the current whole-family exponent.

## 6. Recipe F — current reoptimized thick sieve plus one-cell thin receiver

Status: **PROVED CURRENT ARCHITECTURE**.

Merged source: Stage14-4bx.

Starting from the merged 4bv packet inequality, 4bx reoptimizes the auxiliary prime scale to

```text
L=H^(4/5)
```

and proves

```text
N_packet << M*H^(-4/5) B^o(1).
```

Thus the thick-sector exponent becomes

```text
1-4*tau/5.
```

Combining this stronger thick receiver with the already-proved one-cell thin receiver gives exact thresholds

```text
lambda=15/32
nu=13/32
tau=5/64
```

and exhaustive sector bounds

```text
small denominator  15/16
small numerator    15/16
thick squarepart   15/16
thin numerator     15/16
thin denominator   59/64
```

Therefore

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=15/16
V(B) << B^(15/16+o(1)).
CURRENT_REMAINING_GAP_TO_SQRT=7/16
```

The exact gain over the former `18/19` current bound is

```text
18/19 - 15/16 = 3/304.
```

## 7. Recipe G — adjacent two-cell mixed-character research gate

Status: **CONDITIONAL RESEARCH RECIPE**.

Merged s7-09 proves the algebraic normalization

```text
H(R,S)=(1-R^2*S^2)*(S^2-R^2)
```

and exact complete inert two-dimensional quadratic-character trace zero, but does not prove the required uniform nonzero-frequency mixed Fourier theorem.

Missing theorem gate:

```text
uniform good-inert-prime bound |T_p(h,k)| << p
for the required nonzero additive frequencies
```

Sequential one-cell savings do not automatically multiply.

Historical s7-09 conditional optimization before the 4bx thick improvement was

```text
16/17.
```

After importing the proved 4bx thick improvement, the updated conditional target is

```text
UPDATED_CONDITIONAL_TWO_CELL_WHOLE_FAMILY_EXPONENT=13/14.
```

This is still conditional because

```text
S7_09_TWO_CELL_MIXED_FOURIER_BOUND_PROVED=false.
```

Neither `16/17` nor `13/14` may replace the current proved `15/16` ledger until the missing theorem and full transfer are proved and merged.

## 8. Receiver-composition checklist

Before combining two savings:

```text
[ ] SAME UNIVERSE: both estimates count the same surviving objects
[ ] SAME CONDITIONING: fixed/free variables are compatible
[ ] LEGAL QUANTIFIER TRANSFER: no coordinate/fiber/sector level is skipped
[ ] EXHAUSTIVE RECOMBINATION: complementary sectors are bounded
```

If one gate is false, do not multiply savings or promote the exponent.

## 9. New-result maintenance checklist

```text
[ ] verify merged=true and record merge SHA
[ ] classify theorem vs conditional gate
[ ] identify receiver input/output levels
[ ] determine whether a CURRENT ledger is superseded
[ ] preserve superseded cards and add SUPERSEDED_BY
[ ] recompute exponent arithmetic with exact fractions
[ ] update current ledger only for a proved exhaustive whole-family theorem
[ ] update conditional target separately when a proved ingredient improves it
[ ] add warnings for newly exposed invalid shortcuts
[ ] rerun latest toolbox regression suite
```

## 10. Current boundary at toolbox-al

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=15/16
CURRENT_REMAINING_GAP_TO_SQRT=7/16
HISTORICAL_ONE_CELL_WHOLE_FAMILY_EXPONENT=18/19
HISTORICAL_S7_09_CONDITIONAL_WHOLE_FAMILY_EXPONENT=16/17
UPDATED_CONDITIONAL_TWO_CELL_WHOLE_FAMILY_EXPONENT=13/14
S7_09_TWO_CELL_MIXED_FOURIER_BOUND_PROVED=false
```
