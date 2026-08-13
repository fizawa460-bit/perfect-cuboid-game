# Stage13-12ag — post-R03 proof-explicitness supplement

> STATUS: `STAGE13_12AG_COMPLETE_PROOF_EXPLICITNESS_SUPPLEMENT`
>
> PURPOSE: make three already-used steps independently checkable without changing the Stage13 theorem candidate
>
> FROZEN INPUT: Stage12 R09
>
> REVIEWED SNAPSHOT: `STAGE13-FINAL-SELF-CONTAINED-20260809-R03`
>
> R03 REVIEW RECORD SUPPLIED TO THE PROJECT: Grok `CLOSED`, Qwen `CLOSED`

Stage13-12ag does **not** change the counting convention, the directional constants, the exact-one inclusion-exclusion argument, the fixed-prime overlap squeeze, or the R03 theorem candidate.  It is a post-review proof-explicitness supplement addressing three places where a future reader could reasonably ask for one more line of derivation:

1. the coarea/Fubini step identifying the chamber integral `I_q` with an inner-angle interval-length integral;
2. the exact inert-prime character sum behind the unit-state acceptance `(p+1)^2/2`;
3. an explicit hypothesis map from the zero-mode Euler products to the finite-order Selberg--Delange/Tauberian input used by Stage13-12ad.

The R03 HTML is immutable in this step.  Any future refreshed review artifact must receive a new bundle id rather than rewriting R03.

---

## 1. Exact coarea/Fubini bridge from `I_q` to the inner-angle length

Let `q={i,j}` be one distinguished face and let `k` be the complementary edge.  On the positive unit sphere use `q`-adapted spherical coordinates

\[
x_i=\sin\theta\cos\alpha,
\qquad
x_j=\sin\theta\sin\alpha,
\qquad
x_k=\cos\theta,
\]

with `0<theta<pi/2` and `0<alpha<pi/2`.  For this face,

\[
\sqrt{x_i^2+x_j^2}=\sin\theta,
\]

so the Gelfand--Leray weight is

\[
w_q=\frac{1}{\sqrt{x_i^2+x_j^2}}=\frac1{\sin\theta}.
\]

The spherical area element is

\[
d\omega=\sin\theta\,d\theta\,d\alpha.
\]

Therefore the weight cancels the spherical Jacobian **exactly**:

\[
\boxed{w_q\,d\omega=d\theta\,d\alpha.}
\]

Now set the physical outer angle

\[
\psi=\frac\pi2-\theta.
\]

Thus `dtheta=-dpsi`.  For each fixed `psi`, let

\[
E_q(\psi)
:=\{\alpha:\ (x_1,x_2,x_3)\text{ lies in the canonical chamber }0<x<y<z\},
\]

where the coordinates are interpreted in the `q`-adapted order above.  Define

\[
\ell_q(\psi):=|E_q(\psi)|
\]

to be the one-dimensional Lebesgue length of that admissible inner-angle slice.  Fubini's theorem on the chamber now gives

\[
\begin{aligned}
I_q
&=\int_{\mathcal R}w_q\,d\omega\\
&=\int\!\int_{\alpha\in E_q(\psi)}d\alpha\,d\psi\\
&=\boxed{\int \ell_q(\psi)\,d\psi}.
\end{aligned}
\]

This is the missing explicit bridge between the sphere integral definition

\[
I_q=\int_{\mathcal R}w_q\,d\omega
\]

and the inner-angle interval-length formulation used by the zero Fourier kernel.

### 1.1 Outer Pythagorean angle

In the primitive outer parameterization

\[
P=hrs,
\qquad
z=\frac{h(s^2-r^2)}2,
\qquad
d=\frac{h(r^2+s^2)}2,
\]

write

\[
r=R\cos\phi,
\qquad
s=R\sin\phi,
\qquad
\phi\in[\pi/4,\pi/2].
\]

Then

\[
\frac Pd=\frac{2rs}{r^2+s^2}=\sin(2\phi),
\qquad
\frac zd=\frac{s^2-r^2}{r^2+s^2}=-\cos(2\phi).
\]

Hence, with `psi` the angle satisfying `tan psi=z/P`,

\[
\boxed{\psi=2\phi-\frac\pi2},
\qquad
d\psi=2\,d\phi.
\]

The ordered inner Pythagorean face angle has total length `pi/4`.  Therefore the zero Fourier category kernel is exactly the normalized slice length

\[
k_q(\phi)
=\frac{\ell_q(\psi)}{\pi/4}
=\frac4\pi\ell_q(\psi).
\]

Consequently

\[
\begin{aligned}
J_q
&=\int_{\pi/4}^{\pi/2}k_q(\phi)\,d\phi\\
&=\int \frac4\pi\ell_q(\psi)\frac{d\psi}{2}\\
&=\boxed{\frac2\pi I_q}.
\end{aligned}
\]

