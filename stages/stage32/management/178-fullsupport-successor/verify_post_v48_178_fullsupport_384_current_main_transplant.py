#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

PACKET = HERE / "POST-V48-178-FULLSUPPORT-384-CURRENT-MAIN-TRANSPLANT.json"
PACKET_BLOB = "3395c315dff695bf6ef178bea5c5b3411f853311"
PACKET_CANON = "b80dd49ce146f37a91974e4081c29cd6754d3e68b2dc0c4912650cf4afee2392"

SOURCE_HEAD = "adcb7eb2eef153a1207294e956bf6115794e564d"
SOURCE_HANDOFF_REL = Path("stages/stage32/management/178-fullsupport-successor/POST-V48-178-FULLSUPPORT-384-MAIN-HANDOFF-PREFLIGHT.json")
SOURCE_HANDOFF_BLOB = "3667b2395f50b675f6f8286074e20e0212933e2f"
SOURCE_HANDOFF_CANON = "f52f6e74f3ab20c9d5c8a831351da7035af9cccea50893560f4307de5dab9e76"
SOURCE_VERIFY_REL = Path("stages/stage32/management/178-fullsupport-successor/verify_post_v48_178_fullsupport_384_main_handoff_preflight.py")
SOURCE_VERIFY_BLOB = "484dac8d43fc90357e08d033d2e93835fcad4c2e"

CANDIDATE_REL = Path("stages/stage32/32-01-178/fibration-nef/V48-FULL-SUPPORT-384-EQUIV-DERIVED-BOUND-RETAINED.json")
CANDIDATE_BLOB = "3acb9551db9fda6be8fde0194b23ddb41ca634d0"
CANDIDATE_CANON = "da7eb532daf2b775a49524fe45e5b7bf7851719f19a6926a227f5fa745258aba"
CANDIDATE_VERIFY_REL = Path("stages/stage32/32-01-178/fibration-nef/verify_v48_full_support_384_equiv_derived_bound_retained.py")
CANDIDATE_VERIFY_BLOB = "843d348351a05be083f2d0d6e16b08da45e38040"

CURRENT_MAIN_HEAD = "a834864923086e5f7c1647e462804f45ff9ac28d"
CURRENT_MAIN_STATE_BLOB = "070847c669120aef1ab3777239d45878937b41f3"
V48_SYNC_REL = Path("stages/stage32/management/178-support-qbc/V48-178-SUPPORT-QBC-AUTHORITY-SYNC.json")
V48_SYNC_BLOB = "2733e5519629e6365558bc1b4bfbc6305e0b5533"
V48_SYNC_CANON = "d106029369dd5a029cd7a56e1c7d80fdd29f8471454fd2ed6c638af2b70288b1"

V48_TOTAL = 128470212118313474449
V48_COVERED = 37911631052805557219
REPLACEMENT_COVERED = 37884640022451662730
TIGHTENING = 26991030353894489
CANDIDATE_TOTAL = 128443221087959579960

def req(v: bool, m: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + m)

def blob(p: Path) -> str:
    raw = p.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canon(o: dict) -> str:
    x = dict(o)
    x.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()

def load_locked(path: Path, expected_blob: str, expected_canon: str | None, label: str) -> dict:
    req(path.is_file(), "missing " + label)
    req(blob(path) == expected_blob, label + " blob drift")
    obj = json.loads(path.read_text(encoding="utf-8"))
    if expected_canon is not None:
        req(obj.get("canonical_sha256_without_this_field") == expected_canon, label + " stored canonical drift")
        req(canon(obj) == expected_canon, label + " canonical drift")
    return obj

