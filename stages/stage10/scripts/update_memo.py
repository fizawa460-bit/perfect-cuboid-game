#!/usr/bin/env python3
"""Insert the Stage10 explicit one-face lower-bound family into the research memo."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

START = "<!-- ONE_FACE_LOWER_BOUND_STAGE10_START -->"
END = "<!-- ONE_FACE_LOWER_BOUND_STAGE10_END -->"
INSERT_BEFORE = "## 5. 一面成立曲面 $V_{ab}$ の幾何"
CONFIRMED_HEADING = "### 確定\n"
CONFIRMED_BULLET = (
    "- $m\\bmod14\\in\\{2,4,10,12\\}$ で与えられるprimitiveな一面のみ成立無限族が存在し、"
    "$N_1(B)\\gg B^{1/4}$ という無条件下界が得られること\n"
)
STAGE9_UNCONFIRMED_BULLET = (
    "- 二段階約数鎖上の追加平方条件を、標準的なsquare sieveへ接続できる低次元再パラメータ化、"
    "または漸近的に多数の一面のみ成立点を与える固定合同部分族が存在するか\n"
)
STAGE9_RESOLUTION_NOTE = (
    "  - Stage10追補：後者の固定合同部分族は4.19節で構成した。"
    "未確認なのは、より強い$N_1(B)$下界・主項とsquare sieveへ接続する再パラメータ化である。\n"
)


def example_table(report: dict[str, Any]) -> str:
    rows = report["finite_validation"]["first_examples"][:6]
    lines = [
        "| $m$ | $a$ | $b$ | $c$ | $d$ | 残り二面の法7剰余 |",
        "|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        residues = ", ".join(str(value) for value in row["remaining_face_residues_mod_7"])
        lines.append(
            f"| {row['m']} | {row['a']:,} | {row['b']:,} | "
            f"{row['c']:,} | {row['d']:,} | {residues} |"
        )
    return "\n".join(lines)


def bound_table(report: dict[str, Any]) -> str:
    lines = [
        "| $B$ | $\\lfloor B^{1/4}\\rfloor$ | 証明から保証される族の点数 | 族の実際の点数 |",
        "|---:|---:|---:|---:|",
    ]
    for row in report["lower_bound"]["rows"]:
        lines.append(
            f"| {row['B']:,} | {row['floor_B_fourth_root']:,} | "
            f"{row['explicit_guaranteed_count']:,} | {row['exact_family_count']:,} |"
        )
    return "\n".join(lines)


def build_section(report: dict[str, Any]) -> str:
    validation = report["finite_validation"]
    cross_check = report["stage9_cross_check"]
    successful = report["congruence_certificate"]["successful_even_classes_mod_14"]

    template = r"""@@START@@
### 4.19 一面のみ成立する明示的無限族と $N_1(B)$ の下界【無条件に確定】

再現コードと生成レポートは

- [`scripts/audit_one_face_lower_bound_stage10.py`](../scripts/audit_one_face_lower_bound_stage10.py)
- [`data/one_face_lower_bound_stage10_report.json`](../data/one_face_lower_bound_stage10_report.json)

に保存する。Stage9では法7の合同証明書を満たす有限点が多数見つかったが、その剰余類に属するprimitive点が無限に存在することは未証明だった。本節では二つのPythagorean tripleを最も単純な形で連結し、その空白を埋める。

#### 4.19.1 明示族【確定】

整数 $m\ge2$ が

$$
m\bmod14\in\{@@CLASSES@@\}
$$

を満たすとする。特に $m$ は偶数である。まず

$$
x=2m,\qquad y=m^2-1,\qquad p=m^2+1
$$

と置くと、

$$
x^2+y^2=p^2
$$

である。次に奇数 $p$ を脚とする標準的な直角三角形を接続し、

$$
c=\frac{p^2-1}{2}
 =\frac{m^2(m^2+2)}{2},
\qquad
d=\frac{p^2+1}{2}
 =\frac{m^4+2m^2+2}{2}
$$

と置く。このとき

$$
p^2+c^2=d^2
$$

であり、従って

$$
x^2+y^2+c^2=d^2.
$$

$a=\min(x,y)$、$b=\max(x,y)$ と正規化すれば、$(a,b,c,d)$ は空間対角線が整数の直方体を与える。

#### 4.19.2 primitive性と順序【確定】

$m$ は偶数なので $m^2-1$ は奇数であり、

$$
\gcd(2m,m^2-1)=1.
$$

実際、奇素数が両者を割れば $m$ と $m^2-1$ を同時に割ることになり不可能で、因子2も $m^2-1$ を割らない。従って

$$
\gcd(a,b,c)=1.
$$

また

$$
c-(m^2-1)=\frac{m^4}{2}+1>0,
$$

$$
c-2m=\frac{m(m^3+2m-4)}{2}>0
\qquad(m\ge2)
$$

である。$m^2-1=2m$ も整数解を持たないため、常に

$$
a<b<c.
$$

#### 4.19.3 法7による残り二面の排除【確定】

法7の平方剰余は

$$
\{0,1,2,4\}
$$

である。$q=m^2\bmod7$ と置く。許された4合同類では $q=2$ または $q=4$ であり、次の二場合だけを確認すればよい。

