#!/usr/bin/env python3
"""Create the proposed section-4 expansion without rewriting unrelated sections."""

from __future__ import annotations

import argparse
from pathlib import Path


START = "### 4.2 K3／Kummerに関する状態【未確認】"
END = "\n## 5. 一面成立曲面 $V_{ab}$ の幾何"

NEW_SECTION = r"""### 4.2 文献モデルと今回の位置づけ【文献確認済み／独立検算あり】

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

### 4.9 累積有理曲線と正の順序領域【次段階／未確認】

van Luijkは標準特異曲面上に、座標超平面で切り出される24本の円錐曲線を明示している。各曲線は特異点4個を通り、少なくとも1つの射影座標が0である。この24本と、解消で現れる16本の例外曲線は、厳密な正領域

$$
A,B,C,X,Y,U>0
$$

とは交わらない。

ただし、今回の高さ $H=d$ について点数を累積させ得る有理曲線がこれらだけであることは未証明である。次段階では以下が必要である。

- 24円錐曲線の明示方程式と今回の3座標系への変換
- $\operatorname{NS}(\widetilde V)$ における $\pi^*\mathcal O_V(1)$ の類
- McKinnon, *Counting Rational Points on K3 Surfaces* が扱うample因子との比較
- 正の順序領域へ入る他の有理曲線の有無
- 各候補曲線上の高さ成長率

### 4.10 255件の幾何学的分類【基本監査は確定／Kummer上の分類は未確認】

`data/two_face_cuboids_1e6_fixed.json` の全255件について、次を再計算する監査スクリプトを追加した。

- $0<a<b<c$
- $\gcd(a,b,c)=1$
- $a^2+b^2+c^2=d^2$
- 保存されたcategoryと3面対角線の平方判定の一致
- 欠けた3本目が非平方であること
- 四つ組の重複がないこと
- metadata内の各閾値累積件数との一致

監査はGitHub Actionsでも実行し、結果JSONをartifactとして保存する。元データJSONは変更しない。

現在のJSONだけで可能なのは、上記の算術監査、標準座標への変換、座標境界・既知24円錐曲線への単純な所属判定までである。Kummer商上の幾何学的分類には、少なくとも次の派生情報が必要になる。

- `standard_coordinates`
- `coordinate_boundary_member`
- `candidate_conic_ids`
- $E\times E'$ 上への逆像またはその候補
- Néron–Severi類と曲線ID
- 曲線外の一般点かどうか

これらは元JSONへ追記せず、別の派生データとして生成する。

### 4.11 $N_2=o(N_1)$ に必要な未証明事項【未確認】

有限実測は $N_2/N_1$ の低下を強く示唆するが、little-$o$ の証明には少なくとも次が必要である。

1. 一面成立数 $N_1(B)$ の主項または十分な下界
2. 二面以上成立曲面の正の有理点に対する、同じ高さ $H=d$ での上界
3. 射影有理点と原始正整数四つ組との対応および重複度の制御
4. 高さを累積させる有理曲線の特定と、曲線上・曲線外の別々の評価
5. 「二面以上」から「ちょうど二面」への移行
6. 順序領域 $0<a<b<c$ への局所化

K3／Kummer曲面であること自体は、点数が少ないことを意味しない。既知の一般定理から、今回必要な

$$
N_2(B)=o(N_1(B))
$$

が直ちに従うことは、現時点では確認できていない。255件という有限データは経験的証拠としてのみ扱う。"""

OLD_CONFIRMED = """- $d\\le100{,}000$ での一面のみ成立原始解の実測比が約 $2:1:1$ であること
- 球面積分値、順序領域の面積 $\\pi/12$、積分の大小順、和 $\\pi^2/8$
- primitiveから非primitiveへの有限復元式
- 二面成立が有限範囲で主比率へ与える影響が極めて小さいこと
- $V_{ab}$ が幾何学的に $4A_1$ 型の特異quartic del Pezzo曲面であること"""

NEW_CONFIRMED = """- $d\\le100{,}000$ での一面のみ成立原始解の実測比が約 $2:1:1$ であること
- 球面積分値、順序領域の面積 $\\pi/12$、積分の大小順、和 $\\pi^2/8$
- primitiveから非primitiveへの有限復元式
- 二面成立が有限範囲で主比率へ与える影響が極めて小さいこと
- 三つの二面以上成立曲面が変数置換で $\\mathbf Q$ 上同型であり、文献上のface-cuboid曲面と明示的に一致すること
- 標準face-cuboid曲面の16特異点がすべて $A_1$ 型で、正の領域には特異点がないこと
- 文献上、標準face-cuboid曲面の最小解消が $\\operatorname{Kum}(E\\times E')$ となるK3曲面であること
- 正の整数領域では射影max-heightが $H=d$ となること
- $V_{ab}$ が幾何学的に $4A_1$ 型の特異quartic del Pezzo曲面であること"""

OLD_UNCONFIRMED = """- $V_{ab}$ のtoric性、境界配置、fan、Cox環および算術的分類
- 二面成立曲面の特異点、既約性、最小解消、Kummer構造"""

NEW_UNCONFIRMED = """- $V_{ab}$ のtoric性、境界配置、fan、Cox環および算術的分類
- 二面成立Kummer曲面上で高さ $H=d$ に対応する因子と、既知の有理点計数定理の適用条件
- 高さを累積させる有理曲線の完全な特定と、255件の曲線別分類
- 二面成立数の無条件上界および $N_2(D)=o(N_1(D))$ の証明"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    text = args.input.read_text(encoding="utf-8")
    start = text.find(START)
    end = text.find(END)
    if start < 0 or end < 0 or end <= start:
        raise SystemExit("section-4 markers were not found in the expected order")

    updated = text[:start] + NEW_SECTION + "\n" + text[end:]

    for old, new, label in (
        (OLD_CONFIRMED, NEW_CONFIRMED, "confirmed summary"),
        (OLD_UNCONFIRMED, NEW_UNCONFIRMED, "unconfirmed summary"),
    ):
        if old not in updated:
            raise SystemExit(f"{label} block was not found")
        updated = updated.replace(old, new, 1)

    args.output.write_text(updated, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
