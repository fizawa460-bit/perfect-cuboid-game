#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,pathlib,urllib.parse,urllib.request,xml.etree.ElementTree as ET

ROOT=pathlib.Path(__file__).resolve().parent
SRC=ROOT/"d2-stageA2-genus2-rankle1-rationalpoints-lock.json"
LOCK=ROOT/"d2-stageA2-genus2-rankle1-three-chabauty-lock.json"
OUT=ROOT/"d2-stageA2-genus2-rankle1-three-chabauty-probe.json"
RAW=ROOT/"d2-stageA2-genus2-rankle1-three-chabauty-stdout.txt"
URL="https://magma.maths.usyd.edu.au/xml/calculator.xml"
REFERER="https://magma.maths.usyd.edu.au/calc/"
TIMEOUT=600

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
        "User-Agent":"perfect-cuboid-stage34-genus2-three-chabauty/1.0"
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

def code_for(c,bound):
    a,b=map(int,c["q"].split('/')); d=list(map(int,c["delta"])); f=poly_expr(c["coefficients_desc_t_degree6"])
    return f'''SetColumns(0);\nSetQuitOnError(true);\nQ:=Rationals(); Qx<x>:=PolynomialRing(Q);\nf:={f}; C:=HyperellipticCurve(f); J:=Jacobian(C);\nprint \"BEGIN branch={c['branch_id']} q={c['q']} model={c['model_id']}\";\nhi:=RankBound(J); print \"RANK_UPPER:\",hi; assert hi le 1;\nSJ:=Points(J : Bound:={int(bound)}); inf:=[P : P in SJ | Order(P) eq 0];\nprint \"JPOINT_SEARCH_BOUND:\",{int(bound)}; print \"JPOINT_COUNT:\",#SJ; print \"NONTORSION_COUNT:\",#inf;\nif #inf gt 0 then\n  bas:=ReducedBasis(inf); P:=bas[1]; assert Order(P) eq 0;\n  print \"CHOSEN_JPOINT:\",P; print \"CHOSEN_HEIGHT:\",Height(P);\n  pts:=Chabauty(P : ptC:=C![0,0,1]);\n  print \"CHABAUTY_EXECUTED: true\"; print \"POINT_COUNT:\",#pts;\n  receiver_deg_count:=0; full_parent_count:=0; nondeg_full_parent_count:=0;\n  for CP in pts do\n    X:=CP[1]; Z:=CP[3]; U:=X^2-Z^2; V:=2*X*Z; A:={a}*U+{b}*V; B:={b}*U+{a}*V;\n    zU:=U eq 0; zV:=V eq 0; zA:=A eq 0; zB:=B eq 0; deg:=zU or zV or zA or zB;\n    sU:=IsSquare(U/({d[0]})); sV:=IsSquare(V/({d[1]})); sA:=IsSquare(A/({d[2]})); sB:=IsSquare(B/({d[3]})); parent:=sU and sV and sA and sB;\n    if deg then receiver_deg_count +:= 1; end if; if parent then full_parent_count +:= 1; end if; if parent and not deg then nondeg_full_parent_count +:= 1; end if;\n    print \"POINT:\",CP,\" DEG:\",deg,\" PARENT:\",parent,\" SQ_UVAB:\",sU,sV,sA,sB,\" ZEROS_UVAB:\",zU,zV,zA,zB;\n  end for;\n  print \"RECEIVER_DEGENERATE_COUNT:\",receiver_deg_count; print \"FULL_PARENT_LIFT_COUNT:\",full_parent_count; print \"NONDEGENERATE_FULL_PARENT_LIFT_COUNT:\",nondeg_full_parent_count;\n  print \"CLOSURE_CANDIDATE:\",nondeg_full_parent_count eq 0;\nelse\n  print \"CHABAUTY_EXECUTED: false\"; print \"CLOSURE_CANDIDATE: false\";\nend if;\nprint \"END branch={c['branch_id']}\";\n'''

