#!/usr/bin/env python3
from __future__ import annotations
import collections,hashlib,json,pathlib,urllib.parse,urllib.request,xml.etree.ElementTree as ET
from fractions import Fraction

ROOT=pathlib.Path(__file__).resolve().parent
LOCK=ROOT/"d2-stageA2-six-rankbound-adapter-proof-lock.json"
OUT=ROOT/"d2-stageA2-six-rankbound-adapter-proof-certificate.json"
RAW=ROOT/"d2-stageA2-six-rankbound-adapter-proof-stdout.txt"
URL="https://magma.maths.usyd.edu.au/xml/calculator.xml"; REFERER="https://magma.maths.usyd.edu.au/calc/"; TIMEOUT=600
NAMES=["U","V","A","B"]

def poly_expr(c):
    deg=len(c)-1; parts=[]
    for i,a in enumerate(c):
        a=int(a); e=deg-i
        if a: parts.append(f"({a})*x^{e}" if e else f"({a})")
    return "+".join(parts) or "0"

def submit(code):
    data=urllib.parse.urlencode({"input":code}).encode()
    req=urllib.request.Request(URL,data=data,headers={"Content-Type":"application/x-www-form-urlencoded","Accept":"text/html, application/xml, application/xhtml+xml","Referer":REFERER,"User-Agent":"perfect-cuboid-stage34-six-rank-adapter/1.0"},method="POST")
    with urllib.request.urlopen(req,timeout=TIMEOUT) as resp:
        raw=resp.read().decode("utf-8",errors="replace"); http=resp.status
    root=ET.fromstring(raw); lines=[]
    for result in root.findall(".//results"):
        for line in result.findall(".//line"): lines.append("".join(line.itertext()))
    return http,"\n".join(lines)+("\n" if lines else "")

def val(prefix,out):
    for line in out.splitlines():
        if line.startswith(prefix): return line[len(prefix):].strip()
    raise RuntimeError(prefix+" missing")

def code_for(t):
    a,b=map(int,t["q"].split('/')); d=list(map(int,t["delta"])); f=poly_expr(t["coefficients_desc_t_degree6"])
    scale=Fraction(t["literal_to_integral_y_scale"]); tri=t["triple"].split('*')
    lit='*'.join(f"({name}/({d[NAMES.index(name)]}))" for name in tri)
    return f'''SetColumns(0); SetQuitOnError(true);\nQ:=Rationals(); Qx<x>:=PolynomialRing(Q);\nU:=x^2-1; V:=2*x; A:={a}*U+{b}*V; B:={b}*U+{a}*V;\nflit:={lit}; fint:={f}; assert fint eq ({scale.numerator}/{scale.denominator})^2*flit; print "QUOTIENT_IDENTITY: true";\nC:=HyperellipticCurve(fint); assert Genus(C) eq 2;\npts,complete:=RationalPointsGenus2(C); print "COMPLETE:",complete; print "POINT_COUNT:",#pts;\nreceiver_deg:=0; full_parent:=0; nondeg_parent:=0;\nfor P in pts do\n X:=P[1]; Z:=P[3]; Uh:=X^2-Z^2; Vh:=2*X*Z; Ah:={a}*Uh+{b}*Vh; Bh:={b}*Uh+{a}*Vh;\n zU:=Uh eq 0; zV:=Vh eq 0; zA:=Ah eq 0; zB:=Bh eq 0; deg:=zU or zV or zA or zB;\n sU:=IsSquare(Uh/({d[0]})); sV:=IsSquare(Vh/({d[1]})); sA:=IsSquare(Ah/({d[2]})); sB:=IsSquare(Bh/({d[3]})); parent:=sU and sV and sA and sB;\n if deg then receiver_deg +:= 1; end if; if parent then full_parent +:= 1; end if; if parent and not deg then nondeg_parent +:= 1; end if;\n print "POINT:",P," ZEROS_UVAB:",zU,zV,zA,zB," SQ_UVAB:",sU,sV,sA,sB," PARENT:",parent;\nend for;\nprint "RECEIVER_DEGENERATE_COUNT:",receiver_deg; print "FULL_PARENT_LIFT_POINT_COUNT:",full_parent; print "NONDEGENERATE_FULL_PARENT_LIFT_COUNT:",nondeg_parent; print "PROOF_REPLAY_COMPLETE: true";\n'''

