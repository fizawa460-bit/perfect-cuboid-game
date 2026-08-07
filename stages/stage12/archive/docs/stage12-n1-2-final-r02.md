# Stage12-N1-2 Final R02：primitive oriented count repaired proof

> **DOCUMENT_STATUS:** `REPAIRED_PROOF_CANDIDATE_PENDING_INDEPENDENT_REAUDIT`
>
> **COUNTING_TARGET:** `C_prim(B)` from `stage12-n1-3d-definition-sheet.md`
>
> **CONSTANT_TARGET:** `kappa`, `eta` from `stage12-n1-3d-constant-sheet.md`
>
> **SUPERSEDES:** old `docs/stage12-n1-2-final.md`

## 0. 主張範囲と候補定理

本稿は、Stage12-N1-3a、3b、3c.G、3dを統合した自己完結版である。

対象はdefinition sheetで定義したprimitive oriented count

\[
C_{\rm prim}(B)
=
\sum_{k\le B}\mu(k)
C_{\rm raw}(\lfloor B/k\rfloor),
\]

\[
C_{\rm raw}(B)
=
\sum_{(h,r,s)\in\mathcal D_B}
\{G(hrs)-1\}.
\]

候補定理は

\[
\boxed{
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}
B(\log B)^3
\qquad(B\to\infty).
}
\]

これは完全直方体の存在・非存在、canonical count、exact-one-face countへの自動変換を主張しない。

中心解析項MAJOR-01〜03と自己完結性MAJOR-04は本稿系列で修復した。ただし、独立再監査が完了するまでproject statusは `CLOSED` としない。

---

## 1. exact counting convention

\[
\mathcal D_B
=
\left\{(h,r,s)\in\mathbb N^3:
1\le r<s,
(r,s)=1,
h(r^2+s^2)\le2B,
h(r^2+s^2)\equiv0\pmod2
\right\},
\]

\[
G(n)
=
\prod_{\substack{q\mid n\\q\equiv1(4)}}
(2v_q(n)+1).
\]

`r<s` とStage12のdistinguished-face conventionを保持するため、このcountはorientedである。辺置換のcanonical quotientは行わない。

Stage12-N1-2fのrepeated-side nonexistenceにより

\[
C_{\rm distinct,raw}(B)=C_{\rm raw}(B)
\]

である。

---

## 2. primitive-first exact reindexing

固定coprime pair `(r,s)` に対し

\[
A_{r,s}(m)
=
\sum_{k\mid m}\mu(k)
\{G((m/k)rs)-1\}.
\]

parity factorを

\[
\lambda(r,s)
=
\begin{cases}
2,&r,s\text{ odd},\\
1,&r,s\text{ opposite parity}
\end{cases}
\]

とする。するとexactに

\[
\boxed{
C_{\rm prim}(B)
=
\sum_{1\le r<s\atop(r,s)=1}
\sum_{m\le\lambda(r,s)B/(r^2+s^2)}
A_{r,s}(m).
}
\]

`m=1` では

\[
A_{r,s}(1)=G(rs)-1.
\]

`m>1` では、全素因数が `1 mod 4` の場合だけ非零で、

\[
A_{r,s}(m)
=
G(rs)
\prod_{p\mid m}
\frac{2}{2v_p(rs)+1}.
\]

---

## 3. fixed-height partial sumとMAJOR-02修復

\[
\beta(1)=1,
\]

\[
\beta(q^j)=\frac{2(q-1)}{q+1}
\quad(q\equiv1(4),\ j\ge1),
\]

\[
\beta(p^j)=0
\quad(p=2\text{ or }p\equiv3(4),\ j\ge1).
\]

\[
\gamma(n)
=
\frac1\pi\sum_{d\mid n}\beta(d),
\qquad
g(n):=\pi\gamma(n)=(1*\beta)(n).
\]

fixed-height sumは

\[
\sum_{m\le X}A_{r,s}(m)
=
\gamma(rs)X-1+R_{r,s}(X).
\]

Stage12-N1-3bでは、旧2kの不正な `omega(X/l)` の引き出しを使用せず、base circle remainderの弱い形とfinite Euler correctionのabsolute `1/2`-normから

