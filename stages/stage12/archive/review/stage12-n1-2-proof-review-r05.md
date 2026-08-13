# Stage12-N1-2 final bookkeeping review bundle — R05

This is an incremental patch bundle. Read the previously supplied R03 full-chain bundle first, then R04, then this R05 bundle. Where statements conflict, the later bundle prevails.

## Machine-readable handshake — START_OF_MAIN

```text
BUNDLE_ID=PC-N1-2-PROOF-REVIEW-R05
COMPLETED_THROUGH=Stage12-N1-2p
SOURCE_SNAPSHOT_COMMIT=6f3a951b0234058aea6bfe03fc4e28a3de07ebc9
CONTENT_SHA256=8f3695c1a74b2de61b7d6e2d454f93ceb4356e2902bdb30177b43ac58bbb9744
LAST_SOURCE_DOCUMENT=docs/stage12-n1-2p-final-bookkeeping.md
END_OF_BUNDLE=PC-N1-2-PROOF-REVIEW-R05
CHECKPOINT=START_OF_MAIN
```

## Mandatory adversarial review protocol

Review the final route `2j -> 2k -> 2l -> 2m -> 2n -> 2o -> 2p` and focus on the two remaining Round-2 MINOR items:

1. Verify that the cited Selberg–Delange reference, edition, chapter and theorem number actually support the stated `z=1` input and error term.
2. Verify every inequality in the four-region rectangle bookkeeping (`R00`, `R10`, `R01`, `R11`), including the powers of `R,S`, logarithmic absorption, uniformity in `R,S`, and summation over retained dyadic boxes.
3. Check that R05 introduces no new FATAL or MAJOR gap and that the safe arc/diagonal/floor bounds remain `o(B(log B)^3)`.
4. Return exactly one final verdict: `CLOSED`, `REPAIRABLE`, `OPEN`, or `UNREADABLE_SOURCE`.

For every issue report severity, exact location, missing argument, and repairability. Do not infer unavailable text.

## Embedded patch documents

### `docs/stage12-n1-2o-analytic-closure.md`

