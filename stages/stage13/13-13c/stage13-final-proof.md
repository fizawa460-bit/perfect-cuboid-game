# Stage13 — canonical final proof

> STATUS: `STAGE13_13C_CANONICAL_PROOF_RESYNTHESIS`
>
> PURPOSE: give one self-contained proof of the frozen Stage13 exactly-one directional asymptotic, without requiring the reader to reconstruct the R01/R02/R03 repair history.
>
> FROZEN INPUT: Stage12 R09 primitive-oriented total theorem.
>
> SOURCE LOCK: Stage13-13a claim/dependency ledger + Stage13-13b external-theorem audit + immutable R03 + the proof-explicitness content of Stage13-12ag.
>
> THEOREM CHANGED: `false`.
>
> R03 REWRITTEN: `false`.

---

## 0. The theorem and the proof boundary

Consider primitive canonical integer triples

\[
0<a<b<c,
\qquad \gcd(a,b,c)=1,
\qquad d^2=a^2+b^2+c^2,
\qquad d\in\mathbf Z_{>0}.
\]

For a face label

\[
q\in\{ab,ac,bc\},
\]

let `A_q(B)` be the number of such triples with `d<=B` for which the face `q` has integral diagonal, without excluding the possibility that another face is also integral.

For distinct face labels `q,r`, let `O_{qr}(B)` be the count for which both faces `q` and `r` have integral diagonals, and let `T(B)` be the count for which all three face diagonals are integral.

Let `N_q(B)` be the count with **exactly one** integral face diagonal, that unique face being `q`, and let

\[
N_1(B)=N_{ab}(B)+N_{ac}(B)+N_{bc}(B).
\]

Define the canonical spherical chamber

\[
\mathcal R
=\{(x,y,z)\in S^2:0<x<y<z\}
\]

and the three Gelfand--Leray weights

\[
w_{ab}=\frac1{\sqrt{x^2+y^2}},
\qquad
w_{ac}=\frac1{\sqrt{x^2+z^2}},
\qquad
w_{bc}=\frac1{\sqrt{y^2+z^2}}.
\]

Put

\[
I_q=\int_{\mathcal R}w_q\,d\omega.
\]

The Stage13 theorem is

\[
\boxed{
N_q(B)
\sim
\frac{\kappa I_q}{3\pi^3}B(\log B)^3
\qquad(q\in\{ab,ac,bc\}),
}
\]

and

\[
\boxed{
N_1(B)
\sim
\frac{\kappa}{24\pi}B(\log B)^3.
}
\]

Moreover

\[
\boxed{
I_{ab}+I_{ac}+I_{bc}=\frac{\pi^2}{8}
}
\]

and therefore

\[
\boxed{
\frac{N_q(B)}{N_1(B)}\longrightarrow\frac{8I_q}{\pi^2}.
}
\]

The numerical validator for the ordered vector `(ab,ac,bc)` is

```text
(0.5347369332313988,
 0.24535917783225203,
 0.21990388893634913)
```

but the exact integral formulas, not the decimal values, are authoritative.

### External inputs

The proof uses only the following non-repository inputs.

1. **Frozen Stage12 R09 theorem.** For the Stage12 primitive oriented count,
   \[
   C_{\rm prim}(B)
   \sim
   \frac{\kappa}{12\pi}B(\log B)^3.
   \]
2. **Standard Dirichlet/Hecke analytic theory.** The fixed-field Dirichlet and Gaussian Hecke `L`-functions used below have the required analytic continuation, functional equation and polynomial strip/conductor growth. For nonzero Gaussian angular index the Hecke `L`-function is holomorphic at `s=1`.
3. **Vaaler interval approximation.** A periodic interval indicator admits degree-`L` trigonometric majorants/minorants with zero-mode excess `O(1/L)` and controlled Fourier coefficients.

The historical general Selberg--Delange theorem and the stronger Gaussian-Hecke zero-free region are compatible with the proof but are not logical gates in this canonical version. The only pole orders needed are `0,1,2`; they are handled below by a special Perron/residue lemma.

---

## 1. Exact combinatorics and the Stage12 projection bridge

The exactly-one identities are finite identities:

\[
\boxed{
N_q(B)=A_q(B)-O_{qr}(B)-O_{qs}(B)+T(B),
}
\]

where `{q,r,s}={ab,ac,bc}`, and

\[
\boxed{
N_1(B)
=\sum_qA_q(B)-2\sum_{q<r}O_{qr}(B)+3T(B).
}
\]

No asymptotic argument enters here.

The exact Stage12-to-Stage13 projection multiplicity is

