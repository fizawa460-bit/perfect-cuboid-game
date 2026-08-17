# Stage27-20-r301l — twist-prime support is hosted by the moduli degeneration divisor

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
PARENT_ROUTE=Stage27-20-r301k
SOURCE_STAGE=Stage20

## 1. Reduced physical coordinate

Write

\[
x=q_1=a/b>1,\qquad (a,b)=1.
\]

R301h proved for the common squarefree class `delta` that

\[
\boxed{\delta_{\rm odd}\mid \operatorname{rad}(a^4-b^4).}
\]

R301g also proved that every odd prime dividing `delta` satisfies

\[
\boxed{p\equiv1\pmod4.}
\]

## 2. Compare with the geometric degeneration divisor

The r301i pencil and r301k moduli formula degenerate only at

\[
x=0,\quad x=\infty,\quad x^4=1.
\]

In homogeneous coprime coordinates this parameter divisor is supported on

\[
\boxed{ab(a^4-b^4)=0.}
\]

Therefore every odd twist prime is already supported on the `x^4=1` component of the parameter degeneration divisor:

\[
\boxed{
p\mid\delta_{\rm odd}\Longrightarrow p\mid a^4-b^4.}
\]

No new odd prime support is introduced by the squareclass twist beyond the primes already hosted by the degeneration parameter.

## 3. What this does and does not prove

This localization is useful for any future descent/conductor average because the moving twist primes and the geometric degeneration primes are not independent prime sets.

However, this stage does **not** identify a minimal Weierstrass model.  It therefore does not assert that every such prime is a bad-reduction prime with a specified Kodaira symbol, nor does it prove an equality between the conductor and `delta(a^4-b^4)`.

The prime `2` is also left separate; the statement above is deliberately odd-prime only.

```text
STAGE27_20_R301L_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
ODD_TWIST_PRIMES_SPLIT_GAUSSIAN=true
ODD_TWIST_PRIME_SUPPORT_SUBSET_X4_MINUS_1=true
ODD_TWIST_PRIME_SUPPORT_SUBSET_DEGENERATION_SUPPORT=true
TWIST_AND_DEGENERATION_PRIME_SETS_INDEPENDENT=false
MINIMAL_WEIERSTRASS_MODEL_AUDITED=false
CONDUCTOR_EQUALITY_PROVED=false
TWO_ADIC_CONDUCTOR_CLASSIFIED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-20-r301m
```
