#!/usr/bin/env python3
from __future__ import annotations
import collections,hashlib,json,pathlib,urllib.parse,urllib.request,xml.etree.ElementTree as ET

ROOT=pathlib.Path(__file__).resolve().parent
LOCK=ROOT/"d2-stageA2-genus2-rankle1-rationalpoints-lock.json"
SRC=ROOT/"d2-stageA2-triple-quotient-model-probe.json"
OUT=ROOT/"d2-stageA2-genus2-rankle1-rationalpoints-probe.json"
RAW=ROOT/"d2-stageA2-genus2-rankle1-rationalpoints-probe-stdout.txt"
URL="https://magma.maths.usyd.edu.au/xml/calculator.xml";REFERER="https://magma.maths.usyd.edu.au/calc/";TIMEOUT=180

def poly_expr(c):
    deg=len(c)-1;parts=[]
    for i,a in enumerate(c):
        a=int(a);e=deg-i
        if not a:continue
        parts.append(f"({a})*x^{e}" if e else f"({a})")
    return "+".join(parts) or "0"
def submit(code):
    data=urllib.parse.urlencode({"input":code}).encode()
    req=urllib.request.Request(URL,data=data,headers={"Content-Type":"application/x-www-form-urlencoded","Accept":"text/html, application/xml, application/xhtml+xml","Referer":REFERER,"User-Agent":"perfect-cuboid-stage34-genus2-rankle1-probe/1.0"},method="POST")
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
def code_for(c):
    a,b=map(int,c["q"].split('/'));d=list(map(int,c["delta"]));f=poly_expr(c["coefficients_desc_t_degree6"])
    return f'''SetColumns(0);\nSetQuitOnError(true);\nQ:=Rationals(); Qx<x>:=PolynomialRing(Q);\nf:={f}; C:=HyperellipticCurve(f);\nprint \"BEGIN branch={c['branch_id']} q={c['q']} model={c['model_id']} triple={c['triple']}\";\npts,complete:=RationalPointsGenus2(C);\nprint \"COMPLETE:\",complete; print \"POINT_COUNT:\",#pts;\nreceiver_deg_count:=0; full_parent_count:=0; nondeg_full_parent_count:=0;\nfor P in pts do\n  X:=P[1]; Z:=P[3]; U:=X^2-Z^2; V:=2*X*Z; A:={a}*U+{b}*V; B:={b}*U+{a}*V;\n  zU:=U eq 0; zV:=V eq 0; zA:=A eq 0; zB:=B eq 0; deg:=zU or zV or zA or zB;\n  sU:=IsSquare(U/({d[0]})); sV:=IsSquare(V/({d[1]})); sA:=IsSquare(A/({d[2]})); sB:=IsSquare(B/({d[3]})); parent:=sU and sV and sA and sB;\n  if deg then receiver_deg_count +:= 1; end if; if parent then full_parent_count +:= 1; end if; if parent and not deg then nondeg_full_parent_count +:= 1; end if;\n  print \"POINT:\",P,\" DEG:\",deg,\" PARENT:\",parent,\" SQ_UVAB:\",sU,sV,sA,sB,\" ZEROS_UVAB:\",zU,zV,zA,zB;\nend for;\nprint \"RECEIVER_DEGENERATE_COUNT:\",receiver_deg_count; print \"FULL_PARENT_LIFT_COUNT:\",full_parent_count; print \"NONDEGENERATE_FULL_PARENT_LIFT_COUNT:\",nondeg_full_parent_count;\nprint \"CLOSURE_CANDIDATE:\",complete and nondeg_full_parent_count eq 0;\nprint \"END branch={c['branch_id']}\";\n'''

