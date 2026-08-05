#!/usr/bin/env python3
"""Insert the stage-seven inverse-height audit into the canonical research memo."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


START = "<!-- TWO_FACE_STAGE7_START -->"
END = "<!-- TWO_FACE_STAGE7_END -->"
INSERT_BEFORE = "## 5. 一面成立曲面 $V_{ab}$ の幾何"
CONFIRMED_HEADING = "### 確定\n"
CONFIRMED_BULLET = (
    "- 二面成立楕円ファイバーの正の滑らかな整数点について、明示的な逆写像と "
    "$\\log d\\le6h(x)+12h(\\lambda)+10\\log2$ が成立し、Silvermanの高さ差定理から "
    "$\\log d\\le12\\widehat h(P)+C_\\lambda h(\\lambda)+C_0$ 型の有効な混合逆向き評価が従うこと\n"
)
OLD_UNRESOLVED = (
    "- canonical heightから $d$ への逆向き一様下界、および未観測ファイバーを含む"
    "一様なrank・regulator・点数評価"
)
NEW_UNRESOLVED = (
    "- $h(\\lambda)$ を含まないcanonical heightから $d$ への逆向き評価、"
    "混合評価の $h(\\lambda)$ 係数を計数に有効な範囲まで小さくすること、"
    "および未観測ファイバーを含む一様または平均的なrank・regulator・点数評価"
)


def f6(value: float) -> str:
    return f"{value:.6f}"


def build_section(report: dict[str, Any]) -> str:
    finite = report["finite_audit"]
    raw = finite["raw_inverse_slack_summary"]
    combined = finite["combined_inverse_slack_summary"]
    pure = finite["log_d_minus_12_canonical_summary"]
    lambda_share = finite["h_lambda_over_log_d_summary"]
    return f"""{START}
### 4.16 逆写像と逆向き高さ評価の実現可能性【明示的逆写像・naive height評価は確定／大域計数は未解決】

再現コードと全255点の出力は

- [`scripts/audit_two_face_inverse_height_stage7.py`](../scripts/audit_two_face_inverse_height_stage7.py)
- [`data/two_face_cuboids_1e6_stage7_inverse_height_report.json`](../data/two_face_cuboids_1e6_stage7_inverse_height_report.json)

に保存する。前節では $d$ からcanonical heightへの上界を得た。本節では逆方向を調べ、どこまで進められるかと、どこで別の入力が必要になるかを切り分ける。

#### 4.16.1 Weierstrassモデルからface-cuboid座標への逆写像【確定】

$$
E_t:\quad y^2=x(x+4t^2)(x+(1+t^2)^2),\qquad t=\\lambda
$$

とする。正の滑らかなaffine openでは、標準face-cuboid座標への逆写像は射影的に

$$
\\begin{{aligned}}
A&=2xy(1-t^2),\\\\
B&=x\\left(4t^2(1+t^2)^2-x^2\\right),\\\\
C&=4txy,\\\\
X&=y^2-x^2(1-t^2)^2,\\\\
Y&=2xy(1+t^2),\\\\
U&=y^2+x^2(1-t^2)^2
\\end{{aligned}}
$$

で与えられる。ここで右辺6個は共通の射影スカラー倍を許す。これらを楕円曲線方程式で簡約すると

$$
A^2+C^2=Y^2,\qquad B^2+C^2=X^2,\qquad A^2+X^2=U^2
$$

および

$$
t=\frac{{Y-A}}{{C}}=\frac{{C}}{{Y+A}},
$$

$$
x=4t^2\frac{{U-B}}{{X+B}},\qquad
y=8t^3\frac{{(U+X)(U-B)}}{{C(X+B)}}
$$

が戻る。SymPyによる多項式剰余計算と、保存済み255点の有理数厳密演算の双方で検算した。255点すべてで逆写像をprimitive整数ベクトルへ正規化すると、保存済み $[A:B:C:X:Y:U]$ と完全一致した。

#### 4.16.2 射影高さの明示的逆向き評価【確定】

上の6座標を $(t,x,y)$ の有理数表示で同時に斉次化すると、多重次数は高々

$$
(\\deg_t,\\deg_x,\\deg_y)=(6,3,2)
$$

であり、各座標多項式の係数絶対値和の最大は16である。primitive整数座標では $U=d$ が射影max-heightなので、通常の有理数heightの積・和の評価から

$$
\\boxed{{
\\log d\le6h(t)+3h(x)+2h(y)+\\log16
}}.
$$

一方、Weierstrass方程式から

$$
2h(y)\le3h(x)+6h(t)+6\\log2
$$

である。従って

$$
\\boxed{{
\\log d\le6h(x)+12h(\\lambda)+10\\log2
}}.
$$

これは有限標本の回帰ではなく、対象open上の全有理点に対する明示的不等式である。

#### 4.16.3 canonical heightへの橋【既知定理を用いた有効評価】

整数モデル

$$
\\eta^2=\\xi(\\xi+4m^2n^2)(\\xi+(m^2+n^2)^2),\qquad \\lambda=m/n
$$

