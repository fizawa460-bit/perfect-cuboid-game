# Stage14-t2 — quantitative moving-family attack and explicit chain envelope

> STATUS: `STAGE14_T2_COMPLETE_QUANTITATIVE_BOUNDARY`

Stage14-t2 attacks the triple/perfect-cuboid correction term quantitatively. The main new unconditional result is an explicit Pythagorean-chain envelope with fixed logarithmic loss. It does not reach the target `T(B)=o(sqrt(B))`.

## 1. Perfect cuboids inject into a two-step Pythagorean chain

For a primitive canonical triple object

\[
0<a<b<c,\qquad a^2+b^2+c^2=d^2\le B^2,
\]

put

\[
z=\sqrt{b^2+c^2}.
\]

Because all three face diagonals are integral, `z` is an integer and

\[
b^2+c^2=z^2,
\qquad
 a^2+z^2=d^2.
\]

Thus every Stage14 triple object determines uniquely

```text
(b,c,z)  : integer right triangle with hypotenuse z,
(a,z,d)  : integer right triangle with leg z,
```

with `z<d<=B`. Dropping the remaining two face-square conditions only enlarges the count, so this chain gives an unconditional upper envelope.

## 2. Exact representation factors

Write

\[
z=2^{e_2}\prod_{p\equiv1(4)}p^{e_p}\prod_{p\equiv3(4)}p^{e_p}.
\]

Let

\[
P(z)=\prod_{p\equiv1(4)}(2e_p+1),
\qquad
\tau(z^2)=\prod_p(2e_p+1).
\]

The number `A(z)` of unordered positive pairs `b<c` with `b^2+c^2=z^2` is

\[
A(z)=\frac{P(z)-1}{2}.
\]

For the second chain, factorization

\[
(d-a)(d+a)=z^2
\]

shows that the number `L(z)` of positive completions `(a,d)` is bounded by

\[
L(z)\le \frac{\tau(z^2)-1}{2}.
\]

Hence

\[
T(B)\le\sum_{z\le B}A(z)L(z)
\le \frac14\sum_{z\le B}f(z),
\]

where the multiplicative majorant is

\[
f(z)=P(z)\tau(z^2).
\]

Its prime-power values are

\[
f(p^e)=
\begin{cases}
(2e+1)^2,&p\equiv1\pmod4,\\
2e+1,&p=2\text{ or }p\equiv3\pmod4.
\end{cases}
\]

## 3. Dirichlet-series factorization

Let `chi_4` be the non-principal character modulo `4`. The local generating functions are

\[
\sum_{e\ge0}(2e+1)^2x^e=\frac{1+6x+x^2}{(1-x)^3}
\]

for split primes `p=1 mod 4`, and

\[
\sum_{e\ge0}(2e+1)x^e=\frac{1+x}{(1-x)^2}
\]

for inert primes `p=3 mod 4`.

Matching the linear Euler coefficients gives

\[
\boxed{
\sum_{n\ge1}\frac{f(n)}{n^s}
=\zeta(s)^6L(s,\chi_4)^3G(s),
}
\]

where the odd-prime residual local factors are

\[
G_p(x)=
\begin{cases}
(1+6x+x^2)(1-x)^6,&p\equiv1\pmod4,\\
(1-x^2)^4,&p\equiv3\pmod4,
\end{cases}
\]

and the `p=2` factor is finite and harmless. In both odd cases

\[
G_p(p^{-s})=1+O(p^{-2\Re s}),
\]

so `G(s)` converges absolutely in every half-plane `Re(s)>1/2+epsilon` and is finite and nonzero at `s=1`.

The Selberg--Delange method therefore yields

\[
\sum_{n\le B}f(n)\asymp B(\log B)^5,
\]

and in particular

\[
\boxed{T(B)=O(B(\log B)^5).}
\]

This bound is completely independent of the genus-5 determinant-method route and uses only the exact Pythagorean-chain injection.

## 4. Comparison with the frozen Stage13 theorem

The new bound is explicit but is not the strongest asymptotic statement already available to Stage14. The frozen Stage13 R03 contract gives

\[
\boxed{T(B)=o(B(\log B)^3).}
\]

Therefore t2 does **not** claim an improvement over R03. Its contribution is different: it gives a direct Stage14-native quantitative envelope, with a fully explicit multiplicative mechanism and no overlap-sieve input.

The target

\[
T(B)=o(\sqrt B)
\]

remains far beyond both bounds.

## 5. Why the moving genus-5 route does not yet close the gap

The t1 fiber is a smooth genus-5 curve for every genuine physical Pythagorean base, so Faltings gives finite rational points on each fixed fiber. But there is no unconditional genus-only uniform bound for the number of rational points on arbitrary genus-5 curves.

General determinant-method theorems give coefficient-uniform bounded-height counts for fixed-degree projective varieties, and family-specific results can improve this in special hyperelliptic fibrations. For Stage14, however, a usable global estimate still has to retain simultaneously:

```text
physical q-height v ~ sqrt(Bg/S1),
coefficient height as the Pythagorean base moves,
number of admissible first-face bases,
exceptional/low-degree subfamilies,
and the two simultaneous square conditions.
```

No currently audited theorem turns those ingredients into `o(sqrt(B))` after summation over the moving base.

## 6. Quantitative conclusion

```text
STAGE14_T2=COMPLETE_QUANTITATIVE_BOUNDARY
PYTHAGOREAN_CHAIN_INJECTION_LOCKED=true
CHAIN_MAJORANT_DIRICHLET_SERIES=zeta(s)^6*L(s,chi4)^3*G(s)
CHAIN_ENVELOPE=T(B)=O(B(log B)^5)
CHAIN_ENVELOPE_IMPROVES_R03=false
FROZEN_STRONGEST_GLOBAL_BOUND=T(B)=o(B(log B)^3)
T_O_SQRT_B_PROVED=false
SQRT_B_POWER_SAVING_PROVED=false
NEXT=Stage14-t3 exceptional fibers and low-degree subfamilies
```
