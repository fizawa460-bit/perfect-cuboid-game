# Stage13-13fb — explicit split-prime Wiener bound

> STATUS: `STAGE13_13FB_EXPLICIT_WIENER_LEMMA`
>
> PURPOSE: make the R05 Gate B estimate fully auditable without referring to a hidden numerical sample or an unexplained constant.
>
> INPUT: the primitive raw `j=0` local coefficient system already established in Stage13-12aa.
>
> OUTPUT: a phase-uniform proof of
>
> \[
> \|C_{\ell,p}-1\|_{5/8}\le 529p^{-5/4}
> \qquad(p\equiv1\pmod4,\ p\ge13),
> \]
>
> plus an explicit finite bound for the exceptional split prime `p=5`.

This lemma is deliberately local. It does not perform the curved-region box summation or the retained-harmonic conductor bookkeeping; those are Gates C and D.

---

## 1. Local variables and phase

Let `p≡1 (mod 4)` be a split prime. For the three Dirichlet variables write

\[
x=p^{-s_h},\qquad y=p^{-s_r},\qquad z=p^{-s_s}.
\]

Let `vartheta` denote the local Gaussian angular phase. The proof below is uniform for every real `vartheta`; therefore it is automatically uniform in the retained harmonic index `ell`.

Set

\[
c=\cos\vartheta.
\]

For `n>=0` define

\[
U_n(\vartheta)=2\cos(n\vartheta)
\]

for positive `n`, and

\[
H_n(\vartheta)=1+2\sum_{m=1}^n\cos(m\vartheta).
\]

The primitive raw local subtraction gives

\[
Z_\ell(a,b;\vartheta)=
\begin{cases}
H_b(\vartheta),&a=0,\\
2\cos((a+b)\vartheta),&a\ge1.
\end{cases}
\]

No canonical face label `ab/ac/bc` occurs in these coefficients.

---

## 2. Exact one-variable factors

Define the scale and one-base factors

\[
A_\vartheta(x)
=1+\sum_{a\ge1}2\cos(a\vartheta)x^a,
\]

\[
B_\vartheta(y)
=1+\sum_{b\ge1}H_b(\vartheta)y^b.
\]

Summing the geometric series gives the exact rational functions

\[
\boxed{
A_\vartheta(x)=\frac{1-x^2}{1-2cx+x^2},
}
\]

\[
\boxed{
B_\vartheta(y)=\frac{1+y}{1-2cy+y^2}.
}
\]

At `vartheta=0` these specialize to

\[
A_0(x)=\frac{1+x}{1-x},
\qquad
B_0(y)=\frac{1+y}{(1-y)^2},
\]

so the same formulas include the zero mode.

Write

\[
a_\vartheta(x)=A_\vartheta(x)-1,
\qquad
b_\vartheta(y)=B_\vartheta(y)-1.
\]

The genuine positive-height/base mixed part is

\[
M_\vartheta(x,y)
=\sum_{a,b\ge1}2\cos((a+b)\vartheta)x^ay^b.
\]

Every coefficient of `M_vartheta` has absolute value at most `2`.

---

## 3. Exact three-variable local factor and definition of `C_{ell,p}`

The full split-prime local series is

\[
\begin{aligned}
D_\vartheta(x,y,z)
={}&1+a_\vartheta(x)+b_\vartheta(y)+b_\vartheta(z)\\
&+M_\vartheta(x,y)+M_\vartheta(x,z).
\end{aligned}
\]

There is no term supported simultaneously on positive powers of `y` and `z`, because the primitive outer parameters satisfy `(r,s)=1`.

Define

\[
C_\vartheta(x,y,z)
=\frac{D_\vartheta(x,y,z)}
{A_\vartheta(x)B_\vartheta(y)B_\vartheta(z)}.
\]

For the actual Dirichlet factor we use the notation

\[
\boxed{
C_{\ell,p}(s_h,s_r,s_s)
:=C_\vartheta(p^{-s_h},p^{-s_r},p^{-s_s}),
}
\]

where `vartheta` is the phase attached to `(ell,p)`.

The pure axes agree exactly:

\[
D_\vartheta(x,0,0)=A_\vartheta(x),
\]

\[
D_\vartheta(0,y,0)=B_\vartheta(y),
\]

\[
D_\vartheta(0,0,z)=B_\vartheta(z).
\]

This exact cancellation is why the correction starts at total support size at least two.

---

## 4. Weighted Wiener norm

For

\[
F(x,y,z)=\sum_{i,j,k\ge0}f_{i,j,k}x^iy^jz^k
\]

and `0<rho<1`, define

\[
\|F\|_\rho
=\sum_{i,j,k\ge0}|f_{i,j,k}|\rho^{i+j+k}.
\]

The Cauchy product and Tonelli give

\[
\boxed{
\|FG\|_\rho\le\|F\|_\rho\|G\|_\rho.
}
\]

For the target half-plane

\[
\sigma=\frac58,
\qquad
\rho=p^{-5/8}.
\]

If `p>=13`, then