\[
\boxed{
R_{r,s}(X)
\ll
G(rs)H_{\rm abs}(rs)X^{1/2}
}
\]

を得た。

`W(n):=G(n)H_abs(n)` とし、ある固定 `K` について

\[
\sum_{n\le T}W(n)
\ll T(\log(2T))^K
\]

を使う。retained region

\[
X_{r,s}
:=
\frac{\lambda(r,s)B}{r^2+s^2}
\ge
X_0:=\exp((\log B)^{1/4})
\]

では、dyadic radial shellにより

\[
\sum_{\rm retained}
W(rs)X_{r,s}^{1/2}
\ll
B X_0^{-1/2}(\log B)^{2K}.
\]

従って任意の固定 `A>0` に対して

\[
\boxed{
\sum_{\rm retained}R_{r,s}(X_{r,s})
=o\!\left(B(\log B)^{-A}\right).
}
\]

shallow regionは後のradial main estimateと一緒に低次化する。

---

## 4. residue mainへ還元

fixed-height mainを代入すると

\[
\mathcal M(B)
=
B
\sum_{1\le r<s\atop(r,s)=1}
\frac{\lambda(r,s)\gamma(rs)}{r^2+s^2}
\mathbf1_{r^2+s^2\le\lambda(r,s)B}.
\]

`(r,s)=1` と `g` の乗法性から

\[
\gamma(rs)=\frac1\pi g(r)g(s).
\]

従って

\[
\boxed{
\mathcal M(B)
=
\frac B\pi
\left\{
2\sum_{\substack{r<s,(r,s)=1\\r,s\text{ odd}\\r^2+s^2\le2B}}
\frac{g(r)g(s)}{r^2+s^2}
+
\sum_{\substack{r<s,(r,s)=1\\r,s\text{ opposite}\\r^2+s^2\le B}}
\frac{g(r)g(s)}{r^2+s^2}
\right\}.
}
\]

common cutoff版を

\[
\mathcal H_\lambda(B)
:=
\sum_{\substack{r<s,(r,s)=1\\r^2+s^2\le B}}
\frac{\lambda(r,s)g(r)g(s)}{r^2+s^2}
\]

とする。odd--odd annulus `B<r^2+s^2<=2B` のharmonic massは `O((log B)^2)` なので

\[
\boxed{
\mathcal M(B)
=
\frac B\pi\mathcal H_\lambda(B)
+O(B(\log B)^2).
}
\]

---

## 5. Selberg--Delange reference lock

\[
B_\beta(s)
:=
\sum_{n\ge1}\frac{\beta(n)}{n^s}
=
\zeta(s)L(s,\chi_4)J_\beta(s).
\]

`J_beta` は任意の固定 `epsilon>0` に対して `Re s>=1/2+epsilon` の閉部分領域で局所一様絶対収束し、正則である。

Stage12-N1-3d reference lockではTenenbaum, Chapter II.5, Theorem II.5.2のfinite-order expansionを用い、特定の未照合subexponential remainderを必要としない。

任意の固定 `A>0` に対して

\[
\sum_{n\le x}\beta(n)
=
c_\beta x
+O_A(x(\log(2x))^{-A}).
\]

また `g=1*beta` なので

\[
G_g(s)
:=
\sum_{n\ge1}\frac{g(n)}{n^s}
=
\zeta(s)^2L(s,\chi_4)J_\beta(s),
\]

従って `z=2` caseから

\[
\boxed{
G_0(x)
:=
\sum_{n\le x}g(n)
=
x(c_g\log x+d_g)
+O_A(x(\log(2x))^{-A}).
}
\]

特に

\[
G_0(x)\ll x\log(2x).
\]

---

## 6. parity-weighted coprime rectangle lemma

\[
a_\lambda(r,s)
:=
\lambda(r,s)g(r)g(s)\mathbf1_{(r,s)=1},
\]

\[
T_\lambda(R,S)
:=
\sum_{r\le R}\sum_{s\le S}a_\lambda(r,s).
\]

二変数Dirichlet seriesは

\[
D_\lambda(s_1,s_2)
=
G_g(s_1)G_g(s_2)C_\lambda(s_1,s_2),
\]

ここでcross correction `C_lambda` は `Re(s_1+s_2)>1` で絶対収束する。

