# Stage29-02 — joint-cover field-of-definition audit adapter

```text
ROLE=AUDIT_REPAIR_ADAPTER
STATUS=AUDITED_PASS
PARENT=Stage29-02
```

The Stage29-02 submission correctly identifies the two independent quadratic completion radicands and their V4 compositum, but its screening prose used `K=Qbar(Y)` and then immediately stated an arithmetic rational-lift criterion. Those are two different layers and must be separated.

## Arithmetic and geometric function fields

Let

\[
K_{\mathbf Q}=\mathbf Q(Y),\qquad K_{\rm geom}=\overline{\mathbf Q}(Y),
\]

with

\[
f=t_1^2+t_2^2,\qquad g=1+t_1^2+t_2^2.
\]

The completion covers are defined over `Q`:

\[
K_{\mathbf Q}(\sqrt f),\qquad K_{\mathbf Q}(\sqrt g).
\]

Stage28 proves the two squareclasses remain distinct after base change to `K_geom`. Therefore they are already distinct over `K_Q`, and

\[
[K_{\mathbf Q}(\sqrt f,\sqrt g):K_{\mathbf Q}]=4,
\]

with generic Galois group `(Z/2)^2`. After base change to `Qbar` the same degree-four V4 statement holds geometrically.

The third quadratic quotient is defined over `Q` as well:

\[
K_{\mathbf Q}(\sqrt{fg}).
\]

## Correct endpoint lift semantics

For any field `F` of characteristic not two and any `F`-rational base point away from the branch/pole loci, an **F-rational** lift to the joint cover exists exactly when both `f` and `g` are squares in `F`. Thus over `F=Q` this is the simultaneous third-face plus space-diagonal completion criterion on the common two-face host, subject to the separate primitive/canonical/height adapters.

Over `Qbar`, by contrast, nonzero values always acquire square roots. Geometric lifting over `Qbar` is therefore not itself an arithmetic endpoint criterion; `K_geom` is used for geometric irreducibility, branch-component genus, and divisor-class calculations.

```text
ARITHMETIC_FIELD=Q(Y)
GEOMETRIC_FIELD=Qbar(Y)
V4_DEGREE_OVER_Q=4
V4_DEGREE_AFTER_GEOMETRIC_BASE_CHANGE=4
RATIONAL_LIFT_CRITERION=FIELD_RELATIVE
QBAR_GEOMETRIC_LIFT_IS_NOT_ENDPOINT_ARITHMETIC_CRITERION=true
```

## Cross branch support

The geometric branch analysis remains unchanged. Stage28 gives disjoint reduced geometric supports with profiles `4 x genus0` and `2 x genus1`; hence the cross radicand has geometric odd support equal to their union and class `-4K_Y`. The formal normal-double-cover canonical signal is `pi^*(-K_Y)`, while minimal-resolution/Kodaira-type claims remain deferred.

This adapter changes no V4/cross-quotient conclusion. It only makes the field of definition and rational-point quantifier explicit.