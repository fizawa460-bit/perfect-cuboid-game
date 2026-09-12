#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages/stage32/MAIN-STATE.json"
RECEIPT = ROOT / "stages/stage32/management/post-cut195-current-v14-composition-consumption-20260912.json"

AUDITED_MAIN_V14_HEAD = "da1cdd5391ff7f298979ffacbb37e6f3823ba93f"
AUDITED_MAIN_V14_REVIEW = 5185805886
AUDITED_MAIN_V14_STATE_BLOB = "7f4cdb067959b3ed561013ec195bd3b6f4993baf"
AUDITED_MAIN_V14_STATE_CANONICAL = "81e430b60e184488f3cf07ad7b5b11c083aa4af909a3b87073d03ea95937ce41"
AUDITED_V14_VERIFIER_BLOB = "8c6821721237441c0a12750701ca0ae076578e08"

AUDITED_CUT195_HEAD = "2618f4dcd546d569b212753ac7abc10e07ee5828"
AUDITED_CUT195_REVIEW = 5184909672
CUT195_RESULT_BLOB = "d9fe913dccd41446780dbdde9f0200970ee9129e"
CUT195_RESULT_CANONICAL = "1a7d802f427761d304ee06451d00ea67a1365d7d2629cdbf2ac88b6b4ff08aed"
CUT195_VERIFIER_BLOB = "022a8733eae7763926848b5e8bcf7f54f69bee66"
CUT195_INCREMENT = 26216

AUDITED_COMPOSITION_HEAD = "0bdc3b952b35ea3201d8619f21a3df7a3015ff85"
AUDITED_N357_HEAD = "0d787839b7e0dad4a42108c61d16e7849c50862f"
INNER_COMPOSITION_VERIFIER_BLOB = "fdca9ad629983d8c31c7e6355540af3545910120"

STATE_BLOB = "73cc6ef56647a4be9119e89bf42c8ba4d96d54c9"
STATE_CANONICAL = "d61dd73ecf0c0fa6fc1a96ea37f284dac4d5beb65c88bff59d5cc25b87939193"
RECEIPT_BLOB = "148ea573bb1f618baac33c0d1f8cc91678fbbca2"
RECEIPT_CANONICAL = "e33fb30bef69ce3ef87f095b500ecd4a8a21b155a3d9c957836ed17c82ad6be9"

PRE = 47598978285064933783643
POST = 47598978285064933757427
STRATA = 17128

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit(f"FAIL: {msg}")

def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canonical(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()

def load(path: Path) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(isinstance(obj, dict), f"expected object: {path}")
    return obj

def exact_head(path: Path) -> str:
    return subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True).strip()

