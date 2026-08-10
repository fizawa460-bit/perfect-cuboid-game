# Stage14 toolbox — quantifier mismatch and invalid-shortcut atlas

## 1. Quantifier ladder

Use the following levels as distinct objects unless a proved transfer theorem is cited:

```text
local state
  -> rational/global witness
  -> integral witness coordinate
  -> fixed signed packet
  -> fixed curve/fiber
  -> physical edge
  -> active direction/base
  -> restricted sector
  -> whole physical family
```

A theorem at one level does not automatically propagate upward.

## 2. Ten recurring invalid shortcuts

1. **Coordinate density -> packet existence.** A congruence-line saving for coordinates does not count packets that merely possess one coordinate witness.
2. **Local -> global.** Local admissibility is necessary, not a rational-point theorem.
3. **Necessary physical-image equation -> converse.** An equation inherited from a physical edge is not sufficient unless reconstruction and cutoff are proved.
4. **Fixed genus-one curve -> moving family.** A `B^o(1)` point bound on each fixed curve needs a family count, height transfer, and recovery multiplicity.
5. **Sector exponent -> whole-family exponent.** A strong bound on one branch changes the global exponent only after every complementary branch is controlled.
6. **Large structural parameter -> saving.** `q>=B^eta`, `D>=B^eta`, or a forced large variable is not itself a count reduction.
7. **Deterministic divisor allocation -> random signs.** Physical root signs encoded by gcd cells do not carry a free `2^{-omega}` density.
8. **Automatic square factor -> fresh sieve factor.** A gcd cell already extracted as a square factor cannot be charged again as `1/q` without a new condition.
9. **Fixed-fiber sparsity -> active-direction sparsity.** `B^o(1)` partners per direction leaves the number of active directions as the power-scale problem.
10. **Historical threshold -> current gap.** Thresholds frozen against `41/42` remain historically correct but must not be relabeled as the current missing whole-family saving after later improvements.

## 3. Safe transfer checklist

Before promoting a statement, name:

```text
SOURCE LEVEL
TARGET LEVEL
MAP / RECONSTRUCTION
MULTIPLICITY
HEIGHT / CUTOFF
COMPLEMENTARY SECTORS
CURRENT EXPONENT LEDGER
```

If any required field is absent, keep the statement at its source level.

## 4. Quick examples

```text
N_q(U,V) << UV/q + ...
```
is a coordinate incidence estimate; it is not by itself a packet-existence estimate.

```text
C_sigma is smooth genus one
```
is a geometry statement; it is not by itself a moving-family count.

```text
Q*K=X2/kappa
```
is an exact identity; it is not by itself a density theorem.

```text
q--*q-+*q+-*q++=X2_good
```
is deterministic factorization; it is not a probabilistic sign model.

```text
fixed F2 has B^o(1) partners
```
reduces edge counting to active-direction counting; it does not prove that active directions are sparse.

## 5. Canonical warning cards

```text
TB-WARNING-quantifier-ladder
TB-WARNING-local-to-global-shortcut
TB-WARNING-necessary-sufficient-physical-image
TB-WARNING-fixed-object-moving-family
TB-WARNING-sector-to-whole-family
TB-WARNING-structural-size-to-saving
TB-WARNING-deterministic-allocation-not-random
TB-WARNING-automatic-square-factor-double-count
TB-WARNING-fixed-fiber-active-direction
TB-WARNING-stale-threshold-current-ledger
```
