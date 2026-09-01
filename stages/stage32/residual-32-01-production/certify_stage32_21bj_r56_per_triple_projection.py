#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, json
from pathlib import Path
from z3 import get_version_string, sat, unknown, unsat

from audit_stage32_21be_r51_endpoints import EXPECTED_TRIPLES, predicted_lo
from certify_stage32_21ba_r51_interval_census import prism_triples
from certify_stage32_21bc_pair_combination_projection import CANDIDATE_BOUNDS
from certify_stage32_21bf_r49_per_triple_projection import build_21bf_solver, check_with, independent_integer_projection
from certify_stage32_21bg_r42_per_triple_projection import r49_hi
from certify_stage32_21bh_r54_per_triple_projection import r42_lo
from certify_stage32_21bi_r57_per_triple_projection import load_21bh_lock, r54_lo_from_table
from direct_picard_reynolds_lattice_diagnostic import csha

EXPECTED_21BI_LOCK_SHA256 = "171de3592fec3f32a381de8a07365e3444cbfc75d5acb2e0eff053bd644bc06c"
R56, R57 = 56, 57
R56_BOUND, R57_BOUND = (14, 60), (0, 46)
SCHEMA_SHARD = "STAGE32_21BJ_EXACT_R56_PER_TRIPLE_PROJECTION_SHARD_V1"
SCHEMA_AGG = "STAGE32_21BJ_EXACT_R56_PER_TRIPLE_PROJECTION_AGGREGATE_V1"


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def load_21bi_lock(p: Path) -> dict:
    raw = json.loads(p.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    if claimed != EXPECTED_21BI_LOCK_SHA256 or csha(raw) != claimed:
        raise ValueError("21bi lock canonical regression")
    f = raw.get("lossless_r57_interval_formula", {})
    if (
        raw.get("status") != "PASS_EXACT_21BI_R57_AFTER_TARGETED_UNKNOWN_RESCUE"
        or tuple(raw.get("r57_global_integer_valid_bound", [])) != R57_BOUND
        or f.get("lower") != 0
        or f.get("upper_formula") != "min(46, -r27 - 29)"
        or f.get("r27_domain") != [-96, -48]
        or not f.get("verified_against_all_3234_exact_21bi_rows")
    ):
        raise ValueError("21bi lock metadata regression")
    return raw


def r57_hi(r27: int) -> int:
    return min(46, -r27 - 29)


def audit_r57(solver, expr, hi: int) -> dict:
    checks, states = 0, {}
    for name, constraint in (
        ("lo", expr == 0),
        ("hi", expr == hi),
        ("below", expr <= -1),
        ("above", expr >= hi + 1),
    ):
        result, reason = check_with(solver, constraint)
        checks += 1
        states[name] = str(result)
        if result == unknown:
            return {"status": "UNKNOWN", "phase": name, "reason": reason, "checks": checks}
    ok = states == {"lo": "sat", "hi": "sat", "below": "unsat", "above": "unsat"}
    return {"status": "PASS_EXACT_R57_FORMULA_THRESHOLDS" if ok else "R57_FORMULA_MISMATCH",
            "checks": checks, **states}


def run_shard(a) -> None:
    if CANDIDATE_BOUNDS.get(R56) != R56_BOUND or CANDIDATE_BOUNDS.get(R57) != R57_BOUND:
        raise ValueError("r56/r57 source-domain regression")
    load_21bi_lock(a.eighth_lock)
    _, r54_table = load_21bh_lock(a.seventh_lock)
    triples = list(prism_triples())
    if len(triples) != EXPECTED_TRIPLES:
        raise ValueError("prism count regression")
    start = EXPECTED_TRIPLES * a.shard_index // a.shard_count
    end = EXPECTED_TRIPLES * (a.shard_index + 1) // a.shard_count
    solver, r, target = build_21bf_solver(a)
    rows, checks = [], 0
    mismatch = audit_unknown = proj_unknown = empty = opened = total = 0

    for ordinal in range(start, end):
        r50, r55, r27 = triples[ordinal]
        bands = {
            51: (predicted_lo(r50, r55, r27), -132),
            49: (132, r49_hi(r27)),
            42: (r42_lo(r50, r55, r27), 79),
            54: (r54_lo_from_table(r54_table, r50, r55, r27), -132),
            57: (0, r57_hi(r27)),
        }
        solver.push()
        solver.add(r[50] == r50, r[55] == r55, r[27] == r27)
        for j in (51, 49, 42, 54):
            solver.add(r[j] >= bands[j][0], r[j] <= bands[j][1])
        try:
            audit = audit_r57(solver, r[R57], bands[57][1])
            checks += audit["checks"]
            row = {"ordinal": ordinal, "triple": [r50, r55, r27],
                   "bands": {str(j): list(bands[j]) for j in (51,49,42,54,57)},
                   "r57_formula_audit": audit}
            if audit["status"] == "UNKNOWN":
                audit_unknown += 1
                row["status"] = "UNKNOWN"
            elif audit["status"] != "PASS_EXACT_R57_FORMULA_THRESHOLDS":
                mismatch += 1
                row["status"] = "R57_FORMULA_MISMATCH"
            else:
                solver.add(r[R57] >= bands[57][0], r[R57] <= bands[57][1])
                out = independent_integer_projection(solver, r[R56], *R56_BOUND)
                checks += out["checks"]
                row["projection"] = out
                if out["status"] == "EMPTY_INTEGER_PROJECTION":
                    empty += 1
                    row["status"] = "EXACT_INTEGER_PRUNED_BY_R56_INTEGRALITY"
                elif out["status"] == "UNKNOWN":
                    proj_unknown += 1
                    row["status"] = "UNKNOWN"
                elif out["status"] == "RESOLVED":
                    opened += 1
                    total += out["domain_size"]
                    row["status"] = "OPEN_WITH_EXACT_INTEGER_VALID_R56_INTERVAL"
                else:
                    raise RuntimeError(out["status"])
            rows.append(row)
        finally:
            solver.pop()
        if (ordinal - start + 1) % 250 == 0:
            print(json.dumps({"shard":a.shard_index,"processed":ordinal-start+1,
                              "mismatch":mismatch,"empty":empty,
                              "unknown":audit_unknown+proj_unknown,"open":opened}), flush=True)

    payload = {
        "schema": SCHEMA_SHARD, "stage": 32, "leaf": "32-21bj",
        "mode": "AUDITED_CLOSED_BANDS_PLUS_INDEPENDENT_R57_REAUDIT_THEN_R56_INTEGER_VALID_PROJECTION",
        "source_21bi_lock_sha256": EXPECTED_21BI_LOCK_SHA256,
        "r56_global_integer_valid_bound": list(R56_BOUND),
        "r57_global_integer_valid_bound": list(R57_BOUND),
        "z3_version": get_version_string(), "target": target,
        "partition": {"shard_index":a.shard_index,"shard_count":a.shard_count,
                      "start_ordinal":start,"end_ordinal_exclusive":end,"expected_rows":end-start},
        "result": {"processed_rows":len(rows),"r57_formula_mismatch_count":mismatch,
                   "r57_formula_unknown_count":audit_unknown,"projection_empty_count":empty,
                   "projection_unknown_count":proj_unknown,"resolved_nonempty_count":opened,
                   "exact_qf_lra_checks":checks,"r56_integer_valid_index_count":total,"rows":rows},
        "interpretation": {
            "upstream_r51_r49_r42_r54_bands_are_consumed_only_from_audited_closed_locks": True,
            "r57_formula_is_independently_reaudited_against_original_all140_system_before_consumption": True,
            "empty_r56_projection_prunes_only_this_representative_fixed_triple": True,
            "nonempty_r56_interval_is_integer_valid_necessary_data_not_integer_sat": True,
            "unknown_is_not_unsat": True, "fixed_projection_unsat_is_not_slice_unsat": True,
            "representative_sample_only": True, "not_full178_numerical_credit": True},
        "safety": {"heavy_run_key_used":False,"full178_production_run":False,"integer_solver_used":False,
                   "theorem_credit":False,"receiver_credit":False,"route_credit":False,
                   "perfect_cuboid_existence_claim":False,"perfect_cuboid_nonexistence_claim":False},
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    a.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status":"PASS_SHARD" if mismatch==0 and audit_unknown+proj_unknown==0 else "SHARD_NOT_PASS",
                      "canonical":payload["canonical_sha256_without_this_field"],"processed":len(rows),
                      "mismatch":mismatch,"integer_pruned":empty,"open":opened,
                      "unknown":audit_unknown+proj_unknown,"r56_indices":total}), flush=True)


