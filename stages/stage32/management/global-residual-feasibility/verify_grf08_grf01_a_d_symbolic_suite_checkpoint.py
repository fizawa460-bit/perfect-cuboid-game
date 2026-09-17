#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CERT = HERE / "GRF-08-GRF01-A-D-SYMBOLIC-SUITE-CHECKPOINT.json"
ARCHIVED_MAIN_STATE = ROOT / "stages/stage32/proof/historical-routing-blobs/b8df16056625db5fbb1947f1e927593de258f1ff.json"

FILES = {
    HERE / "GRF-01-DESIGN.md": "7daa489d182e52401df9300acfe9899759515078",
    HERE / "GRF-02-PROJECTED-KERNEL.json": "7c1cda07749fbfb90245995d1def2ae96fb5604b",
    HERE / "verify_grf02_projected_kernel.py": "6c61d66a91bb6beeb2ad29165a269f5c98e20ad0",
    HERE / "GRF-03-NORM-LADDER-RESIDUE-COLLAPSE.json": "d6777200cadb6809dc3b46374c8f714cb6ebd6cd",
    HERE / "verify_grf03_norm_ladder_residue_collapse.py": "eaddc4eaa790742cc92ec0bac3043c6743f947fc",
    HERE / "GRF-04-RATIONAL-QUADRATIC-LOWER-BOUND-KERNEL.json": "f7c1073edbf895f498fd9923e59eedf5a4e981c8",
    HERE / "verify_grf04_rational_quadratic_lower_bound_kernel.py": "af883bd66600c626350f9e6ef4bc12c00e239f45",
    HERE / "GRF-05-INTEGRAL-FINITE-QUOTIENT-LOWER-BOUND-KERNEL.json": "75e556dee57dff282232a57898924d7e1826a40c",
    HERE / "verify_grf05_integral_finite_quotient_lower_bound_kernel.py": "75a92a3ec494481e89b671f4f8f6f7a9162befb8",
    HERE / "GRF-06-ODD-PRIME-AFFINE-COLUMN-IMAGE-KERNEL.json": "fec2271a241c76750d904fb08de48aa068339218",
    HERE / "verify_grf06_odd_prime_affine_column_image_kernel.py": "ff755901b7b55d978a3b523870865c1405035cdb",
    HERE / "GRF-07-COPRIME-CRT-LOCAL-SYSTEM-COMPOSITION-KERNEL.json": "9bec78e154cd903400035db1cab32f1358a2864d",
    HERE / "verify_grf07_coprime_crt_local_system_composition_kernel.py": "16c7245dce063fb7697d9a0619da6f756158e121",
    ARCHIVED_MAIN_STATE: "b8df16056625db5fbb1947f1e927593de258f1ff",
}
EXPECTED_CERT_CANONICAL = "ca09e4a2cc5aec89ba1d0b26de45a37a0fa93b68a78ae54ce39e206249d61344"

def req(ok: bool, msg: str) -> None:
    if not ok:
        raise RuntimeError(msg)

def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()

def read_json(path: Path) -> dict:
    return json.loads(path.read_text())

