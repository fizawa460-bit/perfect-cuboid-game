#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
N380 = HERE / "STATE.json"
N379 = HERE.parent / "N379/STATE.json"

N380_BLOB = "4464d6106d71758bf3e920c3d2963db128e48cf9"
N380_CANON = "bb6b8c48550c60cc090bf1226ae3ee50c5a66c862398df75edc5505001d3a7de"
N379_BLOB = "2aba2e66e11b428ec3650eaa486152472a4681a4"
N379_CANON = "60cc37e8098cba454fe63bbfd3c909802dc623bc67d675b004ba36e3a9fc016f"

PRODUCER_HEAD = "af41c95b9e952ed6cf913f2187a9d3acd94ddef3"
PRODUCER_STATE_REL = Path("stages/stage32/cut-cert-lift/STATE.json")
PRODUCER_STATE_BLOB = "6890392a7b85b71d3eae07cdd6f9e72463c224bc"
RECEIPT_REL = Path("stages/stage32/cert-lift/CERTLIFT-03-G3-MASS7-SYMBOLIC-RECEIPT.json")
RECEIPT_BLOB = "56003ce22f8cc84f18311e6f11eecd6e65824d44"
HANDOFF_REL = Path("stages/stage32/cert-lift/CERTLIFT-03-HOSTILE-AUDIT-HANDOFF.json")
HANDOFF_BLOB = "8fd835d80a3c3585d5f2a7c98696395358e35cdf"
LEMMA_REL = Path("stages/stage32/cert-lift/g3_mass7_symbolic_parity_lemma.py")
LEMMA_BLOB = "af9f4501f911251d41b813770af6e41a706f2c95"
RECEIPT_VERIFY_REL = Path("stages/stage32/cert-lift/verify_certlift03_symbolic_receipt.py")
RECEIPT_VERIFY_BLOB = "b0674bc6af0e3b4934e95c9fd9aeaced3037ec4f"
EX5_HEAD = "fd00531181228c9f367a49eb61ddc3af6ab84ab3"
SYMBOLIC_CANON = "2d1fcfe51420ab01f81d353e0d19a2b1eef467a51e321da953b5cf18aa88e764"


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise RuntimeError(msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    q = dict(obj)
    q.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(q, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def checked_json(path: Path, expected_blob: str) -> dict:
    req(blob(path) == expected_blob, f"blob drift: {path}")
    return json.loads(path.read_text())


def exact_head(path: Path) -> str:
    return subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True).strip()


def run_json(cmd: list[str], *, cwd: Path, env: dict[str, str]) -> dict:
    p = subprocess.run(cmd, cwd=cwd, env=env, text=True, capture_output=True)
    req(p.returncode == 0, f"command failed: {' '.join(cmd)}\nstdout={p.stdout}\nstderr={p.stderr}")
    lines = [line for line in p.stdout.splitlines() if line.strip()]
    req(bool(lines), f"command produced no JSON: {' '.join(cmd)}")
    try:
        return json.loads(lines[-1])
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"last output line is not JSON: {lines[-1]}") from exc


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--certlift-root", type=Path, required=True)
    ap.add_argument("--ex5-source-root", type=Path, required=True)
    args = ap.parse_args()

    n379 = checked_json(N379, N379_BLOB)
    req(n379.get("canonical_sha256_without_this_field") == N379_CANON, "N379 stored canonical drift")
    req(canonical(n379) == N379_CANON, "N379 canonical replay drift")

    n380 = checked_json(N380, N380_BLOB)
    req(n380.get("canonical_sha256_without_this_field") == N380_CANON, "N380 stored canonical drift")
    req(canonical(n380) == N380_CANON, "N380 canonical replay drift")
    req(n380["parent"]["n379_state_blob_sha1"] == N379_BLOB, "N380 parent blob drift")
    req(n380["parent"]["n379_state_canonical_sha256"] == N379_CANON, "N380 parent canonical drift")
    req(n380["status"] == "CERTLIFT03_SYMBOLIC_CANDIDATE_PROMOTED_PENDING_HOSTILE_AUDIT_NO_CREDIT", "N380 status drift")

    certroot = args.certlift_root.resolve()
    ex5root = args.ex5_source_root.resolve()
    req(exact_head(certroot) == PRODUCER_HEAD, "CERT-LIFT promotion exact-head drift")
    req(exact_head(ex5root) == EX5_HEAD, "EX5 geometry exact-head drift")

    producer = checked_json(certroot / PRODUCER_STATE_REL, PRODUCER_STATE_BLOB)
    receipt = checked_json(certroot / RECEIPT_REL, RECEIPT_BLOB)
    handoff = checked_json(certroot / HANDOFF_REL, HANDOFF_BLOB)
    req(blob(certroot / LEMMA_REL) == LEMMA_BLOB, "symbolic lemma blob drift")
    req(blob(certroot / RECEIPT_VERIFY_REL) == RECEIPT_VERIFY_BLOB, "symbolic receipt verifier blob drift")

    req(producer["schema"] == "STAGE32_CUT_CERT_LIFT_STATE_V1", "producer schema drift")
    req(producer["active_node"] == "CERTLIFT-03_SYMBOLIC_G3_MASS7_CANDIDATE_PENDING_HOSTILE_AUDIT", "producer active-node drift")
    c3 = producer["certlift_03"]
    req(c3["status"] == "SYMBOLIC_CANDIDATE_PASS_PENDING_HOSTILE_AUDIT", "producer CERTLIFT03 status drift")
    req(c3["hostile_audited"] is False, "producer candidate unexpectedly hostile-audited")
    req(c3["evidence_exact_head"] == "2ea8f9131de81529ad152665df8b637d72092421", "producer evidence-head drift")
    req(c3["evidence_ci_run"] == 34726357893 and c3["evidence_ci_job"] == 103641044511, "producer evidence-CI drift")
    req(c3["symbolic_canonical"] == SYMBOLIC_CANON, "producer symbolic canonical drift")
    req(c3["finite_replay"]["targeted"] == 1852 and c3["finite_replay"]["closed"] == 1852 and c3["finite_replay"]["survivors"] == 0, "producer finite replay drift")
    req(c3["pre_picard"]["post_fibre_configurations"] == 0, "producer pre-Picard drift")
    req(c3["failure_profile"]["exact_exceptional_completions"] == 23608 and c3["failure_profile"]["fibre_feasible_completions"] == 0, "producer failure-profile drift")
    req(c3["source_locked_geometry"]["free_labels_with_g3_cell_pair"] == [], "producer residual g3-pair escape drift")
    req(not any(producer["credit"].values()), "producer credit firewall drift")

    req(receipt["status"] == "SYMBOLIC_CANDIDATE_PASS_PENDING_HOSTILE_AUDIT", "receipt status drift")
    req(receipt["symbolic_lemma"]["canonical"] == SYMBOLIC_CANON, "receipt symbolic canonical drift")
    req(receipt["finite_replay"]["targeted_blocks"] == 1852 and receipt["finite_replay"]["closed_blocks"] == 1852, "receipt finite count drift")
    req(receipt["finite_replay"]["survivors"] == 0, "receipt finite survivor regression")
    req(receipt["audit"]["hostile_audited"] is False, "receipt hostile-audit firewall drift")
    req(not any(receipt["credit"].values()), "receipt credit firewall drift")

    req(handoff["status"] == "READY_FOR_HOSTILE_AUDIT_NOT_AUDITED", "audit handoff status drift")
    req(handoff["credit_firewall"]["hostile_audit_pass"] is False, "audit handoff falsely marks hostile PASS")
    req(not any(handoff["credit_firewall"].values()), "audit handoff credit firewall drift")

    env = os.environ.copy()
    env["PYTHONPATH"] = str(ex5root / "stages/stage32-ex5/cut-handoff")
    replay = run_json([sys.executable, str(certroot / RECEIPT_VERIFY_REL)], cwd=certroot, env=env)
    req(replay["status"] == "PASS_CERTLIFT03_SYMBOLIC_RECEIPT_REPLAY", "symbolic receipt replay failed")
    req(replay["symbolic_canonical"] == SYMBOLIC_CANON, "live symbolic canonical mismatch")
    req(replay["hostile_audited"] is False and replay["main_credit"] is False and replay["merge_authorized"] is False, "live audit/credit firewall drift")

    rel = n380["current_main_relation"]
    req(rel["certlift02_projection_survivors"] == 275, "N380 residual count drift")
    req(rel["g3_selected_projection_survivors"] == 0, "g3 unexpectedly reduces 275 residual controls")
    req(rel["g3_additional_pruning_beyond_certlift02"] == 0, "g3 double-counting firewall drift")
    req(rel["v20_to_v22_exact_consumption_adapter_required"] is True, "V20-to-V22 adapter firewall drift")
    req(rel["hostile_audit_required_before_consumption"] is True, "hostile-audit consumption firewall drift")

    req(n380["audit_boundary"]["hostile_audit_pass"] is False, "N380 hostile-audit status drift")
    req(n380["n101_contract"]["remains_stopped"] is True, "N101 unexpectedly reopened")
    req(n380["n101_contract"]["symbolic_obstruction_is_not_an_n377_finite_signature_map"] is True, "N101 contract classification drift")
    req(all(value is False for value in n380["anti_loop"].values()), "N380 anti-loop/heavy firewall drift")
    req(all(value is False for value in n380["credit"].values()), "N380 credit firewall drift")

    print(json.dumps({
        "verdict": "PASS_N380_CERTLIFT03_PROMOTED_SYMBOLIC_CANDIDATE_AUDIT_WAIT_BOUNDARY",
        "producer_pr": 1803,
        "producer_promotion_exact_head": PRODUCER_HEAD,
        "symbolic_canonical": SYMBOLIC_CANON,
        "finite_targeted_blocks": 1852,
        "finite_closed_blocks": 1852,
        "current_main_projection_survivors": 275,
        "g3_selected_projection_survivors": 0,
        "hostile_audit_pass": False,
        "v20_to_v22_adapter_required": True,
        "n101_reopened_credit": False,
        "main_pruning_credit": False,
        "full178_complete": False,
        "merge_authorized": False,
        "next_gate": n380["next_gate"]
    }, sort_keys=True))


if __name__ == "__main__":
    main()
