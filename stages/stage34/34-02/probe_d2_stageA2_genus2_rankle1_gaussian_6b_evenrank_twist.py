#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,pathlib,urllib.parse,urllib.request,xml.etree.ElementTree as ET
ROOT=pathlib.Path(__file__).resolve().parent
LOCK=ROOT/"d2-stageA2-genus2-rankle1-gaussian-6b-evenrank-twist-lock.json"
OUT=ROOT/"d2-stageA2-genus2-rankle1-gaussian-6b-evenrank-twist-probe.json"
RAW=ROOT/"d2-stageA2-genus2-rankle1-gaussian-6b-evenrank-twist-stdout.txt"
URL="https://magma.maths.usyd.edu.au/xml/calculator.xml"; REFERER="https://magma.maths.usyd.edu.au/calc/"; TIMEOUT=900

def submit(code):
    data=urllib.parse.urlencode({"input":code}).encode()
    req=urllib.request.Request(URL,data=data,headers={"Content-Type":"application/x-www-form-urlencoded","Accept":"text/html, application/xml, application/xhtml+xml","Referer":REFERER,"User-Agent":"perfect-cuboid-stage34-6b-evenrank-twist/1.0"},method="POST")
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
Q:=Rationals(); Qx<x>:=PolynomialRing(Q);
f:=-11*x*(x^2-1)*(x+10)*(10*x-1);
assert f eq -110*x^5-1089*x^4+220*x^3+1089*x^2-110*x;
C:=HyperellipticCurve(f); J:=Jacobian(C);
Ct:=HyperellipticCurve(-f); Jt:=Jacobian(Ct);
u:=RankBound(J); ut:=RankBound(Jt);
print "ORIGINAL_RANK_UPPER:",u;
print "TWIST_MINUS1_RANK_UPPER:",ut;
print "DESIRED_EVENRANK_TRIGGER:",(u le 1 and ut eq 0);
'''
http,out=submit(code); RAW.write_text(out)
bad=any(x in out for x in ("Runtime error","Assertion failed","User error","Internal error"))
status="PASS_RETURN" if http==200 and not bad and "TWIST_MINUS1_RANK_UPPER:" in out else "UNRESOLVED_RESOURCE_OR_EXTERNAL_WALL"
rec={"branch_id":"6b3bcb70c4fda8e6f1e0","status":status,"http":http,"original_rank_upper":val("ORIGINAL_RANK_UPPER:",out,False),"twist_minus1_rank_upper":val("TWIST_MINUS1_RANK_UPPER:",out,False),"evenrank_trigger":val("DESIRED_EVENRANK_TRIGGER:",out,False)=="true","stdout_sha256":"sha256:"+hashlib.sha256(out.encode()).hexdigest()}
if status!="PASS_RETURN": rec["raw_tail"]=out[-4000:]
payload={"schema":"STAGE34_02B_D2_STAGEA2_GENUS2_RANKLE1_GAUSSIAN_6B_EVENRANK_TWIST_PROBE_V1","status":"DIAGNOSTIC_NO_CREDIT","record":rec,"raw_stdout_sha256":"sha256:"+hashlib.sha256(out.encode()).hexdigest(),"credit":"Diagnostic structural rank test only. No branch closure without exact isogeny/eigenspace replay, finite quotient pullback, and hostile audit.","firewalls":{"evenrank_trigger_is_branch_closure":False,"sign_partner_transfer_authoritative_before_audit":False,"remaining_30_closed":False,"R29_EXT_CHANG_C_closed":False}}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":status,"original_rank_upper":rec["original_rank_upper"],"twist_minus1_rank_upper":rec["twist_minus1_rank_upper"],"evenrank_trigger":rec["evenrank_trigger"]},sort_keys=True))