\[
\boxed{
C^{\rm proj}_{\rm prim,q}(B)=2A_q(B),
\qquad
C_{\rm prim}(B)=2\sum_qA_q(B).
}
\]

The factor `2` is a finite orientation/projection multiplicity. It is not fitted from data and it is not a limiting statement.

The proof therefore separates into two tasks:

1. prove the raw directional asymptotic for `A_q(B)` with one common arithmetic factor;
2. prove every pair overlap is `o(B(log B)^3)`.

The exactly-one theorem will then follow from the identities above.

---

## 2. Canonical chamber geometry

Fix the distinguished face `ab`. Introduce its face diagonal `p` and the space diagonal `d` through

\[
a^2+b^2=p^2,
\qquad
p^2+c^2=d^2.
\]

For the two quadratic constraints

\[
F_1=a^2+b^2-p^2,
\qquad
F_2=p^2+c^2-d^2,
\]

one has

\[
\det\frac{\partial(F_1,F_2)}{\partial(p,d)}=4pd.
\]

After radial normalization to the unit sphere, the corresponding directional density is therefore proportional to

\[
\frac1{p/d}
=\frac1{\sqrt{x^2+y^2}},
\]

which is `w_ab`. Permuting the distinguished face gives `w_ac,w_bc`.

Thus

\[
I_q=\int_{\mathcal R}w_q\,d\omega
\]

is the exact archimedean category factor.

The three canonical categories partition the relevant ordered angular data, and the chamber calculation gives

\[
\boxed{
I_{ab}+I_{ac}+I_{bc}=\frac{\pi^2}{8}.
}
\]

Pointwise on the chamber,

\[
w_{ab}>w_{ac}>w_{bc},
\]

so the limiting directional proportions are not `2:1:1`; their exact values will be obtained only after the arithmetic factor is proved common.

---

## 3. Exact bridge from the chamber integral to the zero Fourier kernel

For a fixed distinguished face `q={i,j}`, let `k` be the complementary coordinate. Use `q`-adapted spherical coordinates

\[
x_i=\sin\theta\cos\alpha,
\qquad
x_j=\sin\theta\sin\alpha,
\qquad
x_k=\cos\theta,
\]

with `0<theta,alpha<pi/2`.

For this face

\[
\sqrt{x_i^2+x_j^2}=\sin\theta,
\]

hence

\[
w_q=\frac1{\sin\theta}.
\]

Since

\[
d\omega=\sin\theta\,d\theta\,d\alpha,
\]

there is exact cancellation:

\[
\boxed{
w_q\,d\omega=d\theta\,d\alpha.
}
\]

Set

\[
\psi=\frac\pi2-\theta.
\]

For fixed `psi`, let `E_q(psi)` be the interval set of inner angles `alpha` which lie in the canonical chamber and define

\[
\ell_q(\psi)=|E_q(\psi)|.
\]

The integrand is nonnegative, so Tonelli applies immediately. The angular domain has finite measure, so ordinary Fubini then follows. Consequently

\[
\boxed{
I_q=\int\ell_q(\psi)\,d\psi.
}
\]

Now write the primitive outer Pythagorean pair in polar form

\[
r=R\cos\phi,
\qquad
s=R\sin\phi,
\qquad
\phi\in[\pi/4,\pi/2].
\]

The standard outer parameterization is

\[
P=hrs,
\qquad
z=\frac{h(s^2-r^2)}2,
\qquad
d=\frac{h(r^2+s^2)}2.
\]

Hence

\[
\frac Pd=\sin(2\phi),
\qquad
\frac zd=-\cos(2\phi),
\]

and therefore

\[
\boxed{
\psi=2\phi-\frac\pi2,
\qquad d\psi=2\,d\phi.
}
\]

The ordered inner Pythagorean angle has total length `pi/4`. Thus the zero Fourier coefficient of the category indicator is

\[
k_q(\phi)=\frac{\ell_q(\psi)}{\pi/4}
=\frac4\pi\ell_q(\psi).
\]

Define

\[
J_q=\int_{\pi/4}^{\pi/2}k_q(\phi)\,d\phi.
\]

Then

\[
\begin{aligned}
J_q
&=\int\frac4\pi\ell_q(\psi)\frac{d\psi}{2}\\
&=\frac2\pi I_q.
\end{aligned}
\]

Therefore

\[
\boxed{
J_q=\frac{2I_q}{\pi},
\qquad
\sum_qJ_q=\frac\pi4.
}
\]

This is an analytic identity. Earlier numerical quadrature is only a validator.

---

## 4. Primitive outer coordinates and the raw `j=0` coefficient system

On each fixed OE/EE parity branch use

