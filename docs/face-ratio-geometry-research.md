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
- 高さ $H=d$ と楕円曲線のcanonical heightの一様比較、および未観測ファイバーを含む一様なrank・点数評価

現在の中心課題は、確定した局所・実幾何の計算と、実際の離散整数点の大域的漸近計数を厳密につなぐことである。
