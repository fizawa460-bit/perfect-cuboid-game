#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,pathlib,urllib.parse,urllib.request,xml.etree.ElementTree as ET

ROOT=pathlib.Path(__file__).resolve().parent
SRC=ROOT/"d2-stageA2-genus2-rankle1-rationalpoints-lock.json"
LOCK=ROOT/"d2-stageA2-genus2-rankle1-three-adapter-lock.json"
OUT=ROOT/"d2-stageA2-genus2-rankle1-three-adapter-probe.json"
RAW=ROOT/"d2-stageA2-genus2-rankle1-three-adapter-stdout.txt"
URL="https://magma.maths.usyd.edu.au/xml/calculator.xml"; REFERER="https://magma.maths.usyd.edu.au/calc/"; TIMEOUT=180

def poly_expr(c):
    deg=len(c)-1;parts=[]
    for i,a in enumerate(c):
        a=int(a);e=deg-i
        if not a:continue
        parts.append(f"({a})*x^{e}" if e else f"({a})")
    return "+".join(parts) or "0"

def submit(code):
    data=urllib.parse.urlencode({"input":code}).encode()
    req=urllib.request.Request(URL,data=data,headers={"Content-Type":"application/x-www-form-urlencoded","Accept":"text/html, application/xml, application/xhtml+xml","Referer":REFERER,"User-Agent":"perfect-cuboid-stage34-genus2-three-adapter/1.0"},method="POST")
    with urllib.request.urlopen(req,timeout=TIMEOUT) as resp: raw=resp.read().decode("utf-8",errors="replace");status=resp.status
    root=ET.fromstring(raw);lines=[]
    for result in root.findall(".//results"):
        for line in result.findall(".//line"):lines.append("".join(line.itertext()))
    return status,"\n".join(lines)+("\n" if lines else "")

def val(prefix,out):
    for line in out.splitlines():
        if line.startswith(prefix):return line[len(prefix):].strip()
    raise RuntimeError(prefix+" missing")

def code_for(c,fac):
    a,b=map(int,c["q"].split('/')); d=list(map(int,c["delta"])); f=poly_expr(c["coefficients_desc_t_degree6"])
    return f'''SetColumns(0);\nSetQuitOnError(true);\nQ:=Rationals(); Qx<x>:=PolynomialRing(Q);\nf:={f}; expected:={fac}; assert f eq expected; C:=HyperellipticCurve(f); J:=Jacobian(C);\nprint \"BEGIN branch={c['branch_id']} q={c['q']} model={c['model_id']}\"; print \"FACTORIZATION:\",Factorization(f);\nlo,hi:=RankBounds(J); print \"RANK_BOUNDS:\",lo,hi; assert hi le 1;\npts,complete:=RationalPointsGenus2(C : RankBound:=1, Fast:=true);\nprint \"COMPLETE:\",complete; print \"POINT_COUNT:\",#pts;\nreceiver_deg_count:=0; full_parent_count:=0; nondeg_full_parent_count:=0;\nfor P in pts do\n X:=P[1]; Z:=P[3]; U:=X^2-Z^2; V:=2*X*Z; A:={a}*U+{b}*V; B:={b}*U+{a}*V;\n zU:=U eq 0; zV:=V eq 0; zA:=A eq 0; zB:=B eq 0; deg:=zU or zV or zA or zB;\n sU:=IsSquare(U/({d[0]})); sV:=IsSquare(V/({d[1]})); sA:=IsSquare(A/({d[2]})); sB:=IsSquare(B/({d[3]})); parent:=sU and sV and sA and sB;\n if deg then receiver_deg_count +:= 1; end if; if parent then full_parent_count +:= 1; end if; if parent and not deg then nondeg_full_parent_count +:= 1; end if;\n print \"POINT:\",P,\" DEG:\",deg,\" PARENT:\",parent,\" SQ_UVAB:\",sU,sV,sA,sB,\" ZEROS_UVAB:\",zU,zV,zA,zB;\nend for;\nprint \"RECEIVER_DEGENERATE_COUNT:\",receiver_deg_count; print \"FULL_PARENT_LIFT_COUNT:\",full_parent_count; print \"NONDEGENERATE_FULL_PARENT_LIFT_COUNT:\",nondeg_full_parent_count;\nprint \"CLOSURE_CANDIDATE:\",complete and nondeg_full_parent_count eq 0; print \"END branch={c['branch_id']}\";\n'''

src=json.loads(SRC.read_text()); lock=json.loads(LOCK.read_text()); byid={x["branch_id"]:x for x in src["targets"]}; records=[];rawparts=[]
for sel in lock["targets"]:
    c=byid[sel["branch_id"]]; assert c["q"]==sel["q"] and int(c["model_id"])==int(sel["model_id"]) and int(c["rank_bounds"][1])==1
    http,out=submit(code_for(c,sel["factorization"])); bad=any(x in out for x in ("Runtime error","Assertion failed","User error","Internal error")); ok=http==200 and f"END branch={c['branch_id']}" in out and not bad
    rec={"branch_id":c["branch_id"],"q":c["q"],"model_id":c["model_id"],"status":"PASS_RETURN" if ok else "UNRESOLVED","stdout_sha256":hashlib.sha256(out.encode()).hexdigest()}
    if ok:
        rb=list(map(int,val("RANK_BOUNDS:",out).split()[:2])); complete=val("COMPLETE:",out)=="true"; cnt=int(val("POINT_COUNT:",out)); deg=int(val("RECEIVER_DEGENERATE_COUNT:",out)); par=int(val("FULL_PARENT_LIFT_COUNT:",out)); nondeg=int(val("NONDEGENERATE_FULL_PARENT_LIFT_COUNT:",out)); cand=val("CLOSURE_CANDIDATE:",out)=="true"
        rec.update({"rank_bounds":rb,"complete":complete,"point_count":cnt,"receiver_degenerate_count":deg,"full_parent_lift_count":par,"nondegenerate_full_parent_lift_count":nondeg,"closure_candidate":cand,"point_lines":[z for z in out.splitlines() if z.startswith("POINT:")]})
    else: rec["raw_tail"]=out[-1200:]
    records.append(rec);rawparts.append(f"===== branch={c['branch_id']} =====\n{out}")
    print(json.dumps({"branch":c["branch_id"],"q":c["q"],"status":rec["status"],"complete":rec.get("complete"),"points":rec.get("point_count"),"candidate":rec.get("closure_candidate")},sort_keys=True))
raw="\n".join(rawparts); RAW.write_text(raw); cands=[r for r in records if r.get("closure_candidate")]
payload={"schema":"STAGE34_02B_D2_STAGEA2_GENUS2_RANKLE1_THREE_ADAPTER_PROBE_V1","status":"DIAGNOSTIC_NO_CREDIT","input_targets":3,"resolved":sum(r["status"]=="PASS_RETURN" for r in records),"complete_pointsets":sum(bool(r.get("complete")) for r in records),"closure_candidate_count":len(cands),"closure_candidate_branch_ids":[r["branch_id"] for r in cands],"records":records,"raw_stdout_sha256":hashlib.sha256(raw.encode()).hexdigest(),"firewalls":{"adapter_candidate_is_parent_closure":False,"unresolved_is_math_failure":False,"remaining_30_closed":False,"R29_EXT_CHANG_C_closed":False}}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print("GENUS2_RANKLE1_THREE_ADAPTER="+json.dumps({k:payload[k] for k in ["status","resolved","complete_pointsets","closure_candidate_count","closure_candidate_branch_ids"]},sort_keys=True))
