#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,pathlib,urllib.parse,urllib.request,xml.etree.ElementTree as ET

ROOT=pathlib.Path(__file__).resolve().parent
LOCK=ROOT/"d2-stageA2-q8413-two-mwsha-descent-lock.json"
OUT=ROOT/"d2-stageA2-q8413-two-mwsha-descent-probe.json"
RAW=ROOT/"d2-stageA2-q8413-two-mwsha-descent-stdout.txt"
URL="https://magma.maths.usyd.edu.au/xml/calculator.xml"
REFERER="https://magma.maths.usyd.edu.au/calc/"
TIMEOUT=1200

def submit(code):
    data=urllib.parse.urlencode({"input":code}).encode()
    req=urllib.request.Request(URL,data=data,headers={
        "Content-Type":"application/x-www-form-urlencoded",
        "Accept":"text/html, application/xml, application/xhtml+xml",
        "Referer":REFERER,
        "User-Agent":"perfect-cuboid-stage34-q8413-mwsha/1.0"
    },method="POST")
    with urllib.request.urlopen(req,timeout=TIMEOUT) as resp:
        raw=resp.read().decode("utf-8",errors="replace"); status=resp.status
    root=ET.fromstring(raw); lines=[]
    for result in root.findall(".//results"):
        for line in result.findall(".//line"):
            lines.append("".join(line.itertext()))
    return status,"\n".join(lines)+("\n" if lines else "")

def marker(prefix,out):
    for line in out.splitlines():
        if line.startswith(prefix): return line[len(prefix):].strip()
    return None

lock=json.loads(LOCK.read_text())
records=[]; raw_sections=[]
for t in lock["targets"]:
    bid=t["branch_id"]
    if bid=="40dc8f63e92a8a3a65e8":
        a2="-89531+578508*ii"; a4="-51794399748*ii"
    elif bid=="7a7ef1a67e794fe1651f":
        a2="1157016-179062*ii"; a4="-207177598992*ii"
    else:
        raise RuntimeError("unexpected target")
    code=f'''SetColumns(0); SetQuitOnError(true);\nQz<z>:=PolynomialRing(Rationals()); K<ii>:=NumberField(z^2+1);\nE:=EllipticCurve([K|0,{a2},0,{a4},0]); assert Discriminant(E) ne 0;\nlo,hi:=RankBounds(E : Effort:=1); print "BASELINE_RANK_BOUNDS:",lo,hi; assert lo eq 0 and hi eq 1;\nT,tm:=TorsionSubgroup(E); print "TORSION_INVARIANTS:",Invariants(T); assert Invariants(T) eq [2,2];\nrinfo,pts,shainfo:=MordellWeilShaInformation(E : Effort:=5);\nprint "MWSHA_RANK_INFO:",rinfo;\nprint "MWSHA_POINT_COUNT:",#pts;\nfor j in [1..#pts] do print "MWSHA_POINT:",j,pts[j]; end for;\nprint "MWSHA_SHA_INFO:",shainfo;\nprint "DIAGNOSTIC_COMPLETE: true";\n'''
    try:
        http,out=submit(code)
        err=None
    except Exception as e:
        http=0; out=""; err=repr(e)
    raw_sections.append(f"===== branch={bid} model={t['model_id']} =====\n{out}\nERROR={err or ''}\n")
    bad=err is not None or http!=200 or any(x in out for x in ("Runtime error","Assertion failed","User error","Internal error"))
    complete=marker("DIAGNOSTIC_COMPLETE:",out)=="true"
    records.append({
        "branch_id":bid,"sign_partner":t["sign_partner"],"q":t["q"],"model_id":t["model_id"],
        "http":http,"status":"PASS_RETURN" if (not bad and complete) else "OPEN_EXTERNAL_OR_RUNTIME",
        "baseline_rank_bounds":marker("BASELINE_RANK_BOUNDS:",out),
        "torsion_invariants":marker("TORSION_INVARIANTS:",out),
        "mwsha_rank_info":marker("MWSHA_RANK_INFO:",out),
        "mwsha_point_count":int(marker("MWSHA_POINT_COUNT:",out)) if marker("MWSHA_POINT_COUNT:",out) not in (None,"") else None,
        "mwsha_sha_info":marker("MWSHA_SHA_INFO:",out),
        "diagnostic_complete":complete,"error":err,
        "stdout_sha256":"sha256:"+hashlib.sha256(out.encode()).hexdigest()
    })
raw="\n".join(raw_sections); RAW.write_text(raw)
payload={
  "schema":"STAGE34_02C_D2_STAGEA2_Q8413_TWO_MWSHA_DESCENT_PROBE_V1",
  "status":"DIAGNOSTIC_NO_CREDIT",
  "source_lock":LOCK.name,
  "source_lock_sha256":"sha256:"+hashlib.sha256(LOCK.read_bytes()).hexdigest(),
  "input_representatives":len(records),
  "resolved_returns":sum(r["status"]=="PASS_RETURN" for r in records),
  "records":records,
  "raw_stdout_sha256":"sha256:"+hashlib.sha256(raw.encode()).hexdigest(),
  "credit":"Diagnostic only. Exact equal rank information, if any, must be frozen into a dedicated classification/proof route with complete rational-X pullback before hostile audit or authority changes.",
  "firewalls":{"mwsha_diagnostic_is_authoritative":False,"hostile_audit_passed":False,"authoritative_remaining_branches":8,"authoritative_remaining_sign_orbits":4,"D2_all_factor_branches_closed":False,"R29_EXT_CHANG_C_closed":False,"perfect_cuboid_nonexistence_claim":False}
}
OUT.write_text(json.dumps(payload,indent=2,sort_keys=True)+"\n")
print(json.dumps({"status":payload["status"],"resolved_returns":payload["resolved_returns"],"records":[{"branch_id":r["branch_id"],"status":r["status"],"mwsha_rank_info":r["mwsha_rank_info"]} for r in records]},sort_keys=True))
