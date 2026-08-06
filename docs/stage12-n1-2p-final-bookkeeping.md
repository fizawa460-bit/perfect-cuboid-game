# Stage12-N1-2p：Selberg–Delange参照固定と長方形誤差の完全bookkeeping

## 結論

Stage12-N1-2oで残した二つのMINORを閉じる。

1. 一変数 Selberg–Delange の使用版・定理番号を固定する。
2. cross correction から一様長方形誤差を得る際の係数領域分割を完全に書き下す。

本段階の分類は

```text
A_FINAL_BOOKKEEPING_WRITTEN_INDEPENDENT_REVIEW_REQUIRED
```

とする。最終ルートは

```text
2j -> 2k -> 2l -> 2m -> 2n -> 2o -> 2p
```

であり、主張範囲は定義済み primitive oriented count に限る。

---

## 1. 使用する一変数定理の固定

参照版を次に固定する。

> Gérald Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*, Third Edition, Graduate Studies in Mathematics 163, American Mathematical Society, 2015, Chapter II.5, Theorem II.5.2（Selberg–Delange method）。

本系列では、その `z=1` 特殊形を使う。すなわち、

\[
F(s)=\zeta(s)H(s)
\]

で、`H` が de la Vallée Poussin 型 zero-free region の必要部分へ正則接続し、同領域で多項式増大度を持ち、`H(1)\ne0` なら、ある `c>0` に対して

\[
\sum_{n\le x}f(n)=H(1)x+O\!\left(xE(x)\right),
\]

\[
E(x)=\exp\{-c(\log x)^{3/5}(\log\log x)^{-1/5}\}
\]

の形を用いる。

Stage12-N1-2o §1で

\[
B_\beta(s)=\zeta(s)H(s),\qquad H(s)=L(s,\chi_4)J(s)
\]

と分解し、`J` は `Re s>1/2+epsilon` で正則・非零、絶対収束部分は垂直方向に一様有界であることを確認した。`L(s,chi_4)` は `s=1` 近傍で正則非零であり、標準 zero-free region と多項式増大度を持つ。したがって定理の解析条件は満たされる。

また

\[
0\le\beta(n)\le2^{\omega(n)}\le\tau(n)
\]

なので、係数成長条件も満たされる。よって

\[
B_\beta(X):=\sum_{n\le X}\beta(n)
=c_\beta X+O(XE(X))
\]

を、`X>=3` で暗黙定数が `X` に依存しない形で使用する。`1<=X<3` は定数調整で同じ上界に吸収する。

---

## 2. cross correction の係数ノルム

Stage12-N1-2m〜2oの分解

\[
F(s_1,s_2)=B_\beta(s_1)B_\beta(s_2)C(s_1,s_2),
\]

\[
C(s_1,s_2)=\sum_{a,b\ge1}\frac{c(a,b)}{a^{s_1}b^{s_2}}
\]

を用いる。任意の固定 `delta in (0,1/4)` に対し

\[
M_\delta:=\sum_{a,b\ge1}\frac{|c(a,b)|}{(ab)^{1/2+\delta}}<\infty.
\]

また、絶対収束点 `(1,1)` では

\[
C(1,1)=\sum_{a,b\ge1}\frac{c(a,b)}{ab}.
\]

以下、暗黙定数は `delta` と `M_delta` のみに依存し、`R,S` には依存しない。

---

## 3. 一様長方形補題

\[
S(R,S):=\sum_{r\le R}\sum_{s\le S}
\beta(r)\beta(s)1_{(r,s)=1}.
\]

Dirichlet畳み込みにより

\[
S(R,S)=\sum_{a\le R}\sum_{b\le S}c(a,b)
B_\beta(R/a)B_\beta(S/b).
\]

`A=R^{1/2}`, `D=S^{1/2}` と置き、係数領域を

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

に分ける。

### 3.1 小係数領域 `R_00`

`a<=A`, `b<=D` なら `R/a>=R^{1/2}`, `S/b>=S^{1/2}`。単調包絡線

\[
E_*(X):=\sup_{Y\ge X}E(Y)
\]

を用いると

\[
B_\beta(R/a)=c_\beta R/a
+O\bigl((R/a)E_*(R^{1/2})\bigr),
\]

