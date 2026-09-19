#!/usr/bin/env python3
from __future__ import annotations
import argparse,bisect,hashlib,importlib.util,json,sys,time
from pathlib import Path

SOURCE_HEAD="4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2"
OLD_REL=Path("stages/stage32-ex5/hpadj-22_ex5/run_full_bband.py")
OLD_BLOB="2c998a190baaf5f29b33a91fd9efedbb036cef46"
SCHEMA="STAGE32_MAIN_HPADJ22_DIRECT_COUNT_EQUIVALENCE_V1"

def req(v,msg):
    if not v: raise SystemExit("FAIL: "+msg)
def blob(p):
    raw=p.read_bytes();return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
def canon(o):
    x=dict(o);x.pop("canonical_sha256_without_this_field",None)
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":")).encode()).hexdigest()
def load_old(root):
    p=root/OLD_REL;req(p.is_file() and blob(p)==OLD_BLOB,"old worker drift")
    spec=importlib.util.spec_from_file_location("hpadj22_old_for_direct",p);req(spec and spec.loader,"load old")
    m=importlib.util.module_from_spec(spec);sys.modules[spec.name]=m;spec.loader.exec_module(m);return m
def prep_hist(hist):
    qs=[];pref=[];tot=0
    for q,v in sorted((int(q),int(v)) for q,v in hist.items() if int(v)):
        qs.append(q);tot+=v;pref.append(tot)
    return qs,pref,tot
def ple(qs,pref,cut):
    i=bisect.bisect_right(qs,cut)-1
    return 0 if i<0 else pref[i]

