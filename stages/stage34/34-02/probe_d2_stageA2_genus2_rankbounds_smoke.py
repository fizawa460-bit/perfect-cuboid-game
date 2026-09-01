#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,pathlib,re,urllib.parse,urllib.request,xml.etree.ElementTree as ET

ROOT=pathlib.Path(__file__).resolve().parent
SRC=ROOT/"d2-stageA2-triple-quotient-model-probe.json"
OUT=ROOT/"d2-stageA2-genus2-rankbounds-smoke.json"
RAW=ROOT/"d2-stageA2-genus2-rankbounds-smoke-stdout.txt"
URL="https://magma.maths.usyd.edu.au/xml/calculator.xml"
REFERER="https://magma.maths.usyd.edu.au/calc/"


def choose(data):
    best={}
    for m in data["models"]:
        c=list(map(int,m["coefficients_desc_t_degree6"]))
        score=(max(abs(x) for x in c),sum(abs(x) for x in c),int(m["model_id"]))
        for a in m["associations"]:
            q=a["q"]
            if q not in best or score<best[q][0]:best[q]=(score,m,a)
    assert len(best)==7
    return [best[q] for q in sorted(best)]


def poly_expr(c):
    deg=len(c)-1; terms=[]
    for i,a in enumerate(c):
        if not a:continue
        e=deg-i
        terms.append(f"({a})*x^{e}" if e else f"({a})")
    return "+".join(terms) or "0"


def code_for(q,m,a):
    f=poly_expr(list(map(int,m["coefficients_desc_t_degree6"])))
    return f'''SetColumns(0);\nSetQuitOnError(true);\nQ:=Rationals(); Qx<x>:=PolynomialRing(Q);\nf:={f}; C:=HyperellipticCurve(f); J:=Jacobian(C);\nprint \"BEGIN q={q} model={m['model_id']} branch={a['branch_id']} triple={a['triple']}\";\nprint \"GENUS:\",Genus(C);\nlo,hi:=RankBounds(J); print \"RANK_BOUNDS:\",lo,hi;\nif hi eq 0 then\n  pts:=Chabauty0(J); print \"CHABAUTY0_COUNT:\",#pts; print \"CHABAUTY0_POINTS:\",pts;\nend if;\nprint \"END q={q} model={m['model_id']}\";\n'''


def submit(code):
    data=urllib.parse.urlencode({"input":code}).encode()
    req=urllib.request.Request(URL,data=data,headers={"Content-Type":"application/x-www-form-urlencoded","Accept":"text/html, application/xml, application/xhtml+xml","Referer":REFERER,"User-Agent":"perfect-cuboid-stage34-genus2-rank-smoke/1.0"},method="POST")
    with urllib.request.urlopen(req,timeout=180) as resp:
        raw=resp.read().decode("utf-8",errors="replace");status=resp.status
    root=ET.fromstring(raw); lines=[]
    for result in root.findall(".//results"):
        for line in result.findall(".//line"):lines.append("".join(line.itertext()))
    return status,raw,"\n".join(lines)+("\n" if lines else "")


def val(prefix,out,required=True):
    for line in out.splitlines():
        if line.startswith(prefix):return line[len(prefix):].strip()
    if required:raise RuntimeError(prefix+" missing")
    return None

data=json.loads(SRC.read_text());assert data["status"]=="DIAGNOSTIC_NO_CREDIT" and data["input_residual_branches"]==52
records=[];rawparts=[]
for score,m,a in choose(data):
    q=a["q"];code=code_for(q,m,a);status,raw,out=submit(code)
    if status!=200 or f"END q={q} model={m['model_id']}" not in out or any(x in out for x in ("Runtime error","Assertion failed","User error","Internal error")):
        raise SystemExit(f"Magma failure q={q} model={m['model_id']}\n{out}\nRAW_HEAD={raw[:1000]}")
    rb=val("RANK_BOUNDS:",out).split();assert len(rb)>=2
    lo,hi=map(int,rb[:2]);assert 0<=lo<=hi
    cnt=val("CHABAUTY0_COUNT:",out,False);pts=val("CHABAUTY0_POINTS:",out,False)
    rec={"q":q,"branch_id":a["branch_id"],"triple":a["triple"],"model_id":int(m["model_id"]),"squareclass":int(a["squareclass"]),"coefficients_desc_t_degree6":m["coefficients_desc_t_degree6"],"height_score":list(score),"rank_lower":lo,"rank_upper":hi,"chabauty0_count":int(cnt) if cnt is not None else None,"chabauty0_points_raw":pts,"stdout_sha256":hashlib.sha256(out.encode()).hexdigest()}
    records.append(rec);rawparts.append(f"===== q={q} model={m['model_id']} =====\n{out}")
    print(json.dumps({"q":q,"model":m["model_id"],"branch":a["branch_id"],"triple":a["triple"],"rank_bounds":[lo,hi],"chabauty0_count":rec["chabauty0_count"]},sort_keys=True))
raw="\n".join(rawparts);RAW.write_text(raw)
hist={}
for r in records:
    k=f"{r['rank_lower']},{r['rank_upper']}";hist[k]=hist.get(k,0)+1
payload={"schema":"STAGE34_02_D2_STAGEA2_GENUS2_RANKBOUNDS_SMOKE_V1","status":"DIAGNOSTIC_NO_CREDIT","protocol":"official-magma-xml-calculator","selection":"For each of seven q values choose the residual triple quotient with lexicographically smallest (max_abs_coeff,sum_abs_coeff,model_id).","sample_count":7,"rank_bounds_histogram":dict(sorted(hist.items())),"rank_upper_lt_2_count":sum(r["rank_upper"]<2 for r in records),"rank_upper_zero_count":sum(r["rank_upper"]==0 for r in records),"records":records,"raw_stdout_sha256":hashlib.sha256(raw.encode()).hexdigest(),"credit":"Smoke-test target selection only. Rank bounds and any Chabauty0 point lists apply only to the seven sampled quotient curves and give no parent-branch closure until exact quotient-to-parent degeneracy pullback is certified.","firewalls":{"sample_generalizes_to_52":False,"rank_bound_is_parent_closure":False,"chabauty0_without_pullback_closes_parent":False,"remaining_52_closed":False,"R29_EXT_CHANG_C_closed":False}}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print("GENUS2_RANKBOUNDS_SMOKE="+json.dumps({"status":payload["status"],"rank_bounds_histogram":payload["rank_bounds_histogram"],"rank_upper_lt_2_count":payload["rank_upper_lt_2_count"],"rank_upper_zero_count":payload["rank_upper_zero_count"]},sort_keys=True))
