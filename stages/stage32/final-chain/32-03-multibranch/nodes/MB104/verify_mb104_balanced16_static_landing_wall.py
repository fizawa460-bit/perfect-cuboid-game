#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "BALANCED16-STATIC-LANDING-AVOIDANCE-CERTIFICATE.json"

LOCKS = {
    "FORMAL_PICARD_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/FORMAL-INFINITE-FAMILY-PICARD-CERTIFICATE.json",
        "32a01bc272f14eca3e8ba3229f021f4140ab7260",
    ),
    "BALANCED_QUOTIENT_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-KNOWN-CONIC-BALANCED-QUOTIENT-CERTIFICATE.json",
        "f63d08b9005762a02935a727f35e6581ae52aaab",
    ),
    "LOCAL_JET_WALL": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/MULTIFIBRATION-LOCAL-JET-WALL.md",
        "8bccb386dbc949fa177f0e08750e040f8439ecde",
    ),
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/BALANCED16-STATIC-LANDING-AVOIDANCE-WALL.md",
        "71f52716b9cbdd0218aa73a138837f3b3891f412",
    ),
}


def require(cond, msg):
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def root():
    p = HERE
    while p != p.parent:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
        p = p.parent
    raise SystemExit("FAIL: repo root not found")


def blob_sha1(path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def main():
    rr = root()
    cert = json.loads(CERT.read_text())
    require(cert["schema"] == "STAGE32_MB104_BALANCED16_STATIC_LANDING_AVOIDANCE_V1", "schema")
    declared = {x["id"]: (x["path"], x["blob_sha1"]) for x in cert["source_locks"]}
    require(declared == LOCKS, "certificate/source-lock table mismatch")
    for key, (rel, sha) in LOCKS.items():
        p = rr / rel
        if not p.is_file():
            raise SystemExit(f"SOURCE_LOCK_FAIL: missing {key}: {rel}")
        got = blob_sha1(p)
        if got != sha:
            raise SystemExit(f"SOURCE_LOCK_FAIL: {key}: expected {sha}, got {got}")

    formal = json.loads((rr / LOCKS["FORMAL_PICARD_CERT"][0]).read_text())
    bal = json.loads((rr / LOCKS["BALANCED_QUOTIENT_CERT"][0]).read_text())

    require(formal["common_contact_skeleton"]["supported_M_i"] == "2k", "supported mass formula")
    require(formal["common_contact_skeleton"]["branch_type"] == "all supported branches FSM-minimal (A,B)=(1,1), m=1", "minimal branch packet")
    require("distinct" in formal["common_contact_skeleton"]["landing_keys"], "distinct landing keys")
    require(formal["families"]["F1-P5-PIC"]["k"] == "4l", "F1-P5 k=4l")

    profiles = bal["balanced16"]["zero_pairing_quartic_profiles"]
    expected = {
        "0000770000ff": (4, 2),
        "00007b0000ff": (4, 2),
        "000707000f0f": (2, 1),
        "00070b000f0f": (2, 1),
    }
    for h, (nq, per_node) in expected.items():
        require(profiles[h]["zero_quartics"] == nq, f"{h} zero quartic count")
        require(profiles[h]["zero_quartics_through_each_supported_node"] == per_node, f"{h} per-node forbidden upper bound")
        require(per_node <= 2, f"{h} finite static forbidden set")

    # k=4l and M_i=2k give M_i=8l. With m=1, the retained formal skeleton uses 8l
    # distinct landing keys at each supported node. The source-locked local-jet wall
    # supplies an exceptional landing coordinate over an infinite characteristic-zero
    # geometric field. Avoiding <=2 fixed landing points therefore leaves infinitely
    # many choices for every finite l>=1. This is a route-wall statement, not a curve construction.
    require(cert["formal_packet"]["supported_minimal_branches_per_node"] == "8l", "8l branch count")
    require(cert["static_forbidden_landing_points_per_node_upper"] == 2, "forbidden-point upper bound")
    require(cert["route_consequence"]["static_landing_avoidance_alone_closes_balanced16"] is False, "negative route wall")
    require(cert["credit_firewall"]["MB104_complete"] is False, "MB104 firewall")

    print("PASS STAGE32_MB104_BALANCED16_STATIC_LANDING_AVOIDANCE_V1")
    print("formal_supported_minimal_branches_per_node=8l distinct_nonzero_landings")
    print("zero_quartic_forbidden_landings_per_node<=2")
    print("static_landing_value_avoidance=locally_feasible_for_all_finite_l")
    print("first_jet_global_compatibility_required=true whole_span5_open=true")


if __name__ == "__main__":
    main()
