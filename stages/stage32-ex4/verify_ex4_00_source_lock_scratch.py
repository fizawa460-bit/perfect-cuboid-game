#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ARTIFACT = HERE / "ex4-00-source-lock-typed-marking-graph-scratch.json"


def load(rel: str):
    return json.loads((ROOT / rel).read_text())


def csha(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def blob_sha(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def main() -> None:
    a = json.loads(ARTIFACT.read_text())
    assert a["schema"] == "STAGE32EX4_EX4_00_SOURCE_LOCK_TYPED_MARKING_GRAPH_SCRATCH_V1"
    assert a["status"] == "SCRATCH_REPLAYABLE_EX4_00_SOURCE_LOCK_COMPLETE_NOT_RETAINED_AUTHORITY"
    stripped = dict(a)
    stored = stripped.pop("canonical_sha256_without_this_field")
    assert csha(stripped) == stored

    for lock in a["source_package"]:
        path = ROOT / lock["path"]
        data = path.read_bytes()
        assert blob_sha(data) == lock["blob_sha1"], lock["role"]
        if "canonical_sha256" in lock:
            obj = json.loads(data)
            want = lock["canonical_sha256"]
            assert obj["canonical_sha256_without_this_field"] == want, lock["role"]
            raw = dict(obj)
            raw.pop("canonical_sha256_without_this_field")
            assert csha(raw) == want, lock["role"]

    hdeck = load("stages/stage32/residual-32-01-production/post1623-hperp-v6-hdeck-character-preflight.json")
    bind = hdeck["abstract_character_to_w_binding"]
    assert bind["chi_u_canonical_pair"] == "Z3"
    assert bind["Z3_pair_ids"] == [2, 4]
    assert bind["Z3_pair_values"] == ["0", "infinity"]
    assert bind["abstract_class_name"] == "delta_0inf"
    assert bind["retained_F2_4_coordinate_line_identified"] is False
    bounded = hdeck["bounded_conclusion"]
    assert bounded["abstract_delta_0inf_direction_recovered"] is True
    assert bounded["absolute_delta0inf_retained_W_line_still_unidentified"] is True
    assert hdeck["fixed_target"]["surviving_residues_decimal"] == [73, 97, 235]

    retained = load("stages/stage32/residual-32-01-production/post1505-o210-q4-x8-v4-torsor-plane-retained-f2-4-adapter.json")
    r = retained["retained_F2_4_adapter"]
    assert r["ordered_basis"] == ["e1", "e2", "r*e1", "r*e2"]
    assert r["multiplication_by_r_mod2"] == [[0,0,0,0],[0,0,0,0],[1,0,0,0],[0,1,0,0]]
    assert r["W_basis_vectors"] == [[0,0,1,0],[0,0,0,1]]
    assert r["W_nonzero_vectors"] == [[0,0,1,0],[0,0,0,1],[0,0,1,1]]
    assert r["W_equals_kernel_r_mod2"] is True

    principal = load("stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-principal-rosati-lock.json")
    p = principal["principal_polarization"]
    assert p["riemann_form_basis"] == ["e1", "e2", "r*e1", "r*e2"]
    e = [[x & 1 for x in row] for row in p["riemann_form_matrix"]]
    assert e == [[0,1,0,1],[1,0,1,0],[0,1,0,0],[1,0,0,0]]
    assert p["principal"] is True

    trans = load("stages/stage32/residual-32-01-production/post1505-o210-q602-weierstrass-parity-transvection-refinement.json")
    assert trans["weierstrass_parity_action"]["branch_permutation"] == "(2 4)"
    assert trans["weierstrass_parity_action"]["transvection_direction_abstract"] == "delta_0inf=[P_0-P_infinity]"
    assert trans["weierstrass_parity_action"]["transvection_direction_in_W"] is True
    pred = trans["basis_independent_predicate"]
    assert pred["rank_T_minus_I"] == 1
    assert pred["individual_retained_W_line_identified"] is False
    filt = trans["retained_residue_filter"]
    residues = filt["surviving_residues_decimal"]
    lines = filt["image_lines_in_W"]
    assert residues == [73, 97, 235]
    assert lines == [[0,0,1,0],[0,0,0,1],[0,0,1,1]]
    exact = [(x["vector"], x["residue_decimal"]) for x in a["exact_line_to_residue_adapter"]["mapping"]]
    assert exact == list(zip(lines, residues))
    assert a["exact_line_to_residue_adapter"]["absolute_residue_selected"] is False

    gauge = load("stages/stage32/residual-32-01-production/post1505-o210-q602-marked-w-line-gauge-orbit.json")
    assert gauge["status"].startswith("PROVISIONAL_")
    assert gauge["mod2_W_action"]["generated_line_action_order"] == 6
    assert gauge["mod2_W_action"]["transitive_on_nonzero_W_lines"] is True
    assert gauge["firewalls"]["absolute_delta0inf_retained_line_identified"] is False

    cec = load("stages/stage32/residual-32-01-production/post1648j-cecotti-trace-orientation-correction.json")
    assert cec["status"] == "EXACT_TRACE_ORIENTATION_CORRECTION_PENDING_HOSTILE_AUDIT"
    consequence = cec["W_line_consequence"]
    assert consequence["all_plus_r_inner_conjugates"]["delta0inf_image_counts"] == {"L1":8,"L2":8,"L3":8}
    assert consequence["all_plus_r_inner_conjugates"]["distinct_W_line_bijections"] == 6
    assert consequence["literal_plus_r_conditional_delta0inf_residue_decimal"] == 97
    assert consequence["literal_plus_r_conditional_only_not_current_credit"] is True
    assert cec["decision"]["absolute_delta0inf_retained_W_line_identified"] is False

    decision = a["decision"]
    assert decision["result"] == "EX4_00_SOURCE_LOCK_AND_TYPED_MARKING_GRAPH_COMPLETE_ON_SCRATCH_BRANCH"
    assert decision["retained_claim_dag_sync_performed"] is False
    for key in ["absolute_delta0inf_retained_W_line_identified","absolute_Q602_residue_identified","Q602_excluded","O210_excluded","stage32_main_credit"]:
        assert decision[key] is False

    assert a["typed_objects"]["absolute_marking_adapter"]["status"] == "MISSING"
    assert any(x["status"] == "OPEN_LOAD_BEARING_ARROW" for x in a["typed_arrows"])
    assert all(v is False for v in a["firewalls"].values())

    print(json.dumps({
        "verdict":"PASS_STAGE32EX4_EX4_00_SCRATCH_SOURCE_LOCK",
        "line_to_residue":{"L1":73,"L2":97,"L3":235},
        "absolute_line_identified":False,
        "absolute_residue_identified":False,
        "claim_dag_sync_performed":False,
        "next_leaf":"EX4-01_MINIMAL_ABSOLUTE_DATUM_SPECIFICATION"
    }, sort_keys=True))


if __name__ == "__main__":
    main()
