# Stage12-N1-2l：de la Bretèche 多重和定理の仮定と β 二法系の適合性監査

## 結論

Stage12-N1-2k の

> 関連する二変数 Dirichlet 級数は de la Bretèche の multiple-sum theorem の標準仮定を満たす

という記述は、原典 Theorem 1 の仮定を実際に照合した証明にはなっていない。

原典の仮定は単なる

- 係数が非負
- Euler 積を持つ
- 極次数が固定

ではない。少なくとも次の三条件を明示的に検証する必要がある。

- **P1**：ある基準点 `a` より右の多変数領域で Dirichlet 級数が絶対収束すること
- **P2**：有限個の非負係数線形形式 `ell_i` に対応する極を除いた関数が、指定された tube domain へ正則接続すること
- **P3**：その tube domain 内で、虚部と極線形形式に関する一様な多項式増大度評価を持つこと

Stage12-N1-2k は P1 の初歩的部分を示唆するが、P2 と P3 を記述も証明もしていない。従って、2k の

```text
A_N1_2_leading_asymptotic_closed_at_standard_theorem_level_series_complete
```

という分類は現時点では強すぎる。

本監査の分類は

```text
B_DLB_DIRECT_APPLICATION_NOT_VERIFIED_REPAIR_ROUTE_AVAILABLE
```

とする。

これは最終漸近式が偽であるという判定ではない。レビュー群の多数意見どおり、最終接続が未検証であり `REPAIRABLE` であるという判定である。

---

## 1. 原典 Theorem 1 の正確な要求

Régis de la Bretèche, *Estimation de sommes multiples de fonctions arithmétiques*, Compositio Math. 128 (2001), Theorem 1 は、非負算術関数 `f(d_1,...,d_m)` の Dirichlet 級数

\[
F(s_1,\ldots,s_m)
=
\sum_{d_1,\ldots,d_m\ge1}
\frac{f(d_1,\ldots,d_m)}{d_1^{s_1}\cdots d_m^{s_m}}
\]

について P1–P3 を仮定する。

### P1：絶対収束

ある `a in R_+^m` が存在し、`Re(s)` が `a` より各座標で右にある領域で `F(s)` が絶対収束する。

### P2：極を除いた正則接続

非零の非負係数線形形式 `ell_1,...,ell_n` と、補助線形形式 `h_r` の有限族が存在し、

\[
H(s)=F(s+a)\prod_{i=1}^n \ell_i(s)
\]

が

\[
\Re \ell_i(s)>-\delta_1,
\qquad
\Re h_r(s)>-\delta_3
\]

で定まる tube domain に正則接続する。

### P3：tube domain での一様増大度

P2 の領域を少し縮めた領域で `H(s)` が、各 `Im ell_i(s)` と `Im(s)` に関する明示的な多項式型上界を一様に満たす。

この P3 は、Euler 積が形式的に収束するというだけでは得られない。zeta/L 因子の vertical growth と正則 Euler 積の一様制御が必要になる。

Theorem 1 の結論は、長方形型の多重和に対する

\[
X^{\langle a,b\rangle}Q_b(\log X)+O(X^{\langle a,b\rangle-\theta})
\]

である。非長方形領域へ使う場合は、さらに smooth dyadic partition と partial summation が必要である。

---

## 2. Stage12 の β 二法係数系

Stage12-N1-2k では

\[
\beta(q^j)=\frac{2(q-1)}{q+1}
\qquad(q\equiv1\pmod4,\ j\ge1)
\]

とし、それ以外を 0 とする。

`(r,s)=1` を含む二法係数を

\[
f(r,s)=\beta(r)\beta(s)\mathbf 1_{(r,s)=1}
\]

とすると、その二変数 Euler 因子は `q≡1 mod 4` に対し

\[
F_q(s_1,s_2)
=
1+b_q\frac{q^{-s_1}}{1-q^{-s_1}}
+b_q\frac{q^{-s_2}}{1-q^{-s_2}},
\qquad
b_q=\frac{2(q-1)}{q+1}.
\]

同一素数が両変数へ同時に入る項は coprimality により存在しない。

### P1

`beta(n) << tau(n)` なので、`Re(s_1)>1, Re(s_2)>1` で絶対収束する。P1 は容易に成立する。

### 想定される極構造

`b_q=2+O(q^{-1})` かつ `q≡1 mod4` の素数密度が 1/2 なので、各座標方向に一次の極が期待される。

一変数因子

\[
D_\beta(s)=\sum_{n\ge1}\frac{\beta(n)}{n^s}
\]

は形式的に

\[
D_\beta(s)=\zeta(s)L(s,\chi_4)\,U(s)
\]

型へ分解でき、`U` は少なくとも `Re(s)>1/2+epsilon` の局所領域で正則な Euler 積になることが期待される。

二変数級数も

\[
F(s_1,s_2)
=D_\beta(s_1)D_\beta(s_2)C(s_1,s_2)
\]

と分解できる。`C` は coprimality による cross correction で、局所因子は

\[
1+O(q^{-\Re(s_1+s_2)})
\]

