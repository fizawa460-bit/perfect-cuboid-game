# Stage13-12af — authoritative R03 current proof

> REVIEW TARGET: `STAGE13-FINAL-SELF-CONTAINED-20260809-R03`
>
> STATUS: `PENDING_EXTERNAL_R03`
>
> PRIOR R02 VERDICTS: Grok `OPEN`, Claude `REPAIRABLE`, Qwen `REPAIRABLE`
>
> SCOPE: Stage13 only, with Stage12 R09 accepted as a frozen prior theorem-level input

This file is the first source a reviewer should read in R03.  It replaces the
R02 proof map as the authoritative proof ordering after the quantitative
repairs Stage13-12ad and Stage13-12ae.

The precedence is

```text
13-12af/current-proof.md
-> 13-12ad/result.md
-> 13-12ae/result.md
-> 13-12aa/result.md
-> 13-12ab/result.md
-> 13-12ac/current-proof.md
-> historical main.md and audit assets
```

The old Stage13-7jb raw direction-neutrality proof and the old Stage13-7jf
fixed-prime overlap proof remain superseded.

Internal PASS/COMPLETE flags, CI outcomes and Git hashes are not mathematical
evidence.  Previous R01/R02 verdicts are not binding on the R03 reviewer.

---

## 1. Definitions and exact combinatorial identities

Let

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,
\qquad D^2=a^2+b^2+c^2
\]

with `D` integral.  For `q in {ab,ac,bc}`, let `A_q(B)` be the primitive
canonical raw count with the `q` face diagonal integral and `D<=B`.

Let `O_{qr}(B)` be the primitive canonical count with both face diagonals `q`
and `r` integral, and let `T(B)` be the triple overlap.

Then exactly

\[
N_q(B)=A_q(B)-O_{qr}(B)-O_{qs}(B)+T(B)
\]

and

\[
N_1(B)=\sum_q A_q(B)-2\sum_{q<r}O_{qr}(B)+3T(B).
\]

The oriented/projected Stage12-facing count has the exact finite bridge

\[
C^{\rm proj}_{\rm prim,q}(B)=2A_q(B),
\qquad
C_{\rm prim}(B)=2\sum_q A_q(B).
\]

The factor `2` is a finite representation/projection multiplicity and is not
an asymptotic heuristic.

---

## 2. Canonical chamber and Gelfand--Leray weights

On the normalized sphere write

\[
\mathcal R=\{(x,y,z)\in S^2:0<x<y<z\}.
\]

For the `ab` distinguished face the equations

\[
a^2+b^2=p^2,
\qquad
p^2+c^2=d^2
\]

have

\[
\det \frac{\partial(F_1,F_2)}{\partial(p,d)}=4pd.
\]

After radial normalization the directional real-density weights on the chamber
are

\[
w_{ab}=\frac1{\sqrt{x^2+y^2}},\qquad
w_{ac}=\frac1{\sqrt{x^2+z^2}},\qquad
w_{bc}=\frac1{\sqrt{y^2+z^2}}.
\]

Hence pointwise on `R`,

\[
w_{ab}>w_{ac}>w_{bc}.
\]

Define

\[
I_q=\int_{\mathcal R}w_q\,d\omega.
\]

The chamber identity is

\[
I_{ab}+I_{ac}+I_{bc}=\frac{\pi^2}{8}.
\]

The locked numerical values are

```text
I_ab = 0.659705248705705
I_ac = 0.3026997526726076
I_bc = 0.2712955487578571
```

and only the exact integral definitions, not these decimal approximations, are
used in the theorem.

---

## 3. Analytic proof of the bridge `J_q = 2 I_q / pi`

R02 relied too heavily on a numerical bridge check.  R03 records the exact
change of variables.

In the outer Pythagorean parameterization, use the angle

\[
\phi\in[\pi/4,\pi/2]
\]

for the coprime pair `(r,s)`.  The physical outer angle `psi` between the face
hypotenuse and the third edge satisfies

\[
\psi=2\phi-\frac\pi2,
\qquad d\psi=2\,d\phi.
\]

For a fixed outer angle `psi`, let `ell_q(psi)` be the unnormalized length of
the admissible inner face-angle interval producing canonical category `q`.
The Stage13-3b Gelfand--Leray chamber integral is precisely

