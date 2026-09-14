#!/usr/bin/env python3
import hashlib, json, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ACTIVE = "MB104-GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-CONDUCTOR-PAIR-MAP"
LOCKS = {
    "WALL": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-DESCENT-DATA-WALL.md", "65a696491a96cedc48754cdeefb88b112148f46f"),
    "CERT": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-RESIDUAL-LIFT-DESCENT-DATA-WALL-CERTIFICATE.json", "3799e31e7651ad19b1b28d75af6aee7e170375cf"),
    "AMBIENT_WRAPPER": ("stages/stage32/final-chain/32-03-multibranch/nodes/MB104/verify_mb104_balanced16_000707_e2_ambient_kummer_conductor_chain.py", "c4671b94b54ce12b45032365df606debb5bee90f"),
    "STATE": ("stages/stage32/final-chain/32-03-multibranch/STATE.json", "b4e34e9e6db30de02adbf88c0f635027fbd04550"),
    "PRIORITY": ("stages/stage32/final-chain/32-03-multibranch/PRIORITY-OVERRIDE-20260912.json", "73cc0979adffe0b17fccfe9705d3e1b86e0f04dd"),
}
AMBIENT_TOKEN = "PASS STAGE32_MB104_000707_E2_AMBIENT_KUMMER_CONDUCTOR_CHAIN_V1"

def req(cond, msg):
    if not cond:
        raise SystemExit("FAIL: " + msg)

def repo_root():
    p = HERE
    while p != p.parent:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
        p = p.parent
    raise SystemExit("FAIL: repo root")

def blob_sha(path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()

def main():
    root = repo_root()
    for key, (rel, expected) in LOCKS.items():
        p = root / rel
        req(p.is_file(), f"missing {key}")
        req(blob_sha(p) == expected, f"source lock {key}")

    cp = subprocess.run(
        [sys.executable, str(root / LOCKS["AMBIENT_WRAPPER"][0])],
        cwd=root, capture_output=True, text=True
    )
    req(cp.returncode == 0, "ambient wrapper replay")
    req(AMBIENT_TOKEN in cp.stdout, "ambient wrapper token")

    cert = json.loads((root / LOCKS["CERT"][0]).read_text())
    state = json.loads((root / LOCKS["STATE"][0]).read_text())
    priority = json.loads((root / LOCKS["PRIORITY"][0]).read_text())

    req(cert["active_leaf"] == ACTIVE, "certificate active leaf")
    req(state["next_obligation"]["active_leaf"] == ACTIVE, "STATE active leaf")
    req(priority["next_execution_leaf"] == ACTIVE, "PRIORITY active leaf")
    req(state["next_obligation"]["old_R8_route_status"] == "FROZEN_DOMINATED_UNTIL_PROGRESS_ENABLING_INPUT", "old R8 frozen")

    required = state["next_obligation"]["required_input"]
    req("R=C8/H" in required, "required residual lift")
    req("sqrt(h o phi)" in required, "required sqrt evaluation")

    missing = cert["exact_missing_datum"]
    req(len(missing) == 3, "three equivalent missing-data forms")
    req(cert["retained_inputs"]["supported_local_plus_minus_is_residual_sheet_bit"] is False, "local +/- firewall")
    req(cert["logical_boundary"]["eta_zero_alone_determines_conductor_sheet_transition"] is False, "eta=0 firewall")
    req(cert["logical_boundary"]["current_retained_boundary_supplies_weighted_cut_upper_bound"] is False, "no weighted upper bound")
    req(cert["logical_boundary"]["identity_gluing_claimed"] is False, "no identity gluing claim")
    req(cert["logical_boundary"]["deck_twisted_gluing_claimed"] is False, "no deck-twisted gluing claim")

    fw = cert["credit_firewall"]
    req(not any(fw.values()), "credit firewall")

    print("PASS STAGE32_MB104_000707_E2_RESIDUAL_LIFT_DESCENT_DATA_WALL_V1")
    print("boundary: residual-lift transition data missing; e=2 remains open")
    print("next: exact E->R lift, sqrt(h o phi) relative evaluations, or equivalent transition cocycle")

if __name__ == "__main__":
    main()
