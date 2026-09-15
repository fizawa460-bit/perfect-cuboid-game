#!/usr/bin/env python3
"""Fail-closed verifier for the MB104 allocation-sensitive eigensection RR wall."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-E2-ALLOCATION-SENSITIVE-EIGENSECTION-EFFECTIVITY-WALL-CERTIFICATE.json"
PASS = "PASS STAGE32_MB104_000707_E2_ALLOCATION_SENSITIVE_EIGENSECTION_EFFECTIVITY_WALL_V1"

LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-ALLOCATION-SENSITIVE-EIGENSECTION-EFFECTIVITY-WALL.md",
        "c09aaaefd7d13fed896e1c938d3c679450bfdb89",
    ),
    "EVEN_RR_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-EVEN-HALF-HYPERPLANE-EIGENSECTION-WALL-CERTIFICATE.json",
        "04a5b572a79f4f9a6d5111f26502cdadfc428c3e",
    ),
    "HALF_HYPERPLANE_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-HALF-HYPERPLANE-FACTORIZATION-CERTIFICATE.json",
        "b166657c08ec90c7b30d5c67ab0991978aa56381",
    ),
    "FINITE_JET_WALL": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/FINITE-JET-MULTIPLICITY-SATURATION-WALL.md",
        "934bc0a66f920b6d14f9dffd7ccf335edb007417",
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
    req(cert["schema"] == "STAGE32_MB104_000707_E2_ALLOCATION_SENSITIVE_EIGENSECTION_EFFECTIVITY_WALL_V1", "schema")
    declared = {x["id"]: (x["path"], x["blob_sha1"]) for x in cert["source_locks"]}
    req(declared == LOCKS, "certificate/source-lock table")
    for key, (rel, expected) in LOCKS.items():
        p = rr / rel
        req(p.is_file(), f"SOURCE_LOCK_FAIL missing {key}")
        req(blob_sha1(p) == expected, f"SOURCE_LOCK_FAIL {key}")

    even = json.loads((rr / LOCKS["EVEN_RR_CERT"][0]).read_text(encoding="utf-8"))
    half = json.loads((rr / LOCKS["HALF_HYPERPLANE_CERT"][0]).read_text(encoding="utf-8"))
    finite = (rr / LOCKS["FINITE_JET_WALL"][0]).read_text(encoding="utf-8")
    req(even["absent_half_line"]["L_abs_square"] == -8, "L_abs square")
    req(even["surface_invariants"]["H_square"] == 16 and even["surface_invariants"]["chi_O_S"] == 8, "surface invariants")
    req(half["even_l"]["pure_pullback"] == "Lambda_(2m)~=pi^*O_S(7*m*H)", "even pure pullback")
    req("adaptive/unbounded jet construction" in finite, "adaptive jet route retained live")

    # Exact per-node substitution and the uniform worst-case RR bound.
    for m in range(1, 41):
        max_m2 = 14 * (4*m)**2
        chi_a_low = 392*m*m - 56*m + 8 - max_m2
        chi_b_low = 392*m*m - 56*m + 4 - max_m2
        req(chi_a_low == 168*m*m - 56*m + 8, f"A lower formula m={m}")
        req(chi_b_low == 168*m*m - 56*m + 4, f"B lower formula m={m}")
        req(chi_a_low > 0 and chi_b_low > 0, f"uniform positivity m={m}")
        req(16*(1-7*m) < 0, f"dual negativity m={m}")
        for b in range(-4*m, 4*m+1):
            y = 4*m + b
            mu = min(y, 8*m-y)
            req(mu == 4*m-abs(b), f"mu identity m={m} b={b}")
            req(0 <= mu <= 4*m, f"mu range m={m} b={b}")
            residual = (y-mu, 8*m-y-mu)
            expected = (2*max(b,0), 2*max(-b,0))
            req(residual == expected, f"residual pair m={m} b={b}")
            req(sum(residual) == 2*abs(b), f"extra cancellation m={m} b={b}")

    rrdata = cert["rr"]
    req(rrdata["m1_A_lower"] == 120 and rrdata["m1_B_lower"] == 116, "m1 bounds")
    req(rrdata["h2_A_zero"] is True and rrdata["h2_B_zero"] is True, "h2 wall")
    req(rrdata["h0_A_positive_uniformly"] is True and rrdata["h0_B_positive_uniformly"] is True, "h0 positivity")
    cancel = cert["residual_cancellation"]
    req(cancel["extra_order"] == "q_j=2*|b_j|", "q identity")
    req(cancel["ambient_effectivity_detects_extra_cancellation"] is False, "effectivity firewall")
    req(cancel["fixed_finite_jet_wall_dominates_adaptive_route"] is False, "adaptive route remains live")
    route = cert["routing"]
    req(route["minimum_allocation_sensitive_effectivity_route_closed"] is True, "route closed")
    req(route["individual_conductor_pair_map_materialized"] is False, "conductor map open")
    req(route["weighted_cut_upper_bound_proved"] is False and route["e2_closed"] is False, "credit firewall")
    req(all(v is False for v in cert["credit_firewall"].values()), "credit firewall")

    print(PASS)
    print("minimum exceptional vanishing leaves both eigensystems nonempty; residual requirement is adaptive cancellation q_j=2|b_j|; e2_closed=false")


if __name__ == "__main__":
    main()