def run_aggregate(a) -> None:
    files = sorted(a.input_dir.glob("**/stage32-21bj-r56-projection-*.json"))
    if len(files) != a.shard_count:
        raise ValueError(f"expected {a.shard_count} shard files, got {len(files)}")
    shards, sources = [], []
    for p in files:
        d = json.loads(p.read_text()); claimed = d.pop("canonical_sha256_without_this_field")
        if d.get("schema") != SCHEMA_SHARD or csha(d) != claimed:
            raise ValueError(f"shard canonical/schema regression {p}")
        d["canonical_sha256_without_this_field"] = claimed
        shards.append(d); sources.append({"file":p.name,"raw_sha256":sha256_file(p),"canonical_sha256":claimed})
    shards.sort(key=lambda x:x["partition"]["shard_index"])
    rows, expected_start, checks = [], 0, 0
    for idx, s in enumerate(shards):
        p=s["partition"]
        if p["shard_index"]!=idx or p["shard_count"]!=a.shard_count or p["start_ordinal"]!=expected_start:
            raise ValueError("shard partition regression")
        expected_start=p["end_ordinal_exclusive"]; rows += s["result"]["rows"]; checks += s["result"]["exact_qf_lra_checks"]
    rows.sort(key=lambda x:x["ordinal"])
    complete = expected_start==EXPECTED_TRIPLES and len(rows)==EXPECTED_TRIPLES and all(r["ordinal"]==i for i,r in enumerate(rows))
    mismatch=[r for r in rows if r["status"]=="R57_FORMULA_MISMATCH"]
    unknown_rows=[r for r in rows if r["status"]=="UNKNOWN"]
    pruned=[r for r in rows if r["status"]=="EXACT_INTEGER_PRUNED_BY_R56_INTEGRALITY"]
    opened=[r for r in rows if r["status"]=="OPEN_WITH_EXACT_INTEGER_VALID_R56_INTERVAL"]
    total=sum(r["projection"]["domain_size"] for r in opened)
    passed=complete and not mismatch and not unknown_rows and len(pruned)+len(opened)==EXPECTED_TRIPLES
    compact_open=[[r["ordinal"],*r["triple"],
                   *r["bands"]["51"],*r["bands"]["49"],*r["bands"]["42"],*r["bands"]["54"],*r["bands"]["57"],
                   r["projection"]["lo"],r["projection"]["hi"]] for r in opened]
    payload={
      "schema":SCHEMA_AGG,"stage":32,"leaf":"32-21bj",
      "status":"PASS_EXACT_21BJ_R56_PER_TRIPLE_PROJECTION" if passed else "FAIL_OR_UNKNOWN_21BJ_R56_PER_TRIPLE_PROJECTION",
      "source_21bi_lock_sha256":EXPECTED_21BI_LOCK_SHA256,
      "r56_global_integer_valid_bound":list(R56_BOUND),
      "coverage":{"expected_triples":EXPECTED_TRIPLES,"complete_partition":complete,
                  "r57_formula_mismatch_triples":len(mismatch),"r56_integer_empty_triples":len(pruned),
                  "exact_integer_pruned_triples":len(pruned),"open_triples":len(opened),
                  "unknown_triples":len(unknown_rows),"exact_qf_lra_checks":checks},
      "compression":{"naive_r56_indices_before_per_triple_projection":EXPECTED_TRIPLES*47,
                     "r56_integer_valid_indices_after_projection":total,
                     "removed_candidate_indices":EXPECTED_TRIPLES*47-total},
      "fixed_projection_integer_unsat":passed and not opened,
      "compact_row_encoding":"[ordinal,r50,r55,r27,r51_lo,r51_hi,r49_lo,r49_hi,r42_lo,r42_hi,r54_lo,r54_hi,r57_lo,r57_hi,r56_lo,r56_hi]",
      "open_rows":compact_open,
      "pruned_rows":[[r["ordinal"],*r["triple"],r["status"]] for r in pruned],
      "r57_formula_mismatch_rows":mismatch,"unknown_rows":unknown_rows,"shard_sources":sources,
      "interpretation":{"pass_includes_independent_r57_formula_threshold_reaudit_on_all_3234_triples":True,
                        "open_rows_are_not_integer_sat_witnesses":True,
                        "fixed_projection_integer_unsat_if_all_3234_triples_pruned":True,
                        "fixed_projection_unsat_is_not_slice_unsat":True,
                        "representative_sample_only":True,"not_full178_numerical_credit":True},
      "safety":{"unknown_is_not_unsat":True,"rational_feasibility_is_not_integer_sat":True,
                "theorem_credit":False,"receiver_credit":False,"route_credit":False,
                "perfect_cuboid_existence_claim":False,"perfect_cuboid_nonexistence_claim":False}}
    payload["canonical_sha256_without_this_field"]=csha(payload)
    a.output.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"status":payload["status"],"canonical":payload["canonical_sha256_without_this_field"],
                      "mismatch":len(mismatch),"integer_pruned":len(pruned),"open":len(opened),
                      "unknown":len(unknown_rows),"r56_indices":total,
                      "fixed_projection_integer_unsat":payload["fixed_projection_integer_unsat"]}),flush=True)
    if not passed: raise SystemExit(1)


def main() -> None:
    p=argparse.ArgumentParser(); sub=p.add_subparsers(dest="mode",required=True)
    s=sub.add_parser("shard")
    for name in ("source-lock","formula-lock","pair-lock","audit-lock","fifth-lock","sixth-lock","seventh-lock","eighth-lock","retained","marking"):
        s.add_argument("--"+name,type=Path,required=True)
    s.add_argument("--shard-index",type=int,required=True); s.add_argument("--shard-count",type=int,default=2)
    s.add_argument("--per-check-timeout-ms",type=int,default=5000); s.add_argument("--output",type=Path,required=True)
    g=sub.add_parser("aggregate"); g.add_argument("--input-dir",type=Path,required=True)
    g.add_argument("--shard-count",type=int,default=2); g.add_argument("--output",type=Path,required=True)
    a=p.parse_args(); run_shard(a) if a.mode=="shard" else run_aggregate(a)

if __name__=="__main__": main()