\[
I_q=\int \ell_q(\psi)\,d\psi.
\]

The fixed-shell zero Fourier kernel used by Stage13-7j/12aa is the same interval
length normalized by the total inner face-angle length `pi/4`:

\[
k_q(\phi)=\frac{\ell_q(\psi)}{\pi/4}=\frac4\pi\ell_q(\psi).
\]

Therefore

\[
\begin{aligned}
J_q
&:=\int_{\pi/4}^{\pi/2} k_q(\phi)\,d\phi\\
&=\int \frac4\pi\ell_q(\psi)\frac{d\psi}{2}\\
&=\frac2\pi I_q.
\end{aligned}
\]

Thus

\[
\boxed{J_q=\frac{2I_q}{\pi}}
\]

analytically, and

\[
\sum_qJ_q=\frac2\pi\frac{\pi^2}{8}=\frac\pi4.
\]

The numerical Simpson/adaptive-quadrature comparison in Stage13-7j is only a
validator of this exact change of variables.

---

## 4. Non-circular raw `j=0` common-factor theorem

Stage13-12aa removes the R01 circularity.  It does **not** define the category
constants from the desired chamber proportions.

Using the primitive outer coordinates

\[
P=hrs,
\qquad
z=\frac{h(s^2-r^2)}2,
\qquad
d=\frac{h(r^2+s^2)}2,
\qquad(r,s)=1,
\]

it derives the raw `j=0` local coefficient system from p-adic valuations and
Gaussian representation multiplicities, then factors the three-variable
Dirichlet series into pure axes and a mixed correction.

Before any Stage12 total calibration, the desired theorem shape is

\[
\boxed{
A_q(B)\sim \Theta J_q B(\log B)^3
}
\]

with a single unknown arithmetic constant `Theta` common to the three
categories.

The commonness of `Theta` is carried by the arithmetic coefficient system;
the category label enters only through the real zero-mode kernel `J_q`.

---

## 5. Quantitative mixed-correction closure — Stage13-12ad

R02 correctly objected that the original 12aa statement of weighted-Wiener
uniformity and curved transfer was too compressed.

Stage13-12ad fixes

\[
\delta=\frac18,\qquad \sigma=\frac58,
\qquad \rho=p^{-5/8}
\]

and proves coefficientwise for every split prime `p>=13` and every angular
phase

\[
\boxed{
\|C_{\ell,p}-1\|_{5/8}\le529p^{-5/4}.
}
\]

The smaller split prime `p=5` is one finite Euler factor.  Since

\[
\sum_{p\equiv1(4)}p^{-5/4}<\infty,
\]

the mixed correction is globally weighted-`l1` uniformly over all retained
harmonics.

Moreover for every fixed logarithmic degree `m`,

\[
\sum_{u,v,w}
\frac{|c_\ell(u,v,w)|(1+\log(uvw))^m}{uvw}<\infty
\]

uniformly in the retained harmonic range.  This is the precise statement
needed for the convolution-induced shifts `log R -> log R-log v`, etc.

### 5.1 Why anisotropic convolution does not alter the leading category factor

For a fixed correction term `(u,v,w)`, substituting

\[
h=H/u,\qquad r=R/v,\qquad s=S/w
\]

changes the physical inequality to an anisotropically scaled homogeneous
region.  The proof does **not** assert that the set is literally unchanged.
Instead it applies the rectangle asymptotic before summing the correction.
The zero-mode rectangle main is a polynomial in the three logarithms whose
top homogeneous term has degree three.  Replacing each log by

\[
\log H-\log u,\quad \log R-\log v,\quad \log S-\log w
\]

leaves the degree-three coefficient unchanged; every term containing at least
one `log u`, `log v` or `log w` has logarithmic degree at most two in `B`.
The logarithmic moment bound above makes the sum of all such lower-degree terms
absolutely convergent.  Consequently the correction contributes to the top
coefficient only through

\[
\sum_{u,v,w}\frac{c_0(u,v,w)}{uvw}=C_0(1,1,1),
\]

a direction-independent arithmetic scalar.  The category geometry is still
entirely in the zero-mode angular kernel `J_q`.

