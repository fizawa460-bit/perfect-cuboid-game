#!/usr/bin/env python3
"""Certify Stage32 #1570 V2 blow-down Route C hostile-audit repair."""
from __future__ import annotations

import hashlib, json, os, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT = HERE / "post1566-orbit-sum-commutator-batch.json"
NOTE = HERE / "post1566-orbit-sum-commutator-batch-source-note.md"
DIAG = HERE / "diagnose_stage32_post1566_orbit_sum_commutator.py"

CERT_CANON = "d96ae71a5a863b66160d510ec26c913aeddec8b3f9aa8709305114aecfe2ee9b"
NOTE_BLOB = "d92921c9008cface4f7c97b1da53c03e2b53fe90"
DIAG_BLOB = "53e9f81813af13637ce62d4bd8770b81b4b23fb2"
HWORDS = {"1", "g7*g8", "g7*g9", "g8*g9"}

JSON_LOCKS = {
    "post1563-ambient-symmetry-exhaustion-batch.json": ("8c626d806c94b32f0930df876ad80fa937a98f6b", "9dbf0bcb144824a14497b663da2200f94d7250bfc755a37d1d65ca0b565fbb2e"),
    "post1490-o210-q4-equivariant-beauville-deck-cross-exclusion.json": ("9cd6d7122b8a3149b8ab79396946d72b986649df", "8c32735092671d725034de8d14d09c09ac275517fa5f0e225791d2fc53eb5bf3"),
    "post1490-o210-q4-bolza-x-relative-h-marked-node-action.json": ("d1437ae97e5d10d66e2b12ca5a95b2e4d78672cc", "d03cfe8c77614943e8d4ab190c046b801bb90aa18f5bb648973bda0a5300c269"),
    "post1484-o210-q4-common-double-cover-cartesian-identity.json": ("def8b60b726c02aa7ee97c0cc25b34f43525ec34", "eb31183bf519fec4ad5bb2d0799b3f0a64b7af893308e09ce0c33119b63440a1"),
    "post1532-q602-single-b3-commutator.json": ("8699cdf52bff82304485a0544131e461b78c1fa6", "a374defb3a888c131ce92db9416702f34a03eb780b76d1dd6c26ab019f3c5064"),
}
WITNESS = ROOT / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json"
WITNESS_BLOB = "dae90ed19395355bebeebe2a6aa6bb1c6e53c244"
WITNESS_CANON = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
HELPER = ROOT / "stages/stage33/33-07/certify_two_coordinate_swap_picard_rows.py"
HELPER_BLOB = "296e2005f822ae89c1aa085161553fe9ef76d077"
OLD_NOTE = HERE / "post1490-o210-q4-equivariant-beauville-deck-cross-exclusion-source-note.md"
OLD_NOTE_BLOB = "a8fe5ea63e1b04ef9c580080410ac683d8b41c7e"


def blob(path: Path) -> str:
    b = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(b)).encode() + b"\0" + b).hexdigest()


