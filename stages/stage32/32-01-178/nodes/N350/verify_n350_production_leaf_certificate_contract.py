#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
CONTRACT_PATH = HERE / "PRODUCTION_LEAF_CERTIFICATE_CONTRACT.json"

EXPECTED_CONTRACT_CANONICAL = "7d64040945f258048f9d61b0f888ca8d3720bedee6eab8902c7233ffc059d25a"
EXPECTED_SOURCE_BLOBS = {
    "stages/stage32/32-01-178/nodes/N240/STATE.json": "869c8b1dc3937a7e78e907e74b0ed08994a5199c",
    "stages/stage32/32-01-178/nodes/N104/STATE.json": "4ac907febfd60a3fb53e57bbb8ede9cf8959e954",
    "stages/stage32/32-01-178/nodes/N106/STATE-AUDITED.json": "0ab8647b5af453e48b786103eb57b2a495f855fc",
    "stages/stage32/32-01-178/nodes/N220/STATE-AUDITED.json": "f5f0e902062c9fafc9f03fe8a203d744cf58281e",
    "stages/stage32/32-01-178/nodes/N230/STATE-AUDITED.json": "9c4ecb012df70dc1b39f6cfffbd7c5b481f51967",
    "stages/stage32/residual-32-01-production/full178-manifest.json": "0a46b34e278688240656b4977e9cb7f589e90e06",
}
REQUIRED_BLOCK_FIELDS = {
    "row_id", "d", "e", "filtered_rank_lo", "filtered_rank_hi",
    "old_rank_intervals", "disposition", "producer_id",
    "producer_contract_sha256", "producer_evidence_sha256", "unknown_count",
}
ALLOWED_DISPOSITIONS = {"EXACT_PRUNED", "NUMERICAL_CHECKED"}


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


def is_sha256(value: object) -> bool:
    if not isinstance(value, str) or len(value) != 64:
        return False
    try:
        int(value, 16)
    except ValueError:
        return False
    return True


def load_json(path: Path) -> dict:
    value = json.loads(path.read_text())
    if not isinstance(value, dict):
        raise ValueError(f"expected dict JSON: {path}")
    return value


def verify_source_locks(contract: dict) -> None:
    for rel, expected in EXPECTED_SOURCE_BLOBS.items():
        path = ROOT / rel
        got = git_blob_sha1(path.read_bytes())
        if got != expected:
            raise ValueError(f"source-lock regression {rel}: {got} != {expected}")

    n240 = load_json(ROOT / "stages/stage32/32-01-178/nodes/N240/STATE.json")
    if n240["validation"].get("status") != "HOSTILE_REAUDIT_PASS_CONSUMED":
        raise ValueError("N240 hostile re-audit PASS is not consumed")
    if n240["validation"].get("hostile_reaudit_review_id") != 5161254728:
        raise ValueError("N240 hostile re-audit review regression")
    if n240["validation"].get("hostile_reaudit_exact_head") != "b56a832e6c194321916fe4ef63eef0d673b8ff9a":
        raise ValueError("N240 hostile re-audit exact-head regression")
    if n240["retained_result"].get("production_complete_available") is not False:
        raise ValueError("N240 must remain fail-closed for production completeness")

    n104 = load_json(ROOT / "stages/stage32/32-01-178/nodes/N104/STATE.json")
    if n104["retained_result"].get("current_full178_complete") is not False:
        raise ValueError("N104 completion authority unexpectedly released")
    if "every canonical terminal rank covered exactly once" not in n104["retained_result"].get("completion_rule", ""):
        raise ValueError("N104 canonical coverage rule regression")

    n106 = load_json(ROOT / "stages/stage32/32-01-178/nodes/N106/STATE-AUDITED.json")
    rr = n106.get("retained_result", {})
    if rr.get("hostile_audit_result") != "PASS" or rr.get("hostile_audit_review_id") != 5153922196:
        raise ValueError("N106 audited execution architecture regression")
    if rr.get("full178_numerical_credit") is not False:
        raise ValueError("N106 must not carry FULL178 numerical credit")

    manifest_lock = contract["source_locks"]["full178_manifest"]
    if manifest_lock.get("canonical_sha256") != "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23":
        raise ValueError("FULL178 manifest canonical regression")


def validate_block(block: dict, producers: dict[str, dict]) -> None:
    if set(block) < REQUIRED_BLOCK_FIELDS:
        missing = sorted(REQUIRED_BLOCK_FIELDS - set(block))
        raise ValueError(f"production block missing fields: {missing}")
    if block["disposition"] not in ALLOWED_DISPOSITIONS:
        raise ValueError("unsupported disposition")
    if int(block["unknown_count"]) != 0:
        raise ValueError("unknown/resource wall cannot receive production credit")
    lo = int(block["filtered_rank_lo"])
    hi = int(block["filtered_rank_hi"])
    if lo < 0 or hi <= lo:
        raise ValueError("invalid filtered half-open interval")
    old = block["old_rank_intervals"]
    if not isinstance(old, list) or not old:
        raise ValueError("canonical old-rank mapping is required")
    prev_hi = None
    for pair in old:
        if not isinstance(pair, list) or len(pair) != 2:
            raise ValueError("old_rank_intervals must contain [lo,hi] pairs")
        a, b = map(int, pair)
        if a < 0 or b <= a:
            raise ValueError("invalid old-rank interval")
        if prev_hi is not None and a < prev_hi:
            raise ValueError("overlapping old-rank intervals")
        prev_hi = b
    producer_id = block["producer_id"]
    if producer_id not in producers:
        raise ValueError("unregistered producer receives zero coverage credit")
    reg = producers[producer_id]
    if block["disposition"] not in reg.get("accepted_dispositions", []):
        raise ValueError("producer not audited for requested disposition")
    if block["producer_contract_sha256"] != reg.get("producer_contract_sha256"):
        raise ValueError("producer contract binding mismatch")
    if not is_sha256(block["producer_evidence_sha256"]):
        raise ValueError("producer evidence digest malformed")


