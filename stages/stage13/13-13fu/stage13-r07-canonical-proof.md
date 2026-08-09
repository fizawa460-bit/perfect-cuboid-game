# Stage13 — R07 canonical proof candidate

> STATUS: `STAGE13_13FU_R07_CANONICAL_PROOF_CANDIDATE`
>
> PURPOSE: single proof-facing synthesis of the Stage13 exactly-one directional asymptotic after the R06 zero-base external reviews and the R07 repairs `13-13fq` through `13-13ft`.
>
> PRECEDENCE: this file supersedes the R06 canonical proof for construction of the future immutable R07 review bundle. R03–R06 remain immutable historical artifacts.
>
> THEOREM_CHANGED: `false`.
>
> THEOREM_CONTRACT_REOPEN_REQUIRED: `false`.

---

## 0. Theorem and scope

Count primitive canonical triples

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,
\qquad d^2=a^2+b^2+c^2,\quad d\in\mathbf Z_{>0}.
\]

For `q in {ab,ac,bc}`, let `A_q(B)` count triples with `d<=B` for which face `q` has integral diagonal, allowing additional integral faces. For distinct `q,r`, let `O_{qr}(B)` count triples with both faces integral. Let `T(B)` count triples with all three faces integral. Let `N_q(B)` count triples with exactly one integral face, namely `q`.

On

\[
\mathcal R=\{(x,y,z)\in S^2:0<x<y<z\}
\]

define

\[
w_{ab}=\frac1{\sqrt{x^2+y^2}},\quad
w_{ac}=\frac1{\sqrt{x^2+z^2}},\quad
w_{bc}=\frac1{\sqrt{y^2+z^2}},
\qquad
I_q=\int_{\mathcal R}w_q\,d\omega.
\]

The Stage13 theorem candidate is

\[
\boxed{N_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3}
\]

and

\[
\boxed{N_1(B):=\sum_qN_q(B)\sim\frac{\kappa}{24\pi}B(\log B)^3}.
\]

Moreover

\[
\boxed{I_{ab}+I_{ac}+I_{bc}=\frac{\pi^2}{8}},
\qquad
\boxed{\frac{N_q(B)}{N_1(B)}\to\frac{8I_q}{\pi^2}}.
\]

No effective convergence rate is claimed. Finite data are not proof of convergence and are not positive convergence evidence in this theorem. No nonexistence assumption for perfect cuboids is used.

---

## 1. Exact combinatorics

For `{q,r,s}={ab,ac,bc}`,

\[
N_q=A_q-O_{qr}-O_{qs}+T,
\]

and

\[
N_1=\sum_qA_q-2\sum_{q<r}O_{qr}+3T.
\]

Thus it is enough to prove, for every face direction,

\[
A_q(B)\sim D_qB(\log B)^3,
\qquad
D_q=\frac{\kappa I_q}{3\pi^3},
\]

and for every distinct pair

\[
O_{qr}(B)=o(B(\log B)^3).
\]

Since `T(B)<=O_{qr}(B)` for every pair, the same bound then holds for `T(B)`.

---

## 2. Frozen Stage12 interface, exact factor two, and kappa

Stage12 uses

\[
1\le r<s,\quad(r,s)=1,
\qquad
P=hrs,\quad z=\frac{h(s^2-r^2)}2,\quad d=\frac{h(r^2+s^2)}2,
\]

with cutoff `d<=B`. Its primitive oriented distinguished-face record count is a frozen input:

\[
\boxed{C_{\rm prim}(B)\sim\frac{\kappa}{12\pi}B(\log B)^3}.
\]

The Euler product is

\[
\kappa=
\left(\frac\pi4\right)^3\left(\frac12\right)^3
\prod_{p\equiv3(4)}(1-p^{-2})^3
\prod_{q\equiv1(4)}
\frac{q^2+6q+1}{q^2-1}(1-q^{-1})^6.
\]

Its absolute convergence is visible locally. For inert primes,

\[
(1-p^{-2})^3=1-3p^{-2}+O(p^{-4}).
\]

For split primes, with `x=q^{-1}`,

\[
\frac{1+6x+x^2}{1-x^2}(1-x)^6=1-19x^2+O(x^3).
\]

Hence every normalized factor is `1+O(p^{-2})`.

### 2.1 The exact projection fiber

The factor two is an identity at the level of **Stage12 primitive oriented distinguished-face records**. It is not a claim that two canonically ordered cuboids represent one object.

