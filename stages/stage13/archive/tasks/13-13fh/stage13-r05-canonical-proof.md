# Stage13 — R05 canonical proof candidate

> STATUS: `STAGE13_13FH_R05_CANONICAL_PROOF_CANDIDATE`
>
> PURPOSE: one proof-facing synthesis of the Stage13 exactly-one directional asymptotic after R05 repair Gates A--G.
>
> PRECEDENCE: this file supersedes `stages/stage13/13-13c/stage13-final-proof.md` for the future R05 bundle only. R03 and R04 remain immutable historical review artifacts.
>
> THEOREM_CHANGED: `false`.
>
> THEOREM_CONTRACT_REOPEN_REQUIRED: `false`.

---

## 0. The theorem, counting convention, and nonclaims

Count primitive canonical integer triples

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,
\qquad d^2=a^2+b^2+c^2,
\qquad d\in\mathbf Z_{>0}.
\]

For a face label

\[
q\in\{ab,ac,bc\},
\]

let `A_q(B)` count triples with `d<=B` for which face `q` has integral diagonal, with additional integral faces allowed. For distinct `q,r`, let `O_{qr}(B)` count triples on which both faces are integral, and let `T(B)` count triples on which all three faces are integral. Let `N_q(B)` count triples with exactly one integral face, namely `q`, and set

\[
N_1(B)=N_{ab}(B)+N_{ac}(B)+N_{bc}(B).
\]

On the canonical spherical chamber

\[
\mathcal R=\{(x,y,z)\in S^2:0<x<y<z\},
\]

define

\[
w_{ab}=\frac1{\sqrt{x^2+y^2}},\qquad
w_{ac}=\frac1{\sqrt{x^2+z^2}},\qquad
w_{bc}=\frac1{\sqrt{y^2+z^2}},
\]

and

\[
I_q=\int_{\mathcal R}w_q\,d\omega.
\]

The theorem is

\[
\boxed{
N_q(B)\sim
\frac{\kappa I_q}{3\pi^3}B(\log B)^3
}
\]

for every `q`, and

\[
\boxed{
N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3.
}
\]

Moreover

\[
\boxed{I_{ab}+I_{ac}+I_{bc}=\frac{\pi^2}{8}},
\]

so

\[
\boxed{
\frac{N_q(B)}{N_1(B)}\to\frac{8I_q}{\pi^2}.
}
\]

The numerical validator is

```text
(ab,ac,bc)
=
(0.5347369332313988,
 0.24535917783225203,
 0.21990388893634913).
```

No effective convergence rate is claimed. No monotonicity of finite directional ratios is claimed. No assumption that perfect cuboids do not exist is used.

---

## 1. Exact combinatorics

For `{q,r,s}={ab,ac,bc}`,

\[
\boxed{N_q=A_q-O_{qr}-O_{qs}+T},
\]

and

\[
\boxed{
N_1=\sum_qA_q-2\sum_{q<r}O_{qr}+3T.
}
\]

These are finite identities. It therefore suffices to prove

\[
A_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3
\]

with the stated category dependence, and

\[
O_{qr}(B)=o(B(\log B)^3).
\]

---

## 2. Complete frozen Stage12 R09 interface

Stage12 uses positive integers `h,r,s` with

\[
1\le r<s,\qquad (r,s)=1,
\]

and

\[
P=hrs,\qquad
z=\frac{h(s^2-r^2)}2,\qquad
d=\frac{h(r^2+s^2)}2.
\]

Its admissible parameter set is

\[
\mathcal D_B=\{(h,r,s):1\le r<s,(r,s)=1,
 h(r^2+s^2)\le2B,
 h(r^2+s^2)\equiv0\pmod2\}.
\]

Thus its cutoff is exactly `d<=B`.

For

\[
G(n)=\prod_{\substack{p\mid n\\p\equiv1(4)}}(2v_p(n)+1),
\]

Stage12 defines

\[
C_{\rm raw}(B)=\sum_{(h,r,s)\in\mathcal D_B}(G(hrs)-1),
\]

and, by exact common-scale decomposition and Möbius inversion,

\[
C_{\rm prim}(B)=\sum_{k\le B}\mu(k)C_{\rm raw}(\lfloor B/k\rfloor).
\]

This is a primitive **oriented distinguished-face record count**. The outer pair already obeys `r<s`; Stage12 retains a distinguished integral face and does not quotient by all edge permutations.

The frozen theorem is

\[
\boxed{
C_{\rm prim}(B)\sim\frac{\kappa}{12\pi}B(\log B)^3.
}
\]

The constant is explicitly

\[
\boxed{
\begin{aligned}
\kappa={}&
\left(\frac\pi4\right)^3\left(\frac12\right)^3
\prod_{p\equiv3(4)}(1-p^{-2})^3\\
&\times
\prod_{q\equiv1(4)}
\frac{q^2+6q+1}{q^2-1}(1-q^{-1})^6.
\end{aligned}}
\]