def git(*args: str, cwd: Path) -> str:
    p = subprocess.run(["git", *args], cwd=cwd, check=True, text=True, stdout=subprocess.PIPE)
    return p.stdout.strip()

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane178-root", type=Path, required=True)
    ap.add_argument("--main-root", type=Path, default=ROOT)
    args = ap.parse_args()

    lane = args.lane178_root.resolve()
    main_root = args.main_root.resolve()

    packet = load_locked(PACKET, PACKET_BLOB, PACKET_CANON, "compact transplant packet")
    req(git("rev-parse", "HEAD", cwd=lane) == SOURCE_HEAD, "source checkout head drift")
    req((main_root / ".git").exists(), "main-root is not a git checkout")
    req(git("merge-base", "HEAD", CURRENT_MAIN_HEAD, cwd=main_root) == CURRENT_MAIN_HEAD,
        "compact branch is not based on frozen current main")

    state = main_root / "stages/stage32/MAIN-STATE.json"
    req(state.is_file() and blob(state) == CURRENT_MAIN_STATE_BLOB, "MAIN-STATE blob drift")
    sync = load_locked(main_root / V48_SYNC_REL, V48_SYNC_BLOB, V48_SYNC_CANON, "V48 authority sync")
    req(int(sync["authority"]["v48_same_population_replacement_upper_bound"]) == V48_TOTAL,
        "V48 authority total drift")
    req(sync["authority"]["additive_subtraction"] is False, "V48 authority additive accounting drift")
    req(sync["authority"]["no_double_charge"] is True, "V48 authority no-double-charge drift")

    handoff = load_locked(lane / SOURCE_HANDOFF_REL, SOURCE_HANDOFF_BLOB, SOURCE_HANDOFF_CANON, "source 178 handoff")
    req((lane / SOURCE_VERIFY_REL).is_file() and blob(lane / SOURCE_VERIFY_REL) == SOURCE_VERIFY_BLOB,
        "source handoff verifier blob drift")
    candidate = load_locked(lane / CANDIDATE_REL, CANDIDATE_BLOB, CANDIDATE_CANON, "source 384 candidate")
    req((lane / CANDIDATE_VERIFY_REL).is_file() and blob(lane / CANDIDATE_VERIFY_REL) == CANDIDATE_VERIFY_BLOB,
        "source candidate verifier blob drift")

    subprocess.run([
        sys.executable,
        str(lane / SOURCE_VERIFY_REL),
        "--lane178-root", str(lane),
        "--main-root", str(main_root),
    ], check=True)

    req(handoff["hostile_audit_gate"]["status"] == "PENDING", "legacy handoff audit status drift")
    req(handoff["disposition"]["handoff_ready_for_main_consumption"] is False,
        "legacy handoff unexpectedly self-authorized")
    req(candidate["semantics"]["main_consumption_performed"] is False,
        "source candidate unexpectedly self-consumed")

    req(packet["status"] == "READY_FOR_HOSTILE_AUDIT__ZERO_MAIN_CREDIT", "packet status drift")
    req(packet["current_main"]["repository_main"] == CURRENT_MAIN_HEAD, "packet main head drift")
    req(packet["source"]["producer_exact_head"] == SOURCE_HEAD, "packet source head drift")
    req(packet["source"]["source_handoff_blob_sha1"] == SOURCE_HANDOFF_BLOB, "packet source handoff lock drift")
    req(packet["source"]["candidate_blob_sha1"] == CANDIDATE_BLOB, "packet candidate lock drift")
    req(packet["source"]["replacement_rule"] ==
        "COMPACT_EXACT_HEAD_CI_REPLAYS_FROZEN_SOURCE_CHECKOUT__DO_NOT_INFER_AUDIT_PASS_FROM_LEGACY_BRANCH",
        "packet replay rule drift")

    a = packet["accounting"]
    req(int(a["v48_covered_384_upper_bound_sum"]) == V48_COVERED, "covered V48 drift")
    req(int(a["replacement_384_upper_bound_sum"]) == REPLACEMENT_COVERED, "replacement sum drift")
    req(int(a["tightening"]) == TIGHTENING, "tightening drift")
    req(V48_COVERED - REPLACEMENT_COVERED == TIGHTENING, "covered arithmetic drift")
    req(V48_TOTAL - V48_COVERED + REPLACEMENT_COVERED == CANDIDATE_TOTAL,
        "global same-population replacement arithmetic drift")
    req(int(a["candidate_global_upper_bound"]) == CANDIDATE_TOTAL, "candidate total drift")
    req(a["composition_rule"] ==
        "SAME_POPULATION_PER_COORDINATE_MIN_UPPER_BOUND_REPLACEMENT__NO_ADDITIVE_SUBTRACTION",
        "composition semantics drift")
    req(a["additive_subtraction"] is False, "additive subtraction forbidden")
    req(a["statistical_independence"] is False, "independence assumption forbidden")
    req(a["no_double_charge"] is True, "no-double-charge drift")
    req(a["uncovered_v48_population_unchanged"] is True, "uncovered V48 drift")
    req(a["identity_set_claimed"] is False, "identity-set overclaim")

    gate = packet["audit_gate"]
    req(gate["required"] is True and gate["status"] == "PENDING", "compact audit gate drift")
    req(gate["source_replay_required"] is True, "source replay firewall drift")
    req(gate["main_consumption_before_pass_forbidden"] is True, "pre-audit consumption firewall drift")
    d = packet["disposition"]
    req(d["handoff_ready_for_hostile_audit"] is True, "audit readiness drift")
    req(d["handoff_ready_for_main_consumption"] is False, "premature MAIN readiness")
    req(d["main_authority_changed"] is False and d["main_credit"] is False, "premature MAIN credit")
    req(d["merge_authorized"] is False, "merge authorization drift")
    for k, v in packet["firewalls"].items():
        req(v is False, "firewall drift " + k)

    print("POST_V48_178_COMPACT_CURRENT_MAIN_TRANSPLANT=PASS")
    print("SOURCE_EXACT_HEAD=" + SOURCE_HEAD)
    print("CURRENT_V48_UPPER_BOUND=128470212118313474449")
    print("CANDIDATE_REPLACEMENT_UPPER_BOUND=128443221087959579960")
    print("TIGHTENING=26991030353894489")
    print("ACCOUNTING=SAME_POPULATION_REPLACEMENT_NOT_ADDITIVE_SUBTRACTION")
    print("HOSTILE_AUDIT_STATUS=PENDING")
    print("MAIN_CONSUMPTION_AUTHORIZED=false")

if __name__ == "__main__":
    main()
