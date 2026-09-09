#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = HERE / "bc2-01b-runtime-node-coordinate-bridge.json"


def csha(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def parse(x):
    return {"0": 0j, "1": 1+0j, "-1": -1+0j, "i": 1j, "-i": -1j}[x]


def residuals(p):
    a1, a2, a3, b1, b2, b3, c = p
    return (
        b1*b1-a2*a2-a3*a3,
        b2*b2-a3*a3-a1*a1,
        b3*b3-a1*a1-a2*a2,
        c*c-a1*a1-a2*a2-a3*a3,
    )


def main():
    d = json.loads(TARGET.read_text(encoding="utf-8"))
    assert d["schema"] == "STAGE32EX5_BC2_01B_RUNTIME_NODE_COORDINATE_BRIDGE_V1"
    assert d["target"] == "BC2-01B_RUNTIME_NODE_COORDINATE_BRIDGE"
    assert d["status"] == "PASS_CANDIDATE_RETAINED_FOR_AUDIT"
    assert d["coordinate_order"] == ["a1", "a2", "a3", "b1", "b2", "b3", "c"]

    rows = d["rows"]
    assert len(rows) == 48
    assert csha(rows) == d["rows_sha256"]
    assert d["rows_sha256"] == "757b73698652e138ef909fa9c425a1dae8f687d58a8ef3910ab7c1612d374870"

    assert [r["runtime_index_0based"] for r in rows] == list(range(48))
    assert [r["retained_exceptional_index_0based"] for r in rows] == list(range(48))
    assert [r["all140_index_0based"] for r in rows] == list(range(92, 140))

    coords = [tuple(r["canonical_stoll_coordinates"]) for r in rows]
    labels = [r["source_label"] for r in rows]
    assert len(set(coords)) == 48
    assert len(set(labels)) == 48

    family_counts = {}
    for r in rows:
        p = tuple(parse(x) for x in r["canonical_stoll_coordinates"])
        assert len(p) == 7
        assert all(x == 0 for x in residuals(p)), r["runtime_index_0based"]
        first = next((x for x in p if x != 0), None)
        assert first == 1, r["runtime_index_0based"]
        fam = r["source_label"].split(":", 1)[0]
        family_counts[fam] = family_counts.get(fam, 0) + 1

    assert family_counts == {
        "AXIS_X1": 8,
        "AXIS_X2": 8,
        "AXIS_X3": 8,
        "Y1_Z_ZERO": 8,
        "Y2_Z_ZERO": 8,
        "Y3_Z_ZERO": 8,
    }

    v = d["mainbatch_independent_validation"]
    assert v["fingerprint_run_id"] == 34321118868
    assert v["fingerprint_job_id"] == 102367754014
    assert v["observed_map_rows"] == 48
    assert v["observed_every_map_row_identity"] is True
    assert v["reported_runtime_to_retained_bijection"] is True
    assert v["reported_runtime_to_retained_identity_permutation"] is True
    assert v["reported_unique_runtime_fingerprints"] is True
    assert v["reported_unique_retained_fingerprints"] is True
    assert v["reported_success"] is True

    a = d["acceptance_matrix"]
    assert all(a[k] is True for k in (
        "source_48_exact_nodes",
        "runtime_48_exceptional_objects_or_order_independent_adapter",
        "exact_48_to_48_bijection",
        "collision_free",
        "omission_free",
        "reproducible_from_exact_inputs",
        "projective_scale_canonicalization_pass",
        "enumeration_order_not_promoted_to_canonical_geometry",
    ))
    assert a["unresolved_scale_sign_orbit_ambiguity"] is False

    f = d["firewalls"]
    assert all(f[k] is False for k in (
        "full178_span_replay_performed",
        "receiver_credit",
        "stage32_main_credit",
        "Q602_excluded",
        "O210_excluded",
        "theorem_credit",
        "endpoint_credit",
        "merge_authorized",
    ))

    print("BC2_01B_RETAINED_BRIDGE_OK")
    print("rows=48 unique_nodes=48 identity_fingerprint_map=48 source_families=6x8")


if __name__ == "__main__":
    main()
