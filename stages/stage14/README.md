# Stage14 — exactly-two integral-face population

Stage14 studies primitive canonical cuboids with integer space diagonal and exactly two integral face diagonals.

## Current state

```text
STAGE14_1=COMPLETE
STAGE14_2=COMPLETE
STAGE14_3=COMPLETE
STAGE14_4AA=COMPLETE
STAGE14_4AB=COMPLETE
STAGE14_4AC=COMPLETE
STAGE14_4AD=COMPLETE
MAX_VERIFIED_B=2000000
STAGE13_FROZEN_CONTRACT=R03_PLUS_13_12AG
STAGE13_DOWNSTREAM_MATHEMATICAL_CONTENT=FROZEN
BIJECTIVE_TWO_FACE_PARAMETER_SPACE_LOCKED=true
RATIONAL_SLOPE_HEIGHT_FACTORIZATION_LOCKED=true
PRODUCT_PYTHAGOREAN_CLOSURE_IDENTITY=true
ELLIPTIC_FIBRATION_NON_ISOTRIVIAL=true
R03_FIXED_PRIME_SIEVE_GIVES_ZERO_DENSITY=true
R03_FIXED_PRIME_SIEVE_GIVES_POWER_SAVING=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
SQRT_B_FINITE_CANDIDATE_SURVIVES=true
SQRT_B_ASYMPTOTIC_CLAIM=false
NEXT=Stage14-4ae elliptic-fibration height/rank analysis
```

Canonical source: `stages/stage14/main.md`.

## Counting convention

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,
\qquad d\le B.
\]

The exactly-two directions are

```text
a = ab+ac only = smallest shared edge
b = ab+bc only = middle shared edge
c = ac+bc only = largest shared edge
```

with

\[
N_a^{(2)}=O_{ab,ac}-T,\qquad
N_b^{(2)}=O_{ab,bc}-T,\qquad
N_c^{(2)}=O_{ac,bc}-T.
\]

No perfect-cuboid nonexistence assumption is made.

## Frozen finite census

Two independent exact cuboid-generation routes agree through `B=2,000,000`. At the ceiling,

\[
(N_a^{(2)},N_b^{(2)},N_c^{(2)})=(142,134,80),
\qquad N_2=356,
\qquad T=0.
\]

This is only a finite search statement.

## Frozen Stage13 input

Stage13-12ah freezes the downstream mathematical content at

```text
c843e039306b40bd3693f89d6199da78c2fb4657
```

with contract `R03 + Stage13-12ag`.

Stage14 may use

\[
A_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\]

\[
O_{qr}(B)=o(B(\log B)^3),\qquad T(B)=o(B(\log B)^3),
\]

hence

\[
\boxed{N_2(B)=o(B(\log B)^3).}
\]

The R03 inert-prime overlap multiplier is

\[
\lambda_p=\frac{p+5}{2(p+1)}.
\]

However the R03 squeeze fixes a finite prime set first, then sends `B->infinity`, and only afterwards enlarges the prime set. Therefore it proves zero density but does not provide a `B`-dependent power saving. Stage14 does not introduce a growing modulus into the frozen theorem.

## Stage14-4ab/4ac coordinates

For oriented primitive Pythagorean face data

\[
F_i=(S_i,X_i,H_i),\qquad S_i^2+X_i^2=H_i^2,
\]

put

\[
g=(S_1,S_2),\qquad
L=\operatorname{lcm}(S_1,S_2),
\qquad
t_i=X_i/S_i.
\]

The primitive raw-pair incidence has exact parameter fiber multiplicity one and satisfies

\[
\boxed{(e,x,y)=L(1,t_1,t_2)},
\]

\[
\boxed{d=L\sqrt{1+t_1^2+t_2^2}}.
\]

The directions are only

```text
a: 1<t1<t2
b: t1<1<t2
c: t1<t2<1
```

and exactly-two excludes `t1^2+t2^2` being a rational square.

The pre-space lcm-denominator envelope has `B(log B)^7` scale, while frozen R03 already lowers the genuine pair population to `o(B(log B)^3)`.

## Stage14-4ad — elliptic square thinning

The space-diagonal condition has the exact product closure

\[
\boxed{
(X_1X_2)^2+(gd)^2=(H_1H_2)^2.
}
\]

Writing

\[
\rho_i=X_i/H_i,
\]

this is equivalent to

\[
\boxed{1-(\rho_1\rho_2)^2\in(\mathbf Q^\times)^2.}
\]

Fix the first face `rho=rho1` and parameterize the second rational unit circle by

\[
\rho_2=\frac{2q}{1+q^2}.
\]

Then the remaining square condition becomes the nonsingular Jacobi quartic

\[
\boxed{
W^2=q^4+2Aq^2+1,
\qquad A=1-2\rho^2.
}
\]

Since

\[
A^2-1=-4\rho^2(1-\rho^2)\ne0,
\]

every genuine fixed first-face fiber is genus one. An explicit birational reduction gives

\[
2V^2=U^3-2AU^2+(A^2-1)U.
\]

With `t1=X1/S1` this scales to

\[
\boxed{
E_{t_1}:\quad Y^2=X(X-1)(X+t_1^2).
}
\]

Its `j`-invariant is

\[
\boxed{
 j(t_1)=256\frac{(1+t_1^2+t_1^4)^3}
 {t_1^4(1+t_1^2)^2},
}
\]

which is nonconstant. Hence Stage14's global square-thinning problem is a **non-isotrivial elliptic fibration** over the first-face slope.

This identifies the missing global mechanism: the true exponent requires average rational-point/height control on these fibers with the Stage14 lcm-denominator height. The frozen R03 local sieve remains useful auxiliary information but does not by itself determine the exponent.

## sqrt(B) status

Finite data remain compatible with `sqrt(B)`:

```text
B          N2/sqrt(B)
200k       0.2593838854
500k       0.2658721497
1m         0.2550000000
2m         0.2517300141
```

and wider effective exponents over `100k..2m` lie roughly in `0.457..0.489`. This is suggestive only.

```text
SQRT_B_FINITE_CANDIDATE_SURVIVES=true
SQRT_B_ASYMPTOTIC_CLAIM=false
SQRT_B_RIGOROUS_UPPER_BOUND=false
SQRT_B_RIGOROUS_LOWER_BOUND=false
```

## Validation

The independent Stage14-4ad audit checks all 25 raw-pair incidences at `B=10000` and verifies the product identity, normalized square condition, Jacobi quartic, cubic transform and elliptic fiber equation for every hit. It also reproduces exactly-two `(9,11,5)` with `T=0`.

Artifacts:

```text
stages/stage14/archive/stage14-4ad-elliptic-thinning.md
stages/stage14/scripts/14-4/elliptic_fiber_audit.py
stages/stage14/data/14-4/elliptic_fiber_audit.json
stages/stage14/data/14-4/proof_input_audit.json
```

## Next

```text
14-4ae  translate d<=B into fiber/base heights and determine what averaged
        rank/rational-point control is needed to prove or reject a sqrt(B)-type law.
```
