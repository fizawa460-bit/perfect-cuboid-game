#!/usr/bin/env python3
from __future__ import annotations
import collections,hashlib,json,pathlib,urllib.parse,urllib.request,xml.etree.ElementTree as ET

ROOT=pathlib.Path(__file__).resolve().parent
SRC=ROOT/"d2-stageA2-triple-quotient-model-probe.json"
LOCK=ROOT/"d2-stageA2-genus2-branch-minimal-rank-census-lock.json"
OUT=ROOT/"d2-stageA2-genus2-branch-minimal-rank-census.json"
RAW=ROOT/"d2-stageA2-genus2-branch-minimal-rank-census-stdout.txt"
URL="https://magma.maths.usyd.edu.au/xml/calculator.xml";REFERER="https://magma.maths.usyd.edu.au/calc/"
TIMEOUT=180


def poly_expr(c):
    deg=len(c)-1;parts=[]
    for i,a in enumerate(c):
        a=int(a);e=deg-i
        if not a:continue
        parts.append(f"({a})*x^{e}" if e else f"({a})")
    return "+".join(parts) or "0"

def choose(data):
    mm={int(m["model_id"]):m for m in data["models"]};out=[]
    for br in data["branches"]:
        opts=[]
        for e in br["triple_quotients"]:
            m=mm[int(e["model_id"])];c=list(map(int,m["coefficients_desc_t_degree6"]))
            score=(max(abs(x) for x in c),sum(abs(x) for x in c),int(m["model_id"]))
            opts.append((score,e,m))
        score,e,m=min(opts,key=lambda z:z[0])
        out.append((br,score,e,m))
    assert len(out)==52 and len({x[0]["branch_id"] for x in out})==52
    return sorted(out,key=lambda z:(z[0]["q"],z[0]["branch_id"]))

def triple_product_expr(triple):
    names=triple.split('*');assert len(names)==3 and len(set(names))==3
    return '*'.join(names)

def code_for(br,e,m):
    a,b=map(int,br["q"].split('/'));f=poly_expr(m["coefficients_desc_t_degree6"]);prod=triple_product_expr(e["triple"])
    return f'''SetColumns(0);\nSetQuitOnError(true);\nQ:=Rationals(); Qx<x>:=PolynomialRing(Q);\nf:={f}; C:=HyperellipticCurve(f); J:=Jacobian(C);\nprint \"BEGIN branch={br['branch_id']} q={br['q']} model={m['model_id']} triple={e['triple']}\";\nlo,hi:=RankBounds(J); print \"RANK_BOUNDS:\",lo,hi;\nif hi eq 0 then\n  pts:=Chabauty0(J); all_deg:=true;\n  for P in pts do\n    X:=P[1]; Z:=P[3]; U:=X^2-Z^2; V:=2*X*Z; A:={a}*U+{b}*V; B:={b}*U+{a}*V;\n    if ({prod}) ne 0 then all_deg:=false; end if;\n  end for;\n  print \"CHABAUTY0_COUNT:\",#pts; print \"ALL_SELECTED_PRODUCT_ZERO:\",all_deg; print \"CHABAUTY0_POINTS:\",pts;\nend if;\nprint \"END branch={br['branch_id']}\";\n'''

def submit(code):
    data=urllib.parse.urlencode({"input":code}).encode();req=urllib.request.Request(URL,data=data,headers={"Content-Type":"application/x-www-form-urlencoded","Accept":"text/html, application/xml, application/xhtml+xml","Referer":REFERER,"User-Agent":"perfect-cuboid-stage34-genus2-census/1.0"},method="POST")
    with urllib.request.urlopen(req,timeout=TIMEOUT) as resp:raw=resp.read().decode("utf-8",errors="replace");status=resp.status
    root=ET.fromstring(raw);lines=[]
    for result in root.findall(".//results"):
        for line in result.findall(".//line"):lines.append("".join(line.itertext()))
    return status,"\n".join(lines)+("\n" if lines else "")
def val(prefix,out,required=True):
    for line in out.splitlines():
        if line.startswith(prefix):return line[len(prefix):].strip()
    if required:raise RuntimeError(prefix+" missing")
    return None

