#!/usr/bin/env python3
"""Update only sections 4.9-4.11 and the corresponding summary bullets."""

from __future__ import annotations

import argparse
from pathlib import Path


START = "### 4.9 累積有理曲線と正の順序領域"
END = "\n## 5. 一面成立曲面 $V_{ab}$ の幾何"

NEW_SECTION = r"""### 4.9 既知24円錐曲線と正の順序領域【方程式照合・255件監査は確定／完全分類ではない】

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
"""


def update(text: str) -> str:
    start = text.find(START)
    if start < 0:
        raise ValueError(f"start marker not found: {START}")
    end = text.find(END, start)
    if end < 0:
        raise ValueError(f"end marker not found: {END}")

    result = text[:start] + NEW_SECTION + text[end:]

    confirmed_anchor = (
        "- 正の整数領域では射影max-heightが $H=d$ となること\n"
    )
    confirmed_addition = (
        confirmed_anchor
        + "- 255件が既知24円錐曲線・16例外曲線の外にあり、"
        + "van Luijkの滑らかな楕円ファイバー193種類へ分布すること\n"
    )
    if confirmed_anchor in result and "滑らかな楕円ファイバー193種類" not in result:
        result = result.replace(confirmed_anchor, confirmed_addition, 1)

    old_unconfirmed = (
        "- 高さを累積させる有理曲線の完全な特定と、255件の曲線別分類\n"
    )
    new_unconfirmed = (
        "- 既知24円錐曲線より先の有理曲線の完全な特定、"
        "rank 20のNéron--Severi群内での高さ因子の明示、および"
        "各滑らかな楕円ファイバー上の群論的分類\n"
    )
    result = result.replace(old_unconfirmed, new_unconfirmed, 1)
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    text = args.input.read_text(encoding="utf-8")
    output = update(text)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(output, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
