#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,pathlib,urllib.parse,urllib.request,xml.etree.ElementTree as ET

ROOT=pathlib.Path(__file__).resolve().parent
SRC=ROOT/"d2-stageA2-genus2-rankle1-rationalpoints-lock.json"
LOCK=ROOT/"d2-stageA2-genus2-rankle1-two-rep-mw-chabauty-lock.json"
OUT=ROOT/"d2-stageA2-genus2-rankle1-two-rep-mw-chabauty-probe.json"
RAW=ROOT/"d2-stageA2-genus2-rankle1-two-rep-mw-chabauty-stdout.txt"
URL="https://magma.maths.usyd.edu.au/xml/calculator.xml"
REFERER="https://magma.maths.usyd.edu.au/calc/"
TIMEOUT=660

def poly_expr(c):
    deg=len(c)-1; parts=[]
    for i,a in enumerate(c):
        a=int(a); e=deg-i
        if not a: continue
        parts.append(f"({a})*x^{e}" if e else f"({a})")
    return "+".join(parts) or "0"

def submit(code):
    data=urllib.parse.urlencode({"input":code}).encode()
    req=urllib.request.Request(URL,data=data,headers={
        "Content-Type":"application/x-www-form-urlencoded",
        "Accept":"text/html, application/xml, application/xhtml+xml",
        "Referer":REFERER,
        "User-Agent":"perfect-cuboid-stage34-genus2-two-rep-mw-chabauty/1.0"
    },method="POST")
    with urllib.request.urlopen(req,timeout=TIMEOUT) as resp:
        raw=resp.read().decode("utf-8",errors="replace"); status=resp.status
    root=ET.fromstring(raw); lines=[]
    for result in root.findall(".//results"):
        for line in result.findall(".//line"):
            lines.append("".join(line.itertext()))
    return status,"\n".join(lines)+("\n" if lines else "")

def val(prefix,out,required=True):
    for line in out.splitlines():
        if line.startswith(prefix): return line[len(prefix):].strip()
    if required: raise RuntimeError(prefix+" missing")
    return None

def code_for(c,params):
    a,b=map(int,c["q"].split('/')); d=list(map(int,c["delta"])); f=poly_expr(c["coefficients_desc_t_degree6"])
    return f'''SetColumns(0);\nSetQuitOnError(true);\nSetVerbose(\"MordellWeilGroup\",0);\nQ:=Rationals(); Qx<x>:=PolynomialRing(Q);\nf:={f}; C:=HyperellipticCurve(f); J:=Jacobian(C);\nprint \"BEGIN branch={c['branch_id']} q={c['q']} model={c['model_id']}\";\nhi:=RankBound(J); print \"RANK_UPPER_RECHECK:\",hi; assert hi le 1;\nG,mp,finite_index,proved,upper:=MordellWeilGroupGenus2(J : Rankbound:=1, RankOnly:=true, MaxBound:={int(params['MaxBound'])}, BoundC:={int(params['BoundC'])});\ninv:=Invariants(G); print \"MW_INVARIANTS:\",inv; print \"MW_FINITE_INDEX:\",finite_index; print \"MW_PROVED:\",proved; print \"MW_RETURNED_UPPER:\",upper;\nfree_idx:=[i : i in [1..#inv] | inv[i] eq 0]; print \"MW_FREE_GENERATOR_COUNT:\",#free_idx;\nif #free_idx gt 0 then\n  P:=mp(G.free_idx[1]); print \"MW_FREE_POINT:\",P; print \"MW_FREE_POINT_ORDER:\",Order(P); assert Order(P) eq 0; assert hi eq 1;\n  pts:=Chabauty(P : ptC:=C![0,0,1]);\n  print \"CHABAUTY_EXECUTED: true\"; print \"POINT_COUNT:\",#pts;\n  receiver_deg_count:=0; full_parent_count:=0; nondeg_full_parent_count:=0;\n  for CP in pts do\n    X:=CP[1]; Z:=CP[3]; U:=X^2-Z^2; V:=2*X*Z; A:={a}*U+{b}*V; B:={b}*U+{a}*V;\n    zU:=U eq 0; zV:=V eq 0; zA:=A eq 0; zB:=B eq 0; deg:=zU or zV or zA or zB;\n    sU:=IsSquare(U/({d[0]})); sV:=IsSquare(V/({d[1]})); sA:=IsSquare(A/({d[2]})); sB:=IsSquare(B/({d[3]})); parent:=sU and sV and sA and sB;\n    if deg then receiver_deg_count +:= 1; end if; if parent then full_parent_count +:= 1; end if; if parent and not deg then nondeg_full_parent_count +:= 1; end if;\n    print \"POINT:\",CP,\" DEG:\",deg,\" PARENT:\",parent,\" SQ_UVAB:\",sU,sV,sA,sB,\" ZEROS_UVAB:\",zU,zV,zA,zB;\n  end for;\n  print \"RECEIVER_DEGENERATE_COUNT:\",receiver_deg_count; print \"FULL_PARENT_LIFT_COUNT:\",full_parent_count; print \"NONDEGENERATE_FULL_PARENT_LIFT_COUNT:\",nondeg_full_parent_count;\n  print \"CLOSURE_CANDIDATE:\",nondeg_full_parent_count eq 0;\nelse\n  print \"CHABAUTY_EXECUTED: false\"; print \"CLOSURE_CANDIDATE: false\";\nend if;\nprint \"END branch={c['branch_id']}\";\n'''

