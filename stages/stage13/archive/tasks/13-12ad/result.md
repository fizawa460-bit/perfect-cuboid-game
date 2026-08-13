# Stage13-12ad — quantitative `j=0` analytic closure

> STATUS: `STAGE13_12AD_COMPLETE_QUANTITATIVE_J0_ANALYTIC_CLOSURE`
>
> INPUT: Stage13-12aa non-circular local `j=0` factorization
>
> R02 REVIEW STATE: Grok `OPEN`, Claude `REPAIRABLE`
>
> SCOPE: close the weighted-Wiener, curved-region and nonzero-harmonic analytic gaps only
>
> GLOBAL STAGE13 STATE AFTER THIS STEP: `OPEN` because the p-adic overlap-tail/local-state issues are intentionally deferred to Stage13-12ae

Stage13-12ad does not alter the chamber geometry, the Stage12 factor-2 bridge,
or the fixed-local overlap strategy.  It addresses the common mathematical
content of the R02 reviews: Stage13-12aa had the correct non-circular proof
architecture, but the two analytic statements carrying that architecture were
not written with enough quantitative detail to be independently checked.

The two targets are

\[
\|C_{\ell,q}-1\|_\delta\ll_\delta q^{-1-2\delta}
\]

uniformly in the retained angular range, and

\[
\sum_{1\le \ell\le L}
\text{nonzero-harmonic contribution}_\ell
=o\!\left(B(\log B)^3\right)
\]

after the rectangle-to-curved-region transfer.

This file supplies explicit constants and one fixed error budget.  Numerical
sampling is not used as proof.

---

## 1. Fixed parameters

Throughout this step fix

\[
\delta=\frac18,\qquad \sigma=\frac12+\delta=\frac58.
\]

For a split prime `q` put

\[
\rho=q^{-\sigma}=q^{-5/8}.
\]

For every split prime `q>=13`,

\[
\rho\le 13^{-5/8}<\frac14.
\]

The only smaller split prime is `q=5`; it is a single finite Euler factor and
is separated once and for all.  Therefore global convergence only requires a
uniform estimate for `q>=13`.

For the curved-region decomposition choose

\[
H_0=U=\exp((\log B)^{1/4}),
\qquad
\eta=(\log B)^{-8}.
\]

For the Selberg--Vaaler angular bracket choose

\[
L=(\log B)^K,\qquad K=4.
\]

When a finite-order logarithmic remainder is needed below, take

\[
A=48.
\]

Nothing is optimized; these choices create a large separation from the main
scale `B(log B)^3`.

---

## 2. Exact Wiener algebra used here

For a power series

\[
F(x,y,z)=\sum_{a,b,c\ge0}f_{a,b,c}x^ay^bz^c
\]

define the local Wiener norm at radius `rho` by

\[
\|F\|_\rho
:=
\sum_{a,b,c\ge0}|f_{a,b,c}|\rho^{a+b+c}.
\]

It is submultiplicative:

\[
\|FG\|_\rho\le\|F\|_\rho\|G\|_\rho.
\]

The Stage13-12aa split-prime local factor is

\[
D_\ell(x,y,z)
=
1+a_\ell(x)+b_\ell(y)+b_\ell(z)
+M_\ell(x,y)+M_\ell(x,z),
\]

where `a=A-1`, `b=B-1`, and `M` is the genuine positive-height/base mixed
part.  There is no `y-z` local support because `(r,s)=1`.

The mixed correction is

\[
C_\ell(x,y,z)
=
\frac{D_\ell(x,y,z)}{A_\ell(x)B_\ell(y)B_\ell(z)}.
\]

All estimates below are uniform in the phase.  They apply both to the zero
mode and every nonzero retained harmonic because

\[
|2\cos(n\theta)|\le2,
\qquad
|H_n(\theta)|\le2n+1.
\]

---

## 3. Explicit pure-axis bounds

For every mode,

\[
\|a\|_\rho
\le
2\sum_{n\ge1}\rho^n
=
\frac{2\rho}{1-\rho}
\le\frac83\rho.
\]

Similarly,

\[
\|b\|_\rho
\le
\sum_{n\ge1}(2n+1)\rho^n
=
\frac{2\rho}{(1-\rho)^2}
+
\frac{\rho}{1-\rho}
\le\frac{44}{9}\rho.
\]

