#!/usr/bin/env python3
"""Insert the Stage11 shared-p convolution audit into the research memo."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

START = "<!-- SHARED_P_CONVOLUTION_STAGE11_START -->"
END = "<!-- SHARED_P_CONVOLUTION_STAGE11_END -->"
INSERT_BEFORE = "## 5. 一面成立曲面 $V_{ab}$ の幾何"
CONFIRMED_HEADING = "### 確定\n"
UNCONFIRMED_HEADING = "### 未確認\n"
CONFIRMED_BULLET = (
    "- 共有面対角線$p$を軸にraw oriented chainが厳密な表現数畳み込みで書け、"
    "$m\\equiv2\\pmod{14}$、$n\\equiv1\\pmod{14}$の二変数primitive族から"
    "$N_1(B)\\gg B^{1/2}$という無条件下界が得られること\n"
)
UNCONFIRMED_BULLET = (
    "- 共有面対角線$p$の畳み込みにおけるprimitive補正と追加面成立補正を平均的に評価し、"
    "$N_2(B)$の上界または$N_2(B)=o(N_1(B))$へ接続できるか\n"
)


def convolution_table(report: dict[str, Any]) -> str:
    lines = [
        "| $B$ | raw convolution | primitive oriented chain | primitive unique点 | 面1本 | 面2本 |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for row in report["shared_p_convolution"]["rows"]:
        hist = row["face_count_histogram"]
        lines.append(
            "| {B:,} | {raw:,} | {prim:,} | {unique:,} | {one:,} | {two:,} |".format(
                B=row["B"],
                raw=row["raw_oriented_chains_convolution"],
                prim=row["primitive_oriented_chains"],
                unique=row["unique_primitive_cuboids"],
                one=int(hist.get("1", 0)),
                two=int(hist.get("2", 0)),
            )
        )
    return "\n".join(lines)


def family_examples(report: dict[str, Any]) -> str:
    examples = report["two_parameter_family"]["finite_validation"]["first_examples"][:6]
    lines = [
        "| $m$ | $n$ | $a$ | $b$ | $c$ | $d$ |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for row in examples:
        lines.append(
            f"| {row['m']} | {row['n']} | {row['a']:,} | {row['b']:,} | "
            f"{row['c']:,} | {row['d']:,} |"
        )
    return "\n".join(lines)


def rectangle_table(report: dict[str, Any]) -> str:
    lines = [
        "| $T$ | 実測coprime対 | $T^2/(24\\pi^2)$ | 実測/主項 |",
        "|---:|---:|---:|---:|",
    ]
    for row in report["coprime_rectangle_count"]["rows"]:
        lines.append(
            f"| {row['T']:,} | {row['coprime_parameter_pairs']:,} | "
            f"{row['main_term_T2_over_24pi2']:.3f} | "
            f"{row['ratio_to_predicted_main']:.6f} |"
        )
    return "\n".join(lines)


def build_section(report: dict[str, Any]) -> str:
    validation = report["two_parameter_family"]["finite_validation"]
    cross = report["two_parameter_family"]["stage9_cross_check"]
    template = r"""@@START@@
### 4.20 共有面対角線 $p$ の畳み込みと二変数下界【畳み込み・$B^{1/2}$下界は確定／$N_2$比較は未確認】

再現コードと生成レポートは

- [`scripts/audit_shared_p_convolution_stage11.py`](../scripts/audit_shared_p_convolution_stage11.py)
- [`data/shared_p_convolution_stage11_report.json`](../data/shared_p_convolution_stage11_report.json)

に保存する。Stage10の1変数族を一般のEuclidパラメータへ広げると同時に、Claudeの外部レビューで提案された共有面対角線 $p$ による表現数畳み込みを監査する。

#### 4.20.1 $p$を斜辺・脚として共有する厳密な畳み込み【確定】

正整数 $p$ に対し、$p$ を斜辺に持つ順序を無視した正のPythagorean tripleの個数を $H(p)$ とする。二平方表現数から

$$
r_2(p^2)=4\prod_{\substack{q\mid p\\q\equiv1\pmod4}}
\bigl(2v_q(p)+1\bigr)
$$

であり、軸上の4表現を除いて符号と順序の8重複を割ると

$$
\boxed{
H(p)=\frac12\left(
\prod_{\substack{q\mid p\\q\equiv1\pmod4}}
\bigl(2v_q(p)+1\bigr)-1
\right)
}.
$$

一方、$p$ を脚に持ち、斜辺 $d\le B$ となるPythagorean tripleの個数は

