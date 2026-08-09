# Stage14-t32 — split-prime torus sieve on the unified Gaussian norm skeleton

## Purpose

Stage14-t31 proved a genuine auxiliary-character saving on full Gaussian cofactor boxes, but that argument discarded the physical norm coupling

\[
N(V)=k\delta,\qquad k\mid\varepsilon N(U),\qquad N(U)\delta\ll B/\ell.
\]

Stage14-t32 keeps this coupling. The main conclusions are:

1. the super-square-root visible rational branch and the super-square-root kernel-invisible local-root branch have the **same Gaussian cofactor norm skeleton**;
2. after restricting auxiliary primes to split primes `lambda = 1 mod 4`, the complete character correlation on fixed Gaussian norm circles improves from the t31 four-variable bound `O(lambda^(7/2))` to
   \[
   \boxed{O(\lambda)};
   \]
3. inert auxiliary primes can be maximally resonant on fixed norm circles, so the split-prime restriction is mathematically necessary for this torus argument;
4. the remaining obstruction is no longer angular cancellation. It is the incomplete hyperbolic norm-index sum over `(m,delta,k)` together with the canonical largest-prime selection.

No global `A_{1,1}` power saving is claimed in t32.

## 1. One cofactor skeleton for visible and invisible states

Keep the super-square-root D/sum branch

\[
\ell>2\sqrt B,
\qquad
D=\frac{\varepsilon}{2}(a^2+b^2),
\qquad
\ell\mid a^2+b^2.
\]

As in t31,

\[
a^2+b^2=\ell m,
\qquad \ell\nmid m.
\]

Write

\[
a+ib=\pi U,\qquad N(\pi)=\ell,\qquad N(U)=m.
\]

### 1.1 Visible rational branch

Visibility is equivalent to

\[
\ell\mid S:=p^2+q^2.
\]

Exact exponent one gives

\[
S=\ell n,
\qquad n=k\delta,
\qquad k=\gcd(n,\varepsilon m),
\qquad k\mid\varepsilon m.
\]

After dividing `p+iq` by the appropriate orientation of `pi`, write

\[
p+iq=\pi^{\pm}V,
\qquad
\boxed{N(V)=k\delta}.
\]

The physical denominator is `delta`, so

\[
\boxed{
\frac{\varepsilon\ell m\delta}{2}\le B.
}
\tag{32.1}
\]

### 1.2 Kernel-invisible local-root branch

On the D/sum residual branch t31 showed

\[
\ell\nmid S.
\]

Now

\[
\operatorname{den}(Q)
=\frac{S}{\gcd(S,\varepsilon\ell m)}
=\frac{S}{\gcd(S,\varepsilon m)}.
\]

Put

\[
k=\gcd(S,\varepsilon m),
\qquad
\delta=S/k.
\]

Then again

\[
\boxed{k\mid\varepsilon m,\qquad S=k\delta,}
\]

and, now taking the raw cover Gaussian integer

\[
V=p+iq,
\]

we have

\[
\boxed{N(V)=k\delta}
\]

with exactly the same scale condition (32.1).

Thus the two branches differ only in the canonical `ell`-adic state:

```text
visible:
  p+iq carries pi or bar(pi), then descend by that Gaussian prime;

invisible:
  p+iq carries no pi factor; the t26 state is only W = +/- rho C S mod ell^2.
```

After choosing the appropriate cofactor variable `V`, both branches live on the same norm skeleton

\[
\boxed{
N(U)=m,
\qquad
N(V)=k\delta,
\qquad
k\mid\varepsilon m,
\qquad
m\delta\le\frac{2B}{\varepsilon\ell}.
}
\tag{32.2}
\]

This is the first exact unification of the visible and invisible super-square-root D/sum states.

## 2. Representation multiplicity is already subpolynomial

For every positive integer `r`,

\[
r_2(r)=\#\{(x,y)\in\mathbb Z^2:x^2+y^2=r\}\le4\tau(r).
\]

Hence each fixed norm layer in (32.2) contains only `B^o(1)` Gaussian `U` and `V` representatives.

On a direction shell `X<D<=2X`,

