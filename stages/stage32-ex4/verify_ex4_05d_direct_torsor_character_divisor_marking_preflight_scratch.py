#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
ART = HERE / "ex4-05d-direct-torsor-character-divisor-marking-preflight-scratch.json"

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

def canonical_sha256_without_field(obj):
    x = dict(obj)
    expected = x.pop("canonical_sha256_without_this_field")
    payload = json.dumps(x, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    actual = hashlib.sha256(payload).hexdigest()
    assert actual == expected, (actual, expected)

a = load(ART)
canonical_sha256_without_field(a)

assert a["schema"] == "STAGE32EX4_EX4_05D_DIRECT_TORSOR_CHARACTER_DIVISOR_MARKING_PREFLIGHT_SCRATCH_V1"
assert a["status"].startswith("SCRATCH_REPLAYABLE_")
assert a["direct_divisor_anchor"]["curve"].startswith("C0: y^2=x^5-x")
assert a["direct_divisor_anchor"]["function"] == "x"
assert a["direct_divisor_anchor"]["divisor_identity"] == "div(x)=2*P_0-2*P_infinity"
assert a["typed_chain"]["normal_label_9"] == "chi_u"
assert a["typed_chain"]["chi_u_canonical_pair"] == "Z3"
assert a["typed_chain"]["Z3_pair_values"] == ["0", "infinity"]
assert a["typed_chain"]["jacobian_class"] == "delta_0inf=[P_0-P_infinity]"

# Exact polynomial/factorization replay used by the source-side divisor anchor.
def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i+j] += x*y
    return out
assert mul(mul([0,1], [-1,0,1]), [1,0,1]) == [0,-1,0,0,0,1]

target = a["retained_target"]
assert target["ordered_basis"] == ["e1","e2","r*e1","r*e2"]
assert target["W"] == "ker(r mod2)"
assert target["lines"] == {
    "L1": [0,0,1,0],
    "L2": [0,0,0,1],
    "L3": [0,0,1,1],
}
assert target["line_to_Q602_residue"] == {"L1":73,"L2":97,"L3":235}

# Replay load-bearing upstream semantics without introducing a new marking.
for k, spec in a["source_locks"].items():
    p = ROOT / spec["path"]
    u = load(p)
    if "canonical_sha256" in spec:
        assert u["canonical_sha256_without_this_field"] == spec["canonical_sha256"], k

wv = load(ROOT / a["source_locks"]["weierstrass_W"]["path"])
assert wv["weierstrass_model"]["curve"] == "y^2=x^5-x"
assert wv["weierstrass_model"]["cusp_pairs"]["Z3"] == [2,4]
assert wv["weierstrass_model"]["id_to_x"]["2"] == "0"
assert wv["weierstrass_model"]["id_to_x"]["4"] == "infinity"
assert wv["character_pushouts"]["characters"]["chi_u"]["canonical_pair"] == "Z3"
assert wv["torsor_plane"]["retained_F2_4_coordinates_identified"] is False

rv4 = load(ROOT / a["source_locks"]["relative_v4"]["path"])
assert rv4["relative_v4_coupling"]["character_plane"] == "W=image(H^* -> H^1(C0,F2))"
assert rv4["relative_v4_coupling"]["W_dimension"] == 2

rf = load(ROOT / a["source_locks"]["retained_f2_4"]["path"])
assert rf["retained_F2_4_adapter"]["ordered_basis"] == ["e1","e2","r*e1","r*e2"]
assert rf["retained_F2_4_adapter"]["W_equals_kernel_r_mod2"] is True
assert rf["retained_F2_4_adapter"]["W_basis_vectors"] == [[0,0,1,0],[0,0,0,1]]

nodes = load(ROOT / a["source_locks"]["relative_h_nodes"]["path"])
assert nodes["interpretation"]["picB_to_picX_divisor_action_claimed"] is False

loc = load(ROOT / a["source_locks"]["post1648_localization"]["path"])
assert loc["source_bound_chain"]["abstract_class"] == "delta_0inf"
assert loc["finite_marking_obstruction"]["absolute_delta0inf_possible_lines"] == ["L1","L2","L3"]
assert loc["firewalls"]["stage33_J2_source_specific_marking_relabelled_into_stage32"] is False

assert a["control_flow"]["EX4-06"] == "BLOCKED_BY_MISSING_DIRECT_ADAPTER"
assert a["control_flow"]["next_leaf"] == "EX4-08_FROZEN_PACKAGE_AMBIGUITY_CERTIFICATE"
assert a["decision"]["absolute_W_line_identified"] is False
assert a["decision"]["absolute_Q602_residue_identified"] is False
assert a["decision"]["conditional_residue97_promoted"] is False
assert a["decision"]["retained_claim_dag_sync_performed"] is False
assert not any([
    a["firewalls"]["scratch_result_promoted_to_retained_claim"],
    a["firewalls"]["Q602_excluded"],
    a["firewalls"]["O210_excluded"],
    a["firewalls"]["stage32_main_credit"],
    a["firewalls"]["perfect_cuboid_existence_claim"],
    a["firewalls"]["perfect_cuboid_nonexistence_claim"],
])

print("EX4-05D direct torsor/character/divisor marking preflight: PASS")
