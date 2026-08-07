# Stage12-N1-2 final review bundle R04

BUNDLE_ID=PC-N1-2-PROOF-REVIEW-R04
COMPLETED_THROUGH=Stage12-N1-2o
SOURCE_SNAPSHOT_COMMIT=8b5622c9aaf3af718f2ee493383b9c084e2333ef
CONTENT_SHA256=b38406a45e88286d8c5df8dacfba1e00d4b8cb1b01fe7bf4fbaab34378dc8ac9
LAST_SOURCE_DOCUMENT=docs/stage12-n1-2o-analytic-closure.md
SOURCE_COUNT=3
CREATED_UTC=2026-08-06T12:36:40+00:00
END_OF_BUNDLE=PC-N1-2-PROOF-REVIEW-R04

CHECKPOINT=START_OF_MAIN

# Review instructions

Conduct an adversarial final review of the repair chain through Stage12-N1-2o.
Do not infer omitted text. Verify the following points explicitly:

1. The Euler-product proof that J(s) is regular and nonvanishing on Re(s)>1/2+epsilon.
2. Whether the stated one-variable Selberg-Delange/Perron input is sufficient and used uniformly.
3. Whether weighted absolute convergence of the coprime cross correction yields the stated uniform rectangle estimate.
4. Whether the dyadic/Abel transfer, arc, diagonal, parity and floor errors are o(B(log B)^3).
5. Whether the conclusion applies only to the defined primitive oriented count C_prim(B).

Classify every issue as FATAL, MAJOR, MINOR or CLARIFICATION and finish with exactly one verdict:
CLOSED, REPAIRABLE or FATAL.

---

## EMBEDDED_SOURCE_1
PATH=docs/stage12-n1-2m-iterated-selberg-delange.md
FILE_SHA256=34e326143244c4be5dc49438ab995a776c0ef96d514786adf4bbc2077119f4e4

# Stage12-N1-2m：反復Selberg–Delangeとcoprime補正の監査

## 結論

Stage12-N1-2lで未検証と判定した de la Bretèche の多変数定理を避け、二法重み \(\beta\) を一変数Dirichlet級数とcoprime補正へ分解する。

判定は

```text
A_ITERATED_SELBERG_DELANGE_MAIN_TERM_FACTORIZATION_CLOSED_REGION_REMAINDER_PENDING
```

とする。

- 一変数 \(\beta\) 級数は \(s=1\) で単純極を持つ。
- 二変数の互いに素条件は、二つの一変数因子と、\(\Re(s_1+s_2)>1\) で絶対収束するcross correctionへ厳密分解できる。
- 従って長方形領域または滑らかな積重み上では、反復Selberg–Delangeにより主項と局所定数を得られる。
- ただし最終的な結合領域 \(h(r^2+s^2)\le 2B\) へ戻す際のpartial summation、境界層、誤差の一様積分をこの段階だけでは完了していない。

したがって、2lで見つかった「多変数定理の仮定未確認」は回避できるが、最終漸近式を再び CLOSED とするには、次段階で結合領域への移送誤差を閉じる必要がある。

---

## 1. 一変数 \(\beta\) Dirichlet級数

\[
\beta(p^j)=\frac{2(p-1)}{p+1}
\quad(p\equiv1\pmod4,\ j\ge1),
\]

それ以外を0とする。一変数級数

\[
B_\beta(s)=\sum_{n\ge1}\frac{\beta(n)}{n^s}
\]

の局所因子は、\(q\equiv1\pmod4\) に対して

\[
1+\frac{b_q q^{-s}}{1-q^{-s}},
\qquad b_q=\frac{2(q-1)}{q+1}=2+O(q^{-1}).
\]

従って

\[
\log B_\beta(s)
=2\sum_{q\equiv1(4)}q^{-s}+O(1)
=\log\frac1{s-1}+O(1),
\]

となり、\(s=1\) で単純極を持つ。

より具体的には

\[
B_\beta(s)=\zeta(s)L(s,\chi_4)\,J(s),
\]

と書け、\(J(s)\) は少なくとも \(\Re s>1/2+\varepsilon\) の固定近傍で正則かつ非零になる。局所一次項を \(\zeta L\) で除去した残りが \(1+O(q^{-2\sigma})\) になるためである。

従って通常の一変数Selberg–Delangeにより

\[
\sum_{n\le x}\beta(n)=c_\beta x+O\left(x\,E(x)\right)
\]

型の評価を使用できる。ここで \(E(x)\to0\) は選択するzero-free region版に依存する。本段階では認証された最良誤差を主張せず、必要な一様版を次段階で固定する。

---

## 2. coprime二法Euler積の厳密分解

対象係数を

\[
f(r,s)=\beta(r)\beta(s)1_{(r,s)=1}
\]

とする。二変数Dirichlet級数

\[
F(s_1,s_2)=\sum_{r,s\ge1}\frac{f(r,s)}{r^{s_1}s^{s_2}}
\]

の \(q\equiv1\pmod4\) 局所因子は

