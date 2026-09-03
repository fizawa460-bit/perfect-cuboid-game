#!/usr/bin/env python3
import argparse
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]

def blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()

def canonical_sha256(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", required=True)
    args = ap.parse_args()
    cert = json.loads((ROOT / args.check).read_text())

    assert cert["schema"] == "STAGE32_POST1490_O210_Q4_BOLZA_RATIONAL_CHARACTER_ALGEBRA_INTEGRAL_INDEX_BOUNDARY_V1"
    assert canonical_sha256(cert) == cert["canonical_sha256_without_this_field"]

    prior_lock = cert["source_locks"]["delta_simplex"]
    prior = json.loads((ROOT / prior_lock["path"]).read_text())
    assert canonical_sha256(prior) == prior_lock["canonical_sha256"]
    hc = prior["hodge_corridor_collapse"]["simplex_reparameterization"]
    assert prior["x_side_exact_lock"]["delta_D"] == 2018
    assert hc["r_sum"] == 377
    assert hc["character_square_formula"] == "E_t^2=-8-16*r_t"

    note_lock = cert["source_locks"]["source_note"]
    note_path = ROOT / note_lock["path"]
    assert blob_sha1(note_path) == note_lock["blob_sha1"]
    note = note_path.read_text()
    for needle in [
        "End_Gamma(JC) tensor Q = M2(Q(sqrt(-2))) x Q(i)^3",
        "The last two statements are explicitly rational",
        "No integral congruence stronger than the already locked",
    ]:
        assert needle in note

    b = cert["source_locks"]["beauville_maximal_picard"]
    assert b["doi"] == "10.5802/jep.5"
    assert b["arxiv"] == "1310.3402v2"
    facts = b["exact_supported_facts"]
    assert "C is the modular curve X(8)." in facts
    assert "Gamma is isomorphic to (Z/2Z)^2 and acts freely on C." in facts
    assert any("three nontrivial one-dimensional representations" in x for x in facts)
    assert any("NS((C x C)/Gamma) tensor Q" in x for x in facts)
    assert "End_Gamma(JC) tensor Q = M2(Q(sqrt(-2))) x Q(i)^3." in facts

    fsm = cert["source_locks"]["freitag_salvati_manni_cover"]
    assert fsm["arxiv"] == "1303.6495"
    ff = fsm["exact_supported_facts"]
    assert any("(Z/2Z)^2" in x and "acts freely" in x for x in ff)
    assert any("diagonal action" in x for x in ff)
    assert any("48 exceptional" in x for x in ff)

    ra = cert["rational_character_adapter"]
    assert ra["nontrivial_character_count"] == 3
    assert ra["nontrivial_character_holomorphic_dimension_each"] == 1
    assert ra["nontrivial_character_rational_endomorphism_algebra_each"] == "Q(i)"
    assert ra["nontrivial_character_NS_rational_dimension_each"] == 2
    assert ra["scope"] == "RATIONAL_NERON_SEVERI_CHARACTER_ALGEBRA_ONLY"

    v = cert["exact_v220_inputs"]
    assert v["delta_D"] == 2018
    assert v["r_sum"] == 377
    assert v["character_square_formula"] == "E_t^2=-8-16*r_t"
    for r in range(378):
        sq = -8 - 16*r
        assert sq % 16 == 8
        assert sq % 8 == 0
        assert sq % 16 != 0
    assert v["character_square_mod16"] == 8
    assert v["character_square_divisible_by_8"] is True
    assert v["character_square_divisible_by_16"] is False
    count = math.comb(379, 2)
    assert count == 71631 == v["ordered_nonnegative_triple_count"]

    gap = cert["integral_index_boundary"]
    for key in [
        "integral_character_lattice_source_locked",
        "primitive_embedding_into_NS_X_source_locked",
        "integral_order_inside_Q_i_source_locked",
        "rosati_or_intersection_scale_source_locked",
        "deck_equivariant_integral_basis_source_locked",
        "can_infer_exact_Z_i_lattice",
        "can_infer_sum_of_two_squares_norm_at_exact_scale",
        "can_infer_square_divisibility_by_16_or_32",
    ]:
        assert gap[key] is False

    dec = cert["decision"]
    assert dec["O210_excluded"] is False
    assert dec["new_rational_X_side_character_structure_source_locked"] is True
    assert dec["new_integral_divisibility_constraint_obtained"] is False
    assert dec["simplex_reduced"] is False
    assert dec["ordered_simplex_count_before"] == count
    assert dec["ordered_simplex_count_after_rational_character_lock"] == count
    assert dec["next_exact_leaf"] == "O210_Q4_BOLZA_INTEGRAL_NS_CHARACTER_LATTICE_INDEX_OR_EXACT_DECK_ACTION_ADAPTER"

    fw = cert["firewalls"]
    assert fw["rational_NS_decomposition_promoted_to_integral_lattice"] is False
    assert fw["arbitrary_B_picard64_promoted_to_picX"] is False
    assert fw["effectivity_credit"] is False
    assert fw["full178_authorized"] is False
    assert fw["receiver_credit"] is False
    assert fw["theorem_credit"] is False
    assert fw["endpoint_credit"] is False

    print("PASS_RATIONAL_CHARACTER_ALGEBRA_INTEGRAL_INDEX_BOUNDARY")

if __name__ == "__main__":
    main()
