# Stage14-t36 — fixed-direction squareclass energy and fiber square-root saving

## Purpose

Stage14-t35 removed the artificial `sqrt(M)` loss caused by independent tensorisation.  It showed that a same-modulus auxiliary prime `varpi` with `lambda=N(varpi)>8M` injects the `U`-variable into an exact Gaussian-unit orbit, leaving a fixed-`U` fiber in the cover variable `V`.

The remaining problem was to obtain **signed cancellation inside one fixed direction fiber** without discarding the physical norm coupling.

Stage14-t36 closes that fixed-direction problem by changing viewpoint once more: instead of estimating each auxiliary trace separately, it bounds the squareclass collision energy of the physical quartic.  The collision curve is a genus-one quadratic twist with four rational branch points, so the uniform bounded-height mechanism already established in Stage14-t22 applies uniformly to every twist.

This gives a genuine square-root bound in the size of each fixed-direction fiber.

The global Stage14 power saving is still not complete because the endpoint where the physical fiber has bounded length (`M` comparable to `N=B/ell`) receives no gain from a square-root-in-fiber estimate.

## 1. Fixed-direction quartic and squareclass

Fix one `(1,1)` direction `0<a<b`.  For a primitive physical ratio

\[
x=\frac pq,
\]

the t28 four-linear product is

\[
F_{a,b}(p,q)
=(b^2p^2-a^2q^2)(b^2q^2-a^2p^2).
\]

Define

\[
\boxed{
f_{a,b}(x)
=(b^2x^2-a^2)(b^2-a^2x^2).
}
\tag{36.1}
\]

Then

\[
\boxed{
F_{a,b}(p,q)=q^4 f_{a,b}(p/q).
}
\tag{36.2}
\]

Since `q^4` is a rational square, the squareclass of the physical cover value depends only on the rational slope:

\[
[F_{a,b}(p,q)]=[f_{a,b}(x)]\in\mathbf Q^*/\mathbf Q^{*2}.
\]

The physical interval

\[
\frac ab<\frac pq<\frac ba
\]

keeps all four linear factors nonzero, so no branch-point degeneracy occurs on the physical fiber.

## 2. Pairwise squareclass collision is a genus-one twist

Fix one physical slope `x'`.  Another slope `x` has the same squareclass exactly when

