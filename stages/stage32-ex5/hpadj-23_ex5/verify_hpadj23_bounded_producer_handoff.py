#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
HANDOFF = HERE / "HPADJ23-BOUNDED-PRODUCER-HANDOFF.json"
SERIALIZER = HERE / "serialize_exact_t_histogram.py"
SER_RESULT = HERE / "HPADJ23-COMPACT-SERIALIZATION-BOUNDED-RESULT.json"
BUILDER = HERE / "build_exact_t_joint_histogram.py"
BUILD_RESULT = HERE / "HPADJ23-EXACT-T-BUILDER-BOUNDED-RESULT.json"

EXPECTED = {
    "handoff_blob": "f2c1d998cd1d2cf032bf1e56c94e710dbc80eddb",
    "handoff_canonical": "d31608f8ab1aa9e0c9b11d71c4e560b1fa9f3eef6f26bb2b56145ca937d38615",
    "serializer_blob": "91be480f62de7c8cac63c4ddc37a372cc3fed33d",
    "serialization_result_blob": "30eb5b36f357c0474454189c8ff52549d943f277",
    "serialization_result_canonical": "c1d79706eaa83f67995836c9bddd074da7a246822277897f094ffb0e12b9d041",
    "builder_blob": "c02973cb9d7fdea7584661a9c5935a43e12efe92",
    "builder_result_blob": "7e919c28f3c259cc1db2743c8deb7c82a5c11612",
    "builder_result_canonical": "0ab20358bdcb62c487cd0213b0156f2f7a95875e147e4733e0f65c7d3df72db3",
    "stream_sha256": "fa84df0ba610c8afec76599a93abe46ed0e494cc3544568f03e6669131d1b4f8",
}

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def canon(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()

def locked_json(path: Path, expected_blob: str, expected_canon: str, label: str) -> dict:
    req(path.is_file(), f"missing {label}")
    req(blob(path) == expected_blob, f"{label} blob drift")
    obj = json.loads(path.read_text())
    req(obj.get("canonical_sha256_without_this_field") == expected_canon, f"{label} stored canonical drift")
    req(canon(obj) == expected_canon, f"{label} canonical drift")
    return obj

def main() -> None:
    handoff = locked_json(HANDOFF, EXPECTED["handoff_blob"], EXPECTED["handoff_canonical"], "HPADJ23 handoff")
    ser = locked_json(SER_RESULT, EXPECTED["serialization_result_blob"], EXPECTED["serialization_result_canonical"], "serialization result")
    build = locked_json(BUILD_RESULT, EXPECTED["builder_result_blob"], EXPECTED["builder_result_canonical"], "builder result")
    req(blob(SERIALIZER) == EXPECTED["serializer_blob"], "serializer blob drift")
    req(blob(BUILDER) == EXPECTED["builder_blob"], "builder blob drift")

    req(handoff["status"] == "BOUNDED_EXACT_T_PRODUCER_READY_FOR_178_CONSUMER_PREFLIGHT__FULL178_NOT_READY__ZERO_MAIN_CREDIT", "handoff status")
    req(handoff["producer"]["serialization"]["bounded_result_canonical_sha256"] == EXPECTED["serialization_result_canonical"], "handoff serialization binding")
    req(handoff["producer"]["builder"]["bounded_result_canonical_sha256"] == EXPECTED["builder_result_canonical"], "handoff builder binding")
    req(handoff["producer"]["serialization"]["bounded_H16_stream_sha256"] == EXPECTED["stream_sha256"], "handoff stream binding")
    req(ser["bounded_H16_stream"]["stream_sha256"] == EXPECTED["stream_sha256"], "serialization stream digest")
    req(ser["bounded_H16_stream"]["line_count"] == 47667, "serialization line count")
    req(ser["bounded_H16_stream"]["utf8_bytes"] == 2248811, "serialization byte count")
    req(ser["bounded_H16_stream"]["exact_t_support_entries"] == 207474, "serialization entry count")
    req(build["bounded_H16"]["exact_bins_with_required_parity"] == 47667, "builder/serializer bin count")
    req(build["bounded_H16"]["exact_t_support_entries_with_required_parity"] == 207474, "builder/serializer t-entry count")

    scope = handoff["scope"]
    req(scope["bounded_consumer_equivalence_ready"] is True, "bounded consumer readiness")
    req(scope["full178_producer_complete"] is False, "unexpected FULL178 producer completion")
    req(scope["full178_scaleout_armed"] is False, "unexpected FULL178 scaleout arm")
    req(scope["heavy_execution_authorized"] is False, "unexpected heavy authorization")
    req(scope["full178_consumer_handoff_ready"] is False, "unexpected FULL178 consumer handoff")

    req(all(v is False for v in handoff["firewalls"].values()), "handoff firewall raised")
    req(handoff["target_consumer"]["consumer_must_not_claim_raw_hull_hole_count_as_terminal_saving"] is True, "raw hole saving firewall")
    req(handoff["target_consumer"]["consumer_must_compute_same_population_numeric_effect_separately"] is True, "consumer numeric separation firewall")

    print(json.dumps({
        "verdict": "PASS_HPADJ23_BOUNDED_PRODUCER_HANDOFF",
        "bounded_H": 16,
        "stream_sha256": EXPECTED["stream_sha256"],
        "line_count": 47667,
        "exact_t_entries": 207474,
        "full178_ready": False,
        "main_credit": False,
    }, sort_keys=True))

if __name__ == "__main__":
    main()
