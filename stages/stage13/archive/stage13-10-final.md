# Stage13-10 final — frozen explanatory snapshot

> **STATUS:** `STAGE13_COMPLETE`
>
> **SCOPE:** frozen task-end provenance snapshot; canonical living mathematics remains `stages/stage13/main.md`

## Final structural answer

Stage13 studies primitive canonical cuboids with integral space diagonal and exactly one integral face diagonal, split into the canonical directions `ab`, `ac`, and `bc`.

At the locked finite cutoff `B=100000`,

```text
exact-one = (84146, 43180, 40704)
ab:ac:bc ~= 2.0673 : 1.0608 : 1
```

so the population looks close to `2:1:1`. The completed asymptotic theorem instead gives

```text
P_inf = (0.5347369332313988,
         0.24535917783225203,
         0.21990388893634913)

ab:ac:bc
 -> 2.431684750178191 : 1.115756428951881 : 1.
```

The explanation is two-scale.

### 1. Geometric backbone

Canonical ordering `0<a<b<c` coupled to the one-face Gelfand--Leray density gives pointwise weights

```text
w_ab > w_ac > w_bc
```

on the canonical spherical chamber. Their chamber integrals `I_ab,I_ac,I_bc` supply the limiting directional vector.

Pure relabelling alone does not create the bias: with uniform weight the chamber gives `1:1:1`, and without the order chamber full coordinate symmetry also gives `1:1:1`.

### 2. Finite arithmetic flattening

At accessible cutoffs, supported-shell richness strongly depresses the geometric `ab` advantage. OE/EE parity strata and pure-`G` components carry opposite `ac-bc` tilts that cancel strongly, while primitive-support reweighting supplies much of the residual finite `ac-bc` gap.

These are finite structural diagnostics, not additional leading asymptotic constants.

The exactly-one sieve is not the source of the near-`2:1:1` shape. At `B=100000`, the raw incidence population is already

```text
(84212, 43236, 40760),
```

and overlap removal changes it only to

```text
(84146, 43180, 40704).
```

### 3. Why the chamber vector survives asymptotically

For each direction `q`,

```text
A_q(B) ~ [kappa I_q/(3 pi^3)] B(log B)^3.
```

The arithmetic factor surviving in the main term is common across directions. After normalization, that common scale cancels and only the chamber integrals remain direction-dependent.

Pair and triple overlaps are `o(B(log B)^3)`, so passing from raw incidence to exactly-one does not change the leading normalized vector.

Therefore

```text
finite near-2:1:1
= a long pre-asymptotic flattening of a stronger chamber bias
```

where the equality sign is explanatory shorthand, not an exact algebraic factorization.

## Scope

Stage13 does not prove an explicit convergence rate, effective threshold, or monotonicity. Therefore it does not justify quantitative closeness to the limiting vector at any specified enormous finite cutoff without further effective estimates.

Stage13 also does not settle perfect-cuboid existence. The triple-overlap population is lower order, but lower-order does not mean empty.

## Completion

```text
STAGE13_10=COMPLETE_FINAL_EXPLANATION
STAGE13=COMPLETE
FINITE_NEAR_2_1_1_EXPLAINED=true
ASYMPTOTIC_DIRECTION_IS_ARCHIMEDEAN_CHAMBER_VECTOR=true
PERFECT_CUBOID_EXISTENCE_RESOLVED=false
EXPLICIT_CONVERGENCE_RATE_PROVED=false
INDEPENDENT_PUBLICATION_REVIEW_COMPLETED=false
NEXT_STAGE13_TASK=NONE
```
