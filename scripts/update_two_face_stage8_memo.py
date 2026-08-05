#!/usr/bin/env python3
"""Insert the stage-eight j-map and local-sieve audit into the research memo."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


START = "<!-- TWO_FACE_STAGE8_START -->"
END = "<!-- TWO_FACE_STAGE8_END -->"
INSERT_BEFORE = "## 5. 一面成立曲面 $V_{ab}$ の幾何"
CONFIRMED_HEADING = "### 確定\n"
UNCONFIRMED_HEADING = "### 未確認\n"
CONFIRMED_PREFIX = "- 二面成立楕円ファイバーの $j$-写像について、"
UNCONFIRMED_PREFIX = "- 実現 $\\lambda$ の疎性を説明する大域的機構として、"


def render(text: str) -> str:
    return text.replace("@@B@@", chr(92))


def f6(value: float) -> str:
    return f"{value:.6f}"


def build_threshold_table(report: dict[str, Any]) -> str:
    lines = [
        "| $B$ | 二面成立点 $N_2(B)$ | 実現 $@@B@@lambda$ 数 $M(B)$ | $N_2/M$ | 候補既約 $(m,n)$ | 実現割合 |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for row in report["empirical_growth"]["rows"]:
        lines.append(
            "| {B:,} | {n2:,} | {m:,} | {mean:.6f} | {pairs:,} | {fraction:.8f} |".format(
                B=row["B"],
                n2=row["two_face_point_count"],
                m=row["realized_lambda_count"],
                mean=row["mean_points_per_realized_lambda"],
                pairs=row["all_reduced_parameter_pair_count"],
                fraction=row["realized_fraction_of_parameter_pairs"],
            )
        )
    return render("\n".join(lines))


def build_prime_table(report: dict[str, Any]) -> str:
    lines = [
        "| $p$ | $qB$ が単元の解を持たない $@@B@@mathbf P^1(@@B@@mathbf F_p)$ の類 | 観測点の該当件数 |",
        "|---:|---|---:|",
    ]
    rows = report["local_divisibility_audit"]["b_unit_refinement"]["per_prime"]
    for row in rows:
        if not row["b_unit_obstructed_class_count"]:
            continue
        labels = ", ".join(row["b_unit_obstructed_classes"])
        lines.append(
            f"| {row['p']} | `{labels}` | {row['observed_points_in_obstructed_classes']} |"
        )
    return render("\n".join(lines))


def build_sieve_table(report: dict[str, Any]) -> str:
    lines = [
        "| $B$ | 候補既約 $(m,n)$ | 単純な $qB$ 可除性で厳密除外 | 最大強制平方自由積 |",
        "|---:|---:|---:|---:|",
    ]
    rows = report["local_divisibility_audit"]["simple_divisor_sieve"]["rows"]
    for row in rows:
        lines.append(
            "| {B:,} | {pairs:,} | {excluded:,} | {product:,} |".format(
                B=row["B"],
                pairs=row["candidate_parameter_pairs"],
                excluded=row["rigorously_excluded_by_simple_qB_divisibility"],
                product=row["maximum_forced_squarefree_product"],
            )
        )
    return "\n".join(lines)


def build_section(report: dict[str, Any]) -> str:
    jmap = report["j_map"]
    obstructing = report["local_divisibility_audit"]["b_unit_refinement"][
        "obstructing_primes_in_tested_range"
    ]
    threshold_table = build_threshold_table(report)
    prime_table = build_prime_table(report)
    sieve_table = build_sieve_table(report)
    template = f"""{START}
### 4.17 $j$-写像の次数と実現 $@@B@@lambda$ の局所sieve監査【$j$-写像・境界解は確定／単純局所sieveは不成立】

再現コードと有限監査結果は

- [`scripts/audit_two_face_local_sieve_stage8.py`](../scripts/audit_two_face_local_sieve_stage8.py)
- [`data/two_face_cuboids_1e6_stage8_local_sieve_report.json`](../data/two_face_cuboids_1e6_stage8_local_sieve_report.json)

に保存する。本節では、stage7後の壁打ちで候補となった二点を調べる。

1. $j(@@B@@lambda)$ の真の次数が24か
2. 実現 $@@B@@lambda$ の疎性を、通常の局所可解性または単純な合同条件で説明できるか

