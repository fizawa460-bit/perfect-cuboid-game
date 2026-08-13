# Stage13-2 — observed 2:1:1 ratio の構造分解

## 0. 目的

Stage13-1 は、primitive、canonical ordering `a<b<c`、space-diagonal cutoff `d<=B`、exactly one integer face diagonal という counting convention を固定した。

本稿の目的は、方向別 count

\[
\mathbf N(B)
=
\bigl(N_{ab}(B),N_{ac}(B),N_{bc}(B)\bigr)
\]

を、後続段階で個別に解析できる構造へ分解することである。

この段階では、比が厳密に `2:1:1` であること、各成分の漸近式、Stage12 の `C_{\rm prim}(B)` との定数倍関係、または Euler 積による因子分解を主張しない。

---

## 1. 基礎母集団

`B\in\mathbf Z_{\ge1}` に対し、

\[
\mathcal U(B)
=
\left\{
(a,b,c,d)\in\mathbf Z_{>0}^4:
\begin{array}{l}
a<b<c,\\
\gcd(a,b,c)=1,\\
a^2+b^2+c^2=d^2,\\
d\le B
\end{array}
\right\}
\]

とする。

`\mathcal U(B)` では、整数面対角線の本数をまだ指定しない。

各 `x=(a,b,c,d)\in\mathcal U(B)` に対し、

\[
I_{ab}(x)=1_{a^2+b^2=\square},
\qquad
I_{ac}(x)=1_{a^2+c^2=\square},
\qquad
I_{bc}(x)=1_{b^2+c^2=\square}
\]

を定義する。

Stage13-1 の三分類は

\[
\mathcal E_{ab}(B)
=
\{x\in\mathcal U(B):I_{ab}=1,I_{ac}=I_{bc}=0\},
\]

\[
\mathcal E_{ac}(B)
=
\{x\in\mathcal U(B):I_{ac}=1,I_{ab}=I_{bc}=0\},
\]

\[
\mathcal E_{bc}(B)
=
\{x\in\mathcal U(B):I_{bc}=1,I_{ab}=I_{ac}=0\}
\]

であり、

\[
N_{uv}(B)=|\mathcal E_{uv}(B)|
\]

である。

---

## 2. raw incidence と overlap correction

exactly-one 条件を課す前の方向別 incidence count を

\[
A_{ab}(B)=\sum_{x\in\mathcal U(B)}I_{ab}(x),
\]

\[
A_{ac}(B)=\sum_{x\in\mathcal U(B)}I_{ac}(x),
\]

\[
A_{bc}(B)=\sum_{x\in\mathcal U(B)}I_{bc}(x)
\]

と定義する。

二面 overlap count を

\[
A_{ab,ac}(B)
=
\sum_{x\in\mathcal U(B)}I_{ab}(x)I_{ac}(x),
\]

\[
A_{ab,bc}(B)
=
\sum_{x\in\mathcal U(B)}I_{ab}(x)I_{bc}(x),
\]

\[
A_{ac,bc}(B)
=
\sum_{x\in\mathcal U(B)}I_{ac}(x)I_{bc}(x)
\]

とし、三面 overlap count を

\[
A_3(B)
=
\sum_{x\in\mathcal U(B)}I_{ab}(x)I_{ac}(x)I_{bc}(x)
\]

とする。

indicator の恒等式から、exactly-one count は厳密に

\[
\boxed{
N_{ab}
=
A_{ab}-A_{ab,ac}-A_{ab,bc}+A_3
}
\]

\[
\boxed{
N_{ac}
=
A_{ac}-A_{ab,ac}-A_{ac,bc}+A_3
}
\]

\[
\boxed{
N_{bc}
=
A_{bc}-A_{ab,bc}-A_{ac,bc}+A_3
}
\]

と分解される。ここおよび以下では、同じ `B` を引数に持つ場合に限り引数を省略する。

したがって、方向別 count vector は

\[
\mathbf N(B)=\mathbf A(B)+\mathbf E_{\rm overlap}(B)
\]

と書ける。ここで

\[
\mathbf A(B)
=
\bigl(A_{ab},A_{ac},A_{bc}\bigr)
\]

は raw incidence vector、

\[
\mathbf E_{\rm overlap}(B)
=
\left(
-A_{ab,ac}-A_{ab,bc}+A_3,
-A_{ab,ac}-A_{ac,bc}+A_3,
-A_{ab,bc}-A_{ac,bc}+A_3
\right)
\]

は exact-one sieve による補正である。

この恒等式により、`2:1:1` に近い形が

1. raw incidence `\mathbf A(B)` の段階ですでに現れるのか、
2. overlap correction によって生成または変形されるのか、

を分離して調べられる。

全 one-face count についても

