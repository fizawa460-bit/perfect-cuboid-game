#!/usr/bin/env python3
"""Insert the Stage12-N1c global Mobius inversion audit into the memo."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

START = "<!-- SHARED_P_GLOBAL_MOBIUS_STAGE12_N1C_START -->"
END = "<!-- SHARED_P_GLOBAL_MOBIUS_STAGE12_N1C_END -->"
ANCHOR = "\n## 5. 一面成立曲面 $V_{ab}$ の幾何"


def render(report: dict) -> str:
    checks = report["checks"]
    rows = report["finite_rows"]
    lines = [
        START,
        "## 4.23 Stage12-N1c：primitive補正のglobal Möbius反転",
        "",
        "再現コードと生成レポートは",
        "",
        "- [`scripts/audit_shared_p_global_mobius_stage12_n1c.py`](../scripts/audit_shared_p_global_mobius_stage12_n1c.py)",
        "- [`data/shared_p_global_mobius_stage12_n1c_report.json`](../data/shared_p_global_mobius_stage12_n1c_report.json)",
        "",
        "に保存する。4.22のjoint weightをさらに縮約すると、primitive補正はraw畳み込み自身のMöbius反転になる。",
        "",
        "### 4.23.1 $A_k$と$B_{k,B}$のスケーリング【確定】",
        "",
        "第一三角形の脚がともに$k$で割れるなら、斜辺$p$も$k$で割れ、$k$で割った三角形は斜辺$p/k$を持つ。従って",
        "",
        r"$$\boxed{A_k(p)=\begin{cases}H(p/k),&k\mid p,\\0,&k\nmid p.\end{cases}}$$",
        "",
        r"同様に$k\mid p$かつ$k\mid c$なら$d$も$k$で割れ、第二三角形を$k$で割れるため",
        "",
        r"$$\boxed{B_{k,B}(p)=L_{\lfloor B/k\rfloor}(p/k)}$$",
        "",
        f"を得る。有限監査では$A_k$を{checks['A_identity_cases']:,}ケース、$B_{{k,B}}$を{checks['B_identity_cases']:,}ケース検算し、相違は0件だった。",
        "",
        "### 4.23.2 joint weightの縮約【確定】",
        "",
        "4.22のMöbius式へ代入すると",
        "",
        r"$$\boxed{J_B(p)=\sum_{k\mid p}\mu(k)H(p/k)L_{\lfloor B/k\rfloor}(p/k)}$$",
        "",
        "となる。つまりprimitive-compatible joint weightは、新しい未知関数ではなく、Stage11の$H$と$L$のスケール付きMöbius和である。",
        "",
        "### 4.23.3 global Möbius反転【確定】",
        "",
        r"等辺を除いたraw oriented chain数を$C_{\mathrm{dist,raw}}(B)$、primitive oriented chain数を$C_{\mathrm{prim}}(B)$とする。任意のdistinct raw chainは三辺gcdで一意にprimitive chainの拡大へ分解されるため",
        "",
        r"$$C_{\mathrm{dist,raw}}(B)=\sum_{k\le B}C_{\mathrm{prim}}(\lfloor B/k\rfloor).$$",
        "",
        "従ってMöbius反転により",
        "",
        r"$$\boxed{C_{\mathrm{prim}}(B)=\sum_{k\le B}\mu(k)C_{\mathrm{dist,raw}}(\lfloor B/k\rfloor)}.$$$",
        "",
        "この式はprimitive補正を局所密度の推測ではなく、完全に厳密な算術反転として与える。",
        "",
        "### 4.23.4 有限完全照合【有限範囲で確定】",
        "",
        "| $B$ | raw全体 | distinct raw | 等辺raw | global Möbius値 | Stage11 primitive |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['B']:,} | {row['raw_all_oriented']:,} | {row['raw_distinct_oriented']:,} | "
            f"{row['raw_repeated_side_oriented']:,} | {row['global_mobius_of_distinct_raw']:,} | "
            f"{row['stage11_primitive_oriented']:,} |"
        )
    lines += [
        "",
        "全閾値でglobal Möbius値はStage11のprimitive oriented countと完全一致した。監査範囲では等辺raw chainは0件だが、一般の不存在は主張しない。",
        "",
        "### 4.23.5 N1枝の現在地【代数的補正は完了／解析的誤差が最後の壁】",
        "",
        "Stage12-N1ではrawからprimitiveへの補正が未知の壁だった。4.22と4.23により、その補正は代数的には完全に閉じた。残る問題は",
        "",
        r"$$C_{\mathrm{dist,raw}}(B)$$",
        "",
        r"の漸近を、$B\mapsto\lfloor B/k\rfloor$に対して一様な誤差項付きで評価し、Möbius和の相殺後にも有効な下界を残せるか、という一点である。",
        "",
        "確定したこと：",
        "",
        "1. primitive補正はglobal Möbius反転で厳密に閉じる",
        r"2. 単純な$1/\zeta(2)$密度仮定は不要である",
        "3. raw平均の主項だけでなく、Möbius反転に耐える一様誤差評価が必要である",
        "",
        "未確認のこと：",
        "",
        r"- $C_{\mathrm{dist,raw}}(B)$の漸近式",
        "- Möbius反転後の正の主項または下界",
        "- Stage11の$B^{1/2}$下界を改善できるか",
        "- 等辺raw chainの一般不存在",
        "",
        "従ってN1枝から新しい枝が生える余地は、distinct raw畳み込みの一様漸近評価にほぼ限定された。",
        END,
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    text = args.input.read_text(encoding="utf-8")
    report = json.loads(args.report.read_text(encoding="utf-8"))
    block = render(report)
    if START in text:
        before, rest = text.split(START, 1)
        _, after = rest.split(END, 1)
        text = before.rstrip() + "\n\n" + block + after
    else:
        if ANCHOR not in text:
            raise SystemExit("memo insertion anchor not found")
        text = text.replace(ANCHOR, "\n\n" + block + ANCHOR, 1)
    args.output.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
