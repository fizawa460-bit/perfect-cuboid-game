#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ART = HERE / "ex1-07-current-main-v6-carrier-promotion-adapter.json"
MAIN = ROOT / "stage32" / "MAIN-STATE.json"
EX100 = HERE / "ex1-00-source-lock-and-target-adapter.json"
ROADMAP = HERE / "stage32-ex1.md"
REGISTRY = ROOT / "stage32" / "proof" / "CLAIM-REGISTRY.json"
FRONTIER = ROOT / "stage32" / "proof" / "ACTIVE-FRONTIER.json"


def load(path: Path):
    return json.loads(path.read_text())


def csha(value) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def pathmap(d: dict) -> dict[str, dict]:
    out = {}
    for item in d.values():
        if isinstance(item, dict) and isinstance(item.get("path"), str):
            out[item["path"]] = item
    return out


def main() -> None:
    art = load(ART)
    stored = art.pop("canonical_sha256_without_this_field")
    assert csha(art) == stored == "e21bf24712be8931b6854e2640cf9ccc02c965a4235be84e60086565c4d76a42"
    art["canonical_sha256_without_this_field"] = stored
    assert art["schema"] == "STAGE32EX1_EX1_07_CURRENT_MAIN_V6_CARRIER_PROMOTION_ADAPTER_V1"
    assert art["status"] == "AUDIT_READY_PROVISIONAL_CURRENT_TARGET_ADAPTER"
    assert art["bridge"] == {
        "from_scope_key": "S32.EX1.V6_CARRIER",
        "to_scope_key": "S32.MAIN.V6_CARRIER",
        "semantics": "population_identity_for_geometric_V6_integral_irreducible_genus1_carriers_only",
    }

    main_state = load(MAIN)
    ex1 = load(EX100)
    registry = load(REGISTRY)
    frontier = load(FRONTIER)

    locks = art["current_target_locks"]
    assert blob_sha1(MAIN) == locks["stage32_main_state"]["blob_sha1"]
    assert blob_sha1(EX100) == locks["ex1_target_adapter"]["blob_sha1"]
    assert ex1["canonical_sha256_without_this_field"] == locks["ex1_target_adapter"]["canonical_sha256"]
    assert blob_sha1(ROADMAP) == locks["stage32_ex1_roadmap"]["blob_sha1"]

    mf = main_state["fixed_target"]
    mc = main_state["current_exact_frontier"]
    xv = ex1["v6_target"]
    xp = ex1["population_contract"]
    ident = art["population_identity"]

    assert mf["row_id"] == xv["row_id"] == ident["row_id"] == "g1-d186"
    assert mf["degree"] == xv["degree_d"] == ident["K_dot_D"] == 186
    assert mf["genus"] == xv["target_geometric_genus"] == ident["geometric_genus"] == 1
    assert mc["v6_self_intersection"] == xv["D_square"] == ident["D_square"] == 758
    assert mc["v6_canonical_intersection"] == xv["K_dot_D"] == ident["K_dot_D"] == 186
    assert xv["arithmetic_genus"] == ident["arithmetic_genus"] == 473
    assert xv["required_total_normalization_genus_defect"] == ident["required_total_delta"] == 472
    assert xp["surface"] == ident["surface"] == "minimal_desingularization_S_of_the_cuboid_surface"
    assert xp["target_geometric_genus"] == ident["geometric_genus"]
    assert xp["geometric_analysis_field"] == ident["geometric_analysis_field"] == "C"
    assert "geometrically_integral_irreducible_curve_C_on_S_with_Picard_class_V6" == xp["carrier"]
    assert ident["picard_class"] == "V6" and ident["integral"] and ident["irreducible"]

    main_locks = pathmap(main_state["source_locks"])
    ex1_locks = pathmap(ex1["source_locks"])
    for expected in art["shared_source_lock_identity"]:
        path = expected["path"]
        assert path in main_locks and path in ex1_locks
        for key in ("blob_sha1", "canonical_sha256"):
            assert main_locks[path][key] == ex1_locks[path][key] == expected[key]

    by_id = {c["claim_id"]: c for c in registry["claims"]}
    terminal = by_id[art["audited_terminal_input"]["claim_id"]]
    ai = art["audited_terminal_input"]
    assert terminal["authority_status"] == ai["authority_status"] == "AUDITED"
    assert terminal["claim_core_sha256"] == ai["claim_core_sha256"]
    assert terminal["scope_key"] == art["bridge"]["from_scope_key"]
    assert terminal["audit_receipt"] == {
        "status": "PASS",
        "pr": ai["pr"],
        "exact_head": ai["exact_head"],
        "review_id": ai["review_id"],
    }

    main_context = by_id["S32.MAIN.CURRENT_TARGET_CONTEXT.V1"]
    assert main_context["scope"]["row_id"] == ident["row_id"]
    assert main_context["scope"]["picard_class"] == ident["picard_class"]

    fby = {c["claim_id"]: c for c in frontier["claims"]}
    goal = fby["S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V1"]
    assert goal["scope_key"] == art["bridge"]["to_scope_key"]
    assert goal["scope"]["row_id"] == ident["row_id"]
    assert goal["scope"]["picard_class"] == ident["picard_class"]
    assert goal["scope"]["integral"] is True and goal["scope"]["irreducible"] is True
    assert goal["scope"]["geometric_genus"] == ident["geometric_genus"]
    assert goal["scope"]["target"] == "population_wide_nonexistence"

    roadmap = ROADMAP.read_text()
    assert "Fix the exact Stage32 V6 target" in roadmap
    assert "ALL_V6_GENUS1_CARRIERS_EXCLUDED" in roadmap
    assert "Transfer into Stage32 MAIN requires a separate explicit adapter/promotion step" in roadmap

    assert art["promotion_candidate"]["main_claim_id"] == "S32.V6.NO_INTEGRAL_IRREDUCIBLE_GENUS1_MEMBER.V2"
    assert art["promotion_candidate"]["authority_status"] == "PROVISIONAL"
    assert art["promotion_candidate"]["hostile_audit_required"] is True
    assert art["promotion_candidate"]["active_frontier_remap_deferred_until_promotion_audit_pass"] is True
    assert all(v is False for v in art["firewalls"].values())

    print("PASS_EX1_07_CURRENT_MAIN_V6_CARRIER_POPULATION_IDENTITY_ADAPTER")


if __name__ == "__main__":
    main()