The normalized local factors are `1+O(p^-2)`, so the product converges absolutely. Stage12 also has a constant `eta` satisfying the exact identity

\[
\boxed{\eta=\pi\kappa}.
\]

### Exact projection fiber

Fix one primitive canonical raw incidence counted by `A_q(B)`. Stage12 has exactly two oriented preimages for that distinguished face:

\[
(x,y),\qquad(y,x).
\]

There is no additional outer factor because `r<s` already fixes the outer orientation; canonical sorting preserves the cutoff and gcd; OE/EE parity does not change the two-element leg-order fiber; and the repeated-side contribution is zero. The statement remains true on exactly-two and exactly-three face objects because the distinguished incidence is retained.

Hence, for every `B` and `q`,

\[
\boxed{C^{\rm proj}_{\rm prim,q}(B)=2A_q(B)},
\]

and therefore

\[
\boxed{C_{\rm prim}(B)=2\sum_qA_q(B)}.
\]

This factor two is exact, finite, and independent of asymptotics.

---

## 3. Canonical chamber geometry

Fix distinguished face `ab` and write

\[
a^2+b^2=P^2,\qquad P^2+c^2=d^2.
\]

For

\[
F_1=a^2+b^2-P^2,\qquad F_2=P^2+c^2-d^2,
\]

one has

\[
\det\frac{\partial(F_1,F_2)}{\partial(P,d)}=4Pd.
\]

After radial normalization to `S^2`, the directional Gelfand--Leray factor is proportional to

\[
\frac1{P/d}=\frac1{\sqrt{x^2+y^2}}=w_{ab}.
\]

The other two categories follow by permutation. Thus the category dependence at the real place is exactly `I_q`.

Pointwise on the chamber,

\[
w_{ab}>w_{ac}>w_{bc}.
\]

The chamber partition gives

\[
\boxed{\sum_qI_q=\frac{\pi^2}{8}}.
\]

---

## 4. Exact bridge to the zero Fourier kernel; notation separation

For a fixed face `q={i,j}` and complementary coordinate `k`, use geometric spherical variables

\[
x_i=\sin\theta\cos\alpha,\qquad
x_j=\sin\theta\sin\alpha,\qquad
x_k=\cos\theta.
\]

Here and only here `theta` is the geometric polar angle. Then

\[
w_q=\frac1{\sin\theta},\qquad
d\omega=\sin\theta\,d\theta\,d\alpha,
\]

so

\[
\boxed{w_q\,d\omega=d\theta\,d\alpha}.
\]

Put

\[
\psi=\frac\pi2-\theta,
\]

and let `ell_q(psi)` be the allowed inner-angle length in the canonical chamber. Tonelli applies because the integrand is nonnegative; the domain has finite measure. Hence

\[
I_q=\int\ell_q(\psi)\,d\psi.
\]

Write

\[
r=R\cos\phi,\qquad s=R\sin\phi,
\qquad\phi\in[\pi/4,\pi/2].
\]

Then

\[
\frac Pd=\sin2\phi,\qquad\frac zd=-\cos2\phi,
\]

so

\[
\psi=2\phi-\frac\pi2,\qquad d\psi=2d\phi.
\]

The ordered inner Pythagorean angle has total length `pi/4`. Therefore its category zero-mode coefficient is

\[
k_q(\phi)=\frac4\pi\ell_q(\psi).
\]

Define

\[
J_q=\int_{\pi/4}^{\pi/2}k_q(\phi)\,d\phi.
\]

Then

\[
\boxed{J_q=\frac{2I_q}{\pi}},\qquad
\boxed{\sum_qJ_q=\frac\pi4}.
\]

Numerical integration is only a validator for this analytic identity.

From now on the **Gaussian local angular phase** is denoted `vartheta`; it is never denoted `theta`. This removes the R04 notation collision.

---

## 5. Primitive split-prime coefficient system

On each fixed OE/EE branch retain

\[
P=hrs,\qquad z=\frac{h(s^2-r^2)}2,
\qquad d=\frac{h(r^2+s^2)}2,
\qquad(r,s)=1.
\]

The parity distinction is finite and 2-adic. For odd primes the coefficient system is common to every canonical face category.

Let `p congruent 1 mod 4` be split. Put

\[
a=v_p(h),\qquad b=v_p(rs),\qquad e=a+b.
\]

At zero Gaussian angular mode the representation multiplicity is

\[
G_e=2e+1.
\]

For local phase `vartheta`, put

\[
H_e(\vartheta)=1+2\sum_{m=1}^e\cos(m\vartheta).
\]

Primitive support subtraction gives

\[
Z_0(a,b)=
\begin{cases}
2b+1,&a=0,\\
2,&a\ge1,
\end{cases}
\]

and

\[
Z_\ell(a,b;\vartheta)=
\begin{cases}
H_b(\vartheta),&a=0,\\
2\cos((a+b)\vartheta),&a\ge1.
\end{cases}
\]

No face label occurs in these coefficients.

