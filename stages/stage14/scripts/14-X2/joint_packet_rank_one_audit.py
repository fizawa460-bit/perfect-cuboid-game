#!/usr/bin/env python3
"""Stage14-X2 regression and Pluecker rank-one-collapse audit.

The asymptotic rank-one theorem is the exact minor-divisibility argument in
stages/stage14/14-X2/result.md.  The finite checks below validate the algebra,
the predecessor boundaries, and several projection diagnostics.  They are not
used to infer the asymptotic endpoint theorem from search.
"""

from collections import Counter, defaultdict
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
import json
from math import gcd
from pathlib import Path


HERE = Path(__file__).resolve()
ROOT = HERE.parents[4]


def load_module(name: str, path: Path):
    spec = spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


x1 = load_module(
    "stage14_x1_x2",
    HERE.parents[1] / "14-X1" / "joint_physical_fiber_audit.py",
)
s7 = x1.s7
ch = x1.ch


def gcd_many(values: tuple[int, ...]) -> int:
    out = 0
    for value in values:
        out = gcd(out, abs(value))
    return out


def minor(u: tuple[int, ...], v: tuple[int, ...], i: int, j: int) -> int:
    return u[i] * v[j] - u[j] * v[i]


def pluecker(u: tuple[int, ...], v: tuple[int, ...]) -> dict[str, int]:
    return {
        "12": minor(u, v, 0, 1),
        "13": minor(u, v, 0, 2),
        "14": minor(u, v, 0, 3),
        "23": minor(u, v, 1, 2),
        "24": minor(u, v, 1, 3),
        "34": minor(u, v, 2, 3),
    }


def independent(u: tuple[int, ...], v: tuple[int, ...]) -> bool:
    return any(pluecker(u, v).values())


def crt_pair(a: int, m: int, b: int, n: int) -> tuple[int, int]:
    """Return the least nonnegative solution modulo m*n; gcd(m,n)=1."""
    if m == 1:
        return b % n if n > 1 else 0, n
    if n == 1:
        return a % m, m
    assert gcd(m, n) == 1
    value = a + ((b - a) * pow(m, -1, n) % n) * m
    return value % (m * n), m * n


def ratio_mod(num: int, den: int, cell: int) -> int:
    if cell == 1:
        return 0
    modulus = cell * cell
    assert gcd(den, modulus) == 1
    return num * pow(den, -1, modulus) % modulus


def xi_lambdas(a: dict[str, int], b: dict[str, int], cells: tuple[int, ...]):
    R, S, T, J = cells[:4]
    return {
        "R": ratio_mod(a["y"], b["y"], R),
        "J": ratio_mod(a["x"], b["x"], J),
        "S": ratio_mod(b["x"], a["y"], S),
        "T": ratio_mod(b["y"], a["x"], T),
    }


def in_xi_lattice(vector, cells, lambdas) -> bool:
    x1, y1, x2, y2 = vector
    R, S, T, J = cells[:4]
    return (
        (y1 - lambdas["R"] * y2) % (R * R) == 0
        and (x1 - lambdas["J"] * x2) % (J * J) == 0
        and (x2 - lambdas["S"] * y1) % (S * S) == 0
        and (y2 - lambdas["T"] * x1) % (T * T) == 0
    )


def make_independent_lattice_vector(
    physical: tuple[int, ...], cells: tuple[int, ...], lambdas: dict[str, int]
) -> tuple[int, ...]:
    """Construct a second exact lattice vector by the two coprime CRT pairs."""
    R, S, T, J = cells[:4]
    for shift in range(1, 9):
        x1 = physical[0] + shift
        y1 = physical[1] + 2 * shift

        x2_j = (
            x1 * pow(lambdas["J"], -1, J * J) % (J * J)
            if J > 1
            else 0
        )
        x2_s = lambdas["S"] * y1 % (S * S) if S > 1 else 0
        x2, x2_period = crt_pair(x2_j, J * J, x2_s, S * S)

        y2_r = (
            y1 * pow(lambdas["R"], -1, R * R) % (R * R)
            if R > 1
            else 0
        )
        y2_t = lambdas["T"] * x1 % (T * T) if T > 1 else 0
        y2, y2_period = crt_pair(y2_r, R * R, y2_t, T * T)

        for x2_step, y2_step in ((0, 0), (1, 0), (0, 1), (1, 1)):
            vector = (
                x1,
                y1,
                x2 + x2_step * x2_period,
                y2 + y2_step * y2_period,
            )
            assert in_xi_lattice(vector, cells, lambdas)
            if independent(physical, vector):
                return vector
    raise AssertionError("failed to construct an independent xi-lattice vector")


