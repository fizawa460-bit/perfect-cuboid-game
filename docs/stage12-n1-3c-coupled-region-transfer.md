# Stage12-N1-3c：coupled-region transfer の完全変数展開とresidue-first閉包

> **STATUS:** `MAJOR_03_CLOSED_BY_STAGE12_N1_3C_G`
>
> **SOURCE_AUDIT:** `docs/review/stage12-n1-2-full-audit-r01.md`
>
> **SUPERSEDES:** Stage12-N1-2n §3 および旧Final §5の概要的な `L^3/12` 移送
>
> **DETAILED_CLOSURE:** `docs/stage12-n1-3c-g-residue-first-closure.md`
>
> **THEOREM_STATUS:** `REPAIRABLE — NOT CLOSED`

## 0. 目的と最終判定

本稿は独立監査R01のMAJOR-03を修復する。

旧2nと旧Finalでは、長方形主項から

\[
\int_{2\max(y,z)<L}
(L-2\max(y,z))\,dy\,dz
=\frac{L^3}{12}
\]

へ移る部分が概要に留まり、元変数、divisor variables、倍数変数、radial kernel、parity、orientation、境界項が一つの等式鎖で接続されていなかった。

Stage12-N1-3cではまずfixed divisor variables `(b,c)` を含むexact kernelまで変数台帳を復元し、model kernelから `L^3/12` を得るStieltjes計算を書いた。その結果、fixed-`(b,c)` anisotropic kernel remainderが残った。

Stage12-N1-3c.Gでは、このfixed-divisor statementが最終漸近式に必要な主張より強いことを確認した。除数展開を元へ戻し、元のedge variables `(r,s)` 上のparity-weighted coprime rectangle sumを先に平均することで、fixed-`(b,c)` kernel lemmaを使わずにexact residue mainを直接移送できる。

従って最終判定は

```text
OLD_3C_G_FIXED_DIVISOR_KERNEL=SUPERSEDED_NOT_REQUIRED
NEW_3C_G_RESIDUE_FIRST_RECTANGLE=PROVED
NEW_3C_G_RADIAL_TRANSFER=PROVED
MAJOR_03=CLOSED_BY_STAGE12_N1_3C_G
```

とする。

---

## 1. exact residue main

Stage12-N1-3bによりfixed-`(r,s)` height sumは

\[
\sum_{m\le X}A_{r,s}(m)
=
\gamma(rs)X-1
+O\!\left(G(rs)H_{\rm abs}(rs)X^{1/2}\right)
\]

であり、retained regionにおけるremainderのouter averageは任意の固定対数冪より小さい。

従ってMAJOR-03ではresidue mainだけを扱う。

\[
g(n):=\pi\gamma(n)
=\sum_{d\mid n}\beta(d)
=(1*\beta)(n)
\]

と置く。parity height factorを

\[
\lambda(r,s)
=
1+\mathbf1_{r\ \mathrm{odd}}\mathbf1_{s\ \mathrm{odd}}
\]

とする。

exact residue mainは

\[
\mathcal M(B)
=
\frac B\pi
\left\{
2\!\sum_{\substack{r<s,(r,s)=1\\r,s\ \mathrm{odd}\\r^2+s^2\le2B}}
\frac{g(r)g(s)}{r^2+s^2}
+
\sum_{\substack{r<s,(r,s)=1\\r,s\ \mathrm{opposite}\\r^2+s^2\le B}}
\frac{g(r)g(s)}{r^2+s^2}
\right\}.
\]

共通cutoffを使った

\[
\mathcal H_\lambda(B)
:=
\sum_{\substack{r<s,(r,s)=1\\r^2+s^2\le B}}
\frac{\lambda(r,s)g(r)g(s)}{r^2+s^2}
\]

との差はodd–odd annulus `B<r^2+s^2<=2B` だけである。長方形上界をdyadicに合計するとこのannulusのharmonic massは `O((log B)^2)` なので

\[
\boxed{
\mathcal M(B)
=
\frac B\pi\mathcal H_\lambda(B)
+O\!\left(B(\log B)^2\right)
}.
\]

---

## 2. fixed-divisor exact ledger

監査可能性のため、3cで復元した除数変数表示も記録する。

`(r,s)=1` と

\[
\gamma(n)=\frac1\pi\sum_{d\mid n}\beta(d)
\]

から各 `d|rs` は一意に

\[
d=bc,
\qquad b\mid r,
\qquad c\mid s,
\qquad(b,c)=1
\]

と分解される。

\[
r=bu,
\qquad s=cv
\]

と置けば

\[
(u,v)=1,
\qquad(u,c)=1,
\qquad(v,b)=1.
\]

従って

