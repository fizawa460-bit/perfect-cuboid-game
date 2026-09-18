#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from collections import Counter
from pathlib import Path

from z3 import Int, SolverFor, sat, unknown, unsat

ROOT = Path(__file__).resolve().parents[4]
FULL_WORKER = ROOT / "stages/stage32/management/btva-compressed-lift/run_btva_base4_full343_shard.py"
FULL_WORKER_BLOB = "63321a54f565b2da38efbef756caf8db148f0063"
RETAINED = ROOT / "stages/stage32/management/btva-compressed-lift/BTVA-D8-FULL343-RETAINED-CHECKPOINT.json"
RETAINED_BLOB = "4ae970e17b0d7168f6d2ffd0644195f2ab57ae8d"
RETAINED_CANON = "5e111a460381d9df7662b7f552eadde68953ecee304cf7a47d4aa52d2a9ba776"
TARGET_INDICES = (289,296,280,313,321,237,248,164,279,290,311,225,287,68,307,316)
TARGET_MASS = 128029

def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)

def blob(path: Path) -> str:
    raw=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def load_module(path: Path, name: str):
    spec=importlib.util.spec_from_file_location(name,path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    mod=importlib.util.module_from_spec(spec)
    sys.modules[name]=mod
    spec.loader.exec_module(mod)
    return mod

def load_canonical(path: Path, expected_blob: str, expected_canon: str) -> dict:
    req(blob(path)==expected_blob, path.name+" blob drift")
    obj=json.loads(path.read_text(encoding="utf-8"))
    stored=obj.get("canonical_sha256_without_this_field")
    body=dict(obj); body.pop("canonical_sha256_without_this_field",None)
    req(stored==expected_canon and csha(body)==expected_canon, path.name+" canonical drift")
    return obj

def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--retained",type=Path,required=True)
    ap.add_argument("--marking",type=Path,required=True)
    ap.add_argument("--lane178-root",type=Path,required=True)
    ap.add_argument("--solver-timeout-ms",type=int,default=5000)
    ap.add_argument("--max-flat-cuts",type=int,default=32)
    ap.add_argument("--output",type=Path,required=True)
    args=ap.parse_args()
    req(1500 < args.solver_timeout_ms <= 10000, "rescue timeout range")
    req(16 <= args.max_flat_cuts <= 64, "rescue flat-cut range")

    retained=load_canonical(RETAINED,RETAINED_BLOB,RETAINED_CANON)
    pairs=[(int(i),int(m)) for i,m in retained["result"]["survivor_index_mass_pairs"]]
    req(len(pairs)==88 and sum(m for _,m in pairs)==248374, "retained survivor boundary drift")
    top16=tuple(i for i,_ in sorted(pairs,key=lambda x:(-x[1],x[0]))[:16])
    req(top16==TARGET_INDICES, "top16 selector drift")
    target_pair_map=dict(pairs)
    req(sum(target_pair_map[i] for i in TARGET_INDICES)==TARGET_MASS, "target mass drift")

    req(blob(FULL_WORKER)==FULL_WORKER_BLOB, "full343 worker drift")
    full=load_module(FULL_WORKER,"stage32_main_btva_timeout_rescue_full_worker")
    req(full.PARENT.is_file() and full.blob(full.PARENT)==full.PARENT_BLOB, "full343 parent drift")
    parent=full.load_module(full.PARENT,"stage32_main_btva_timeout_rescue_parent")
    old=parent.load_module(parent.RELAXED,"stage32_main_btva_timeout_rescue_relaxed")
    req(old.BASE.is_file() and old.git_blob(old.BASE)==old.BASE_BLOB, "base Picard solver drift")
    req(old.NODE_BRIDGE.is_file() and old.git_blob(old.NODE_BRIDGE)==old.NODE_BRIDGE_BLOB, "node bridge drift")
    lane_agg=args.lane178_root / old.LANE178_AGG_REL
    req(lane_agg.is_file() and old.git_blob(lane_agg)==old.LANE178_AGG_BLOB, "lane178 aggregate drift")

    v1=old.load_module(old.BASE,"stage32_main_btva_timeout_rescue_base")
    indexer=v1.CompressedTerminalIndexer(full.EXCEPTIONAL_MASS,full.DEGREE)
    req(indexer.normal_budget==full.NORMAL_MASS, "normal budget drift")
    req(int(indexer.terminal_count)==full.EXPECTED_TERMINAL_MASS, "terminal population drift")
    counts: Counter[tuple[int,int,int,int]]=Counter()
    stride=full.X4_VALUES
    for erank in range(int(indexer.exceptional_count)):
        x=tuple(int(v) for v in indexer.unrank(erank*stride))
        req(x[4]==0,"x4 stride replay")
        counts[tuple(old.static_from_terminal(x)[:4])]+=1
    keys=sorted(counts)
    req(len(keys)==343,"base4 key count")
    for idx in TARGET_INDICES:
        req(int(counts[keys[idx]])*full.X4_VALUES==target_pair_map[idx],f"target mass reconstruction {idx}")

    bundle=v1.load_retained(args.retained,"stage32_main_btva_timeout_rescue_bundle")
    marking=v1.load_retained(args.marking,"stage32_main_btva_timeout_rescue_marking")
    data=v1.reconstruct_translation_data(marking,bundle)
    adapter=data["adapter"]; bridge=data["bridge"]; P=adapter.pairing_matrix
    req(P.shape==(140,full.PICARD_RANK),"pairing matrix shape")
    req(bridge.certificate.get("mass_identity_exact_on_picard64") is True,"mass identity drift")
    nodes=old.node_matrix(json.loads(old.NODE_BRIDGE.read_text(encoding="utf-8")))
    req(nodes.shape==(48,7) and int(nodes.rank())==7,"node ambient rank")

    rows=[]
    for global_index in TARGET_INDICES:
        base4=keys[global_index]
        xvars=[Int(f"rescue_{global_index}_{j}") for j in range(full.PICARD_RANK)]
        solver=SolverFor("QF_LIA"); solver.set(timeout=args.solver_timeout_ms)
        pairings=[v1.linear_expr(P.row(i),xvars) for i in range(140)]
        normal=pairings[:full.NORMAL_COUNT]
        exceptional=pairings[full.NORMAL_COUNT:full.NORMAL_COUNT+full.EXCEPTIONAL_COUNT]
        for expr in normal: solver.add(expr>=0,expr<=full.NORMAL_MASS)
        for expr in exceptional: solver.add(expr>=0,expr<=full.EXCEPTIONAL_MASS)
        solver.add(v1.linear_expr(bridge.degree_functional,xvars)==full.DEGREE)
        solver.add(v1.linear_expr(bridge.exceptional_mass_functional,xvars)==full.EXCEPTIONAL_MASS)
        solver.add(sum(normal)==full.NORMAL_MASS)
        solver.add(sum(exceptional)==full.EXCEPTIONAL_MASS)
        assignment=[pairings[label-1] for label in old.ASSIGNMENT]
        aggregate4=[sum(int(old.L[i][j])*assignment[j] for j in range(len(old.ASSIGNMENT))) for i in range(4)]
        for expr,value in zip(aggregate4,base4): solver.add(expr==int(value))
        x4_expr=assignment[4]
        cuts=[]; seen=set(); iterations=0; status="UNKNOWN"; reason=None; compatible=None
        while iterations<=args.max_flat_cuts:
            iterations+=1
            result=solver.check()
            if result==unsat:
                status="UNSAT_BASE4_BTVA_EFFECTIVE_PAIRING_FIBER"; break
            if result==unknown:
                reason=solver.reason_unknown(); break
            req(result==sat,"unexpected solver status")
            model=solver.model()
            ev=[int(model.eval(expr,model_completion=True).as_long()) for expr in exceptional]
            x4=int(model.eval(x4_expr,model_completion=True).as_long())
            req(0<=x4<=full.NORMAL_MASS,"x4 model range")
            support=tuple(i for i,v in enumerate(ev) if v>0)
            rank=old.support_rank(nodes,support)
            if rank==7:
                status="SAT_BTVA_COMPATIBLE_BASE4_LIFT"
                compatible={"x4_witness":x4,"exceptional_pairings_sha256":v1.csha(ev),"support_indices_0based":list(support),"support_size":len(support),"support_rank":rank}
                break
            flat=old.closure(nodes,support)
            req(flat not in seen,"repeated lazy flat")
            seen.add(flat)
            outside=[k for k in range(full.EXCEPTIONAL_COUNT) if k not in flat]
            req(outside,"improper lazy flat")
            solver.add(sum(exceptional[k] for k in outside)>=1)
            cuts.append({"support_rank":rank,"support_size":len(support),"closure_size":len(flat),"outside_count":len(outside)})
        else:
            reason="max_flat_cuts_exhausted"
        rows.append({"global_base4_index":global_index,"base4":list(base4),"terminal_mass":target_pair_map[global_index],"result":status,"solver_iterations":iterations,"lazy_flat_cut_count":len(cuts),"reason_unknown":reason,"compatible_support":compatible})

    unsat_rows=[r for r in rows if r["result"].startswith("UNSAT_")]
    sat_rows=[r for r in rows if r["result"].startswith("SAT_")]
    unknown_rows=[r for r in rows if r["result"]=="UNKNOWN"]
    rescued_mass=sum(int(r["terminal_mass"]) for r in unsat_rows)
    candidate_survivor=248374-rescued_mass
    payload={
      "schema":"STAGE32_MAIN_BTVA_D8_TIMEOUT_RESCUE_TOP16_V1",
      "stage":32,
      "status":"BOUNDED_TIMEOUT_RESCUE_COMPLETE_ZERO_CREDIT",
      "target":{"row_id":"g0-d008","source_unknown_count":88,"source_survivor_terminal_mass":248374,"selected_global_base4_indices":list(TARGET_INDICES),"selected_terminal_mass":TARGET_MASS},
      "execution":{"solver":"Z3_QF_LIA","solver_timeout_ms":args.solver_timeout_ms,"max_flat_cuts":args.max_flat_cuts,"effective_concurrency":1,"projected_artifact_bytes_under":131072,"repository_budget_bytes":524288000},
      "source_locks":{"retained_checkpoint_blob_sha1":RETAINED_BLOB,"retained_checkpoint_canonical_sha256":RETAINED_CANON,"full343_worker_blob_sha1":FULL_WORKER_BLOB,"base_picard_solver_blob_sha1":old.BASE_BLOB,"node_bridge_blob_sha1":old.NODE_BRIDGE_BLOB,"lane178_head":old.LANE178_HEAD,"lane178_aggregate_picard_blob_sha1":old.LANE178_AGG_BLOB},
      "rows":rows,
      "summary":{"selected_count":len(rows),"rescued_unsat_count":len(unsat_rows),"compatible_sat_count":len(sat_rows),"remaining_unknown_count":len(unknown_rows),"rescued_unsat_terminal_mass":rescued_mass,"selected_unresolved_or_sat_mass":TARGET_MASS-rescued_mass,"candidate_d8_survivor_terminal_mass_after_rescue":candidate_survivor},
      "firewalls":{"bounded_rescue_only":True,"unknown_is_not_unsat":True,"main_pruning_credit":False,"receiver_credit":False,"effectivity_credit":False,"theorem_credit":False,"endpoint_credit":False,"full178_complete":False,"stage32_closed":False,"merge_authorized":False},
    }
    payload["canonical_sha256_without_this_field"]=csha(payload)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print("BTVA_D8_TIMEOUT_RESCUE_SUMMARY="+json.dumps(payload["summary"],sort_keys=True))
    print("BTVA_D8_TIMEOUT_RESCUE_CANONICAL="+payload["canonical_sha256_without_this_field"])

if __name__=="__main__":
    main()
