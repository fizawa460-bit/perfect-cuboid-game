#!/usr/bin/env python3
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CERT = HERE / "e3-pw05-naive-divisor-module-bridge-rejection-v49.json"
ANCHOR = ROOT / "stages/stage33/33-11e/stage33-11e-prime-galois-transport-certificate.json"
TARGET = ROOT / "stages/stage33/33-07/proper-brauer2-from-discriminant.json"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def identity(n: int):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def main() -> None:
    d = load(CERT)
    anchor = load(ANCHOR)
    target = load(TARGET)

    assert d["schema"] == "stage33.e3.pw05_naive_divisor_module_bridge_rejection.v49"
    assert d["parent_v48_commit"] == "8f25d594b6e435359d0455bb0ca7db0ebc017037"
    assert anchor["canonical_sha256"] == d["semantic_anchor"]["canonical_sha256"]

    records = anchor["generator_records"]
    assert len(records) == 14
    for rec in records:
        assert rec["exact_consequence"] == "ZERO_EXACT_PRIME_LEVEL_CC_CT"
        diffs = rec["prime_level_galois_differences"]
        for action in ("cc", "ct"):
            assert diffs[action]["nonzero_prime_coefficients"] == 0
            assert diffs[action]["status"] == "ZERO_EXACT_PRIME_LEVEL"

    assert d["naive_source_module"]["dimension"] == 14
    assert d["naive_source_module"]["cc_action"] == "I14"
    assert d["naive_source_module"]["ct_action"] == "I14"

    assert target["canonical_sha256"] == d["proper14_target"]["canonical_sha256"]
    cc = target["proper_Br2_cc_action_f2"]
    ct = target["proper_Br2_ct_action_f2"]
    I = identity(14)
    assert len(cc) == 14 and all(len(r) == 14 for r in cc)
    assert len(ct) == 14 and all(len(r) == 14 for r in ct)
    assert cc != I or ct != I
    assert d["proper14_target"]["joint_action_is_not_trivial"] is True

    obstruction = d["exact_obstruction"]
    assert obstruction["invertible_equivariant_map_from_naive_source_to_proper14_exists"] is False
    assert obstruction["pw05_direct_basis_identification_route_authorized"] is False
    assert obstruction["p_w_nonexistence_claimed"] is False

    assert d["v48_resolution"]["common_cc_ct_semantic_anchor_found"] is True
    assert d["v48_resolution"]["nine_generator_word_reconstruction_required"] is False
    assert d["v48_resolution"]["result_of_pw05_test"] == "DIRECT_14D_EQUIVARIANT_ISOMORPHISM_REJECTED"

    assert d["next_exact_leaf"]["name"] == "A1_1_H1_DEFINE_THE_ACTUAL_COHOMOLOGICAL_BOUNDARY_SOURCE_TO_PROPER_BR2_MAP"
    assert d["p_w"] == {
        "materialized": False,
        "columns_materialized": 0,
        "e3_mask20_mapped": False,
    }
    assert d["stage33_credit"]["progress_big_tasks"] == "6/11"
    assert d["stage33_credit"]["stage33_12_exact_closed"] is False
    assert d["stage33_credit"]["merge_allowed"] is False
    assert d["status"] == "PASS_EXACT_A1_1_NAIVE_DIVISOR_PACKAGE_EQUIVARIANT_BRIDGE_REJECTED_ROUTE_REFINED"

    print("PASS: V49 naive divisor-package equivariant bridge rejected")


if __name__ == "__main__":
    main()
