#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

from z3 import Int, SolverFor, sat, unknown, unsat

ROOT = Path(__file__).resolve().parents[4]
FULL_WORKER = ROOT / "stages/stage32/management/btva-compressed-lift/run_btva_base4_full343_shard.py"
FULL_WORKER_BLOB = "63321a54f565b2da38efbef756caf8db148f0063"
FULL_RETAINED = ROOT / "stages/stage32/management/btva-compressed-lift/BTVA-D8-FULL343-RETAINED-CHECKPOINT.json"
FULL_RETAINED_BLOB = "4ae970e17b0d7168f6d2ffd0644195f2ab57ae8d"
FULL_RETAINED_CANON = "5e111a460381d9df7662b7f552eadde68953ecee304cf7a47d4aa52d2a9ba776"
R1_RETAINED = ROOT / "stages/stage32/management/btva-compressed-lift/BTVA-D8-TIMEOUT-RESCUE-TOP16-RETAINED.json"
R1_RETAINED_BLOB = "e1c4b0e04fa7f291cdbb42b3aafd62c869f47220"
R1_RETAINED_CANON = "99b0294b87df9d6b41e52b186af0b079eda5c3f37f5d94fc215aca7d435b2ad4"
RESIDUAL_HNF = ROOT / "stages/stage32/management/btva-compressed-lift/BTVA-D8-RESIDUAL-BLOCK-PICARD-HNF-RETAINED.json"
RESIDUAL_HNF_BLOB = "8f111c209b8863419b190702cfe40fe26ea43407"
RESIDUAL_HNF_CANON = "9a4899cad0a4d135e21ebdb6cfeb888c4bb77980f96d0c802e4aacb9be049ec8"

