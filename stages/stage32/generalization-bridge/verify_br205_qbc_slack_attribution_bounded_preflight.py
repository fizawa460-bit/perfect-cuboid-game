#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
KERNEL = HERE / "verify_br205_deeper_qbc_same_population_bounded_pilot.cpp"
RESULT = HERE / "BR205-DEEPER-QBC-SAME-POPULATION-BOUNDED-PILOT.json"

EXPECTED_KERNEL_BLOB = "ef6e5b41ed11421d8c48cfbe30be79634bf707b5"
EXPECTED_RESULT_BLOB = "4b5e650bf1b95857959b66dc886ef53319c09d2b"
EXPECTED_K8 = 230_521_553_871
EXPECTED_FULL = 191_776_755_135
EXPECTED_TIGHTENING = 38_744_798_736
EXPECTED_BC_BASE_STATES = 16_781
EXPECTED_TAIL_BASE_STATES = 7_840


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    payload = b"blob " + str(len(raw)).encode() + b"\0" + raw
    return hashlib.sha1(payload).hexdigest()


def main() -> None:
    req(KERNEL.is_file(), "missing BR205 bounded pilot kernel")
    req(RESULT.is_file(), "missing BR205 bounded pilot result")
    req(git_blob(KERNEL) == EXPECTED_KERNEL_BLOB, "BR205 bounded pilot kernel blob drift")
    req(git_blob(RESULT) == EXPECTED_RESULT_BLOB, "BR205 bounded pilot result blob drift")

    source = KERNEL.read_text()
    data = json.loads(RESULT.read_text())

    req(
        data.get("schema") == "STAGE32_BR205_DEEPER_QBC_SAME_POPULATION_BOUNDED_PILOT_V1",
        "BR205 bounded pilot schema drift",
    )
    req(
        data.get("status") == "PASS_STRICT_DEEPER_QBC_BOUNDED_ZERO_CREDIT",
        "BR205 bounded pilot is not retained PASS",
    )

    regression = data.get("regression", {})
    deeper = data.get("deeper_qBC", {})
    tail = data.get("tail_activity", {})
    gate = data.get("transition_gate", {})

    k8 = int(regression.get("K8", -1))
    full = int(deeper.get("FULL", -1))
    tightening = int(deeper.get("K8_minus_FULL", -1))
    tail_base_states = int(tail.get("BC_base_states_with_more_than_8_levels", -1))
    active_cells = int(tail.get("active_K8_tail_evaluation_cells", -1))
    active_mass = int(tail.get("active_K8_tail_multiplicity", -1))

    req(regression.get("BR202_K8_exact_match") is True, "BR202 K8 replay is not exact")
    req(k8 == EXPECTED_K8, "K8 bounded survivor regression")
    req(full == EXPECTED_FULL, "FULL-qBC bounded survivor regression")
    req(tightening == EXPECTED_TIGHTENING, "K8-minus-FULL regression")
    req(k8 - full == tightening, "reported K8-minus-FULL arithmetic mismatch")
    req(tail_base_states == EXPECTED_TAIL_BASE_STATES, "K8 tail base-state regression")
    req(active_cells > 0, "K8 tail has no active evaluation cells")
    req(active_mass > 0, "K8 tail has no active retained multiplicity")
    req(tail.get("qBC_K8_truncation_active_on_nonzero_retained_mass") is True, "tail activity flag false")
    req(gate.get("BR205_authorized") is False, "bounded preflight must not authorize BR205")
    req(gate.get("heavy_compute_authorized") is False, "bounded preflight must not authorize heavy compute")

    # The source blob is locked above.  These exact statements are therefore a
    # source-level proof of where K8-vs-FULL slack can occur:
    #   FULL always charges ep[L], i.e. every exact qBC level;
    #   the K-tier evaluator also charges ep[L] whenever L <= K.
    # For the K8 slot, every BC base state with L <= 8 consequently contributes
    # exactly the same amount to K8 and FULL.  Hence the complete global
    # K8-minus-FULL difference is attributable to the L > 8 population.
    req(
        "const std::array<int,6> Ks{1,2,4,8,16,32};" in source,
        "K8 tier declaration drift",
    )
    req(
        "full+=(i128)AR.mult*ep[L];" in source,
        "FULL exact-level accumulation drift",
    )
    req(
        "if(L<=K)bc=ep[L];else{int j=K-1;bc=ep[j]+(i128)(B.total_mult-pm[j])*f[j];}" in source,
        "K-tier exact/nonexact branch drift",
    )

    non_tail_base_states = EXPECTED_BC_BASE_STATES - tail_base_states
    req(non_tail_base_states == 8_941, "non-tail base-state arithmetic regression")

    out = {
        "schema": "STAGE32_BR205_QBC_SLACK_ATTRIBUTION_BOUNDED_PREFLIGHT_V1",
        "status": "PASS_SOURCE_LOCKED_STRUCTURAL_ATTRIBUTION_ZERO_CREDIT",
        "scope": {
            "H": 16,
            "max_d": 32,
            "population": "BR202_P1_SAME_POPULATION",
            "not_full178_authority": True,
        },
        "source_locks": {
            "bounded_pilot_kernel_git_blob_sha1": EXPECTED_KERNEL_BLOB,
            "bounded_pilot_result_git_blob_sha1": EXPECTED_RESULT_BLOB,
        },
        "partition": {
            "BC_base_states_total": EXPECTED_BC_BASE_STATES,
            "BC_base_states_L_le_8": non_tail_base_states,
            "BC_base_states_L_gt_8": tail_base_states,
        },
        "slack_attribution": {
            "K8": k8,
            "FULL_qBC": full,
            "K8_minus_FULL_global": tightening,
            "K8_minus_FULL_from_L_le_8": 0,
            "K8_minus_FULL_from_L_gt_8": tightening,
            "tail_fraction_of_global_tightening": 1.0,
            "active_tail_evaluation_cells": active_cells,
            "active_tail_retained_multiplicity": active_mass,
            "classification": "ALL_BOUNDED_K8_QBC_SLACK_IS_LOCALIZED_TO_L_GT_8",
        },
        "transition": {
            "bounded_slack_attribution_machinery_ready_for_BR204_certificate_shape": True,
            "bounded_deeper_qBC_strict_improvement_already_passed": True,
            "formal_BR205_gate_passed": False,
            "formal_BR205_remaining_condition": "BR204 exact FULL178 compact survivor certificate must emit the same qBC-tail attribution on its exact population",
            "BR204_FULL178_scaleout_authorized": False,
            "heavy_compute_authorized": False,
            "BR206_authorized": False,
        },
        "credit": {
            "stage32_main": False,
            "source_lane": False,
            "full178_complete": False,
            "theorem": False,
            "effectivity": False,
            "receiver": False,
            "endpoint": False,
            "perfect_cuboid": False,
            "merge": False,
        },
    }
    print(json.dumps(out, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
