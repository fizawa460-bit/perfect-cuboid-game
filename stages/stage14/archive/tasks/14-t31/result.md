# Stage14-t31 — Gaussian cofactor compression and moving auxiliary-prime sieve boundary

## Purpose

Stage14-t30 separated the canonical direction prime from the auxiliary character primes. Stage14-t31 now pushes the kernel-visible super-square-root branch into Gaussian cofactors and proves a genuine fixed-canonical-prime moving-family correlation saving.

The new structure is:

1. on the visible branch with `ell>2sqrt(B)`, both `a^2+b^2` and `p^2+q^2` contain `ell` to exact exponent one;
2. both norms descend through one Gaussian prime of norm `ell` to cofactors below `sqrt(B)`;
3. the physical scale condition becomes an exact divisor-coupled norm inequality;
4. a four-variable auxiliary-prime complete-correlation bound gives a real cofactor-box square-sieve power saving;
5. that box saving is still too weak after existential projection to active directions because it discards the thin norm/scale coupling;
6. the kernel-invisible Gaussian/dual state is only a local square-root selection at the canonical prime, not a rational congruence thinning of `(p,q)`.

No global `A_11` power saving is claimed here.

## 1. Exact exponent-one norm descent

Keep

\[
D=\frac{\varepsilon}{2}(a^2+b^2),\qquad C=\varepsilon ab,
\]

and the primitive cover ratio `(p,q)` with

\[
S=p^2+q^2\le2B.
\]

Let

\[
\ell=P^+(\Delta)_{\rm odd},\qquad
\Delta=2ab(b^2-a^2)(a^2+b^2).
\]

By t30, on a kernel-visible non-torsion point,

\[
\ell>2\sqrt B
\Longrightarrow
\ell\mid a^2+b^2,
\quad
\ell\mid p^2+q^2.
\]

Since `D<=B`,

\[
a^2+b^2=\frac{2D}{\varepsilon}\le2B.
\]

Because `ell^2>4B`, both divisibilities have exact exponent one. Thus

\[
\boxed{a^2+b^2=\ell m,\qquad p^2+q^2=\ell n}
\]

with

\[
\boxed{v_\ell(a^2+b^2)=v_\ell(p^2+q^2)=1,\qquad m,n<\sqrt B.}
\]

## 2. Exact physical scale compression

The t30 denominator formula is

\[
\operatorname{den}(Q)=\frac{S}{\gcd(S,2D)}.
\]

Now

\[
S=\ell n,\qquad 2D=\varepsilon\ell m,\qquad \ell\nmid mn,
\]

so

\[
\boxed{
\operatorname{den}(Q)=\frac{n}{\gcd(n,\varepsilon m)}.
}
\]

Put

\[
\delta=\frac{n}{\gcd(n,\varepsilon m)}.
\]

Since `delta|g` and the actual diagonal is `gD<=B`,

\[
\boxed{\frac{\varepsilon\ell m\delta}{2}\le B.}
\tag{31.1}
\]

Hence

\[
\boxed{m\delta\le\frac{2B}{\varepsilon\ell}<\frac{\sqrt B}{\varepsilon}.}
\tag{31.2}
\]

Writing

\[
k=\gcd(n,\varepsilon m),\qquad n=k\delta,
\]

we have `k|epsilon*m`. Thus for fixed `(ell,m)`, the allowed cover norm cofactors satisfy

\[
\boxed{n=k\delta,\qquad k\mid\varepsilon m,\qquad \delta\ll B/(\ell m).}
\]

This thin divisor-coupled norm condition is strictly stronger than the disk bound `p^2+q^2<=2B`.

## 3. Gaussian factorisation

Because `ell|a^2+b^2` with `(a,b)=1`,

\[
\ell\equiv1\pmod4.
\]

Choose

\[
\pi=s+it,\qquad N(\pi)=\ell.
\]

Exact exponent one implies that, up to a unit and conjugation,

\[
a+ib=\pi U,
\]

while

\[
p+iq=\pi V
\]

or

\[
p+iq=\bar\pi V,
\]

with

\[
\boxed{N(U)=m,\qquad N(V)=n.}
\]

The t29 matching identifies the orientation exactly:

- `{1,4}` means the same Gaussian prime orientation;
- `{2,3}` means opposite orientation.

Indeed,

