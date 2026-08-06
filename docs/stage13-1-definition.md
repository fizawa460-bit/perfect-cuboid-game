# Stage13-1 — observed 2:1:1 ratio の定義

## 0. 目的

Stage13 の目的は、比が厳密に `2:1:1` であることを先に仮定して証明することではない。

本稿では、有限計算で観測された `2:1:1` に近い方向別比率について、何を数え、どの同値関係と切断を用い、どの極限問題を研究するのかを固定する。

---

## 1. 基本対象

正整数四つ組

\[
(a,b,c,d)\in\mathbf Z_{>0}^4
\]

で、次を満たすものを考える。

\[
a<b<c,
\qquad
\gcd(a,b,c)=1,
\qquad
 a^2+b^2+c^2=d^2.
\]

ここで `a<b<c` は辺の置換を一意に代表させる canonical ordering、`gcd(a,b,c)=1` は拡大コピーを除く primitive 条件である。狭義不等号を採用するため、`a=b` または `b=c` となる等辺の境界ケースは本稿の研究対象から除外する。なお、`a=b` または `b=c` の場合には二つの面平方和が一致するため、整数面対角線の本数は 0 本または 2 本以上となり、exactly one face 条件を満たさない。

三つの面平方和を

\[
Q_{ab}=a^2+b^2,
\qquad
Q_{ac}=a^2+c^2,
\qquad
Q_{bc}=b^2+c^2
\]

とする。

本稿で `Q=\square` と書くときは、ある `m\in\mathbf Z_{>0}` が存在して `Q=m^2` となること、すなわち `Q` が正整数の平方であることを意味する。

Stage13 で扱う one-face object は、`Q_ab`, `Q_ac`, `Q_bc` のうち **ちょうど一つだけ** が平方数である四つ組である。したがって二面以上が同時に整数面対角線を持つ対象は、この三分類には含めない。

---

## 2. 三つの方向別カテゴリ

以下の `ab`, `ac`, `bc` は固定された座標軸のラベルではなく、canonical ordering `a<b<c` による大きさ順の辺の組、すなわち最小二辺・最小辺と最大辺・最大二辺を表す。この規約は、辺ラベル付きの全 orientation を数える Stage12 の oriented count とは異なる。

本稿では `B\in\mathbf Z_{\ge1}` とし、空間対角線の切断 `d<=B` を課す。

### `ab_only`

\[
Q_{ab}=\square,
\qquad
Q_{ac}\ne\square,
\qquad
Q_{bc}\ne\square.
\]

その個数を

\[
N_{ab}(B)
\]

と書く。

### `ac_only`

\[
Q_{ac}=\square,
\qquad
Q_{ab}\ne\square,
\qquad
Q_{bc}\ne\square.
\]

その個数を

\[
N_{ac}(B)
\]

と書く。

### `bc_only`

\[
Q_{bc}=\square,
\qquad
Q_{ab}\ne\square,
\qquad
Q_{ac}\ne\square.
\]

その個数を

\[
N_{bc}(B)
\]

と書く。

全 one-face count を

\[
N_1(B)=N_{ab}(B)+N_{ac}(B)+N_{bc}(B)
\]

と定義する。

---

## 3. 観測比率

方向別 count vector を

\[
\mathbf N(B)
=
\bigl(N_{ab}(B),N_{ac}(B),N_{bc}(B)\bigr)
\]

とする。

Stage13 でいう observed `2:1:1 ratio` とは、射影比

\[
N_{ab}(B):N_{ac}(B):N_{bc}(B)
\]

が `2:1:1` に近いという有限範囲の観測を指す。ここで「近い」は本段階では記述的な表現であり、距離、ノルム、許容誤差、または収束速度を定義するものではない。その定量化は Stage13-5 以降で行う。

`N_1(B)>0` のとき、総数で正規化した proportion vector を

\[
\mathbf P(B)
=
\frac{1}{N_1(B)}
\bigl(N_{ab}(B),N_{ac}(B),N_{bc}(B)\bigr)
\]