\[
f_{a,b}(x)f_{a,b}(x')\in\mathbf Q^{*2}.
\]

Equivalently, with `c=f_{a,b}(x') != 0`, the pair lies on

\[
\boxed{
C_{a,b,c}:\quad Y^2
=c(b^2X^2-a^2)(b^2-a^2X^2).
}
\tag{36.3}
\]

Its branch points are

\[
\boxed{
X=\pm\frac ab,\qquad X=\pm\frac ba.
}
\tag{36.4}
\]

They are four distinct rational points because `0<a<b`.  Thus (36.3) is a smooth genus-one curve with rational points and full rational `2`-torsion after choosing any branch point as origin.

An explicit transformation makes this completely transparent.  Move `X=a/b` to infinity by

\[
T=\frac1{X-a/b},\qquad Y_1=YT^2.
\]

Then

\[
Y_1^2=cT^4 f_{a,b}\!\left(\frac ab+\frac1T\right)
\]

is a cubic in `T`.  Its three finite roots are

\[
\boxed{
-\frac b{2a},\qquad
\frac{ab}{b^2-a^2},\qquad
-\frac{ab}{a^2+b^2}.
}
\tag{36.5}
\]

Hence the cubic has three rational roots for every nonzero twist parameter `c`.

## 3. Uniform bounded-height collision multiplicity

Stage14-t22 already established the following reusable project lemma:

> An elliptic curve over `Q` with a rational point of exact prime torsion, whose model height and counted-point height are `B^{O(1)}`, has at most `B^{o(1)}` rational points in the physical height window, uniformly in the curve.

The collision curves (36.3) satisfy exactly the same hypotheses.

For a physical point,

\[
H(x)=H(p/q)\le \sqrt{2B}
\]

by the t30 disk `p^2+q^2<=2B`.  For the frozen direction variables, `a,b<=B^{1/2+o(1)}`.  Also

\[
c=f_{a,b}(x')
\]

has rational height `B^{O(1)}` after clearing the fourth-power denominator of `x'`.  Under the transformation above, both the cubic model and the image point therefore have height `B^{O(1)}`.

Because (36.5) gives rational `2`-torsion uniformly, the t22 bounded-height theorem applies to every fixed `x'` and yields

\[
\boxed{
\#\{x:\ [f_{a,b}(x)]=[f_{a,b}(x')],\ H(x)\le B^{O(1)}\}
\le B^{o(1)}.
}
\tag{36.6}
\]

Primitive positivity makes a rational slope determine only boundedly many physical `(p,q)` lifts.  Therefore the same bound holds for physical cover states.

## 4. Fixed-direction squareclass energy

Let `H_{a,b}` be the physical fixed-direction fiber, and put

\[
J_{a,b}=|H_{a,b}|.
\]

For each squareclass `d`, let

\[
r_{a,b}(d)
=\#\{V\in H_{a,b}:[F_{a,b}(V)]=d\}.
\]

Define the collision energy

\[
E_{a,b}
=\sum_d r_{a,b}(d)^2
=\#\{(V,V')\in H_{a,b}^2:
F_{a,b}(V)F_{a,b}(V')\in\square\}.
\]

By (36.6), for every fixed `V'` there are only `B^{o(1)}` possible `V`.  Hence

\[
\boxed{
E_{a,b}\le J_{a,b}B^{o(1)}.
}
\tag{36.7}
\]

This is the signed-cancellation input that was missing in t35.  It is stronger than a positive residue-collision estimate because it controls precisely the pairs that survive every quadratic auxiliary character.

## 5. Square-root saving for target points in one fiber

Let

\[
R_{a,b}
=\#\{V\in H_{a,b}:F_{a,b}(V)\in\square\}.
\]

Every target point lies in the trivial squareclass, so all ordered pairs of target points are counted by `E_{a,b}`.  Therefore

\[
R_{a,b}^2\le E_{a,b}.
\]

Using (36.7),

\[
\boxed{
R_{a,b}
\le J_{a,b}^{1/2}B^{o(1)}.
}
\tag{36.8}
\]

Thus **signed fixed-direction fiber cancellation is proved** at the polynomial-exponent level.

This does not assert that an individual auxiliary-prime trace is always small.  It proves the stronger square-sieve statement that the common surviving squareclass has near-linear collision energy.

## 6. Projection to a fixed canonical-prime shell

Fix the canonical super-square-root prime `ell` and a dyadic cofactor shell

\[
m=N(U)\asymp M,
\qquad
N=\frac B\ell.
\]

The physical scale gives `M<=N`.  The number of possible directions in the shell is

\[
\ll M B^{o(1)}
\]

by the sum-of-two-squares divisor bound.  The t32/t35 norm skeleton gives total ambient fiber mass

\[
\sum_{a,b}J_{a,b}
\le N B^{o(1)}.
\]

Let `A_{ell,M}` denote the number of directions in this shell carrying at least one target point.  Since `1_{R>0}<=R`, (36.8) and Cauchy give

\[
\begin{aligned}
A_{\ell,M}
&\le \sum_{a,b}R_{a,b}\\
&\le B^{o(1)}\sum_{a,b}J_{a,b}^{1/2}\\
&\le B^{o(1)}
\left(\#\{a,b\}\sum_{a,b}J_{a,b}\right)^{1/2}.
\end{aligned}
\]

Hence

\[
\boxed{
A_{\ell,M}
\le \sqrt{MN}\,B^{o(1)}.
}
\tag{36.9}
\]

Relative to the ambient `N B^{o(1)}` shell mass, this saves the factor

\[
\sqrt{M/N}.
\]

In particular, for any fixed `eta>0`,

\[
M\le N B^{-2\eta}
\quad\Longrightarrow\quad
\boxed{
A_{\ell,M}\le N B^{-\eta+o(1)}.
}
\tag{36.10}
\]

So the **long-fiber range has a genuine fixed power saving**.

## 7. What remains: the short-fiber endpoint

The estimate (36.8) cannot save when `J_{a,b}=B^{o(1)}` already.  In shell language this is the endpoint

\[
M\asymp N=B/\ell,
\]

where the physical denominator variable

\[
\delta\ll N/M
\]

is bounded.

This is now the only obstruction inside the t30--t36 super-square-root architecture.  It is qualitatively different from the earlier analytic barriers:

- higher Mellin orders: closed in t34;
- independent tensor loss: closed in t35;
- fixed-direction signed squareclass cancellation: closed in t36;
- remaining endpoint: finitely many/small `delta` layers with short fibers.

The natural next attack is therefore arithmetic classification of the small-denominator layers, using the canonical-largest-prime Gaussian norm factorisation rather than another generic character sieve.

## 8. Frozen finite audit

At the t35 frozen cutoff

```text
B=10000, a,b,p,q<=40
```

t36 refines the 1120 states into exact `(a,b)` direction fibers:

```text
exact direction fibers                 137
states                                1120
max direction fiber                     32
squareclass collision energy          2240
max squareclass multiplicity             2
squareclass classes of multiplicity 2   560
reciprocal p/q <-> q/p pairs            560
transformed-cubic rational-root checks  411
```

Every frozen squareclass occurs exactly twice, and every duplicate is exactly the reciprocal symmetry

\[
(p,q)\leftrightarrow(q,p),
\]

consistent with

\[
f_{a,b}(1/x)=x^{-4}f_{a,b}(x).
\]

Thus the frozen energy attains the symmetry floor

\[
E_{\rm frozen}=2|H|=2240.
\]

This finite injectivity beyond the reciprocal symmetry is diagnostic only; the asymptotic theorem is (36.7), not an assertion that no other collisions ever occur.

For the same split auxiliary primes used in t35, the signed direction traces are:

```text
lambda   total trace   sum |fiber trace|   sum fiber trace^2   max |fiber trace|
 53          -58               342                 1380                12
 61          -76               384                 1672                 8
 73         -164               376                 1720                12
 89         -142               442                 2420                16
 97          -70               334                 1372                 8
```

These numbers are diagnostics only; the proof of (36.7)--(36.9) comes from the genus-one collision curve and the t22 uniform bounded-height theorem.

## Boundary

```text
STAGE14_T36=COMPLETE_FIXED_DIRECTION_SQUARECLASS_ENERGY_AND_FIBER_SQRT_SAVING
FIXED_DIRECTION_SQUARECLASS_COLLISION_CURVE_GENUS_ONE=true
COLLISION_CURVE_FULL_RATIONAL_2_TORSION=true
T22_UNIFORM_BOUNDED_HEIGHT_REUSED_FOR_COLLISIONS=true
FIXED_DIRECTION_SQUARECLASS_ENERGY=J*B^o(1)
SIGNED_TRACE_FIBER_CANCELLATION_PROVED=true
FIXED_DIRECTION_TARGET_FIBER_BOUND=sqrt(J)*B^o(1)
FIXED_ELL_SHELL_ACTIVE_DIRECTION_BOUND=sqrt(M*N)*B^o(1)
LONG_FIBER_POWER_SAVING_PROVED=true
SHORT_FIBER_ENDPOINT_POWER_SAVING_PROVED=false
NORM_INDEX_HYPERBOLIC_CORRELATION_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t37 attack the short-fiber endpoint M~N=B/ell, where delta is O(1), by classifying the finitely many small-denominator layers and exploiting canonical-largest-prime Gaussian norm structure
```
