# Stage14-4ad — quantitative square thinning and elliptic-fibration reduction

## Purpose

Stage14-4ac isolated the exact rational-slope height

\[
(e,x,y)=L(1,t_1,t_2),\qquad
 d=L\sqrt{1+t_1^2+t_2^2},
\]

and observed that the frozen finite totals are numerically compatible with a `sqrt(B)` scale. Stage14-4ad asks whether that scale follows from the frozen Stage13 R03 overlap sieve and, if not, identifies the global arithmetic object that must control the true thinning rate.

The answer is sharp:

1. the Stage13 R03 fixed-prime sieve proves zero density but does **not** by itself supply a power saving in `B`;
2. the Stage14 space-diagonal condition admits an exact product-Pythagorean identity;
3. after one primitive face is fixed, the remaining second-face condition is a nonsingular Jacobi quartic, hence an elliptic curve;
4. the fibers form a non-isotrivial elliptic family
   \[
   E_{t_1}:Y^2=X(X-1)(X+t_1^2);
   \]
5. therefore proving or rejecting `N_2(B)\asymp B^{1/2}` is an average rational-point/height problem on this elliptic fibration, coupled to the lcm-denominator height from Stage14-4ac.

No `sqrt(B)` theorem is claimed in this substage.

---

## 1. What the frozen Stage13 sieve really gives

Stage13-12ae proves, for every inert prime `p=3 mod 4`, the exact local multiplier

\[
\lambda_p=\frac{p+5}{2(p+1)}
=\frac12+\frac{2}{p+1}.
\]

For fixed distinct inert primes `S_k={p_1,...,p_k}`, held fixed while `B->infinity`, the tagged overlap bound gives

\[
\limsup_{B\to\infty}
\frac{O_{qr}(B)}{B(\log B)^3}
\le 2D_q\prod_{i=1}^k\lambda_{p_i}.
\]

Choosing `p_i>=7` gives `lambda_{p_i}<=3/4`, so after taking the `B->infinity` limit for fixed `k`, one may then let `k->infinity` and obtain

\[
O_{qr}(B)=o(B(\log B)^3).
\]

This order of quantifiers is essential:

```text
fix k and the modulus first
B -> infinity
then k -> infinity
```

The frozen R03 theorem deliberately avoids a growing-modulus assertion. Consequently Stage14 may import

\[
N_2(B)=o(B(\log B)^3),
\]

but it may **not** infer a bound such as `O(B^(1-epsilon))`, `O(sqrt(B) log^C B)`, or `O(sqrt(B))` by choosing `k=k(B)` inside the R03 proof.

Thus the fixed-prime sieve is a powerful density theorem and local-obstruction map, but it does not identify the Stage14 power exponent.

---

## 2. Product-Pythagorean closure identity

Take the exact Stage14-4ab primitive face data

\[
F_1=(S_1,X_1,H_1),\qquad
F_2=(S_2,X_2,H_2),
\]

with

\[
S_i^2+X_i^2=H_i^2,
\qquad
\gcd(S_i,X_i)=1.
\]

Put

\[
g=\gcd(S_1,S_2),\qquad
\alpha=S_1/g,\qquad
\beta=S_2/g.
\]

The Stage14 glued space diagonal satisfies

\[
d^2=\beta^2H_1^2+\alpha^2X_2^2.
\]

Multiplying by `g^2` gives

\[
g^2d^2=S_2^2H_1^2+S_1^2X_2^2.
\]

On the other hand,

\[
\begin{aligned}
H_1^2H_2^2-X_1^2X_2^2
&=H_1^2(S_2^2+X_2^2)-X_1^2X_2^2\\
&=S_2^2H_1^2+(H_1^2-X_1^2)X_2^2\\
&=S_2^2H_1^2+S_1^2X_2^2.
\end{aligned}
\]

Therefore the space-diagonal condition is equivalent to the exact identity

\[
\boxed{
(X_1X_2)^2+(gd)^2=(H_1H_2)^2.
}
\]

So every raw two-face incidence creates a third integer right triangle

```text
(X1 X2, g d, H1 H2).
```

This is not an additional independent Euclid parameter; it is a closure identity forced by the two primitive faces and the space diagonal.

Normalize by `H_1H_2`. Define

