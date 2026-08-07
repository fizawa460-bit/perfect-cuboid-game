#!/usr/bin/env python3
"""Insert the Stage12-N1d analytic-exit audit into the research memo."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

START = "<!-- SHARED_P_ANALYTIC_EXIT_STAGE12_N1D_START -->"
END = "<!-- SHARED_P_ANALYTIC_EXIT_STAGE12_N1D_END -->"
ANCHOR = "\n## 5. 一面成立曲面 $V_{ab}$ の幾何"


def render(report: dict) -> str:
    checks = report["structural_checks"]
    rows = report["finite_rows"]
    decision = report["decision"]
    lines = [
        START,
        "## 4.24 Stage12-N1d：共有$p$枝の解析的出口監査",
        "",
        "再現コードと生成レポートは",
        "",
        "- [`scripts/audit_shared_p_analytic_exit_stage12_n1d.py`](../scripts/audit_shared_p_analytic_exit_stage12_n1d.py)",
        "- [`data/shared_p_analytic_exit_stage12_n1d_report.json`](../data/shared_p_analytic_exit_stage12_n1d_report.json)",
        "",
        "に保存する。4.22–4.23でprimitive補正は厳密なMöbius反転まで閉じたため、今回は既知の一変数乗法関数平均定理へ直接接続できるかを判定した。",
        "",
        "### 4.24.1 係数列の乗法性監査【有限範囲で確定】",
        "",
        "Stage11の係数は固定$B$に対して",
        "",
        "$$F_B(p)=H(p)L_B(p)$$",
        "",
        "である。監査の結果、$H$自体は定義中のアフィン項のため乗法的ではなく、$L_B$は高さ条件$d\le B$を通じて$p$と外部変数$B$を同時に含むため、固定された一変数乗法関数ではない。従って$F_B$も乗法的ではない。",
        "",
        f"$H$の互いに素な積に対する有限検査は{checks['H_multiplicativity']['samples']:,}件で、乗法性違反は{checks['H_multiplicativity']['violations']:,}件だった。",
        "",
        "| $B$ | $L_B$検査数 | 違反数 | $H L_B$違反数 |",
        "|---:|---:|---:|---:|",
    ]
    for lrow, frow in zip(checks["L_B_multiplicativity"], checks["H_times_L_B_multiplicativity"]):
        lines.append(f"| {lrow['B']:,} | {lrow['samples']:,} | {lrow['violations']:,} | {frow['violations']:,} |")
    lines += [
        "",
        "この有限検査は非乗法性の証明例を与えるだけで、漸近評価そのものではない。ただしWirsing・Delange・Halász等を$F_B$へそのまま適用する前提が成立しないことは確定する。",
        "",
        "### 4.24.2 高さ結合が残る【確定】",
        "",
        "$$L_B(p)=\#\{(c,d):p^2+c^2=d^2,\ d\le B\}$$",
        "",
        "は$p$だけの係数ではない。約数表示では$p^2=uv$かつ$u+v\le2B$という双曲線型の切断条件になる。従って必要なのは通常のEuler積ではなく、$p$と$B$を同時に制御する二変数の約数和・双曲線法型評価である。",
        "",
        "### 4.24.3 Möbius反転後に必要な誤差条件【必要条件の明文化】",
        "",
        "4.23の厳密式",
        "",
        "$$C_{\mathrm{prim}}(B)=\sum_{k\le B}\mu(k)C_{\mathrm{dist,raw}}(\lfloor B/k\rfloor)$$",
        "",
        "へ$C_{\mathrm{dist,raw}}(X)=M(X)+R(X)$を代入する場合、主項$M$のMöbius変換が正でStage11の$B^{1/2}$下界を上回ることに加え、",
        "",
        "$$\sum_{k\le B}\left|R(\lfloor B/k\rfloor)\right|$$",
        "",
        "が変換後の主項より低次である一様誤差評価、または符号付きMöbius和に対する別の相殺定理が必要である。raw主項だけを得てもprimitive下界改善には足りない。",
        "",
        "| $B$ | distinct raw oriented | primitive oriented | 有限保持率 | Möbius再構成 |",
        "|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['B']:,} | {row['distinct_raw_oriented']:,} | {row['primitive_oriented']:,} | "
            f"{row['finite_retention']:.6f} | {row['mobius_reconstruction']:,} |"
        )
    lines += [
        "",
        "有限保持率は漸近密度と解釈しない。表はMöbius再構成の完全一致と、誤差評価が主項級の問題であることを確認するためのものに限る。",
        "",
        "### 4.24.4 既知定理への直接適用判定【不可】",
        "",
        "現状の$F_B(p)$は$B$依存・非乗法的であるため、Wirsing、Delange、Halászの一変数乗法関数平均定理を直接適用できない。Landau–Ramanujan型理論は$H$側の支持や平均の入力にはなり得るが、$L_B$の高さ切断とMöbius反転に必要な一様誤差を単独では供給しない。",
        "",
        "次に本当に必要な入力は次の4点である。",
        "",
        "1. $C_{\mathrm{dist,raw}}(X)$の一様漸近式",
        "2. $X=\lfloor B/k\rfloor$全域で使える誤差評価",
        "3. 主項のMöbius変換が正であることの確認",
        "4. 等辺chainを一般に除外できない場合の別評価",
        "",
        "### 4.24.5 N1枝の判定【B：新しい解析入力が必要】",
        "",
        f"判定は `{decision['classification']}` である。primitive補正・重複度・Möbius反転は既に閉じており、残る障害は有限監査や既知の一変数乗法関数定理の直接適用では解消しない。共有$p$枝をさらに進めるには、二変数双曲線和に対する新しい一様評価が必要である。",
        "",
        "確定したこと：",
        "",
        "- N1枝の代数的補正は完了している",
        "- $H(p)L_B(p)$は通常の固定乗法関数ではない",
        "- 標準的なWirsing・Delange・Halászへの直結はできない",
        "- 残る問題はMöbius反転に耐える二変数の一様平均評価である",
        "",
        "主張しないこと：",
        "",
        "- 将来の解析手法でもN1改善が不可能であること",
        "- $C_{\mathrm{dist,raw}}(B)$の漸近式",
        "- Stage11を超える新しい下界",
        "",
        "従ってN1枝はここで一旦停止し、完成した式と必要定理を外部査読へ渡した後、N2枝との研究コストを比較するのが妥当である。",
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
