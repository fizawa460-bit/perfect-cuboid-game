#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT = HERE / "post1623-hperp-v6-hdeck-character-preflight.json"
DIAG = HERE / "diagnose_stage32_post1623_hperp_v6_hdeck_anchor.py"
EXPECTED_CERT = "00843ec64f7ecd522614f750c9f84d3a746ce664064d1c4413784cab9d26791c"
EXPECTED_PROFILE_DISTRIBUTION = {
    "0000": 48, "0001": 3, "0010": 3, "0100": 3,
    "0101": 6, "0111": 1, "1000": 3, "1010": 6,
    "1011": 1, "1101": 1, "1110": 1, "1111": 16,
}


def csha(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_canonical(path: Path, expected: str):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256_without_this_field")
    assert claimed == expected == csha(body), (path, claimed, csha(body))
    return obj


def source_path(rel: str) -> Path:
    return ROOT / rel


cert = load_canonical(CERT, EXPECTED_CERT)
for lock_name, lock in cert["source_locks"].items():
    expected = lock.get("canonical_sha256")
    if expected is None:
        continue
    load_canonical(source_path(lock["path"]), expected)

# Independent semantic firewalls from retained source assets.
abstract_w = json.loads(source_path(cert["source_locks"]["abstract_w_weierstrass_lock"]["path"]).read_text(encoding="utf-8"))
relative = json.loads(source_path(cert["source_locks"]["relative_v4_coupling"]["path"]).read_text(encoding="utf-8"))
gauge = json.loads(source_path(cert["source_locks"]["marked_w_line_gauge_orbit"]["path"]).read_text(encoding="utf-8"))
assert relative["relative_v4_coupling"]["character_plane"] == "W=image(H^* -> H^1(C0,F2))"
assert relative["relative_v4_coupling"]["W_dimension"] == 2
chars = abstract_w["character_pushouts"]["characters"]
assert chars["chi_u"]["values"] == {"u": 1, "v": 0, "uv": 1}
assert chars["chi_u"]["canonical_pair"] == "Z3"
assert abstract_w["weierstrass_model"]["cusp_pairs"]["Z3"] == [2, 4]
assert abstract_w["torsor_plane"]["nonzero_classes"][2] == {
    "name": "delta_0inf", "pair_ids": [2, 4], "pair_values": ["0", "infinity"]
}
assert abstract_w["torsor_plane"]["retained_F2_4_coordinates_identified"] is False
assert gauge["firewalls"]["absolute_delta0inf_retained_line_identified"] is False

# Recompute the bounded Picard/H-deck diagnostic at the exact head.
proc = subprocess.run([sys.executable, str(DIAG)], check=True, text=True, capture_output=True)
diag = json.loads(proc.stdout)
assert diag["schema"] == "STAGE32_POST1623_HPERP_V6_HDECK_COMMON_ANCHOR_DIAGNOSTIC_V2"
assert diag["fixed_target"]["surviving_residues_decimal"] == [73, 97, 235]
records = diag["v6_hdeck_translate_records"]
assert [r["h_element"] for r in records] == ["id", "u", "v", "uv"]
assert [r["v6_translate_intersection_with_normal_label_1"] for r in records] == [13, 11, 7, 9]
assert [r["v6_translate_intersection_with_normal_label_1_mod2"] for r in records] == [1, 1, 1, 1]
assert [r["hperp_separator_coordinate_1_value_mod2"] for r in records] == [1, 1, 1, 1]
assert all(r["translate_outside_exceptional_span_mod2"] for r in records)

profiles = diag["all_92_normal_curve_intersection_parity_profiles"]
assert profiles["coordinate_order"] == ["id", "u", "v", "uv"]
assert profiles["distinct_profile_count"] == 12
assert profiles["profile_distribution"] == EXPECTED_PROFILE_DISTRIBUTION
assert profiles["nonconstant_profile_label_count"] == 28
assert profiles["first_nonconstant_profile"] == {
    "normal_label_1based": 9, "profile_id_u_v_uv": [0, 1, 0, 1]
}
assert profiles["first_nontrivial_affine_H_character_hit"] == {
    "normal_label_1based": 9, "character": "chi_u", "profile_id_u_v_uv": [0, 1, 0, 1]
}
hits = profiles["nontrivial_affine_H_character_label_sets"]
assert hits["chi_u"] == [9, 14, 85, 88, 89, 92]
assert hits["1+chi_u"] == [12, 15, 86, 87, 90, 91]
assert hits["chi_v"] == [] and hits["chi_uv"] == []
assert diag["h_orbit_sum"] == {
    "separator_coordinate_1_value_mod2": 0,
    "outside_exceptional_span_mod2": True,
}

# Certificate must report only the exact bounded consequence.
assert cert["exact_hdeck_probe"]["source_bound_nontrivial_character"]["normal_curve_label_1based"] == 9
assert cert["exact_hdeck_probe"]["source_bound_nontrivial_character"]["profile"] == [0, 1, 0, 1]
assert cert["abstract_character_to_w_binding"]["abstract_class_name"] == "delta_0inf"
assert cert["abstract_character_to_w_binding"]["retained_F2_4_coordinate_line_identified"] is False
assert cert["bounded_conclusion"]["absolute_delta0inf_retained_W_line_still_unidentified"] is True
assert cert["bounded_conclusion"]["audited_three_residues_still_not_arithmetically_contracted"] is True
assert cert["bounded_conclusion"]["q602_residue_specific_commutator_obtained"] is False
assert cert["firewalls"]["abstract_group_isomorphism_used_as_semantic_adapter"] is False
assert cert["firewalls"]["cecotti_curve_automorphism_to_retained_lattice_generator_identification_claimed"] is False
assert cert["firewalls"]["Q602_excluded"] is False
assert cert["firewalls"]["O210_excluded"] is False
assert cert["firewalls"]["O212_plus_advance_allowed"] is False

print("POST1623_HPERP_V6_HDECK_CHARACTER_PREFLIGHT_COMPLETE")
print(f"certificate_canonical={EXPECTED_CERT}")
print("normal_label_9_profile=id,u,v,uv:0,1,0,1=chi_u")
print("abstract_character=chi_u -> Z3 -> delta_0inf")
print("absolute_retained_W_line_identified=false")
print("Q602_excluded=false O210_excluded=false O212_plus_advance_allowed=false")
