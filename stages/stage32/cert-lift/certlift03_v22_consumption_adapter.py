#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent

V15_ADAPTER_AUDIT_RECEIPT = HERE / "CERTLIFT-03-MAIN-CONSUMPTION-ADAPTER-HOSTILE-AUDIT-PASS.json"
V22_SOURCE_RECEIPT = HERE / "CERTLIFT-03-V22-AUTHORITY-SOURCE-RECEIPT.json"

AUDITED_ADAPTER_REVIEW_ID = 5188753236
AUDITED_ADAPTER_REVIEWED_HEAD = "7c3a9c301d9e1d98678fcd1532afce62c44d56e0"
AUDITED_ADAPTER_EVIDENCE_HEAD = "9215d4f365ee6400c7de9ba169fe670ddde1d067"
AUDITED_ADAPTER_BLOB = "97ece748a7cd30bd718ea87a64405ab592548aa9"
AUDITED_ADAPTER_CANONICAL = "ba5079e4370db0467a40c80646bce90fae5e907993a3614c928fae1a73cb5ebb"
AUDITED_ADAPTER_RECEIPT_BLOB = "994d518394e39e857adaace8cb79989f44a87301"
AUDITED_ADAPTER_RECEIPT_CANONICAL = "f21181472a589efd39f1fe15ccbdec8062e6af2e993946fcdf571da30e68a59d"
V15_ADAPTER_AUDIT_RECEIPT_BLOB = "6ea2f6cf8e10adab4acf49e70da3dd892e817cf7"
V15_ADAPTER_AUDIT_RECEIPT_CANONICAL = "b747660bada9c83a4815862b686fa8e5cea7f24e4ea85394040d25ea8d0a81d8"

V22_HEAD = "f8039b4ce479a4b91f2f0547e7049f629e9be5f5"
V22_REVIEW_ID = 5188224290
V22_MAIN_STATE_BLOB = "80fb35c79854bfdf775dc5b94c331f5f8a535ced"
V22_MAIN_STATE_CANONICAL = "82ca200d81b0ce844b1756dc0c3205eec388a20cae312af5e0f3c55d959d491c"
V22_SOURCE_RECEIPT_BLOB = "2ca912e9aafeebfc8962a127887947f5c9ec0b90"
V22_SOURCE_RECEIPT_CANONICAL = "16bba90759c021552a80950d7d0feef00323cd8c6ac47767678b0a65bc2381ce"
V22_AUTHORITY_REMAINING = 47589703313957134804198
V22_AUTHORITY_STRATA = 17128

N357_COMPOSITION_VERIFIER_BLOB = "fdca9ad629983d8c31c7e6355540af3545910120"
N358_RECEIPT_BLOB = "efa87a1b62cc698745f87814cd8f9eb9fe95dbd2"
N358_RECEIPT_CANONICAL = "27c50848e19c242389298b6a23d7c5b6a8ea86afd97c36ced16905adc66a5bdc"

CUT191_BLOB = "a90042ec931cb487ae6be852524db5a4537862f4"
CUT191_CANONICAL = "1e681c456dc30342346d134f5e0d89150573f8a756cbd808c309d2af89821fdd"

