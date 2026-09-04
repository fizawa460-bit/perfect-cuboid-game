#!/usr/bin/env python3
"""Certify Stage32 #1570 V2 blow-down Route C hostile-audit repair."""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT = HERE / "post1566-orbit-sum-commutator-batch.json"
SOURCE_NOTE = HERE / "post1566-orbit-sum-commutator-batch-source-note.md"
DIAGNOSTIC = HERE / "diagnose_stage32_post1566_orbit_sum_commutator.py"

EXPECTED_CERT_CANONICAL = "a898c9ad478ea4724de72ec862c048e90ce809edda16c8a81b082f7e6d7e1fea"
EXPECTED_SOURCE_NOTE_BLOB = "d92921c9008cface4f7c97b1da53c03e2b53fe90"
EXPECTED_DIAGNOSTIC_BLOB = "53e9f81813af13637ce62d4bd8770b81b4b23fb2"
EXPECTED_H_WORDS = {"1", "g7*g8", "g7*g9", "g8*g9"}

JSON_LOCKS = {
    "stages/stage32/residual-32-01-production/post1563-ambient-symmetry-exhaustion-batch.json": (
        "8c626d806c94b32f0930df876ad80fa937a98f6b",
        "9dbf0bcb144824a14497b663da2200f94d7250bfc755a37d1d65ca0b565fbb2e",
    ),
    "stages/stage32/32-21/post1473-v6-witness-body-recovered.json": (
        "dae90ed19395355bebeebe2a6aa6bb1c6e53c244",
        "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8",
    ),
    "stages/stage32/residual-32-01-production/post1490-o210-q4-equivariant-beauville-deck-cross-exclusion.json": (
        "9cd6d7122b8a3149b8ab79396946d72b986649df",
        "8c32735092671d725034de8d14d09c09ac275517fa5f0e225791d2fc53eb5bf3",
    ),
    "stages/stage32/residual-32-01-production/post1490-o210-q4-bolza-x-relative-h-marked-node-action.json": (
        "d1437ae97e5d10d66e2b12ca5a95b2e4d78672cc",
        "d03cfe8c77614943e8d4ab190c046b801bb90aa18f5bb648973bda0a5300c269",
    ),
    "stages/stage32/residual-32-01-production/post1484-o210-q4-common-double-cover-cartesian-identity.json": (
        "def8b60b726c02aa7ee97c0cc25b34f43525ec34",
        "eb31183bf519fec4ad5bb2d0799b3f0a64b7af893308e09ce0c33119b63440a1",
    ),
    "stages/stage32/residual-32-01-production/post1532-q602-single-b3-commutator.json": (
        "8699cdf52bff82304485a0544131e461b78c1fa6",
        "a374defb3a888c131ce92db9416702f34a03eb780b76d1dd6c26ab019f3c5064",
    ),
}

BLOB_LOCKS = {
    "stages/stage33/33-07/certify_two_coordinate_swap_picard_rows.py":
        "296e2005f822ae89c1aa085161553fe9ef76d077",
    "stages/stage32/residual-32-01-production/post1490-o210-q4-equivariant-beauville-deck-cross-exclusion-source-note.md":
        "a8fe5ea63e1b04ef9c580080410ac683d8b41c7e",
    "stages/stage32/residual-32-01-production/post1500-hostile-audit-rosati-trace-repair-source-note.md":
        "b0ea281eae453929c292059a919bc1f68b3080b3",
    "stages/stage32/residual-32-01-production/post1555-b3-full-g-box-quotient-normalizer-source-note.md":
        "88f5a34e05962b61f8079c147c5adc5a79ab6d2b",
}


def blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def canonical_sha256(obj: dict) -> str:
    core = dict(obj)
    claimed = core.pop("canonical_sha256_without_this_field")
    got = hashlib.sha256(json.dumps(core, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    assert claimed == got, (claimed, got)
    return got


def run_diagnostic() -> dict:
    raw = subprocess.check_output([sys.executable, str(DIAGNOSTIC)], cwd=ROOT, text=True)
    return json.loads(raw)


def main() -> None:
    cert = json.loads(CERT.read_text())
    assert cert["schema"] == "STAGE32_POST1566_ORBIT_SUM_CORRESPONDENCE_COMMUTATOR_BATCH_V2_BLOWDOWN_AUDIT_REPAIR"

    expected_base = os.environ.get("STAGE32_EXPECTED_BASE_SHA")
    assert expected_base, "STAGE32_EXPECTED_BASE_SHA is required for freshness fail-close"
    assert cert["base_main_sha"] == expected_base, (
        f"certificate base_main_sha {cert['base_main_sha']} != authoritative base {expected_base}"
    )
    assert canonical_sha256(cert) == EXPECTED_CERT_CANONICAL
    assert blob_sha1(SOURCE_NOTE) == EXPECTED_SOURCE_NOTE_BLOB
    assert blob_sha1(DIAGNOSTIC) == EXPECTED_DIAGNOSTIC_BLOB

    for rel, (expected_blob, expected_canonical) in JSON_LOCKS.items():
        p = ROOT / rel
        assert blob_sha1(p) == expected_blob, rel
        assert canonical_sha256(json.loads(p.read_text())) == expected_canonical, rel
    for rel, expected_blob in BLOB_LOCKS.items():
        assert blob_sha1(ROOT / rel) == expected_blob, rel

    # Exact source-bound facts needed by the repaired exceptional quotient.
    node = json.loads((HERE / "post1490-o210-q4-bolza-x-relative-h-marked-node-action.json").read_text())
    assert node["marked_node_action"]["exceptional_labels"] == [93, 140]

    old_note = (HERE / "post1490-o210-q4-equivariant-beauville-deck-cross-exclusion-source-note.md").read_text()
    assert "same square remains equivariant after blowing up the 48 distinguished X points" in old_note
    assert "Dtilde = pi_tilde^* C" in old_note
    assert "D . t(D) = Dtilde . t(Dtilde) + sum_j m_j m_{t(j)}" in old_note

    repaired_note = SOURCE_NOTE.read_text()
    assert "That bridge is withdrawn" in repaired_note
    assert "exceptional multiplicity vector" in repaired_note
    assert "N^1(Btilde)_Q / <E_93,...,E_140>_Q" in repaired_note
    assert "quotient both numerical Neron-Severi spaces by their exceptional spans" in repaired_note

    # Recompute both resolved and blow-down stabilizers instead of trusting copied data.
    diag = run_diagnostic()
    assert diag["schema"] == "STAGE32_POST1566_ORBIT_SUM_COMMUTATOR_DIAGNOSTIC_V2_BLOWDOWN"
    assert diag["retained_stoll_group_order"] == 1536
    assert diag["h_deck_group_order"] == 4
    assert diag["resolved_h_orbit_sum_stabilizer_count"] == 4
    assert diag["resolved_h_orbit_sum_stabilizer_outside_h_count"] == 0
    assert {row["word"] for row in diag["resolved_h_orbit_sum_stabilizer_elements"]} == EXPECTED_H_WORDS
    assert all(row["is_H_deck_element"] for row in diag["resolved_h_orbit_sum_stabilizer_elements"])
    assert diag["exceptional_labels_1based"] == [93, 140]
    assert diag["exceptional_curve_count"] == 48
    assert diag["exceptional_span_rank_over_Q"] == 48
    assert diag["blowdown_n1_quotient_rank"] == 16
    assert diag["blowdown_h_orbit_sum_stabilizer_count"] == 4
    assert diag["blowdown_h_orbit_sum_stabilizer_outside_h_count"] == 0
    assert {row["word"] for row in diag["blowdown_h_orbit_sum_stabilizer_elements"]} == EXPECTED_H_WORDS
    assert all(row["is_H_deck_element"] for row in diag["blowdown_h_orbit_sum_stabilizer_elements"])
    assert diag["blowdown_stabilizer_equals_H"] is True
    assert diag["beta_B_in_full_stoll"] is True
    assert diag["beta_B_in_H"] is False
    assert diag["beta_B_fixes_resolved_h_orbit_sum"] is False
    assert diag["beta_B_blowdown_noninvariance_proved"] is True
    assert diag["q602_residues"] == [73, 97, 235]
    assert diag["all_q602_residues_noncommuting_mod2"] is True

    fr = cert["finite_result"]
    for key in (
        "retained_stoll_group_order", "h_deck_group_order",
        "resolved_h_orbit_sum_stabilizer_count",
        "resolved_h_orbit_sum_stabilizer_outside_h_count",
        "exceptional_curve_count", "exceptional_span_rank_over_Q",
        "blowdown_n1_quotient_rank", "blowdown_h_orbit_sum_stabilizer_count",
        "blowdown_h_orbit_sum_stabilizer_outside_h_count",
    ):
        assert fr[key] == diag[key], key
    assert set(fr["resolved_h_orbit_sum_stabilizer_words"]) == EXPECTED_H_WORDS
    assert set(fr["blowdown_h_orbit_sum_stabilizer_words"]) == EXPECTED_H_WORDS
    assert fr["exceptional_labels_1based"] == [93, 140]
    assert fr["blowdown_stabilizer_exactly_H"] is True
    assert fr["beta_B_in_full_stoll"] is True
    assert fr["beta_B_in_H"] is False
    assert fr["beta_B_blowdown_h_orbit_sum_noninvariance_proved"] is True
    assert fr["q602_residues"] == [73, 97, 235]
    assert fr["all_q602_residues_noncommuting_mod2"] is True

    # Source-bound degree-two pullback used after the blow-down quotient.
    cover = json.loads((HERE / "post1484-o210-q4-common-double-cover-cartesian-identity.json").read_text())
    square = cover["group_quotient_square"]
    assert square["H"].endswith("normal index 2")
    assert "degree-two pullback" in square["generic_fiber_argument"]
    assert "generic degree two extension" in square["normalization_statement"]

    post1566 = json.loads((HERE / "post1563-ambient-symmetry-exhaustion-batch.json").read_text())
    assert post1566["decision"]["retained_stoll_full_aut_equality_proved"] is True
    assert post1566["routes"]["C_principal_b3_membership"]["beta_B_in_retained_stoll_group"] is True
    assert post1566["routes"]["C_principal_b3_membership"]["beta_B_in_H"] is False

    h_adapter = json.loads((HERE / "post1490-o210-q4-equivariant-beauville-deck-cross-exclusion.json").read_text())
    assert h_adapter["equivariant_adapter"]["modular_to_stoll"] == {
        "u": "g7*g9", "uv": "g8*g9", "v": "g7*g8"
    }

    post1532 = json.loads((HERE / "post1532-q602-single-b3-commutator.json").read_text())
    assert post1532["audited_q602_residues"] == [73, 97, 235]
    assert post1532["finite_mod2_check"]["all_audited_q602_residues_fail_b3_commutation"] is True

    routes = cert["routes"]
    assert routes["A_current_main_orbit_sum"]["historical_PR1547_used_as_authority"] is False
    b = routes["B_post1566_membership"]
    assert b["retained_stoll_equals_full_Aut_B"] is True
    assert b["beta_B_in_retained_stoll"] is True
    assert b["beta_B_outside_H"] is True

    c = routes["C_cover_transport_audit_repair"]
    assert c["result"] == "PASS_EXACT_BLOWDOWN_NUMERICAL_GAMMA_NONINVARIANCE_CONDITIONAL"
    assert c["strict_transform_bridge_used"] is False
    assert c["exceptional_multiplicity_invariance_assumed"] is False
    assert c["blowdown_n1_route_used"] is True
    assert c["exceptional_labels_1based"] == [93, 140]
    assert c["exceptional_span_rank_over_Q"] == 48
    assert c["blowdown_n1_quotient_rank"] == 16
    assert c["blowdown_stabilizer_exactly_H"] is True
    assert c["beta_B_blowdown_S_B_noninvariance_proved"] is True
    assert c["pi_generic_degree"] == 2
    assert c["pi_numerical_pullback_injective_over_Q"] is True
    assert c["pi_projection_formula"] == "pi_*pi^*=2*id"
    assert c["q_pullback_identity"] == "q^*Gamma=D+uD+vD+uvD"
    assert c["blowdown_pullback_identity"] == "[q^*Gamma]=pi^*[S_B] in N^1(X)_Q"
    assert c["pi_beta_equivariant"] is True
    assert c["q_beta_equivariant"] is True
    assert c["Gamma_b3_diagonal_numerical_invariant"] is False
    assert c["conditional_on_exact_carrier_correspondence_existence"] is True

    d = routes["D_corr_to_endomorphism"]
    assert d["Corr_to_EndJ_isomorphism_source_locked"] is True
    assert d["Gamma_bidegree"] == [105, 81]
    assert d["difference_bidegree"] == [0, 0]
    assert d["nonzero_NS_difference_survives_fiber_quotient"] is True
    assert d["actual_T_b3_noncommutation_proved"] is True
    assert d["conditional_on_exact_carrier_correspondence_existence"] is True

    e = routes["E_valence_scalarity"]
    assert e["valence_implies_scalar_T_minus_nu"] is True
    assert e["scalar_T_would_commute_with_b3"] is True
    assert e["valence_refuted"] is True
    assert e["scalarity_refuted"] is True
    assert e["post1522_valence_route_promoted_to_Q602_exclusion"] is False

    f = routes["F_q602_firewall"]
    assert f["q602_residues"] == [73, 97, 235]
    assert f["all_three_fail_b3_commutation_mod2"] is True
    assert f["noncommutation_excludes_Q602"] is False
    assert f["O210_excluded"] is False

    ext = cert["source_locks"]["external_dolgachev_zarhin"]
    assert ext["title"] == "Endomorphisms of Complex Abelian Varieties"
    assert ext["authors"] == ["Igor Dolgachev", "Yuri G. Zarhin"]
    assert ext["date"] == "2025-04-08"
    assert ext["locator"].startswith("Chapter 10 §10.1")
    assert "Corr(C)=NS(CxC)/(two fiber classes) maps isomorphically to End(J(C))" in ext["exact_used_facts"]
    assert "valence nu is equivalent to induced Jacobian endomorphism [-nu]" in ext["exact_used_facts"]

    cond = cert["conditionality"]
    assert cond["exact_carrier_existence_assumed_for_correspondence_consequences"] is True
    assert cond["carrier_existence_proved"] is False
    assert cond["carrier_nonexistence_proved"] is False
    assert cond["Gamma_exists_unconditionally_proved"] is False

    dec = cert["decision"]
    assert dec["result"] == "PASS_EXACT_BLOWDOWN_ORBIT_SUM_CORRESPONDENCE_NONINVARIANCE_AND_B3_NONCOMMUTATION"
    assert dec["resolved_h_orbit_sum_stabilizer_exactly_H"] is True
    assert dec["blowdown_h_orbit_sum_stabilizer_exactly_H"] is True
    assert dec["beta_B_blowdown_h_orbit_sum_noninvariance_proved"] is True
    assert dec["correspondence_numerical_noninvariance_proved"] is True
    assert dec["actual_T_b3_noncommutation_proved"] is True
    assert dec["actual_T_b3_commutation_proved"] is False
    assert dec["valence_refuted"] is True and dec["scalarity_refuted"] is True
    assert dec["Q602_excluded"] is False
    assert dec["O210_excluded"] is False
    assert dec["O212_plus_advance_allowed"] is False
    assert dec["controller_change_authorized"] is False

    fw = cert["firewalls"]
    assert fw["strict_transform_bridge_reused"] is False
    assert fw["exceptional_multiplicity_invariance_assumed"] is False
    assert fw["historical_PR1547_promoted_to_authority"] is False
    assert fw["noncommutation_promoted_to_Q602_exclusion"] is False
    assert fw["correspondence_noninvariance_promoted_to_carrier_nonexistence"] is False
    assert fw["conditional_correspondence_claim_promoted_to_unconditional_existence"] is False
    assert fw["Q602_excluded"] is False and fw["O210_excluded"] is False
    assert fw["O212_plus_advance_allowed"] is False
    for key in ("effectivity_credit", "full178_closed", "receiver_credit", "route_credit", "theorem_credit", "endpoint_credit", "perfect_cuboid_credit"):
        assert fw[key] is False, key

    lane = cert["lane_closure"]
    assert lane["ambient_symmetry_lane_already_closed_by_1566"] is True
    assert lane["direct_principal_b3_Gamma_invariance_lane_closed_negative"] is True
    assert lane["independent_valence_or_scalarity_lane_closed_negative_for_fixed_target"] is True

    print(json.dumps({
        "success": True,
        "schema": cert["schema"],
        "canonical_sha256": EXPECTED_CERT_CANONICAL,
        "base_main_sha": cert["base_main_sha"],
        "resolved_stabilizer_equals_H": True,
        "exceptional_span_rank_over_Q": 48,
        "blowdown_n1_quotient_rank": 16,
        "blowdown_stabilizer_equals_H": True,
        "strict_transform_bridge_used": False,
        "conditional_T_b3_noncommutation": True,
        "valence_refuted": True,
        "Q602_excluded": False,
        "O210_excluded": False,
        "result": dec["result"],
    }, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