def audit_minor_divisibility(
    u: tuple[int, ...], v: tuple[int, ...], cells: tuple[int, ...]
) -> int:
    """Check the four exact cell-square divisibilities used by X2."""
    R, S, T, J = cells[:4]
    p = pluecker(u, v)
    assert p["24"] % (R * R) == 0
    assert p["13"] % (J * J) == 0
    assert p["23"] % (S * S) == 0
    assert p["14"] % (T * T) == 0
    assert p["12"] * p["34"] - p["13"] * p["24"] + p["14"] * p["23"] == 0
    return sum(p[key] != 0 for key in ("13", "14", "23", "24"))


def coordinate_plane_lemma_audit() -> int:
    """Exhaust a small box for the exact four-zero-minor classification."""
    checked = 0
    for entries in product(range(-2, 3), repeat=8):
        u = entries[:4]
        v = entries[4:]
        p = pluecker(u, v)
        if not any(p.values()):
            continue
        if any(p[key] for key in ("13", "14", "23", "24")):
            continue

        assert p["12"] * p["34"] == 0
        first_block_zero = u[0] == u[1] == v[0] == v[1] == 0
        second_block_zero = u[2] == u[3] == v[2] == v[3] == 0
        assert first_block_zero != second_block_zero
        checked += 1
    assert checked > 0
    return checked


def histogram(groups: dict[object, list[object]]) -> dict[int, int]:
    return dict(sorted(Counter(map(len, groups.values())).items()))


def check_boundaries() -> dict[str, object]:
    sources = {
        "x1": ROOT / "stages/stage14/14-X1/result.md",
        "four_ci": ROOT / "stages/stage14/14-4ci/result.md",
        "s7_23": ROOT / "stages/stage14/14-s7-23/result.md",
        "four_cj": ROOT / "stages/stage14/14-4cj/result.md",
        "s7_24": ROOT / "stages/stage14/14-s7-24/result.md",
        "t60": ROOT / "stages/stage14/14-t60/result.md",
        "x2": ROOT / "stages/stage14/14-X2/result.md",
    }
    text = {name: path.read_text() for name, path in sources.items()}
    assert "JOINT_COMMON_CORE_CRT_PHYSICAL_FIBER_LEMMA_PROVED=true" in text["x1"]
    assert "COMMON_CORE_FULL_K_DUAL_XI_STRATIFIED_MULTIPLICITY_PROVED=false" in text["four_ci"]
    assert "RANK3_PHYSICAL_ENDPOINT_PACKETS_EXIST=false" in text["s7_23"]
    assert "LOW_RANK_JOINT_COMMON_CORE_CRT_CELL_MULTIPLICITY_PROVED=false" in text["s7_23"]
    assert "XI_RANK2_PHYSICAL_ENDPOINT_PACKETS_EXIST=false" in text["four_cj"]
    assert "XI_PHYSICAL_SHORT_SPAN_RANK=1" in text["four_cj"]
    assert "XI_RANK2_PHYSICAL_ENDPOINT_PACKETS_EXIST=false" in text["s7_24"]
    assert "XI_PHYSICAL_ENDPOINT_SHORT_RANK_EXACT=1" in text["s7_24"]
    assert "XI_ROOT_LINE_QUOTIENT_SATURATION_ORDER=xi^2" in text["s7_24"]
    assert "CANONICAL_PRIME_POLAR_KUMMER_FOURTH_MOMENT_PROVED=false" in text["t60"]
    assert "XI_ROOT_SHORT_VECTOR_RANK_EXACT=1" in text["x2"]
    assert "RANK2_PHYSICAL_ENDPOINT_PACKETS_EXIST=false" in text["x2"]
    assert "JOINT_COMMON_CORE_RESIDUAL_DUAL_RESONANCE_PACKET_ENERGY_PROVED=false" in text["x2"]
    assert "MERGED_4CJ_CORROBORATES_X2=true" in text["x2"]
    assert "MERGED_S7_24_CORROBORATES_X2=true" in text["x2"]
    assert "X2_RANK_ONE_NOVEL_ON_PUBLICATION_BASE=false" in text["x2"]

    summary = json.loads(
        (ROOT / "stages/stage14/data/14-X2/joint_packet_rank_one_summary.json").read_text()
    )
    assert summary["rank_collapse"]["final_physical_short_rank"] == 1
    assert summary["rank_collapse"]["rank_two_exists"] is False
    assert summary["energy_transfer"]["joint_packet_energy_proved"] is False
    assert summary["publication_alignment"]["merged_4cj_corroborates_x2"] is True
    assert summary["publication_alignment"]["merged_s7_24_corroborates_x2"] is True
    assert summary["publication_alignment"]["rank_one_novel_on_publication_base"] is False
    assert summary["current_exponent"] == "7/8"
    assert summary["new_power_saving_proved"] is False
    return summary


