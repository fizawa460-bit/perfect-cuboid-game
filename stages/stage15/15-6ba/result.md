# Stage15-6ba — AR-012 false-trigger audit after complete 2-descent

Base: Stage15-6az. Audit verdict: `BLOCK`.

The rational descent packet is

\[
U^2-kV_-^2=d,\qquad U^2-kV_+^2=-d.
\]

At first sight this resembles the AR-012 reverse difference-of-squares trigger. It is not an exact match.

Stage15-6ay defines

\[
U=\frac{kZ}{\lambda T},\quad
V_- =\frac{f-g}{\lambda T},\quad
V_+=\frac{f+g}{\lambda T}.
\]

Thus `U,V_-,V_+` are rational numbers with the moving denominator `lambda*T`. Clearing denominators gives

\[
(kZ)^2-k(f-g)^2=d(\lambda T)^2,
\]

\[
(kZ)^2-k(f+g)^2=-d(\lambda T)^2.
\]

The right hand sides therefore contain the moving square `T^2`. AR-012 requires a fixed polynomially bounded right hand side after the outer variables have been fixed, so that signed factor pairs are divisor-many. Here clearing the rational denominator restores a genuine moving support variable.

Equivalently,

\[
V_+^2-V_-^2=\frac{2d}{k}
\]

has infinitely many rational factorizations as the projective ratio varies; it is not an integer divisor problem.

Therefore

```text
AR-012_TRIGGER=false
AR-012_REASON=MOVING_RATIONAL_DENOMINATOR_T
```

No Stage14 exponent or divisor multiplicity is imported.

## Frozen exit

```text
STAGE15_6_SUBSTAGE=6ba
STAGE15_6BA_AUDIT=true
STAGE15_6BA_AUDIT_VERDICT=BLOCK
STAGE15_6BA_AR012_TRIGGER=false
STAGE15_6BA_DESCENT_VARIABLES_RATIONAL=true
STAGE15_6BA_MOVING_DENOMINATOR_T_GENUINE=true
STAGE15_6BA_DIVISOR_MANY_COMPLETION_PROVED=false
STAGE15_6BA_EXIT=AUDIT_RATIONAL_RATIO_SUPPORT
```