For the one-variable pure axes define

\[
A_\vartheta(x)=\frac{1-x^2}{1-2\cos\vartheta\,x+x^2},
\qquad
B_\vartheta(y)=\frac{1+y}{1-2\cos\vartheta\,y+y^2}.
\]

At `vartheta=0`,

\[
A_0(x)=\frac{1+x}{1-x},\qquad
B_0(y)=\frac{1+y}{(1-y)^2}.
\]

After finite 2-adic and inert factors are collected into residual Euler products,

\[
A_0(s)=\zeta(s)L(s,\chi_4)E_{h,0}(s),
\]

\[
B_0(s)=\zeta(s)^2L(s,\chi_4)E_{b,0}(s),
\]

whereas for `ell>=1`,

\[
A_\ell(s)=L(s,\Xi_{8\ell})E_{h,\ell}(s).
\]

Thus the zero-mode scale/base pole orders are `1,2,2`; the nonzero angular scale channel has no zeta pole.

---

## 6. Three-variable mixed correction and the explicit Wiener constant

At a split prime define

\[
\begin{aligned}
D_\vartheta(x,y,z)={}&1
+\sum_{a\ge1}2\cos(a\vartheta)x^a\\
&+\sum_{b\ge1}H_b(\vartheta)(y^b+z^b)\\
&+\sum_{a,b\ge1}2\cos((a+b)\vartheta)x^a(y^b+z^b).
\end{aligned}
\]

There is no simultaneous positive `y,z` support because `(r,s)=1`. Define

\[
C_\vartheta(x,y,z)=
\frac{D_\vartheta(x,y,z)}
{A_\vartheta(x)B_\vartheta(y)B_\vartheta(z)}.
\]

The actual local Dirichlet factor notation is fixed at first use by

\[
\boxed{
C_{\ell,p}(s_h,s_r,s_s)
:=C_\vartheta(p^{-s_h},p^{-s_r},p^{-s_s}),
}
\]

where `vartheta` is the phase attached to `(ell,p)`.

The pure axes cancel exactly. Every nonconstant monomial of `C_vartheta-1` therefore uses at least two coordinates.

For

\[
\sigma=\frac58,\qquad\rho=p^{-5/8},
\]

define the weighted Wiener norm

\[
\|F\|_\rho=\sum_{i,j,k\ge0}|f_{ijk}|\rho^{i+j+k}.
\]

It is submultiplicative by the Cauchy product and Tonelli.

For `p>=13`, `rho<1/4`. Put `a=A_vartheta-1`, `b=B_vartheta-1`, and let `M` be the positive-height/base mixed part. Coefficientwise,

\[
\|a\|_\rho\le\frac83\rho,
\qquad
\|b\|_\rho\le\frac{44}{9}\rho,
\qquad
\|M\|_\rho\le\frac{32}{9}\rho^2,
\]

and the exact inverse formulas give

\[
\|A_\vartheta^{-1}\|_\rho\le\frac53,
\qquad
\|B_\vartheta^{-1}\|_\rho\le\frac{25}{12}.
\]

If

\[
E_\vartheta=D_\vartheta-A_\vartheta B_\vartheta(y)B_\vartheta(z),
\]

then exact pure-axis cancellation gives

\[
E_\vartheta=(M_{xy}-ab_y)+(M_{xz}-ab_z)-b_yb_z-ab_yb_z.
\]

Hence

\[
\|E_\vartheta\|_\rho
\le\frac{17744}{243}\rho^2.
\]

Therefore

\[
\begin{aligned}
\|C_\vartheta-1\|_\rho
&\le
\frac{17744}{243}\rho^2
\frac53\left(\frac{25}{12}\right)^2\\
&=
\frac{3465625}{6561}\rho^2
<529\rho^2.
\end{aligned}
\]

Since `rho^2=p^-5/4`,

\[
\boxed{
\|C_{\ell,p}-1\|_{5/8}\le529p^{-5/4}
\qquad(p\ge13,\ p\equiv1(4)).
}
\]

The constant is therefore derived, not fitted. The split prime `p=5` is separated and the same coefficient argument gives the explicit phase-uniform finite bound

\[
\boxed{\|C_{\ell,5}-1\|_{5/8}<432}.
\]

Because

\[
\sum_{p\equiv1(4),p\ge13}p^{-5/4}<\infty,
\]

the global mixed correction converges absolutely in the weighted Wiener algebra, uniformly in the retained phase family. For every fixed integer `m>=0`,

\[
\boxed{
\sum_{u,v,w}\frac{|c_\ell(u,v,w)|(1+\log(uvw))^m}{uvw}<\infty
}
\]

uniformly in retained `ell`. Consequently correction-induced logarithmic shifts are absolutely summable and every nonconstant shift lowers the final log degree.

---

## 7. Exact external analytic boundary

The proof imports only the following analytic statements beyond frozen Stage12.

### H1: nonzero Gaussian angular Hecke functions

For nonzero integer `k`, the Gaussian ideal character `Xi_k` has an `L`-function

