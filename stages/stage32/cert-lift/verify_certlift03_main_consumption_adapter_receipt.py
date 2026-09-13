#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "CERTLIFT-03-MAIN-CONSUMPTION-ADAPTER-RECEIPT.json"
ADAPTER = HERE / "certlift03_main_consumption_adapter.py"

EXPECTED_RECEIPT_BLOB = "994d518394e39e857adaace8cb79989f44a87301"
EXPECTED_RECEIPT_CANONICAL = "f21181472a589efd39f1fe15ccbdec8062e6af2e993946fcdf571da30e68a59d"
EXPECTED_ADAPTER_BLOB = "97ece748a7cd30bd718ea87a64405ab592548aa9"
EXPECTED_ADAPTER_CANONICAL = "ba5079e4370db0467a40c80646bce90fae5e907993a3614c928fae1a73cb5ebb"
EXPECTED_REVIEW = 5188640528
EXPECTED_TARGETS = 1677
EXPECTED_INCREMENTAL_BLOCKS = 1615
EXPECTED_INCREMENTAL_TERMINALS = 182495
EXPECTED_PRIOR_UNION = 62


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise RuntimeError(msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(obj: object) -> str:
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def main() -> None:
    req(git_blob(RECEIPT) == EXPECTED_RECEIPT_BLOB, "receipt blob drift")
    req(git_blob(ADAPTER) == EXPECTED_ADAPTER_BLOB, "adapter blob drift")
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    claimed = receipt.get("canonical_sha256_without_this_field")
    body = dict(receipt)
    body.pop("canonical_sha256_without_this_field", None)
    req(claimed == EXPECTED_RECEIPT_CANONICAL, "receipt claimed canonical drift")
    req(csha(body) == EXPECTED_RECEIPT_CANONICAL, "receipt canonical replay drift")
    req(receipt.get("status") == "PASS_EXACT_CURRENT_MAIN_CONSUMPTION_ADAPTER_CANDIDATE_PENDING_HOSTILE_AUDIT", "receipt status drift")
    req(receipt["source_locks"]["certlift_hostile_audit_review_id"] == EXPECTED_REVIEW, "symbolic hostile-audit review drift")
    req(receipt["adapter_canonical_sha256"] == EXPECTED_ADAPTER_CANONICAL, "adapter canonical receipt drift")
    req(receipt["population"]["symbolic_target_blocks_before_prior_consumption"] == EXPECTED_TARGETS, "target count drift")
    req(receipt["prior_authority_overlap"]["union_blocks"] == EXPECTED_PRIOR_UNION, "prior overlap union drift")
    req(receipt["prior_authority_overlap"]["double_charge"] is False, "double-charge firewall drift")
    req(receipt["candidate_increment"]["incremental_blocks"] == EXPECTED_INCREMENTAL_BLOCKS, "incremental block count drift")
    req(receipt["candidate_increment"]["incremental_terminals"] == EXPECTED_INCREMENTAL_TERMINALS, "incremental terminal count drift")
    req(receipt["credit"]["adapter_hostile_audited"] is False, "adapter audit firewall drift")
    req(receipt["credit"]["main_pruning"] is False, "MAIN credit firewall drift")
    req(receipt["credit"]["main_authority_mutated"] is False, "MAIN authority mutation firewall drift")
    req(receipt["credit"]["merge_authorized"] is False, "merge firewall drift")

    import certlift03_main_consumption_adapter as adapter
    live = adapter.run()
    req(live["canonical_sha256_without_this_field"] == EXPECTED_ADAPTER_CANONICAL, "adapter replay canonical drift")
    req(live["population"]["symbolic_target_blocks_before_prior_consumption"] == EXPECTED_TARGETS, "adapter replay target drift")
    req(live["prior_authority_overlap"]["union_blocks"] == EXPECTED_PRIOR_UNION, "adapter replay prior-overlap drift")
    req(live["candidate_increment"]["incremental_blocks"] == EXPECTED_INCREMENTAL_BLOCKS, "adapter replay block drift")
    req(live["candidate_increment"]["incremental_terminals"] == EXPECTED_INCREMENTAL_TERMINALS, "adapter replay terminal drift")
    req(live["firewall"]["main_pruning_credit"] is False, "adapter replay MAIN credit firewall drift")

    print(json.dumps({
        "status": "PASS_CERTLIFT03_MAIN_CONSUMPTION_ADAPTER_RECEIPT_REPLAY",
        "adapter_canonical": EXPECTED_ADAPTER_CANONICAL,
        "target_blocks": EXPECTED_TARGETS,
        "prior_overlap_union_blocks": EXPECTED_PRIOR_UNION,
        "incremental_blocks": EXPECTED_INCREMENTAL_BLOCKS,
        "incremental_terminals": EXPECTED_INCREMENTAL_TERMINALS,
        "adapter_hostile_audited": False,
        "main_credit": False,
        "merge_authorized": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
