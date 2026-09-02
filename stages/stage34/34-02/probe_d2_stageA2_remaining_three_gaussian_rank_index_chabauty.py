#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import pathlib
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent
LOCK = ROOT / "d2-stageA2-remaining-three-gaussian-rank-index-lock.json"
OUT = ROOT / "d2-stageA2-remaining-three-gaussian-rank-index-chabauty-probe.json"
RAW = ROOT / "d2-stageA2-remaining-three-gaussian-rank-index-chabauty-stdout.txt"
URL = "https://magma.maths.usyd.edu.au/xml/calculator.xml"
REFERER = "https://magma.maths.usyd.edu.au/calc/"
TIMEOUT = 1200


def poly_expr(coeffs: list[int]) -> str:
    deg = len(coeffs) - 1
    parts: list[str] = []
    for i, a0 in enumerate(coeffs):
        a = int(a0)
        e = deg - i
        if a:
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
            "User-Agent": "perfect-cuboid-stage34-remaining-three-gaussian-rank-index/1.0",
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
            return line[len(prefix):].strip()
    if required:
        raise RuntimeError(prefix + " missing")
    return None


def code_for(t: dict) -> str:
    a, b = map(int, t["q"].split("/"))
    d = list(map(int, t["delta"]))
    f = poly_expr(t["coefficients_desc_t_degree6"])
    rhs = magma_k(t["quotient_cubic"])
    alpha = int(t["alpha"])
    a2 = magma_k(t["elliptic_a2"])
    a4 = magma_k(t["elliptic_a4"])
    a6 = magma_k(t["elliptic_a6"])
    return f'''SetColumns(0); SetQuitOnError(true);\nQ:=Rationals(); Qz<z>:=PolynomialRing(Q); K<ii>:=NumberField(z^2+1);\nKx<x>:=PolynomialRing(K); FF:=FieldOfFractions(Kx); xx:=FF!x;\nf:={f}; ff:=FF!f; u:=xx-1/xx;\nassert Evaluate(f,-1/xx) eq -ff/xx^6;\nlhs:=ff*(xx-ii)^2/xx^4; rhs:=FF!({rhs}); assert lhs eq rhs;\nXq:=({alpha})*u; assert ({alpha})^2*rhs eq Xq^3+({a2})*Xq^2+({a4})*Xq+({a6});\nprint "BEGIN branch={t['branch_id']} q={t['q']} model={t['model_id']}"; print "SYMBOLIC_QUOTIENT_IDENTITIES: true";\nE<EX,EY,EZ>:=EllipticCurve([K|0,{a2},0,{a4},{a6}]); assert Discriminant(E) ne 0;\nlo,hi:=RankBounds(E : Effort:=1); print "RANK_LOWER:",lo; print "RANK_UPPER:",hi;\nT,tm:=TorsionSubgroup(E); tinv:=Invariants(T); print "TORSION_INVARIANTS:",tinv;\nsuccess,G,pm:=PseudoMordellWeilGroup(E); pinv:=Invariants(G); print "PMW_SUCCESS:",success; print "PMW_INVARIANTS:",pinv;\nP1:=ProjectiveSpace(Q,1); pi:=map< E -> P1 | [EX,EZ] >; pie:=Extend(pi);\nmode:="OPEN_RANK_OR_INDEX"; complete_index:=false; RR:=0;\nquotient_rational_x:=0; reconstructed_C_x:=0; full_parent:=0; nondeg_parent:=0; quotient_infinity:=0;\nif lo eq 0 and hi eq 0 then\n  mode:="RANK0_TORSION_FULL"; complete_index:=true; print "FULL_GROUP_MODE: RANK0_TORSION_FULL";\n  for g in T do\n    Pcur:=tm(g); im:=pie(Pcur); print "GROUP_IMAGE:",g," -> ",im;\n    if im[2] eq 0 then\n      quotient_infinity +:= 1;\n    else\n      kval:=im[1]/im[2]; ok,qx:=IsCoercible(Q,kval);\n      if ok then\n        quotient_rational_x +:= 1; uu:=qx/({alpha}); sq,sd:=IsSquare(uu^2+4); print "QX:",qx," U:",uu," XDISCR_SQUARE:",sq;\n        if sq then\n          for xp in [(uu+sd)/2,(uu-sd)/2] do\n            cpt,yy:=IsSquare(Evaluate(f,xp)); U:=xp^2-1; V:=2*xp; A:={a}*U+{b}*V; B:={b}*U+{a}*V; deg:=U eq 0 or V eq 0 or A eq 0 or B eq 0;\n            sU:=IsSquare(U/({d[0]})); sV:=IsSquare(V/({d[1]})); sA:=IsSquare(A/({d[2]})); sB:=IsSquare(B/({d[3]})); parent:=cpt and sU and sV and sA and sB;\n            if cpt then reconstructed_C_x +:= 1; end if; if parent then full_parent +:= 1; end if; if parent and not deg then nondeg_parent +:= 1; end if;\n            print "PULLBACK_X:",xp," C_POINT:",cpt," DEG:",deg," PARENT:",parent," SQ_UVAB:",sU,sV,sA,sB;\n          end for;\n        end if;\n      end if;\n    end if;\n  end for;\nelif lo eq 1 and hi eq 1 then\n  gensG:=[G.i : i in [1..Ngens(G)]]; freeG:=[g : g in gensG | Order(g) eq 0]; print "PMW_FREE_GENERATOR_COUNT:",#freeG;\n  if #freeG eq 1 and tinv eq [2,2] then\n    P:=pm(freeG[1]); assert Order(P) eq 0; print "FREE_POINT:",P;\n    SP:=Saturation([P],2 : TorsionFree:=true); print "SAT2_COUNT:",#SP;\n    if #SP eq 1 then\n      QP:=SP[1]; assert Order(QP) eq 0; print "SAT2_POINT:",QP;\n      H:=AbelianGroup([2,2,0]); T1:=tm(T.1); T2:=tm(T.2);\n      hm:=map< H -> E | h :-> (Integers()!Eltseq(h)[1])*T1 + (Integers()!Eltseq(h)[2])*T2 + (Integers()!Eltseq(h)[3])*QP >;\n      VV,RR:=Chabauty(hm,pi : IndexBound:=2); rr:=RR; while rr gt 0 and rr mod 2 eq 0 do rr div:=2; end while;\n      print "ELLCHAB_R:",RR; print "ELLCHAB_R_2_PRIMARY:",RR gt 0 and rr eq 1; print "ELLCHAB_COUNT:",#VV;\n      if RR gt 0 and rr eq 1 then\n        mode:="RANK1_SAT2_ELLCHAB"; complete_index:=true;\n        for g in VV do\n          Pcur:=hm(g); im:=pie(Pcur); print "GROUP_IMAGE:",g," -> ",im;\n          if im[2] eq 0 then\n            quotient_infinity +:= 1;\n          else\n            kval:=im[1]/im[2]; ok,qx:=IsCoercible(Q,kval);\n            if ok then\n              quotient_rational_x +:= 1; uu:=qx/({alpha}); sq,sd:=IsSquare(uu^2+4); print "QX:",qx," U:",uu," XDISCR_SQUARE:",sq;\n              if sq then\n                for xp in [(uu+sd)/2,(uu-sd)/2] do\n                  cpt,yy:=IsSquare(Evaluate(f,xp)); U:=xp^2-1; V:=2*xp; A:={a}*U+{b}*V; B:={b}*U+{a}*V; deg:=U eq 0 or V eq 0 or A eq 0 or B eq 0;\n                  sU:=IsSquare(U/({d[0]})); sV:=IsSquare(V/({d[1]})); sA:=IsSquare(A/({d[2]})); sB:=IsSquare(B/({d[3]})); parent:=cpt and sU and sV and sA and sB;\n                  if cpt then reconstructed_C_x +:= 1; end if; if parent then full_parent +:= 1; end if; if parent and not deg then nondeg_parent +:= 1; end if;\n                  print "PULLBACK_X:",xp," C_POINT:",cpt," DEG:",deg," PARENT:",parent," SQ_UVAB:",sU,sV,sA,sB;\n                end for;\n              end if;\n            end if;\n          end if;\n        end for;\n      end if;\n    end if;\n  end if;\nend if;\nprint "MODE:",mode; print "INDEX_COMPLETENESS_PROVED:",complete_index;\nprint "QUOTIENT_INFINITY_COUNT:",quotient_infinity; print "QUOTIENT_RATIONAL_X_COUNT:",quotient_rational_x; print "RECONSTRUCTED_C_X_COUNT_WITH_MULTIPLICITY:",reconstructed_C_x;\nprint "FULL_PARENT_LIFT_X_COUNT:",full_parent; print "NONDEGENERATE_FULL_PARENT_LIFT_COUNT:",nondeg_parent; print "EXCEPTIONAL_X0_INFINITY_RECEIVER_DEGENERATE: true";\nprint "CLOSURE_CANDIDATE:",complete_index and nondeg_parent eq 0; print "END branch={t['branch_id']}";\n'''


