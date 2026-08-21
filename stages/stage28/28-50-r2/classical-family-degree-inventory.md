# Stage28-50-r2 — classical polynomial-family efficiency inventory

```text
ROUTE=L9_CLASSICAL_POLYNOMIAL_FAMILY_INVENTORY
STATUS=NEGATIVE_CERTIFICATE_WITH_REUSE
TARGET=M3
```

Checkpoint50-r2 rematches the classical closed-form Euler-brick families against the exact primitive/canonical Euclidean-height lower-bound question.

## Saunderson

The audited project family has Pythagorean input

\[
u=r^2-s^2,\quad v=2rs,\quad w=r^2+s^2
\]

and Euler-brick edges cubic in `(u,v,w)`, hence homogeneous degree `6` in `(r,s)`.  Primitive Euclid inputs have quadratic parameter count.  This is the current efficiency

```text
PARAMETER_COUNT_EXPONENT=2
HEIGHT_DEGREE=6
KAPPA_OVER_H=1/3
```

and r2 proves a positive-density injective cone.

## Rule-1 transform of Saunderson

The classical transform

\[
(4xz(x^2-3y^2),\ 4yz(3x^2-y^2),\ (x^2-3y^2)(3x^2-y^2))
\]

with `(x,y,z)` Pythagorean is degree `8` in the Euclid parameters.  Even under bounded fibers its natural two-parameter efficiency is at most `2/8=1/4`, so it does not improve the one-third target floor.

## Lenhart/Piezas pair

For

\[
u^2+v^2=5w^2,
\]

the Lenhart-attributed and companion Piezas families use

\[
((u^2-w^2)(v^2-w^2),\ 4uvw^2,\ 2uw(v^2-w^2))
\]

or the `u<->v` companion.  The conic `u^2+v^2=5w^2` has the usual quadratic two-integer parametrization, while the displayed edges are quartic in `(u,v,w)`.  Thus after substitution they are degree `8` in the two integer parameters.  Their natural construction efficiency is again `1/4`, not above `1/3`.

## Bremner 1988 boundary

Andrew Bremner, *The rational cuboid and a quartic surface*, Rocky Mountain J. Math. 18 (1988), 105-121, supplies a general quartic-surface framework and further parametrizations.  Secondary family compendia report Bremner's observation/evidence for polynomial Euler-brick parametrizations in every even degree `>=6`.

This is used only as a literature boundary, not as a theorem that degree `6` is globally minimal.  The safe conclusion is narrower:

```text
KNOWN_CLOSED_FORM_POLYNOMIAL_FAMILY_WITH_DEGREE_LT_6_FOUND=false
KNOWN_DEGREE6_FAMILY=SAUNDERSON
CHECKED_RULE1_LENHART_FAMILIES_DEGREE=8
GLOBAL_MINIMAL_POLYNOMIAL_DEGREE_THEOREM_CLAIMED=false
```

Thus the classical polynomial-family inventory contains no currently certified target construction with `kappa/h>1/3`.

## Sources

- Peschmann 2026, arXiv:2605.00573, Section 6 family classification: Saunderson, Lenhart, Himane and sporadic classes.
- Bremner 1988, DOI `10.1216/RMJ-1988-18-1-105`.
- Himane 2024, arXiv:2405.13061, for the modern coupled-Pythagorean templates handled separately.

```text
CLASSICAL_FAMILY_ROUTE_IMPROVES_M3_EXPONENT=false
M3_PROGRESS_GATE_KAPPA_OVER_H_GT_1_OVER_3_NOT_MET=true
AUDIT_REQUIRED=true
```
