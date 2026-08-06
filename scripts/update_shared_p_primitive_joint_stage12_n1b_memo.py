#!/usr/bin/env python3
"""Insert the Stage12-N1b primitive-joint audit into the research memo."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

START = "<!-- SHARED_P_PRIMITIVE_JOINT_STAGE12_N1B_START -->"
END = "<!-- SHARED_P_PRIMITIVE_JOINT_STAGE12_N1B_END -->"
ANCHOR = "\n## 5. 一面成立曲面 $V_{ab}$ の幾何"


def render(report: dict) -> str:
    rows = report["finite_rows"]
    lines = [
        START,
        "## 4.22 Stage12-N1b：primitive-compatible共有$p$畳み込み",
        "",
        "再現コードと生成レポートは",
        "",
        "- [`scripts/audit_shared_p_primitive_joint_stage12_n1b.py`](../scripts/audit_shared_p_primitive_joint_stage12_n1b.py)",
        "- [`data/shared_p_primitive_joint_stage12_n1b_report.json`](../data/shared_p_primitive_joint_stage12_n1b_report.json)",
        "",
        "に保存する。Stage12-N1でraw平均からprimitive点へ移る補正が主項級の問題と判明したため、その補正を共有$p$ごとの厳密な重みに組み込む。",
        "",
        "### 4.22.1 gcd縮約【確定】",
        "",
        "第一の直角三角形を",
        "",
        "$$x^2+y^2=p^2,\qquad g=\gcd(x,y),$$",
        "",
        "第二の直角三角形を",
        "",
        "$$p^2+c^2=d^2$$",
        "",
        "とする。このとき結合後の三辺の最大公約数は恒等的に",
        "",
        "$$\boxed{\gcd(x,y,c)=\gcd(g,c)}$$",
        "",
        "である。従って結合直方体がprimitiveであるための必要十分条件は",
        "",
        "$$\boxed{\gcd(g,c)=1}$$",
        "",
        "となる。全三辺のgcd条件は、第一三角形のスケール$g$と第二三角形の脚$c$の互いに素条件へ縮約された。",
        "",
        "### 4.22.2 第一三角形のprimitive-scale分解【確定】",
        "",
        "固定した$p$に対し、$x<y$かつ$x^2+y^2=p^2$を満たす表現のうち$\gcd(x,y)=g$となる個数は、$p/g$を斜辺とするprimitive Pythagorean tripleの個数$P(p/g)$に等しい。",
        "",
        "$$\#\{(x,y):x<y,\ x^2+y^2=p^2,\ \gcd(x,y)=g\}=P(p/g).$$",
        "",
        "ここで$h>1$に対して",
        "",
        "$$P(h)=\begin{cases}2^{\omega(h)-1},&h\text{が奇数で、全素因子が }1\pmod4,\\0,&\text{それ以外}\end{cases}$$",
        "",
        "である。$p\le20{,}000$の13,211個の支持$p$、22,389個の$(p,g)$群で直接列挙と完全一致した。",
        "",
        "### 4.22.3 primitive-compatible joint weightとMöbius反転【確定】",
        "",
        "共有$p$に対して",
        "",
        "$$J_B(p)=\sum_{\substack{x<y\\x^2+y^2=p^2}}\ \sum_{\substack{p^2+c^2=d^2\\d\le B}}\mathbf1_{(\gcd(x,y),c)=1}$$",
        "",
        "と定義する。さらに",
        "",
        "$$A_k(p)=\#\{(x,y):x<y,\ x^2+y^2=p^2,\ k\mid\gcd(x,y)\},$$",
        "",
        "$$B_{k,B}(p)=\#\{(c,d):p^2+c^2=d^2,\ d\le B,\ k\mid c\}$$",
        "",
        "とすれば、Möbius反転から厳密に",
        "",
        "$$\boxed{J_B(p)=\sum_{k\ge1}\mu(k)A_k(p)B_{k,B}(p)}$$",
        "",
        "を得る。これはraw積$H(p)L_B(p)$をprimitive条件付きのjoint weightへ置き換える正確な式である。",
        "",
        "### 4.22.4 有限完全照合【有限範囲で確定】",
        "",
        "| $B$ | raw oriented | 互いに素条件後 | 等辺補正 | primitive distinct oriented | Stage11値 |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['B']:,} | {row['raw_oriented_chains']:,} | "
            f"{row['coprime_joint_oriented_before_distinctness']:,} | "
            f"{row['repeated_side_oriented_correction']:,} | "
            f"{row['primitive_distinct_oriented']:,} | {row['stage11_primitive_oriented']:,} |"
        )
    lines += [
        "",
        "各閾値で、直接の互いに素判定とMöbius和が完全一致し、等辺補正後の値はStage11のprimitive oriented countと完全一致した。監査範囲では等辺補正は0件だが、一般の不存在は未証明なので恒等式から削除しない。",
        "",
        "### 4.22.5 研究判断【補正の代数的閉包は成功／平均評価は未解決】",
        "",
        "Stage12-N1で壁として残ったprimitive補正は、少なくとも代数的には閉じた。次の問題は曖昧なgcd補正ではなく、squarefreeな$k$について",
        "",
        "$$\sum_{p\le B}A_k(p)B_{k,B}(p)$$",
        "",
        "を$k$に一様に評価できるか、という明確な平均値問題である。",
        "",
        "確定したこと：",
        "",
        "1. primitive条件は$\gcd(g,c)=1$へ縮約される",
        "2. 第一三角形のスケール分布は$P(p/g)$で完全に記述できる",
        "3. primitive-compatible joint weightはMöbius反転で厳密に表現できる",
        "4. 有限範囲ではStage11のprimitive oriented countを完全再現する",
        "",
        "未確認のこと：",
        "",
        "- $A_k(p)B_{k,B}(p)$の一様平均評価",
        "- Möbius和の打切りと誤差評価",
        "- Stage11の$N_1(B)\gg B^{1/2}$を改善できるか",
        "- 等辺補正が一般に0か",
        "",
        "従ってN1枝は『補正が書けない』段階を脱し、『書けたMöbius joint weightを解析できるか』という次の一点へ絞られた。",
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
