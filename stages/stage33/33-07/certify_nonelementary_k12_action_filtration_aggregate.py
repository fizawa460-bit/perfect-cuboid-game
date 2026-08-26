#!/usr/bin/env python3
"""Aggregate the exhaustive sharded k1/k2 action-filtration census."""
import hashlib
import json
import os
import struct
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = Path(os.environ.get("SHARD_DIR", "."))
NSHARDS = int(os.environ.get("SHARD_COUNT", "16"))
RECORD = struct.Struct("<BHI")
Q2_LOCK = "18d33892d04de286bfa8aa006fb8e4d133d7b51472e950c51bc74cc67a366300"
Q2_BIN_LOCK = "4eebb36004d88917a233a7f449056e9d20082de94018d9ce4b48bbbbfe144c36"
K1_LOCK = "702758b2c085db70b48577531377b5c8dace827f3080f43486fbcf0fd0605cf2"
K2_LOCK = "cfa87933b595744811b8ea2e04bf71ea39b75b0c3a9255437c4bc507b3846a95"
ACTION_LOCK = "a988ea03c86feced95ff41cc5eacb245a5c4e87506bd47848da3125ab16e1f20"
TARGET_LOCK = "4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0"

docs = []
for shard in range(NSHARDS):
    path = ROOT / f"nonelementary-k12-action-filtration-shard-{shard:02d}.json"
    d = json.loads(path.read_text())
    u = dict(d)
    stored = u.pop("canonical_sha256", None)
    rehash = hashlib.sha256(json.dumps(u, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    if stored != rehash:
        raise SystemExit(f"shard hash regression {shard}")
    if d["shard_index"] != shard or d["shard_count"] != NSHARDS:
        raise SystemExit("shard identity regression")
    if d["source_q2_sha256"] != Q2_LOCK or d["source_q2_binary_sha256"] != Q2_BIN_LOCK:
        raise SystemExit("Q2 source lock moved")
    if d["source_k1_skeleton_sha256"] != K1_LOCK or d["source_k2_skeleton_sha256"] != K2_LOCK:
        raise SystemExit("skeleton source lock moved")
    if d["source_action_sha256"] != ACTION_LOCK or d["source_endpoint_sha256"] != TARGET_LOCK:
        raise SystemExit("action/endpoint source lock moved")
    if not d["exact_shard_action_filtration_certified"]:
        raise SystemExit("uncertified shard")
    docs.append(d)

status = Counter()
by_kind = {1: Counter(), 2: Counter()}
input_by_kind = Counter()
survivors = []
shard_hashes = []
for d in docs:
    status.update(d["status_counts"])
    for kind in (1, 2):
        input_by_kind[kind] += int(d["input_count_by_kind"][f"k{kind}"])
        by_kind[kind].update(d["status_counts_by_kind"][f"k{kind}"])
    survivors.extend(d["survivors"])
    shard_hashes.append(d["canonical_sha256"])

if input_by_kind != Counter({1: 28076, 2: 75952}):
    raise SystemExit(f"full input census regression {dict(input_by_kind)}")
if sum(status.values()) != 104028:
    raise SystemExit("full classification coverage regression")
if len(survivors) != status.get("ACTION_FILTRATION_MATCH", 0):
    raise SystemExit("survivor/status mismatch")
ordinals = [int(r["ordinal"]) for r in survivors]
if len(ordinals) != len(set(ordinals)):
    raise SystemExit("duplicate survivor ordinal")
survivors.sort(key=lambda r: int(r["ordinal"]))

binary = b"".join(RECORD.pack(
    int(r["kind"]),
    int(r["skeleton_orbit_index"]),
    int(r["affine_solution_mask"]),
) for r in survivors)
bin_sha = hashlib.sha256(binary).hexdigest()
bin_path = HERE / "nonelementary-k12-action-filtration-survivors.bin"
bin_path.write_bytes(binary)

cert = {
    "schema": "STAGE33_07_NONELEMENTARY_K12_ACTION_FILTRATION_EXACT_V1",
    "source_q2_sha256": Q2_LOCK,
    "source_q2_binary_sha256": Q2_BIN_LOCK,
    "source_k1_skeleton_sha256": K1_LOCK,
    "source_k2_skeleton_sha256": K2_LOCK,
    "source_action_sha256": ACTION_LOCK,
    "source_endpoint_sha256": TARGET_LOCK,
    "shard_count": NSHARDS,
    "shard_certificate_sha256": shard_hashes,
    "input_count": 104028,
    "input_count_by_kind": {"k1": 28076, "k2": 75952},
    "filtration": docs[0]["filtration"],
    "target_cc_fixed_dimensions": docs[0]["target_cc_fixed_dimensions"],
    "target_ct_fixed_dimensions": docs[0]["target_ct_fixed_dimensions"],
    "target_joint_v4_fixed_dimensions": docs[0]["target_joint_v4_fixed_dimensions"],
    "status_counts": dict(sorted(status.items())),
    "status_counts_by_kind": {f"k{k}": dict(sorted(by_kind[k].items())) for k in (1, 2)},
    "survivor_count": len(survivors),
    "survivor_count_by_kind": {
        f"k{k}": sum(int(r["kind"]) == k for r in survivors) for k in (1, 2)
    },
    "survivor_binary_record_struct": "<BHI",
    "survivor_binary_record_size": RECORD.size,
    "survivor_binary_size": len(binary),
    "survivor_binary_sha256": bin_sha,
    "full_action_filtration_exhaustive_certified": True,
    "all_104028_q2_2q_surviving_full_source_symmetry_orbits_classified": True,
    "rejections_are_exact_action_conjugacy_obstructions": True,
    "matches_are_only_necessary_matches": True,
    "endpoint_finite_q_certified": False,
    "endpoint_full_action_certified": False,
    "actual_index512_glue_identified": False,
    "arithmetic_HS_closed": False,
    "stage33_progress": "6/11",
    "stage33_08_released": False,
    "stage33_09_released": False,
    "theorem_credit": False,
    "endpoint_credit": False,
    "perfect_cuboid_nonexistence_claim": False,
    "next_exact_leaf": "L33-07-EXACT-FULL-Q-PLUS-SIMULTANEOUS-V4-ON-ACTION-FILTRATION-SURVIVORS",
}
raw = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(raw).hexdigest()
out = HERE / "nonelementary-k12-action-filtration-certified.json"
out.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "success": True,
    "input": cert["input_count"],
    "status_counts": cert["status_counts"],
    "survivor_count": cert["survivor_count"],
    "survivor_count_by_kind": cert["survivor_count_by_kind"],
    "binary_sha256": bin_sha,
    "certificate_sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