\[
L(s,\Xi_k)
\]

which is entire, and whose completion

\[
\xi(s,k)=\pi^{-(s+2|k|)}\Gamma(s+2|k|)L(s,\Xi_k)
\]

satisfies

\[
\xi(s,k)=\xi(1-s,k).
\]

In particular, for Stage13 `k=8ell`, `ell>=1`, there is no pole at `s=1`.

### H2: fixed finite residue twists

For any fixed finite residue modulus used later in the overlap proof, a nontrivial Dirichlet or Gaussian/ray-class Hecke twist is holomorphic at `s=1` and satisfies the classical continuation and functional equation. Only the trivial Hecke character may have a pole at `s=1`. The finite residue set is fixed before `B->infinity`, so no conductor growing with `B` occurs.

### D1: `L(s,chi_4)`

The primitive nonprincipal Dirichlet `L`-function `L(s,chi_4)` is holomorphic at `s=1`, has the classical continuation and functional equation, and has polynomial growth on fixed strips.

### V1: Vaaler sawtooth approximation

For degree `L`, Vaaler's finite sawtooth approximation has a nonnegative Fejer-kernel error. Applying it to the two endpoint sawtooths of an interval gives internal trigonometric majorants/minorants `P^pm` with

\[
\boxed{\widehat P^\pm(0)=|I|\pm\frac1{L+1}},
\]

and, for `1<=|h|<=L`,

\[
\boxed{
|\widehat P^\pm(h)|
\le\frac1{\pi|h|}+\frac1{L+1}<1.
}
\]

Thus Vaaler contributes no positive power of the harmonic index.

### Fixed-strip growth and Riesz/Perron consequence

On a fixed strip, right-boundary absolute convergence, the functional equation, Stirling, and Phragmen--Lindelof give polynomial growth in `2+|t|+|k|`. Multiplying by the phase-uniform residual Wiener factor preserves polynomial growth.

To pass from this to ordinary partial sums, use an `m`-fold Riesz/Perron kernel

\[
\frac{X^s}{s(s+1)\cdots(s+m)}
\]

with `m` larger than the fixed vertical-growth exponent, shift the smoothed contour to a fixed line left of `1`, and recover the ordinary sum by finite differencing plus the coefficient majorant. Therefore there exist fixed

\[
\delta_H>0,\qquad C_H,D_H\ge0
\]

such that, for every `X>=2` and `ell>=1`,

\[
\boxed{
S_\ell(X):=\sum_{h\le X}a_\ell(h)
\ll X^{1-\delta_H}(1+\ell)^{C_H}(\log2X)^{D_H}.
}
\]

This is an all-`ell` family bound. The invalid shortcut `ell<=(log X)^4` near the core lower endpoint is not used.

No Gaussian-Hecke zero-free region, general Selberg--Delange theorem, growing-modulus theorem, or Dirichlet prime-distribution theorem is a logical input.

---

## 8. Zero mode on the curved physical region: explicit accumulation

Write

\[
\Lambda=\log B,
\qquad
H_0=U=\exp(\Lambda^{1/4}),
\qquad
\eta=\Lambda^{-8}.
\]

The physical cutoff is

\[
h(r^2+s^2)\le2B.
\]

Remove the wings

```text
h < H0,
min(r,s) < U.
```

Positive zero-mode partial summation gives

\[
\boxed{\mathcal E_{\rm small\ h}\ll B\Lambda^{9/4}},
\]

\[
\boxed{\mathcal E_{\rm small\ coord}\ll B\Lambda^{5/2}}.
\]

Both are `o(B Lambda^3)`.

On the core use the multiplicative mesh `e^eta`. Every coordinate is at most `2B`, and one coordinate needs at most

\[
O(\Lambda^9)
\]

mesh intervals. Hence the actual three-dimensional box count is

\[
\boxed{N_{\rm box}=O(\Lambda^{27})}.
\]

For the finite-order zero-mode Perron endpoint expansions choose

\[
N=64.
\]

On a core box, `H(R^2+S^2)<<B`, hence `HRS<<B`. A one-variable finite-order remainder costs at most

\[
B\Lambda^{2-N}=B\Lambda^{-62}
\]

per box. After every box,

\[
\boxed{\mathcal E_{\rm finite}\ll B\Lambda^{-35}}.
\]

For the rectangle power tails choose `epsilon=1/16`. The saving exponent is

\[
\frac14-\varepsilon=\frac3{16}.
\]

Since every core variable is at least `H0=U`, the total after all boxes is

\[
\boxed{
\mathcal E_{\rm pow,total}
\ll
B\Lambda^{C_{\rm rect}+27}
\exp\left(-\frac3{16}\Lambda^{1/4}\right)
}
\]

for one fixed `C_rect`. This is `o_A(B Lambda^-A)` for every fixed `A>0`.

The mixed-correction logarithmic moments imply that every nonconstant convolution shift lowers the global log degree; altogether

