#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = Path(__file__).resolve().parents[3]

V6_CANONICAL = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
PICARD_SHA256 = "2d5b956b182369cf42d3c34352e79c6306700ff87907f4e6d25d5743d7f12726"
ALL140_SHA256 = "4d4f6d306fcd1974ebb539c5adc65a0d595ca8d471d2a12b1e785bac7f41c9a3"
SOURCE_NOTE_GIT_BLOB_SHA1 = "203838b6e7504fcda517ce3aadd9b5f09063257c"
TARGET_DEGREE = 186
TARGET_GENUS = 1
EXCEPTIONAL_COUNT = 48


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def git_blob_sha1(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def build_certificate() -> dict:
    v6_path = REPO / "stages/stage32/32-21/post1473-v6-witness-body-recovered.json"
    v6 = json.loads(v6_path.read_text())
    body = dict(v6)
    claimed = body.pop("canonical_sha256_without_this_field", None)
    if claimed != V6_CANONICAL or csha(body) != V6_CANONICAL:
        raise ValueError("V6 recovered witness canonical lock moved")

    witness = v6["witness"]
    if witness.get("picard_coordinates_sha256") != PICARD_SHA256:
        raise ValueError("V6 Picard-coordinate lock moved")
    all140 = [int(x) for x in witness["all140_pairings"]]
    if len(all140) != 140 or csha(all140) != ALL140_SHA256:
        raise ValueError("V6 all140 lock moved")
    if witness.get("all140_pairings_sha256") != ALL140_SHA256:
        raise ValueError("V6 persisted all140 SHA lock moved")

    note = HERE / "post1473-specific-class-fsm-refined-pole-obstruction.md"
    if git_blob_sha1(note) != SOURCE_NOTE_GIT_BLOB_SHA1:
        raise ValueError("FSM refined-pole source note moved")
    note_text = note.read_text()
    for phrase in (
        "d <= 16*g - 16 + 4*n1",
        "m = min(r/4, s/4, (r+s)/8) = min(r,s)/4",
        "local_pole_order <= max(0, 16-8*m)*k",
        "bijective-normalization branch exclusion only",
        "10.1307/mmj/1480734014",
    ):
        if phrase not in note_text:
            raise ValueError(f"FSM source-note semantic lock moved: {phrase}")

    exceptional = all140[-EXCEPTIONAL_COUNT:]
    if min(exceptional) < 0:
        raise ValueError("V6 exceptional pairing nonnegativity regression")
    zero_count = sum(x == 0 for x in exceptional)
    one_count = sum(x == 1 for x in exceptional)
    ge2_count = sum(x >= 2 for x in exceptional)
    support = sum(x > 0 for x in exceptional)
    if (zero_count, one_count, ge2_count, support) != (1, 9, 38, 47):
        raise ValueError(
            f"V6 exceptional histogram regression: {(zero_count, one_count, ge2_count, support)}"
        )

    coarse_fsm_bound = 176 + 16 * TARGET_GENUS
    refined_bound = 16 * TARGET_GENUS - 16 + 4 * one_count
    excluded = TARGET_DEGREE > refined_bound
    if coarse_fsm_bound != 192 or refined_bound != 36 or not excluded:
        raise ValueError("refined FSM arithmetic regression")

    cert = {
        "schema": "STAGE32_POST1473_FSM_REFINED_BIJECTIVE_NORMALIZATION_POLE_OBSTRUCTION_V1",
        "stage": 32,
        "leaf": "POST1473_FIXED_Z_FSM_REFINED_BIJECTIVE_NORMALIZATION_OBSTRUCTION",
        "target": {
            "row_id": v6["target"]["row_id"],
            "z": v6["target"]["z"],
            "degree": TARGET_DEGREE,
            "geometric_genus": TARGET_GENUS,
        },
        "source_locks": {
            "v6_witness_body_canonical_sha256": V6_CANONICAL,
            "picard_coordinates_sha256": PICARD_SHA256,
            "all140_pairings_sha256": ALL140_SHA256,
            "fsm_refined_source_note_git_blob_sha1": SOURCE_NOTE_GIT_BLOB_SHA1,
            "fsm_doi": "10.1307/mmj/1480734014",
            "fsm_arxiv": "1303.6495",
        },
        "exact_exceptional_histogram": {
            "exceptional_count": EXCEPTIONAL_COUNT,
            "zero": zero_count,
            "equal_one": one_count,
            "at_least_two": ge2_count,
            "positive_support": support,
            "exceptional_sum": sum(exceptional),
            "exceptional_pairings_sha256": csha(exceptional),
        },
        "local_refinement": {
            "node_model": "(C^2)/(+/-1), invariants x=p^2,y=q^2,u=p*q",
            "exceptional_intersection_formula": "m=C.E=min(r,s)/4",
            "cusp_sum_lower_bound": "r+s>=8*m",
            "local_pole_order_upper_bound": "max(0,16-8*m)*k",
            "positive_pole_possible_only_when_C_dot_E_equals_1": True,
            "total_pole_order_upper_bound": f"8*k*{one_count}=72*k",
        },
        "fsm_degree_bounds": {
            "coarse_theorem_3_1": coarse_fsm_bound,
            "refined_with_exact_C_dot_E_histogram": refined_bound,
            "refined_formula": "d<=16*g-16+4*n1",
            "n1": one_count,
        },
        "verdict": {
            "degree": TARGET_DEGREE,
            "refined_degree_upper_bound": refined_bound,
            "contradiction": excluded,
            "bijective_normalization_integral_genus1_carrier_in_this_exact_class": False,
            "status": "EXACT_BIJECTIVE_NORMALIZATION_G1_EXCLUDED_BY_REFINED_FSM_POLE_BOUND",
        },
        "firewalls": {
            "nonbijective_normalization_multibranch_case_closed": False,
            "fixed_z_all_integral_genus1_carriers_closed": False,
            "full178_closed": False,
            "general_low_genus_classification_closed": False,
            "receiver_credit": False,
            "route_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    cert["canonical_sha256_without_this_field"] = csha(cert)
    return cert


def main() -> None:
    cert = build_certificate()
    out = HERE / "post1473-specific-class-fsm-refined-pole-obstruction.json"
    out.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "success": True,
        "n1": cert["fsm_degree_bounds"]["n1"],
        "refined_degree_upper_bound": cert["fsm_degree_bounds"]["refined_with_exact_C_dot_E_histogram"],
        "degree": cert["verdict"]["degree"],
        "bijective_normalization_genus1_excluded": cert["verdict"]["contradiction"],
        "canonical_sha256": cert["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