def validate_production_certificate(contract: dict, cert: dict) -> None:
    if cert.get("schema") != contract["production_certificate"]["schema"]:
        raise ValueError("production certificate schema mismatch")
    if cert.get("contract_canonical_sha256") != EXPECTED_CONTRACT_CANONICAL:
        raise ValueError("contract canonical binding mismatch")
    registry = contract["producer_registry"]
    registry_sha = csha(registry)
    if cert.get("producer_registry_canonical_sha256") != registry_sha:
        raise ValueError("producer registry binding mismatch")
    if int(cert.get("unknown_count", -1)) != 0:
        raise ValueError("unknown_count must be zero")
    blocks = cert.get("coverage_blocks")
    if not isinstance(blocks, list):
        raise ValueError("coverage_blocks must be a list")
    producers = {row["producer_id"]: row for row in registry}
    for block in blocks:
        if not isinstance(block, dict):
            raise ValueError("coverage block must be dict")
        validate_block(block, producers)
    if cert.get("verdict") == contract["production_certificate"]["complete_verdict"]:
        if not registry:
            raise ValueError("PASS production coverage forbidden with empty producer registry")
        if not blocks:
            raise ValueError("PASS production coverage requires replayed credited blocks")


def expect_reject(contract: dict, cert: dict) -> None:
    try:
        validate_production_certificate(contract, cert)
    except (ValueError, KeyError, TypeError):
        return
    raise ValueError("hostile fixture unexpectedly accepted")


def main() -> None:
    contract = load_json(CONTRACT_PATH)
    canonical = contract.pop("canonical_sha256_without_this_field")
    if canonical != EXPECTED_CONTRACT_CANONICAL or csha(contract) != canonical:
        raise ValueError("N350 contract canonical regression")
    if contract.get("node_id") != "N350":
        raise ValueError("N350 node identity regression")
    if contract["canonical_domain"].get("expected_residual_rows") != 178:
        raise ValueError("FULL178 row-count regression")
    if contract["canonical_domain"].get("expected_coarse_strata") != 64111:
        raise ValueError("FULL178 coarse-strata regression")
    if contract["producer_registry"] != []:
        raise ValueError("N350 V1 checkpoint must start with empty producer registry")
    cp = contract["current_checkpoint"]
    if cp.get("production_complete_available") is not False:
        raise ValueError("N350 V1 must fail closed for production completeness")
    if cp.get("heavy_compute_authorized") is not False:
        raise ValueError("N350 V1 must not authorize heavy compute")
    if contract["firewalls"].get("n341_picard64_sat_is_full_production_leaf") is not False:
        raise ValueError("Picard64 SAT firewall regression")

    verify_source_locks(contract)

    base = {
        "schema": contract["production_certificate"]["schema"],
        "contract_canonical_sha256": EXPECTED_CONTRACT_CANONICAL,
        "producer_registry_canonical_sha256": csha(contract["producer_registry"]),
        "coverage_blocks": [],
        "unknown_count": 0,
        "verdict": "CONTRACT_ONLY_NOT_COMPLETE",
    }
    validate_production_certificate(contract, base)

    fake_complete = dict(base, verdict=contract["production_certificate"]["complete_verdict"])
    expect_reject(contract, fake_complete)

    fake_digest_only = dict(base)
    fake_digest_only["coverage_blocks"] = [{
        "row_id": "g1-d008", "d": 8, "e": 4,
        "filtered_rank_lo": 0, "filtered_rank_hi": 1,
        "old_rank_intervals": [[0, 1]],
        "disposition": "EXACT_PRUNED",
        "producer_id": "UNREGISTERED",
        "producer_contract_sha256": "0" * 64,
        "producer_evidence_sha256": "1" * 64,
        "unknown_count": 0,
    }]
    expect_reject(contract, fake_digest_only)

    picard64_only = json.loads(json.dumps(fake_digest_only))
    picard64_only["coverage_blocks"][0]["disposition"] = "PICARD64_SAT"
    expect_reject(contract, picard64_only)

    unresolved = dict(base, unknown_count=1)
    expect_reject(contract, unresolved)

    out = {
        "schema": "STAGE32_32_01_178_N350_CONTRACT_VERIFICATION_V1",
        "verdict": "PASS_N350_FAIL_CLOSED_PRODUCTION_LEAF_META_CONTRACT",
        "contract_canonical_sha256": EXPECTED_CONTRACT_CANONICAL,
        "producer_registry_canonical_sha256": csha(contract["producer_registry"]),
        "registered_producer_count": 0,
        "hostile_fixture_count": 4,
        "production_complete_available": False,
        "n104_old_domain_release_available": False,
        "full178_complete": False,
        "heavy_compute_authorized": False,
        "theorem_credit": False,
        "merge_authorized": False,
    }
    print(json.dumps({**out, "canonical_sha256_without_this_field": csha(out)}, sort_keys=True))


if __name__ == "__main__":
    main()
