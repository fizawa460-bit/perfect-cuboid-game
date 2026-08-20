# Stage27-60a — roadmap causal decomposition: transition ledger

```text
TASK_ID=Stage27-60a
CHECKPOINT=60
PARENT_ROADMAP=docs/stage16-28-population-roadmap.md
ROADMAP_TRANSITION=Stage16 -> Stage20
ROUTE_KIND=CAUSAL_DECOMPOSITION
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

The Stage16-28 roadmap defines Stage27 as the total transition from exactly one
integral face diagonal to Euler cuboids:

```text
Stage16: M1 = exactly one integral face diagonal
Stage18: M2 = exactly two integral face diagonals
Stage20: M3 = exactly three integral face diagonals
```

All three use the common primitive/canonical physical cutoff `R<=B`.  No integral
space diagonal is part of the Stage27 source or target contract.

The audited adjacent population laws available to Stage27 are

\[
M_1(B)\sim \frac{3}{4\pi^2}B^2\log B,
\qquad
M_2(B)\sim C_{M_2}B(\log B)^5,
\]

and the current Stage20/26 Euler-cuboid envelope

\[
B^{1/3-\varepsilon}\ll_\varepsilon M_3(B)
\ll_\eta B(\log B)^{5-\eta}
\qquad (0<\eta<1/46).
\]

Hence the total Stage27 population-size ratio factors algebraically as

\[
\boxed{\frac{M_3}{M_1}
=\frac{M_2}{M_1}\frac{M_3}{M_2}}.
\]

This identity is only a decomposition of matched population sizes.  The strata
`M1`, `M2`, and `M3` are disjoint exact-face populations, so it must not be called
an objectwise survival chain or a proof that the two arithmetic mechanisms are
independent.

Stage22 gives the first factor sharply:

\[
\boxed{\frac{M_2}{M_1}
\sim \frac{4\pi^2C_{M_2}}3\frac{(\log B)^4}{B}}.
\]

Stage26 gives for the second factor

\[
\frac{M_3}{M_2}\to0,
\]

with the certified corridor, for fixed `epsilon>0` and `0<delta<1/46`,

\[
B^{-2/3-\varepsilon}(\log B)^{-5}
\ll_\varepsilon \frac{M_3}{M_2}
=o((\log B)^{-\delta}).
\]

Therefore Stage27 already has a rigorous two-step causal ledger:

```text
FIRST_ADDED_CONDITION=second integral face diagonal
FIRST_STEP_POLYNOMIAL_LOSS=B^-1
FIRST_STEP_LOG_COMPENSATION=(log B)^4
SECOND_ADDED_CONDITION=third integral face diagonal
SECOND_STEP_ZERO_DENSITY=true
SECOND_STEP_TRUE_POLYNOMIAL_COST=UNKNOWN
```

The next checkpoint60 task is to identify which arithmetic structures pay these
losses and to firewall common interfaces, space-diagonal effects, and repeated
versions of the same restriction from being charged twice.

```text
ROADMAP_CHECKPOINT60_ROLE=CAUSAL_DECOMPOSITION
TOTAL_RATIO_FACTOR_LEDGER_PROVED=true
LITERAL_SUBSET_CHAIN=false
MECHANISM_INDEPENDENCE_FROM_RATIO_IDENTITY=false
SPACE_DIAGONAL_PART_OF_STAGE27_TARGET=false
NEXT_DERIVED_ROUTE=27-60b
```