\[
B_\beta(S/b)=c_\beta S/b
+O\bigl((S/b)E_*(S^{1/2})\bigr).
\]

積を展開し、

\[
\sum_{\mathcal R_{00}}\frac{|c(a,b)|}{ab}
\le M_\delta
\]

を使えば、誤差は

\[
O_\delta\!\left(
RS\{E_*(R^{1/2})+E_*(S^{1/2})
+E_*(R^{1/2})E_*(S^{1/2})\}
\right).
\]

最後の積項は前二項へ吸収できる。

小係数領域の主項は

\[
c_\beta^2RS
\sum_{a\le A,b\le D}\frac{c(a,b)}{ab}.
\]

完全Euler定数との差は尾部評価へ移す。

### 3.2 `a` 大・`b` 小の領域 `R_10`

自明評価

\[
B_\beta(X)\ll X\log(2X)
\]

を両変数へ用いる。`a>A` では

\[
a^{-1}=a^{-1/2+\delta}a^{-1/2-\delta}
\le R^{-1/4+\delta/2}a^{-1/2-\delta}.
\]

したがって

\[
\sum_{\mathcal R_{10}}
|c(a,b)|\frac{R}{a}\frac{S}{b}
\log(2R/a)\log(2S/b)
\]

\[
\ll_\delta
R^{3/4+\delta/2}S\,(\log 2R)(\log 2S)M_\delta.
\]

任意の固定 `delta>0` を小さく取り直し、対数因子を小べきへ吸収すると

\[
\mathcal R_{10}\ll_\delta R^{1/2+\delta}S.
\]

同じ評価は、完全主項の尾

\[
RS\sum_{a>A,b\le D}\frac{|c(a,b)|}{ab}
\]

にも適用できる。

### 3.3 `a` 小・`b` 大の領域 `R_01`

対称性により

\[
\mathcal R_{01}\ll_\delta RS^{1/2+\delta}.
\]

主項尾部も同じ上界に入る。

### 3.4 両係数が大きい領域 `R_11`

上の二つのどちらか一方の尾部評価だけでも

\[
\mathcal R_{11}
\ll_\delta
R^{1/2+\delta}S+RS^{1/2+\delta}
\]

を得る。より対称に評価すれば積型のさらに小さい上界も得られるが、最終用途には不要である。

### 3.5 合成

以上より

\[
\boxed{
S(R,S)=\mathfrak C RS
+O_\delta\!\left(
RS\{E_*(R^{1/2})+E_*(S^{1/2})\}
+R^{1/2+\delta}S
+RS^{1/2+\delta}
\right)
}
\]

が成り立つ。ここで

\[
\mathfrak C=c_\beta^2C(1,1).
\]

暗黙定数は `R,S` に一様である。

---

## 4. retained regionでの総誤差

Stage12-N1-2n〜2oの retained regionでは

\[
\min(R,S)\ge
\exp\{\tfrac12(\log B)^{1/4}\},
\qquad
R,S\ll B^{1/2}.
\]

したがってzero-free-region誤差は任意の固定対数冪より小さく、べき誤差は

\[
R^{1/2+\delta}S+RS^{1/2+\delta}
\ll B^{3/4+\delta/2}.
\]

固定 `delta<1/2` なら、dyadic boxの多項対数個の総和を取っても

\[
o(B(\log B)^3)
\]

である。

shallow・arc・diagonal・floor・parityについては2oの安全側評価を使用する：

\[
O(BL^{3/2+o(1)}),\quad
O(BL^{2+o(1)}),\quad
O(BL^{1+o(1)}),
\]

はいずれも `o(BL^3)` である。

---

## 5. 状態

ClaudeのR03+R04独立レビューで残った

- Selberg–Delange参照の版・定理番号
- 長方形補題の完全な係数領域bookkeeping

を本文へ固定した。

従って現在の状態は

```text
PROVISIONALLY_CLOSED_FINAL_BOOKKEEPING_WRITTEN_REVIEW_PENDING
```

とする。独立レビューで新たなFATAL／MAJORが出ず、本節の参照番号と各不等式が確認されれば、Stage12-N1-2系列を `CLOSED` へ更新できる。

候補結論は変更しない：

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3.
\]
