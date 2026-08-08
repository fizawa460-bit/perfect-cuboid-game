# Stage14 — primitive canonical exactly-two-face population

> **STATUS:** `STAGE14_4AD_COMPLETE_ELLIPTIC_FIBRATION_14_4AE_NEXT`
>
> **TRACK:** integer-space-diagonal / two-integral-face layer
>
> **CANONICAL_WORKING_FILE:** `stages/stage14/main.md`

Stage14 studies primitive canonical cuboids with integer space diagonal and exactly two integral face diagonals. Stage14-1 through Stage14-3 are complete. Stage14-4 is active at proof level. The Stage13 R03+13-12ag downstream mathematics is frozen and available as an explicit upstream contract.

## §1. Locked population

For `B>=1`, count

\[
0<a<b<c,
\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,
\qquad d\le B.
\]

Let

\[
I_{ab}=\mathbf1_{a^2+b^2=\square},\quad
I_{ac}=\mathbf1_{a^2+c^2=\square},\quad
I_{bc}=\mathbf1_{b^2+c^2=\square}.
\]

Raw pair counts are

\[
O_{ab,ac}=\sum I_{ab}I_{ac},\quad
O_{ab,bc}=\sum I_{ab}I_{bc},\quad
O_{ac,bc}=\sum I_{ac}I_{bc},
\]

and

\[
T=\sum I_{ab}I_{ac}I_{bc}.
\]

Exactly-two counts are

\[
N_a^{(2)}=O_{ab,ac}-T,
\qquad
N_b^{(2)}=O_{ab,bc}-T,
\qquad
N_c^{(2)}=O_{ac,bc}-T,
\]

where

```text
a = shared smallest edge
b = shared middle edge
c = shared largest edge
```

and

\[
N_2=N_a^{(2)}+N_b^{(2)}+N_c^{(2)}.
\]

No perfect-cuboid nonexistence assumption is made. Any `T>0` object remains an exact witness candidate.

## §2. Frozen finite data

Two independent exact generation routes agree at all 11 audited cutoffs through `B=2,000,000`. At the ceiling,

\[
(N_a^{(2)},N_b^{(2)},N_c^{(2)})=(142,134,80),
\qquad N_2=356,
\qquad T=0.
\]

No limiting directional ratio or monotonicity theorem is inferred from the finite table.

## §3. Frozen Stage13 theorem contract

Stage13-12ah freezes downstream mathematical content at

```text
c843e039306b40bd3693f89d6199da78c2fb4657
STAGE13_FROZEN_CONTRACT=R03_PLUS_13_12AG
```

with recorded R03 review state Grok=`CLOSED`, Qwen=`CLOSED`, Claude=`NOT_RECORDED`, Copilot=`PENDING_FINAL_REVIEW`.

Stage14 may use

\[
A_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\]

\[
O_{qr}(B)=o(B(\log B)^3),
\qquad
T(B)=o(B(\log B)^3),
\]

hence

\[
\boxed{N_2(B)=o(B(\log B)^3).}
\]

At inert `p=3 mod 4`, the frozen overlap local multiplier is

\[
\boxed{\lambda_p=\frac{p+5}{2(p+1)}}.
\]

For fixed finite inert-prime set `S_k`, Stage13 obtains

\[
\limsup_{B\to\infty}
\frac{O_{qr}(B)}{B(\log B)^3}
\le 2D_q\prod_{p\in S_k}\lambda_p.
\]

The proof order is

```text
fix S_k
B -> infinity
then k -> infinity
```

and this order is part of the frozen theorem. It gives zero density but no `B`-dependent power saving. Stage14 does not replace it by a growing-modulus assertion.

## §4. Exact Stage14 two-face coordinates

Let the two integral faces share edge `e`; let the other edges be `x<y`, with face diagonals `u,v`. A raw pair incidence satisfies

\[
e^2+x^2=u^2,
\qquad
e^2+y^2=v^2,
\qquad
u^2+y^2=d^2,
\]

and then automatically `v^2+x^2=d^2`.

Take two oriented primitive Pythagorean face data

\[
F_i=(S_i,X_i,H_i),
\qquad
S_i^2+X_i^2=H_i^2,
\]

where `S_i` is designated as the shared-edge leg. Put

\[
g=\gcd(S_1,S_2),
\quad
\alpha=S_1/g,
\quad
\beta=S_2/g.
\]

The shared-edge scale equation has all solutions

\[
k_1=t\beta,
\qquad
k_2=t\alpha.
\]