The mixed coefficient has absolute value at most `2`, hence

\[
\|M\|_\rho
\le
2\sum_{a,b\ge1}\rho^{a+b}
=
\frac{2\rho^2}{(1-\rho)^2}
\le\frac{32}{9}\rho^2.
\]

These are coefficientwise bounds, not sampled values.

---

## 4. Explicit inverse bounds

For a nonzero phase `c=cos(theta)`,

\[
A_\ell(x)^{-1}
=
\frac{1-2cx+x^2}{1-x^2}.
\]

Every nonconstant coefficient has absolute value at most `2`, so

\[
\|A_\ell^{-1}\|_\rho
\le
1+\frac{2\rho}{1-\rho}
\le\frac53.
\]

The zero-mode inverse `(1-x)/(1+x)` satisfies the same bound.

Also

\[
B_\ell(y)^{-1}
=
\frac{1-2cy+y^2}{1+y}.
\]

Its coefficient of `y` has absolute value at most `3`, and every coefficient
of degree at least two has absolute value at most `4`.  Therefore

\[
\|B_\ell^{-1}\|_\rho
\le
1+3\rho+\frac{4\rho^2}{1-\rho}
\le\frac{25}{12}.
\]

Again the zero-mode inverse `(1-y)^2/(1+y)` is the endpoint `c=1` and obeys
the same estimate.

Thus no inverse constant depends on `q`, `ell`, or the phase.

---

## 5. The missing uniform weighted-`l1` estimate

Write

\[
E_\ell
:=D_\ell-A_\ell B_\ell(y)B_\ell(z).
\]

Since the pure axes agree exactly,

\[
E_\ell
=(M_{xy}-ab_y)+(M_{xz}-ab_z)-b_yb_z-ab_yb_z.
\]

Every displayed term has at least two positive coordinate exponents.  Using
Sections 3--4 and `rho<=1/4`,

\[
\begin{aligned}
\|E_\ell\|_\rho
&\le
2\|M\|_\rho
+2\|a\|_\rho\|b\|_\rho
+\|b\|_\rho^2
+\|a\|_\rho\|b\|_\rho^2\\
&\le
\frac{17744}{243}\rho^2.
\end{aligned}
\]

Therefore

\[
\begin{aligned}
\|C_\ell-1\|_\rho
&\le
\|E_\ell\|_\rho
\|A_\ell^{-1}\|_\rho
\|B_\ell^{-1}\|_\rho^2\\
&\le
\frac{3465625}{6561}\rho^2\\
&<529\rho^2.
\end{aligned}
\]

Since `rho=q^{-5/8}`,

\[
\boxed{
\|C_{\ell,q}-1\|_{5/8}
\le529q^{-5/4}
\qquad(q\ge13,\ q\equiv1\pmod4),
}
\]

uniformly for **every** angular phase, hence in particular uniformly for all

\[
1\le\ell\le(\log B)^4.
\]

The series

\[
\sum_{q\equiv1(4)}q^{-5/4}
\]

converges.  The finite `q=5` factor is harmless.  Thus the global mixed Euler
product converges in the weighted Wiener algebra with a norm independent of the
retained harmonic cutoff.

This replaces the R02 numerical samples by an actual all-prime/all-harmonic
bound.

---

## 6. Logarithmic moments of the global correction

Let

\[
C_\ell(\mathbf s)
=
\sum_{u,v,w\ge1}
\frac{c_\ell(u,v,w)}{u^{s_h}v^{s_r}w^{s_s}}.
\]

The previous section gives

\[
\sum_{u,v,w}
\frac{|c_\ell(u,v,w)|}{(uvw)^{5/8}}
<\infty
\]

uniformly in the retained `ell` range.

For each fixed integer `m>=0`,

\[
\frac{(1+\log(uvw))^m}{(uvw)}
\ll_m
\frac1{(uvw)^{5/8}},
\]

because `(1+log n)^m n^{-3/8}` is bounded.  Hence

\[
\boxed{
\sum_{u,v,w}
\frac{|c_\ell(u,v,w)|(1+\log(uvw))^m}{uvw}
<\infty
}
\]

uniformly for retained harmonics.

