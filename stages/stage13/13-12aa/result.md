# Stage13-12aa — non-circular `j=0` common-factor repair

> **STATUS:** `STAGE13_12AA_COMPLETE_COMMON_FACTOR_REPAIR`
>
> **EXTERNAL_REVIEW_TRIGGER:** Claude returned `OPEN`
>
> **FATAL_UNDER_REPAIR:** direction-neutrality of the raw `j=0` arithmetic factor
>
> **STAGE13_GLOBAL_REVIEW_STATUS:** `OPEN`
>
> **NEXT:** `Stage13-12ab` — independent audit of the fixed-modulus overlap transfer

Stage13-12aa reopens the Stage13 proof after the external review of the R01
single-file bundle identified a fatal gap in the old Stage13-7jb presentation.

The external review was correct on the central point: the old
`supported_richness_raw_asymptotic.py` is not an independent proof that the
raw-incidence arithmetic amplification is the same in the `ab/ac/bc`
directions. It first forms

\[
D_q=\frac{\kappa I_q}{3\pi^3}
\]

from the Stage12 total constant and the chamber proportions, and only
afterwards checks that \(D_q/K_q\) is common. Since Stage13-7j already has
\(K_q\propto I_q\), the equality of those three ratios is algebraic. That
validator remains useful provenance, but it is not accepted here as the proof
of direction-neutrality.

This repair therefore starts over at the raw channel and uses the following
rule:

```text
NO_CATEGORYWISE_RAW_CONSTANT_IS_SEEDED.
FIRST_PROVE: A_q(B) ~ Theta * J_q * B(log B)^3 with one unknown Theta.
ONLY_AFTER_THAT: use the frozen Stage12 TOTAL theorem to determine Theta.
```

That removes the circularity.

---

## 1. Exact raw `j=0` primitive local kernel

Use the Stage13-7g/Stage12 outer coordinates

\[
p=hrs,\qquad
z=\frac{h(s^2-r^2)}2,\qquad
d=\frac{h(r^2+s^2)}2,\qquad
(r,s)=1,
\]

with the already locked OE/EE parity split. Let \(q\equiv1\pmod4\) be a split
prime and write

\[
a=v_q(h),\qquad b=v_q(rs),\qquad e=a+b.
\]

Because \((r,s)=1\), at most one of the two base variables carries \(b>0\).

For the **raw** primitive face count there is no normalization
\(1/(G-1)\). The relevant channel is therefore \(j=0\). If

\[
G_e=2e+1
\]

is the zero angular representation count and

\[
H_e(\theta)=1+2\sum_{m=1}^{e}\cos(m\theta)
\]

is its \(\ell\)-th Gaussian angular numerator, primitive support gives the
exact local differences

\[
Z_0(a,b)
=
G_{a+b}-\mathbf 1_{a\ge1}G_{a+b-1}
=
\begin{cases}
2b+1,&a=0,\\
2,&a\ge1,
\end{cases}
\]

and

\[
Z_\ell(a,b;\theta)
=
H_{a+b}(\theta)
-\mathbf 1_{a\ge1}H_{a+b-1}(\theta)
=
\begin{cases}
H_b(\theta),&a=0,\\
2\cos((a+b)\theta),&a\ge1.
\end{cases}
\]

This is the same primitive subtraction that appears in the Stage12
coefficient system, now written explicitly for \(j=0\). No chamber constant
or Stage12 value of \(\kappa\) enters these identities.

The companion audit checks these identities coefficient by coefficient.

---

## 2. Pure one-variable factors

Put \(x=q^{-s_h}\) for the height/scale variable and \(y=q^{-s_r}\) for one
base variable. For a nonzero angular phase \(\theta\), the pure split-prime
series are

\[
A_\ell(x)
=
1+\sum_{a\ge1}2\cos(a\theta)x^a
=
\frac{1-x^2}{1-2\cos\theta\,x+x^2},
\]

and

\[
B_\ell(y)
=
1+\sum_{b\ge1}H_b(\theta)y^b
=
\frac{1+y}{1-2\cos\theta\,y+y^2}.
\]

At the zero angular mode \(\theta=0\),

\[
A_0(x)=\frac{1+x}{1-x},
\qquad
B_0(y)=\frac{1+y}{(1-y)^2}.
\]

Hence, after the standard split/inert/2-adic finite factors are collected into
absolutely convergent residual products,

\[
\boxed{
A_0(s)=\zeta(s)L(s,\chi_4)E_{h,0}(s),
}
\]

\[
\boxed{
B_0(s)=\zeta(s)^2L(s,\chi_4)E_{b,0}(s).
}
\]

For every nonzero Gaussian harmonic \(\ell\ge1\),

\[
\boxed{
A_\ell(s)=L(s,\xi_{8\ell})E_{h,\ell}(s),
}
\]