\[
L_q(s_1,s_2)
=1+\frac{b_q q^{-s_1}}{1-q^{-s_1}}
 +\frac{b_q q^{-s_2}}{1-q^{-s_2}},
\]

である。同じ素数が両変数を割る項はcoprime条件により除かれる。

一変数局所因子

\[
A_q(s)=1+\frac{b_q q^{-s}}{1-q^{-s}}
\]

を使うと

\[
L_q(s_1,s_2)=A_q(s_1)A_q(s_2)C_q(s_1,s_2),
\]

\[
C_q(s_1,s_2)
=1-\frac{u_q(s_1)u_q(s_2)}{(1+u_q(s_1))(1+u_q(s_2))},
\quad
u_q(s)=\frac{b_q q^{-s}}{1-q^{-s}}.
\]

よって

\[
C_q(s_1,s_2)=1+O\left(q^{-\sigma_1-\sigma_2}\right)
\]

が一様に成り立つ。したがって

\[
C(s_1,s_2)=\prod_{q\equiv1(4)}C_q(s_1,s_2)
\]

は

\[
\Re(s_1+s_2)>1
\]

で絶対収束し、\((1,1)\) の近傍で正則かつ非零である。

従って

\[
F(s_1,s_2)=B_\beta(s_1)B_\beta(s_2)C(s_1,s_2)
\]

という厳密分解を得る。

---

## 3. 反復Selberg–Delangeで得られる範囲

長方形和

\[
S(R,S)=\sum_{r\le R}\sum_{s\le S}
\beta(r)\beta(s)1_{(r,s)=1}
\]

または固定された滑らかな積重み

\[
\sum_{r,s}\beta(r)\beta(s)1_{(r,s)=1}
W_1(r/R)W_2(s/S)
\]

については、一方の変数を固定して一変数Selberg–Delangeを適用し、その主項係数を他方の変数で再度平均する方法が使える。

cross correctionが \((1,1)\) 近傍で正則であるため、主項定数は

\[
\operatorname*{Res}_{s_1=1}B_\beta(s_1)
\operatorname*{Res}_{s_2=1}B_\beta(s_2)
C(1,1)
\]

で与えられる。これはStage12-N1-2kの二法Euler定数 \(\eta\) の有限素数局所因子と一致する。

この段階で de la Bretèche のP2・P3を検証する必要はない。

---

## 4. まだ残る結合領域の問題

最終対象は単純な長方形和ではなく、概略

\[
h(r^2+s^2)\le2B
\]

とprimitive-first height weightを含む。固定 \(h\) または固定radial shellごとに二法和を評価し、partial summationで戻す必要がある。

この移送では次を明示的に確認する必要がある。

1. 一変数Selberg–Delange誤差が、外側変数・shell parameterに対して一様であること。
2. \(r<s\)、parity class、\((r,s)=1\) を含む切断で、境界誤差が \(o(B(\log B)^3)\) になること。
3. shallow cutoffとmain regionの接続で、2jの低次評価を二法主項に合わせて再導出すること。
4. 2h–2iのPoisson・指数対評価が最終ルートで不要なのか、一部のみ再利用するのかを確定すること。

これらはStage12-N1-2nで監査する。

---

## 5. 有限監査の意味

専用スクリプトでは以下を確認する。

- 先頭11個の \(1\bmod4\) 素数で、二変数局所因子と一変数因子×cross correctionが有理数として完全一致。
- cross correctionの一次項がなく、最初の混合項が \(q^{-s_1-s_2}\) であること。
- \(C_q(1,1)\) の有限部分積が正で安定すること。
- 長方形有限和とEuler係数列が小範囲で一致すること。

有限監査は解析接続やSelberg–Delange誤差の証明ではない。

---

## 6. 判定

2lのレビュー指摘に対して、de la Bretècheの直接適用を使わない修復経路は成立する。

ただし、現段階で閉じたのは

- 一変数極構造
- coprime cross correctionの絶対収束
- 長方形・積重み上の主項因子分解

までである。

最終結合領域への一様移送が残るため、Stage12-N1-2系列全体の状態は引き続き

```text
REPAIRABLE_AFTER_ADVERSARIAL_REVIEW
```

とする。

次は

```text
Stage12-N1-2n:
反復Selberg–Delange主項をradial/height結合領域へ移送し、
境界・一様誤差・2h–2iとの継承関係を確定する監査
```

とする。

---

## EMBEDDED_SOURCE_2
PATH=docs/stage12-n1-2n-coupled-region.md
FILE_SHA256=9fe5b5ad1eea9d1b9c5cce69d48dd766a1ad7507ba0824299cffac48695186e2

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

---

## EMBEDDED_SOURCE_3
PATH=docs/stage12-n1-2o-analytic-closure.md
FILE_SHA256=25b55f8bae62ae5e04172076665e3637211019fd03eec84bb9efa34421f165c6

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


---

CHECKPOINT=END_OF_MAIN
END_OF_BUNDLE=PC-N1-2-PROOF-REVIEW-R04
