#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parent
PREFLIGHT = HERE / "EFF-CFRR01-PREFLIGHT.json"
RETAINED_PILOT_CANON = "240fb8fe2641cb0a62df986449498107af3442786da0916a304a307df767f3dd"
PILOT_DISPOSITION_CANON = "aeb2405d44d9a597fdd8d7f055fde7ae90177c40367f8034f310ad81181a7864"


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

    # Source-retained bounded pilot evidence.  Kept inline so the V47/V48
    # successor scope does not need to broaden for a zero-credit diagnostic.
    retained = json.loads("{\"canonical_sha256_without_this_field\":\"240fb8fe2641cb0a62df986449498107af3442786da0916a304a307df767f3dd\",\"decision_problem\":{\"all140_pairings_nonnegative\":true,\"bad_rr_shell\":[-20,3],\"bad_rr_shell_solver\":\"Z3_QF_NIA\",\"base4_plus_e_d_fixed\":true,\"exceptional_pairing_sum\":8,\"linear_feasibility_solver\":\"Z3_QF_LIA\",\"normal_pairing_sum\":302,\"picard_integer_variables\":64,\"safe_logic\":\"UNSAT of the enlarged low-C2 shell over the relaxed base4 Picard64 fiber implies every actual source terminal under that base4 key has C2>=d-14. SAT only proves an ambiguous numerical lift exists and is not a non-effectivity certificate.\",\"x4_and_residual_observables_existential\":true},\"firewalls\":{\"effectivity_credit\":false,\"endpoint_credit\":false,\"full178_complete\":false,\"main_pruning_credit\":false,\"merge_authorized\":false,\"perfect_cuboid_existence_claim\":false,\"perfect_cuboid_nonexistence_claim\":false,\"qf_nia_unsat_is_independently_certified\":false,\"receiver_credit\":false,\"route_credit\":false,\"stage32_closed\":false,\"theorem_credit\":false},\"item\":\"32-02_EFFECTIVITY_SURVIVOR_DISPOSAL\",\"next_exact_step\":\"Run this five-key pilot. If any RR-all-lifts candidates appear, replace QF_NIA UNSAT reliance with an independent HNF/Gram-LLL/Fincke-Pohst base4-fiber checker before expanding to all 343 d18/e8 base4 keys.\",\"panel\":[{\"bad_shell_status\":null,\"base4\":[0,1,1,1],\"base_linear_status\":\"UNKNOWN\",\"classification\":\"UNKNOWN_BASE_LINEAR\",\"exceptional_multiplicity_per_x4\":4,\"reason_unknown\":\"timeout\",\"source_terminal_mass\":1212,\"x4_values_covered\":303},{\"bad_shell_status\":null,\"base4\":[0,4,4,8],\"base_linear_status\":\"UNKNOWN\",\"classification\":\"UNKNOWN_BASE_LINEAR\",\"exceptional_multiplicity_per_x4\":15,\"reason_unknown\":\"timeout\",\"source_terminal_mass\":4545,\"x4_values_covered\":303},{\"bad_shell_status\":null,\"base4\":[0,6,2,6],\"base_linear_status\":\"UNKNOWN\",\"classification\":\"UNKNOWN_BASE_LINEAR\",\"exceptional_multiplicity_per_x4\":50,\"reason_unknown\":\"timeout\",\"source_terminal_mass\":15150,\"x4_values_covered\":303},{\"bad_shell_status\":null,\"base4\":[1,2,2,2],\"base_linear_status\":\"UNKNOWN\",\"classification\":\"UNKNOWN_BASE_LINEAR\",\"exceptional_multiplicity_per_x4\":39,\"reason_unknown\":\"timeout\",\"source_terminal_mass\":11817,\"x4_values_covered\":303},{\"bad_shell_status\":null,\"base4\":[1,3,3,3],\"base_linear_status\":\"UNKNOWN\",\"classification\":\"UNKNOWN_BASE_LINEAR\",\"exceptional_multiplicity_per_x4\":93,\"reason_unknown\":\"timeout\",\"source_terminal_mass\":28179,\"x4_values_covered\":303}],\"route\":\"EFF_CFRR01_COMPRESSED_BASE4_PICARD64_RR_FAILURE_SHELL\",\"rr_gate\":{\"adapter_gate_rhs\":16640,\"adjunction_C2_lower\":-20,\"bad_shell_upper_safe\":3,\"boundary_16N\":16640,\"boundary_N\":1040,\"gcd_d_16\":2,\"m\":8,\"rr_effective_C2_threshold\":4,\"source_affirmed_by_this_worker_only_after_retained_bundle_marking_and_lane178_replay\":true},\"schema\":\"STAGE32_MAIN_32_02_EFF_CFRR01_D18E8_BASE4_PILOT_V1\",\"source_locks\":{\"base_picard_solver_blob_sha1\":\"6b4c3514b5b4cbccd8e66cbffc7f61f8830d1633\",\"btva_base4_parent_blob_sha1\":\"29114c0cd8a2c604d24b2a9ad3418fc2b5200171\",\"full178_manifest_blob_sha1\":\"0a46b34e278688240656b4977e9cb7f589e90e06\",\"lane178_aggregate_picard_blob_sha1\":\"5fa9f1d67d6411cb550230b62398aff7bd6488ff\",\"rr_adapter_blob_sha1\":\"069e9215305fe4fa34d9949c871914b5ee17f19d\",\"scalar_handoff_blob_sha1\":\"61da6fb75643d8e58b642f5de5d90dc6fe9ff227\"},\"stage\":32,\"status\":\"BOUNDED_FIVE_BASE4_PILOT_COMPLETE_ZERO_CREDIT\",\"summary\":{\"linear_fiber_unsat\":0,\"rr_all_lifts_candidate\":0,\"rr_ambiguous_low_c2_witness\":0,\"sample_base4_keys\":5,\"source_terminal_mass_in_sample\":60903,\"source_terminal_mass_rr_candidate\":0,\"unknown\":5},\"target\":{\"base4_key_count\":343,\"base4_order\":[\"a\",\"b\",\"c\",\"t\"],\"degree\":18,\"exceptional_mass\":8,\"exceptional_state_count\":11318,\"genus\":0,\"normal_mass\":302,\"row_id\":\"g0-d018\",\"static7_key_count\":103929,\"terminal_mass\":3429354,\"x4_existential\":true,\"x4_values_per_base4\":303}}")
    req(retained["schema"] == "STAGE32_MAIN_32_02_EFF_CFRR01_D18E8_BASE4_PILOT_V1",
        "retained pilot schema")
    req(retained["canonical_sha256_without_this_field"] == RETAINED_PILOT_CANON
        and canonical(retained) == RETAINED_PILOT_CANON, "retained pilot canonical")
    req(retained["status"] == "BOUNDED_FIVE_BASE4_PILOT_COMPLETE_ZERO_CREDIT",
        "retained pilot status")
    rs = retained["summary"]
    req(rs == {
        "linear_fiber_unsat": 0,
        "rr_all_lifts_candidate": 0,
        "rr_ambiguous_low_c2_witness": 0,
        "sample_base4_keys": 5,
        "source_terminal_mass_in_sample": 60903,
        "source_terminal_mass_rr_candidate": 0,
        "unknown": 5,
    }, "retained pilot summary")
    expected_keys = [[0,1,1,1],[0,4,4,8],[0,6,2,6],[1,2,2,2],[1,3,3,3]]
    req([row["base4"] for row in retained["panel"]] == expected_keys, "retained pilot key order")
    req(all(row["base_linear_status"] == "UNKNOWN"
            and row["classification"] == "UNKNOWN_BASE_LINEAR"
            and row["bad_shell_status"] is None
            and row["reason_unknown"] == "timeout"
            for row in retained["panel"]), "retained pilot timeout classification")
    req(sum(int(row["source_terminal_mass"]) for row in retained["panel"]) == 60903,
        "retained pilot sample mass")
    for key in (
        "main_pruning_credit","effectivity_credit","receiver_credit","route_credit",
        "theorem_credit","endpoint_credit","stage32_closed",
        "perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","merge_authorized",
    ):
        req(retained["firewalls"][key] is False, f"retained pilot firewall {key}")

    disp = json.loads("{\"canonical_sha256_without_this_field\":\"aeb2405d44d9a597fdd8d7f055fde7ae90177c40367f8034f310ad81181a7864\",\"firewalls\":{\"effectivity_credit\":false,\"endpoint_credit\":false,\"main_pruning_credit\":false,\"merge_authorized\":false,\"perfect_cuboid_existence_claim\":false,\"perfect_cuboid_nonexistence_claim\":false,\"receiver_credit\":false,\"route_credit\":false,\"stage32_closed\":false,\"theorem_credit\":false},\"interpretation\":{\"blind_timeout_extension_selected_as_next_step\":false,\"effectivity_credit\":false,\"mathematical_failure\":false,\"mathematical_unsat_credit\":false,\"timeout_is_resource_wall_not_mathematical_evidence\":true,\"why\":\"All five keys timed out before bad-shell search. The bounded pilot therefore does not distinguish feasibility, bad-shell existence, or RR-all-lifts candidacy.\"},\"item\":\"32-02_EFFECTIVITY_SURVIVOR_DISPOSAL\",\"next_exact_step\":{\"full343_scaleout_authorized\":false,\"main_consumption_gate\":\"EX5 result must be source-retained, exact-scope compatible, hostile-audited, and explicitly handed off before MAIN effectivity credit.\",\"preferred_existing_specialist\":\"Stage32EX5 EFF-AFFINE01 family\",\"required_result\":\"Replace each of the five BASE_LINEAR_QF_LIA UNKNOWN results with source-locked exact integer-fiber feasibility and, for feasible fibers, exact bad-shell SAT/UNSAT classification.\",\"route\":\"INDEPENDENT_EXACT_AFFINE_LATTICE_BACKEND\"},\"observed_result\":{\"all_unknown_reason\":\"timeout\",\"all_unknown_stage\":\"BASE_LINEAR_QF_LIA\",\"linear_fiber_unsat\":0,\"rr_all_lifts_candidate\":0,\"rr_ambiguous_low_c2_witness\":0,\"sample_base4_keys\":5,\"solver_timeout_ms_per_key\":15000,\"source_terminal_mass_in_sample\":60903,\"unknown\":5},\"pilot_provenance\":{\"artifact_id\":10845511372,\"artifact_name\":\"stage32-main-eff-cfrr01-d18e8-five-key-pilot\",\"artifact_zip_digest_sha256\":\"c570110941b8e6bfe828410dbfde7fe64ea8cc12bb74870899bd952768489dca\",\"execution_head\":\"d38b31458833f13ae8fb7d679e35a9ad99a28d51\",\"job_id\":107931867358,\"result_canonical_sha256\":\"240fb8fe2641cb0a62df986449498107af3442786da0916a304a307df767f3dd\",\"workflow_run_id\":36090549352},\"route\":\"EFF_CFRR01_COMPRESSED_BASE4_PICARD64_RR_FAILURE_SHELL\",\"schema\":\"STAGE32_MAIN_32_02_EFF_CFRR01_PILOT_DISPOSITION_V1\",\"stage\":32,\"status\":\"PILOT_COMPLETE__5_OF_5_UNKNOWN_BASE_LINEAR_TIMEOUT__ZERO_CREDIT__EXACT_AFFINE_SUCCESSOR_REQUIRED\"}")
    req(disp["schema"] == "STAGE32_MAIN_32_02_EFF_CFRR01_PILOT_DISPOSITION_V1",
        "pilot disposition schema")
    req(disp["canonical_sha256_without_this_field"] == PILOT_DISPOSITION_CANON
        and canonical(disp) == PILOT_DISPOSITION_CANON, "pilot disposition canonical")
    req(disp["status"] ==
        "PILOT_COMPLETE__5_OF_5_UNKNOWN_BASE_LINEAR_TIMEOUT__ZERO_CREDIT__EXACT_AFFINE_SUCCESSOR_REQUIRED",
        "pilot disposition status")
    prov = disp["pilot_provenance"]
    req(prov["execution_head"] == "d38b31458833f13ae8fb7d679e35a9ad99a28d51",
        "pilot execution head")
    req(prov["workflow_run_id"] == 36090549352 and prov["job_id"] == 107931867358,
        "pilot workflow provenance")
    req(prov["artifact_id"] == 10845511372, "pilot artifact id")
    req(prov["artifact_zip_digest_sha256"] ==
        "c570110941b8e6bfe828410dbfde7fe64ea8cc12bb74870899bd952768489dca",
        "pilot artifact digest")
    req(prov["result_canonical_sha256"] == RETAINED_PILOT_CANON,
        "pilot result canonical binding")
    obs = disp["observed_result"]
    req(obs["sample_base4_keys"] == 5 and obs["unknown"] == 5
        and obs["all_unknown_stage"] == "BASE_LINEAR_QF_LIA"
        and obs["all_unknown_reason"] == "timeout"
        and obs["solver_timeout_ms_per_key"] == 15000,
        "pilot disposition observation")
    req(disp["interpretation"]["timeout_is_resource_wall_not_mathematical_evidence"] is True,
        "timeout firewall")
    req(disp["interpretation"]["blind_timeout_extension_selected_as_next_step"] is False,
        "blind timeout extension selected")
    req(disp["next_exact_step"]["route"] == "INDEPENDENT_EXACT_AFFINE_LATTICE_BACKEND",
        "next exact route")
    req(disp["next_exact_step"]["full343_scaleout_authorized"] is False,
        "full343 scaleout firewall")
    for key in (
        "main_pruning_credit","effectivity_credit","receiver_credit","route_credit",
        "theorem_credit","endpoint_credit","stage32_closed",
        "perfect_cuboid_existence_claim","perfect_cuboid_nonexistence_claim","merge_authorized",
    ):
        req(disp["firewalls"][key] is False, f"pilot disposition firewall {key}")

    print("PASS: retained EFF-CFRR01 pilot is 5/5 BASE_LINEAR timeout, zero-credit, exact-affine successor required")
    print("PASS: Stage32 32-02 EFF-CFRR01 compressed-base4 RR preflight is source-locked and zero-credit")


if __name__ == "__main__":
    main()
