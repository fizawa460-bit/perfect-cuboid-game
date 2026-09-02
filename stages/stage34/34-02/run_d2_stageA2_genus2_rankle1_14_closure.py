#!/usr/bin/env python3
from __future__ import annotations
import collections,hashlib,json,pathlib,urllib.parse,urllib.request,xml.etree.ElementTree as ET

ROOT=pathlib.Path(__file__).resolve().parent
TARGETS=ROOT/"d2-stageA2-genus2-rankle1-rationalpoints-lock.json"
LOCK=ROOT/"d2-stageA2-genus2-rankle1-14-closure-lock.json"
OUT=ROOT/"d2-stageA2-genus2-rankle1-14-closure.json"
RAW=ROOT/"d2-stageA2-genus2-rankle1-14-closure-stdout.txt"
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
    req=urllib.request.Request(URL,data=data,headers={"Content-Type":"application/x-www-form-urlencoded","Accept":"text/html, application/xml, application/xhtml+xml","Referer":REFERER,"User-Agent":"perfect-cuboid-stage34-genus2-rankle1-proof/1.0"},method="POST")
    with urllib.request.urlopen(req,timeout=TIMEOUT) as resp: raw=resp.read().decode("utf-8",errors="replace");status=resp.status
    root=ET.fromstring(raw);lines=[]
    for result in root.findall(".//results"):
        for line in result.findall(".//line"):lines.append("".join(line.itertext()))
    return status,"\n".join(lines)+( "\n" if lines else "")

def val(prefix,out):
    for line in out.splitlines():
        if line.startswith(prefix):return line[len(prefix):].strip()
    raise RuntimeError(prefix+" missing")

def code_for(c,expected_count):
    a,b=map(int,c["q"].split('/'));d=list(map(int,c["delta"]));f=poly_expr(c["coefficients_desc_t_degree6"])
    return f'''SetColumns(0);\nSetQuitOnError(true);\nQ:=Rationals(); Qx<x>:=PolynomialRing(Q);\nf:={f}; C:=HyperellipticCurve(f); J:=Jacobian(C);\nprint \"BEGIN branch={c['branch_id']} q={c['q']} model={c['model_id']} triple={c['triple']}\";\nlo,hi:=RankBounds(J); print \"RANK_BOUNDS:\",lo,hi; assert hi le 1;\npts,complete:=RationalPointsGenus2(C); print \"COMPLETE:\",complete; print \"POINT_COUNT:\",#pts; assert complete; assert #pts eq {expected_count};\nreceiver_deg_count:=0; full_parent_count:=0; nondeg_full_parent_count:=0;\nfor P in pts do\n  X:=P[1]; Z:=P[3]; U:=X^2-Z^2; V:=2*X*Z; A:={a}*U+{b}*V; B:={b}*U+{a}*V;\n  zU:=U eq 0; zV:=V eq 0; zA:=A eq 0; zB:=B eq 0; deg:=zU or zV or zA or zB;\n  sU:=IsSquare(U/({d[0]})); sV:=IsSquare(V/({d[1]})); sA:=IsSquare(A/({d[2]})); sB:=IsSquare(B/({d[3]})); parent:=sU and sV and sA and sB;\n  if deg then receiver_deg_count +:= 1; end if; if parent then full_parent_count +:= 1; end if; if parent and not deg then nondeg_full_parent_count +:= 1; end if;\n  print \"POINT:\",P,\" DEG:\",deg,\" PARENT:\",parent,\" SQ_UVAB:\",sU,sV,sA,sB,\" ZEROS_UVAB:\",zU,zV,zA,zB;\nend for;\nprint \"RECEIVER_DEGENERATE_COUNT:\",receiver_deg_count; print \"FULL_PARENT_LIFT_COUNT:\",full_parent_count; print \"NONDEGENERATE_FULL_PARENT_LIFT_COUNT:\",nondeg_full_parent_count;\nassert nondeg_full_parent_count eq 0;\nprint \"END branch={c['branch_id']}\";\n'''

