#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,pathlib,urllib.parse,urllib.request,xml.etree.ElementTree as ET

ROOT=pathlib.Path(__file__).resolve().parent
LOCK=ROOT/"d2-stageA2-q8413-model38-frozen-cover-twocover-descent-lock.json"
OUT=ROOT/"d2-stageA2-q8413-model38-frozen-cover-twocover-descent-probe.json"
RAW=ROOT/"d2-stageA2-q8413-model38-frozen-cover-twocover-descent-stdout.txt"
URL="https://magma.maths.usyd.edu.au/xml/calculator.xml"
REFERER="https://magma.maths.usyd.edu.au/calc/"
TIMEOUT=1800

def submit(code:str):
    data=urllib.parse.urlencode({"input":code}).encode()
    req=urllib.request.Request(URL,data=data,headers={
        "Content-Type":"application/x-www-form-urlencoded",
        "Accept":"text/html, application/xml, application/xhtml+xml",
        "Referer":REFERER,
        "User-Agent":"perfect-cuboid-stage34-q8413-frozen-cover/1.0"
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
Qz<z>:=PolynomialRing(Rationals()); K<ii>:=NumberField(z^2+1); R<x>:=PolynomialRing(K);
c0:=K!(-71563-103532*ii); c1:=K!(-246956-305762*ii); c2:=K!(21797-173796*ii); c3:=K!(-75720+204690*ii); c4:=K!(32409-20313*ii);
f:=c0+c1*x+c2*x^2+c3*x^3+c4*x^4; C:=HyperellipticCurve(f);
assert Genus(C) eq 1; assert Degree(f) eq 4;
assert [Coefficient(f,j): j in [0..4]] eq [c0,c1,c2,c3,c4];
disc:=Discriminant(C); assert disc eq K!(14020898335778241125546999481038592-4446296205218480995817430937503744*ii);
print "FROZEN_COVER_GENUS:",Genus(C);
print "FROZEN_COVER_F_COEFFS:",[Coefficient(f,j): j in [0..4]];
print "FROZEN_COVER_DISCRIMINANT:",disc;
Hk,AtoHk:=TwoCoverDescent(C);
print "FAKE_TWO_SELMER_CARDINALITY:",#Hk;
print "FAKE_TWO_SELMER_SET:",Hk;
if #Hk gt 0 then
  j:=0; for a in Hk do j+:=1; print "FAKE_TWO_SELMER_ELEMENT:",j,a; end for;
end if;
print "DESCENT_COMPLETE: true";
'''
try:
    http,out=submit(code); err=None
except Exception as e:
    http=0; out=""; err=repr(e)
RAW.write_text(out)
bad=err is not None or http!=200 or any(x in out for x in ("Runtime error","Assertion failed","User error","Internal error"))
complete=val("DESCENT_COMPLETE:",out)=="true"
try: card=int(val("FAKE_TWO_SELMER_CARDINALITY:",out))
except Exception: card=None
empty_candidate=(not bad and complete and card==0)
payload={
  "schema":"STAGE34_02C_D2_STAGEA2_Q8413_MODEL38_FROZEN_COVER_TWOCOVER_DESCENT_PROBE_V1",
  "status":"PASS_EXACT_FROZEN_COVER_NO_QI_POINT_CANDIDATE_PREAUDIT" if empty_candidate else ("PASS_NONEMPTY_FAKE_TWO_SELMER_NO_CLOSURE" if (not bad and complete and card is not None) else "OPEN_EXTERNAL_OR_RUNTIME_NO_CREDIT"),
  "source_lock":LOCK.name,
  "source_lock_sha256":"sha256:"+hashlib.sha256(LOCK.read_bytes()).hexdigest(),
  "http":http,"error":err,"descent_complete":complete,
  "frozen_cover_genus":val("FROZEN_COVER_GENUS:",out),
  "frozen_cover_discriminant":val("FROZEN_COVER_DISCRIMINANT:",out),
  "fake_two_selmer_cardinality":card,
  "fake_two_selmer_set":val("FAKE_TWO_SELMER_SET:",out),
  "frozen_cover_no_Qi_point_candidate":empty_candidate,
  "raw_stdout_sha256":"sha256:"+hashlib.sha256(out.encode()).hexdigest(),
  "credit":"Diagnostic only. If the fake two-Selmer set is empty, this is an exact no-Q(i)-point proof candidate for the frozen quartic under the locked Magma theorem contract. Rank and branch authority remain unchanged pending a separately frozen TwoDescent-to-rank adapter and hostile audit.",
  "firewalls":{"diagnostic_is_authoritative":False,"empty_fake_two_selmer_is_rank_zero_without_adapter":False,"rank_zero_authoritative":False,"rational_X_transfer_proved":False,"parent_transfer_proved":False,"hostile_audit_passed":False,"authoritative_remaining_branches":8,"authoritative_remaining_sign_orbits":4,"D2_all_factor_branches_closed":False,"R29_EXT_CHANG_C_closed":False,"perfect_cuboid_nonexistence_claim":False}
}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":payload["status"],"fake_two_selmer_cardinality":card,"frozen_cover_no_Qi_point_candidate":empty_candidate},sort_keys=True))