\[
\rho\le13^{-5/8}<\frac14.
\]

The last inequality is exact because

\[
4^8=65536<13^5=371293.
\]

---

## 5. Pure-axis coefficient bounds

Since `|2 cos(n vartheta)|<=2`,

\[
\begin{aligned}
\|a_\vartheta\|_\rho
&\le2\sum_{n\ge1}\rho^n\\
&=\frac{2\rho}{1-\rho}\\
&\le\frac83\rho
\qquad(\rho\le1/4).
\end{aligned}
\]

Thus

\[
\boxed{\|a_\vartheta\|_\rho\le\frac83\rho.}
\]

Also

\[
|H_n(\vartheta)|\le2n+1.
\]

Hence

\[
\begin{aligned}
\|b_\vartheta\|_\rho
&\le\sum_{n\ge1}(2n+1)\rho^n\\
&=\frac{2\rho}{(1-\rho)^2}+\frac{\rho}{1-\rho}\\
&\le\frac{44}{9}\rho.
\end{aligned}
\]

Therefore

\[
\boxed{\|b_\vartheta\|_\rho\le\frac{44}{9}\rho.}
\]

For the mixed part,

\[
\begin{aligned}
\|M_\vartheta\|_\rho
&\le2\sum_{a,b\ge1}\rho^{a+b}\\
&=\frac{2\rho^2}{(1-\rho)^2}\\
&\le\frac{32}{9}\rho^2.
\end{aligned}
\]

Thus

\[
\boxed{\|M_\vartheta\|_\rho\le\frac{32}{9}\rho^2.}
\]

Every bound is uniform in `vartheta`.

---

## 6. Exact inverse formulas and Wiener bounds

From the rational form of `A_vartheta`,

\[
A_\vartheta(x)^{-1}
=\frac{1-2cx+x^2}{1-x^2}.
\]

After the constant term, every coefficient has absolute value at most `2`: odd coefficients are `-2c` up to sign and even positive coefficients are bounded by `2`. Therefore

\[
\begin{aligned}
\|A_\vartheta^{-1}\|_\rho
&\le1+\frac{2\rho}{1-\rho}\\
&\le\frac53.
\end{aligned}
\]

So

\[
\boxed{\|A_\vartheta^{-1}\|_\rho\le\frac53.}
\]

Likewise

\[
B_\vartheta(y)^{-1}
=\frac{1-2cy+y^2}{1+y}.
\]

Using

\[
\frac1{1+y}=\sum_{n\ge0}(-1)^ny^n,
\]

the coefficient of `y` is `-(1+2c)`, hence has absolute value at most `3`. For every degree `n>=2`, the coefficient is

\[
2(1+c)(-1)^n,
\]

whose absolute value is at most `4`. Therefore

\[
\begin{aligned}
\|B_\vartheta^{-1}\|_\rho
&\le1+3\rho+\frac{4\rho^2}{1-\rho}\\
&\le\frac{25}{12}.
\end{aligned}
\]

Thus

\[
\boxed{\|B_\vartheta^{-1}\|_\rho\le\frac{25}{12}.}
\]

Again these estimates include `vartheta=0` and are phase-uniform.

---

## 7. Pure-axis cancellation and the exact error identity

Put

\[
E_\vartheta
=D_\vartheta-A_\vartheta B_\vartheta(y)B_\vartheta(z).
\]

Since

\[
A_\vartheta=1+a,
\qquad
B_\vartheta(y)=1+b_y,
\qquad
B_\vartheta(z)=1+b_z,
\]

one has the exact expansion

\[
A_\vartheta B_\vartheta(y)B_\vartheta(z)
=1+a+b_y+b_z+ab_y+ab_z+b_yb_z+ab_yb_z.
\]

Subtracting from `D_vartheta` gives

\[
\boxed{
E_\vartheta
=(M_{xy}-ab_y)+(M_{xz}-ab_z)-b_yb_z-ab_yb_z.
}
\]

Every term on the right contains at least two positive coordinate supports. No first-order monomial survives.

By submultiplicativity,

\[
\|E_\vartheta\|_\rho
\le
2\|M\|_\rho
+2\|a\|_\rho\|b\|_\rho
+\|b\|_\rho^2
+\|a\|_\rho\|b\|_\rho^2.
\]

The first three terms are already multiples of `rho^2`. For the last term,

\[
\|a\|_\rho\|b\|_\rho^2
\le
\frac83\left(\frac{44}{9}\right)^2\rho^3.
\]

Since `rho<=1/4`,

\[
\rho^3\le\frac14\rho^2.
\]

Therefore the four contributions are respectively

\[
\frac{64}{9}\rho^2,
\qquad
\frac{704}{27}\rho^2,
\qquad
\frac{1936}{81}\rho^2,
\qquad
\frac{3872}{243}\rho^2.
\]

On the common denominator `243`,

\[
\frac{64}{9}
+\frac{704}{27}
+\frac{1936}{81}
+\frac{3872}{243}
=
\frac{1728+6336+5808+3872}{243}
=
\frac{17744}{243}.
\]

