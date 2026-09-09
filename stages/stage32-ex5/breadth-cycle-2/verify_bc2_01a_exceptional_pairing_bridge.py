#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
PATH = HERE / "bc2-01a-exceptional-pairing-bridge.json"


def canonical_sha256_without_this_field(obj):
    payload = dict(obj)
    expected = payload.pop("canonical_sha256_without_this_field")
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return expected, hashlib.sha256(raw).hexdigest()


def require(cond, msg):
    if not cond:
        raise AssertionError(msg)


data = json.loads(PATH.read_text(encoding="utf-8"))
expected, actual = canonical_sha256_without_this_field(data)
require(expected == actual, f"canonical sha mismatch: {expected} != {actual}")
require(data["schema"] == "STAGE32EX5_BC2_01A_EXCEPTIONAL_PAIRING_BRIDGE_V1", "schema drift")
require(data["leaf"] == "BC2-01A_EXCEPTIONAL_PAIRING_BRIDGE", "leaf drift")
require(data["status"] == "PAIRING_LAST48_BRIDGE_PASS_NODE_COORDINATE_BRIDGE_PENDING", "status drift")

auth = data["authority"]
for key, value in auth.items():
    require(value is False, f"unauthorized authority credit: {key}")

est = data["established"]
require(est["all140_count"] == 140, "all140 count drift")
require(est["normal_indices_0based"] == [0, 91], "normal index split drift")
require(est["exceptional_indices_0based"] == [92, 139], "exceptional index split drift")
require(est["exceptional_count"] == 48, "exceptional count drift")
require(est["aggregate_mass_not_used"] is True, "aggregate mass firewall lost")
require("pairings[92+k] > 0" in est["runtime_support_under_effective_curve_hypothesis"],
        "last48 support rule drift")
require("by construction" in est["known32_calibration_in_same_runtime"],
        "known32 runtime calibration statement drift")

pending = data["pending"]
require(pending["persisted_runtime_node_index_to_exact_projective_coordinate_table_found"] is False,
        "coordinate bridge unexpectedly claimed")
require(pending["btva_projective_span_replay_ready"] is False,
        "BTVA span replay unexpectedly claimed ready")
require("must not be inferred" in pending["reason"], "node-coordinate anti-inference firewall weakened")

fw = data["firewalls"]
for key, value in fw.items():
    require(value is False, f"unsafe firewall value: {key}={value}")

nxt = data["next_leaf"]
require(nxt["id"] == "BC2-01B_RUNTIME_NODE_COORDINATE_BRIDGE", "next leaf drift")
require("48/48 bijection" in nxt["promotion_condition"], "promotion condition weakened")
require("permutation-invariant exact canonicalization" in nxt["promotion_condition"],
        "canonicalization condition weakened")

print("PASS BC2-01A exceptional-pairing bridge contract")
print(f"canonical_sha256={actual}")
print("node_coordinate_bridge=PENDING")
print("stage32_main_credit=NO")