Thus the full chain

\[
\boxed{
\int_{\mathcal R}w_q\,d\omega
=\int\ell_q(\psi)\,d\psi
\Longrightarrow
J_q=\frac2\pi I_q
}
\]

is now written without a definitional shortcut.  Numerical quadrature remains only a validator.

---

## 2. Exact inert-prime unit-state character sum

Let

\[
p\equiv3\pmod4
\]

be an odd inert prime and let `chi` denote the quadratic character on `F_p`, extended by `chi(0)=0`.  Since `chi(-1)=-1`, define the normalized unit-state varieties

\[
\mathcal C_p=\{(X,Y):X^2+Y^2=1\},
\]

\[
\mathcal H_p=\{(Z,\Delta):\Delta^2-Z^2=1\}.
\]

The second-face local test is

\[
Q(X,Z):=X^2+Z^2\in QR_0(\mathbf F_p).
\]

We prove from scratch that the number of accepted unit states is

\[
\boxed{\frac{(p+1)^2}{2}}.
\]

### 2.1 Elementary quadratic-character lemma

For distinct `a,b in F_p` and `c != 0`,

\[
\boxed{
\sum_{t\in\mathbf F_p}\chi(c(t-a)(t-b))=-\chi(c).
}
\]

Equivalently, for nonzero `A`,

\[
\sum_t\chi(t^2-A)=-1.
\]

This is the standard degree-two character identity and is the only finite-field input needed below.  It also gives the quadratic Jacobi sum

\[
J(\chi,\chi)
:=\sum_u\chi(u)\chi(1-u)
=-\chi(-1)=1
\]

for `p=3 mod 4`.

### 2.2 Total unit states

The number of `Y` for a fixed `X` is

\[
1+\chi(1-X^2).
\]

Therefore

\[
\#\mathcal C_p
=p+\sum_X\chi(1-X^2)
=p+1.
\]

Likewise the number of `Delta` for fixed `Z` is

\[
1+\chi(1+Z^2),
\]

and

\[
\#\mathcal H_p
=p+\sum_Z\chi(1+Z^2)
=p-1.
\]

Hence

\[
T:=\#(\mathcal C_p\times\mathcal H_p)
=(p+1)(p-1)=p^2-1.
\]

### 2.3 The weighted character sum

Set

\[
S
:=\sum_{(X,Y)\in\mathcal C_p}
\sum_{(Z,\Delta)\in\mathcal H_p}
\chi(X^2+Z^2).
\]

Eliminating `Y,Delta` by their solution multiplicities gives

\[
S
=\sum_{x,z}
(1+\chi(1-x^2))
(1+\chi(1+z^2))
\chi(x^2+z^2).
\]

Write

\[
S=S_0+S_1+S_2+S_3
\]

with

\[
S_0=\sum_{x,z}\chi(x^2+z^2),
\]

\[
S_1=\sum_{x,z}\chi(1-x^2)\chi(x^2+z^2),
\]

\[
S_2=\sum_{x,z}\chi(1+z^2)\chi(x^2+z^2),
\]

\[
S_3=\sum_{x,z}
\chi(1-x^2)\chi(1+z^2)\chi(x^2+z^2).
\]

#### The first three terms

For `z=0`,

\[
\sum_x\chi(x^2)=p-1,
\]

while for every `z != 0`,

\[
\sum_x\chi(x^2+z^2)=-1.
\]

Thus

\[
\boxed{S_0=0}.
\]

Similarly, for `x=0` the inner `z`-sum is `p-1`, while for `x != 0` it is `-1`.  Since

\[
\sum_x\chi(1-x^2)=1,
\]

we have

\[
\sum_{x\ne0}\chi(1-x^2)=0
\]

and therefore

\[
\boxed{S_1=p-1}.
\]

For `S_2`, the `z=0` contribution is again `p-1`.  Also

\[
\sum_z\chi(1+z^2)=-1,
\]

so

\[
\sum_{z\ne0}\chi(1+z^2)=-2.
\]

Hence

\[
\boxed{S_2=p+1}.
\]

#### The cubic-looking term `S_3`

Put

\[
u=x^2,
\qquad
t=-z^2.
\]

Because `chi(-1)=-1`, the fiber multiplicities are

\[
\#\{x:x^2=u\}=1+\chi(u),
\]

\[
\#\{z:-z^2=t\}=1-\chi(t).
\]

Thus

\[
S_3
=\sum_{u,t}
(1+\chi(u))(1-\chi(t))
\chi((1-u)(1-t)(u-t)).
\]

Let

\[
K(u,t)=(1-u)(1-t)(u-t)
\]

and define

\[
A=\sum_{u,t}\chi(K(u,t)),
\]

