# Stage14-t32 — split-prime torus sieve on the unified Gaussian norm skeleton

## Purpose

Stage14-t31 obtained auxiliary-character cancellation on full Gaussian cofactor boxes but lost the physical coupling

\[
N(V)=k\delta,\qquad k\mid\varepsilon N(U),\qquad N(U)\delta\ll B/\ell.
\]

Stage14-t32 keeps this coupling. The new output is an exact unification of the super-square-root visible and invisible D/sum states, plus a much stronger complete auxiliary-character bound on fixed Gaussian norm circles.

## 1. Visible and invisible states have the same norm skeleton

On the super-square-root D/sum branch,

\[
\ell>2\sqrt B,
\qquad a^2+b^2=\ell m,
\qquad a+ib=\pi U,
\qquad N(\pi)=\ell,
\qquad N(U)=m.
\]

For the visible rational branch, `ell|S=p^2+q^2`, so exact exponent one gives

\[
S=\ell n,
\qquad n=k\delta,
\qquad k=\gcd(n,\varepsilon m),
\]

and after dividing `p+iq` by the correct orientation of `pi`,

\[
N(V)=k\delta.
\]

For the kernel-invisible D/sum residual, `ell` does not divide `S`. Therefore

\[
\operatorname{den}(Q)
=\frac{S}{\gcd(S,\varepsilon\ell m)}
=\frac{S}{\gcd(S,\varepsilon m)}.
\]

Writing

\[
k=\gcd(S,\varepsilon m),\qquad \delta=S/k,
\]

and now taking `V=p+iq`, again

\[
N(V)=k\delta.
\]

Both branches therefore satisfy the identical cofactor skeleton

\[
\boxed{
N(U)=m,
\qquad N(V)=k\delta,
\qquad k\mid\varepsilon m,
\qquad \frac{\varepsilon\ell m\delta}{2}\le B.
}
\tag{32.1}
\]

The canonical `ell`-adic datum is now only a bounded state label: Gaussian orientation on the visible branch, local square-root sign on the invisible branch.

Since

\[
r_2(r)\le4\tau(r)=r^{o(1)},
\]

each fixed norm layer has only subpolynomially many Gaussian representatives. On a shell `X<D<=2X`, one has `m~X/ell` and `delta<<B/X`, so the unsieved mass at one fixed canonical prime is

\[
\boxed{\mathcal M_\ell(X,B)\ll (B/\ell)B^{o(1)}.}
\tag{32.2}
\]

This removes the full-box enlargement from t31, but summing (32.2) over all possible canonical primes still does not close the active-direction count.

## 2. Inert auxiliary primes can resonate on norm circles

The t30 condition `lambda` not dividing `Delta` is enough for the unrestricted quartic, but not for a uniform fixed-norm-circle estimate.

A frozen counterexample is

\[
\pi=1+2i,\qquad \lambda=11,\qquad N(U)=1,\qquad N(V)=2.
\]

For the same Gaussian orientation the complete norm-circle product has `(11+1)^2=144` points and every point contributes the same nonzero quadratic-character value. Hence

\[
\boxed{|C_{11}(1,2)|=144.}
\]

Thus inert auxiliary primes can be maximally resonant. Stage14-t32 therefore restricts the torus sieve to

\[
\boxed{\lambda\equiv1\pmod4,\qquad \lambda\nmid\ell\Delta mn.}
\tag{32.3}
\]

## 3. Split norm circles are one-dimensional tori

Choose `iota^2=-1 mod lambda`. For a nonzero norm `R`, write

\[
s=x+\iota y,\qquad x-\iota y=R/s.
\]

Then

\[
x=\frac{s+R/s}{2},\qquad y=\frac{s-R/s}{2\iota}.
\]

For a nonzero Gaussian constant `c`, with split components `c_+,c_-`,

\[
\boxed{
\Re(cz)\Im(cz)
=\frac{c_+^2s^4-c_-^2R^2}{4\iota s^2}.
}
\tag{32.4}
\]

The numerator is a squarefree quartic. Therefore the untwisted one-variable character sum is bounded by `3 sqrt(lambda)`. After inserting the quadratic torus character, the relevant polynomial has degree five and the bound is `4 sqrt(lambda)`.

## 4. Exact two-torus factorisation

After the Gaussian descent, the Stage14 four-linear character is, up to a fixed square/sign, a product of two terms of the form

\[
\Re(c_1U\bar V)\Im(c_1U\bar V),
\qquad
\Re(c_2UV)\Im(c_2UV),
\]

with nonzero constants `c_1,c_2`. This holds for both visible orientations and for the invisible local-root state.

Write

\[
U=U_0s,\qquad V=V_0t
\]

on the split norm-one torus. The two arguments depend on