This is the precise statement needed when the convolution change of variables
shifts `log R` to `log R-log v` and similarly in the other variables.  Every
such shift can affect at most one lower logarithmic degree; summing it over the
correction coefficients is legitimate.

---

## 7. Zero-mode one-variable summatory inputs

At `ell=0`, the pure factors have pole orders

\[
A_0(s):\ 1,
\qquad
B_0(s):\ 2.
\]

At the same standard finite-order Selberg--Delange/Tauberian theorem boundary
already used in Stage12 and Stage13-7h, for any fixed `N` one has uniformly on
our fixed parity channels

\[
\sum_{h\le X}a_0(h)
=\alpha X+O_N(X(\log 2X)^{-N}),
\]

and

\[
\sum_{r\le X}b_0(r)
=X(\beta_1\log X+\beta_0)
+O_N(X(\log 2X)^{-N}).
\]

The constants `alpha,beta_1,beta_0` are arithmetic and independent of the
canonical direction.  The OE/EE finite factors only alter their common
arithmetic combination.

After convolving the correction from Section 6, the same formulas hold on a
rectangle with the main coefficient multiplied by the absolutely convergent
value of the correction at `(1,1,1)`.  Logarithmic shifts from `(u,v,w)` have
finite moments and contribute only lower log degrees.

Consequently, for a core rectangle

\[
H<h\le e^\eta H,
\quad
R<r\le e^\eta R,
\quad
S<s\le e^\eta S,
\]

the zero-mode main is a common arithmetic constant times the volume and a
polynomial whose leading base term is `log R log S`.  A standard convolution
tail split at square roots gives a rectangle error of the explicit form

\[
\boxed{
\mathcal E_{\rm rect}
\ll
(\log B)^C
\left(H^{3/4+\varepsilon}RS
+HR^{3/4+\varepsilon}S
+HRS^{3/4+\varepsilon}\right),
}
\]

plus arbitrarily high finite-order one-variable logarithmic remainders.

The point relevant to R02 is that this is now a `j=0` statement: its mixed
correction is supplied by Sections 3--6 rather than by invoking the old `j>=1`
validator.

---

## 8. Core/wing decomposition for the curved region

The physical region is

\[
h(r^2+s^2)\le2B
\]

with the fixed OE/EE variants.  Separate

```text
small height:      h < H0
small coordinate:  min(r,s) < U
core:              h >= H0 and min(r,s) >= U
```

where `H0=U=exp((log B)^(1/4))`.

### 8.1 Small height

Partial summation from Section 7 gives

\[
\sum_{h\le H_0}\frac{a_0(h)}h\ll\log H_0,
\]

while each base variable contributes one logarithm.  Therefore

\[
\boxed{
\mathcal E_{\rm small\ h}
\ll
B(\log B)^2\log H_0
=
B(\log B)^{9/4}.
}
\]

This is `o(B(log B)^3)`.

### 8.2 Small base coordinate

Similarly

\[
\sum_{r\le U}\frac{b_0(r)}r\ll(\log U)^2.
\]

Using the positive zero-mode majorant for the other variables gives

\[
\boxed{
\mathcal E_{\rm small\ coord}
\ll
B(\log B)^2(\log U)^2
=
B(\log B)^{5/2}.
}
\]

Again this is lower order.

### 8.3 Rectangle power tails on the core

On the core, every coordinate to which the `3/4+eps` rectangle error is
applied is at least `H0` or `U`.  Summing the logarithmic rectangle grid costs
only a fixed power of `log B`, so for sufficiently small fixed `eps<1/8`,

\[
\boxed{
\mathcal E_{\rm power}
\ll
B(\log B)^C
\left(H_0^{-1/4+\varepsilon}
+U^{-1/4+\varepsilon}\right)
=o(B(\log B)^{-100}).
}
\]

The last `-100` is not special: the stretched-exponential decay beats every
fixed logarithmic power.

---

## 9. Rectangle-to-curved-sector transfer

Partition the core in multiplicative rectangles with mesh

\[
e^\eta,\qquad \eta=(\log B)^{-8}.
\]

The number of boxes is polynomial in `log B`.  Boxes wholly inside or outside
`h(r^2+s^2)<=2B` are handled by the rectangle expansion.  A box intersecting
the curved boundary lies in a multiplicative `O(eta)` thickening of that
boundary.