\[
B=\sum_{u,t}\chi(u)\chi(K(u,t)),
\]

\[
C=\sum_{u,t}\chi(t)\chi(K(u,t)),
\]

\[
D=\sum_{u,t}\chi(ut)\chi(K(u,t)).
\]

Then

\[
S_3=A+B-C-D.
\]

For fixed `u != 1`, the polynomial `(1-t)(u-t)` has distinct roots and leading coefficient `+1`, hence its character sum is `-1`.  Therefore

\[
A=-\sum_{u\ne1}\chi(1-u)=0.
\]

The same evaluation with the additional `chi(u)` gives

\[
B=-\sum_u\chi(u)\chi(1-u)
=-J(\chi,\chi)
=-1.
\]

For fixed `t != 1`, the polynomial `(1-u)(u-t)` has leading coefficient `-1`, hence its character sum is

\[
-\chi(-1)=1.
\]

Therefore

\[
C=\sum_t\chi(t)\chi(1-t)
=J(\chi,\chi)
=1.
\]

Finally, interchanging `u` and `t` changes only the factor `(u-t)` in `K`, so

\[
\chi(utK(t,u))
=\chi(-1)\chi(utK(u,t))
=-\chi(utK(u,t)).
\]

The diagonal has zero contribution.  Since the summation domain is symmetric,

\[
\boxed{D=0}.
\]

Consequently

\[
\boxed{S_3=-2}
\]

and hence

\[
\boxed{
S=0+(p-1)+(p+1)-2=2(p-1).
}
\]

### 2.4 Accepted count

Because `-1` is a non-square,

\[
X^2+Z^2=0
\]

forces `X=Z=0`.  Then `Y=+-1` and `Delta=+-1`, so exactly

\[
N_0=4
\]

unit states have `Q=0`.

For any `a in F_p`,

\[
\mathbf 1_{QR_0}(a)
=\frac{1+\chi(a)+\mathbf 1_{a=0}}2.
\]

Therefore

\[
\begin{aligned}
N_{\rm acc}
&=\frac{T+S+N_0}{2}\\
&=\frac{p^2-1+2(p-1)+4}{2}\\
&=\boxed{\frac{(p+1)^2}{2}}.
\end{aligned}
\]

Dividing by `T=p^2-1` yields the exact unit-state acceptance

\[
\boxed{
\alpha_p
=\frac{(p+1)^2/2}{p^2-1}
=\frac{p+1}{2(p-1)}.
}
\]

Thus the Stage13-12ae local multiplier computation

\[
\lambda_p
=\frac{p+5}{2(p+1)}
\]

now rests on an explicit symbolic character-sum derivation, not on finite enumeration.

---

## 3. Selberg--Delange / Tauberian hypothesis crosswalk

Stage13 treats the finite-order Selberg--Delange theorem and the standard Gaussian-Hecke zero-free input as external theorem boundaries, in the same sense as the frozen Stage12 analysis.  This section does not reprove those external theorems; it records exactly why the Stage13 Dirichlet series meet their hypotheses.

### 3.1 Zero mode: one scale variable

Stage13-12aa gives

\[
A_0(s)=\zeta(s)L(s,\chi_4)E_{h,0}(s).
\]

Write

\[
G_h(s):=L(s,\chi_4)E_{h,0}(s).
\]

The residual local quotient has the form

\[
1+O(p^{-2\sigma})
\]

for `sigma>1/2`, after separating finitely many small/2-adic factors.  Hence the Euler product for `E_{h,0}` converges absolutely and locally uniformly in every half-plane

\[
\Re s\ge\frac12+\delta.
\]

Thus `E_{h,0}` is holomorphic there.  The fixed Dirichlet factor `L(s,chi_4)` is holomorphic and nonzero at `s=1`.  Therefore near `s=1`,

\[
A_0(s)=\zeta(s)G_h(s)
\]

has exactly one zeta pole with a holomorphic arithmetic factor.  The finite-order Selberg--Delange theorem with exponent `1` gives

\[
\sum_{h\le X}a_0(h)
=\alpha X+O_N(X(\log 2X)^{-N})
\]

at the external-theorem level used in Stage13-12ad.

### 3.2 Zero mode: each base variable

Likewise

\[
B_0(s)=\zeta(s)^2L(s,\chi_4)E_{b,0}(s)
=\zeta(s)^2G_b(s),
\]

where `G_b` is holomorphic near `1` and its residual Euler product has the same `1+O(p^{-2sigma})` absolute-convergence property after finite local factors are removed.

Thus the zero base channel has exactly a double zeta pole.  Finite-order Selberg--Delange with exponent `2` gives

\[
\sum_{r\le X}b_0(r)
=X(\beta_1\log X+\beta_0)
+O_N(X(\log 2X)^{-N}).
\]

