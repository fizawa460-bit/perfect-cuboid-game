#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCAL = ROOT / ".local-stage32-full178-heavy"
EXEC_ROOT = LOCAL / "exec-repo"
SOURCE_ROOT = LOCAL / "source-lf"
WORKER_PATH = EXEC_ROOT / "stages/stage32/management/grf04-hpadj22-joint/run_grf04_hpadj22_full178_parent.py"
WORKER_BLOB = "c9fbf71242581f096718ebf0dbc9ac88878c91f1"
SOURCE_HEAD = "4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2"
CURRENT_AUTHORITY = 138_652_739_800_650_593_494


def canonical(doc: dict) -> str:
    body = dict(doc)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def load_worker():
    spec = importlib.util.spec_from_file_location("full178_partial_accounting_worker", WORKER_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    module.req(module.blob(WORKER_PATH) == WORKER_BLOB, "production worker blob drift")
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificates", nargs="+", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    worker = load_worker()
    hd = worker.load_helper()
    direct = hd.load(hd.DIRECT, hd.DIRECT_BLOB, "v46_partial_accounting_direct")
    old = direct.load_old(SOURCE_ROOT)
    rows = old.source_context()[8]
    worker.req(len(rows) == 178, "FULL178 row identity drift")

    accepted = []
    seen = set()
    for path in args.certificates:
        doc = json.loads(path.read_text())
        target = doc["target"]
        band, chunk, row = int(target["band_position"]), int(target["chunk_position"]), int(target["row_index"])
        worker.req(0 <= band < 8 and 0 <= chunk < 4 and 0 <= row < 178, "target outside FULL178 partition")
        key = (band, chunk, row)
        worker.req(key not in seen, f"duplicate accounting key {key}")
        seen.add(key)
        b0, b1 = worker.chunks_for_band(band)[chunk]
        row_id, g, d = rows[row]
        worker.req(int(d) // 2 >= b0, f"implicit-zero target cannot carry improvement {key}")
        valid = worker.validate_carry(
            path, worker_blob=WORKER_BLOB, band=band, chunk=chunk, b0=b0, b1=b1,
            row_index=row, row_id=str(row_id), g=int(g), d=int(d))
        worker.req(valid is not None, f"production validate_carry rejected {path}")
        result = valid["result"]
        baseline, joint = int(result["hpadj22_exact_survivors"]), int(result["joint_exact_survivors"])
        improvement = int(result["exact_improvement"])
        worker.req(baseline - joint == improvement >= 0, f"improvement identity drift {key}")
        accepted.append({
            "accounting_key": {"band_position": band, "chunk_position": chunk, "row_index": row},
            "b_chunk": [b0, b1], "row_id": str(row_id), "g": int(g), "d": int(d),
            "hpadj22_baseline": str(baseline), "joint": str(joint), "exact_improvement": str(improvement),
            "certificate_canonical_sha256": valid["canonical_sha256_without_this_field"],
            "production_validate_carry": "PASS",
        })

    total = sum(int(item["exact_improvement"]) for item in accepted)
    output = {
        "schema": "STAGE32_MAIN_V46_GRF04_HPADJ22_SELECTED_DISJOINT_PARTIAL_ACCOUNTING_RESEARCH_V1",
        "stage": 32,
        "status": "EXACT_SELECTED_DISJOINT_PARTIAL_ACCOUNTING_ZERO_CREDIT_HOSTILE_AUDIT_REQUIRED",
        "purpose": "Research-only exact accounting proposal for selected high-ROI GRF04 x HPADJ22 row-chunks without waiting for FULL178 completion.",
        "source_locks": {"production_worker_blob_sha1": WORKER_BLOB, "hpadj22_source_head": SOURCE_HEAD,
                         "current_hpadj22_main_authority": str(CURRENT_AUTHORITY)},
        "coverage": {"selected_certificate_count": len(accepted), "unique_accounting_key_count": len(seen),
                     "gaps_claimed": False, "overlaps": 0, "full178_complete": False},
        "certificates": sorted(accepted, key=lambda item: tuple(item["accounting_key"].values())),
        "result": {"selected_exact_improvement": str(total),
                   "research_candidate_upper_bound_if_separately_audited_and_promoted": str(CURRENT_AUTHORITY - total),
                   "global_main_reduction_fraction": total / CURRENT_AUTHORITY},
        "composition": {"same_population_exact_intersection": True, "selected_keys_pairwise_disjoint": True,
                        "integer_exact_sum": True, "min_of_counts": False, "additive_stacking": False,
                        "accounting_operation": "Replace each selected HPADJ22 disjoint summand by its exact GRF04 intersection; leave every unselected summand unchanged."},
        "promotion_gate": {"research_only": True, "main_authority_changed": False,
                           "independent_hostile_audit_required": True,
                           "main_transition_and_claim_sync_required": True},
        "firewalls": {"main_pruning_credit": False, "full178_credit": False, "theorem_credit": False,
                      "effectivity_credit": False, "receiver_credit": False, "route_credit": False,
                      "endpoint_credit": False, "merge_authorized": False},
    }
    output["canonical_sha256_without_this_field"] = canonical(output)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": output["status"], "certificates": len(accepted),
                      "improvement": str(total), "candidate": str(CURRENT_AUTHORITY - total),
                      "canonical": output["canonical_sha256_without_this_field"]}, sort_keys=True))


if __name__ == "__main__":
    main()
