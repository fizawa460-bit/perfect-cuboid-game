# Stage14-t37 — common-core Gaussian orientation packets and fixed-ell power saving

## Purpose

Stage14-t36 proved a square-root bound inside every fixed direction fiber,

\[
R_{a,b}\le J_{a,b}^{1/2}B^{o(1)},
\]

and therefore closed the long-fiber range.  The only remaining obstruction inside a fixed canonical super-square-root prime `ell` was the endpoint where the direction cofactor norm `m=N(U)` is comparable to `N=B/ell`, so the physical denominator `delta` is small and every individual fiber is already short.

Stage14-t37 attacks that endpoint arithmetically.  The main new points are:

1. the physical norm relation has a second exact divisor parameter `h`;
2. after reducing `(delta,h)`, the direction and cover cofactors have a common Gaussian norm core `t`;
3. equal-norm Gaussian cofactors split canonically into a same-orientation factor `R` and an opposite-orientation factor `S`;
4. the Stage14 squareclass then factors into one quartic squareclass in `R` and one in `S`;
5. each one-variable squareclass has `B^{o(1)}` collision multiplicity by the same rational-2-torsion bounded-height mechanism used in t22/t36;
6. combining the new packet estimate with the reverse form of t36 gives a uniform fixed-`ell` shell bound
   \[
   R_{\ell,M}\ll (B/\ell)^{5/6}B^{o(1)}.
   \]

Thus the **entire norm-index problem is power-saving once `ell` is fixed**.  The remaining global obstruction is now the summation over the moving canonical prime `ell`, especially the large-`ell` / tiny-cofactor regime `B/ell=O(1)`.

No global `A_{1,1}` or `T=o(sqrt(B))` claim is made in t37.

## 1. Exact second divisor parameter

Recall the t32 norm skeleton

\[
N(U)=m,\qquad N(V)=n=k\delta,\qquad k\mid\varepsilon m,
\]

with

\[
k=\gcd(n,\varepsilon m).
\]

Define

\[
\boxed{h=\frac{\varepsilon m}{k}.}
\tag{37.1}
\]

Then

\[
n=k\delta,\qquad \varepsilon m=kh,
\]

and the definition of `k` gives the exact coprimality

\[
\boxed{\gcd(\delta,h)=1.}
\tag{37.2}
\]

Hence

\[
\boxed{\frac nm=\frac{\varepsilon\delta}{h}.}
\tag{37.3}
\]

Let

\[
g=\gcd(\varepsilon,h),\qquad
A_0=\frac{\varepsilon\delta}{g},\qquad
B_0=\frac hg.
\]

Then `(A0,B0)=1`, and there is an integer common core `t` such that

\[
\boxed{m=B_0t,\qquad n=A_0t.}
\tag{37.4}
\]

This is exact, not an asymptotic approximation.

## 2. Primitive Gaussian norm restrictions

Both `U` and `V` are primitive Gaussian integers.  Therefore every odd rational prime dividing either `m` or `n` is `1 mod 4`, and

\[
v_2(m),v_2(n)\le1.
\]

Consequently the reduced packet norms `A0`, `B0` and the common core `t` inherit the same sum-of-two-squares admissibility after the finite allocation of the ramified prime `2`.

The super-square-root hypothesis gives a stronger separation than was previously recorded.  Since

\[
B_{\min}=\frac{\varepsilon\ell m\delta}{2}\le B
\]

and

\[
\ell^2>4B,
\]

we obtain

\[
\boxed{\ell>2\varepsilon m\delta.}
\tag{37.5}
\]

As `n=k delta<=epsilon m delta`, this implies

\[
\boxed{\ell>2m,\qquad \ell>2n.}
\tag{37.6}
\]

Thus the canonical prime is completely separated from every Gaussian cofactor norm in this branch.

## 3. Reverse fixed-cover squareclass energy

The quartic used in t36 is symmetric enough to run the same argument in the opposite direction.  Fix a primitive cover slope

\[
x=\frac pq.
\]

For a direction slope `y=a/b`,