$$
L_B(p)=\#\left\{
u\mid p^2:
u<p,\quad
u\equiv\frac{p^2}{u}\pmod2,\quad
u+\frac{p^2}{u}\le2B
\right\}.
$$

ここで

$$
c=\frac{p^2/u-u}{2},\qquad
d=\frac{p^2/u+u}{2}
$$

である。一つの生成面には脚の向きが2通りあるため、primitive化・辺の相異性・重複除去を行う前のoriented chain総数は

$$
\boxed{
C_{\mathrm{raw}}(B)
=
2\sum_{p\le B}H(p)L_B(p)
}.
$$

$B\le20{,}000$ で、表現数公式・約数対公式・直接二段階列挙の三者を全件照合した。

@@CONVOLUTION_TABLE@@

#### 4.20.2 primitive unique点へ移る際の補正【構造は確定／平均評価は未確認】

primitiveかつ三辺相異なる点では、整数面対角線が $k$ 本ならoriented chainは $2k$ 個である。従って

$$
\boxed{
C_{\mathrm{prim}}(B)
=
2N_1(B)+4N_{=2}(B)+6N_3(B)
}.
$$

有限範囲では完全直方体が0件なので $N_3(B)=0$ だが、一般式では残しておく。

重要なのは、積 $H(p)L_B(p)$ がそのままprimitive unique点数ではないことである。第一・第二Pythagorean tripleを結合した後に

- $\gcd(a,b,c)=1$
- 三辺が相異なること
- 複数の生成面による重複度

を処理する必要がある。従ってClaude案はraw母集団を正確に分離する座標になるが、$N_1$や$N_2$の主項を直ちに与えるわけではない。

#### 4.20.3 二変数の一面のみ成立族【確定】

整数 $m,n$ が

$$
m>n\ge1,\qquad
m\equiv2\pmod{14},\qquad
n\equiv1\pmod{14},\qquad
\gcd(m,n)=1
$$

を満たすとする。次を置く。

$$
x=m^2-n^2,\qquad
y=2mn,\qquad
p=m^2+n^2,
$$

$$
c=\frac{p^2-1}{2},\qquad
d=\frac{p^2+1}{2}.
$$

合同条件から $m,n$ は異なる偶奇であり、Euclidの標準定理により $(x,y,p)$ はprimitive Pythagorean tripleである。また

$$
x^2+y^2=p^2,\qquad
p^2+c^2=d^2
$$

が恒等的に成り立つ。

$p\ge5$ なので $c>p>x,y$ であり、$x=y$ は $(m/n)^2-2(m/n)-1=0$ を要求して不可能である。従って $(a,b)=(\min(x,y),\max(x,y))$ とすれば常に

$$
a<b<c,\qquad \gcd(a,b,c)=1.
$$

法7では

$$
m\equiv2,\qquad n\equiv1
$$

なので

$$
x^2\equiv2,\qquad
y^2\equiv2,\qquad
p^2\equiv4,\qquad
c^2\equiv4\pmod7.
$$

従って残り二面はともに

$$
x^2+c^2\equiv y^2+c^2\equiv6\pmod7.
$$

法7の平方剰余は $\{0,1,2,4\}$ なので、両方とも整数平方ではない。この二変数族は常にprimitiveかつ**ちょうど一面のみ成立**する。

$m\le@@MAX_M@@$ の該当 @@VALIDATED@@ 対について整数演算で再検算し、全件通過した。Stage9の $d\le20{,}000$ 完全集合では $(m,n)=(@@CROSS_M@@,@@CROSS_N@@)$ の点 @@CROSS_POINT@@ と完全一致した。

@@FAMILY_EXAMPLES@@

#### 4.20.4 coprime対の計数と $N_1(B)$ の下界【確定】

$$
T<m\le2T,\qquad 1\le n\le T,
$$

$$
m\equiv2\pmod{14},\qquad n\equiv1\pmod{14}
$$

の長方形内で $\gcd(m,n)=1$ の対の個数を $C(T)$ とする。Möbius反転により

$$
C(T)
=
\sum_{\substack{e\ge1\\(e,14)=1}}
\mu(e)A_e(T)B_e(T),
$$

ここで $A_e,B_e$ は各区間・合同類で $e$ の倍数となる個数である。$(e,14)=1$ なら中国剰余定理から

$$
A_e(T)=\frac{T}{14e}+O(1),\qquad
B_e(T)=\frac{T}{14e}+O(1).
$$