def direct_count(old,ctx,joint,band,row_index):
    bc,bnd,h21,h18,h16,p15,p14,counter,rows,rejected,profiles,classes_gt2,tuples_above_second=ctx
    row_id,g0,d0=rows[row_index];g,d=int(g0),int(d0);h=d//2
    interval=old.PLANNED[band];b0,b1=interval
    K=counter.ceil_div(d-16*g+16,4)
    tq=(d*d+16*d+(32 if g==0 else 0))//8
    pre=reject=h22=0
    ca=[counter.component_a(d,a) for a in range(h+1)]
    aprof={}
    qa_values=set()
    for a in range(h+1):
        if ca[a]<0: continue
        for sa in range(4):
            tiers=profiles[a][sa]
            if tiers:
                tt=tuple((int(q),int(v)) for q,v in tiers)
                aprof[(a,sa)]=(tt,sum(v for _,v in tt))
                qa_values.update(q for q,_ in tt)

    for b in range(b0,min(b1,h)+1):
      for c in range(h+1):
        jbc=joint[b][c]
        active=[]
        for sbc in range(8):
          for r in (0,1):
            hist=jbc[sbc][r]
            if hist:
              qs,pref,left=prep_hist(hist)
              if left: active.append((sbc,r,qs,pref,left))
        if not active: continue
        c3=counter.component3(d,b,c)
        if c3<0: continue
        caps=bnd.x4_caps(h16,h,g,b,c)
        surv=[{qa:bnd.survivor_count(caps,0,qa) for qa in qa_values},
              {qa:bnd.survivor_count(caps,1,qa) for qa in qa_values}]
        for a in range(h+1):
          if ca[a]<0: continue
          srem=min(16,d)+ca[a]+c3
          ec={}
          for support in range(11):
            es=bnd.eligible_e(counter,d,g,h,a,b,c,support,srem,K)
            if es:
              ne=len(es); normal_sum=sum(19*d-5*int(e)+1 for e in es)
              ec[support]=(ne,normal_sum)
          if not ec: continue
          for sbc,r,qs,pref,left in active:
            for sa in range(4):
              pv=aprof.get((a,sa)); ev=ec.get(sbc+sa)
              if pv is None or ev is None: continue
              tiers,a_total=pv;ne,normal_sum=ev
              pre += left*a_total*normal_sum
              for qa,va in tiers:
                survive=ple(qs,pref,tq-qa)
                reject += (left-survive)*va*normal_sum
                h22 += survive*va*surv[r][qa]*ne
    retained=int(rejected[(interval,g,d)])
    req(reject==retained,f"retained HPADJ08 reject mismatch {reject}!={retained}")
    req(pre-reject>=0,"negative post")
    return {"pre_mass":pre,"rejected_mass":reject,"post_mass":pre-reject,"hpadj22_exact_survivors":h22,
            "row":{"index":row_index,"row_id":row_id,"g":g,"d":d},"b_interval":list(interval),
            "profile":{"classes_with_more_than_two_qA_bins":classes_gt2,"tuples_above_second_qA_level":tuples_above_second}}

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--source-root",type=Path,required=True);ap.add_argument("--baseline-row",type=Path,required=True)
    ap.add_argument("--band-position",type=int,default=7);ap.add_argument("--row-index",type=int,default=177);ap.add_argument("--output",type=Path,required=True);a=ap.parse_args()
    old=load_old(a.source_root);ctx=old.source_context()
    baseline=json.loads(a.baseline_row.read_text())
    old.validate_row_obj(baseline,a.band_position,a.row_index,ctx[8],old.row_source_locks(ctx[0],ctx[1],ctx[2],ctx[6]))
    b0,b1=old.PLANNED[a.band_position]
    t0=time.perf_counter();joint=ctx[0].build_joint_bc_shard(old.HMAX,b0,b1);t1=time.perf_counter()
    got=direct_count(old,ctx,joint,a.band_position,a.row_index);t2=time.perf_counter()
    bt=baseline["totals"]
    req(got["row"]==baseline["row"],"row identity")
    req(got["b_interval"]==baseline["b_interval"],"band identity")
    for k in ("pre_mass","rejected_mass","post_mass","hpadj22_exact_survivors"):
        req(int(got[k])==int(bt[k]),f"direct-count mismatch {k}: {got[k]} != {bt[k]}")
    req(got["profile"]==baseline["profile"],"profile drift")
    out={"schema":SCHEMA,"stage":32,"status":"EXACT_DIRECT_COUNT_EQUIVALENCE_PASS_ZERO_CREDIT",
      "source":{"hpadj22_source_head":SOURCE_HEAD,"old_band_worker_blob_sha1":OLD_BLOB,
        "baseline_row_canonical":baseline["canonical_sha256_without_this_field"]},
      "target":{"band_position":a.band_position,**got["row"]},
      "timing":{"joint_build_seconds":round(t1-t0,6),"direct_row_seconds":round(t2-t1,6),"total_seconds":round(t2-t0,6)},
      "result":{"pre_mass":got["pre_mass"],"rejected_mass":got["rejected_mass"],"post_mass":got["post_mass"],
        "hpadj22_exact_survivors":got["hpadj22_exact_survivors"],"baseline_hpadj21_floor":int(bt["hpadj21_floor"]),
        "full_exact_identity_on_direct_count_fields":True},
      "replacement_semantics":{"direct_same_population_upper_bound":True,
        "does_not_require_reoptimizing_hpadj21_lp":True,
        "future_full178_composition":"MIN_OF_CURRENT_AUTHORITY_AND_EXACT_HPADJ22_DIRECT_COUNT",
        "additive_subtraction":False,"statistical_independence":False},
      "optimization":{"qbc_prefix":True,"x4_survivor_cache":True,"eligible_e_support_cache":True,"hpadj21_capacity_lp_removed":True},
      "firewalls":{"main_pruning_credit":False,"full178_complete":False,"hostile_audit_required_before_promotion":True,"merge_authorized":False}}
    out["canonical_sha256_without_this_field"]=canon(out)
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,sort_keys=True,separators=(",",":"))+"\n")
    print("HPADJ22_DIRECT_BENCHMARK="+json.dumps(out,sort_keys=True))
if __name__=="__main__":main()
