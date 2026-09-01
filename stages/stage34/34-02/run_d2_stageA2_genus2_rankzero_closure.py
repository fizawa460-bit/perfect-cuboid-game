#!/usr/bin/env python3
from __future__ import annotations
import collections,hashlib,json,pathlib,urllib.parse,urllib.request,xml.etree.ElementTree as ET

ROOT=pathlib.Path(__file__).resolve().parent
SRC=ROOT/"d2-stageA2-triple-quotient-model-probe.json"
LOCK=ROOT/"d2-stageA2-genus2-rankzero-closure-lock.json"
OUT=ROOT/"d2-stageA2-genus2-rankzero-closure.json"
RAW=ROOT/"d2-stageA2-genus2-rankzero-closure-stdout.txt"
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
    req=urllib.request.Request(URL,data=data,headers={"Content-Type":"application/x-www-form-urlencoded","Accept":"text/html, application/xml, application/xhtml+xml","Referer":REFERER,"User-Agent":"perfect-cuboid-stage34-genus2-rankzero-proof/1.0"},method="POST")
    with urllib.request.urlopen(req,timeout=TIMEOUT) as resp:raw=resp.read().decode("utf-8",errors="replace");status=resp.status
    root=ET.fromstring(raw);lines=[]
    for result in root.findall(".//results"):
        for line in result.findall(".//line"):lines.append("".join(line.itertext()))
    return status,"\n".join(lines)+("\n" if lines else "")
def val(prefix,out):
    for line in out.splitlines():
        if line.startswith(prefix):return line[len(prefix):].strip()
    raise RuntimeError(prefix+" missing")
def code_for(c):
    a,b=map(int,c["q"].split('/'));f=poly_expr(c["coefficients_desc_t_degree6"]);triple=c["triple"].split('*')
    prod='*'.join(triple)
    return f'''SetColumns(0);\nSetQuitOnError(true);\nQ:=Rationals(); Qx<x>:=PolynomialRing(Q);\nf:={f}; C:=HyperellipticCurve(f); J:=Jacobian(C);\nprint \"BEGIN branch={c['branch_id']} q={c['q']} triple={c['triple']}\";\nlo,hi:=RankBounds(J); print \"RANK_BOUNDS:\",lo,hi;\nassert lo eq 0 and hi eq 0;\npts:=Chabauty0(J); print \"CHABAUTY0_COUNT:\",#pts; assert #pts eq 6;\nall_deg:=true; receiver_ok:=true;\nfor P in pts do\n  X:=P[1]; Z:=P[3]; U:=X^2-Z^2; V:=2*X*Z; A:={a}*U+{b}*V; B:={b}*U+{a}*V;\n  zU:=U eq 0; zV:=V eq 0; zA:=A eq 0; zB:=B eq 0;\n  if ({prod}) ne 0 then all_deg:=false; end if;\n  if not (zU or zV or zA or zB) then receiver_ok:=false; end if;\n  print \"POINT:\",P,\" ZEROS_UVAB:\",zU,zV,zA,zB;\nend for;\nprint \"ALL_SELECTED_PRODUCT_ZERO:\",all_deg; print \"ALL_RECEIVER_DEGENERATE:\",receiver_ok;\nassert all_deg and receiver_ok;\nprint \"END branch={c['branch_id']}\";\n'''

lock=json.loads(LOCK.read_text());src=json.loads(SRC.read_text())
assert lock["status"]=="SOURCE_LOCKED_PREEXECUTION" and src["status"]=="DIAGNOSTIC_NO_CREDIT" and src["input_residual_branches"]==52
branches={x["branch_id"]:x for x in src["branches"]};models={int(x["model_id"]):x for x in src["models"]}
records=[];rawparts=[]
for i,c in enumerate(lock["candidates"],1):
    br=branches[c["branch_id"]];assert br["q"]==c["q"] and list(map(int,br["delta"]))==list(map(int,c["delta"]))
    ent=next(x for x in br["triple_quotients"] if x["triple"]==c["triple"]);assert int(ent["squareclass"])==int(c["squareclass"])
    m=models[int(ent["model_id"])];assert list(map(int,m["coefficients_desc_t_degree6"]))==list(map(int,c["coefficients_desc_t_degree6"]))
    http,out=submit(code_for(c));bad=any(x in out for x in ("Runtime error","Assertion failed","User error","Internal error"))
    assert http==200 and f"END branch={c['branch_id']}" in out and not bad,(c["branch_id"],out[:1500])
    rb=list(map(int,val("RANK_BOUNDS:",out).split()[:2]));assert rb==[0,0]
    count=int(val("CHABAUTY0_COUNT:",out));assert count==6
    allsel=val("ALL_SELECTED_PRODUCT_ZERO:",out)=="true";alldeg=val("ALL_RECEIVER_DEGENERATE:",out)=="true";assert allsel and alldeg
    pts=[line[len("POINT:"):].strip() for line in out.splitlines() if line.startswith("POINT:")]
    rec={"q":c["q"],"branch_id":c["branch_id"],"delta":c["delta"],"triple":c["triple"],"squareclass":c["squareclass"],"coefficients_desc_t_degree6":c["coefficients_desc_t_degree6"],"rank_bounds":[0,0],"complete_qpoint_count":6,"all_selected_product_zero":True,"all_receiver_degenerate":True,"point_lines":pts,"stdout_sha256":hashlib.sha256(out.encode()).hexdigest()}
    records.append(rec);rawparts.append(f"===== branch={c['branch_id']} =====\n{out}")
    print(json.dumps({"index":i,"q":c["q"],"branch":c["branch_id"],"rank_bounds":[0,0],"complete_qpoints":6,"all_receiver_degenerate":True},sort_keys=True))
raw="\n".join(rawparts);RAW.write_text(raw)
byq=collections.Counter(x["q"] for x in records);exp=lock["expected"]
assert len(records)==int(exp["candidate_count"])
assert dict(sorted(byq.items()))==dict(sorted((k,int(v)) for k,v in exp["closed_by_q"].items()))
payload={"schema":"STAGE34_02_D2_STAGEA2_GENUS2_RANKZERO_CLOSURE_V1","status":"PASS_EXACT_GENUS2_RANKZERO_PARENT_CLOSURE_8_OF_52","source_lock":"d2-stageA2-genus2-rankzero-closure-lock.json","input_remaining_branches":52,"closed_branches":len(records),"closed_by_q":dict(sorted(byq.items())),"remaining_branches":int(exp["remaining_after_closure"]),"remaining_by_q":exp["remaining_by_q"],"records":records,"raw_stdout_sha256":hashlib.sha256(raw.encode()).hexdigest(),"proof":"For every listed branch, RankBounds(J)=[0,0] proves genus-two Jacobian rank zero; Chabauty0 therefore gives the complete six-point C(Q) set; every point has a zero selected factor and hence receiver image x in {0,infinity,-1,-q^2}, pure torsion/origin outside the audited nonzero-free-part population.","firewalls":{"eight_branch_closure_is_all_factor_closure":False,"remaining_44_closed":False,"R29_EXT_CHANG_C_closed":False,"perfect_cuboid_nonexistence_claim":False}}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print("GENUS2_RANKZERO_CLOSURE="+json.dumps({"status":payload["status"],"closed":8,"closed_by_q":payload["closed_by_q"],"remaining":44,"remaining_by_q":payload["remaining_by_q"]},sort_keys=True))