Fix one canonical raw incidence counted by `A_q(B)`. Before canonical sorting, Stage12 has exactly the two ordered distinguished-face records

\[
(x,y),\qquad(y,x).
\]

The outer convention `r<s` fixes the outer Pythagorean orientation, the cutoff and gcd are unchanged by swapping the distinguished face legs, repeated-side cases do not contribute to `0<a<b<c`, and the same two-element fiber holds separately on both OE and EE parity branches. Therefore for every finite `B`,

\[
\boxed{C^{\rm proj}_{\rm prim,q}(B)=2A_q(B)},
\qquad
\boxed{C_{\rm prim}(B)=2\sum_qA_q(B)}.
\]

For a multi-face cuboid this remains an incidence identity: an exactly-two-face object contributes two canonical incidences and four Stage12 records; an exactly-three-face object contributes three incidences and six records.

---

## 3. Archimedean factor and the exact identity sum Iq

For face `ab`, write

\[
a^2+b^2=P^2,\qquad P^2+c^2=d^2.
\]

For

\[
F_1=a^2+b^2-P^2,\qquad F_2=P^2+c^2-d^2,
\]

we have

\[
\det\frac{\partial(F_1,F_2)}{\partial(P,d)}=4Pd.
\]

After radial scaling by `d`, the directional Gelfand–Leray factor is

\[
\frac dP=\frac1{P/d}=\frac1{\sqrt{x^2+y^2}}=w_{ab}.
\]

The other directions follow by coordinate permutation.

Let

\[
\mathcal O=\{(x,y,z)\in S^2:x,y,z>0\},
\qquad W=w_{ab}+w_{ac}+w_{bc}.
\]

The function `W` is invariant under all coordinate permutations. The positive octant is, up to equality walls of spherical measure zero, the disjoint union of the six order chambers. Hence

\[
\int_{\mathcal O}W\,d\omega=6(I_{ab}+I_{ac}+I_{bc}).
\]

For one pair use

\[
x=\sin\phi\cos\theta,\quad y=\sin\phi\sin\theta,\quad z=\cos\phi,
\quad 0<\phi,\theta<\frac\pi2.
\]

Then

\[
\sqrt{x^2+y^2}=\sin\phi,
\qquad d\omega=\sin\phi\,d\phi\,d\theta,
\]

so

\[
\int_{\mathcal O}w_{ab}\,d\omega
=\int_0^{\pi/2}\int_0^{\pi/2}d\phi\,d\theta
=\frac{\pi^2}{4}.
\]

The same value holds for `w_ac,w_bc` by coordinate permutation. Therefore

\[
6\sum_qI_q=3\frac{\pi^2}{4},
\]

and

\[
\boxed{\sum_qI_q=\frac{\pi^2}{8}}.
\]

This argument uses symmetry only for the **sum** `W`; it does not assert `I_ab=I_ac=I_bc`.

---

## 4. Zero Fourier kernel and real-angle notation

For a face `q={i,j}` and complementary coordinate `k`, use

\[
x_i=\sin\theta\cos\alpha,\quad
x_j=\sin\theta\sin\alpha,\quad
x_k=\cos\theta.
\]

Here `theta` is only the geometric polar angle. Then

\[
w_qd\omega=d\theta d\alpha.
\]

Put

\[
\psi=\frac\pi2-\theta.
\]

For each `psi`, let `ell_q(psi)` denote the admissible inner-angle length of the canonical chamber. Fubini gives

\[
I_q=\int\ell_q(\psi)d\psi.
\]

Write

\[
r=R\cos\phi,\qquad s=R\sin\phi,
\qquad \phi\in[\pi/4,\pi/2].
\]

Then

\[
\frac Pd=\sin(2\phi),
\qquad
\frac zd=-\cos(2\phi),
\qquad
\psi=2\phi-\frac\pi2.
\]

Define

\[
k_q(\phi)=\frac4\pi\ell_q(\psi),
\qquad
J_q=\int_{\pi/4}^{\pi/2}k_q(\phi)d\phi.
\]

Thus

\[
\boxed{J_q=\frac{2I_q}{\pi}},
\qquad
\boxed{\sum_qJ_q=\frac\pi4}.
\]

From this point the Gaussian arithmetic phase is denoted `vartheta`; it is never denoted `theta`.

---

## 5. Odd-prime coefficient system and the weighted Wiener correction