\[
P=hrs,
\qquad
z=\frac{h(s^2-r^2)}2,
\qquad
d=\frac{h(r^2+s^2)}2,
\qquad(r,s)=1.
\]

The OE/EE distinction is finite and 2-adic. For odd primes the coefficient system is the same; the branch constants will enter only the common arithmetic scalar.

Let `p≡1 mod 4` be split. For the scale variable and one base variable write

\[
a=v_p(h),
\qquad b=v_p(rs),
\qquad e=a+b.
\]

Because `(r,s)=1`, at most one base variable carries positive `p`-valuation.

For zero angular mode the Gaussian representation multiplicity is

\[
G_e=2e+1.
\]

For angular phase `theta`, let

\[
H_e(\theta)=1+2\sum_{m=1}^e\cos(m\theta).
\]

Primitive support subtraction gives exactly

\[
Z_0(a,b)
=G_{a+b}-\mathbf1_{a\ge1}G_{a+b-1}
=
\begin{cases}
2b+1,&a=0,\\
2,&a\ge1,
\end{cases}
\]

and

\[
Z_\ell(a,b;\theta)
=H_{a+b}(\theta)-\mathbf1_{a\ge1}H_{a+b-1}(\theta)
=
\begin{cases}
H_b(\theta),&a=0,\\
2\cos((a+b)\theta),&a\ge1.
\end{cases}
\]

No chamber constant and no Stage12 value of `kappa` enters these local identities.

For the pure scale axis put `x=p^{-s_h}` and for one base axis put `y=p^{-s_r}`. Then for nonzero angular phase

\[
A_\ell(x)
=1+\sum_{a\ge1}2\cos(a\theta)x^a
=\frac{1-x^2}{1-2\cos\theta\,x+x^2},
\]

\[
B_\ell(y)
=1+\sum_{b\ge1}H_b(\theta)y^b
=\frac{1+y}{1-2\cos\theta\,y+y^2}.
\]

At zero mode,

\[
A_0(x)=\frac{1+x}{1-x},
\qquad
B_0(y)=\frac{1+y}{(1-y)^2}.
\]

After collecting the inert and finite 2-adic factors into residual Euler products, the one-variable Dirichlet factors have the forms

\[
\boxed{
A_0(s)=\zeta(s)L(s,\chi_4)E_{h,0}(s),
}
\]

\[
\boxed{
B_0(s)=\zeta(s)^2L(s,\chi_4)E_{b,0}(s),
}
\]

while for every nonzero retained harmonic

\[
\boxed{
A_\ell(s)=L(s,\xi_{8\ell})E_{h,\ell}(s).
}
\]

The crucial pole pattern is therefore

```text
zero mode:        scale pole order 1, base pole orders 2 and 2
nonzero harmonic: scale pole order 0
```

and this conclusion has been obtained without seeding any categorywise asymptotic constant.

---

## 5. The three-variable mixed correction

At a split prime the full local series is

\[
\begin{aligned}
D_\ell(x,y,z)
={}&1
+\sum_{a\ge1}2\cos(a\theta)x^a\\
&+\sum_{b\ge1}H_b(\theta)(y^b+z^b)\\
&+\sum_{a,b\ge1}2\cos((a+b)\theta)x^a(y^b+z^b).
\end{aligned}
\]

There is no term with positive exponents in both `y` and `z` because `(r,s)=1`.

Factor

\[
C_\ell(x,y,z)
=\frac{D_\ell(x,y,z)}{A_\ell(x)B_\ell(y)B_\ell(z)}.
\]

The pure axes agree exactly:

\[
D_\ell(x,0,0)=A_\ell(x),
\quad
D_\ell(0,y,0)=B_\ell(y),
\quad
D_\ell(0,0,z)=B_\ell(z).
\]

Thus every nonconstant monomial of `C_ell-1` has support on at least two coordinates.

For

\[
\sigma=\frac58,
\qquad
\rho=p^{-5/8},
\]

define the weighted Wiener norm

\[
\|F\|_\rho
=\sum_{a,b,c\ge0}|f_{a,b,c}|\rho^{a+b+c}.
\]

It is submultiplicative directly from the Cauchy product and Tonelli.

The explicit local estimates give, for every split `p>=13` and every angular phase,

\[
\boxed{
\|C_{\ell,p}-1\|_{5/8}
\le529p^{-5/4}.
}
\]

The finite split prime `p=5` is separated once. Since

\[
\sum_{p\equiv1(4)}p^{-5/4}<\infty,
\]

the global mixed correction converges in the weighted Wiener algebra uniformly over the retained harmonic range.

Writing

