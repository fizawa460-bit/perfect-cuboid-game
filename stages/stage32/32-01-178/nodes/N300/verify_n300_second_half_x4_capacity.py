#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
N260_STATE = HERE.parent / "N260/STATE.json"
N280_STATE = HERE.parent / "N280/STATE.json"
N290_STATE = HERE.parent / "N290/STATE.json"

EXPECTED = {
    ("g0-d174", 48): {"normal": 3066, "n280_rejected": 3067, "a": None},
    ("g0-d176", 48): {"normal": 3104, "n280_rejected": 0, "a": 1172},
    ("g1-d190", 48): {"normal": 3370, "n280_rejected": 3371, "a": None},
    ("g1-d192", 48): {"normal": 3408, "n280_rejected": 0, "a": 1292},
}


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def main() -> None:
    n260 = json.loads(N260_STATE.read_text())
    n280 = json.loads(N280_STATE.read_text())
    n290 = json.loads(N290_STATE.read_text())
    if n260.get("node_id") != "N260" or n260["proof"].get("full_exceptional_vector") != "[1]^48":
        raise ValueError("N260 rigidity authority regression")
    if n280.get("node_id") != "N280" or n290.get("node_id") != "N290":
        raise ValueError("N280/N290 authority regression")
    if n290["validation"].get("forced_a_formula") != "a=(-2024 + 15*normal_mass)/38":
        raise ValueError("N290 forced-a formula regression")
    if int(n290["validation"].get("x4_coefficient", -1)) != 0:
        raise ValueError("N290 x4 coefficient regression")

    n260_blocks = {
        (str(row["row_id"]), int(row["e"])): int(row["normal_x4_block"])
        for row in n260["retained_result"]["one_block_strata"]
    }
    n280_rows = {
        (str(row["row_id"]), int(row["e"])): row
        for row in n280["validation"]["strata"]
    }
    n290_remaining = {
        (str(row["row_id"]), int(row["e"])): row
        for row in n290["validation"]["remaining_strata"]
    }

    rows = []
    n280_rejected_total = 0
    n300_additional_rejected_total = 0
    survivor_total = 0
    for key, expected in EXPECTED.items():
        block = n260_blocks[key]
        normal = int(expected["normal"])
        if block != normal + 1:
            raise ValueError(f"x4 block / normal total regression: {key}")
        n280_row = n280_rows[key]
        n280_rejected = int(n280_row["rejected"])
        if n280_rejected != int(expected["n280_rejected"]):
            raise ValueError(f"N280 rejection regression: {key}")
        n280_rejected_total += n280_rejected

        if n280_rejected == block:
            rows.append({
                "row_id": key[0], "e": key[1], "normal_total": normal,
                "n280_rejected": block,
                "n300_additional_rejected": 0,
                "survivor_count_after_n300": 0,
                "x4_max_after_n300": None,
                "second_half_total": None,
            })
            continue

        rem = n290_remaining.get(key)
        if rem is None:
            raise ValueError(f"missing N290 survivor stratum: {key}")
        a = int(rem["forced_a"])
        if a != int(expected["a"]):
            raise ValueError(f"forced-a regression: {key}")
        second_half = normal - a
        if not 0 <= second_half <= normal:
            raise ValueError(f"invalid second-half total: {key}")

        # Source semantics: normal pairings labels 1..92 are nonnegative;
        # first half is labels 1..46, so second half is labels 47..92.
        # label49=x4 lies in the second half. Hence x4 cannot exceed the
        # entire second-half mass.
        x4_max = second_half
        survivors = x4_max + 1
        additional_rejected = block - survivors
        if additional_rejected != a:
            raise AssertionError("tail-rejection identity should equal first-half mass")
        rows.append({
            "row_id": key[0], "e": key[1], "normal_total": normal,
            "forced_first_half_total": a,
            "second_half_total": second_half,
            "label49_x4_is_in_second_half": True,
            "necessary_cut": f"0 <= x4 <= {second_half}",
            "n280_rejected": 0,
            "n300_additional_rejected": additional_rejected,
            "survivor_count_after_n300": survivors,
            "x4_max_after_n300": x4_max,
        })
        n300_additional_rejected_total += additional_rejected
        survivor_total += survivors

    total = sum(n260_blocks.values())
    if n280_rejected_total != 6438:
        raise ValueError("N280 total regression")
    if n300_additional_rejected_total != 2464:
        raise ValueError("N300 additional rejection regression")
    if survivor_total != 4050:
        raise ValueError("N300 survivor total regression")
    if n280_rejected_total + n300_additional_rejected_total + survivor_total != total:
        raise ValueError("N260 four-stratum partition regression")

    body = {
        "schema": "STAGE32_32_01_178_N300_SECOND_HALF_X4_CAPACITY_V1",
        "source_scope": "N260 four e=K=48 one-exceptional-block strata",
        "derivation": {
            "all_92_normal_pairings_nonnegative": True,
            "first_half_labels_1based": [1, 46],
            "second_half_labels_1based": [47, 92],
            "x4_known_label_1based": 49,
            "x4_is_second_half_coordinate": True,
            "normal_total": "19*d-5*e",
            "first_half_total": "N290 exact forced a",
            "second_half_total": "normal_total-a",
            "necessary_inequality": "0 <= x4 <= second_half_total"
        },
        "strata": rows,
        "aggregate": {
            "n260_four_stratum_terminal_count": total,
            "n280_lattice_rejected": n280_rejected_total,
            "n300_additional_nonnegativity_rejected": n300_additional_rejected_total,
            "combined_n280_n300_rejected": n280_rejected_total + n300_additional_rejected_total,
            "survivors_after_n300": survivor_total
        },
        "semantics": {
            "exact_necessary_nonnegativity_cut": True,
            "zero_loss_relative_to_n260_n290_authorities": True,
            "does_not_run_z3": True,
            "does_not_duplicate_ex5_adaptive_exceptional_partition": True,
            "n260_n280_n290_audit_dependencies_must_be_respected": True,
            "survival_is_not_picard_sat": True,
            "full178_complete": False,
            "heavy_compute": False,
            "theorem_credit": False
        }
    }
    print(json.dumps({**body, "canonical_sha256_without_this_field": csha(body)}, sort_keys=True))


if __name__ == "__main__":
    main()
