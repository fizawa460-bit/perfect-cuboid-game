# Stage12-N1-3a：一様長方形誤差の指数修復

> **STATUS:** `MAJOR_01_CLOSED_AT_RECTANGULAR_LEMMA_LEVEL`
>
> **SOURCE_AUDIT:** `docs/review/stage12-n1-2-full-audit-r01.md`
>
> **SUPERSEDES:** Stage12-N1-2p §3.2–§3.5 の `R^{1/2+δ}S + RS^{1/2+δ}` 型誤差
>
> **THEOREM_STATUS:** `REPAIRABLE — NOT CLOSED`

## 0. 目的と主張範囲

本稿は、独立監査R01の **MAJOR-01** を修復する。

Stage12-N1-2pでは、大係数領域で実際に得られた

\[
R^{3/4+\delta/2}S
\]

を、\(\delta\in(0,1/4)\) のもとで

\[
R^{1/2+\delta}S
\]

へ強化していた。しかし

\[
\frac34+\frac\delta2\le \frac12+\delta
\]

には \(\delta\ge1/2\) が必要であり、使用範囲と両立しない。

本稿では、誤った強化を撤回し、正しい弱い一様長方形誤差

\[
R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}
\]

へ置き換える。また、後続の結合領域移送で必要となるboxwise kernelとの適合性を、抽象的な部分和分ノルムのもとで確認する。

本稿だけでは、次を閉じない。

- MAJOR-02：fixed-circle remainder;
- MAJOR-03：完全なcoupled-region transferと係数 \(1/12\);
- MAJOR-04：自己完結bundle。

したがって最終漸近式は引き続き `NOT CLOSED` とする。

---

## 1. 使用する既存分解

\[
B_\beta(X):=\sum_{n\le X}\beta(n)
\]

とする。Stage12-N1-2m〜2pの一変数評価から

\[
B_\beta(X)=c_\beta X+O(XE(X))
\]

が得られているため、有限区間 \(1\le X<3\) を定数調整へ吸収すれば

\[
B_\beta(X)\ll X
\qquad(X\ge1)
\]

を使用できる。

coprime cross correctionを

\[
C(s_1,s_2)
=
\sum_{a,b\ge1}\frac{c(a,b)}{a^{s_1}b^{s_2}}
\]

とし、任意の固定 \(\delta\in(0,1/4)\) に対して

\[
M_\delta
:=
\sum_{a,b\ge1}
\frac{|c(a,b)|}{(ab)^{1/2+\delta}}
<\infty
\]

を用いる。

長方形和は

\[
S(R,S)
:=
\sum_{r\le R}\sum_{s\le S}
\beta(r)\beta(s)1_{(r,s)=1}
\]

であり、Dirichlet畳み込みにより

\[
S(R,S)
=
\sum_{a\le R}\sum_{b\le S}
 c(a,b)B_\beta(R/a)B_\beta(S/b)
\]

と書ける。

---

## 2. 修正版一様長方形補題

### 補題 3a.1

任意の固定

\[
0<\varepsilon<\frac18
\]

に対し、\(R,S\ge2\) で一様に

\[
\boxed{
S(R,S)
=
\mathfrak C RS
+O_\varepsilon\!\left(
RS\{E_*(R^{1/2})+E_*(S^{1/2})\}
+R^{3/4+\varepsilon}S
+RS^{3/4+\varepsilon}
\right)
}
\]

が成り立つ。ここで

\[
\mathfrak C=c_\beta^2C(1,1),
\qquad
E_*(X)=\sup_{Y\ge X}E(Y).
\]

暗黙定数は \(\varepsilon\) と \(M_{2\varepsilon}\) に依存するが、\(R,S\) には依存しない。

### 証明

\[
A=R^{1/2},
\qquad
D=S^{1/2}
\]

と置き、係数領域を

\[
\mathcal R_{00}:a\le A,b\le D,
\quad
\mathcal R_{10}:a>A,b\le D,
\]

\[
\mathcal R_{01}:a\le A,b>D,
\quad
\mathcal R_{11}:a>A,b>D
\]

へ分割する。

#### 小係数領域

\(\mathcal R_{00}\) では、Stage12-N1-2p §3.1と同じ一変数展開により

\[
O_\varepsilon\!\left(
RS\{E_*(R^{1/2})+E_*(S^{1/2})\}
\right)
\]

を得る。主項を完全和 \(C(1,1)\) へ延長した差は、以下の大係数尾部へ含める。

#### \(a\) 大・\(b\) 小

\(B_\beta(X)\ll X\) を使うと

\[
\sum_{\mathcal R_{10}}
|c(a,b)|B_\beta(R/a)B_\beta(S/b)
\ll
RS
\sum_{\mathcal R_{10}}
\frac{|c(a,b)|}{ab}.
\]

\(a>R^{1/2}\) かつ \(\delta=2\varepsilon\) とすると

\[
\frac1a
=
a^{-1/2+2\varepsilon}a^{-1/2-2\varepsilon}
\le
R^{-1/4+\varepsilon}a^{-1/2-2\varepsilon}.
\]

また \(0<2\varepsilon<1/4\) なので、\(b\ge1\) に対して

\[
\frac1b\le b^{-1/2-2\varepsilon}.
\]

従って