The OE/EE distinction is entirely 2-adic. On each branch separately, the odd-prime coefficient system is the same for `ab,ac,bc`; the face direction enters through the real chamber factor `J_q`. Thus the branch arithmetic constant is direction-independent.

For split `p≡1 (4)`, set

\[
x=p^{-s_h},\qquad y=p^{-s_r},\qquad z=p^{-s_s}.
\]

Let `vartheta` be the local angular phase. Define

\[
A_\vartheta(x)=\frac{1-x^2}{1-2\cos\vartheta\,x+x^2},
\qquad
B_\vartheta(y)=\frac{1+y}{1-2\cos\vartheta\,y+y^2}.
\]

The genuine mixed positive-height/base term is

\[
M_\vartheta(x,y)=\sum_{a,b\ge1}2\cos((a+b)\vartheta)x^ay^b.
\]

The primitive three-variable local factor is

\[
D_\vartheta
=1+a_\vartheta(x)+b_\vartheta(y)+b_\vartheta(z)
+M_\vartheta(x,y)+M_\vartheta(x,z),
\]

where `a=A-1` and `b=B-1`. Define

\[
C_\vartheta(x,y,z)=\frac{D_\vartheta(x,y,z)}{A_\vartheta(x)B_\vartheta(y)B_\vartheta(z)}.
\]

At the retained mode `ell>=1`, `C_{ell,p}` is this factor at the phase attached to `(ell,p)`.

For the weighted Wiener norm

\[
\|F\|_\rho=\sum|f_{i,j,k}|\rho^{i+j+k},
\qquad \rho=p^{-5/8},
\]

we have submultiplicativity and, for `p>=13`, `rho<1/4` because

\[
4^8=65536<13^5=371293.
\]

The phase-uniform coefficient estimates are

\[
\|a\|\le\frac83\rho,
\qquad
\|b\|\le\frac{44}{9}\rho,
\qquad
\|M\|\le\frac{32}{9}\rho^2,
\]

and

\[
\|A^{-1}\|\le\frac53,
\qquad
\|B^{-1}\|\le\frac{25}{12}.
\]

The pure-axis cancellation gives the exact mixed error identity

\[
E=(M_{xy}-ab_y)+(M_{xz}-ab_z)-b_yb_z-ab_yb_z.
\]

Therefore

\[
\|E\|\le\frac{17744}{243}\rho^2,
\]

and

\[
\|C_{\ell,p}-1\|_{5/8}
\le
\frac{3465625}{6561}p^{-5/4}
<529p^{-5/4}.
\]

The last inequality is exact, not floating point:

\[
\boxed{3465625<529\cdot6561=3470769}.
\]

For `p=5`, the explicit coefficientwise calculation gives

\[
\|C_{\ell,5}-1\|_{5/8}
\le\frac{10799919009}{25000000}<432,
\]

again by an exact integer inequality:

\[
\boxed{10799919009<432\cdot25000000=10800000000}.
\]

Since

\[
\sum_{p\equiv1(4)}p^{-5/4}<\infty,
\]

the global mixed correction is absolutely convergent in the weighted Wiener region, uniformly in the real phase and hence uniformly in every retained `ell`.

### 5.1 Uniform logarithmic moments

Write

\[
C_\ell(\mathbf s)=\sum_{u,v,w}\frac{c_\ell(u,v,w)}{u^{s_h}v^{s_r}w^{s_s}}.
\]

The weighted estimate gives one phase-uniform constant `K` such that

\[
\sup_{\ell\ge1}\sum_{u,v,w}
\frac{|c_\ell(u,v,w)|}{(uvw)^{5/8}}\le K.
\]

For fixed `m>=0`, put `X=log(uvw)`. Then

\[
\frac{(1+\log(uvw))^m}{uvw}
=
\frac1{(uvw)^{5/8}}(1+X)^me^{-3X/8}.
\]

The function `(1+X)^me^{-3X/8}` is bounded on `[0,infinity)`. Hence

\[
\boxed{
\sup_{\ell\ge1}
\sum_{u,v,w}
\frac{|c_\ell(u,v,w)|(1+\log(uvw))^m}{uvw}<\infty.
}
\]

Thus every mixed-logarithmic shift estimate used below is genuinely uniform in the retained harmonic index.

---

## 6. Fixed finite Gaussian/ray-class twists: R07 Gate A

The retained Fourier exponent is

\[
m=8\ell,\qquad\ell\ge1.
\]

Huang–Liu–Rudnick use

