#!/usr/bin/env python3
from __future__ import annotations

import argparse
import bisect
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DIRECT_REL = Path("stages/stage32/management/hpadj22-fast-global/benchmark_direct_count.py")
DIRECT_BLOB = "e965ab0a6ea51938006882ca2110016f48b3768e"
FAST = HERE / "verify_fibration_nef_lowmass_parity_separable_picard_min.py"
FAST_BLOB = "a4f7b35e52d01d36614c7f46a592fdb7cb54518b"
BAND = 4
EXPECTED_CURRENT_BAND = 36265487246132086252
CURRENT_GLOBAL = 138652739800650593494


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, "cannot load " + str(path))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def ple(qs, pref, cut: int) -> int:
    i = bisect.bisect_right(qs, int(cut)) - 1
    return 0 if i < 0 else int(pref[i])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", type=Path, required=True)
    ap.add_argument("--source-root", type=Path, required=True)
    args = ap.parse_args()

    direct_path = args.repo_root / DIRECT_REL
    req(direct_path.is_file() and blob(direct_path) == DIRECT_BLOB, "direct-count source drift")
    req(FAST.is_file() and blob(FAST) == FAST_BLOB, "zero-center parity source drift")
    direct = load(direct_path, "stage32_178_global_parity_direct")
    fast = load(FAST, "stage32_178_global_parity_fast")
    old = direct.load_old(args.source_root)
    ctx = old.source_context()
    bc,bnd,h21,h18,h16,p15,p14,counter,rows,rejected,profiles,classes_gt2,tuples_above_second = ctx

    # The source-locked Picard lattice says r0=(b+t) mod2, r1=a mod2.
    # The retained H parity is x1+x8+x9+x10 == 0 mod2, while
    # t=x0+x1+x6+x9 and c=x0+x6+x8+x10. Hence t==c mod2 exactly.
    # Therefore r0=(b+c) mod2 on every current H tuple.
    #
    # The residual penalty is r0/2+r1/10 plus nonnegative terms.  If either
    # r0 or r1 is nonzero, the exact integer qexc=qA+qBC must satisfy
    # qexc <= T-1, where current HPADJ22 only uses qexc<=T.
    # This is a zero-loss necessary cut and deliberately drops every stronger
    # t/x4/cap contribution.
    _cert = fast.load_certificate()

    b0,b1 = old.PLANNED[BAND]
    joint = bc.build_joint_bc_shard(old.HMAX,b0,b1)
    current = refined = 0
    strict_rows = 0
    row_records = []

    ca_cache = {}
    aprof = {}
    qa_values = set()
    for row_index,(row_id,g0,d0) in enumerate(rows):
        g,d = int(g0),int(d0)
        req(d % 2 == 0, f"odd FULL178 degree {row_id}")
        h = d//2
        K = counter.ceil_div(d-16*g+16,4)
        tq = (d*d+16*d+(32 if g==0 else 0))//8

        ca = [counter.component_a(d,a) for a in range(h+1)]
        ca_cache[row_index] = ca
        row_aprof = {}
        row_qas = set()
        for a in range(h+1):
            if ca[a] < 0:
                continue
            for sa in range(4):
                tiers = profiles[a][sa]
                if tiers:
                    tt = tuple((int(q),int(v)) for q,v in tiers)
                    row_aprof[(a,sa)] = (tt,sum(v for _,v in tt))
                    row_qas.update(q for q,_ in tt)
        aprof[row_index] = row_aprof

        row_cur = row_ref = 0
        for b in range(b0,min(b1,h)+1):
            for c in range(h+1):
                jbc = joint[b][c]
                active = []
                for sbc in range(8):
                    for r in (0,1):
                        hist = jbc[sbc][r]
                        if not hist:
                            continue
                        qs=[];pref=[];tot=0
                        for q,v in sorted((int(q),int(v)) for q,v in hist.items() if int(v)):
                            qs.append(q);tot += v;pref.append(tot)
                        if tot:
                            active.append((sbc,r,qs,pref,tot))
                if not active:
                    continue
                c3 = counter.component3(d,b,c)
                if c3 < 0:
                    continue
                caps = bnd.x4_caps(h16,h,g,b,c)
                surv = [
                    {qa:bnd.survivor_count(caps,0,qa) for qa in row_qas},
                    {qa:bnd.survivor_count(caps,1,qa) for qa in row_qas},
                ]
                for a in range(h+1):
                    if ca[a] < 0:
                        continue
                    srem = min(16,d)+ca[a]+c3
                    ec={}
                    for support in range(11):
                        es=bnd.eligible_e(counter,d,g,h,a,b,c,support,srem,K)
                        if es:
                            req(all((int(e)&1)==0 for e in es), f"odd eligible e {(row_id,a,b,c,support)}")
                            ec[support]=len(es)
                    if not ec:
                        continue
                    delta = 1 if ((a & 1) or ((b+c)&1)) else 0
                    for sbc,r,qs,pref,left in active:
                        for sa in range(4):
                            pv=row_aprof.get((a,sa)); ne=ec.get(sbc+sa)
                            if pv is None or ne is None:
                                continue
                            tiers,_atotal=pv
                            for qa,va in tiers:
                                x4count = int(surv[r][qa])
                                if not x4count:
                                    continue
                                cur_h = ple(qs,pref,tq-qa)
                                ref_h = ple(qs,pref,tq-delta-qa)
                                row_cur += cur_h*int(va)*x4count*int(ne)
                                row_ref += ref_h*int(va)*x4count*int(ne)

        req(row_ref <= row_cur, f"refinement weakened {row_id}")
        strict_rows += int(row_ref < row_cur)
        current += row_cur
        refined += row_ref
        row_records.append({
            "row_index":row_index,"row_id":row_id,"g":g,"d":d,
            "current_band4":str(row_cur),"refined_band4":str(row_ref),
            "reduction":str(row_cur-row_ref),
        })

    req(current == EXPECTED_CURRENT_BAND, f"current band4 identity drift {current}")
    reduction = current-refined
    candidate = CURRENT_GLOBAL-reduction
    out = {
        "schema":"STAGE32_32_01_178_HPADJ22_ZERO_CENTER_PARITY_BAND4_V1",
        "status":"EXACT_BAND4_CURRENT_HPADJ22_SAME_POPULATION_REFINEMENT__ZERO_MAIN_CREDIT",
        "band":{"position":BAND,"b_interval":[b0,b1],"rows":len(rows)},
        "result":{
            "current_band_survivors":str(current),
            "refined_band_survivors":str(refined),
            "exact_reduction":str(reduction),
            "strict_rows":strict_rows,
            "current_global_upper_bound":str(CURRENT_GLOBAL),
            "candidate_global_upper_bound_if_promoted":str(candidate),
            "global_reduction_fraction":reduction/CURRENT_GLOBAL,
        },
        "mathematics":{
            "picard_r0":"(b+t) mod 2",
            "retained_H_implies":"t == c (mod 2)",
            "therefore_r0":"(b+c) mod 2",
            "picard_r1":"a mod 2",
            "positive_minimum_penalty_implies_integer_qexc_cut":"qA+qBC <= T-1 whenever r0=1 or r1=1",
            "stronger_t_x4_and_general_cap_terms_deliberately_ignored":True,
            "zero_loss_necessary_condition":True,
        },
        "semantics":{
            "same_population_as_current_hpadj22":True,
            "direct_replacement_not_additive_subtraction":True,
            "statistical_independence":False,
            "non_band4_current_survivors_left_unchanged":True,
            "main_consumption_performed":False,
        },
        "rows":row_records,
        "firewalls":{
            "main_credit_changed":False,"full178_complete":False,
            "hostile_audit_required_before_promotion":True,
            "theorem_credit_changed":False,"endpoint_credit_changed":False,"merge":False,
        },
    }
    print("HPADJ22_ZERO_CENTER_PARITY_BAND4="+json.dumps({
        "current":str(current),"refined":str(refined),"reduction":str(reduction),
        "global_fraction":reduction/CURRENT_GLOBAL,
        "candidate_global":str(candidate),"strict_rows":strict_rows,
    },sort_keys=True))
    print(json.dumps(out,indent=2,sort_keys=True))


if __name__=="__main__":
    main()
