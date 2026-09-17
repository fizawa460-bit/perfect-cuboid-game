#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CERT = HERE / "GRF-09-CUT201-E8-PICARD-PARITY-CHECKPOINT.json"
PROBE = HERE / "probe_grf09_e8_picard_completion_parity.py"
ARCHIVED_MAIN_STATE = ROOT / "stages/stage32/proof/historical-routing-blobs/b8df16056625db5fbb1947f1e927593de258f1ff.json"
CUT201_ROOT = ROOT / ".stage32-cut201"
PASS_MARKER = "PASS_GRF09_CUT201_E8_PICARD_COMPLETION_PARITY_PROBE"
EXPECTED_CERT_CANONICAL = "ddb7787190a8c37d8a913bcd81c39cff471828fd553b91f5268ed4f56dba5646"

CURRENT_FILES = {
    PROBE: "ff3c5037e720561c35fe44649f2faf4dc8c6ef8e",
    ROOT / "stages/stage32-ex5/hpadj-handoff/INTERFACE.json": "8a30e3aa30777460f344eb19836dc725dd442329",
    ROOT / "stages/stage32/residual-32-01-production/compressed_terminal_family.py": "90ff82ed312dcc0cb32cf207935945f550e29170",
    ROOT / "stages/stage32/residual-32-01-production/compressed_terminal_indexer.py": "4fb0a8dd34909494bd62646373e42877ed7a3c9e",
    ROOT / "stages/stage32/residual-32-01-production/pairing_prefix_engine.py": "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",
    ROOT / "stages/stage33/33-07/picard_base_rows_retained.py": "82e4d450a1d852e34f6615440fb88a029c6e54eb",
    ARCHIVED_MAIN_STATE: "b8df16056625db5fbb1947f1e927593de258f1ff",
}
CUT201_FILES = {
    CUT201_ROOT / "stages/stage32/full178-cut/CUT201-e8-common-adapter-wave9-preflight.json": "87b2f139b576b3b8bddea336396c8c2da30014b1",
    CUT201_ROOT / "stages/stage32-ex5/cut-handoff/e8_terminal_population_adapter.py": "6026d2c8b4a2eb69c453a2bd38c5923f46d6d74f",
    CUT201_ROOT / "stages/stage32/residual-32-01-production/compressed_terminal_family.py": "90ff82ed312dcc0cb32cf207935945f550e29170",
    CUT201_ROOT / "stages/stage32/residual-32-01-production/compressed_terminal_indexer.py": "4fb0a8dd34909494bd62646373e42877ed7a3c9e",
}
CUT201_EXACT_HEAD = "118c1df8f33759cc2e4da7e53fb8c8d7463a5bb0"
EXPECTED_INDEX_TO_LABEL = {
    "0": 95,
    "1": 99,
    "2": 103,
    "3": 102,
    "4": 49,
    "5": 97,
    "6": 94,
    "7": 101,
    "8": 93,
    "9": 98,
    "10": 96,
}


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
    return json.loads(path.read_text(encoding="utf-8"))


def parse_probe_output(text: str) -> dict:
    req(PASS_MARKER in text, "GRF-09 PASS marker missing")
    payload = text.split(PASS_MARKER, 1)[0].strip()
    return json.loads(payload)