The minimal gluing is primitive, and the physical cuboid gcd equals `t`; therefore primitive cuboids force exactly `t=1`. Hence

\[
\boxed{
\begin{aligned}
e&=\operatorname{lcm}(S_1,S_2),\\
x&=\beta X_1,\\
y&=\alpha X_2,\\
u&=\beta H_1,\\
v&=\alpha H_2,\\
d^2&=\beta^2H_1^2+\alpha^2X_2^2.
\end{aligned}}
\]

After imposing `x<y`, a fixed raw pair incidence has parameter-fiber multiplicity exactly `1`.

## §5. Rational-slope height

Define

\[
t_i=X_i/S_i,
\qquad
L=\operatorname{lcm}(S_1,S_2).
\]

Then

\[
\boxed{(e,x,y)=L(1,t_1,t_2)}
\]

and

\[
\boxed{d=L\sqrt{1+t_1^2+t_2^2}}.
\]

Each `t_i` is a positive rational Pythagorean slope:

\[
1+t_i^2=(H_i/S_i)^2.
\]

The three directions are chamber inequalities only:

```text
a: 1<t1<t2
b: t1<1<t2
c: t1<t2<1
```

Exactly-two excludes

\[
t_1^2+t_2^2\in(\mathbf Q^\times)^2.
\]

With

\[
M=L\max(1,t_2)=\max(e,y),
\]

we have

\[
\boxed{M<d<\sqrt3 M}.
\]

The primitive-face multiplicity at a fixed distinguished shared leg is

\[
\boxed{
a(S)=
\begin{cases}
0,&S\le1\text{ or }S\equiv2\pmod4,\\
2^{\omega(S)-1},&\text{otherwise}.
\end{cases}}
\]

Ignoring the space-square condition, the lcm denominator envelope has standard finite-order Selberg--Delange scale

\[
B(\log B)^7.
\]

This is only a pre-space envelope. Frozen R03 supplies the far sharper genuine pair ceiling `o(B(log B)^3)`.

## §6. Stage14-4ad — product-Pythagorean closure

The Stage14 space condition has an exact multiplicative identity. From

\[
d^2=\beta^2H_1^2+\alpha^2X_2^2
\]

and `g alpha=S1`, `g beta=S2`,

\[
g^2d^2=S_2^2H_1^2+S_1^2X_2^2.
\]

Using `H_i^2=S_i^2+X_i^2`,

\[
H_1^2H_2^2-X_1^2X_2^2
=S_2^2H_1^2+S_1^2X_2^2.
\]

Therefore

\[
\boxed{
(X_1X_2)^2+(gd)^2=(H_1H_2)^2.
}
\]

So the integer space diagonal is equivalent to the statement that the products of the two primitive face data close into another Pythagorean triangle.

Normalize

\[
\rho_i=X_i/H_i.
\]

Then

\[
\boxed{1-(\rho_1\rho_2)^2\in(\mathbf Q^\times)^2.}
\]

This is the global form of the second-face thinning condition.

## §7. Fixed first face gives a genus-one fiber

Fix

\[
\rho=\rho_1\in(0,1).
\]

Parameterize the rational unit circle for the second face by

\[
\rho_2=\frac{2q}{1+q^2},
\qquad
\frac{S_2}{H_2}=\frac{1-q^2}{1+q^2}.
\]

Let

\[
z^2=1-\rho^2\rho_2^2,
\qquad
W=z(1+q^2),
\qquad
A=1-2\rho^2.
\]

Then the global square condition becomes

\[
\boxed{
W^2=q^4+2Aq^2+1.
}
\]

Since

\[
A^2-1=-4\rho^2(1-\rho^2)\ne0,
\]

the quartic is nonsingular. It has rational base point `(q,W)=(0,1)`, hence its smooth projective model is an elliptic curve.

For `q!=0`, set

\[
X_0=\frac{W+1}{q^2},
\qquad
U=A+X_0,
\qquad
V=\frac q2(X_0^2-1).
\]

Direct substitution yields

\[
\boxed{
2V^2=U^3-2AU^2+(A^2-1)U.
}
\]

Now write

\[
r=X_1/H_1,
\qquad
s=S_1/H_1,
\qquad
r^2+s^2=1.
\]

Then

\[
2V^2=U(U-2s^2)(U+2r^2).
\]

With

\[
U=2s^2X,
\qquad
Y=V/(2s^3),
\qquad
t_1=r/s=X_1/S_1,
\]

we obtain

