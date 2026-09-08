#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ART = HERE / "EX2-04/two-divisor-section-pencil.json"
P03 = HERE / "EX2-03/known140-zero-curve-omission-witnesses.json"
P00 = HERE / "EX2-00/v6-source-lock-target-contract.json"
P01 = HERE / "EX2-01/section-source-inventory.json"

def blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], cwd=ROOT, text=True).strip()

def canonical_sha256(obj: dict) -> str:
    x = dict(obj)
    x.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()

a = json.loads(ART.read_text())
p03 = json.loads(P03.read_text())
p00 = json.loads(P00.read_text())
p01 = json.loads(P01.read_text())

assert a["schema"] == "STAGE32EX2_EX2_04A_TWO_DIVISOR_SECTION_PENCIL_V1"
assert a["status"] == "PASS_CERTIFIED_TWO_DIMENSIONAL_DIVISOR_THEORETIC_SECTION_SUBSPACE"
assert canonical_sha256(a) == a["canonical_sha256_without_this_field"] == "ba5a134d3438453ece33ad05ea5ab556db5108c894864ff3c067269b38d46b34"
for key, path in [("ex2_00", P00), ("ex2_01", P01), ("ex2_03c", P03)]:
    assert blob(path) == a["source_locks"][key]["blob_sha1"]
assert p03["canonical_sha256_without_this_field"] == a["source_locks"]["ex2_03c"]["canonical_sha256"]
assert p00["riemann_roch_scope"]["h0_lower_bound"] == 294
assert p01["target"]["h0_lower_bound"] == 294

W = {w["zero_label_1based"]: w for w in p03["positive_witnesses"]}
assert set(W) == {17, 98}
for k in (17, 98):
    assert W[k]["omitted_curve_coefficient"] == 0
    assert W[k]["picard64_reconstruction_exact"] is True
    assert W[k]["all140_pairing_reconstruction_exact"] is True

def coeff(w: dict, label: int) -> int:
    return next((int(t["multiplicity"]) for t in w["decomposition"] if int(t["known140_label_1based"]) == label), 0)

assert coeff(W[17], 17) == 0 and coeff(W[17], 98) == 1
assert coeff(W[98], 98) == 0 and coeff(W[98], 17) == 1
assert W[17]["decomposition_sha256"] == a["endpoint_divisors"][0]["decomposition_sha256"]
assert W[98]["decomposition_sha256"] == a["endpoint_divisors"][1]["decomposition_sha256"]
assert a["reconstruction"]["endpoint_divisors_distinct"] is True
assert a["reconstruction"]["projective_section_lines_distinct"] is True
assert a["reconstruction"]["certified_section_subspace_dimension"] == 2
assert a["reconstruction"]["projective_pencil_dimension"] == 1
assert a["reconstruction"]["output_type"] == "CERTIFIED_SUBSPACE_NOT_COMPLETE_H0"
assert a["reconstruction"]["complete_H0"] is False
assert a["reconstruction"]["proper_subspace_certified_from_h0_lower_bound"] is True
assert a["section_space_context"]["h0_lower_bound"] == 294

five = [21, 24, 25, 30, 31]
mins = {str(j): min(coeff(W[17], j), coeff(W[98], j)) for j in five}
assert mins == {"21": 3, "24": 3, "25": 6, "30": 2, "31": 5}
assert a["common_divisor_inside_certified_pencil"]["retained_labels_1based"] == five
assert a["common_divisor_inside_certified_pencil"]["minimum_multiplicity_by_label"] == mins
assert a["common_divisor_inside_certified_pencil"]["scope"] == "FIXED_DIVISOR_OF_THIS_CERTIFIED_2D_SUBSPACE_ONLY_NOT_FIXED_PART_OF_COMPLETE_LINEAR_SYSTEM"

for k in [
    "ambient_coordinate_section_coefficients_obtained", "explicit_surface_polynomial_obtained",
    "complete_H0_reconstructed", "outside_known140_member_certified",
    "third_explicit_section_line_outside_pencil_obtained",
    "remaining_five_fixedness_in_complete_linear_system_classified",
    "integral_irreducible_V6_member_obtained", "geometric_genus1_V6_member_verified",
    "Q_defined_member_obtained", "population_wide_nonexistence_proved",
    "stage32_main_credit", "Q602_excluded", "O210_excluded", "stage32_closed",
]:
    assert a["limitations"][k] is False, k
for k, v in a["credit_firewall"].items():
    assert v is False, k
assert a["claim_sync"]["new_claim_id"] == "S32.EX2.TWO_DIVISOR_SECTION_PENCIL.V1"
assert a["claim_sync"]["authority_status"] == "PROVISIONAL"
assert a["claim_sync"]["active_frontier_remap_required"] is False
assert a["claim_sync"]["stage32_main_authority_changed"] is False
print("PASS Stage32EX2 EX2-04A two-divisor section pencil")
print("certified_subspace_dimension=2 complete_H0=false h0_lower_bound=294")
print("common_pencil_divisor_labels=21,24,25,30,31 multiplicities=3,3,6,2,5")
print("outside_known140_member=false integral_genus1_member=false stage32_main_credit=false")
