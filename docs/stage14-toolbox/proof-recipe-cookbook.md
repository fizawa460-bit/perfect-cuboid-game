# Stage14 proof recipe cookbook

This cookbook turns the Stage14 toolbox dependency map into an operational checklist for `14-4` main and `s` work.

The cookbook does not create a theorem. It tells a later stage what it may legally reuse, which quantifier level it is at, when it must stop, and what theorem would be required to continue.

## 0. Universal preflight

Before using any recipe, record all of the following.

```text
[ ] SOURCE: every theorem input is merged
[ ] STATUS: PROVED / CONDITIONAL / HEURISTIC is explicit
[ ] INPUT LEVEL: L0..L8 from the proof-receiver map is named
[ ] COUNTED UNIVERSE: coordinates / packets / fibers / directions / sector / whole family
[ ] CONDITIONING: every fixed packet, direction, coefficient, modulus, or sector is named
[ ] SCALE: M-scale and physical B-scale are not mixed
[ ] TRANSFER: any skipped receiver level has a merged transfer theorem
[ ] COMPLEMENT: a sector claim is promoted globally only after complementary sectors close
[ ] OUTPUT LEVEL: the exact receiver level reached is stated
[ ] CURRENT LEDGER: current whole-family exponent is read from the terminal CURRENT ledger card
```

If any box is unknown, stop at the current level. Do not infer the missing transfer.

## 1. Recipe A — local admissibility to global witness

Input: `L0 local state`.

Use:

```text
TB-DICTIONARY-five-column-local-routing
TB-RECIPE-full-local-character-check
TB-WARNING-local-to-global-shortcut
TB-RECIPE-dispatch-local-to-global-witness
```

Procedure:

1. Normalize the Euclid orientation and five columns.
2. Check all odd selected/unselected local rows.
3. Check the `Q_2` eight-state image.
4. Record only `LOCAL_ADMISSIBLE`.
5. Continue to `L1` only if a separate merged global-witness theorem constructs the rational point.

Stop condition:

```text
local admissible but no global witness theorem
```

Output: `L0`, or `L1` only through explicit global construction.

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
```

Procedure:

1. Write `Y^2=G0*G1*G2` with the exact three factor differences.
2. Extract the signed squarefree edge packet.
3. Decide whether the useful receiver is full-radical incidence or fixed-packet geometry.
4. If using incidence, keep coordinate density separate from packet existence.
5. If using genus-one geometry, keep the packet fixed unless a moving-family transfer is supplied.

Stop conditions:

```text
coordinate saving without packet/base transfer
fixed-curve point bound without moving-family transfer
```

Output: usually `L3` or `L4`, not automatically `L6-L8`.

## 3. Recipe C — physical compact half-angle routing

Input: `L5 physical edge/pair`.

Use:

```text
TB-FORMULA-compact-t0-torsion-translation
TB-FORMULA-dual-compact-half-angle-selectors
TB-FORMULA-dual-denominator-cancellation-product
TB-DICTIONARY-dual-selector-gcd-matrix
TB-RECIPE-compact-half-angle-prime-routing
TB-WARNING-compact-selector-quantifier-boundary
```

Procedure:

1. Translate the physical point into the compact chamber.
2. Form the two selectors `D_-`, `D_+` and cancellation cofactors `k_-`, `k_+`.
3. Use `Q=D_+D_-`, `K=k_+k_-`, `QK=X2/kappa`.
4. Route good odd primes deterministically into the four gcd cells.
5. Do not assign independent Bernoulli probabilities to root signs.

Output: structured physical arithmetic at `L5`; a count improvement requires a later incidence/count receiver.

## 4. Recipe D — fixed fiber to active direction

Input: `L4 fixed curve/fiber` with a proved `B^o(1)` partner bound.

Use:

```text
TB-RECIPE-dispatch-fixed-fiber-active-direction
TB-WARNING-fixed-fiber-active-direction
TB-WARNING-fixed-object-moving-family
```

Procedure:

1. Freeze exactly the coordinates required by the fixed-fiber theorem.
2. Record the partner multiplicity as a fiber statement only.
3. Identify the remaining active direction/base family.
4. Supply an independent count for active directions before multiplying by fiber multiplicity.

Stop condition:

```text
B^o(1) partners per direction, but no bound for number of active directions
```

Output: a legal handoff from `L4` toward `L6`, not a global saving by itself.

## 5. Recipe E — proved one-cell adaptive sieve

Status: **PROVED**.

Merged canonical source: Stage14-s7-08. Main-track independent corroboration: Stage14-4bw.

Input: product-square / same-kernel hard sector at `L7` after the balanced/small-coordinate decompositions.

Use:

```text
TB-RECIPE-dispatch-balanced-inert-square-sieve
TB-RECIPE-dispatch-shared-xi-cell-switch
TB-WARNING-proof-receiver-composition-boundary
TB-LEDGER-current-whole-family-after-s7-08
```

Core exact structure:

```text
ab=cd=xi