\[
\Xi_k(\mathfrak a)=\left(\frac\alpha{\bar\alpha}\right)^{2k}=e^{i4k\theta_{\mathfrak a}},
\]

so

\[
\boxed{k_{HLR}=2\ell},
\qquad
\boxed{\text{gamma shift}=4\ell}.
\]

Merikoski writes

\[
\xi_j(z)=\left(\frac z{|z|}\right)^j,
\]

therefore

\[
\boxed{\Xi_{2\ell}=\xi_{8\ell}}.
\]

Fix a finite inert-prime set `S` before the limit `B->infinity`. Choose one Gaussian modulus `u_S` encoding the finite residue predicates and fixed 2-adic branch. It depends on `S`, not on `B` and not on `ell`. Let

\[
\mathcal X_S^{Gau}=\widehat{(\mathbf Z[i]/u_S\mathbf Z[i])^\times}.
\]

For `omega in X_S^{Gau}`, define

\[
\Psi_{\ell,\omega}=\Xi_{2\ell}\omega=\xi_{8\ell}\omega.
\]

The finite-order character `omega` has trivial infinity type. Hence the product remains a Hecke/ray-class character with nonzero infinity type for every `ell>=1`. Its finite conductor belongs to a finite set depending only on fixed `S`. Primitive reduction changes an imprimitive member by finitely many Euler polynomials at the fixed modulus primes.

The primitive completed function has the form

\[
\Lambda(s,\Psi_{\ell,\omega})
=Q_\omega^{s/2}\pi^{-(s+4\ell)}
\Gamma(s+4\ell)L(s,\Psi_{\ell,\omega}),
\]

and satisfies the Hecke functional equation up to a unit-modulus root number. Since the infinity type is nonzero, the primitive Hecke `L`-function is entire; therefore every fixed finite twist is holomorphic at `s=1`.

On a fixed strip, right-boundary absolute convergence, the functional equation, Stirling, and Phragmen–Lindelof give common constants over the finite twist family:

\[
\boxed{
|L(\sigma+it,\Psi_{\ell,\omega})|
\ll_S(2+|t|+\ell)^{C_S}.
}
\]

A Riesz order greater than the common vertical-growth exponent permits the contour shift. Finite differencing and the positive coefficient majorant recover the sharp sum with a slightly weakened but positive saving. Thus for fixed `S` there are

\[
\delta_S>0,\qquad C_{H,S},D_{H,S}\ge0
\]

such that retained nonzero harmonics satisfy a bound of the form

\[
S_{\ell,S}(X)
\ll_S X^{1-\delta_S}(1+\ell)^{C_{H,S}}
(\log(2X))^{D_{H,S}}.
\]

No zero-free region, `1/L`, `L'/L`, or theorem uniform in a modulus growing with `B` is used.

---

## 7. Vaaler, angular endpoints, and the physical cutoff

Vaaler's finite approximation is used **only** for the one-dimensional inner-angle chamber interval indicator. It is not used to approximate the physical curved height condition.

Take degree

\[
L=\lfloor(\log B)^4\rfloor.
\]

The interval majorant/minorant has zero-mode excess `1/(L+1)` and nonzero coefficients bounded by the standard Vaaler coefficient majorant.

Canonical equality-wall endpoints correspond to repeated-side/equality configurations excluded by the strict discrete condition `0<a<b<c`. This is an exact statement at the counted-object level, not an appeal to continuous measure zero. By contrast, the physical endpoint `d=B` is part of the count because the cutoff is `d<=B`; it is retained exactly. The two endpoint issues are separate.

The physical cutoff is

\[
F(h,r,s):=h(r^2+s^2)\le2B.
\]

It is handled by the multiplicative box construction of the next section.

---

## 8. Curved-region transfer: R07 Gate C

Put

\[
\Lambda=\log B,
\qquad
H_0=U=e^{\Lambda^{1/4}},
\qquad
\eta=\Lambda^{-8},
\qquad
\varepsilon=\frac1{16},
\qquad
N=64.
\]

Remove the positive-majorant wings

\[
h<H_0,
\qquad
\min(r,s)<U.
\]

They contribute respectively

\[
O(B\Lambda^{9/4}),
\qquad
O(B\Lambda^{5/2}),
\]

both `o(B Lambda^3)`.

### 8.1 Multiplicative boxes and uniformity

Partition each coordinate into intervals

\[
[e^{j\eta},e^{(j+1)\eta}).
\]

