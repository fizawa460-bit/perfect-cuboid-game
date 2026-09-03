#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def canonical_sha256(doc: dict) -> str:
    body = dict(doc)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load_json_lock(lock: dict) -> dict:
    path = ROOT / lock["path"]
    assert path.is_file(), path
    if "blob_sha1" in lock:
        assert blob_sha1(path) == lock["blob_sha1"], path
    doc = json.loads(path.read_text())
    if "canonical_sha256" in lock:
        assert canonical_sha256(doc) == lock["canonical_sha256"], path
    return doc


def odd_divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0 and d % 2 == 1]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", required=True)
    args = ap.parse_args()

    cert = json.loads((ROOT / args.check).read_text())
    assert cert["schema"] == "STAGE32_POST1500_HOSTILE_AUDIT_ROSATI_TRACE_REPAIR_V1"
    assert canonical_sha256(cert) == cert["canonical_sha256_without_this_field"]
    assert cert["canonical_sha256_without_this_field"] == "e28c7539e05b9c4836b9bc51c8f69316723eb8c368700a26706627045525fe07"
    locks = cert["source_locks"]

    note_path = ROOT / locks["repair_source_note"]["path"]
    assert blob_sha1(note_path) == locks["repair_source_note"]["blob_sha1"]
    note = note_path.read_text()
    for needle in [
        "bidegree does not determine self-intersection",
        "Gamma^2 = 3874+11932 = 15806",
        "sigma(Gamma)=2*105*81-15806=1204",
        "Q(T)=602",
        "a(301)=24*(1+7+43+301)=8448>0",
        "delta_Gamma=7984",
        "O210 is reopened",
    ]:
        assert needle in note, needle

    # The V224 claim is retained only as an explicitly superseded object.
    old = load_json_lock(locks["superseded_v224_certificate"])
    assert old["qprime4_all_overlap_argument"]["pair_map"]["image_self_intersection"] == 17010
    assert old["qprime4_all_overlap_argument"]["contradiction_gap"] == 1204
    assert old["decision"]["fixed_V6_all_integral_genus1_carriers_excluded"] is True
    assert cert["superseded_claims"]["v224_all_genus1_fixed_v6_exclusion"] is True
    assert cert["superseded_claims"]["post1490_o210_exclusion_reopened"] is True

    boundary = load_json_lock(locks["modular_factor_boundary"])
    tr = boundary["product_cover_degree_transport"]
    assert tr["qprime_1"]["possible"] is False
    assert tr["qprime_2"]["possible"] is False
    assert tr["qprime_4"]["projection_degrees"] == [105, 81]
    assert boundary["new_O_wall"]["provisional_O_min"] == 210

    self_adapter = load_json_lock(locks["beauville_self_adapter"])
    C2 = self_adapter["exact_v6_inputs"]["Btilde_class_self_intersection"]
    exceptional2 = self_adapter["exact_v6_inputs"]["exceptional_square_sum"]
    D2 = 2 * C2 + exceptional2
    assert (C2, exceptional2, D2) == (758, 2358, 3874)
    assert self_adapter["x_side_exact_lock"]["D_square"] == D2

    deck = load_json_lock(locks["equivariant_deck_cross"])
    crosses = [deck["exact_cross"][t]["D_dot_tD"] for t in ["u", "v", "uv"]]
    assert crosses == [3892, 4020, 4020]
    deck_sum = sum(crosses)
    assert deck_sum == deck["exact_cross"]["computed_D_translate_sum"] == 11932

    frontier = load_json_lock(locks["correspondence_rosati_frontier"])
    assert frontier["fixed_correspondence"]["maps"]["f1"]["degree"] == 105
    assert frontier["fixed_correspondence"]["maps"]["f2"]["degree"] == 81
    assert frontier["correspondence_endomorphism"]["schur_bound"] == "T^dagger*T <= 8505"

    d4 = load_json_lock(locks["d4d4_trace_reduction"])
    pm = d4["pair_map_birationality"]
    assert pm["finite_etale_degree"] == 4
    assert pm["deck_group"] == "(H x H)/H_diag ~= V4"
    assert pm["projection_degrees"] == [105, 81]
    assert pm["generic_pair_degree_allowed_by_deck_stabilizer"] == [1, 2, 4]
    assert pm["generic_pair_degree_divides_gcd"] == math.gcd(105, 81) == 3
    assert pm["generic_pair_degree"] == 1
    assert pm["pair_map_birational"] is True
    external = d4["source_locks"]["correspondence_intersection_external"]["exact_supported_fact"]
    assert "sigma(D)=2*d1*d2-D^2" in external
    assert d4["correspondence_trace"]["matrix_trace_relation"] == "Tr_Q(T^dagger*T)=2*Q(T)"
    assert d4["trace_lattice"]["isometry"] == "U^t*A*U = D4 direct-sum D4"

    # Correct the audited arithmetic without assuming zero Rosati component.
    gamma2 = D2 + deck_sum
    sigma = 2 * 105 * 81 - gamma2
    Q = sigma // 2
    assert gamma2 == 15806
    assert sigma == 1204 and sigma % 2 == 0
    assert Q == 602

    # For O=210, g(Y)=106 remains source-locked. Adjunction on C0 x C0
    # gives p_a(Gamma)=1+(Gamma^2+2*(105+81))/2.
    gY = 106
    pa_gamma = 1 + (gamma2 + 2 * (105 + 81)) // 2
    delta = pa_gamma - gY
    assert pa_gamma == 8090
    assert delta == 7984
    assert Q == 8586 - delta
    assert d4["correspondence_trace"]["exact_identity"] == "Q(T)=8586-delta"

    # Q=602 is inside the automatic operator corridor and is represented by
    # the retained D4 lattice; no full enumeration is needed.
    assert Q <= 8504 < d4["exact_preflight"]["old_operator_bound"] + 1
    assert "Q<=8504 is automatic" in d4["exact_preflight"]["automatic_implication"]
    m = Q // 2
    assert m == 301 and 301 == 7 * 43
    divs = odd_divisors(m)
    assert divs == [1, 7, 43, 301]
    shell_count = 24 * sum(divs)
    assert shell_count == 8448 > 0
    assert "a(m)=24*sum_{d|m,d odd} d" in d4["exact_preflight"]["d4_shell_formula"]

    wei = load_json_lock(locks["weierstrass_collision"])
    delta_min = wei["collision_optimization"]["exact_minimum_delta"]
    assert delta_min == 1924
    assert delta >= delta_min
    assert wei["decision"]["O210_excluded"] is False

    repaired = cert["corrected_rosati_arithmetic"]
    assert repaired["Gamma_square"] == gamma2
    assert repaired["sigma"] == sigma
    assert repaired["Q"] == Q
    assert repaired["Gamma_arithmetic_genus"] == pa_gamma
    assert repaired["Gamma_normalization_defect"] == delta

    bounded = cert["bounded_retained_rosati_search"]
    assert bounded["Q_represented"] is True
    assert bounded["D4_shell"]["one_D4_shell_count"] == shell_count
    assert bounded["weierstrass_bound_satisfied"] is True
    assert bounded["existing_assets_exclude_Q602"] is False

    dec = cert["decision"]
    assert dec["O186_closed_audited"] is True
    assert dec["O188_closed_audited"] is True
    assert dec["O210_reopened"] is True
    assert dec["O210_excluded"] is False
    assert dec["O212_plus_advance_allowed"] is False
    assert dec["fixed_V6_all_integral_genus1_carriers_excluded"] is False
    assert dec["repair_is_exact_nonexclusion_boundary"] is True
    assert cert["firewalls"]["Gamma_square_from_bidegree_alone_forbidden"] is True
    assert cert["firewalls"]["zero_rosati_specialization_reuse_forbidden"] is True
    assert cert["firewalls"]["full178_authorized"] is False

    print("PASS_POST1500_ROSATI_TRACE_REPAIR_SIGMA1204_Q602_NONEXCLUSION")


if __name__ == "__main__":
    main()
