#!/usr/bin/env python3
"""Stage14-X1 regression and finite joint physical-fiber audit.

The asymptotic B^o(1) fiber theorem is the divisor reconstruction proved in
merged Stage14-4ch and specialized in the X1 result.  The finite enumeration
below checks the exact maps, their quantifier boundary, and frozen diagnostics;
it is not used as the asymptotic proof.
"""

from collections import Counter, defaultdict
from importlib.util import module_from_spec, spec_from_file_location
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


s7 = load_module(
    "stage14_s7_21_x1",
    HERE.parents[1] / "14-s7-21" / "dual_crt_short_vector_audit.py",
)
x0 = load_module(
    "stage14_x0_x1",
    HERE.parents[1] / "14-X0" / "receiver_transfer_audit.py",
)
ch = load_module(
    "stage14_4ch_x1",
    HERE.parents[1] / "14-4" / "eight_cell_residual_lift_audit.py",
)


def ratio_mod(num: int, den: int, cell: int) -> int:
    """Actual aggregate CRT root ratio; zero is the trivial-cell marker."""
    if cell == 1:
        return 0
    modulus = cell * cell
    assert gcd(den, modulus) == 1
    return (num * pow(den, -1, modulus)) % modulus


def orientation_signature(a: dict[str, int], b: dict[str, int], cells: tuple[int, ...]):
    R, S, T, J, alpha, beta, gamma, delta = cells
    return (
        ratio_mod(a["y"], b["y"], R),
        ratio_mod(a["x"], b["x"], J),
        ratio_mod(b["x"], a["y"], S),
        ratio_mod(b["y"], a["x"], T),
        ratio_mod(a["z"], b["z"], alpha),
        ratio_mod(a["z"], b["z"], beta),
        ratio_mod(a["z"], b["z"], gamma),
        ratio_mod(a["z"], b["z"], delta),
    )


def histogram(groups: dict[object, list[object]]) -> dict[int, int]:
    return dict(sorted(Counter(len(rows) for rows in groups.values()).items()))


def group_rows(rows: list[dict[str, object]], key_name: str):
    groups: dict[object, list[object]] = defaultdict(list)
    for row in rows:
        groups[row[key_name]].append(row["physical"])
    return groups


def check_boundaries() -> dict[str, object]:
    sources = {
        "x0": ROOT / "stages/stage14/14-X0/result.md",
        "four_cf": ROOT / "stages/stage14/14-4cf/result.md",
        "four_ch": ROOT / "stages/stage14/14-4ch/result.md",
        "s7_21": ROOT / "stages/stage14/14-s7-21/result.md",
        "s7_22": ROOT / "stages/stage14/14-s7-22/result.md",
        "t59": ROOT / "stages/stage14/14-t59/result.md",
        "x1": ROOT / "stages/stage14/14-X1/result.md",
    }
    text = {name: path.read_text() for name, path in sources.items()}

    assert "JOINT_COMMON_CORE_CRT_PHYSICAL_FIBER_LEMMA_PROVED=false" in text["x0"]
    assert "GAUSSIAN_SWITCH_ORIENTATION_UNIQUE_UP_TO_UNIT=true" in text["four_cf"]
    assert "FIXED_EIGHT_CELLS_COMMON_CORE_RESIDUAL_PHYSICAL_LIFT_BO1=true" in text["four_ch"]
    assert "PRIMEWISE_ORIENTATION_REFINEMENT_COST=B^o(1)" in text["s7_21"]
    assert "PRODUCT_RATIO_STRATIFIED_XI_DUAL_RESONANCE_ENERGY_PROVED=false" in text["s7_22"]
    assert "SHARED_U_ENERGY_BALANCED_ORTHOGONAL_RECTANGLE_SECOND_MOMENT_PROVED=false" in text["t59"]
    assert "JOINT_COMMON_CORE_CRT_PHYSICAL_FIBER_LEMMA_PROVED=true" in text["x1"]
    assert "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=7/8" in text["x1"]
    assert "NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false" in text["x1"]

    summary = json.loads(
        (ROOT / "stages/stage14/data/14-X1/joint_physical_fiber_summary.json").read_text()
    )
    assert summary["theorem"]["verdict"] == "PROVED_AS_COROLLARY_OF_MERGED_14_4CH"
    assert summary["theorem"]["physical_fiber_bound"] == "B^o(1)"
    assert summary["current_exponent"] == "7/8"
    assert summary["new_power_saving_proved"] is False
    return summary