\[
r=s/t,\qquad w=st.
\]

The map `(s,t)->(r,w)` has kernel `{(1,1),(-1,-1)}` and image characterised by `rw` being a square. Hence

\[
\boxed{
\sum_{s,t}A(s/t)B(st)
=
\Big(\sum A\Big)\Big(\sum B\Big)
+
\Big(\sum\eta A\Big)\Big(\sum\eta B\Big).
}
\tag{32.5}
\]

Combining the `3 sqrt(lambda)` and `4 sqrt(lambda)` one-variable bounds yields

\[
\boxed{|C_\lambda(m,n)|\le25\lambda.}
\tag{32.6}
\]

For two distinct split good primes, CRT gives

\[
\boxed{|C_{\lambda\mu}(m,n)|\le625\lambda\mu.}
\tag{32.7}
\]

This is full square-root cancellation relative to the `~lambda^2` points on the product of two norm circles and is much stronger than t31's unrestricted four-variable complete estimate.

## 5. Exact remaining analytic object

The angular complete correlation is now closed. The remaining sum is the incomplete arithmetic average

\[
\boxed{
\Sigma_{\lambda,\mu}(\ell;X,B)
=
\sum_{m\asymp X/\ell}
\sum_{\delta\ll B/X}
\sum_{k\mid\varepsilon m}
\sum_{\substack{N(U)=m\\N(V)=k\delta}}
\chi_{\lambda\mu}(\widetilde F_\ell(U,V)),
}
\tag{32.8}
\]

with the canonical-largest-prime condition, physical interval/reconstruction and the bounded visible/invisible state label retained.

A complete finite-field torus estimate cannot simply replace (32.8): an integral norm circle has only `r_2(n)=n^o(1)` representatives. The missing theorem is therefore a large-sieve estimate over the **Gaussian norm indices and representations**, not another local Weil bound.

Goldmakher--Louvel's quadratic large sieve over number fields is structurally relevant and includes the `Q(i)` setting, but Stage14 still needs to identify the character in (32.8) with the required quadratic Hecke-family symbol while preserving `k|epsilon*m`, the hyperbolic cutoff, canonical `ell`, and the existential direction projection. That transfer is not claimed here.

## 6. Frozen diagnostics

The t32 audit keeps `a,b,p,q<=40` and checks the unified skeleton on every super-square-root D/sum non-torsion tuple:

```text
visible non-torsion states        1018
invisible non-torsion states     12190
unified cofactor checks          13208

visible delta=1                    676
visible delta>1                    342
invisible delta=1                  230
invisible delta>1                11960
```

For `pi=1+2i`, every nonzero norm pair is checked for both orientations at split auxiliary primes:

```text
lambda   max |C_lambda|
  13          64
  17         160
  29         144
  37          16
  41         288
```

All satisfy `|C_lambda|<=25 lambda`. The inert resonance is frozen at `lambda=11`, `m=1`, `n=2`, where `|C_11|=144=(11+1)^2`.

## Boundary

```text
STAGE14_T32=COMPLETE_SPLIT_TORUS_NORM_CORRELATION_AND_UNIFIED_COFACTOR_SKELETON
VISIBLE_INVISIBLE_SUPER_SQRT_NORM_SKELETON_UNIFIED=true
UNIFIED_NORM_SKELETON=N(U)=m,N(V)=k*delta,k|epsilon*m,m*delta<<B/ell
FIXED_ELL_UNSIEVED_NORM_MASS=B/ell*B^o(1)
INERT_AUXILIARY_NORM_CIRCLE_RESONANCE_EXISTS=true
SPLIT_AUXILIARY_PRIME_RESTRICTION_REQUIRED_FOR_TORUS_BOUND=true
SPLIT_NORM_CIRCLE_PARAMETERIZATION=true
SPLIT_TORUS_TWO_FACTOR_IDENTITY=true
SPLIT_GOOD_PRIME_NORM_CIRCLE_CORRELATION=O(lambda)
SPLIT_GOOD_TWO_PRIME_NORM_CIRCLE_CORRELATION=O(lambda*mu)
ANGULAR_COMPLETE_CORRELATION_CLOSED=true
GAUSSIAN_HECKE_LARGE_SIEVE_TRANSFER_PROVED=false
NORM_INDEX_HYPERBOLIC_CORRELATION_POWER_SAVING_PROVED=false
VISIBLE_BRANCH_POWER_SAVING_PROVED=false
INVISIBLE_BRANCH_POWER_SAVING_PROVED=false
JOINT_COVER_CONDITIONED_SMOOTH_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t33 convert the split-torus character into a quadratic Hecke-family symbol over Q(i) and prove a large-sieve bound for the divisor-coupled norm-index sum Sigma(lambda,mu;ell;X,B)
```
