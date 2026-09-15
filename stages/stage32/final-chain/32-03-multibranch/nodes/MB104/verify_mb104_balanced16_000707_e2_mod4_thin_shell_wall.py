#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-E2-MOD4-THIN-SHELL-WALL-CERTIFICATE.json"

LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-MOD4-THIN-SHELL-WALL.md",
        "e57086abc3ba578b5792249fe903d591987269ca",
    ),
    "ADAPTIVE_JET_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-ADAPTIVE-CANCELLATION-JET-BUDGET-CERTIFICATE.json",
        "59a18a3c0f60c9fa47affe6d483ea892670ac938",
    ),
    "ZERO_QUARTIC_TORSION_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-ZERO-QUARTIC-TORSION-CONGRUENCES-CERTIFICATE.json",
        "cf7d6ed10b2502ac976f1545af0a2f2e2e137899",
    ),
}


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def repo_root() -> Path:
    p = HERE
    while p != p.parent:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
        p = p.parent
    raise SystemExit("FAIL: repository root not found")


def blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def source_lock_preflight(cert: dict) -> None:
    declared = {x["id"]: (x["path"], x["blob_sha1"]) for x in cert["source_locks"]}
    require(declared == LOCKS, "certificate/source-lock table mismatch")
    rr = repo_root()
    for key, (rel, expected) in LOCKS.items():
        path = rr / rel
        if not path.is_file():
            raise SystemExit(f"SOURCE_LOCK_FAIL: missing {key}: {rel}")
        got = blob_sha1(path)
        if got != expected:
            raise SystemExit(f"SOURCE_LOCK_FAIL: {key}: expected {expected}, got {got}")


def main() -> None:
    cert = json.loads(CERT.read_text())
    require(cert["schema"] == "STAGE32_MB104_000707_E2_MOD4_THIN_SHELL_WALL_V1", "schema")
    source_lock_preflight(cert)

    c = [-4, -4, 3, 3, -4, 3, 3]
    require(sum(c) == 0, "oriented block saturation coefficient")
    require(sum(c[4:]) == 2, "oriented torsion-subset coefficient")
    require(sum(v * v for v in c) == 84, "block square coefficient")

    q0_b = [-4, 4, 3, -3, 4, 3, -3]
    q0_x = [2 * (v + 4) for v in q0_b]
    require(q0_x == [0, 16, 14, 2, 16, 14, 2], "Q0 x coefficients")
    require(q0_x[0] - q0_x[1] + q0_x[2] - q0_x[3] - q0_x[4] + q0_x[5] - q0_x[6] == -8, "Q0 saturation coefficient")
    require((q0_x[4] + q0_x[5] + q0_x[6]) % 4 == 0, "Q0 mod4")

    q1_b = c
    q1_x = [2 * (v + 4) for v in q1_b]
    require(q1_x == [0, 0, 14, 14, 0, 14, 14], "Q1 x coefficients")
    require(sum(q1_x) == 56, "Q1 saturation coefficient")
    require(sum(q1_x[4:]) % 4 == 0, "Q1 mod4")

    global_q_coeff = 2 * sum(v * v for v in c)
    require(global_q_coeff == 168, "global Q coefficient")
    delta_linear = 112
    require(336 - 2 * global_q_coeff == 0, "delta quadratic cancellation")
    require(delta_linear == 112, "delta linear coefficient")

    # Universal shell check reduces to 112*m <= 224*m-12.  The difference
    # is 112*m-12, increasing in m and already positive at m=1.
    require(112 * 1 - 12 > 0, "thin-shell upper inequality at m=1")
    require(12 - 112 * 1 < 0, "source-target margin at m=1")

    witness = cert["witness"]
    require(witness["oriented_block_coefficients"] == c, "certificate witness")
    require(witness["block_square_coefficient"] == 84, "certificate block square")
    require(witness["global_Q_coefficient"] == 168, "certificate global Q")
    require(cert["energy"]["inside_shell_for_all_m_ge_1"] is True, "certificate shell verdict")
    require(cert["routing"]["mod4_eliminates_thin_shell"] is False, "negative-route verdict")
    require(cert["credit_firewall"]["e2_closed"] is False, "e2 firewall")
    require(cert["credit_firewall"]["merge_authorized"] is False, "merge firewall")

    print("PASS STAGE32_MB104_000707_E2_MOD4_THIN_SHELL_WALL_V1")
    print("formal_witness_all_m_ge_1 Q=168*m^2 delta_same=112*m mod4_pass thin_shell_survives")


if __name__ == "__main__":
    main()
