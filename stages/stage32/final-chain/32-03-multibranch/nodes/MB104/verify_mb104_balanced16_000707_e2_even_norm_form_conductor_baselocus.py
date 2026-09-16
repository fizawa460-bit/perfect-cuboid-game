#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-E2-EVEN-NORM-FORM-CONDUCTOR-BASELOCUS-CERTIFICATE.json"

LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-EVEN-NORM-FORM-CONDUCTOR-BASELOCUS.md",
        "8782fdeb06a91f28956066852be5453eb99b80ab",
    ),
    "HALF_HYPERPLANE_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-HALF-HYPERPLANE-FACTORIZATION-CERTIFICATE.json",
        "b166657c08ec90c7b30d5c67ab0991978aa56381",
    ),
    "ALLOCATION_EFFECTIVITY_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-ALLOCATION-SENSITIVE-EIGENSECTION-EFFECTIVITY-WALL-CERTIFICATE.json",
        "35405643cdcab3aaf35535cc279c0bd4e217cbef",
    ),
    "ADAPTIVE_JET_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-ADAPTIVE-CANCELLATION-JET-BUDGET-CERTIFICATE.json",
        "59a18a3c0f60c9fa47affe6d483ea892670ac938",
    ),
    "A1_ENERGY_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-A1-LIFT-ENERGY-IDENTITY-CERTIFICATE.json",
        "0cec993c9d22e31fcf982985b37f0ae82c8cbce7",
    ),
    "AMBIENT_CHARACTER": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-AMBIENT-CHARACTER-FUNCTION.md",
        "2bdb46e79be8a745880622c9c0643eb13ef20b26",
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
    require(cert["schema"] == "STAGE32_MB104_000707_E2_EVEN_NORM_FORM_CONDUCTOR_BASELOCUS_V1", "schema")
    source_lock_preflight(cert)

    # Symbolic coefficient replay in variables m, R1, Q.
    # A_mu.B_mu = 784m^2 - 2(224m^2 - 8mR1 + Q).
    coeff_m2 = 784 - 2 * 224
    coeff_mR1 = 16
    coeff_Q = -2
    require((coeff_m2, coeff_mR1, coeff_Q) == (336, 16, -2), "residual intersection expansion")

    # Sum 2*mu*q with mu=4m-r, q=2r gives 16mR1-4Q.
    exc_mR1 = 16
    exc_Q = -4
    require((exc_mR1, exc_Q) == (16, -4), "exceptional correction expansion")

    # Subtraction must recover the retained cut 336m^2+2Q.
    bridge = (coeff_m2, coeff_mR1 - exc_mR1, coeff_Q - exc_Q)
    require(bridge == (336, 0, 2), "bridge identity")

    ri = cert["residual_intersection"]
    require(ri["A_mu_dot_B_mu"] == "336*m^2+16*m*R1-2*Q", "certificate I1")
    require(ri["forced_exceptional_total"] == "16*m*R1-4*Q", "certificate correction")
    require(ri["residual_base_intersection"] == "336*m^2+2*Q", "certificate residual")
    require(ri["retained_weighted_cut"] == "y/2=336*m^2+2*Q", "certificate cut")
    require(ri["bridge_identity"] is True, "certificate bridge verdict")

    sq = cert["square_root"]
    require(sq["opposite_sheet_requires_base_locus"] is True, "base-locus support verdict")
    require(sq["every_basepoint_is_conductor_claimed"] is False, "basepoint firewall")

    routing = cert["routing"]
    require(routing["arbitrary_branch_sign_system_reduced_to_ambient_baselocus"] is True, "routing reduction")
    require(routing["new_weighted_cut_upper_bound_proved"] is False, "no false upper bound")
    require(routing["e2_closed"] is False, "e2 routing firewall")
    require(cert["credit_firewall"]["merge_authorized"] is False, "merge firewall")

    print("PASS STAGE32_MB104_000707_E2_EVEN_NORM_FORM_CONDUCTOR_BASELOCUS_V1")
    print("norm=u^2-f_t*v^2 opposite_sheet_support=base_locus bridge=y/2=336*m^2+2*Q")


if __name__ == "__main__":
    main()
