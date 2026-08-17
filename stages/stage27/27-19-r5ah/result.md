# Stage27-19-r5ah — exact primitive-scale factorization and integer physical-height quotient

```text
TASK_ID=Stage27-19-r5ah
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PARALLEL
PARENT_ROUTE=Stage27-19-r5ag
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
PARALLEL_LANE=true
```

Stage27-19-r5ag retained the primitive toric scale

\[
\Gamma=\gcd(E,X,Y)
\]

inside

\[
\Gamma^2R^2=4\delta^2h^2J(p+q).
\]

The unresolved question was whether a large, poorly controlled `Gamma` can cancel the exact physical height. This route removes that ambiguity: `Gamma` has an exact factorization into three explicit cross-gcd channels and one parity bit.

Write

\[
n=\delta n_0,\qquad s=\delta s_0,\qquad (n_0,s_0)=1,
\]

and retain

\[
M=m^2+n^2=ha,\qquad K=r^2-s^2=hb,
\]

\[
p=s_0^2a,\qquad q=n_0^2b,
\]

with `(m,n)=(r,s)=1` in the primitive slope sense. Define

\[
c_0=(m,r),\qquad c_s=(m,s_0),\qquad c_n=(r,n_0),
\]

\[
C=c_0c_sc_n,
\]

and

\[
\varepsilon=
\begin{cases}
2,&m,n,r,s\text{ all odd},\\
1,&\text{otherwise}.
\end{cases}
\]

## 1. The three cross-gcd channels are pairwise coprime

Any common prime of `c_0` and `c_s` would divide both `r` and `s_0`, hence `r` and `s`, contradicting `(r,s)=1`. Any common prime of `c_0` and `c_n` would divide `m` and `n`, contradicting `(m,n)=1`. Likewise a common prime of `c_s` and `c_n` would divide `m` and `n_0`, again contradicting `(m,n)=1`.

Therefore

\[
\boxed{(c_0,c_s)=(c_0,c_n)=(c_s,c_n)=1.}
\]

## 2. Exact formula for the primitive toric scale

The raw toric coordinates are

\[
E=4mnrs,
\]

\[
X=2rs(m^2-n^2),
\]

\[
Y=2mn(r^2-s^2).
\]

After dividing the universal factor `2 delta`,

\[
\frac{E}{2\delta}=2mr\delta n_0s_0,
\]

\[
\frac{X}{2\delta}=rs_0(m^2-\delta^2n_0^2),
\]

\[
\frac{Y}{2\delta}=mn_0hb.
\]

For every odd prime `ell`, primitive coprimality forces a prime dividing all three displayed integers into exactly one of the channels

\[
(m,r),\qquad(m,s_0),\qquad(r,n_0).
\]

More precisely:

- a prime carried by `m` must also divide `r` or `s_0` in order to divide `X/(2delta)`;
- a prime carried by `r` must also divide `m` or `n_0` in order to divide `Y/(2delta)`;
- a prime dividing `delta` cannot survive, because then the second coordinate would force it into `s_0` and the third into `n_0`, contradicting `(n_0,s_0)=1`;
- a prime carried by `n_0` must enter through `r`, and a prime carried by `s_0` must enter through `m`.

The valuation in each surviving channel is exactly the minimum valuation defining the corresponding gcd. Since the three channels are pairwise coprime, the odd part is exactly `C`.

For the prime `2`, use the nine admissible primitive parity patterns of `(m,n)` and `(r,s)`. If all four variables are odd, the first divided coordinate has 2-adic valuation exactly `1`, while both difference-of-odd-squares coordinates have valuation at least `3`; hence there is one extra factor `2`. In every other primitive parity pattern, the 2-adic valuation is already exactly accounted for by the appropriate cross-gcd channel and there is no extra factor.

Thus

\[
\boxed{\Gamma=2\delta\,\varepsilon\,C.}
\]

This is an exact identity, not merely an upper bound.

## 3. The cancellation channels sit inside the two square roots

From the normalized reconstruction,

\[
a r^2-bm^2=\delta^2(p+q).
\]

Since `c_0` divides both `m` and `r`, while `(c_0,delta)=1`,

\[
\boxed{c_0^2\mid p+q.}
\]

