#!/usr/bin/env python3
"""Insert the stage-nine divisor-chain audit into the research memo."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

START = "<!-- FACE_DIVISOR_CHAIN_STAGE9_START -->"
END = "<!-- FACE_DIVISOR_CHAIN_STAGE9_END -->"
INSERT_BEFORE = "## 5. 一面成立曲面 $V_{ab}$ の幾何"
CONFIRMED_HEADING = "### 確定\n"
UNCONFIRMED_HEADING = "### 未確認\n"
CONFIRMED_BULLET = (
    "- 一面以上成立する整数直方体について、二段階の約数鎖による完全な有限列挙が可能で、"
    "$d\\le20{,}000$ のprimitive点と既存の二面成立42件を完全再現したこと\n"
)
UNCONFIRMED_BULLET = (
    "- 二段階約数鎖上の追加平方条件を、標準的なsquare sieveへ接続できる低次元再パラメータ化、"
    "または漸近的に多数の一面のみ成立点を与える固定合同部分族が存在するか\n"
)


def percent(value: float) -> str:
    return f"{100.0 * value:.4f}\\%"


def threshold_table(report: dict[str, Any]) -> str:
    lines = [
        "| $B$ | 一面以上 | ちょうど一面 $N_1(B)$ | 二面以上 $N_2(B)$ | $N_2/(N_1+N_2)$ | oriented chainでの通過率 |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for row in report["threshold_rows"]:
        lines.append(
            "| {B:,} | {total:,} | {one:,} | {two:,} | {point_rate} | {chain_rate} |".format(
                B=row["B"],
                total=row["unique_at_least_one_face"],
                one=row["exactly_one_face"],
                two=row["at_least_two_faces"],
                point_rate=percent(row["extra_square_point_pass_rate"]),
                chain_rate=percent(row["extra_square_oriented_chain_pass_rate"]),
            )
        )
    return "\n".join(lines)


def category_table(report: dict[str, Any]) -> str:
    row = report["threshold_rows"][-1]
    counts = row["category_counts"]
    order = ["ab_only", "ac_only", "bc_only", "ab+ac", "ab+bc", "ac+bc", "perfect"]
    labels = {
        "ab_only": "abのみ",
        "ac_only": "acのみ",
        "bc_only": "bcのみ",
        "ab+ac": "ab+ac",
        "ab+bc": "ab+bc",
        "ac+bc": "ac+bc",
        "perfect": "三面（完全直方体）",
    }
    lines = ["| 分類 | 件数 |", "|---|---:|"]
    for name in order:
        lines.append(f"| {labels[name]} | {int(counts.get(name, 0)):,} |")
    return "\n".join(lines)


def certificate_table(report: dict[str, Any]) -> str:
    rows = report["congruence_certificates"]["per_modulus"][:8]
    lines = [
        "| 法 $M$ | 小素数剰余だけで二つの残り面を非平方と保証できた件数 | 有限標本被覆率 |",
        "|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| {row['modulus']} | {row['certified_exactly_one_count']:,} | {percent(row['coverage_fraction'])} |"
        )
    return "\n".join(lines)


def build_section(report: dict[str, Any]) -> str:
    final = report["threshold_rows"][-1]
    comparison = report["known_two_face_comparison"]
    certificates = report["congruence_certificates"]
    one_counts = report["published_d20000_one_face_counts"]["generated"]

    template = r"""@@START@@
### 4.18 一面・二面成立の二段階約数鎖監査【有限列挙は確定／square sieve接続は未確認】

再現コードと生成レポートは

- [`scripts/audit_face_divisor_chain_stage9.py`](../scripts/audit_face_divisor_chain_stage9.py)
- [`data/face_divisor_chain_stage9_report.json`](../data/face_divisor_chain_stage9_report.json)

に保存する。本節では楕円ファイバーの高さから離れ、一面成立点を二つのPythagorean tripleの結合として直接列挙する。

#### 4.18.1 二段階約数鎖【確定】

一つの面と空間対角線について

$$
a^2+b^2=p^2,\qquad p^2+c^2=d^2
$$

とする。正整数

$$
r=p-b,\quad s=p+b,\quad u=d-c,\quad v=d+c
$$

を導入すると

$$
rs=a^2,\qquad uv=p^2
$$

であり、逆に同じ偶奇の約数対から

$$
b=\frac{s-r}{2},\quad p=\frac{s+r}{2},\qquad
c=\frac{v-u}{2},\quad d=\frac{v+u}{2}
$$

を回復できる。従って、生成面を固定した一面以上成立点と二段階約数鎖の間には完全な対応がある。

三辺が相異なる正整数の場合、整数となる面対角線が $k$ 本なら、各面の二つの脚のどちらを最初の固定脚にするかで、**oriented divisor chainは正確に $2k$ 個**である。$d\le20{,}000$ の全列挙でこの重複度を検算した。

