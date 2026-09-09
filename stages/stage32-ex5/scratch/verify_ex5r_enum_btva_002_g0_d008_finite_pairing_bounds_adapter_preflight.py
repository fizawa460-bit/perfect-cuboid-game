#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[3]
CERT = HERE / "ex5r-enum-btva-002-g0-d008-finite-pairing-bounds-adapter-preflight.json"
LEDGER = HERE / "post1728-cycle2-candidate-ledger-v3.json"
SOURCE = HERE / "ex5r_enum_btva_002_finite_pairing_bounds_adapter.py"
RUNKEY = HERE / "runkeys" / "ex5r-enum-btva-002-g0-d008-rank61.json"

EXPECTED_CERT_CANONICAL = "21c956b374b175157abfab55c864b801b37d276b4f2ec6ef9b834db204610d31"
EXPECTED_LEDGER_CANONICAL = "663294aa9b5ac2ac8b61a8a02b39cca29e1e54433dd2be8604f99f9bd3c71517"
EXPECTED_SOURCE_BLOB = "fa337fc07e084d163e982c0dbcd7744cdc2f3e1a"
EXPECTED_PREVIOUS_BLOCKER = "BTVA_G0_D008_EXACT_FINITE_PAIRING_PREFIX_BOUNDS_ADAPTER_NOT_SOURCE_BOUND"
EXPECTED_BLOCKER = "BTVA_G0_D008_FINITE_PAIRING_BOUNDS_RUNTIME_WITNESS_NOT_MATERIALIZED"
EXPECTED_STATUS = "LIVE_AT_FINITE_PAIRING_BOUNDS_RUNTIME_WITNESS_GATE"


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def verify_canonical(path: Path, expected: str) -> dict:
    raw = json.loads(path.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    if claimed != expected or csha(raw) != expected:
        raise SystemExit(f"canonical regression: {path.name}")
    return raw


def main() -> None:
    cert = verify_canonical(CERT, EXPECTED_CERT_CANONICAL)
    ledger = verify_canonical(LEDGER, EXPECTED_LEDGER_CANONICAL)

    if cert["authority"] != "SCRATCH_NONAUTHORITATIVE":
        raise SystemExit("authority firewall regression")
    if cert["target"] != {
        "d": 8,
        "factor_d2_minus_16lower": 224,
        "g": 0,
        "legacy_lower_formula": "-d-2+2g",
        "lower_self_intersection": -10,
        "row_id": "g0-d008",
    }:
        raise SystemExit("g0-d008 target/lower regression")

    source_bytes = SOURCE.read_bytes()
    if git_blob_sha(source_bytes) != EXPECTED_SOURCE_BLOB:
        raise SystemExit("finite-bounds adapter source blob regression")
    source_text = source_bytes.decode()
    required_literals = [
        "EXPECTED_FACTOR_G0_D008 = 224",
        "lower = -d - 2 + 2 * g",
        "minus_hperp_gram = -(basis.T * gram * basis)",
        "pd = exact_positive_definite(minus_hperp_gram)",
        "radicand = factor * orthogonal_norm_numerator",
        "radius_floor = math.isqrt(radicand)",
        "floating_point_used\": False",
    ]
    if any(x not in source_text for x in required_literals):
        raise SystemExit("finite-bounds source semantic regression")
    if "Fraction(int(a[i, j]), 1)" in source_text:
        raise SystemExit("rational LDL truncation regression")

    if not cert["adapter_source"]["source_ready"]:
        raise SystemExit("source-ready regression")
    if cert["adapter_source"]["runtime_instance_verified"]:
        raise SystemExit("premature runtime-witness credit")
    if cert["adapter_source"]["blob_sha1"] != EXPECTED_SOURCE_BLOB:
        raise SystemExit("source lock regression")

    for rec in cert["source_locks"].values():
        path = ROOT / rec["path"]
        if not path.is_file():
            raise SystemExit(f"missing source lock: {rec['path']}")
        if git_blob_sha(path.read_bytes()) != rec["blob_sha1"]:
            raise SystemExit(f"source lock blob regression: {rec['path']}")

    math_adapter = cert["mathematical_adapter"]
    if math_adapter["inequality"] != "(16*p-d*delta)^2 <= (d^2-16*lower)*(delta^2-16*q)":
        raise SystemExit("Cauchy inequality regression")
    if not math_adapter["finite_pairing_coordinate_ranges_constructible"]:
        raise SystemExit("finite coordinate construction regression")
    if math_adapter["finite_cartesian_box_runtime_witness_present"]:
        raise SystemExit("premature finite-box runtime witness")
    if math_adapter["old_rank2_bound_promoted_to_complete_bound"]:
        raise SystemExit("rank2 semantic-promotion regression")
    if math_adapter["floating_point_used"]:
        raise SystemExit("floating-point firewall regression")

    dec = cert["route_decision"]
    if dec["previous_blocker"] != EXPECTED_PREVIOUS_BLOCKER or not dec["previous_blocker_cleared_at_source_level"]:
        raise SystemExit("previous blocker transition regression")
    if dec["blocker_code"] != EXPECTED_BLOCKER or dec["status"] != EXPECTED_STATUS:
        raise SystemExit("current gate regression")
    if dec["mathematical_failure"] or not dec["predicate_survives"]:
        raise SystemExit("route survival regression")
    if dec["nontrivial_receiver_effect_obtained"] or dec["qualified_independent_route_established"]:
        raise SystemExit("premature route credit")

    btva = next(r for r in ledger["candidate_records"] if r["candidate_id"] == "EX5R-ENUM-BTVA-002")
    if btva["cleared_previous_blocker"] != EXPECTED_PREVIOUS_BLOCKER:
        raise SystemExit("ledger blocker transition regression")
    if btva["blocker_code"] != EXPECTED_BLOCKER or btva["status"] != EXPECTED_STATUS:
        raise SystemExit("ledger current gate regression")
    if ledger["cycle"]["route_status"] != EXPECTED_STATUS:
        raise SystemExit("ledger route-status regression")

    key = json.loads(RUNKEY.read_text())
    if key["generation"] != 0 or key["armed"] is not False:
        raise SystemExit("cold run-key regression")
    if key["authorization"]["heavy_execution_authorized"]:
        raise SystemExit("heavy execution authorization regression")
    if key["scope"]["full178_rerun_authorized"] or key["scope"]["cross_row_expansion_authorized"]:
        raise SystemExit("scope expansion regression")
    if key["source_contract"]["materializer_source_ready"]:
        raise SystemExit("materializer must remain fail-closed before integration")

    if any(cert["credit"].values()) or any(ledger["credit"].values()):
        raise SystemExit("credit firewall regression")
    if cert["execution"]["heavy_run_performed"] or cert["execution"]["generation1_arm_authorized"]:
        raise SystemExit("execution firewall regression")
    if cert["firewalls"]["g0_d008_closed"] or cert["firewalls"]["full178_completed"]:
        raise SystemExit("closure firewall regression")
    if cert["firewalls"]["perfect_cuboid_claim"] or cert["firewalls"]["merge_authorized"]:
        raise SystemExit("endpoint/merge firewall regression")

    print(json.dumps({
        "status": "PASS_STAGE32EX5_BTVA_G0_D008_FINITE_PAIRING_BOUNDS_ADAPTER_PREFLIGHT",
        "route": cert["route_id"],
        "cleared_blocker": EXPECTED_PREVIOUS_BLOCKER,
        "current_blocker": EXPECTED_BLOCKER,
        "next_unit": dec["next_unit"],
        "factor": cert["target"]["factor_d2_minus_16lower"],
        "canonical_sha256": EXPECTED_CERT_CANONICAL,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