lock=json.loads(LOCK.read_text());targets=json.loads(TARGETS.read_text())
assert lock["status"]=="SOURCE_LOCKED_PREEXECUTION" and len(lock["candidates"])==14 and len(targets["targets"])==17
byid={x["branch_id"]:x for x in targets["targets"]}
records=[];rawparts=[]
for i,sel in enumerate(lock["candidates"],1):
    c=byid[sel["branch_id"]];assert c["q"]==sel["q"]
    http,out=submit(code_for(c,int(sel["expected_point_count"])))
    bad=any(x in out for x in ("Runtime error","Assertion failed","User error","Internal error"))
    assert http==200 and f"END branch={c['branch_id']}" in out and not bad,(c["branch_id"],out[:2000])
    rb=list(map(int,val("RANK_BOUNDS:",out).split()[:2]));assert rb[1]<=1
    complete=val("COMPLETE:",out)=="true";assert complete
    cnt=int(val("POINT_COUNT:",out));assert cnt==int(sel["expected_point_count"])
    deg=int(val("RECEIVER_DEGENERATE_COUNT:",out));par=int(val("FULL_PARENT_LIFT_COUNT:",out));nondeg=int(val("NONDEGENERATE_FULL_PARENT_LIFT_COUNT:",out));assert nondeg==0
    pts=[line[len("POINT:"):].strip() for line in out.splitlines() if line.startswith("POINT:")]
    rec={"q":c["q"],"branch_id":c["branch_id"],"delta":c["delta"],"triple":c["triple"],"model_id":c["model_id"],"squareclass":c["squareclass"],"coefficients_desc_t_degree6":c["coefficients_desc_t_degree6"],"rank_bounds":rb,"complete":True,"complete_qpoint_count":cnt,"receiver_degenerate_count":deg,"full_parent_lift_count":par,"nondegenerate_full_parent_lift_count":0,"point_lines":pts,"stdout_sha256":hashlib.sha256(out.encode()).hexdigest()}
    records.append(rec);rawparts.append(f"===== branch={c['branch_id']} =====\n{out}")
    print(json.dumps({"index":i,"q":c["q"],"branch":c["branch_id"],"rank_bounds":rb,"complete_qpoints":cnt,"full_parent_lifts":par,"nondeg_parent":0},sort_keys=True))
raw="\n".join(rawparts);RAW.write_text(raw)
byq=collections.Counter(x["q"] for x in records);exp=lock["expected"]
assert len(records)==int(exp["candidate_count"])
assert dict(sorted(byq.items()))==dict(sorted((k,int(v)) for k,v in exp["closed_by_q"].items()))
payload={"schema":"STAGE34_02B_D2_STAGEA2_GENUS2_RANKLE1_14_CLOSURE_V1","status":"PASS_EXACT_GENUS2_RANKLE1_PARENT_CLOSURE_14_OF_44","source_lock":"d2-stageA2-genus2-rankle1-14-closure-lock.json","input_remaining_branches":44,"closed_branches":14,"closed_by_q":dict(sorted(byq.items())),"remaining_branches":int(exp["remaining_after_closure"]),"remaining_by_q":exp["remaining_by_q"],"records":records,"raw_stdout_sha256":hashlib.sha256(raw.encode()).hexdigest(),"proof":"For each of the fourteen hostile-audited selected genus-two quotients, an independent replay verifies Jacobian rank upper bound at most one, RationalPointsGenus2 returns complete=true, and exhaustive exact U,V,A,B/delta square tests show that every full parent lift has a zero factor. Those zero-factor lifts are the previously audited torsion/origin degeneracies, so no point belongs to the nonzero-free-part receiver population.","firewalls":{"fourteen_branch_closure_is_all_factor_closure":False,"remaining_30_closed":False,"direct_cover_rational_points_complete":False,"all_multiples_closed":False,"R29_EXT_CHANG_C_closed":False,"perfect_cuboid_nonexistence_claim":False}}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print("GENUS2_RANKLE1_14_CLOSURE="+json.dumps({"status":payload["status"],"closed":14,"closed_by_q":payload["closed_by_q"],"remaining":payload["remaining_branches"],"remaining_by_q":payload["remaining_by_q"]},sort_keys=True))