Every relevant coordinate is at most `2B`. Thus one coordinate needs

\[
O\!\left(\frac{\log(2B)}\eta\right)=O(\Lambda^9)
\]

intervals and the crude three-coordinate family has

\[
\boxed{N_{box}=O(\Lambda^{27})}.
\]

On any core box meeting the physical region,

\[
H(R^2+S^2)\ll B
\]

and hence, because `2RS<=R^2+S^2`,

\[
HRS\ll B.
\]

The finite-order endpoint remainder of each zero-mode rectangle is uniformly

\[
O(B\Lambda^{-62}).
\]

Summing this crude bound over all boxes gives

\[
\boxed{O(B\Lambda^{-35})}.
\]

The rectangle power tails have, after all boxes, the form

\[
B\Lambda^{C_{rect}+27}
\exp\!\left(-\frac3{16}\Lambda^{1/4}\right),
\]

which is smaller than `B Lambda^{-A}` for every fixed `A`.

### 8.2 Curved boundary shell

Within one multiplicative box, `h` changes by at most `e^eta` and `r^2+s^2` by at most `e^{2eta}`. Thus any box meeting `F=2B` lies inside

\[
2Be^{-3\eta}\le F(h,r,s)\le2Be^{3\eta}.
\]

The main cumulative measure has degree one in `B` and logarithmic degree at most three. A mean-value estimate in the logarithmic radial variable therefore gives shell main mass

\[
O(\eta B\Lambda^3)=\boxed{O(B\Lambda^{-5})}.
\]

The analytic rectangle remainders of boundary boxes are already contained in the global remainder sums above; they are not hidden inside the shell estimate.

### 8.3 Interior mesh variation

After removing boundary-intersecting boxes, the physical indicator is constant on every remaining box. In logarithmic coordinates the main density is piecewise `C^1`, and its total first-variation majorant is `O(B Lambda^3)`. The mesh width is `eta`, so the full Riemann-sum variation is

\[
\boxed{O(\eta B\Lambda^3)=O(B\Lambda^{-5})}.
\]

No additional factor `N_box` appears: the estimate is total variation times mesh width, already summed over cells. Multiplying again by the number of cells would double-count the Riemann-sum argument.

### 8.4 Mixed logarithmic shifts

A nonconstant correction shift satisfies, for fixed integer `j`,

\[
(\log(X/n))^j-(\log X)^j
=O((1+\log n)\Lambda^{j-1}).
\]

The uniform logarithmic moments proved in §5.1 therefore give the global bound

\[
\boxed{O(B\Lambda^2)}.
\]

### 8.5 Retained harmonics

One retained mode costs

\[
B\Lambda^{D_H+2}(1+\ell)^{C_H}
\exp(-\delta_H\Lambda^{1/4}).
\]

Since `ell<=L=Lambda^4`,

\[
\sum_{\ell\le L}(1+\ell)^{C_H}
=O(\Lambda^{4C_H+4}).
\]

Thus

\[
\boxed{
\mathcal E_{harm,core}
\ll B\Lambda^{4C_H+D_H+6}
\exp(-\delta_H\Lambda^{1/4})
=o_A(B\Lambda^{-A})
}
\]

for every fixed `A>0`. The exponent ledger is explicitly

\[
\boxed{(4C_H+4)+D_H+2=4C_H+D_H+6}.
\]

The Vaaler zero-mode excess is `O(1/L)` times the positive Stage12 total majorant, hence `O(B Lambda^{-1})`, also negligible.

Consequently the raw one-face count has a common arithmetic constant `Theta`, independent of `q`, with

\[
A_q(B)\sim\Theta J_qB\Lambda^3.
\]

---

## 9. Calibration of the common arithmetic constant

Direction-independence is established branchwise before using Stage12. Summing the OE/EE constants gives one `Theta`. Now use

\[
C_{prim}=2\sum_qA_q,
\qquad
\sum_qJ_q=\frac\pi4,
\]

and the frozen Stage12 asymptotic. Then

\[
2\Theta\frac\pi4=\frac\kappa{12\pi},
\]

so

\[
\boxed{\Theta=\frac\kappa{6\pi^2}}.
\]

Because `J_q=2I_q/pi`,

\[
\boxed{
A_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3.
}
\]

This calibration is not circular: odd-prime and 2-adic branchwise commonness first proves that `Theta` does not depend on `q`; only then is the total Stage12 theorem used to determine its value.