| $q=m^2\bmod7$ | $x^2\bmod7$ | $y^2\bmod7$ | $c^2\bmod7$ | $x^2+c^2$ | $y^2+c^2$ |
|---:|---:|---:|---:|---:|---:|
| 2 | 1 | 1 | 2 | 3 | 3 |
| 4 | 2 | 2 | 4 | 6 | 6 |

3と6はいずれも法7の平方剰余ではない。従って

$$
x^2+c^2\ne\square,\qquad y^2+c^2\ne\square
$$

が整数上で従う。一方 $x^2+y^2=p^2$ は恒等的に平方であるため、この族は常に**ちょうど一面のみ成立**する。

#### 4.19.4 再現監査【有限計算】

$m\le@@MAX_M@@$ の許容パラメータ @@PARAM_COUNT@@ 個について、Pythagorean恒等式、空間対角線、primitive性、順序、二つの非平方条件を整数演算で再検算した。

@@EXAMPLE_TABLE@@

Stage9の完全列挙 $d\le@@STAGE9_BOUND@@$ との照合では、$m=@@STAGE9_PARAMETERS@@$ に対応する @@STAGE9_COUNT@@ 点がすべて `ab_only` として存在し、分類不一致はなかった。この有限照合は証明そのものではなく、実装と既存母集団の整合性確認である。

#### 4.19.5 無条件下界【確定】

高さは

$$
d(m)=\frac{m^4+2m^2+2}{2}
$$

であり、$m>0$ で狭義単調増加する。また $m\ge2$ なら

$$
d(m)\le m^4.
$$

$T=\lfloor B^{1/4}\rfloor$ と置けば、許容合同類に属する各 $m\le T$ は $d(m)\le B$ の相異なる一面のみ成立primitive点を与える。従って

$$
N_1(B)\ge
\sum_{r\in\{2,4,10,12\}}
\max\left(
0,\,
1+\left\lfloor\frac{\lfloor B^{1/4}\rfloor-r}{14}\right\rfloor
\right).
$$

特に

$$
\boxed{
N_1(B)\ge\frac{2}{7}B^{1/4}-O(1)
}
$$

であり、

$$
\boxed{N_1(B)\gg B^{1/4}}
$$

という無条件下界を得る。

@@BOUND_TABLE@@

#### 4.19.6 研究上の意味と次の分岐

Stage9で未確認だった「固定合同類の中にprimitiveな一面のみ成立無限族が存在するか」は肯定的に解決した。これは $N_1(B)$ に対する最初の無条件な冪下界である。

ただし、次は主張しない。

- この $B^{1/4}$ が $N_1(B)$ の正しい増大次数であること
- $N_2(B)$ に対する新しい上界
- $N_2(B)=o(N_1(B))$
- 現在の約数鎖表示へsquare sieveまたはdeterminant methodが直接適用できること

次の主候補は、共有面対角線 $p$ を軸に、

1. $p$ を斜辺に持つPythagorean tripleの表現数
2. $p$ を脚に持つPythagorean tripleの表現数

を畳み込んで、一面以上成立母集団と一面のみ成立部分族を古典解析数論の形で評価できるか監査することである。明示族はこの畳み込み空間内の最も単純な1パラメータ切片と解釈できる。
@@END@@
"""
    replacements = {
        "@@START@@": START,
        "@@END@@": END,
        "@@CLASSES@@": ",".join(str(value) for value in successful),
        "@@MAX_M@@": f"{validation['max_m']:,}",
        "@@PARAM_COUNT@@": f"{validation['eligible_parameter_count']:,}",
        "@@EXAMPLE_TABLE@@": example_table(report),
        "@@STAGE9_BOUND@@": f"{cross_check['bound']:,}",
        "@@STAGE9_PARAMETERS@@": ",".join(str(value) for value in cross_check["parameters"]),
        "@@STAGE9_COUNT@@": str(cross_check["matched_count"]),
        "@@BOUND_TABLE@@": bound_table(report),
    }
    for token, value in replacements.items():
        template = template.replace(token, value)
    return template


def replace_section(text: str, section: str) -> str:
    if START in text or END in text:
        if START not in text or END not in text:
            raise ValueError("only one Stage10 marker is present")
        before, rest = text.split(START, 1)
        _, after = rest.split(END, 1)
        return before.rstrip() + "\n\n" + section.rstrip() + "\n" + after.lstrip("\n")
    if INSERT_BEFORE not in text:
        raise ValueError("section-5 insertion point not found")
    return text.replace(INSERT_BEFORE, section.rstrip() + "\n\n" + INSERT_BEFORE, 1)


def insert_bullet(text: str) -> str:
    if CONFIRMED_BULLET in text:
        return text
    if CONFIRMED_HEADING not in text:
        raise ValueError("confirmed conclusion heading not found")
    return text.replace(CONFIRMED_HEADING, CONFIRMED_HEADING + "\n" + CONFIRMED_BULLET, 1)


def insert_resolution_note(text: str) -> str:
    if STAGE9_RESOLUTION_NOTE in text:
        return text
    if STAGE9_UNCONFIRMED_BULLET not in text:
        raise ValueError("Stage9 unconfirmed conclusion bullet not found")
    return text.replace(
        STAGE9_UNCONFIRMED_BULLET,
        STAGE9_UNCONFIRMED_BULLET + STAGE9_RESOLUTION_NOTE,
        1,
    )


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
    text = insert_bullet(text)
    text = insert_resolution_note(text)
    args.output.write_text(text.rstrip() + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
