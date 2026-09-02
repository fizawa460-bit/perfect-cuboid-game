#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import pathlib
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parent
LOCK = ROOT / "d2-stageA2-model191-gaussian-quartic-genusone-lock.json"
OUT = ROOT / "d2-stageA2-model191-gaussian-quartic-genusone-chabauty-probe.json"
RAW = ROOT / "d2-stageA2-model191-gaussian-quartic-genusone-chabauty-stdout.txt"
URL = "https://magma.maths.usyd.edu.au/xml/calculator.xml"
REFERER = "https://magma.maths.usyd.edu.au/calc/"
TIMEOUT = 1200


def submit(code: str) -> tuple[int, str]:
    data = urllib.parse.urlencode({"input": code}).encode()
    req = urllib.request.Request(
        URL,
        data=data,
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "text/html, application/xml, application/xhtml+xml",
            "Referer": REFERER,
            "User-Agent": "perfect-cuboid-stage34-model191-quartic-genusone/1.0",
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


def magma_code(lock: dict) -> str:
    t = lock["target"]
    a, b = map(int, t["q"].split("/"))
    d = list(map(int, t["delta"]))
    ad = lock["exact_quartic_adapter"]
    alpha = int(ad["alpha"])
    return f'''SetColumns(0); SetQuitOnError(true);\nQ:=Rationals(); Qx<t>:=PolynomialRing(Q); fQ:=1560*t^6+7921*t^5+1560*t^4-15842*t^3-1560*t^2+7921*t-1560;\nassert fQ eq (t-1)*(t+1)*(3*t+13)*(5*t+8)*(8*t-5)*(13*t-3);\nQz<z>:=PolynomialRing(Q); K<ii>:=NumberField(z^2+1); Kx<x>:=PolynomialRing(K); FF:=FieldOfFractions(Kx); xx:=FF!x; ff:=FF!Evaluate(fQ,xx);\nu:=xx-1/xx; v2:=ff*(xx-ii)^2/xx^4; quartic:=u*(u-2*ii)*(39*u+160)*(40*u+39);\nassert Evaluate(ff,-1/xx) eq -ff/xx^6; assert v2 eq quartic;\ns:=1/u; w2:=(1+ii)^2*quartic/u^4; cubic:=24960*s^3+(31684+12480*ii)*s^2+(6240+15842*ii)*s+3120*ii; assert w2 eq cubic;\nXq:=({alpha})*s; assert ({alpha})^2*cubic eq Xq^3+(31684+12480*ii)*Xq^2+(155750400+395416320*ii)*Xq+1943764992000*ii;\nprint "BEGIN branch={t['branch_id']} q={t['q']} model={t['model_id']}"; print "SYMBOLIC_QUARTIC_TO_CUBIC_IDENTITIES: true";\nE<EX,EY,EZ>:=EllipticCurve([K|0,31684+12480*ii,0,155750400+395416320*ii,1943764992000*ii]); assert Discriminant(E) ne 0;\nlo,hi:=RankBounds(E : Effort:=1); print "RANK_LOWER:",lo; print "RANK_UPPER:",hi;\nT,tm:=TorsionSubgroup(E); tinv:=Invariants(T); print "TORSION_INVARIANTS:",tinv;\nsuccess,G,pm:=PseudoMordellWeilGroup(E); pinv:=Invariants(G); print "PMW_SUCCESS:",success; print "PMW_INVARIANTS:",pinv;\nP1:=ProjectiveSpace(Q,1); pi:=map< E -> P1 | [EX,EZ] >; pie:=Extend(pi);\nmode:="OPEN_RANK_OR_INDEX"; complete_index:=false; RR:=0; quotient_rational_X:=0; reconstructed_C_x:=0; full_parent:=0; nondeg_parent:=0; quotient_infinity:=0; inversion_boundary:=0;\nprocedure ReplayPoint(Pcur, ~quotient_rational_X, ~reconstructed_C_x, ~full_parent, ~nondeg_parent, ~quotient_infinity, ~inversion_boundary)\n  im:=pie(Pcur); print "GROUP_IMAGE:",im;\n  if im[2] eq 0 then quotient_infinity +:= 1; return; end if;\n  kval:=im[1]/im[2]; ok,qX:=IsCoercible(Q,kval); if not ok then return; end if; quotient_rational_X +:= 1;\n  ss:=qX/({alpha}); print "QX:",qX," S:",ss;\n  if ss eq 0 then inversion_boundary +:= 1; print "INVERSION_BOUNDARY_S0: true"; return; end if;\n  uu:=1/ss; sq,sd:=IsSquare(uu^2+4); print "U:",uu," XDISCR_SQUARE:",sq;\n  if not sq then return; end if;\n  for xp in [(uu+sd)/2,(uu-sd)/2] do\n    cpt,yy:=IsSquare(Evaluate(fQ,xp)); U:=xp^2-1; V:=2*xp; A:={a}*U+{b}*V; B:={b}*U+{a}*V; deg:=U eq 0 or V eq 0 or A eq 0 or B eq 0;\n    sU:=IsSquare(U/({d[0]})); sV:=IsSquare(V/({d[1]})); sA:=IsSquare(A/({d[2]})); sB:=IsSquare(B/({d[3]})); parent:=cpt and sU and sV and sA and sB;\n    if cpt then reconstructed_C_x +:= 1; end if; if parent then full_parent +:= 1; end if; if parent and not deg then nondeg_parent +:= 1; end if;\n    print "PULLBACK_X:",xp," C_Q_POINT:",cpt," DEG:",deg," PARENT:",parent," ZERO_UVAB:",U eq 0,V eq 0,A eq 0,B eq 0," SQ_UVAB:",sU,sV,sA,sB;\n  end for;\nend procedure;\nif lo eq 0 and hi eq 0 then\n  mode:="RANK0_TORSION_FULL"; complete_index:=true; print "FULL_GROUP_MODE: RANK0_TORSION_FULL";\n  for g in T do Pcur:=tm(g); ReplayPoint(Pcur,~quotient_rational_X,~reconstructed_C_x,~full_parent,~nondeg_parent,~quotient_infinity,~inversion_boundary); end for;\nelif lo eq 1 and hi eq 1 then\n  gensG:=[G.i : i in [1..Ngens(G)]]; freeG:=[g : g in gensG | Order(g) eq 0]; print "PMW_FREE_GENERATOR_COUNT:",#freeG;\n  if #freeG eq 1 and tinv eq [2,2] then\n    P:=pm(freeG[1]); assert Order(P) eq 0; print "FREE_POINT:",P; SP:=Saturation([P],2 : TorsionFree:=true); print "SAT2_COUNT:",#SP;\n    if #SP eq 1 then\n      QP:=SP[1]; assert Order(QP) eq 0; print "SAT2_POINT:",QP; H:=AbelianGroup([2,2,0]); T1:=tm(T.1); T2:=tm(T.2);\n      hm:=map< H -> E | h :-> (Integers()!Eltseq(h)[1])*T1 + (Integers()!Eltseq(h)[2])*T2 + (Integers()!Eltseq(h)[3])*QP >;\n      VV,RR:=Chabauty(hm,pi : IndexBound:=2); rr:=RR; while rr gt 0 and rr mod 2 eq 0 do rr div:=2; end while;\n      print "ELLCHAB_R:",RR; print "ELLCHAB_R_2_PRIMARY:",RR gt 0 and rr eq 1; print "ELLCHAB_COUNT:",#VV;\n      if RR gt 0 and rr eq 1 then\n        mode:="RANK1_SAT2_ELLCHAB"; complete_index:=true;\n        for g in VV do Pcur:=hm(g); print "GROUP_ELEMENT:",g; ReplayPoint(Pcur,~quotient_rational_X,~reconstructed_C_x,~full_parent,~nondeg_parent,~quotient_infinity,~inversion_boundary); end for;\n      end if;\n    end if;\n  end if;\nend if;\nprint "MODE:",mode; print "INDEX_COMPLETENESS_PROVED:",complete_index;\nprint "QUOTIENT_INFINITY_COUNT:",quotient_infinity; print "QUOTIENT_RATIONAL_X_COUNT:",quotient_rational_X; print "INVERSION_BOUNDARY_S0_COUNT:",inversion_boundary;\nprint "RECONSTRUCTED_C_Q_X_COUNT_WITH_MULTIPLICITY:",reconstructed_C_x; print "FULL_PARENT_LIFT_X_COUNT:",full_parent; print "NONDEGENERATE_FULL_PARENT_LIFT_COUNT:",nondeg_parent;\nprint "EXCEPTIONAL_U0_XPM1_RECEIVER_DEGENERATE: true"; print "EXCEPTIONAL_S0_AND_QUOTIENT_INFINITY_RECEIVER_DEGENERATE: true";\nprint "CLOSURE_CANDIDATE:",complete_index and nondeg_parent eq 0; print "END branch={t['branch_id']}";\n'''


lock_bytes = LOCK.read_bytes()
lock = json.loads(lock_bytes)
assert lock["schema"] == "STAGE34_02C_D2_STAGEA2_MODEL191_GAUSSIAN_QUARTIC_GENUSONE_LOCK_V1"
t = lock["target"]
out = ""
err = None
status = "UNRESOLVED_RESOURCE_OR_EXTERNAL_WALL"
try:
    http, out = submit(magma_code(lock))
    bad = any(x in out for x in ("Runtime error", "Assertion failed", "User error", "Internal error"))
    if http == 200 and f"END branch={t['branch_id']}" in out and not bad:
        status = "PASS_RETURN"
    else:
        err = f"http={http} malformed_or_magma_error"
except Exception as ex:
    err = f"{type(ex).__name__}: {ex}"

RAW.write_text(out + "\nERROR=" + (err or "") + "\n")
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
    ("SYMBOLIC_QUARTIC_TO_CUBIC_IDENTITIES:", "symbolic_quartic_to_cubic_identities", lambda s: s == "true"),
    ("RANK_LOWER:", "rank_lower", int), ("RANK_UPPER:", "rank_upper", int),
    ("PMW_SUCCESS:", "pmw_success", lambda s: s == "true"),
    ("PMW_FREE_GENERATOR_COUNT:", "pmw_free_generator_count", int),
    ("SAT2_COUNT:", "sat2_count", int), ("ELLCHAB_R:", "ellchab_R", int),
    ("ELLCHAB_R_2_PRIMARY:", "ellchab_R_2_primary", lambda s: s == "true"),
    ("ELLCHAB_COUNT:", "ellchab_count", int),
    ("INDEX_COMPLETENESS_PROVED:", "index_completeness_proved", lambda s: s == "true"),
    ("QUOTIENT_INFINITY_COUNT:", "quotient_infinity_count", int),
    ("QUOTIENT_RATIONAL_X_COUNT:", "quotient_rational_X_count", int),
    ("INVERSION_BOUNDARY_S0_COUNT:", "inversion_boundary_s0_count", int),
    ("RECONSTRUCTED_C_Q_X_COUNT_WITH_MULTIPLICITY:", "reconstructed_C_Q_x_count_with_multiplicity", int),
    ("FULL_PARENT_LIFT_X_COUNT:", "full_parent_lift_x_count", int),
    ("NONDEGENERATE_FULL_PARENT_LIFT_COUNT:", "nondegenerate_full_parent_lift_count", int),
    ("EXCEPTIONAL_U0_XPM1_RECEIVER_DEGENERATE:", "exceptional_u0_xpm1_receiver_degenerate", lambda s: s == "true"),
    ("EXCEPTIONAL_S0_AND_QUOTIENT_INFINITY_RECEIVER_DEGENERATE:", "exceptional_s0_and_quotient_infinity_receiver_degenerate", lambda s: s == "true"),
    ("CLOSURE_CANDIDATE:", "closure_candidate", lambda s: s == "true"),
]:
    z = val(pfx, out, False)
    if z is not None:
        try:
            rec[key] = typ(z)
        except Exception:
            rec[key + "_raw"] = z
