#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,pathlib,urllib.parse,urllib.request,xml.etree.ElementTree as ET

ROOT=pathlib.Path(__file__).resolve().parent
LOCK=ROOT/"d2-stageA2-q8413-model38-parity-rootnumber-lock.json"
OUT=ROOT/"d2-stageA2-q8413-model38-parity-rootnumber-probe.json"
RAW=ROOT/"d2-stageA2-q8413-model38-parity-rootnumber-stdout.txt"
URL="https://magma.maths.usyd.edu.au/xml/calculator.xml"
REFERER="https://magma.maths.usyd.edu.au/calc/"
TIMEOUT=600

def submit(code:str):
    data=urllib.parse.urlencode({"input":code}).encode()
    req=urllib.request.Request(URL,data=data,headers={
        "Content-Type":"application/x-www-form-urlencoded",
        "Accept":"text/html, application/xml, application/xhtml+xml",
        "Referer":REFERER,
        "User-Agent":"perfect-cuboid-stage34-q8413-rootnumber/1.0"
    },method="POST")
    with urllib.request.urlopen(req,timeout=TIMEOUT) as resp:
        raw=resp.read().decode("utf-8",errors="replace"); status=resp.status
    root=ET.fromstring(raw); lines=[]
    for result in root.findall(".//results"):
        for line in result.findall(".//line"):
            lines.append("".join(line.itertext()))
    return status,"\n".join(lines)+("\n" if lines else "")

def val(prefix:str,out:str):
    for line in out.splitlines():
        if line.startswith(prefix): return line[len(prefix):].strip()
    return None

code=r'''SetColumns(0); SetQuitOnError(true);
Qz<z>:=PolynomialRing(Rationals()); K<ii>:=NumberField(z^2+1);
E:=EllipticCurve([K|0,-89531+578508*ii,0,-51794399748*ii,0]); assert Discriminant(E) ne 0;
T2,t2m:=TwoTorsionSubgroup(E); print "TWO_TORSION_INVARIANTS:",Invariants(T2); assert Invariants(T2) eq [2,2];
w:=RootNumber(E); print "GLOBAL_ROOT_NUMBER:",w; assert w in {-1,1};
print "ROOTNUMBER_COMPLETE: true";
'''
try:
    http,out=submit(code); err=None
except Exception as e:
    http=0; out=""; err=repr(e)
RAW.write_text(out)
bad=err is not None or http!=200 or any(x in out for x in ("Runtime error","Assertion failed","User error","Internal error"))
complete=val("ROOTNUMBER_COMPLETE:",out)=="true"
try: w=int(val("GLOBAL_ROOT_NUMBER:",out))
except Exception: w=None
parity_rankzero_candidate=(not bad and complete and w==1 and val("TWO_TORSION_INVARIANTS:",out)=="[ 2, 2 ]")
payload={
  "schema":"STAGE34_02C_D2_STAGEA2_Q8413_MODEL38_PARITY_ROOTNUMBER_PROBE_V1",
  "status":"PASS_ROOT_PLUS_PARITY_RANKZERO_CANDIDATE_PREAUDIT" if parity_rankzero_candidate else ("PASS_ROOT_MINUS_PARITY_UNRESOLVED" if (not bad and complete and w==-1) else "OPEN_EXTERNAL_OR_RUNTIME_NO_CREDIT"),
  "source_lock":LOCK.name,
  "source_lock_sha256":"sha256:"+hashlib.sha256(LOCK.read_bytes()).hexdigest(),
  "http":http,"error":err,"rootnumber_complete":complete,
  "two_torsion_invariants":val("TWO_TORSION_INVARIANTS:",out),
  "global_root_number":w,
  "parity_rankzero_candidate":parity_rankzero_candidate,
  "raw_stdout_sha256":"sha256:"+hashlib.sha256(out.encode()).hexdigest(),
  "credit":"Root number +1 gives a PREAUDIT exact rank-zero candidate only through the separately locked 2-parity/Selmer adapter. Root number -1 gives no Mordell-Weil rank closure. Authority remains unchanged pending replay/audit and parent classification.",
  "firewalls":{"analytic_rank_used":False,"root_minus_one_proves_MW_rank_one":False,"diagnostic_is_authoritative":False,"hostile_audit_passed":False,"authoritative_remaining_branches":8,"authoritative_remaining_sign_orbits":4,"D2_all_factor_branches_closed":False,"R29_EXT_CHANG_C_closed":False}
}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":payload["status"],"global_root_number":w,"parity_rankzero_candidate":parity_rankzero_candidate},sort_keys=True))
