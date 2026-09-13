#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RECEIPT = HERE / "CERTLIFT-03-V22-CONSUMPTION-ADAPTER-RECEIPT.json"
ADAPTER = HERE / "certlift03_v22_consumption_adapter.py"

RECEIPT_BLOB = "4aebf10fe9381314859d87fa2395a4d0e48cb579"
RECEIPT_CANONICAL = "983042fb058d60b9c2ab39ee24c7192d93fec92ab6c9b81c840c91903133c858"
ADAPTER_BLOB = "327aa601acad47bc1e486cccbbac3d3dee7c2681"
ADAPTER_CANONICAL = "597fe83b10c7a23f1da9748423ea3f70a78d448991a253777b64cab554c7ffaf"
TARGET_BLOCKS = 1677
OVERLAP_UNION = 308
INCREMENTAL_BLOCKS = 1369
INCREMENTAL_TERMINALS = 154697
AUTHORITY_BEFORE = 47589703313957134804198
CANDIDATE_AFTER = 47589703313957134649501


def req(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    req(git_blob(RECEIPT) == RECEIPT_BLOB, "V22 receipt blob drift")
    receipt = json.loads(RECEIPT.read_text(encoding="utf-8"))
    stored = receipt.get("canonical_sha256_without_this_field")
    req(stored == RECEIPT_CANONICAL, "V22 receipt stored canonical drift")
    body = dict(receipt)
    body.pop("canonical_sha256_without_this_field", None)
    req(csha(body) == RECEIPT_CANONICAL, "V22 receipt canonical replay drift")
    req(git_blob(ADAPTER) == ADAPTER_BLOB, "V22 adapter blob drift")

    mod = load_module(ADAPTER, "s32_certlift03_v22_receipt_replay")
    live = mod.run()
    req(live["status"] == "PASS_EXACT_HOSTILE_AUDITED_V22_CONSUMPTION_ADAPTER_CANDIDATE", "V22 live adapter verdict drift")
    req(live["canonical"] == ADAPTER_CANONICAL, "V22 live adapter canonical drift")

    req(receipt["adapter_canonical_sha256"] == ADAPTER_CANONICAL, "V22 receipt adapter canonical drift")
    req(receipt["population"]["target_blocks"] == TARGET_BLOCKS, "V22 target count drift")
    req(receipt["prior_authority_overlap"]["union_blocks"] == OVERLAP_UNION, "V22 overlap union drift")
    req(receipt["candidate_increment"]["incremental_blocks"] == INCREMENTAL_BLOCKS, "V22 incremental block drift")
    req(receipt["candidate_increment"]["incremental_terminals"] == INCREMENTAL_TERMINALS, "V22 incremental terminal drift")
    req(receipt["candidate_increment"]["authoritative_remaining_terminals_before"] == AUTHORITY_BEFORE, "V22 authority-before drift")
    req(receipt["candidate_increment"]["candidate_remaining_terminals_if_later_consumed"] == CANDIDATE_AFTER, "V22 candidate-after drift")

    req(live["population"]["symbolic_target_blocks_before_v22_consumption_subtraction"] == TARGET_BLOCKS, "V22 live target count drift")
    req(live["prior_authority_overlap"]["union_blocks"] == OVERLAP_UNION, "V22 live overlap union drift")
    req(live["candidate_increment"]["incremental_blocks"] == INCREMENTAL_BLOCKS, "V22 live incremental block drift")
    req(live["candidate_increment"]["incremental_terminals"] == INCREMENTAL_TERMINALS, "V22 live incremental terminal drift")
    req(live["candidate_increment"]["candidate_remaining_terminals_if_later_consumed"] == CANDIDATE_AFTER, "V22 live candidate-after drift")

    for value in receipt["firewall"].values():
        req(value is False, "V22 receipt credit firewall opened")
    req(live["firewall"]["main_authority_mutated"] is False, "V22 live authority mutation firewall opened")
    req(live["firewall"]["main_pruning_credit"] is False, "V22 live MAIN credit firewall opened")
    req(live["firewall"]["merge_authorized"] is False, "V22 live merge firewall opened")

    print(json.dumps({
        "status": "PASS_CERTLIFT03_V22_CONSUMPTION_ADAPTER_RECEIPT_REPLAY",
        "adapter_canonical": ADAPTER_CANONICAL,
        "target_blocks": TARGET_BLOCKS,
        "prior_overlap_union_blocks": OVERLAP_UNION,
        "incremental_blocks": INCREMENTAL_BLOCKS,
        "incremental_terminals": INCREMENTAL_TERMINALS,
        "candidate_remaining": CANDIDATE_AFTER,
        "adapter_hostile_audited": False,
        "main_credit": False,
        "merge_authorized": False
    }, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