---

## 10. Concrete inert local model: R07 Gate B

Fix an inert odd prime

\[
p\equiv3\pmod4.
\]

For a tagged distinguished face write

\[
x^2+y^2=P^2,
\qquad
P^2+z^2=d^2,
\]

with

\[
P=hrs,
\qquad
z=\frac{h(s^2-r^2)}2,
\qquad
d=\frac{h(r^2+s^2)}2.
\]

If the second integral face shares the tagged edge `x`, then for some integer `w`,

\[
x^2+z^2=w^2.
\]

Hence every true global pair overlap passes the local predicate

\[
\boxed{W_p(x,z)=1_{\{x^2+z^2\in QR_0(\mathbf F_p)\}}=1}.
\]

The other tag is obtained by `x<->y`.

### 10.1 Complete valuation strata

Put

\[
a=v_p(h),\qquad b=v_p(r),\qquad c=v_p(s).
\]

Inertness and global primitivity force `a=0`. Since `(r,s)=1`, exactly one of `b,c` can be positive. Therefore the complete local strata are

```text
U   : (0,0,0),
R_b : (0,b,0), b>=1,
S_c : (0,0,c), c>=1.
```

The unrestricted zero-mode local series is

\[
L_{p,0}=1+\sum_{b\ge1}p^{-b}+\sum_{c\ge1}p^{-c}
=\frac{p+1}{p-1}.
\]

On `R_b` or `S_c`, we have `p|P`; inertness in `x^2+y^2=P^2` forces `p|x,y`, while primitivity leaves `z` a unit. Thus

\[
x^2+z^2\equiv z^2\pmod p,
\]

so every positive-valuation state passes automatically.

### 10.2 Unit stratum

On `U`, divide by the unit `P` and set

\[
X=x/P,\quad Y=y/P,\quad Z=z/P,\quad\Delta=d/P.
\]

The actual constrained finite set is

\[
\boxed{
\Omega_{p,U}=
\{(X,Y,Z,\Delta)\in\mathbf F_p^4:
X^2+Y^2=1,\ \Delta^2-Z^2=1\}.
}
\]

The accepted subset is

\[
\Omega^W_{p,U}
=\{\omega\in\Omega_{p,U}:X^2+Z^2\in QR_0(\mathbf F_p)\}.
\]

The two conics have `p+1` and `p-1` points, so

\[
|\Omega_{p,U}|=p^2-1.
\]

Let `chi` be the quadratic character extended by `chi(0)=0`. The symbolic character-sum calculation gives

\[
S=S_0+S_1+S_2+S_3
=0+(p-1)+(p+1)-2
=2(p-1).
\]

Because `X^2+Z^2=0` has exactly four states on the constrained product when `chi(-1)=-1`,

\[
|\Omega^W_{p,U}|
=\frac{(p^2-1)+2(p-1)+4}{2}
=\boxed{\frac{(p+1)^2}{2}}.
\]

Hence

\[
\alpha_p=\frac{p+1}{2(p-1)}.
\]

Adding the automatically accepted positive-valuation mass yields

\[
L^W_{p,0}=\alpha_p+\frac2{p-1}
=\frac{p+5}{2(p-1)},
\]

and therefore

\[
\boxed{\lambda_p=\frac{p+5}{2(p+1)}}.
\]

In particular

\[
\boxed{\lambda_3=1},
\qquad
\boxed{\lambda_p\le\frac34\quad(p\ge7,\ p\equiv3\bmod4)}.
\]

The unit state and its measure are symmetric under `X<->Y`, so the same `lambda_p` applies to either tag.

---

## 11. Fixed-S Fourier quotient and the principal pole sector

Fix a finite inert set `S` before taking `B->infinity`. For each `p in S`, choose a finite abelian ambient encoding `G_p` that records the residue coordinates used by the coefficient system, and map the actual admissible local states into it by `iota_p`.

Define the finite physical residue function by the actual local test, zero-extended off the admissible image. Fourier inversion gives a finite expansion in `widehat G_p`; CRT tensors these expansions over fixed `S`.

### 11.1 Alias quotient and well-definedness

Let

\[
N_p=\{\chi\in\widehat G_p:
\chi(\iota_p(\omega))=1
\text{ for every actual admissible coefficient state }\omega\}.
\]

Two ambient characters are identified exactly when they have the same restriction to every actual coefficient state. Representatives differing by `N_p` therefore give the same twisted coefficient system term by term. Any analytic pole-slot character induced by that coefficient system is consequently representative-independent.