#### 4.18.2 既存データの完全再現【有限範囲について確定】

@@THRESHOLD_TABLE@@

$d\le20{,}000$ の分類は次の通りだった。

@@CATEGORY_TABLE@@

特に一面のみ成立は

$$
N_1(20{,}000)=@@ONE_TOTAL@@
$$

で、内訳

$$
(ab,ac,bc)=(@@AB_ONLY@@,@@AC_ONLY@@,@@BC_ONLY@@)
$$

は既存研究メモの値と完全一致した。二面以上成立は @@TWO_COUNT@@ 件で、`data/two_face_cuboids_1e6_fixed.json` の $d\le20{,}000$ 部分と点・分類とも完全一致した。

これにより二段階約数鎖は、有限探索の高速化だけでなく、一面成立母集団と二面成立部分集合を同一の離散パラメータ空間で比較する座標として利用できる。

#### 4.18.3 二面成立を与える追加平方条件【確定】

生成面を $ab$ とすると、残りの二面成立条件は

$$
4(a^2+c^2)=4rs+(v-u)^2=\square,
$$

$$
4(b^2+c^2)=(s-r)^2+(v-u)^2=\square
$$

となる。従って「二面成立の希少性」は、二段階約数鎖上でこれらの追加平方条件が通過する頻度として厳密に分離できる。

ただし変数は独立なboxを動くのではなく、

$$
rs=a^2,\qquad uv=\left(\frac{r+s}{2}\right)^2
$$

という乗法的な平方・約数制約で強く結合している。そのため、現時点で標準的なsquare sieveへそのまま適用できる形ではない。追加平方式を得たことと、指数改善を証明したことを区別する。

#### 4.18.4 一面のみを保証する合同証明書【有限探索】

生成面以外の二つの平方和が、ある法 $M$ で平方剰余でなければ、その面対角線は整数にならない。この十分条件を小さい法で探索した。

@@CERTIFICATE_TABLE@@

試した法の和集合では、一面のみ成立 @@CERT_POP@@ 件のうち @@CERT_COUNT@@ 件、すなわち @@CERT_RATE@@ に有限の合同証明書が見つかった。二面以上成立点に対する偽陽性は0件である。

これは個々の剰余類が一面のみ成立を保証するという厳密な十分条件だが、**その剰余類に属するprimitive約数鎖が漸近的に多数存在することは未証明**である。有限被覆率をそのまま $N_1(B)$ の下界へ読み替えない。

#### 4.18.5 分岐点としての結論【次の再パラメータ化が必要】

Stage9で確定したことは、

1. 一面以上成立点を二段階約数鎖で完全列挙できる
2. 二面成立を二つの明示的な追加平方条件として切り出せる
3. $d\le20{,}000$ の既存一面・二面データを完全再現できる
4. 小さい法による一面のみ成立の十分条件は有限データ上で多数見つかる

ことである。

一方、追加平方式は divisor constraints によって変数が強く結合しており、現段階では標準square sieveの入力にはなっていない。また、合同証明書を満たす点が十分多数存在するという下界族も得ていない。

次の短期タスクは、

- Euclid型Pythagoreanパラメータへ移して自由変数を減らし、追加平方条件を低次数形式へ書き直す
- または、固定合同類の中でprimitiveな一面のみ成立点を無限に生成できる明示的部分族を探索する

ことである。これが得られなければ、約数鎖を数えるだけではlittle-oへ接続せず、determinant methodによる直接計数との比較へ移る。

$$
N_2(B)=o(N_1(B))
$$

および $N_1(B)$ の漸近下界は未証明のままである。
@@END@@
"""

    replacements = {
        "@@START@@": START,
        "@@END@@": END,
        "@@THRESHOLD_TABLE@@": threshold_table(report),
        "@@CATEGORY_TABLE@@": category_table(report),
        "@@ONE_TOTAL@@": f"{final['exactly_one_face']:,}",
        "@@AB_ONLY@@": f"{one_counts['ab_only']:,}",
        "@@AC_ONLY@@": f"{one_counts['ac_only']:,}",
        "@@BC_ONLY@@": f"{one_counts['bc_only']:,}",
        "@@TWO_COUNT@@": str(comparison["generated_two_face_count"]),
        "@@CERTIFICATE_TABLE@@": certificate_table(report),
        "@@CERT_POP@@": f"{certificates['exactly_one_population']:,}",
        "@@CERT_COUNT@@": f"{certificates['union_certified_count']:,}",
        "@@CERT_RATE@@": percent(certificates["union_coverage_fraction"]),
    }
    for token, value in replacements.items():
        template = template.replace(token, value)
    return template


def replace_section(text: str, section: str) -> str:
    if START in text or END in text:
        if START not in text or END not in text:
            raise ValueError("only one stage-nine marker is present")
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