lock=json.loads(LOCK.read_text());data=json.loads(SRC.read_text())
assert lock["status"]=="SOURCE_LOCKED_PREEXECUTION" and data["status"]=="DIAGNOSTIC_NO_CREDIT" and data["input_residual_branches"]==52
records=[];rawparts=[]
for idx,(br,score,e,m) in enumerate(choose(data),1):
    code=code_for(br,e,m);status="UNRESOLVED";out="";err=None
    try:
        http,out=submit(code)
        bad=any(x in out for x in ("Runtime error","Assertion failed","User error","Internal error"))
        if http==200 and f"END branch={br['branch_id']}" in out and not bad:status="PASS_RANK_BOUNDS"
        else:err=f"http={http} malformed_or_magma_error"
    except Exception as ex:err=f"{type(ex).__name__}: {ex}"
    rec={"index":idx,"q":br["q"],"branch_id":br["branch_id"],"delta":br["delta"],"triple":e["triple"],"model_id":int(m["model_id"]),"squareclass":int(e["squareclass"]),"coefficients_desc_t_degree6":m["coefficients_desc_t_degree6"],"height_score":list(score),"status":status,"error":err}
    if status=="PASS_RANK_BOUNDS":
        rb=val("RANK_BOUNDS:",out).split();lo,hi=map(int,rb[:2]);assert 0<=lo<=hi
        rec.update({"rank_lower":lo,"rank_upper":hi,"chabauty0_count":None,"all_selected_product_zero":None,"chabauty0_points_raw":None})
        if hi==0:
            rec["chabauty0_count"]=int(val("CHABAUTY0_COUNT:",out));rec["all_selected_product_zero"]=(val("ALL_SELECTED_PRODUCT_ZERO:",out)=="true");rec["chabauty0_points_raw"]=val("CHABAUTY0_POINTS:",out)
    records.append(rec);rawparts.append(f"===== index={idx} branch={br['branch_id']} =====\n{out}\nERROR={err or ''}")
    print(json.dumps({"index":idx,"branch":br["branch_id"],"q":br["q"],"model":m["model_id"],"triple":e["triple"],"status":status,"rank_bounds":[rec.get("rank_lower"),rec.get("rank_upper")],"rank0_all_deg":rec.get("all_selected_product_zero")},sort_keys=True))
raw="\n".join(rawparts);RAW.write_text(raw)
hist=collections.Counter();byq=collections.Counter();candidates=[];unresolved=[]
for r in records:
    if r["status"]!="PASS_RANK_BOUNDS":unresolved.append(r["branch_id"]);continue
    hist[f"{r['rank_lower']},{r['rank_upper']}"]+=1
    if r["rank_upper"]==0 and r["all_selected_product_zero"]:
        candidates.append(r["branch_id"]);byq[r["q"]]+=1
payload={"schema":"STAGE34_02_D2_STAGEA2_GENUS2_BRANCH_MINIMAL_RANK_CENSUS_V1","status":"PASS_COMPLETE_52_RANKBOUND_CENSUS" if not unresolved else "PARTIAL_RANKBOUND_CENSUS_WITH_UNRESOLVED","source_lock":"d2-stageA2-genus2-branch-minimal-rank-census-lock.json","protocol":"official-magma-xml-calculator","input_branches":52,"executed_branches":len(records),"resolved_rankbounds":52-len(unresolved),"unresolved_count":len(unresolved),"unresolved_branch_ids":unresolved,"rank_bounds_histogram":dict(sorted(hist.items())),"rank_upper_lt_2_count":sum(1 for r in records if r.get("rank_upper",99)<2),"rank_upper_zero_count":sum(1 for r in records if r.get("rank_upper")==0),"rankzero_all_degenerate_closure_candidate_count":len(candidates),"rankzero_all_degenerate_closure_candidate_by_q":dict(sorted(byq.items())),"rankzero_all_degenerate_closure_candidate_branch_ids":sorted(candidates),"records":records,"raw_stdout_sha256":hashlib.sha256(raw.encode()).hexdigest(),"credit":"Census and closure-candidate discovery only. Parent closure requires a dedicated proof replay of every promoted rank-zero candidate.","firewalls":{"census_is_parent_closure":False,"rankzero_candidate_is_parent_closure":False,"rank_upper_one_is_complete_Qpointset":False,"unresolved_is_rank_ge_2":False,"remaining_52_closed":False,"R29_EXT_CHANG_C_closed":False}}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print("GENUS2_BRANCH_MINIMAL_CENSUS="+json.dumps({k:payload[k] for k in ["status","resolved_rankbounds","unresolved_count","rank_bounds_histogram","rank_upper_lt_2_count","rank_upper_zero_count","rankzero_all_degenerate_closure_candidate_count","rankzero_all_degenerate_closure_candidate_by_q"]},sort_keys=True))