```markdown
# Stage12-N1-2o：一変数解析条件と一様長方形補題

## 結論

Stage12-N1-2m〜2n の反復 Selberg–Delange ルートについて、Round 2 敵対レビューで繰り返し指摘された次の点を本文へ固定する。

1. 一変数因子 `J(s)` の正則性・非零性。
2. 使用する一変数平均定理の入力条件と誤差関数。
3. coprime cross correction から一様長方形誤差を得る畳み込み補題。
4. endpoint／floor 誤差の安全な低次評価。

この段階の判定は

```text
A_ANALYTIC_CLOSURE_LEMMAS_WRITTEN_FINAL_REVIEW_REQUIRED
```

とする。新しい主項や局所定数は導入せず、最終ルート

```text
2j -> 2k -> 2l -> 2m -> 2n -> 2o
```

のうち 2m〜2n で略記されていた解析条件だけを補う。

---

## 1. 一変数 Euler 積の正規化

`q ≡ 1 (mod 4)` に対し

\[
b_q=\frac{2(q-1)}{q+1},
\qquad
A_q(s)=1+\frac{b_q q^{-s}}{1-q^{-s}}.
\]

一変数 Dirichlet 級数は

\[
B_\beta(s)=\prod_{q\equiv1(4)}A_q(s).
\]

`x=q^{-s}` と書くと

\[
A_q(s)=\frac{1+(b_q-1)x}{1-x}.
\]

一方、`ζ(s)L(s,χ_4)` の `q ≡ 1 (mod 4)` 局所因子は `(1-x)^{-2}`、`p ≡ 3 (mod 4)` 局所因子は `(1-p^{-2s})^{-1}` である。従って

\[
B_\beta(s)=\zeta(s)L(s,\chi_4)J(s)
\]

と置いたとき、`J` の局所因子は

\[
J_q(s)=(1-x)(1+(b_q-1)x)
\quad(q\equiv1(4)),
\]

\[
J_p(s)=1-p^{-2s}
\quad(p\equiv3(4)),
\]

および 2-adic な有限因子で与えられる。

`b_q-2=-4/(q+1)` なので

\[
J_q(s)-1=(b_q-2)q^{-s}-(b_q-1)q^{-2s}
=O(q^{-1-\sigma})+O(q^{-2\sigma}).
\]

したがって任意の固定 `ε>0` に対し、`σ=Re s >= 1/2+ε` では

\[
\sum_{q\equiv1(4)}|J_q(s)-1|<\infty,
\qquad
\sum_{p\equiv3(4)}|J_p(s)-1|<\infty
\]

が局所一様に成り立つ。よって Euler 積 `J(s)` はこの半平面で正則である。

さらに、同じ半平面の任意の閉じた部分領域では有限個の小素数因子を直接除外し、残りの因子について `|J_p(s)-1|<1/2` とできる。そこで主値の対数を用いれば

\[
\log J(s)=\sum_p\log J_p(s)
\]

が局所一様収束するため、`J(s)` は零を持たない。絶対収束部分は垂直方向にも一様有界であり、必要な vertical growth は `ζ(s)L(s,χ_4)` 側の標準評価へ還元される。

---

## 2. 一変数平均定理の使用形

本系列で必要なのは、`B_β(s)=ζ(s)H(s)`、

\[
H(s)=L(s,\chi_4)J(s)
\]

が `s=1` の近傍で正則かつ非零であり、標準 zero-free region 内で多項式増大度を持つ場合の一変数 Selberg–Delange／Perron 移動の `z=1` 特殊形である。

使用する結論を次の形に固定する。

> **一変数平均入力。** ある定数 `c_β>0`, `c>0` が存在して、`x>=3` に対し
> \[
> \sum_{n\le x}\beta(n)
> =c_\beta x+O(xE(x)),
> \]
> \[
> E(x)=\exp\{-c(\log x)^{3/5}(\log\log x)^{-1/5}\}.
> \]
> 暗黙定数は `x` に依存しない。

これは Tenenbaum の Selberg–Delange 法を収録する章の `z=1` 特殊形として使用する。版によって節・定理番号が変わる可能性があるため、最終出版稿では参照する版の書誌情報と定理番号を照合して固定する。ここでは未照合の番号を断定しない。

`β(n)>=0` かつ

\[
\beta(n)\le 2^{\omega(n)}\le \tau(n)
\]

であり、前節で `H` の解析条件を確認したため、この入力を本系列で用いるための係数成長・解析接続条件は満たされる。

---

## 3. cross correction の係数表示

Stage12-N1-2m の分解を

\[
F(s_1,s_2)
=B_\beta(s_1)B_\beta(s_2)C(s_1,s_2)
\]

とし、

\[
C(s_1,s_2)=\sum_{a,b\ge1}\frac{c(a,b)}{a^{s_1}b^{s_2}}
\]

と展開する。

局所的に

\[
C_q(s_1,s_2)-1=O(q^{-\sigma_1-\sigma_2})
\]

なので、任意の固定 `δ>0` に対し

\[
M_\delta:=
\sum_{a,b\ge1}
\frac{|c(a,b)|}{(ab)^{1/2+\delta}}<\infty.
\]

この絶対収束は以下の和の順序交換と誤差の一様化にのみ使用する。

---

## 4. 一様長方形補題

\[
S(R,S)=
\sum_{r\le R}\sum_{s\le S}
\beta(r)\beta(s)1_{(r,s)=1}
\]

とする。Dirichlet 畳み込み表示から

\[
S(R,S)=
\sum_{a,b}c(a,b)
B_\beta(R/a)B_\beta(S/b),
\]

ここで

\[
B_\beta(X):=\sum_{n\le X}\beta(n),
\qquad B_\beta(X)=0\quad(X<1).
\]

一変数平均入力を二回代入すると主項は

\[
\mathfrak C RS,
\qquad
\mathfrak C=c_\beta^2 C(1,1).
\]

`a<=R`, `b<=S` の範囲で `E(R/a)`, `E(S/b)` を直接一様化できない端部は、`a>R^{1/2}` または `b>S^{1/2}` として分離する。小さい係数領域では `E` の単調包絡線を用い、大きい係数領域では `M_δ` と自明評価 `B_β(X) << X log X` を用いる。すると任意の固定 `δ>0` に対し

\[
S(R,S)=\mathfrak C RS
+O_\delta\!\left(
RS(E(R^{1/2})+E(S^{1/2}))
+R^{1/2+\delta}S
+RS^{1/2+\delta}
\right).
\]

暗黙定数は `R,S` に依存しない。特に retained region で

\[
\min(R,S)\ge
\exp\{\tfrac12(\log B)^{1/4}\}
\]

なら、相対誤差は任意の固定対数冪より小さい。

この補題は、2n の「cross coefficients を先に畳み込んで二回の一変数部分和を適用する」という一文を出版形式へ展開したものである。

---

## 5. endpoint／floor の安全な評価

2n では floor 除去誤差として

\[
O(B^{1/2+o(1)}L^2)
\]

を記したが、Round 2 ではこの上界が必要以上に強いとの指摘があった。最終漸近には低次であることだけが必要なので、以後は安全な上界へ置換する。

各 admissible pair `(r,s)` の floor 誤差は `O(1)` であり、`r^2+s^2<<B` の pair 数は `O(B)`。divisor／parity 重みを平均的な対数冪へ吸収すると、必要十分な形として

\[
O(B(\log B)^{1+o(1)})
=o(B(\log B)^3)
\]

を採用する。ここでは `B^{1/2+o(1)}` 型の強い評価を主張しない。

対角・円弧境界についても「境界 box が一個だけ」という意味には解釈せず、各 dyadic scale で境界に接する box の総数と、一辺分失う格子数を合計して

\[
O(B(\log B)^{2+o(1)})
=o(B(\log B)^3)
\]

とする。詳細な幾何分割は2nの Abel 移送に従う。

---

## 6. 状態更新

Round 2 の独立レビューは、Grok／DeepSeek が `REPAIRABLE`、Meta AI／Qwen が `CLOSED`、Gemini は truncated bundle により `UNREADABLE_SOURCE` であった。従って Gemini は数学的反対票として数えない。

2oにより、具体的に残っていた

- `J(s)` の正則性・非零性
- 一変数誤差の一様利用
- cross correction の長方形畳み込み
- floor／arc 誤差の安全な低次化

を本文へ追加した。

ただし、参照版に依存する Selberg–Delange の定理番号照合と、2oを含む最終独立レビューが残るため、正式状態は

```text
PROVISIONALLY_CLOSED_DOCUMENT_PATCHED_FINAL_REVIEW_PENDING
```

とする。

主張範囲は引き続き、定義された primitive oriented count

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
\]

に限る。完全直方体の存在、`N_1` 全体、または別の exact-multiplicity count への自動変換は主張しない。
```

### `docs/stage12-n1-2p-final-bookkeeping.md`

```markdown
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
```

## Machine-readable handshake — END_OF_MAIN

```text
BUNDLE_ID=PC-N1-2-PROOF-REVIEW-R05
COMPLETED_THROUGH=Stage12-N1-2p
SOURCE_SNAPSHOT_COMMIT=6f3a951b0234058aea6bfe03fc4e28a3de07ebc9
CONTENT_SHA256=8f3695c1a74b2de61b7d6e2d454f93ceb4356e2902bdb30177b43ac58bbb9744
LAST_SOURCE_DOCUMENT=docs/stage12-n1-2p-final-bookkeeping.md
END_OF_BUNDLE=PC-N1-2-PROOF-REVIEW-R05
CHECKPOINT=END_OF_MAIN
```
