#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT = HERE / "post1648ak-v6-multibranch-stabilizer-orbits.json"
DIAG = HERE / "diagnose_stage32_post1648ak_v6_multibranch_stabilizer_orbits.py"


def canonical_sha(payload: dict) -> str:
    body = dict(payload)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    cert = json.loads(CERT.read_text())
    got = canonical_sha(cert)
    if got != cert["canonical_sha256_without_this_field"]:
        raise SystemExit(f"certificate canonical mismatch: {got}")

    proc = subprocess.run(
        [sys.executable, str(DIAG)],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    diag = json.loads(proc.stdout)
    exp = cert["exact_results"]

    direct = {
        "full_aut_group_order": diag["full_aut_group_order"],
        "v6_stabilizer_order": diag["v6_stabilizer_order"],
        "exactly_three_multibranch_candidate_count": diag["exactly_three_multibranch_candidate_count"],
        "exactly_three_candidate_orbit_count_under_v6_stabilizer":
            diag["exactly_three_candidate_orbit_count_under_v6_stabilizer"],
    }
    for key, value in direct.items():
        if value != exp[key]:
            raise SystemExit(f"{key} moved")

    pareto = diag["r_conditioned_branch_pareto"]
    by_r = {row["multibranch_node_count"]: row for row in pareto}
    if by_r[3]["minimum_total_normalization_preimages"] != exp["exactly_three_minimum_total_normalization_preimages"]:
        raise SystemExit("exactly-three normalization lower bound moved")
    if by_r[3]["minimum_branch_excess_over_47_met_nodes"] != exp["exactly_three_minimum_branch_excess_over_47_met_nodes"]:
        raise SystemExit("exactly-three branch excess moved")

    minimum = min(row["minimum_total_normalization_preimages"] for row in pareto)
    minimizers = [
        row["multibranch_node_count"]
        for row in pareto
        if row["minimum_total_normalization_preimages"] == minimum
    ]
    if minimum != exp["global_minimum_total_normalization_preimages"]:
        raise SystemExit("global branch minimum moved")
    if minimizers != exp["global_minimum_attained_for_multibranch_node_counts"]:
        raise SystemExit("global branch minimizers moved")

    if exp["v6_stabilizer_order"] != 1:
        raise SystemExit("AK bounded wall requires trivial V6 stabilizer")
    if exp["exactly_three_multibranch_candidate_count"] != 65:
        raise SystemExit("AK candidate count moved")
    if exp["exactly_three_candidate_orbit_count_under_v6_stabilizer"] != 65:
        raise SystemExit("AK singleton-orbit count moved")

    if not all(cert["firewalls"].values()):
        raise SystemExit("AK firewall moved")

    print("PASS_STAGE32_POST1648AK_V6_MULTIBRANCH_STABILIZER_ORBIT_BOUNDED_WALL")
    print(cert["canonical_sha256_without_this_field"])


if __name__ == "__main__":
    main()