def enumerate_packets(limit: int) -> list[dict[str, object]]:
    state_groups: dict[tuple[int, int], list[dict[str, int]]] = defaultdict(list)
    for Q in range(2, limit + 1):
        for P in range(1, Q):
            if gcd(P, Q) != 1:
                continue
            state = s7.make_state(P, Q)
            state_groups[(state["xi"], state["k"])].append(state)

    rows: list[dict[str, object]] = []
    for states in state_groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a, b = states[i], states[j]
                if (a["a"], a["b"]) == (b["a"], b["b"]):
                    continue
                if (a["km"], a["kp"]) == (b["km"], b["kp"]):
                    continue

                # Full predecessor regressions on the same physical pair.
                s7.audit_pair(a, b)
                xrow = x0.packet(a, b)
                cells, triple, _, divisor_proxy = ch.audit_pair(a, b)

                assert xrow["cells"] == cells
                assert xrow["labels"] == (a["xi"], a["k"])
                assert xrow["common"][2:] == triple
                assert a["xi"] == cells[0] * cells[1] * cells[2] * cells[3]
                assert a["k"] == cells[4] * cells[5] * cells[6] * cells[7]

                zratio = xrow["crt"][2]
                orientation = orientation_signature(a, b, cells)
                physical = xrow["physical"]
                rows.append(
                    {
                        "physical": physical,
                        "residual": triple,
                        "cells_residual": (cells, triple),
                        "cells_residual_z": (cells, triple, zratio),
                        "joint": (cells, triple, zratio, orientation),
                        "divisor_proxy": divisor_proxy,
                    }
                )
    return rows


def main() -> None:
    summary = check_boundaries()
    expected = summary["finite_audit"]
    limit = expected["cutoff_Q"]
    rows = enumerate_packets(limit)
    assert rows

    residual = group_rows(rows, "residual")
    cells_residual = group_rows(rows, "cells_residual")
    cells_residual_z = group_rows(rows, "cells_residual_z")
    joint = group_rows(rows, "joint")

    residual_max = max(map(len, residual.values()))
    cells_residual_max = max(map(len, cells_residual.values()))
    cells_residual_z_max = max(map(len, cells_residual_z.values()))
    joint_max = max(map(len, joint.values()))
    max_proxy = max(int(row["divisor_proxy"]) for row in rows)

    assert len(rows) == expected["dual_cross_pairs"]
    assert len(residual) == expected["residual_triple_keys"]
    assert residual_max == expected["residual_triple_max_fiber"]
    assert len(cells_residual) == expected["cells_residual_keys"]
    assert cells_residual_max == expected["cells_residual_max_fiber"]
    assert len(joint) == expected["joint_keys"]
    assert joint_max == expected["joint_max_fiber"]
    assert max_proxy == expected["max_divisor_bound_proxy"]
    assert cells_residual_z_max == 1

    witness = residual[(5, 104, 17)]
    assert set(witness) == {
        (41, 54, 1, 246),
        (29, 70, 45, 406),
    }
    companion = residual[(5, 17, 104)]
    assert set(companion) == {
        (13, 95, 245, 247),
        (41, 99, 361, 451),
    }

    # The finite fibers must lie below the explicit divisor-count proxy.
    for key, physical_rows in cells_residual.items():
        proxies = [
            int(row["divisor_proxy"])
            for row in rows
            if row["cells_residual"] == key
        ]
        assert len(physical_rows) <= max(proxies)

    print("Stage14-X1 joint physical-fiber audit: PASS")
    print(f"finite cutoff Q<={limit}")
    print(f"dual-cross physical pairs={len(rows)}")
    print(f"residual projection fiber histogram={histogram(residual)}")
    print(f"cells+residual fiber histogram={histogram(cells_residual)}")
    print(f"cells+residual+z fiber histogram={histogram(cells_residual_z)}")
    print(f"full joint fiber histogram={histogram(joint)}")
    print(f"maximum finite divisor-bound proxy={max_proxy}")
    print("residual-only injectivity=false (frozen two-cell-packet witness)")
    print("fixed cells+residual finite injectivity=true")
    print("asymptotic joint physical fiber B^o(1)=proved by divisor reconstruction")
    print("new whole-family power saving=not proved")


if __name__ == "__main__":
    main()