CUT_SOURCES = {
    "CUT193": {
        "head": "5b2ebb3f67805eddefef835878ba4b9744bfdbd9",
        "path": "stages/stage32/full178-cut/CUT193-e8-common-adapter-wave1-result.json",
        "blob": "ef72967a97e41287671f25647ad6fc24aef31ccb",
        "canonical": "161abe2cf9a00b95ce2b1acd422008bbb5c72929ea7a72e9892b94546abae2c1",
        "closed": 227,
    },
    "CUT194": {
        "head": "847f3bff0c5e0d0530bfb8db406e955b2d231d9a",
        "path": "stages/stage32/full178-cut/CUT194-e8-common-adapter-wave2-result.json",
        "blob": "dab1a28f55918b617112799f11ac9614eb8a481c",
        "canonical": "c63f6da3dd0ec443572f8561bb7774491ce7d7c09ce319a322fb52e5b1e08cd4",
        "closed": 234,
    },
    "CUT195": {
        "head": "2618f4dcd546d569b212753ac7abc10e07ee5828",
        "path": "stages/stage32/full178-cut/CUT195-e8-common-adapter-wave3-result.json",
        "blob": "d9fe913dccd41446780dbdde9f0200970ee9129e",
        "canonical": "1a7d802f427761d304ee06451d00ea67a1365d7d2629cdbf2ac88b6b4ff08aed",
        "closed": 232,
    },
    "CUT196": {
        "head": "85f4e988acf6446fa0d472208e21990621a650b4",
        "path": "stages/stage32/full178-cut/CUT196-e8-common-adapter-wave4-result.json",
        "blob": "ae23ce6c44f69f9b2abe15e5aff09c2a10c45fde",
        "canonical": "194a37f87355f781f9aca341f9935645d818d5daa1c377883606627c80558a92",
        "closed": 242,
    },
    "CUT197": {
        "head": "adce53dc9004c24bffb3ba9f88e9d5d6e51cf6a5",
        "path": "stages/stage32/full178-cut/CUT197-e8-common-adapter-wave5-result.json",
        "blob": "e98f33ef093003e724ff6574bfec546ab1221955",
        "canonical": "f99d0f051ce95e269658e0ec945d727db32a94687bfd8acde5ee354e00776fa0",
        "closed": 250,
    },
    "CUT198": {
        "head": "16e439bc65e723c9f2658c274d53fb839738dcd2",
        "path": "stages/stage32/full178-cut/CUT198-e8-common-adapter-wave6-result.json",
        "blob": "29a392b20d3f88519f5e8a6f3d2225ec5955bcb2",
        "canonical": "60f2d1d4d926d3f0c527a15fb2978d11dea7ca5dc9d02825c2671fc793618607",
        "closed": 248,
    },
}

CURRENT_PREFIX_BLOCK_COUNT = 7596
CURRENT_PREFIX_STREAM = "529b9c31d36c517484dc176ba1d37674790eec05dc01853f9ce93b36e416c8e3"
EXPECTED_TARGET_BLOCKS = 1677
BLOCK_WIDTH = 113
ASSIGNMENT_ORDER = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
X4_LABEL = 49
G3 = [93, 94, 95, 96]


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


def exact_head(root: Path) -> str:
    return subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()


def load(path: Path) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(isinstance(obj, dict), f"expected object: {path}")
    return obj


def checked_json(path: Path, blob: str, canonical: str) -> dict:
    req(path.is_file(), f"missing source: {path}")
    req(git_blob(path) == blob, f"blob drift: {path}")
    obj = load(path)
    req(obj.get("canonical_sha256_without_this_field") == canonical, f"stored canonical drift: {path}")
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    req(csha(body) == canonical, f"canonical replay drift: {path}")
    return obj


def env_root(name: str) -> Path:
    raw = os.environ.get(name)
    req(bool(raw), f"{name} missing")
    root = Path(raw).resolve()
    req(root.is_dir(), f"{name} is not a directory")
    return root


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def stream_sha(values: list[int]) -> str:
    h = hashlib.sha256()
    for value in values:
        h.update(f"{int(value)}\n".encode())
    return h.hexdigest()


