#!/usr/bin/env python3
"""Insert the stage-five rank, generator, and height results into the memo."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


START = "<!-- TWO_FACE_STAGE5_START -->"
END = "<!-- TWO_FACE_STAGE5_END -->"


def fmt(value: float, digits: int = 6) -> str:
    return f"{value:.{digits}f}"


def build_section(report: dict[str, Any]) -> str:
    rank = report["unresolved_rank_retry"]
    generator = report["lambda_7_32_generator"]
    height = report["height_pilot"]
    fibers = rank["fibers"]
    unresolved_rows = "\n".join(
        f"| ${item['lambda']}$ | {', '.join(map(str, item['source_indices']))} | "
        f"${item['final_rank_lower_bound']}\\ldots {item['final_rank_upper_bound']}$ | 未確定 |"
        for item in fibers
    )
    g = generator["saturated_generator"]
    gp = (
        f"\\left({g['x']['text']},\\,{g['y']['text']}\\right)"
    )
    canonical = height["canonical_height_summary"]
    ratio = height["canonical_over_log_d_summary"]
    corr = height["correlations"]
    ols = height["ols_model"]
    residual = (
        f"[{fmt(ols['residual_min'])},\\,{fmt(ols['residual_max'])}]"
    )
    return f"""
{START}
### 4.14 未確定rank・index 2生成点・canonical height予備解析【有限計算は確定／一様評価は未証明】

再現コードは

- [`scripts/audit_two_face_rank_height_stage5.py`](../scripts/audit_two_face_rank_height_stage5.py)
- [`scripts/audit_two_face_rank_height_stage5_runner.py`](../scripts/audit_two_face_rank_height_stage5_runner.py)

であり、全出力は

[`data/two_face_cuboids_1e6_stage5_report.json`](../data/two_face_cuboids_1e6_stage5_report.json)

に保存する。

#### 4.14.1 rank未確定3ファイバーの再監査【未確定のまま】

前段階でPARI/GP `ellrank` の下界・上界が $1\\ldots3$ のまま残った3本について、effortを4および8へ上げて再実行した。3本とも計算自体は成功したが、区間は縮まらず、新たな独立生成点も得られなかった。

| $\\lambda$ | source index | 再計算後のrank区間 | 状態 |
|---:|---:|---:|---|
{unresolved_rows}

3本すべてでroot numberは $-1$ である。ただし、root numberからrankの奇偶性を使う議論は一般には予想を含み、今回の計算だけからrank $1$ と確定しない。したがって、これら3本の正確なMordell--Weil rankは依然として未確認である。

#### 4.14.2 $\\lambda=7/32$ の飽和生成点【確定】

source index {generator['source_index']} の観測点を $P$ とする。この点の元の直方体は

$$
(a,b,c,d)=({generator['source_tuple']['a']},{generator['source_tuple']['b']},{generator['source_tuple']['c']},{generator['source_tuple']['d']})
$$

である。PARI/GP `ellsaturation(E,[P],100)` が返した点を $G$ とすると、

$$
G={gp}
$$

であり、有理数の厳密な群法則計算により

$$
P=2G
$$

が成立した。regulator比は

$$
\\frac{{\\operatorname{{Reg}}(P)}}{{\\operatorname{{Reg}}(G)}}=4
$$

であり、自由部分におけるindexが2であることと一致する。したがって、前段階で検出された唯一のindex 2事例について、欠けていた半点を明示できた。

`ellsaturation(...,100)` が保証するのは、返された部分群のindexが100未満の素数で割れないことである。100以上の素数に関する完全飽和性までは主張しない。

#### 4.14.3 255点のcanonical height予備解析【有限標本について確定】

対応する特殊化楕円曲線上で、保存済み255点すべてのPARI canonical height $\\widehat h(P)$ を計算した。

| 指標 | 最小 | 中央値 | 平均 | 最大 |
|---|---:|---:|---:|---:|
| $\\widehat h(P)$ | {fmt(canonical['min'])} | {fmt(canonical['median'])} | {fmt(canonical['mean'])} | {fmt(canonical['max'])} |
| $\\widehat h(P)/\\log d$ | {fmt(ratio['min'])} | {fmt(ratio['median'])} | {fmt(ratio['mean'])} | {fmt(ratio['max'])} |

有限標本内のPearson相関は次である。

| 組 | 相関係数 |
|---|---:|
| $\\widehat h(P)$ と $\\log d$ | {fmt(corr['canonical_height_vs_log_d'])} |
| $\\widehat h(P)$ と $h(\\lambda)$ | {fmt(corr['canonical_height_vs_lambda_log_height'])} |
| $\\widehat h(P)$ とnaive $x$-height | {fmt(corr['canonical_height_vs_x_log_height'])} |
| $\\log d$ と $h(\\lambda)$ | {fmt(corr['log_d_vs_lambda_log_height'])} |

さらに有限標本へ

$$
\\widehat h(P)=\\beta_0+\\beta_d\\log d+\\beta_\\lambda h(\\lambda)+\\varepsilon
$$

を最小二乗で当てはめると、

$$
\\beta_0={fmt(ols['beta0'])},\\qquad
\\beta_d={fmt(ols['beta_d'])},\\qquad
\\beta_\\lambda={fmt(ols['beta_lambda'])},
$$

$$
R^2={fmt(ols['r_squared'])},\\qquad
\\varepsilon\\in {residual}
$$

となった。この回帰は有限データの記述にすぎない。特に、残差が将来の点でも有界であること、$\\widehat h(P)$ と $\\log d$ の一様な上下評価、またはファイバーごとの点数上界を与えない。

今回の標本では $\\widehat h(P)/\\log d$ が約0.100から0.470の範囲にあり、単純な固定比例よりも大きな散らばりがある。次に必要なのは回帰の追加ではなく、Weierstrass写像の分子・分母、$h(\\lambda)$、射影高さ $H=d$ を使った理論的な高さ不等式の導出である。

#### 4.14.4 $N_2=o(N_1)$ への位置づけ【未証明】

この段階で確定したのは、1件のindex 2部分群の真の生成点と、保存済み255点のcanonical heightである。rank未確定3本は解消できず、有限標本の高さ統計から大域的な点数上界も得られない。

次の理論課題は次である。

1. $x(P)$ の有理数heightを $d$ と $h(\\lambda)$ で厳密に評価する
2. naive $x$-heightとcanonical heightの差を曲線係数のheight込みで一様に評価する
3. ファイバー内の格子点数評価を $\\lambda$ 全体で総和できる形にする
4. 一面成立数 $N_1(B)$ の下界または主項と比較する

したがって、二面成立数の無条件上界および $N_2(B)=o(N_1(B))$ は未証明のままである。
{END}
""".strip()


def update_text(text: str, section: str) -> str:
    if START in text and END in text:
        before, remainder = text.split(START, 1)
        _, after = remainder.split(END, 1)
        return before.rstrip() + "\n\n" + section + "\n\n" + after.lstrip()
    marker = "\n## 5. 一面成立曲面"
    if marker not in text:
        raise ValueError("section 5 marker was not found")
    return text.replace(marker, "\n\n" + section + marker, 1)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = json.loads(args.report.read_text(encoding="utf-8"))
    text = args.input.read_text(encoding="utf-8")
    updated = update_text(text, build_section(report))
    args.output.write_text(updated.rstrip() + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
