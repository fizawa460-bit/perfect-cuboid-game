# Stage26-60 proof ledger — generalized Saunderson family

## A. Algebraic identities

Assume `u^2+v^2=w^2` with positive integers `u,v,w`. Put

\[
A=u|4v^2-w^2|,\quad B=v|4u^2-w^2|,\quad C=4uvw.
\]

Absolute values do not matter after squaring. Direct expansion using `u^2+v^2=w^2` gives

\[
A^2+B^2=w^6,
\]

\[
A^2+C^2=u^2(4v^2+w^2)^2,
\]

\[
B^2+C^2=v^2(4u^2+w^2)^2.
\]

Hence all three face diagonals are integral.

The factors `4v^2-w^2` and `4u^2-w^2` cannot vanish. If `w=2v`, then `u^2=3v^2`; if `w=2u`, then `v^2=3u^2`. Neither has a positive integral solution.

## B. Primitive input gives primitive output

For a primitive Pythagorean triple, `u,v,w` are pairwise coprime, exactly one of `u,v` is even, and `w` is odd. Label the odd leg `u` and the even leg `v` as in the Euclidean parametrization.

Then `A` is odd, so 2 cannot divide all three output edges. If an odd prime `p` divided `A,B,C`, then `p|uvw`. Pairwise coprimality means exactly one of `u,v,w` is divisible by `p`.

- If `p|u`, then `B=v(4u^2-w^2)=-vw^2 mod p`, nonzero.
- If `p|v`, then `A=u(4v^2-w^2)=-uw^2 mod p`, nonzero.
- If `p|w`, then `A=u(4v^2-w^2)=4uv^2 mod p`, nonzero.

Contradiction in every case. Therefore `gcd(A,B,C)=1`.

## C. Uniform height

Since `0<u,v<w`,

\[
|4v^2-w^2|\le4v^2+w^2\le5w^2,
\]

and similarly for the other factor. Thus

\[
A\le5w^3,\quad B\le5w^3,\quad C\le4w^3,
\]

so

\[
R\le\sqrt{66}w^3<9w^3.
\]

For Euclidean parameters `u=r^2-s^2`, `v=2rs`, `w=r^2+s^2` with `r,s<=T`, one has `w<=2T^2`, hence `R<72T^6`.

## D. Quadratic parameter count

The primitive Euclidean parameter set

\[
\mathcal P(T)=\{(r,s):1\le s<r\le T,(r,s)=1,r-s\text{ odd}\}
\]

has cardinality `asymp T^2`.

A self-contained route is Möbius inversion separated by parity. Only the lower statement is load-bearing: a positive proportion of lattice pairs in the triangle are coprime and of opposite parity. Thus there exists an absolute `c_0>0` and `T_0` such that

\[
\#\mathcal P(T)\ge c_0T^2\qquad(T\ge T_0).
\]

No exact density constant is used in the theorem.

## E. Fiber bound from the cube face-diagonal invariant

For every input, the output face formed by the `A,B` edges has diagonal `w^3`. After canonical sorting, the unordered set of three face diagonals is unchanged. Hence if a fixed canonical Euler cuboid has a generalized-Saunderson preimage, that preimage hypotenuse `w` must be the positive cube root of one of at most three face diagonals.

Fix such a `w`. The number of possible Pythagorean leg pairs satisfies

\[
\#\{(u,v):u^2+v^2=w^2\}\le r_2(w^2)\le4\tau(w^2).
\]

For every fixed `kappa>0`, the elementary divisor estimate gives

\[
\tau(n)\ll_\kappa n^\kappa.
\]

Also `w^3` is a face diagonal and every face diagonal is at most the space diagonal `R`, so for outputs counted by `M3(B)`, `w<=B^(1/3)`. Therefore, after fixing any target epsilon and choosing kappa sufficiently small, the number of parameter preimages of one canonical output is `O_epsilon(B^epsilon)`.

This includes leg exchange and all other representation collisions; no global injectivity is claimed.

## F. Quotient count

Choose

\[
T=\lfloor(B/72)^{1/6}\rfloor.
\]

All pairs in `P(T)` map into `M3(B)`. The domain size is `>>T^2>>B^(1/3)`, while every fiber is `O_epsilon(B^epsilon)`. Hence, for every fixed epsilon>0,

\[
M_3(B)\gg_\epsilon B^{1/3-\epsilon}.
\]

Equivalently

\[
M_3(B)\ge B^{1/3-o(1)}.
\]

The epsilon-free endpoint `M3(B)>>B^(1/3)` is not obtained by this maximum-fiber argument.

## G. Audit targets

A fresh hostile audit should attack, in order:

1. whether the Stage20 algebra/primitivity proof really extends to every primitive Pythagorean input;
2. whether `R<72T^6` is uniform;
3. whether `#P(T)>>T^2` under the parity condition is valid;
4. whether `w^3` survives canonicalization as one of exactly three physical face diagonals;
5. whether the fixed-`w` representation count is bounded by `4 tau(w^2)`;
6. whether the divisor bound supplies the required epsilon-fiber estimate without hidden uniformity;
7. whether dividing the parameter count by maximum fiber legitimately yields `B^(1/3-epsilon)`;
8. whether any statement accidentally promotes the result to an epsilon-free `B^(1/3)` lower or a true exponent.
