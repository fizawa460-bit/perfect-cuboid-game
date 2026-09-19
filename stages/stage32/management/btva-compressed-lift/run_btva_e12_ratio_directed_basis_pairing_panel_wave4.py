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

ROOT=Path(__file__).resolve().parents[4]
SELECTOR=ROOT/"stages/stage32/management/btva-compressed-lift/BTVA-D8-E12-RATIO-DIRECTED-WAVE4-SELECTOR-RETAINED.json"
SELECTOR_BLOB="2e340d1605f6b86b5e8bcc681871e1e9656e545c"
FULL_WORKER=ROOT/"stages/stage32/management/btva-compressed-lift/run_btva_base4_full343_shard.py"
FULL_WORKER_BLOB="63321a54f565b2da38efbef756caf8db148f0063"
ALL140=ROOT/"stages/stage32/management/btva-compressed-lift/BTVA-D8-ALL140-RECEIVER-SEMANTICS-RETAINED.json"
ALL140_BLOB="c4c94fc8e2b45ee51660fe3665160fde98659056"
CONIC=ROOT/"stages/stage32/management/btva-compressed-lift/BTVA-D8-PLANE-CONIC-EXCEPTION-SEPARATION.json"
CONIC_BLOB="75d384c194c678ff6158ea793e943bce91741bb8"

DEGREE=8
E=12
NORMAL_MASS=92
NORMAL_COUNT=92
EXCEPTIONAL_COUNT=48
PICARD_RANK=64
EXPECTED_GRAM_DET=268435456

def req(v: bool,msg: str)->None:
    if not v: raise SystemExit("FAIL: "+msg)

def blob(path: Path)->str:
    raw=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()

def csha(v: object)->str:
    return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def load_module(path: Path,name: str):
    spec=importlib.util.spec_from_file_location(name,path)
    req(spec is not None and spec.loader is not None,"module spec "+str(path))
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod);return mod

def functional_u_coeffs(coeffs,ginv: Matrix)->list[int]:
    q=Matrix([[int(v) for v in coeffs]])*ginv
    req(q.shape==(1,PICARD_RANK),"functional shape")
    req(all(sympy.denom(v)==1 for v in q),"functional transform integrality")
    return [int(q[0,j]) for j in range(PICARD_RANK)]