について、$c_4$、判別式 $\\Delta$、$j$ は明示的に計算できる。$0<m<n$ とすると

$$
c_4\le512n^8,\qquad
\\Delta\le4096n^{{24}},\qquad
h(j)\le24h(\\lambda)+27\\log2.
$$

Silverman, *The difference between the Weil height and the canonical height on elliptic curves*, Math. Comp. 55 (1990), Theorem 1.1 は、$\\widehat h(P)-\\frac12h(x(P))$ を積分Weierstrass方程式の判別式と $j$-invariantで有効に評価する。上の不変量評価と組み合わせると、絶対的で有効な定数 $C_\\lambda,C_0$ が存在して

$$
\\boxed{{
\\log d\le12\\widehat h(P)+C_\\lambda h(\\lambda)+C_0
}}
$$

が従う。従って「逆向き高さ評価そのものが存在しない」という障害ではない。

ただし、本段階ではSilvermanの $p(E)$ に含まれる全規格化項をコードへ転記していないため、$C_\\lambda$ の数値は固定しない。定理の存在だけを使って係数を小さく見積もることもしない。

#### 4.16.4 255点での再監査【有限集合について確定】

全255点で逆写像、射影正規化、不変量式、三つのheight上界を再検算し、全件が通過した。理論上界と実値の差は次である。

| 指標 | 最小 | 中央値 | 平均 | 最大 |
|---|---:|---:|---:|---:|
| $6h(\\lambda)+3h(x)+2h(y)+\\log16-\\log d$ | {f6(raw['min'])} | {f6(raw['median'])} | {f6(raw['mean'])} | {f6(raw['max'])} |
| $6h(x)+12h(\\lambda)+10\\log2-\\log d$ | {f6(combined['min'])} | {f6(combined['median'])} | {f6(combined['mean'])} | {f6(combined['max'])} |
| $\\log d-12\\widehat h(P)$ | {f6(pure['min'])} | {f6(pure['median'])} | {f6(pure['mean'])} | {f6(pure['max'])} |

有限標本での $h(\\lambda)/\\log d$ は {f6(lambda_share['min'])} から {f6(lambda_share['max'])} の範囲だった。これらの数値は、上界の正しさの再検算には使うが、将来の点に対する漸近法則とは解釈しない。

#### 4.16.5 分岐点としての結論【次は方針選択が必要】

逆写像と混合高さ比較は構成できた。しかし、現在の評価には正の $h(\\lambda)$ 項が残る。前節の

$$
h(\\lambda)\le\frac12\\log(2d)
$$

を代入して $\\log d$ を左辺へ戻すには、最終的な $h(\\lambda)$ の係数を2未満まで下げる必要がある。今回の粗い明示式はこの水準から遠く、Silvermanの補正項も $h(\\lambda)$ に依存する。

従って次の選択肢は二つである。

1. 逆写像と局所heightをさらに利用し、正の整数点に限定して $h(\\lambda)$ 係数を劇的に改善できるか調べる
2. ファイバーごとの一様評価に固執せず、$\\lambda$ 全体についてrank、regulator、局所可解性、合同条件を平均化して総和を直接抑える

これは低優先度の残件処理ではなく、最終計数へ向かうルートの分岐である。逆向き評価の実現可能性調査という当初の目的は本節で完了したため、次段階へ進む前に研究方針を壁打ちするのが妥当である。

二面成立数の無条件上界および

$$
N_2(B)=o(N_1(B))
$$

は依然として未証明である。
{END}
"""


def update_section(text: str, section: str) -> str:
    if START in text or END in text:
        if START not in text or END not in text:
            raise ValueError("only one stage-seven marker is present")
        before, rest = text.split(START, 1)
        _, after = rest.split(END, 1)
        return before.rstrip() + "\n\n" + section + after
    if INSERT_BEFORE not in text:
        raise ValueError("could not find section-5 insertion point")
    return text.replace(INSERT_BEFORE, "\n\n" + section + "\n" + INSERT_BEFORE, 1)


def update_conclusion(text: str) -> str:
    if CONFIRMED_BULLET not in text:
        if CONFIRMED_HEADING not in text:
            raise ValueError("confirmed conclusion heading not found")
        text = text.replace(
            CONFIRMED_HEADING,
            CONFIRMED_HEADING + "\n" + CONFIRMED_BULLET,
            1,
        )
    if OLD_UNRESOLVED in text:
        text = text.replace(OLD_UNRESOLVED, NEW_UNRESOLVED, 1)
    elif NEW_UNRESOLVED not in text:
        raise ValueError("unresolved inverse-height conclusion bullet not found")
    return text


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = json.loads(args.report.read_text(encoding="utf-8"))
    if not report.get("valid"):
        raise ValueError("stage-seven report is not valid")
    text = args.input.read_text(encoding="utf-8")
    updated = update_section(text, build_section(report))
    updated = update_conclusion(updated)
    args.output.write_text(updated, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
