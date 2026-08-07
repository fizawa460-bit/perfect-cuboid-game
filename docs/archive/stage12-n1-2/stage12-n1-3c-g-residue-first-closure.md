# Stage12-N1-3c.G：residue-first radial transfer による幾何kernel課題の解消

> **STATUS:** `MAJOR_03_CLOSED_BY_RESIDUE_FIRST_BYPASS`
>
> **PARENT:** `docs/stage12-n1-3c-coupled-region-transfer.md`
>
> **SOURCE_AUDIT:** `docs/review/stage12-n1-2-full-audit-r01.md`
>
> **THEOREM_STATUS:** `REPAIRABLE — NOT CLOSED`
>
> **SCOPE:** primitive oriented residue main only

## 0. 結論と方針転換

Stage12-N1-3cでは、除数変数 `(b,c)` を固定したexact kernel

\[
\mathcal K_B(b,c)
\]

を個別にarchimedean modelへ置き換える補題3c.Gを設定した。しかし、この補題は最終漸近式に必要な主張より強い。極端なanisotropyを持つ各 `(b,c)` について一様評価する必要はなく、最終的に必要なのは `(b,c)` を再び合計したresidue mainの評価だけである。

本稿では除数展開をいったん元へ戻し、元のedge variables `(r,s)` 上の非負乗法係数を先に平均する。すると、

- anisotropic family;
- side exclusions `(u,c)=1`, `(v,b)=1`;
- orientation boundary `bu=cv`;
- fixed-`(b,c)` arc discrepancy

を個別に評価する必要がなくなる。

代わりに必要なのは、元変数上の二変数長方形和とradial kernel `1/(r^2+s^2)` のStieltjes移送である。この長方形和は、一変数Selberg–Delangeの `z=2` 特殊形と絶対収束するcoprime cross correctionで処理できる。

したがって補題3c.Gは、固定 `(b,c)` ごとのstatementとして証明するのではなく、次の弱いが十分な命題へ置き換える。

> **Residue-first transfer.** exact residue main全体を元変数 `(r,s)` 上で直接平均すると、model mainと同じ
> \[
> \frac{\eta}{12\pi^2}B(\log B)^3
> =\frac{\kappa}{12\pi}B(\log B)^3
> \]
> を持ち、移送誤差は `o(B(log B)^3)` である。

---

## 1. 除数和を元へ戻した係数

Stage12-N1-2jのresidue weightを

\[
\gamma(n)=\frac1\pi\sum_{d\mid n}\beta(d)
\]

とする。以下

\[
g(n):=\pi\gamma(n)=\sum_{d\mid n}\beta(d)
=(1*\beta)(n)
\]

と置く。

`g` は非負乗法関数であり、`q\equiv1\pmod4` に対し

\[
\beta(q^j)=b_q:=\frac{2(q-1)}{q+1}
\qquad(j\ge1)
\]

だから

\[
g(q^k)=1+kb_q.
\]

`p\not\equiv1\pmod4` では

\[
g(p^k)=1.
\]

parity height factorを

\[
\lambda(r,s)
=
1+\mathbf1_{r\text{ odd}}\mathbf1_{s\text{ odd}}
\]

と書く。`(r,s)=1` のもとでは、これはodd–oddで2、opposite parityで1に一致する。

exact residue mainは

\[
\mathcal M(B)
=
\frac B\pi
\left\{
2\!\sum_{\substack{1\le r<s,(r,s)=1\\r,s\ \mathrm{odd}\\r^2+s^2\le2B}}
\frac{g(r)g(s)}{r^2+s^2}
+
\sum_{\substack{1\le r<s,(r,s)=1\\r,s\ \mathrm{opposite}\\r^2+s^2\le B}}
\frac{g(r)g(s)}{r^2+s^2}
\right\}.
\]

ここではfixed-`(b,c)` kernelを導入しない。

---

## 2. 共通cutoffへの還元

\[
\mathcal H_\lambda(B)
:=
\sum_{\substack{1\le r<s,(r,s)=1\\r^2+s^2\le B}}
\frac{\lambda(r,s)g(r)g(s)}{r^2+s^2}
\]

と置く。exact residue mainとの差はodd–odd annulus

\[
B<r^2+s^2\le2B
\]

だけであり、

\[
\mathcal M(B)
=
\frac B\pi\mathcal H_\lambda(B)
+
\frac{2B}{\pi}
\sum_{\substack{r<s,(r,s)=1\\r,s\ \mathrm{odd}\\B<r^2+s^2\le2B}}
\frac{g(r)g(s)}{r^2+s^2}.
\]

