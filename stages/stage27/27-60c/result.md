# Stage27-60c — Stage18 -> Stage19 causal synthesis boundary

```text
TASK_ID=Stage27-60c
CHECKPOINT=60
PARENT=Stage27-60b
PARENT_ROADMAP=docs/stage16-29-population-roadmap.md
CURRENT_STAGE27_SCOPE=Stage18 -> Stage19 reentry refinement
ROUTE_KIND=CAUSAL_DECOMPOSITION_SYNTHESIS_BOUNDARY
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

Checkpoint60 now answers the roadmap question "why does the population decrease?"
for the present Stage27 Stage18 -> Stage19 campaign without pretending that the
true exponent is known.

## Certified causal decomposition

The Stage18 source is the shared-edge double-Pythagorean exactly-two-face host.
Stage19 adds exactly one new arithmetic predicate: the space diagonal must be
integral.  That predicate admits several useful but non-independent descriptions:

- a square condition `w^2=a^2+b^2+c^2`;
- a degree-two space-square cover of the two-face host;
- paired-Gaussian/squareclass compatibility;
- local split-prime valuation-parity restrictions.

These descriptions explain qualitative rarity and furnish attack coordinates, but
they are not separate probabilities.  The audited upper/lower state is

\[
\boxed{B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}},
\qquad
N_2(B)=o(M_2(B)).
\]

The r5--r7/r402 reentry establishes that several tempting extra charges are
illusory or currently insufficient: fixed-`R` fiber sparsity, `kappa` factor
packets, recycled squareclass collisions, and fixed-core multiplicity reduction do
not by themselves yield a new whole-family fixed-power saving.  The missing upper
input is a genuinely global same-measure support/correlation theorem.

The r8--r10 lower reentry shows that the quarter-power construction is not known to
be optimal.  Low-height cross-cancellation, a `rho/h>1/4` thick family, a
Saunderson space-lift family, and a moving Peschmann/Master-Hit square-lift section
were all tested without producing a denser proved family.

Therefore the current causal status is:

```text
ADDED_CONDITION=integral space diagonal on the exactly-two-face host
GLOBAL_ZERO_DENSITY_CAUSE=GENUINE_SPACE_SQUARE_RESTRICTION
GEOMETRIC_RARITY=PROVED
LOCAL_ARITHMETIC_RARITY=PROVED
CURRENT_QUANTITATIVE_UPPER_EXPONENT=1/2_PLUS_EPSILON
CURRENT_CONSTRUCTIVE_LOWER_EXPONENT=1/4
HALF_POWER_INTRINSIC_PROVED=false
QUARTER_POWER_INTRINSIC_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
```

## Interaction status

Stage16S/Stage21 show that an integral space diagonal has intrinsic ambient
polynomial cost `B^-1`, with a positive logarithmic interaction after one-face
conditioning.  For the two-face host, the present Stage19 corridor still does not
resolve whether the space-diagonal condition is polynomially stronger or weaker
than that ambient baseline.  Hence the global interaction sign remains open.

This comparison is explanatory context only; its ambient `B^-1` cost is not
multiplied into the Stage19 theorem as a second charge.

```text
AMBIENT_SPACE_COST_COMPARISON_AVAILABLE=true
TWO_FACE_INTERACTION_SIGN_RESOLVED=false
AMBIENT_COST_DOUBLE_CHARGED=false
```

## Checkpoint60 closure

Checkpoint60 is complete as a causal ledger even though the true exponent remains
open.  The roadmap permits an explicit `OPEN_GATE` when the missing theorem is
identified.

```text
CHECKPOINT60_CAUSAL_DECOMPOSITION_COMPLETE=true
DOUBLE_CHARGE_CHECK=PASS
OPEN_GATE_UPPER=SAME_MEASURE_GLOBAL_SUPPORT_OR_CORRELATION_THEOREM
OPEN_GATE_LOWER=DENSER_STAGE19_COMPATIBLE_CONSTRUCTION
OPEN_GATE_INTERACTION=TWO_FACE_SPACE_DIAGONAL_INTERACTION_SIGN
STAGE19_REENTRY_STATUS=FROZEN_UNTIL_GENUINELY_NEW_INPUT
ADVANCE_TO_CHECKPOINT70=false
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=Stage27-60-audit
POST_AUDIT_NEXT_ROUTE=Stage27-70-main-batch
```

`ADVANCE_TO_CHECKPOINT70=false` is a pre-audit lifecycle flag only.  A fresh PASS
audit may set advancement to checkpoint70 without requiring the open mathematical
gates above to be solved; those gates are legitimate roadmap `OPEN_GATE` results.
