#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, pathlib, urllib.parse, urllib.request, xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent
LOCK = ROOT / "d2-stageA2-hard-rank02-two-orbit-lock.json"
OUT = ROOT / "d2-stageA2-hard-rank02-twocover-diagnostic.json"
RAW = ROOT / "d2-stageA2-hard-rank02-twocover-diagnostic-stdout.txt"
URL = "https://magma.maths.usyd.edu.au/xml/calculator.xml"
REFERER = "https://magma.maths.usyd.edu.au/calc/"
TIMEOUT = 600


def poly_expr(coeffs):
    deg = len(coeffs) - 1
    parts = []
    for i, a in enumerate(coeffs):
        a = int(a)
        e = deg - i
        if a:
            parts.append(f"({a})*x^{e}" if e else f"({a})")
    return "+".join(parts) or "0"


def submit(code):
    data = urllib.parse.urlencode({"input": code}).encode()
    req = urllib.request.Request(
        URL,
        data=data,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "text/html, application/xml, application/xhtml+xml",
            "Referer": REFERER,
            "User-Agent": "perfect-cuboid-stage34-hard-rank02-twocover/1.0",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        raw = resp.read().decode("utf-8", errors="replace")
        http = resp.status
    root = ET.fromstring(raw)
    lines = []
    for result in root.findall(".//results"):
        for line in result.findall(".//line"):
            lines.append("".join(line.itertext()))
    return http, "\n".join(lines) + ("\n" if lines else "")


def val(prefix, out):
    for line in out.splitlines():
        if line.startswith(prefix):
            return line[len(prefix):].strip()
    raise RuntimeError(prefix + " missing")


lock = json.loads(LOCK.read_text())
assert lock["schema"] == "STAGE34_02B_D2_STAGEA2_HARD_RANK02_TWO_ORBIT_LOCK_V1"
records = []
rawparts = []
for i, branch in enumerate(lock["representatives"], 1):
    mid = int(branch["preferred_first_higher_rank_model"])
    model = next(m for m in branch["alternate_rank_diagnostic"] if int(m["model_id"]) == mid)
    f = poly_expr(model["coefficients_desc_t_degree6"])
    code = f'''SetColumns(0); SetQuitOnError(true);
Q:=Rationals(); Qx<x>:=PolynomialRing(Q); f:={f}; C:=HyperellipticCurve(f); assert Genus(C) eq 2;
J:=Jacobian(C); rb:=RankBounds(J); print "RANK_BOUNDS:",rb[1],rb[2];
Hk,AtoHk:=TwoCoverDescent(C : PrimeBound:=30);
print "FAKE_TWO_SELMER_SIZE:",#Hk;
print "PROBE_COMPLETE: true";
'''
    out = ""
    err = None
    try:
        http, out = submit(code)
        bad = any(s in out for s in ("Runtime error", "Assertion failed", "User error", "Internal error"))
        ok = http == 200 and not bad and val("PROBE_COMPLETE:", out) == "true"
    except Exception as ex:
        http = None
        ok = False
        err = f"{type(ex).__name__}: {ex}"
    rec = {
        "branch_id": branch["branch_id"],
        "partner": branch["partner"],
        "q": branch["q"],
        "model_id": mid,
        "triple": model["triple"],
        "locked_rank_bounds": model["rank_bounds"],
        "prime_bound": 30,
        "execution_complete": ok,
        "http_status": http,
        "error": err,
        "stdout_sha256": "sha256:" + hashlib.sha256(out.encode()).hexdigest(),
    }
    if ok:
        rb = val("RANK_BOUNDS:", out).split()
        rec["fresh_rank_bounds"] = [int(rb[0]), int(rb[1])]
        rec["fake_two_selmer_size_primebound30"] = int(val("FAKE_TWO_SELMER_SIZE:", out))
    records.append(rec)
    rawparts.append(f"===== index={i} branch={branch['branch_id']} model={mid} =====\n{out}\nERROR={err or ''}")
    print(json.dumps(rec, sort_keys=True))

raw = "\n".join(rawparts)
RAW.write_text(raw)
payload = {
    "schema": "STAGE34_02B_D2_STAGEA2_HARD_RANK02_TWOCOVER_DIAGNOSTIC_V1",
    "status": "DIAGNOSTIC_COMPLETE_NO_CREDIT" if all(r["execution_complete"] for r in records) else "DIAGNOSTIC_EXTERNAL_RESPONSE_PARTIAL_NO_CREDIT",
    "source_lock": LOCK.name,
    "source_lock_sha256": "sha256:" + hashlib.sha256(LOCK.read_bytes()).hexdigest(),
    "records": records,
    "raw_stdout_sha256": "sha256:" + hashlib.sha256(raw.encode()).hexdigest(),
    "interpretation": "PrimeBound=30 is intentionally diagnostic and may enlarge the fake 2-Selmer set. Its size is routing information only. No emptiness, rational-point completeness, parent-lift, theorem, or receiver credit is granted by this probe.",
    "firewalls": {
        "diagnostic_is_exact_two_selmer_set": False,
        "diagnostic_closes_parent": False,
        "hostile_audit_passed": False,
        "D2_all_factor_branches_closed": False,
        "all_multiples_closed": False,
        "R29_EXT_CHANG_C_closed": False,
        "parent_route_closed": False,
        "perfect_cuboid_nonexistence_claim": False,
    },
}
OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
print("HARD_RANK02_TWOCOVER=" + json.dumps({"status": payload["status"]}, sort_keys=True))
