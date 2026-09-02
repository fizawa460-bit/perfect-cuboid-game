#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,pathlib,urllib.parse,urllib.request,xml.etree.ElementTree as ET

ROOT=pathlib.Path(__file__).resolve().parent
LOCK=ROOT/"d2-stageA2-genus2-rankle1-gaussian-03f-proof-lock.json"
OUT=ROOT/"d2-stageA2-genus2-rankle1-gaussian-03f-proof-certificate.json"
RAW=ROOT/"d2-stageA2-genus2-rankle1-gaussian-03f-proof-stdout.txt"
URL="https://magma.maths.usyd.edu.au/xml/calculator.xml"
REFERER="https://magma.maths.usyd.edu.au/calc/"
TIMEOUT=900

def submit(code):
    data=urllib.parse.urlencode({"input":code}).encode()
    req=urllib.request.Request(URL,data=data,headers={
        "Content-Type":"application/x-www-form-urlencoded",
        "Accept":"text/html, application/xml, application/xhtml+xml",
        "Referer":REFERER,
        "User-Agent":"perfect-cuboid-stage34-gaussian-03f-proof/1.0"
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
    raise RuntimeError(prefix+" missing")

lock=json.loads(LOCK.read_text())
t=lock["target"]
assert t["branch_id"]=="03f88290bf80ef2e6c98"
code=r'''SetColumns(0); SetQuitOnError(true);
Q:=Rationals(); Qz<z>:=PolynomialRing(Q); K<ii>:=NumberField(z^2+1);
Kx<x>:=PolynomialRing(K); FF:=FieldOfFractions(Kx); xx:=FF!x;
f:=11*x*(x-1)*(x+1)*(x+11)*(11*x-1);
assert f eq 121*x^5+1320*x^4-242*x^3-1320*x^2+121*x;
ff:=FF!f; u:=xx-1/xx;
assert Evaluate(f,-1/xx) eq -ff/xx^6;
lhs:=ff*(xx-ii)^2/xx^4;
rhs:=11*u*(11*u+120)*(u-2*ii);
assert lhs eq rhs;
Xq:=121*u;
assert 121^2*rhs eq Xq^3+(1320-242*ii)*Xq^2-319440*ii*Xq;
print "SYMBOLIC_QUOTIENT_IDENTITIES: true";
E<EX,EY,EZ>:=EllipticCurve([K|0,1320-242*ii,0,-319440*ii,0]);
assert Discriminant(E) ne 0;
lo,hi:=RankBounds(E : Effort:=1); print "RANK_BOUNDS:",lo,hi; assert lo eq 1 and hi eq 1;
T,tm:=TorsionSubgroup(E); tinv:=Invariants(T); print "TORSION_INVARIANTS:",tinv; assert tinv eq [2,2];
P:=E![96+1392*ii,-17376+53808*ii,1]; assert P in E; assert Order(P) eq 0; print "FIXED_FREE_POINT:",P;
SP:=Saturation([P],2 : TorsionFree:=true); assert #SP eq 1; QP:=SP[1];
assert QP eq P or QP eq -P; print "SAT2_FIXED_POINT: true";
H:=AbelianGroup([2,2,0]); T1:=tm(T.1); T2:=tm(T.2);
hm:=map< H -> E | h :-> (Integers()!Eltseq(h)[1])*T1 + (Integers()!Eltseq(h)[2])*T2 + (Integers()!Eltseq(h)[3])*QP >;
P1:=ProjectiveSpace(Q,1); pi:=map< E -> P1 | [EX,EZ] >; pie:=Extend(pi);
VV,RR:=Chabauty(hm,pi : IndexBound:=2);
print "ELLCHAB_R:",RR; print "ELLCHAB_COUNT:",#VV; assert RR eq 4; assert #VV eq 3;
qxset:={@ Q | @}; infcount:=0;
for g in VV do
  im:=pie(hm(g)); print "GROUP_IMAGE:",g," -> ",im;
  if im[2] eq 0 then infcount +:= 1; else Include(~qxset,Q!(im[1]/im[2])); end if;
end for;
assert infcount eq 1; assert Setseq(qxset) eq [Q!0,Q!-1320] or Setseq(qxset) eq [Q!-1320,Q!0];
print "QUOTIENT_INFINITY_COUNT:",infcount; print "FINITE_QX_SET:",qxset;
xs:={@ Q | @}; nondeg_parent:=0; cpoint_count:=0;
for qx in qxset do
  uu:=qx/121; sq,sd:=IsSquare(uu^2+4); assert sq;
  for xp in [(uu+sd)/2,(uu-sd)/2] do Include(~xs,xp); end for;
end for;
assert Seqset(Setseq(xs)) eq {Q!1,Q!-1,Q!(1/11),Q!-11};
for xp in xs do
  fc:=11*xp*(xp^2-1)*(xp+11)*(11*xp-1); cpt,yy:=IsSquare(fc); assert cpt; cpoint_count +:= 1;
  U:=xp^2-1; V:=2*xp; A:=60*U+11*V; B:=11*U+60*V;
  deg:=U eq 0 or V eq 0 or A eq 0 or B eq 0;
  sU:=IsSquare(U/330); sV:=IsSquare(V/2); sA:=IsSquare(A/22); sB:=IsSquare(B/30);
  parent:=sU and sV and sA and sB;
  if parent and not deg then nondeg_parent +:= 1; end if;
  print "PULLBACK_X:",xp," DEG:",deg," PARENT:",parent," SQ_UVAB:",sU,sV,sA,sB;
  assert deg;
end for;
assert cpoint_count eq 4; assert nondeg_parent eq 0;
print "EXCEPTIONAL_X0_DEGENERATE: true"; // x=0 has V=0
print "EXCEPTIONAL_INFINITY_DEGENERATE: true"; // Z=0 has V=2XZ=0
print "NONDEGENERATE_FULL_PARENT_LIFT_COUNT:",nondeg_parent;
print "PROOF_STATUS: PASS_EXACT_GAUSSIAN_ELLIPTIC_PARENT_CLOSURE_03F_PREAUDIT";
'''
http,out=submit(code); RAW.write_text(out)
bad=any(x in out for x in ("Runtime error","Assertion failed","User error","Internal error"))
if http!=200 or bad or "PROOF_STATUS: PASS_EXACT_GAUSSIAN_ELLIPTIC_PARENT_CLOSURE_03F_PREAUDIT" not in out:
    payload={"schema":"STAGE34_02B_D2_STAGEA2_GENUS2_RANKLE1_GAUSSIAN_03F_PROOF_CERTIFICATE_V1","status":"FAIL_REPLAY_NO_CREDIT","http":http,"raw_stdout_sha256":hashlib.sha256(out.encode()).hexdigest(),"raw_tail":out[-5000:],"firewalls":{"branch_closed":False,"sign_partner_closed":False,"R29_EXT_CHANG_C_closed":False}}
    OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
    raise SystemExit("03f proof replay failed")
payload={
  "schema":"STAGE34_02B_D2_STAGEA2_GENUS2_RANKLE1_GAUSSIAN_03F_PROOF_CERTIFICATE_V1",
  "status":val("PROOF_STATUS:",out),
  "branch_id":t["branch_id"],
  "source_lock":LOCK.name,
  "source_lock_sha256":"sha256:"+hashlib.sha256(LOCK.read_bytes()).hexdigest(),
  "symbolic_quotient_identities":val("SYMBOLIC_QUOTIENT_IDENTITIES:",out)=="true",
  "rank_bounds":val("RANK_BOUNDS:",out),
  "torsion_invariants":val("TORSION_INVARIANTS:",out),
  "fixed_free_point":val("FIXED_FREE_POINT:",out),
  "sat2_fixed_point":val("SAT2_FIXED_POINT:",out)=="true",
  "elliptic_chabauty_R":int(val("ELLCHAB_R:",out)),
  "elliptic_chabauty_count":int(val("ELLCHAB_COUNT:",out)),
  "quotient_infinity_count":int(val("QUOTIENT_INFINITY_COUNT:",out)),
  "finite_QX_set":val("FINITE_QX_SET:",out),
  "nondegenerate_full_parent_lift_count":int(val("NONDEGENERATE_FULL_PARENT_LIFT_COUNT:",out)),
  "exceptional_x0_receiver_degenerate":val("EXCEPTIONAL_X0_DEGENERATE:",out)=="true",
  "exceptional_infinity_receiver_degenerate":val("EXCEPTIONAL_INFINITY_DEGENERATE:",out)=="true",
  "raw_stdout_sha256":"sha256:"+hashlib.sha256(out.encode()).hexdigest(),
  "credit":"Exact pre-audit closure evidence for branch 03f88290bf80ef2e6c98 only. Hostile audit is still required before authoritative branch closure; sign-partner transfer separately requires audited sign-involution adapter.",
  "firewalls":{"hostile_audit_passed":False,"sign_partner_closed":False,"remaining_30_closed":False,"R29_EXT_CHANG_C_closed":False,"perfect_cuboid_nonexistence_claim":False}
}
assert payload["symbolic_quotient_identities"] and payload["sat2_fixed_point"]
assert payload["elliptic_chabauty_R"]==4 and payload["elliptic_chabauty_count"]==3
assert payload["nondegenerate_full_parent_lift_count"]==0
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":payload["status"],"branch_id":payload["branch_id"],"R":4,"chabauty_count":3,"nondegenerate_full_parent_lift_count":0},sort_keys=True))
