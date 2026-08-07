# Stage12-N1-3d：Constant sheet for `kappa`, `eta`, and front factors

> **STATUS:** `MAJOR_04_CONSTANT_SHEET_COMPLETE`
>
> **SCOPE:** Stage12-N1-2 primitive oriented leading coefficient
>
> **THEOREM_STATUS:** `REPAIRED_CANDIDATE_PENDING_INDEPENDENT_REAUDIT`

## 0. このsheetの目的

本稿は、独立監査R01で不足とされた

- `kappa` の完全なEuler積;
- `eta` の完全なEuler積;
- 各odd-prime local factor;
- 2-adic / archimedean front factor;
- `eta=pi*kappa` のprime-by-prime comparison;
- 最終係数 `1/(12*pi)` までのfactor ledger

を一枚に固定する。

以下、`p` は `3 mod 4` の奇素数、`q` は `1 mod 4` の奇素数を表す。

---

## 1. three-variable constant `kappa`

Stage12-N1-2fのthree-law Euler factorを

\[
F_q(s)
:=
1+
\frac{2}{q^s-1}
+
\frac{4q}{(q+1)(q^s-1)}
\qquad(q\equiv1\pmod4)
\]

とする。`s=1` では

\[
\boxed{
F_q(1)
=
\frac{q^2+6q+1}{q^2-1}.
}
\]

`kappa` を

\[
\boxed{
\begin{aligned}
\kappa
:={}&
\left(\frac\pi4\right)^3
\left(\frac12\right)^3
\prod_{p\equiv3(4)}(1-p^{-2})^3\\
&\times
\prod_{q\equiv1(4)}
F_q(1)(1-q^{-1})^6.
\end{aligned}
}
\]

と定義する。

local notationでは

\[
\kappa_{\rm front}
:=
\left(\frac\pi4\right)^3
\left(\frac12\right)^3,
\]

\[
\kappa_p:=(1-p^{-2})^3,
\]

\[
\kappa_q
:=
\frac{q^2+6q+1}{q^2-1}
(1-q^{-1})^6.
\]

従って

\[
\kappa
=
\kappa_{\rm front}
\prod_{p\equiv3(4)}\kappa_p
\prod_{q\equiv1(4)}\kappa_q.
\]

normalized local factorsは `1+O(l^{-2})` であり、Euler積は絶対収束する。

---

## 2. two-variable residue constant `eta`

Stage12-N1-2kおよびStage12-N1-3c.Gのtwo-variable constantを

\[
\boxed{
\begin{aligned}
\eta
:={}&
\left(\frac\pi4\right)^2
\left(\frac12\right)^2
\prod_{p\equiv3(4)}(1-p^{-2})^2\\
&\times
\prod_{q\equiv1(4)}
\left(1+\frac{4q}{(q+1)^2}\right)
(1-q^{-1})^4.
\end{aligned}
}
\]

と定義する。

local notationでは

\[
\eta_{\rm front}
:=
\left(\frac\pi4\right)^2
\left(\frac12\right)^2,
\]

\[
\eta_p:=(1-p^{-2})^2,
\]

\[
\eta_q
:=
\left(1+\frac{4q}{(q+1)^2}\right)
(1-q^{-1})^4.
\]

したがって

\[
\eta
=
\eta_{\rm front}
\prod_{p\equiv3(4)}\eta_p
\prod_{q\equiv1(4)}\eta_q.
\]

ここでもnormalized factorsは `1+O(l^{-2})` であり、Euler積は絶対収束する。

---

## 3. `eta/kappa` のlocal comparison

### 3.1 `p congruent 3 mod 4`

\[
\boxed{
\frac{\eta_p}{\kappa_p}
=
\frac{(1-p^{-2})^2}{(1-p^{-2})^3}
=
(1-p^{-2})^{-1}.
}
\]

### 3.2 `q congruent 1 mod 4`

まず

\[
1+\frac{4q}{(q+1)^2}
=
\frac{q^2+6q+1}{(q+1)^2}.
\]

従って

\[
\begin{aligned}
\frac{\eta_q}{\kappa_q}
&=
\frac{
\dfrac{q^2+6q+1}{(q+1)^2}(1-q^{-1})^4
}{
\dfrac{q^2+6q+1}{q^2-1}(1-q^{-1})^6
}\\
&=
\frac{q^2}{q^2-1}
=
(1-q^{-2})^{-1}.
\end{aligned}
\]

よって

\[
\boxed{
\frac{\eta_q}{\kappa_q}
=(1-q^{-2})^{-1}.
}
\]

### 3.3 front factor

\[
\boxed{
\frac{\eta_{\rm front}}{\kappa_{\rm front}}
=
\frac{
(\pi/4)^2(1/2)^2
}{
(\pi/4)^3(1/2)^3
}
=
\frac8\pi.
}
\]

### 3.4 全積

\[
\prod_{\ell\ {m odd}}
(1-\ell^{-2})^{-1}
=
(1-2^{-2})\zeta(2)
=
\frac{\pi^2}{8}.
\]

従って