Hence

\[
\boxed{
\|E_\vartheta\|_\rho
\le\frac{17744}{243}\rho^2.
}
\]

This is the complete origin of the numerator constant used below.

---

## 8. The constant `529`

Because

\[
C_\vartheta-1
=E_\vartheta
A_\vartheta^{-1}
B_\vartheta(y)^{-1}
B_\vartheta(z)^{-1},
\]

submultiplicativity yields

\[
\begin{aligned}
\|C_\vartheta-1\|_\rho
&\le
\frac{17744}{243}\rho^2
\cdot\frac53
\cdot\left(\frac{25}{12}\right)^2\\
&=\frac{3465625}{6561}\rho^2.
\end{aligned}
\]

The exact rational constant satisfies

\[
\frac{3465625}{6561}
=528.2159731748209\ldots
<529.
\]

Therefore

\[
\boxed{
\|C_\vartheta-1\|_\rho<529\rho^2.
}
\]

With `rho=p^{-5/8}`,

\[
\rho^2=p^{-5/4}.
\]

Thus for every split prime `p>=13`, every harmonic index and every phase,

\[
\boxed{
\|C_{\ell,p}-1\|_{5/8}
\le529p^{-5/4}.
}
\]

There is no hidden dependence on `ell`, `p` beyond `p^{-5/4}`, or the local phase.

---

## 9. The split prime `p=5` is finite with an explicit phase-uniform bound

For `p=5`,

\[
\rho_5=5^{-5/8}<\frac38.
\]

Indeed this is equivalent after taking eighth powers to

\[
8^8<3^8 5^5,
\]

and

\[
16777216<20503125.
\]

Repeating the same coefficient estimates with `rho<=3/8` gives

\[
\|a\|_\rho\le\frac65,
\qquad
\|b\|_\rho\le\frac{63}{25},
\qquad
\|M\|_\rho\le\frac{18}{25},
\]

\[
\|A^{-1}\|_\rho\le\frac{11}{5},
\qquad
\|B^{-1}\|_\rho\le\frac{121}{40}.
\]

Consequently

\[
\|E\|_\rho
\le
2\frac{18}{25}
+2\frac65\frac{63}{25}
+\left(\frac{63}{25}\right)^2
+\frac65\left(\frac{63}{25}\right)^2
=
\frac{67059}{3125}.
\]

Hence

\[
\begin{aligned}
\|C_{\ell,5}-1\|_{5/8}
&\le
\frac{67059}{3125}
\cdot\frac{11}{5}
\cdot\left(\frac{121}{40}\right)^2\\
&=\frac{10799919009}{25000000}\\
&=431.99676036\\
&<432.
\end{aligned}
\]

Thus `p=5` is not merely called harmless: it has an explicit finite Wiener bound uniform in the phase. Since it is one Euler factor, it does not affect convergence of the infinite product over `p>=13`.

---

## 10. Global consequence needed later

For the infinite split-prime tail,

\[
\sum_{p\equiv1(4),\ p\ge13}
\|C_{\ell,p}-1\|_{5/8}
\le
529\sum_{p\ge13}p^{-5/4}
<\infty.
\]

Therefore the Euler product of mixed corrections converges absolutely in the weighted Wiener algebra. Because the local majorant is phase-uniform, the resulting global Wiener norm is uniform in every retained harmonic range, in particular

\[
1\le\ell\le(\log B)^4.
\]

This also implies the fixed logarithmic moments used by the convolution step: for every fixed integer `m>=0`,

\[
\sum_{u,v,w\ge1}
\frac{|c_\ell(u,v,w)|(1+\log(uvw))^m}{uvw}<\infty,
\]

uniformly in retained `ell`, because

\[
(1+\log n)^m n^{-3/8}
\]

is bounded on `n>=1`.

The present gate establishes only this Wiener/moment interface. The summation of rectangle errors and the nonzero-harmonic family estimate remain separate R05 gates.

---

## 11. Review-facing lock

The constant `529` is therefore not an empirical constant and not a black box. It is the rounded-up product

```text
E support bound        = 17744/243
A inverse bound        = 5/3
B inverse bound        = 25/12, twice
exact product          = 3465625/6561
                       = 528.2159731748209...
rounded majorant       = 529
rho^2                  = p^(-5/4)
```

and `p=5` separately satisfies the explicit phase-uniform finite bound `<432`.

```text
STAGE13_13FB=COMPLETE_EXPLICIT_WIENER_BOUND
WIENER_SIGMA=5/8
SPLIT_PRIME_TAIL_START=13
WIENER_E_BOUND=17744/243
WIENER_EXACT_CONSTANT=3465625/6561
WIENER_ROUNDED_CONSTANT=529
WIENER_EXPONENT=5/4
P5_EXPLICIT_FINITE_BOUND_LT=432
PHASE_UNIFORM=true
RETAINED_HARMONIC_UNIFORM=true
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R04_IMMUTABLE=true
NEXT=13-13fc
```