\[
\boxed{\mathcal E_{\rm shift}\ll B\Lambda^2}.
\]

A box meeting the curved boundary lies in a shell of logarithmic thickness `O(eta)`. The cumulative main expression is homogeneous of degree one in `B` with log degree at most three, hence

\[
\boxed{
\mathcal E_{\rm boundary}=O(B\Lambda^{-5})+
\text{already-counted lower-order terms}.
}
\]

On interior boxes, total first variation times mesh width gives

\[
\boxed{\mathcal E_{\rm mesh}=O(B\Lambda^{-5})}.
\]

No extra `N_box` multiplies this Riemann-sum variation estimate.

The resulting zero-mode main is

\[
\boxed{
A_q^{(0)}(B)=\Theta J_qB\Lambda^3+o(B\Lambda^3)
}
\]

for one arithmetic constant `Theta>0` independent of `q`. The reason is structural: every arithmetic coefficient system above is category-independent, while the category enters only through the real zero-mode kernel `J_q`.

---

## 9. Retained nonzero harmonics with visible conductor loss

Use Vaaler degree

\[
L=\lfloor\Lambda^4\rfloor.
\]

The small-height and small-coordinate wings have already been removed by positive majorants before Fourier expansion; they are not multiplied by `L`.

On the core, partial summation of the Hecke-family bound gives

\[
\left|\sum_{H_0<h\le B}\frac{a_\ell(h)}h\right|
\ll
(1+\ell)^{C_H}\Lambda^{D_H}
\exp(-\delta_H\Lambda^{1/4}).
\]

The two positive base channels cost at most `Lambda^2`, and the phase-uniform mixed correction adds no positive `ell` power. Therefore one mode contributes

\[
\mathcal H_\ell(B)
\ll
B\Lambda^{D_H+2}(1+\ell)^{C_H}
\exp(-\delta_H\Lambda^{1/4}).
\]

Since the Vaaler nonzero coefficient is `<1`, summing `ell<=L` yields

\[
\boxed{
\mathcal E_{\rm harm,core}
\ll
B\Lambda^{4C_H+D_H+6}
\exp(-\delta_H\Lambda^{1/4}).
}
\]

For every fixed `A>0`, this is

\[
o_A(B\Lambda^{-A}).
\]

Thus the old fixed cancellation choice `A=48` is not a logical parameter.

The Vaaler zero-mode excess is exactly `1/(L+1)=O(L^-1)`. The positive total identity from Stage12 gives

\[
\sum_qA_q(B)=O(B\Lambda^3),
\]

so

\[
\boxed{\mathcal E_{\rm Vaaler}=O(B\Lambda^{-1})}.
\]

This use of Stage12 is only a positive error majorant, not a source of directional proportions.

Consequently

\[
\boxed{
A_q(B)\sim\Theta J_qB(\log B)^3
}
\]

with one common `Theta`.

---

## 10. Calibration of the common constant only after commonness

Summing the raw asymptotics and using `sum J_q=pi/4`,

\[
\sum_qA_q(B)\sim\Theta\frac\pi4B(\log B)^3.
\]

The exact Stage12 bridge gives

\[
C_{\rm prim}(B)=2\sum_qA_q(B),
\]

hence

\[
C_{\rm prim}(B)\sim\Theta\frac\pi2B(\log B)^3.
\]

Compare with the frozen Stage12 theorem:

\[
\Theta\frac\pi2=\frac\kappa{12\pi},
\]

so

\[
\boxed{\Theta=\frac\kappa{6\pi^2}}.
\]

Since `J_q=2I_q/pi`,

\[
\boxed{
A_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3.
}
\]

The order is non-circular:

```text
local arithmetic commonness
-> common Theta
-> sum over q
-> frozen Stage12 total calibration.
```

No Stage12 directional constant is used upstream.

---

## 11. Finite directional discrepancy is not an omitted theorem premise

At `B=100000`, exactly-one counts are

```text
(84146, 43180, 40704)
```

with normalized vector approximately

```text
(0.500779622686425,
 0.256977920609415,
 0.242242456704160).
```

At `B=5000000`, the counts are

```text
(7846274, 4018971, 3708949)
```

with vector

```text
(0.503799682988410,
 0.258053225739979,
 0.238147091271611).
```

Over this audited endpoint interval the L1 distance to exact `2:1:1` increases from about `0.0155151` to `0.0237058`, while the distance to the claimed limiting vector decreases from about `0.0679146` to `0.0618745`. The finite population therefore does not remain stationary at `2:1:1`.

This is diagnostic only. The theorem proves a little-`o` remainder and does **not** give an effective function controlling the ratio at `B=5m`. Accordingly

```text
FINITE_DATA_CONTRADICTS_THEOREM=false
PROVED_EFFECTIVE_CONVERGENCE_RATE=false
FINITE_DISCREPANCY_QUANTITATIVELY_EXPLAINED_BY_PROVED_REMAINDER=false
```