def finite_physical_audit(limit: int):
    groups = ch.make_groups(limit)
    rows = []
    nonzero_cross_minors = 0
    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a, b = states[i], states[j]
                if (a["a"], a["b"]) == (b["a"], b["b"]):
                    continue
                if (a["km"], a["kp"]) == (b["km"], b["kp"]):
                    continue

                s7.audit_pair(a, b)
                cells, triple, _, _ = ch.audit_pair(a, b)
                physical = (a["x"], a["y"], b["x"], b["y"])
                assert gcd_many(physical) == 1

                lambdas = xi_lambdas(a, b, cells)
                assert in_xi_lattice(physical, cells, lambdas)
                second = make_independent_lattice_vector(physical, cells, lambdas)
                nonzero_cross_minors += audit_minor_divisibility(physical, second, cells)

                rows.append(
                    {
                        "physical_state": (a["P"], a["Q"], b["P"], b["Q"]),
                        "root_line": physical,
                        "cells": cells,
                        "triple": triple,
                    }
                )

    residual = defaultdict(list)
    residual_line = defaultdict(list)
    joint = defaultdict(list)
    for row in rows:
        residual[row["triple"]].append(row["physical_state"])
        residual_line[(row["triple"], row["root_line"])].append(row["physical_state"])
        joint[(row["triple"], row["cells"], row["root_line"])].append(
            row["physical_state"]
        )

    return {
        "rows": rows,
        "residual": residual,
        "residual_line": residual_line,
        "joint": joint,
        "nonzero_cross_minors": nonzero_cross_minors,
    }


def exponent_ledger_audit() -> None:
    root = Fraction(1, 16)
    minor_ceiling = 2 * root
    cell_floor = Fraction(1, 8)
    modulus_floor = 2 * cell_floor
    gap = modulus_floor - minor_ceiling
    residual_support = Fraction(5, 8)
    current = Fraction(7, 8)

    assert minor_ceiling == Fraction(1, 8)
    assert modulus_floor == Fraction(1, 4)
    assert gap == Fraction(1, 8)
    assert current - residual_support == Fraction(1, 4)


def main() -> None:
    summary = check_boundaries()
    exponent_ledger_audit()
    coordinate_planes = coordinate_plane_lemma_audit()

    expected = summary["finite_audit"]
    finite = finite_physical_audit(expected["cutoff_Q"])
    rows = finite["rows"]
    residual = finite["residual"]
    residual_line = finite["residual_line"]
    joint = finite["joint"]

    assert len(rows) == expected["dual_cross_pairs"]
    assert len(residual) == expected["residual_triple_keys"]
    assert max(map(len, residual.values())) == expected["residual_triple_max_fiber"]
    assert max(map(len, residual_line.values())) == expected["residual_line_max_fiber"]
    assert max(map(len, joint.values())) == expected["joint_key_max_fiber"]
    assert coordinate_planes == expected["coordinate_plane_matrix_pairs_checked"]
    assert finite["nonzero_cross_minors"] == expected["nonzero_cross_minors_checked"]

    witness = residual[(5, 104, 17)]
    assert set(witness) == {
        (41, 54, 1, 246),
        (29, 70, 45, 406),
    }

    print("Stage14-X2 joint packet rank-one audit: PASS")
    print(f"finite cutoff Q<={expected['cutoff_Q']}")
    print(f"dual-cross physical pairs={len(rows)}")
    print(f"residual projection fiber histogram={histogram(residual)}")
    print(f"residual+primitive-line max fiber={max(map(len, residual_line.values()))}")
    print(f"cells+residual+primitive-line max fiber={max(map(len, joint.values()))}")
    print(f"nonzero exact cell-square Pluecker divisibilities={finite['nonzero_cross_minors']}")
    print(f"coordinate-plane matrix pairs checked={coordinate_planes}")
    print("endpoint cross-minor ceiling exponent=1/8")
    print("endpoint cell-square floor exponent=1/4")
    print("endpoint xi short rank=1 (algebraic theorem, not finite inference)")
    print("joint packet energy and new whole-family power saving=not proved")


if __name__ == "__main__":
    main()
