#!/usr/bin/env python3
"""Insert the reproducible stage-three Mordell-Weil audit into the research memo."""

from __future__ import annotations

import argparse
from pathlib import Path


START = "### 4.12 楕円ファイバー上のMordell–Weil関係"
END = "\n## 5. 一面成立曲面 $V_{ab}$ の幾何"

SECTION = r"""### 4.12 楕円ファイバー上のMordell–Weil関係【有限データは確定／大域計数は未証明】

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
"""


def patch(text: str) -> str:
    if END not in text:
        raise ValueError("section 5 marker was not found")
    if START in text:
        prefix = text.split(START, 1)[0]
        suffix = END + text.split(END, 1)[1]
        text = prefix + SECTION + suffix
    else:
        text = text.replace(END, "\n\n" + SECTION + END, 1)

    confirmed_anchor = (
        "- 正の整数領域では射影max-heightが $H=d$ となること\n"
    )
    confirmed_addition = (
        "- 255点すべてがvan LuijkのWeierstrassファイバーへ写り、"
        "複数点50ファイバーの特殊化rankが30本で1、20本で2と確定したこと\n"
    )
    if confirmed_addition not in text and confirmed_anchor in text:
        text = text.replace(
            confirmed_anchor, confirmed_anchor + confirmed_addition, 1
        )

    unchecked_anchor = (
        "- 二面成立数の無条件上界および $N_2(D)=o(N_1(D))$ の証明\n"
    )
    unchecked_addition = (
        "- 高さ $H=d$ と楕円曲線のcanonical heightの一様比較、および"
        "未観測ファイバーを含む一様なrank・点数評価\n"
    )
    if unchecked_addition not in text and unchecked_anchor in text:
        text = text.replace(
            unchecked_anchor, unchecked_anchor + unchecked_addition, 1
        )
    return text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source = args.input.read_text(encoding="utf-8")
    result = patch(source)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(result, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
