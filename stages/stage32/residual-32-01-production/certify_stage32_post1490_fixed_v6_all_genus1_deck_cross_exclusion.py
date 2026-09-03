#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]


def blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def canonical_sha256(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load_json_lock(lock: dict) -> dict:
    path = ROOT / lock["path"]
    if "blob_sha1" in lock:
        assert blob_sha1(path) == lock["blob_sha1"], path
    doc = json.loads(path.read_text())
    if "canonical_sha256" in lock:
        assert canonical_sha256(doc) == lock["canonical_sha256"], path
    return doc


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", required=True)
    args = ap.parse_args()
    cert = json.loads((ROOT / args.check).read_text())
    assert cert["schema"] == "STAGE32_POST1490_FIXED_V6_ALL_GENUS1_DECK_CROSS_EXCLUSION_V1"
    assert canonical_sha256(cert) == cert["canonical_sha256_without_this_field"]
    locks = cert["source_locks"]

    # Source-lock the new O-independent argument and the retained definitions.
    for key in ["general_source_note", "odd_branch_wall", "v4_defect_source_note", "o210_exact_verifier"]:
        assert blob_sha1(ROOT / locks[key]["path"]) == locks[key]["blob_sha1"]

    odd_note = (ROOT / locks["odd_branch_wall"]["path"]).read_text()
    for needle in [
        "sum_P m_P = C.E = e = 266",
        "O = #{P : m_P is odd}",
        "2*g(Y)-2 = O",
        "reachable total odd-contact counts: every even integer from `26` through `266`",
    ]:
        assert needle in odd_note

    boundary = load_json_lock(locks["modular_factor_boundary"])
    transport = boundary["product_cover_degree_transport"]
    assert transport["qprime_1"]["possible"] is False
    assert transport["qprime_2"]["possible"] is False
    assert transport["qprime_4"]["possible"] is True
    assert transport["qprime_4"]["projection_degrees"] == [105, 81]
    assert boundary["new_O_wall"]["provisional_O_min"] == 210

    common = load_json_lock(locks["common_double_cover"])
    square = common["group_quotient_square"]
    assert square["X"] == "P/H_diag (Beauville cover surface)"
    assert square["Q"] if "Q" in square else True
    assert "degree-two pullback" in square["generic_fiber_argument"]
    assert common["carrier_consequence"]["same_quadratic_extension"] is True

    pair = load_json_lock(locks["pair_map_reduction"])
    pm = pair["pair_map_birationality"]
    assert pm["finite_etale_degree"] == 4
    assert pm["deck_group"] == "(H x H)/H_diag ~= V4"
    assert pm["projection_degrees"] == [105, 81]
    assert pm["generic_pair_degree_allowed_by_deck_stabilizer"] == [1, 2, 4]
    assert pm["generic_pair_degree_divides_gcd"] == math.gcd(105, 81) == 3
    assert set(pm["generic_pair_degree_allowed_by_deck_stabilizer"]).intersection({d for d in range(1, 4) if 105 % d == 0 and 81 % d == 0}) == {1}
    assert pm["generic_pair_degree"] == 1
    assert pm["pair_map_birational"] is True

    self_adapter = load_json_lock(locks["beauville_self_adapter"])
    assert self_adapter["resolved_double_cover_adapter"]["conditional_on_hypothetical_carrier_in_exact_v6_class"] is True
    assert self_adapter["resolved_double_cover_adapter"]["arbitrary_B_picard64_promoted_to_picX"] is False
    assert self_adapter["exact_v6_inputs"]["Btilde_class_self_intersection"] == 758
    assert self_adapter["exact_v6_inputs"]["exceptional_square_sum"] == 2358
    d_square = 2 * 758 + 2358
    assert d_square == self_adapter["x_side_exact_lock"]["D_square"] == 3874

    old = load_json_lock(locks["equivariant_deck_cross"])
    expected_cross = old["exact_cross"]
    picard_sum = sum(expected_cross[t]["D_dot_tD"] for t in ["u", "v", "uv"])
    assert [expected_cross[t]["D_dot_tD"] for t in ["u", "v", "uv"]] == [3892, 4020, 4020]
    assert picard_sum == expected_cross["computed_D_translate_sum"] == 11932

    # Re-run the old exact verifier. It in turn reconstructs the recovered V6
    # class from all 140 pairings and reruns the composite deck actions.
    old_verifier = ROOT / locks["o210_exact_verifier"]["path"]
    old_cert = locks["equivariant_deck_cross"]["path"]
    proc = subprocess.run(
        [sys.executable, str(old_verifier), "--check", old_cert],
        cwd=ROOT, text=True, capture_output=True, check=True, timeout=240,
    )
    assert "PASS_EXACT_EQUIVARIANT_BEAUVILLE_DECK_CROSS_O210_Q4_EXCLUSION" in proc.stdout

    # O-independent quotient-square arithmetic.
    gamma_square = 2 * 105 * 81
    assert gamma_square == 17010
    required_sum = gamma_square - d_square
    assert required_sum == 13136
    assert required_sum - picard_sum == 1204

    arg = cert["qprime4_all_overlap_argument"]
    assert arg["pair_map"]["image_self_intersection"] == gamma_square
    assert arg["fixed_x_class"]["D_square"] == d_square
    assert arg["required_translate_sum"]["value"] == required_sum
    assert arg["exact_picard_deck_sum"]["sum"] == picard_sum
    assert arg["contradiction_gap"] == 1204
    assert arg["O_independent"] is True

    # Exhaust the only q'=4 overlap values left by the retained wall and the
    # exact odd-contact definition: sum m_P=266 implies O is even and O<=266.
    candidates = [O for O in range(210, 267) if O % 2 == 266 % 2]
    assert candidates == list(range(210, 267, 2))
    assert candidates == arg["candidate_overlaps"]
    assert all(O > 0 for O in candidates)
    assert required_sum != picard_sum

    dec = cert["decision"]
    assert dec["qprime4_all_admissible_overlaps_excluded"] is True
    assert dec["qprime1_qprime2_retained_excluded"] is True
    assert dec["fixed_V6_all_integral_genus1_carriers_excluded"] is True
    assert dec["promotion_requires_hostile_audit"] is True
    assert dec["stage32_closed"] is False
    assert cert["firewalls"]["all_overlap_generalization_already_audited"] is False
    assert cert["firewalls"]["full178_authorized"] is False
    assert cert["firewalls"]["receiver_credit"] is False

    print("PASS_PROVISIONAL_FIXED_V6_ALL_GENUS1_DECK_CROSS_EXCLUSION")


if __name__ == "__main__":
    main()