Applying the positive zero-mode rectangle majorant to this boundary shell gives

\[
\boxed{
\mathcal E_{\rm boundary}
\ll
\eta B(\log B)^3+\mathcal E_{\rm power}
=
O(B(\log B)^{-5})+o(B(\log B)^{-100}).
}
\]

Inside the core, the leading rectangle polynomial is a Riemann sum in the
radial and angular variables.  The radial summation of the two base logarithms
against the homogeneous `1/(r^2+s^2)` scale contributes the third logarithm.
The angular zero Fourier coefficient is exactly the already-derived category
kernel `k_q(t(phi))`.  Therefore the core main is

\[
\Theta J_q B(\log B)^3,
\qquad
J_q=\int_{\pi/4}^{\pi/2}k_q(t(\phi))\,d\phi.
\]

The mesh error in this Riemann sum is at most

\[
O(\eta B(\log B)^3)=O(B(\log B)^{-5}).
\]

Combining Sections 8--9 proves, for the zero angular mode alone,

\[
\boxed{
A_q^{(0)}(B)
=
\Theta J_qB(\log B)^3
+o(B(\log B)^3),
}
\]

with one arithmetic `Theta`, before any use of the Stage12 directional
constant.

---

## 10. Uniform nonzero Gaussian harmonics: exact external boundary

R02 was correct that the phrase “same polylog-uniform Hecke machinery” was too
compressed.  The dependence needed here is the following standard
external-theorem-level input.

For Gaussian angular Hecke characters `xi_k`, the classical Landau--Page
zero-free region has denominator

\[
\log((2+|t|)(2+|k|))
\]

(up to a fixed finite modulus factor), and a possible exceptional real zero can
occur only for angular frequency `k=0`.  A convenient published formulation is
J. Merikoski, *On Gaussian primes in sparse sets*, Compositio Mathematica
(2025), Lemma 2.13, which states precisely this `k`-dependent zero-free region.

Here

\[
k=8\ell,\qquad1\le\ell\le(\log B)^4,
\]

so the exceptional case is absent and the angular conductor is only
polylogarithmic in `B`.

Together with the standard polynomial vertical growth of these Hecke
`L`-functions and the finite-order Selberg--Delange theorem, this yields the
following uniform finite-order consequence: for every fixed `A,K`,

\[
\boxed{
\sum_{h\le X}a_\ell(h)
\ll_{A,K}
X(\log 2X)^{-A}
\qquad
(1\le\ell\le(\log X)^K),
}
\]

for the nonzero `j=0` scale channel.  The crucial point specific to `j=0` is
that

\[
A_\ell(s)=L(s,\xi_{8\ell})E_{h,\ell}(s)
\]

has no zeta pole and no fractional Hecke power.  Thus there is no branch issue
at zeros of `L`; the finite-order `z=0` expansion has no main pole term.  The
Wiener factor of Sections 3--6 is uniform in `ell`, so its convolution does not
spoil this estimate.

This paragraph states the external analytic theorem actually used and its
parameter dependence; the proof no longer hides it behind a reference to
Stage13-7i.

---

## 11. Concrete harmonic budget

Use

\[
L=(\log B)^4,
\qquad A=48.
\]

The Selberg--Vaaler pointwise majorant/minorant has constant-term excess
`O(1/L)`.  The exact Stage13-3d bridge plus the frozen Stage12 total theorem is
used here only as a positive total upper bound

\[
A_{ab}+A_{ac}+A_{bc}=O(B(\log B)^3).
\]

Therefore the Vaaler excess is

\[
\boxed{
\mathcal E_{\rm Vaaler}
\ll
\frac{B(\log B)^3}{(\log B)^4}
=
O(B(\log B)^{-1}).
}
\]

Using `h>=H0` on the core,

\[
\log H_0=(\log B)^{1/4},
\]

so the uniform scale cancellation with `A=48` supplies

\[
(\log H_0)^{-48}=(\log B)^{-12}.
\]

The two base channels and rectangle/partial-summation bookkeeping cost at most
`(log B)^2` at the raw `j=0` scale.  Summing the very crude bound over all
`L=(log B)^4` retained modes therefore gives

