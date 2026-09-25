#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from collections import Counter
from functools import lru_cache
from itertools import product
from pathlib import Path

HERE=Path(__file__).resolve().parent
TQ=HERE/"verify_support_qbc_exact_tq_support_preflight.py"
TQ_BLOB="1f6ede0e60689bcd4c42f4a41252289b241bd213"
PANEL=HERE/"V48-EXACT-TSET-HIGHVALUE-PANEL-RETAINED.json"
PANEL_BLOB="19cfa17b049b94dee5f406cb8db32ca94e8cf318"
PANEL_CANON="ec9aa7f7300f7613bd05ef3dbdd56de45db0193f91c1d7a82ed7f3e4c972de60"
QCAP=4992


def req(v,m):
    if not v: raise SystemExit("FAIL: "+m)


def blob(p):
    b=p.read_bytes();return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\0"+b).hexdigest()


def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()


def load(p,name):
    spec=importlib.util.spec_from_file_location(name,p)
    req(spec is not None and spec.loader is not None,"cannot load "+str(p))
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod);return mod


@lru_cache(maxsize=None)
def pair_q_counts(total:int,k:int,first_lower:int):
    out=Counter()
    for x8 in range(int(total)+1):
        x10=int(total)-x8
        if x8<int(first_lower):
            continue
        if int(x8>0)+int(x10>0)!=int(k):
            continue
        out[x8*x8+x10*x10]+=1
    return out


@lru_cache(maxsize=None)
def exact_tq_counts(b:int,c:int,t:int,support:int,r:int,qcap:int=QCAP):
    """Exact multiplicity Counter qBC -> # canonical H tuples at fixed t."""
    b,c,t,support,r,qcap=map(int,(b,c,t,support,r,qcap))
    out=Counter()
    if not (0<=support<=7 and r in (0,1)) or ((t-c)&1):
        return out

    for x0 in range(min(c,t)+1):
        for x1 in range(x0,min(b,t-x0)+1):
            rem=t-x0-x1
            for x9 in range(max(0,rem-c),min(b-x1,rem)+1):
                x5=b-x1-x9
                x6=rem-x9
                pair_total=c-t+x1+x9
                if min(x5,x6,pair_total)<0:
                    continue
                if ((x0+pair_total)&1)!=r:
                    continue
                base_support=sum(int(v>0) for v in (x0,x1,x5,x6,x9))
                pair_support=support-base_support
                if not (0<=pair_support<=2):
                    continue
                first_lower=0 if x0<x1 else x5+int(x6>x9)
                base_q=x0*x0+x1*x1+x5*x5+x6*x6+x9*x9
                if base_q>qcap:
                    continue
                for pair_q,mult in pair_q_counts(pair_total,pair_support,first_lower).items():
                    q=base_q+pair_q
                    if q<=qcap:
                        out[q]+=int(mult)
    return out


def bounded_literal_regression():
    literal={}
    for xs in product(range(5),repeat=7):
        x0,x1,x5,x6,x8,x9,x10=xs
        b=x1+x5+x9
        c=x0+x6+x8+x10
        if b>4 or c>4:
            continue
        if x0>x1:
            continue
        if x0==x1 and (x5,x6)>(x8,x9):
            continue
        if (x1+x8+x9+x10)&1:
            continue
        t=x0+x1+x6+x9
        support=sum(int(v>0) for v in xs)
        r=(x0+x8+x10)&1
        q=sum(v*v for v in xs)
        literal.setdefault((b,c,t,support,r),Counter())[q]+=1

    mismatch=0
    total_tuple_multiplicity=0
    total_exact_q_values=0
    max_single_q_multiplicity=0
    for key,cnt in literal.items():
        got=exact_tq_counts(*key,QCAP)
        mismatch += int(got!=cnt)
        total_tuple_multiplicity += sum(cnt.values())
        total_exact_q_values += len(cnt)
        max_single_q_multiplicity=max(max_single_q_multiplicity,max(cnt.values()))
    return {
        "literal_keys":len(literal),
        "formula_mismatches":mismatch,
        "total_tuple_multiplicity":total_tuple_multiplicity,
        "total_exact_q_values":total_exact_q_values,
        "max_single_q_multiplicity":max_single_q_multiplicity,
    }


def active_cell_stats(c:int):
    b=36
    t_domain=tuple(range(c&1,b+c+1,2))
    qbc_bins=0
    joint_t_qbc_cells=0
    total_h_multiplicity=0
    max_single_t_qbc_multiplicity=0
    qbc_bins_with_multiple_t=0
    max_exact_t_per_qbc=0

    for support in range(8):
        for r in (0,1):
            per_q={}
            for t in t_domain:
                cnt=exact_tq_counts(b,c,t,support,r,QCAP)
                for q,mult in cnt.items():
                    if mult:
                        per_q.setdefault(q,{})[t]=int(mult)
                        joint_t_qbc_cells += 1
                        total_h_multiplicity += int(mult)
                        max_single_t_qbc_multiplicity=max(
                            max_single_t_qbc_multiplicity,int(mult)
                        )
            qbc_bins += len(per_q)
            qbc_bins_with_multiple_t += sum(int(len(x)>1) for x in per_q.values())
            if per_q:
                max_exact_t_per_qbc=max(max_exact_t_per_qbc,max(len(x) for x in per_q.values()))

    return {
        "c":c,
        "qbc_bins":qbc_bins,
        "joint_t_qbc_cells":joint_t_qbc_cells,
        "total_h_multiplicity_qcap":total_h_multiplicity,
        "max_single_t_qbc_multiplicity":max_single_t_qbc_multiplicity,
        "qbc_bins_with_multiple_t":qbc_bins_with_multiple_t,
        "max_exact_t_per_qbc":max_exact_t_per_qbc,
    }


