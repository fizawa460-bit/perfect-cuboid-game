#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
LOCAL_V19 = ROOT / "stages/stage32/management/MAIN-STATE-V19-N358-PRE-REAUDIT.json"

V19_HEAD = "56c52a64dc402126431a6de6d023007052f4112c"
V19_STATE_BLOB = "acad022fe90b4d72edeac5f9d7ba08930decdff2"
V19_STATE_CANON = "2f0ed49bd3640f4f7158176bc435344d46785928e20c4ce67173305eb3974771"
N372_HEAD = "9fb78a0e0c7b52baca84058dea69b8b083e33774"
N372_RESULT_BLOB = "c0267d903fd0b397fcd4766b03964bde788650e7"
N372_RESULT_CANON = "b9852fcfa926e77e8c51defe31002e0bf4b281dd1db4b5f320326166932fef48"
N372_STATE_BLOB = "e73af40e1433e6ab7227791c9501e51dfca1406c"
N372_STATE_CANON = "ce99f0f14445a2b48c7024bde853470291f604378709fcc7747104efdcd5c6b2"
N372_HANDOFF_BLOB = "0e44cbc2b9bcb4d541d02c0fc4f6a23edaa722c4"
N372_HANDOFF_CANON = "d3058de322e2e93abbfe74d47f6edc7a7d7d1c38cb6368c85ff347684351b6bd"
N372_CLOSURE_BLOB = "34bd579ba456c070735045b60bb1f76265cd1a7b"
N372_AUDIT_VERIFIER_BLOB = "e57bf9a009b86926bdb2ddfd7c86889b2901a6a8"
N372_REPLAY_BLOB = "4368be620af7f8ee903c9a278f6b3157646d9fd8"
AUTH_STRATA = 17128
AUTH_TERMS = 47589703313957134886123

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

def exact_head(root: Path) -> str:
    return subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()

def locked_json(path: Path, blob: str, can: str) -> dict:
    req(path.is_file(), f"missing {path}")
    req(git_blob(path) == blob, f"blob drift {path}")
    obj = json.loads(path.read_text(encoding="utf-8"))
    req(obj.get("canonical_sha256_without_this_field") == can, f"stored canonical drift {path}")
    req(canonical(obj) == can, f"canonical drift {path}")
    return obj

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--audited-main-v19-root", type=Path, required=True)
    ap.add_argument("--n372-candidate-root", type=Path, required=True)
    args = ap.parse_args()
    main_root = args.audited_main_v19_root.resolve()
    n372_root = args.n372_candidate_root.resolve()

    req(exact_head(main_root) == V19_HEAD, "audited MAIN V19 exact head drift")
    audited_state_path = main_root / "stages/stage32/MAIN-STATE.json"
    audited = locked_json(audited_state_path, V19_STATE_BLOB, V19_STATE_CANON)
    local = locked_json(LOCAL_V19, V19_STATE_BLOB, V19_STATE_CANON)
    req(audited == local, "retained V19 snapshot differs from hostile-audited exact-head MAIN state")
    af = audited["current_exact_frontier"]
    req(af["authoritative_remaining_strata"] == AUTH_STRATA, "audited V19 strata drift")
    req(af["authoritative_remaining_terminals"] == AUTH_TERMS, "audited V19 authority drift")
    req(af["n358_main_pruning_credit"] is True, "audited V19 N358 credit missing")

    req(exact_head(n372_root) == N372_HEAD, "N372 repaired exact head drift")
    n = n372_root / "stages/stage32/32-01-178/nodes/N372"
    result = locked_json(n / "RESULT.json", N372_RESULT_BLOB, N372_RESULT_CANON)
    locked_json(n / "STATE.json", N372_STATE_BLOB, N372_STATE_CANON)
    handoff = locked_json(n / "AUDIT-HANDOFF.json", N372_HANDOFF_BLOB, N372_HANDOFF_CANON)
    req(git_blob(n / "verify_n372_transitive_source_lock_closure.py") == N372_CLOSURE_BLOB, "N372 closure verifier blob drift")
    req(git_blob(n / "verify_n372_audit_boundary.py") == N372_AUDIT_VERIFIER_BLOB, "N372 audit-boundary verifier blob drift")
    req(git_blob(n / "verify_n372_current_v15_witness_replay.py") == N372_REPLAY_BLOB, "N372 replay verifier blob drift")

    req(result["status"] == "SAT_CURRENT_V15_WITNESS_CANDIDATE", "N372 result status drift")
    w = result["witness"]
    req(w["terminal_identity"] == "g1-d008|e=8|rank=128820", "N372 witness identity drift")
    req(w["self_square"] == -4 and w["negative_hperp_square_N"] == 32, "N372 witness invariants drift")
    for key in ("main_pruning_credit","full178_complete","effectivity_final","receiver_credit","theorem_credit","endpoint_credit","stage32_closed","merge_authorized"):
        req(result["credit"][key] is False, f"N372 result credit firewall drift: {key}")
    req(handoff["status"] == "READY_FOR_HOSTILE_AUDIT_NO_MAIN_CREDIT", "N372 handoff status drift")
    req(handoff["next_gate"] == "stage32-01-178-audit", "N372 handoff next gate drift")
    req(handoff["credit"]["current_v15_witness_candidate_only"] is True, "N372 witness-only marker drift")
    for key in ("main_pruning_credit","full178_complete","effectivity_final","receiver_credit","theorem_credit","endpoint_credit","stage32_closed","merge_authorized"):
        req(handoff["credit"][key] is False, f"N372 handoff credit firewall drift: {key}")

    print(json.dumps({
        "verdict":"PASS_V20_EXTERNAL_SOURCE_LOCKS",
        "audited_main_v19_exact_head":V19_HEAD,
        "n372_candidate_exact_head":N372_HEAD,
        "n372_current_v15_witness_candidate_only":True,
        "n372_hostile_audit_required":True,
        "authority_unchanged":True,
        "merge_authorized":False
    }, sort_keys=True))

if __name__ == "__main__":
    main()