\[
m\asymp X/\ell,
\qquad
\delta\ll B/X.
\]

After the divisor choice `k|epsilon*m`, the entire unsieved cofactor mass at one fixed canonical prime satisfies

\[
\boxed{
\mathcal M_\ell(X,B)
\ll \frac{B}{\ell}B^{o(1)}.
}
\tag{32.3}
\]

Thus the full-box loss from t31 is removed: the correct ambient object is already hyperbolic and essentially two-dimensional in the norm variables.

However, summing (32.3) over all possible super-square-root canonical primes still does not produce a fixed power saving for the active-direction first moment. Character cancellation must therefore act on the norm-indexed family itself.

## 3. Why auxiliary primes are restricted to `lambda = 1 mod 4`

The t30 good-prime condition `lambda not | Delta` is sufficient for the unrestricted quartic. On fixed norm circles there is one further issue: inert primes can create angular resonance.

A frozen counterexample is

\[
\ell=5,\qquad \pi=1+2i,
\qquad \lambda=11,
\qquad N(U)=1,
\qquad N(V)=2.
\]

For the same Gaussian orientation, every one of the `(lambda+1)^2=144` norm-circle pairs has the same nonzero quadratic-character value, so the complete correlation has absolute value

\[
\boxed{144=(11+1)^2.}
\]

Thus there is **no uniform square-root cancellation on norm circles over inert auxiliary primes**.

Stage14-t32 therefore uses only split auxiliary primes

\[
\boxed{\lambda\equiv1\pmod4,\qquad \lambda\nmid\ell\Delta mn.}
\tag{32.4}
\]

This loses only a fixed-density prime subfamily and removes the torus resonance.

## 4. Split norm circles become a one-dimensional torus

Fix a split auxiliary prime `lambda` and choose

\[
\iota^2=-1\pmod\lambda.
\]

For a nonzero norm `R`, the circle

\[
x^2+y^2=R
\]

is identified with `F_lambda^*` by

\[
s=x+\iota y,
\qquad
x-\iota y=R/s.
\]

Hence

\[
x=\frac{s+R/s}{2},
\qquad
y=\frac{s-R/s}{2\iota}.
\]

For any nonzero Gaussian constant `c` with split components

\[
c_+=c_x+\iota c_y,
\qquad c_-=c_x-\iota c_y,
\]

we obtain

\[
\boxed{
\Re(cz)\Im(cz)
=\frac{c_+^2s^4-c_-^2R^2}{4\iota s^2}.
}
\tag{32.5}
\]

The denominator is a square for the Legendre symbol. Since `c_+c_-R != 0`, the numerator is a squarefree quartic. Therefore

\[
\left|\sum_{s\in\mathbf F_\lambda^*}
\chi_\lambda(\Re(cz)\Im(cz))\right|
\le3\sqrt\lambda.
\tag{32.6}
\]

If the quadratic character of the torus parameter is inserted, the relevant polynomial is degree five and squarefree, giving

\[
\left|\sum_s\chi_\lambda(s)\,
\chi_\lambda(\Re(cz)\Im(cz))\right|
\le4\sqrt\lambda.
\tag{32.7}
\]

## 5. Exact two-torus factorisation of the Stage14 character

On the visible same-orientation branch,

\[
(a+ib)(p-iq)=\ell\,U\bar V,
\]

while

\[
(a+ib)(p+iq)=\pi^2UV.
\]

The four-linear product is, up to a fixed nonzero square and a fixed sign, the product of

\[
\Re(U\bar V)\Im(U\bar V)
\]

and

\[
\Re(cUV)\Im(cUV)
\]

for a nonzero constant `c`. The opposite visible orientation and the invisible local-root branch have the same form with different invertible constants.

Write fixed norm-circle points as

\[
U=U_0s,
\qquad V=V_0t,
\qquad s,t\in T_\lambda,
\]

where the split norm-one torus is `T_lambda ~= F_lambda^*`.

The two arguments depend only on

\[
r=s/t,
\qquad w=st.
\]

The map

\[
(s,t)\mapsto(r,w)
\]

has kernel `{(1,1),(-1,-1)}` and image characterised by `rw` being a square in the torus. Therefore, for one-variable character functions `A(r),B(w)`, the exact identity is

