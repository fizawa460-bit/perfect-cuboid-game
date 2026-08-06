#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

START = "<!-- SHARED_P_AVERAGE_STAGE12_N1_2B_START -->"
END = "<!-- SHARED_P_AVERAGE_STAGE12_N1_2B_END -->"


def render(report: dict) -> str:
    rows = report["finite_rows"]
    lines = [
        START,
        "## 4.26 Stage12-N1-2b：乗法重みの共有素因子補正",
        "",
        "### 4.26.1 厳密分解【確定】",
        "",
        "Stage12-N1-2 の座標で $p=hrs$、$(r,s)=1$ とする。",
        "",
        "$$",
        "G(n)=\\prod_{q\\mid n,\\ q\\equiv1\\ (4)}(2v_q(n)+1)",
        "$$",
        "",
        "とおく。$a=v_q(h)$、$b=v_q(rs)$ に対し",
        "",
        "$$",
        "K_q(a,b)=\\frac{2(a+b)+1}{(2a+1)(2b+1)}",
        "$$",
        "",
        "と定義すると、厳密に",
        "",
        "$$",
        "\\boxed{G(hrs)=G(h)G(r)G(s)K(h,rs)}",
        "$$",
        "",
        "$$",
        "K(h,rs)=\\prod_{\\substack{q\\equiv1\\ (4)\\\\q\\mid(h,rs)}}K_q(v_q(h),v_q(rs))",
        "$$",
        "",
        "となる。$0<K\\le1$ であり、$K=1$ となるのは $q\\equiv1\\pmod4$ の素数が $h$ と $rs$ に共有されない場合に限る。$2$ および $3\\pmod4$ の共有素因子は $G$ に影響しない。",
        "",
        "### 4.26.2 有限監査",
        "",
        "| $B$ | exact raw | 分離積による上界 | 補正損失 | 上界/exact |",
        "|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['B']:,} | {row['exact_raw_weight']:,} | {row['naive_separated_weight']:,} | "
            f"{row['overlap_correction_loss']:,} | {row['naive_over_exact_ratio']:.6f} |"
        )
    lines += [
        "",
        f"全 {report['audit_counts']['exact_identity_checks']:,} 件で局所補正式を検算した。有限比率を漸近密度とは解釈しない。",
        "",
        "### 4.26.3 解析上の現在地",
        "",
        "共有素因子による非乗法性は、$q\\equiv1\\pmod4$ にのみ支えられた明示的局所因子 $K$ へ隔離された。従って",
        "",
        "$$",
        "G(hrs)\\le G(h)G(r)G(s)",
        "$$",
        "",
        "が無条件に成り立つ。ただし、補正損失の総和が主項より低次であることは未証明である。次に必要なのは、二次領域上の分離積平均と、共有 $1\\pmod4$ 素数の総寄与を一様に制御する補題である。",
        "",
        "判定は `A_local_correction_isolated_mean_value_still_open` とする。",
        "",
        END,
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    text = args.input.read_text(encoding="utf-8")
    block = render(json.loads(args.report.read_text(encoding="utf-8")))
    if START in text and END in text:
        before, rest = text.split(START, 1)
        _, after = rest.split(END, 1)
        text = before.rstrip() + "\n\n" + block + after.lstrip("\n")
    else:
        marker = "## 5. 一面成立曲面"
        if marker not in text:
            raise SystemExit("insertion marker not found")
        text = text.replace(marker, block + "\n" + marker, 1)
    args.output.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
