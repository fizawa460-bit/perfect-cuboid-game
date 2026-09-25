#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ART = HERE / "SUPPORT-QBC-CANONICAL-JOINT-MIN-PREFLIGHT.json"
ART_BLOB = "234e411fe38b442525c5c9cc6e2dadfaaec46248"
ART_CANON = "a3fd353ee8e6ce8e0a1c66ccb0abef5c25f169f89dd9269cf68bd468a4044cd2"
FORMULA = HERE / "verify_support_qbc_canonical_joint_min_preflight.py"
FORMULA_BLOB = "4296a18f9fb1b59f963206ff28af73a4e9cf7ef0"
SOURCE_BLOB = "37e72735125c232e534d92c6e24c7afc0a0f4f24"
RELAXED_BLOB = "490db30dc7e4bfc42da0e6dd9947a644dea14275"


def req(v: bool, m: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + m)


def blob(p: Path) -> str:
    raw = p.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(o: dict) -> str:
    x = dict(o)
    x.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def main() -> None:
    req(ART.is_file() and blob(ART) == ART_BLOB, "canonical-joint artifact blob drift")
    req(FORMULA.is_file() and blob(FORMULA) == FORMULA_BLOB, "canonical-joint formula verifier blob drift")

    art = json.loads(ART.read_text())
    req(canon(art) == ART_CANON == art["canonical_sha256_without_this_field"],
        "canonical-joint artifact canonical drift")
    req(art["status"] == "EXACT_CANONICAL_H_MIN_STRICTLY_DOMINATES_RELAXED_JOINT__ZERO_MAIN_CREDIT",
        "status drift")

    locks = art["source_locks"]
    req(locks == {
        "support_qbc_worker_blob_sha1": SOURCE_BLOB,
        "relaxed_joint_min_verifier_blob_sha1": RELAXED_BLOB,
        "canonical_joint_min_verifier_blob_sha1": FORMULA_BLOB,
    }, "source lock drift")

    req(art["bounded_formula_regression"] == {
        "states": 2952,
        "relaxed_joint_finite": 1268,
        "canonical_finite": 1128,
        "canonical_infeasible_relaxed_finite": 140,
        "strict_finite": 137,
        "equal_finite": 991,
        "max_strict_gain": 24,
        "weakening": 0,
    }, "bounded formula summary drift")
    req(art["bounded_literal_enumeration"] == {
        "literal_keys": 670,
        "formula_mismatches": 0,
        "strict_vs_relaxed_joint": 65,
        "max_strict_gain": 4,
    }, "literal regression summary drift")

    w = art["active_structural_witness"]
    req((w["b"],w["c"],w["t"],w["support"]) == (36,89,103,5),
        "active witness target drift")
    req((w["separate_floor"],w["relaxed_joint_floor"],w["canonical_joint_floor"]) ==
        (3137,3377,3617), "active witness floor drift")
    req((w["canonical_gain_vs_relaxed"],w["canonical_gain_vs_separate"]) == (240,480),
        "active witness gain drift")

    panel = art["active_three_cell_structural_scan"]
    req(sum(int(x["strict_with_relaxed_floor_at_most_4992"]) for x in panel["rows"]) == 559,
        "active panel <=4992 strict-state total drift")
    req(sum(int(x["crosses_qbc_cap_4992"]) for x in panel["rows"]) == 9,
        "active panel qBC-cap crossing total drift")
    req(len(panel["qbc_cap_crossing_states"]) == 9, "active panel crossing list size drift")
    for x in panel["qbc_cap_crossing_states"]:
        req(int(x["relaxed_joint_floor"]) <= 4992 < int(x["canonical_joint_floor"]),
            "qBC cap crossing witness drift")

    claim = art["claim"]
    req(claim["actual_weighted_v48_gain_claimed"] is False,
        "weighted V48 gain overclaim")
    req("canonical_joint_q_lower >= relaxed joint_q_lower" in claim["dominance"],
        "dominance statement drift")

    for k,v in art["firewalls"].items():
        req(v is False, "credit firewall drift " + k)

    subprocess.run([sys.executable, str(FORMULA)], check=True)

    print("SUPPORT_QBC_CANONICAL_JOINT_MIN_RETAINED=PASS")
    print("ACTIVE_PANEL_STRUCTURAL_STRICT_STATES_LE4992=559")
    print("ACTIVE_PANEL_QBC_CAP_CROSSINGS=9")
    print("ACTIVE_WITNESS=3137_to_3377_to_3617")
    print("WEIGHTED_V48_GAIN_CLAIMED=false")
    print("MAIN_CREDIT_CHANGED=false")


if __name__ == "__main__":
    main()