後述する長方形上界

\[
T_\lambda(R,S)\ll RS\log(2R)\log(2S)
\]

をdyadic boxesへ適用すると、任意の固定比annulus上で

\[
\sum_{B<r^2+s^2\le2B}
\frac{\lambda(r,s)g(r)g(s)\mathbf1_{(r,s)=1}}
{r^2+s^2}
\ll (\log B)^2.
\]

従って

\[
\boxed{
\mathcal M(B)
=
\frac B\pi\mathcal H_\lambda(B)
+O\!\left(B(\log B)^2\right)
}.
\]

cutoff `B` と `2B` の差はleading cubic logarithmに影響しない。

---

## 3. 一変数 `z=2` 平均

`g=1*\beta` なのでDirichlet級数は

\[
G(s)
:=
\sum_{n\ge1}\frac{g(n)}{n^s}
=
\zeta(s)B_\beta(s).
\]

Stage12-N1-2oで

\[
B_\beta(s)
=
\zeta(s)L(s,\chi_4)J_\beta(s)
\]

と分解し、`J_beta` が `Re s>1/2+epsilon` で正則かつ非零であることを確認した。従って

\[
G(s)
=
\zeta(s)^2H_g(s),
\qquad
H_g(s):=L(s,\chi_4)J_\beta(s),
\]

であり、`H_g` は同じ半平面の固定近傍で正則かつ非零である。

標準Selberg–Delangeの `z=2` 特殊形から、定数 `c_g>0,d_g` とzero-free-region saving `E_g(x)` が存在して

\[
\boxed{
G_0(X)
:=
\sum_{n\le X}g(n)
=
c_gX\log X+d_gX+O\!\left(XE_g(X)\right)
}
\]

を得る。特に

\[
G_0(X)\ll X\log(2X).
\]

本稿で必要なのはこの形と、そのodd/even restrictionである。parity restrictionは2-adic Euler factorを有限変更するだけなので、同じ誤差関数と次数を持つ。

---

## 4. 元変数上の二変数Dirichlet factorization

二変数係数を

\[
a_\lambda(r,s)
:=
\lambda(r,s)g(r)g(s)\mathbf1_{(r,s)=1}
\]

とし、

\[
D_\lambda(s_1,s_2)
:=
\sum_{r,s\ge1}
\frac{a_\lambda(r,s)}{r^{s_1}s^{s_2}}
\]

を考える。

### 4.1 odd primeのcross correction

odd prime `p` に対して

\[
U_p(s)
:=
\sum_{k\ge1}\frac{g(p^k)}{p^{ks}}.
\]

coprime条件によりlocal factorは

\[
D_p(s_1,s_2)
=
1+U_p(s_1)+U_p(s_2).
\]

一変数local factorは

\[
G_p(s)=1+U_p(s).
\]

従って

\[
D_p(s_1,s_2)
=
G_p(s_1)G_p(s_2)C_p(s_1,s_2),
\]

\[
C_p(s_1,s_2)
=
1-
\frac{U_p(s_1)U_p(s_2)}
{(1+U_p(s_1))(1+U_p(s_2))}.
\]

`g(p^k)\ll k+1` なので、固定 `epsilon>0` と

\[
\sigma_i:=\Re s_i\ge\frac12+\varepsilon
\]

に対して

\[
C_p(s_1,s_2)-1
=O_\varepsilon(p^{-\sigma_1-\sigma_2}).
\]

よって

\[
C_{\rm odd}(s_1,s_2)
:=
\prod_{p\ \mathrm{odd}}C_p(s_1,s_2)
\]

は `Re(s_1+s_2)>1` で絶対収束し、`(1,1)` の近傍で正則かつ非零である。

### 4.2 2-adic factor

`g(2^k)=1` である。coprime pairの2-adic exponentsは、両方0または一方だけ正である。`lambda` を含むlocal factorは、`x=2^{-s_1}`, `y=2^{-s_2}` として

\[
D_{2,\lambda}(s_1,s_2)
=
2+\frac{x}{1-x}+\frac{y}{1-y}.
\]

一方

\[
G_2(s_1)G_2(s_2)
=
\frac1{(1-x)(1-y)}.
\]

従って

\[
C_{2,\lambda}(s_1,s_2)
:=
D_{2,\lambda}(s_1,s_2)(1-x)(1-y)
\]

は全平面で正則な有限因子であり、

