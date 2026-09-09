#!/usr/bin/env python3
"""Reconstruct the Stage33-11g exact-exit candidate on the repaired 47-prime inventory."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE33 = HERE.parent
G_CERT = HERE / "e3-v91c1x-r5b3b3c4b2b2g-repaired-stage33-11f-26-column-closure.json"
STATE = STAGE33 / "MAIN-STATE.json"
OUT = HERE / "e3-v91c1x-r5b3b3c4b2b2h-repaired-stage33-11g-exact-exit.json"

G_SHA = "e9b3bad7d1c74d40e0a4114659e4e2bb9c5866f1548a28204e3e2dd11ad2ed32"
G_AUDIT_REVIEW = 5151676010
G_AUDITED_HEAD = "8edfc08159cca1b95815278317873488075657f1"
AUTH = "V91C1V_A2_02_ACTUAL_PRIME_KNOWN140_LOCATOR_BOUNDED_RESULT"
CANDIDATE = "V91C1X_R5B3B3C4B2B2H_REPAIRED_STAGE33_11G_EXACT_EXIT"
NEXT = "V91C1X_R5B3B3C4B2B2H_REPAIRED_STAGE33_11G_EXACT_EXIT_HOSTILE_AUDIT"


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_checked(path: Path, expected: str | None = None):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    actual = csha(body)
    if claimed != actual:
        raise SystemExit(f"canonical certificate mismatch: {path}")
    if expected is not None and claimed != expected:
        raise SystemExit(f"locked canonical sha moved: {path}")
    return obj


def assert_consumed_audit(state: dict):
    wc = state.get("work_checkpoint", {})
    required = {
        "authority": "OPERATIONAL_ONLY_NOT_PROOF",
        "consumed_c4b2b2g_hostile_audit_review": G_AUDIT_REVIEW,
        "consumed_c4b2b2g_hostile_audit_exact_head": G_AUDITED_HEAD,
        "repaired_stage33_11f_26_column_closure_materialized": True,
        "repaired_stage33_11f_26_column_closure_audited": True,
        "repaired_stage33_11f_exact_audited_connecting_columns": "26/26",
        "historical_stage33_11f_26_column_closure_reuse_allowed": False,
        "historical_stage33_11g_44_prime_exact_exit_reuse_allowed": False,
        "stage33_11_closed_exact": False,
        "pr": 1722,
    }
    for key, value in required.items():
        if wc.get(key) != value:
            raise SystemExit(f"consumed C4B2B2G audit/state lock moved: {key}")
    if state.get("stage33_progress") != "6/11":
        raise SystemExit("Stage33 progress moved")
    if state.get("authority_sync", {}).get("frontier_authority") != AUTH:
        raise SystemExit("Stage33 mathematical authority moved")
    return wc


def audit_g_certificate(g: dict):
    if g.get("candidate") != "V91C1X_R5B3B3C4B2B2G_REPAIRED_STAGE33_11F_26_COLUMN_CLOSURE":
        raise SystemExit("C4B2B2G candidate identity moved")
    if g.get("entry") != {"authority": AUTH, "stage33_progress": "6/11", "successor_pr": 1722}:
        raise SystemExit("C4B2B2G authority/progress/PR entry moved")

    inv = g["repair_inventory"]
    if inv["repaired_distinct_prime_inventory_count"] != 47:
        raise SystemExit("repaired prime inventory is not 47")
    if inv["historical_prime_inventory_count"] != 44:
        raise SystemExit("historical inventory count moved")
    if inv["historical_nonprime_direct_support_ids_removed"] != 9:
        raise SystemExit("pseudo-prime removal count moved")
    if inv["historical_pseudo_prime_ids_absent_from_repaired_inventory"] is not True:
        raise SystemExit("historical pseudo-prime IDs leaked into repaired inventory")
    if inv["cc_ct_actions_total_on_repaired_inventory"] is not True:
        raise SystemExit("cc/ct are not total on repaired inventory")
    if inv["all_generator_component_prime_ids_inside_repaired_inventory"] is not True:
        raise SystemExit("generator package escaped repaired inventory")

    adapter = g["exact_adapter"]
    if adapter["historical_44_slot_prime_inventory_reused_as_is"] is not False:
        raise SystemExit("historical 44-slot inventory reuse firewall moved")
    if adapter["historical_source_orbit_spans_recomputed"] is not True:
        raise SystemExit("source orbit spans were not recomputed")
    if adapter["historical_source_orbit_spans_match_exactly"] is not True:
        raise SystemExit("source orbit span mismatch")
    if adapter["repaired_generator_prime_vectors_consumed"] is not True:
        raise SystemExit("repaired generator prime vectors not consumed")
    if adapter["no_receiver_splitting_used"] is not True or adapter["finite_v4_shortcut_used"] is not False:
        raise SystemExit("receiver/finite-V4 firewall moved")

    summary = g["summary"]
    if summary["repaired_exact_generator_inputs"] != "14/14":
        raise SystemExit("repaired generator input count moved")
    if summary["named_source_directions"] != 26:
        raise SystemExit("source dimension moved")
    if summary["repaired_exact_main_connecting_columns"] != "26/26":
        raise SystemExit("repaired MAIN columns incomplete")
    if summary["unresolved_connecting_columns"] != 0:
        raise SystemExit("unresolved repaired connecting columns remain")
    if summary["connecting_map_repaired_main_value"] != "ZERO_EXACT_ALL_26_COLUMNS_ON_REPAIRED_47_PRIME_INVENTORY":
        raise SystemExit("repaired MAIN connecting-map value moved")
    if summary["stage33_11_closed_exact"] is not False:
        raise SystemExit("C4B2B2G unexpectedly carried Stage33-11 close credit")

    columns = g["columns"]
    if len(columns) != 26 or {c["column_1based"] for c in columns} != set(range(1, 27)):
        raise SystemExit("C4B2B2G column inventory is not exactly 1..26")

    replay = []
    for col in sorted(columns, key=lambda c: c["column_1based"]):
        i = col["column_1based"]
        expected_basis = [int(j == i - 1) for j in range(26)]
        if col["source_basis_name"] != f"A2_{i:02d}" or col["source_basis_vector_f2"] != expected_basis:
            raise SystemExit(f"source basis moved at column {i}")
        if col["unresolved"] is not False or col["status"] != "ZERO_EXACT_REPAIRED_11F_MAIN":
            raise SystemExit(f"column {i} is not exact-zero MAIN evidence")
        if col["prime_level_galois_difference_cc"] != "ZERO_EXACT_REPAIRED_PRIME_LEVEL":
            raise SystemExit(f"column {i} cc difference moved")
        if col["prime_level_galois_difference_ct"] != "ZERO_EXACT_REPAIRED_PRIME_LEVEL":
            raise SystemExit(f"column {i} ct difference moved")
        transport = col["source_transport"]
        if transport["kind"] not in {"DIRECT_EXACT_GENERATOR", "CERTIFIED_F2_ORBIT_SPAN"}:
            raise SystemExit(f"column {i} source transport is not exact")
        if col["historical_source_transport_identical"] is not True:
            raise SystemExit(f"column {i} source adapter drifted")
        recv = col["absolute_receiver_value"]
        if recv != {
            "X_Q_power_5": "ZERO",
            "X_Q_i_power_3": "ZERO",
            "E_L": "ZERO_CLASS",
            "E_L_filtration_subobject": "ZERO",
            "E_L_filtration_quotient": "ZERO",
            "E_L_splitting_used": False,
        }:
            raise SystemExit(f"column {i} receiver value moved")
        replay.append({
            "column_1based": i,
            "source_basis_name": col["source_basis_name"],
            "exact_zero_generator": col["exact_zero_generator"],
            "repaired_generator_package_prime_vector_sha256": col["repaired_generator_package_prime_vector_sha256"],
            "transport_kind": transport["kind"],
            "absolute_receiver_status": "ZERO_EXACT_NO_E_L_SPLITTING",
        })
    return replay


def build_certificate():
    g = load_checked(G_CERT, G_SHA)
    state = load_checked(STATE)
    assert_consumed_audit(state)
    replay = audit_g_certificate(g)

    cert = {
        "schema": "stage33.e3.v91c1x.r5b3b3c4b2b2h.repaired_stage33_11g_exact_exit.v1",
        "candidate": CANDIDATE,
        "role": "EXACT_NONCREDIT_STAGE33_11G_EXIT_RECONSTRUCTION_ON_HOSTILE_AUDITED_REPAIRED_47_ACTUAL_PRIME_INVENTORY",
        "entry": {
            "authority": AUTH,
            "stage33_progress": "6/11",
            "successor_pr": 1722,
        },
        "source_locks": {
            "c4b2b2g_repaired_stage33_11f_sha256": G_SHA,
            "c4b2b2g_hostile_audit_review": G_AUDIT_REVIEW,
            "c4b2b2g_hostile_audit_exact_head": G_AUDITED_HEAD,
            "stage33_11f_source_lock_sha256": g["source_locks"]["stage33_11f_source_lock_sha256"],
            "stage33_10_absolute_receiver_handoff_sha256": g["source_locks"]["stage33_10_absolute_receiver_handoff_sha256"],
        },
        "inventory_boundary": {
            "canonical_actual_height_one_prime_inventory": 47,
            "historical_pseudo_prime_ids_removed": 9,
            "historical_44_slot_prime_inventory_reused_as_is": False,
            "historical_stage33_11g_44_prime_exact_exit_reused_as_is": False,
            "cc_ct_total_on_repaired_inventory": True,
            "repaired_generator_inputs": "14/14",
        },
        "exact_exit_reconstruction": {
            "source_dimension_f2": 26,
            "source_basis_columns_checked": "26/26",
            "connecting_columns_exact_main": "26/26",
            "connecting_columns_exact_hostile_audited_upstream": "26/26",
            "unresolved_connecting_columns": 0,
            "linearity_step": "ZERO_ON_ALL_26_NAMED_F2_BASIS_COLUMNS_IMPLIES_ZERO_CONNECTING_HOMOMORPHISM",
            "arithmetic_localization_connecting_map_candidate": "COMPUTED_EXACT_ZERO_MAP_ON_REPAIRED_47_ACTUAL_PRIME_INVENTORY",
            "stage33_11_exact_exit_condition_reconstructed": True,
            "stage33_11_closed_exact_candidate": True,
        },
        "independent_exit_replay": {
            "columns": replay,
            "all_26_basis_columns_zero_in_absolute_receiver": True,
            "E_L_splitting_used": False,
            "finite_v4_shortcut_used": False,
            "carrier_level_substitute_used": False,
            "historical_pseudo_prime_substitute_used": False,
        },
        "absolute_receiver": g["absolute_receiver"],
        "operational_credit": {
            "hostile_audit_required": True,
            "hostile_audit_passed": False,
            "repaired_stage33_11g_exact_exit_materialized": True,
            "repaired_stage33_11g_exact_exit_audited": False,
            "stage33_11_closed_exact": False,
            "status": "MAIN_COMPLETE_EXACT_EXIT_CANDIDATE_PENDING_HOSTILE_AUDIT",
            "next_exact_leaf": NEXT,
        },
        "audit_debt": [
            "Fresh hostile audit must independently verify the C4B2B2G exact-head PASS consumption and all 26 repaired column-to-exit witnesses.",
            "The historical Stage33-11g 44-prime exact-exit certificate is not reused as proof; only the exact-exit criterion is reconstructed from the audited repaired 47-prime evidence.",
            "Stage33-11 exact close remains false operationally until this C4B2B2H exact-exit candidate receives hostile PASS at its exact head.",
        ],
        "credit_firewall": {
            "authority_promotion": False,
            "stage33_11_close_credit": False,
            "stage33_12_release_credit": False,
            "stage33_close_credit": False,
            "stage33_release_credit": False,
            "unramifiedness_credit": False,
            "offboundary_cancellation_credit": False,
            "marked_brauer_image_credit": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "endpoint_credit": False,
            "merge_allowed": False,
            "perfect_cuboid_credit": False,
        },
    }
    cert["canonical_sha256"] = csha(cert)
    return cert


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    cert = build_certificate()
    if args.write:
        OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    elif not OUT.exists() or json.loads(OUT.read_text(encoding="utf-8")) != cert:
        raise SystemExit("recorded C4B2B2H certificate differs; regenerate and review")
    print("STAGE33_C4B2B2H_REPAIRED_11G_EXACT_EXIT_CANDIDATE=PASS")
    print("CONNECTING_COLUMNS_EXACT_MAIN=26/26")
    print("CONNECTING_COLUMNS_EXACT_HOSTILE_AUDITED_UPSTREAM=26/26")
    print("UNRESOLVED_CONNECTING_COLUMNS=0")
    print("STAGE33_11_EXACT_EXIT_CONDITION_RECONSTRUCTED=true")
    print("STAGE33_11_CLOSED_EXACT=false")
    print("CERTIFICATE_SHA256=" + cert["canonical_sha256"])


if __name__ == "__main__":
    main()