\[
\boxed{
B_\ell(s)=\zeta(s)L(s,\xi_{8\ell})E_{b,\ell}(s).
}
\]

The decisive difference is visible here: the zero mode has one zeta pole in
the \(h\)-variable and two zeta poles in each base variable, while every
nonzero harmonic loses the zeta pole in \(h\).

---

## 3. Three-variable mixed correction at `j=0`

At a split prime the full local three-variable series is

\[
\begin{aligned}
D_\ell(x,y,z)
={}&1
+\sum_{a\ge1}2\cos(a\theta)x^a\\
&+\sum_{b\ge1}H_b(\theta)(y^b+z^b)\\
&+\sum_{a,b\ge1}2\cos((a+b)\theta)x^a(y^b+z^b).
\end{aligned}
\]

There is no term with positive exponents in both \(y\) and \(z\), because
\((r,s)=1\).

Factor

\[
C_\ell(x,y,z)
=
\frac{D_\ell(x,y,z)}
{A_\ell(x)B_\ell(y)B_\ell(z)}.
\]

Exactly,

\[
D_\ell(x,0,0)=A_\ell(x),\qquad
D_\ell(0,y,0)=B_\ell(y),\qquad
D_\ell(0,0,z)=B_\ell(z).
\]

Therefore every nonconstant monomial of \(C_\ell-1\) contains at least two
positive coordinate exponents.

For \(|x|,|y|,|z|\le q^{-1/2-\delta}\), the displayed rational forms for
\(A_\ell,B_\ell\) and their inverses have bounds depending only on
\(\delta\), uniformly in the phase \(\theta\). The coefficient series for
\(D_\ell\) is also uniformly bounded because

\[
|2\cos(n\theta)|\le2,
\qquad
|H_b(\theta)|\le 2b+1.
\]

In the same weighted Dirichlet/Wiener algebra used in Stage13-7h this gives

\[
\boxed{
\|C_{\ell,q}-1\|_\delta
\ll_\delta q^{-1-2\delta},
}
\]

uniformly in the retained harmonic range. Thus the global mixed correction
product converges absolutely on

\[
\Re s_h,\Re s_r,\Re s_s\ge\frac12+\delta.
\]

The inert-prime coprimality factors and the finite \(2\)-adic OE/EE factors
are independent of the canonical category \(q\in\{ab,ac,bc\}\); they enter
the common arithmetic multiplier only.

This is the `j=0` globalization that was missing from the old 7jb presentation.

---

## 4. Zero angular mode: the category enters only archimedeanly

Let \(\phi\in(\pi/4,\pi/2)\) be the outer \((r,s)\) polar angle and

\[
t(\phi)=\frac{s^2-r^2}{2rs}.
\]

Let \(k_q(t)\) be the zero Fourier coefficient of the inner-face interval
indicator that becomes canonical category \(q\). These are exactly the
Stage13-7j category kernels. Define

\[
J_q
=
\int_{\pi/4}^{\pi/2}k_q(t(\phi))\,d\phi.
\]

Stage13-7j independently checked the exact bridge

\[
\boxed{
J_q=\frac{2}{\pi}I_q
}
\]

and the partition identity

\[
\boxed{
J_{ab}+J_{ac}+J_{bc}=\frac{\pi}{4}.
}
\]

Apply the Stage13-7h three-variable rectangle argument to the newly justified
\(j=0\) factorization. The zero-mode one-variable pole orders are now
\(1,2,2\). After summing \(h\) under
\(h(r^2+s^2)\le 2B\) (with the already locked OE/EE radial variants) and
passing from rectangles to the curved sector, the leading logarithmic degree
is \(3\).

The weighted mixed correction does not create a directional constant. For a
fixed convolution term \((u,v,w)\), the change of variables

\[
H=uh,\qquad R=vr,\qquad S=ws
\]

restores the same homogeneous region in the actual variables and contributes
the usual \(1/(uvw)\) factor. The shifts
\(\log(R/v)=\log R+O_v(1)\) and
\(\log(S/w)=\log S+O_w(1)\) affect only lower logarithmic degrees.
Absolute weighted-\(\ell^1\) convergence then permits summation over
\((u,v,w)\).

Consequently there exists a single arithmetic constant
\(\Theta>0\), independent of the canonical category, such that the zero
angular modes satisfy

\[
\boxed{
A_q^{(0)}(B)
\sim
\Theta\,J_q\,B(\log B)^3.
}
\]

No \(D_q\), no chamber proportion, and no Stage12 \(\kappa\) was used to
obtain the commonness of \(\Theta\).

---

## 5. Nonzero harmonics are lower order at the raw scale

The exact category indicators are recovered by pointwise
Selberg--Vaaler majorants/minorants of degree