\[
\rho_i:=X_i/H_i\in(0,1).
\]

Then

\[
1-\rho_i^2=(S_i/H_i)^2
\]

is already a rational square, and the space condition becomes

\[
\boxed{
1-(\rho_1\rho_2)^2\in(\mathbf Q^\times)^2.
}
\]

This is the global square condition whose quantitative frequency Stage14 must understand.

---

## 3. Fixing one face produces a Jacobi quartic

Fix the first primitive face and write

\[
\rho:=\rho_1=X_1/H_1,\qquad 0<\rho<1.
\]

Every possible second-face normalized coordinate `rho_2` lies on the rational unit circle. Parameterize it by

\[
\rho_2=\frac{2t}{1+t^2},
\qquad
\frac{S_2}{H_2}=\frac{1-t^2}{1+t^2},
\]

with rational `t` away from the usual finite boundary charts.

The space condition is

\[
z^2=1-\rho^2\rho_2^2.
\]

Multiply by `(1+t^2)^2` and put

\[
Y=z(1+t^2),
\qquad
A:=1-2\rho^2.
\]

Then exactly

\[
\boxed{
Y^2=t^4+2At^2+1.
}
\]

The quartic discriminant is nonzero because

\[
A^2-1
=(1-2\rho^2)^2-1
=-4\rho^2(1-\rho^2)\ne0.
\]

Hence for every genuine positive primitive first face the fixed fiber is a nonsingular genus-one curve. It has the rational point `(t,Y)=(0,1)`, so it is an elliptic curve over `Q`.

The points `t=0` and the finite boundary charts are not physical second faces; they merely supply the rational base point needed to identify the smooth projective genus-one curve with its Jacobian.

---

## 4. Explicit Weierstrass and Legendre-type model

For `t!=0`, write the Jacobi quartic coordinate as `(t,Y)` and define

\[
X_0:=\frac{Y+1}{t^2},
\qquad
U:=A+X_0,
\]

\[
V:=\frac{t}{2}(X_0^2-1).
\]

A direct substitution using

\[
Y^2=t^4+2At^2+1
\]

gives

\[
\boxed{
2V^2
=U^3-2AU^2+(A^2-1)U.
}
\]

Now put

\[
r:=X_1/H_1,
\qquad
s:=S_1/H_1,
\qquad
r^2+s^2=1.
\]

Since `A=1-2r^2=2s^2-1`, the cubic factors as

\[
\boxed{
2V^2=U(U-2s^2)(U+2r^2).
}
\]

Scale

\[
U=2s^2X,
\qquad
Y_E=\frac{V}{2s^3},
\qquad
 t_1:=\frac{r}{s}=\frac{X_1}{S_1}.
\]

Then the fixed fiber is birational to

\[
\boxed{
E_{t_1}:\quad
Y_E^2=X(X-1)(X+t_1^2).
}
\]

The three visible roots give full rational 2-torsion on each nonsingular fiber.

This is a Legendre-type curve with parameter `lambda=-t_1^2`. Its `j`-invariant is

\[
\boxed{
 j(t_1)
 =256\frac{(1+t_1^2+t_1^4)^3}
 {t_1^4(1+t_1^2)^2}.
}
\]

This rational function is nonconstant. Therefore the family is

\[
\boxed{\text{non-isotrivial}.}
\]

The second-face square thinning is therefore not a single fixed elliptic-curve counting problem. Stage14 must average rational points over a varying elliptic family while simultaneously respecting the Stage14 lcm-denominator height.

---

## 5. Relationship to the Stage13 ambient family

Stage13 R03 has already counted the one-face-plus-space-diagonal ambient population at

\[
B(\log B)^3
\]

scale and proved that imposing the second-face condition gives zero relative density.

Stage14-4ad now identifies the exact global geometry behind that second-face condition:

```text
Stage13 ambient incidence
+ second-face local tests at inert primes
+ global rational point on E_t1
+ lcm-denominator height coupling
```

The R03 local multipliers remain valid necessary local conditions and are useful inputs to any future sieve/height argument. But the missing exponent is global: one needs uniform or averaged information on rational points of `E_t1` with the induced nonstandard height.

This explains why simply multiplying local probabilities is not enough to justify a `sqrt(B)` law.