lock=json.loads(LOCK.read_text());src=json.loads(SRC.read_text())
assert lock["status"] in ("SOURCE_LOCKED_COLD_NOT_ARMED","SOURCE_LOCKED_PREEXECUTION") and len(lock["targets"])==17
branches={x["branch_id"]:x for x in src["branches"]};models={int(x["model_id"]):x for x in src["models"]}
records=[];rawparts=[]
for i,c in enumerate(lock["targets"],1):
    br=branches[c["branch_id"]];assert br["q"]==c["q"] and list(map(int,br["delta"]))==list(map(int,c["delta"]))
    ent=next(x for x in br["triple_quotients"] if x["triple"]==c["triple"]);assert int(ent["model_id"])==int(c["model_id"]) and int(ent["squareclass"])==int(c["squareclass"])
    m=models[int(c["model_id"])];assert list(map(int,m["coefficients_desc_t_degree6"]))==list(map(int,c["coefficients_desc_t_degree6"]))
    status="UNRESOLVED";err=None;out=""
    try:
        http,out=submit(code_for(c));bad=any(x in out for x in ("Runtime error","Assertion failed","User error","Internal error"))
        if http==200 and f"END branch={c['branch_id']}" in out and not bad:status="PASS_RATIONALPOINTS_RETURN"
        else:err=f"http={http} malformed_or_magma_error"
    except Exception as ex:err=f"{type(ex).__name__}: {ex}"
    rec={"index":i,"q":c["q"],"branch_id":c["branch_id"],"delta":c["delta"],"triple":c["triple"],"model_id":c["model_id"],"rank_bounds_from_census":c["rank_bounds"],"status":status,"error":err}
    if status=="PASS_RATIONALPOINTS_RETURN":
        complete=val("COMPLETE:",out)=="true";cnt=int(val("POINT_COUNT:",out));deg=int(val("RECEIVER_DEGENERATE_COUNT:",out));par=int(val("FULL_PARENT_LIFT_COUNT:",out));nondeg=int(val("NONDEGENERATE_FULL_PARENT_LIFT_COUNT:",out));cand=val("CLOSURE_CANDIDATE:",out)=="true"
        rec.update({"complete":complete,"point_count":cnt,"receiver_degenerate_count":deg,"full_parent_lift_count":par,"nondegenerate_full_parent_lift_count":nondeg,"closure_candidate":cand,"point_lines":[x for x in out.splitlines() if x.startswith("POINT:")],"stdout_sha256":hashlib.sha256(out.encode()).hexdigest()})
        assert cand==(complete and nondeg==0)
    records.append(rec);rawparts.append(f"===== index={i} branch={c['branch_id']} =====\n{out}\nERROR={err or ''}")
    print(json.dumps({"index":i,"branch":c["branch_id"],"q":c["q"],"status":status,"complete":rec.get("complete"),"points":rec.get("point_count"),"nondeg_parent":rec.get("nondegenerate_full_parent_lift_count"),"candidate":rec.get("closure_candidate")},sort_keys=True))
raw="\n".join(rawparts);RAW.write_text(raw)
resolved=[r for r in records if r["status"]=="PASS_RATIONALPOINTS_RETURN"];cands=[r for r in resolved if r.get("closure_candidate")];byq=collections.Counter(r["q"] for r in cands)
payload={"schema":"STAGE34_02_D2_STAGEA2_GENUS2_RANKLE1_RATIONALPOINTS_PROBE_V1","status":"DIAGNOSTIC_NO_CREDIT","input_targets":17,"resolved":len(resolved),"unresolved":17-len(resolved),"complete_pointsets":sum(bool(r.get("complete")) for r in resolved),"closure_candidate_count":len(cands),"closure_candidate_by_q":dict(sorted(byq.items())),"closure_candidate_branch_ids":sorted(r["branch_id"] for r in cands),"nondegenerate_parent_lift_branch_ids":sorted(r["branch_id"] for r in resolved if int(r.get("nondegenerate_full_parent_lift_count",0))>0),"records":records,"raw_stdout_sha256":hashlib.sha256(raw.encode()).hexdigest(),"credit":"Diagnostic complete-pointset and exact parent-lift candidate discovery only. No parent closure is granted here.","firewalls":{"complete_quotient_pointset_is_parent_closure":False,"quotient_point_is_parent_point":False,"diagnostic_candidate_is_parent_closure":False,"unresolved_is_math_failure":False,"R29_EXT_CHANG_C_closed":False}}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print("GENUS2_RANKLE1_RATIONALPOINTS_PROBE="+json.dumps({k:payload[k] for k in ["status","resolved","unresolved","complete_pointsets","closure_candidate_count","closure_candidate_by_q","nondegenerate_parent_lift_branch_ids"]},sort_keys=True))