The second base variable is identical.  The finite OE/EE `2`-adic factors alter only the common arithmetic constants and not these pole orders.

### 3.3 Mixed correction

Stage13-12ad proves

\[
\|C_{\ell,p}-1\|_{5/8}\le529p^{-5/4}
\]

for every split `p>=13`, uniformly in retained harmonic phase, with the finite prime `p=5` separated.  Therefore the global mixed Euler product converges in a weighted Wiener algebra and, for every fixed `m`,

\[
\sum_{u,v,w}
\frac{|c_\ell(u,v,w)|(1+\log(uvw))^m}{uvw}<\infty.
\]

This is stronger than what is needed to convolve the one-variable Selberg--Delange expansions: the top logarithmic coefficient is multiplied only by

\[
C_0(1,1,1)
\]

and every convolution-induced logarithmic shift is absolutely summable and lowers the logarithmic degree.

### 3.4 Why the total logarithmic degree is three

The one-scale channel has no logarithm in its summatory main; each of the two base channels contributes one logarithm.  After the scale variable is summed to the physical cutoff

\[
h\le\frac{2B}{r^2+s^2},
\]

the main becomes a direction-neutral constant times

\[
B\sum_{r,s}
\frac{b_0(r)b_0(s)}{r^2+s^2}.
\]

In polar/homogeneous coordinates the radial measure against `(r^2+s^2)^{-1}` supplies one further logarithm, while the two base densities supply the other two.  Hence the zero-mode curved-region main has degree

\[
\boxed{(\log B)^3}.
\]

The angular slice is exactly `J_q`; no arithmetic factor introduced in this reduction depends on the category.

### 3.5 Nonzero harmonics

For `ell>=1`, the scale factor is

\[
A_\ell(s)=L(s,\xi_{8\ell})E_{h,\ell}(s),
\]

with **no zeta pole**.  The residual Euler products are uniformly controlled by the same Wiener estimate.  The external Gaussian-Hecke input used by Stage13-12ad supplies a zero-free region whose conductor dependence is logarithmic in `2+|8ell|`; for

\[
1\le\ell\le(\log B)^4
\]

this is only polylogarithmic.  A possible exceptional real zero occurs only in the zero angular frequency and is therefore absent here.  The finite-order Perron/Selberg--Delange consequence used in Stage13-12ad is consequently

\[
\sum_{h\le X}a_\ell(h)
\ll_{A,K}X(\log 2X)^{-A}
\]

uniformly for the retained range.  With `A=48` and `K=4`, the harmonic sum remains `O(B(log B)^-6)` after the two base logarithms and the harmonic count are included.

### 3.6 External theorem boundary, explicitly separated

The proof therefore separates into:

```text
proved inside Stage13:
  exact local factors
  residual 1+O(p^-2sigma) Euler convergence
  weighted-Wiener mixed correction and all log moments
  pole/no-pole classification
  coarea/chamber geometry
  curved-region error budget
  fixed-prime p-adic state calculation

external analytic theorem boundary:
  finite-order Selberg--Delange/Tauberian expansion for zeta^z G
  standard fixed-field Dirichlet/Hecke zero-free regions and vertical growth
  polylog-uniform Gaussian angular Hecke zero-free estimate used for ell<=log^4 B
```

This makes clear which inference is proved in the repository and which is a declared standard external theorem input.

---

## 4. Consequence for Stage13

Sections 1--3 add no new arithmetic or archimedean constant.  They only expand steps already used in R03.  Therefore the theorem candidate remains

\[
\boxed{
N_q(B)
\sim
\frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\qquad q\in\{ab,ac,bc\},
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

The normalized directional vector is unchanged.

No claim about existence/nonexistence of a perfect cuboid, an effective convergence threshold, monotonicity, or publication-grade peer review is introduced.

---

## 5. Status

```text
STAGE13_12AG=COMPLETE_PROOF_EXPLICITNESS_SUPPLEMENT
COAREA_IQ_TO_INTERVAL_LENGTH=PROVED_EXPLICITLY
ANALYTIC_JQ_EQ_2IQ_OVER_PI=PROVED_WITH_FULL_JACOBIAN_CHAIN
INERT_UNIT_CHARACTER_SUM=PROVED_SYMBOLICALLY
INERT_UNIT_ACCEPTED_COUNT=(p+1)^2/2
SELBERG_DELANGE_HYPOTHESIS_CROSSWALK=RECORDED
R03_ARTIFACT_MUTATED=false
R03_GROK_VERDICT=CLOSED
R03_QWEN_VERDICT=CLOSED
STAGE13_THEOREM_CONSTANTS_CHANGED=false
STAGE13_COUNTING_CONVENTION_CHANGED=false
NEXT=FINAL_EXTERNAL_REVIEW_FREEZE_OR_NEW_R04_ONLY_IF_REQUESTED
```