と定義する。`N_1(B)=0` の場合、`\mathbf P(B)` は定義しない。

理想化された `2:1:1` に対応する基準ベクトルは

\[
\mathbf P_*
=
\left(\frac12,\frac14,\frac14\right).
\]

ただし、この段階では

\[
\mathbf P(B)\to\mathbf P_*
\]

を仮定しない。収束の有無、正しい極限、有限範囲の偏り、およびズレの構造は Stage13-5 以降の研究対象である。

---

## 4. 有限計算による動機

既存データ `ab_ac_bc_actual.json` は、

- `d<=100000`;
- `a<b<c`;
- `gcd(a,b,c)=1`;
- integer space diagonal;
- exactly one integer face diagonal;
- permutations and scaled copies deduplicated;

という条件で列挙されている。

このデータでは

\[
N_{ab}(100000)=84146,
\]

\[
N_{ac}(100000)=43180,
\]

\[
N_{bc}(100000)=40704,
\]

したがって

\[
\mathbf N(100000)
=(84146,43180,40704)
\]

であり、`bc_only` を 1 に正規化すると概ね

\[
2.0673:1.0608:1
\]

となる。また総数 `168030` で正規化すると

\[
\mathbf P(100000)
\approx
(0.50078,0.25698,0.24224).
\]

これらは Stage13 の動機となる有限観測であり、漸近定理ではない。

---

## 5. counting convention と同値関係

Stage13 の方向別観測 count では、次を固定する。

1. **primitive only** — `gcd(a,b,c)=1` とする。
2. **canonical unordered representative** — `a<b<c` により辺の置換を一つにまとめる。本 Stage は strictly ordered な対象のみを数える。
3. **space-diagonal cutoff** — 高さ変数ではなく `d<=B` を用いる。
4. **exactly one face** — 二面または三面成立を除外する。
5. **no scale multiplicity** — primitive 条件により相似拡大を重複計数しない。

従って、ここでの `N_ab`, `N_ac`, `N_bc` は、辺のラベル付き全 orientation をそのまま数える count ではない。

---

## 6. Stage12 との関係

Stage12-N1-2 は primitive oriented count

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
\]

を与えた。

一方、本稿の `N_ab(B)`, `N_ac(B)`, `N_bc(B)` は、canonical ordering `a<b<c` の下で exact-one-face objects を方向別に分類した count である。

したがって、Stage12 の `C_prim(B)` を三つの count のいずれか、または `N_1(B)` へ自動的に同一視しない。orientation、multiplicity、parity、および canonical ordering の変換係数を明示することが必要であり、その接続は Stage13-2 および Stage13-8 の課題とする。

Stage13-1 は `C_{\rm prim}(B)` と `N_{ab}(B)`, `N_{ac}(B)`, `N_{bc}(B)`, `N_1(B)` の間に、等式、漸近式、または定数倍関係を主張しない。

---

## 7. Stage13 の中心問題

本定義の下で、Stage13 の中心問題は次である。

> なぜ
> \[
> N_{ab}(B):N_{ac}(B):N_{bc}(B)
> \]
> が有限範囲で `2:1:1` に近い形を示すのか。

研究対象には次を含む。

- leading `2` を生む構造;
- 二つの `1` が近い値になる理由;
- `ac_only` と `bc_only` の非対称なズレ;
- orientation、primitive 条件、multiplicity、parity、local density の寄与;
- `B->infinity` での正しい漸近比または補正式。

厳密な `2:1:1` を結論として先取りせず、主構造とズレをともに説明することを Stage13 の最終目標とする。

---

## 8. 本段階の状態

```text
DEFINITION_FIXED_STRUCTURAL_DECOMPOSITION_PENDING
```

本稿により、Task 13-1 で必要な

- counted objects;
- normalization;
- limiting parameter;
- equivalence relation;
- Stage12 との非自明な接続;

を固定した。次は Task 13-2 で、三方向 count を orientation、multiplicity、parity、および local density の寄与へ分解する。