\[
F_{a,b}(p,q)
=b^4\,(p^2-y^2q^2)(q^2-y^2p^2).
\]

Hence its squareclass as a function of `y` is represented by

\[
\boxed{g_{p,q}(y)=(p^2-y^2q^2)(q^2-y^2p^2).}
\tag{37.7}
\]

The branch points are

\[
y=\pm p/q,\qquad y=\pm q/p,
\]

so the pairwise squareclass-collision curve again has four rational branch points and full rational `2`-torsion.  The t22/t36 uniform bounded-height argument therefore gives, for a fixed cover state `V`,

\[
\boxed{E_V^{\rm rev}\le K_V B^{o(1)},}
\tag{37.8}
\]

where `K_V` is the number of physical directions paired with `V`.

Thus target points in a reverse fiber satisfy

\[
\boxed{R_V\le K_V^{1/2}B^{o(1)}.}
\tag{37.9}
\]

This reverse estimate is the tool that controls the large-`h` part below.

## 4. Equal-norm Gaussian orientation decomposition

Fix one packet `(epsilon,delta,h,A0,B0)` and one finite allocation state for the prime factors of `A0` and `B0`.

Choose Gaussian divisors

\[
\beta\mid U,\qquad N(\beta)=B_0,
\]

and

\[
\alpha\mid V,\qquad N(\alpha)=A_0.
\]

Then

\[
U=\beta Z_1,\qquad V=\alpha Z_2,
\]

with

\[
N(Z_1)=N(Z_2)=t.
\]

Because primitive Gaussian integers contain only one prime above each split rational prime, compare the Gaussian orientations of `Z1` and `Z2` prime by prime.  Put primes with the same orientation into `R`, and primes with opposite orientations into `S`.  Up to units,

\[
\boxed{Z_1=RS,\qquad Z_2=R\bar S,}
\tag{37.10}
\]

with

\[
\boxed{N(R)N(S)=t.}
\tag{37.11}
\]

The finite unit choices and the allocation choices for `alpha,beta` cost only `B^{o(1)}` states.

## 5. Exact common-core squareclass factorization

Let

\[
\pi\bar\pi=\ell
\]

be the canonical Gaussian prime, and write the actual direction complex number as

\[
A_c=a+ib=\pi U.
\]

The cover complex number has the uniform form

\[
P_c=p+iq=\eta V,
\]

where

```text
visible, same Gaussian orientation:      eta = pi
visible, opposite Gaussian orientation:  eta = bar(pi)
invisible:                               eta = 1
```

Define, for a Gaussian coefficient `c` and Gaussian variable `z`,

\[
\boxed{\Phi_c(z)=\Re(cz^2)\Im(cz^2).}
\tag{37.12}
\]

The two exact complex identities are

\[
A_c\overline{P_c}=g_4+i g_1,
\qquad
A_cP_c=-g_3+i g_2.
\]

Using (37.10), set

\[
c_S=\pi\bar\eta\,\beta\bar\alpha,
\qquad
c_R=\pi\eta\,\beta\alpha.
\]

Then

\[
A_c\overline{P_c}=c_S N(R)S^2,
\qquad
A_cP_c=c_R N(S)R^2.
\]

Therefore

\[
\boxed{
F=g_1g_2g_3g_4
=-\bigl(N(R)N(S)\bigr)^2\Phi_{c_R}(R)\Phi_{c_S}(S).
}
\tag{37.13}
\]

The norm factor is a rational square.  Hence the Stage14 target squareclass separates exactly:

\[
\boxed{
[F]=[-\Phi_{c_R}(R)\Phi_{c_S}(S)].
}
\tag{37.14}
\]

This is the corrected integral Gaussian `spin packet` behind the short-fiber endpoint.

## 6. One-variable spin squareclass collision

Write `c=u+iv` and `z=x+iy`.  In the slope coordinate `r=x/y`,

\[
y^{-4}\Phi_c(x+iy)
=
\bigl(u(r^2-1)-2vr\bigr)
\bigl(v(r^2-1)+2ur\bigr).
\tag{37.15}
\]

This is a product of two rational quadratic polynomials.  For a fixed reference slope `r'`, equality of squareclasses is represented by a quartic genus-one twist