lock = json.loads(LOCK.read_text())
assert lock["schema"] == "STAGE34_02C_D2_STAGEA2_REMAINING_THREE_GAUSSIAN_RANK_INDEX_LOCK_V1"
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
        "branch_id": t["branch_id"], "sign_partner": t["sign_partner"], "q": t["q"], "model_id": t["model_id"],
        "status": status, "error": err, "stdout_sha256": "sha256:" + hashlib.sha256(out.encode()).hexdigest(),
    }
    for pfx, key, typ in [
        ("SYMBOLIC_QUOTIENT_IDENTITIES:", "symbolic_quotient_identities", lambda s: s == "true"),
        ("RANK_LOWER:", "rank_lower", int), ("RANK_UPPER:", "rank_upper", int),
        ("PMW_SUCCESS:", "pmw_success", lambda s: s == "true"),
        ("PMW_FREE_GENERATOR_COUNT:", "pmw_free_generator_count", int),
        ("SAT2_COUNT:", "sat2_count", int), ("ELLCHAB_R:", "ellchab_R", int),
        ("ELLCHAB_R_2_PRIMARY:", "ellchab_R_2_primary", lambda s: s == "true"),
        ("ELLCHAB_COUNT:", "ellchab_count", int),
        ("INDEX_COMPLETENESS_PROVED:", "index_completeness_proved", lambda s: s == "true"),
        ("QUOTIENT_INFINITY_COUNT:", "quotient_infinity_count", int),
        ("QUOTIENT_RATIONAL_X_COUNT:", "quotient_rational_x_count", int),
        ("RECONSTRUCTED_C_X_COUNT_WITH_MULTIPLICITY:", "reconstructed_C_x_count_with_multiplicity", int),
        ("FULL_PARENT_LIFT_X_COUNT:", "full_parent_lift_x_count", int),
        ("NONDEGENERATE_FULL_PARENT_LIFT_COUNT:", "nondegenerate_full_parent_lift_count", int),
        ("EXCEPTIONAL_X0_INFINITY_RECEIVER_DEGENERATE:", "exceptional_x0_infinity_receiver_degenerate", lambda s: s == "true"),
        ("CLOSURE_CANDIDATE:", "closure_candidate", lambda s: s == "true"),
    ]:
        z = val(pfx, out, False)
        if z is not None:
            try: rec[key] = typ(z)
            except Exception: rec[key + "_raw"] = z
    rec["torsion_invariants"] = val("TORSION_INVARIANTS:", out, False)
    rec["pmw_invariants"] = val("PMW_INVARIANTS:", out, False)
    rec["free_point"] = val("FREE_POINT:", out, False)
    rec["sat2_point"] = val("SAT2_POINT:", out, False)
    rec["mode"] = val("MODE:", out, False)
    rec["evidence_lines"] = [x for x in out.splitlines() if x.startswith(("GROUP_IMAGE:", "QX:", "PULLBACK_X:"))]
    if status != "PASS_RETURN": rec["raw_tail"] = out[-3500:]
    records.append(rec)
    rawparts.append(f"===== branch={t['branch_id']} model={t['model_id']} =====\n{out}\nERROR={err or ''}\n")
    print(json.dumps({"branch": t["branch_id"], "model": t["model_id"], "status": status, "rank": [rec.get("rank_lower"), rec.get("rank_upper")], "mode": rec.get("mode"), "candidate": rec.get("closure_candidate")}, sort_keys=True))

