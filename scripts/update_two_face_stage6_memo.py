#!/usr/bin/env python3
"""Insert or replace the stage-six height-theory section in the research memo."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


START = "<!-- TWO_FACE_STAGE6_START -->"
END = "<!-- TWO_FACE_STAGE6_END -->"
INSERT_BEFORE = "\n## 5. 一面成立曲面"


def f6(value: float) -> str:
    return f"{value:.6f}"


def build_section(report: dict[str, Any]) -> str:
    audit = report["finite_audit"]
    point_slack = audit["point_specific_slack_summary"]
    coarse_slack = audit["coarse_slack_summary"]
    lambda_ratio = audit["h_lambda_over_log_d_summary"]
    x_ratio = audit["H_x_over_8d2_summary"]
    xi_ratio = audit["H_xi_over_4d3_summary"]

    template = r"""<!-- TWO_FACE_STAGE6_START -->
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

保存済み@@POINT_COUNT@@点すべてについて、次を有理数の厳密演算で再検算した。

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
| 点別上界 $-\widehat h(P)$ | @@PS_MIN@@ | @@PS_MEDIAN@@ | @@PS_MEAN@@ | @@PS_MAX@@ |
| 一様上界 $-\widehat h(P)$ | @@CS_MIN@@ | @@CS_MEDIAN@@ | @@CS_MEAN@@ | @@CS_MAX@@ |

また有限標本では

- $h(\lambda)/\log d$ の最大値：@@LR_MAX@@
- $H(x)/(8d^2)$ の最大値：@@XR_MAX@@
- $H(\xi)/(4d^3)$ の最大値：@@XIR_MAX@@

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
"""

    replacements = {
        "@@POINT_COUNT@@": str(audit["point_count"]),
        "@@PS_MIN@@": f6(point_slack["min"]),
        "@@PS_MEDIAN@@": f6(point_slack["median"]),
        "@@PS_MEAN@@": f6(point_slack["mean"]),
        "@@PS_MAX@@": f6(point_slack["max"]),
        "@@CS_MIN@@": f6(coarse_slack["min"]),
        "@@CS_MEDIAN@@": f6(coarse_slack["median"]),
        "@@CS_MEAN@@": f6(coarse_slack["mean"]),
        "@@CS_MAX@@": f6(coarse_slack["max"]),
        "@@LR_MAX@@": f6(lambda_ratio["max"]),
        "@@XR_MAX@@": f6(x_ratio["max"]),
        "@@XIR_MAX@@": f6(xi_ratio["max"]),
    }
    for old, new in replacements.items():
        template = template.replace(old, new)
    return template


def update_memo(text: str, section: str) -> str:
    if START in text or END in text:
        if START not in text or END not in text:
            raise ValueError("only one stage-six marker is present")
        before, rest = text.split(START, 1)
        _, after = rest.split(END, 1)
        return before.rstrip() + "\n\n" + section + after
    if INSERT_BEFORE not in text:
        raise ValueError("could not find section-5 insertion point")
    return text.replace(INSERT_BEFORE, "\n\n" + section + INSERT_BEFORE, 1)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    report = json.loads(args.report.read_text(encoding="utf-8"))
    if not report.get("valid"):
        raise ValueError("stage-six report is not valid")
    text = args.input.read_text(encoding="utf-8")
    updated = update_memo(text, build_section(report))
    args.output.write_text(updated, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