rec["torsion_invariants"] = val("TORSION_INVARIANTS:", out, False)
rec["pmw_invariants"] = val("PMW_INVARIANTS:", out, False)
rec["free_point"] = val("FREE_POINT:", out, False)
rec["sat2_point"] = val("SAT2_POINT:", out, False)
rec["mode"] = val("MODE:", out, False)
rec["evidence_lines"] = [x for x in out.splitlines() if x.startswith(("GROUP_ELEMENT:", "GROUP_IMAGE:", "QX:", "U:", "PULLBACK_X:", "INVERSION_BOUNDARY_S0:"))]
if status != "PASS_RETURN":
    rec["raw_tail"] = out[-5000:]

candidate = bool(
    rec.get("symbolic_quartic_to_cubic_identities")
    and rec.get("index_completeness_proved")
    and rec.get("exceptional_u0_xpm1_receiver_degenerate")
    and rec.get("exceptional_s0_and_quotient_infinity_receiver_degenerate")
    and rec.get("nondegenerate_full_parent_lift_count") == 0
)
payload = {
    "schema": "STAGE34_02C_D2_STAGEA2_MODEL191_GAUSSIAN_QUARTIC_GENUSONE_CHABAUTY_PROBE_V1",
    "status": "DIAGNOSTIC_NO_CREDIT",
    "source_lock": LOCK.name,
    "source_lock_sha256": "sha256:" + hashlib.sha256(lock_bytes).hexdigest(),
    "record": rec,
    "closure_candidate_branch_ids": [t["branch_id"]] if candidate else [],
    "authoritative_remaining_branches": 8,
    "authoritative_remaining_sign_orbits": 4,
    "firewalls": {
        "diagnostic_candidate_is_authoritative": False,
        "hostile_audit_passed": False,
        "sign_partner_transfer_authoritative": False,
        "D2_all_factor_branches_closed": False,
        "all_multiples_closed": False,
        "R29_EXT_CHANG_C_closed": False,
        "parent_route_closed": False,
        "perfect_cuboid_nonexistence_claim": False,
    },
}
OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
print(json.dumps({"branch": t["branch_id"], "model": t["model_id"], "status": status, "rank": [rec.get("rank_lower"), rec.get("rank_upper")], "mode": rec.get("mode"), "candidate": candidate}, sort_keys=True))