a=r*s
b=t*j
c=r*t
d=s*j
xi=r*s*t*j
```

For a selected cell `q~T`, the nondegenerate quartic square sieve gives

```text
#solutions << T^(1/2) B^o(1)
```

with relative saving `T^(-1/2)`.

The exhaustive optimized thresholds are

```text
lambda=9/19
tau=2/19
theta=8/19
```

and the proved whole-family result is

```text
V(B) << B^(18/19+o(1)).
```

Current square-root gap:

```text
18/19 - 1/2 = 17/38.
```

## 6. Recipe F — adjacent two-cell mixed-character research gate

Status: **CONDITIONAL RESEARCH RECIPE**.

Merged source Stage14-s7-09 proves the algebraic normalization and complete inert trace, but does **not** prove the required uniform nonzero-frequency mixed Fourier estimate.

Exact universal polynomial:

```text
H(R,S)=(1-R^2*S^2)*(S^2-R^2).
```

Proved inputs:

```text
no repeated component in characteristic != 2
complete 2D inert quadratic-character trace = 0
sequential one-cell savings do not automatically multiply
```

Missing theorem gate:

```text
uniform good-inert-prime bound |T_p(h,k)| << p
for all required nonzero additive frequencies
```

Only if that theorem is proved with the correct uniformity may the proposed two-cell square-sieve receiver be activated.

Conditional consequences recorded by s7-09:

```text
N_2cell(R,S) << (R*S)^(2/3) B^o(1)
conditional optimized exponent = 16/17
```

These are not current theorem values. The current whole-family exponent remains `18/19`.

## 7. Receiver-composition checklist

Before combining two savings, answer yes to all four gates.

```text
[ ] SAME UNIVERSE: both estimates count the same surviving objects
[ ] SAME CONDITIONING: fixed/free variables are compatible
[ ] LEGAL QUANTIFIER TRANSFER: no coordinate/fiber/sector level is skipped
[ ] EXHAUSTIVE RECOMBINATION: complementary sectors are bounded
```

If one gate is false, do not multiply savings or promote the exponent.

## 8. New-result maintenance checklist

When a new main/s stage merges:

```text
[ ] verify merged=true and record merge SHA
[ ] classify theorem vs conditional gate
[ ] identify receiver input/output levels
[ ] determine whether it supersedes a CURRENT card
[ ] preserve the superseded card and add SUPERSEDED_BY
[ ] recompute exponent arithmetic with exact fractions
[ ] update the current ledger only for a proved exhaustive whole-family theorem
[ ] add warnings for any newly exposed invalid shortcut
[ ] rerun the latest toolbox regression suite
```

## 9. Current boundary at toolbox-al

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=18/19
CURRENT_REMAINING_GAP_TO_SQRT=17/38
S7_09_CONDITIONAL_WHOLE_FAMILY_EXPONENT=16/17
S7_09_MIXED_FOURIER_OP_BOUND_PROVED=false
```

The `16/17` line is a research target under an explicit missing theorem, not a current bound.