def main()->None:
    ap=argparse.ArgumentParser()
    ap.add_argument("--retained",type=Path,required=True)
    ap.add_argument("--marking",type=Path,required=True)
    ap.add_argument("--lane178-root",type=Path,required=True)
    ap.add_argument("--solver-timeout-ms",type=int,default=2500)
    ap.add_argument("--max-flat-cuts",type=int,default=64)
    ap.add_argument("--output",type=Path,required=True)
    args=ap.parse_args()
    req(0<args.solver_timeout_ms<=5000,"timeout range")
    req(0<args.max_flat_cuts<=128,"cut range")

    req(blob(SELECTOR)==SELECTOR_BLOB,"selector receipt drift")
    sel=json.loads(SELECTOR.read_text())
    keys=[tuple(int(v) for v in row) for row in sel["selected_base4_in_order"]]
    req(len(keys)==32 and len(set(keys))==32,"selector key count")
    req(sel["hypothetical_if_all_selected_unsat"]["additional_tightening_beyond_wave3_partial"]==8360,"selector impact drift")
    req(blob(ALL140)==ALL140_BLOB,"all140 semantics drift")
    req(blob(CONIC)==CONIC_BLOB,"conic separation drift")
    req(blob(FULL_WORKER)==FULL_WORKER_BLOB,"full343 worker drift")

    full=load_module(FULL_WORKER,"s32_e12_ratio_solver_full")
    req(full.PARENT.is_file() and full.blob(full.PARENT)==full.PARENT_BLOB,"parent drift")
    parent=full.load_module(full.PARENT,"s32_e12_ratio_solver_parent")
    old=parent.load_module(parent.RELAXED,"s32_e12_ratio_solver_relaxed")
    lane=args.lane178_root/old.LANE178_AGG_REL
    req(lane.is_file() and old.git_blob(lane)==old.LANE178_AGG_BLOB,"178 source drift")
    v1=old.load_module(old.BASE,"s32_e12_ratio_solver_base")
    bundle=v1.load_retained(args.retained,"s32_e12_ratio_bundle")
    marking=v1.load_retained(args.marking,"s32_e12_ratio_marking")
    data=v1.reconstruct_translation_data(marking,bundle)
    adapter=data["adapter"];bridge=data["bridge"]
    coords=adapter.class_coordinates_in_retained_basis
    gram=Matrix(bundle["picard_gram_64x64"])
    req(coords.shape==(140,64) and gram.shape==(64,64) and gram==gram.T,"Picard shape")
    req(abs(int(gram.det()))==EXPECTED_GRAM_DET,"Gram determinant")
    labels=[int(x) for x in adapter.certificate["retained_basis_known_labels_1based"]]
    req(len(labels)==64 and len(set(labels))==64,"retained labels")
    req(coords.extract([x-1 for x in labels],list(range(64)))==Matrix.eye(64),"retained basis identity")
    req(adapter.pairing_matrix==coords*gram,"pairing reconstruction")

    H=hermite_normal_form(gram); Hinv=H.inv(); modulus=1
    for value in Hinv: modulus=math.lcm(modulus,int(sympy.denom(value)))
    invq=Hinv*modulus
    req(all(sympy.denom(v)==1 for v in invq),"HNF denominator clear")
    congr=[]
    if modulus!=1:
        for i in range(64):
            row=[int(invq[i,j])%modulus for j in range(64)]
            if any(row): congr.append(row)
    req(modulus==8 and len(congr)==23,"Gram HNF regression")

    ginv=gram.inv()
    du=functional_u_coeffs(bridge.degree_functional,ginv)
    eu=functional_u_coeffs(bridge.exceptional_mass_functional,ginv)
    nodes=old.node_matrix(json.loads(old.NODE_BRIDGE.read_text()))
    req(nodes.shape==(48,7) and int(nodes.rank())==7,"node rank")

    rows=[]
    for pos,base4 in enumerate(keys):
        u=[Int(f"u_{pos}_{j}") for j in range(64)]
        s=SolverFor("QF_LIA");s.set(timeout=args.solver_timeout_ms)
        for j,lab in enumerate(labels):
            upper=NORMAL_MASS if lab<=NORMAL_COUNT else E
            s.add(u[j]>=0,u[j]<=upper)
        for row in congr:
            s.add(sum(row[j]*u[j] for j in range(64)) % modulus == 0)
        pair=[sum(int(coords[i,j])*u[j] for j in range(64)) for i in range(140)]
        normal=pair[:92]; exc=pair[92:]
        for expr in normal:s.add(expr>=0,expr<=NORMAL_MASS)
        for expr in exc:s.add(expr>=0,expr<=E)
        s.add(sum(normal)==NORMAL_MASS)
        s.add(sum(exc)==E)
        s.add(sum(du[j]*u[j] for j in range(64))==DEGREE)
        s.add(sum(eu[j]*u[j] for j in range(64))==E)
        assignment=[pair[int(label)-1] for label in old.ASSIGNMENT]
        agg=[sum(int(old.L[i][j])*assignment[j] for j in range(len(old.ASSIGNMENT))) for i in range(4)]
        for expr,val in zip(agg,base4): s.add(expr==int(val))

        seen=set(); cuts=[]; iterations=0; status="UNKNOWN"; reason=None; witness=None
        while iterations<=args.max_flat_cuts:
            iterations+=1; res=s.check()
            if res==unsat:
                status="UNSAT_BASIS_PAIRING_PICARD_FIBER"; break
            if res==unknown:
                reason=s.reason_unknown(); break
            req(res==sat,"unexpected solver status")
            m=s.model();uvals=[int(m.eval(v,model_completion=True).as_long()) for v in u]
            U=Matrix(uvals);xq=ginv*U
            req(all(sympy.denom(v)==1 for v in xq),"SAT Gram integrality")
            pvals=[int(v) for v in coords*U]
            req(min(pvals)>=0 and sum(pvals[:92])==NORMAL_MASS and sum(pvals[92:])==E,"SAT pairing replay")
            support=tuple(i for i,v in enumerate(pvals[92:]) if v>0)
            rank=old.support_rank(nodes,support)
            if rank==7:
                status="SAT_BTVA_COMPATIBLE_BASIS_PAIRING_LIFT"
                witness={"all140_pairings_sha256":csha(pvals),"support_indices_0based":list(support),"support_size":len(support),"support_rank":rank}
                break
            flat=old.closure(nodes,support); req(flat not in seen,"repeated lazy flat");seen.add(flat)
            outside=[k for k in range(48) if k not in flat];req(outside,"proper flat outside")
            s.add(sum(exc[k] for k in outside)>=1)
            cuts.append({"support_rank":rank,"support_size":len(support),"closure_size":len(flat),"outside_count":len(outside)})
        else:
            reason="max_flat_cuts_exhausted"
        rows.append({"selection_order":pos,"base4":list(base4),"result":status,"solver_iterations":iterations,"lazy_flat_cut_count":len(cuts),"reason_unknown":reason,"compatible_witness":witness})

    uc=sum(r["result"].startswith("UNSAT_") for r in rows)
    sc=sum(r["result"].startswith("SAT_") for r in rows)
    kc=sum(r["result"]=="UNKNOWN" for r in rows)
    out={
      "schema":"STAGE32_MAIN_BTVA_D8_E12_RATIO_DIRECTED_BASIS_PAIRING_PANEL_WAVE4_V1",
      "stage":32,
      "status":"EXACT_RATIO_DIRECTED_WAVE4_PANEL_COMPLETE_ZERO_CREDIT" if kc==0 else "BOUNDED_RATIO_DIRECTED_WAVE4_PANEL_WITH_UNKNOWN_ZERO_CREDIT",
      "target":{"row_id":"g0-d008","g":0,"d":8,"e":12,"selected_count":32,"selected_base4_in_order":[list(k) for k in keys]},
      "coordinate_change":{"variables":"64 retained-basis curve pairings u=Gram*x","gram_determinant_abs":EXPECTED_GRAM_DET,"gram_hnf_membership_modulus":modulus,"gram_hnf_active_congruence_rows":len(congr),"gram_lattice_membership_exact_for_integral_picard64":True},
      "rows":rows,
      "summary":{"unsat_base4_count":uc,"compatible_sat_base4_count":sc,"unknown_base4_count":kc,"all_selected_unsat":uc==32,"max_lazy_flat_cut_count":max(r["lazy_flat_cut_count"] for r in rows)},
      "hypothetical_selector_effect_if_all_unsat":sel["hypothetical_if_all_selected_unsat"],
      "source_locks":{"selector_retained_blob_sha1":SELECTOR_BLOB,"full343_worker_blob_sha1":FULL_WORKER_BLOB,"all140_semantics_blob_sha1":ALL140_BLOB,"conic_separation_blob_sha1":CONIC_BLOB,"lane178_head":old.LANE178_HEAD,"lane178_aggregate_blob_sha1":old.LANE178_AGG_BLOB},
      "execution":{"solver":"Z3_QF_LIA","solver_timeout_ms":args.solver_timeout_ms,"max_flat_cuts":args.max_flat_cuts,"effective_concurrency":1},
      "semantics":{"unsat_is_safe_rejection_within_selected_e12_raw_compressed_slice":True,"all140_nonnegativity_used_as_d8_necessary_condition":True,"known_plane_conic_exception_separated_by_d8_degree":True,"sat_does_not_claim_effective_curve":True,"unknown_is_not_unsat":True,"selector_hypothetical_becomes_real_only_for_keys_proved_unsat":True},
      "firewalls":{"main_pruning_credit":False,"receiver_credit":False,"effectivity_credit":False,"theorem_credit":False,"endpoint_credit":False,"full178_complete":False,"stage32_closed":False,"merge_authorized":False}
    }
    out["canonical_sha256_without_this_field"]=csha(out)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n")
    print("BTVA_E12_RATIO_PANEL_SUMMARY="+json.dumps(out["summary"],sort_keys=True))
    print("BTVA_E12_RATIO_PANEL_CANONICAL="+out["canonical_sha256_without_this_field"])

if __name__=="__main__":
    main()