\[
C_\ell(\mathbf s)
=\sum_{u,v,w\ge1}
\frac{c_\ell(u,v,w)}{u^{s_h}v^{s_r}w^{s_s}},
\]

we also have, for each fixed integer `m>=0`,

\[
\boxed{
\sum_{u,v,w}
\frac{|c_\ell(u,v,w)|(1+\log(uvw))^m}{uvw}<\infty
}
\]

uniformly over retained harmonics.

Hence convolution-induced shifts such as

\[
\log R\mapsto\log R-\log v
\]

are absolutely summable, and every term containing at least one logarithm of a correction variable lowers the logarithmic degree in `B`.

In particular, the top-degree category factor remains entirely archimedean, through `J_q`; the mixed correction contributes only a common arithmetic scalar at top degree.

---

## 6. Special Perron/residue lemma for pole orders `0,1,2`

We isolate the only one-variable analytic statement needed in this proof.

### Lemma

Suppose

\[
F(s)=\zeta(s)^mH(s),
\qquad m\in\{0,1,2\},
\]

where `H` is holomorphic in a fixed half-plane

\[
\Re s\ge\sigma_0<1,
\]

has polynomial vertical growth there, and the Dirichlet coefficients have polynomial growth sufficient for truncated Perron inversion.

Then a standard finite Perron contour, shifted from `Re s>1` to a fixed line `Re s=sigma_1` with `sigma_0<sigma_1<1`, gives:

- if `m=0`, no pole is crossed and the summatory function has a fixed power saving;
- if `m=1`, the only residue is at `s=1` and the main term is `cX`;
- if `m=2`, the double pole at `s=1` gives `X(c_1 log X+c_0)`;
- in each case the fixed power saving is stronger than `O_A(X(log X)^-A)` for every fixed `A` after `X` is sufficiently large.

### Verification for Stage13

For the zero-mode factors,

\[
A_0(s)=\zeta(s)G_h(s),
\qquad
B_0(s)=\zeta(s)^2G_b(s),
\]

with

\[
G_h=L(s,\chi_4)E_{h,0}(s),
\qquad
G_b=L(s,\chi_4)E_{b,0}(s).
\]

The residual local quotient is `1+O(p^{-2sigma})` for `sigma>1/2`, after finitely many local factors are separated. Hence the residual Euler products converge absolutely and locally uniformly in every fixed half-plane `Re s>=1/2+delta`; they are holomorphic there. The fixed Dirichlet factor `L(s,chi_4)` is holomorphic at `s=1`.

Thus

\[
\sum_{h\le X}a_0(h)
=\alpha X+O_A(X(\log 2X)^{-A}),
\]

\[
\sum_{r\le X}b_0(r)
=X(\beta_1\log X+\beta_0)
+O_A(X(\log 2X)^{-A})
\]

for every fixed finite order `A` needed below.

For nonzero harmonic `ell>=1`,

\[
A_\ell(s)=L(s,\xi_{8\ell})E_{h,\ell}(s)
\]

has no zeta pole. Standard Hecke analytic continuation, functional equation and polynomial strip/conductor growth apply. On the retained range

\[
1\le\ell\le(\log X)^4,
\]

the conductor growth is only polylogarithmic. Therefore the same contour argument gives, for some fixed `delta'>0` and fixed `C`,

