#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ART = HERE / "EX2-04/third-section-valuation-separation.json"
P04A = HERE / "EX2-04/two-divisor-section-pencil.json"
PKNOWN = ROOT / "stages/stage32/residual-32-01-production/post1648ag-v6-known140-basis-elimination.json"

def blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], cwd=ROOT, text=True).strip()

def canonical_sha256(obj: dict) -> str:
    x = dict(obj)
    x.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()

def coeff(decomposition: list[dict], label: int) -> int:
    return next((int(t["multiplicity"]) for t in decomposition if int(t["known140_label_1based"]) == label), 0)

a = json.loads(ART.read_text())
p04 = json.loads(P04A.read_text())
pk = json.loads(PKNOWN.read_text())

assert a["schema"] == "STAGE32EX2_EX2_04B_THIRD_SECTION_VALUATION_SEPARATION_V1"
assert a["status"] == "PASS_CERTIFIED_THREE_DIMENSIONAL_DIVISOR_THEORETIC_SECTION_SUBSPACE_AWAITING_FRESHNESS_CLAIM_SYNC"
assert canonical_sha256(a) == a["canonical_sha256_without_this_field"] == "9d50dc72c467edce946427f1b74786464e1c6401ca86dab6af87bea792d23c70"
assert blob(P04A) == a["source_locks"]["ex2_04a"]["blob_sha1"]
assert p04["canonical_sha256_without_this_field"] == a["source_locks"]["ex2_04a"]["canonical_sha256"]
assert blob(PKNOWN) == a["source_locks"]["known140_v6_divisor"]["blob_sha1"]
assert pk["canonical_sha256_without_this_field"] == a["source_locks"]["known140_v6_divisor"]["canonical_sha256"]

assert pk["decision"]["bounded_positive"] == "V6_CLASS_HAS_AN_EXPLICIT_EFFECTIVE_DIVISOR_REPRESENTATIVE_AS_A_NONNEGATIVE_INTEGER_SUM_OF_KNOWN140_CURVES"
assert pk["known140_monoid"]["all140_pairing_reconstruction_exact"] is True
assert pk["exact_reduction"]["v6_all140_pairing_replay_exact"] is True
D = pk["known140_monoid"]["decomposition"]
selected = {str(j): coeff(D, j) for j in [21, 24, 25, 30, 31]}
assert selected == {"21": 3, "24": 4, "25": 4, "30": 3, "31": 5}
assert a["third_divisor"]["selected_multiplicity_by_label"] == selected
assert a["third_divisor"]["effective"] is True
assert a["third_divisor"]["linearly_equivalent_to_V6"] is True

common04 = p04["common_divisor_inside_certified_pencil"]["minimum_multiplicity_by_label"]
assert common04["25"] == 6
assert p04["reconstruction"]["certified_section_subspace_dimension"] == 2
assert p04["reconstruction"]["complete_H0"] is False
sep = a["valuation_separator"]
assert sep["curve_label_1based"] == 25
assert sep["endpoint_orders"] == {"E17": 6, "E98": 6}
assert sep["all_nonzero_sections_in_W_order_lower_bound"] == 6
assert sep["third_divisor_C25_multiplicity"] == coeff(D, 25) == 4
assert sep["third_divisor_C25_multiplicity"] < sep["all_nonzero_sections_in_W_order_lower_bound"]
assert sep["third_section_line_outside_W"] is True

r = a["reconstruction"]
assert r["previous_subspace_dimension"] == 2
assert r["certified_section_subspace_dimension"] == 3
assert r["linear_independence_certified"] is True
assert r["complete_H0"] is False
assert r["output_type"] == "CERTIFIED_3D_DIVISOR_THEORETIC_SUBSPACE_NOT_COMPLETE_H0"
expected_common = {str(j): min(int(common04[str(j)]), coeff(D, j)) for j in [21, 24, 25, 30, 31]}
assert expected_common == {"21": 3, "24": 3, "25": 4, "30": 2, "31": 5}
assert r["common_retained_divisor_minimum_multiplicity_by_label"] == expected_common

assert a["claim_sync"]["candidate_claim_id"] == "S32.EX2.THREE_DIVISOR_SECTION_SUBSPACE.V1"
assert a["claim_sync"]["authority_status"] == "SCRATCH_PENDING_CURRENT_MAIN_RECONCILIATION"
assert a["claim_sync"]["shared_claim_registry_updated"] is False
assert a["claim_sync"]["stage32_main_authority_changed"] is False
for k in [
    "ambient_coordinate_section_coefficients_obtained", "explicit_surface_polynomial_obtained",
    "complete_H0_reconstructed", "effective_V6_divisor_outside_known140_monoid_obtained",
    "integral_irreducible_V6_member_obtained", "geometric_genus1_V6_member_verified",
    "Q_defined_member_obtained", "population_wide_nonexistence_proved",
    "remaining_five_fixedness_in_complete_linear_system_classified", "stage32_main_credit",
    "Q602_excluded", "O210_excluded", "stage32_closed",
]:
    assert a["limitations"][k] is False, k
for k, v in a["credit_firewall"].items():
    assert v is False, k

print("PASS Stage32EX2 EX2-04B third-section valuation separation")
print("ord_C25(W)>=6 ord_C25(s_EAG)=4 => s_EAG notin W")
print("certified_subspace_dimension=3 complete_H0=false claim_sync=pending_freshness")
print("integral_genus1_member=false stage32_main_credit=false")
