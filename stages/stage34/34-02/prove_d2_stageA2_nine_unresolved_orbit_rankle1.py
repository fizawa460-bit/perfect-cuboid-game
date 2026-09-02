#!/usr/bin/env python3
from __future__ import annotations
import collections,hashlib,json,pathlib,urllib.parse,urllib.request,xml.etree.ElementTree as ET
from fractions import Fraction

ROOT=pathlib.Path(__file__).resolve().parent
LOCK=ROOT/"d2-stageA2-nine-unresolved-orbit-rankle1-proof-lock.json"
OUT=ROOT/"d2-stageA2-nine-unresolved-orbit-rankle1-proof-certificate.json"
RAW=ROOT/"d2-stageA2-nine-unresolved-orbit-rankle1-proof-stdout.txt"
URL="https://magma.maths.usyd.edu.au/xml/calculator.xml"; REFERER="https://magma.maths.usyd.edu.au/calc/"; TIMEOUT=600
NAMES=["U","V","A","B"]

def poly_expr(c):
    deg=len(c)-1;parts=[]
    for i,a in enumerate(c):
        a=int(a);e=deg-i
        if a: parts.append(f"({a})*x^{e}" if e else f"({a})")
    return "+".join(parts) or "0"

def submit(code):
    data=urllib.parse.urlencode({"input":code}).encode()
    req=urllib.request.Request(URL,data=data,headers={"Content-Type":"application/x-www-form-urlencoded","Accept":"text/html, application/xml, application/xhtml+xml","Referer":REFERER,"User-Agent":"perfect-cuboid-stage34-nine-alt-rankle1-proof/1.0"},method="POST")
    with urllib.request.urlopen(req,timeout=TIMEOUT) as resp:
        raw=resp.read().decode("utf-8",errors="replace");http=resp.status
    root=ET.fromstring(raw);lines=[]
    for result in root.findall(".//results"):
        for line in result.findall(".//line"):lines.append("".join(line.itertext()))
    return http,"\n".join(lines)+("\n" if lines else "")

def val(prefix,out):
    for line in out.splitlines():
        if line.startswith(prefix): return line[len(prefix):].strip()
    raise RuntimeError(prefix+" missing")

def code_for(t):
    a,b=map(int,t["q"].split('/'));d=list(map(int,t["delta"]));f=poly_expr(t["coefficients_desc_t_degree6"])
    scale=Fraction(t["literal_to_integral_y_scale"]);scale_expr=f"({scale.numerator}/{scale.denominator})"
    tri=t["triple"].split('*');assert len(tri)==3 and len(set(tri))==3
    lit='*'.join(f"({name}/({d[NAMES.index(name)]}))" for name in tri)
    if t["point_method"]=="Chabauty0":
        pointcode='''assert lo eq 0 and hi eq 0;\npts:=Chabauty0(J); complete:=true; print "POINT_METHOD: Chabauty0";'''
    else:
        pointcode='''assert hi le 1;\npts,complete:=RationalPointsGenus2(C); print "POINT_METHOD: RationalPointsGenus2";'''
    return f'''SetColumns(0); SetQuitOnError(true);\nQ:=Rationals(); Qx<x>:=PolynomialRing(Q);\nU:=x^2-1; V:=2*x; A:={a}*U+{b}*V; B:={b}*U+{a}*V;\nflit:={lit}; fint:={f};\nassert fint eq ({scale_expr})^2*flit; print "QUOTIENT_IDENTITY: true"; print "INTEGRAL_SCALE: {scale.numerator}/{scale.denominator}";\nC:=HyperellipticCurve(fint); assert Genus(C) eq 2; J:=Jacobian(C);\nlo,hi:=RankBounds(J); print "RANK_BOUNDS:",lo,hi;\n{pointcode}\nprint "COMPLETE:",complete; print "POINT_COUNT:",#pts;\nreceiver_deg:=0; full_parent:=0; nondeg_parent:=0;\nfor P in pts do\n X:=P[1]; Z:=P[3]; Uh:=X^2-Z^2; Vh:=2*X*Z; Ah:={a}*Uh+{b}*Vh; Bh:={b}*Uh+{a}*Vh;\n zU:=Uh eq 0; zV:=Vh eq 0; zA:=Ah eq 0; zB:=Bh eq 0; deg:=zU or zV or zA or zB;\n sU:=IsSquare(Uh/({d[0]})); sV:=IsSquare(Vh/({d[1]})); sA:=IsSquare(Ah/({d[2]})); sB:=IsSquare(Bh/({d[3]})); parent:=sU and sV and sA and sB;\n if deg then receiver_deg +:= 1; end if; if parent then full_parent +:= 1; end if; if parent and not deg then nondeg_parent +:= 1; end if;\n print "POINT:",P," ZEROS_UVAB:",zU,zV,zA,zB," SQ_UVAB:",sU,sV,sA,sB," PARENT:",parent;\nend for;\nprint "RECEIVER_DEGENERATE_COUNT:",receiver_deg; print "FULL_PARENT_LIFT_POINT_COUNT:",full_parent; print "NONDEGENERATE_FULL_PARENT_LIFT_COUNT:",nondeg_parent;\nprint "PROOF_REPLAY_COMPLETE: true";\n'''