\[
N_1
=
A_{ab}+A_{ac}+A_{bc}
-2\bigl(A_{ab,ac}+A_{ab,bc}+A_{ac,bc}\bigr)
+3A_3
\]

という厳密な恒等式を得る。

---

## 3. canonical size-order layer

Stage13 の `ab`, `ac`, `bc` は固定座標軸の名称ではなく、`a<b<c` による大きさ順の辺の組である。

- `ab`：最小辺と中間辺;
- `ac`：最小辺と最大辺;
- `bc`：中間辺と最大辺。

従って、三方向の差は canonical chamber

\[
0<a<b<c
\]

内で、整数面条件がどの size-position に置かれるかの差である。

この layer を **canonical size-order effect** と呼ぶ。

これは単なる記号変更ではない。canonical ordering の後では、三つの面は同じ位置にないため、幾何学的な領域、cutoff、parameter range、および arithmetic weight が方向ごとに異なり得る。

ただし、本稿ではその差の大きさや符号をまだ評価しない。

---

## 4. full orientation lift

`x=(a,b,c,d)\in\mathcal U(B)` は `a,b,c` が相異なるため、辺に座標ラベルを付ける全順列は `6` 個ある。

full orientation lift を

\[
\widetilde{\mathcal U}(B)
=
\mathcal U(B)\times S_3
\]

とする。

canonical object が exactly one integer face を持つとする。その一つの unordered edge pair を全 `6` 順列へ持ち上げると、固定された座標面 `xy`, `xz`, `yz` の各々に、その整数面が現れる orientation はそれぞれ `2` 個である。

従って、全 `S_3` orientation を同じ重みで数えるだけなら、axis-labelled incidence は

\[
2:2:2=1:1:1
\]

へ対称化される。

よって、Stage13 で観測された canonical ratio `2:1:1` に近い形を、**full orientation multiplicity だけ**で説明することはできない。

orientation が最終比へ影響する場合は、次のいずれかが必要である。

- Stage12 の parameterization が全 `S_3` orientation を同じ重みで数えていない;
- admissibility 条件が orientation ごとに異なる;
- canonical projection の fiber multiplicity が一定でない;
- parity、local condition、boundary condition が orientation と相関する。

これらの可能性は、本稿では未決定の bridge problem として残す。

---

## 5. primitive layer

Stage13 の count は初めから

\[
\gcd(a,b,c)=1
\]

を課している。

primitive 条件は、単に全 count へ一つの定数を掛ける操作とは限らない。方向別 face condition や parity class と相関する可能性があるため、方向ごとに監査する必要がある。

非 primitive 母集団を一時的に導入する場合、その count を `N_{uv}^{\rm all}(B)` とし、primitive projection を形式的に

\[
N_{uv}(B)
=
\sum_{g\ge1}\mu(g)\,
N_{uv}^{\rm all}(B/g;g)
\]

のような Möbius bookkeeping で扱う可能性がある。ただし、ここでは右辺の具体的な parameterization や一様誤差を主張しない。

Stage12 の primitive-first reduction を Stage13 の三方向へ移植できるかは、Stage13-8 で検証する。

---

## 6. parity layer

各 `x=(a,b,c,d)` に parity vector

\[
\varepsilon(x)
=
(a\bmod2,b\bmod2,c\bmod2)
\in\{0,1\}^3
\]

を対応させる。

方向 `uv\in\{ab,ac,bc\}` と parity class `\varepsilon` に対し、

\[
N_{uv}^{(\varepsilon)}(B)
=
\#\{x\in\mathcal E_{uv}(B):\varepsilon(x)=\varepsilon\}
\]

と定義する。

すると厳密に

\[
N_{uv}(B)
=
\sum_{\varepsilon\in\{0,1\}^3}
N_{uv}^{(\varepsilon)}(B)
\]

である。実現不能な parity class の項は `0` とする。

同様に raw incidence と overlap count も parity class ごとに分割できる。

parity layer の目的は、

- 2-adic admissibility;
- integer face diagonal の parity pattern;
- Stage12 の odd–odd / opposite-parity bookkeeping;
- canonical direction との相関;

を混同せずに分離することである。

この段階では、どの parity class が主項を支配するかを決めない。

---

## 7. representation multiplicity layer

Stage12 は、共有面対角線の parameterization と primitive-first reindexing を通じて `C_{\rm prim}(B)` を数えた。

Stage13 の canonical object count と接続するには、Stage12 の parameter record から

\[
(x,\text{distinguished face},\text{orientation})
\]

への写像を明示する必要がある。

この写像を将来

\[
\Pi_{12}:\mathcal R_{12}(B)
\longrightarrow
\mathcal U(B)\times\{ab,ac,bc\}\times S_3
\]

として固定したとき、fiber multiplicity を

\[
m_{12}(x,f,\sigma)
=
|\Pi_{12}^{-1}(x,f,\sigma)|
\]

