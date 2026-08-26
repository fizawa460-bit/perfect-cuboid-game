#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name):
    return json.loads((HERE / name).read_text(encoding="utf-8"))


def verify_canonical(name, want):
    d = load(name)
    got = d.get("canonical_sha256")
    assert got == want, (name, got, want)
    u = dict(d)
    u.pop("canonical_sha256", None)
    rec = hashlib.sha256(json.dumps(u, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert rec == want, (name, rec, want)
    return d

coord = verify_canonical(
    "elementary-index512-q64-coordinate-sign-census.json",
    "0cbf3a858453b8d2e5dac0f9a0eca5f250e2a079cdc73e508625a55f50f11b62",
)
orbits = verify_canonical(
    "elementary-index512-q64-integral-orbits.json",
    "0b7a0846172706f831b030cb76984a50d47784ca1081fea99a7de65f10d27483",
)
red = verify_canonical(
    "elementary-q64-coordinate-sign-orbit-reduction.json",
    "cea153835ad70d0942c40d972b1e424359f523316f9b0545fa0f7a0b23a9fab6",
)
ne = verify_canonical(
    "nonelementary-k1-action33-simultaneous-q-v4-certified.json",
    "1c09c4cf1367155fbfa73ff3cc28d40b0064b68d4418fe46d44020f32c25502a",
)

assert coord["candidate_count_before"] == 64
assert coord["survivor_indices"] == [120, 121, 122, 123]
assert coord["simultaneous_q_cc_ct_7sign_survivor_count"] == 4
assert coord["rejected_count"] == 60
assert orbits["survivor_count_before"] == 64
assert orbits["integral_Aut_L0_orbit_count"] == 3
assert orbits["orbit_sizes"] == [4, 36, 24]
assert orbits["orbit_representatives"] == [64, 68, 88]
assert orbits["full_Aut_L0_separation_proved_by_split_weight_enumerator"] is True
assert orbits["within_orbit_equivalence_proved_by_explicit_geometric_permutations"] is True
assert red["source_coordinate_sign_census_sha256"] == coord["canonical_sha256"]
assert red["source_integral_orbits_sha256"] == orbits["canonical_sha256"]
assert red["surviving_integral_orbit_count"] == 1
assert red["rejected_integral_orbit_representatives"] == [64, 68]
assert red["surviving_labeled_embedding_indices"] == [120, 121, 122, 123]
r = red["surviving_integral_orbits"][0]
assert r["representative"] == 88 and r["integral_orbit_size"] == 24
assert r["surviving_labeled_embeddings"] == [120, 121, 122, 123]

assert ne["records_checked"] == 33
assert ne["status_counts"] == {"UNSAT": 33}
assert ne["survivor_count"] == 0
assert ne["all_non_elementary_index512_types_eliminated"] is True
assert ne["k1_type_eliminated_by_simultaneous_full_q_v4"] is True
assert ne["k2_type_eliminated_by_predecessor_action_filtration"] is True
assert ne["k3_type_eliminated_by_exact_full_q4"] is True

cert = {
    "schema": "STAGE33_07_INDEX512_UNIQUE_SURVIVING_GLUE_ORBIT_BRIDGE_V1",
    "source_locks": {
        "elementary_coordinate_sign_census_sha256": coord["canonical_sha256"],
        "elementary_integral_orbits_sha256": orbits["canonical_sha256"],
        "elementary_coordinate_sign_orbit_reduction_sha256": red["canonical_sha256"],
        "nonelementary_full_elimination_sha256": ne["canonical_sha256"],
    },
    "elementary_finite_q_v4_compatible_labeled_embeddings_before_seven_signs": 64,
    "elementary_simultaneous_q_cc_ct_seven_sign_labeled_embeddings_after": 4,
    "elementary_surviving_labeled_embeddings": [120, 121, 122, 123],
    "elementary_integral_Aut_L0_orbits_before_seven_signs": 3,
    "elementary_integral_Aut_L0_orbit_representatives_before_seven_signs": [64, 68, 88],
    "elementary_surviving_integral_Aut_L0_orbit_count": 1,
    "elementary_surviving_integral_Aut_L0_orbit_representative": 88,
    "elementary_surviving_integral_Aut_L0_orbit_size": 24,
    "non_elementary_survivor_count": 0,
    "all_non_elementary_index512_types_eliminated": True,
    "unique_surviving_integral_glue_orbit_among_locked_endpoint_compatibility_candidates": True,
    "unique_surviving_integral_glue_orbit_representative": 88,
    "actual_geometry_glue_existence_in_rep88_orbit_proved": False,
    "actual_index512_glue_identified": False,
    "actual_index512_glue_identification_blocker": "Need an exact adapter from the geometric endpoint overlattice/theta data to the locked ambient L0 candidate universe and the surviving rep88 orbit; endpoint-compatible candidate uniqueness alone does not prove actual-glue existence or equality.",
    "new_residual_kernel": "R33-BR2A-INDEX512-UNIQUE-SURVIVING-ELEMENTARY-REP88-INTEGRAL-ORBIT-BUT-ACTUAL-GLUE-ADAPTER-OPEN",
    "next_exact_leaf": "L33-07-MATCH-REP88-TO-ACTUAL-ENDPOINT-THETA-GLUE-OR-REJECT",
    "arithmetic_HS_closed": False,
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "stage33_09_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
    "unit_status": "RUNNING_REPAIR",
}
canonical = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(canonical).hexdigest()
out = HERE / "index512-unique-surviving-glue-orbit-bridge.json"
out.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "non_elementary_survivors": 0,
    "surviving_integral_orbits": 1,
    "representative": 88,
    "actual_glue_identified": False,
    "next_exact_leaf": cert["next_exact_leaf"],
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