This explicitly answers Qwen R02 MAJOR-2.

---

## 6. Quantitative curved-region and harmonic remainder

Stage13-12ad fixes

```text
H0 = U = exp((log B)^(1/4))
eta = (log B)^(-8)
L = (log B)^4
finite-order remainder A = 48
```

and proves the following error ledger:

```text
small height                 O(B (log B)^(9/4))
small coordinate             O(B (log B)^(5/2))
mixed logarithmic shifts     O(B (log B)^2)
rectangle power tails        B(log B)^C exp(-c(log B)^(1/4))
curved boundary / mesh       O(B (log B)^(-5))
Vaaler excess                O(B (log B)^(-1))
all retained harmonics core  O(B (log B)^(-6))
```

Every line is `o(B(log B)^3)`.

The Gaussian angular character has frequency `k=8 ell`.  The standard
fixed-field zero-free input depends on

\[
\log((2+|t|)(2+|k|)).
\]

With `ell<=L=(log B)^4`, the conductor dependence is polylogarithmic.  The
nonzero angular characters have no exceptional real zero of the principal
zero-frequency type.  Taking the finite logarithmic order `A=48` absorbs the
`L=(log B)^4` harmonic sum and leaves the displayed `O(B(log B)^-6)` bound.

### 6.1 OE/EE parity branches

The OE branch has `r,s` odd and `h` odd; the EE branch has opposite parity in
`r,s` and the locked `2`-adic valuation of `h`.  These are finite 2-adic radial
variants of the same odd-prime coefficient system.  On each branch the
physical inequality remains

\[
h(r^2+s^2)\le2B
\]

up to the already fixed finite normalization of the 2-adic parameterization.
The rectangle estimates and the curved boundary decomposition are performed
branchwise; the finite 2-adic constants then add to the same direction-neutral
arithmetic `Theta`.  No odd-prime directional factor is introduced by the
OE/EE split.

This restates the historical parity input at the point where R03 uses it,
rather than leaving it as an unexplained reference.

---

## 7. Limited and non-circular use of Stage12 total mass

Stage12 R09 is a frozen prior theorem-level input.  It is used twice, for two
different purposes.

First, after Sections 4--6 have already proved the common form

\[
A_q(B)\sim\Theta J_qB(\log B)^3,
\]

the exact projection identity gives

\[
C_{\rm prim}(B)=2\sum_qA_q(B)
\sim2\Theta\left(\sum_qJ_q\right)B(\log B)^3
=\Theta\frac\pi2B(\log B)^3.
\]

The frozen Stage12 total theorem is

\[
C_{\rm prim}(B)\sim\frac{\kappa}{12\pi}B(\log B)^3.
\]

Hence only now

\[
\Theta\frac\pi2=\frac{\kappa}{12\pi},
\qquad
\boxed{\Theta=\frac{\kappa}{6\pi^2}}.
\]

Therefore

\[
\boxed{
A_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3.
}
\]

Second, Stage12's total upper scale may be used as a positive majorant for the
constant-term Vaaler bracketing excess.  This use controls an error only; it is
not used to establish commonness of `Theta` or category proportions.  Thus it
does not reintroduce the R01 circularity.

This explicitly answers Qwen R02 MINOR-2.

---

## 8. Exact inert-prime local state — Stage13-12ae

For an inert odd prime

\[
p\equiv3\pmod4
\]

write

\[
a=v_p(h),\qquad b=v_p(r),\qquad c=v_p(s).
\]

Primitivity forces `a=0`: if `p|h`, then `p|P,z`, and inertness in
`x^2+y^2=P^2` forces `p|x,y`, contradicting `gcd(x,y,z)=1`.

Also `(r,s)=1` gives `min(b,c)=0`.  Thus the complete valuation table is

```text
U    : (0,0,0)
R_b  : (0,b,0), b>=1
S_c  : (0,0,c), c>=1
```

with no omitted primitive state.

The unrestricted zero-mode local series is therefore exactly

\[
L_{p,0}(Y,Z)
=1+\sum_{b\ge1}Y^b+\sum_{c\ge1}Z^c
=\frac{1-YZ}{(1-Y)(1-Z)}.
\]