lock=json.loads(LOCK.read_text())
assert lock["schema"]=="STAGE34_02B_D2_STAGEA2_NINE_UNRESOLVED_ORBIT_RANKLE1_PROOF_LOCK_V1" and lock["status"]=="SOURCE_LOCKED_COLD_NOT_ARMED"
assert len(lock["targets"])==9 and len({t["branch_id"] for t in lock["targets"]})==9 and len({t["partner"] for t in lock["targets"]})==9
records=[];rawparts=[]
for i,t in enumerate(lock["targets"],1):
    out="";err=None;http=None
    try:
        http,out=submit(code_for(t));bad=any(x in out for x in ("Runtime error","Assertion failed","User error","Internal error"))
        ok=http==200 and not bad and val("PROOF_REPLAY_COMPLETE:",out)=="true"
    except Exception as ex:
        ok=False;err=f"{type(ex).__name__}: {ex}"
    rawparts.append(f"===== index={i} branch={t['branch_id']} model={t['model_id']} =====\n{out}\nERROR={err or ''}")
    rec={"branch_id":t["branch_id"],"partner":t["partner"],"q":t["q"],"delta":t["delta"],"triple":t["triple"],"model_id":t["model_id"],"squareclass":t["squareclass"],"coefficients_desc_t_degree6":t["coefficients_desc_t_degree6"],"point_method":t["point_method"],"diagnostic_rank_bounds":t["diagnostic_rank_bounds"],"execution_complete":ok,"error":err}
    if ok:
        rb=[int(x) for x in val("RANK_BOUNDS:",out).split()[:2]]
        method=val("POINT_METHOD:",out);complete=val("COMPLETE:",out)=="true";cnt=int(val("POINT_COUNT:",out))
        deg=int(val("RECEIVER_DEGENERATE_COUNT:",out));par=int(val("FULL_PARENT_LIFT_POINT_COUNT:",out));nondeg=int(val("NONDEGENERATE_FULL_PARENT_LIFT_COUNT:",out))
        rank_ok=(rb==[0,0]) if t["point_method"]=="Chabauty0" else (rb[1]<=1)
        rec.update({"quotient_identity_verified":val("QUOTIENT_IDENTITY:",out)=="true","integral_scale":val("INTEGRAL_SCALE:",out),"rank_bounds":rb,"rank_condition_verified":rank_ok,"point_method_replayed":method,"complete":complete,"complete_qpoint_count":cnt,"receiver_degenerate_count":deg,"full_parent_lift_point_count":par,"nondegenerate_full_parent_lift_count":nondeg,"point_lines":[x for x in out.splitlines() if x.startswith("POINT:")],"stdout_sha256":"sha256:"+hashlib.sha256(out.encode()).hexdigest()})
        rec["direct_closure_candidate"]=bool(rec["quotient_identity_verified"] and rank_ok and complete and nondeg==0)
    else:
        rec["direct_closure_candidate"]=False
    records.append(rec)
    print(json.dumps({"index":i,"branch":t["branch_id"],"model":t["model_id"],"execution_complete":ok,"rank_bounds":rec.get("rank_bounds"),"complete":rec.get("complete"),"qpoints":rec.get("complete_qpoint_count"),"nondeg_parent":rec.get("nondegenerate_full_parent_lift_count"),"closure_candidate":rec["direct_closure_candidate"]},sort_keys=True))
raw="\n".join(rawparts);RAW.write_text(raw)
closed=[r for r in records if r["direct_closure_candidate"]]
closed_by_q=collections.Counter(r["q"] for r in closed)
baseline=lock["authoritative_baseline"];remain_by_q={k:int(v)-2*int(closed_by_q.get(k,0)) for k,v in baseline["remaining_by_q"].items()}
allclose=len(closed)==9
payload={
 "schema":"STAGE34_02B_D2_STAGEA2_NINE_UNRESOLVED_ORBIT_RANKLE1_PROOF_CERTIFICATE_V1",
 "status":"READY_FOR_HOSTILE_AUDIT_NINE_REPRESENTATIVE_EIGHTEEN_BRANCH_CANDIDATE" if allclose else "EXACT_PROOF_REPLAY_PARTIAL_CANDIDATES_REQUIRE_HOSTILE_AUDIT",
 "source_lock":LOCK.name,"source_lock_sha256":"sha256:"+hashlib.sha256(LOCK.read_bytes()).hexdigest(),
 "authoritative_baseline_remaining_d1":22,"records":records,"direct_closure_candidate_count":len(closed),"direct_closure_candidate_branch_ids":[r["branch_id"] for r in closed],"sign_transfer_candidate_count":len(closed),"sign_transfer_candidate_branch_ids":[r["partner"] for r in closed],
 "candidate_closed_branches_if_hostile_audit_passes":2*len(closed),"candidate_remaining_if_hostile_audit_passes":22-2*len(closed),"candidate_remaining_by_q_if_hostile_audit_passes":remain_by_q,
 "raw_stdout_sha256":"sha256:"+hashlib.sha256(raw.encode()).hexdigest(),
 "credit":"Exact pre-audit proof replay only. Direct representative closure and already-audited sign-partner transfer remain candidate-only until a separate hostile audit independently validates this proof and explicitly authorizes promotion.",
 "firewalls":{"hostile_audit_passed":False,"candidate_is_authoritative":False,"authoritative_remaining_d1":22,"remaining_22_closed":False,"D2_all_factor_branches_closed":False,"direct_cover_rational_points_complete":False,"all_multiples_closed":False,"R29_EXT_CHANG_C_closed":False,"parent_route_closed":False,"perfect_cuboid_nonexistence_claim":False}
}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print("NINE_ALT_PROOF="+json.dumps({"status":payload["status"],"direct_candidates":payload["direct_closure_candidate_count"],"candidate_remaining":payload["candidate_remaining_if_hostile_audit_passes"],"candidate_remaining_by_q":remain_by_q},sort_keys=True))
