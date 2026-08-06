#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

START = "<!-- SHARED_P_HYPERBOLA_STAGE12_N1_2_START -->"
END = "<!-- SHARED_P_HYPERBOLA_STAGE12_N1_2_END -->"


def render(report: dict) -> str:
    rows = report["finite_rows"]
    lines = [
        START,
        "### 4.25 Stage12-N1-2：共有$p$畳み込みの双曲線座標化【厳密恒等式は確定／平均評価は未証明】",
        "",
        "Stage12-N1dでは$L_B(p)$の外部高さ依存が、一変数乗法関数平均定理への直接接続を妨げることを確認した。ここでは第二の直角三角形",
        "",
        r"$$p^2+c^2=d^2$$",
        "",
        "を直接再パラメータ化する。",
        "",
        "#### 4.25.1 一意な双曲線座標【確定】",
        "",
        "",
        r"$$u=d-c,\qquad v=d+c$$",
        "",
        "と置くと$uv=p^2$である。$h=\gcd(u,v)$とし、互いに素な商の積が平方であることを使うと、一意に",
        "",
        r"$$u=hr^2,\qquad v=hs^2,\qquad 1\le r<s,\qquad \gcd(r,s)=1$$",
        "",
        "と書ける。従って",
        "",
        r"$$p=hrs,\qquad c=\frac{h(s^2-r^2)}2,\qquad d=\frac{h(r^2+s^2)}2.$$
",
        "整数性と高さ条件は",
        "",
        r"$$h(r^2+s^2)\equiv0\pmod2,\qquad h(r^2+s^2)\le2B$$",
        "",
        "に一致する。監査スクリプトはStage11の全第二三角形について順逆変換を再検算した。",
        "",
        "#### 4.25.2 固定乗法重みへの変換【確定】",
        "",
        "",
        r"$$G(n)=2H(n)+1=\prod_{q\mid n,\ q\equiv1\ (4)}(2v_q(n)+1)$$",
        "",
        "と置く。$G$は乗法的である。各第二三角形の共有対角線は$p=hrs$なので、raw oriented chain数は厳密に",
        "",
        r"$$\boxed{C_{\mathrm{raw}}(B)=\sum_{\substack{h\ge1,\ 1\le r<s,\ (r,s)=1\\ h(r^2+s^2)\le2B\\ h(r^2+s^2)\equiv0\ (2)}}\bigl(G(hrs)-1\bigr)}$$",
        "",
        "となる。これにより、$B$依存関数$L_B(p)$は被加重関数から消え、すべての$B$依存性が明示的な二次高さ領域へ移った。",
        "",
        "#### 4.25.3 有限監査【確定】",
        "",
        "| $B$ | raw oriented | 双曲線重み和 | $(h,r,s)$点数 | 最大$h$ |",
        "|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['B']:,} | {row['raw_oriented_chains']:,} | "
            f"{row['hyperbola_weighted_sum']:,} | "
            f"{row['second_triangle_parameter_points']:,} | {row['max_scale_h']:,} |"
        )
    lines.extend(
        [
            "",
            "全閾値でStage11のraw畳み込みと双曲線重み和は完全一致した。有限比率やscale別寄与は漸近密度と解釈しない。",
            "",
            "#### 4.25.4 解析的進展と残る補題【進展あり／未証明】",
            "",
            "Stage12-N1dでの判定を一段改善できた。被加重関数は固定された乗法関数$G$になり、外部高さ$B$は領域にのみ現れる。従って、今後の解析対象は明確に",
            "",
            r"$$\sum_{h(r^2+s^2)\le2B\atop r<s,(r,s)=1,\ \mathrm{parity}}G(hrs)$$",
            "",
            "という三変数の二次領域平均である。",
            "",
            "未証明事項：",
            "",
            "- $h$と$rs$が素因数を共有し得る状況での$G(hrs)$の平均評価",
            "- 等辺chainの一般的除外または別評価",
            "- global Möbius反転に耐える一様誤差項",
            "",
            "判定は `A_reparameterization_progress_new_mean_value_lemma_needed` とする。標準一変数定理へ直接戻ったわけではないが、$L_B(p)$の非乗法的高さ切断は明示的な双曲線領域へ吸収された。次に必要なのはこの領域上の新しい平均値補題である。",
            END,
        ]
    )
    return "\n".join(lines) + "\n"


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
        text = before.rstrip() + "\n\n" + block + after.lstrip("\n")
    else:
        marker = "## 5. 一面成立曲面"
        if marker not in text:
            raise RuntimeError("section 5 marker not found")
        text = text.replace(marker, block + "\n" + marker, 1)
    args.output.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