lock=json.loads(LOCK.read_text()); assert lock["schema"]=="STAGE34_02B_D2_STAGEA2_SIX_DIAGNOSTIC_RANKBOUND_ADAPTER_PROOF_LOCK_V1" and len(lock["targets"])==6
records=[]; rawparts=[]
for i,t in enumerate(lock["targets"],1):
    out=""; err=None
    try:
        http,out=submit(code_for(t)); bad=any(x in out for x in ("Runtime error","Assertion failed","User error","Internal error")); ok=http==200 and not bad and val("PROOF_REPLAY_COMPLETE:",out)=="true"
    except Exception as ex: ok=False; err=f"{type(ex).__name__}: {ex}"
    rawparts.append(f"===== index={i} branch={t['branch_id']} model={t['model_id']} =====\n{out}\nERROR={err or ''}")
    rec={**t,"execution_complete":ok,"error":err,"locked_rank_condition_verified":int(t["locked_rank_bounds"][1])<=1}
    if ok:
        complete=val("COMPLETE:",out)=="true"; cnt=int(val("POINT_COUNT:",out)); deg=int(val("RECEIVER_DEGENERATE_COUNT:",out)); par=int(val("FULL_PARENT_LIFT_POINT_COUNT:",out)); nondeg=int(val("NONDEGENERATE_FULL_PARENT_LIFT_COUNT:",out))
        rec.update({"quotient_identity_verified":val("QUOTIENT_IDENTITY:",out)=="true","complete":complete,"complete_qpoint_count":cnt,"receiver_degenerate_count":deg,"full_parent_lift_point_count":par,"nondegenerate_full_parent_lift_count":nondeg,"point_lines":[x for x in out.splitlines() if x.startswith("POINT:")],"stdout_sha256":"sha256:"+hashlib.sha256(out.encode()).hexdigest()})
        rec["direct_closure_candidate"]=bool(rec["locked_rank_condition_verified"] and rec["quotient_identity_verified"] and complete and nondeg==0)
    else: rec["direct_closure_candidate"]=False
    records.append(rec); print(json.dumps({"branch":t["branch_id"],"model":t["model_id"],"complete":rec.get("complete"),"qpoints":rec.get("complete_qpoint_count"),"nondeg_parent":rec.get("nondegenerate_full_parent_lift_count"),"candidate":rec["direct_closure_candidate"]},sort_keys=True))
raw="\n".join(rawparts); RAW.write_text(raw)
closed=[r for r in records if r["direct_closure_candidate"]]; cby=collections.Counter(r["q"] for r in closed)
base={"20/99":4,"24/7":0,"48/55":0,"60/11":6,"80/39":4,"84/13":8}; rem={k:v-2*cby.get(k,0) for k,v in base.items()}
payload={"schema":"STAGE34_02B_D2_STAGEA2_SIX_DIAGNOSTIC_RANKBOUND_ADAPTER_PROOF_CERTIFICATE_V1","status":"READY_FOR_HOSTILE_AUDIT_SIX_ADAPTER_CANDIDATES" if len(closed)==6 else "EXACT_ADAPTER_PROOF_PARTIAL_CANDIDATES_REQUIRE_HOSTILE_AUDIT","source_lock":LOCK.name,"source_lock_sha256":"sha256:"+hashlib.sha256(LOCK.read_bytes()).hexdigest(),"rank_evidence":lock["rank_evidence"],"records":records,"direct_closure_candidate_count":len(closed),"direct_closure_candidate_branch_ids":[r["branch_id"] for r in closed],"sign_transfer_candidate_branch_ids":[r["partner"] for r in closed],"candidate_closed_branches_from_this_adapter_if_audited":2*len(closed),"candidate_remaining_from_22_if_only_this_adapter_audited":22-2*len(closed),"candidate_remaining_by_q_from_22_if_only_this_adapter_audited":rem,"raw_stdout_sha256":"sha256:"+hashlib.sha256(raw.encode()).hexdigest(),"credit":"Pre-audit adapter proof only. The source-locked prior RankBounds supplies only the rigorous rank<=1 premise; this run supplies quotient completeness and exact parent pullback. No authoritative promotion without hostile audit.","firewalls":{"hostile_audit_passed":False,"candidate_is_authoritative":False,"authoritative_remaining_d1":22,"D2_all_factor_branches_closed":False,"all_multiples_closed":False,"R29_EXT_CHANG_C_closed":False,"perfect_cuboid_nonexistence_claim":False}}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n"); print("SIX_ADAPTER_PROOF="+json.dumps({"status":payload["status"],"direct_candidates":len(closed)},sort_keys=True))
