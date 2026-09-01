#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = Path(__file__).resolve().parents[3]

V6_CANONICAL = "d0c1c8bddfe3950737ed6f87ffa74acd850c736298bd12ec1eceac609625b8a8"
PICARD_SHA256 = "2d5b956b182369cf42d3c34352e79c6306700ff87907f4e6d25d5743d7f12726"
ALL140_SHA256 = "4d4f6d306fcd1974ebb539c5adc65a0d595ca8d471d2a12b1e785bac7f41c9a3"
SOURCE_NOTE_GIT_BLOB_SHA1 = "cb20a9b287430c2e238f79d3151500c262905468"
ARSENAL_STAGE32_PROMOTION_GIT_BLOB_SHA1 = "02fdae0b3a2e78e073035b7f373884262183e2fb"
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


@lru_cache(maxsize=None)
def partition_state_set(total: int, minimum_part: int = 1) -> frozenset[tuple[int, int, int]]:
    """Return exact (branch_count, odd_branch_count, multiplicity_one_count) states."""
    if total == 0:
        return frozenset({(0, 0, 0)})
    states: set[tuple[int, int, int]] = set()

    def rec(remaining: int, lo: int, parts: tuple[int, ...]) -> None:
        if remaining == 0:
            states.add(
                (
                    len(parts),
                    sum(x % 2 for x in parts),
                    sum(x == 1 for x in parts),
                )
            )
            return
        for first in range(lo, remaining + 1):
            rec(remaining - first, first, parts + (first,))

    rec(total, minimum_part, ())
    return frozenset(states)


