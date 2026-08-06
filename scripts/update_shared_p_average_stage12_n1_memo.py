#!/usr/bin/env python3
"""Insert Stage12-N1 shared-p average audit into the research memo."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

START = "<!-- SHARED_P_AVERAGE_STAGE12_N1_START -->"
END = "<!-- SHARED_P_AVERAGE_STAGE12_N1_END -->"
INSERT_BEFORE = "## 5. 一面成立曲面 $V_{ab}$ の幾何"


def raw_table(report: dict[str, Any]) -> str:
    lines = [
        "| $B$ | $C_{raw}(B)$ | $C_{raw}/B$ | $C_{raw}/(B\\log B)$ | $H L_B>0$ の$p$数 |",
        "|---:|---:|---:|---:|---:|",
    ]
    for row in report["finite_raw_average"]["rows"]:
        lines.append(
            f"| {row['B']:,} | {row['C_raw']:,} | {row['C_raw_over_B']:.6f} | "
            f"{row['C_raw_over_B_log_B']:.6f} | {row['support_product']:,} |"
        )
    return "\n".join(lines)


def primitive_table(report: dict[str, Any]) -> str:
    lines = [
        "| $B$ | raw oriented | primitive oriented | 有限保持率 | primitive unique点 |",
        "|---:|---:|---:|---:|---:|",
    ]
    for row in report["primitive_retention"]["rows"]:
        lines.append(
            f"| {row['B']:,} | {row['C_raw_direct']:,} | "
            f"{row['primitive_oriented_chains']:,} | "
            f"{row['primitive_retention_ratio']:.6f} | "
            f"{row['unique_primitive_cuboids']:,} |"
        )
    return "\n".join(lines)


def scaling_table(report: dict[str, Any]) -> str:
    lines = [
        "| $B$ | $t\\le B/13$ | この族のraw oriented | primitiveとなる$t$数 |",
        "|---:|---:|---:|---:|",
    ]
    for row in report["scaling_trap"]["rows"]:
        lines.append(
            f"| {row['B']:,} | {row['parameters_t']:,} | "
            f"{row['oriented_raw_chains']:,} | {row['primitive_parameters']:,} |"
        )
    return "\n".join(lines)


def build_section(report: dict[str, Any]) -> str:
    return f"""{START}
### 4.21 Stage12-N1：共有 $p$ 畳み込みの平均構造【raw成長は確認／primitiveへの移行が壁】

再現コードと生成レポートは

- [`scripts/audit_shared_p_average_stage12_n1.py`](../scripts/audit_shared_p_average_stage12_n1.py)
- [`data/shared_p_average_stage12_n1_report.json`](../data/shared_p_average_stage12_n1_report.json)

に保存する。Stage11で得た

$$
C_{{\\mathrm{{raw}}}}(B)=2\\sum_{{p\\le B}}H(p)L_B(p)
$$

をMeta AI案に沿って平均値問題として監査した。ただし、raw chainの下界とprimitive unique点の下界を明確に分離する。

#### 4.21.1 有限平均監査【有限範囲で確定／漸近式ではない】

$H(p)$、$L_B(p)$をStage11の厳密公式から再計算し、$B\\le200,000$で積和を集計した。

{raw_table(report)}

この範囲では $C_{{\\mathrm{{raw}}}}(B)/(B\\log B)$ は増加しているが、極限値や $B\\log B$ 漸近を主張しない。寄与は最大素因子が小さい $p$ に強く集中しており、smooth数・高約数数がraw平均に重要であるというMeta AIの着眼は有限データ上で支持される。

#### 4.21.2 raw線形下界は容易だがprimitive下界にはならない【確定】

任意の整数 $t\\ge1$ に対して

$$
(3t)^2+(4t)^2=(5t)^2,
$$

$$
(5t)^2+(12t)^2=(13t)^2.
$$

従って $13t\\le B$ なら、共有対角線 $p=5t$ から2個のoriented raw chainが得られる。よって

$$
\\boxed{{C_{{\\mathrm{{raw}}}}(B)\\ge2\\left\\lfloor\\frac{{B}}{{13}}\\right\\rfloor}}.
$$

しかし生成される直方体は

$$
(3t,4t,12t,13t)
$$

であり、三辺の最大公約数は正確に $t$ である。従ってこの線形raw族のうちprimitiveなのは $t=1$ の一点だけである。

{scaling_table(report)}

これはMeta AI案の核心的な注意点である。$C_{{\\mathrm{{raw}}}}(B)\\gg B$、さらにはそれ以上のraw下界を示しても、拡大コピーが主寄与なら $N_1(B)$ は全く改善しない。

#### 4.21.3 primitive補正は主項級の問題【有限監査】

Stage11と同じ完全列挙を $B\\le20,000$ で再実行した。

{primitive_table(report)}

有限保持率を漸近密度とは解釈しない。ただし、rawからprimitiveへ移る際の損失が無視できる境界補正ではなく、主要な研究対象であることは明確である。単純な $1/\\zeta(2)$ 定数を仮定してはならない。

#### 4.21.4 Meta AI案への判定【第一タスクは壁まで到達】

確定したこと：

1. 共有 $p$ 畳み込みは解析数論の自然な平均値問題である
2. smooth・高約数型の $p$ が有限raw寄与の大部分を担う
3. raw chainには極めて簡単な線形下界がある
4. しかし、その線形下界全体がprimitive化で一点へ潰れる明示例がある

未確認のこと：

- $C_{{\\mathrm{{raw}}}}(B)$ の真の漸近式
- primitive-compatibleな共有 $p$ 畳み込みの平均値
- raw平均からStage11の $N_1(B)\\gg B^{{1/2}}$ を改善できるか

従って、このN1枝を続けるための次の対象は $H(p)L_B(p)$ そのものではなく、**二つのPythagorean tripleを結合した後のgcdを記録するprimitive-compatible joint weight** である。Möbius反転または原始表現数への分解が、この補正を実際に閉じられるかが次の分岐判定になる。
{END}
"""


def replace_section(text: str, section: str) -> str:
    if START in text or END in text:
        if text.count(START) != 1 or text.count(END) != 1:
            raise ValueError("Stage12-N1 markers are missing or duplicated")
        before, rest = text.split(START, 1)
        _, after = rest.split(END, 1)
        return before.rstrip() + "\n\n" + section.rstrip() + "\n\n" + after.lstrip("\n")
    if INSERT_BEFORE not in text:
        raise ValueError("section-5 insertion point not found")
    return text.replace(INSERT_BEFORE, section.rstrip() + "\n\n" + INSERT_BEFORE, 1)


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
    args.output.write_text(
        replace_section(text, build_section(report)).rstrip() + "\n", encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