\[
C_{2,\lambda}(1,1)=1.
\]

以上から

\[
\boxed{
D_\lambda(s_1,s_2)
=
G(s_1)G(s_2)C_\lambda(s_1,s_2)
}
\]

を得る。ここで

\[
C_\lambda
=C_{2,\lambda}C_{\rm odd}
\]

は `(1,1)` の近傍で正則かつ非零であり、任意の固定 `delta>0` に対して係数展開

\[
C_\lambda(s_1,s_2)
=
\sum_{a,b\ge1}\frac{c_\lambda(a,b)}{a^{s_1}b^{s_2}}
\]

が

\[
\sum_{a,b\ge1}
\frac{|c_\lambda(a,b)|}{(ab)^{1/2+\delta}}
<\infty
\]

を満たす。

---

## 5. parity-weighted rectangle lemma

\[
T_\lambda(R,S)
:=
\sum_{r\le R}\sum_{s\le S}a_\lambda(r,s)
\]

とする。

### 補題 3c.G.1

任意の固定

\[
0<\varepsilon<\frac18
\]

に対し、`R,S>=2` で一様に

\[
\boxed{
\begin{aligned}
T_\lambda(R,S)
={}&C_\lambda^{(0)}RS\log R\log S
+RS\{C_{10}\log R+C_{01}\log S+C_{00}\}\\
&+O_\varepsilon\!\Bigl(
RS\log(2R)\log(2S)
\{E_{g,*}(R^{1/2})+E_{g,*}(S^{1/2})\}\\
&\hspace{34mm}
+\log(2R)\log(2S)
\{R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}\}
\Bigr),
\end{aligned}
}
\]

が成り立つ。ここで

\[
C_\lambda^{(0)}=c_g^2C_\lambda(1,1)>0
\]

であり、`E_{g,*}` は `E_g` の単調包絡線である。

### 証明

Dirichlet factorizationから厳密に

\[
T_\lambda(R,S)
=
\sum_{a\le R,b\le S}
 c_\lambda(a,b)
G_0(R/a)G_0(S/b)
\]

と書ける。係数領域を

\[
a\le R^{1/2},\quad b\le S^{1/2}
\]

とその補集合へ分ける。

小係数領域では一変数 `z=2` 展開を二回代入する。`C_lambda` が `(1,1)` の近傍で絶対収束するため、

\[
\sum\frac{|c_\lambda(a,b)|}{ab}
(1+\log a)(1+\log b)<\infty
\]

であり、主項はlogarithmに関するbidegree `(1,1)` の多項式になる。そのleading coefficientが

\[
c_g^2C_\lambda(1,1)
\]

である。

一変数誤差には小係数領域で

\[
E_g(R/a)\le E_{g,*}(R^{1/2}),
\qquad
E_g(S/b)\le E_{g,*}(S^{1/2})
\]

を使う。

大係数領域では

\[
G_0(X)\ll X\log(2X)
\]

とweighted coefficient normを使う。例えば `a>R^{1/2}` では

\[
\frac1a
\le
R^{-1/4+\varepsilon}a^{-1/2-2\varepsilon},
\]

したがって

\[
\sum_{a>R^{1/2},b\le S}
|c_\lambda(a,b)|G_0(R/a)G_0(S/b)
\]

\[
\ll_\varepsilon
R^{3/4+\varepsilon}S
\log(2R)\log(2S).
\]

`b>S^{1/2}` は対称であり、両方大きい領域も二つの尾部へ含める。これで補題が従う。`□`

---

## 6. leading rectangle constantと `eta`

補題3c.G.1のleading coefficientをEuler factorごとに計算する。

### 6.1 `p congruent 3 mod 4`

この場合 `g(p^k)=1`。一変数analytic factor `J_beta` のlocal factorは

\[
1-p^{-2s}
\]

であり、coprime cross correctionの `(1,1)` 値も

\[
1-p^{-2}
\]

である。従ってnormalized local factorは

\[
(1-p^{-2})^3.
\]

### 6.2 `q congruent 1 mod 4`

\[
b_q=\frac{2(q-1)}{q+1}
\]

とする。`x=q^{-1}` において

\[
G_q(1)
=
\sum_{k\ge0}(1+kb_q)x^k,
\]

二変数coprime local factorの分子は

\[
D_q(1,1)=2G_q(1)-1.
\]

直接計算すると

\[
D_q(1,1)
=
\frac{q+1}{q-1}
\left(1+\frac{4q}{(q+1)^2}\right).
\]

