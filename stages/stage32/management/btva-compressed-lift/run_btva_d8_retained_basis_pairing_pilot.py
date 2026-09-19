#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import sys
from pathlib import Path

import sympy
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form
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
R2_RETAINED = ROOT / "stages/stage32/management/btva-compressed-lift/BTVA-D8-TIMEOUT-RESCUE-ROUND2-RETAINED.json"
R2_RETAINED_BLOB = "4330fde6607c5119806ed114b45362e9790dc247"
R2_RETAINED_CANON = "ae647aaecf768b74df2fb7be881ff7220867acc6700f9f8cae38dbdb7ff4e2fe"

DEGREE=8
EXCEPTIONAL_MASS=8
NORMAL_MASS=112
NORMAL_COUNT=92
EXCEPTIONAL_COUNT=48
PICARD_RANK=64
TARGET_INDICES=(289,296,280,313,237,248,279,290,311,225,287,68,307,316)
TARGET_MASS=111079
EXPECTED_GRAM_DET=268435456


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: "+msg)


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


def functional_u_coeffs(coeffs, gram_inv: Matrix) -> list[int]:
    row=Matrix([[int(v) for v in coeffs]])
    q=row*gram_inv
    req(q.shape==(1,PICARD_RANK),"functional transform shape")
    req(all(sympy.denom(v)==1 for v in q),"functional not integral in retained-basis pairing coordinates")
    return [int(q[0,j]) for j in range(PICARD_RANK)]


