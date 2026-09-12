#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]

LOCKS = {
    ROOT / "stages/stage32/32-01-178/nodes/N104/FULL178_COMPLETENESS_REPLAY_CERTIFICATE_ARCHITECTURE.md": "a8ebfa9c734c584aed35c20ab1928b6be8f205eb",
    ROOT / "stages/stage32/residual-32-01-production/full178-manifest.json": "0a46b34e278688240656b4977e9cb7f589e90e06",
    ROOT / "stages/stage32/residual-32-01-production/pairing_prefix_engine.py": "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",
    ROOT / "stages/stage32/residual-32-01-production/hperp_integral_adapter.py": "fb1eb380ca786e42a6b00c5ef454b0e79fdba771",
    ROOT / "stages/stage33/33-07/picard_base_rows_retained.py": "82e4d450a1d852e34f6615440fb88a029c6e54eb",
    ROOT / "stages/stage33/33-07/stage32_picard_marking_retained.py": "5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7",
    ROOT / "stages/stage32/32-01-178/nodes/N359/HOSTILE-AUDIT-PASS.json": "d94ac41e470992e11850a3670295b6a9438cdaea",
}

SCHEMA = "STAGE32_32_01_178_SELECTED64_SURVIVOR_SIDECAR_V1"
PICARD_LOCKS = {
    "stages/stage32/residual-32-01-production/pairing_prefix_engine.py": "c8e87c6598fa1cd7ba1675fc35fa83bea983c94b",
    "stages/stage32/residual-32-01-production/hperp_integral_adapter.py": "fb1eb380ca786e42a6b00c5ef454b0e79fdba771",
    "stages/stage33/33-07/picard_base_rows_retained.py": "82e4d450a1d852e34f6615440fb88a029c6e54eb",
    "stages/stage33/33-07/stage32_picard_marking_retained.py": "5a0708a4ddb171e30d85c5a768e0f14ee0eb05f7",
}

def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def digest(v) -> str:
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def validate(record: dict) -> None:
    required = {
        "schema","row_id","e","terminal_rank","terminal_identity","d",
        "selected64_pairings","picard64_coordinates",
        "selected_pairing_matrix_sha256","gram64_sha256","picard64_coordinates_sha256",
        "witness_source_locks","coverage_source",
    }
    missing = sorted(required - set(record))
    if missing:
        raise ValueError("missing sidecar fields: " + ",".join(missing))
    if record["schema"] != SCHEMA:
        raise ValueError("schema mismatch")
    if not isinstance(record["row_id"], str) or not record["row_id"]:
        raise ValueError("row identity required")
    for key in ("e","terminal_rank","d"):
        if type(record[key]) is not int:
            raise ValueError("exact integer required: " + key)
    if record["e"] < 0 or record["terminal_rank"] < 0 or record["d"] <= 0:
        raise ValueError("invalid e/rank/degree")
    expected_id = f'{record["row_id"]}|e={record["e"]}|rank={record["terminal_rank"]}'
    if record["terminal_identity"] != expected_id:
        raise ValueError("terminal identity is not canonical N104 (row,e,rank)")
    for key in ("selected64_pairings","picard64_coordinates"):
        vec = record[key]
        if not isinstance(vec, list) or len(vec) != 64 or any(type(x) is not int for x in vec):
            raise ValueError("exact 64-vector required: " + key)
    if record["picard64_coordinates_sha256"] != digest(record["picard64_coordinates"]):
        raise ValueError("Picard64 coordinate commitment mismatch")
    if record["witness_source_locks"] != PICARD_LOCKS:
        raise ValueError("Picard witness source locks mismatch")
    if not isinstance(record["coverage_source"], dict):
        raise ValueError("coverage source required")
    if record["coverage_source"].get("identity_contract") != "N104_CANONICAL_INDEXED_TERMINAL_RANK":
        raise ValueError("coverage identity contract mismatch")
    for key in ("selected_pairing_matrix_sha256","gram64_sha256"):
        value = record[key]
        if not isinstance(value, str) or len(value) != 64:
            raise ValueError("sha256 commitment required: " + key)

def main() -> None:
    for path, expected in LOCKS.items():
        actual = blob(path)
        if actual != expected:
            raise ValueError(f"source-lock regression {path}: {actual} != {expected}")

    receipt = json.loads((HERE.parent / "N359" / "HOSTILE-AUDIT-PASS.json").read_text())
    if receipt.get("status") != "PASS" or receipt.get("review_id") != 5184650856:
        raise ValueError("N359 hostile-audit receipt regression")
    if receipt["consumed_counts"]["remaining_terminals"] != 47589703313957134966240:
        raise ValueError("N359 retained frontier regression")

    zero = [0] * 64
    fixture = {
        "schema": SCHEMA,
        "row_id": "g0-d008",
        "e": 8,
        "terminal_rank": 0,
        "terminal_identity": "g0-d008|e=8|rank=0",
        "d": 8,
        "selected64_pairings": zero,
        "picard64_coordinates": zero,
        "selected_pairing_matrix_sha256": "0" * 64,
        "gram64_sha256": "1" * 64,
        "picard64_coordinates_sha256": digest(zero),
        "witness_source_locks": PICARD_LOCKS,
        "coverage_source": {"identity_contract": "N104_CANONICAL_INDEXED_TERMINAL_RANK", "producer_status": "SYNTHETIC_SCHEMA_FIXTURE_ONLY"},
    }
    validate(fixture)

    bad = dict(fixture)
    bad["terminal_identity"] = "route-local-rank-0"
    try:
        validate(bad)
    except ValueError:
        pass
    else:
        raise ValueError("noncanonical terminal identity did not fail closed")

    print(json.dumps({
        "verdict": "PASS_N360_SELECTED64_SURVIVOR_SIDECAR_INTERFACE_PREFLIGHT",
        "n359_hostile_audit_pass": True,
        "canonical_terminal_identity": "(row_id,e,terminal_rank)",
        "sidecar_schema_defined": True,
        "actual_current_survivor_sidecars_emitted": 0,
        "rank_to_selected64_witness_producer_implemented": False,
        "main_pruning_credit": False,
        "full178_complete": False,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