are part of the theorem scope. Finite data neither prove nor disprove the common-`Theta` argument.

---

## 12. Exact inert local state for a second-face test

For a tagged raw incidence

\[
x^2+y^2=P^2,\qquad P^2+z^2=d^2,
\]

a second face sharing tagged leg `x` requires

\[
x^2+z^2=w^2.
\]

For inert odd `p congruent 3 mod 4`, define

\[
W_p=1_{\{x^2+z^2\in QR_0(\mathbf F_p)\}}.
\]

Write

\[
a=v_p(h),\qquad b=v_p(r),\qquad c=v_p(s).
\]

Primitivity forces `a=0`: if `p|h`, then `p|P,z`, while inertness in `x^2+y^2=P^2` forces `p|x,y`, contradicting gcd one. Also `(r,s)=1` gives `min(b,c)=0`. The complete valuation states are therefore

```text
U   = (0,0,0)
R_b = (0,b,0), b>=1
S_c = (0,0,c), c>=1.
```

The unrestricted zero-mode inert local series is

\[
L_{p,0}(Y,Z)=\frac{1-YZ}{(1-Y)(1-Z)}.
\]

At `Y=Z=1/p`,

\[
L_{p,0}=\frac{p+1}{p-1},
\]

and positive-valuation mass is exactly

\[
\frac2{p-1},
\]

or fraction

\[
\boxed{\frac2{p+1}}.
\]

Every positive-valuation state passes automatically, because `p|P` forces `x=y=0 mod p` while `z` is a unit.

---

## 13. Exact inert unit-state character sum

On `U`, normalize `P=1`:

\[
X^2+Y^2=1,\qquad \Delta^2-Z^2=1.
\]

For `p congruent 3 mod 4`, the circle has `p+1` points and the hyperbola `p-1`, hence

\[
T=p^2-1
\]

unit states.

Let `chi` be the quadratic character with `chi(0)=0`. The symbolic sum

\[
S=\sum_{x,z}
(1+\chi(1-x^2))(1+\chi(1+z^2))\chi(x^2+z^2)
\]

splits as `S0+S1+S2+S3`. The quadratic character identity

\[
\sum_t\chi(t^2-A)=-1\quad(A\ne0)
\]

and the Jacobi sum give

\[
S_0=0,\qquad S_1=p-1,\qquad S_2=p+1.
\]

After `u=x^2`, `t=-z^2`, the final term is `A+B-C-D` with

\[
(A,B,C,D)=(0,-1,1,0),
\]

so

\[
S_3=-2,
\qquad
\boxed{S=2(p-1)}.
\]

Exactly four unit states have `X^2+Z^2=0`. Therefore the accepted unit count is

\[
\frac{T+S+4}{2}=\frac{(p+1)^2}{2},
\]

and

\[
\boxed{\alpha_p=\frac{p+1}{2(p-1)}}.
\]

Adding the automatically accepted positive-valuation mass gives

\[
L^W_{p,0}=\frac{p+5}{2(p-1)}.
\]

Thus the exact constrained/unrestricted multiplier is

\[
\boxed{
\lambda_p=\frac{p+5}{2(p+1)}
=\frac12+\frac2{p+1}.
}
\]

For every inert `p>=7`,

\[
\boxed{\lambda_p\le\frac34}.
\]

There are infinitely many primes `3 mod 4` by the elementary Euclidean argument applied to `4p_1...p_k-1`; no Dirichlet theorem on arithmetic progressions is needed.

---

## 14. Fixed inert-prime residue transfer: full character argument

A unit residue predicate is not merely a replacement of one Euler factor: the residue of a multiplicatively built coordinate depends on all prime factors. We therefore separate p-adic valuation strata from unit residue conditions.

Fix a finite inert-prime set

\[
S=\{p_1,\dots,p_k\}
\]

before `B` grows. On each valuation stratum, the remaining unit predicate is a finite function on a finite product of residue groups `G_p`. Fourier inversion gives

\[
W_p(u)=\sum_{\chi\in\widehat G_p}c_{p,\chi}\chi(u).
\]

CRT tensors the groups and gives an exact finite expansion

\[
W_S=\prod_{p\in S}W_p
=
\sum_{\boldsymbol\chi\in\widehat G_S}
 c_{S,\boldsymbol\chi}\boldsymbol\chi.
\]

The auxiliary residue coordinates may satisfy algebraic relations, so the safe leading classification is not “the literally all-trivial auxiliary tuple.” Define the **principal pole sector** to be the full set of auxiliary character tuples whose induced characters on every unbounded pole-producing multiplicative channel are principal.

Summing this entire sector exactly reproduces the finite accepted local average at each `p`; hence its top coefficient is

\[
\boxed{
2D_q\prod_{p\in S}\lambda_p,
\qquad
D_q=\frac{\kappa I_q}{3\pi^3}.
}
\]

The factor `2` is only the safe two-tag upper multiplicity. It is not an exact two-to-one assertion about pair-overlap objects.

### Mixed correction in the character sectors

