# 研究メモ（2026-08-05時点）

## 空間対角線整数解における面成立比率・球面積分・代数幾何

> **状態表示**
> - **確定**：厳密計算、代数的検算、または記載範囲での有限集計として確認済み
> - **経験的結果**：有限範囲のデータから確認済みだが、極限については未証明
> - **有望な仮説**：計算や実測が支持する予想
> - **未確認**：必要な検算・理論接続が未完了

## 1. 対象と実測結果

正の整数

$$
a<b<c,\qquad a^2+b^2+c^2=d^2
$$

を満たす四つ組について、三つの面 $a^2+b^2$、$a^2+c^2$、$b^2+c^2$ のどれが平方数になるかを調査した。

### 1.1 一面のみ成立する原始解【経験的結果】

条件

$$
d\le100{,}000,\qquad \gcd(a,b,c)=1
$$

で合計168,030件あり、内訳は次のとおり。

$$
\begin{aligned}
ab_{\mathrm{only}}&=84{,}146,\\
ac_{\mathrm{only}}&=43{,}180,\\
bc_{\mathrm{only}}&=40{,}704.
\end{aligned}
$$

データには $a,b,c,d$、分類、および成立しない二面の最近接平方数との差 $\Delta$ が保存されている。

データファイル：[ab_ac_bc_actual.json](../ab_ac_bc_actual.json)

$ac$ を1とした原始解比は

$$
ab:ac:bc=1.94873:1:0.94266
$$

であり、概略では $2:1:1$ である。割合は $50.078\%:25.698\%:24.224\%$ である。

### 1.2 非原始解込み【経験的結果】

$d\le100{,}000$ での件数は次のとおり。

| 分類 | 原始解 | 非原始込み | 倍率 |
|---|---:|---:|---:|
| abのみ | 84,146 | 362,324 | 4.3059 |
| acのみ | 43,180 | 179,313 | 4.1527 |
| bcのみ | 40,704 | 178,089 | 4.3752 |
| 合計 | 168,030 | 719,726 | 4.2833 |

非原始解込みの比は

$$
ab:ac:bc=2.02062:1:0.99317
$$

であり、割合は $50.342\%:24.914\%:24.744\%$ である。

### 1.3 二面成立【経験的結果】

$d\le1{,}000{,}000$ の二面成立原始解は255件である。

$$
\begin{aligned}
ab+ac&=98,\\
ab+bc&=101,\\
ac+bc&=56,\\
\mathrm{perfect}&=0.
\end{aligned}
$$

$d\le100{,}000$ では一面のみ成立が168,030件、二面成立が89件で、$N_2/N_1\approx0.0530\%$ である。二面成立89件を各面へ加え戻すと、比は補正前の $1.94873:1:0.94266$ から補正後の $1.94772:1:0.94274$ となる。したがって、二面成立が主比率へ与える影響は有限範囲では極めて小さい。

## 2. 解析①：球面積分モデル

### 2.1 正規化と順序領域【確定】

$$
x=\frac ad,\qquad y=\frac bd,\qquad z=\frac cd
$$

と置き、

$$
R=\{(x,y,z)\in S^2:0<x<y<z\}
$$

とする。球面座標

$$
x=\sin\theta\cos\varphi,\quad
y=\sin\theta\sin\varphi,\quad
z=\cos\theta
$$

では

$$
\frac{\pi}{4}<\varphi<\frac{\pi}{2},\qquad
0<\theta<\arctan(\csc\varphi)
$$

で表される。正の八分球を6つの大小順序に分割でき、境界の面積は0なので、$R$ の球面積は厳密に

$$
\operatorname{area}(R)=\frac{1}{6}\cdot\frac{4\pi}{8}=\frac{\pi}{12}
$$

である。

### 2.2 重み、大小順、数値積分【確定】

平方数密度モデルの重みを

$$
w_{ab}=\frac1{\sqrt{x^2+y^2}},\qquad
w_{ac}=\frac1{\sqrt{x^2+z^2}},\qquad
w_{bc}=\frac1{\sqrt{y^2+z^2}}
$$

とする。$R$ 内では点ごとに

$$
x^2+y^2<x^2+z^2<y^2+z^2
$$

なので

$$
w_{ab}>w_{ac}>w_{bc}
$$

であり、対応する積分について厳密に

$$
I_{ab}>I_{ac}>I_{bc}
$$

が成立する。数値積分値は

$$
\begin{aligned}
I_{ab}&=0.6597052487\ldots,\\
I_{ac}&=0.3026997527\ldots,\\
I_{bc}&=0.2712955488\ldots
\end{aligned}
$$

であり、比は

$$
I_{ab}:I_{ac}:I_{bc}=2.17940465:1:0.89625296
$$

である。

### 2.3 和の厳密恒等式【確定】

$$
I_{ab}+I_{ac}+I_{bc}=\frac{\pi^2}{8}
$$

が厳密に成立する。証明概要は次のとおりである。正の八分球 $S^+$ を6つの順序領域へ分割する。$w_{ab}+w_{ac}+w_{bc}$ は $x,y,z$ の置換に対して対称なので、各順序領域上の積分は等しい。

$$
J=\int_{S^+}\frac{1}{\sqrt{x^2+y^2}}\,d\omega
$$

と置く。置換対称性から3種類の重みの各全領域積分は $J$ であり、

$$
6(I_{ab}+I_{ac}+I_{bc})=3J.
$$

上の球面座標では $d\omega=\sin\theta\,d\theta\,d\varphi$、$\sqrt{x^2+y^2}=\sin\theta$ なので

$$
J=\int_0^{\pi/2}\int_0^{\pi/2}d\theta\,d\varphi=\frac{\pi^2}{4}.
$$

したがって

$$
I_{ab}+I_{ac}+I_{bc}=\frac{J}{2}=\frac{\pi^2}{8}.
$$

## 3. 解析②：primitive／非primitive比較

### 3.1 有限復元【確定】

原始解 $(a,b,c,d)$ の整数倍 $(ka,kb,kc,kd)$ も同じ面成立分類を保つ。原始解の空間対角線を $d_p$ とすると、非原始解込みの件数は正確に

$$
A_i(D)=\sum_{\substack{p\in P_i\\d_p\le D}}\left\lfloor\frac{D}{d_p}\right\rfloor
$$

で復元できる。

### 3.2 漸近比【条件付き／未証明】

もし3分類に共通の $\alpha>1$ が存在し、

$$
P_i(D)\sim c_iD^\alpha
$$

ならば部分和の評価から

$$
A_i(D)\sim\zeta(\alpha)c_iD^\alpha
$$

となり、分類比は保存される。しかし $\alpha=1$ や $D(\log D)^m$ 型では単純な $\zeta(\alpha)$ 倍率は使えず、対数次数が変化する可能性がある。したがって、primitiveと非primitiveの極限比が一致することは未証明である。

## 4. 解析③：二面成立の寄与

### 4.1 有限範囲の比較【経験的結果】

| $D$ | 一面のみ $N_1(D)$ | 二面成立 $N_2(D)$ | $N_2/N_1$ |
|---:|---:|---:|---:|
| 1,000 | 600 | 2 | 0.333% |
| 2,000 | 1,434 | 5 | 0.349% |
| 5,000 | 4,485 | 15 | 0.334% |
| 10,000 | 10,630 | 25 | 0.235% |
| 20,000 | 24,712 | 42 | 0.170% |
| 50,000 | 73,875 | 62 | 0.0839% |
| 100,000 | 168,030 | 89 | 0.0530% |

また

