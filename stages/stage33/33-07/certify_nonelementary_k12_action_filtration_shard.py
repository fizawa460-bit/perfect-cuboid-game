#!/usr/bin/env python3
"""Exact sharded action-filtration census on all retained non-elementary k1/k2 Q2+2Q survivors.

Each shard reconstructs its assigned exact H <= A0, transports every retained
cc/ct action class to Q=H^perp/H, and applies conjugacy-invariant fixed-dimension
signatures on the characteristic filtration
    Q[2] >= Q[2] cap 2Q >= Q[2] cap 4Q.
Rejections are exact necessary-condition failures for simultaneous endpoint
action conjugacy. Matches are retained only; they do not certify full finite-q
or action conjugacy.
"""
import hashlib
import json
import os
import runpy
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_PREFIX = HERE / "nonelementary-k12-action-filtration-shard"
Q2_LOCK = "18d33892d04de286bfa8aa006fb8e4d133d7b51472e950c51bc74cc67a366300"
Q2_BIN_LOCK = "4eebb36004d88917a233a7f449056e9d20082de94018d9ce4b48bbbbfe144c36"
K1_LOCK = "702758b2c085db70b48577531377b5c8dace827f3080f43486fbcf0fd0605cf2"
K2_LOCK = "cfa87933b595744811b8ea2e04bf71ea39b75b0c3a9255437c4bc507b3846a95"
ACTION_LOCK = "a988ea03c86feced95ff41cc5eacb245a5c4e87506bd47848da3125ab16e1f20"
TARGET_LOCK = "4ca7567205455175a5f9bef7a74bc9ec31cd68f831aec60aa88a637b5c0cfdf0"

old = os.environ.get("SAMPLE_PER_KIND")
os.environ["SAMPLE_PER_KIND"] = "0"
ns = runpy.run_path(str(HERE / "scout_nonelementary_k12_action_filtration.py"))
if old is None:
    os.environ.pop("SAMPLE_PER_KIND", None)
else:
    os.environ["SAMPLE_PER_KIND"] = old

reconstruct_rows = ns["reconstruct_rows"]
verify_isotropic = ns["verify_isotropic"]
subgroup = ns["subgroup"]
quotient_context = ns["quotient_context"]
classes = ns["classes"]
sig = ns["sig"]
jsig = ns["jsig"]
compose = ns["compose"]
TCC = tuple(ns["TCC"])
TCT = tuple(ns["TCT"])
TJ = tuple(ns["TJ"])
all_records = ns["all_records"]

if ns["Q2_LOCK"] != Q2_LOCK or ns["Q2_BIN_LOCK"] != Q2_BIN_LOCK:
    raise SystemExit("Q2 lock moved")
if ns["ACTION_LOCK"] != ACTION_LOCK or ns["TARGET_LOCK"] != TARGET_LOCK:
    raise SystemExit("action/target lock moved")
k1src = json.loads((HERE / "nonelementary-k1-q2-2q-cc-orbits.json").read_text())
k2src = json.loads((HERE / "nonelementary-k2-q2-2q-skeleton-orbits.json").read_text())
if k1src.get("canonical_sha256") != K1_LOCK:
    raise SystemExit("k1 skeleton source moved")
if k2src.get("canonical_sha256") != K2_LOCK:
    raise SystemExit("k2 skeleton source moved")
if len(all_records[1]) != 28076 or len(all_records[2]) != 75952:
    raise SystemExit("retained-record census moved")

shard = int(os.environ["SHARD_INDEX"])
nshards = int(os.environ["SHARD_COUNT"])
if not (0 <= shard < nshards) or nshards <= 0:
    raise SystemExit("bad shard configuration")

status = Counter()
by_kind = {1: Counter(), 2: Counter()}
input_by_kind = Counter()
survivors = []

for kind in (1, 2):
    for local_index, record in enumerate(all_records[kind]):
        if local_index % nshards != shard:
            continue
        ordinal, sk, sol = record
        input_by_kind[kind] += 1
        rows = reconstruct_rows(kind, sk, sol)
        verify_isotropic(rows)
        H = subgroup(rows, kind)
        B, Bi, T, Ti = quotient_context(rows)

        cc = classes(rows, "cc", B, Bi, T, Ti, H)
        cm = [i for i, (A, mult) in enumerate(cc) if sig(A) == TCC]
        if not cm:
            label = "REJECT_CC_FILTRATION"
            status[label] += 1
            by_kind[kind][label] += 1
            continue

        ct = classes(rows, "ct", B, Bi, T, Ti, H)
        tm = [i for i, (A, mult) in enumerate(ct) if sig(A) == TCT]
        if not tm:
            label = "REJECT_CT_FILTRATION"
            status[label] += 1
            by_kind[kind][label] += 1
            continue

        pair_count = 0
        for ci in cm:
            for ti in tm:
                A = cc[ci][0]
                C = ct[ti][0]
                if compose(A, C) == compose(C, A) and jsig(A, C) == TJ:
                    pair_count += 1
        if not pair_count:
            label = "REJECT_JOINT_V4_FILTRATION"
            status[label] += 1
            by_kind[kind][label] += 1
            continue

        label = "ACTION_FILTRATION_MATCH"
        status[label] += 1
        by_kind[kind][label] += 1
        survivors.append({
            "kind": int(kind),
            "ordinal": int(ordinal),
            "skeleton_orbit_index": int(sk),
            "affine_solution_mask": int(sol),
            "matching_cc_classes": len(cm),
            "matching_ct_classes": len(tm),
            "matching_joint_pairs": int(pair_count),
        })

expected = sum((len(all_records[k]) + nshards - 1 - shard) // nshards for k in (1, 2))
if sum(input_by_kind.values()) != expected:
    raise SystemExit("shard partition coverage regression")
if sum(status.values()) != expected:
    raise SystemExit("shard classification coverage regression")

cert = {
    "schema": "STAGE33_07_NONELEMENTARY_K12_ACTION_FILTRATION_SHARD_V1",
    "source_q2_sha256": Q2_LOCK,
    "source_q2_binary_sha256": Q2_BIN_LOCK,
    "source_k1_skeleton_sha256": K1_LOCK,
    "source_k2_skeleton_sha256": K2_LOCK,
    "source_action_sha256": ACTION_LOCK,
    "source_endpoint_sha256": TARGET_LOCK,
    "shard_index": shard,
    "shard_count": nshards,
    "partition_rule": "within-kind local record index modulo shard_count",
    "input_count": expected,
    "input_count_by_kind": {f"k{k}": input_by_kind[k] for k in (1, 2)},
    "filtration": "Q[2] >= Q[2] cap 2Q >= Q[2] cap 4Q",
    "target_cc_fixed_dimensions": list(TCC),
    "target_ct_fixed_dimensions": list(TCT),
    "target_joint_v4_fixed_dimensions": list(TJ),
    "status_counts": dict(sorted(status.items())),
    "status_counts_by_kind": {f"k{k}": dict(sorted(by_kind[k].items())) for k in (1, 2)},
    "survivor_count": len(survivors),
    "survivors": survivors,
    "exact_shard_action_filtration_certified": True,
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
}
raw = json.dumps(cert, sort_keys=True, separators=(",", ":")).encode()
cert["canonical_sha256"] = hashlib.sha256(raw).hexdigest()
out = Path(f"{OUT_PREFIX}-{shard:02d}.json")
out.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
print(json.dumps({
    "success": True,
    "shard": shard,
    "input": expected,
    "status_counts": cert["status_counts"],
    "survivors": len(survivors),
    "sha256": cert["canonical_sha256"],
}, indent=2, sort_keys=True))