src=json.loads(SRC.read_text()); lock=json.loads(LOCK.read_text())
byid={x["branch_id"]:x for x in src["targets"]}
records=[]; rawparts=[]
for sel in lock["targets"]:
    c=byid[sel["branch_id"]]
    assert c["q"]==sel["q"] and int(c["model_id"])==int(sel["model_id"]) and int(c["rank_bounds"][1])==1
    out=""; err=None; status="UNRESOLVED"
    try:
        http,out=submit(code_for(c,sel["jacobian_search_bound"]))
        bad=any(x in out for x in ("Runtime error","Assertion failed","User error","Internal error"))
        if http==200 and f"END branch={c['branch_id']}" in out and not bad: status="PASS_RETURN"
        else: err=f"http={http} malformed_or_magma_error"
    except Exception as ex:
        err=f"{type(ex).__name__}: {ex}"
    rec={"branch_id":c["branch_id"],"q":c["q"],"model_id":c["model_id"],"status":status,"error":err,"stdout_sha256":hashlib.sha256(out.encode()).hexdigest()}
    if status=="PASS_RETURN":
        rec.update({
            "rank_upper":int(val("RANK_UPPER:",out)),
            "jacobian_search_bound":int(val("JPOINT_SEARCH_BOUND:",out)),
            "jacobian_point_count":int(val("JPOINT_COUNT:",out)),
            "nontorsion_count":int(val("NONTORSION_COUNT:",out)),
            "chabauty_executed":val("CHABAUTY_EXECUTED:",out)=="true",
            "closure_candidate":val("CLOSURE_CANDIDATE:",out)=="true",
            "chosen_jpoint":val("CHOSEN_JPOINT:",out,False),
            "chosen_height":val("CHOSEN_HEIGHT:",out,False),
            "point_lines":[z for z in out.splitlines() if z.startswith("POINT:")]
        })
        if rec["chabauty_executed"]:
            rec.update({
                "point_count":int(val("POINT_COUNT:",out)),
                "receiver_degenerate_count":int(val("RECEIVER_DEGENERATE_COUNT:",out)),
                "full_parent_lift_count":int(val("FULL_PARENT_LIFT_COUNT:",out)),
                "nondegenerate_full_parent_lift_count":int(val("NONDEGENERATE_FULL_PARENT_LIFT_COUNT:",out))
            })
    else:
        rec["raw_tail"]=out[-1600:]
    records.append(rec); rawparts.append(f"===== branch={c['branch_id']} =====\n{out}\nERROR={err or ''}\n")
    print(json.dumps({"branch":c["branch_id"],"status":status,"nontorsion":rec.get("nontorsion_count"),"chabauty":rec.get("chabauty_executed"),"candidate":rec.get("closure_candidate")},sort_keys=True))
raw="\n".join(rawparts); RAW.write_text(raw)
cands=[r for r in records if r.get("closure_candidate")]
payload={
    "schema":"STAGE34_02B_D2_STAGEA2_GENUS2_RANKLE1_THREE_CHABAUTY_PROBE_V1",
    "status":"DIAGNOSTIC_NO_CREDIT",
    "input_targets":3,
    "resolved":sum(r["status"]=="PASS_RETURN" for r in records),
    "nontorsion_found":sum(int(r.get("nontorsion_count",0))>0 for r in records),
    "chabauty_executed":sum(bool(r.get("chabauty_executed")) for r in records),
    "closure_candidate_count":len(cands),
    "closure_candidate_branch_ids":[r["branch_id"] for r in cands],
    "records":records,
    "raw_stdout_sha256":hashlib.sha256(raw.encode()).hexdigest(),
    "credit":"Diagnostic proof-capable Chabauty adapter only. No parent branch closure is granted here.",
    "firewalls":{"finite_height_search_exhausts_JQ":False,"no_nontorsion_below_bound_implies_rank_zero":False,"chabauty_candidate_is_parent_closure":False,"remaining_30_closed":False,"R29_EXT_CHANG_C_closed":False}
}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print("GENUS2_RANKLE1_THREE_CHABAUTY="+json.dumps({k:payload[k] for k in ["status","resolved","nontorsion_found","chabauty_executed","closure_candidate_count","closure_candidate_branch_ids"]},sort_keys=True))
