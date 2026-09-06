#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT_PATH = HERE / "post1648-delta0inf-retained-w-absolute-marking-localization.json"
EXPECTED_CERT = "edb37e52cd92ae56c4c12c59d0af974dc4463bce52b25b3e8b64dc2c7afdd3c2"


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def canonical_without_field(obj: dict, field: str) -> str:
    body = dict(obj)
    body.pop(field, None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load_locked_json(lock: dict) -> dict:
    path = ROOT / lock["path"]
    assert path.is_file(), lock["path"]
    assert git_blob_sha(path) == lock["blob_sha1"], lock["path"]
    obj = json.loads(path.read_text(encoding="utf-8"))
    expected = lock["canonical_sha256"]
    if "canonical_sha256_without_this_field" in obj:
        assert obj["canonical_sha256_without_this_field"] == expected
        assert canonical_without_field(obj, "canonical_sha256_without_this_field") == expected
    elif "canonical_sha256" in obj:
        assert obj["canonical_sha256"] == expected
        assert canonical_without_field(obj, "canonical_sha256") == expected
    else:
        raise AssertionError(f"no canonical field: {lock['path']}")
    return obj


cert = json.loads(CERT_PATH.read_text(encoding="utf-8"))
assert cert["canonical_sha256_without_this_field"] == EXPECTED_CERT
assert canonical_without_field(cert, "canonical_sha256_without_this_field") == EXPECTED_CERT

locks = cert["source_locks"]
for name, lock in locks.items():
    path = ROOT / lock["path"]
    assert path.is_file(), name
    assert git_blob_sha(path) == lock["blob_sha1"], name

post1643 = load_locked_json(locks["post1643_h_character"])
abstract_w = load_locked_json(locks["abstract_w_weierstrass"])
satake = load_locked_json(locks["satake_boundary_marking"])
boundary = load_locked_json(locks["boundary_weierstrass_adapter"])
gauge = load_locked_json(locks["marked_w_gauge_orbit"])
fsm = load_locked_json(locks["fsm_stoll_diagonal_action"])
relative = load_locked_json(locks["relative_h_deck"])
node = load_locked_json(locks["relative_h_marked_node_action"])

# Source-bound delta_0inf chain.
probe = post1643["exact_hdeck_probe"]["source_bound_nontrivial_character"]
assert probe["normal_curve_label_1based"] == 9
assert probe["character_name"] == "chi_u"
assert probe["profile"] == [0, 1, 0, 1]
chars = abstract_w["character_pushouts"]["characters"]
assert chars["chi_u"]["canonical_pair"] == "Z3"
assert abstract_w["weierstrass_model"]["cusp_pairs"]["Z3"] == [2, 4]
assert abstract_w["torsor_plane"]["nonzero_classes"][2] == {
    "name": "delta_0inf",
    "pair_ids": [2, 4],
    "pair_values": ["0", "infinity"],
}
z3_block = next(x for x in satake["C2_blocks"] if x["box_coordinate"] == "Z3=b3")
assert z3_block["labels"] == [41, 42, 43, 44]
for label, wid in {"41": 4, "42": 4, "43": 2, "44": 2}.items():
    assert boundary["boundary_label_to_weierstrass_id"][label] == wid

# Reconstruct the exact abstract S action from locked box/H naming.
S = fsm["fsm_section2_actions"]["S"]
assert S["normalized_box_action"] == ["a3", "-a2", "a1", "b3", "b2", "b1", "c"]
assert relative["equivariant_adapter"]["modular_to_stoll"] == {
    "u": "g7*g9", "uv": "g8*g9", "v": "g7*g8"
}
assert node["modular_to_stoll"]["T"] == "g9 (b3 sign)"
assert node["modular_to_stoll"]["Tprime"] == "g7 (b1 sign)"
assert node["modular_to_stoll"]["R"] == "g7*g8*g9 (b1,b2,b3 signs projectively)"

H_support = {
    "u": frozenset({"b1", "b3"}),
    "v": frozenset({"b1", "b2"}),
    "uv": frozenset({"b2", "b3"}),
}
S_coord = {"b1": "b3", "b2": "b2", "b3": "b1"}
conj = {}
for h, support in H_support.items():
    image = frozenset(S_coord[x] for x in support)
    conj[h] = next(k for k, v in H_support.items() if v == image)
assert conj == {"u": "u", "v": "uv", "uv": "v"}

char_values = {
    "chi_u": {"u": 1, "v": 0, "uv": 1},
    "chi_v": {"u": 0, "v": 1, "uv": 1},
    "chi_uv": {"u": 1, "v": 1, "uv": 0},
}
char_action = {}
for cname, vals in char_values.items():
    transformed = {h: vals[conj[h]] for h in ["u", "v", "uv"]}
    char_action[cname] = next(k for k, v in char_values.items() if v == transformed)
assert char_action == {"chi_u": "chi_uv", "chi_v": "chi_v", "chi_uv": "chi_u"}
pair_to_delta = {"Z1": "delta_pm1", "Z2": "delta_pmi", "Z3": "delta_0inf"}
char_to_delta = {name: pair_to_delta[data["canonical_pair"]] for name, data in chars.items()}
delta_action = {
    char_to_delta[c]: char_to_delta[char_action[c]]
    for c in ["chi_u", "chi_v", "chi_uv"]
}
assert delta_action == {
    "delta_pm1": "delta_0inf",
    "delta_pmi": "delta_pmi",
    "delta_0inf": "delta_pm1",
}

# Retained W-side exact finite action.
assert gauge["audited_input"]["residues_decimal"] == [73, 97, 235]
assert gauge["mod2_W_action"]["line_labels"] == {
    "L1": [1, 0], "L2": [0, 1], "L3": [1, 1]
}
assert gauge["mod2_W_action"]["b3_line_permutation"] == "L1->L3->L2->L1"
assert gauge["mod2_W_action"]["b4_line_permutation"] == "L1 fixed; L2<->L3"
assert gauge["firewalls"]["absolute_delta0inf_retained_line_identified"] is False

# Exact finite ambiguity: without a common source anchor all 3! bijections survive.
source = ["delta_pm1", "delta_pmi", "delta_0inf"]
target = ["L1", "L2", "L3"]
bijections = [dict(zip(source, p)) for p in itertools.permutations(target)]
assert len(bijections) == 6
assert sorted({m["delta_0inf"] for m in bijections}) == ["L1", "L2", "L3"]

# Conditional diagnostic only: if FSM S were source-bound to principal b4,
# equivariance would leave exactly two mappings. This is NOT promoted to credit.
abstract_S = delta_action
target_b4 = {"L1": "L1", "L2": "L3", "L3": "L2"}
compatible = []
for m in bijections:
    if all(m[abstract_S[x]] == target_b4[m[x]] for x in source):
        compatible.append(m)
assert len(compatible) == 2
assert all(m["delta_pmi"] == "L1" for m in compatible)
assert sorted(m["delta_0inf"] for m in compatible) == ["L2", "L3"]

# Arsenal firewall: finite action matching is not a semantic adapter.
formal = (ROOT / locks["formal_finite_action_router"]["path"]).read_text(encoding="utf-8")
assert "require a common/source-derived semantic anchor before adapter credit" in formal
assert "gauge representative => canonical marking" in formal
provisional = (ROOT / locks["provisional_equivariant_reconstruction"]["path"]).read_text(encoding="utf-8")
assert "semantic/geometric identification merely from reconstructed algebra" in provisional

decision = cert["decision"]
assert decision["absolute_delta0inf_retained_W_line_identified"] is False
assert decision["q602_residue_specific_commutator_obtained"] is False
assert decision["Q602_excluded"] is False
assert decision["O210_excluded"] is False
assert cert["firewalls"]["matching_transposition_cycle_type_promoted_to_generator_identification"] is False

print("POST1648_DELTA0INF_RETAINED_W_ABSOLUTE_MARKING_LOCALIZATION_COMPLETE")
print(f"certificate_canonical={EXPECTED_CERT}")
print("delta_0inf=chi_u=Z3=b3=retained_boundary_labels_41_42_43_44")
print("fsm_S_abstract_W_action=delta_pm1<->delta_0inf;delta_pmi_fixed")
print("unanchored_source_target_bijections=6")
print("conditional_S_to_b4_bijections=2_NOT_CREDIT")
print("absolute_delta0inf_retained_W_line_identified=false")
print("survivors=73,97,235 Q602_excluded=false O210_excluded=false")