Also

\[
J=bm^2+p\delta^2=ar^2-q\delta^2.
\]

Because `p=s_0^2a` and `q=n_0^2b`,

\[
\boxed{c_s^2\mid J,\qquad c_n^2\mid J.}
\]

On a Stage19 survivor write

\[
p+q=\kappa c^2,\qquad J=\kappa w^2,
\qquad \kappa=\operatorname{sf}(p+q)=\operatorname{sf}(J).
\]

A square divisor of a squarefree-times-square integer is absorbed by the square part. Hence

\[
\boxed{c_0\mid c,\qquad c_sc_n\mid w.}
\]

Write

\[
c=c_0c',\qquad w=c_sc_nw',
\]

with positive integers `c',w'`.

## 4. Exact integer factorization of the physical space diagonal

Stage27-19-r5ag proved

\[
\Gamma R=2\delta h\kappa wc.
\]

Insert the exact primitive-scale formula:

\[
2\delta\varepsilon C R=2\delta h\kappa wc.
\]

After canceling `2delta C`,

\[
\boxed{\varepsilon R=h\kappa w'c'.}
\]

If `epsilon=2`, all four slope parameters are odd. Then

\[
v_2(m^2+n^2)=1,
\]

while `r^2-s^2` is divisible by `8`, so for `h=gcd(M,K)` one has `v_2(h)=1`. Thus `epsilon` always divides `h`.

Therefore the physical space diagonal has the exact integer product

\[
\boxed{
R=\frac{h}{\varepsilon}\,\kappa\,w'c'.
}
\]

This removes `Gamma` completely. There is no hidden primitive-scale cancellation beyond the three explicit cross-gcd channels.

Immediate global necessary consequences are

\[
\boxed{\frac{h}{\varepsilon}\mid R,}
\]

\[
\boxed{\kappa\mid R,}
\]

and on `R<=B`,

\[
\boxed{h\kappa\le\varepsilon B\le2B.}
\]

The last inequality is a genuine new exact-height coupling, but it is not by itself a strict-sub-square-root count: `kappa` can be small, including `kappa=1`, on actual Stage19 survivors.

## 5. What remains after exact Gamma elimination

The exact-height problem is now reduced to the residual product

\[
L=w'c'=\frac{wc}{C}.
\]

The physical cutoff is simply

\[
\frac{h}{\varepsilon}\kappa L\le B.
\]

Thus the only way the square roots `w,c` can be heavily canceled is through the explicit cross-gcd product

\[
C=(m,r)(m,s_0)(r,n_0).
\]

Any future fixed-power saving must therefore prove one of two things on the actual Stage19 population: either the residual product `L` is power-large often enough to compress `h*kappa`, or near-total cancellation `C approx wc` occurs on a fixed-power sparse set. Merely treating `Gamma` as an uncontrolled gcd is no longer necessary.

```text
EXACT_PRIMITIVE_SCALE_FACTORIZATION_PROVED=true
EXACT_PRIMITIVE_SCALE_FACTORIZATION=Gamma=2*delta*epsilon*C
CROSS_GCD_PRODUCT=C=gcd(m,r)*gcd(m,s0)*gcd(r,n0)
CROSS_GCD_CHANNELS_PAIRWISE_COPRIME=true
C0_SQUARE_DIVIDES_P_PLUS_Q=true
CS_SQUARE_DIVIDES_J=true
CN_SQUARE_DIVIDES_J=true
C0_DIVIDES_C=true
CS_CN_DIVIDES_W=true
EXACT_PHYSICAL_DIAGONAL_PRODUCT_PROVED=true
EXACT_PHYSICAL_DIAGONAL_PRODUCT=R=(h/epsilon)*kappa*w_prime*c_prime
H_OVER_EPSILON_DIVIDES_R=true
KAPPA_DIVIDES_R=true
H_KAPPA_BOUND_PROVED=true
H_KAPPA_BOUND=h*kappa<=epsilon*B<=2B
HIDDEN_GAMMA_CANCELLATION_REMAINS=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-19-r5ai
NEXT_TARGET=QUANTITATIVE_RESIDUAL_HEIGHT_VERSUS_CROSS_GCD_CANCELLATION_DICHOTOMY
```
