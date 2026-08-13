# Stage14-e4 — directionwise ambient asymptotic via the archimedean Tamagawa measure

> STATUS: `STAGE14_E4_COMPLETE_DIRECTIONAL_ASYMPTOTIC`
>
> INPUT: Stage14-e3 toric anticanonical model, Huang toric adelic equidistribution, Browning--Loughran thin-set zero-density theorem
>
> RESULT: the three exactly-two ambient directions have a common arithmetic factor and explicit real-chamber factors.

## 1. Object and notation

Stage14-e counts primitive triples `(e,x,y)` with `x<y`,

\[
e^2+x^2=\square,\qquad e^2+y^2=\square,
\qquad \gcd(e,x,y)=1,
\]

under the real Euclidean height

\[
D_{\mathbf R}=\sqrt{e^2+x^2+y^2}\le B.
\]

No rationality or integrality condition is imposed on `D_R`.

The exactly-two population excludes

\[
x^2+y^2=\square.
\]

Normalize

\[
t_1=x/e,\qquad t_2=y/e,
\]

so `0<t1<t2`. The three directions are

\[
\begin{array}{ll}
a:&1<t_1<t_2,\\
b:&t_1<1<t_2,\\
c:&t_1<t_2<1.
\end{array}
\]

Write their exactly-two counts as `E_a(B),E_b(B),E_c(B)` and

\[
E_2(B)=E_a(B)+E_b(B)+E_c(B).
\]

## 2. Frozen e3 torus coordinate

For each rational Pythagorean slope,

\[
h_i^2-t_i^2=1,
\]

put

\[
q_i=h_i+t_i>1.
\]

Then

\[
q_i^{-1}=h_i-t_i,
\]

and

\[
\boxed{
 t_i=\frac{q_i-q_i^{-1}}2,
 \qquad
 h_i=\frac{q_i+q_i^{-1}}2.
}
\]

Thus the positive two-face shapes are the real chamber

\[
1<q_1<q_2<\infty
\]

of the torus `T=(G_m)^2`.

Stage14-e3 identifies the compactification

\[
Y=\operatorname{Bl}_4(\mathbf P^1\times\mathbf P^1)
\]

at the four torus-fixed corners and proves that the line bundle producing the physical projective point

\[
[1:t_1:t_2]
\]

is

\[
L=-K_Y.
\]

The Picard rank is six, hence the anticanonical logarithmic exponent is five.

## 3. The physical height is the chosen anticanonical height

For the primitive integer representative

\[
[1:t_1:t_2]=[e:x:y],
\]

the Euclidean projective metric gives exactly

\[
H([1:t_1:t_2])=\sqrt{e^2+x^2+y^2}=D_{\mathbf R}.
\]

Therefore e4 does not replace the physical cutoff by a merely comparable height when computing direction ratios: it uses the actual adelic height whose archimedean norm is Euclidean.

On the torus, let

\[
\omega=\frac{dq_1}{q_1}\wedge\frac{dq_2}{q_2}.
\]

Its inverse is the invariant anticanonical frame. In the e3 `(2,2)` projective presentation, the first coordinate section is

\[
s_0=4q_1q_2
\]

in the standard affine trivialization, while the invariant anticanonical frame is proportional to `q1 q2`. Consequently the pulled-back Euclidean metric gives, up to one global positive normalization constant independent of the chamber,

\[
\|\omega^{-1}\|_\infty
\propto
\frac{1}{\sqrt{1+t_1^2+t_2^2}}.
\]

Hence the archimedean Tamagawa density on the positive torus is

\[
\boxed{
 d\tau_\infty
 \propto
 \frac{dq_1\,dq_2}
 {q_1q_2\sqrt{1+t_1^2+t_2^2}}.
}
\]

All finite-place density factors are common to the three directions because the direction cut is purely archimedean.

## 4. Hyperbolic and angular forms of the density

Put

\[
r_i=\log q_i.
\]

Then

\[
t_i=\sinh r_i,
\qquad
\frac{dq_i}{q_i}=dr_i.
\]

Therefore

\[
\boxed{
 d\tau_\infty
 \propto
 \frac{dr_1\,dr_2}
 {\sqrt{1+\sinh^2r_1+\sinh^2r_2}}.
}
\]