def load_probe_output(path: Path | None) -> dict:
    if path is not None:
        req(path.is_file(), f"missing probe output: {path}")
        return parse_probe_output(path.read_text(encoding="utf-8"))
    proc = subprocess.run(
        [sys.executable, str(PROBE)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    req(proc.returncode == 0, f"GRF-09 probe failed: {proc.stderr[-2000:]}")
    return parse_probe_output(proc.stdout)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--probe-output", type=Path)
    args = parser.parse_args()

    for path, expected in CURRENT_FILES.items():
        req(path.is_file(), f"missing source lock: {path.relative_to(ROOT)}")
        req(blob(path) == expected, f"source-lock drift: {path.relative_to(ROOT)}")

    req(CUT201_ROOT.is_dir(), "missing source-locked .stage32-cut201 checkout")
    head = subprocess.run(
        ["git", "-C", str(CUT201_ROOT), "rev-parse", "HEAD"],
        text=True,
        capture_output=True,
        check=True,
    ).stdout.strip()
    req(head == CUT201_EXACT_HEAD, "CUT201 exact-head drift")
    for path, expected in CUT201_FILES.items():
        req(path.is_file(), f"missing CUT201 source lock: {path.relative_to(CUT201_ROOT)}")
        req(blob(path) == expected, f"CUT201 source-lock drift: {path.relative_to(CUT201_ROOT)}")

    cert = read_json(CERT)
    stored = cert.pop("canonical_sha256_without_this_field", None)
    req(stored == EXPECTED_CERT_CANONICAL, "GRF-09 checkpoint stored canonical drift")
    req(csha(cert) == EXPECTED_CERT_CANONICAL, "GRF-09 checkpoint canonical drift")
    req(cert["node"] == "GRF-09", "GRF-09 node drift")

    summary = load_probe_output(args.probe_output)
    pop = cert["population_identity"]
    result = cert["exact_result"]

    req(summary["scope"] == "CUT201_g1_d008_e8_SURVIVOR_OFFSETS_2041_2295_INDEPENDENT_MAIN_PARITY_PROBE", "scope drift")
    req(summary["source_cut201_exact_head"] == CUT201_EXACT_HEAD, "summary CUT201 head drift")
    req(summary["source_cut201_preflight_blob"] == cert["source_locks"]["cut201_preflight_blob_sha1"], "summary preflight drift")
    req(summary["source_cut201_adapter_blob"] == cert["source_locks"]["cut201_adapter_blob_sha1"], "summary adapter drift")
    req(summary["survivor_offset_range"] == pop["survivor_offset_range"], "survivor offset drift")
    req(summary["actual_block_index_minmax"] == pop["actual_block_index_minmax"], "actual block min/max drift")
    req(summary["actual_block_index_stream_sha256"] == pop["actual_block_index_stream_sha256"], "actual block stream drift")
    req(summary["block_count"] == pop["block_count"] == 255, "block-count drift")
    req(summary["terminal_count"] == pop["terminal_count"] == 28815, "terminal-count drift")
    req(summary["completion_modulus"] == result["completion_modulus"] == 8, "completion modulus drift")
    req(summary["mask_distribution"] == result["mask_distribution"] == {"0x55": 198, "0xaa": 57}, "mask distribution drift")
    req(summary["affine_gf2_model_count"] == result["affine_gf2_model_count"] == 4, "affine model count drift")
    req(summary["selected_affine_gf2_coefficients"] == result["selected_affine_gf2_coefficients"], "selected affine model drift")
    req(summary["sat_terminal_count"] == result["sat_terminal_count"] == 14478, "SAT count drift")
    req(summary["unsat_terminal_count"] == result["unsat_terminal_count"] == 14337, "UNSAT count drift")
    req(summary["unsat_fraction"] == result["unsat_fraction"] == [14337, 28815], "UNSAT fraction drift")

    even_blocks = int(result["mask_distribution"]["0x55"])
    odd_blocks = int(result["mask_distribution"]["0xaa"])
    req(even_blocks + odd_blocks == 255, "mask block partition drift")
    req(result["sat_terminal_count"] == 57 * even_blocks + 56 * odd_blocks, "SAT parity reconstruction drift")
    req(result["unsat_terminal_count"] == 56 * even_blocks + 57 * odd_blocks, "UNSAT parity reconstruction drift")
    req(result["sat_terminal_count"] + result["unsat_terminal_count"] == 28815, "terminal partition drift")

    coeff = result["selected_affine_gf2_coefficients"]
    req(coeff["constant"] == 0 and coeff["x1"] == 1 and coeff["x9"] == 1, "selected parity identity drift")
    req(sum(int(v) for v in coeff.values()) == 2, "unexpected selected parity support")
    req(result["coordinate_index_to_assignment_label"] == EXPECTED_INDEX_TO_LABEL, "assignment-label map drift")
    req(
        result["selected_model_coordinate_identity"]
        == "coordinate_index_4_mod2 = coordinate_index_1_mod2 XOR coordinate_index_9_mod2",
        "coordinate-index parity identity drift",
    )
    req(
        result["selected_model_assignment_label_identity"]
        == "assignment_label_49_mod2 = assignment_label_99_mod2 XOR assignment_label_98_mod2",
        "assignment-label parity identity drift",
    )

    credit = summary["credit"]
    req(credit["cut201_survivor_offset_identity_proved"], "CUT201 survivor identity not retained")
    req(not credit["current_main_residual_subset_identity_proved"], "unexpected current-MAIN subset identity")
    req(not credit["main_pruning_credit"], "unexpected MAIN pruning credit")
    req(not credit["double_charge_authorized"], "unexpected double-charge authorization")
    req(not credit["full178_complete"], "unexpected FULL178 completion")

    firewall = cert["credit_firewall"]
    for key in (
        "current_main_residual_subset_identity_proved",
        "authority_changed_by_checkpoint",
        "main_pruning_credit",
        "double_charge_authorized",
        "full178_complete",
        "effectivity_released",
        "receiver_credit",
        "theorem_credit",
        "endpoint_credit",
        "stage32_closed",
        "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim",
        "merge_authorized",
    ):
        req(not firewall[key], f"credit firewall drift: {key}")

    # GRF-09 is a retained zero-credit checkpoint from the V24 authority
    # boundary. Replay that authority firewall against the exact archived V24
    # MAIN state rather than the mutable V25 startup projection after N400.
    state = read_json(ARCHIVED_MAIN_STATE)
    frontier = state["current_exact_frontier"]
    req(frontier["authoritative_remaining_strata"] == 17128, "V24 authority strata drift")
    req(frontier["authoritative_remaining_terminals"] == 26876434389242951089388, "V24 authority terminal upper bound drift")
    req(frontier["authoritative_remaining_terminals_semantics"] == "CERTIFIED_UPPER_BOUND_NOT_EXACT_RESIDUAL_IDENTITY_SET", "V24 authority semantics drift")

    cross = cert["independent_arithmetic_cross_check"]
    req(not cross["proof_authority"], "Wolfram cross-check must not become proof authority")
    req(cross["result"] == {"sat": 14478, "unsat": 14337, "total": 28815}, "Wolfram cross-check record drift")

    print(
        "GRF-09 CHECKPOINT PASS: corrected CUT201 survivor-offset slice is frozen at "
        "255 blocks / 28,815 terminals, masks 198:57, SAT 14,478 / UNSAT 14,337; "
        "label-49 parity = label-99 XOR label-98 on the selected model; MAIN pruning credit remains zero."
    )


if __name__ == "__main__":
    main()
