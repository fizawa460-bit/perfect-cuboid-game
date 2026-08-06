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
