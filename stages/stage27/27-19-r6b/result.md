# Stage27-19-r6b — squareclass-collision equivalence audit

```text
TASK_ID=Stage27-19-r6b
PARENT_ROUTE=Stage27-19-r6a
ROUTE_KIND=UPPER_SUPPORT_REENTRY
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
CURRENT_MU=1/2
```

## Purpose

Stage27-19-r6a rewrote occupied space-diagonal support using the two positive norm-`R^2` representations

\[
D_x^2+y^2=R^2,\qquad D_y^2+x^2=R^2,
\]

and

\[
P=D_xD_y-xy,\qquad Q=D_xD_y+xy,
\]

with `PQ=(eR)^2`.  The intended r6b question is whether

\[
\operatorname{sf}(P)=\operatorname{sf}(Q)
\]

is a genuinely new sieve condition, independent of the frozen Stage15 squareclass receiver.

## Exact toric comparison

Use the frozen Stage15 positive shared-edge toric coordinates

\[
E=4mnrs,
\quad X=2rs(m^2-n^2),
\quad Y=2mn(r^2-s^2),
\]

and `G=gcd(E,X,Y)`.  The primitive physical edges are

\[
e=E/G,\qquad x=X/G,\qquad y=Y/G.
\]

The two guaranteed face diagonals are

\[
D_x=\frac{2rs(m^2+n^2)}G,
\qquad
D_y=\frac{2mn(r^2+s^2)}G.
\]

Stage15 defines

\[
A_0=m^2r^2+n^2s^2,
\qquad
B_0=m^2s^2+n^2r^2.
\]

Direct expansion gives

\[
\begin{aligned}
P
&=D_xD_y-xy\\
&=\frac{4mnrs}{G^2}
\big((m^2+n^2)(r^2+s^2)-(m^2-n^2)(r^2-s^2)\big)\\
&=\frac{8mnrs}{G^2}(m^2s^2+n^2r^2)\\
&=\boxed{\frac{2E}{G^2}B_0},
\end{aligned}
\]

and similarly

\[
\boxed{Q=\frac{2E}{G^2}A_0}.
\]

The common rational factor causes no parity ambiguity because `P,Q` are integers.  For every rational prime `ell`,

\[
v_\ell(P)-v_\ell(Q)=v_\ell(B_0)-v_\ell(A_0).
\]

Therefore

\[
v_\ell(P)\equiv v_\ell(Q)\pmod 2
\iff
v_\ell(A_0)\equiv v_\ell(B_0)\pmod 2
\]

prime by prime, and hence

\[
\boxed{
\operatorname{sf}(P)=\operatorname{sf}(Q)
\iff
\operatorname{sf}(A_0)=\operatorname{sf}(B_0).
}
\]

The right-hand predicate is exactly the frozen Stage15/Stage19 space-diagonal squareclass normal form.

## Consequence

The r6a collision is a useful support-level coordinate system, but it is **not an independent arithmetic condition**.  Applying a local squareclass sieve to `P,Q` and multiplying its saving by the Stage15 squareclass sieve would double-charge the same valuation-parity predicate.

This closes the planned route

`OCCUPIED_R_SQUARECLASS_COLLISION_SIEVE_WITH_PHYSICAL_MASKS`

as a source of a second independent fixed-power saving.

```text
R6A_COLLISION_TO_STAGE15_TORIC_IDENTITY_PROVED=true
P_IDENTITY=P=(2E/G^2)*B0
Q_IDENTITY=Q=(2E/G^2)*A0
VALUATION_PARITY_EQUIVALENCE_PROVED=true
R6_COLLISION_INDEPENDENT_OF_STAGE15=false
SECOND_SQUARECLASS_SIEVE_CHARGE_ALLOWED=false
OCCUPIED_R_SUPPORT_FIXED_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-19-r6c
```