任意の固定 `0<epsilon<1/8` に対して

\[
\begin{aligned}
T_\lambda(R,S)
={}&C_\lambda^{(0)}RS\log R\log S
+RS\{C_{10}\log R+C_{01}\log S+C_{00}\}\\
&+O_{\varepsilon,A}\!\Bigl(
RS\log(2R)\log(2S)
\{(\log(2R))^{-A}+(\log(2S))^{-A}\}\\
&\hspace{24mm}
+\log(2R)\log(2S)
\{R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}\}
\Bigr).
\end{aligned}
\]

この式は、cross coefficientsを先に畳み込み、小係数領域で `z=2` 一変数展開を二回適用し、大係数領域でweighted absolute normを用いて得る。

Stage12-N1-3aで修復した

\[
R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}
\]

型のtail exponentと同じ機構であり、旧文書の不成立な `R^(1/2+delta)S` への強化は使用しない。

---

## 7. rectangle leading constant

constant sheetのlocal calculationにより

\[
\boxed{
C_\lambda^{(0)}
=
\frac8{\pi^2}\eta.
}
\]

ここで

\[
\eta
=
\left(\frac\pi4\right)^2
\left(\frac12\right)^2
\prod_{p\equiv3(4)}(1-p^{-2})^2
\prod_{q\equiv1(4)}
\left(1+\frac{4q}{(q+1)^2}\right)
(1-q^{-1})^4.
\]

three-variable constantは

\[
\kappa
=
\left(\frac\pi4\right)^3
\left(\frac12\right)^3
\prod_{p\equiv3(4)}(1-p^{-2})^3
\prod_{q\equiv1(4)}
\frac{q^2+6q+1}{q^2-1}
(1-q^{-1})^6.
\]

prime-by-prime comparisonから

\[
\boxed{\eta=\pi\kappa.}
\]

---

## 8. radial Stieltjes transferと係数 `1/12`

full quadrant harmonic sumを

\[
\widetilde{\mathcal H}_\lambda(B)
:=
\sum_{\substack{r,s\ge1,(r,s)=1\\r^2+s^2\le B}}
\frac{\lambda(r,s)g(r)g(s)}{r^2+s^2}
\]

とする。

係数とkernelは対称であり、`r=s` とcoprimalityを同時に満たすのは `(1,1)` だけなので

\[
\mathcal H_\lambda(B)
=
\frac12\widetilde{\mathcal H}_\lambda(B)+O(1).
\]

二変数Stieltjes表示は

\[
\widetilde{\mathcal H}_\lambda(B)
=
\iint_{x^2+y^2\le B}
\frac1{x^2+y^2}
\,dT_\lambda(x,y).
\]

leading rectangle termのmixed derivativeは

\[
C_\lambda^{(0)}
(\log x+1)(\log y+1)\,dx\,dy.
\]

cubic termは

\[
I(B)
:=
\int_{\substack{x,y\ge1\\x^2+y^2\le B}}
\frac{\log x\log y}{x^2+y^2}
\,dx\,dy.
\]

polar coordinatesで

\[
\frac{dx\,dy}{x^2+y^2}
=
\frac{dt}{t}\,d\theta
\]

となり、`L=log B` として

\[
\boxed{
I(B)
=
\frac\pi{48}L^3+O(L^2).
}
\]

従って

\[
\widetilde{\mathcal H}_\lambda(B)
=
\frac{\pi C_\lambda^{(0)}}{48}L^3
+o(L^3),
\]

orientationを半分にして

\[
\boxed{
\mathcal H_\lambda(B)
=
\frac{\pi C_\lambda^{(0)}}{96}L^3
+o(L^3)
=
\frac\eta{12\pi}L^3
+o(L^3).
}
\]

ここで係数 `1/12` はradial kernelを保持したStieltjes integral、full-quadrant angle、orientation factorから得られている。

---

## 9. radial transfer error

対数dyadic box

\[
\mathcal B(R,S)=[R,2R]\times[S,2S]
\]

上で

\[
K(x,y)=\frac1{x^2+y^2}
\]

の部分和分ノルムは

\[
\|K\|_{{\rm PS},\mathcal B}
\ll
\frac1{R^2+S^2}.
\]

