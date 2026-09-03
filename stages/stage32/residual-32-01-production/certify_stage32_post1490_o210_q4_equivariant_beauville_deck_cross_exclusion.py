#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]


def blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def canonical_sha256(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def load_json_lock(lock: dict) -> dict:
    path = ROOT / lock["path"]
    if "blob_sha1" in lock:
        assert blob_sha1(path) == lock["blob_sha1"]
    doc = json.loads(path.read_text())
    if "canonical_sha256" in lock:
        assert canonical_sha256(doc) == lock["canonical_sha256"]
    return doc


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", required=True)
    args = ap.parse_args()
    cert_path = ROOT / args.check
    cert = json.loads(cert_path.read_text())
    assert cert["schema"] == "STAGE32_POST1490_O210_Q4_EQUIVARIANT_BEAUVILLE_DECK_CROSS_EXCLUSION_V1"
    assert canonical_sha256(cert) == cert["canonical_sha256_without_this_field"]
    locks = cert["source_locks"]

    witness = load_json_lock(locks["exact_v6_witness"])
    assert witness["witness"]["picard_coordinates_sha256"] == locks["exact_v6_witness"]["picard_coordinates_sha256"]
    assert witness["witness"]["self_intersection"] == 758
    pairings = [int(x) for x in witness["witness"]["all140_pairings"]]
    assert len(pairings) == 140
    assert sum(m*m for m in pairings[-48:]) == 2358

    rel = load_json_lock(locks["relative_h_node_action"])
    ma = rel["marked_node_action"]
    assert ma["all_three_involutions"] is True
    assert ma["u_v_commute_and_compose_to_uv"] is True
    assert ma["all_nonidentity_fixed_point_free_on_48_nodes"] is True
    assert rel["modular_to_stoll"]["u=TTprime"] == "g7*g9"
    assert rel["modular_to_stoll"]["v=RT"] == "g7*g8"
    assert rel["modular_to_stoll"]["uv=RTprime"] == "g8*g9"

    self_adapter = load_json_lock(locks["beauville_self_adapter"])
    assert self_adapter["x_side_exact_lock"]["D_square"] == 3874
    assert self_adapter["x_side_exact_lock"]["delta_D"] == 2018

    defect = load_json_lock(locks["v4_defect"])
    ia = defect["intersection_arithmetic"]
    assert ia["half_intersection_definition"] == "c_t=D.t(D)/2"
    assert ia["deck_translate_intersection_sum_formula"] == "sum_{t!=1} D.t(D)=17172-2*delta_D"

    for name in ["relative_h_source_note", "beauville_self_source_note", "equivariant_source_note", "picard_recovery_helper", "diagnostic"]:
        path = ROOT / locks[name]["path"]
        assert blob_sha1(path) == locks[name]["blob_sha1"]

    note = (ROOT / locks["equivariant_source_note"]["path"]).read_text()
    for needle in [
        "pi o t_h = bar t_h o pi",
        "D . t(D) = 2 * C . bar t(C) + sum_j m_j m_{t(j)}",
        "sum_{t!=1} D.t(D) = 11932",
        "17172 - 4036 = 13136",
        "13136 - 11932 = 1204",
    ]:
        assert needle in note

    # Independent exact replay of the retained Picard reconstruction and the
    # three composite deck actions. The imported Stage33 helper prints its own
    # audit block first; the diagnostic JSON is intentionally the final line.
    diag_path = ROOT / locks["diagnostic"]["path"]
    proc = subprocess.run([sys.executable, str(diag_path)], cwd=ROOT, text=True, capture_output=True, check=True, timeout=180)
    lines = [line for line in proc.stdout.splitlines() if line.strip()]
    diag = json.loads(lines[-1])
    assert diag["canonical_sha256_without_this_field"] == locks["diagnostic"]["diagnostic_canonical_sha256"]
    assert canonical_sha256(diag) == locks["diagnostic"]["diagnostic_canonical_sha256"]
    assert diag["exact_v6_recovery"]["all140_pairings_replayed"] is True
    assert diag["exact_v6_recovery"]["self_square"] == 758

    expected = cert["exact_cross"]
    for t in ["u", "v", "uv"]:
        got = diag["deck_cross"][t]
        exp = expected[t]
        assert got["B_C_dot_tC"] == exp["C_dot_tC"]
        assert got["exceptional_mass_cross"] == exp["exceptional_cross"]
        assert got["X_D_dot_tD"] == exp["D_dot_tD"]
        assert got["c_t"] == exp["c_t"]

    computed_D_sum = sum(expected[t]["D_dot_tD"] for t in ["u", "v", "uv"])
    computed_c_sum = sum(expected[t]["c_t"] for t in ["u", "v", "uv"])
    assert computed_D_sum == expected["computed_D_translate_sum"] == 11932
    assert computed_c_sum == expected["computed_c_sum"] == 5966

    # Identity specialization checks the sign and normalization of the
    # polarized blow-up formula against the already certified self adapter.
    ident = cert["equivariant_adapter"]["identity_specialization"]
    assert 2*ident["C_square"] + ident["exceptional_square_sum"] == ident["D_square"] == 3874

    xc = cert["independent_x_constraint"]
    required_D_sum = 17172 - 2*xc["delta_D"]
    assert required_D_sum == xc["required_D_translate_sum"] == 13136
    assert required_D_sum // 2 == xc["required_c_sum"] == 6568
    assert required_D_sum - computed_D_sum == xc["full_intersection_gap"] == 1204
    assert xc["required_c_sum"] - computed_c_sum == xc["half_intersection_gap"] == 602
    assert computed_D_sum != required_D_sum

    dec = cert["decision"]
    assert dec["independent_x_defect_sum_contradicted"] is True
    assert dec["O210_q4_exact_v6_carrier_excluded"] is True
    assert dec["effectivity_proved"] is False
    assert cert["firewalls"]["arbitrary_B_picard64_promoted_to_picX"] is False
    assert cert["firewalls"]["post21bl_representative_sample_substituted"] is False
    assert cert["firewalls"]["full178_authorized"] is False

    print("PASS_EXACT_EQUIVARIANT_BEAUVILLE_DECK_CROSS_O210_Q4_EXCLUSION")


if __name__ == "__main__":
    main()
