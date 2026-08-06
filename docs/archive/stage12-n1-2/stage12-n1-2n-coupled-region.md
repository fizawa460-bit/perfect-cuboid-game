# Stage12-N1-2n：radial／height結合領域・境界・誤差経路監査

## 結論

Stage12-N1-2mで得た二法長方形和の因子分解を、primitive-first の結合領域へ移送する。

判定は

```text
A_FINAL_ROUTE_REPAIRED_AT_STANDARD_ONE_VARIABLE_THEOREM_LEVEL_REVIEW_REQUIRED
```

とする。

- retained region は対数dyadic長方形の有限重なり和へ分解できる。
- 一変数 Selberg–Delange の一様誤差と、絶対収束する coprime cross correction を畳み込むことで、各長方形に一様な二法誤差を得る。
- 二変数 Abel／Stieltjes 部分和分により、radial weight と height length を含む結合領域へ主項を移送できる。
- shallow boxes と対角・円弧境界の寄与は `o(B(log B)^3)` である。
- Stage12-N1-2h〜2i の Poisson・Ramanujan・指数対ルートは、最終 primitive-first 証明では使用しない。歴史的な障害診断および代替ルート監査として残す。

従って、AI敵対レビューで共通指摘された

1. de la Bretèche の未検証 P2/P3
2. 2h〜2i と 2j〜2k の接続不明
3. 結合領域への移送不足

は、de la Bretèche を使わない一変数ルートで修復できる。

ただし、独立再レビュー前に `CLOSED` へ戻すのではなく、上記分類で停止する。

---

## 1. primitive-first 主項の形

Stage12-N1-2j〜2kから、固定された coprime pair `(r,s)` の height 部分和は

\[
\sum_{m\le X}A_{r,s}(m)
=
\gamma(rs)X-1+R_{r,s}(X),
\]

\[
\gamma(n)=\frac1\pi\sum_{d\mid n}\beta(d).
\]

odd–odd と opposite-parity の二場合は、height 上限の係数が異なるだけで、いずれも概略

\[
B\sum_{r<s\atop(r,s)=1}
\frac{\gamma(rs)}{r^2+s^2}
\]

型の主項へ帰着する。parity の局所質量は Stage12-N1-2f, 2j の 2-adic bookkeeping と一致する。

`(r,s)=1` なので divisor 展開は二法へ分離し、Stage12-N1-2m の

\[
f(b,c)=\beta(b)\beta(c)1_{(b,c)=1}
\]

に対する長方形和を使用できる。

---

## 2. 一様な二法長方形和

一変数級数を

\[
B_\beta(s)=\zeta(s)L(s,\chi_4)J(s)
\]

とし、`J` は `Re s>1/2+epsilon` で正則とする。標準 zero-free region 版の一変数 Selberg–Delange から

\[
\sum_{n\le x}\beta(n)
=c_\beta x+O(xE(x)),
\]

\[
E(x)=\exp\{-c(\log x)^{3/5}(\log\log x)^{-1/5}\}
\]

型を使用する。

Stage12-N1-2mの cross correction を

\[
C(s_1,s_2)=\sum_{a,b\ge1}\frac{c(a,b)}{a^{s_1}b^{s_2}}
\]

と展開する。`Re(s1+s2)>1` で絶対収束するため、任意の固定 `delta>0` に対し

\[
\sum_{a,b}\frac{|c(a,b)|}{(ab)^{1/2+\delta}}<\infty.
\]

従って長方形和

\[
S(R,S)=\sum_{r\le R,s\le S}
\beta(r)\beta(s)1_{(r,s)=1}
\]

は、cross coefficients を先に畳み込んで二回の一変数部分和を適用することで

\[
S(R,S)=\mathfrak C RS
+O\bigl(RS(E(R)+E(S))\bigr)
+O\bigl(R^{1/2+\delta}S+RS^{1/2+\delta}\bigr)
\]

となる。暗黙定数は retained region 内で `R,S` に依存しない。

最短辺が

\[
S_0=\exp\bigl(\tfrac12(\log B)^{1/4}\bigr)
\]

以上なら、右辺の相対誤差は任意の固定対数冪より小さい。

---

## 3. 結合領域への移送

対数変数

\[
y=\log r,\qquad z=\log s,\qquad L=\log B
\]

を用いると、height の主項長さは区分的滑らかな重み

\[
\Phi_L(y,z)=\bigl(L-2\max(y,z)\bigr)_+
\]

で表される。

領域を固定比の対数dyadic boxesへ分割する。各box上で

- `r^2+s^2` は box scale と定数倍で比較可能
- `Phi_L` の全変動は `O(1)`
- 円弧境界を横切るboxは一層だけ

である。

二変数 Abel／Stieltjes 部分和分を各boxへ適用すると、長方形主項の積分は

\[
\int_{y,z\ge0\atop2\max(y,z)<L}
(L-2\max(y,z))\,dy\,dz
=\frac{L^3}{12}
\]

となる。

Stage12-N1-2kで確定した局所定数

\[
\eta=\pi\kappa
\]

と parity／orientation factor を組み合わせると、先頭候補は従来通り

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3.
\]

---

## 4. 境界誤差

### 4.1 shallow boxes

\[
L-2\max(y,z)\le\tau L,
\qquad \tau=L^{-3/4}
\]

の対数質量比は

\[
3\tau^2-2\tau^3.
\]

従って寄与は

\[
O(BL^{3/2+o(1)})=o(BL^3).
\]

### 4.2 円弧・対角境界

`r=s` は oriented domain では境界であり、幅1の格子帯は一変数少ないため

\[
O(BL^{2+o(1)})
\]

以下になる。円弧境界を横切るdyadic boxesも、boxの一辺分の損失と一様長方形誤差で同じ次数以下になる。

### 4.3 endpoint と floor

height 上限の floor を外す誤差は各 `(r,s)` につき `O(1)`。重み付き pair 数の標準 divisor boundを用いると総和は

\[
O(B^{1/2+o(1)}L^2)
\]

で、主項より小さい。

---

## 5. 2h〜2iの最終的な位置づけ

最終ルートは

```text
2j primitive-first exact reindexing
 -> 2k fixed-circle height remainder
 -> 2l de la Bretèche direct application rejected
 -> 2m one-variable beta factorization
 -> 2n dyadic rectangle + Abel transfer
```

である。

従って2h〜2iの

- 二次元Poisson
- Ramanujan Fourier coefficients
- nonlinear reciprocal phase
- exponent-pair core/wing budget

は最終漸近式の証明入力ではない。

これらは、raw三法ルートを続けた場合の適合性監査、および primitive-first へ切り替える動機を記録する歴史的段階である。2k本文の「2iの評価をそのまま移植できる」という記述は撤回し、2m〜2nの反復Selberg–Delange移送へ置換する。

---

## 6. 残るレビュー項目

数学的に新しい解析入力として残るものはないが、次の文書化確認は必要である。

1. 一変数 Selberg–Delange の使用版と誤差関数を定理番号付きで固定する。
2. cross correction係数の weighted absolute convergenceから長方形誤差を導く補題を出版形式で書く。
3. parity classごとの前置因子を一つの表に統合する。
4. 2kの旧 `CLOSED` 文言と2i移植文言を、2l〜2nの結論に合わせて更新する。
5. 修正版バンドルを再発行し、Claude/Grok/DeepSeek等でRound 2敵対レビューを行う。

したがって現状は

```text
REPAIRED_PROOF_CHAIN_PENDING_ROUND2_ADVERSARIAL_REVIEW
```

であり、独立レビューで新しいMAJOR/FATALが出なければ `CLOSED` に戻せる候補である。