retained boxesでは

\[
\min(R,S)
\ge
S_0
:=
\exp\!\left(\frac12(\log B)^{1/4}\right).
\]

power-tail errorのbox contributionは、例えば `R<=S` なら

\[
\ll
(\log B)^2R^{-1/4+\varepsilon}.
\]

`epsilon<1/8` のため、これは任意の固定log-powerより小さい。Selberg--Delange remainderも展開次数を十分大きく固定することで同様に全box合計 `o(L^3)` となる。

shallow boxesの全harmonic massは

\[
O(L^{3/2}),
\]

radial arc boxesは

\[
O(L^2),
\]

lower rectangle polynomialとStieltjes boundary termsも

\[
O(L^2).
\]

従って

\[
\boxed{
\widetilde{\mathcal H}_\lambda(B)
-
\frac{\pi C_\lambda^{(0)}}{48}L^3
=o(L^3).
}
\]

---

## 10. endpointと非residue terms

- fixed-height remainder: `o(B(log B)^(-A))` on retained region by Stage12-N1-3b;
- shallow fixed-height sector: `o(BL^3)` by nonnegative rectangle upper bounds;
- constant `-1` in each fixed-height partial sum: `O(B)`;
- height floor replacement: `O(B(log B)^{1+o(1)})`;
- odd--odd cutoff `2B` versus `B`: `O(BL^2)`;
- primitive diagonal: `O(B)` after outer normalization;
- radial arc and Stieltjes boundaries: `O(BL^2)`.

すべて `o(BL^3)` である。

---

## 11. leading asymptoticの合成

Sections 4、8、9から

\[
\mathcal M(B)
=
\frac B\pi
\left\{
\frac\eta{12\pi}L^3+o(L^3)
\right\}
+O(BL^2).
\]

従って

\[
\mathcal M(B)
\sim
\frac\eta{12\pi^2}B L^3.
\]

Section 3と10のnonresidue termsはすべて低次なので

\[
\boxed{
C_{\rm prim}(B)
\sim
\frac\eta{12\pi^2}B(\log B)^3.
}
\]

最後に `eta=pi*kappa` を代入して

\[
\boxed{
C_{\rm prim}(B)
\sim
\frac\kappa{12\pi}B(\log B)^3.
}
\]

---

## 12. supersession table

| 旧箇所 | 問題 | 標準置換 |
|---|---|---|
| 旧2p / 旧Final §4 | 不成立な `R^(1/2+delta)S` 強化 | Stage12-N1-3aの `R^(3/4+epsilon)S` 型 |
| 旧2k / 旧Final §1 | `omega(X/l)` の誤った引き出し | Stage12-N1-3bのpointwise `X^(1/2)` とouter average |
| 旧2n / 旧Final §5 | radial kernelを省略した概要的 `L^3/12` | Stage12-N1-3c.Gのresidue-first radial Stieltjes transfer |
| fixed-`(b,c)` 3c.G案 | 最終定理より強い未証明kernel statement | `SUPERSEDED_NOT_REQUIRED` |
| specific `3/5` remainder | theorem referenceとの接続未固定 | Stage12-N1-3d arbitrary fixed log-power reference lock |
| 旧Finalの外部記号 | 自己完結でない | 3d definition / constant sheetsと本R02 |

---

## 13. 現在の判定

本R02は監査R01のMAJOR-01〜04、CLARIFICATION-01、MINOR-01〜02に対応した再提出候補である。

```text
MAJOR_01=CLOSED_BY_3A
MAJOR_02=CLOSED_BY_3B
MAJOR_03=CLOSED_BY_3C_G
MAJOR_04=CLOSED_BY_3D
CLARIFICATION_01=CLOSED_BY_3D_REFERENCE_LOCK
MINOR_01=CORRECTED_IN_ARCHIVED_2J_AND_NEW_BUNDLE
MINOR_02=CLOSED_BY_SELF_CONTAINED_R02
THEOREM_STATUS=REPAIRED_CANDIDATE_PENDING_INDEPENDENT_REAUDIT
```

独立再監査が `CLOSED` を返すまでは、project-wideには「証明済み完成定理」と呼ばない。