従って

$$
C(T)
=
\frac{T^2}{196}
\sum_{\substack{e\ge1\\(e,14)=1}}
\frac{\mu(e)}{e^2}
+O(T\log T).
$$

Euler積は

$$
\sum_{\substack{e\ge1\\(e,14)=1}}
\frac{\mu(e)}{e^2}
=
\prod_{q\nmid14}\left(1-\frac1{q^2}\right)
=
\frac{49}{6\pi^2},
$$

したがって

$$
\boxed{
C(T)=\frac{T^2}{24\pi^2}+O(T\log T)
}.
$$

有限計算はこの主項の検算にのみ用いる。

@@RECTANGLE_TABLE@@

この長方形では

$$
p=m^2+n^2\le5T^2,
$$

$$
d=\frac{p^2+1}{2}\le\frac{25T^4+1}{2}.
$$

そこで

$$
T=
\left\lfloor
\left(\frac{2B-1}{25}\right)^{1/4}
\right\rfloor
$$

と取れば、各coprime対が $d\le B$ の相異なる一面のみ成立primitive点を与える。primitive Pythagorean tripleのEuclidパラメータは一意であるため、この写像は単射である。

従って

$$
\boxed{
N_1(B)
\ge
\frac{\sqrt2}{120\pi^2}B^{1/2}
-
O(B^{1/4}\log B)
}
$$

であり、

$$
\boxed{N_1(B)\gg B^{1/2}}
$$

という無条件下界を得る。Stage10の $B^{1/4}$ 下界を二変数化により改善した。

#### 4.20.5 研究判断【次は補正項の平均評価】

Stage11で確定したことは、

1. raw oriented chainが共有面対角線 $p$ に関する厳密な表現数畳み込みで書ける
2. primitive unique点へ移る際の補正内容が明示された
3. 固定合同類の二変数Euclid族がprimitiveかつちょうど一面のみ成立する
4. $N_1(B)\gg B^{1/2}$ という無条件下界が得られる

ことである。

一方、

- primitive補正を含む全 $N_1(B)$ の主項
- 二面以上成立を与える追加平方条件の平均的通過数
- $N_2(B)$ の新しい上界
- $N_2(B)=o(N_1(B))$

は未確認である。

次は外部AIへ、共有 $p$ 畳み込みにおけるprimitive補正と追加面成立補正をどの古典解析数論の道具で評価できるか、今回の式を基準に独立レビューさせる価値がある。
@@END@@
"""
    replacements = {
        "@@START@@": START,
        "@@END@@": END,
        "@@CONVOLUTION_TABLE@@": convolution_table(report),
        "@@FAMILY_EXAMPLES@@": family_examples(report),
        "@@RECTANGLE_TABLE@@": rectangle_table(report),
        "@@MAX_M@@": f"{validation['max_m']:,}",
        "@@VALIDATED@@": f"{validation['validated_parameter_count']:,}",
        "@@CROSS_M@@": str(cross["parameter"]["m"]),
        "@@CROSS_N@@": str(cross["parameter"]["n"]),
        "@@CROSS_POINT@@": str(tuple(cross["point"])),
    }
    for token, value in replacements.items():
        template = template.replace(token, value)
    return template


def replace_section(text: str, section: str) -> str:
    if START in text or END in text:
        if text.count(START) != 1 or text.count(END) != 1:
            raise ValueError("Stage11 markers are missing or duplicated")
        before, rest = text.split(START, 1)
        _, after = rest.split(END, 1)
        return before.rstrip() + "\n\n" + section.rstrip() + "\n" + after.lstrip("\n")
    if INSERT_BEFORE not in text:
        raise ValueError("section-5 insertion point not found")
    return text.replace(INSERT_BEFORE, section.rstrip() + "\n\n" + INSERT_BEFORE, 1)


def insert_bullet(text: str, heading: str, bullet: str) -> str:
    if bullet in text:
        return text
    if heading not in text:
        raise ValueError(f"conclusion heading not found: {heading!r}")
    return text.replace(heading, heading + "\n" + bullet, 1)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = json.loads(args.report.read_text(encoding="utf-8"))
    text = args.input.read_text(encoding="utf-8")
    text = replace_section(text, build_section(report))
    text = insert_bullet(text, CONFIRMED_HEADING, CONFIRMED_BULLET)
    text = insert_bullet(text, UNCONFIRMED_HEADING, UNCONFIRMED_BULLET)
    args.output.write_text(text.rstrip() + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
