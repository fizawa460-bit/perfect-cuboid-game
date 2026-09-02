#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,pathlib,urllib.parse,urllib.request,xml.etree.ElementTree as ET

ROOT=pathlib.Path(__file__).resolve().parent
LOCK=ROOT/"d2-stageA2-q8413-model38-residual-cover-extract-lock.json"
OUT=ROOT/"d2-stageA2-q8413-model38-residual-cover-extract-probe.json"
RAW=ROOT/"d2-stageA2-q8413-model38-residual-cover-extract-stdout.txt"
URL="https://magma.maths.usyd.edu.au/xml/calculator.xml"
REFERER="https://magma.maths.usyd.edu.au/calc/"
TIMEOUT=1800

def submit(code:str):
    data=urllib.parse.urlencode({"input":code}).encode()
    req=urllib.request.Request(URL,data=data,headers={
        "Content-Type":"application/x-www-form-urlencoded",
        "Accept":"text/html, application/xml, application/xhtml+xml",
        "Referer":REFERER,
        "User-Agent":"perfect-cuboid-stage34-q8413-cover-extract/1.0"
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
covers,maps,gmap:=TwoDescent(E : RemoveTorsion:=true);
G:=Domain(gmap);
print "RESIDUAL_SELMER_QUOTIENT_INVARIANTS:",Invariants(G);
print "RESIDUAL_SELMER_QUOTIENT_ORDER:",#G;
print "RESIDUAL_COVER_COUNT:",#covers;
if #covers eq 1 then
  C:=covers[1]; f,h:=HyperellipticPolynomials(C);
  print "RESIDUAL_COVER_GENUS:",Genus(C);
  print "RESIDUAL_COVER_F_DEGREE:",Degree(f);
  print "RESIDUAL_COVER_F_COEFFS:",[K|Coefficient(f,j): j in [0..Degree(f)]];
  print "RESIDUAL_COVER_H_DEGREE:",Degree(h);
  print "RESIDUAL_COVER_H_COEFFS:",[K|Coefficient(h,j): j in [0..Degree(h)]];
  print "RESIDUAL_COVER_DISCRIMINANT:",Discriminant(C);
end if;
print "EXTRACTION_COMPLETE: true";
'''
try:
    http,out=submit(code); err=None
except Exception as e:
    http=0; out=""; err=repr(e)
RAW.write_text(out)
bad=err is not None or http!=200 or any(x in out for x in ("Runtime error","Assertion failed","User error","Internal error"))
complete=val("EXTRACTION_COMPLETE:",out)=="true"
try: order=int(val("RESIDUAL_SELMER_QUOTIENT_ORDER:",out))
except Exception: order=None
try: count=int(val("RESIDUAL_COVER_COUNT:",out))
except Exception: count=None
success=(not bad and complete and order==2 and count==1 and val("RESIDUAL_COVER_F_COEFFS:",out) is not None and val("RESIDUAL_COVER_H_COEFFS:",out) is not None)
payload={
  "schema":"STAGE34_02C_D2_STAGEA2_Q8413_MODEL38_RESIDUAL_COVER_EXTRACT_PROBE_V1",
  "status":"PASS_EXACT_RESIDUAL_COVER_EXTRACTED_PREAUDIT" if success else "OPEN_EXTRACTION_NO_CREDIT",
  "source_lock":LOCK.name,
  "source_lock_sha256":"sha256:"+hashlib.sha256(LOCK.read_bytes()).hexdigest(),
  "http":http,"error":err,"extraction_complete":complete,
  "residual_selmer_quotient_invariants":val("RESIDUAL_SELMER_QUOTIENT_INVARIANTS:",out),
  "residual_selmer_quotient_order":order,"residual_cover_count":count,
  "residual_cover_genus":val("RESIDUAL_COVER_GENUS:",out),
  "residual_cover_f_degree":val("RESIDUAL_COVER_F_DEGREE:",out),
  "residual_cover_f_coeffs":val("RESIDUAL_COVER_F_COEFFS:",out),
  "residual_cover_h_degree":val("RESIDUAL_COVER_H_DEGREE:",out),
  "residual_cover_h_coeffs":val("RESIDUAL_COVER_H_COEFFS:",out),
  "residual_cover_discriminant":val("RESIDUAL_COVER_DISCRIMINANT:",out),
  "raw_stdout_sha256":"sha256:"+hashlib.sha256(out.encode()).hexdigest(),
  "credit":"Extraction only. Even exact success is not rank-zero or branch closure evidence; the frozen quartic must pass a separately source-locked TwoCoverDescent route.",
  "firewalls":{"extraction_success_is_rank_zero":False,"diagnostic_is_authoritative":False,"hostile_audit_passed":False,"authoritative_remaining_branches":8,"authoritative_remaining_sign_orbits":4,"D2_all_factor_branches_closed":False,"R29_EXT_CHANG_C_closed":False,"perfect_cuboid_nonexistence_claim":False}
}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":payload["status"],"order":order,"cover_count":count,"has_f":payload["residual_cover_f_coeffs"] is not None,"has_h":payload["residual_cover_h_coeffs"] is not None},sort_keys=True))
