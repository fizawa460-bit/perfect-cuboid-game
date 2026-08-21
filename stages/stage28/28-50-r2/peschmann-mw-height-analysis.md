# Stage28-50-r2 — Peschmann Mordell-Weil height/count rematch

```text
ROUTE=L11_PESCHMANN_MW_HEIGHT_COUNT
STATUS=NEGATIVE_CERTIFICATE_WITH_PRECISE_RECEIVER
SOURCE=arXiv:2605.00573
TARGET=M3
```

Peschmann 2026 constructs a very large set of Euler bricks by an elliptic fibration over coprime `(m,n)`.  For a fixed base pair the Master-Hit quartic is transformed to an elliptic curve `E_{m,n}`, bounded Mordell-Weil combinations are enumerated, and points satisfying the required square-lift condition are certified exactly.

The finite output is substantial:

```text
MW_ACTIVE_FIBRES=411
MW_GENERATED_MASTER_HITS=1,222,841
TOTAL_EXTENDED_DATABASE=1,284,670
```

but this is not a bounded-physical-height counting theorem.  In particular, the paper records outputs of enormous height (including parameter sizes around `10^888`) and explicitly identifies a uniform height/discriminant estimate on `E_{m,n}` as a missing ingredient in its open-question discussion.

For Stage28 checkpoint50, two distinct uniformities would be required before the Mordell-Weil generator could improve `M3(B)`:

1. **base-height uniformity:** relate the physical Euclidean height `R` of a generated brick to `(m,n)` and the canonical/naive height of the elliptic point, uniformly as the base varies;
2. **square-lift counting uniformity:** count Mordell-Weil points whose rational function `tau(P)` is a positive rational square, uniformly over the moving family.

A fixed positive-rank elliptic fibre by itself gives at most polylogarithmic growth in a canonical-height ball; it does not automatically add a new polynomial power of `B`.  The observed huge number of finite generated records therefore cannot be converted into `kappa/h>1/3` without these moving-family height and lift-count estimates.

The precise future receiver is

```text
RECEIVER=UniformMovingEllipticFibreSquareLiftHeightCount
BASE=(m,n) coprime opposite-parity Master-Hit base
POINTS=P in E_{m,n}(Q) with tau(P) in Q_{>0}^square
MEASURE=primitive canonical physical Euler cuboids under R<=B
REQUIRED_STRENGTH=produce M3(B)>>B^(1/3+delta) for some delta>0, or another strict lower comparison against N2
```

This is genuinely narrower than “use Mordell-Weil constructions.”

```text
PESCHMANN_FINITE_DATABASE_ASYMPTOTIC_PROMOTION=false
PESCHMANN_MW_MATCHED_HEIGHT_POWER_LOWER=false
MOVING_FAMILY_HEIGHT_UNIFORMITY_PROVED=false
SQUARE_LIFT_COUNT_UNIFORMITY_PROVED=false
M3_EXPONENT_IMPROVED_BY_MW_ROUTE=false
AUDIT_REQUIRED=true
```