This is the required compatibility between the effective-character quotient and pole classification; no group structure is assumed for `Omega_{p,U}` itself.

### 11.2 Five raw pole slots

At zero mode the unbounded principal poles arise from

\[
\boxed{\mathscr P=\{H,R_1,R_2,S_1,S_2\}},
\]

corresponding to one scale zeta factor and two copies for each base variable. Fixed `L(s,chi_4)`, 2-adic factors and the mixed Wiener correction are holomorphic at `s=1`.

Each effective character class induces five slot characters. The principal sector is the kernel of this reduced pole-signature map: all five slot characters are principal.

Let `Res_S(F)` denote the coefficient of the full raw principal polar term after inserting a fixed residue function `F`. It is linear in `F`. Every class outside the principal kernel has at least one nonprincipal slot, and that zeta pole is replaced by a fixed-conductor Dirichlet or Gaussian/ray-class Hecke factor holomorphic at `s=1`.

A finite sum of functions each having pole order at most three cannot create a pole of order four absent from every summand. Cancellation can lower pole order; it cannot manufacture a missing higher Laurent coefficient. Hence the complete nonprincipal fixed-S contribution is

\[
o_S(B(\log B)^3).
\]

### 11.3 Principal multiplier in the same physical model

Evaluate the same principal-residue functional directly on the physical local state measure. At each `p in S`, the accepted/unrestricted ratio is exactly `lambda_p`; CRT tensors the fixed local insertions. Hence

\[
\boxed{
\frac{Res_S(W_S)}{Res_S(1)}
=\prod_{p\in S}\lambda_p.
}
\]

Thus the entire principal sector, including harmless aliases that are principal on the effective coefficient system, has exactly the multiplier `prod lambda_p`.

---

## 12. Tagged shared-edge injection and fixed-S compatibility

For every raw `q` incidence, tag one of its two distinguished-face legs. Therefore the ambient tagged count satisfies the exact finite identity

\[
\boxed{|\mathcal T_q(B)|=2A_q(B)}.
\]

If two distinct integral faces `q,r` occur, they share exactly one cuboid edge. Map the overlap object to the `q`-incidence tagged by that unique shared edge. The shared edge is literally one of the two legs of the `q` face, so this is a well-defined tagged incidence. The original canonical cuboid and face pair recover the image source, so the map is injective.

If the second face is globally integral, §10 shows that the shared tagged edge passes every local `W_p` for every `p in S`. Tagging changes no underlying edge, residue coordinate, valuation or parity branch. Therefore the injection is compatible with the fixed-S accepted tagged set:

\[
\boxed{O_{qr}(B)\le A^{tag}_{q,S}(B)}.
\]

The tagged asymptotic is

\[
A^{tag}_{q,S}(B)
=2D_q\left(\prod_{p\in S}\lambda_p\right)
B(\log B)^3+o_S(B(\log B)^3).
\]

---

## 13. Pair-overlap squeeze in epsilon form

Choose distinct inert primes `p_i>=7` and set

\[
S_k=\{p_1,\dots,p_k\}.
\]

For fixed `k`,

\[
\limsup_{B\to\infty}
\frac{O_{qr}(B)}{B(\log B)^3}
\le
2D_q\prod_{p\in S_k}\lambda_p
\le2D_q\left(\frac34\right)^k.
\]

To spell out the little-`o` quantifiers, let `epsilon>0`. Choose **one fixed** `k` such that

\[
2D_q\left(\frac34\right)^k<\frac\epsilon2.
\]

Hold this finite set `S_k` fixed. By the fixed-S asymptotic there is `B_0(k,epsilon)` such that for every `B>=B_0`, the normalized fixed-S remainder has magnitude below `epsilon/2`. Hence

\[
\frac{O_{qr}(B)}{B(\log B)^3}<\epsilon
\]

for all sufficiently large `B`. Therefore

\[
\boxed{O_{qr}(B)=o(B(\log B)^3)}.
\]

There is no exchange of limits and no modulus growing with `B`. The quantifier order is permanently

```text
choose epsilon
-> choose fixed k
-> fix S_k
-> B -> infinity.
```

Since `T(B)<=O_{qr}(B)`, also

\[
\boxed{T(B)=o(B(\log B)^3)}.
\]

---

## 14. Exactly-one conclusion

Insert the pair/triple overlap estimates into the exact combinatorial identities of §1. Then

