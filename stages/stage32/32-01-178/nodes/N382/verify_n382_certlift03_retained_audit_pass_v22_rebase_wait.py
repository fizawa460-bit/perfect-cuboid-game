#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

EXPECTED_N381_BLOB = "9da9b6e4488bb127bf43ac6c1fed9567ee14d2c2"
EXPECTED_N381_CANONICAL = "e9c8efa33cce2251fe0ac6f35b9b1664af74fe46ccc2fde32ff5cf394030a276"
EXPECTED_N382_CANONICAL = "f5b6b08264c1743df1d633bad47c9cb435ba569da3eff2ce808053cfb36eec1d"
EXPECTED_AUDIT_PASS_BLOB = "6ea2f6cf8e10adab4acf49e70da3dd892e817cf7"
EXPECTED_V15_MAIN_BLOB = "73cc6ef56647a4be9119e89bf42c8ba4d96d54c9"
EXPECTED_V22_MAIN_BLOB = "80fb35c79854bfdf775dc5b94c331f5f8a535ced"


def req(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def load(path: Path) -> dict:
    return json.loads(path.read_text())


def canonical(obj: dict) -> str:
    x = dict(obj)
    x.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def check_blob(path: Path, expected: str, label: str) -> None:
    req(path.is_file(), f"missing {label}: {path}")
    req(git_blob_sha1(path) == expected, f"{label} blob drift")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--certlift-root", required=True)
    ap.add_argument("--source-main-v15-root", required=True)
    ap.add_argument("--current-main-v22-root", required=True)
    args = ap.parse_args()

    cert = Path(args.certlift_root)
    v15 = Path(args.source_main_v15_root)
    v22 = Path(args.current_main_v22_root)

    n381_path = HERE.parent / "N381" / "STATE.json"
    n382_path = HERE / "STATE.json"
    check_blob(n381_path, EXPECTED_N381_BLOB, "N381 state")
    n381 = load(n381_path)
    req(canonical(n381) == EXPECTED_N381_CANONICAL, "N381 canonical drift")

    n382 = load(n382_path)
    req(canonical(n382) == EXPECTED_N382_CANONICAL, "N382 canonical drift")
    req(n382["canonical_sha256_without_this_field"] == EXPECTED_N382_CANONICAL, "N382 retained canonical mismatch")
    req(n382["status"] == "CERTLIFT03_ADAPTER_HOSTILE_AUDIT_PASS_RETAINED_V15_COUNT_VALID_V22_REBASE_REQUIRED_NO_CREDIT", "N382 status drift")

    audit_path = cert / "stages/stage32/cert-lift/CERTLIFT-03-MAIN-CONSUMPTION-ADAPTER-HOSTILE-AUDIT-PASS.json"
    check_blob(audit_path, EXPECTED_AUDIT_PASS_BLOB, "adapter audit pass")
    audit = load(audit_path)
    req(audit["status"] == "HOSTILE_AUDIT_PASS", "adapter audit status drift")
    req(audit["review_id"] == 5188753236, "adapter audit review drift")
    req(audit["reviewed_pr_head"] == "7c3a9c301d9e1d98678fcd1532afce62c44d56e0", "adapter reviewed head drift")
    req(audit["adapter_evidence_exact_head"] == "9215d4f365ee6400c7de9ba169fe670ddde1d067", "adapter evidence head drift")
    req(audit["adapter_blob_sha1"] == "97ece748a7cd30bd718ea87a64405ab592548aa9", "adapter blob drift")
    req(audit["adapter_canonical_sha256"] == "ba5079e4370db0467a40c80646bce90fae5e907993a3614c928fae1a73cb5ebb", "adapter canonical drift")
    req(audit["candidate_receipt"]["blob_sha1"] == "994d518394e39e857adaace8cb79989f44a87301", "adapter receipt blob drift")
    req(audit["audited_scope"]["authority_snapshot_exact_head"] == "4c51b4ea90a84f9a22a90f194c6d8ecadd9f0d1c", "audited V15 authority drift")
    req(audit["audited_scope"]["incremental_blocks"] == 1615, "audited increment block drift")
    req(audit["audited_scope"]["incremental_terminals"] == 182495, "audited increment terminal drift")
    req(audit["credit_firewall"]["main_pruning"] is False, "audit pass improperly grants MAIN credit")
    req(audit["credit_firewall"]["main_authority_mutated"] is False, "audit pass improperly mutates MAIN")

    v15_path = v15 / "stages/stage32/MAIN-STATE.json"
    v22_path = v22 / "stages/stage32/MAIN-STATE.json"
    check_blob(v15_path, EXPECTED_V15_MAIN_BLOB, "V15 MAIN state")
    check_blob(v22_path, EXPECTED_V22_MAIN_BLOB, "V22 MAIN state")
    m15 = load(v15_path)
    m22 = load(v22_path)

    req(m15["schema"] == "STAGE32_MAIN_COMPACT_STATE_V15_CUT195_AUDITED_CONSUMED", "V15 schema drift")
    req(m15["canonical_sha256_without_this_field"] == "d61dd73ecf0c0fa6fc1a96ea37f284dac4d5beb65c88bff59d5cc25b87939193", "V15 canonical drift")
    req(m15["current_exact_frontier"]["authoritative_remaining_terminals"] == 47598978285064933757427, "V15 authority drift")

    req(m22["schema"] == "STAGE32_MAIN_COMPACT_STATE_V22_BATCH_CUT193_CUT197_CUT198_CONSUMED", "V22 schema drift")
    req(m22["canonical_sha256_without_this_field"] == "82ca200d81b0ce844b1756dc0c3205eec388a20cae312af5e0f3c55d959d491c", "V22 canonical drift")
    req(m22["current_exact_frontier"]["authoritative_remaining_terminals"] == 47589703313957134804198, "V22 authority drift")
    req(m22["current_exact_frontier"]["authoritative_remaining_strata"] == 17128, "V22 strata drift")
    req(m22["current_exact_frontier"]["full178_numerical_census_complete"] is False, "V22 FULL178 unexpectedly complete")
    for key in ("cut196_main_pruning_credit", "cut193_main_pruning_credit", "cut197_main_pruning_credit", "cut198_main_pruning_credit", "n358_main_pruning_credit"):
        req(m22["current_exact_frontier"][key] is True, f"V22 consumed-set drift: {key}")

    rb = n382["rebase_contract"]
    req(n382["producer"]["adapter_audit_pass"]["review_id"] == 5188753236, "N382 audit review id drift")
    req(n382["producer"]["retained_audit_pass_head"] == "7304511aff6f59f406d610cd48cc02d7c25fb2bb", "N382 retained audit head drift")
    req(n382["audited_v15_adapter_result"]["audited_scope_is_v15_only"] is True, "V15 scope firewall lost")
    req(n382["current_hostile_audited_main"]["exact_head"] == "f8039b4ce479a4b91f2f0547e7049f629e9be5f5", "N382 V22 source lock drift")
    req(n382["current_hostile_audited_main"]["v15_minus_v22_authority_terminals"] == 47598978285064933757427 - 47589703313957134804198, "V15/V22 delta drift")
    req(rb["required"] is True, "V22 rebase requirement lost")
    req(rb["must_recompute_predicate_on_v22_current_population"] is True, "V22 predicate recomputation gate lost")
    req(rb["must_subtract_exact_block_sets_for_all_post_v15_consumption"] is True, "post-V15 overlap gate lost")
    req(rb["must_prove_union_overlap_and_no_double_charge"] is True, "double-charge gate lost")
    req(rb["must_hostile_audit_replacement_adapter"] is True, "replacement adapter audit gate lost")
    req(rb["v15_incremental_terminals_may_not_be_subtracted_from_v22"] is True, "stale subtraction firewall lost")
    req(rb["v22_incremental_blocks"] is None and rb["v22_incremental_terminals"] is None, "V22 increment invented")

    req(n382["n101_contract"]["remains_stopped"] is True, "N101 stop lost")
    req(not any(n382["credit"].values()), "N382 credit firewall regression")
    req(not any(n382["anti_loop"].values()), "N382 anti-loop regression")

    print(json.dumps({
        "adapter_audit_pass_retained": True,
        "adapter_audit_review_id": 5188753236,
        "audited_v15_incremental_blocks": 1615,
        "audited_v15_incremental_terminals": 182495,
        "current_audited_main_version": "V22",
        "current_audited_main_terminals": 47589703313957134804198,
        "full178_complete": False,
        "main_pruning_credit": False,
        "n101_reopened_credit": False,
        "next_gate": n382["next_gate"],
        "v22_rebase_required": True,
        "verdict": "PASS_N382_CERTLIFT03_RETAINED_ADAPTER_AUDIT_PASS_V22_REBASE_WAIT_BOUNDARY"
    }, sort_keys=True))


if __name__ == "__main__":
    main()