\[
\sum_{h\le X}a_\ell(h)
\ll X^{1-\delta'}(1+\ell)^C,
\]

uniformly on the retained range. Consequently, for every fixed `A`,

\[
\boxed{
\sum_{h\le X}a_\ell(h)
\ll_A X(\log 2X)^{-A}
\qquad
(1\le\ell\le(\log X)^4).
}
\]

Zeros of `L(s,xi_{8ell})` do not obstruct this contour because the proof contains `L` itself, not `1/L`, `L'/L`, or a fractional power.

This is the only role of the external Dirichlet/Hecke analytic theory in the raw asymptotic.

---

## 7. Zero-mode main term on the physical curved region

The physical cutoff is

\[
h(r^2+s^2)\le2B
\]

on each fixed parity branch.

Convolving the one-variable expansions with the mixed correction is legitimate by the logarithmic moment bound of §5. The top homogeneous logarithmic coefficient is unchanged by the shifts from correction variables; the correction contributes only its common value at `(1,1,1)`.

Separate

\[
H_0=U=\exp((\log B)^{1/4})
\]

and the regions

```text
small height:       h < H0
small coordinate:   min(r,s) < U
core:               h >= H0 and min(r,s) >= U.
```

The positive zero-mode majorants and partial summation give

\[
\mathcal E_{\rm small\ h}
\ll B(\log B)^2\log H_0
=B(\log B)^{9/4},
\]

and

\[
\mathcal E_{\rm small\ coord}
\ll B(\log B)^2(\log U)^2
=B(\log B)^{5/2}.
\]

Both are `o(B(log B)^3)`.

On the core, partition multiplicatively with mesh

\[
e^\eta,
\qquad
\eta=(\log B)^{-8}.
\]

The number of boxes is `O((log B)^C)` for a fixed `C`. The one-variable Perron expansions and a standard convolution-tail split give power-tail errors of the form

\[
(\log B)^C
\left(
H^{3/4+\varepsilon}RS
+HR^{3/4+\varepsilon}S
+HRS^{3/4+\varepsilon}
\right)
\]

on a core rectangle. Since every relevant variable is at least `H0` or `U`, the total core power tail is smaller than every fixed negative power of `log B` times `B`.

Boxes meeting the curved boundary lie in a multiplicative `O(eta)` thickening, so

\[
\mathcal E_{\rm boundary}
\ll
\eta B(\log B)^3+o(B(\log B)^{-100})
=O(B(\log B)^{-5}).
\]

The rectangle main terms form a Riemann sum. The two base pole orders contribute two logarithms, and the radial summation against the homogeneous scale

\[
\frac1{r^2+s^2}
\]

contributes the third logarithm. The angular zero Fourier coefficient is exactly `k_q(phi)`. Hence the zero-mode contribution is

\[
\boxed{
A_q^{(0)}(B)
=\Theta J_q B(\log B)^3
+o(B(\log B)^3)
}
\]

for one arithmetic constant `Theta>0` independent of `q`.

The independence of `q` is now structural: the arithmetic local coefficient system and the mixed Euler correction are common; the category label enters only through the archimedean zero-mode kernel `J_q`.

No Stage12 category constant has been used.

---

## 8. Nonzero harmonics and Vaaler bracketing

Apply Vaaler's periodic interval majorants/minorants of degree

\[
L=(\log B)^4
\]

(with harmless integer flooring).

The constant-term excess is `O(1/L)`. The exact Stage12/Stage13 bridge plus the frozen Stage12 total theorem supplies the positive bound

\[
\sum_qA_q(B)=O(B(\log B)^3),
\]

so the Vaaler excess is

\[
\boxed{
\mathcal E_{\rm Vaaler}
\ll
\frac{B(\log B)^3}{(\log B)^4}
=O(B(\log B)^{-1}).
}
\]

This use of Stage12 is only an error majorant; it does not establish direction-neutrality or category proportions.

For the retained nonzero harmonics choose the finite-order cancellation strength `A=48`. Since on the core

\[
\log H_0=(\log B)^{1/4},
\]

we obtain

\[
(\log H_0)^{-48}=(\log B)^{-12}.
\]

The two base channels and partial-summation bookkeeping cost at most `(log B)^2`, and summing over at most `L=(log B)^4` retained modes gives

\[
\boxed{
\mathcal E_{\rm harm,core}
\ll
B(\log B)^{4+2-12}
=O(B(\log B)^{-6}).
}
\]

The small-height and small-coordinate pieces are dominated in absolute value by the positive zero-mode estimates of §7.

Therefore

\[
\boxed{
A_q(B)
=A_q^{(0)}(B)+o(B(\log B)^3)
}
\]

and hence

\[
\boxed{
A_q(B)
\sim
\Theta J_qB(\log B)^3
}
\]

with the same unknown `Theta` for all three directions.

This completes the non-circular common-factor theorem.

---

## 9. Only now calibrate the common arithmetic constant by Stage12

Sum the raw asymptotics:

\[
\sum_qA_q(B)
\sim
\Theta\left(\sum_qJ_q\right)B(\log B)^3
=\Theta\frac\pi4B(\log B)^3.
\]

The exact factor-two projection gives

\[
C_{\rm prim}(B)=2\sum_qA_q(B),
\]

so

\[
C_{\rm prim}(B)
\sim
\Theta\frac\pi2B(\log B)^3.
\]

The frozen Stage12 R09 theorem is

\[
C_{\rm prim}(B)
\sim
\frac\kappa{12\pi}B(\log B)^3.
\]

Therefore

\[
\Theta\frac\pi2=\frac\kappa{12\pi},
\]

hence

\[
\boxed{
\Theta=\frac\kappa{6\pi^2}.
}
\]

Using

\[
J_q=\frac{2I_q}{\pi},
\]

we obtain the raw directional theorem

\[
\boxed{
A_q(B)
\sim
\frac{\kappa I_q}{3\pi^3}B(\log B)^3.
}
\]

The logical order is essential:

```text
first:  prove one common Theta from the Stage13 arithmetic system;
then:   use Stage12 total mass to determine Theta.
```

Thus the Stage12 theorem does not manufacture the directional proportions.

---

## 10. Exact inert-prime local state for a second-face test

It remains to show pair overlaps are lower order.

Fix one tagged raw incidence

\[
x^2+y^2=P^2,
\qquad
P^2+z^2=d^2.
\]

If a second integral face shares the tagged leg `x`, then

\[
x^2+z^2=w^2.
\]

For an inert odd prime

\[
p\equiv3\pmod4
\]

define

\[
W_p=\mathbf1_{x^2+z^2\in QR_0(\mathbf F_p)}.
\]

Every genuine second-face incidence passes every `W_p`.

Write

\[
a=v_p(h),
\qquad b=v_p(r),
\qquad c=v_p(s).
\]

Because `(r,s)=1`,

\[
\min(b,c)=0.
\]

If `a>=1`, then `p|P,z`. Since `p≡3 mod 4`, `-1` is a nonsquare, and

\[
x^2+y^2\equiv0\pmod p
\]

forces `p|x,y`. Then `p|x,y,z`, contradicting primitivity. Therefore

\[
\boxed{a=0}.
\]

Exactly three valuation-state types remain:

```text
U   : (0,0,0)
R_b : (0,b,0), b>=1
S_c : (0,0,c), c>=1.
```

On `R_b` or `S_c`, `P≡0 mod p` while `z` is a unit. Inertness again gives `x≡y≡0 mod p`, so

\[
x^2+z^2\equiv z^2\not\equiv0\pmod p,
\]

and the test passes automatically.

Hence the only rejecting stratum is the unit state `U`.

The unrestricted inert zero-mode local series is

\[
L_{p,0}(Y,Z)
=1+\sum_{b\ge1}Y^b+\sum_{c\ge1}Z^c
=\frac{1-YZ}{(1-Y)(1-Z)}.
\]

At `Y=Z=1/p`,

\[
\boxed{
L_{p,0}(1,1,1)=\frac{p+1}{p-1},
}
\]

while the total positive-valuation mass is

\[
\boxed{
T_p^+=\frac2{p-1}.
}
\]

Therefore

\[
\boxed{
\frac{T_p^+}{L_{p,0}(1,1,1)}
=\frac2{p+1}\le\frac2p.
}
\]

---

## 11. Exact inert unit-state acceptance

On the unit state normalize by `P`:

\[
X=x/P,
\quad
Y=y/P,
\quad
Z=z/P,
\quad
\Delta=d/P.
\]

Then over `F_p`,

\[
X^2+Y^2=1,
\qquad
\Delta^2-Z^2=1.
\]

Let `chi` be the quadratic character, extended by `chi(0)=0`. Since `p≡3 mod4`,

\[
\chi(-1)=-1.
\]

The circle has `p+1` points and the hyperbola has `p-1` points, so the unit state space has

\[
T=p^2-1
\]

points.

We count the states for which

\[
Q=X^2+Z^2
\]

is a square or zero.

The elementary quadratic-character identity

\[
\sum_{t\in\mathbf F_p}\chi(t^2-A)=-1
\qquad(A\ne0)
\]

and the corresponding Jacobi sum

\[
J(\chi,\chi)=1
\]

are enough.

Eliminating `Y,Delta` by their solution multiplicities, define

\[
S
=\sum_{x,z}
(1+\chi(1-x^2))
(1+\chi(1+z^2))
\chi(x^2+z^2).
\]

Split

\[
S=S_0+S_1+S_2+S_3.
\]

The degree-two character identity gives

\[
S_0=0,
\qquad
S_1=p-1,
\qquad
S_2=p+1.
\]

For the remaining term, put

\[
u=x^2,
\qquad t=-z^2.
\]

Then

\[
S_3
=\sum_{u,t}(1+\chi(u))(1-\chi(t))
\chi((1-u)(1-t)(u-t)).
\]

Writing this as `A+B-C-D`, the same degree-two identities and antisymmetry under `u<->t` give

\[
A=0,
\qquad B=-1,
\qquad C=1,
\qquad D=0,
\]

hence

\[
\boxed{S_3=-2}.
\]

Therefore

\[
\boxed{S=2(p-1)}.
\]

Because `-1` is a nonsquare,

\[
X^2+Z^2=0
\]

forces `X=Z=0`. Then `Y=±1` and `Delta=±1`, so exactly four unit states have `Q=0`.

Using

\[
\mathbf1_{QR_0}(a)
=\frac{1+\chi(a)+\mathbf1_{a=0}}2,
\]

the accepted count is

\[
\frac{T+S+4}{2}
=\frac{(p+1)^2}{2}.
\]

Thus the exact unit-state acceptance is

\[
\boxed{
\alpha_p
=\frac{p+1}{2(p-1)}.
}
\]

This is symbolic; finite-field enumeration is unnecessary for the proof.

---

## 12. Exact inert local multiplier

Normalize the unrestricted unit-state coefficient to `1`. The constrained unit coefficient is `alpha_p`, and every positive-valuation state is accepted. Hence

\[
L^W_{p,0}(1,1,1)
=\alpha_p+\frac2{p-1}
=\frac{p+5}{2(p-1)}.
\]

Dividing by the unrestricted factor gives

\[
\boxed{
\lambda_p
=\frac{L^W_{p,0}(1,1,1)}{L_{p,0}(1,1,1)}
=\frac{p+5}{2(p+1)}.
}
\]

Therefore for every inert prime `p>=7`,

\[
\boxed{
\lambda_p\le\frac34.
}
\]

We need arbitrarily many such primes. No prime-number theorem or Dirichlet theorem is required. If `p_1,...,p_k` were all primes congruent to `3 mod 4`, then

\[
N=4p_1\cdots p_k-1\equiv3\pmod4.
\]

At least one prime divisor of `N` is congruent to `3 mod 4`, and none of the `p_i` divides `N`, a contradiction. Thus there are infinitely many inert primes.

---

## 13. Fixed-prime residue transfer and the order of limits

Fix a finite set `S` of odd inert primes **before** letting `B` grow.

At each `p in S`, split the local state into finitely many residue classes needed to evaluate `W_p`. Finite character orthogonality decomposes the restriction into a finite sum of Dirichlet/Gaussian-Hecke character combinations, and CRT tensors the local conditions across the fixed prime set.

For the principal character tuple, the same zero-mode pole structure remains and the leading constant is multiplied by

\[
\prod_{p\in S}\lambda_p.
\]

For every nonprincipal tuple, at least one principal zeta pole is replaced by a fixed-conductor nonprincipal Dirichlet/Hecke factor holomorphic at `s=1`; the Perron lemma therefore lowers the order. Since `S` is fixed, every conductor here is fixed.

Thus for one tag the constrained raw count has leading multiplier

\[
\prod_{p\in S}\lambda_p
\]

relative to the raw directional main term. Taking both possible face-leg tags gives the harmless upper factor `2`.

No modulus grows with `B`.

---

## 14. Pair overlaps are lower order

Fix a pair type `q,r`. A genuine pair-overlap incidence, with the appropriate shared-edge tag, passes every local test in any chosen finite inert set `S`.

Choose for each integer `k>=1` a set

\[
S_k=\{p_1,\ldots,p_k\}
\]

of distinct inert primes `p_i>=7`.

Hold `S_k` fixed and let `B->infinity`. By the fixed-prime transfer,

\[
\limsup_{B\to\infty}
\frac{O_{qr}(B)}{B(\log B)^3}
\le
2D_q\prod_{i=1}^k\lambda_{p_i},
\]

where

\[
D_q=\frac{\kappa I_q}{3\pi^3}.
\]

Since every factor is at most `3/4`,

\[
\limsup_{B\to\infty}
\frac{O_{qr}(B)}{B(\log B)^3}
\le
2D_q\left(\frac34\right)^k.
\]

Only **after** this `B->infinity` limsup do we let `k->infinity`. Therefore

\[
\boxed{
O_{qr}(B)=o(B(\log B)^3)
}
\]

for every pair of face labels.

The triple overlap is a subset of every pair overlap, so

\[
\boxed{
T(B)=o(B(\log B)^3).
}
\]

No nonexistence assumption for perfect cuboids is used.

---

## 15. Exactly-one directional and total asymptotics

Return to the exact identity

\[
N_q
=A_q-O_{qr}-O_{qs}+T.
\]

The raw theorem gives

\[
A_q(B)
\sim
\frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\]

and every overlap term is lower order. Hence

\[
\boxed{
N_q(B)
\sim
\frac{\kappa I_q}{3\pi^3}B(\log B)^3.
}
\]

Summing over directions and using

\[
\sum_qI_q=\frac{\pi^2}{8},
\]

we obtain

\[
\begin{aligned}
N_1(B)
&\sim
\frac\kappa{3\pi^3}
\frac{\pi^2}{8}
B(\log B)^3\\
&=
\boxed{
\frac\kappa{24\pi}B(\log B)^3
}.
\end{aligned}
\]

Dividing the directional formula by the total formula yields

\[
\boxed{
\frac{N_q(B)}{N_1(B)}
\longrightarrow
\frac{8I_q}{\pi^2}.
}
\]

This proves the frozen Stage13 theorem.

---

## 16. Error and uniformity ledger

For clarity, the quantitative choices used above are

```text
H0 = U = exp((log B)^(1/4))
eta = (log B)^(-8)
L = (log B)^4
finite harmonic cancellation order A = 48.
```

The corresponding raw-directional error ledger is

```text
small height                 O(B (log B)^(9/4))
small coordinate             O(B (log B)^(5/2))
mixed logarithmic shifts     O(B (log B)^2)
rectangle power tails        B(log B)^C exp(-c(log B)^(1/4))
curved boundary / mesh       O(B (log B)^(-5))
Vaaler excess                O(B (log B)^(-1))
all retained harmonics core  O(B (log B)^(-6))
```

Every term is `o(B(log B)^3)`.

The overlap argument has a different and explicit order of limits:

```text
1. choose k and fix S_k;
2. let B -> infinity;
3. take the limsup;
4. only then let k -> infinity.
```

This prevents any hidden growing-modulus input.

---

## 17. What is proved internally and what is imported

### Proved in the Stage13 repository chain and inlined here

- exact inclusion-exclusion;
- exact factor-two Stage12 projection bridge;
- Gelfand--Leray chamber weights;
- chamber/zero-mode bridge `J_q=2I_q/pi`;
- primitive split-prime `j=0` coefficient system;
- uniform weighted-Wiener correction bound;
- logarithmic moments of the mixed correction;
- curved-region decomposition and error budget;
- non-circular common arithmetic factor;
- exact inert valuation-state table;
- exact inert unit-state character sum;
- exact local multiplier `lambda_p=(p+5)/(2(p+1))`;
- fixed-prime order-of-limits squeeze;
- elementary infinitude of primes `3 mod 4`;
- exactly-one transfer.

### Imported

- Stage12 R09 total primitive-oriented asymptotic;
- standard analytic continuation/functional equation/polynomial strip growth for fixed-field Dirichlet and Gaussian Hecke `L`-functions;
- Vaaler's periodic interval majorant/minorant.

### Valid historical references but not required as final logical gates

- general Selberg--Delange black-box formulations;
- Merikoski/Coleman Gaussian-Hecke zero-free regions.

---

## 18. Provenance and supersession

This file is the canonical proof ordering for the future R04 review bundle. It does not mutate the immutable R03 artifact.

The following historical routes are **not** mathematical dependencies of this proof:

```text
Stage13-7jb old categorywise raw direction-neutrality check
Stage13-7jf old fixed-prime overlap presentation
R01 bundle as a proof dependency
R02 bundle as a proof dependency
finite directional fits as proof of limiting proportions
finite-field enumeration as proof of alpha_p
categorywise D_q/K_q numerical equality as proof of commonness
```

The repair history remains useful provenance, but the theorem no longer requires a reader to reconstruct it.

---

## 19. Canonical theorem lock

The proof has reproduced the 13-13a frozen theorem without changing any counting convention or constant:

```text
COUNTING_CONVENTION=primitive canonical exactly-one-face count with integer space diagonal
STAGE12_INPUT=C_prim(B) ~ kappa/(12*pi) B(log B)^3
RAW_DIRECTIONAL=A_q(B) ~ kappa*I_q/(3*pi^3) B(log B)^3
PAIR_OVERLAP=O_qr(B)=o(B(log B)^3)
TRIPLE_OVERLAP=T(B)=o(B(log B)^3)
EXACT_ONE_DIRECTIONAL=N_q(B) ~ kappa*I_q/(3*pi^3) B(log B)^3
EXACT_ONE_TOTAL=N1(B) ~ kappa/(24*pi) B(log B)^3
DIRECTION_LIMIT=P_q=8*I_q/pi^2
CHAMBER_SUM=sum I_q=pi^2/8
JQ_BRIDGE=J_q=2*I_q/pi
INERT_LOCAL_MULTIPLIER=lambda_p=(p+5)/(2*(p+1))
NO_PERFECT_CUBOID_NONEXISTENCE_ASSUMPTION=true
```

```text
STAGE13_13C=COMPLETE_CANONICAL_PROOF_RESYNTHESIS
THEOREM_CHANGED=false
R03_REWRITTEN=false
HISTORICAL_SUPERSEDED_ARGUMENT_REQUIRED=false
MINIMAL_EXTERNAL_BOUNDARY_PRESERVED=true
NEXT=13-13d
```