\[
\boxed{
N_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3.
}
\]

Summing over `q` and using

\[
\sum_qI_q=\frac{\pi^2}{8}
\]

gives

\[
\boxed{
N_1(B)\sim\frac\kappa{24\pi}B(\log B)^3.
}
\]

Consequently

\[
\boxed{
\frac{N_q(B)}{N_1(B)}\to\frac{8I_q}{\pi^2}.
}
\]

---

## 15. R07 quantitative ledger

With `Lambda=log B`, the proof uses the following fixed bookkeeping:

```text
Stage13 Fourier exponent                 = 8*ell
HLR Xi index                             = 2*ell
Merikoski angular index                  = 8*ell
Xi_{2ell}                                = xi_{8ell}
Hecke gamma shift                        = 4*ell
retained ell                             >= 1
H0=U                                     = exp(Lambda^(1/4))
eta                                      = Lambda^(-8)
rectangle epsilon                        = 1/16
finite Perron order                      = 64
Vaaler degree                            = floor(Lambda^4)
mesh intervals per coordinate            = O(log(2B)/eta)=O(Lambda^9)
box count                                = O(Lambda^27)
per-box finite remainder                 = O(B Lambda^(-62))
all-box finite remainder                 = O(B Lambda^(-35))
curved-boundary main mass                = O(B Lambda^(-5))
interior mesh error                      = O(B Lambda^(-5))
mixed logarithmic shifts                 = O(B Lambda^2)
retained harmonic exponent               = 4*C_H+D_H+6
split-prime Wiener exact constant        = 3465625/6561 < 529
exceptional p=5 Wiener bound             = 10799919009/25000000 < 432
inert local multiplier                   = (p+5)/(2(p+1))
lambda_3                                 = 1
contraction starts                       = inert p>=7
Stage12 projection fiber                 = 2 oriented face-leg records
```

---

## 16. External theorem and frozen-input boundary

The internal Stage13 proof uses the following declared external/frozen inputs rather than silently treating them as proved here:

1. **Frozen Stage12 R09 theorem:** the primitive oriented distinguished-face total asymptotic `C_prim(B)~kappa/(12*pi) B(log B)^3`, together with its exact counting convention.
2. **Classical Hecke theory over Q(i):** analytic continuation and functional equation for primitive nontrivial Hecke/ray-class characters. The exact angular normalization is fixed by the HLR/Merikoski crosswalk in §6.
3. **Classical Dirichlet L-function theory:** fixed finite rational residue twists are holomorphic at one when nonprincipal.
4. **Finite-order Perron/Selberg–Delange/Tauberian machinery:** used on fixed Euler products satisfying the explicit local analyticity and Wiener hypotheses recorded above.
5. **Vaaler finite interval approximation:** used only on the one-dimensional angular chamber interval; never on the physical curved height cutoff.

R07 does not require a zero-free region for its retained Hecke factors and does not require uniformity in any modulus growing with `B`.

---

## 17. R07 repair closure and review policy

The R06 zero-base reviews generated four R07 obligations. They are integrated here as follows:

```text
R07 Gate A: fixed finite Hecke/ray-class twist contract       COMPLETE (§6)
R07 Gate B: concrete fixed-S residue/pole model               COMPLETE (§§10-12)
R07 Gate C: self-contained curved-region transfer             COMPLETE (§§7-8)
R07 Gate D: exact arithmetic and quantifier hardening         COMPLETE (§§2.1,5.1,13)
```

The following challenged but correct points are not reopened:

```text
sum I_q = pi^2/8 is analytic and valid
finite sums cannot restore an absent higher-order pole
tagged shared-edge injection is valid at fixed S
Stage12 factor two is a fiber of oriented records, not canonical cuboids
```

R06 remains immutable. Its review votes are historical evidence only and do not count as R07 reviews. After this synthesis is merged, the next stage must build a new immutable R07 review artifact from a fixed merged source snapshot and reset the R07 external-review ledger to zero.

```text
R07_CANONICAL_PROOF_SINGLE_ENTRYPOINT=true
R07_GATES_A_B_C_D_COMPLETE=true
R07_REPAIR_BLOCKERS_OPEN=0
R07_HARDENING_OBLIGATIONS_OPEN=0
R07_BUNDLE_CREATED=false
R07_FRESH_EXTERNAL_REVIEW_REQUIRED=true
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
PROMOTE_TO_13_13G=false
```