def main():
    req(TQ.is_file() and blob(TQ)==TQ_BLOB,"exact tq support verifier blob drift")
    req(PANEL.is_file() and blob(PANEL)==PANEL_BLOB,"retained panel blob drift")
    panel=json.loads(PANEL.read_text())
    req(canon(panel)==PANEL_CANON==panel["canonical_sha256_without_this_field"],
        "retained panel canonical drift")

    tq=load(TQ,"exact_tq_multiplicity_support")
    literal=bounded_literal_regression()
    req(literal=={
        "literal_keys":197,
        "formula_mismatches":0,
        "total_tuple_multiplicity":686,
        "total_exact_q_values":256,
        "max_single_q_multiplicity":10,
    },f"bounded multiplicity regression drift {literal}")

    expected={
        83:{"qbc_bins":8274,"joint_t_qbc_cells":268838,
            "total_h_multiplicity_qcap":11772562,
            "max_single_t_qbc_multiplicity":641,
            "qbc_bins_with_multiple_t":8202,"max_exact_t_per_qbc":56},
        85:{"qbc_bins":7909,"joint_t_qbc_cells":261160,
            "total_h_multiplicity_qcap":12073210,
            "max_single_t_qbc_multiplicity":665,
            "qbc_bins_with_multiple_t":7841,"max_exact_t_per_qbc":58},
        89:{"qbc_bins":7152,"joint_t_qbc_cells":240759,
            "total_h_multiplicity_qcap":12448811,
            "max_single_t_qbc_multiplicity":671,
            "qbc_bins_with_multiple_t":7104,"max_exact_t_per_qbc":59},
    }
    retained={int(x["c"]):int(x["active_tset_states"]) for x in panel["cells"]}
    rows=[]
    for c in (83,85,89):
        row=active_cell_stats(c)
        req({k:row[k] for k in expected[c]}==expected[c],
            f"active multiplicity summary drift c={c}: {row}")
        req(row["qbc_bins"]==retained[c],
            f"multiplicity marginal support disagrees with retained qBC histogram c={c}")
        rows.append(row)

    req(sum(x["qbc_bins"] for x in rows)==23335,"three-cell qBC bin total drift")
    req(sum(x["joint_t_qbc_cells"] for x in rows)==770757,"three-cell joint t-qBC cell total drift")
    req(sum(x["total_h_multiplicity_qcap"] for x in rows)==36294583,
        "three-cell H multiplicity total drift")

    out={
        "schema":"STAGE32_32_01_178_SUPPORT_QBC_EXACT_TQ_MULTIPLICITY_PREFLIGHT_V1",
        "status":"EXACT_CANONICAL_T_QBC_MULTIPLICITY_FACTORIZATION__ZERO_MAIN_CREDIT",
        "source_locks":{
            "exact_tq_support_verifier_blob_sha1":TQ_BLOB,
            "retained_exact_tset_panel_blob_sha1":PANEL_BLOB,
            "retained_exact_tset_panel_canonical_sha256":PANEL_CANON,
        },
        "claim":{
            "fixed_data":"(b,c,H-support,r)",
            "exact_factorization":"for every t and exact qBC bin, count the exact multiplicity of retained canonical H tuples",
            "marginal_identity_required_at_replay":"future consumer must require sum_t multiplicity(t,qBC)=the source qBC histogram multiplicity for every (support,r,qBC) before using the refinement",
            "consumer_improvement":"replace qBC-bin multiplicity times union-over-t x4 count by sum_t exact_multiplicity(t,qBC) times the single-t x4 count",
            "dominance":"the exact correlated count is <= the exact-tset union upper bound pointwise because each single-t x4 count is bounded by the union x4 count",
            "actual_weighted_v48_gain_claimed":False,
        },
        "bounded_literal_enumeration":literal,
        "active_three_cell_structural_scan":rows,
        "active_three_cell_totals":{
            "qbc_bins":23335,
            "joint_t_qbc_cells":770757,
            "total_h_multiplicity_qcap":36294583,
        },
        "next_gate":"in the weighted panel replay, cross-check every exact multiplicity marginal against the source qBC histogram, then consume the t-correlated multiplicities directly",
        "firewalls":{
            "main_credit":False,"full178_numerical_census_changed":False,
            "effectivity_credit":False,"receiver_credit":False,"route_credit":False,
            "theorem_credit":False,"endpoint_credit":False,"stage32_closed":False,
            "merge_authorized":False,
        },
    }
    print("SUPPORT_QBC_EXACT_TQ_MULTIPLICITY_PREFLIGHT="+json.dumps(out,sort_keys=True))

if __name__=="__main__": main()
