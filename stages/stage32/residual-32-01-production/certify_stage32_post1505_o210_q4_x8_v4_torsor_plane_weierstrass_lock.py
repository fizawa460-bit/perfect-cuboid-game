#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
EXPECTED_CANONICAL = "c84242981cbf81c9935c6851d8a95dc4dc0f1d8afbdba7ba7bbe16385bf1282f"


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def canonical_sha256(doc: dict) -> str:
    body = dict(doc)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load_json_lock(lock: dict) -> dict:
    path = ROOT / lock["path"]
    assert path.is_file(), path
    assert blob_sha1(path) == lock["blob_sha1"], path
    doc = json.loads(path.read_text())
    if "canonical_sha256" in lock:
        assert canonical_sha256(doc) == lock["canonical_sha256"], path
    return doc


def dot2(a: tuple[int, int], b: tuple[int, int]) -> int:
    return (a[0] * b[0] + a[1] * b[1]) & 1


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", required=True)
    args = ap.parse_args()

    cert_path = ROOT / args.check
    cert = json.loads(cert_path.read_text())
    assert cert["schema"] == "STAGE32_POST1505_O210_Q4_X8_V4_TORSOR_PLANE_WEIERSTRASS_LOCK_V1"
    assert canonical_sha256(cert) == cert["canonical_sha256_without_this_field"]
    assert cert["canonical_sha256_without_this_field"] == EXPECTED_CANONICAL

    locks = cert["source_locks"]
    x8 = load_json_lock(locks["x8_v4_quotient"])
    adapter = load_json_lock(locks["weierstrass_adapter"])
    principal = load_json_lock(locks["principal_rosati"])
    coupling = load_json_lock(locks["upstream_relative_v4_coupling"])

    adapter_note_path = ROOT / locks["weierstrass_adapter_note"]["path"]
    assert adapter_note_path.is_file()
    assert blob_sha1(adapter_note_path) == locks["weierstrass_adapter_note"]["blob_sha1"]
    adapter_note = adapter_note_path.read_text()

    note_path = ROOT / locks["source_note"]["path"]
    assert note_path.is_file()
    assert blob_sha1(note_path) == locks["source_note"]["blob_sha1"]
    note = note_path.read_text()

    assert x8["exact_group_checks"]["Gamma_prime_4_over_Gamma8_order"] == 4
    assert x8["exact_group_checks"]["Gamma_prime_4_over_Gamma8_free_on_X8"] is True
    assert x8["quotient_geometry"]["X8_to_C0_degree"] == 4
    assert x8["quotient_geometry"]["X8_to_C0_etale"] is True
    assert x8["quotient_geometry"]["six_quotient_cusps_are_Weierstrass_points"] is True
    assert coupling["relative_v4_coupling"]["W_dimension"] == 2
    assert coupling["relative_v4_coupling"]["character_plane"] == "W=image(H^* -> H^1(C0,F2))"

    assert locks["weierstrass_adapter"]["hostile_reaudit_review"] == 5083834097
    assert adapter["cusp_pairs"] == {"Z1": [1, 6], "Z2": [3, 5], "Z3": [2, 4]}
    assert adapter["inertia"] == {"Z1": "T4*u", "Z2": "T4*uv", "Z3": "T4*1"}
    assert "{+1:1, -1:6, +i:3, -i:5, 0:2, infinity:4}" in adapter_note

    supported = principal["source_locks"]["external_principal_g12"]["exact_supported_facts"]
    assert any("Bolza curve y^2=x^5-x" in s for s in supported)
    assert principal["principal_polarization"]["riemann_form_basis"] == ["e1", "e2", "r*e1", "r*e2"]

    pairs = {k: set(v) for k, v in adapter["cusp_pairs"].items()}
    inertia_h = {"Z1": (1, 0), "Z2": (1, 1), "Z3": (0, 0)}
    chars = {"chi_u": (1, 0), "chi_v": (0, 1), "chi_uv": (1, 1)}
    universe = set(range(1, 7))

    expected_canonical = {"chi_u": "Z3", "chi_v": "Z2", "chi_uv": "Z1"}
    expected_branch_pairs = {
        "chi_u": ["Z1", "Z2"],
        "chi_v": ["Z2"],
        "chi_uv": ["Z1"],
    }

    derived_pairs: dict[str, frozenset[int]] = {}
    for name, chi in chars.items():
        branch_names = [z for z in ("Z1", "Z2", "Z3") if dot2(chi, inertia_h[z])]
        assert branch_names == expected_branch_pairs[name]
        branch = set().union(*(pairs[z] for z in branch_names))
        canonical = branch if len(branch) <= 2 else universe - branch
        zcanon = expected_canonical[name]
        assert canonical == pairs[zcanon]
        derived_pairs[name] = frozenset(canonical)

        cdoc = cert["character_pushouts"]["characters"][name]
        assert cdoc["branch_pairs"] == branch_names
        assert cdoc["canonical_pair"] == zcanon

    plane_pairs = [frozenset(x["pair_ids"]) for x in cert["torsor_plane"]["nonzero_classes"]
    assert set(plane_pairs) == set(derived_pairs.values())
    assert all(len(p) == 2 for p in plane_pairs)
    assert set().union(*[set(p) for p in plane_pairs]) == universe
    assert sum(len(p) for p in plane_pairs) == 6
    for i in range(3):
        for j in range(i + 1, 3):
            assert plane_pairs[i].isdisjoint(plane_pairs[j])
            assert (len(plane_pairs[i] & plane_pairs[j]) & 1) == 0

    symdiff = set()
    for p in plane_pairs:
        symdiff ^= set(p)
    assert symdiff == universe

    assert cert["torsor_plane"]["dimension"] == 2
    assert cert["torsor_plane"]["sum_of_three_nonzero_classes_zero"] is True
    assert cert["torsor_plane"]["pairwise_weil_orthogonal"] is True
    assert cert["torsor_plane"]["maximal_weil_isotropic"] is True
    assert cert["torsor_plane"]["richelot_kernel_for_factorization"] is True
    assert cert["torsor_plane"]["retained_F2_4_coordinates_identified"] is False

    model = cert["weierstrass_model"]
    assert model["curve"] == "y^2=x^5-x"
    assert model["factorization"] == "x^5-x = x*(x^2-1)*(x^2+1)"
    assert model["id_to_x"] == {"1": "+1", "6": "-1", "3": "+i", "5": "-i", "2": "0", "4": "infinity"}

    for needle in [
        "W\\{0} = { [w_1-w_6], [w_3-w_5], [w_2-w_4] }",
        "x^5-x = x * (x^2-1) * (x^2+1)",
        "no coordinate vector in `F2^4` is guessed here",
    ]:
        assert needle in note, needle

    decision = cert["decision"]
    assert decision["actual_global_W_abstractly_identified"] is True
    assert decision["arbitrary_two_plane_search_authorized"] is False
    assert decision["exact_retained_F2_4_translation_pending"] is True
    assert decision["pointwise_28_residue_test_pending"] is True
    assert decision["Q602_excluded"] is False
    assert decision["O210_excluded"] is False

    print(json.dumps({
        "schema": cert["schema"],
        "canonical": EXPECTED_CANONICAL,
        "W_nonzero_pair_ids": [sorted(p) for p in plane_pairs],
        "W_dimension": 2,
        "maximal_weil_isotropic": True,
        "retained_F2_4_coordinates_identified": False,
        "next_exact_leaf": decision["next_exact_leaf"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