def canon(obj: dict) -> str:
    core = dict(obj)
    claimed = core.pop("canonical_sha256_without_this_field")
    got = hashlib.sha256(json.dumps(core, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert claimed == got, (claimed, got)
    return got


def main() -> None:
    cert = json.loads(CERT.read_text())
    assert cert["schema"] == "STAGE32_POST1566_ORBIT_SUM_CORRESPONDENCE_COMMUTATOR_BATCH_V2_BLOWDOWN_AUDIT_REPAIR"
    base = os.environ.get("STAGE32_EXPECTED_BASE_SHA")
    assert base and cert["base_main_sha"] == base, (cert["base_main_sha"], base)
    assert canon(cert) == CERT_CANON
    assert blob(NOTE) == NOTE_BLOB
    assert blob(DIAG) == DIAG_BLOB
    assert blob(WITNESS) == WITNESS_BLOB and canon(json.loads(WITNESS.read_text())) == WITNESS_CANON
    assert blob(HELPER) == HELPER_BLOB
    assert blob(OLD_NOTE) == OLD_NOTE_BLOB

    for name, (want_blob, want_canon) in JSON_LOCKS.items():
        p = HERE / name
        assert blob(p) == want_blob, name
        assert canon(json.loads(p.read_text())) == want_canon, name

    node = json.loads((HERE / "post1490-o210-q4-bolza-x-relative-h-marked-node-action.json").read_text())
    assert node["marked_node_action"]["exceptional_labels"] == [93, 140]
    old = OLD_NOTE.read_text()
    assert "same square remains equivariant after blowing up the 48 distinguished X points" in old
    assert "Dtilde = pi_tilde^* C" in old
    assert "D . t(D) = Dtilde . t(Dtilde) + sum_j m_j m_{t(j)}" in old
    note = NOTE.read_text()
    assert "That bridge is withdrawn" in note
    assert "quotient both numerical Neron-Severi spaces by their exceptional spans" in note

    diag = json.loads(subprocess.check_output([sys.executable, str(DIAG)], cwd=ROOT, text=True))
    assert diag["schema"] == "STAGE32_POST1566_ORBIT_SUM_COMMUTATOR_DIAGNOSTIC_V2_BLOWDOWN"
    assert diag["retained_stoll_group_order"] == 1536 and diag["h_deck_group_order"] == 4
    assert diag["resolved_h_orbit_sum_stabilizer_count"] == 4
    assert diag["resolved_h_orbit_sum_stabilizer_outside_h_count"] == 0
    assert {x["word"] for x in diag["resolved_h_orbit_sum_stabilizer_elements"]} == HWORDS
    assert diag["exceptional_labels_1based"] == [93, 140]
    assert diag["exceptional_curve_count"] == 48
    assert diag["exceptional_span_rank_over_Q"] == 48
    assert diag["blowdown_n1_quotient_rank"] == 16
    assert diag["blowdown_h_orbit_sum_stabilizer_count"] == 4
    assert diag["blowdown_h_orbit_sum_stabilizer_outside_h_count"] == 0
    assert {x["word"] for x in diag["blowdown_h_orbit_sum_stabilizer_elements"]} == HWORDS
    assert all(x["is_H_deck_element"] for x in diag["blowdown_h_orbit_sum_stabilizer_elements"])
    assert diag["blowdown_stabilizer_equals_H"] is True
    assert diag["beta_B_in_full_stoll"] is True and diag["beta_B_in_H"] is False
    assert diag["beta_B_blowdown_noninvariance_proved"] is True
    assert diag["q602_residues"] == [73, 97, 235]
    assert diag["all_q602_residues_noncommuting_mod2"] is True

    fr = cert["finite_result"]
    assert fr["exceptional_curve_count"] == 48
    assert fr["exceptional_span_rank_over_Q"] == 48
    assert fr["blowdown_n1_quotient_rank"] == 16
    assert fr["blowdown_h_orbit_sum_stabilizer_count"] == 4
    assert fr["blowdown_h_orbit_sum_stabilizer_outside_h_count"] == 0
    assert set(fr["blowdown_h_orbit_sum_stabilizer_words"]) == HWORDS
    assert fr["blowdown_stabilizer_exactly_H"] is True
    assert fr["beta_B_blowdown_h_orbit_sum_noninvariance_proved"] is True

    cover = json.loads((HERE / "post1484-o210-q4-common-double-cover-cartesian-identity.json").read_text())
    sq = cover["group_quotient_square"]
    assert sq["H"].endswith("normal index 2")
    assert "degree-two pullback" in sq["generic_fiber_argument"]
    assert "generic degree two extension" in sq["normalization_statement"]

    post1566 = json.loads((HERE / "post1563-ambient-symmetry-exhaustion-batch.json").read_text())
    assert post1566["decision"]["retained_stoll_full_aut_equality_proved"] is True
    assert post1566["routes"]["C_principal_b3_membership"]["beta_B_in_retained_stoll_group"] is True
    assert post1566["routes"]["C_principal_b3_membership"]["beta_B_in_H"] is False

    c = cert["routes"]["C_cover_transport_audit_repair"]
    assert c["strict_transform_bridge_used"] is False
    assert c["exceptional_multiplicity_invariance_assumed"] is False
    assert c["blowdown_n1_route_used"] is True
    assert c["exceptional_span_rank_over_Q"] == 48 and c["blowdown_n1_quotient_rank"] == 16
    assert c["blowdown_stabilizer_exactly_H"] is True
    assert c["beta_B_blowdown_S_B_noninvariance_proved"] is True
    assert c["pi_generic_degree"] == 2 and c["pi_numerical_pullback_injective_over_Q"] is True
    assert c["pi_projection_formula"] == "pi_*pi^*=2*id"
    assert c["q_pullback_identity"] == "q^*Gamma=D+uD+vD+uvD"
    assert c["blowdown_pullback_identity"] == "[q^*Gamma]=pi^*[S_B] in N^1(X)_Q"
    assert c["pi_beta_equivariant"] is True and c["q_beta_equivariant"] is True
    assert c["Gamma_b3_diagonal_numerical_invariant"] is False
    assert c["conditional_on_exact_carrier_correspondence_existence"] is True

    d = cert["routes"]["D_corr_to_endomorphism"]
    assert d["Corr_to_EndJ_isomorphism_source_locked"] is True
    assert d["Gamma_bidegree"] == [105, 81] and d["difference_bidegree"] == [0, 0]
    assert d["nonzero_NS_difference_survives_fiber_quotient"] is True
    assert d["actual_T_b3_noncommutation_proved"] is True

    e = cert["routes"]["E_valence_scalarity"]
    assert e["valence_refuted"] is True and e["scalarity_refuted"] is True
    assert e["post1522_valence_route_promoted_to_Q602_exclusion"] is False
    f = cert["routes"]["F_q602_firewall"]
    assert f["q602_residues"] == [73, 97, 235]
    assert f["all_three_fail_b3_commutation_mod2"] is True
    assert f["noncommutation_excludes_Q602"] is False and f["O210_excluded"] is False

    dec = cert["decision"]
    assert dec["result"] == "PASS_EXACT_BLOWDOWN_ORBIT_SUM_CORRESPONDENCE_NONINVARIANCE_AND_B3_NONCOMMUTATION"
    assert dec["correspondence_numerical_noninvariance_proved"] is True
    assert dec["actual_T_b3_noncommutation_proved"] is True
    assert dec["Q602_excluded"] is False and dec["O210_excluded"] is False
    assert dec["O212_plus_advance_allowed"] is False and dec["controller_change_authorized"] is False

    fw = cert["firewalls"]
    assert fw["strict_transform_bridge_reused"] is False
    assert fw["exceptional_multiplicity_invariance_assumed"] is False
    assert fw["noncommutation_promoted_to_Q602_exclusion"] is False
    assert fw["Q602_excluded"] is False and fw["O210_excluded"] is False
    for k in ("effectivity_credit", "full178_closed", "receiver_credit", "route_credit", "theorem_credit", "endpoint_credit", "perfect_cuboid_credit"):
        assert fw[k] is False, k

    cond = cert["conditionality"]
    assert cond["exact_carrier_existence_assumed_for_correspondence_consequences"] is True
    assert cond["carrier_existence_proved"] is False and cond["carrier_nonexistence_proved"] is False
    assert cond["Gamma_exists_unconditionally_proved"] is False

    print(json.dumps({
        "success": True,
        "schema": cert["schema"],
        "canonical_sha256": CERT_CANON,
        "base_main_sha": cert["base_main_sha"],
        "exceptional_span_rank_over_Q": 48,
        "blowdown_n1_quotient_rank": 16,
        "blowdown_stabilizer_equals_H": True,
        "strict_transform_bridge_used": False,
        "conditional_T_b3_noncommutation": True,
        "Q602_excluded": False,
        "O210_excluded": False,
        "result": dec["result"],
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
