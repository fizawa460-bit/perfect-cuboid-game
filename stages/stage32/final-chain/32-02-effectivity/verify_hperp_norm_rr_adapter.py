#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import runpy
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[3]
ADAPTER_JSON = HERE / "HPERP-NORM-RR-ADAPTER.json"
ADAPTER_PY = HERE / "hperp_norm_rr_adapter.py"
RR_PY = HERE / "rr_effectivity_sufficient.py"
SURFACE_LOCK_VERIFIER = HERE / "verify_surface_invariant_source_lock.py"


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit(f"FAIL: {message}")


def canonical_without_self(obj: dict) -> str:
    payload = dict(obj)
    payload.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")).hexdigest()


def blob(path: Path) -> str:
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot load {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    data = json.loads(ADAPTER_JSON.read_text(encoding="utf-8"))
    req(data["schema"] == "STAGE32_FINAL_CHAIN_32_02_HPERP_NORM_RR_ADAPTER_V1", "adapter schema drift")
    req(canonical_without_self(data) == data["canonical_sha256_without_this_field"], "adapter canonical drift")

    locks = data["source_locks"]
    result_lock = locks["stage29_finite_picard_result"]
    result_path = REPO / result_lock["path"]
    req(blob(result_path) == result_lock["blob_sha"], "Stage29 finite-Picard result blob drift")
    result_text = result_path.read_text(encoding="utf-8")
    for token in (
        "STATUS=AUDITED_PASS",
        "r = gcd(d,16)",
        "m = 16/r",
        "n = d/r",
        "y = m C - n H",
        "y^2 = m^2 (C^2 - d^2/16)",
        "EFFECTIVITY_CERTIFIED=false",
    ):
        req(token in result_text, f"Stage29 result formula/provenance missing: {token}")

    audit_lock = locks["stage29_finite_picard_audit"]
    audit_path = REPO / audit_lock["path"]
    req(blob(audit_path) == audit_lock["blob_sha"], "Stage29 finite-Picard audit blob drift")
    audit_text = audit_path.read_text(encoding="utf-8")
    req(f"AUDIT_VERDICT={audit_lock['audit_verdict']}" in audit_text, "Stage29 finite-Picard audit verdict drift")
    for token in (
        "FINITE_PICARD_REDUCTION_AUDIT=PASS",
        "PICARD_DIVISIBILITY_RECONSTRUCTION_AUDIT=PASS",
        "y^2 = m^2*(C^2-d^2/16)",
        "EFFECTIVITY_CERTIFIED=false",
    ):
        req(token in audit_text, f"Stage29 audit formula/firewall missing: {token}")

    runpy.run_path(str(SURFACE_LOCK_VERIFIER), run_name="__main__")
    surface = json.loads((HERE / "SURFACE-INVARIANT-SOURCE-LOCK.json").read_text(encoding="utf-8"))
    surface_lock = locks["surface_invariant_lock"]
    req(surface_lock["path"] == "stages/stage32/final-chain/32-02-effectivity/SURFACE-INVARIANT-SOURCE-LOCK.json", "surface-lock path drift")
    req(surface_lock["canonical_sha256_without_this_field"] == surface["canonical_sha256_without_this_field"], "surface-lock canonical mismatch")

    exact = data["exact_adapter"]
    req(exact["reconstruction"] == "C2=d^2/16-N/m^2", "C2 reconstruction drift")
    req(exact["rr_sufficient_gate_from_norm"] == "d>16 and 16*N <= m^2*(d^2-16*d+224)", "scalar RR gate drift")

    interface = data["minimal_survivor_interface"]
    req(interface["full_59_entry_picard_vector_required_for_rr_gate"] is False, "minimal scalar-interface claim lost")
    req(interface["current_full178_producer_exports_this_scalar_source_locked_here"] is False, "producer availability overclaimed")
    req(interface["required_fields"] == ["row_id", "d", "negative_hperp_square_N"], "minimal survivor fields drift")

    adapter = load_module("stage32_hperp_rr", ADAPTER_PY)
    rr = load_module("stage32_rr_effectivity_crosscheck", RR_PY)

    default = adapter.classify_from_norm(186, 83472)
    req(default.status == "RR_INCONCLUSIVE_SOURCE_NOT_AFFIRMED", "norm adapter default did not fail closed")

    for row in data["regressions"]:
        got = adapter.classify_from_norm(row["d"], row["N"], source_affirmed=True)
        req(got.C2 == row["expected_C2"], f"C2 reconstruction mismatch: {row['id']}")
        req(got.status == row["expected_status"], f"norm adapter status mismatch: {row['id']}")
        direct = rr.classify(row["d"], row["expected_C2"], assumptions_affirmed=True)
        req(direct.status == got.status, f"direct-C2 and norm-adapter RR status disagree: {row['id']}")
        req(direct.effective_divisor_certified == got.effective_divisor_certified, f"direct-C2 and norm-adapter effectivity bit disagree: {row['id']}")

    invalid_fraction = adapter.classify_from_norm(10, 0, source_affirmed=True)
    req(invalid_fraction.status == "INVALID_INTEGRAL_CLASS_RECONSTRUCTION", "fractional C2 reconstruction did not fail closed")
    low_degree = adapter.classify_from_norm(16, 16, source_affirmed=True)
    req(low_degree.C2 == 0 and low_degree.status == "RR_INCONCLUSIVE", "d=16 boundary overclaimed")

    fw = data["credit_firewall"]
    req(fw["effectivity_preparation_credit"] is True, "preparation credit missing")
    for key in (
        "survivor_scalar_producer_complete",
        "full178_rows_effectivity_classified",
        "effectivity_final_execution_released",
        "integral_irreducible_low_genus_carrier_proved",
        "receiver_credit",
        "theorem_credit",
        "endpoint_credit",
        "stage32_closed",
        "merge_authorized",
    ):
        req(fw[key] is False, f"adapter leaked credit: {key}")

    print("PASS: Stage32 final-chain 32-02 Hperp-norm RR scalar adapter")
    print("minimal survivor interface for RR gate: row_id, d, N=-y^2")
    print("exact reconstruction: C2=d^2/16-N/m^2; RR gate: 16N<=m^2(d^2-16d+224)")
    print("full 59-entry Picard vector is not required by this RR sufficient test")
    print("producer gap remains: 32-01 must source-lock exact N per final survivor")
    print("credit: preparation only; no FULL178/effectivity-final/carrier/receiver/theorem/endpoint credit")


if __name__ == "__main__":
    main()
