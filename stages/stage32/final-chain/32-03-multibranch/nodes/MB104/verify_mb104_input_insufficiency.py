#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
CERT_PATH = Path(__file__).with_name("OBSTRUCTION.json")


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def main() -> None:
    cert = json.loads(CERT_PATH.read_text())
    require(cert["schema"] == "STAGE32_MB104_FINITE_WINDOW_INPUT_INSUFFICIENCY_V1", "schema")
    require(cert["status"] == "RETAINED_OBSTRUCTION_MB104_INCOMPLETE", "status")
    require(cert["receiver"] == "R29-LG2-MB", "receiver")

    fam = cert["formal_family"]
    require(fam["parameter"] == "k>=1", "parameter")
    require(fam["degree"] == "d=2k", "even degree family")
    require(fam["existence_of_actual_curves_claimed"] is False, "no existence claim")

    # Verify the exact formal identities over a broad deterministic range.
    for k in range(1, 10001):
        d = 2 * k
        for g, d2, delta, pa_expected in [
            (1, -d, 0, 1),
            (0, -d - 2, 0, 0),
        ]:
            pa = 1 + (d2 + d) // 2
            require(2 * (pa - 1) == d2 + d, "adjunction arithmetic genus")
            require(pa == pa_expected, "arithmetic genus specialization")
            require(pa - g == delta, "normalization genus relation")
            require(d2 + d == 2 * g - 2 + 2 * delta, "MB102 exact identity")
            require(16 * d2 <= d * d, "Hodge upper bound")

    mb = cert["multibranch_compatibility"]
    require(mb["required"] == "exists node i with r_i>=2", "multibranch semantics")
    require(mb["current_contract_couples_this_to_degree_upper_bound"] is False,
            "no hidden local-to-degree bound")

    route = cert["route_consequence"]
    require(route["finite_degree_window_proved"] is False, "no finite window")
    require(route["mb104_complete"] is False, "MB104 remains open")
    require(route["new_geometric_input_required"] is True, "new input required")
    require(route["candidate_route_classes_are_not_claimed_lemmas"] is True,
            "route-class firewall")

    for lock in cert["source_locks"]:
        path = ROOT / lock["path"]
        require(path.is_file(), f"missing source lock {lock['path']}")
        require(git_blob_sha1(path) == lock["blob_sha1"], f"source drift {lock['path']}")

    fw = cert["credit_firewall"]
    for key in [
        "finite_picard_enumeration_released",
        "r29_lg2_mb_discharged",
        "receiver_credit",
        "effectivity_credit",
        "final_milestone_credit",
        "theorem_credit",
        "endpoint_credit",
        "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim",
        "merge_authorized",
    ]:
        require(fw[key] is False, f"credit firewall {key}")

    print("PASS: MB104 current contracts admit formal arbitrary-degree low-genus data; finite window not proved")


if __name__ == "__main__":
    main()