$$
\begin{aligned}
N_2(100{,}000)&=89,\\
N_2(200{,}000)&=116,\\
N_2(500{,}000)&=188,\\
N_2(1{,}000{,}000)&=255.
\end{aligned}
$$

見かけの成長が一面成立より遅いことは $N_2(D)=o(N_1(D))$ を強く支持するが、無条件証明ではない。

### 4.2 文献モデルと今回の位置づけ【文献確認済み／独立検算あり】

二面成立の標準モデルは、文献で **face cuboid をパラメータ化する曲面**として研究されている。標準座標を

$$
[A:B:C:X:Y:U]\in\mathbf P^5
$$

とし、

$$
V:\quad
A^2+C^2=Y^2,\qquad
B^2+C^2=X^2,\qquad
A^2+X^2=U^2
$$

と置く。第3式と第2式から $A^2+B^2+C^2=U^2$ も従う。

van Luijk はこの $V$ が幾何学的既約な次数8の3二次式完全交叉で、16個のordinary double pointを持ち、最小特異点解消がK3曲面になることを示している。また、$V$ を2本の楕円曲線の積の反転商として明示している。Jarossay–Enriquez–Saettone–Svorayも同じ標準方程式とKummer構造を記載している。

主要文献：

- R. van Luijk, [On Perfect Cuboids](https://pub.math.leidenuniv.nl/~luijkrmvan/ps/cuboids.pdf), Definition 4.1.1 および §4.1
- D. Jarossay, B. Enriquez, N. Saettone, L. Svoray, [The fundamental group of surfaces parametrizing cuboids](https://arxiv.org/abs/2310.12710), §1.1
- M. Stoll and D. Testa, [The surface parametrizing cuboids](https://arxiv.org/abs/1009.0388)（48節点を持つ完全直方体のbox surfaceと、そのK3商を扱う別の曲面であり、上のface-cuboid曲面そのものと混同しない）

以下では、文献記載事項と、このリポジトリで独立に再計算した事項を区別する。

### 4.3 二面成立曲面の厳密な定義【確定】

成立する面対角線をそれぞれ $p,q,r$ とする。三種類の「指定した二面以上が成立する」射影曲面を次で定義する。

$$
V_{ab+ac}\subset\mathbf P^5_{[a:b:c:p:q:d]}:
\begin{cases}
a^2+b^2=p^2,\\
a^2+c^2=q^2,\\
p^2+c^2=d^2,
\end{cases}
$$

$$
V_{ab+bc}\subset\mathbf P^5_{[a:b:c:p:r:d]}:
\begin{cases}
a^2+b^2=p^2,\\
b^2+c^2=r^2,\\
p^2+c^2=d^2,
\end{cases}
$$

$$
V_{ac+bc}\subset\mathbf P^5_{[a:b:c:q:r:d]}:
\begin{cases}
a^2+c^2=q^2,\\
b^2+c^2=r^2,\\
q^2+b^2=d^2.
\end{cases}
$$

各場合、3本目の式は

$$
a^2+b^2+c^2=d^2
$$

と同値であり、もう一方の成立面対角線を用いた式も従う。例えば $V_{ab+ac}$ では $q^2+b^2=d^2$ である。

三曲面は $a,b,c$ の置換と対応する面対角線座標の置換により $\mathbf Q$ 上同型である。ただし、実際の計数では同じ曲面の異なる実領域へ

$$
0<a<b<c
$$

を課すため、三分類の件数が等しくなるとは限らない。

### 4.4 「二面以上」と「ちょうど二面」の区別【確定】

上の代数曲面は、指定した二面対角線が有理数になる点を表す。欠けている第3面対角線については条件を課していないため、曲面上の有理点には次の両方が含まれる。

1. 欠けた面対角線が非有理である「ちょうど二面成立」
2. 欠けた面対角線も有理である「三面成立」、すなわち空間対角線も含めたperfect cuboid点

したがって、代数曲面が直接表すのは **二面以上成立**である。整数データで「ちょうど二面」に限定するには、欠けた平方和が平方数でないという追加の算術条件を課す。

この区別は単純な幾何学的開部分の除去とは異なる。欠けた面対角線の平方根を追加する有限被覆上に有理点が持ち上がるかという、有理点上の条件である。

`data/two_face_cuboids_1e6_fixed.json` は、ちょうど二面成立する原始整数点と、三面成立した場合の `perfect` 分類を保存する。$d\le1{,}000{,}000$ では `perfect=0` であるが、これは有限探索結果であり、完全直方体が存在しないことを意味しない。

低次性の上界を考える際には

$$
N_2^{\mathrm{exact}}(B)\le N_2^{\ge2}(B)
$$

なので、まず曲面全体の「二面以上成立」の正の有理点数を上から評価すれば十分である。

### 4.5 文献上のface-cuboid曲面との座標対応【確定】

標準曲面

$$
V:
\begin{cases}
A^2+C^2=Y^2,\\
B^2+C^2=X^2,\\
A^2+X^2=U^2
\end{cases}
$$

との座標対応は次のとおりである。

| 今回の曲面 | 標準座標 $(A,B,C,X,Y,U)$ |
|---|---|
| $V_{ab+ac}$ | $(c,b,a,p,q,d)$ |
| $V_{ab+bc}$ | $(a,c,b,r,p,d)$ |
| $V_{ac+bc}$ | $(a,b,c,r,q,d)$ |

各行を標準3式へ代入すると、4.3の定義式がそのまま得られる。したがって、今回の二面以上成立曲面は、単なる類似ではなく、文献上のface-cuboid曲面と明示的に $\mathbf Q$ 上同型である。

なお、Cohn等で `face-cuboid` が「3面対角線が整数のEuler brick」の意味に使われる場合がある一方、van Luijkおよび近年のface-cuboid曲面文献では「7つの長さのうち面対角線1本を除いて有理」という意味で使われる。用語だけで同一視せず、上の方程式を基準とする。

### 4.6 16特異点と $A_1$ 型の独立検算【確定】

標準3式を

$$
F_1=A^2+C^2-Y^2,\quad
F_2=B^2+C^2-X^2,\quad
F_3=A^2+X^2-U^2
$$

とする。Jacobianの全$3\times3$小行列式と $F_1,F_2,F_3$ を連立し、6個の各射影chartで解いた。再現スクリプトは

[`scripts/audit_two_face_cuboids.py`](../scripts/audit_two_face_cuboids.py)

に置いた。

代数閉包上の特異点は、$\varepsilon,\delta\in\{\pm1\}$ として、ちょうど次の16点である。

$$
[1:0:0:0:\varepsilon:\delta],\qquad
[0:1:0:\varepsilon:0:\delta],
$$

$$
[1:0:\varepsilon i:\delta i:0:0],\qquad
[0:1:\varepsilon i:0:\delta i:0].
$$

前半8点は $\mathbf Q$ 上、後半8点は $\mathbf Q(i)$ 上で定義され、後半は複素共役で入れ替わる。各点でJacobian rankは2である。

4つの対称型ごとに滑らかな局所変数を2個消去すると、残る二次接錐はそれぞれ

$$
B^2+C^2-X^2,\quad
A^2+C^2-Y^2,\quad
B^2+Y^2-U^2,\quad
A^2+X^2-U^2
$$

となる。各Hessian行列式は $-8$ で非退化である。よって16点はすべてordinary double point、すなわち $A_1$ 特異点である。

すべての特異点は複数の座標が0になる境界点であり、

$$
A,B,C,X,Y,U>0
$$

を満たす特異点は存在しない。したがって、今回の正の順序領域 $0<a<b<c$ は曲面の滑らかな部分に含まれる。

### 4.7 最小解消とK3／Kummer構造【文献確認済み／独立再構成は未完了】

3二次式完全交叉の標準束は、形式的には

$$
K_V=\mathcal O_V(2+2+2-6)=\mathcal O_V
$$

である。16個の $A_1$ 特異点はDu Val特異点なので、最小解消はcrepantである。

van Luijkは、特異点解消曲面について $p_g=1,q=0$ を確認し、K3曲面になることを示している。さらに

$$
E:\ y^2z=x^3-4xz^2,
$$

その有理2-torsion点による2-isogenous quotient

$$
E':\ y^2z=x^3+xz^2
$$

を用いて、標準曲面 $V$ を

$$
(E\times E')/\{(P,Q)\sim(-P,-Q)\}
$$

と $\mathbf Q$ 上で同型に記述している。したがって、$V$ の最小特異点解消は積型Kummer曲面 $\operatorname{Kum}(E\times E')$ である。

ここで確定しているのは曲面の幾何学的分類である。次の点数評価は直ちには従わない。

- 今回の高さ $d$ に対する有理点数の成長率
- 累積する有理曲線の完全な一覧
- $N_2(B)=O((\log B)^r)$ または $O(B^{1/2+\varepsilon})$
- $N_2(B)=o(N_1(B))$

K3／Kummerという名称だけを根拠に、これらを主張しない。

### 4.8 高さ $H=d$【正の整数領域では確定／解消上の高さ理論との照合は未確認】

正の整数点では

$$
d^2=a^2+b^2+c^2
$$

なので $a,b,c<d$ である。また、成立する面対角線は、例えば

$$
p^2=a^2+b^2=d^2-c^2<d^2
$$

であり、他の面対角線も同様に $d$ より小さい。したがって、各射影モデルの標準max-heightは

$$
H=\max(a,b,c,d,p,q)=d
$$

または対応する $p,q,r$ を含めても $H=d$ となる。

一方、最小解消 $\pi:\widetilde V\to V$ 上では、$\pi^*\mathcal O_V(1)$ はnefかつbigであるが、例外曲線との交点が0なのでampleではない。既知のKummer曲面上の有理点計数定理を使う場合、その定理が扱う因子・高さと $\pi^*\mathcal O_V(1)$ を明示的に照合する必要がある。この照合は未完了である。

### 4.9 既知24円錐曲線と正の順序領域【方程式照合・255件監査は確定／完全分類ではない】

van Luijk, §4.2 は標準曲面

$$
A^2+C^2=Y^2,\qquad B^2+C^2=X^2,\qquad A^2+X^2=U^2
$$

上の24本の円錐曲線を明示している。符号 $\varepsilon,\delta\in\{\pm1\}$ に対し、6組の4本は次で与えられる。

$$
\begin{array}{ll}
D_{C,\varepsilon,\delta}:&C=0,\ Y=\varepsilon A,\ X=\delta B,\ A^2+B^2=U^2,\\
D_{A,\varepsilon,\delta}:&A=0,\ Y=\varepsilon C,\ X=\delta U,\ B^2+C^2=X^2,\\
D_{B,\varepsilon,\delta}:&B=0,\ X=\varepsilon C,\ Y=\delta U,\ A^2+C^2=Y^2,\\
D_{Y,\varepsilon,\delta}:&Y=0,\ iA=\varepsilon C,\ B=\delta U,\ B^2+C^2=X^2,\\
D_{X,\varepsilon,\delta}:&X=0,\ iB=\varepsilon C,\ A=\delta U,\ A^2+C^2=Y^2,\\
D_{U,\varepsilon,\delta}:&U=0,\ iX=\varepsilon A,\ iY=\delta B,\ B^2+C^2=X^2.
\end{array}
$$

各曲線は少なくとも1つの射影座標が0である。最小解消で現れる16本の例外曲線も特異点上の境界にある。したがって、厳密な正領域

$$
A,B,C,X,Y,U>0
$$

はこれら40本と交わらない。

[`scripts/classify_two_face_kummer_curves.py`](../scripts/classify_two_face_kummer_curves.py) により全255件を各分類から標準座標へ変換して検査した結果、次が確認された。

- 標準3方程式を満たす点：255件
- 6座標がすべて正：255件
- 座標境界上の点：0件
- 上記24円錐曲線上の点：0件

集計結果は [`data/two_face_cuboids_1e6_kummer_report.json`](../data/two_face_cuboids_1e6_kummer_report.json) に保存した。全点の派生情報はGitHub Actionsで再生成可能であり、artifactとして保存する。

ただし、この結果は **van Luijkが明示した24円錐曲線と16例外曲線を除外しただけ**である。K3曲面には他の有理曲線が存在し得るため、「255件はすべての有理曲線の外にある」とは結論しない。

### 4.10 楕円ファイバーによる255件の分類【有限データについて確定】

van Luijkの楕円ファイブレーションは

$$
\varphi:V\dashrightarrow\mathbf P^1,\qquad
[A:B:C:X:Y:U]\longmapsto[Y-A:C]
$$

で与えられる。$C\ne0$ ではアフィンパラメータを

$$
\lambda=\frac{Y-A}{C}
$$

と置ける。標準方程式 $Y^2-A^2=C^2$ から

$$
\lambda=\frac{Y-A}{C}=\frac{C}{Y+A}
$$

が厳密に成立する。正領域では

$$
0<\lambda<1.
$$

文献上、特異ファイバーのパラメータは

$$
\lambda=0,\infty,\pm1,\pm i
$$

である。255件について計算したところ、全点で $0<\lambda<1$ であり、これらの特異パラメータには該当しなかった。したがって、255件はこのファイブレーションに関してすべて滑らかな種数1ファイバー上にある。

有限データ内のファイバー分布は次のとおりである。

- 異なる $\lambda$：193種類
- 1点だけを含むファイバー：143種類
- 2点を含むファイバー：44種類
- 3点を含むファイバー：3種類
- 4点を含むファイバー：2種類
- 7点を含むファイバー：1種類
- 最大多重点：$\lambda=16/21$ の7点
- 複数点を含む $\lambda$：50種類
- 複数の面分類にまたがる $\lambda$：27種類

同じ $\lambda$ を持つことは、同じ楕円ファイバーに属することを意味する。ただし、そのファイバー上で同一の生成族・同一のMordell--Weil軌道に属することや、点数の累積を意味するものではない。この追加分類には、各ファイバーをWeierstrass形式へ移し、有理点の群構造を個別に調べる必要がある。

### 4.11 McKinnon型計数定理の適用監査と $N_2=o(N_1)$【直接適用不可／未証明】

McKinnon, *Counting Rational Points on K3 Surfaces* は、2本の楕円曲線の積に付随するKummer曲面について有理点計数を扱う。ただし、同論文の主定理には少なくとも次の条件がある。

1. 基礎体 $K$ 上で両楕円曲線の全2-torsionが有理であること
2. 最小解消K3曲面上の **ample divisor** $D$ に付随する高さを用いること
3. $D$ が論文中の $A_{S,T},F_1,F_2$ で記述されるconeに入り、係数・正値条件を満たすこと
4. 累積曲線に関するCorollaryを使う場合は、さらに論文の不等式条件を満たすこと

今回の楕円曲線は

$$
E:y^2=x^3-4x,\qquad E':y^2=x^3+x
$$

である。$E$ の2-torsionは $\mathbf Q$ 上で分裂するが、$E'$ の非零2-torsionには $x=\pm i$ が現れる。そのため、全2-torsionを有理にする標準設定は少なくとも $\mathbf Q(i)$ 上で考える必要がある。$\mathbf Q$-有理点は $\mathbf Q(i)$-有理点の部分集合だが、これだけで今回の高さ・順序領域に必要な上界が自動的に得られるわけではない。

さらに、今回の高さに対応する

$$
L=\pi^*\mathcal O_V(1)
$$

はnefかつbigだが、16本の例外曲線 $E_j$ に対して

$$
L\cdot E_j=0
$$

であり、ampleではない。したがって、McKinnonの主定理のample仮定を満たさず、同論文のCorollaryで使われる最小曲線次数も0になってしまう。よって、同定理をそのまま引用して高さ $H=d$ の計数上界を得ることはできない。

また、今回の $E$ と $E'$ は2-isogenousで、van Luijkが計算した幾何Picard数は20である。McKinnonが用いる標準的な $E_{ij},L_i,M_j,F_1,F_2$ の部分はrank 18の格子を与えるが、今回の超平面類 $L$ をrank 20のNéron--Severi群内で明示し、追加のisogeny由来クラスとの成分を調べる作業は未完了である。

したがって、現時点で確定した結論は次である。

- 既知24円錐曲線と16例外曲線は正の255件を説明しない
- 255件はすべて滑らかな楕円ファイバー上にある
- McKinnonのample-height定理は高さ $H=d$ へ直接適用できない
- 二面成立数の無条件上界および $N_2(B)=o(N_1(B))$ は依然として未証明

次に必要な理論作業は、次のいずれかである。

1. $L$ をrank 20の $\operatorname{NS}(\widetilde V)$ 内で明示し、$L$-次数が小さい全曲線を特定する
2. McKinnonの議論をnefかつbigな境界因子 $L$ へ拡張する
3. ample因子 $D_\varepsilon$ と $L$ の高さを、計数に使える一様性を保って比較する
4. 楕円ファイブレーションと $H=d$ を直接使って、ファイバーごとの上界を総和する

なお、$N_2=o(N_1)$ の証明には二面成立側の上界だけでなく、一面成立数 $N_1(B)$ の十分な下界または主項も必要である。


### 4.12 楕円ファイバー上のMordell–Weil関係【有限データは確定／大域計数は未証明】

van Luijk, *On Perfect Cuboids*, §4.2 により、滑らかな一般ファイバーは

$$
C_\lambda:\quad
y^2z=x\bigl(x+4\lambda^2z\bigr)
\bigl(x+(\lambda^2+1)^2z\bigr)
$$

というWeierstrass形を持つ。標準face-cuboid座標からの逆向きの写像は

$$
\begin{aligned}
x&=4\lambda^2C(U-B),\\
y&=8\lambda^3(U+X)(U-B),\\
z&=C(X+B)
\end{aligned}
$$

である。出典：R. van Luijk, [On Perfect Cuboids](https://pub.math.leidenuniv.nl/~luijkrmvan/ps/cuboids.pdf), pp.55--58（式(41)以後、Proposition 4.2.12）。

この写像と楕円曲線の群法則を有理数の厳密演算で実装した。再現コードは

- [`scripts/analyze_two_face_mordell_weil.py`](../scripts/analyze_two_face_mordell_weil.py)
- [`scripts/audit_focus_fiber_with_pari.py`](../scripts/audit_focus_fiber_with_pari.py)
- [`scripts/audit_repeated_fibers_with_pari.py`](../scripts/audit_repeated_fibers_with_pari.py)

である。

#### 4.12.1 255点のWeierstrass写像【確定】

`data/two_face_cuboids_1e6_kummer_classification.json` の255点すべてについて、上の写像で得られた点が対応する $C_\lambda(\mathbf Q)$ の方程式を満たすことを確認した。

- 写像成功：255/255点
- 有限位数を24倍まで探索して零点となった観測点：0件
- 複数の観測点を含むファイバー：50本

有限位数探索は再現可能な厳密計算であるが、この項目単独では特殊化後のtorsion群を完全決定したとは扱わない。

#### 4.12.2 観測点間の厳密な有限係数関係【確定】

van Luijkは一般ファイバーについて

$$
C_\lambda(\mathbf Q(\lambda))_{\mathrm{tors}}
\cong \mathbf Z/4\mathbf Z\times\mathbf Z/2\mathbf Z
$$

を示し、生成点を $T_1,T_3$ としている。この8点を各有理 $\lambda$ へ特殊化し、観測点を係数範囲 $[-8,8]$ の整数結合とtorsionの和として探索した。

50本の複数点ファイバーすべてで、保存された全観測点について厳密な群法則の等式が得られた。観測点を覆うために導入したseed点数は

| bounded seed数 | ファイバー数 |
|---:|---:|
| 1 | 41 |
| 2 | 9 |

であった。ただし、このseed数は **保存された有限個の観測点を係数範囲内で表すための数**であり、特殊化ファイバーのMordell–Weil rankではない。

#### 4.12.3 $\lambda=16/21$ の7点【確定】

最多の7点を含むファイバーでは、source index 18の点を $P$、74の点を $Q$ と置くと、全7点が次の厳密な関係を満たした。

| source index | 群法則上の表現 |
|---:|---|
| 18 | $P$ |
| 33 | $-P+3T_1$ |
| 74 | $Q$ |
| 84 | $-Q+3T_1$ |
| 102 | $P-Q+2T_1$ |
| 129 | $P+Q+3T_1$ |
| 173 | $-2P$ |

PARI/GP 2.15.4 の `ellrank` による2-descentでは、この特殊化曲線について

$$
\operatorname{rank} C_{16/21}(\mathbf Q)=2,
$$

が下界2・上界2として一致した。またtorsion群は

$$
C_{16/21}(\mathbf Q)_{\mathrm{tors}}
\cong \mathbf Z/4\mathbf Z\times\mathbf Z/2\mathbf Z
$$

と計算された。PARIの `ellrank` が返す下界・上界の意味は公式文書
[PARI/GP: Elliptic curves](https://pari.math.u-bordeaux.fr/dochtml/ref-stable/Elliptic_curves.html#ellrank)
に従う。

この結果はファイバー $\lambda=16/21$ のrankを確定するが、$P,Q$ が飽和されたMordell–Weil基底であることまでは証明していない。

#### 4.12.4 複数点50ファイバーのPARI 2-descent【有限集合について確定】

複数の観測点を含む50本すべてについてPARI/GPの2-descentを実行した。タイムアウト・計算エラーはなく、全50本でrank下界と上界が一致した。

| 特殊化rank | ファイバー数 |
|---:|---:|
| 1 | 30 |
| 2 | 20 |

50本すべてでtorsion群は $\mathbf Z/4\mathbf Z\times\mathbf Z/2\mathbf Z$ と計算された。bounded seed数と確定rankが一致したのは39本である。残る11本では観測点は1 seedとtorsionで表せたが、曲線自体のrankは2だった。したがって、観測された直方体点だけからファイバー全体のrankを推定することはできない。

この有限集合のrank分布から、未観測の $\lambda$ に対する一様なrank上界や、K3曲面全体の有理点数の成長率は導かれない。

#### 4.12.5 $N_2=o(N_1)$ への意味【未証明】

今回確定したのは、既に観測された255点が多数の滑らかな楕円ファイバーへ分散し、複数点ファイバーではrank 1または2の算術構造を持つという有限範囲の事実である。

一方、$N_2=o(N_1)$ の証明には依然として、少なくとも次が必要である。

1. 高さ $H=d$ と各ファイバー上のcanonical heightの一様比較
2. $\lambda$ の高さとファイバー内の点の高さを同時に制御する評価
3. 未観測ファイバーを含むrank・torsion・局所条件の一様な扱い
4. 正の順序領域およびprimitive条件への局所化
5. 一面成立数 $N_1(B)$ の十分な下界

したがって、楕円ファイバー分類は二面成立解の生成構造を明確にしたが、二面成立数の無条件上界や $N_2=o(N_1)$ は未証明のままである。

### 4.13 観測済み193ファイバー全体のrank・飽和監査【有限集合について確定】

4.12では複数点を含む50本だけをPARI/GPで監査した。次の段階として、単一点143本を含む観測済み全ファイバーについて同じWeierstrassモデルを用い、PARI/GP `ellrank` の2-descentを実行した。再現コードと結果は

- [`scripts/audit_all_observed_fibers_with_pari.py`](../scripts/audit_all_observed_fibers_with_pari.py)
- [`data/two_face_cuboids_1e6_all_fibers_pari_report.json`](../data/two_face_cuboids_1e6_all_fibers_pari_report.json)

に保存した。

#### 4.13.1 全193ファイバーの特殊化rank【有限集合について確定】

- 対象ファイバー：193本
- 単一点ファイバー：143本
- 複数点ファイバー：50本
- PARI成功：193本
- タイムアウト：0本
- PARIエラー：0本
- rank確定：190本
- rank未確定：3本

今回の計算では、3本ではrank区間が残った。確定した特殊化rankの分布は次である。

| 特殊化rank | ファイバー数 |
|---:|---:|
| 1 | 106 |
| 2 | 80 |
| 3 | 3 |
| 4 | 1 |

単一点143ファイバーだけに限定した分布は次である。

| 単一点ファイバーの特殊化rank | ファイバー数 |
|---:|---:|
| 1 | 76 |
| 2 | 60 |
| 3 | 3 |
| 4 | 1 |

この分布は $d\le10^6$ で実際に点が観測された193個の $\lambda$ に対する結果である。未観測の有理 $\lambda$ を含む一般ファイバーのrank分布や、一様なrank上界を意味しない。

#### 4.13.2 torsion構造【有限集合について確定】

成功した各ファイバーについてPARIの `elltors` を実行した。構造別集計は

```text
{"[4, 2]": 193}
```

である。これは観測済み特殊化ファイバーの有限集合に関する計算結果であり、特殊化によるtorsion増大がすべての有理 $\lambda$ で起きないことを証明するものではない。

#### 4.13.3 観測seed部分群の小素数飽和監査【適用対象について確定】

PARI公式文書の `ellsaturation(E,V,B)` は、$V$ が有限指数部分群を生成する独立な非torsion点集合であるとき、返された部分群のindexが $B$ 未満の素数で割れないことを保証する。そこで、次の条件を満たすファイバーだけを対象にした。

1. `ellrank` の下界と上界が一致する
2. 観測bounded seed数が確定rankに等しい
3. canonical height pairingが非退化である

飽和上限は

$$
B=100
$$

とした。結果は次である。

- 飽和監査の適用条件を満たしたファイバー：115本
- `ellsaturation` 実行：115本
- 観測seed部分群のindexが1だったもの：114本
- より大きい部分群へ拡大されたもの：1本

index分布は次のとおりである。

| 観測seed部分群から飽和後部分群へのindex | ファイバー数 |
|---:|---:|
| 1 | 114 |
| 2 | 1 |

indexが1である場合、観測seed部分群は少なくとも100未満の素数に関して飽和している。indexが1より大きい場合は、観測seedが同じrankの部分群を生成していても完全なMordell--Weil基底ではなかったことを意味する。ただし、100以上の素数に関する飽和性は今回の計算からは分からない。

#### 4.13.4 $N_2=o(N_1)$ への位置づけ【未証明】

今回の監査により、保存された255点が属する全193ファイバーについて、特殊化rankと観測seed部分群の有限指数問題を以前より詳細に整理できた。しかし、これは横方向に動く $\lambda$ の個数を制御しない。二面成立数の上界には依然として

1. $H=d$ と各ファイバーのcanonical heightの一様比較
2. $\lambda$ のheightと $d$ の同時制御
3. 未観測ファイバーを含む一様なrank・局所条件の評価
4. ファイバーごとの点数上界を全 $\lambda$ について総和する議論

が必要である。したがって、観測済み全ファイバーのrankが計算できても、二面成立数の無条件上界および $N_2=o(N_1)$ はまだ従わない。



<!-- TWO_FACE_STAGE5_START -->
### 4.14 未確定rank・index 2生成点・canonical height予備解析【有限計算は確定／一様評価は未証明】

再現コードは

- [`scripts/audit_two_face_rank_height_stage5.py`](../scripts/audit_two_face_rank_height_stage5.py)
- [`scripts/audit_two_face_rank_height_stage5_runner.py`](../scripts/audit_two_face_rank_height_stage5_runner.py)

であり、全出力は

[`data/two_face_cuboids_1e6_stage5_report.json`](../data/two_face_cuboids_1e6_stage5_report.json)

に保存する。

#### 4.14.1 rank未確定3ファイバーの再監査【未確定のまま】

前段階でPARI/GP `ellrank` の下界・上界が $1\ldots3$ のまま残った3本について、effortを4および8へ上げて再実行した。3本とも計算自体は成功したが、区間は縮まらず、新たな独立生成点も得られなかった。

| $\lambda$ | source index | 再計算後のrank区間 | 状態 |
|---:|---:|---:|---|
| $81/385$ | 85 | $1\ldots 3$ | 未確定 |
| $147/194$ | 134 | $1\ldots 3$ | 未確定 |
| $119/130$ | 205 | $1\ldots 3$ | 未確定 |

3本すべてでroot numberは $-1$ である。ただし、root numberからrankの奇偶性を使う議論は一般には予想を含み、今回の計算だけからrank $1$ と確定しない。したがって、これら3本の正確なMordell--Weil rankは依然として未確認である。

#### 4.14.2 $\lambda=7/32$ の飽和生成点【確定】

source index 224 の観測点を $P$ とする。この点の元の直方体は

$$
(a,b,c,d)=(251328,418304,546975,733025)
$$

である。PARI/GP `ellsaturation(E,[P],100)` が返した点を $G$ とすると、

$$
G=\left(-41209/65536,\,-24107265/67108864\right)
$$

であり、有理数の厳密な群法則計算により

$$
P=2G
$$

が成立した。regulator比は

$$
\frac{\operatorname{Reg}(P)}{\operatorname{Reg}(G)}=4
$$

であり、自由部分におけるindexが2であることと一致する。したがって、前段階で検出された唯一のindex 2事例について、欠けていた半点を明示できた。

`ellsaturation(...,100)` が保証するのは、返された部分群のindexが100未満の素数で割れないことである。100以上の素数に関する完全飽和性までは主張しない。

#### 4.14.3 255点のcanonical height予備解析【有限標本について確定】

対応する特殊化楕円曲線上で、保存済み255点すべてのPARI canonical height $\widehat h(P)$ を計算した。

| 指標 | 最小 | 中央値 | 平均 | 最大 |
|---|---:|---:|---:|---:|
| $\widehat h(P)$ | 1.252274 | 3.614779 | 3.569709 | 6.213705 |
| $\widehat h(P)/\log d$ | 0.100240 | 0.308216 | 0.301833 | 0.469561 |

有限標本内のPearson相関は次である。

| 組 | 相関係数 |
|---|---:|
| $\widehat h(P)$ と $\log d$ | 0.471976 |
| $\widehat h(P)$ と $h(\lambda)$ | -0.044721 |
| $\widehat h(P)$ とnaive $x$-height | 0.086138 |
| $\log d$ と $h(\lambda)$ | 0.503442 |

さらに有限標本へ

$$
\widehat h(P)=\beta_0+\beta_d\log d+\beta_\lambda h(\lambda)+\varepsilon
$$

を最小二乗で当てはめると、

$$
\beta_0=0.244208,\qquad
\beta_d=0.406533,\qquad
\beta_\lambda=-0.363341,
$$

$$
R^2=0.329536,\qquad
\varepsilon\in [-2.592250,\,2.358422]
$$

となった。この回帰は有限データの記述にすぎない。特に、残差が将来の点でも有界であること、$\widehat h(P)$ と $\log d$ の一様な上下評価、またはファイバーごとの点数上界を与えない。

今回の標本では $\widehat h(P)/\log d$ が約0.100から0.470の範囲にあり、単純な固定比例よりも大きな散らばりがある。次に必要なのは回帰の追加ではなく、Weierstrass写像の分子・分母、$h(\lambda)$、射影高さ $H=d$ を使った理論的な高さ不等式の導出である。

#### 4.14.4 $N_2=o(N_1)$ への位置づけ【未証明】

この段階で確定したのは、1件のindex 2部分群の真の生成点と、保存済み255点のcanonical heightである。rank未確定3本は解消できず、有限標本の高さ統計から大域的な点数上界も得られない。

次の理論課題は次である。

1. $x(P)$ の有理数heightを $d$ と $h(\lambda)$ で厳密に評価する
2. naive $x$-heightとcanonical heightの差を曲線係数のheight込みで一様に評価する
3. ファイバー内の格子点数評価を $\lambda$ 全体で総和できる形にする
4. 一面成立数 $N_1(B)$ の下界または主項と比較する

したがって、二面成立数の無条件上界および $N_2(B)=o(N_1(B))$ は未証明のままである。
<!-- TWO_FACE_STAGE5_END -->

<!-- TWO_FACE_STAGE6_START -->
### 4.15 楕円ファイバーのパラメータ・canonical height一様上界【確定】

再現コードは

- [`scripts/audit_two_face_height_theory_stage6.py`](../scripts/audit_two_face_height_theory_stage6.py)

であり、全255点の監査結果は

- [`data/two_face_cuboids_1e6_stage6_height_report.json`](../data/two_face_cuboids_1e6_stage6_height_report.json)

に保存する。この節では、有限標本の回帰ではなく、正の整数点すべてに適用できる一方向の高さ不等式を導く。

#### 4.15.1 $\lambda=m/n$ の分母制御【確定】

標準face-cuboid座標を

$$
A^2+C^2=Y^2,\qquad B^2+C^2=X^2,\qquad A^2+X^2=U^2
$$

とし、正の整数領域で $d=U$ とする。van Luijkのファイバー・パラメータを既約分数で

$$
\lambda=\frac{Y-A}{C}=\frac{C}{Y+A}=\frac{m}{n},
\qquad 0<m<n,\qquad \gcd(m,n)=1
$$

と書く。円周上の通常の有理パラメータ表示から

$$
\frac{A}{Y}=\frac{n^2-m^2}{n^2+m^2},\qquad
\frac{C}{Y}=\frac{2mn}{n^2+m^2}
$$

を得る。特に

$$
Y-A=\frac{2Ym^2}{m^2+n^2}
$$

は整数であり、$\gcd(m^2,m^2+n^2)=1$ なので

$$
\boxed{m^2+n^2\mid 2Y}.
$$

したがって

$$
m^2+n^2\le 2Y\le2d,\qquad n^2\le2d,
$$

$$
\boxed{h(\lambda)=\log n\le\frac12\log(2d)}.
$$

これは保存済みデータだけの性質ではなく、上記の正の整数点すべてに対する算術的制約である。従って $d\le B$ で現れ得る既約対 $(m,n)$ は、粗く数えても高々 $2B$ 個であり、ファイバー数は $O(B)$ である。ただし、この評価だけでは各ファイバー上の点数を制御しない。

#### 4.15.2 affine $x$-heightと整数Weierstrassモデル【確定】

van LuijkのWeierstrassモデルは

$$
y^2=x(x+4\lambda^2)(x+(\lambda^2+1)^2)
$$

であり、標準座標からの写像は

$$
x=4\lambda^2\frac{U-B}{X+B}.
$$

$0<m<n$、$U=d$、$0<U-B<d$、$0<X+B\le2d$ を使うと、約分前の分子・分母から

$$
H(x)\le4n^2d\le8d^2,
$$

$$
\boxed{h(x)\le2\log d+\log8}.
$$

さらに

$$
\xi=n^4x,\qquad \eta=n^6y
$$

と変換すると、$\mathbf Q$ 上同型な整数係数モデル

$$
E_{m,n}:\quad
\eta^2=\xi(\xi+4m^2n^2)(\xi+(m^2+n^2)^2)
$$

を得る。これを

$$
\eta^2=\xi^3+A_2\xi^2+A_4\xi
$$

と書けば

$$
A_2=(m^2+n^2)^2+4m^2n^2,\qquad
A_4=4m^2n^2(m^2+n^2)^2.
$$

$m^2+n^2\le2d$ と $4m^2n^2\le(m^2+n^2)^2$ から

$$
A_2\le8d^2,\qquad A_4\le16d^4.
$$

また

$$
\xi=4m^2n^2\frac{U-B}{X+B}
$$

なので

$$
H(\xi)\le4d^3,
$$

$$
\boxed{h(\xi)\le3\log d+\log4}.
$$

#### 4.15.3 duplicationによるcanonical height上界【確定】

$E_{m,n}$ 上の倍点公式は

$$
\xi(2P)=
\frac{(\xi(P)^2-A_4)^2}
{4\xi(P)(\xi(P)^2+A_2\xi(P)+A_4)}.
$$

この恒等式はSymPyによる展開でも独立に検算する。$\xi=R/S$ を既約表示し、$M=\max(|R|,|S|)$ とすると、分子・分母を与える次数4の斉次式から

$$
h(\xi(2P))\le4h(\xi(P))+\log C_{m,n},
$$

$$
C_{m,n}=\max\left\{(1+A_4)^2,\,4(1+A_2+A_4)\right\}.
$$

上の係数評価より

$$
C_{m,n}\le289d^8.
$$

canonical heightを標準的な規格化

$$
\widehat h(P)=\frac12\lim_{k\to\infty}4^{-k}
 h(\xi(2^kP))
$$

で定義すると、上の漸化式を反復して

$$
\widehat h(P)
\le\frac12h(\xi(P))+\frac16\log C_{m,n}.
$$

従って

$$
\boxed{
\widehat h(P)
\le\frac{17}{6}\log d+\log2+\frac13\log17
}.
$$

点がtorsionの場合は左辺が0なので同じ評価が自明に成立する。この結果は $H=d$ からcanonical heightへの**一方向の一様上界**であり、前節で未確認としていた高さ接続の一部を解消する。

ただし、逆向きの下界

$$
\widehat h(P)\ge c\log d-O(h(\lambda))
$$

や、異なるファイバーを横断する一様な非零高さ下界を与えるものではない。

#### 4.15.4 255点での再検算【有限集合について確定】

保存済み255点すべてについて、次を有理数の厳密演算で再検算した。

- $m^2+n^2\mid2Y$
- $m^2+n^2\le2d$
- Weierstrass写像と整数モデルの方程式
- $H(x)\le8d^2$
- $H(\xi)\le4d^3$
- $A_2\le8d^2$、$A_4\le16d^4$
- $C_{m,n}\le289d^8$
- PARI/GPで保存した $\widehat h(P)$ が点別上界および粗い一様上界を超えないこと

全件が通過した。有限標本での余裕は次である。

| 指標 | 最小 | 中央値 | 平均 | 最大 |
|---|---:|---:|---:|---:|
| 点別上界 $-\widehat h(P)$ | 3.940152 | 14.072872 | 14.736882 | 27.587077 |
| 一様上界 $-\widehat h(P)$ | 17.993351 | 32.917339 | 31.612541 | 39.352865 |

また有限標本では

- $h(\lambda)/\log d$ の最大値：0.530927
- $H(x)/(8d^2)$ の最大値：0.049981
- $H(\xi)/(4d^3)$ の最大値：0.000012

であった。これらの有限標本比率自体を漸近法則とは解釈しない。

#### 4.15.5 点数評価への意味と残る壁【一部確定／大域評価は未証明】

固定した滑らかなファイバー $E_\lambda$ の自由部分のrankを $r$、選んだ基底に対するcanonical height行列の最小固有値を $\mu_\lambda>0$ とする。$d\le B$ の点は

$$
\widehat h(P)\le T(B),\qquad
T(B)=\frac{17}{6}\log B+\log2+\frac13\log17
$$

を満たすため、自由部分の係数ベクトルは半径

$$
\sqrt{T(B)/\mu_\lambda}
$$

の球内に入る。従って、**各固定ファイバーについては**点数が $O_\lambda((\log B)^{r/2})$ となることが従う。

しかし $\lambda$ は $B$ とともに動き、現れ得るファイバーは $O(B)$ 本ある。大域和を評価するには依然として

1. 全有理 $\lambda$ に対するrankの一様評価または平均評価
2. $\mu_\lambda$、regulator、非torsion最小高さの一様な下界または平均評価
3. 特殊ファイバーとtorsion増大の処理
4. $O(B)$ 本のファイバーにわたる総和を一面成立数より低く抑える議論
5. 比較対象となる $N_1(B)$ の十分強い下界または漸近公式

が必要である。

従って今回確定したのは

$$
H=d\quad\Longrightarrow\quad
\widehat h(P)\le\frac{17}{6}\log d+O(1)
$$

という一方向の接続であり、二面成立数の無条件上界および

$$
N_2(B)=o(N_1(B))
$$

は未証明のままである。
<!-- TWO_FACE_STAGE6_END -->

<!-- TWO_FACE_STAGE7_START -->
### 4.16 逆写像と逆向き高さ評価の実現可能性【明示的逆写像・naive height評価は確定／大域計数は未解決】

再現コードと全255点の出力は

- [`scripts/audit_two_face_inverse_height_stage7.py`](../scripts/audit_two_face_inverse_height_stage7.py)
- [`data/two_face_cuboids_1e6_stage7_inverse_height_report.json`](../data/two_face_cuboids_1e6_stage7_inverse_height_report.json)

に保存する。前節では $d$ からcanonical heightへの上界を得た。本節では逆方向を調べ、どこまで進められるかと、どこで別の入力が必要になるかを切り分ける。

#### 4.16.1 Weierstrassモデルからface-cuboid座標への逆写像【確定】

$$
E_t:\quad y^2=x(x+4t^2)(x+(1+t^2)^2),\qquad t=\lambda
$$

とする。正の滑らかなaffine openでは、標準face-cuboid座標への逆写像は射影的に

$$
egin{aligned}
A&=2xy(1-t^2),\\
B&=x\left(4t^2(1+t^2)^2-x^2
ight),\\
C&=4txy,\\
X&=y^2-x^2(1-t^2)^2,\\
Y&=2xy(1+t^2),\\
U&=y^2+x^2(1-t^2)^2
\end{aligned}
$$

で与えられる。右辺6個は共通の射影スカラー倍を許す。楕円曲線方程式で簡約すると

$$
A^2+C^2=Y^2,\qquad B^2+C^2=X^2,\qquad A^2+X^2=U^2
$$

および

$$
t=
rac{Y-A}{C}=
rac{C}{Y+A},
$$

$$
x=4t^2
rac{U-B}{X+B},\qquad
y=8t^3
rac{(U+X)(U-B)}{C(X+B)}
$$

が戻る。SymPyによる多項式剰余計算と、保存済み255点の有理数厳密演算の双方で検算した。全255点で逆写像をprimitive整数ベクトルへ正規化すると、保存済み $[A:B:C:X:Y:U]$ と完全一致した。

#### 4.16.2 射影高さの明示的逆向き評価【確定】

6座標を $(t,x,y)$ の有理数表示で同時に斉次化すると、多重次数は高々

$$
(\deg_t,\deg_x,\deg_y)=(6,3,2)
$$

であり、各座標多項式の係数絶対値和の最大は17である。primitive整数座標では $U=d$ が射影max-heightなので

$$
oxed{
\log d\le6h(t)+3h(x)+2h(y)+\log17
}.
$$

一方、Weierstrass方程式から

$$
2h(y)\le3h(x)+6h(t)+6\log2
$$

である。従って

$$
oxed{
\log d\le6h(x)+12h(\lambda)+6\log2+\log17
}.
$$

これは有限標本の回帰ではなく、対象open上の全有理点に対する明示的不等式である。

#### 4.16.3 canonical heightへの橋【既知定理を用いた有効評価】

整数モデル

$$
\eta^2=\xi(\xi+4m^2n^2)(\xi+(m^2+n^2)^2),\qquad \lambda=m/n
$$

について、$0<m<n$ とすると

$$
c_4\le512n^8,\qquad
\Delta\le4096n^{24},\qquad
h(j)\le24h(\lambda)+27\log2.
$$

Silverman, *The difference between the Weil height and the canonical height on elliptic curves*, Math. Comp. 55 (1990), Theorem 1.1 は、$\widehat h(P)-
rac12h(x(P))$ を積分Weierstrass方程式の判別式と $j$-invariantで有効に評価する。上の不変量評価と組み合わせると、絶対的で有効な定数 $C_\lambda,C_0$ が存在して

$$
oxed{
\log d\le12\widehat h(P)+C_\lambda h(\lambda)+C_0
}
$$

が従う。従って、逆向き高さ評価そのものが存在しないことが障害なのではない。

ただし、本段階ではSilvermanの $p(E)$ に含まれる全規格化項をコードへ転記していないため、$C_\lambda$ の数値は固定しない。定理の存在だけを使って係数を小さく見積もることもしない。

#### 4.16.4 255点での再監査【有限集合について確定】

全255点で逆写像、射影正規化、不変量式、三つのheight上界を再検算し、全件が通過した。

| 指標 | 最小 | 中央値 | 平均 | 最大 |
|---|---:|---:|---:|---:|
| $6h(\lambda)+3h(x)+2h(y)+\log17-\log d$ | 39.493797 | 103.032286 | 102.899442 | 175.424541 |
| $6h(x)+12h(\lambda)+6\log2+\log17-\log d$ | 51.245930 | 126.310431 | 127.778723 | 214.167048 |
| $\log d-12\widehat h(P)$ | -61.331466 | -31.201737 | -30.997207 | -2.799613 |

有限標本での $h(\lambda)/\log d$ は 0.162401 から 0.530927 の範囲だった。これらの数値は上界の再検算には使うが、漸近法則とは解釈しない。

#### 4.16.5 分岐点としての結論【次は方針選択が必要】

逆写像と混合高さ比較は構成できた。しかし現在の評価には正の $h(\lambda)$ 項が残る。前節の

$$
h(\lambda)\le
rac12\log(2d)
$$

を代入して $\log d$ を左辺へ戻すには、最終的な $h(\lambda)$ の係数を2未満まで下げる必要がある。今回の粗い明示式はこの水準から遠く、Silvermanの補正項も $h(\lambda)$ に依存する。

従って次の選択肢は二つである。

1. 逆写像と局所heightをさらに利用し、正の整数点に限定して $h(\lambda)$ 係数を劇的に改善できるか調べる
2. ファイバーごとの一様評価に固執せず、$\lambda$ 全体についてrank、regulator、局所可解性、合同条件を平均化して総和を直接抑える

これは低優先度の残件処理ではなく、最終計数へ向かうルートの分岐である。逆向き評価の実現可能性調査という当初の目的は本節で完了したため、次段階へ進む前に研究方針を壁打ちするのが妥当である。

二面成立数の無条件上界および

$$
N_2(B)=o(N_1(B))
$$

は依然として未証明である。
<!-- TWO_FACE_STAGE7_END -->



## 5. 一面成立曲面 $V_{ab}$ の幾何

### 5.1 定義とGelfand–Leray形式【局所計算は確定／大域計数との接続は未証明】

$$
V_{ab}:\quad
a^2+b^2=p^2,\qquad p^2+c^2=d^2
\subset\mathbf P^4
$$

とする。方程式を順に消去したGelfand–Leray形式は定数倍を除いて

$$
\frac{da\,db\,dc}{4|pd|}
$$

となる。さらに

$$
(a,b,c)=r(x,y,z),\qquad
p=r\sqrt{x^2+y^2},\qquad d=r
$$

と置くと、球面方向の測度に

$$
\frac{d\omega}{\sqrt{x^2+y^2}}
$$

が現れ、平方数密度モデルの $w_{ab}$ と一致する。

ただし、次は未証明である。

- この局所計算が実際の整数解計数の主項定数になること
- 有限素点の局所密度が3分類で一致すること
- 順序領域制限を含むManin–Peyre型漸近公式
- 実際の整数点比が積分比へ収束すること

### 5.2 特異点【確定】

$$
F_1=a^2+b^2-p^2,\qquad F_2=p^2+c^2-d^2
$$

に対するヤコビ行列の行は

$$
\nabla F_1=(2a,2b,0,0,-2p),\qquad
\nabla F_2=(0,0,2c,-2d,2p)
$$

である。代数閉包上の特異点はちょうど

$$
\begin{aligned}
P_1&=[0:0:1:1:0],&P_2&=[0:0:1:-1:0],\\
P_3&=[1:i:0:0:0],&P_4&=[1:-i:0:0:0]
\end{aligned}
$$

の4点である。$P_1,P_2$ は $\mathbf Q$ 上、$P_3,P_4$ は $\mathbf Q(i)$ 上のガロア共役対である。

4点はいずれも $A_1$ 型ordinary double pointである。$P_1,P_2$ では $F_2$ の滑らかな変数を消去すると局所方程式は $a^2+b^2-p^2=0$ という非退化二次錐になる。$P_3,P_4$ では $F_1$ の滑らかな変数を消去すると局所方程式は $p^2+c^2-d^2=0$ となる。

### 5.3 quartic del Pezzo構造【確定】

随伴公式により

$$
K_V=\mathcal O_V(2+2-5)=\mathcal O_V(-1)=-H|_V.
$$

したがって

$$
(-K_V)^2=H^2=4.
$$

よって $V_{ab}$ は幾何学的に $4A_1$ 型の特異quartic del Pezzo曲面である。

### 5.4 二次曲面pencilの退化【確定】

$\lambda F_1+\mu F_2$ の対角係数は

$$
(\lambda,\lambda,\mu,-\mu,\mu-\lambda)
$$

である。$\mu=0$ でcorank 2、$\lambda=0$ でcorank 2、$\lambda=\mu$ でcorank 1となる。2つのcorank-2退化二次曲面の頂点直線と、もう一方の二次式との交点が上記4個の $A_1$ 特異点を与え、特異点構造を独立に再確認する。Segre記号や算術的タイプは現時点では断定しない。

### 5.5 toric性【未確認】

「滑らかな次数4 del Pezzo曲面がtoricでない」ことから、この特異 $4A_1$ 型もtoricでないとは結論できない。特異toric del Pezzo曲面には別の分類があるため、$V_{ab}$ のtoric性は現時点で未確定であり、split toricであるという根拠もない。

$\mathbf Q$ 上の2特異点と $\mathbf Q(i)$ 上の共役対という非自明なガロア作用から、toricである場合はnon-split型である可能性があるが、これも未証明である。確定には次の作業が必要である。

- 最小特異点解消上の境界曲線配置
- ガロア作用
- 明示的トーラス開軌道
- fanまたはCox環
- 既知の $4A_1$ 型quartic del Pezzo曲面の算術的分類表との照合

## 6. 現時点の結論

### 確定

- 二面成立楕円ファイバーの正の滑らかな整数点について、明示的な逆写像と $\log d\le6h(x)+12h(\lambda)+6\log2+\log17$ が成立し、Silvermanの高さ差定理から $\log d\le12\widehat h(P)+C_\lambda h(\lambda)+C_0$ 型の有効な混合逆向き評価が従うこと



- 二面成立楕円ファイバーの正の整数点について、$\lambda=m/n$ が $m^2+n^2\le2d$ を満たし、$\widehat h(P)\le(17/6)\log d+\log2+(1/3)\log17$ という一方向の一様上界が成立すること
- $d\le100{,}000$ での一面のみ成立原始解の実測比が約 $2:1:1$ であること
- 球面積分値、順序領域の面積 $\pi/12$、積分の大小順、和 $\pi^2/8$
- primitiveから非primitiveへの有限復元式
- 二面成立が有限範囲で主比率へ与える影響が極めて小さいこと
- 三つの二面以上成立曲面が変数置換で $\mathbf Q$ 上同型であり、文献上のface-cuboid曲面と明示的に一致すること
- 標準face-cuboid曲面の16特異点がすべて $A_1$ 型で、正の領域には特異点がないこと
- 文献上、標準face-cuboid曲面の最小解消が $\operatorname{Kum}(E\times E')$ となるK3曲面であること
- 正の整数領域では射影max-heightが $H=d$ となること
- 255点すべてがvan LuijkのWeierstrassファイバーへ写り、複数点50ファイバーの特殊化rankが30本で1、20本で2と確定したこと
- 255件が既知24円錐曲線・16例外曲線の外にあり、van Luijkの滑らかな楕円ファイバー193種類へ分布すること
- $V_{ab}$ が幾何学的に $4A_1$ 型の特異quartic del Pezzo曲面であること

### 有望だが未証明

- Leray形式の実因子が実際の主項比を与えること
- 有限素点因子が3分類で共通であること
- $V_{ab}$ がnon-split toricであること
- Manin–Peyre理論により実際の整数点比が球面積分比へ収束すること
- $N_2(D)=o(N_1(D))$
- primitiveと非primitiveの極限比が一致すること

### 未確認

- $V_{ab}$ のtoric性、境界配置、fan、Cox環および算術的分類
- 二面成立Kummer曲面上で高さ $H=d$ に対応する因子と、既知の有理点計数定理の適用条件
- 既知24円錐曲線より先の有理曲線の完全な特定、rank 20のNéron--Severi群内での高さ因子の明示、および各滑らかな楕円ファイバー上の群論的分類
- 二面成立数の無条件上界および $N_2(D)=o(N_1(D))$ の証明
- $h(\lambda)$ を含まないcanonical heightから $d$ への逆向き評価、混合評価の $h(\lambda)$ 係数を計数に有効な範囲まで小さくすること、および未観測ファイバーを含む一様または平均的なrank・regulator・点数評価

現在の中心課題は、確定した局所・実幾何の計算と、実際の離散整数点の大域的漸近計数を厳密につなぐことである。