src=json.loads(SRC.read_text()); lock=json.loads(LOCK.read_text())
byid={x["branch_id"]:x for x in src["targets"]}; params=lock["adapter"]["parameters"]
records=[]; rawparts=[]
for sel in lock["targets"]:
    c=byid[sel["branch_id"]]
    assert c["q"]==sel["q"] and int(c["model_id"])==int(sel["model_id"]) and int(c["rank_bounds"][1])==1
    out=""; err=None; status="UNRESOLVED_RESOURCE_OR_EXTERNAL_WALL"
    try:
        http,out=submit(code_for(c,params))
        bad=any(x in out for x in ("Runtime error","Assertion failed","User error","Internal error"))
        if http==200 and f"END branch={c['branch_id']}" in out and not bad: status="PASS_RETURN"
        else: err=f"http={http} malformed_or_magma_error"
    except Exception as ex:
        err=f"{type(ex).__name__}: {ex}"
    rec={"branch_id":c["branch_id"],"q":c["q"],"model_id":c["model_id"],"sign_partner":sel["sign_partner"],"status":status,"error":err,"stdout_sha256":hashlib.sha256(out.encode()).hexdigest()}
    for pfx,key,typ in [
        ("RANK_UPPER_RECHECK:","rank_upper_recheck",int),
        ("MW_FINITE_INDEX:","mw_finite_index",lambda s:s=="true"),
        ("MW_PROVED:","mw_proved",lambda s:s=="true"),
        ("MW_RETURNED_UPPER:","mw_returned_upper",int),
        ("MW_FREE_GENERATOR_COUNT:","mw_free_generator_count",int),
        ("CHABAUTY_EXECUTED:","chabauty_executed",lambda s:s=="true"),
        ("CLOSURE_CANDIDATE:","closure_candidate",lambda s:s=="true")]:
        z=val(pfx,out,False)
        if z is not None:
            try: rec[key]=typ(z)
            except Exception: rec[key+"_raw"]=z
    rec["mw_invariants"]=val("MW_INVARIANTS:",out,False)
    rec["mw_free_point"]=val("MW_FREE_POINT:",out,False)
    rec["mw_free_point_order"]=val("MW_FREE_POINT_ORDER:",out,False)
    if rec.get("chabauty_executed"):
        for pfx,key in [("POINT_COUNT:","point_count"),("RECEIVER_DEGENERATE_COUNT:","receiver_degenerate_count"),("FULL_PARENT_LIFT_COUNT:","full_parent_lift_count"),("NONDEGENERATE_FULL_PARENT_LIFT_COUNT:","nondegenerate_full_parent_lift_count")]:
            rec[key]=int(val(pfx,out))
        rec["point_lines"]=[z for z in out.splitlines() if z.startswith("POINT:")]
    if status!="PASS_RETURN": rec["raw_tail"]=out[-2200:]
    records.append(rec); rawparts.append(f"===== branch={c['branch_id']} =====\n{out}\nERROR={err or ''}\n")
    print(json.dumps({"branch":c["branch_id"],"status":status,"free":rec.get("mw_free_generator_count"),"chabauty":rec.get("chabauty_executed"),"candidate":rec.get("closure_candidate")},sort_keys=True))
raw="\n".join(rawparts); RAW.write_text(raw)
cands=[r for r in records if r.get("closure_candidate")]
payload={
    "schema":"STAGE34_02B_D2_STAGEA2_GENUS2_RANKLE1_TWO_REP_MW_CHABAUTY_PROBE_V1",
    "status":"DIAGNOSTIC_NO_CREDIT",
    "input_representatives":2,
    "resolved_returns":sum(r["status"]=="PASS_RETURN" for r in records),
    "free_generator_returns":sum(int(r.get("mw_free_generator_count",0))>0 for r in records),
    "chabauty_executed":sum(bool(r.get("chabauty_executed")) for r in records),
    "closure_candidate_count":len(cands),
    "closure_candidate_branch_ids":[r["branch_id"] for r in cands],
    "records":records,
    "raw_stdout_sha256":hashlib.sha256(raw.encode()).hexdigest(),
    "credit":"Diagnostic only. Bounded MW effort or external failure is not a rank or nonexistence result; successful candidates require separate proof replay and audit.",
    "firewalls":{"bounded_MW_effort_exhausts_JQ":False,"no_generator_returned_implies_rank_zero":False,"sign_partner_transfer_authoritative_before_audit":False,"diagnostic_candidate_is_parent_closure":False,"remaining_30_closed":False,"R29_EXT_CHANG_C_closed":False}
}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print("GENUS2_RANKLE1_TWO_REP_MW_CHABAUTY="+json.dumps({k:payload[k] for k in ["status","resolved_returns","free_generator_returns","chabauty_executed","closure_candidate_count","closure_candidate_branch_ids"]},sort_keys=True))
