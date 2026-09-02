#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,pathlib,urllib.parse,urllib.request,xml.etree.ElementTree as ET

ROOT=pathlib.Path(__file__).resolve().parent
LOCK=ROOT/"d2-stageA2-q8413-model38-residual-twocover-descent-lock.json"
OUT=ROOT/"d2-stageA2-q8413-model38-residual-twocover-descent-probe.json"
RAW=ROOT/"d2-stageA2-q8413-model38-residual-twocover-descent-stdout.txt"
URL="https://magma.maths.usyd.edu.au/xml/calculator.xml"
REFERER="https://magma.maths.usyd.edu.au/calc/"
TIMEOUT=1800

def submit(code):
    data=urllib.parse.urlencode({"input":code}).encode()
    req=urllib.request.Request(URL,data=data,headers={
        "Content-Type":"application/x-www-form-urlencoded",
        "Accept":"text/html, application/xml, application/xhtml+xml",
        "Referer":REFERER,
        "User-Agent":"perfect-cuboid-stage34-q8413-twocover-descent/1.1"
    },method="POST")
    with urllib.request.urlopen(req,timeout=TIMEOUT) as resp:
        raw=resp.read().decode("utf-8",errors="replace"); status=resp.status
    root=ET.fromstring(raw); lines=[]
    for result in root.findall(".//results"):
        for line in result.findall(".//line"):
            lines.append("".join(line.itertext()))
    return status,"\n".join(lines)+("\n" if lines else "")

def val(prefix,out):
    for line in out.splitlines():
        if line.startswith(prefix): return line[len(prefix):].strip()
    return None

lock=json.loads(LOCK.read_text())
code=r'''SetColumns(0); SetQuitOnError(true);
Qz<z>:=PolynomialRing(Rationals()); K<ii>:=NumberField(z^2+1);
E:=EllipticCurve([K|0,-89531+578508*ii,0,-51794399748*ii,0]); assert Discriminant(E) ne 0;
lo,hi:=RankBounds(E : Effort:=1); print "BASELINE_RANK_BOUNDS:",lo,hi; assert lo eq 0 and hi eq 1;
T,tm:=TorsionSubgroup(E); print "TORSION_INVARIANTS:",Invariants(T); assert Invariants(T) eq [2,2];
covers,maps,gmap:=TwoDescent(E : RemoveTorsion:=true);
G:=Domain(gmap); print "RESIDUAL_SELMER_QUOTIENT_INVARIANTS:",Invariants(G); print "RESIDUAL_SELMER_QUOTIENT_ORDER:",#G;
print "RESIDUAL_COVER_COUNT:",#covers;
if #covers eq 1 then
  print "RESIDUAL_COVER:",covers[1];
  Hk,AtoHk:=TwoCoverDescent(covers[1]);
  print "FAKE_TWO_SELMER_CARDINALITY:",#Hk;
else
  print "FAKE_TWO_SELMER_CARDINALITY: -1";
end if;
print "DIAGNOSTIC_COMPLETE: true";
'''
try:
    http,out=submit(code); err=None
except Exception as e:
    http=0; out=""; err=repr(e)
RAW.write_text(out)
bad=err is not None or http!=200 or any(x in out for x in ("Runtime error","Assertion failed","User error","Internal error"))
complete=val("DIAGNOSTIC_COMPLETE:",out)=="true"
cc=int(val("RESIDUAL_COVER_COUNT:",out)) if val("RESIDUAL_COVER_COUNT:",out) not in (None,"") else None
fc=int(val("FAKE_TWO_SELMER_CARDINALITY:",out)) if val("FAKE_TWO_SELMER_CARDINALITY:",out) not in (None,"") else None
go=int(val("RESIDUAL_SELMER_QUOTIENT_ORDER:",out)) if val("RESIDUAL_SELMER_QUOTIENT_ORDER:",out) not in (None,"") else None
rank_zero_candidate=(not bad and complete and go==2 and cc==1 and fc==0)
payload={
  "schema":"STAGE34_02C_D2_STAGEA2_Q8413_MODEL38_RESIDUAL_TWOCOVER_DESCENT_PROBE_V2",
  "status":"PASS_EXACT_RANK_ZERO_CANDIDATE_PREAUDIT" if rank_zero_candidate else "OPEN_DIAGNOSTIC_NO_CREDIT",
  "source_lock":LOCK.name,
  "source_lock_sha256":"sha256:"+hashlib.sha256(LOCK.read_bytes()).hexdigest(),
  "http":http,"error":err,
  "baseline_rank_bounds":val("BASELINE_RANK_BOUNDS:",out),
  "torsion_invariants":val("TORSION_INVARIANTS:",out),
  "residual_selmer_quotient_invariants":val("RESIDUAL_SELMER_QUOTIENT_INVARIANTS:",out),
  "residual_selmer_quotient_order":go,
  "residual_cover_count":cc,
  "fake_two_selmer_cardinality":fc,
  "rank_zero_candidate":rank_zero_candidate,
  "raw_stdout_sha256":"sha256:"+hashlib.sha256(out.encode()).hexdigest(),
  "credit":"Diagnostic only. Empty fake 2-Selmer set on the sole nontrivial class of the order-2 Selmer quotient is an exact rank-zero proof candidate under the locked theorem adapter, but deterministic replay and hostile audit are required before any authority change.",
  "firewalls":{"diagnostic_is_authoritative":False,"rank_zero_authoritative":False,"rational_X_transfer_proved":False,"parent_transfer_proved":False,"hostile_audit_passed":False,"authoritative_remaining_branches":8,"authoritative_remaining_sign_orbits":4,"D2_all_factor_branches_closed":False,"R29_EXT_CHANG_C_closed":False,"perfect_cuboid_nonexistence_claim":False}
}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":payload["status"],"residual_selmer_quotient_order":go,"residual_cover_count":cc,"fake_two_selmer_cardinality":fc,"rank_zero_candidate":rank_zero_candidate},sort_keys=True))
