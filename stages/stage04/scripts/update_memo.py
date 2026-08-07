#!/usr/bin/env python3
"""Insert the all-observed-fiber PARI audit into the research memo."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


START = "### 4.13 観測済み193ファイバー全体のrank・飽和監査"
END = "\n## 5. 一面成立曲面 $V_{ab}$ の幾何"


def histogram_table(histogram: dict[str, Any], first: str, second: str) -> str:
    rows = [f"| {first} | {second} |", "|---:|---:|"]
    for key, value in sorted(histogram.items(), key=lambda item: int(item[0])):
        rows.append(f"| {key} | {value} |")
    return "\n".join(rows)


def build_section(report: dict[str, Any]) -> str:
    exact_table = histogram_table(
        report["exact_rank_histogram"], "特殊化rank", "ファイバー数"
    )
    singleton_table = histogram_table(
        report["singleton_exact_rank_histogram"],
        "単一点ファイバーの特殊化rank",
        "ファイバー数",
    )
    saturation_table = histogram_table(
        report["saturation_index_histogram"],
        "観測seed部分群から飽和後部分群へのindex",
        "ファイバー数",
    )
    unresolved = int(report["unresolved_rank_count"])
    exact_status = (
        "全観測ファイバーでrank下界と上界が一致した"
        if unresolved == 0
        else f"{unresolved}本ではrank区間が残った"
    )

    return f"""### 4.13 観測済み193ファイバー全体のrank・飽和監査【有限集合について確定】

4.12では複数点を含む50本だけをPARI/GPで監査した。次の段階として、単一点143本を含む観測済み全ファイバーについて同じWeierstrassモデルを用い、PARI/GP `ellrank` の2-descentを実行した。再現コードと結果は

- [`scripts/audit_all_observed_fibers_with_pari.py`](../scripts/audit_all_observed_fibers_with_pari.py)
- [`data/two_face_cuboids_1e6_all_fibers_pari_report.json`](../data/two_face_cuboids_1e6_all_fibers_pari_report.json)

に保存した。

#### 4.13.1 全193ファイバーの特殊化rank【有限集合について確定】

- 対象ファイバー：{report['fiber_count']}本
- 単一点ファイバー：{report['singleton_fiber_count']}本
- 複数点ファイバー：{report['repeated_fiber_count']}本
- PARI成功：{report['success_count']}本
- タイムアウト：{report['timeout_count']}本
- PARIエラー：{report['pari_error_count']}本
- rank確定：{report['exact_rank_count']}本
- rank未確定：{report['unresolved_rank_count']}本

今回の計算では、{exact_status}。確定した特殊化rankの分布は次である。

{exact_table}

単一点143ファイバーだけに限定した分布は次である。

{singleton_table}

この分布は $d\le10^6$ で実際に点が観測された193個の $\lambda$ に対する結果である。未観測の有理 $\lambda$ を含む一般ファイバーのrank分布や、一様なrank上界を意味しない。

#### 4.13.2 torsion構造【有限集合について確定】

成功した各ファイバーについてPARIの `elltors` を実行した。構造別集計は

```text
{json.dumps(report['torsion_structure_histogram'], ensure_ascii=False, sort_keys=True)}
```

である。これは観測済み特殊化ファイバーの有限集合に関する計算結果であり、特殊化によるtorsion増大がすべての有理 $\lambda$ で起きないことを証明するものではない。

#### 4.13.3 観測seed部分群の小素数飽和監査【適用対象について確定】

PARI公式文書の `ellsaturation(E,V,B)` は、$V$ が有限指数部分群を生成する独立な非torsion点集合であるとき、返された部分群のindexが $B$ 未満の素数で割れないことを保証する。そこで、次の条件を満たすファイバーだけを対象にした。

1. `ellrank` の下界と上界が一致する
2. 観測bounded seed数が確定rankに等しい
3. canonical height pairingが非退化である

飽和上限は

$$
B={report['saturation_bound']}
$$

とした。結果は次である。

- 飽和監査の適用条件を満たしたファイバー：{report['saturation_eligible_count']}本
- `ellsaturation` 実行：{report['saturation_run_count']}本
- 観測seed部分群のindexが1だったもの：{report['observed_seed_subgroup_saturated_below_bound_count']}本
- より大きい部分群へ拡大されたもの：{report['observed_seed_subgroup_enlarged_count']}本

index分布は次のとおりである。

{saturation_table}

indexが1である場合、観測seed部分群は少なくとも100未満の素数に関して飽和している。indexが1より大きい場合は、観測seedが同じrankの部分群を生成していても完全なMordell--Weil基底ではなかったことを意味する。ただし、100以上の素数に関する飽和性は今回の計算からは分からない。

#### 4.13.4 $N_2=o(N_1)$ への位置づけ【未証明】

今回の監査により、保存された255点が属する全193ファイバーについて、特殊化rankと観測seed部分群の有限指数問題を以前より詳細に整理できた。しかし、これは横方向に動く $\lambda$ の個数を制御しない。二面成立数の上界には依然として

1. $H=d$ と各ファイバーのcanonical heightの一様比較
2. $\lambda$ のheightと $d$ の同時制御
3. 未観測ファイバーを含む一様なrank・局所条件の評価
4. ファイバーごとの点数上界を全 $\lambda$ について総和する議論

が必要である。したがって、観測済み全ファイバーのrankが計算できても、二面成立数の無条件上界および $N_2=o(N_1)$ はまだ従わない。

"""


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    text = args.input.read_text(encoding="utf-8")
    report = json.loads(args.report.read_text(encoding="utf-8"))
    if START in text:
        before, rest = text.split(START, 1)
        if END not in rest:
            raise SystemExit("section 4.13 exists but section 5 marker is missing")
        _, after = rest.split(END, 1)
        text = before.rstrip() + "\n\n" + END.lstrip("\n") + after
    if END not in text:
        raise SystemExit("section 5 marker was not found")
    before, after = text.split(END, 1)
    updated = before.rstrip() + "\n\n" + build_section(report) + END + after
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(updated, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