At `Y=Z=1/p`,

\[
L_{p,0}(1,1,1)=\frac{p+1}{p-1}
\]

and the entire positive-valuation mass is

\[
T_p^+=\frac{2}{p-1}.
\]

Hence

\[
\boxed{
\frac{T_p^+}{L_{p,0}(1,1,1)}
=\frac{2}{p+1}\le\frac2p
}
\]

with the explicit absolute constant

\[
\boxed{C_0=2}.
\]

---

## 9. Exact unit-state acceptance and local multiplier

On the unit state normalize by `P`:

\[
X=x/P,\quad Y=y/P,\quad Z=z/P,\quad \Delta=d/P.
\]

Then

\[
X^2+Y^2=1,
\qquad
\Delta^2-Z^2=1.
\]

For inert `p`, the first set has `p+1` points and is the norm-one subgroup of
`F_{p^2}^*`; the second has `p-1` points and is parameterized bijectively by

\[
u=s/r\in\mathbf F_p^*,
\quad
Z=\frac{u-u^{-1}}2,
\quad
\Delta=\frac{u+u^{-1}}2.
\]

The second-face necessary condition is

\[
X^2+Z^2\in QR_0(\mathbf F_p).
\]

The exact finite-field character sum gives accepted unit states

\[
\frac{(p+1)^2}{2}
\]

out of `p^2-1`, hence

\[
\alpha_p=\frac{p+1}{2(p-1)}.
\]

All positive valuation states `R_b,S_c` pass automatically because `p|P`
forces `x=y=0 mod p` while `z` is a unit.

Therefore

\[
L^W_{p,0}(1,1,1)
=\alpha_p+\frac2{p-1}
=\frac{p+5}{2(p-1)}
\]

and the exact constrained multiplier is

\[
\boxed{
\lambda_p
=\frac{p+5}{2(p+1)}
=\frac12+\frac{2}{p+1}.
}
\]

Thus

\[
\lambda_7=\frac34,
\qquad
\lambda_p<\frac34\quad(p>7,\ p\equiv3\pmod4).
\]

---

## 10. Why finite residue refinement produces the leading local density

The fixed-prime transfer is performed with `p` fixed before `B->infinity`.
The unit circle is a finite norm-one group of size `p+1`; the outer hyperbola
is a finite multiplicative group parameterized by `u in F_p^*` of size `p-1`.
Indicators of their fixed residue classes expand in the finite character bases
of these groups.  Rational residue variables use Dirichlet characters; the
Gaussian representation variable uses fixed-conductor Gaussian/ray-class
characters.

The principal character tuple reproduces the untwisted zero-mode pole and
weights the finite admissible states by the local counting density above.
Every nonprincipal fixed character tuple removes at least one principal pole
and is lower order at the same fixed-conductor Selberg--Delange/Hecke theorem
boundary used in Stage13-12ad.

For a fixed finite set `S` of primes, CRT tensors the finite state spaces and
the principal local multipliers multiply.  No modulus is allowed to grow with
`B`.

The OE/EE distinction is purely 2-adic and hence independent of every odd inert
prime used here.

---

## 11. Pair and triple overlap lower order

Every genuine second integral face satisfies the local necessary condition
`W_p=1` at each chosen inert prime.  The complete state table in Sections 8--10
therefore injects pair overlaps into the corresponding constrained tagged
population.

Using both possible selected-leg tags gives only the safe upper multiplicity

\[
O_{qr}(B)
\le A^{\rm tagged\ union}_{q,S}(B)
\le A^{(1)}_{q,S}(B)+A^{(2)}_{q,S}(B).
\]

For fixed

\[
S_k=\{p_1,\ldots,p_k\},\qquad p_i\ge7,
\]

take `B->infinity` while `S_k` is fixed.  Then

\[
\limsup_{B\to\infty}
\frac{O_{qr}(B)}{B(\log B)^3}
\le
2D_q\prod_{i=1}^k\lambda_{p_i}
\le2D_q\left(\frac34\right)^k.
\]

Only afterwards let `k->infinity`.  Therefore

\[
\boxed{O_{qr}(B)=o(B(\log B)^3)}.
\]

