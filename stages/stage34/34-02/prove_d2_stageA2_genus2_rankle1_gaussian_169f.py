#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,pathlib,urllib.parse,urllib.request,xml.etree.ElementTree as ET

ROOT=pathlib.Path(__file__).resolve().parent
LOCK=ROOT/"d2-stageA2-genus2-rankle1-gaussian-169f-proof-lock.json"
OUT=ROOT/"d2-stageA2-genus2-rankle1-gaussian-169f-proof-certificate.json"
RAW=ROOT/"d2-stageA2-genus2-rankle1-gaussian-169f-proof-stdout.txt"
URL="https://magma.maths.usyd.edu.au/xml/calculator.xml"
REFERER="https://magma.maths.usyd.edu.au/calc/"
TIMEOUT=1200

def submit(code):
    data=urllib.parse.urlencode({"input":code}).encode()
    req=urllib.request.Request(URL,data=data,headers={
        "Content-Type":"application/x-www-form-urlencoded",
        "Accept":"text/html, application/xml, application/xhtml+xml",
        "Referer":REFERER,
        "User-Agent":"perfect-cuboid-stage34-gaussian-169f-proof/1.0"
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
assert t["branch_id"]=="169f94dd000a9c5c053f"
code=r'''SetColumns(0); SetQuitOnError(true);
Q:=Rationals(); Qz<z>:=PolynomialRing(Q); K<ii>:=NumberField(z^2+1);
Kx<x>:=PolynomialRing(K); FF:=FieldOfFractions(Kx); xx:=FF!x;
f:=-1560*x^5-7921*x^4-3120*x^3+7921*x^2-1560*x;
ff:=FF!f; u:=xx-1/xx;
assert Evaluate(f,-1/xx) eq -ff/xx^6;
lhs:=ff*(xx-ii)^2/xx^4;
rhs:=-(u-2*ii)*(39*u+160)*(40*u+39);
assert lhs eq rhs;
Xq:=-1560*u;
assert (-1560)^2*rhs eq Xq^3+(-7921+3120*ii)*Xq^2+(9734400-24713520*ii)*Xq+30371328000*ii;
print "SYMBOLIC_QUOTIENT_IDENTITIES: true";
E<EX,EY,EZ>:=EllipticCurve([K|0,-7921+3120*ii,0,9734400-24713520*ii,30371328000*ii]);
assert Discriminant(E) ne 0;
lo,hi:=RankBounds(E : Effort:=1); print "RANK_BOUNDS:",lo,hi; assert lo eq 1 and hi eq 1;
T,tm:=TorsionSubgroup(E); tinv:=Invariants(T); print "TORSION_INVARIANTS:",tinv; assert tinv eq [2,2];
P:=E![1/4*(-7140*ii+26433),1/8*(-1461558*ii+1429785),1]; assert P in E; assert Order(P) eq 0; print "FIXED_FREE_POINT:",P;
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
assert infcount eq 1; assert Seqset(Setseq(qxset)) eq {Q!1521,Q!6400};
print "QUOTIENT_INFINITY_COUNT:",infcount; print "FINITE_QX_SET:",qxset;
xs:={@ Q | @};
for qx in qxset do
  uu:=qx/(-1560); sq,sd:=IsSquare(uu^2+4); assert sq;
  for xp in [(uu+sd)/2,(uu-sd)/2] do Include(~xs,xp); end for;
end for;
assert Seqset(Setseq(xs)) eq {Q!(5/8),Q!(-8/5),Q!(3/13),Q!(-13/3)};
nondeg_parent:=0; cpoint_count:=0; degA:=0; degB:=0;
for xp in xs do
  cpt,yy:=IsSquare(Evaluate(f,xp)); assert cpt; cpoint_count +:= 1;
  U:=xp^2-1; V:=2*xp; A:=80*U+39*V; B:=39*U+80*V;
  deg:=U eq 0 or V eq 0 or A eq 0 or B eq 0;
  if A eq 0 then degA +:= 1; end if; if B eq 0 then degB +:= 1; end if;
  assert ((xp eq Q!(5/8) or xp eq Q!(-8/5)) and A eq 0) or ((xp eq Q!(3/13) or xp eq Q!(-13/3)) and B eq 0);
  sU:=IsSquare(U/(-1)); sV:=IsSquare(V/(-195)); sA:=IsSquare(A/(-5)); sB:=IsSquare(B/(-39));
  parent:=sU and sV and sA and sB;
  if parent and not deg then nondeg_parent +:= 1; end if;
  print "PULLBACK_X:",xp," DEG:",deg," A_ZERO:",A eq 0," B_ZERO:",B eq 0," PARENT:",parent," SQ_UVAB:",sU,sV,sA,sB;
  assert deg; assert not parent;
end for;
assert cpoint_count eq 4; assert degA eq 2; assert degB eq 2; assert nondeg_parent eq 0;
X0:=Q!0; Z0:=Q!1; V0:=2*X0*Z0; assert V0 eq 0;
Xinf:=Q!1; Zinf:=Q!0; Vinf:=2*Xinf*Zinf; assert Vinf eq 0;
print "EXCEPTIONAL_X0_DEGENERATE: true";
print "EXCEPTIONAL_INFINITY_DEGENERATE: true";
print "DEGENERATE_A_ZERO_COUNT:",degA; print "DEGENERATE_B_ZERO_COUNT:",degB;
print "NONDEGENERATE_FULL_PARENT_LIFT_COUNT:",nondeg_parent;
print "PROOF_STATUS: PASS_EXACT_GAUSSIAN_ELLIPTIC_PARENT_CLOSURE_169F_PREAUDIT";
'''
http,out=submit(code); RAW.write_text(out)
bad=any(x in out for x in ("Runtime error","Assertion failed","User error","Internal error"))
if http!=200 or bad or "PROOF_STATUS: PASS_EXACT_GAUSSIAN_ELLIPTIC_PARENT_CLOSURE_169F_PREAUDIT" not in out:
    payload={"schema":"STAGE34_02C_D2_STAGEA2_GENUS2_RANKLE1_GAUSSIAN_169F_PROOF_CERTIFICATE_V1","status":"FAIL_REPLAY_NO_CREDIT","http":http,"raw_stdout_sha256":"sha256:"+hashlib.sha256(out.encode()).hexdigest(),"raw_tail":out[-5000:],"firewalls":{"hostile_audit_passed":False,"branch_closed":False,"sign_partner_closed":False,"authoritative_remaining_branches":8,"authoritative_remaining_sign_orbits":4,"R29_EXT_CHANG_C_closed":False}}
    OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
    raise SystemExit("169f proof replay failed")
payload={
  "schema":"STAGE34_02C_D2_STAGEA2_GENUS2_RANKLE1_GAUSSIAN_169F_PROOF_CERTIFICATE_V1",
  "status":val("PROOF_STATUS:",out),
  "branch_id":t["branch_id"],
  "sign_partner":t["sign_partner"],
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
  "degenerate_A_zero_count":int(val("DEGENERATE_A_ZERO_COUNT:",out)),
  "degenerate_B_zero_count":int(val("DEGENERATE_B_ZERO_COUNT:",out)),
  "nondegenerate_full_parent_lift_count":int(val("NONDEGENERATE_FULL_PARENT_LIFT_COUNT:",out)),
  "exceptional_x0_receiver_degenerate":val("EXCEPTIONAL_X0_DEGENERATE:",out)=="true",
  "exceptional_infinity_receiver_degenerate":val("EXCEPTIONAL_INFINITY_DEGENERATE:",out)=="true",
  "raw_stdout_sha256":"sha256:"+hashlib.sha256(out.encode()).hexdigest(),
  "credit":"Exact pre-audit closure evidence for branch 169f94dd000a9c5c053f only. Hostile audit is required before authoritative branch closure; sign-partner transfer separately requires audited sign-involution adapter.",
  "firewalls":{"hostile_audit_passed":False,"branch_closed":False,"sign_partner_closed":False,"authoritative_remaining_branches":8,"authoritative_remaining_sign_orbits":4,"D2_all_factor_branches_closed":False,"R29_EXT_CHANG_C_closed":False,"perfect_cuboid_nonexistence_claim":False}
}
assert payload["symbolic_quotient_identities"] and payload["sat2_fixed_point"]
assert payload["elliptic_chabauty_R"]==4 and payload["elliptic_chabauty_count"]==3
assert payload["quotient_infinity_count"]==1
assert payload["degenerate_A_zero_count"]==2 and payload["degenerate_B_zero_count"]==2
assert payload["nondegenerate_full_parent_lift_count"]==0
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":payload["status"],"branch_id":payload["branch_id"],"R":4,"chabauty_count":3,"nondegenerate_full_parent_lift_count":0},sort_keys=True))