`J_beta` のlocal factor

\[
J_q(1)
=(1-q^{-1})
\left(1+(b_q-1)q^{-1}\right)
\]

とcross correctionを組み合わせると

\[
J_q(1)^2C_q(1,1)
=(1-q^{-1})^6D_q(1,1)
\]

\[
=
(1-q^{-2})
\left(1+\frac{4q}{(q+1)^2}\right)
(1-q^{-1})^4.
\]

### 6.3 front factor

\[
L(1,\chi_4)^2
=\left(\frac\pi4\right)^2,
\]

2-adic analytic factorは

\[
(1-2^{-1})^2C_{2,\lambda}(1,1)
=\left(\frac12\right)^2.
\]

従って

\[
\begin{aligned}
C_\lambda^{(0)}
={}&
\left(\frac\pi4\right)^2
\left(\frac12\right)^2
\prod_{p\equiv3(4)}(1-p^{-2})^3\\
&\times
\prod_{q\equiv1(4)}
(1-q^{-2})
\left(1+\frac{4q}{(q+1)^2}\right)
(1-q^{-1})^4.
\end{aligned}
\]

一方

\[
\prod_{p\ \mathrm{odd}}(1-p^{-2})
=\frac8{\pi^2}
\]

であり、Stage12-N1-2kの

\[
\eta
=
\left(\frac\pi4\right)^2
\left(\frac12\right)^2
\prod_{p\equiv3(4)}(1-p^{-2})^2
\prod_{q\equiv1(4)}
\left(1+\frac{4q}{(q+1)^2}\right)
(1-q^{-1})^4
\]

と比較して

\[
\boxed{
C_\lambda^{(0)}
=\frac8{\pi^2}\eta
}.
\]

これは、odd-prime primitive density `8/pi^2` とdensity-corrected divisor residue `eta` の積に一致する。

---

## 7. radial Stieltjes transfer

full quadrantのharmonic sumを

\[
\widetilde{\mathcal H}_\lambda(B)
:=
\sum_{\substack{r,s\ge1,(r,s)=1\\r^2+s^2\le B}}
\frac{\lambda(r,s)g(r)g(s)}{r^2+s^2}
\]

とする。

係数とkernelは `r,s` に関して対称である。また `(r,s)=1` と `r=s` は `(r,s)=(1,1)` しか許さないため、diagonalは `O(1)` である。従って

\[
\boxed{
\mathcal H_\lambda(B)
=\frac12\widetilde{\mathcal H}_\lambda(B)+O(1)
}.
\]

orientation境界の平均格子点評価は不要である。

### 7.1 main polynomialの移送

二変数Stieltjes表示は

\[
\widetilde{\mathcal H}_\lambda(B)
=
\iint_{x^2+y^2\le B}
\frac1{x^2+y^2}\,dT_\lambda(x,y).
\]

leading rectangle term

\[
C_\lambda^{(0)}xy\log x\log y
\]

のmixed derivativeは

\[
C_\lambda^{(0)}
(\log x+1)(\log y+1)\,dx\,dy.
\]

lower logarithmic termsと境界項は `O(L^2)` である。leading integralは

\[
I(B)
:=
\int_{\substack{x,y\ge1\\x^2+y^2\le B}}
\frac{\log x\log y}{x^2+y^2}\,dx\,dy.
\]

polar coordinates

\[
x=t\cos\theta,
\qquad
y=t\sin\theta
\]

を使うと

\[
\frac{dx\,dy}{x^2+y^2}
=\frac{dt}{t}\,d\theta.
\]

`theta` のendpoint近傍は `log sin theta`, `log cos theta` が可積分であり、leading cubic termは `(log t)^2` だけから来る。`L=log B` として

\[
I(B)
=
\frac\pi2
\int_1^{B^{1/2}}
\frac{(\log t)^2}{t}\,dt
+O(L^2)
\]

\[
=
\frac\pi2\cdot\frac{(L/2)^3}{3}
+O(L^2)
=
\frac\pi{48}L^3+O(L^2).
\]

従ってfull quadrantでは

\[
\widetilde{\mathcal H}_\lambda(B)
=
\frac{\pi C_\lambda^{(0)}}{48}L^3
+o(L^3),
\]

orientation `r<s` では

\[
\boxed{
\mathcal H_\lambda(B)
=
\frac{\pi C_\lambda^{(0)}}{96}L^3
+o(L^3)
=
\frac\eta{12\pi}L^3
+o(L^3)
}.
\]