Since the triple overlap is contained in every pair overlap,

\[
\boxed{T(B)=o(B(\log B)^3)}.
\]

The factor `2` is an upper multiplicity and cannot weaken the limiting squeeze.
This explicitly answers Qwen R02 MINOR-1.

---

## 12. Exactly-one directional theorem candidate

Combining the raw theorem with pair/triple lower order and exact
inclusion--exclusion yields

\[
\boxed{
N_q(B)
\sim
\frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\qquad q\in\{ab,ac,bc\}.
}
\]

Summing and using `sum I_q=pi^2/8`,

\[
\boxed{
N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3.
}
\]

The normalized candidate limit is

\[
\left(
\frac{I_{ab}}{\pi^2/8},
\frac{I_{ac}}{\pi^2/8},
\frac{I_{bc}}{\pi^2/8}
\right)
\]

with numerical display

```text
(0.5347369332313988,
 0.24535917783225203,
 0.21990388893634913)

ab:ac:bc = 2.431684750178191 : 1.115756428951881 : 1
```

These decimals are consequences of the chamber integrals, not separately
fitted asymptotic constants.

---

## 13. R02 review crosswalk

### Grok R02

```text
zero-mode curved-region quantitative closure     -> 13-12ad §§7-10
mixed correction uniformity / harmonics          -> 13-12ad §§2-11
positive-valuation absolute constant             -> 13-12ae §§2-7
complete local-state refinement                  -> 13-12ae §§3,5,6,8
```

### Claude R02

```text
weighted-l1 uniformity                           -> 13-12ad §§2-6
nonzero harmonic lower order                     -> 13-12ad §§10-11
```

### Qwen R02

```text
MAJOR-1 inert positive valuation tail             -> 13-12ae §§2-7
MAJOR-2 convolution / curved transfer             -> 13-12ad §§6-9 and R03 §5.1
MINOR-1 tagged factor 2                           -> 13-12ae §8 and R03 §11
MINOR-2 Stage12 use in Vaaler error               -> R03 §7
MINOR-3 OE/EE curved branch summary               -> R03 §6.1
MINOR-4 analytic J_q=2I_q/pi bridge               -> R03 §3
```

This crosswalk is only navigation.  It does not tell the reviewer what verdict
to return.

---

## 14. Required R03 audit questions

A reviewer should independently check at least:

1. definitions, canonicalization, projection factor 2 and inclusion--exclusion;
2. Gelfand--Leray weights and chamber integrals;
3. the analytic `J_q=2I_q/pi` change of variables;
4. the raw `j=0` local coefficient system without seeded directional constants;
5. the explicit `529 p^-5/4` Wiener estimate and uniformity in harmonics;
6. logarithmic moments and the anisotropic convolution/curved-region transfer;
7. the concrete small-height, wing, mesh, Vaaler and harmonic error budgets;
8. OE/EE parity handling at the claimed finite 2-adic level;
9. whether common `Theta` is proved before Stage12 total calibration;
10. the exact inert valuation table, including exclusion of `v_p(h)>0`;
11. the unit-state finite-field acceptance calculation;
12. the exact local multiplier `(p+5)/(2(p+1))`;
13. fixed-conductor residue-character transfer with `p` fixed before `B`;
14. tagged pair-overlap majorization and the order of limits;
15. the final exactly-one theorem and all non-claims.

---

## 15. Non-claims and verdict status

R03 does not claim:

- existence or nonexistence of a perfect cuboid;
- an effective convergence threshold or explicit convergence rate;
- monotonicity of finite directional ratios;
- publication-grade independent peer review;
- a certified numerical enclosure for `kappa`;
- correctness of Stage12 R09 beyond treating it as the declared prior input.

The project does **not** self-declare Stage13 closed here.

```text
STAGE13_12AD=COMPLETE_QUANTITATIVE_J0_ANALYTIC_CLOSURE
STAGE13_12AE=COMPLETE_EXACT_PADIC_LOCAL_CLOSURE
STAGE13_12AF=R03_REVIEW_RESYNTHESIS
STAGE13_GLOBAL_REVIEW_STATUS=PENDING_EXTERNAL_R03
R03_SELF_DECLARED_CLOSED=false
```
