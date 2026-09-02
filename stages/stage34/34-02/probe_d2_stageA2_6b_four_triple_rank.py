#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,pathlib,urllib.parse,urllib.request,xml.etree.ElementTree as ET
ROOT=pathlib.Path(__file__).resolve().parent
OUT=ROOT/"d2-stageA2-6b-four-triple-rank-probe.json"
RAW=ROOT/"d2-stageA2-6b-four-triple-rank-stdout.txt"
URL="https://magma.maths.usyd.edu.au/xml/calculator.xml"; REFERER="https://magma.maths.usyd.edu.au/calc/"; TIMEOUT=900

def submit(code):
    data=urllib.parse.urlencode({"input":code}).encode()
    req=urllib.request.Request(URL,data=data,headers={"Content-Type":"application/x-www-form-urlencoded","Accept":"text/html, application/xml, application/xhtml+xml","Referer":REFERER,"User-Agent":"perfect-cuboid-stage34-6b-four-triple-rank/1.0"},method="POST")
    with urllib.request.urlopen(req,timeout=TIMEOUT) as resp:
        raw=resp.read().decode("utf-8",errors="replace"); status=resp.status
    root=ET.fromstring(raw); lines=[]
    for result in root.findall(".//results"):
        for line in result.findall(".//line"): lines.append("".join(line.itertext()))
    return status,"\n".join(lines)+("\n" if lines else "")

code=r'''SetColumns(0); SetQuitOnError(true);
Q:=Rationals(); Qx<x>:=PolynomialRing(Q);
U:=x^2-1; V:=2*x; A:=20*(x^2-1)+198*x; B:=99*(x^2-1)+40*x;
triples:=[<"U*V*A",U*V*A/((-1)*(-55)*(-5))>,<"U*V*B",U*V*B/((-1)*(-55)*(-11))>,<"U*A*B",U*A*B/((-1)*(-5)*(-11))>,<"V*A*B",V*A*B/((-55)*(-5)*(-11))>];
for rec in triples do
  name:=rec[1]; f:=rec[2]; C:=HyperellipticCurve(f); assert Genus(C) eq 2; J:=Jacobian(C); hi:=RankBound(J); print "TRIPLE:",name," RANK_UPPER:",hi," POLY:",f;
end for;
'''
http,out=submit(code); RAW.write_text(out)
bad=any(x in out for x in ("Runtime error","Assertion failed","User error","Internal error"))
status="PASS_RETURN" if http==200 and not bad and out.count("TRIPLE:")==4 else "UNRESOLVED_RESOURCE_OR_EXTERNAL_WALL"
records=[]
for line in out.splitlines():
    if line.startswith("TRIPLE:"):
        # Magma prints: TRIPLE: name RANK_UPPER: n POLY: ...
        left,poly=line.split(" POLY:",1); toks=left.split(); name=toks[1]; upper=int(toks[3]); records.append({"triple":name,"rank_upper":upper,"polynomial":poly.strip()})
payload={"schema":"STAGE34_02B_D2_STAGEA2_6B_FOUR_TRIPLE_RANK_PROBE_V1","status":"DIAGNOSTIC_NO_CREDIT","branch_id":"6b3bcb70c4fda8e6f1e0","resolved":len(records),"records":records,"rankzero_triples":[r["triple"] for r in records if r["rank_upper"]==0],"raw_stdout_sha256":"sha256:"+hashlib.sha256(out.encode()).hexdigest(),"credit":"Diagnostic rank classification only; no quotient or parent closure credit.","firewalls":{"rankzero_quotient_is_parent_closure":False,"rankbound_is_complete_Qpointset":False,"remaining_30_closed":False,"R29_EXT_CHANG_C_closed":False}}
if status!="PASS_RETURN": payload["raw_tail"]=out[-5000:]
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":status,"records":records,"rankzero_triples":payload["rankzero_triples"]},sort_keys=True))