For chamber integration it is convenient to set

\[
t_i=\tan\theta_i,
\qquad 0<\theta_i<\frac\pi2.
\]

Since

\[
dr_i=\frac{dt_i}{\sqrt{1+t_i^2}}=\sec\theta_i\,d\theta_i
\]

and

\[
1+\tan^2\theta_1+\tan^2\theta_2
=
\frac{1-\sin^2\theta_1\sin^2\theta_2}
{\cos^2\theta_1\cos^2\theta_2},
\]

we obtain the especially simple density

\[
\boxed{
 d\tau_\infty
 \propto
 \frac{d\theta_1\,d\theta_2}
 {\sqrt{1-\sin^2\theta_1\sin^2\theta_2}}.
}
\]

The ordering is `theta1<theta2`, and the shared-edge threshold `t=1` is exactly

\[
\theta=\frac\pi4.
\]

## 5. Three chamber masses

Define

\[
W(\theta_1,\theta_2)
=
\frac1{\sqrt{1-\sin^2\theta_1\sin^2\theta_2}}.
\]

The direction masses are

\[
\boxed{
M_a=
\int_{\pi/4}^{\pi/2}
\int_{\theta_1}^{\pi/2}
W(\theta_1,\theta_2)\,d\theta_2\,d\theta_1,
}
\]

\[
\boxed{
M_b=
\int_{0}^{\pi/4}
\int_{\pi/4}^{\pi/2}
W(\theta_1,\theta_2)\,d\theta_2\,d\theta_1,
}
\]

and

\[
\boxed{
M_c=
\int_{0}^{\pi/4}
\int_{\theta_1}^{\pi/4}
W(\theta_1,\theta_2)\,d\theta_2\,d\theta_1.
}
\]

Their sum

\[
M=M_a+M_b+M_c
\]

is the archimedean mass of the positive ordered chamber.

A deterministic 64-point tensor Gauss--Legendre audit in nonsingular hyperbolic coordinates gives

\[
\boxed{M_a=0.7295086229844\ldots}
\]

\[
\boxed{M_b=0.6753521849590\ldots}
\]

\[
\boxed{M_c=0.3139356465617\ldots}
\]

and

\[
\boxed{M=1.7187964545051\ldots}.
\]

Thus the normalized chamber vector is

\[
\boxed{
(p_a,p_b,p_c)
=
(0.4244299091218\ldots,
 0.3929215604261\ldots,
 0.1826485304521\ldots).
}
\]

Equivalently, relative to the `c` chamber,

\[
\boxed{
E_a:E_b:E_c
\longrightarrow
2.323752115996\ldots:
2.151244028372\ldots:
1.
}
\]

These numbers come from the physical archimedean height measure, not from fitting the e2 finite census.

## 6. Raw directional asymptotic

Huang's toric equidistribution theorem applies to the smooth proper split toric surface `Y` with the anticanonical height fixed above. The three real chambers are continuity sets: their separating hypersurfaces and toric boundary have archimedean Tamagawa measure zero.

Therefore there is one positive global arithmetic factor `Lambda_E`, containing the geometric/Peyre factor and all finite-place densities, such that the raw two-face chamber counts satisfy

\[
R_q(B)
\sim
\Lambda_E M_q\,B(\log B)^5,
\qquad q\in\{a,b,c\}.
\]

In particular

\[
R_{\rm ord,+}(B)
\sim
\Lambda_E M\,B(\log B)^5.
\]

No finite local factor needs to be recomputed direction-by-direction: the direction partition lives only at the real place.

## 7. The third-face-square locus is thin

The exactly-two condition removes points for which

\[
t_1^2+t_2^2=w^2
\]

for some rational `w`.

Consider the function-field extension

\[
\mathbf Q(Y)
\subset
\mathbf Q(Y)\bigl(\sqrt{t_1^2+t_2^2}\bigr).
\]

It has degree two. Indeed, over the geometric function field,

\[
t_1^2+t_2^2=(t_1+i t_2)(t_1-i t_2)
\]

has odd valuation along each of the two irreducible divisors `t1 +/- i t2=0`, so it is not a square.