\[
(a+ib)(p-iq)=g_4+i g_1,
\]

and

\[
(a+ib)(p+iq)=-g_3+i g_2.
\]

On the matched pair, the product is divisible by the rational prime `ell`.

Since every physical `g_i` is positive and

\[
g_i\le\sqrt{(a^2+b^2)(p^2+q^2)}\le2B<\ell^2,
\]

we obtain

\[
\boxed{v_\ell(g_i)=1}
\]

for each matched factor. Therefore the rational-even kernel-invisible subcase is impossible in the super-square-root range.

Thus the super-square-root `D` branch is exactly

```text
ell | p^2+q^2      -> rational matching, automatically kernel-visible
ell not | p^2+q^2  -> t26 Gaussian local-root branch, kernel-invisible
```

## 4. Good auxiliary primes survive Gaussian descent

Let

\[
F_{a,b}(p,q)
=(b^2p^2-a^2q^2)(b^2q^2-a^2p^2).
\]

On the visible Gaussian lattice, two matched factors contain one factor of `ell`, so

\[
\widetilde F_{\pi,U}(V)
:=\frac{F_{a,b}(p(V),q(V))}{\ell^2}
\]

is integral.

For an odd auxiliary prime `lambda` with

\[
\lambda\nmid\Delta,
\]

the Gaussian linear change `V -> (p,q)` has determinant `ell`, hence is invertible modulo `lambda`; division by `ell^2` is multiplication by a nonzero square. Therefore

\[
\boxed{
\chi_\lambda(\widetilde F_{\pi,U}(V))
=
\chi_\lambda(F_{a,b}(p(V),q(V))).
}
\]

The binary quartic remains squarefree/admissible because `disc(F)=Delta^4` on the ratio line. Pierce--Xu's admissible-form Burgess theorem is uniform in the coefficients of fixed-degree admissible forms, so moving Stage14 direction coefficients are not themselves an obstruction at a fixed good auxiliary prime.

## 5. Four-variable complete correlation

Fix `pi` and let `U,V` range modulo a good prime `lambda`.

For all but `O(lambda)` projective direction vectors `U`, the induced quartic in `V` is squarefree. The complete `V`-sum is then `O(lambda^(3/2))`: there are `lambda-1` scalar representatives for each projective ratio and the projective Weil sum is `O(sqrt(lambda))`. The exceptional `U` contribute trivially.

Therefore

\[
\boxed{
\left|
\sum_{U,V\bmod\lambda}
\chi_\lambda(\widetilde F_\pi(U,V))
\right|
\ll\lambda^{7/2}.
}
\tag{31.3}
\]

For two distinct good primes `lambda,mu`, CRT gives

\[
\boxed{|C_{\lambda\mu}|\ll(\lambda\mu)^{7/2}.}
\tag{31.4}
\]

This is a genuine moving-family correlation theorem: both the direction cofactor `U` and cover cofactor `V` move.

## 6. Cofactor-box square sieve

Let

\[
|\Re U|,|\Im U|\le H_U,
\qquad
|\Re V|,|\Im V|\le H_V,
\qquad H_U\le H_V.
\]

For auxiliary primes of size `L`, the pair modulus is `q~L^2`. Tiling the four-dimensional box by complete residue boxes modulo `q` and using (31.4) gives

\[
\boxed{
|S_{\lambda\mu}|
\ll
H_U^2H_V^2
\left(L^{-1}+\frac{L^2}{H_U}\right)B^{o(1)}.
}
\tag{31.5}
\]

The first term is complete square-root cancellation; the second is the boundary loss from the shortest side.

The quadratic-character second-moment detector has the same two-prime correlations. Balancing at

\[
L=H_U^{1/3}
\]

yields

\[
\boxed{
N_{\rm square}(H_U,H_V)
\ll H_U^2H_V^2H_U^{-1/3+o(1)}.
}
\tag{31.6}
\]

For a direction shell `X<D<=2X`,

\[
H_U^2\asymp X/\ell,
\qquad
H_V^2\ll B/\ell,
\]

so

\[
\boxed{
N_{\rm square,\ell}(X,B)
\ll B X^{5/6}\ell^{-11/6+o(1)}.
}
\tag{31.7}
\]

Hence t31 proves a fixed-canonical-prime moving-family square-sieve saving.

