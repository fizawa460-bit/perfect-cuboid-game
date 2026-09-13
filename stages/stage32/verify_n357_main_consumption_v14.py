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
CURRENT_STATE = ROOT / "stages/stage32/MAIN-STATE.json"
CURRENT_RECEIPT = ROOT / "stages/stage32/management/post-n357-composition-pass-consumption-20260912.json"

AUDITED_COMPOSITION_HEAD = "0bdc3b952b35ea3201d8619f21a3df7a3015ff85"
AUDITED_COMPOSITION_REVIEW = 5184369560
AUDITED_COMPOSITION_CI = 34659920867
AUDITED_N357_HEAD = "0d787839b7e0dad4a42108c61d16e7849c50862f"

STATE_BLOB = "7f4cdb067959b3ed561013ec195bd3b6f4993baf"
STATE_CANONICAL = "81e430b60e184488f3cf07ad7b5b11c083aa4af909a3b87073d03ea95937ce41"
RECEIPT_BLOB = "033500e397a0e9d6dfa04638ab765a861cc523b8"
RECEIPT_CANONICAL = "9e5209b77b7852df66673827782bbd6c0def6651409b711aff6969c69b8a8a5f"

HISTORICAL_LOCKS = {
    "state": ("stages/stage32/MAIN-STATE.json", "0f281111572572a8068cc38bb77f5f1c869b98ad"),
    "composition_receipt": ("stages/stage32/management/N357-V13-CURRENT-AUTHORITY-COMPOSITION.json", "5abac38ee21713fd978ae59e85a0e705c2eb7b6c"),
    "inner_verifier": ("stages/stage32/verify_n357_v13_current_authority_composition.py", "fdca9ad629983d8c31c7e6355540af3545910120"),
    "fail_closed_verifier": ("stages/stage32/verify_n357_v13_current_authority_composition_fail_closed.py", "8c3bb80e6fe1c552171d3c1a4eb63cd2bb6e482a"),
    "v13_startup_verifier": ("stages/stage32/verify_main_startup_authority_v13.py", "9a083e2f2e165edc26dd025558b8a459739968b4"),
}
N357_INCREMENT = 17797986705435299826016
PRE = 65396964990500233609659
POST = 47598978285064933783643

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

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--audited-composition-root", type=Path, required=True)
    ap.add_argument("--audited-n357-root", type=Path, required=True)
    args = ap.parse_args()
    comp_root = args.audited_composition_root.resolve()
    n357_root = args.audited_n357_root.resolve()
    req(exact_head(comp_root) == AUDITED_COMPOSITION_HEAD, "audited composition exact head drift")
    req(exact_head(n357_root) == AUDITED_N357_HEAD, "audited N357 candidate exact head drift")

    hist = {}
    for name, (rel, blob) in HISTORICAL_LOCKS.items():
        p = comp_root / rel
        req(p.is_file(), f"missing audited composition boundary file: {rel}")
        req(git_blob(p) == blob, f"audited composition boundary blob drift: {rel}")
        hist[name] = p

    proc = subprocess.run(
        [
            sys.executable,
            str(hist["fail_closed_verifier"]),
            "--audited-n357-root",
            str(n357_root),
        ],
        cwd=comp_root,
        text=True,
        capture_output=True,
    )
    if proc.returncode != 0:
        sys.stderr.write(proc.stdout)
        sys.stderr.write(proc.stderr)
        raise SystemExit("FAIL: hostile-audited V13 composition boundary no longer replays")
    print(proc.stdout, end="")

    inner = load_module(hist["inner_verifier"], "s32_n357_v13_composition_audited")
    residual = comp_root / "stages/stage32/residual-32-01-production"
    sys.path.insert(0, str(residual))
    from compressed_terminal_indexer import CompressedTerminalIndexer

    idx = CompressedTerminalIndexer(8, 8)
    req(idx.normal_budget + 1 == 113, "e=8 block width drift")
    survivors = []
    stream = hashlib.sha256()
    for block_index in range(idx.exceptional_count):
        base = tuple(int(v) for v in idx.unrank(block_index * 113))
        if inner.prefix_survives(base):
            survivors.append(block_index)
            stream.update(f"{block_index}\n".encode())
    req(len(survivors) == 7596, "g1-d008 prefix block count drift")
    req(stream.hexdigest() == "529b9c31d36c517484dc176ba1d37674790eec05dc01853f9ce93b36e416c8e3",
        "g1-d008 prefix stream drift")
    rejecting_prefix = [
        b for b in survivors
        if not inner.n357_accepts(tuple(int(v) for v in idx.unrank(b * 113)))
    ]
    req(rejecting_prefix == [], f"N357 unexpectedly rejects g1-d008 prefix blocks: {rejecting_prefix[:8]}")
    preferred = survivors[1:256]
    req(len(preferred) == 255, "CUT192 preferred wave width drift")
    rejecting_preferred = [
        b for b in preferred
        if not inner.n357_accepts(tuple(int(v) for v in idx.unrank(b * 113)))
    ]
    req(rejecting_preferred == [], "N357 invalidates CUT192 preferred wave")

    req(git_blob(CURRENT_STATE) == STATE_BLOB, "current V14 MAIN state blob drift")
    state = load(CURRENT_STATE)
    req(state["canonical_sha256_without_this_field"] == STATE_CANONICAL, "current V14 state stored canonical drift")
    req(canonical(state) == STATE_CANONICAL, "current V14 state canonical drift")
    req(git_blob(CURRENT_RECEIPT) == RECEIPT_BLOB, "current N357 consumption receipt blob drift")
    receipt = load(CURRENT_RECEIPT)
    req(receipt["canonical_sha256_without_this_field"] == RECEIPT_CANONICAL, "consumption receipt stored canonical drift")
    req(canonical(receipt) == RECEIPT_CANONICAL, "consumption receipt canonical drift")

    frontier = state["current_exact_frontier"]
    req(frontier["authoritative_remaining_terminals"] == POST, "post-N357 authority drift")
    req(frontier["authoritative_remaining_strata"] == 17128, "post-N357 strata drift")
    req(frontier["n357_main_pruning_credit"] is True, "N357 MAIN credit not consumed")
    req(frontier["n357_current_v13_composition_hostile_audited"] is True, "composition audit not retained")
    req(frontier["n357_current_v13_composition_audit_review_id"] == AUDITED_COMPOSITION_REVIEW,
        "composition review drift")
    req(frontier["n357_synchronized_head_hostile_audited"] is False,
        "replacement head self-awarded hostile audit")
    req(PRE - N357_INCREMENT == POST, "N357 consumption arithmetic drift")

    r = receipt["overlap_and_cross_lane_replay"]
    req(r["n357_rejecting_current_prefix_blocks"] == 0, "receipt prefix overlap drift")
    req(r["n357_rejecting_cut192_preferred_wave_blocks"] == 0, "receipt CUT192 overlap drift")
    req(r["n357_rejecting_cut192_preferred_wave_terminals"] == 0, "receipt CUT192 terminal overlap drift")
    req(r["cut192_satisfied_handoff_remains_current_main_surviving"] is True,
        "receipt invalidates CUT192 handoff")
    req(receipt["authority"]["after_remaining_terminals"] == POST, "receipt post authority drift")
    req(receipt["authority"]["n357_main_pruning_credit"] is True, "receipt lost N357 credit")

    fw = receipt["credit_firewall"]
    req(fw["numerical_pruning_credit_only"] is True, "N357 credit widened beyond numerical pruning")
    for key in ("full178_complete", "receiver_credit", "theorem_credit", "effectivity_credit",
                "endpoint_credit", "stage32_closed", "perfect_cuboid_existence_claim",
                "perfect_cuboid_nonexistence_claim", "merge_authorized"):
        req(fw[key] is False, f"forbidden credit enabled: {key}")

    print(json.dumps({
        "verdict": "PASS_N357_MAIN_CONSUMPTION_V14_FAIL_CLOSED",
        "audited_composition_head": AUDITED_COMPOSITION_HEAD,
        "audited_composition_review": AUDITED_COMPOSITION_REVIEW,
        "audited_n357_head": AUDITED_N357_HEAD,
        "incremental_rejected_terminals": N357_INCREMENT,
        "remaining_strata": 17128,
        "remaining_terminals": POST,
        "cut192_preferred_wave_n357_overlap": 0,
        "replacement_head_hostile_reaudit_required": True,
        "full178_complete": False,
        "merge_authorized": False,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
