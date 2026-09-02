#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,pathlib,urllib.parse,urllib.request,xml.etree.ElementTree as ET

ROOT=pathlib.Path(__file__).resolve().parent
LOCK=ROOT/"d2-stageA2-6b-uvb-rankzero-proof-lock.json"
OUT=ROOT/"d2-stageA2-6b-uvb-rankzero-proof-certificate.json"
RAW=ROOT/"d2-stageA2-6b-uvb-rankzero-proof-stdout.txt"
URL="https://magma.maths.usyd.edu.au/xml/calculator.xml"; REFERER="https://magma.maths.usyd.edu.au/calc/"; TIMEOUT=600

def submit(code):
    data=urllib.parse.urlencode({"input":code}).encode()
    req=urllib.request.Request(URL,data=data,headers={"Content-Type":"application/x-www-form-urlencoded","Accept":"text/html, application/xml, application/xhtml+xml","Referer":REFERER,"User-Agent":"perfect-cuboid-stage34-6b-uvb-rankzero-proof/1.0"},method="POST")
    with urllib.request.urlopen(req,timeout=TIMEOUT) as resp:
        raw=resp.read().decode("utf-8",errors="replace"); status=resp.status
    root=ET.fromstring(raw); lines=[]
    for result in root.findall(".//results"):
        for line in result.findall(".//line"): lines.append("".join(line.itertext()))
    return status,"\n".join(lines)+("\n" if lines else "")

def val(prefix,out):
    for line in out.splitlines():
        if line.startswith(prefix): return line[len(prefix):].strip()
    raise RuntimeError(prefix+" missing")

lock=json.loads(LOCK.read_text()); assert lock["status"]=="SOURCE_LOCKED_PREEXECUTION_PROOF_REPLAY"
code=r'''SetColumns(0); SetQuitOnError(true);
Q:=Rationals(); Qx<x>:=PolynomialRing(Q);
U:=x^2-1; V:=2*x; A:=20*U+99*V; B:=99*U+20*V;
f:=(U/(-1))*(V/(-55))*(B/(-11));
fexp:=-18/55*x^5-16/121*x^4+36/55*x^3+16/121*x^2-18/55*x;
assert f eq fexp; print "QUOTIENT_IDENTITY: true";
C:=HyperellipticCurve(f); assert Genus(C) eq 2; J:=Jacobian(C);
lo,hi:=RankBounds(J); print "RANK_BOUNDS:",lo,hi; assert lo eq 0 and hi eq 0;
pts:=Chabauty0(J); print "CHABAUTY0_COUNT:",#pts;
nondeg_parent:=0; full_parent:=0; receiver_deg:=0;
for P in pts do
  X:=P[1]; Z:=P[3]; Uh:=X^2-Z^2; Vh:=2*X*Z; Ah:=20*Uh+99*Vh; Bh:=99*Uh+20*Vh;
  zU:=Uh eq 0; zV:=Vh eq 0; zA:=Ah eq 0; zB:=Bh eq 0; deg:=zU or zV or zA or zB;
  sU:=IsSquare(Uh/(-1)); sV:=IsSquare(Vh/(-55)); sA:=IsSquare(Ah/(-5)); sB:=IsSquare(Bh/(-11)); parent:=sU and sV and sA and sB;
  if deg then receiver_deg +:= 1; end if; if parent then full_parent +:= 1; end if; if parent and not deg then nondeg_parent +:= 1; end if;
  print "POINT:",P," ZEROS_UVAB:",zU,zV,zA,zB," SQ_UVAB:",sU,sV,sA,sB," PARENT:",parent;
end for;
print "RECEIVER_DEGENERATE_COUNT:",receiver_deg;
print "FULL_PARENT_LIFT_POINT_COUNT:",full_parent;
print "NONDEGENERATE_FULL_PARENT_LIFT_COUNT:",nondeg_parent;
assert nondeg_parent eq 0;
print "PROOF_STATUS: PASS_EXACT_6B_UVB_RANKZERO_PARENT_CLOSURE_PREAUDIT";
'''
http,out=submit(code); RAW.write_text(out)
bad=any(x in out for x in ("Runtime error","Assertion failed","User error","Internal error"))
if http!=200 or bad or "PROOF_STATUS: PASS_EXACT_6B_UVB_RANKZERO_PARENT_CLOSURE_PREAUDIT" not in out:
    payload={"schema":"STAGE34_02B_D2_STAGEA2_6B_UVB_RANKZERO_PROOF_CERTIFICATE_V1","status":"FAIL_REPLAY_NO_CREDIT","http":http,"raw_stdout_sha256":"sha256:"+hashlib.sha256(out.encode()).hexdigest(),"raw_tail":out[-5000:],"firewalls":{"branch_authoritatively_closed":False,"sign_partner_closed":False,"R29_EXT_CHANG_C_closed":False}}
    OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n"); raise SystemExit("6b UVB proof replay failed")
point_lines=[z for z in out.splitlines() if z.startswith("POINT:")]
payload={
  "schema":"STAGE34_02B_D2_STAGEA2_6B_UVB_RANKZERO_PROOF_CERTIFICATE_V1",
  "status":val("PROOF_STATUS:",out),
  "branch_id":"6b3bcb70c4fda8e6f1e0",
  "q":"20/99",
  "delta":[-1,-55,-5,-11],
  "triple":"U*V*B",
  "source_lock":LOCK.name,
  "source_lock_sha256":"sha256:"+hashlib.sha256(LOCK.read_bytes()).hexdigest(),
  "quotient_identity_verified":val("QUOTIENT_IDENTITY:",out)=="true",
  "rank_bounds":[int(x) for x in val("RANK_BOUNDS:",out).split()[:2]],
  "complete_qpoint_count":int(val("CHABAUTY0_COUNT:",out)),
  "receiver_degenerate_count":int(val("RECEIVER_DEGENERATE_COUNT:",out)),
  "full_parent_lift_point_count":int(val("FULL_PARENT_LIFT_POINT_COUNT:",out)),
  "nondegenerate_full_parent_lift_count":int(val("NONDEGENERATE_FULL_PARENT_LIFT_COUNT:",out)),
  "point_lines":point_lines,
  "raw_stdout_sha256":"sha256:"+hashlib.sha256(out.encode()).hexdigest(),
  "proof":"The literal U*V*B quotient is reconstructed directly from the four parent square equations. Exact RankBounds(J)=[0,0] makes Chabauty0 a complete enumeration of the quotient rational points. Every returned quotient point is checked against all four square conditions U/-1, V/-55, A/-5, B/-11 and receiver degeneracy. No point gives a nondegenerate full parent lift, so every parent branch point is excluded from the audited nonzero-free-part receiver population.",
  "credit":"Exact pre-audit closure evidence for branch 6b3bcb70c4fda8e6f1e0 only. Hostile audit is still required before authoritative branch closure; transfer to bb08690eaf9880e595ea separately requires audited sign-involution adapter.",
  "firewalls":{"hostile_audit_passed":False,"branch_authoritatively_closed":False,"sign_partner_closed":False,"remaining_30_closed":False,"R29_EXT_CHANG_C_closed":False,"perfect_cuboid_nonexistence_claim":False}
}
assert payload["quotient_identity_verified"] and payload["rank_bounds"]==[0,0] and payload["nondegenerate_full_parent_lift_count"]==0
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":payload["status"],"branch_id":payload["branch_id"],"complete_qpoints":payload["complete_qpoint_count"],"nondegenerate_full_parent_lift_count":0},sort_keys=True))
