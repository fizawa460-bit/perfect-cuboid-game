#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,pathlib,urllib.parse,urllib.request,xml.etree.ElementTree as ET

ROOT=pathlib.Path(__file__).resolve().parent
LOCK=ROOT/"d2-stageA2-genus2-rankle1-gaussian-elliptic-quotient-lock.json"
OUT=ROOT/"d2-stageA2-genus2-rankle1-gaussian-elliptic-chabauty-probe.json"
RAW=ROOT/"d2-stageA2-genus2-rankle1-gaussian-elliptic-chabauty-stdout.txt"
URL="https://magma.maths.usyd.edu.au/xml/calculator.xml"
REFERER="https://magma.maths.usyd.edu.au/calc/"
TIMEOUT=660

def submit(code):
    data=urllib.parse.urlencode({"input":code}).encode()
    req=urllib.request.Request(URL,data=data,headers={
        "Content-Type":"application/x-www-form-urlencoded",
        "Accept":"text/html, application/xml, application/xhtml+xml",
        "Referer":REFERER,
        "User-Agent":"perfect-cuboid-stage34-gaussian-elliptic-chabauty/1.0"
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

def code_for(t):
    a,b=map(int,t["q"].split('/')); d=list(map(int,t["delta"])); n=int(t["n"]); c=int(t["c"]); A=int(t["A"])
    a2=t["elliptic_a2"].replace("i","ii"); a4=t["elliptic_a4"].replace("i","ii")
    selected=t["selected_triple"]
    return f'''SetColumns(0);\nSetQuitOnError(true);\nQ:=Rationals(); Qz<z>:=PolynomialRing(Q); K<ii>:=NumberField(z^2+1);\nE<EX,EY,EZ>:=EllipticCurve([K|0,{a2},0,{a4},0]); assert Discriminant(E) ne 0;\nprint \"BEGIN branch={t['branch_id']} q={t['q']} model={t['model_id']}\";\nprint \"ELLIPTIC_DISCRIMINANT_NONZERO: true\";\nsuccess,G,m:=PseudoMordellWeilGroup(E); print \"PMW_SUCCESS:\",success; print \"PMW_INVARIANTS:\",Invariants(G);\nif success then\n  P1:=ProjectiveSpace(Q,1); pi:=map< E -> P1 | [EX,EZ] >;\n  V,R:=Chabauty(m,pi : IndexBound:=2); print \"ELLCHAB_EXECUTED: true\"; print \"ELLCHAB_COUNT:\",#V; print \"ELLCHAB_R:\",R;\n  assert IsOdd(R) eq false or R eq 1;\n  pie:=Extend(pi); parent_candidates:=0; nondeg_parent_candidates:=0; quotient_infinity:=0;\n  for g in V do\n    P:=m(g); im:=pie(P); print \"ELLCHAB_GROUP_ELEMENT:\",g,\" IMAGE:\",im;\n    if im[2] eq 0 then\n      quotient_infinity +:= 1; print \"QX_INFINITY: true\";\n    else\n      qx:=Q!(im[1]/im[2]); uu:=qx/({A}); discr:=uu^2+4; issq,sd:=IsSquare(discr);\n      print \"QX:\",qx,\" U:\",uu,\" XDISCR_SQUARE:\",issq;\n      if issq then\n        for xx in [(uu+sd)/2,(uu-sd)/2] do\n          ff:=({c})*xx*(xx^2-1)*(xx+({n}))*(({n})*xx-1); cpt,yy:=IsSquare(ff);\n          U:=xx^2-1; VV:=2*xx; AA:={a}*U+{b}*VV; BB:={b}*U+{a}*VV; deg:=U eq 0 or VV eq 0 or AA eq 0 or BB eq 0;\n          sU:=IsSquare(U/({d[0]})); sV:=IsSquare(VV/({d[1]})); sA:=IsSquare(AA/({d[2]})); sB:=IsSquare(BB/({d[3]})); parent:=cpt and sU and sV and sA and sB;\n          if cpt then parent_candidates +:= 1; end if; if parent and not deg then nondeg_parent_candidates +:= 1; end if;\n          print \"PULLBACK_X:\",xx,\" C_POINT:\",cpt,\" DEG:\",deg,\" PARENT:\",parent,\" SQ_UVAB:\",sU,sV,sA,sB;\n        end for;\n      end if;\n    end if;\n  end for;\n  print \"QUOTIENT_INFINITY_COUNT:\",quotient_infinity; print \"RATIONAL_C_PULLBACK_X_COUNT_WITH_MULTIPLICITY:\",parent_candidates; print \"NONDEGENERATE_FULL_PARENT_LIFT_COUNT:\",nondeg_parent_candidates;\n  print \"CLOSURE_CANDIDATE:\",nondeg_parent_candidates eq 0;\nelse\n  print \"ELLCHAB_EXECUTED: false\"; print \"CLOSURE_CANDIDATE: false\";\nend if;\nprint \"END branch={t['branch_id']}\";\n'''

d=json.loads(LOCK.read_text()); records=[]; rawparts=[]
for t in d["targets"]:
    out=""; err=None; status="UNRESOLVED_RESOURCE_OR_EXTERNAL_WALL"
    try:
        http,out=submit(code_for(t)); bad=any(x in out for x in ("Runtime error","Assertion failed","User error","Internal error"))
        if http==200 and f"END branch={t['branch_id']}" in out and not bad: status="PASS_RETURN"
        else: err=f"http={http} malformed_or_magma_error"
    except Exception as ex: err=f"{type(ex).__name__}: {ex}"
    rec={"branch_id":t["branch_id"],"q":t["q"],"model_id":t["model_id"],"sign_partner":t["sign_partner"],"status":status,"error":err,"stdout_sha256":hashlib.sha256(out.encode()).hexdigest()}
    for pfx,key,typ in [
      ("ELLIPTIC_DISCRIMINANT_NONZERO:","elliptic_discriminant_nonzero",lambda s:s=="true"),
      ("PMW_SUCCESS:","pmw_success",lambda s:s=="true"),
      ("ELLCHAB_EXECUTED:","ellchab_executed",lambda s:s=="true"),
      ("ELLCHAB_COUNT:","ellchab_count",int),("ELLCHAB_R:","ellchab_R",int),
      ("QUOTIENT_INFINITY_COUNT:","quotient_infinity_count",int),
      ("RATIONAL_C_PULLBACK_X_COUNT_WITH_MULTIPLICITY:","rational_C_pullback_x_count_with_multiplicity",int),
      ("NONDEGENERATE_FULL_PARENT_LIFT_COUNT:","nondegenerate_full_parent_lift_count",int),
      ("CLOSURE_CANDIDATE:","closure_candidate",lambda s:s=="true")]:
        z=val(pfx,out,False)
        if z is not None:
            try: rec[key]=typ(z)
            except Exception: rec[key+"_raw"]=z
    rec["pmw_invariants"]=val("PMW_INVARIANTS:",out,False)
    rec["image_lines"]=[x for x in out.splitlines() if " IMAGE:" in x or x.startswith("QX:") or x.startswith("PULLBACK_X:")]
    if status!="PASS_RETURN": rec["raw_tail"]=out[-2600:]
    records.append(rec); rawparts.append(f"===== branch={t['branch_id']} =====\n{out}\nERROR={err or ''}\n")
    print(json.dumps({"branch":t["branch_id"],"status":status,"pmw":rec.get("pmw_success"),"ellchab":rec.get("ellchab_executed"),"candidate":rec.get("closure_candidate")},sort_keys=True))
raw="\n".join(rawparts); RAW.write_text(raw)
cands=[r for r in records if r.get("closure_candidate") and r.get("pmw_success") and r.get("ellchab_executed")]
payload={
  "schema":"STAGE34_02B_D2_STAGEA2_GENUS2_RANKLE1_GAUSSIAN_ELLIPTIC_CHABAUTY_PROBE_V1",
  "status":"DIAGNOSTIC_NO_CREDIT",
  "input_representatives":2,
  "resolved_returns":sum(r["status"]=="PASS_RETURN" for r in records),
  "pmw_successes":sum(bool(r.get("pmw_success")) for r in records),
  "ellchab_executed":sum(bool(r.get("ellchab_executed")) for r in records),
  "closure_candidate_count":len(cands),
  "closure_candidate_branch_ids":[r["branch_id"] for r in cands],
  "records":records,
  "raw_stdout_sha256":hashlib.sha256(raw.encode()).hexdigest(),
  "credit":"Diagnostic only; candidate completeness must be separately replayed from the exact quotient identity, PMW odd-index semantics, Chabauty IndexBound=2 result, and parent pullback before hostile audit.",
  "firewalls":{"pmw_failure_is_math_failure":False,"ellchab_without_index_semantics_is_complete":False,"diagnostic_candidate_is_parent_closure":False,"sign_partner_transfer_authoritative_before_audit":False,"remaining_30_closed":False,"R29_EXT_CHANG_C_closed":False}
}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print("GAUSSIAN_ELLIPTIC_CHABAUTY="+json.dumps({k:payload[k] for k in ["status","resolved_returns","pmw_successes","ellchab_executed","closure_candidate_count","closure_candidate_branch_ids"]},sort_keys=True))
