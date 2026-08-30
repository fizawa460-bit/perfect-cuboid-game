#!/usr/bin/env python3
from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import json
import math
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
REPO_ROOT = ROOT.parents[2]
MANIFEST = ROOT / "full178-manifest.json"
PREFLIGHT = ROOT / "full178-production-preflight.json"
AUDITED_STATE = REPO_ROOT / "stages/stage32/post-b16-residual-feasibility/state.json"
AUDITED_PAYLOAD_SHA256 = "e787c75b845b691c934fcba5a09a1a76c3c95a82a2deb6563bb7e8fbcd636897"
EXCLUDED_ROW_IDS = {"g0-d002", "g0-d004", "g0-d006", "g1-d004", "g1-d006"}


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def parse_row_id(row_id: str) -> tuple[int, int]:
    g, d = row_id.split("-")
    return int(g[1:]), int(d[1:])


def row_id(genus: int, degree: int) -> str:
    return f"g{genus}-d{degree:03d}"


def load_audited_rows() -> tuple[list[dict], dict]:
    state = json.loads(AUDITED_STATE.read_text())
    assert state["schema"] == "STAGE32_POST_B16_RESIDUAL_FEASIBILITY_STATE_V2_HOSTILE_AUDIT_PASS"
    assert state["hostile_audit"]["review_id"] == 5055351647
    assert state["hostile_audit"]["verdict"] == "PASS_RESIDUAL_FEASIBILITY_GATE_SCOPE_LOCKED"
    analyzer_rel = state["static_analyzer"]["path"]
    assert state["static_analyzer"]["expected_payload_sha256"] == AUDITED_PAYLOAD_SHA256
    assert state["static_analyzer"]["row_count"] == 183
    analyzer = REPO_ROOT / analyzer_rel
    spec = importlib.util.spec_from_file_location("stage32_audited_residual_feasibility", analyzer)
    assert spec is not None and spec.loader is not None
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    assert mod.payload["payload_sha256"] == AUDITED_PAYLOAD_SHA256
    rows = list(mod.audited_rows())
    assert len(rows) == 183
    assert sum(r["genus"] == 0 for r in rows) == state["static_analyzer"]["g0_rows"] == 88
    assert sum(r["genus"] == 1 for r in rows) == state["static_analyzer"]["g1_rows"] == 95
    return rows, state


def main() -> None:
    audited_rows, audited_state = load_audited_rows()
    audited_ids = {row_id(r["genus"], r["degree"]) for r in audited_rows}
    assert EXCLUDED_ROW_IDS <= audited_ids
    residual_source_rows = [
        (r["genus"], r["degree"])
        for r in audited_rows
        if row_id(r["genus"], r["degree"]) not in EXCLUDED_ROW_IDS
    ]
    assert len(residual_source_rows) == audited_state["coarse_partition"]["residual_rows"] == 178

    manifest = json.loads(MANIFEST.read_text())
    expected_hash = manifest.pop("canonical_sha256_without_this_field")
    assert csha(manifest) == expected_hash
    manifest["canonical_sha256_without_this_field"] = expected_hash
    assert set(manifest["audited_source"]["exclude_degree_le_6"]) == EXCLUDED_ROW_IDS

    seen = []
    counts = {}
    strata = 0
    max_norm = (-1, None)
    for m_text, ids in manifest["m_class_rows"].items():
        m = int(m_text)
        counts[m_text] = len(ids)
        for rid in ids:
            genus, degree = parse_row_id(rid)
            r = math.gcd(degree, 16)
            assert m == 16 // r
            norm = m * m * (degree * degree + 16 * degree + (32 if genus == 0 else 0))
            assert norm % 16 == 0
            norm //= 16
            if norm > max_norm[0]:
                max_norm = (norm, rid)
            emin = 8 if genus == 0 else 4
            emax = (19 * degree) // 5
            strata += max(0, emax - emin + 1)
            seen.append((genus, degree))

    assert sorted(seen) == sorted(residual_source_rows)
    assert len(seen) == len(set(seen)) == 178
    assert counts == {"1": 23, "2": 23, "4": 44, "8": 88}
    assert strata == manifest["coarse_strata_count"] == audited_state["coarse_partition"]["filtered_exceptional_mass_strata"] == 64111
    assert max_norm == (156560, "g1-d190")

    preflight = json.loads(PREFLIGHT.read_text())
    provenance = preflight["source_provenance"]
    assert provenance["audited_state"] == "stages/stage32/post-b16-residual-feasibility/state.json"
    assert provenance["audited_analyzer"] == audited_state["static_analyzer"]["path"]
    assert provenance["audited_payload_sha256"] == AUDITED_PAYLOAD_SHA256
    assert provenance["audited_row_count"] == 183
    assert set(provenance["excluded_degree_le_6_row_ids"]) == EXCLUDED_ROW_IDS
    assert provenance["derivation"] == "AUDITED_183_ROWS_MINUS_EXACTLY_FIVE_AUDITED_DEGREE_LE_6_ROWS"
    assert preflight["manifest_sha256"] == expected_hash
    assert preflight["residual_row_count"] == 178
    assert preflight["coarse_strata_count"] == 64111
    assert preflight["production_policy"]["first_pass_node_ceiling"] == 64000000
    assert preflight["effective_heavy_concurrency"] == 17
    assert preflight["wave_policy"]["effective_heavy_concurrency"] == 17
    assert preflight["effective_heavy_concurrency"] <= 18
    assert preflight["projected_peak_artifact_mb"] < 500
    assert preflight["raw_evidence_persisted"] is False
    assert preflight["full_178_heavy_sweep_authorized"] is False
    assert preflight["heavy_compute_armed"] is False
    assert preflight["unknown_is_unsat"] is False
    assert preflight["B18_RELEASE_AUTHORIZED"] is False
    assert preflight["THEOREM_CREDIT"] is False
    assert preflight["RECEIVER_CREDIT"] is False

    print(json.dumps({
        "audited_payload_sha256": AUDITED_PAYLOAD_SHA256,
        "audited_rows": len(audited_rows),
        "excluded_rows": sorted(EXCLUDED_ROW_IDS),
        "manifest_sha256": expected_hash,
        "residual_rows": len(seen),
        "m_class_counts": counts,
        "coarse_strata_count": strata,
        "max_hperp_norm_bound": max_norm[0],
        "max_row": max_norm[1],
        "node_ceiling_per_work_unit": preflight["production_policy"]["first_pass_node_ceiling"],
        "effective_heavy_concurrency": preflight["effective_heavy_concurrency"],
        "source_provenance_lock": "PASS",
        "preflight_verdict": "PASS_COLD_PREFLIGHT_STATIC_CONTRACT_WITH_AUDITED_SOURCE_PROVENANCE",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