と定義できる。

重要なのは、`m_{12}` が一定であることをこの段階で仮定しないことである。

変動要因の候補は

- parameter sign;
- coprime representation;
- parity branch;
- distinguished face の選択;
- orientation;
- boundary identification;
- exceptional stabilizer

である。

Stage12 と Stage13 の間の「変換係数」は、fiber multiplicity を監査した後にのみ定義できる。

---

## 8. local-density layer

方向差に arithmetic origin があるかを調べるため、各 prime `p` に対する局所可解性を方向別に分ける。

具体的な局所密度は、使用する parameter space と congruence model を固定した後、

\[
\delta_{uv,p}^{(\varepsilon)}
\]

の形で定義する。

ここで `uv` は canonical direction、`\varepsilon` は 2-adic parity class を表す。

本稿では

\[
\prod_p\delta_{uv,p}^{(\varepsilon)}
\]

が収束すること、global count の主定数になること、または prime ごとに独立であることを主張しない。

local-density layer で検証すべき問いは次である。

1. odd-prime local factors は三方向で同一か。
2. 方向差は主に `p=2` から生じるか。
3. canonical chamber と局所条件の間に相関があるか。
4. Stage12 の `\kappa`, `\eta` を共通因子として抽出できるか。
5. overlap correction は異なる Euler factor を持つか。

これらは Stage13-8 の主要課題である。

---

## 9. cutoff and boundary layer

Stage13 の cutoff は

\[
d\le B
\]

である。

Stage12 の証明では、parameter height、radial condition、dyadic boxes、arc boundary、diagonal boundary、および floor endpoint が現れた。

Stage12 から Stage13 へ主項を移送する場合、次を区別する。

- interior contribution;
- canonical chamber boundary;
- parameterization boundary;
- exact-one overlap boundary;
- floor and endpoint correction。

境界寄与が `o(B(\log B)^3)` であることは、Stage12 の結果から三方向へ自動的には従わない。方向別領域と bridge map を固定した後に再監査する。

---

## 10. master ledger

Stage13 の方向別 count は、次の順序で解析する。

```text
canonical primitive space-diagonal objects
        |
        v
raw directional incidence A_ab, A_ac, A_bc
        |
        +-- canonical size-order layer
        +-- parity layer
        +-- local-density layer
        +-- cutoff / boundary layer
        |
        v
exact-one overlap correction
        |
        v
N_ab, N_ac, N_bc
```

Stage12 と接続する場合は、これとは別に

```text
Stage12 parameter records
        |
        v
orientation and representation map Pi_12
        |
        v
fiber multiplicity m_12
        |
        v
canonical directional ledger
```

を構成する。

従って、現時点での master decomposition は

\[
\boxed{
\mathbf N
=
\mathbf A
+
\mathbf E_{\rm overlap}
}
\]

という exact layer と、`\mathbf A` をさらに

\[
\text{canonical geometry}
+\text{parity stratification}
+\text{local arithmetic}
+\text{boundary bookkeeping}
\]

へ解析する未完 layer から成る。

後者の `+` は概念的な解析順序を表し、現時点で additive factorization や multiplicative independence を主張する記号ではない。

---

## 11. Stage13-3 以降への割当て

### Stage13-3 — leading 2

まず raw incidence

\[
A_{ab}:A_{ac}:A_{bc}
\]

を調べ、leading `2` が canonical size-order geometry、parameter multiplicity、parity、または local density のどこで初めて現れるかを特定する。

### Stage13-4 — two 1s

`A_ac` と `A_bc` の主構造が同一かを調べ、差が overlap、boundary、または arithmetic correction に由来するかを判定する。

### Stage13-5 / 13-6 — deviation

\[
\mathbf P(B)-\mathbf P_*
\]

を定量化し、raw-incidence deviation と overlap deviation を分ける。

### Stage13-8 — Stage12 connection

`\Pi_{12}`、`m_{12}`、parity branch、`\kappa`、`\eta`、local factors、および境界移送を監査する。

---

## 12. この段階で確定したこと

本稿で確定したのは次の点である。

1. exactly-one count は raw incidence と overlap correction に厳密分解できる。
2. canonical categories は固定座標軸ではなく size-order positions である。
3. full `S_3` orientation lift だけでは canonical `2:1:1` を生成せず、axis-labelled count を対称化する。
4. parity、representation multiplicity、local density、boundary は別々に監査する必要がある。
5. Stage12 との変換係数は bridge map の fiber multiplicity を確定する前には導入しない。

この段階では、どの mechanism が leading contribution を与えるかは未決定である。

---

## 13. 状態

```text
STRUCTURAL_LEDGER_FIXED_MECHANISM_ANALYSIS_PENDING
```

次は Stage13-3 で、raw incidence と canonical size-order layer を起点として leading `2` の候補を検証する。