\[
\boxed{
\mathcal E_{\rm harm,core}
\ll
B(\log B)^{4+2-12}
=
O(B(\log B)^{-6}).
}
\]

Using the actual Fourier coefficient `O(1/ell)` would improve this, but is not
needed.

On the small-height and small-coordinate pieces, absolute values of all
harmonic numerators are dominated by the positive zero-mode coefficients, so
the bounds of Section 8 dominate those pieces.  Thus the entire nonzero
harmonic family is lower order.

Consequently

\[
\boxed{
A_q(B)
=A_q^{(0)}(B)+o(B(\log B)^3).
}
\]

---

## 12. Full explicit error ledger

With the single fixed choice

```text
delta = 1/8
H0 = U = exp((log B)^(1/4))
eta = (log B)^(-8)
L = (log B)^4
A = 48
```

all errors are bounded as follows.

| source | bound |
|---|---|
| small height | `O(B (log B)^(9/4))` |
| small coordinate | `O(B (log B)^(5/2))` |
| mixed-convolution log shifts | `O(B (log B)^2)` |
| rectangle power tails | `B (log B)^C exp(-c (log B)^(1/4))` |
| curved-boundary / Riemann mesh | `O(B (log B)^(-5))` |
| Vaaler constant-term excess | `O(B (log B)^(-1))` |
| all retained nonzero harmonics on core | `O(B (log B)^(-6))` |

Every row is `o(B(log B)^3)`.

This is the quantitative closure that was absent from R02.

---

## 13. Common factor and delayed Stage12 calibration

Sections 2--12 prove first

\[
\boxed{
A_q(B)
\sim
\Theta J_q B(\log B)^3,
}
\]

with one `Theta` independent of `q`.

Only now use

\[
\sum_qA_q(B)
\sim
\frac{\kappa}{24\pi}B(\log B)^3
\]

from the frozen Stage12 total plus the exact factor-2 bridge, together with

\[
\sum_qJ_q=\frac\pi4.
\]

Then

\[
\Theta\frac\pi4=\frac\kappa{24\pi},
\qquad
\boxed{\Theta=\frac\kappa{6\pi^2}}.
\]

Since `J_q=2I_q/pi`,

\[
\boxed{
A_q(B)
\sim
\frac{\kappa I_q}{3\pi^3}B(\log B)^3.
}
\]

The logical order remains non-circular.

---

## 14. What 13-12ad does not repair

The R02 Grok review also identified two overlap-side issues:

1. the positive-valuation inert-prime local tail was written as `O(1/p)` without an explicit all-valuation derivation and absolute constant;
2. the finite local-state refinement was not enumerated through every valuation/parity/primitivity stratum strongly enough to let a reviewer verify that the constrained tagged count really majorizes every pair overlap.

Those are separate p-adic/local-state questions.  They are **not** declared
repaired here and will be the sole target of Stage13-12ae.

Accordingly Stage13 remains externally open after 13-12ad.

---

## 15. Decision

```text
STAGE13_12AD=COMPLETE_QUANTITATIVE_J0_ANALYTIC_CLOSURE

CLAUDE_R02_WEIGHTED_L1_UNIFORMITY=REPAIRED
CLAUDE_R02_NONZERO_HARMONIC_LOWER_ORDER=REPAIRED
GROK_R02_ZERO_MODE_CURVED_TRANSFER=REPAIRED

WIENER_DELTA=1/8
WIENER_SIGMA=5/8
WIENER_UNIFORM_BOUND=529*q^(-5/4)
VAALER_K=4
FINITE_ORDER_SD_A=48

RAW_DIRECTIONAL_ANALYTIC_CORE=RESTORED_WITH_EXPLICIT_ERROR_BUDGET
RAW_COMMON_FACTOR_CALIBRATION_REMAINS_NON_CIRCULAR=true

P_ADIC_POSITIVE_VALUATION_TAIL=PENDING_13_12AE
LOCAL_STATE_REFINEMENT_COMPLETENESS=PENDING_13_12AE
EXACT_ONE_THEOREM_EXTERNAL_STATUS=OPEN
STAGE13_GLOBAL_REVIEW_STATUS=OPEN
NEXT=Stage13-12ae
```