\[
\mathcal M(B)
=
\frac B\pi
\sum_{(b,c)=1}
\beta(b)\beta(c)\mathcal K_B(b,c),
\]

\[
\mathcal K_B(b,c)
=
\sum_{\substack{u,v\ge1\\(u,v)=1,(u,c)=1,(v,b)=1\\bu<cv}}
\frac{\lambda(u,v)}{b^2u^2+c^2v^2}
\mathbf1_{b^2u^2+c^2v^2\le\lambda(u,v)B}.
\]

この表示はexactである。ただし、最終証明はfixed `(b,c)` ごとに `K_B` を近似する経路を採用しない。

---

## 3. model routeの整合性

\[
\rho(n):=\prod_{p\mid n}\frac{p}{p+1},
\qquad
\alpha(n):=\beta(n)\rho(n)
\]

と置く。fixed-divisor local-density / archimedean modelは

\[
\mathcal K_B^{\rm main}(b,c)
=
\frac{\rho(bc)}{\pi bc}
[L-2\max(\log b,\log c)]_+.
\]

`alpha` のcoprime rectangle residue constantは

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

model kernelへ到達した後のStieltjes積分は

\[
\int_{y,z\ge0\atop2\max(y,z)<L}
(L-2\max(y,z))\,dy\,dz
=
\frac{L^3}{12}.
\]

従ってmodel mainは

\[
\frac\eta{12\pi^2}B(\log B)^3
=
\frac\kappa{12\pi}B(\log B)^3.
\]

このmodel routeはconstant checkとして有効だが、fixed-divisor remainderを最終入力にはしない。

---

## 4. residue-first二変数factorization

`g=1*beta` の一変数Dirichlet級数は

\[
G(s)
=
\sum_{n\ge1}\frac{g(n)}{n^s}
=
\zeta(s)B_\beta(s)
=
\zeta(s)^2H_g(s),
\]

\[
H_g(s)=L(s,\chi_4)J_\beta(s).
\]

Stage12-N1-2oの解析条件から `H_g` は `Re s>1/2+epsilon` の固定近傍で正則かつ非零である。標準Selberg–Delangeの `z=2` 特殊形により

\[
\sum_{n\le X}g(n)
=c_gX\log X+d_gX+O(XE_g(X)).
\]

二変数係数

\[
a_\lambda(r,s)
=
\lambda(r,s)g(r)g(s)\mathbf1_{(r,s)=1}
\]

のDirichlet級数は

\[
D_\lambda(s_1,s_2)
=
G(s_1)G(s_2)C_\lambda(s_1,s_2)
\]

と分解される。

odd prime `p` で

\[
U_p(s)=\sum_{k\ge1}g(p^k)p^{-ks}
\]

と置くと、coprime local factorは

\[
1+U_p(s_1)+U_p(s_2),
\]

従ってcross correctionは

\[
C_p(s_1,s_2)
=
1-
\frac{U_p(s_1)U_p(s_2)}
{(1+U_p(s_1))(1+U_p(s_2))}
=
1+O(p^{-\sigma_1-\sigma_2}).
\]

よって `C_lambda` は `Re(s_1+s_2)>1` で絶対収束する。2-adic factorは有限で、`lambda` のweighted massを正確に保持する。

---

## 5. parity-weighted rectangle lemma

\[
T_\lambda(R,S)
:=
\sum_{r\le R,s\le S}a_\lambda(r,s)
\]

とする。任意の固定 `0<epsilon<1/8` に対し

\[
\begin{aligned}
T_\lambda(R,S)
={}&C_\lambda^{(0)}RS\log R\log S
+RS\{C_{10}\log R+C_{01}\log S+C_{00}\}\\
&+O_\varepsilon\!\Bigl(
RS\log(2R)\log(2S)
\{E_{g,*}(R^{1/2})+E_{g,*}(S^{1/2})\}\\
&\hspace{29mm}
+\log(2R)\log(2S)
\{R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}\}
\Bigr).
\end{aligned}
\]

証明は `C_lambda` の係数を先に畳み込み、一変数 `z=2` 平均を二回代入する。大係数領域はStage12-N1-3aと同じweighted coefficient normで処理する。

leading coefficientはlocal factor計算により

\[
\boxed{
C_\lambda^{(0)}
=
\frac8{\pi^2}\eta
}.
\]

`p congruent 3 mod 4` のnormalized factorは `(1-p^{-2})^3`。`q congruent 1 mod 4` では

\[
D_q(1,1)
=
\frac{q+1}{q-1}
\left(1+\frac{4q}{(q+1)^2}\right),
\]

したがってnormalized factorは

\[
(1-q^{-2})
\left(1+\frac{4q}{(q+1)^2}\right)
(1-q^{-1})^4.
\]

front factorは