def main() -> None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--retained",type=Path,required=True)
    ap.add_argument("--marking",type=Path,required=True)
    ap.add_argument("--lane178-root",type=Path,required=True)
    ap.add_argument("--solver-timeout-ms",type=int,default=2000)
    ap.add_argument("--max-flat-cuts",type=int,default=64)
    ap.add_argument("--output",type=Path,required=True)
    args=ap.parse_args()
    req(0<args.solver_timeout_ms<=5000,"timeout range")
    req(0<args.max_flat_cuts<=128,"flat-cut range")

    full_ret=load_canonical(FULL_RETAINED,FULL_RETAINED_BLOB,FULL_RETAINED_CANON)
    r1=load_canonical(R1_RETAINED,R1_RETAINED_BLOB,R1_RETAINED_CANON)
    r2=load_canonical(R2_RETAINED,R2_RETAINED_BLOB,R2_RETAINED_CANON)
    req(tuple(int(i) for i in r1["result"]["remaining_unknown_indices_0based"])==TARGET_INDICES,"target index drift")
    req(r2["result"]["candidate_d8_survivor_terminal_mass_after_round2"]==231424,"R2 survivor boundary")

    req(blob(FULL_WORKER)==FULL_WORKER_BLOB,"full343 worker drift")
    full=load_module(FULL_WORKER,"stage32_main_btva_basis_pairing_full_worker")
    req(full.PARENT.is_file() and full.blob(full.PARENT)==full.PARENT_BLOB,"full343 parent drift")
    parent=full.load_module(full.PARENT,"stage32_main_btva_basis_pairing_parent")
    old=parent.load_module(parent.RELAXED,"stage32_main_btva_basis_pairing_relaxed")
    lane_agg=args.lane178_root / old.LANE178_AGG_REL
    req(lane_agg.is_file() and old.git_blob(lane_agg)==old.LANE178_AGG_BLOB,"lane178 aggregate drift")

    v1=old.load_module(old.BASE,"stage32_main_btva_basis_pairing_base")
    bundle=v1.load_retained(args.retained,"stage32_main_btva_basis_pairing_bundle")
    marking=v1.load_retained(args.marking,"stage32_main_btva_basis_pairing_marking")
    data=v1.reconstruct_translation_data(marking,bundle)
    adapter=data["adapter"]
    bridge=data["bridge"]
    coords=adapter.class_coordinates_in_retained_basis
    gram=Matrix(bundle["picard_gram_64x64"])
    req(coords.shape==(140,PICARD_RANK),"class coordinate shape")
    req(gram.shape==(PICARD_RANK,PICARD_RANK) and gram==gram.T,"Gram shape/symmetry")
    req(abs(int(gram.det()))==EXPECTED_GRAM_DET,"Gram determinant drift")
    retained_labels=[int(x) for x in adapter.certificate["retained_basis_known_labels_1based"]]
    req(len(retained_labels)==PICARD_RANK and len(set(retained_labels))==PICARD_RANK,"retained label basis")
    retained_idx=[x-1 for x in retained_labels]
    req(coords.extract(retained_idx,list(range(PICARD_RANK)))==Matrix.eye(PICARD_RANK),"retained coordinate identity")
    req(adapter.pairing_matrix==coords*gram,"pairing reconstruction drift")

    # Exact membership u in Gram*Z^64, with u_j = <retained_basis_j, x>.
    H=hermite_normal_form(gram)
    req(H.shape==(PICARD_RANK,PICARD_RANK),"Gram HNF shape")
    req(abs(int(H.det()))==EXPECTED_GRAM_DET,"Gram HNF determinant")
    Hinv=H.inv()
    modulus=1
    for value in Hinv:
        modulus=math.lcm(modulus,int(sympy.denom(value)))
    invq=Hinv*modulus
    req(all(sympy.denom(v)==1 for v in invq),"Gram HNF denominator clearing")
    congruence_rows=[]
    if modulus!=1:
        for i in range(PICARD_RANK):
            row=[int(invq[i,j])%modulus for j in range(PICARD_RANK)]
            if any(row):
                congruence_rows.append(row)

    gram_inv=gram.inv()
    degree_u=functional_u_coeffs(bridge.degree_functional,gram_inv)
    emass_u=functional_u_coeffs(bridge.exceptional_mass_functional,gram_inv)

    # Rebuild exact base4 population and current target masses.
    indexer=v1.CompressedTerminalIndexer(EXCEPTIONAL_MASS,DEGREE)
    counts={}
    from collections import Counter
    cc=Counter()
    stride=NORMAL_MASS+1
    for erank in range(int(indexer.exceptional_count)):
        terminal=tuple(int(v) for v in indexer.unrank(erank*stride))
        req(terminal[4]==0,"x4 stride replay")
        cc[tuple(old.static_from_terminal(terminal)[:4])]+=1
    keys=sorted(cc)
    req(len(keys)==343,"base4 key population")
    source_mass={int(i):int(m) for i,m in full_ret["result"]["survivor_index_mass_pairs"]}
    target_mass={i:source_mass[i] for i in TARGET_INDICES}
    req(sum(target_mass.values())==TARGET_MASS,"target mass")

    nodes=old.node_matrix(json.loads(old.NODE_BRIDGE.read_text(encoding="utf-8")))
    req(nodes.shape==(48,7) and int(nodes.rank())==7,"node ambient rank")

    rows=[]
    for idx in TARGET_INDICES:
        base4=keys[idx]
        u=[Int(f"u_{idx}_{j}") for j in range(PICARD_RANK)]
        solver=SolverFor("QF_LIA")
        solver.set(timeout=args.solver_timeout_ms)

        # Every u_j is itself a known-curve pairing, hence directly bounded.
        for j,lab in enumerate(retained_labels):
            upper=NORMAL_MASS if lab<=NORMAL_COUNT else EXCEPTIONAL_MASS
            solver.add(u[j]>=0,u[j]<=upper)

        if modulus!=1:
            for row in congruence_rows:
                solver.add(sum(row[j]*u[j] for j in range(PICARD_RANK)) % modulus == 0)

        pairings=[
            sum(int(coords[i,j])*u[j] for j in range(PICARD_RANK))
            for i in range(140)
        ]
        normal=pairings[:NORMAL_COUNT]
        exceptional=pairings[NORMAL_COUNT:NORMAL_COUNT+EXCEPTIONAL_COUNT]
        for expr in normal:
            solver.add(expr>=0,expr<=NORMAL_MASS)
        for expr in exceptional:
            solver.add(expr>=0,expr<=EXCEPTIONAL_MASS)
        solver.add(sum(normal)==NORMAL_MASS)
        solver.add(sum(exceptional)==EXCEPTIONAL_MASS)
        solver.add(sum(degree_u[j]*u[j] for j in range(PICARD_RANK))==DEGREE)
        solver.add(sum(emass_u[j]*u[j] for j in range(PICARD_RANK))==EXCEPTIONAL_MASS)

        assignment=[pairings[int(label)-1] for label in old.ASSIGNMENT]
        aggregate4=[
            sum(int(old.L[i][j])*assignment[j] for j in range(len(old.ASSIGNMENT)))
            for i in range(4)
        ]
        for expr,value in zip(aggregate4,base4):
            solver.add(expr==int(value))

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
                status="UNSAT_BASIS_PAIRING_PICARD_FIBER"
                break
            if result==unknown:
                reason=solver.reason_unknown()
                break
            req(result==sat,"unexpected basis-pairing solver status")
            model=solver.model()
            uvals=[int(model.eval(v,model_completion=True).as_long()) for v in u]
            U=Matrix(uvals)
            xq=gram_inv*U
            req(all(sympy.denom(v)==1 for v in xq),"SAT u failed Gram-lattice integrality")
            x=Matrix([int(v) for v in xq])
            pvals=[int(v) for v in (coords*U)]
            req(min(pvals)>=0 and sum(pvals[:NORMAL_COUNT])==NORMAL_MASS and sum(pvals[NORMAL_COUNT:])==EXCEPTIONAL_MASS,"SAT pairing replay")
            req(adapter.pairing_matrix*x==Matrix(pvals),"SAT Picard reconstruction")
            support=tuple(i for i,v in enumerate(pvals[NORMAL_COUNT:]) if v>0)
            rank=old.support_rank(nodes,support)
            if rank==7:
                status="SAT_BTVA_COMPATIBLE_BASIS_PAIRING_LIFT"
                witness={
                    "retained_basis_pairings_sha256":csha(uvals),
                    "picard_coordinates_sha256":csha([int(v) for v in x]),
                    "all140_pairings_sha256":csha(pvals),
                    "support_indices_0based":list(support),
                    "support_size":len(support),
                    "support_rank":rank,
                }
                break
            flat=old.closure(nodes,support)
            req(flat not in seen,"repeated basis-pairing lazy flat")
            seen.add(flat)
            outside=[k for k in range(EXCEPTIONAL_COUNT) if k not in flat]
            req(outside,"proper flat has no outside node")
            solver.add(sum(exceptional[k] for k in outside)>=1)
            cuts.append({"support_rank":rank,"support_size":len(support),"closure_size":len(flat),"outside_count":len(outside)})
        else:
            reason="max_flat_cuts_exhausted"

        rows.append({
            "global_base4_index":idx,
            "base4":list(base4),
            "terminal_mass":target_mass[idx],
            "result":status,
            "solver_iterations":iterations,
            "lazy_flat_cut_count":len(cuts),
            "reason_unknown":reason,
            "compatible_witness":witness,
        })

    unsat_mass=sum(r["terminal_mass"] for r in rows if r["result"].startswith("UNSAT_"))
    sat_mass=sum(r["terminal_mass"] for r in rows if r["result"].startswith("SAT_"))
    unknown_mass=sum(r["terminal_mass"] for r in rows if r["result"]=="UNKNOWN")
    req(unsat_mass+sat_mass+unknown_mass==TARGET_MASS,"pilot mass conservation")
    out={
      "schema":"STAGE32_MAIN_BTVA_D8_RETAINED_BASIS_PAIRING_PILOT_V1",
      "stage":32,
      "status":"EXACT_BASIS_PAIRING_PILOT_COMPLETE_ZERO_CREDIT" if unknown_mass==0 else "BOUNDED_BASIS_PAIRING_PILOT_WITH_UNKNOWN_ZERO_CREDIT",
      "target":{"row_id":"g0-d008","base4_indices":list(TARGET_INDICES),"selected_terminal_mass":TARGET_MASS},
      "coordinate_change":{
        "variables":"64 retained-basis curve pairings u=Gram*x",
        "retained_basis_known_labels_1based":retained_labels,
        "gram_determinant_abs":EXPECTED_GRAM_DET,
        "gram_hnf_membership_modulus":modulus,
        "gram_hnf_active_congruence_rows":len(congruence_rows),
        "all140_pairings_reconstructed_as_integral_class_coordinates_times_u":True,
        "gram_lattice_membership_exact_for_integral_picard64":True,
      },
      "rows":rows,
      "summary":{
        "unsat_base4_count":sum(1 for r in rows if r["result"].startswith("UNSAT_")),
        "compatible_sat_base4_count":sum(1 for r in rows if r["result"].startswith("SAT_")),
        "unknown_base4_count":sum(1 for r in rows if r["result"]=="UNKNOWN"),
        "unsat_terminal_mass":unsat_mass,
        "compatible_sat_terminal_mass":sat_mass,
        "unknown_terminal_mass":unknown_mass,
        "max_lazy_flat_cut_count":max(int(r["lazy_flat_cut_count"]) for r in rows),
      },
      "source_locks":{
        "full343_worker_blob_sha1":FULL_WORKER_BLOB,
        "full343_retained_blob_sha1":FULL_RETAINED_BLOB,
        "round1_retained_blob_sha1":R1_RETAINED_BLOB,
        "round2_retained_blob_sha1":R2_RETAINED_BLOB,
        "base_picard_solver_blob_sha1":old.BASE_BLOB,
        "node_bridge_blob_sha1":old.NODE_BRIDGE_BLOB,
        "lane178_head":old.LANE178_HEAD,
        "lane178_aggregate_picard_blob_sha1":old.LANE178_AGG_BLOB,
      },
      "execution":{"solver":"Z3_QF_LIA","solver_timeout_ms":args.solver_timeout_ms,"max_flat_cuts":args.max_flat_cuts,"effective_concurrency":1},
      "semantics":{
        "coordinate_change_exact_not_relaxation":True,
        "unsat_is_safe_receiver_rejection":True,
        "sat_is_integral_picard64_plus_rank7_support_but_not_effectivity_claim":True,
        "unknown_is_not_unsat":True,
      },
      "firewalls":{
        "main_pruning_credit":False,"receiver_credit":False,"effectivity_credit":False,
        "theorem_credit":False,"endpoint_credit":False,"full178_complete":False,
        "stage32_closed":False,"merge_authorized":False,
      },
    }
    out["canonical_sha256_without_this_field"]=csha(out)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print("BTVA_D8_BASIS_PAIRING_PILOT_SUMMARY="+json.dumps(out["summary"],sort_keys=True))
    print("BTVA_D8_BASIS_PAIRING_COORDS="+json.dumps(out["coordinate_change"],sort_keys=True))
    print("BTVA_D8_BASIS_PAIRING_PILOT_CANONICAL="+out["canonical_sha256_without_this_field"])


if __name__=="__main__":
    main()