DEGREE = 8
EXCEPTIONAL_MASS = 8
EXCEPTIONAL_COUNT = 48
X4_VALUES = 113


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
    req(blob(path)==expected_blob,path.name+" blob drift")
    obj=json.loads(path.read_text(encoding="utf-8"))
    stored=obj.get("canonical_sha256_without_this_field")
    body=dict(obj); body.pop("canonical_sha256_without_this_field",None)
    req(stored==expected_canon and csha(body)==expected_canon,path.name+" canonical drift")
    return obj


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--solver-timeout-ms",type=int,default=5000)
    ap.add_argument("--max-flat-cuts",type=int,default=256)
    ap.add_argument("--output",type=Path,required=True)
    args=ap.parse_args()
    req(args.solver_timeout_ms>0 and args.solver_timeout_ms<=10000,"timeout range")
    req(args.max_flat_cuts>0 and args.max_flat_cuts<=512,"flat-cut range")

    full_ret=load_canonical(FULL_RETAINED,FULL_RETAINED_BLOB,FULL_RETAINED_CANON)
    r1=load_canonical(R1_RETAINED,R1_RETAINED_BLOB,R1_RETAINED_CANON)
    residual=load_canonical(RESIDUAL_HNF,RESIDUAL_HNF_BLOB,RESIDUAL_HNF_CANON)
    req(residual["result"]["candidate_d8_survivor_terminal_mass_after_residual_picard_hnf"]==231424,"residual-HNF boundary drift")

    req(blob(FULL_WORKER)==FULL_WORKER_BLOB,"full343 worker drift")
    full=load_module(FULL_WORKER,"stage32_main_btva_support_only_full_worker")
    req(full.PARENT.is_file() and full.blob(full.PARENT)==full.PARENT_BLOB,"full343 parent drift")
    parent=full.load_module(full.PARENT,"stage32_main_btva_support_only_parent")
    old=parent.load_module(parent.RELAXED,"stage32_main_btva_support_only_relaxed")
    node_bridge=json.loads(old.NODE_BRIDGE.read_text(encoding="utf-8"))
    nodes=old.node_matrix(node_bridge)
    req(nodes.shape==(48,7) and int(nodes.rank())==7,"node ambient rank")

    # Build the exact a,b,c,t map directly on the 48 exceptional pairings.
    coeffs=[[0]*EXCEPTIONAL_COUNT for _ in range(4)]
    for i in range(4):
        for j,coef in enumerate(old.L[i]):
            lab=int(old.ASSIGNMENT[j])
            c=int(coef)
            if lab>=93:
                coeffs[i][lab-93]+=c
            else:
                req(lab==49 and c==0,"normal x4 leaked into base4 exceptional map")
    req(all(any(row) for row in coeffs),"degenerate base4 exceptional map")

    v1=old.load_module(old.BASE,"stage32_main_btva_support_only_base")
    indexer=v1.CompressedTerminalIndexer(EXCEPTIONAL_MASS,DEGREE)
    req(indexer.normal_budget==112 and indexer.normal_budget+1==X4_VALUES,"indexer budget drift")
    counts={}
    tmp={}
    stride=X4_VALUES
    from collections import Counter
    cc=Counter()
    for erank in range(int(indexer.exceptional_count)):
        terminal=tuple(int(v) for v in indexer.unrank(erank*stride))
        req(terminal[4]==0,"x4 stride replay")
        base4=tuple(old.static_from_terminal(terminal)[:4])
        cc[base4]+=1
        # Exact replay of a,b,c,t from the observed exceptional coordinates.
        ev=[0]*EXCEPTIONAL_COUNT
        for lab,val in zip(old.ASSIGNMENT,terminal):
            if int(lab)>=93:
                ev[int(lab)-93]=int(val)
        replay=tuple(sum(coeffs[i][k]*ev[k] for k in range(EXCEPTIONAL_COUNT)) for i in range(4))
        req(replay==base4,"base4 exceptional-map replay drift")
    keys=sorted(cc)
    req(len(keys)==343,"base4 key population drift")
    key_to_index={k:i for i,k in enumerate(keys)}

    original={int(i):int(m) for i,m in full_ret["result"]["survivor_index_mass_pairs"]}
    removed_r1=set(int(i) for i in r1["result"]["rescued_unsat_indices_0based"])
    survivors={i:m for i,m in original.items() if i not in removed_r1}
    req(len(survivors)==86 and sum(survivors.values())==231424,"survivor boundary reconstruction")

    rows=[]
    unsat_mass=0
    sat_mass=0
    unknown_mass=0
    for idx,mass in sorted(survivors.items()):
        base4=keys[idx]
        evars=[Int(f"e_{idx}_{k}") for k in range(EXCEPTIONAL_COUNT)]
        solver=SolverFor("QF_LIA")
        solver.set(timeout=args.solver_timeout_ms)
        for e in evars:
            solver.add(e>=0,e<=EXCEPTIONAL_MASS)
        solver.add(sum(evars)==EXCEPTIONAL_MASS)
        for i,value in enumerate(base4):
            solver.add(sum(coeffs[i][k]*evars[k] for k in range(EXCEPTIONAL_COUNT))==int(value))

        seen=set()
        cuts=[]
        iterations=0
        status="UNKNOWN"
        reason=None
        witness=None
        while iterations<=args.max_flat_cuts:
            iterations+=1
            result=solver.check()
            if result==unsat:
                status="UNSAT_NO_RANK7_EXCEPTIONAL_SUPPORT"
                break
            if result==unknown:
                reason=solver.reason_unknown()
                break
            req(result==sat,"unexpected support-only solver status")
            model=solver.model()
            ev=[int(model.eval(e,model_completion=True).as_long()) for e in evars]
            req(min(ev)>=0 and sum(ev)==EXCEPTIONAL_MASS,"exceptional mass model drift")
            replay=tuple(sum(coeffs[i][k]*ev[k] for k in range(EXCEPTIONAL_COUNT)) for i in range(4))
            req(replay==base4,"support witness base4 drift")
            support=tuple(i for i,v in enumerate(ev) if v>0)
            rank=old.support_rank(nodes,support)
            if rank==7:
                req(7<=len(support)<=8,"rank7 support size outside mass-8 bound")
                weights=sorted(ev[i] for i in support)
                if len(support)==8:
                    req(weights==[1]*8,"8-support mass shape")
                else:
                    req(weights==[1]*6+[2],"7-support mass shape")
                status="SAT_RANK7_EXCEPTIONAL_SUPPORT"
                witness={
                    "exceptional_pairings_sha256":v1.csha(ev),
                    "support_indices_0based":list(support),
                    "support_labels_1based":[93+i for i in support],
                    "support_size":len(support),
                    "weights_on_support":[ev[i] for i in support],
                    "support_rank":rank,
                }
                break
            flat=old.closure(nodes,support)
            req(flat not in seen,"repeated support flat")
            seen.add(flat)
            outside=[k for k in range(EXCEPTIONAL_COUNT) if k not in flat]
            req(outside,"proper rank-deficient flat has no outside node")
            solver.add(sum(evars[k] for k in outside)>=1)
            cuts.append({
                "support_rank":rank,
                "support_size":len(support),
                "closure_size":len(flat),
                "outside_count":len(outside),
            })
        else:
            reason="max_flat_cuts_exhausted"

        if status.startswith("UNSAT_"):
            unsat_mass+=mass
        elif status.startswith("SAT_"):
            sat_mass+=mass
        else:
            unknown_mass+=mass
        rows.append({
            "global_base4_index":idx,
            "base4":list(base4),
            "terminal_mass":mass,
            "result":status,
            "solver_iterations":iterations,
            "lazy_flat_cut_count":len(cuts),
            "reason_unknown":reason,
            "rank7_witness":witness,
        })

    req(unsat_mass+sat_mass+unknown_mass==231424,"support-only mass conservation")
    out={
      "schema":"STAGE32_MAIN_BTVA_D8_EXCEPTIONAL_SUPPORT_ONLY_DIAGNOSTIC_V1",
      "stage":32,
      "status":"EXACT_SUPPORT_ONLY_PANEL_COMPLETE_ZERO_CREDIT" if unknown_mass==0 else "BOUNDED_SUPPORT_ONLY_PANEL_WITH_UNKNOWN_ZERO_CREDIT",
      "target":{
        "row_id":"g0-d008","degree":DEGREE,"exceptional_mass":EXCEPTIONAL_MASS,
        "source_base4_survivor_count":86,"source_terminal_mass":231424,
      },
      "decision_problem":{
        "picard64_constraints_included":False,
        "all140_nonnegativity_included":False,
        "base4_exact":True,
        "exceptional_mass_exact":True,
        "node_span_rank7_required":True,
        "rank7_mass8_support_shape":"7 nodes with weights 2,1,1,1,1,1,1 or 8 nodes all weight 1",
      },
      "rows":rows,
      "summary":{
        "support_unsat_base4_count":sum(1 for r in rows if r["result"].startswith("UNSAT_")),
        "support_sat_base4_count":sum(1 for r in rows if r["result"].startswith("SAT_")),
        "support_unknown_base4_count":sum(1 for r in rows if r["result"]=="UNKNOWN"),
        "support_unsat_terminal_mass":unsat_mass,
        "support_sat_terminal_mass":sat_mass,
        "support_unknown_terminal_mass":unknown_mass,
        "candidate_d8_survivor_terminal_mass_after_support_only_filter":sat_mass+unknown_mass,
        "max_lazy_flat_cut_count":max(int(r["lazy_flat_cut_count"]) for r in rows),
      },
      "semantics":{
        "support_only_unsat_is_safe_receiver_rejection":True,
        "support_only_sat_does_not_claim_integral_picard_completion":True,
        "support_only_sat_does_not_claim_effectivity":True,
        "composition_with_prior_filters_is_set_intersection_not_additive_independence":True,
      },
      "source_locks":{
        "full343_worker_blob_sha1":FULL_WORKER_BLOB,
        "full343_retained_blob_sha1":FULL_RETAINED_BLOB,
        "round1_retained_blob_sha1":R1_RETAINED_BLOB,
        "residual_hnf_retained_blob_sha1":RESIDUAL_HNF_BLOB,
        "node_bridge_blob_sha1":old.NODE_BRIDGE_BLOB,
        "base_picard_solver_blob_sha1":old.BASE_BLOB,
      },
      "execution":{"solver":"Z3_QF_LIA","solver_timeout_ms":args.solver_timeout_ms,"max_flat_cuts":args.max_flat_cuts},
      "firewalls":{
        "main_pruning_credit":False,"receiver_credit":False,"effectivity_credit":False,
        "theorem_credit":False,"endpoint_credit":False,"full178_complete":False,
        "stage32_closed":False,"merge_authorized":False,
      },
    }
    out["canonical_sha256_without_this_field"]=csha(out)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print("BTVA_D8_SUPPORT_ONLY_SUMMARY="+json.dumps(out["summary"],sort_keys=True))
    print("BTVA_D8_SUPPORT_ONLY_CANONICAL="+out["canonical_sha256_without_this_field"])


if __name__=="__main__":
    main()