\[
RS
\sum_{\mathcal R_{10}}
\frac{|c(a,b)|}{ab}
\le
R^{3/4+\varepsilon}S
M_{2\varepsilon}.
\]

完全主項の尾

\[
RS
\sum_{a>A,b\le D}
\frac{|c(a,b)|}{ab}
\]

にも同じ評価を適用できる。

#### \(a\) 小・\(b\) 大

対称性により

\[
\mathcal R_{01}
\ll_\varepsilon
RS^{3/4+\varepsilon},
\]

主項尾部も同じ上界に入る。

#### 両係数が大きい領域

\(\mathcal R_{11}\) は \(a>A\) または \(b>D\) のいずれの尾部評価にも含められるため

\[
\mathcal R_{11}
\ll_\varepsilon
R^{3/4+\varepsilon}S
+RS^{3/4+\varepsilon}.
\]

四領域を合成して補題を得る。\(\square\)

---

## 3. 旧指数が使えないことの固定

旧Stage12-N1-2pの操作は

\[
R^{3/4+\delta/2}S(\log 2R)(\log 2S)
\stackrel{\rm invalid}{\ll}
R^{1/2+\delta}S
\]

であった。

本修復では、そもそも

\[
B_\beta(X)\ll X
\]

を使って不要な対数因子を除き、そのうえで得られる正しいべき

\[
R^{3/4+\varepsilon}S
\]

を保持する。指数をこれより小さくする主張はしない。

以後、Stage12-N1-2p §3.2〜§3.5および旧Final §4の

\[
R^{1/2+\delta}S+RS^{1/2+\delta}
\]

は引用禁止とし、本稿の補題3a.1で置き換える。

---

## 4. boxwise kernelとの適合性

MAJOR-03の完全な結合領域移送は別稿で行う。ただし、修正後の弱い指数が予定されるkernel適用後にも低次であることは、次の抽象形で確認できる。

長方形box

\[
\mathcal B(R,S)=[R,2R]\times[S,2S]
\]

上のkernel \(K_B(r,s)\) に対し、二変数部分和分で現れる境界値・一次変分・混合変分をまとめたノルムを

\[
\|K_B\|_{\rm PS,\mathcal B}
\]

と書く。

後続のcoupled-region transferで証明すべきkernel評価を

\[
\|K_B\|_{\rm PS,\mathcal B}
\ll
\frac{B(\log B)^C}{R^2+S^2}
\]

とする。このとき補題3a.1のべき誤差がboxへ与える寄与は

\[
\ll
\frac{B(\log B)^C}{R^2+S^2}
\left(
R^{3/4+\varepsilon}S
+RS^{3/4+\varepsilon}
\right).
\]

\[
m=\min(R,S)
\]

と置く。例えば \(R\le S\) なら

\[
\frac{R^{3/4+\varepsilon}S}{R^2+S^2}
\le
\frac{R^{3/4+\varepsilon}}{S}
\le
R^{-1/4+\varepsilon},
\]

また

\[
\frac{RS^{3/4+\varepsilon}}{R^2+S^2}
\le
\frac{R}{S^{5/4-\varepsilon}}
\le
R^{-1/4+\varepsilon}.
\]

対称な場合も同様なので

\[
\frac{
R^{3/4+\varepsilon}S
+RS^{3/4+\varepsilon}
}{R^2+S^2}
\ll
m^{-1/4+\varepsilon}.
\]

retained regionの下限

\[
m
\ge
\exp\!\left\{
\frac12(\log B)^{1/4}
\right\}
\]

を使えば、\(\varepsilon<1/8\) に対し

\[
m^{-1/4+\varepsilon}
\le
\exp\{-c_\varepsilon(\log B)^{1/4}\}
\]

となる。従って、kernel評価がMAJOR-03で確立された後には、各boxの修正版べき誤差は任意の固定 \(A>0\) に対して

\[
o\!\left(B(\log B)^{-A}\right)
\]

となり、多項対数個のboxを合計しても低次である。

重要なのは、この節は **修正版指数の適合性** を示すだけであり、kernelノルムそのもの、正確な主定数、境界項、parity/orientation factorを証明したものではないことである。それらはMAJOR-03として未解決のまま残す。

---

## 5. 修復判定

独立監査R01のMAJOR-01に対して、次を実施した。

1. 不成立な指数強化を撤回した。
2. \(B_\beta(X)\ll X\) を使い、大係数領域を正しい指数で再評価した。
3. 一様長方形補題を
   \[
   R^{3/4+\varepsilon}S+RS^{3/4+\varepsilon}
   \]
   型へ修正した。
4. 後続kernelの標準的な部分和分ノルムのもとで、修正版誤差がretained regionで超対数的に小さいことを確認した。
5. MAJOR-03のkernel導出そのものとは明確に分離した。

従って状態は

```text
MAJOR_01_RECTANGULAR_ERROR_EXPONENT=CLOSED_BY_STAGE12_N1_3A
MAJOR_02_FIXED_CIRCLE_REMAINDER=OPEN
MAJOR_03_COUPLED_REGION_TRANSFER=OPEN
MAJOR_04_REVIEW_SELF_CONTAINMENT=OPEN
THEOREM_STATUS=REPAIRABLE_NOT_CLOSED
NEXT_TASK=STAGE12_N1_3B_FIXED_CIRCLE_REMAINDER
```

とする。
