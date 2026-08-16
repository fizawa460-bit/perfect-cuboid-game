# Stage27-19-r402a — reduced tau height / support upper preflight

```text
TASK_ID=Stage27-19-r402a
OWNER_STAGE=Stage27
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY
PARENT_ROUTE=Stage27-19-r402
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
CURRENT_UPPER_EXPONENT=1/2
ADVANCE_TO_CHECKPOINT50=false
```

## 1. Purpose

`Stage27-19-r402` passed hostile audit and PR #1037 merged at

```text
77dc7bc7eb29f4113d59c8255ab4b2148bd52690
```

The accepted `tau` pushforward is

\[
\tau=\frac{s^2(m^2+n^2)}{n^2(r^2-s^2)}
\]

on the positive Stage19 two-face toric host. r402a performs the first quantitative test requested by the r402 audit: bound the **reduced rational height** of `tau` on the exact physical cutoff `R<=B`, then determine whether height/support counting alone yields a strict support exponent `sigma<1/2`.

This is a support preflight only. It does not assume a fixed-`tau` fiber theorem or collision-energy theorem.

## 2. Reduced toric representatives and physical face diagonals

Choose the homogeneous slope representatives in reduced positive form

\[
\gcd(m,n)=\gcd(r,s)=1,\qquad m>n>0,\quad r>s>0.
\]

As in the Stage19 frozen toric interface, put

\[
E=4mnrs,\qquad X=2rs(m^2-n^2),\qquad Y=2mn(r^2-s^2),
\]
\[
G=\gcd(E,X,Y),\qquad (e,x,y)=\frac1G(E,X,Y).
\]

The two integral face diagonals through the shared edge are exactly

\[
F_X=\sqrt{e^2+x^2}=\frac{2rs(m^2+n^2)}G,
\]
\[
F_Y=\sqrt{e^2+y^2}=\frac{2mn(r^2+s^2)}G.
\]

For coprime `m,n`,

\[
\gcd(2mn,m^2-n^2)\le2.
\]

Therefore

\[
G\mid\gcd(E,X)=2rs\,\gcd(2mn,m^2-n^2),
\]
so

\[
\boxed{G\le4rs}.
\]

Likewise

\[
\boxed{G\le4mn}.
\]

Consequently

\[
F_X\ge\frac{m^2+n^2}{2},\qquad
F_Y\ge\frac{r^2+s^2}{2}.
\]

Every face diagonal is strictly smaller than the space diagonal `R`, hence on `R<=B`,

\[
\boxed{m^2+n^2<2B},\qquad
\boxed{r^2+s^2<2B}.
\]

Since `m>n` and `r>s`, this also gives

\[
\boxed{n^2<B},\qquad \boxed{s^2<B}.
\]

These bounds retain the primitive scaling factor `G`; no raw toric height is identified with physical height.

```text
REDUCED_SLOPE_PAIR_HEIGHT_BOUND_PROVED=true
M2_PLUS_N2_LT_2B=true
R2_PLUS_S2_LT_2B=true
N2_LT_B=true
S2_LT_B=true
```

## 3. Exact reduced tau-height bound

Write the unreduced positive numerator and denominator as

\[
N_0=s^2(m^2+n^2),\qquad
D_0=n^2(r^2-s^2).
\]

The bounds above imply

\[
0<N_0<2B^2
\]

and, using `r^2-s^2<r^2+s^2`,

\[
0<D_0<2B^2.
\]

Let

\[
g_\tau=\gcd(N_0,D_0),\qquad
\tau=\frac pq=\frac{N_0/g_\tau}{D_0/g_\tau},\qquad \gcd(p,q)=1.
\]

For the standard rational height

\[
H(\tau)=\max(p,q),
\]

reduction can only decrease numerator and denominator, so

\[
\boxed{H(\tau)<2B^2}.
\]

This is a genuine same-physical-measure height theorem for the r402 label.

```text
TAU_REDUCED_HEIGHT_BOUND_PROVED=true
TAU_REDUCED_HEIGHT_BOUND=H(tau)<2B^2
TAU_HEIGHT_PHYSICAL_CUTOFF_MATCH=true
```

## 4. Why rational-height counting does not beat the half-power wall

The number of positive reduced rationals with `H(tau)<2B^2` is at most the number of positive numerator/denominator pairs in that box, hence

\[
\#\{t\in\mathbf Q_{>0}:H(t)<2B^2\}=O(B^4).
\]

A direct toric source count is better but still far too large: each reduced pair `(m,n)` lies in `m^2+n^2<2B`, so there are `O(B)` such pairs, and similarly `O(B)` pairs `(r,s)`. Thus the ambient toric image gives only

\[
\#\operatorname{Im}(\tau;R\le B)=O(B^2)
\]

before the space filter.

Both estimates are weaker than the already certified tautological survivor bound

\[
\#\mathcal T(B)\le N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

Therefore the strongest currently certified support upper exponent remains the inherited half-power boundary:

\[
\boxed{\sigma\le\frac12\ \text{only in the }+\varepsilon\text{ sense}.}
\]

No `sigma<1/2` follows from reduced rational height or ambient toric cardinality alone.

Together with the r402 audited support lower bound,

\[
\#\mathcal T(B)\gg B^{1/4},
\]

the current support corridor is

\[
\boxed{B^{1/4}\ll\#\mathcal T(B)\ll_\varepsilon B^{1/2+\varepsilon}.}
\]

This corridor does **not** identify the true support exponent.

```text
TAU_RATIONAL_HEIGHT_COUNT_EXPONENT=4
TAU_AMBIENT_TORIC_COUNT_EXPONENT=2
TAU_BEST_CERTIFIED_SUPPORT_UPPER=1/2_PLUS_EPSILON
TAU_SUPPORT_STRICT_SUBHALF_PROVED=false
TAU_SUPPORT_EXPONENT_IDENTIFIED=false
HEIGHT_ONLY_SUPPORT_ROUTE_CLOSED=true
```

`HEIGHT_ONLY_SUPPORT_ROUTE_CLOSED=true` is deliberately scoped: it closes only the route that tries to obtain a strict support deficit from the present physical height bound plus raw cardinality. It is not an impossibility theorem for arithmetic support sparsity on the survivor set.

## 5. Consequence for the r402 upper gates

The r402 max-fiber gate is

\[
\sigma+\phi<\frac12.
\]

Since r402a does not improve the certified support exponent below `1/2`, the support side alone cannot create slack. Any continuation must now prove actual anti-concentration inside the survivor pushforward, rather than merely count the available rational labels.

The natural next test is the fixed-`tau` fiber route:

1. fix a reduced rational `tau=t>0`;
2. retain the exact genus-one fiber from r401a/r402;
3. count **physical Stage19 survivors** on that fiber under `R<=B`;
4. test whether a uniform or averaged fiber estimate supplies a nontrivial exponent `phi`, or feeds the collision-energy gate.

No uniform fixed-`tau` point bound is claimed here.

```text
TAU_UNIFORM_FIBER_SUBPOWER_PROVED=false
TAU_WEIGHTED_SECOND_MOMENT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
CURRENT_CHECKPOINT=40
NEXT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
CONTINUE_UPPER_EXPLORATION=true
NEXT_DERIVED_ROUTE=27-19-r402b
NEXT_EXPECTED_COMMAND=Stage27-19-r402-audit
```