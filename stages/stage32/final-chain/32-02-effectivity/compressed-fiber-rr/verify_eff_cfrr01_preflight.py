#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parent
PREFLIGHT = HERE / "EFF-CFRR01-PREFLIGHT.json"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def main() -> None:
    p = json.loads(PREFLIGHT.read_text(encoding="utf-8"))
    req(p["schema"] == "STAGE32_MAIN_32_02_EFF_CFRR01_PREFLIGHT_V1", "schema")
    req(p["canonical_sha256_without_this_field"] == canonical(p), "preflight canonical")

    locks = p["source_locks"]
    for key in (
        "pilot_worker",
        "rr_adapter",
        "scalar_handoff",
        "btva_base4_parent",
        "btva_compressed_preflight",
        "historical_affine_lattice",
        "full178_manifest",
        "v47_authority",
    ):
        path = ROOT / locks[f"{key}_path"]
        req(path.is_file(), f"missing source {key}")
        req(git_blob(path) == locks[f"{key}_blob_sha1"], f"source drift {key}")

    manifest = json.loads((ROOT / locks["full178_manifest_path"]).read_text(encoding="utf-8"))
    req(manifest["schema"] == "STAGE32_RESIDUAL32_01_FULL178_MANIFEST_V1", "manifest schema")
    req(manifest["residual_row_count"] == 178, "manifest row count")
    target = p["pilot"]
    d = int(target["degree"])
    g = int(target["genus"])
    e = int(target["exceptional_mass"])
    req((g, d, e) == (0, 18, 8), "pilot target")
    r = math.gcd(d, 16)
    m = 16 // r
    req(target["gcd_d_16"] == r and target["m"] == m, "m-class arithmetic")
    req(target["row_id"] in manifest["m_class_rows"][str(m)], "pilot row absent")
    req(e >= manifest["row_parameter_derivation"]["exceptional_mass_min_g0"], "e lower bound")
    req(e <= (19 * d) // 5, "e upper bound")

    normal_mass = 19 * d - 5 * e
    req(normal_mass == 302 == target["normal_mass"], "normal mass")
    req(target["x4_values_per_base4"] == normal_mass + 1 == 303, "x4 count")
    req(target["base4_key_count"] == 343, "base4 count")
    req(target["exceptional_state_count"] == 11318, "exceptional state count")
    req(target["static7_key_count"] == 343 * 303 == 103929, "static7 count")
    req(target["terminal_mass"] == 11318 * 303 == 3429354, "terminal mass")

    rr = p["rr_gate"]
    lower = -d - 2 + 2 * g
    threshold = d - 14
    req(rr["adjunction_C2_lower"] == lower == -20, "adjunction lower")
    req(rr["rr_effective_C2_threshold"] == threshold == 4, "RR threshold")
    req(rr["bad_shell_checked_by_pilot"] == [lower, threshold - 1], "bad shell")
    req(rr["actual_bad_shell_top_under_parity"] == d - 16 == 2, "parity shell top")
    boundary_num = m * m * (d * d - 16 * threshold)
    req(boundary_num % 16 == 0, "boundary N integrality")
    boundary_N = boundary_num // 16
    rhs = m * m * (d * d - 16 * d + 224)
    req(boundary_N == rr["boundary_N"] == 1040, "boundary N")
    req(16 * boundary_N == rr["boundary_16N"] == rhs == rr["adapter_gate_rhs"] == 16640,
        "RR gate identity")

    btva = json.loads((ROOT / locks["btva_compressed_preflight_path"]).read_text(encoding="utf-8"))
    req(btva["schema"] == "STAGE32_MAIN_BTVA_COMPRESSED_PICARD_LIFT_INTERSECTION_PREFLIGHT_V1",
        "BTVA preflight schema")
    iface = btva["exact_interface"]
    req(iface["picard_variable"] == "x in Z^64 retained Picard basis", "Picard64 interface")
    req(iface["compressed_observable_order"] == ["a","b","c","t","x4","e","d","r0","r1","r2","r3","r4"],
        "compressed observable order")
    relaxed = iface["safe_relaxed_effective_curve_conditions"]
    req("the twelve compressed observables equal the requested static/residual key" in relaxed,
        "compressed-key equality contract")
    req("x is integral Picard64" in relaxed, "integral Picard64 existential lift")
    req(iface["all140_normal_nonnegativity_required_for_this_preflight"] is False,
        "normal nonnegativity relaxation")
    req("UNSAT" in iface["why_relaxed_is_safe"] and "sound exclusion" in iface["why_relaxed_is_safe"],
        "relaxation UNSAT safety")

    v47 = json.loads((ROOT / locks["v47_authority_path"]).read_text(encoding="utf-8"))
    req(p["authority"]["v47_full178_numerical_census_complete"] is True, "V47 completion flag")
    req(p["authority"]["v47_certified_upper_bound"] == "128645575147764659235", "V47 bound")
    req(p["authority"]["authority_changed_by_this_preflight"] is False, "authority firewall")

    cf = p["compressed_fiber"]
    req(cf["x4_existential"] is True and cf["r0_r1_r2_r3_r4_existential"] is True,
        "compressed relaxation")
    req(cf["per_terminal_picard64_witness_required"] is False, "witness firewall")
    req(cf["full12_residual_multiplicity_adapter_required_for_pilot"] is False,
        "residual adapter firewall")
    req(p["independent_certification_gap"]["qf_nia_bad_shell_unsat_is_pilot_diagnostic_only"] is True,
        "QF_NIA firewall")
    req(p["firewalls"]["pilot_run_complete"] is False, "pilot prematurely complete")
    for key in (
        "main_pruning_credit",
        "effectivity_credit",
        "receiver_credit",
        "route_credit",
        "theorem_credit",
        "endpoint_credit",
        "full178_complete",
        "stage32_closed",
        "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim",
        "merge_authorized",
    ):
        req(p["firewalls"][key] is False, f"firewall {key}")

    print("PASS: Stage32 32-02 EFF-CFRR01 compressed-base4 RR preflight is source-locked and zero-credit")


if __name__ == "__main__":
    main()