def main() -> None:
    for path, expected in FILES.items():
        req(path.is_file(), f"missing source lock: {path.relative_to(ROOT)}")
        req(blob(path) == expected, f"source-lock drift: {path.relative_to(ROOT)}")

    cert = read_json(CERT)
    stored = cert.pop("canonical_sha256_without_this_field", None)
    req(stored == EXPECTED_CERT_CANONICAL, "GRF-08 stored canonical drift")
    req(csha(cert) == EXPECTED_CERT_CANONICAL, "GRF-08 canonical drift")
    req(cert["node"] == "GRF-08", "GRF-08 node drift")

    design = (HERE / "GRF-01-DESIGN.md").read_text()
    for label in (
        "**A. Linear congruence projection.**",
        "**B. 2-adic quadratic projection.**",
        "**C. Rational quadratic lower bound.**",
        "**D. Odd-prime CUT layer.**",
    ):
        req(label in design, f"GRF-01 design step missing: {label}")

    grf03 = read_json(HERE / "GRF-03-NORM-LADDER-RESIDUE-COLLAPSE.json")
    req(
        grf03["status"]
        == "EXACT_SYMBOLIC_NO_GO_NORM_LADDER_CONGRUENCE_ADDS_NO_OBSTRUCTION_NO_CREDIT",
        "GRF-03 no-go status drift",
    )
    req(grf03["even_lattice_collapse"]["norm_ladder_congruence_automatic_for_every_integral_completion"],
        "GRF-03 automatic-collapse theorem drift")

    grf04 = read_json(HERE / "GRF-04-RATIONAL-QUADRATIC-LOWER-BOUND-KERNEL.json")
    req(not grf04["credit_firewall"]["main_pruning_credit"], "GRF-04 unexpected credit")
    grf05 = read_json(HERE / "GRF-05-INTEGRAL-FINITE-QUOTIENT-LOWER-BOUND-KERNEL.json")
    req(not grf05["credit_firewall"]["main_pruning_credit"], "GRF-05 unexpected credit")
    grf06 = read_json(HERE / "GRF-06-ODD-PRIME-AFFINE-COLUMN-IMAGE-KERNEL.json")
    req(not grf06["credit_firewall"]["main_pruning_credit"], "GRF-06 unexpected credit")
    grf07 = read_json(HERE / "GRF-07-COPRIME-CRT-LOCAL-SYSTEM-COMPOSITION-KERNEL.json")
    req(not grf07["credit_firewall"]["main_pruning_credit"], "GRF-07 unexpected credit")

    disposition = cert["design_disposition"]
    req(set(disposition) == {
        "A_linear_congruence_projection",
        "B_2adic_quadratic_projection",
        "C_quadratic_lower_bound",
        "D_odd_prime_cut_layer",
    }, "A-D disposition key drift")
    req(cert["milestone"]["grf01_symbolic_elimination_order_A_through_D_disposed"],
        "GRF-01 A-D milestone not retained")
    req(cert["milestone"]["concrete_full178_application_count"] == 0,
        "unexpected concrete FULL178 application")
    req(cert["milestone"]["new_main_pruning_credit"] == 0,
        "unexpected new MAIN pruning credit")
    req(cert["milestone"]["natural_hostile_audit_checkpoint"],
        "checkpoint must remain audit-ready")

    # GRF-08 is a retained V24 zero-credit checkpoint. Replay its authority
    # firewall against the exact archived V24 MAIN state, not the mutable V25
    # startup projection after N400 consumption.
    state = read_json(ARCHIVED_MAIN_STATE)
    auth = cert["authority_firewall"]
    frontier = state["current_exact_frontier"]
    req(auth["authority_remaining_strata"] == frontier["authoritative_remaining_strata"],
        "authority stratum count drift")
    req(auth["authority_remaining_terminals_upper_bound"] == frontier["authoritative_remaining_terminals"],
        "authority terminal upper bound drift")
    req(auth["authority_semantics"] == frontier["authoritative_remaining_terminals_semantics"],
        "authority semantics drift")
    req(not auth["authority_changed_by_checkpoint"], "checkpoint changed authority")
    req(not auth["main_pruning_credit"], "checkpoint granted MAIN pruning credit")
    req(not auth["full178_complete"], "checkpoint marked FULL178 complete")
    req(not auth["stage32_closed"], "checkpoint closed Stage32")
    req(not auth["merge_authorized"], "checkpoint authorized merge")

    for verifier in (
        HERE / "verify_grf06_odd_prime_affine_column_image_kernel.py",
        HERE / "verify_grf07_coprime_crt_local_system_composition_kernel.py",
    ):
        subprocess.run([sys.executable, str(verifier)], check=True)

    print(
        "GRF-08 PASS: GRF-01 A-D symbolic disposition is frozen as one no-credit "
        "audit checkpoint; concrete FULL178 application remains outside MAIN."
    )

if __name__ == "__main__":
    main()
