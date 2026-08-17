# Stage27-20-r301h — fixed-coordinate squareclass support collapse

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
PARENT_ROUTE=Stage27-20-r301g
SOURCE_STAGE=Stage20

## 1. One torus coordinate already contains every odd squareclass prime

Keep the notation of r301g:

\[
q_1=a/b,\qquad q_2=c/e
\]

in lowest terms, and let `delta` be the common positive squarefree class of the two factors.

For every odd `p|delta`, r301g proves that either

\[
p\mid a^2-b^2
\]

or

\[
p\mid a^2+b^2.
\]

Therefore

\[
\boxed{
\delta_{\rm odd}\mid\operatorname{rad}(a^4-b^4).
}
\]

By symmetry,

\[
\boxed{
\delta_{\rm odd}\mid\operatorname{rad}(c^4-e^4).
}
\]

Thus after **either** torus coordinate is fixed, the moving common squareclass is restricted to squarefree divisors of one fixed integer.  The two-adic choice contributes at most one additional factor `2`.

Because the physical positive Pythagorean branch has `q_i>1`, neither `a^4-b^4` nor `c^4-e^4` vanishes.

## 2. Physical height gives a uniform polynomial bound for H(q_i)

For one physical face write

\[
E^2+X^2=U^2,
\qquad
q=\frac{U+X}{E}.
\]

Under the Stage27 physical cutoff

\[
R=\sqrt{E^2+X^2+Y^2}\le B,
\]

we have

\[
E\le B,\qquad X\le B,\qquad U=\sqrt{E^2+X^2}\le R\le B.
\]

After reducing `(U+X)/E`, its rational height therefore satisfies

\[
\boxed{H(q)\le 2B.}
\]

Hence for `q_1=a/b` in lowest terms,

\[
|a^4-b^4|\ll B^4.
\]

## 3. Subpolynomial squareclass count per fixed coordinate

For fixed `q_1=a/b`, every admissible common squareclass `delta` divides, up to the optional factor `2`, the squarefree radical of `a^4-b^4`.  Therefore

\[
\#\{\delta:\text{compatible with this fixed }q_1\}
\le 2^{1+\omega(a^4-b^4)}
\le 2\tau(|a^4-b^4|).
\]

The standard divisor bound, uniformly for integers of polynomial size in `B`, gives

\[
\boxed{
\#\{\delta:\text{compatible with fixed }q_1\}=B^{o(1)}.
}
\]

Equivalently, for every fixed `epsilon>0`, the number is `O_epsilon(B^epsilon)` uniformly over all physical `q_1` occurring under `R<=B`.  The same statement holds with `q_1` and `q_2` interchanged.

This is a real support collapse: the squareclass variable does **not** add a new fixed positive exponent once one torus coordinate is frozen.

## 4. What this does and does not buy

This does not by itself bound the number of possible first coordinates `q_1`, nor the number of Stage27 survivors inside one fixed `(q_1,delta)` fiber.  Therefore it cannot simply be multiplied into the existing half-power theorem as an independent saving.

The next legal question is the geometry and arithmetic of the fixed `(q_1,delta)` fiber.

```text
STAGE27_20_R301H_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
DELTA_ODD_DIVIDES_RAD_A4_MINUS_B4=true
DELTA_ODD_DIVIDES_RAD_C4_MINUS_E4=true
PHYSICAL_Q_HEIGHT_LE_2B=true
FIXED_Q1_SQUARECLASS_SUPPORT_SUBPOLYNOMIAL=true
FIXED_Q2_SQUARECLASS_SUPPORT_SUBPOLYNOMIAL=true
GLOBAL_Q1_SUPPORT_DEFICIT_PROVED=false
FIXED_Q1_DELTA_FIBER_UNIFORM_SUBPOWER_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEXT_DERIVED_ROUTE=27-20-r301i
```
