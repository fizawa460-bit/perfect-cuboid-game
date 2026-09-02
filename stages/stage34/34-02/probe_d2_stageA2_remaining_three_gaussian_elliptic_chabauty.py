#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import pathlib
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent
LOCK = ROOT / "d2-stageA2-remaining-three-gaussian-elliptic-quotient-lock.json"
OUT = ROOT / "d2-stageA2-remaining-three-gaussian-elliptic-chabauty-probe.json"
RAW = ROOT / "d2-stageA2-remaining-three-gaussian-elliptic-chabauty-stdout.txt"
URL = "https://magma.maths.usyd.edu.au/xml/calculator.xml"
REFERER = "https://magma.maths.usyd.edu.au/calc/"
TIMEOUT = 900


def poly_expr(coeffs: list[int]) -> str:
    deg = len(coeffs) - 1
    parts: list[str] = []
    for i, a0 in enumerate(coeffs):
        a = int(a0)
        e = deg - i
        if not a:
            continue
        parts.append(f"({a})*x^{e}" if e else f"({a})")
    return "+".join(parts) or "0"


def magma_k(expr: str) -> str:
    return expr.replace("i", "ii")


def submit(code: str) -> tuple[int, str]:
    data = urllib.parse.urlencode({"input": code}).encode()
    req = urllib.request.Request(
        URL,
        data=data,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "text/html, application/xml, application/xhtml+xml",
            "Referer": REFERER,
            "User-Agent": "perfect-cuboid-stage34-remaining-three-gaussian-ellchab/1.0",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        raw = resp.read().decode("utf-8", errors="replace")
        status = resp.status
    root = ET.fromstring(raw)
    lines: list[str] = []
    for result in root.findall(".//results"):
        for line in result.findall(".//line"):
            lines.append("".join(line.itertext()))
    return status, "\n".join(lines) + ("\n" if lines else "")


def val(prefix: str, out: str, required: bool = True) -> str | None:
    for line in out.splitlines():
        if line.startswith(prefix):
            return line[len(prefix) :].strip()
    if required:
        raise RuntimeError(prefix + " missing")
    return None


def code_for(t: dict) -> str:
    a, b = map(int, t["q"].split("/"))
    d = list(map(int, t["delta"]))
    f = poly_expr(t["coefficients_desc_t_degree6"])
    rhs = magma_k(t["quotient_cubic"])
    a2 = magma_k(t["elliptic_a2"])
    a4 = magma_k(t["elliptic_a4"])
    a6 = magma_k(t["elliptic_a6"])
    alpha = int(t["alpha"])
    return f'''SetColumns(0); SetQuitOnError(true);\nQ:=Rationals(); Qz<z>:=PolynomialRing(Q); K<ii>:=NumberField(z^2+1);\nKx<x>:=PolynomialRing(K); FF:=FieldOfFractions(Kx); xx:=FF!x;\nf:={f}; ff:=FF!f; u:=xx-1/xx;\nassert Evaluate(f,-1/xx) eq -ff/xx^6;\nlhs:=ff*(xx-ii)^2/xx^4; rhs:=FF!({rhs}); assert lhs eq rhs;\nXq:=({alpha})*u; assert ({alpha})^2*rhs eq Xq^3+({a2})*Xq^2+({a4})*Xq+({a6});\nprint "BEGIN branch={t['branch_id']} q={t['q']} model={t['model_id']}"; print "SYMBOLIC_QUOTIENT_IDENTITIES: true";\nE<EX,EY,EZ>:=EllipticCurve([K|0,{a2},0,{a4},{a6}]); assert Discriminant(E) ne 0; print "ELLIPTIC_DISCRIMINANT_NONZERO: true";\nsuccess,G,m:=PseudoMordellWeilGroup(E); print "PMW_SUCCESS:",success; print "PMW_INVARIANTS:",Invariants(G);\nif success then\n  P1:=ProjectiveSpace(Q,1); pi:=map< E -> P1 | [EX,EZ] >;\n  VV,RR:=Chabauty(m,pi : IndexBound:=2); print "ELLCHAB_EXECUTED: true"; print "ELLCHAB_COUNT:",#VV; print "ELLCHAB_R:",RR;\n  rr:=RR; while IsDivisibleBy(rr,2) do rr div:= 2; end while; assert rr eq 1; print "ELLCHAB_R_2_PRIMARY: true";\n  pie:=Extend(pi); qxset:={{@ Q | @}}; quotient_infinity:=0;\n  for g in VV do\n    im:=pie(m(g)); print "ELLCHAB_GROUP_ELEMENT:",g," IMAGE:",im;\n    if im[2] eq 0 then quotient_infinity +:= 1; else Include(~qxset,Q!(im[1]/im[2])); end if;\n  end for;\n  xs:={{@ Q | @}}; rational_c_points:=0; full_parent:=0; nondeg_parent:=0;\n  for qx in qxset do\n    uu:=qx/({alpha}); discr:=uu^2+4; sq,sd:=IsSquare(discr); print "QX:",qx," U:",uu," XDISCR_SQUARE:",sq;\n    if sq then\n      for xp in [(uu+sd)/2,(uu-sd)/2] do Include(~xs,xp); end for;\n    end if;\n  end for;\n  for xp in xs do\n    cpt,yy:=IsSquare(Evaluate(f,xp));\n    U:=xp^2-1; V:=2*xp; A:={a}*U+{b}*V; B:={b}*U+{a}*V; deg:=U eq 0 or V eq 0 or A eq 0 or B eq 0;\n    sU:=IsSquare(U/({d[0]})); sV:=IsSquare(V/({d[1]})); sA:=IsSquare(A/({d[2]})); sB:=IsSquare(B/({d[3]})); parent:=cpt and sU and sV and sA and sB;\n    if cpt then rational_c_points +:= 1; end if; if parent then full_parent +:= 1; end if; if parent and not deg then nondeg_parent +:= 1; end if;\n    print "PULLBACK_X:",xp," C_POINT:",cpt," DEG:",deg," PARENT:",parent," SQ_UVAB:",sU,sV,sA,sB;\n  end for;\n  print "QUOTIENT_INFINITY_COUNT:",quotient_infinity; print "FINITE_RATIONAL_QX_COUNT:",#qxset; print "RECONSTRUCTED_RATIONAL_X_COUNT:",#xs; print "RATIONAL_C_X_COUNT:",rational_c_points;\n  print "FULL_PARENT_LIFT_X_COUNT:",full_parent; print "NONDEGENERATE_FULL_PARENT_LIFT_COUNT:",nondeg_parent;\n  print "EXCEPTIONAL_X0_INFINITY_RECEIVER_DEGENERATE: true";\n  print "CLOSURE_CANDIDATE:",nondeg_parent eq 0;\nelse\n  print "ELLCHAB_EXECUTED: false"; print "CLOSURE_CANDIDATE: false";\nend if;\nprint "END branch={t['branch_id']}";\n'''


lock = json.loads(LOCK.read_text())
assert lock["schema"] == "STAGE34_02C_D2_STAGEA2_REMAINING_THREE_GAUSSIAN_ELLIPTIC_QUOTIENT_LOCK_V1"
assert len(lock["targets"]) == 3
records: list[dict] = []
rawparts: list[str] = []
for t in lock["targets"]:
    out = ""
    err = None
    status = "UNRESOLVED_RESOURCE_OR_EXTERNAL_WALL"
    try:
        http, out = submit(code_for(t))
        bad = any(x in out for x in ("Runtime error", "Assertion failed", "User error", "Internal error"))
        if http == 200 and f"END branch={t['branch_id']}" in out and not bad:
            status = "PASS_RETURN"
        else:
            err = f"http={http} malformed_or_magma_error"
    except Exception as ex:
        err = f"{type(ex).__name__}: {ex}"
    rec = {
        "branch_id": t["branch_id"],
        "sign_partner": t["sign_partner"],
        "q": t["q"],
        "model_id": t["model_id"],
        "status": status,
        "error": err,
        "stdout_sha256": "sha256:" + hashlib.sha256(out.encode()).hexdigest(),
    }
    for pfx, key, typ in [
        ("SYMBOLIC_QUOTIENT_IDENTITIES:", "symbolic_quotient_identities", lambda s: s == "true"),
        ("ELLIPTIC_DISCRIMINANT_NONZERO:", "elliptic_discriminant_nonzero", lambda s: s == "true"),
        ("PMW_SUCCESS:", "pmw_success", lambda s: s == "true"),
        ("ELLCHAB_EXECUTED:", "ellchab_executed", lambda s: s == "true"),
        ("ELLCHAB_COUNT:", "ellchab_count", int),
        ("ELLCHAB_R:", "ellchab_R", int),
        ("ELLCHAB_R_2_PRIMARY:", "ellchab_R_2_primary", lambda s: s == "true"),
        ("QUOTIENT_INFINITY_COUNT:", "quotient_infinity_count", int),
        ("FINITE_RATIONAL_QX_COUNT:", "finite_rational_qx_count", int),
        ("RECONSTRUCTED_RATIONAL_X_COUNT:", "reconstructed_rational_x_count", int),
        ("RATIONAL_C_X_COUNT:", "rational_c_x_count", int),
        ("FULL_PARENT_LIFT_X_COUNT:", "full_parent_lift_x_count", int),
        ("NONDEGENERATE_FULL_PARENT_LIFT_COUNT:", "nondegenerate_full_parent_lift_count", int),
        ("EXCEPTIONAL_X0_INFINITY_RECEIVER_DEGENERATE:", "exceptional_x0_infinity_receiver_degenerate", lambda s: s == "true"),
        ("CLOSURE_CANDIDATE:", "closure_candidate", lambda s: s == "true"),
    ]:
        z = val(pfx, out, False)
        if z is not None:
            try:
                rec[key] = typ(z)
            except Exception:
                rec[key + "_raw"] = z
    rec["pmw_invariants"] = val("PMW_INVARIANTS:", out, False)
    rec["image_lines"] = [
        x for x in out.splitlines()
        if " IMAGE:" in x or x.startswith("QX:") or x.startswith("PULLBACK_X:")
    ]
    if status != "PASS_RETURN":
        rec["raw_tail"] = out[-3000:]
    records.append(rec)
    rawparts.append(f"===== branch={t['branch_id']} model={t['model_id']} =====\n{out}\nERROR={err or ''}\n")
    print(json.dumps({
        "branch": t["branch_id"],
        "model": t["model_id"],
        "status": status,
        "pmw": rec.get("pmw_success"),
        "ellchab": rec.get("ellchab_executed"),
        "candidate": rec.get("closure_candidate"),
    }, sort_keys=True))

raw = "\n".join(rawparts)
RAW.write_text(raw)
cands = [
    r for r in records
    if r.get("symbolic_quotient_identities")
    and r.get("pmw_success")
    and r.get("ellchab_executed")
    and r.get("ellchab_R_2_primary")
    and r.get("exceptional_x0_infinity_receiver_degenerate")
    and r.get("nondegenerate_full_parent_lift_count") == 0
]
payload = {
    "schema": "STAGE34_02C_D2_STAGEA2_REMAINING_THREE_GAUSSIAN_ELLIPTIC_CHABAUTY_PROBE_V1",
    "status": "DIAGNOSTIC_NO_CREDIT",
    "source_lock": LOCK.name,
    "source_lock_sha256": "sha256:" + hashlib.sha256(LOCK.read_bytes()).hexdigest(),
    "input_representatives": 3,
    "resolved_returns": sum(r["status"] == "PASS_RETURN" for r in records),
    "pmw_successes": sum(bool(r.get("pmw_success")) for r in records),
    "ellchab_executed": sum(bool(r.get("ellchab_executed")) for r in records),
    "closure_candidate_count": len(cands),
    "closure_candidate_branch_ids": [r["branch_id"] for r in cands],
    "sign_transfer_candidate_branch_ids": [r["sign_partner"] for r in cands],
    "records": records,
    "raw_stdout_sha256": "sha256:" + hashlib.sha256(raw.encode()).hexdigest(),
    "credit": "Diagnostic only. Successful records still require dedicated exact proof replay and hostile audit before direct or sign-transfer branch closure. External/resource failure is not mathematical failure.",
    "firewalls": {
        "diagnostic_candidate_is_authoritative": False,
        "sign_partner_transfer_authoritative_before_audit": False,
        "authoritative_remaining_branches": 8,
        "authoritative_remaining_sign_orbits": 4,
        "D2_all_factor_branches_closed": False,
        "all_multiples_closed": False,
        "R29_EXT_CHANG_C_closed": False,
        "parent_route_closed": False,
        "perfect_cuboid_nonexistence_claim": False,
    },
}
OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
print("REMAINING_THREE_GAUSSIAN_ELLCHAB=" + json.dumps({
    "status": payload["status"],
    "resolved_returns": payload["resolved_returns"],
    "pmw_successes": payload["pmw_successes"],
    "ellchab_executed": payload["ellchab_executed"],
    "closure_candidate_count": payload["closure_candidate_count"],
    "closure_candidate_branch_ids": payload["closure_candidate_branch_ids"],
}, sort_keys=True))
