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
RECEIPT = ROOT / "stages/stage32/management/post-cut196-current-v16-composition-consumption-20260912.json"

AUDITED_MAIN_V16_HEAD = "bc4463794055b8442814b892fd33204416c2b531"
AUDITED_MAIN_V16_REVIEW = 5186235938
AUDITED_MAIN_V16_STATE_BLOB = "1b46f01070f5bbf1b81ba5c84684dcaa1a459119"
AUDITED_MAIN_V16_STATE_CANONICAL = "cd1865abe9918e1b5a64d2b9148f378a54cc24b203f16295ce256685164d3fd8"
AUDITED_CUT196_HEAD = "85f4e988acf6446fa0d472208e21990621a650b4"
AUDITED_CUT196_REVIEW = 5186302071
CUT196_RESULT_BLOB = "ae23ce6c44f69f9b2abe15e5aff09c2a10c45fde"
CUT196_RESULT_CANONICAL = "194a37f87355f781f9aca341f9935645d818d5daa1c377883606627c80558a92"
CUT196_VERIFIER_BLOB = "1364dc9321edc8b294c19ce43ca89d0be91192ac"
CUT196_INCREMENT = 27346
AUDITED_COMPOSITION_HEAD = "0bdc3b952b35ea3201d8619f21a3df7a3015ff85"
INNER_COMPOSITION_VERIFIER_BLOB = "fdca9ad629983d8c31c7e6355540af3545910120"
STATE_CANONICAL = "a21faa5b3c3f5be259d8c5bc7ffa6f7aac827b911256e7a916e0bf9ea8e85de9"
RECEIPT_CANONICAL = "2c55ddd13f90068fc8383c755dcada07f265c40c6ff468709b0add12a390c0e2"
PRE = 47598978285064933757427
POST = 47598978285064933730081
STRATA = 17128

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canonical(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()

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
    ap.add_argument("--audited-main-v16-root", type=Path, required=True)
    ap.add_argument("--audited-cut196-root", type=Path, required=True)
    ap.add_argument("--audited-n357-composition-root", type=Path, required=True)
    args = ap.parse_args()
    main_root = args.audited_main_v16_root.resolve()
    cut_root = args.audited_cut196_root.resolve()
    comp_root = args.audited_n357_composition_root.resolve()
    req(exact_head(main_root) == AUDITED_MAIN_V16_HEAD, "audited MAIN V16 exact head drift")
    req(exact_head(cut_root) == AUDITED_CUT196_HEAD, "audited CUT196 exact head drift")
    req(exact_head(comp_root) == AUDITED_COMPOSITION_HEAD, "audited N357 composition exact head drift")
    old_state_path = main_root / "stages/stage32/MAIN-STATE.json"
    req(git_blob(old_state_path) == AUDITED_MAIN_V16_STATE_BLOB, "audited V16 MAIN state blob drift")
    old_state = load(old_state_path)
    req(old_state["canonical_sha256_without_this_field"] == AUDITED_MAIN_V16_STATE_CANONICAL, "audited V16 stored canonical drift")
    req(canonical(old_state) == AUDITED_MAIN_V16_STATE_CANONICAL, "audited V16 canonical drift")
    old_frontier = old_state["current_exact_frontier"]
    req(old_frontier["authoritative_remaining_strata"] == STRATA, "V16 strata drift")
    req(old_frontier["authoritative_remaining_terminals"] == PRE, "V16 terminal authority drift")
    req(old_frontier["cut196_main_pruning_credit"] is False, "V16 self-awarded CUT196 credit")
    req(old_frontier["cut196_candidate_exact_head"] == AUDITED_CUT196_HEAD, "V16 selected CUT196 head drift")
    req(old_frontier["cut196_claim_frontier_ci_status"] == "SUCCESS", "V16 CUT196 CI not SUCCESS")
    cut_result_path = cut_root / "stages/stage32/full178-cut/CUT196-e8-common-adapter-wave4-result.json"
    cut_verifier_path = cut_root / "stages/stage32/full178-cut/verify_cut196_e8_common_adapter_wave4.py"
    req(git_blob(cut_result_path) == CUT196_RESULT_BLOB, "CUT196 result blob drift")
    req(git_blob(cut_verifier_path) == CUT196_VERIFIER_BLOB, "CUT196 verifier blob drift")
    cut = load(cut_result_path)
    req(cut["canonical_sha256_without_this_field"] == CUT196_RESULT_CANONICAL, "CUT196 result stored canonical drift")
    req(canonical(cut) == CUT196_RESULT_CANONICAL, "CUT196 result canonical drift")
    req(cut["target"]["survivor_offset_range"] == [766, 1020], "CUT196 offset range drift")
    req(cut["target"]["block_count"] == 255 and cut["target"]["terminal_count"] == 28815, "CUT196 target population drift")
    req(cut["target"]["cut191_block0_disjoint"] is True, "CUT196/CUT191 disjointness lost")
    req(cut["target"]["cut193_wave1_disjoint"] is True, "CUT196/CUT193 disjointness lost")
    req(cut["target"]["cut194_wave2_disjoint"] is True, "CUT196/CUT194 disjointness lost")
    req(cut["target"]["cut195_wave3_disjoint"] is True, "CUT196/CUT195 disjointness lost")
    req(cut["target"]["n356_preserved_all_wave_blocks"] is True, "CUT196 N356 preservation lost")
    req(cut["result"]["candidate_closed_block_count"] == 242, "CUT196 closed count drift")
    req(cut["result"]["candidate_pruned_terminals"] == CUT196_INCREMENT, "CUT196 pruning count drift")
    req(cut["result"]["remaining_nonclosed_block_count"] == 13, "CUT196 residual count drift")
    inner_path = comp_root / "stages/stage32/verify_n357_v13_current_authority_composition.py"
    req(git_blob(inner_path) == INNER_COMPOSITION_VERIFIER_BLOB, "N357 composition verifier blob drift")
    inner = load_module(inner_path, "s32_n357_composition_for_cut196")
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
    req(stream_sha(survivors) == "529b9c31d36c517484dc176ba1d37674790eec05dc01853f9ce93b36e416c8e3", "current e8 prefix stream drift")
    expected_wave = survivors[766:1021]
    target = [int(v) for v in cut["target"]["block_indices"]]
    req(target == expected_wave, "CUT196 target is not exact current-prefix offsets 766..1020")
    req(stream_sha(target) == "93685ab29273b4d23b4da99dba273482489b16d25e142ec84c3bb9736f30756a", "CUT196 target block stream replay drift")
    rejecting = [block_index for block_index in target if not inner.n357_accepts(tuple(int(v) for v in idx.unrank(block_index * 113)))]
    req(rejecting == [], f"N357 overlaps CUT196 target blocks: {rejecting[:8]}")
    closed = [int(v) for v in cut["result"]["candidate_closed_block_indices"]]
    req(len(closed) == 242 and len(set(closed)) == 242, "CUT196 closed-set uniqueness drift")
    req(set(closed).issubset(set(target)), "CUT196 credited set escapes target population")
    req(stream_sha(closed) == "d1f31fc45f13d7d6aa20b00f952cc55e197e582a25901b54c084bf0ab8112984", "CUT196 credited block stream replay drift")
    req(CUT196_INCREMENT == len(closed) * 113, "CUT196 terminal arithmetic drift")
    req(PRE - CUT196_INCREMENT == POST, "CUT196 MAIN consumption arithmetic drift")
    state = load(STATE)
    req(state["canonical_sha256_without_this_field"] == STATE_CANONICAL, "V17 stored canonical drift")
    req(canonical(state) == STATE_CANONICAL, "V17 canonical drift")
    frontier = state["current_exact_frontier"]
    req(frontier["authoritative_remaining_terminals"] == POST, "V17 terminal authority drift")
    req(frontier["cut196_main_pruning_credit"] is True, "V17 CUT196 credit missing")
    req(frontier["cut196_current_v16_overlap_n357_terminals"] == 0, "V17 CUT196/N357 overlap drift")
    req(frontier["cut196_synchronized_head_hostile_audited"] is False, "V17 replacement head self-awarded audit")
    receipt = load(RECEIPT)
    req(receipt["canonical_sha256_without_this_field"] == RECEIPT_CANONICAL, "CUT196 receipt stored canonical drift")
    req(canonical(receipt) == RECEIPT_CANONICAL, "CUT196 receipt canonical drift")
    rr = receipt["current_v16_composition_replay"]
    req(rr["cut196_target_equals_current_prefix_offsets_766_1020"] is True, "receipt population identity drift")
    req(rr["n357_rejecting_cut196_target_blocks"] == 0, "receipt N357 block overlap drift")
    req(rr["n357_rejecting_cut196_target_terminals"] == 0, "receipt N357 terminal overlap drift")
    req(rr["double_charge"] is False, "receipt double-charge firewall drift")
    req(receipt["cut196_candidate"]["hostile_audit_review_id"] == AUDITED_CUT196_REVIEW, "CUT196 audit review drift")
    req(receipt["prior_main_boundary"]["hostile_reaudit_review_id"] == AUDITED_MAIN_V16_REVIEW, "V16 audit review drift")
    req(receipt["authority"]["before_remaining_terminals"] == PRE, "receipt pre-authority drift")
    req(receipt["authority"]["incremental_rejected_terminals"] == CUT196_INCREMENT, "receipt increment drift")
    req(receipt["authority"]["after_remaining_terminals"] == POST, "receipt post-authority drift")
    print(json.dumps({"verdict":"PASS_CUT196_CURRENT_V16_COMPOSITION_AND_MAIN_CONSUMPTION","cut196_audited_exact_head":AUDITED_CUT196_HEAD,"cut196_hostile_audit_review_id":AUDITED_CUT196_REVIEW,"target_offsets":[766,1020],"target_blocks":255,"closed_blocks":242,"n357_overlap_blocks":0,"n357_overlap_terminals":0,"incremental_rejected_terminals":CUT196_INCREMENT,"remaining_terminals":POST,"replacement_head_hostile_reaudit_required":True,"merge_authorized":False}, sort_keys=True))

if __name__ == "__main__":
    main()