---

## 8. rectangle errorのradial適合性

補題3c.G.1の誤差を対数dyadic box

\[
\mathcal B(R,S)=[R,2R]\times[S,2S]
\]

上で移送する。

arcとbox境界を除くbox上で

\[
K(x,y)=\frac1{x^2+y^2}
\]

の二変数部分和分ノルムは

\[
\boxed{
\|K\|_{{\rm PS},\mathcal B}
\ll\frac1{R^2+S^2}
}.
\]

### 8.1 retained boxes

\[
\min(R,S)
\ge
S_0
:=
\exp\!\left(\frac12(\log B)^{1/4}\right)
\]

とする。例えば `R<=S` ならpower errorのbox寄与は

\[
\ll
\log(2R)\log(2S)
\frac{R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}}
{R^2+S^2}
\]

\[
\ll
(\log B)^2R^{-1/4+\varepsilon}.
\]

`epsilon<1/8` なので、これは

\[
\ll
(\log B)^2
\exp\{-c_\varepsilon(\log B)^{1/4}\}
\]

であり、任意の固定対数冪より小さい。多項対数個のboxesを足しても `o(L^3)` である。zero-free-region errorも同様に小さい。

### 8.2 shallow boxes

`R<=S` とし `R<S_0` のboxでは、非負性と長方形上界から

\[
\sum_{(r,s)\in\mathcal B(R,S)}
\frac{a_\lambda(r,s)}{r^2+s^2}
\ll
\frac{RS\log(2R)\log(2S)}{S^2}
\]

\[
\ll
\frac RS\log(2R)\log(2S).
\]

`R` と `S` をdyadicに合計すると

\[
\ll
L(\log S_0)^2
=O(L^{3/2})
=o(L^3).
\]

対称領域も同じである。

### 8.3 radial arc boxes

sharp arc `x^2+y^2=B` を横切るdyadic boxesは、固定比annulus

\[
cB\le x^2+y^2\le CB
\]

に含まれる。長方形上界を使うと、その全harmonic massは

\[
O(L^2).
\]

従ってarcに接するboxesを内側または外側へ丸める差はlower orderである。fixed-`(b,c)` arc discrepancyを評価する必要はない。

以上からrectangle error、shallow region、arc boundaryを合計して

\[
\boxed{
\widetilde{\mathcal H}_\lambda(B)
-
\frac{\pi C_\lambda^{(0)}}{48}L^3
=o(L^3)
}.
\]

---

## 9. residue mainの完成

Section 2とSection 7–8を組み合わせると

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
\boxed{
\mathcal M(B)
\sim
\frac\eta{12\pi^2}B(\log B)^3
}.
\]

Stage12-N1-2kの厳密局所恒等式

\[
\eta=\pi\kappa
\]

を使えば

\[
\boxed{
\mathcal M(B)
\sim
\frac\kappa{12\pi}B(\log B)^3
}.
\]

Stage12-N1-3bによりfixed-height remainderのouter averageは任意の固定対数冪より小さいため、residue mainとheight remainderは接続済みである。Stage12-N1-3aの旧divisor-variable rectangle lemmaは、このresidue-first経路では3c.Gを閉じるための必須入力ではないが、別のmodel routeの整合性確認として残る。

---

## 10. 補題3c.Gの最終的な扱い

fixed `(b,c)` ごとの

\[
\mathcal K_B(b,c)
=
\mathcal K_B^{\rm main}(b,c)+\mathcal R_B(b,c)
\]

を平均する旧補題3c.Gは、最終証明に不要な強いstatementである。これを未証明の仮定として残さない。

代わりに、本稿の補題3c.G.1とradial transferを採用する。

```text
OLD_3C_G_FIXED_DIVISOR_KERNEL=SUPERSEDED_NOT_REQUIRED
NEW_3C_G_RESIDUE_FIRST_RECTANGLE=PROVED
NEW_3C_G_RADIAL_STIELTJES_TRANSFER=PROVED
MAJOR_03_COUPLED_REGION_TRANSFER=CLOSED_BY_STAGE12_N1_3C_G
```

ただし、次は引き続き未完了である。

- MAJOR-04：counting definition / constant sheet / self-contained bundle;
- Tenenbaum参照版と定理番号の固定;
- 2jの壊れたcontrol character修正;
- 3a〜3c.Gを反映した新しい統合稿;
- 独立Round 2再監査。

従ってStage12-N1-2全体はまだ `CLOSED` と呼ばない。
