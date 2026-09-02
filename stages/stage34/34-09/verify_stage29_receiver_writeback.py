#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CERT_PATH = ROOT / "stages/stage34/34-09/stage29-receiver-writeback-certificate.json"


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def load_locked(path: str, expected: str):
    data = (ROOT / path).read_bytes()
    assert git_blob_sha(data) == expected, (path, git_blob_sha(data), expected)
    suffix = Path(path).suffix
    if suffix == ".json":
        return json.loads(data)
    return data.decode()


def main():
    cert = json.loads(CERT_PATH.read_text())
    assert cert["status"] == "PASS_EXACT_CROSS_STAGE_RECEIVER_WRITEBACK"
    locked = {k: load_locked(*v) for k, v in cert["stage29_source_locks"].items()}

    active = locked["active_kernel_ledger"]
    target = [k for k in active["class3_kernels"] if k["kernel"] == cert["kernel"]]
    assert len(target) == 1
    target = target[0]
    assert target["children"] == [cert["receiver"]]
    assert target["parent_routes"] == [cert["parent_route"]]
    assert target["endpoint_decisive_alone"] is False

    portfolio = locked["route_portfolio"]
    route = [r for r in portfolio["routes"] if r["route"] == cert["parent_route"]]
    assert len(route) == 1
    assert cert["kernel"] in route[0]["kernels"]
    assert route[0]["color"] == "AMBER"

    final = locked["final_handoff"]
    assert final["stage29_closed"] is True
    assert final["perfect_cuboid_problem_status"] == "OPEN"
    assert cert["kernel"] in final["final_active_kernels"]["class3"]
    assert final["final_active_kernels"]["total"] == 13
    assert len(final["final_active_kernels"]["class3"]) == 9
    assert len(final["final_active_kernels"]["class2"]) == 4

    research_os = locked["post_stage29_research_os"]
    assert "new published theorem/preprint materially changes a Class-3 applicability verdict" in research_os
    assert "new exact structure that changes the dependency graph" in research_os

    promo = cert["stage34_promotion_lock"]
    promo_data = load_locked(promo["path"], promo["blob_sha"])
    assert promo_data["hostile_audit"]["review_id"] == promo["hostile_audit_review_id"] == 5088591887
    assert promo_data["promotion"]["all_multiples_closed"] is True
    assert promo_data["promotion"]["R29_EXT_CHANG_C_closed"] is True

    wb = cert["writeback"]
    assert wb["remove_from_post_stage29_active_kernel_frontier"] is True
    assert wb["historical_stage29_ledgers_rewritten"] is False

    counts = cert["updated_frontier_accounting"]
    assert counts["post_stage34_active_kernel_count"] == counts["stage29_frozen_active_kernel_count"] - 1 == 12
    assert counts["post_stage34_class3_kernel_count"] == counts["stage29_frozen_class3_kernel_count"] - 1 == 8
    assert counts["post_stage34_class2_kernel_count"] == counts["stage29_frozen_class2_kernel_count"] == 4
    assert cert["kernel"] not in counts["J12_PARAMETRIC_remaining_kernels"]

    fw = cert["semantic_firewalls"]
    assert fw["J12_PARAMETRIC_closed"] is False
    assert fw["parent_route_closed"] is False
    assert fw["all_Master_Hit_fibers_closed"] is False
    assert fw["perfect_cuboid_existence_claim"] is False
    assert fw["perfect_cuboid_nonexistence_claim"] is False
    assert fw["merge_authorized"] is False

    print("PASS_EXACT_STAGE29_RECEIVER_WRITEBACK_ONLY")


if __name__ == "__main__":
    main()
