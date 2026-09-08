#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CERT = ROOT / "stages/stage32/scratch/ex1-ex4-deraux-order8-fixed-point-difference-criterion-20260908.json"
ORDER8 = ROOT / "stages/stage32/scratch/ex1-ex4-order8-fixed-line-reentry-20260908.json"


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def det_int(a: list[list[int]]) -> int:
    if len(a) == 1:
        return a[0][0]
    out = 0
    for j, x in enumerate(a[0]):
        minor = [row[:j] + row[j+1:] for row in a[1:]]
        out += (-1) ** j * x * det_int(minor)
    return out


def sub_identity(a: list[list[int]]) -> list[list[int]]:
    out = [row[:] for row in a]
    for i in range(len(out)):
        out[i][i] -= 1
    return out


def matvec_mod2(a: list[list[int]], v: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(x*y for x, y in zip(row, v)) & 1 for row in a)


def fixed_nonzero_mod2(a: list[list[int]]) -> list[tuple[int, ...]]:
    n = len(a)
    ans = []
    for bits in range(1, 1 << n):
        v = tuple((bits >> i) & 1 for i in range(n))
        if matvec_mod2(a, v) == v:
            ans.append(v)
    return ans


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    prior = json.loads(ORDER8.read_text(encoding="utf-8"))

    assert cert["schema"] == "STAGE32_MAIN_SCRATCH_EX1_EX4_DERAUX_ORDER8_FIXED_POINT_DIFFERENCE_CRITERION_V1"
    assert cert["status"] == "SCRATCH_EXACT_UNAUDITED_CROSS_LANE_REENTRY_CRITERION"
    lock = cert["source_locks"]["order8_reentry_scratch"]
    assert blob_sha1(ORDER8) == lock["blob_sha1"]

    kkk = prior["kkk_order8_homology"]
    M = kkk["T_mu1"]
    assert det_int(sub_identity(M)) == 2
    assert fixed_nonzero_mod2(M) == [tuple(kkk["unique_nonzero_mod2_fixed_vector"])]

    retained = prior["retained_order8_representative"]
    R = retained["matrix_on_retained_integral_basis"]
    assert det_int(sub_identity(R)) == 2
    assert fixed_nonzero_mod2(R) == [tuple(retained["unique_nonzero_mod2_fixed_vector"])]
    assert retained["unique_fixed_W_line"] == "L2"
    assert retained["conditional_residue_if_B9_equals_this_marked_element"] == 97

    lemma = cert["fixed_point_difference_lemma"]
    assert lemma["hypothesis_characteristic_polynomial"] == "chi_M(x)=x^4+1"
    assert "chi_M(1)=2" in lemma["kernel_order_formula"]
    assert cert["curve_side_specialization"]["fixed_pair"] == ["0", "delta_0inf"]
    assert cert["curve_side_specialization"]["fixed_point_difference"] == "delta_0inf"

    decision = cert["decision"]
    assert decision["absolute_delta0inf_retained_W_line_identified_now"] is False
    assert decision["uniform_EX1_residue_count_now"] == 3
    assert decision["conditional_if_difference_maps_to_L1"] == 73
    assert decision["conditional_if_difference_maps_to_L2"] == 97
    assert decision["conditional_if_difference_maps_to_L3"] == 235
    assert decision["authority_changed"] is False
    assert decision["claim_dag_changed"] is False
    assert decision["Q602_excluded"] is False
    assert decision["O210_excluded"] is False

    fw = cert["firewalls"]
    assert fw["Deraux_R1R2R3_assumed_to_be_the_exact_marked_B9_image"] is False
    assert fw["one_fixed_point_promoted_to_fixed_point_difference"] is False
    assert fw["conditional_residue97_promoted"] is False

    print("PASS scratch Deraux order-8 fixed-point difference criterion")
    print("det(I-M)=2 on both explicit order-8 H1 models; fixed difference is one nonzero A[2] class")
    print("absolute_line=UNRESOLVED residues=73,97,235 authority=SCRATCH_UNAUDITED")


if __name__ == "__main__":
    main()