\[
L=(\log B)^K
\]

with fixed \(K>0\).

The constant-term bracketing error is \(O(1/L)\) times the positive total raw
incidence mass. The exact Stage13-3d bridge and frozen Stage12 theorem give
the total bound

\[
A_{ab}(B)+A_{ac}(B)+A_{bc}(B)
=O(B(\log B)^3),
\]

so this error is

\[
O\!\left(\frac{B(\log B)^3}{L}\right)
=o(B(\log B)^3).
\]

For every retained \(\ell\ge1\), the \(h\)-factor is
\(L(s,\xi_{8\ell})E_{h,\ell}(s)\) with **no zeta pole**. The same
polylog-uniform Gaussian-Hecke zero-free input used in Stage13-7i therefore
gives arbitrary logarithmic cancellation in the \(h\)-summatory function for
\(\ell\le(\log B)^K\). The base factors have only the displayed single zeta
pole. The Stage13-7h rectangle/wing transfer, with the \(j=0\) weighted
correction above, then yields a lower-order contribution after summing the
\(O(L)\) retained harmonics.

The small-height channel may be separated before applying the Hecke
cancellation. Its two-base zero-mode majorant has one fewer radial logarithm
and is \(o(B(\log B)^3)\) for the same slowly growing height threshold used in
the 7h/7i boundary decomposition.

Therefore

\[
\boxed{
A_q(B)
=
A_q^{(0)}(B)
+o(B(\log B)^3)
}
\]

and hence

\[
\boxed{
A_q(B)
\sim
\Theta\,J_q\,B(\log B)^3
}
\]

with the **same unknown \(\Theta\)** for all three categories.

This is the missing non-circular common-factor lemma.

---

## 6. Only now calibrate with the frozen Stage12 total theorem

The exact Stage13-3d projection identity is

\[
C_{\rm prim}(B)
=
2\bigl(A_{ab}(B)+A_{ac}(B)+A_{bc}(B)\bigr).
\]

The frozen Stage12 R09 input is only the total theorem

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3.
\]

Therefore

\[
\sum_q A_q(B)
\sim
\frac{\kappa}{24\pi}B(\log B)^3.
\]

On the other hand, the independently proved common-factor form gives

\[
\sum_q A_q(B)
\sim
\Theta
\left(\sum_qJ_q\right)
B(\log B)^3
=
\Theta\frac{\pi}{4}B(\log B)^3.
\]

Thus

\[
\boxed{
\Theta=\frac{\kappa}{6\pi^2}.
}
\]

Using \(J_q=2I_q/\pi\),

\[
\boxed{
A_q(B)
\sim
\frac{\kappa I_q}{3\pi^3}B(\log B)^3.
}
\]

This obtains the old 7jb formula **after** direction-neutrality has been proved,
rather than using that formula to manufacture direction-neutrality.

The normalized raw limit is therefore restored non-circularly:

\[
\frac{A_q(B)}{\sum_r A_r(B)}
\longrightarrow
\frac{8I_q}{\pi^2},
\]

namely

```text
(0.5347369332313988,
 0.24535917783225203,
 0.21990388893634913)

ab:ac:bc
-> 2.431684750178191 : 1.115756428951881 : 1
```

at the same external-theorem level used by the Stage13-7h/7i analytic chain.

---

## 7. What is and is not repaired

The Claude review's main FATAL finding is accepted as a valid defect in the old
presentation. Stage13-12aa repairs that defect by replacing the circular
7jb constant check with the independent `j=0` factorization/common-factor
argument above.

The old files

```text
stages/stage13/scripts/13-7/supported_richness_raw_asymptotic.py
stages/stage13/data/13-7/supported_richness_raw_asymptotic_report.json
```

remain provenance and numerical diagnostics. Their categorywise
`D_q/K_q` equality is **not** cited as proof after 13-12aa.

This step does **not** re-close all of Stage13. Claude also raised a separate
major question about the fixed-modulus transfer used in the pair-overlap
sieve. That issue is logically downstream of the raw theorem and is assigned
to Stage13-12ab for an independent proof audit.

Accordingly the current precedence is

```text
STAGE13_EXTERNAL_REVIEW_R01=OPEN
STAGE13_12AA=COMPLETE_COMMON_FACTOR_REPAIR
CLAUDE_FATAL_DIRECTION_NEUTRALITY=REPAIRED
RAW_DIRECTIONAL_ASYMPTOTIC=RESTORED_NON_CIRCULARLY
EXACT_ONE_DIRECTIONAL_ASYMPTOTIC=NOT_YET_RECLOSED
PAIR_OVERLAP_FIXED_MODULUS_TRANSFER=PENDING_REAUDIT
STAGE13_GLOBAL_REVIEW_STATUS=OPEN
NEXT=Stage13-12ab
```