---

## 6. Finite sqrt(B) test survives but is not promoted

Use the frozen Stage14 totals

```text
B          N2
100,000    89
200,000    116
500,000    188
1,000,000  255
2,000,000  356
```

The adjacent pure-power effective exponents

\[
\theta(B_1,B_2)
:=\frac{\log(N_2(B_2)/N_2(B_1))}
{\log(B_2/B_1)}
\]

are

```text
100k -> 200k   0.3822475642
200k -> 500k   0.5269635007
500k -> 1m     0.4397645852
1m   -> 2m     0.4813799941
```

Wider windows are

```text
100k -> 500k   0.4646377393
100k -> 1m     0.4571501738
100k -> 2m     0.4627564263
200k -> 1m     0.4894089719
200k -> 2m     0.4869920087
500k -> 2m     0.4605722896
```

These values are compatible with a limiting exponent `1/2`, but they are also visibly pre-asymptotic and do not separate `B^(1/2)` from `B^(1/2)(log B)^gamma` or from a slowly drifting effective exponent.

Together with the Stage14-4ac stability of `N_2/sqrt(B)`, the correct status is

```text
SQRT_B_FINITE_CANDIDATE_SURVIVES=true
SQRT_B_ASYMPTOTIC_CLAIM=false
SQRT_B_RIGOROUS_UPPER_BOUND=false
SQRT_B_RIGOROUS_LOWER_BOUND=false
```

---

## 7. Deterministic audit

The Stage14-4ad audit enumerates the exact Stage14-4ab face-pair bijection at `B=10000` and verifies all 25 raw-pair incidences. For every hit it checks:

1. the original two primitive-face Pythagorean identities;
2. the glued integer space diagonal;
3. the product-Pythagorean closure
   \[
   (X_1X_2)^2+(gd)^2=(H_1H_2)^2;
   \]
4. the normalized condition `1-(rho1 rho2)^2=z^2`;
5. the unit-circle rational parameterization of the second face;
6. the Jacobi quartic equation;
7. nonsingularity via `A^2-1 != 0`;
8. the explicit cubic birational identity;
9. the Legendre-type fiber equation `Y_E^2=X(X-1)(X+t1^2)`.

It also records the finite effective-exponent diagnostics above.

Artifacts:

```text
stages/stage14/scripts/14-4/elliptic_fiber_audit.py
stages/stage14/data/14-4/elliptic_fiber_audit.json
```

The audit is arithmetic validation, not evidence for an asymptotic exponent.

---

## 8. Stage14-4ad decision

```text
STAGE14_4AD=COMPLETE

PRODUCT_PYTHAGOREAN_CLOSURE_IDENTITY=true
NORMALIZED_PRODUCT_SQUARE_CONDITION=true
SECOND_FACE_FIXED_FIBER_GENUS=1
JACOBI_QUARTIC_MODEL_LOCKED=true
ELLIPTIC_FIBER_MODEL=Y^2=X(X-1)(X+t1^2)
ELLIPTIC_FIBRATION_NON_ISOTRIVIAL=true

R03_FIXED_PRIME_SIEVE_GIVES_ZERO_DENSITY=true
R03_FIXED_PRIME_SIEVE_GIVES_POWER_SAVING=false
GROWING_MODULUS_NOT_IMPORTED=true

SQRT_B_FINITE_CANDIDATE_SURVIVES=true
SQRT_B_ASYMPTOTIC_CLAIM=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
LEADING_CONSTANT_IDENTIFIED=false

NEXT=Stage14-4ae elliptic-fibration height/rank analysis
```

---

## 9. Next question

Stage14-4ae should not add more finite fitting. It should attack the new global bottleneck:

1. translate the lcm-denominator height `d<=B` into a height on the elliptic fiber coordinates;
2. stratify the first-face base by its primitive denominator/height;
3. determine what uniform rank/height information is actually needed to sum rational points over `E_{t1}`;
4. use the frozen R03 local restrictions as auxiliary sieve information, without replacing the global height problem by an independence heuristic;
5. prove or rule out a `B^(1/2)`-type upper/lower scale only after this height comparison is controlled.

The problem is no longer "which square condition is responsible?". The responsible condition is now an explicit non-isotrivial elliptic fibration.