\[
\boxed{
\frac\eta\kappa
=
\frac8\pi\cdot\frac{\pi^2}{8}
=
\pi,
}
\]

すなわち

\[
\boxed{\eta=\pi\kappa.}
\]

この恒等式は数値近似ではなく、front factorと各odd-prime local factorのexact comparisonである。

---

## 4. residue-first rectangle coefficient

Stage12-N1-3c.Gでは

\[
g(n)=\pi\gamma(n)=(1*\beta)(n)
\]

を元変数 `(r,s)` 上で平均する。

parity-weighted coprime rectangle sumのleading coefficientを `C_lambda^(0)` とすると、local calculationにより

\[
\boxed{
C_\lambda^{(0)}
=
\frac8{\pi^2}\eta.
}
\]

`8/pi^2` はodd-prime primitive density

\[
\prod_{\ell\ {m odd}}(1-\ell^{-2})
=
\frac8{\pi^2}
\]

に一致する。

---

## 5. 2-adic parity ledger

`(r,s)=1` のため、許されるparity classはodd--oddまたはopposite parityだけである。

| branch | natural 2-adic mass | height factor `lambda` | weighted mass | radial cutoff |
|---|---:|---:|---:|---:|
| odd--odd | `1/4` | `2` | `1/2` | `r^2+s^2 <= 2B` |
| opposite parity | `1/2` | `1` | `1/2` | `r^2+s^2 <= B` |
| total |  |  | `1` |  |

従ってleading logarithmic coefficientにおける2-adic weighted massは正確に1である。

odd--odd branchのcutoff `2B` とcommon cutoff `B` の差は

\[
\log(2B)=\log B+\log2
\]

であり、cubic leading termを変えず、最大でもquadratic log termへ入る。

---

## 6. archimedean / orientation ledger

`L:=log B` とする。元変数上のleading mixed densityは

\[
C_\lambda^{(0)}
(\log x+1)(\log y+1)\,dx\,dy
\]

であり、cubic termは

\[
I(B)
:=
\int_{\substack{x,y\ge1\\x^2+y^2\le B}}
\frac{\log x\log y}{x^2+y^2}
\,dx\,dy
\]

から生じる。

polar coordinates

\[
x=t\cos\theta,
\qquad
y=t\sin\theta
\]

では

\[
\frac{dx\,dy}{x^2+y^2}
=
\frac{dt}{t}\,d\theta.
\]

full first quadrantのangular massは `pi/2` であり、

\[
\int_1^{B^{1/2}}
\frac{(\log t)^2}{t}\,dt
=
\frac{(L/2)^3}{3}
=
\frac{L^3}{24}.
\]

よって

\[
\boxed{
I(B)
=
\frac\pi{48}L^3+O(L^2).
}
\]

係数とkernelは `x,y` に対称である。primitive diagonal `x=y` はparameter levelでは `(r,s)=(1,1)` しか残さず `O(1)` なので、orientation `r<s` はleading termを正確に半分にする。

従ってoriented harmonic mainは

\[
\boxed{
\frac12\cdot
\frac\pi{48}\cdot
C_\lambda^{(0)}L^3
=
\frac\eta{12\pi}L^3.
}
\]

---

## 7. 最終front-factor product

fixed-height residue formulaには外側に

\[
\frac B\pi
\]

がある。前節のoriented harmonic coefficientを掛けると

\[
\frac B\pi
\cdot
\frac\eta{12\pi}L^3
=
\frac\eta{12\pi^2}B L^3.
\]

`eta=pi*kappa` を代入して

\[
\boxed{
\frac\eta{12\pi^2}
=
\frac\kappa{12\pi}.
}
\]

従って候補leading termは

\[
\boxed{
C_{\rm prim}(B)
\sim
\frac\eta{12\pi^2}B(\log B)^3
=
\frac\kappa{12\pi}B(\log B)^3.
}
\]

---

## 8. factor ledger summary

| source | factor |
|---|---:|
| fixed-height residue normalization | `B/pi` |
| parity-weighted coprime rectangle residue | `C_lambda^(0)=8 eta/pi^2` |
| full-quadrant radial cubic integral | `pi/48` |
| orientation `r<s` | `1/2` |
| combined | `eta B (log B)^3/(12 pi^2)` |
| exact local identity | `eta=pi*kappa` |
| final form | `kappa B (log B)^3/(12 pi)` |

---

## 9. diagnostic numerical values

既存のfinite prime productsは概ね

\[
\kappa\approx0.01855917,
\]

\[
\eta\approx0.05830533485,
\]

\[
\frac\kappa{12\pi}
\approx0.0004922973.
\]

を与える。これらはEuler積の収束診断であり、認証区間ではない。exact proofには使用しない。

---

## 10. source map

- `kappa`, `F_q`, three-law normalization: Stage12-N1-2f
- `eta`, local comparison `eta=pi*kappa`: Stage12-N1-2k
- `C_lambda^(0)`, parity ledger, radial/orientation factors: Stage12-N1-3c.G
- counting target: Stage12-N1-3d definition sheet

このsheetを今後のconstant normalizationの標準参照とする。