\[
L(1,\chi_4)^2(1-2^{-1})^2
=
\left(\frac\pi4\right)^2\left(\frac12\right)^2.
\]

これを `eta` と比較し

\[
\prod_{p\ \mathrm{odd}}(1-p^{-2})
=\frac8{\pi^2}
\]

を使う。

---

## 6. radial Stieltjes transfer

full quadrantのharmonic sumを

\[
\widetilde{\mathcal H}_\lambda(B)
:=
\sum_{\substack{r,s\ge1,(r,s)=1\\r^2+s^2\le B}}
\frac{\lambda(r,s)g(r)g(s)}{r^2+s^2}
\]

とする。

係数とkernelは対称である。また `(r,s)=1` と `r=s` は `(1,1)` しか許さない。従って

\[
\mathcal H_\lambda(B)
=
\frac12\widetilde{\mathcal H}_\lambda(B)+O(1).
\]

leading rectangle termを二変数Stieltjes移送すると

\[
\int_{x^2+y^2\le B}
\frac{\log x\log y}{x^2+y^2}\,dx\,dy
=
\frac\pi{48}(\log B)^3+O((\log B)^2).
\]

これはpolar coordinatesで

\[
\frac{dx\,dy}{x^2+y^2}
=\frac{dt}{t}\,d\theta
\]

を使い、full quadrant angle `pi/2` と

\[
\int_1^{B^{1/2}}
\frac{(\log t)^2}{t}\,dt
=
\frac{(\log B)^3}{24}
\]

から得る。

従って

\[
\widetilde{\mathcal H}_\lambda(B)
=
\frac{\pi C_\lambda^{(0)}}{48}(\log B)^3
+o((\log B)^3),
\]

\[
\boxed{
\mathcal H_\lambda(B)
=
\frac\eta{12\pi}(\log B)^3
+o((\log B)^3)
}.
\]

---

## 7. 誤差・境界予算

対数dyadic box

\[
[R,2R]\times[S,2S]
\]

上でradial kernelの部分和分ノルムは

\[
\left\|\frac1{x^2+y^2}\right\|_{{\rm PS}}
\ll\frac1{R^2+S^2}.
\]

retained boxesで `R<=S` の場合、rectangle power errorの寄与は

\[
\ll
(\log B)^2R^{-1/4+\varepsilon},
\]

したがって `min(R,S)>=exp((log B)^(1/4)/2)` では任意の固定対数冪より小さい。

shallow boxesは非負性と

\[
T_\lambda(R,S)\ll RS\log(2R)\log(2S)
\]

からdyadicに合計して `o((log B)^3)` となる。

radial arcを横切るboxesは固定比annulusへ含まれ、その全harmonic massは `O((log B)^2)`。odd–odd cutoff `2B` とcommon cutoff `B` の差も同じ次数である。

従ってrectangle error、shallow region、arc、parity cutoff差をすべて含めて

\[
\widetilde{\mathcal H}_\lambda(B)
-
\frac{\pi C_\lambda^{(0)}}{48}(\log B)^3
=o((\log B)^3).
\]

---

## 8. residue mainの完成

Sections 1、6、7より

\[
\mathcal M(B)
=
\frac B\pi
\left\{
\frac\eta{12\pi}(\log B)^3
+o((\log B)^3)
\right\}
+O(B(\log B)^2).
\]

従って

\[
\boxed{
\mathcal M(B)
\sim
\frac\eta{12\pi^2}B(\log B)^3
}.
\]

Stage12-N1-2kのlocal identity `eta=pi kappa` を使えば

\[
\boxed{
\mathcal M(B)
\sim
\frac\kappa{12\pi}B(\log B)^3
}.
\]

Stage12-N1-3bのfixed-height remainderと接続することで、MAJOR-03のcoupled-region transferを閉じる。

---

## 9. 残る項目

MAJOR-03は修復文書上で閉じたが、Stage12-N1-2全体はまだclosedではない。

残る項目:

- MAJOR-04：counting definition / constant sheet / self-contained bundle;
- Tenenbaumの使用版、定理番号、`z=1` と `z=2` の採用形の固定;
- 2jの壊れたcontrol character修正;
- 3a〜3c.Gを反映した新しい統合稿;
- 独立再監査。

```text
MAJOR_01=CLOSED_BY_STAGE12_N1_3A
MAJOR_02=CLOSED_BY_STAGE12_N1_3B
MAJOR_03=CLOSED_BY_STAGE12_N1_3C_G
MAJOR_04=OPEN_NEXT
THEOREM_STATUS=REPAIRABLE_NOT_CLOSED
NEXT_TASK=STAGE12_N1_3D_SELF_CONTAINED_DEFINITION_AND_CONSTANT_SHEETS
```
