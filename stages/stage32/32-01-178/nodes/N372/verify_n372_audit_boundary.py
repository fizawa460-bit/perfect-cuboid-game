#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
HANDOFF = HERE / "AUDIT-HANDOFF.json"
STATE = HERE / "STATE.json"
RESULT = HERE / "RESULT.json"
REPLAY = HERE / "verify_n372_current_v15_witness_replay.py"

HANDOFF_BLOB = "0e44cbc2b9bcb4d541d02c0fc4f6a23edaa722c4"
HANDOFF_CANON = "d3058de322e2e93abbfe74d47f6edc7a7d7d1c38cb6368c85ff347684351b6bd"
STATE_BLOB = "e73af40e1433e6ab7227791c9501e51dfca1406c"
STATE_CANON = "ce99f0f14445a2b48c7024bde853470291f604378709fcc7747104efdcd5c6b2"
RESULT_BLOB = "c0267d903fd0b397fcd4766b03964bde788650e7"
RESULT_CANON = "b9852fcfa926e77e8c51defe31002e0bf4b281dd1db4b5f320326166932fef48"
REPLAY_BLOB = "4368be620af7f8ee903c9a278f6b3157646d9fd8"


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(v: object) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def canonical(obj: dict) -> str:
    q = dict(obj); q.pop("canonical_sha256_without_this_field", None)
    return csha(q)


def req(v: bool, msg: str) -> None:
    if not v:
        raise RuntimeError(msg)


def checked(path: Path, expected_blob: str, expected_canon: str | None = None) -> dict:
    req(blob(path) == expected_blob, f"blob drift: {path}")
    obj = json.loads(path.read_text())
    if expected_canon is not None:
        req(obj.get("canonical_sha256_without_this_field") == expected_canon, f"stored canonical drift: {path}")
        req(canonical(obj) == expected_canon, f"canonical drift: {path}")
    return obj


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cut196-root", type=Path, required=True)
    ap.add_argument("--n357-composition-root", type=Path, required=True)
    args = ap.parse_args()

    handoff = checked(HANDOFF, HANDOFF_BLOB, HANDOFF_CANON)
    checked(STATE, STATE_BLOB, STATE_CANON)
    checked(RESULT, RESULT_BLOB, RESULT_CANON)
    req(blob(REPLAY) == REPLAY_BLOB, "N372 replay verifier blob drift")

    req(handoff["status"] == "READY_FOR_HOSTILE_AUDIT_NO_MAIN_CREDIT", "handoff status drift")
    req(handoff["next_gate"] == "stage32-01-178-audit", "handoff next gate drift")
    req(handoff["generation"]["exact_head"] == "37bb955b584adee3a44489c2d484d5b933d61c5e", "generation exact head drift")
    req(handoff["generation"]["ci_run"] == 34697493512, "generation run drift")
    req(handoff["solver_independent_replay"]["exact_head"] == "136e14521223d50dcc116996bae9d87bf82ee71f", "replay exact head drift")
    req(handoff["solver_independent_replay"]["ci_run"] == 34697800114, "replay run drift")
    req(handoff["solver_independent_replay"]["verifier_blob_sha1"] == REPLAY_BLOB, "replay blob handoff drift")
    req(handoff["solver_independent_replay"]["z3_imported"] is False, "handoff z3 firewall drift")
    req(handoff["witness"]["terminal_identity"] == "g1-d008|e=8|rank=128820", "handoff witness identity drift")
    req(handoff["witness"]["self_square"] == -4 and handoff["witness"]["negative_hperp_square_N"] == 32, "handoff witness invariants drift")
    req(handoff["current_main"]["authoritative_remaining_strata"] == 17128, "handoff strata drift")
    req(handoff["current_main"]["authoritative_remaining_terminals"] == 47598978285064933757427, "handoff terminals drift")
    req(handoff["credit"]["current_v15_witness_candidate_only"] is True, "witness-only credit marker drift")
    for key in ("main_pruning_credit","full178_complete","n350_registered","effectivity_final","receiver_credit","theorem_credit","endpoint_credit","stage32_closed","merge_authorized"):
        req(handoff["credit"][key] is False, f"handoff credit firewall drift: {key}")

    proc = subprocess.run([
        sys.executable, str(REPLAY),
        "--cut196-root", str(args.cut196_root.resolve()),
        "--n357-composition-root", str(args.n357_composition_root.resolve())
    ], text=True, capture_output=True)
    if proc.returncode != 0:
        sys.stderr.write(proc.stdout); sys.stderr.write(proc.stderr)
        raise RuntimeError("N372 solver-independent replay failed at audit boundary")
    print(proc.stdout, end="")
    req("PASS_N372_CURRENT_V15_WITNESS_SOLVER_INDEPENDENT_REPLAY" in proc.stdout, "replay PASS verdict missing")
    req('"z3_imported": false' in proc.stdout, "replay z3 firewall verdict missing")

    print(json.dumps({
        "verdict":"PASS_N372_AUDIT_BOUNDARY_READY_FOR_HOSTILE_AUDIT",
        "pr":1797,
        "terminal_identity":"g1-d008|e=8|rank=128820",
        "self_square":-4,
        "negative_hperp_square_N":32,
        "current_v15_witness_candidate_only":True,
        "main_pruning_credit":False,
        "full178_complete":False,
        "stage32_closed":False,
        "merge_authorized":False,
        "next_gate":"stage32-01-178-audit"
    }, sort_keys=True))


if __name__ == "__main__":
    main()