#### 4.17.1 $j$-写像と6本の $I_4$ ファイバー【確定】

楕円ファイバー

$$
E_t:\quad y^2=x(x+4t^2)(x+(1+t^2)^2)
$$

の不変量を直接計算すると、

$$
@@B@@begin{{aligned}}
c_4={jmap['c4_factorized']},\\
@@B@@Delta={jmap['delta_factorized']}.
@@B@@end{{aligned}}
$$

従って

$$
j(t)=@@B@@frac{{c_4^3}}{{@@B@@Delta}}
$$

の分子と分母は互いに素で、分子次数24、分母次数20である。無限遠に4位の極があるため、

$$
@@B@@boxed{{@@B@@deg(j)=24}}.
$$

判別式の零点 $t=0,1,-1,i,-i$ では $@@B@@operatorname{{ord}}(@@B@@Delta)=4$ かつ $c_4$ は消えない。無限遠では $s=1/t$, $x=X/s^4$, $y=Y/s^6$ とすると同じ形の $s$-モデルへ戻る。従って6か所はいずれも乗法的な $I_4$ 型で、Euler数の和は24である。

ここで $@@B@@deg(j)=24$ は具体的な有理関数の既約化から得た結果であり、「K3曲面だから自動的に24」と推論したものではない。

#### 4.17.2 点数増加と実現ファイバー増加の分離【有限データについて確定】

{threshold_table}

候補既約対は

$$
0<m<n,@@B@@qquad @@B@@gcd(m,n)=1,@@B@@qquad m^2+n^2@@B@@le2B
$$

を数えたものである。実現割合は有限範囲で小さいが、これだけから密度0や $B^{{1/2}}$ 型の指数を主張しない。$N_2(B)/M(B)$ も有限範囲では小さいが、1ファイバー当たりの一様点数上界とは解釈しない。

#### 4.17.3 Pythagoreanパラメータと整数 $q$【確定】

$@@B@@lambda=m/n$ を既約、$0<m<n$ とすると、

$$
q=@@B@@frac{{2Y}}{{m^2+n^2}}@@B@@in@@B@@mathbf Z
$$

であり、

$$
A=@@B@@frac q2(n^2-m^2),@@B@@qquad C=qmn,@@B@@qquad Y=@@B@@frac q2(m^2+n^2).
$$

保存済み255点で全式を厳密検算した。$m,n$ が異なる偶奇を持つ場合は $q$ が偶数である。

#### 4.17.4 通常の局所可解性が $@@B@@lambda$ を削らない理由【確定】

奇素数 $p$ で $p@@B@@nmid q$ とし、$q$ で座標を割った剰余を

$$
a_0=@@B@@frac{{n^2-m^2}}2,@@B@@qquad c_0=mn
$$

とする。残りの二式は

$$
b^2+c_0^2=x_0^2,@@B@@qquad a_0^2+x_0^2=u^2
$$

である。しかしすべての $[m:n]@@B@@in@@B@@mathbf P^1(@@B@@mathbf F_p)$ に対し、

$$
b=0,@@B@@qquad x_0=c_0,@@B@@qquad u=@@B@@frac{{m^2+n^2}}2
$$

が解になる。元の座標では

$$
B=0,@@B@@qquad X=C,@@B@@qquad U=Y
$$

という既知の境界円錐曲線である。従って、**ファイバーの通常の局所可解性だけでは $@@B@@lambda$ を一つも除外できない**。

これは正の整数点が存在するという意味ではない。境界を除いたopen部分の整数点問題と、射影曲面の局所点問題を混同してはならない。

#### 4.17.5 $qB$ 単元条件による第一段階の可除性監査【有限計算】

さらに $p@@B@@nmid qB$ を仮定し、$b=B/q$ が非零となる解を探索した。該当解が存在しない剰余類では、任意の大域整数点が

$$
p@@B@@mid qB
$$

を満たす。奇素数 $p@@B@@le {report['local_divisibility_audit']['prime_limit']}$ の全射影パラメータ類を監査したところ、非空の障害集合が現れた素数は

$$
{', '.join(str(p) for p in obstructing)}
$$

だけだった。

{prime_table}

保存済み255点について、障害類に入る場合はすべて実際に $p@@B@@mid qB$ となることを確認した。

