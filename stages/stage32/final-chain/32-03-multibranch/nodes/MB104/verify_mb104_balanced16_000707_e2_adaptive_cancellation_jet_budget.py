#!/usr/bin/env python3
"""Fail-closed verifier for the MB104 adaptive cancellation jet budget."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-E2-ADAPTIVE-CANCELLATION-JET-BUDGET-CERTIFICATE.json"
PASS = "PASS STAGE32_MB104_000707_E2_ADAPTIVE_CANCELLATION_JET_BUDGET_V1"

LOCKS = {
    "HUMAN_NOTE": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-ADAPTIVE-CANCELLATION-JET-BUDGET.md",
        "0cbe49c719362fcfc3eb0492833e02a551dcd1fe",
    ),
    "ALLOCATION_WALL_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-ALLOCATION-SENSITIVE-EIGENSECTION-EFFECTIVITY-WALL-CERTIFICATE.json",
        "35405643cdcab3aaf35535cc279c0bd4e217cbef",
    ),
    "A1_ENERGY_CERT": (
        "stages/stage32/final-chain/32-03-multibranch/nodes/MB104/GENUS1-SPAN5-BALANCED16-000707-E2-A1-LIFT-ENERGY-IDENTITY-CERTIFICATE.json",
        "0cec993c9d22e31fcf982985b37f0ae82c8cbce7",
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
    req(cert["schema"] == "STAGE32_MB104_000707_E2_ADAPTIVE_CANCELLATION_JET_BUDGET_V1", "schema")
    declared = {x["id"]: (x["path"], x["blob_sha1"]) for x in cert["source_locks"]}
    req(declared == LOCKS, "certificate/source-lock table")
    for key, (rel, expected) in LOCKS.items():
        p = rr / rel
        req(p.is_file(), f"SOURCE_LOCK_FAIL missing {key}")
        req(blob_sha1(p) == expected, f"SOURCE_LOCK_FAIL {key}")

    alloc = json.loads((rr / LOCKS["ALLOCATION_WALL_CERT"][0]).read_text(encoding="utf-8"))
    energy = json.loads((rr / LOCKS["A1_ENERGY_CERT"][0]).read_text(encoding="utf-8"))
    finite = (rr / LOCKS["FINITE_JET_WALL"][0]).read_text(encoding="utf-8")
    req(alloc["variables"]["mu_j"] == "min(y_j,8*m-y_j)=4*m-|b_j|", "mu source")
    req(alloc["variables"]["q_j"] == "2*|b_j|", "q source")
    req(alloc["routing"]["minimum_allocation_sensitive_effectivity_route_closed"] is True, "allocation wall source")
    req(energy["exact_identity"]["same_sheet_formula"] == "84*l^2+56*l-(1/8)*sum_j d_j^2", "same-sheet source")
    req("adaptive/unbounded jet construction" in finite, "fixed finite-jet boundary")

    # Exact local target identity and global dimension algebra.
    for m in range(1, 61):
        for r in range(0, 4*m+1):
            mu = 4*m-r
            q = 2*r
            local = sum(2*mu+2*k+1 for k in range(q))
            req(local == q*(2*mu+q), f"local filtration m={m} r={r}")
            req(local == 16*m*r, f"local 16mr m={m} r={r}")

        bulk_max = 168*m*m - 56*m + 5
        shell_min = bulk_max + 1
        req(shell_min == 168*m*m - 56*m + 6, f"shell threshold m={m}")
        # At the last guaranteed-bulk Q, source-target lower bound is +2.
        slack_bulk_edge = 336*m*m - 112*m + 12 - 2*bulk_max
        req(slack_bulk_edge == 2, f"bulk edge slack m={m}")
        # At the first shell Q, the RR lower-bound slack is zero.
        slack_shell_edge = 336*m*m - 112*m + 12 - 2*shell_min
        req(slack_shell_edge == 0, f"shell edge slack m={m}")
        delta_shell_edge = 336*m*m + 112*m - 2*shell_min
        req(delta_shell_edge == 224*m-12, f"thin-shell delta edge m={m}")

    loc = cert["local_target"]
    req(loc["jet_dimension"] == "q*(2*mu+q)", "jet dimension")
    req(loc["active_dimension"] == "16*m*|b|", "active local dimension")
    glob = cert["global_target"]
    req(glob["target_dimension"] == "16*m*R1", "global target")
    src = cert["source_lower_bound"]
    req(src["source_dim_lower"] == "336*m^2-112*m+12+16*m*R1-2*Q", "source lower")
    req(src["source_minus_target_lower"] == "336*m^2-112*m+12-2*Q", "slack")
    req(src["bulk_kernel_nonzero_for_every_linear_evaluation_map"] is True, "bulk kernel consequence")
    shell = cert["thin_shell"]
    req(shell["raw_rank_possible_implies_delta_same_upper"] == "224*m-12", "thin shell")
    route = cert["routing"]
    req(route["bulk_raw_rank_injectivity_impossible"] is True, "bulk wall")
    req(route["thin_shell_remains_live"] is True, "shell live")
    req(route["global_evaluation_rank_computed"] is False, "rank not overclaimed")
    req(route["exact_order_realization_proved"] is False, "exact order not overclaimed")
    req(route["e2_closed"] is False and route["active_leaf_unchanged"] is True, "open route")
    req(all(v is False for v in cert["credit_firewall"].values()), "credit firewall")

    print(PASS)
    print("local target=16m|b|; source-target RR slack=336m^2-112m+12-2Q; raw-rank route only possibly live when delta_same<=224m-12; e2_closed=false")


if __name__ == "__main__":
    main()
