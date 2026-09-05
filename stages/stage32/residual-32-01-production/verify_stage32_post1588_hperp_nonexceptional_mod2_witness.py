#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[3]
CERT_PATH = HERE / "post1588-hperp-nonexceptional-mod2-witness.json"
DIAG_PATH = HERE / "diagnose_stage32_post1588_hperp_nonexceptional_mod2.py"
EXPECTED_CANONICAL = "a81b679286be37cb47b3a96607694b265ea36fb7ba5c5aaf046e4119451f7c1a"


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def main() -> None:
    cert = json.loads(CERT_PATH.read_text())
    claimed = cert.pop("canonical_sha256_without_this_field")
    if claimed != EXPECTED_CANONICAL or csha(cert) != claimed:
        raise SystemExit("certificate canonical regression")
    cert["canonical_sha256_without_this_field"] = claimed

    for lock in cert["source_locks"].values():
        path = ROOT / lock["path"]
        if git_blob_sha1(path) != lock["blob_sha1"]:
            raise SystemExit(f"source blob moved: {lock['path']}")

    proc = subprocess.run(
        [sys.executable, str(DIAG_PATH)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    lines = [line for line in proc.stdout.splitlines() if line.strip()]
    if not lines:
        raise SystemExit("diagnostic emitted no output")
    observed = json.loads(lines[-1])

    if observed["verdict"] != "PASS_SOURCE_BOUND_NONEXCEPTIONAL_NORMAL_CURVE_MOD2":
        raise SystemExit(f"unexpected diagnostic verdict: {observed['verdict']}")
    if observed["adapter_canonical_sha256"] != cert["source_locks"]["hperp_integral_adapter"]["adapter_canonical_sha256"]:
        raise SystemExit("adapter canonical moved")
    if observed["hperp_text_sha256"] != cert["source_locks"]["hperp_integral_adapter"]["hperp_text_sha256"]:
        raise SystemExit("Hperp text moved")
    if observed["all140_retained_coordinates_sha256"] != cert["geometry"]["all140_retained_coordinates_sha256"]:
        raise SystemExit("all140 coordinate hash moved")
    if observed["selected64_change_of_basis_sha256"] != cert["geometry"]["selected64_change_of_basis_sha256"]:
        raise SystemExit("selected64 change-of-basis hash moved")

    ranks = cert["mod2_rank_test"]
    expected_rank_values = {
        "exceptional_rank_F2": ranks["exceptional_rank_F2"],
        "normal_rank_F2": ranks["normal_rank_F2"],
        "all140_rank_F2": ranks["all140_rank_F2"],
        "quotient_dimension_lower_bound_from_all140": ranks["normal_contribution_to_quotient_dimension"],
        "escaping_normal_count": ranks["escaping_normal_count"],
        "escaping_normal_labels_1based": ranks["escaping_normal_labels_1based"],
    }
    for key, value in expected_rank_values.items():
        if observed[key] != value:
            raise SystemExit(f"F2 rank/witness regression at {key}")

    witness = cert["deterministic_witness"]
    if observed["first_escaping_normal_label_1based"] != witness["normal_curve_label_1based"]:
        raise SystemExit("deterministic first witness moved")
    if observed["first_escaping_is_in_selected64_geometric_basis"] != witness["is_in_selected64_geometric_basis"]:
        raise SystemExit("selected64 witness membership moved")
    if observed["separator_support_retained_picard_coordinates_1based"] != witness["separator_support_retained_picard_coordinates_1based"]:
        raise SystemExit("separator support moved")
    if not observed["separator_annihilates_all_48_exceptionals"] or not observed["separator_detects_first_escaping_normal"]:
        raise SystemExit("separator replay failed")

    target = cert["fixed_target"]
    decision = cert["decision"]
    if target["Q"] != 602 or target["surviving_residues_decimal"] != [73]:
        raise SystemExit("fixed Stage32 frontier moved inside certificate")
    if not decision["missing_input_subgoal_obtained"]:
        raise SystemExit("missing-input subgoal credit missing")
    for forbidden in ("q602_residue_specific_commutator_obtained", "Q602_excluded", "O210_excluded", "controller_change_authorized"):
        if decision[forbidden]:
            raise SystemExit(f"credit firewall violated: {forbidden}")
    for forbidden in ("receiver_credit", "route_credit", "theorem_credit", "endpoint_credit", "perfect_cuboid_credit"):
        if cert["firewalls"][forbidden]:
            raise SystemExit(f"credit firewall violated: {forbidden}")

    print(json.dumps({
        "verdict": "PASS_STAGE32_POST1588_HPERP_NONEXCEPTIONAL_MOD2_WITNESS",
        "certificate_canonical_sha256": claimed,
        "exceptional_rank_F2": ranks["exceptional_rank_F2"],
        "all140_rank_F2": ranks["all140_rank_F2"],
        "escaping_normal_count": ranks["escaping_normal_count"],
        "first_witness_label_1based": witness["normal_curve_label_1based"],
        "separator_support_1based": witness["separator_support_retained_picard_coordinates_1based"],
        "Q602_excluded": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