raw = "\n".join(rawparts)
RAW.write_text(raw)
cands = [r for r in records if r.get("symbolic_quotient_identities") and r.get("index_completeness_proved") and r.get("exceptional_x0_infinity_receiver_degenerate") and r.get("nondegenerate_full_parent_lift_count") == 0]
payload = {
    "schema": "STAGE34_02C_D2_STAGEA2_REMAINING_THREE_GAUSSIAN_RANK_INDEX_CHABAUTY_PROBE_V1",
    "status": "DIAGNOSTIC_NO_CREDIT",
    "source_lock": LOCK.name,
    "source_lock_sha256": "sha256:" + hashlib.sha256(LOCK.read_bytes()).hexdigest(),
    "input_representatives": 3,
    "resolved_returns": sum(r["status"] == "PASS_RETURN" for r in records),
    "exact_rank_resolved": sum(r.get("rank_lower") == r.get("rank_upper") and r.get("rank_lower") in (0,1) for r in records),
    "index_completeness_proved": sum(bool(r.get("index_completeness_proved")) for r in records),
    "closure_candidate_count": len(cands),
    "closure_candidate_branch_ids": [r["branch_id"] for r in cands],
    "sign_transfer_candidate_branch_ids": [r["sign_partner"] for r in cands],
    "records": records,
    "raw_stdout_sha256": "sha256:" + hashlib.sha256(raw.encode()).hexdigest(),
    "credit": "Diagnostic only. Equal exact rank, index/Chabauty completeness, and zero nondegenerate parent lifts make a branch a proof-replay candidate only. Dedicated deterministic replay plus hostile audit remain mandatory.",
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
print("REMAINING_THREE_GAUSSIAN_RANK_INDEX=" + json.dumps({k: payload[k] for k in ["resolved_returns", "exact_rank_resolved", "index_completeness_proved", "closure_candidate_count", "closure_candidate_branch_ids"]}, sort_keys=True))