## 7. Why this still does not close the direction projection

The box sieve enlarges the physical set by forgetting (31.1), namely

\[
N(V)=n=k\delta,
\qquad
k\mid\varepsilon N(U),
\qquad
N(U)\delta\ll B/\ell.
\]

Summing the enlarged-box bound over `ell>2sqrt(B)` gives only

\[
\ll B^{7/12+o(1)}X^{5/6},
\]

which is not a useful upper bound for the active-direction first moment in the relevant shells. The next sieve must remain on the Gaussian norm circles/divisor-coupled scale set instead of replacing it by full cofactor boxes.

Thus the precise remaining loss is now identified: **norm-circle projection plus physical scale coupling**, not lack of auxiliary local cancellation.

## 8. Kernel-invisible local-root state

The t26 Gaussian/dual routes do not provide a rational `(p,q)` line when the canonical prime is kernel-invisible.

For example, if `ell^e|D`, then

\[
W^2+C^2S^2=(2Dpq)^2
\]

gives

\[
W^2\equiv-C^2S^2\pmod{\ell^{2e}}.
\]

For a split prime with `rho^2=-1`, the states

\[
W\equiv\pm\rho CS\pmod{\ell^{2e}}
\]

are simply the two local square-root sections. They do not impose an additional rational congruence on `(p,q)`.

The same interpretation applies to the split `r/u` Gaussian state and the `C`-column dual state. Thus on the kernel-invisible branch the canonical prime is a local root label, not an incidence-saving modulus.

The global square detector is again the auxiliary good-prime family

\[
\chi_\lambda(F_{a,b}(p,q)),
\qquad \lambda\nmid\Delta,
\]

with the `ell`-adic root label carried independently by CRT.

## 9. Frozen diagnostics

The deterministic t31 audit reuses `a,b,p,q<=40`. On every non-torsion visible incidence with

\[
\ell^2>4B_{\min},
\]

it verifies exact norm descent, scale descent, Gaussian orientation, and exact `ell`-adic valuation one on the matched factors.

It also checks the invisible `D`/sum residual directly: for every no-linear-factor sum-column tuple in the frozen box, the t26 Gaussian root `W=±rho*C*S (mod ell^2)` is a local root of the cover polynomial. This confirms that the invisible state is local-root selection rather than rational `(p,q)` thinning.

## Boundary

```text
STAGE14_T31=COMPLETE_GAUSSIAN_COFACTOR_AND_MOVING_AUXILIARY_CORRELATION_BOUNDARY
SUPER_SQRT_VISIBLE_NORMS_HAVE_ELL_EXACT_EXPONENT_ONE=true
SUPER_SQRT_VISIBLE_GAUSSIAN_COFACTOR_COMPRESSION=true
SUPER_SQRT_MATCHED_G_FACTORS_HAVE_ELL_EXACT_EXPONENT_ONE=true
SUPER_SQRT_RATIONAL_EVEN_INVISIBLE_BRANCH_EMPTY=true
PHYSICAL_SCALE_COFACTOR_IDENTITY=true
PHYSICAL_SCALE_THIN_NORM_CONDITION=true
GOOD_AUXILIARY_ADMISSIBILITY_SURVIVES_GAUSSIAN_DESCENT=true
FIXED_ELL_MOVING_FAMILY_COMPLETE_CORRELATION_POWER_SAVING=true
FIXED_ELL_COFACTOR_BOX_SQUARE_SIEVE_POWER_SAVING=true
FIXED_ELL_BOX_SIEVE_EXPONENT=H_U^(-1/3+o(1))
BOX_SIEVE_CLOSES_DIRECTION_PROJECTION=false
INVISIBLE_CANONICAL_PRIME_GIVES_RATIONAL_PQ_INCIDENCE=false
INVISIBLE_GOOD_AUXILIARY_SQUARE_SIEVE_OBJECT_DEFINED=true
VISIBLE_BRANCH_POWER_SAVING_PROVED=false
INVISIBLE_BRANCH_POWER_SAVING_PROVED=false
JOINT_COVER_CONDITIONED_SMOOTH_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t32 auxiliary-character sieve on Gaussian norm circles with n=k*delta, k|epsilon*m and m*delta<<B/ell; compare visible rational and invisible local-root states without enlarging to full cofactor boxes
```