\[
Y^2=d\,Q_1(r)Q_2(r).
\]

The rational factorization into the two quadratics gives a rational `2`-torsion divisor on the Jacobian; the reference point makes the twist an elliptic curve.  Its coefficient height and the physical point heights are `B^{O(1)}`.  The same t22 uniform bounded-height theorem therefore gives

\[
\boxed{
\#\{z:[\Phi_c(z)]=[\Phi_c(z')],\ H(z)\le B^{O(1)}\}
\le B^{o(1)}
}
\tag{37.16}
\]

uniformly in the packet coefficient `c`.

## 7. Fixed `(delta,h)` packet count

Let

\[
m\asymp M,
\qquad
N=\frac B\ell.
\]

For fixed `delta,h`, equation (37.4) gives

\[
t\asymp \frac{M}{B_0}\asymp\frac Mh
\]

up to absolute factors from `epsilon` and `g`.

Decompose

\[
N(R)\asymp R_0,
\qquad
N(S)\asymp S_0,
\qquad
R_0S_0\asymp t.
\]

There are `O(R0)` Gaussian integers in the first annulus and `O(S0)` in the second.  By (37.14)--(37.16), fixing one side determines only `B^{o(1)}` points on the other side with the matching squareclass.  Hence the number of target states in one dyadic orientation box is

\[
\ll \min(R_0,S_0)B^{o(1)}.
\]

Summing the `O(log B)` dyadic factorizations of `t`,

\[
\boxed{
R_{\delta,h}\ll \sqrt{M/h}\,B^{o(1)}.
}
\tag{37.17}
\]

## 8. Small-`h` / large-`h` decomposition

The physical scale gives

\[
\delta\ll \frac NM.
\tag{37.18}
\]

Choose a threshold `H`.

For `h<=H`, summing (37.17) over the `O(N/M)` possible `delta` layers and over `h` gives

\[
\boxed{
R_{h\le H}
\ll
N\sqrt{H/M}\,B^{o(1)}.
}
\tag{37.19}
\]

For `h>H`, equation (37.3) gives

\[
n=\frac{\varepsilon m\delta}{h}\ll \frac NH.
\]

Thus all such cover cofactors `V` lie in a Gaussian disk containing only

\[
O(N/H)
\]

integer points.  The total ambient mass of the shell is `<=N B^{o(1)}`.  Applying the reverse squareclass estimate (37.9) and Cauchy gives

\[
\boxed{
R_{h>H}
\ll \frac N{\sqrt H}B^{o(1)}.
}
\tag{37.20}
\]

Balance (37.19) and (37.20) with

\[
H=M^{1/2}.
\]

Then

\[
\boxed{
R^{\rm packet}_{\ell,M}
\ll N M^{-1/4}B^{o(1)}.
}
\tag{37.21}
\]

This estimate is strongest precisely where the t36 fiber estimate is weakest.

## 9. Combine with t36: uniform fixed-ell power saving

Stage14-t36 gave

\[
R^{\rm fiber}_{\ell,M}
\ll \sqrt{MN}\,B^{o(1)}
=N\sqrt{M/N}\,B^{o(1)}.
\tag{37.22}
\]

Combining (37.21) and (37.22),

\[
\boxed{
R_{\ell,M}
\ll
N\min\!\left(\sqrt{M/N},M^{-1/4}\right)B^{o(1)}.
}
\tag{37.23}
\]

The two factors are equal when

\[
M=N^{2/3}.
\]

Therefore, uniformly for every shell `1<=M<=N`,

\[
\boxed{
R_{\ell,M}
\ll N^{5/6}B^{o(1)}.
}
\tag{37.24}
\]

There are only `O(log B)` dyadic `M` shells, so for one fixed canonical super-square-root prime,

\[
\boxed{
R_\ell(B)
\ll
\left(\frac B\ell\right)^{5/6}B^{o(1)}.
}
\tag{37.25}
\]

In particular, the fixed-`ell` norm-index hyperbola now has a genuine fixed power saving relative to its ambient mass `B/ell`.