Let `Z` be the normalization of `Y` in this quadratic extension and resolve if necessary. Then

\[
\pi:Z\to Y
\]

is generically finite of degree two, and every third-face-square torus point lies in

\[
\pi(Z(\mathbf Q)).
\]

Hence the Euler-brick/third-face-square population is a thin subset of type II.

## 8. Thin-set removal does not change the leading term

The surface `Y` is toric, smooth and projective. Its anticanonical divisor is globally generated, nef and big, with

\[
(-K_Y)^2=8-4=4>0.
\]

Thus it lies in the almost-Fano setting used by Browning--Loughran. Huang supplies the required rational-point equidistribution on the open torus.

Browning--Loughran's thin-set theorem therefore gives

\[
\#\{P\in\pi(Z(\mathbf Q)):H(P)\le B\}
=o\!\left(B(\log B)^5\right).
\]

This global little-o is automatically a little-o inside each chamber, since each chamber itself has a positive `B(log B)^5` main term.

Therefore removing all third-face-square points leaves every chamber leading coefficient unchanged:

\[
\boxed{
E_q(B)
\sim
\Lambda_E M_q\,B(\log B)^5,
\qquad q\in\{a,b,c\}.
}
\]

Summing,

\[
\boxed{
E_2(B)
\sim
\Lambda_E M\,B(\log B)^5.
}
\]

This upgrades e3 from matching order `asymp` to existence of a full exactly-two main term, while leaving the global arithmetic constant `Lambda_E` unevaluated.

## 9. Direction limit

Dividing the three asymptotics by their sum gives the unconditional e4 direction limit within the frozen theorem inputs:

\[
\boxed{
\lim_{B\to\infty}
\frac{(E_a(B),E_b(B),E_c(B))}{E_2(B)}
=
(0.4244299091218\ldots,
 0.3929215604261\ldots,
 0.1826485304521\ldots).
}
\]

The e2 value at `B=10^6`, approximately

```text
(0.33237, 0.42097, 0.24667)
```

is therefore retained as pre-asymptotic data only. Its discrepancy from the toric limit is not used to tune the proof.

## 10. Literature boundary

The external theorem inputs are explicitly separated from the repository-local computation:

```text
Batyrev--Tschinkel: toric anticanonical bounded-height asymptotic
Huang: toric adelic equidistribution / real chamber restriction
Browning--Loughran: equidistributed thin subsets have zero density
```

Adjacent Pythagorean literature includes common-leg formulas and one-circle angular distributions, but the current search found no direct theorem for this exact common-edge two-face anticanonical-height chamber vector.

See

```text
stages/stage14/14-e4/literature-directional-audit.md
```

for the collision record.

## 11. What e4 does not claim

Stage14-e4 does not:

- evaluate the common global arithmetic factor `Lambda_E` as an Euler product;
- infer the main Stage14 integer-space-diagonal direction vector from the ambient vector;
- assert that the main-track square filter is direction-neutral;
- use the e2 finite direction ratios as proof input;
- claim novelty from absence in the current literature search.

Those questions belong to e5 or a later constant-computation supplement.

## 12. Locked conclusion

```text
STAGE14_E4=COMPLETE_DIRECTIONAL_ASYMPTOTIC
E3_TOTAL_ORDER_RETAINED=true
EXACTLY_TWO_THIRD_FACE_SQUARE_LOCUS=THIN_TYPE_II
THIN_SET_ZERO_DENSITY_INPUT=BROWNING_LOUGHRAN_THEOREM_1_2
ARCHIMEDEAN_TAMAGAWA_DENSITY_DERIVED=true
COMMON_FINITE_ARITHMETIC_FACTOR_ACROSS_DIRECTIONS=true
DIRECTIONAL_ASYMPTOTIC_PROVED=true
EXACTLY_TWO_FULL_MAIN_TERM_EXISTENCE_PROVED=true
GLOBAL_ARITHMETIC_CONSTANT_LAMBDA_E_EVALUATED=false
PA=0.4244299091218
PB=0.3929215604261
PC=0.1826485304521
NEXT_E_TASK=Stage14-e5 space-diagonal filter comparison
```
