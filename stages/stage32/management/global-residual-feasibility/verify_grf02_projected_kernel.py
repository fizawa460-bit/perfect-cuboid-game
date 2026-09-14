#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CERT = HERE / "GRF-02-PROJECTED-KERNEL.json"
DERIVE = HERE / "derive_grf02_selected64_projected_kernel.py"

EXPECTED_CERT_BLOB = "7c1cda07749fbfb90245995d1def2ae96fb5604b"
EXPECTED_DERIVE_BLOB = "05b5c5134261c4d35c3433d509d4968c820dc227"
EXPECTED_CANONICAL = "2e08a25e2de891bfabd0bf96ba06d928d733711b2c27449c9818b856665d4d6f"
EXPECTED_ASSIGNMENT_LABELS = [95, 99, 103, 102, 49, 97, 94, 101, 93, 98, 96]
EXPECTED_PARITY_ROW = {
    "modulus": 2,
    "coefficients": [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
}
EXPECTED_ACTIVE_LABELS = [49, 93, 95, 96]


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise RuntimeError(msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(v: object) -> str:
    return hashlib.sha256(
        json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_certificate() -> dict:
    req(CERT.is_file(), "missing GRF-02 certificate")
    req(blob(CERT) == EXPECTED_CERT_BLOB, "GRF-02 certificate blob drift")
    body = json.loads(CERT.read_text())
    stored = body.pop("canonical_sha256_without_this_field", None)
    req(stored == EXPECTED_CANONICAL, "GRF-02 stored canonical drift")
    req(csha(body) == EXPECTED_CANONICAL, "GRF-02 canonical recomputation failed")
    body["canonical_sha256_without_this_field"] = stored
    return body


def replay_derivation() -> dict:
    req(DERIVE.is_file(), "missing GRF-02 derivation script")
    req(blob(DERIVE) == EXPECTED_DERIVE_BLOB, "GRF-02 derivation blob drift")
    proc = subprocess.run(
        [sys.executable, str(DERIVE)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    req(not proc.stderr.strip(), f"GRF-02 derivation wrote stderr: {proc.stderr.strip()}")
    return json.loads(proc.stdout)


def verify_semantics(cert: dict) -> None:
    req(cert["schema"] == "STAGE32_MAIN_GRF02_SELECTED64_PROJECTED_KERNEL_DERIVATION_V2", "schema drift")
    req(cert["stage"] == 32 and cert["surface"] == "MAIN", "surface drift")
    req(
        cert["status"] == "EXACT_SYMBOLIC_PROJECTED_KERNEL_ONLY_NO_CONCRETE_178_TARGET_NO_CREDIT",
        "status drift",
    )

    fixed = cert["fixed_selected64"]
    req(fixed["assignment_labels_1based"] == EXPECTED_ASSIGNMENT_LABELS, "assignment-label order drift")
    req(fixed["free_coordinate_count"] == 53, "free-coordinate count drift")
    req(fixed["inverse_denominator"] == 8, "selected64 denominator drift")

    kernel = cert["exact_completion_kernel"]
    req(kernel["primitive_equation_rows"] == [EXPECTED_PARITY_ROW], "projected parity row drift")
    row = EXPECTED_PARITY_ROW["coefficients"]
    active = sorted(label for label, coeff in zip(EXPECTED_ASSIGNMENT_LABELS, row) if coeff % 2)
    req(active == EXPECTED_ACTIVE_LABELS, "projected active-label set drift")
    req(
        kernel["theorem"] == "A fixed x11 extends to some z53 iff every listed modular linear form vanishes.",
        "completion theorem wording drift",
    )

    projected = cert["projected_fixed_image"]
    req(projected["nontrivial_invariant_factors"] == [2], "projected fixed image is not Z/2")
    req(projected["order"] == 2, "projected fixed image order drift")
    req(projected["fixed_domain_cardinality"] == 8 ** 11, "fixed mod8 domain cardinality drift")
    req(
        projected["kernel_cardinality_in_mod8_fixed_domain"] * projected["order"]
        == projected["fixed_domain_cardinality"],
        "projected fixed-domain kernel/image cardinality identity failed",
    )

    classes = cert["fixed_coordinate_classes"]
    req(
        classes["equivalence_classes_by_projected_quotient_signature"]
        == [[49, 93, 95, 96], [94, 97, 98, 99, 101, 102, 103]],
        "projected quotient signature classes drift",
    )
    req(
        classes["hpadj_group_collapses_to_group_sum"] == {"a": True, "b": True, "c": False},
        "HPADJ group-collapse status drift",
    )

    ownership = cert["ownership"]
    req(ownership["concrete_application_owner"] == "stage32-01-178-mainbatch", "178 ownership drift")
    for key in (
        "concrete_row_or_stratum_selected",
        "population_replay_performed",
        "bounded_leaf_search_performed",
        "exact_subset_certificate_generated",
    ):
        req(ownership[key] is False, f"MAIN ownership firewall drift: {key}")

    firewall = cert["credit_firewall"]
    for key, value in firewall.items():
        req(value is False, f"GRF-02 credit firewall opened unexpectedly: {key}")


def main() -> None:
    cert = load_certificate()
    replay = replay_derivation()
    req(replay == cert, "GRF-02 exact replay differs from frozen certificate")
    verify_semantics(cert)
    print(
        json.dumps(
            {
                "status": "PASS",
                "certificate_canonical_sha256": EXPECTED_CANONICAL,
                "completion_condition": "x95 + x49 + x93 + x96 == 0 (mod 2)",
                "projected_fixed_image": "Z/2",
                "fixed_mod8_domain_fraction_extendable": "1/2",
                "concrete_application_owner": "stage32-01-178-mainbatch",
                "main_credit": False,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
