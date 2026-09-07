#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT_PATH = HERE / "post1648ae-v6-carrier-member-source-gap.json"

EXPECTED = "db362e83d721a8a344683062c0fbfc4fb5c39ac0ad665b6d46be877257e15047"

def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canonical(doc: dict) -> str:
    body = dict(doc)
    claimed = body.pop("canonical_sha256_without_this_field")
    got = hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()
    assert claimed == got
    return got

def load_json(path: str) -> dict:
    return json.loads((ROOT / path).read_text())

cert = json.loads(CERT_PATH.read_text())
assert canonical(cert) == EXPECTED

locks = cert["source_locks"]

ad = load_json(locks["parent_ad"]["path"])
assert blob_sha1(ROOT / locks["parent_ad"]["path"]) == locks["parent_ad"]["blob_sha1"]
assert canonical(ad) == locks["parent_ad"]["canonical_sha256"]
assert ad["verdict"] == "PASS_STAGE32_POST1648AD_GENUS1_NODE_SPAN_NONEXCLUSION"
assert ad["conditional_geometric_reading"]["actual_carrier_equation_or_ideal_materialized"] is False

ac = load_json(locks["parent_ac"]["path"])
assert canonical(ac) == locks["parent_ac"]["canonical_sha256"]
assert ac["retained_member_level_interface"]["defining_equation_or_ideal_for_carrier_member"] is False
assert ac["retained_member_level_interface"]["distinguished_defining_section_for_carrier_member"] is False
assert ac["retained_member_level_interface"]["uniqueness_of_integral_carrier_in_fixed_V6_class"] is False
assert ac["exact_conditional_common_support_reduction"]["actual_four_way_common_support_materialized"] is False

v6 = load_json(locks["v6_witness"]["path"])
assert blob_sha1(ROOT / locks["v6_witness"]["path"]) == locks["v6_witness"]["blob_sha1"]
assert canonical(v6) == locks["v6_witness"]["canonical_sha256"]
assert v6["target"]["d"] == 186
assert v6["witness"]["self_intersection"] == 758
assert v6["witness"]["positive_exceptional_support"] == 47

src_path = ROOT / locks["audited_surface_invariants"]["path"]
assert blob_sha1(src_path) == locks["audited_surface_invariants"]["blob_sha1"]
src = src_path.read_text()
for fact in locks["audited_surface_invariants"]["required_facts"]:
    assert fact in src

gap = load_json(locks["audited_member_level_gap"]["path"])
assert blob_sha1(ROOT / locks["audited_member_level_gap"]["path"]) == locks["audited_member_level_gap"]["blob_sha1"]
assert canonical(gap) == locks["audited_member_level_gap"]["canonical_sha256"]
missing = gap["missing_member_level_data"]
assert missing["defining_equation_or_ideal_for_N"] is False
assert missing["distinguished_defining_section_for_N"] is False
assert missing["uniqueness_of_integral_carrier_in_fixed_V6_class"] is False
assert missing["picard_class_invariance_sufficient_for_member_invariance"] is False

# Independent exact Riemann--Roch/adjunction replay for the recovered V6 class.
C2 = v6["witness"]["self_intersection"]
KC = v6["target"]["d"]
K2, pg, q = 16, 7, 0
chi_O = 1 - q + pg
K_KminusC = K2 - KC
assert (C2 - KC) % 2 == 0
chi_C = chi_O + (C2 - KC) // 2
assert K_KminusC < 0
# K nef + K.(K-C)<0 => K-C not effective => h2(O(C))=0.
h2 = 0
h0_lower = chi_C
pa = (C2 + KC) // 2 + 1
defect = pa - 1
assert (chi_O, K_KminusC, chi_C, h2, h0_lower, pa, defect) == (8, -170, 294, 0, 294, 473, 472)
assert h0_lower > 0

rr = cert["exact_effective_divisor_replay"]
assert rr["C_square"] == C2
assert rr["K_dot_C"] == KC
assert rr["chi_O"] == chi_O
assert rr["K_dot_K_minus_C"] == K_KminusC
assert rr["h2_O_C"] == h2
assert rr["chi_O_C"] == chi_C
assert rr["h0_lower_bound"] == h0_lower
assert rr["effective_divisor_exists_in_V6_class"] is True
assert rr["arithmetic_genus"] == pa
assert rr["required_total_genus_defect_if_integral"] == defect
assert rr["effective_divisor_is_not_integral_irreducible_genus1_carrier"] is True

b = cert["retained_member_level_boundary"]
assert b["defining_equation_or_ideal_for_carrier_member_materialized"] is False
assert b["distinguished_defining_section_for_carrier_member_materialized"] is False
assert b["uniqueness_of_integral_carrier_in_fixed_V6_class_materialized"] is False
assert b["actual_integral_irreducible_genus1_carrier_materialized"] is False
assert b["class_level_data_sufficient_to_choose_member"] is False
assert b["effective_divisor_existence_sufficient_to_choose_integral_genus1_member"] is False
assert b["C_intersection_ctC_scheme_support_materialized"] is False
assert b["local_ct_fixed_point_adapter_materialized"] is False

dec = cert["decision"]
assert dec["mathematical_nonexistence_claimed"] is False
assert dec["repository_wide_absence_claimed"] is False
assert dec["Q602_excluded"] is False
assert dec["O210_excluded"] is False
assert dec["O212_plus_advance_allowed"] is False
assert dec["survivors_current_credit"] == [73, 97, 235]
assert not any(cert["firewalls"].values())
assert cert["verdict"] == "PASS_STAGE32_POST1648AE_V6_CARRIER_MEMBER_SOURCE_GAP_NONEXCLUSION"

print(json.dumps({
    "verdict": cert["verdict"],
    "certificate_canonical_sha256": EXPECTED,
    "effective_divisor_exists": True,
    "h0_lower_bound": 294,
    "arithmetic_genus": 473,
    "required_genus_defect_if_integral_g1": 472,
    "actual_integral_irreducible_genus1_carrier_materialized": False,
    "carrier_ideal_or_distinguished_section_materialized": False,
    "C_intersection_ctC_scheme_support_materialized": False,
    "Q602_excluded": False,
    "O210_excluded": False,
    "survivors_current_credit": [73,97,235],
}, sort_keys=True))
