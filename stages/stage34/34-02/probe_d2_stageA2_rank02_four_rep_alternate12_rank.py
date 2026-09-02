#!/usr/bin/env python3
from __future__ import annotations
import collections, hashlib, json, pathlib, urllib.parse, urllib.request, xml.etree.ElementTree as ET

ROOT=pathlib.Path(__file__).resolve().parent
LOCK=ROOT/"d2-stageA2-rank02-four-rep-alternate12-lock.json"
OUT=ROOT/"d2-stageA2-rank02-four-rep-alternate12-rank-probe.json"
RAW=ROOT/"d2-stageA2-rank02-four-rep-alternate12-rank-probe-stdout.txt"
URL="https://magma.maths.usyd.edu.au/xml/calculator.xml"; REFERER="https://magma.maths.usyd.edu.au/calc/"; TIMEOUT=180

def poly_expr(c):
    deg=len(c)-1; parts=[]
    for i,a in enumerate(c):
        a=int(a); e=deg-i
        if a: parts.append(f"({a})*x^{e}" if e else f"({a})")
    return "+".join(parts) or "0"

def code_for(t):
    f=poly_expr(t["coefficients_desc_t_degree6"])
    return f'''SetColumns(0);\nSetQuitOnError(true);\nQ:=Rationals(); Qx<x>:=PolynomialRing(Q);\nf:={f}; C:=HyperellipticCurve(f); J:=Jacobian(C);\nprint \"BEGIN branch={t['branch_id']} model={t['model_id']} triple={t['alternate_triple']}\";\nlo,hi:=RankBounds(J); print \"RANK_BOUNDS:\",lo,hi;\nprint \"END branch={t['branch_id']} model={t['model_id']}\";\n'''

def submit(code):
    data=urllib.parse.urlencode({"input":code}).encode()
    req=urllib.request.Request(URL,data=data,headers={"Content-Type":"application/x-www-form-urlencoded","Accept":"text/html, application/xml, application/xhtml+xml","Referer":REFERER,"User-Agent":"perfect-cuboid-stage34-alt12-rank/1.0"},method="POST")
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

lock=json.loads(LOCK.read_text())
assert lock["schema"]=="STAGE34_02B_D2_STAGEA2_RANK02_FOUR_REP_ALTERNATE12_LOCK_V1"
assert lock["status"]=="SOURCE_LOCKED_COLD_NOT_ARMED"
targets=lock["targets"]
assert len(targets)==12 and len({int(t["model_id"]) for t in targets})==12
assert collections.Counter(t["branch_id"] for t in targets)==collections.Counter({x:3 for x in lock["representatives"]})

records=[]; rawparts=[]
for i,t in enumerate(targets,1):
    out=""; err=None; status="UNRESOLVED"
    try:
        http,out=submit(code_for(t)); bad=any(x in out for x in ("Runtime error","Assertion failed","User error","Internal error"))
        marker=f"END branch={t['branch_id']} model={t['model_id']}"
        if http==200 and marker in out and not bad: status="PASS_RANK_BOUNDS"
        else: err=f"http={http} malformed_or_magma_error"
    except Exception as ex: err=f"{type(ex).__name__}: {ex}"
    rec={"index":i,**t,"status":status,"error":err}
    if status=="PASS_RANK_BOUNDS":
        vals=val("RANK_BOUNDS:",out).split(); lo,hi=map(int,vals[:2]); assert 0<=lo<=hi
        rec.update({"rank_lower":lo,"rank_upper":hi})
    records.append(rec); rawparts.append(f"===== index={i} branch={t['branch_id']} model={t['model_id']} =====\n{out}\nERROR={err or ''}")
    print(json.dumps({"index":i,"branch":t["branch_id"],"model":t["model_id"],"triple":t["alternate_triple"],"status":status,"rank_bounds":[rec.get("rank_lower"),rec.get("rank_upper")]},sort_keys=True))
raw="\n".join(rawparts); RAW.write_text(raw)
resolved=[r for r in records if r["status"]=="PASS_RANK_BOUNDS"]
fav=[r for r in resolved if int(r["rank_upper"])<=1]
hist=collections.Counter(f"{r['rank_lower']},{r['rank_upper']}" for r in resolved)
best={}
for r in resolved:
    b=r["branch_id"]; u=int(r["rank_upper"])
    if b not in best or u<best[b]: best[b]=u
payload={
  "schema":"STAGE34_02B_D2_STAGEA2_RANK02_FOUR_REP_ALTERNATE12_RANK_PROBE_V1",
  "status":"DIAGNOSTIC_NO_CREDIT_COMPLETE" if len(resolved)==12 else "DIAGNOSTIC_NO_CREDIT_PARTIAL",
  "source_lock":LOCK.name,"source_lock_sha256":"sha256:"+hashlib.sha256(LOCK.read_bytes()).hexdigest(),
  "input_targets":12,"resolved":len(resolved),"unresolved":12-len(resolved),
  "rank_bounds_histogram":dict(sorted(hist.items())),"best_alternate_rank_upper_by_branch":dict(sorted(best.items())),
  "favorable_rank_upper_le_1_count":len(fav),"favorable_targets":[{"branch_id":r["branch_id"],"q":r["q"],"triple":r["alternate_triple"],"model_id":r["model_id"],"rank_bounds":[r["rank_lower"],r["rank_upper"]]} for r in fav],
  "records":records,"raw_stdout_sha256":"sha256:"+hashlib.sha256(raw.encode()).hexdigest(),
  "credit":"Targeted RankBounds diagnostic only. A favorable alternate quotient does not close a parent branch; it only authorizes a smaller follow-up rational-point/proof leaf.",
  "firewalls":{"rank_bound_is_complete_pointset":False,"diagnostic_is_parent_closure":False,"unresolved_is_math_failure":False,"remaining_26_closed":False,"D2_all_factor_branches_closed":False,"all_multiples_closed":False,"R29_EXT_CHANG_C_closed":False,"perfect_cuboid_nonexistence_claim":False}
}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print("ALT12_RANK_PROBE="+json.dumps({k:payload[k] for k in ["status","resolved","unresolved","rank_bounds_histogram","best_alternate_rank_upper_by_branch","favorable_rank_upper_le_1_count"]},sort_keys=True))