となるため、`Re(s_1+s_2)>1+epsilon` で絶対収束する修復ルートが期待できる。

しかし 2k では、この因子分解、正則領域、非零性、vertical growth を証明していない。

---

## 3. P2 監査

P2 を閉じるには、少なくとも次を明示する必要がある。

1. 極線形形式は座標形式
   \[
   \ell_1(s)=s_1,
   \qquad
   \ell_2(s)=s_2
   \]
   だけで足りるか。
2. coprimality correction が新しい極超平面を作らないか。
3. 正規化後 Euler 積が、原典が要求する tube domain へ正則接続するか。
4. その領域で Euler 積が非零か。

局所一次項を除くと cross term は `q^{-s_1-s_2}` 型であり、`s_1,s_2` が 1 の近傍では絶対収束する。このため P2 は成立する可能性が高い。

ただし「成立する可能性が高い」と「原典仮定を検証済み」は異なる。現時点では P2 は未証明と分類する。

---

## 4. P3 監査

P3 は今回の直接適用で最も記述が欠けている箇所である。

必要なのは、極を除いた正規化関数について

- `zeta(s_i)` の zero-free strip 内の増大度
- `L(s_i,chi_4)` の vertical growth
- cross correction Euler 積の一様有界性
- dyadic partial summationで必要な導関数の制御

を同時に与えることである。

`beta(p^j)<2` や非負性だけでは P3 は従わない。

従って、2k の「標準仮定を満たす」という一文は P3 を代用できない。

---

## 5. de la Bretèche を使わない修復ルート

今回の係数系は一般の多変数算術関数より単純である。

1. 一変数 `D_beta(s)` を Selberg–Delange で処理する。
2. coprimality を
   \[
   \mathbf 1_{(r,s)=1}=\sum_{d\mid r,s}\mu(d)
   \]
   または絶対収束する cross Euler factor として処理する。
3. rectangular dyadic block 内の二変数和を一変数部分和の反復と partial summation で評価する。
4. Stage12 の非長方形対数領域は smooth dyadic partition で合成する。

この方法なら、de la Bretèche Theorem 1 の一般的な P2/P3 全体系を呼ぶ必要がない可能性がある。

ただし、この迂回法でも次が必要である。

- `D_beta(s)` の正確な Euler 分解
- 一変数部分和の主項と一様誤差
- coprimality correction の絶対収束
- 全 dyadic block を合成したときの誤差総和
- 最終 degree 3 polynomial と係数 `eta/(12 pi^2)` の再導出

従って本段階だけで最終漸近式を再び CLOSED にはしない。

---

## 6. レビュー指摘との照合

### Claude / Grok / DeepSeek

「de la Bretèche の具体的仮定が未検証」という指摘は正しい。

### Meta

「仮定を満たす」としたが、P2/P3 の具体的照合を提示していないため、CLOSED 判定の根拠としては不足する。

### Copilot / Qwen

旧三法 Poisson 誤差を最終障害として再提示した部分は、primitive-first 後の最終ルートを十分反映していない。ただし 2h–2i と 2j–2k の継承関係を明記すべきという問題は残る。

---

## 7. 決定

### 閉じたこと

- de la Bretèche Theorem 1 の実際の仮定が P1–P3 であること
- 2k が P2/P3 を検証していないこと
- 非負性と局所上界だけでは Theorem 1 を適用できないこと
- β 二法系には、座標極＋絶対収束 cross correction という修復可能な構造があること

### 閉じていないこと

- P2/P3 の完全な証明
- de la Bretèche直接適用による非長方形領域の主項導出
- 一変数 Selberg–Delange迂回ルートの全誤差合成

### 分類

```text
B_DLB_DIRECT_APPLICATION_NOT_VERIFIED_REPAIR_ROUTE_AVAILABLE
```

Stage12-N1-2 系列の状態は

```text
REPAIRABLE_AFTER_ADVERSARIAL_REVIEW
```

へ更新する。

---

## 次段階

**Stage12-N1-2m**：β 一変数 Dirichlet 級数と coprime 二変数 correction を厳密に因子分解し、de la Bretèche を使わない反復 Selberg–Delange ルートで主項と一様誤差を閉じられるか監査する。

このルートが閉じなければ、Stage12-N1-2n で P2/P3 を直接証明する。

---

## 主張しないこと

- de la Bretèche Theorem 1 が今回に適用不能であること
- 最終漸近式が偽であること
- P2/P3 が成立しないこと
- 一変数迂回ルートが既に完成したこと
- 完全直方体の存在・非存在

---

## 文献

- Régis de la Bretèche, *Estimation de sommes multiples de fonctions arithmétiques*, Compositio Mathematica 128 (2001), 261–298, Theorem 1.
- Régis de la Bretèche and Gérald Tenenbaum, *Remarks on the Selberg–Delange method*, Acta Arithmetica 200 (2021), 349–369.
- Wenguang Zhai, *On primitive lattice points in planar domains*, Acta Arithmetica 109 (2003), 1–26.
