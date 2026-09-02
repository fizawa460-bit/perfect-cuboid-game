#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,pathlib,urllib.parse,urllib.request,xml.etree.ElementTree as ET
ROOT=pathlib.Path(__file__).resolve().parent
OUT=ROOT/"d2-stageA2-genus2-rankle1-6b-full-parent-genus1-probe.json"
RAW=ROOT/"d2-stageA2-genus2-rankle1-6b-full-parent-genus1-stdout.txt"
URL="https://magma.maths.usyd.edu.au/xml/calculator.xml"; REFERER="https://magma.maths.usyd.edu.au/calc/"; TIMEOUT=600

def submit(code):
    data=urllib.parse.urlencode({"input":code}).encode()
    req=urllib.request.Request(URL,data=data,headers={"Content-Type":"application/x-www-form-urlencoded","Accept":"text/html, application/xml, application/xhtml+xml","Referer":REFERER,"User-Agent":"perfect-cuboid-stage34-6b-full-parent-genus1/1.0"},method="POST")
    with urllib.request.urlopen(req,timeout=TIMEOUT) as resp:
        raw=resp.read().decode("utf-8",errors="replace"); status=resp.status
    root=ET.fromstring(raw); lines=[]
    for result in root.findall(".//results"):
        for line in result.findall(".//line"): lines.append("".join(line.itertext()))
    return status,"\n".join(lines)+("\n" if lines else "")

def val(prefix,out,required=True):
    for line in out.splitlines():
        if line.startswith(prefix): return line[len(prefix):].strip()
    if required: raise RuntimeError(prefix+" missing")
    return None

code=r'''SetColumns(0); SetQuitOnError(true);
Q:=Rationals(); Qp<p>:=PolynomialRing(Q);
q:=9801*p^4-18002*p^2+9801;
H:=HyperellipticCurve(q); assert Genus(H) eq 1;
E,mp:=EllipticCurve(H); print "ELLIPTIC_MODEL:",E;
lo,hi:=RankBounds(E); print "RANK_BOUNDS:",lo,hi;
T,tm:=TorsionSubgroup(E); print "TORSION_INVARIANTS:",Invariants(T); print "TORSION_ORDER:",#T;
print "RANKZERO_TRIGGER:",(lo eq 0 and hi eq 0);
'''
http,out=submit(code); RAW.write_text(out)
bad=any(x in out for x in ("Runtime error","Assertion failed","User error","Internal error"))
status="PASS_RETURN" if http==200 and not bad and "RANK_BOUNDS:" in out else "UNRESOLVED_RESOURCE_OR_EXTERNAL_WALL"
rec={"branch_id":"6b3bcb70c4fda8e6f1e0","status":status,"http":http,"elliptic_model":val("ELLIPTIC_MODEL:",out,False),"rank_bounds":val("RANK_BOUNDS:",out,False),"torsion_invariants":val("TORSION_INVARIANTS:",out,False),"torsion_order":val("TORSION_ORDER:",out,False),"rankzero_trigger":val("RANKZERO_TRIGGER:",out,False)=="true","stdout_sha256":"sha256:"+hashlib.sha256(out.encode()).hexdigest()}
if status!="PASS_RETURN": rec["raw_tail"]=out[-4000:]
payload={"schema":"STAGE34_02B_D2_STAGEA2_GENUS2_RANKLE1_6B_FULL_PARENT_GENUS1_PROBE_V1","status":"DIAGNOSTIC_NO_CREDIT","record":rec,"raw_stdout_sha256":"sha256:"+hashlib.sha256(out.encode()).hexdigest(),"credit":"Diagnostic only. Rank zero would make the elliptic model finite, but complete H(Q) pullback and parent-to-H implication still require exact replay and hostile audit.","firewalls":{"rankzero_alone_closes_branch":False,"diagnostic_is_parent_closure":False,"remaining_30_closed":False,"R29_EXT_CHANG_C_closed":False}}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":status,"rank_bounds":rec["rank_bounds"],"torsion_invariants":rec["torsion_invariants"],"rankzero_trigger":rec["rankzero_trigger"]},sort_keys=True))
