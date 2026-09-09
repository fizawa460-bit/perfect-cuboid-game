#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ARTIFACT = ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2-00-second-pass-repository-dedup.json"
FIRST = ROOT / "stages/stage32-ex5/breadth-cycle-2/bc2-00-btva-node-support-span-diagnostic.json"
POLICY = ROOT / "docs/research-os/policies/repository-asset-discovery.md"
INDEX = ROOT / "docs/arsenal/index.json"
CATALOG = ROOT / "docs/arsenal/catalog.md"
CONTRACT = ROOT / "stages/stage29/29-02c-LG2/finite-search-contract.md"
AGG = ROOT / "stages/stage32/residual-32-01-production/aggregate_stage32_post21bl_full178_node_mass_shards.py"

EXPECTED_CANONICAL = "c3789b3b4ac53fe2162f580989fbca6512007f1b7b19cdeef54ca541a3abfedc"
EXPECTED_BLOBS = {
    FIRST: "554f8626e0ea225ffb7e6a5b6fe40ee41a7448ee",
    POLICY: "bf001d4ff4375281a901d52c147c35c28643b8a3",
    INDEX: "82cbbe88b2a3afc7f3a13d34ce0ca6a43004ea98",
    CATALOG: "87c4c896cc04a34e8e12ede92ced1c6079b76874",
    CONTRACT: "2c1a4813a77b517482b6fef497f9a517c9d12fe6",
    AGG: "92561bbc1cac6f2d5c47bf37bfbc9c6bfaba3cdd",
}


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def main() -> None:
    p = json.loads(ARTIFACT.read_text())
    got = p.pop("canonical_sha256_without_this_field")
    assert got == EXPECTED_CANONICAL
    assert csha(p) == EXPECTED_CANONICAL

    assert p["schema"] == "STAGE32EX5_BC2_00_SECOND_PASS_REPOSITORY_DEDUP_V1"
    assert p["status"] == "SECOND_PASS_DEDUP_PASS_MATERIALLY_NEW_ROUTE_FAMILY_REENTRY_ELIGIBLE_UNAUDITED"
    assert p["route_id"] == "EX5R-SYMDIFF-NODE-SPAN-001"
    assert p["route_family"] == "SYMMETRIC_DIFFERENTIAL_NODE_SUPPORT_SPAN_LANE"
    assert p["decision"]["classification"] == "NEW_ROUTE_WITH_EXISTING_EXACT_RESOURCE_PROVIDERS"
    assert p["decision"]["materially_new_route_family"] is True
    assert p["decision"]["formal_reentry_eligible"] is True
    assert p["decision"]["route_qualified"] is False
    assert p["decision"]["mathematical_credit"] is False
    assert p["decision"]["receiver_credit"] is False
    assert p["decision"]["stage32_main_credit"] is False
    assert p["decision"]["next_leaf"] == "BC2-01_SUPPORT_ADAPTER_PREFLIGHT"

    for path, expected in EXPECTED_BLOBS.items():
        actual = git_blob_sha(path)
        assert actual == expected, (str(path), actual, expected)

    assert INDEX.stat().st_size == 101763
    assert p["basis"]["arsenal_index_whole_fetched_into_chat"] is False
    assert p["arsenal_second_pass"]["search_miss_used_as_proof_of_absence"] is False
    assert p["arsenal_second_pass"]["absence_is_not_repository_wide_mathematical_absence"] is True
    assert p["arsenal_second_pass"]["dedup_decision_derived_from_exact_non_equivalence_with_nearest_bound_assets"] is True

    assets = {a["id"]: a for a in p["nearest_assets"]}
    assert assets["STAGE29_LG2_COARSE_EXCEPTIONAL_INCIDENCE_FILTER"]["classification"] == "STRICTLY_WEAKER_EXISTING_INPUT_NOT_DUPLICATE"
    assert assets["STAGE32_FULL178_NODE_MASS_AGGREGATE"]["classification"] == "EXISTING_WITH_MISSING_SUPPORT_GEOMETRY_ADAPTER_NOT_DUPLICATE"
    assert assets["STOLL_EXACT_CUBOID_48_NODE_MODEL"]["classification"] == "EXISTING_RESOURCE_PROVIDER_NOT_ROUTE_DUPLICATE"

    contract_text = CONTRACT.read_text()
    assert "exceptional-divisor incidence lower bounds from Testa--Stoll Lemma 21" in contract_text
    assert "These filters do not by themselves certify effectivity." in contract_text

    agg_text = AGG.read_text()
    assert '"strong_48bit_node_support_not_inferred_from_exceptional_mass": True' in agg_text
    assert '"receiver_credit": False' in agg_text
    assert '"theorem_credit": False' in agg_text

    first = json.loads(FIRST.read_text())
    assert first["route_family"] == p["route_family"]
    assert first["reentry"]["final_material_novelty_requires_second_pass_dedup"] is True
    assert first["authority"]["repository_wide_dedup_complete"] is False

    assert p["cycle1_nonduplicate"]["same_as_any_cycle1_family"] is False
    assert p["cycle1_nonduplicate"]["reentry_condition_satisfied"] == "MATERIALLY_NEW_ROUTE_FAMILY_WITH_NEW_BREADTH_CYCLE"
    assert p["external_theorem"]["locator"] == "Theorem 1.2"
    assert "seven singularities that span P6" in p["external_theorem"]["genus0_nonconic"]
    assert "six singularities spanning a hyperplane" in p["external_theorem"]["genus1"]

    for k in [
        "cycle1_audited_closure_revoked",
        "cycle2_reentry_is_stage32_main_promotion",
        "new_theorem_name_alone_is_route_qualification",
        "mass_treated_as_labelled_support",
        "node_count_treated_as_span_rank",
        "search_miss_promoted_to_absence",
        "effectivity_inferred_from_numerical_survival",
        "Q602_excluded",
        "O210_excluded",
        "FULL178_closed",
        "perfect_cuboid_nonexistence_claim",
    ]:
        assert p["firewalls"][k] is False
    assert p["firewalls"]["known_32_conic_exception_preserved"] is True
    assert p["firewalls"]["genus1_hyperplane_component_alternative_preserved"] is True

    print(json.dumps({
        "verdict": "PASS_BC2_00_SECOND_PASS_DEDUP_MATERIALLY_NEW_ROUTE_REENTRY_ELIGIBLE",
        "canonical_sha256": EXPECTED_CANONICAL,
        "route_qualified": False,
        "mathematical_credit": False,
        "next_leaf": "BC2-01_SUPPORT_ADAPTER_PREFLIGHT",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