\[
\boxed{
\sum_{s,t}A(s/t)B(st)
=
\left(\sum_rA(r)\right)\left(\sum_wB(w)\right)
+
\left(\sum_r\eta(r)A(r)\right)
\left(\sum_w\eta(w)B(w)\right),
}
\tag{32.8}
\]

where `eta` is the quadratic character of the split torus.

Applying (32.6)--(32.7) gives the uniform fixed-norm correlation theorem

\[
\boxed{
|C_\lambda(m,n)|\le25\lambda.
}
\tag{32.9}
\]

For two distinct split good primes, CRT gives

\[
\boxed{
|C_{\lambda\mu}(m,n)|\le625\lambda\mu.
}
\tag{32.10}
\]

This is a full square-root saving relative to the `~lambda^2` points on the product of two norm circles, and is much stronger than the unrestricted four-variable complete bound from t31.

## 6. What the stronger local theorem does — and does not — solve

The angular variables are now closed at the complete finite-field level. What remains is the incomplete norm-index sum

\[
\boxed{
\Sigma_{\lambda,\mu}(\ell;X,B)
=
\sum_{m\asymp X/\ell}
\sum_{\delta\ll B/X}
\sum_{k\mid\varepsilon m}
\sum_{\substack{N(U)=m\\N(V)=k\delta}}
\chi_{\lambda\mu}(\widetilde F_{\ell}(U,V)),
}
\tag{32.11}
\]

with the canonical-largest-prime condition and the physical interval/reconstruction conditions retained.

The complete torus estimate (32.10) cannot simply be inserted into (32.11), because an integral norm circle contains only `r_2(n)=n^o(1)` representatives rather than a complete residue torus. The missing theorem is an arithmetic average over Gaussian representations and the divisor coupling `k|epsilon*m`.

This is the exact place where a quadratic large sieve over `Q(i)` becomes structurally relevant. Goldmakher--Louvel prove a quadratic large-sieve inequality for Hecke families over general number fields, explicitly including the `Q(i)` setting and generalising Onodera's Gaussian-integer large sieve. But Stage14 still needs an explicit transfer of the character in (32.11) into that Hecke-family formalism while preserving:

- `k|epsilon*m`;
- `m delta << B/ell`;
- the canonical largest-prime condition;
- the visible orientation or invisible local-root label;
- the existential projection from cover points to directions.

That transfer is not claimed in t32.

## 7. Visible and invisible branches are now analytically aligned

Before t32 the two super-square-root states appeared different:

- visible: rational congruence `ell|p^2+q^2`;
- invisible: local Gaussian root `W=+/-rho C S mod ell^2`.

After descent, both are represented by the same norm set (32.2), and the auxiliary split-prime character has the same torus-factorised shape. The canonical `ell`-adic state only changes a bounded orientation/root label.

Therefore the next global estimate does **not** need two unrelated sieve theories. It needs one norm-indexed Gaussian/Hecke average with finitely many local state labels.

## 8. Frozen finite diagnostics

The deterministic t32 audit keeps the t31 box `a,b,p,q<=40`.

For every super-square-root D/sum non-torsion tuple it verifies the unified norm skeleton:

```text
visible non-torsion states        1018
invisible non-torsion states     12190
unified cofactor checks          13208

visible delta=1                    676
visible delta>1                    342
invisible delta=1                  230
invisible delta>1                11960
```

For the split auxiliary torus audit it uses `pi=1+2i` and checks **all nonzero norm pairs** for both Gaussian orientations:

```text
lambda   max |C_lambda|
  13          64
  17         160
  29         144
  37          16
  41         288
```

All satisfy `|C_lambda|<=25 lambda`.

The inert-prime resonance counterexample is frozen as

```text
lambda=11, pi=1+2i, m=1, n=2:
|C_11|=144=(11+1)^2.
```

These are finite algebraic diagnostics only; they are not asymptotic density statements.

## Boundary

```text
STAGE14_T32=COMPLETE_SPLIT_TORUS_NORM_CORRELATION_AND_UNIFIED_COFATOR_SKELETON
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