## 10. What remains: summation over the canonical prime

Equation (37.25) does **not** close the global Stage14 problem.  A separate bound for every `ell` is too weak when summed over all possible canonical primes.

The difficult endpoint is now especially transparent:

\[
N=\frac B\ell=O(1),
\]

so `m,n,delta,h,R,S` all belong to finitely many/small cofactor packets while the Gaussian prime `pi` itself moves through a long family.  In that range the target condition (37.14) becomes a moving-prime Gaussian spin condition.

Thus the next stage must average **across `ell`** rather than improve the already power-saving fixed-`ell` estimate.

A nearby literature is the spin-of-prime-ideals / Gaussian-spin technology.  However the general Friedlander--Iwaniec--Mazur--Rubin theorem is formulated for cyclic extensions of degree at least three, and the paper explicitly notes that the involution/degree-two case behaves differently.  Therefore it is a structural guide, not a theorem that can simply be quoted for `Q(i)` here.

## 11. Frozen diagnostics

The t36 frozen population is regenerated at

```text
B=10000, a,b,p,q<=40.
```

The exact common-core identities hold on all 1120 states:

```text
states checked                       1120
primitive Gaussian norm checks       2240
unique (epsilon,delta,h,A0,B0) packets 31
```

Frozen denominator and `h` distributions are

```text
delta: 1:232, 5:456, 13:176, 17:116, 25:64, 29:44, 37:20, 41:12
h:     1:398, 2:676, 5:24, 10:22
B0:    1:790, 2:284, 5:46
t:     1:882, 2:130, 5:108
```

Every frozen state satisfies

```text
gcd(delta,h)=1
m=B0*t
n=A0*t
ell > 2*epsilon*m*delta
ell > 2*m and ell > 2*n
```

The reverse squareclass audit gives

```text
ordered cover-slope fibers             216
max reverse fiber                       110
reverse squareclass collision energy   1132
max reverse squareclass multiplicity      2
nontrivial duplicate unordered pairs      6
```

Synthetic exact Gaussian packet checks verify (37.13) in all three visible/invisible orientation modes.

The optimization identity is frozen at perfect-power samples:

```text
N=64     worst M=16    bound=32    =N^(5/6)
N=729    worst M=81    bound=243   =N^(5/6)
N=4096   worst M=256   bound=1024  =N^(5/6)
N=15625  worst M=625   bound=3125  =N^(5/6)
```

These computations are diagnostics only; the asymptotic claims are the algebraic bounds (37.17)--(37.25).

## Boundary

```text
STAGE14_T37=COMPLETE_COMMON_CORE_SPIN_FACTORIZATION_AND_FIXED_ELL_POWER_SAVING
REVERSE_FIXED_COVER_SQUARECLASS_ENERGY=K*B^o(1)
DELTA_H_COMMON_CORE_IDENTITY=true
SUPER_SQRT_ELL_SEPARATES_COFACTOR_NORMS=true
EQUAL_NORM_GAUSSIAN_ORIENTATION_DECOMPOSITION=true
COMMON_CORE_SQUARECLASS_FACTORIZATION=true
ONE_VARIABLE_SPIN_SQUARECLASS_COLLISION=B^o(1)
SMALL_H_PACKET_BOUND=N*sqrt(H/M)*B^o(1)
LARGE_H_REVERSE_BOUND=N/sqrt(H)*B^o(1)
PACKET_OPTIMIZED_BOUND=N*M^(-1/4)*B^o(1)
FIXED_ELL_SHELL_COMBINED_BOUND=N*min(sqrt(M/N),M^(-1/4))*B^o(1)
FIXED_ELL_SHELL_UNIFORM_BOUND=N^(5/6)*B^o(1)
FIXED_ELL_NORM_INDEX_POWER_SAVING_PROVED=true
CANONICAL_PRIME_SUM_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t38 average the common-core Gaussian spin packets over the moving canonical prime ell, with special attention to the N=B/ell=O(1) prime-family endpoint; identify a Gaussian-prime bilinear/spin estimate that is actually valid in the degree-two Q(i) setting
```
