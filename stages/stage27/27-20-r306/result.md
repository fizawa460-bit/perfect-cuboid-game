# Stage27-20-r306 — new upper receiver search after r303-r305 gates

```text
TASK_ID=Stage27-20-r306
ROUTE_KIND=UPPER_RECEIVER_SEARCH
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
R302_STATE=FROZEN
R303_STATE=THEOREM_GATE_PAUSED
R304_STATE=PAUSED_PENDING_NEW_EXACT_IDENTITY
R305_STATE=THEOREM_ADAPTER_GATE_PAUSED
```

## Search boundary

Do not reopen the known gates by renaming them. A new Stage27-20 receiver is admissible only if it changes at least one of:

- charged measure;
- structural invariant;
- modulus family length;
- coefficient separation profile;
- support variable;
- large-core/low-core dichotomy;
- theorem species that can legally attach.

## Remaining StructureRadar directions worth testing

1. **Large-core forcing / low-core sparsity** on the fixed wall slab. This is the unresolved intrinsic wall alternative from `27-40ac` and is independent of the r302 operator formulation if it can be proved directly on physical packet support.
2. **Divisor-window geometry** (`SR-STR-170/171`) only if a new bounded-distortion adapter from the physical reciprocal/unitary divisor window is derived. Ambient Ford-type density is not enough.
3. **Structured-selector decomposition** (`SR-STR-167`) only if Stage27 produces an explicit `B^{o(1)}`-complexity multiplicative/Hecke decomposition of the actual selector.
4. **Gaussian norm-ratio collision** (`SR-STR-168`) only if the Stage27 receiver exposes a polynomial-length modulus/sample family or same-measure weighted collision theorem.
5. **Geometry/descent** is lower priority for this Stage27-20 upper roadmap unless it yields a moving-family sparsity theorem directly on the wall/support population.

## First target

The cleanest next target is the intrinsic wall dichotomy:

`MAINWallLargeCoreForcingOrLowCoreSparsity`.

Prove either that all half-power-saturating physical wall mass carries a charged core/modulus at least `B^delta`, or that the complementary low-core wall population has mass `<<B^(1/2-delta+o(1))`.

This bypasses r302 if obtained directly from packet support/arithmetic geometry rather than from the frozen same-measure Fourier collision theorem.

```text
NEW_RECEIVER_SEARCH_OPENED=true
FIRST_NEW_RECEIVER=MAINWallLargeCoreForcingOrLowCoreSparsity
STRICT_SUB_SQRT_UPPER_PROVED=false
NEXT_DERIVED_ROUTE=27-20-r306a
```