Outside the fixed modulus, the principal sector has the same infinite split-prime mixed correction as the raw zero mode. The finitely many modulus primes are absorbed into the finite local multiplier.

For a nonprincipal fixed-conductor sector, inserted character phases have modulus at most one. The Gate-B Wiener estimate is phase-uniform, so the same coefficientwise majorant applies. Therefore the mixed correction remains absolutely convergent and holomorphic on the same half-plane, has the same finite logarithmic moments, and cannot create or restore a pole at `s=1`.

### Pole loss outside the principal sector

Every tuple outside the principal pole sector makes at least one unbounded pole-producing channel nonprincipal. That channel is then represented by a fixed-conductor nonprincipal Dirichlet or Gaussian-Hecke factor, holomorphic at `s=1` by the external contracts. Hence the total zero-mode pole order drops by at least one.

The same finite Riesz/Perron/residue machinery gives at most `O_S(B(log B)^2)` at the rectangular zero-mode level, plus the already-audited curved/harmonic lower-order terms. Since the character expansion is finite for fixed `S`, all nonprincipal sectors together are

\[
\boxed{o_S(B(\log B)^3)}.
\]

Thus, for fixed `S`, the tagged constrained raw count satisfies

\[
\boxed{
A^{\rm tag}_{q,S}(B)
=
2D_q\left(\prod_{p\in S}\lambda_p\right)
B(\log B)^3
+o_S(B(\log B)^3).
}
\]

No uniformity as `|S|` grows is asserted or needed.

---

## 15. Pair and triple overlaps

Choose `k` distinct inert primes `p_i>=7`, set `S_k={p_1,...,p_k}`, and hold `S_k` fixed. Every pair-overlap object passes every selected second-face test, with an appropriate shared-edge tag. Therefore

\[
O_{qr}(B)\le A^{\rm tag}_{q,S_k}(B).
\]

Taking `B->infinity` first,

\[
\limsup_{B\to\infty}
\frac{O_{qr}(B)}{B(\log B)^3}
\le
2D_q\prod_{p\in S_k}\lambda_p
\le
2D_q\left(\frac34\right)^k.
\]

Only after this limsup do we let `k->infinity`. Hence

\[
\boxed{O_{qr}(B)=o(B(\log B)^3)}.
\]

The triple overlap is a subset of every pair overlap, so

\[
\boxed{T(B)=o(B(\log B)^3)}.
\]

The permanent quantifier order is

```text
fix S_k
-> B -> infinity
-> take limsup
-> k -> infinity.
```

There is no `k=k(B)` and no growing modulus.

---

## 16. Exactly-one theorem

Insert the overlap estimates into

\[
N_q=A_q-O_{qr}-O_{qs}+T.
\]

The raw directional asymptotic gives

\[
\boxed{
N_q(B)\sim
\frac{\kappa I_q}{3\pi^3}B(\log B)^3.
}
\]

Summing and using `sum I_q=pi^2/8`,

\[
\boxed{
N_1(B)\sim\frac\kappa{24\pi}B(\log B)^3.
}
\]

Dividing gives

\[
\boxed{
\frac{N_q(B)}{N_1(B)}\to\frac{8I_q}{\pi^2}.
}
\]

No perfect-cuboid nonexistence assumption has appeared.

---

## 17. Consolidated quantitative ledger

With `Lambda=log B`,

```text
H0 = U = exp(Lambda^(1/4))
eta = Lambda^(-8)
epsilon = 1/16
zero-mode finite remainder order N = 64
Vaaler degree L = floor(Lambda^4)
box count = O(Lambda^27)
```

we have

```text
small height                  O(B Lambda^(9/4))
small coordinate              O(B Lambda^(5/2))
mixed logarithmic shifts      O(B Lambda^2)
all-box finite remainders     O(B Lambda^(-35))
power tails                   B Lambda^(C_rect+27) exp(-(3/16)Lambda^(1/4))
curved boundary               O(B Lambda^(-5)) + lower-order ledger
interior mesh                 O(B Lambda^(-5))
Vaaler zero-mode excess       O(B Lambda^(-1))
retained harmonic core        B Lambda^(4C_H+D_H+6) exp(-delta_H Lambda^(1/4))
```

Every term is `o(B Lambda^3)`. The fixed historical value `A=48` is not required.

---

## 18. Deterministic audits: exact scope

Repository CI and deterministic scripts check reproducibility and consistency only. They are not substitutes for the mathematical arguments above.

They may verify, for example:

- chamber quadrature and `J_q=2I_q/pi` numerically;
- exact finite Stage12/Stage13 factor-two checksums;
- exact unit-state enumeration for small inert primes;
- exact constants such as `3465625/6561<529`;
- the declared box exponent `27`, finite remainder order `64`, and workflow locks;
- absence of superseded formulas in the R05 proof core.

A displayed `PASS` therefore means

```text
DETERMINISTIC_AUDIT_SCOPE=REPRODUCIBILITY_AND_CONSISTENCY_ONLY
```

