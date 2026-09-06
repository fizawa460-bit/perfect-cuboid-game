#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "post1648y-cecotti-kkk-literal-branch-anchor-subsumption.json"

LOCKS = {
    "post1648X": (
        HERE / "post1648x-florit-smith-richelot-e2-marking-nonadapter.json",
        "eacdd1f74d8d010136596c833c197f281e352890a3c0e768147046642dd62bf6",
        "74774adc45ff0d6010b0f1cd792706c7f5ca817c",
    ),
    "post1648N": (
        HERE / "post1648n-canonical-period-marked-ppav-torsor-obstruction.json",
        "060d940626cd59b00efb67db7f27914e6a440c92968600a3d82a208d5a5d76ba",
        "0ee05f679c7706113feed2c217e08a95b3bd6f06",
    ),
    "post1648U": (
        HERE / "post1648u-kkk-delta0inf-explicit-half-period-nonpruning.json",
        "eb0d69e1f219e6204399aeed2a0498bbefd13d2e6dc9a02f0927bb7eec73f281",
        "4151d5644b264f1ff1fd175f4fb1652354458d95",
    ),
    "post1648J": (
        HERE / "post1648j-cecotti-trace-orientation-correction.json",
        "3f6fd55ced259c6f28949df61865e22d43a669a50bdaf2adf5ddcd88411a48ec",
        "17641753c33ae46e9b7517dc85a915edd70d2057",
    ),
    "post1648S": (
        HERE / "post1648s-inner-conjugacy-invariant-nonselection-theorem.json",
        "b79aa40f805957b5e122aaff4791cab9b456409380d7f7d5214c7f3573cf3488",
        "a452fffad42516feaadf3ad44852bdc5c4f3090e",
    ),
}

EXPECTED_CERT_CANONICAL = "9cdab994c8dfa46a9f86825dc0590c08a42830d2e4fc6cc8b32ac18bfd33e1fd"
EXPECTED_NOTE_BLOB = "242e55462b6e63530374ae5b9966758c41c1b175"


def canonical_sha(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def load_locked(path: Path, canonical: str, blob: str) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    assert canonical_sha(obj) == canonical
    assert obj["canonical_sha256_without_this_field"] == canonical
    assert git_blob_sha(path) == blob
    return obj


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    assert canonical_sha(cert) == EXPECTED_CERT_CANONICAL
    assert cert["canonical_sha256_without_this_field"] == EXPECTED_CERT_CANONICAL

    loaded = {name: load_locked(*spec) for name, spec in LOCKS.items()}
    note = HERE / "post1648y-cecotti-kkk-literal-branch-anchor-subsumption-source-note.md"
    assert git_blob_sha(note) == EXPECTED_NOTE_BLOB

    n = loaded["post1648N"]
    u = loaded["post1648U"]
    j = loaded["post1648J"]
    s = loaded["post1648S"]

    assert n["source_marking"]["mu1_x_map"] == "x->i*x"
    assert n["exact_enumeration"]["principal_polarization_maps_found"] == 48
    assert n["exact_enumeration"]["distinct_target_mu1_images"] == 6
    assert n["exact_enumeration"]["isomorphisms_per_target_mu1_image"] == 8
    assert n["exact_enumeration"]["delta0inf_fixed_line_counts"] == {"L1": 16, "L2": 16, "L3": 16}

    assert u["external_source_lock"]["klein_kokotov_korotkin"]["exact_supported_facts"][1] == "mu1 acts by z->i*z and fixes the branch points 0 and infinity"
    assert u["kkk_mod2_derivation"]["delta_0inf_half_period_vector_mod2"] == [0, 0, 1, 1]

    cec = j["external_source_lock"]["cecotti"]["exact_supported_facts"]
    assert "the source does not explicitly identify B.7 with S or B.8 with T or T^-1" in cec
    assert j["decision"]["absolute_delta0inf_retained_W_line_identified"] is False

    theorem = s["anti_loop_theorem"]
    assert s["exact_group_action"]["pair_set_is_one_simultaneous_inner_conjugacy_orbit"] is True
    assert s["exact_group_action"]["B9_fixed_line_counts_over_pair_orbit"] == {"L1": 8, "L2": 8, "L3": 8}
    assert "orders of A,B or words in A,B" in theorem["examples_closed_as_selectors"]

    test = cert["literal_common_anchor_test"]
    assert test["literal_base_map_equal"] is True
    assert test["new_source_branch_label_obtained"] is False
    assert test["cecotti_elementwise_curve_to_retained_lattice_word_map_obtained"] is False
    assert test["order_sequence_2_6_8_promoted_to_S_T_ST_identification"] is False

    sub = cert["subsumption_audit"]
    assert sub["B9_mu1_literal_curve_anchor"] == "SUBSUMED_BY_POST1648N_AND_POST1648U"
    assert sub["B7_B8_literal_differential_pair"] == "SUBSUMED_BY_POST1648J"
    assert sub["order_trace_relation_word_filters"] == "SUBSUMED_BY_POST1648S"
    assert sub["new_constraint_on_48_isomorphism_torsor_added"] is False
    assert sub["remaining_isomorphisms_after_this_leaf"] == 48

    decision = cert["decision"]
    assert decision["cecotti_kkk_literal_branch_recombination_is_new_route"] is False
    assert decision["cecotti_kkk_literal_branch_recombination_prunes"] is False
    assert decision["absolute_delta0inf_retained_W_line_identified"] is False
    assert decision["survivors_current_credit"] == [73, 97, 235]
    assert decision["Q602_excluded"] is False
    assert decision["O210_excluded"] is False
    assert decision["O212_plus_advance_allowed"] is False

    fw = cert["firewalls"]
    assert not any([
        fw["scratch_result_promoted_to_MAIN_authority"],
        fw["scratch_result_promoted_to_current_credit"],
        fw["same_curve_map_promoted_to_target_lattice_element"],
        fw["order_listing_promoted_to_elementwise_generator_table"],
        fw["co_location_promoted_to_semantic_adapter"],
        fw["Q602_excluded"],
        fw["O210_excluded"],
        fw["receiver_credit"],
        fw["route_credit"],
        fw["theorem_credit"],
        fw["endpoint_credit"],
        fw["perfect_cuboid_credit"],
    ])

    print("POST1648Y_CECOTTI_KKK_LITERAL_BRANCH_ANCHOR_SUBSUMPTION_COMPLETE")
    print("B9_mu1=subsumed_N_U B7_B8=subsumed_J inner_invariants=subsumed_S")
    print("new_constraint_on_48_torsor=false remaining_isomorphisms=48")
    print("absolute_delta0inf_retained_W_line_identified=false")
    print("survivors=73,97,235 Q602_excluded=false O210_excluded=false")


if __name__ == "__main__":
    main()