def aggregate_partition_states(exceptional: list[int]) -> set[tuple[int, int, int]]:
    states: set[tuple[int, int, int]] = {(0, 0, 0)}
    for m in exceptional:
        local = partition_state_set(m)
        states = {
            (b0 + b1, o0 + o1, s0 + s1)
            for (b0, o0, s0) in states
            for (b1, o1, s1) in local
        }
    return states


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

    note = HERE / "post1473-specific-class-multibranch-beauville-odd-branch-wall.md"
    if git_blob_sha1(note) != SOURCE_NOTE_GIT_BLOB_SHA1:
        raise ValueError("multibranch Beauville source note moved")
    note_text = note.read_text()
    for phrase in (
        "O >= d",
        "O >= 186",
        "S1 >= 146",
        "B >= ceil((d+4e)/8) = 157",
        "S32-PW01",
        "10.1307/mmj/1480734014",
        "non-bijective/multibranch carrier remains open",
    ):
        if phrase not in note_text:
            raise ValueError(f"source-note semantic lock moved: {phrase}")

    arsenal = REPO / "docs/stage32-arsenal-promotion.md"
    if git_blob_sha1(arsenal) != ARSENAL_STAGE32_PROMOTION_GIT_BLOB_SHA1:
        raise ValueError("Stage32 Arsenal promotion source moved")
    if "S32-PW01" not in arsenal.read_text() or "EXACT_ENUMERATION_COMPRESSION_AND_INDEXER" not in arsenal.read_text():
        raise ValueError("Stage32 Arsenal S32-PW01 semantic lock moved")

    exceptional = all140[-EXCEPTIONAL_COUNT:]
    if min(exceptional) < 0:
        raise ValueError("negative V6 exceptional intersection")
    exceptional_mass = sum(exceptional)
    odd_total_nodes = sum(m % 2 for m in exceptional)
    if exceptional_mass != 266 or odd_total_nodes != 26:
        raise ValueError(
            f"V6 exceptional mass/parity regression: mass={exceptional_mass}, odd_nodes={odd_total_nodes}"
        )

    states = aggregate_partition_states(exceptional)
    sorted_states = sorted(states)
    reachable_odd = sorted({o for _, o, _ in states})
    expected_odd = list(range(26, 267, 2))
    if reachable_odd != expected_odd:
        raise ValueError("reachable odd-contact count set regression")

    beauville_odd_lower_bound = TARGET_DEGREE
    fsm_branch_lower_bound = (TARGET_DEGREE + 4 * exceptional_mass + 7) // 8
    admissible = [(b, o, s) for (b, o, s) in states if o >= beauville_odd_lower_bound]
    if not admissible:
        raise ValueError("no branch-partition state reaches Beauville odd-contact lower bound")
    min_simple = min(s for _, _, s in admissible)
    extremal = (186, 186, 146)
    if fsm_branch_lower_bound != 157 or min_simple != 146 or extremal not in states:
        raise ValueError(
            "multibranch burden arithmetic/state regression: "
            f"fsm={fsm_branch_lower_bound}, min_simple={min_simple}, extremal={extremal in states}"
        )

    cert = {
        "schema": "STAGE32_POST1473_MULTIBRANCH_BEAUVILLE_ODD_BRANCH_WALL_V1",
        "stage": 32,
        "leaf": "POST1473_FIXED_Z_NONBIJECTIVE_NORMALIZATION_MULTIBRANCH_CARRIER_OR_EXCLUSION",
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
            "multibranch_source_note_git_blob_sha1": SOURCE_NOTE_GIT_BLOB_SHA1,
            "stage32_arsenal_promotion_git_blob_sha1": ARSENAL_STAGE32_PROMOTION_GIT_BLOB_SHA1,
            "fsm_doi": "10.1307/mmj/1480734014",
            "fsm_arxiv": "1303.6495",
            "arsenal_card": "S32-PW01 EXACT_ENUMERATION_COMPRESSION_AND_INDEXER",
        },
        "exact_exceptional_data": {
            "exceptional_count": EXCEPTIONAL_COUNT,
            "exceptional_mass_e": exceptional_mass,
            "odd_total_intersection_node_count": odd_total_nodes,
            "exceptional_pairings": exceptional,
            "exceptional_pairings_sha256": csha(exceptional),
        },
        "beauville_product_cover_necessary_condition": {
            "x8_genus": 5,
            "product_to_beauville_unramified_degree": 4,
            "beauville_to_box_degree": 2,
            "normalized_odd_contact_count_symbol": "O",
            "derivation": "qprime*O >= 8*max(n1,n2) >= 4*(n1+n2) = qprime*d",
            "odd_contact_lower_bound": beauville_odd_lower_bound,
            "total_branch_count_lower_bound_from_O": beauville_odd_lower_bound,
            "multiplicity_one_branch_lower_bound": min_simple,
        },
        "branchwise_fsm_crosscheck": {
            "derivation": "16*(2g-2) >= 2*d + 8*e - 16*B",
            "total_branch_count_lower_bound": fsm_branch_lower_bound,
            "dominated_by_beauville_odd_contact_bound": True,
        },
        "compressed_partition_state": {
            "method": "exact per-node integer-partition states aggregated by dynamic programming",
            "arsenal_pattern": "S32-PW01",
            "reachable_state_count": len(states),
            "reachable_states_sha256": csha(sorted_states),
            "reachable_odd_contact_counts": {
                "minimum": reachable_odd[0],
                "maximum": reachable_odd[-1],
                "step": 2,
                "count": len(reachable_odd),
            },
            "odd_contact_186_reachable": any(o == 186 for _, o, _ in states),
            "minimum_multiplicity_one_branches_given_O_ge_186": min_simple,
            "extremal_reachable_state": {
                "B": extremal[0],
                "O": extremal[1],
                "S1": extremal[2],
            },
        },
        "verdict": {
            "beauville_odd_branch_burden_exactly_derived": True,
            "current_exceptional_intersection_data_excludes_multibranch_carrier": False,
            "coarse_branch_partition_layer_has_surviving_states": True,
            "status": "PROVISIONAL_EXACT_MULTIBRANCH_BEAUVILLE_ODD_BRANCH_BURDEN_NONEXCLUSION_WALL",
        },
        "firewalls": {
            "coarse_partition_is_analytic_branch_realization": False,
            "local_valuation_compatibility_is_global_curve_existence": False,
            "bijective_normalization_exclusion_reopened": False,
            "fixed_z_multibranch_carrier_closed": False,
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


def render(cert: dict) -> str:
    return json.dumps(cert, indent=2, sort_keys=True) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    cert = build_certificate()
    out = HERE / "post1473-specific-class-multibranch-beauville-odd-branch-wall.json"
    text = render(cert)
    if args.check:
        if not out.exists() or out.read_text() != text:
            raise SystemExit("persisted multibranch Beauville certificate differs from deterministic replay")
    else:
        out.write_text(text)
    print(
        json.dumps(
            {
                "success": True,
                "odd_contact_lower_bound": cert["beauville_product_cover_necessary_condition"]["odd_contact_lower_bound"],
                "minimum_multiplicity_one_branches": cert["beauville_product_cover_necessary_condition"]["multiplicity_one_branch_lower_bound"],
                "multibranch_excluded": cert["verdict"]["current_exceptional_intersection_data_excludes_multibranch_carrier"],
                "canonical_sha256": cert["canonical_sha256_without_this_field"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
