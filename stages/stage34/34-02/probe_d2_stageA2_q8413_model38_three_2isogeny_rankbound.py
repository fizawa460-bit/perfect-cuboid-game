#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,pathlib,urllib.parse,urllib.request,xml.etree.ElementTree as ET

ROOT=pathlib.Path(__file__).resolve().parent
LOCK=ROOT/"d2-stageA2-q8413-model38-three-2isogeny-rankbound-lock.json"
OUT=ROOT/"d2-stageA2-q8413-model38-three-2isogeny-rankbound-probe.json"
RAW=ROOT/"d2-stageA2-q8413-model38-three-2isogeny-rankbound-stdout.txt"
URL="https://magma.maths.usyd.edu.au/xml/calculator.xml"; REFERER="https://magma.maths.usyd.edu.au/calc/"; TIMEOUT=1200

def submit(code:str):
    data=urllib.parse.urlencode({"input":code}).encode(); req=urllib.request.Request(URL,data=data,headers={"Content-Type":"application/x-www-form-urlencoded","Accept":"text/html, application/xml, application/xhtml+xml","Referer":REFERER,"User-Agent":"perfect-cuboid-stage34-q8413-2isogeny/1.1"},method="POST")
    with urllib.request.urlopen(req,timeout=TIMEOUT) as resp: raw=resp.read().decode("utf-8",errors="replace"); status=resp.status
    root=ET.fromstring(raw); lines=[]
    for result in root.findall(".//results"):
        for line in result.findall(".//line"): lines.append("".join(line.itertext()))
    return status,"\n".join(lines)+("\n" if lines else "")

def val(prefix,out):
    for line in out.splitlines():
        if line.startswith(prefix): return line[len(prefix):].strip()
    return None

code=r'''SetColumns(0); SetQuitOnError(true);
Qz<z>:=PolynomialRing(Rationals()); K<ii>:=NumberField(z^2+1);
E:=EllipticCurve([K|0,-89531+578508*ii,0,-51794399748*ii,0]); assert Discriminant(E) ne 0;
A,mp:=TwoTorsionSubgroup(E); assert Invariants(A) eq [2,2];
T:=[mp(a): a in A | a ne A!0]; assert #T eq 3;
print "TWO_TORSION_INVARIANTS:",Invariants(A); print "NONZERO_TWO_TORSION_COUNT:",#T;
bounds:=[];
for j in [1..3] do
  P:=T[j]; print "KERNEL_X_" cat IntegerToString(j) cat ":",P[1];
  phi:=TwoIsogeny(P); b:=RankBound(E : Isogeny:=phi); Append(~bounds,b);
  print "ISOGENY_BOUND_" cat IntegerToString(j) cat ":",b;
end for;
mb,mi:=Minimum(bounds); print "MIN_ISOGENY_BOUND:",mb; print "MIN_ISOGENY_INDEX:",mi;
print "ISOGENY_DIAGNOSTIC_COMPLETE: true";
'''
try: http,out=submit(code); err=None
except Exception as e: http=0; out=""; err=repr(e)
RAW.write_text(out); bad=err is not None or http!=200 or any(x in out for x in ("Runtime error","Assertion failed","User error","Internal error")); complete=val("ISOGENY_DIAGNOSTIC_COMPLETE:",out)=="true"
bounds=[]
for j in range(1,4):
    try: bounds.append(int(val(f"ISOGENY_BOUND_{j}:",out)))
    except Exception: bounds.append(None)
try: minb=int(val("MIN_ISOGENY_BOUND:",out))
except Exception: minb=min((b for b in bounds if b is not None),default=None)
rankzero=(not bad and complete and len(bounds)==3 and all(b is not None for b in bounds) and minb==0)
payload={"schema":"STAGE34_02C_D2_STAGEA2_Q8413_MODEL38_THREE_2ISOGENY_RANKBOUND_PROBE_V2","status":"PASS_EXACT_2ISOGENY_RANKZERO_CANDIDATE_PREAUDIT" if rankzero else ("PASS_2ISOGENY_BOUNDS_NO_CLOSURE" if (not bad and complete and minb is not None) else "OPEN_EXTERNAL_OR_RUNTIME_NO_CREDIT"),"source_lock":LOCK.name,"source_lock_sha256":"sha256:"+hashlib.sha256(LOCK.read_bytes()).hexdigest(),"http":http,"error":err,"complete":complete,"two_torsion_invariants":val("TWO_TORSION_INVARIANTS:",out),"nonzero_two_torsion_count":int(val("NONZERO_TWO_TORSION_COUNT:",out)) if val("NONZERO_TWO_TORSION_COUNT:",out) else None,"kernel_x":[val(f"KERNEL_X_{j}:",out) for j in range(1,4)],"isogeny_rank_bounds":bounds,"minimum_isogeny_rank_bound":minb,"rankzero_candidate":rankzero,"raw_stdout_sha256":"sha256:"+hashlib.sha256(out.encode()).hexdigest(),"credit":"Exact rank-zero PREAUDIT candidate because an exact 2-isogeny Selmer rank upper bound is 0. Authority remains unchanged pending hostile audit and branch adapters.","firewalls":{"positive_bound_proves_rank_one":False,"diagnostic_is_authoritative":False,"hostile_audit_passed":False,"authoritative_remaining_branches":8,"authoritative_remaining_sign_orbits":4,"D2_all_factor_branches_closed":False,"R29_EXT_CHANG_C_closed":False}}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n"); print(json.dumps({"status":payload["status"],"bounds":bounds,"min":minb,"rankzero_candidate":rankzero},sort_keys=True))