ただし、これは $p@@B@@mid q$ または $p@@B@@mid B$ という可除性を強制するだけで、$@@B@@lambda$ 自体を排除する条件ではない。パリティによる $2@@B@@mid q$ と上記有限素数の条件を組み合わせ、

$$
qB@@B@@le@@B@@frac{{2B_0^2}}{{m^2+n^2}}
$$

を用いて $d@@B@@le B_0$ の候補を除外した結果は次の通りである。

{sieve_table}

監査した全閾値で厳密除外は0件だった。従って、**通常の局所可解性と第一段階の $qB$ 可除性だけでは、観測された実現 $@@B@@lambda$ の疎性を説明できない**。

#### 4.17.6 分岐点としての結論【単純局所ルートは見切り】

今回否定されたのは、

- 各ファイバーの局所可解性だけで候補 $@@B@@lambda$ を削る方法
- $p@@B@@nmid qB$ という最初の単元条件だけで候補数を減らす方法

である。より強いsquare sieve、複数の平方条件を同時に扱うdeterminant method、$p$-進高さ、最小非torsion高さの大域評価まで否定したわけではない。

一方、$j$-写像の次数24が確定したため、一般的なSilverman型高さ差評価の係数だけを磨いて $h(@@B@@lambda)$ 係数を2未満へ落とす方針は主ルートから外すのが妥当である。ただし、正・primitive・整数点に固有の相殺まで不可能と証明したわけではない。

次の候補は、

1. Pythagoreanパラメータ化後の二つの追加平方条件に対するsquare sieve
2. 二面成立曲面へのdeterminant methodまたは直接的な整数点計数
3. 比較対象 $N_1(B)$ の明示的な下界族の構成

である。どれを次の主ルートにするかは、理論的投入量と得られる中間定理を比較して決める必要がある。

$$
N_2(B)=O(B^{{1/2+@@B@@varepsilon}}),@@B@@qquad N_2(B)=o(N_1(B))
$$

はいずれも未証明のままである。
{END}
"""
    return render(template)


def replace_section(text: str, section: str) -> str:
    if START in text or END in text:
        if START not in text or END not in text:
            raise ValueError("only one stage-eight marker is present")
        before, rest = text.split(START, 1)
        _, after = rest.split(END, 1)
        return before.rstrip() + "\n\n" + section.rstrip() + "\n" + after.lstrip("\n")
    if INSERT_BEFORE not in text:
        raise ValueError("section-5 insertion point not found")
    return text.replace(INSERT_BEFORE, section.rstrip() + "\n\n" + INSERT_BEFORE, 1)


def confirmed_bullet() -> str:
    return render(
        CONFIRMED_PREFIX
        + "$@@B@@deg j=24$ で、$t=0,@@B@@pm1,@@B@@pm i,@@B@@infty$ に6本の $I_4$ ファイバーを持つこと、"
        "および全 $@@B@@lambda$ に境界解 $B=0,X=C,U=Y$ があるため通常の局所可解性だけでは"
        "$@@B@@lambda$ を削れないこと"
    )


def unconfirmed_bullet() -> str:
    return render(
        UNCONFIRMED_PREFIX
        + "square sieve、determinant method、最小非torsion高さまたは一面成立数の下界のどれが"
        "有効な大域計数へ接続するか"
    )


def replace_prefixed_bullet(text: str, heading: str, prefix: str, bullet: str) -> str:
    lines = [line for line in text.splitlines() if not line.startswith(prefix)]
    text = "\n".join(lines) + ("\n" if text.endswith("\n") else "")
    if heading not in text:
        raise ValueError(f"conclusion heading not found: {heading.strip()}")
    return text.replace(heading, heading + "\n" + bullet + "\n", 1)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = json.loads(args.report.read_text(encoding="utf-8"))
    if not report.get("valid"):
        raise ValueError("stage-eight report is not valid")
    text = args.input.read_text(encoding="utf-8")
    text = replace_section(text, build_section(report))
    text = replace_prefixed_bullet(
        text, CONFIRMED_HEADING, CONFIRMED_PREFIX, confirmed_bullet()
    )
    text = replace_prefixed_bullet(
        text, UNCONFIRMED_HEADING, UNCONFIRMED_PREFIX, unconfirmed_bullet()
    )
    args.output.write_text(text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