and does not mean “the theorem has been proved by computation.”

---

## 19. Imported source boundary and historical nondependencies

The final proof imports:

1. frozen Stage12 R09 total primitive-oriented theorem and its explicit counting definition;
2. classical Hecke continuation/functional equation for the Gaussian angular characters and fixed finite twists;
3. the classical Dirichlet `L(s,chi_4)` continuation/functional equation;
4. Vaaler's finite sawtooth approximation.

The Gaussian angular normalization is the one recorded in Huang--Liu--Rudnick, `Gaussian primes in almost all narrow sectors`, §2.1; the fixed Gaussian residue-character model is the one recorded in Merikoski, `On Gaussian primes in sparse sets`, §2.7; Vaaler is `Some extremal functions in Fourier analysis` (1985). The stronger Gaussian zero-free-region references are valid context but not required.

The following historical routes are not proof dependencies:

```text
Stage13-7jb old direction-neutrality route
Stage13-7jf old compressed fixed-prime route
R01/R02/R03/R04 verdicts as mathematical evidence
finite directional fitting as proof of the limiting vector
finite-field enumeration as proof of alpha_p
old categorywise D_q/K_q equality as proof of common Theta
general Selberg--Delange as a black box
Gaussian-Hecke zero-free region
Dirichlet theorem on primes in arithmetic progressions
growing-modulus sieve theorem
```

---

## 20. R05 canonical theorem lock

```text
COUNTING_CONVENTION=primitive canonical exactly-one-face count with integer space diagonal
STAGE12_COUNTING_TARGET=PRIMITIVE_ORIENTED_DISTINGUISHED_FACE_RECORDS
STAGE12_PRIMITIVE_DEFINITION=MOBIUS_COMMON_SCALE
STAGE12_INPUT=C_prim(B)~kappa/(12*pi)B(log B)^3
STAGE12_KAPPA_EXPLICIT=true
STAGE12_ETA_EQUALS_PI_KAPPA=true
STAGE13_PROJECTION_FIBER=2
PROJECTION_FIBER_REASON=TWO_ORDERS_OF_DISTINGUISHED_FACE_LEGS
JQ_BRIDGE=J_q=2*I_q/pi
RAW_DIRECTIONAL=A_q(B)~kappa*I_q/(3*pi^3)B(log B)^3
COMMON_THETA_PROVED_BEFORE_STAGE12_CALIBRATION=true
WIENER_EXACT_CONSTANT=3465625/6561
WIENER_ROUNDED_CONSTANT=529
P5_EXPLICIT_FINITE_BOUND_LT=432
BOX_COUNT=O((log B)^27)
FINITE_REMAINDER_N=64
FINITE_REMAINDER_AFTER_ALL_BOXES=O(B(log B)^-35)
FIXED_A48_REQUIRED=false
HECKE_FAMILY_BOUND=all_ell_polynomial_conductor_times_fixed_power_saving
VAALER_ZERO_MODE_EXCESS=1/(L+1)
VAALER_NONZERO_COEFFICIENT_BOUND_LT=1
INERT_LOCAL_MULTIPLIER=lambda_p=(p+5)/(2*(p+1))
FIXED_RESIDUE_TRANSFER=FINITE_CHARACTER_ORTHOGONALITY_PLUS_CRT
PRINCIPAL_POLE_SECTOR_MULTIPLIER=product_{p_in_S}_lambda_p
AUXILIARY_CHARACTER_ALIASING_INCLUDED=true
NONPRINCIPAL_POLE_SECTOR_LOSS_AT_LEAST_ONE=true
LIMIT_ORDER=FIX_S_THEN_B_TO_INFINITY_THEN_ENLARGE_S
PAIR_OVERLAP=O_qr(B)=o(B(log B)^3)
TRIPLE_OVERLAP=T(B)=o(B(log B)^3)
EXACT_ONE_DIRECTIONAL=N_q(B)~kappa*I_q/(3*pi^3)B(log B)^3
EXACT_ONE_TOTAL=N1(B)~kappa/(24*pi)B(log B)^3
DIRECTION_LIMIT=P_q=8*I_q/pi^2
CHAMBER_SUM=sum I_q=pi^2/8
FINITE_DATA_CONTRADICTS_THEOREM=false
PROVED_EFFECTIVE_CONVERGENCE_RATE=false
DETERMINISTIC_AUDIT_SCOPE=REPRODUCIBILITY_AND_CONSISTENCY_ONLY
NO_PERFECT_CUBOID_NONEXISTENCE_ASSUMPTION=true
GAUSSIAN_HECKE_ZERO_FREE_REGION_REQUIRED=false
GENERAL_SELBERG_DELANGE_REQUIRED=false
GROWING_MODULUS_THEOREM_USED=false
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
R03_IMMUTABLE=true
R04_IMMUTABLE=true
```

This is the repaired canonical proof candidate to be frozen into R05 only after Gate H's deterministic synthesis audit passes.