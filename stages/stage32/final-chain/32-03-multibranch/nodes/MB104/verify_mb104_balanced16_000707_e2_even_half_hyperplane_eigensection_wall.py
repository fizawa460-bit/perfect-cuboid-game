#!/usr/bin/env python3
"""Fail-closed verifier for the MB104 even-l eigensection RR wall."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-E2-EVEN-HALF-HYPERPLANE-EIGENSECTION-WALL-CERTIFICATE.json"
PASS = "PASS STAGE32_MB104_000707_E2_EVEN_HALF_HYPERPLANE_EIGENSECTION_WALL_V1"

LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-EVEN-HALF-HYPERPLANE-EIGENSECTION-WALL.md",
        "e1297a4a1b46fd52b78db4b5be80665a0ed8beeb",
    ),
    "HALF_HYPERPLANE_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-HALF-HYPERPLANE-FACTORIZATION-CERTIFICATE.json",
        "b166657c08ec90c7b30d5c67ab0991978aa56381",
    ),
    "STOLL_CANONICAL_SOURCE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/STOLL-CANONICAL-C0-SOURCE-NOTE.md",
        "e344290d5241c3f7f165ea3027cfc778abec3360",
    ),
    "ANTIINVARIANT_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-ANTIINVARIANT-CLASS-DECOMPOSITION.md",
        "8217f81e6ee176f4b760a5609a6048bf823b3721",
    ),
}


def req(ok, msg):
    if not ok:
        raise SystemExit("FAIL: " + msg)


def root():
    p = HERE
    while p != p.parent:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
        p = p.parent
    raise SystemExit("FAIL: repo root")


def blob_sha1(path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def main():
    rr = root()
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    req(cert["schema"] == "STAGE32_MB104_000707_E2_EVEN_HALF_HYPERPLANE_EIGENSECTION_WALL_V1", "schema")
    declared = {x["id"]: (x["path"], x["blob_sha1"]) for x in cert["source_locks"]}
    req(declared == LOCKS, "certificate/source-lock table")
    for key, (rel, expected) in LOCKS.items():
        p = rr / rel
        req(p.is_file(), f"SOURCE_LOCK_FAIL missing {key}")
        req(blob_sha1(p) == expected, f"SOURCE_LOCK_FAIL {key}")

    half = json.loads((rr / LOCKS["HALF_HYPERPLANE_CERT"][0]).read_text(encoding="utf-8"))
    stoll = (rr / LOCKS["STOLL_CANONICAL_SOURCE"][0]).read_text(encoding="utf-8")
    anti = (rr / LOCKS["ANTIINVARIANT_NOTE"][0]).read_text(encoding="utf-8")

    req(half["even_l"]["pure_pullback"] == "Lambda_(2m)~=pi^*O_S(7*m*H)", "even-l pure pullback")
    req(half["even_l"]["necessary_antiinvariant_eigenspace"] == "H0(S,O_S(7*m*H) tensor L_abs^(-1))!=0", "anti eigenspace target")
    req("K_S = b^* O_barS(1)" in stoll and "K_S^2 = 16" in stoll and "chi(O_S) = 8" in stoll, "canonical invariants source")
    req("branch divisor of `pi` consists only of the sixteen exceptional curves of the absent node type" in anti, "16 absent branch exceptionals")
    req("(E_j^+)^2=(E_j^-)^2=-2" in anti, "exceptional square source")

    inv = cert["surface_invariants"]
    req(inv == {"K_S":"H","H_square":16,"chi_O_S":8,"H_big_and_nef":True}, "surface invariants")
    lab = cert["absent_half_line"]
    req(lab["branch_exceptional_count"] == 16, "branch count")
    req(lab["B_abs_square"] == -32 and lab["L_abs_square"] == -8, "half-line square")
    req(lab["H_dot_B_abs"] == 0 and lab["H_dot_L_abs"] == 0, "H orthogonality")

    for m in range(1, 101):
        d2 = 784*m*m - 8
        dk = 112*m
        chi = 8 + (d2-dk)//2
        req(chi == 392*m*m-56*m+4, f"RR formula m={m}")
        req(chi > 0, f"RR positivity m={m}")
        req(16*(1-7*m) < 0, f"dual H negativity m={m}")
    req(cert["even_l"]["minimum_m1_chi"] == 340, "m=1 chi")
    req(cert["even_l"]["h2_zero"] is True, "h2 zero")
    req(cert["even_l"]["h0_positive_for_all_m_ge_1"] is True, "h0 positivity")

    wall = cert["route_wall"]
    req(wall["unrestricted_antiinvariant_eigensection_nonvanishing_is_obstruction"] is False, "route wall")
    req(wall["e2_closed"] is False and wall["active_leaf_unchanged"] is True, "open leaf")
    req(all(v is False for v in cert["credit_firewall"].values()), "credit firewall")

    print(PASS)
    print("chi(7mH-L_abs)=392m^2-56m+4>0; h2=0; unrestricted anti-eigensection exists for every m>=1; e2_closed=false")


if __name__ == "__main__":
    main()