def run() -> dict:
    v22_root = env_root("CERTLIFT_V22_MAIN_ROOT")
    audited_adapter_root = env_root("CERTLIFT_ADAPTER_AUDITED_ROOT")
    req(exact_head(v22_root) == V22_HEAD, "V22 exact head drift")
    req(exact_head(audited_adapter_root) == AUDITED_ADAPTER_REVIEWED_HEAD, "audited adapter reviewed head drift")

    audit_receipt = checked_json(
        V15_ADAPTER_AUDIT_RECEIPT,
        V15_ADAPTER_AUDIT_RECEIPT_BLOB,
        V15_ADAPTER_AUDIT_RECEIPT_CANONICAL,
    )
    req(audit_receipt["status"] == "HOSTILE_AUDIT_PASS", "adapter audit status drift")
    req(audit_receipt["review_id"] == AUDITED_ADAPTER_REVIEW_ID, "adapter audit review drift")
    req(audit_receipt["reviewed_pr_head"] == AUDITED_ADAPTER_REVIEWED_HEAD, "adapter reviewed head receipt drift")
    req(audit_receipt["adapter_evidence_exact_head"] == AUDITED_ADAPTER_EVIDENCE_HEAD, "adapter evidence head receipt drift")

    audited_adapter = audited_adapter_root / "stages/stage32/cert-lift/certlift03_main_consumption_adapter.py"
    req(git_blob(audited_adapter) == AUDITED_ADAPTER_BLOB, "audited adapter blob drift")
    audited_candidate_receipt = checked_json(
        audited_adapter_root / "stages/stage32/cert-lift/CERTLIFT-03-MAIN-CONSUMPTION-ADAPTER-RECEIPT.json",
        AUDITED_ADAPTER_RECEIPT_BLOB,
        AUDITED_ADAPTER_RECEIPT_CANONICAL,
    )
    req(audited_candidate_receipt["adapter_canonical_sha256"] == AUDITED_ADAPTER_CANONICAL, "audited adapter canonical receipt drift")
    req(audited_candidate_receipt["population"]["current_prefix_blocks"] == CURRENT_PREFIX_BLOCK_COUNT, "audited adapter prefix count drift")
    req(audited_candidate_receipt["population"]["symbolic_target_blocks_before_prior_consumption"] == EXPECTED_TARGET_BLOCKS, "audited adapter target count drift")

    source_receipt = checked_json(V22_SOURCE_RECEIPT, V22_SOURCE_RECEIPT_BLOB, V22_SOURCE_RECEIPT_CANONICAL)
    req(source_receipt["hostile_audit_review_id"] == V22_REVIEW_ID, "V22 review id drift")
    req(source_receipt["audited_exact_head"] == V22_HEAD, "V22 source receipt head drift")

    state = checked_json(
        v22_root / "stages/stage32/MAIN-STATE.json",
        V22_MAIN_STATE_BLOB,
        V22_MAIN_STATE_CANONICAL,
    )
    frontier = state["current_exact_frontier"]
    req(frontier["authoritative_remaining_strata"] == V22_AUTHORITY_STRATA, "V22 stratum authority drift")
    req(frontier["authoritative_remaining_terminals"] == V22_AUTHORITY_REMAINING, "V22 terminal authority drift")
    for key in ["cut191_main_pruning_credit", "cut193_main_pruning_credit", "cut194_main_pruning_credit", "cut195_main_pruning_credit", "cut196_main_pruning_credit", "cut197_main_pruning_credit", "cut198_main_pruning_credit", "n358_main_pruning_credit"]:
        req(frontier.get(key) is True, f"V22 credit drift: {key}")
    req(frontier.get("n358_synchronized_head_hostile_audited") is True, "V22 N358 synchronization audit drift")

    n358 = checked_json(
        v22_root / "stages/stage32/management/post-n358-current-v18-composition-consumption-20260912.json",
        N358_RECEIPT_BLOB,
        N358_RECEIPT_CANONICAL,
    )
    zero = n358["current_v18_composition_replay"]["zero_overlap_reason"]
    req(zero["consumed_cut_d"] == 8 and zero["consumed_cut_e"] == 8, "N358 zero-overlap d/e drift")
    req(zero["h"] == 4 and zero["h_minus_5"] == -1, "N358 zero-overlap h drift")
    req(zero["equivalently_n358_incremental_domain_empty_on_g1_d008_e8"] is True, "N358 e8 empty-domain drift")
    req(zero["nonnegative_b_cannot_satisfy_b_le_h_minus_5"] is True, "N358 nonnegative-b contradiction drift")

    n357_path = v22_root / "stages/stage32/verify_n357_v13_current_authority_composition.py"
    req(git_blob(n357_path) == N357_COMPOSITION_VERIFIER_BLOB, "N357 verifier blob drift")
    n357 = load_module(n357_path, "s32_certlift03_v22_n357")

    residual = v22_root / "stages/stage32/residual-32-01-production"
    sys.path.insert(0, str(residual))
    from compressed_terminal_indexer import CompressedTerminalIndexer

    idx = CompressedTerminalIndexer(8, 8)
    req(idx.normal_budget + 1 == BLOCK_WIDTH, "e8 block width drift")
    survivors: list[int] = []
    for block_index in range(idx.exceptional_count):
        base = tuple(int(v) for v in idx.unrank(block_index * BLOCK_WIDTH))
        req(base[4] == 0, "block-base x4 drift")
        if n357.prefix_survives(base):
            survivors.append(block_index)
    req(len(survivors) == CURRENT_PREFIX_BLOCK_COUNT, "V22 current-prefix block count drift")
    req(stream_sha(survivors) == CURRENT_PREFIX_STREAM, "V22 current-prefix block stream drift")

    target: list[int] = []
    n357_rejected: list[int] = []
    for block_index in survivors:
        base = tuple(int(v) for v in idx.unrank(block_index * BLOCK_WIDTH))
        by = {label: int(value) for label, value in zip(ASSIGNMENT_ORDER, base)}
        fixed_mass = sum(value for label, value in by.items() if label != X4_LABEL)
        g3 = sum(by[label] for label in G3)
        if fixed_mass < 7 or g3 != 3:
            continue
        target.append(block_index)
        if not n357.n357_accepts(base):
            n357_rejected.append(block_index)
    req(len(target) == EXPECTED_TARGET_BLOCKS, "V22 symbolic target count drift")
    req(len(n357_rejected) == 0, "V22 symbolic target unexpectedly overlaps N357 rejection")

    cut191 = checked_json(
        v22_root / "stages/stage32/full178-cut/CUT191-first-block-closure-checkpoint.json",
        CUT191_BLOB,
        CUT191_CANONICAL,
    )
    req(cut191["population_preimage"]["first_block_rank_range"] == [0, 112], "CUT191 identity drift")
    cut_sets: dict[str, set[int]] = {"CUT191": {int(survivors[0])}}
    req(cut_sets["CUT191"] == {0}, "CUT191 block identity drift")

    for cut_id, src in CUT_SOURCES.items():
        root = env_root(f"CERTLIFT_{cut_id}_ROOT")
        req(exact_head(root) == src["head"], f"{cut_id} exact head drift")
        result = checked_json(root / src["path"], src["blob"], src["canonical"])
        values = {int(v) for v in result["result"]["candidate_closed_block_indices"]}
        req(len(values) == src["closed"], f"{cut_id} closed-block count drift")
        req(result["result"]["candidate_closed_block_count"] == src["closed"], f"{cut_id} stored closed-block count drift")
        cut_sets[cut_id] = values

    for a, b in combinations(sorted(cut_sets), 2):
        req(not (cut_sets[a] & cut_sets[b]), f"consumed CUT overlap drift: {a}/{b}")

    target_set = set(target)
    overlap_counts = {name.lower() + "_blocks": len(target_set & values) for name, values in cut_sets.items()}
    overlap_counts["n357_blocks"] = 0
    overlap_counts["n358_blocks"] = 0

    already_consumed = set().union(*cut_sets.values())
    prior_union = target_set & already_consumed
    incremental = sorted(target_set - already_consumed)
    req(not (set(incremental) & already_consumed), "V22 incremental set double-charges consumed CUT authority")
    req(len(incremental) + len(prior_union) == len(target), "V22 target partition accounting drift")

    incremental_terminals = len(incremental) * BLOCK_WIDTH
    candidate_remaining = V22_AUTHORITY_REMAINING - incremental_terminals
    req(incremental_terminals >= 0 and candidate_remaining >= 0, "V22 candidate arithmetic invalid")

    out = {
        "schema": "STAGE32_CERTLIFT_03_V22_CONSUMPTION_ADAPTER_V1",
        "stage": "32",
        "node": "CERTLIFT-03-V22-CONSUME",
        "status": "PASS_EXACT_HOSTILE_AUDITED_V22_CONSUMPTION_ADAPTER_CANDIDATE",
        "source_locks": {
            "audited_adapter_review_id": AUDITED_ADAPTER_REVIEW_ID,
            "audited_adapter_reviewed_head": AUDITED_ADAPTER_REVIEWED_HEAD,
            "audited_adapter_evidence_head": AUDITED_ADAPTER_EVIDENCE_HEAD,
            "v22_hostile_audit_review_id": V22_REVIEW_ID,
            "v22_exact_head": V22_HEAD,
            "v22_main_state_blob_sha1": V22_MAIN_STATE_BLOB,
            "v22_main_state_canonical_sha256": V22_MAIN_STATE_CANONICAL,
        },
        "predicate": {
            "d": 8,
            "e": 8,
            "fixed_exceptional_mass_lower_bound": 7,
            "g3_labels": G3,
            "g3_sum": 3,
        },
        "population": {
            "current_prefix_blocks": len(survivors),
            "current_prefix_block_stream_sha256": stream_sha(survivors),
            "symbolic_target_blocks_before_v22_consumption_subtraction": len(target),
            "symbolic_target_block_stream_sha256": stream_sha(target),
            "block_width_terminals": BLOCK_WIDTH,
        },
        "prior_authority_overlap": {
            **overlap_counts,
            "union_blocks": len(prior_union),
            "double_charge": False,
            "n358_overlap_reason": "audited empty incremental domain on g1-d008/e8",
        },
        "candidate_increment": {
            "incremental_blocks": len(incremental),
            "incremental_terminals": incremental_terminals,
            "incremental_block_stream_sha256": stream_sha(incremental),
            "authoritative_remaining_strata_before": V22_AUTHORITY_STRATA,
            "authoritative_remaining_terminals_before": V22_AUTHORITY_REMAINING,
            "candidate_remaining_terminals_if_later_consumed": candidate_remaining,
            "first_incremental_blocks": incremental[:32],
        },
        "firewall": {
            "adapter_is_main_consumption": False,
            "main_authority_mutated": False,
            "main_pruning_credit": False,
            "full178_credit": False,
            "effectivity_credit": False,
            "theorem_credit": False,
            "stage32_closed": False,
            "merge_authorized": False,
            "hostile_audit_required_before_consumption": True,
        },
    }
    out["canonical"] = csha(out)
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-check", action="store_true")
    args = parser.parse_args()
    out = run()
    if args.self_check:
        req(out["status"] == "PASS_EXACT_HOSTILE_AUDITED_V22_CONSUMPTION_ADAPTER_CANDIDATE", "V22 adapter status drift")
        req(out["population"]["symbolic_target_blocks_before_v22_consumption_subtraction"] == EXPECTED_TARGET_BLOCKS, "V22 target self-check drift")
        req(out["prior_authority_overlap"]["double_charge"] is False, "V22 double-charge self-check drift")
        req(out["candidate_increment"]["incremental_blocks"] > 0, "V22 adapter produced empty increment")
        req(out["firewall"]["main_authority_mutated"] is False, "V22 authority mutation firewall drift")
        req(out["firewall"]["main_pruning_credit"] is False, "V22 credit firewall drift")
    print(json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