def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def stream_sha(values: list[int]) -> str:
    h = hashlib.sha256()
    for value in values:
        h.update(f"{value}\n".encode())
    return h.hexdigest()

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--audited-main-v14-root", type=Path, required=True)
    ap.add_argument("--audited-cut195-root", type=Path, required=True)
    ap.add_argument("--audited-composition-root", type=Path, required=True)
    ap.add_argument("--audited-n357-root", type=Path, required=True)
    args = ap.parse_args()

    v14_root = args.audited_main_v14_root.resolve()
    cut_root = args.audited_cut195_root.resolve()
    comp_root = args.audited_composition_root.resolve()
    n357_root = args.audited_n357_root.resolve()

    req(exact_head(v14_root) == AUDITED_MAIN_V14_HEAD, "audited MAIN V14 exact head drift")
    req(exact_head(cut_root) == AUDITED_CUT195_HEAD, "audited CUT195 exact head drift")
    req(exact_head(comp_root) == AUDITED_COMPOSITION_HEAD, "audited N357 composition exact head drift")
    req(exact_head(n357_root) == AUDITED_N357_HEAD, "audited N357 exact head drift")

    v14_state_path = v14_root / "stages/stage32/MAIN-STATE.json"
    v14_verifier = v14_root / "stages/stage32/verify_main_startup_authority_v14.py"
    v14_consumption = v14_root / "stages/stage32/verify_n357_main_consumption_v14.py"
    req(git_blob(v14_state_path) == AUDITED_MAIN_V14_STATE_BLOB, "audited V14 MAIN state blob drift")
    req(git_blob(v14_verifier) == AUDITED_V14_VERIFIER_BLOB, "audited V14 startup verifier blob drift")
    v14_state = load(v14_state_path)
    req(v14_state["canonical_sha256_without_this_field"] == AUDITED_MAIN_V14_STATE_CANONICAL,
        "audited V14 MAIN state stored canonical drift")
    req(canonical(v14_state) == AUDITED_MAIN_V14_STATE_CANONICAL,
        "audited V14 MAIN state canonical drift")
    req(v14_state["authority_sync"]["n357_post_sync_reaudit_status"] == "PENDING",
        "audited V14 boundary was not the pre-re-audit state")

    # Re-run the exact V14 fail-closed N357 consumption replay from the audited V14 tree.
    proc = subprocess.run(
        [
            sys.executable, str(v14_consumption),
            "--audited-composition-root", str(comp_root),
            "--audited-n357-root", str(n357_root),
        ],
        cwd=v14_root,
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        sys.stderr.write(proc.stdout)
        sys.stderr.write(proc.stderr)
        raise SystemExit("FAIL: audited V14 N357 consumption boundary no longer replays")
    req("PASS_N357_MAIN_CONSUMPTION_V14_FAIL_CLOSED" in proc.stdout,
        "audited V14 replay verdict missing")

    cut_result_path = cut_root / "stages/stage32/full178-cut/CUT195-e8-common-adapter-wave3-result.json"
    cut_verifier_path = cut_root / "stages/stage32/full178-cut/verify_cut195_e8_common_adapter_wave3.py"
    req(git_blob(cut_result_path) == CUT195_RESULT_BLOB, "CUT195 result blob drift")
    req(git_blob(cut_verifier_path) == CUT195_VERIFIER_BLOB, "CUT195 audited verifier blob drift")
    cut = load(cut_result_path)
    req(cut["canonical_sha256_without_this_field"] == CUT195_RESULT_CANONICAL,
        "CUT195 result stored canonical drift")
    req(canonical(cut) == CUT195_RESULT_CANONICAL, "CUT195 result canonical drift")
    req(cut["source"]["main_v12_exact_head"] == "6d63d798adb50dd4efc5f0d5abc553b3dfa23060",
        "CUT195 source MAIN V12 drift")
    req(cut["target"]["survivor_offset_range"] == [511, 765], "CUT195 offset range drift")
    req(cut["target"]["block_count"] == 255, "CUT195 target block count drift")
    req(cut["target"]["terminal_count"] == 28815, "CUT195 target terminal count drift")
    req(cut["target"]["cut191_block0_disjoint"] is True, "CUT195/CUT191 disjointness lost")
    req(cut["target"]["cut193_wave1_disjoint"] is True, "CUT195/CUT193 disjointness lost")
    req(cut["target"]["cut194_wave2_disjoint"] is True, "CUT195/CUT194 disjointness lost")
    req(cut["result"]["candidate_closed_block_count"] == 232, "CUT195 closed count drift")
    req(cut["result"]["candidate_pruned_terminals"] == CUT195_INCREMENT, "CUT195 pruning count drift")
    req(cut["result"]["remaining_nonclosed_block_count"] == 23, "CUT195 residual count drift")
    req(cut["result"]["candidate_closed_block_stream_sha256"] ==
        "fbcca36528528b16c9082e72602e897c7de6ca6693caac90133ae779b0d1264a",
        "CUT195 closed stream drift")

    # Reconstruct the exact current g1-d008/e8 prefix from the hostile-audited
    # N357 composition boundary and prove the CUT195 target is exactly offsets
    # 511..765 of that same population. Then replay N357 on every target block.
    inner_path = comp_root / "stages/stage32/verify_n357_v13_current_authority_composition.py"
    req(git_blob(inner_path) == INNER_COMPOSITION_VERIFIER_BLOB,
        "audited N357 composition verifier blob drift")
    inner = load_module(inner_path, "s32_n357_v13_composition_for_cut195")
    residual = comp_root / "stages/stage32/residual-32-01-production"
    sys.path.insert(0, str(residual))
    from compressed_terminal_indexer import CompressedTerminalIndexer

    idx = CompressedTerminalIndexer(8, 8)
    req(idx.normal_budget + 1 == 113, "e=8 block width drift")
    survivors: list[int] = []
    for block_index in range(idx.exceptional_count):
        base = tuple(int(v) for v in idx.unrank(block_index * 113))
        if inner.prefix_survives(base):
            survivors.append(block_index)
    req(len(survivors) == 7596, "current e8 prefix block count drift")
    req(stream_sha(survivors) ==
        "529b9c31d36c517484dc176ba1d37674790eec05dc01853f9ce93b36e416c8e3",
        "current e8 prefix stream drift")

    expected_wave = survivors[511:766]
    target = [int(v) for v in cut["target"]["block_indices"]]
    req(target == expected_wave, "CUT195 target is not exact current-prefix offsets 511..765")
    req(stream_sha(target) == cut["target"]["block_index_stream_sha256"],
        "CUT195 target block stream replay drift")
    rejecting = [
        block_index for block_index in target
        if not inner.n357_accepts(tuple(int(v) for v in idx.unrank(block_index * 113)))
    ]
    req(rejecting == [], f"N357 overlaps CUT195 target blocks: {rejecting[:8]}")

    closed = [int(v) for v in cut["result"]["candidate_closed_block_indices"]]
    req(len(closed) == 232 and len(set(closed)) == 232, "CUT195 closed-set uniqueness drift")
    req(set(closed).issubset(set(target)), "CUT195 credited set escapes target population")
    req(stream_sha(closed) == cut["result"]["candidate_closed_block_stream_sha256"],
        "CUT195 credited block stream replay drift")
    req(CUT195_INCREMENT == len(closed) * 113, "CUT195 terminal arithmetic drift")
    req(PRE - CUT195_INCREMENT == POST, "CUT195 MAIN consumption arithmetic drift")

    req(git_blob(STATE) == STATE_BLOB, "current V15 MAIN state blob drift")
    state = load(STATE)
    req(state["canonical_sha256_without_this_field"] == STATE_CANONICAL,
        "current V15 MAIN state stored canonical drift")
    req(canonical(state) == STATE_CANONICAL, "current V15 MAIN state canonical drift")
    req(git_blob(RECEIPT) == RECEIPT_BLOB, "CUT195 MAIN consumption receipt blob drift")
    receipt = load(RECEIPT)
    req(receipt["canonical_sha256_without_this_field"] == RECEIPT_CANONICAL,
        "CUT195 receipt stored canonical drift")
    req(canonical(receipt) == RECEIPT_CANONICAL, "CUT195 receipt canonical drift")

    auth = state["authority_sync"]
    req(auth["n357_post_sync_reaudit_status"] == "PASS", "N357 replacement-head re-audit not consumed")
    req(auth["n357_post_sync_reaudit_review_id"] == AUDITED_MAIN_V14_REVIEW,
        "N357 replacement-head re-audit review drift")
    req(auth["n357_post_sync_reaudit_exact_head"] == AUDITED_MAIN_V14_HEAD,
        "N357 replacement-head audited head drift")
    req(auth["cut195_candidate_hostile_audit_status"] == "PASS", "CUT195 hostile audit not retained")
    req(auth["cut195_candidate_hostile_audit_review_id"] == AUDITED_CUT195_REVIEW,
        "CUT195 hostile audit review drift")
    req(auth["cut195_current_v14_composition_replayed"] is True,
        "CUT195 current-V14 composition replay not retained")
    req(auth["cut195_current_v14_overlap_n357_terminals"] == 0,
        "CUT195/N357 overlap not zero")
    req(auth["cut195_main_pruning_credit_consumed"] is True,
        "CUT195 MAIN credit not consumed")
    req(auth["cut195_post_sync_reaudit_status"] == "PENDING",
        "V15 replacement head self-awarded audit")

    frontier = state["current_exact_frontier"]
    req(frontier["authoritative_remaining_strata"] == STRATA, "V15 strata drift")
    req(frontier["authoritative_remaining_terminals"] == POST, "V15 terminal authority drift")
    req(frontier["cut195_incremental_rejected_terminals"] == CUT195_INCREMENT,
        "V15 CUT195 increment drift")
    req(frontier["cut195_main_pruning_credit"] is True, "V15 CUT195 credit missing")
    req(frontier["cut195_synchronized_head_hostile_audited"] is False,
        "V15 synchronized head self-awarded audit")
    req(frontier["full178_numerical_census_complete"] is False, "FULL178 closed unexpectedly")
    req(frontier["stage32_closed"] is False, "Stage32 closed unexpectedly")

    rr = receipt["current_v14_composition_replay"]
    req(rr["cut195_target_equals_current_prefix_offsets_511_765"] is True,
        "receipt population identity drift")
    req(rr["n357_rejecting_cut195_target_blocks"] == 0, "receipt N357 block overlap drift")
    req(rr["n357_rejecting_cut195_target_terminals"] == 0, "receipt N357 terminal overlap drift")
    req(rr["double_charge"] is False, "receipt double-charge firewall drift")
    ra = receipt["authority"]
    req(ra["before_remaining_terminals"] == PRE, "receipt pre-authority drift")
    req(ra["incremental_rejected_terminals"] == CUT195_INCREMENT, "receipt increment drift")
    req(ra["after_remaining_terminals"] == POST, "receipt post-authority drift")
    req(ra["cut195_main_pruning_credit"] is True, "receipt CUT195 credit missing")
    req(ra["cut193_main_pruning_credit"] is False, "CUT193 credit leaked during CUT195 consumption")

    cs = receipt["claim_sync"]
    req(cs["full178_claim_id"] == "S32.FULL178.NUMERICAL_CENSUS.V1", "FULL178 claim id drift")
    req(cs["claim_core_changed"] is False, "FULL178 immutable core mutated by pruning transition")
    req(cs["authority_status_changed"] is False, "FULL178 goal authority improperly upgraded")
    req(cs["frontier_status"] == "ACTIVE_INCOMPLETE", "FULL178 frontier status drift")

    fw = receipt["credit_firewall"]
    req(fw["numerical_pruning_credit_only"] is True, "CUT195 credit widened beyond numerical pruning")
    for key in ("full178_complete", "receiver_credit", "theorem_credit", "effectivity_credit",
                "endpoint_credit", "stage32_closed", "perfect_cuboid_existence_claim",
                "perfect_cuboid_nonexistence_claim", "merge_authorized"):
        req(fw[key] is False, f"forbidden credit enabled: {key}")

    print(json.dumps({
        "verdict": "PASS_CUT195_MAIN_CONSUMPTION_V15_FAIL_CLOSED",
        "audited_main_v14_head": AUDITED_MAIN_V14_HEAD,
        "audited_main_v14_review": AUDITED_MAIN_V14_REVIEW,
        "audited_cut195_head": AUDITED_CUT195_HEAD,
        "audited_cut195_review": AUDITED_CUT195_REVIEW,
        "cut195_incremental_rejected_terminals": CUT195_INCREMENT,
        "cut195_n357_overlap": 0,
        "remaining_strata": STRATA,
        "remaining_terminals": POST,
        "cut193_main_credit": False,
        "full178_complete": False,
        "replacement_head_hostile_reaudit_required": True,
        "merge_authorized": False,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