\[
\boxed{
E_{t_1}:\quad Y^2=X(X-1)(X+t_1^2).
}
\]

Thus the second-face square condition, after the first face is fixed, is an elliptic-curve rational-point problem.

## §8. The elliptic fibration is non-isotrivial

The fiber is Legendre-type with parameter `lambda=-t_1^2`. Its `j`-invariant is

\[
\boxed{
 j(t_1)
 =256\frac{(1+t_1^2+t_1^4)^3}
 {t_1^4(1+t_1^2)^2}.
}
\]

This is nonconstant in `t_1`. Therefore

\[
\boxed{\text{the Stage14 elliptic fibration is non-isotrivial}.}
\]

The true growth-order problem is consequently an average rational-point/height problem over varying fibers, not a count on one fixed elliptic curve.

The original Stage14 height is also nonstandard: the two slopes are coupled by

\[
L=\operatorname{lcm}(S_1,S_2)
\]

and

\[
d=L\sqrt{1+t_1^2+t_2^2}.
\]

A future proof must compare this lcm-height to standard naive/canonical heights on `E_{t_1}` and sum the fibers over the first-face base.

## §9. What R03 does and does not solve

R03 remains extremely useful:

- it supplies the correct one-face ambient scale `B(log B)^3`;
- it supplies exact inert-prime local obstructions;
- it proves the global second-face population has zero relative density;
- it prevents Stage14 from searching inside the much larger `B(log B)^7` pre-space envelope.

But R03 does **not** supply the missing Stage14 exponent, because its local squeeze is intentionally fixed-modulus. The exponent must come from the global elliptic/lcm-height geometry identified above, possibly assisted by the R03 local restrictions.

## §10. sqrt(B) diagnostic after 14-4ad

The frozen finite totals give adjacent effective exponents

```text
100k -> 200k   0.3822475642
200k -> 500k   0.5269635007
500k -> 1m     0.4397645852
1m   -> 2m     0.4813799941
```

and wider-window exponents

```text
100k -> 500k   0.4646377393
100k -> 1m     0.4571501738
100k -> 2m     0.4627564263
200k -> 1m     0.4894089719
200k -> 2m     0.4869920087
500k -> 2m     0.4605722896
```

Meanwhile `N_2/sqrt(B)` over `200k,500k,1m,2m` has coefficient of variation about `2.05%`.

These data remain compatible with an exponent `1/2`, but do not distinguish

\[
\sqrt B,
\qquad
\sqrt B(\log B)^\gamma,
\]

or another slowly drifting effective law.

Therefore

```text
SQRT_B_FINITE_CANDIDATE_SURVIVES=true
SQRT_B_ASYMPTOTIC_CLAIM=false
SQRT_B_RIGOROUS_UPPER_BOUND=false
SQRT_B_RIGOROUS_LOWER_BOUND=false
TRUE_GROWTH_ORDER_IDENTIFIED=false
```

## §11. Deterministic validation

The Stage14-4ad audit enumerates the exact Stage14-4ab face-pair bijection at `B=10000`. It finds 25 raw pair incidences, with exactly-two directional count

\[
(9,11,5)
\]

and `T=0`, matching the frozen census.

For every one of the 25 raw pair incidences it verifies:

```text
product-Pythagorean closure
normalized product-square identity
rational unit-circle parameterization
Jacobi quartic equation
quartic nonsingularity
explicit cubic birational identity
Legendre-type elliptic fiber equation
```

Artifacts:

```text
stages/stage14/archive/stage14-4ad-elliptic-thinning.md
stages/stage14/scripts/14-4/elliptic_fiber_audit.py
stages/stage14/data/14-4/elliptic_fiber_audit.json
stages/stage14/data/14-4/proof_input_audit.json
```

## §12. Locked 14-4ad decision

```text
STAGE14_4AA=COMPLETE
STAGE14_4AB=COMPLETE
STAGE14_4AC=COMPLETE
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

## §13. Next — Stage14-4ae

The next substage should work on the actual global bottleneck rather than adding more finite fits:

1. translate `d<=B` and the lcm denominator into a height on `E_{t_1}`;
2. compare that induced height to standard naive/canonical elliptic heights;
3. stratify the first-face base by primitive denominator/height;
4. determine the uniform or averaged rank/rational-point bounds sufficient to sum the fibers;
5. use R03 local conditions only as auxiliary restrictions;
6. prove or reject a `B^(1/2)`-type growth law only after the fiber/base height sum is controlled.
