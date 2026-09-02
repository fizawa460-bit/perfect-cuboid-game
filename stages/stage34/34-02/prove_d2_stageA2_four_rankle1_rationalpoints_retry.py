#!/usr/bin/env python3
from __future__ import annotations
import collections, hashlib, json, pathlib, urllib.error, urllib.parse, urllib.request, xml.etree.ElementTree as ET
from fractions import Fraction

ROOT = pathlib.Path(__file__).resolve().parent
LOCK = ROOT / "d2-stageA2-four-rankle1-rationalpoints-retry-lock.json"
OUT = ROOT / "d2-stageA2-four-rankle1-rationalpoints-retry-certificate.json"
RAW = ROOT / "d2-stageA2-four-rankle1-rationalpoints-retry-stdout.txt"
URL = "https://magma.maths.usyd.edu.au/xml/calculator.xml"
REFERER = "https://magma.maths.usyd.edu.au/calc/"
TIMEOUT = 600
NAMES = ["U", "V", "A", "B"]
VARIANTS = [
    ("rank1_fast_small", "RankBound:=1, Fast:=true, Bound1:=100, Bound2:=1000"),
    ("rank1_fast_default", "RankBound:=1, Fast:=true"),
    ("rank1_default", "RankBound:=1"),
]


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
            "User-Agent": "perfect-cuboid-stage34-four-rank1-rp-retry/1.0",
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


def code_for(t, params):
    a, b = map(int, t["q"].split("/"))
    d = list(map(int, t["delta"]))
    f = poly_expr(t["coefficients_desc_t_degree6"])
    scale = Fraction(t["literal_to_integral_y_scale"])
    tri = t["triple"].split("*")
    lit = "*".join(f"({name}/({d[NAMES.index(name)]}))" for name in tri)
    return f'''SetColumns(0); SetQuitOnError(true);
Q:=Rationals(); Qx<x>:=PolynomialRing(Q);
U:=x^2-1; V:=2*x; A:={a}*U+{b}*V; B:={b}*U+{a}*V;
flit:={lit}; fint:={f}; assert fint eq ({scale.numerator}/{scale.denominator})^2*flit; print "QUOTIENT_IDENTITY: true";
C:=HyperellipticCurve(fint); assert Genus(C) eq 2;
pts,complete:=RationalPointsGenus2(C : {params}); print "COMPLETE:",complete; print "POINT_COUNT:",#pts;
receiver_deg:=0; full_parent:=0; nondeg_parent:=0;
for P in pts do
 X:=P[1]; Z:=P[3]; Uh:=X^2-Z^2; Vh:=2*X*Z; Ah:={a}*Uh+{b}*Vh; Bh:={b}*Uh+{a}*Vh;
 zU:=Uh eq 0; zV:=Vh eq 0; zA:=Ah eq 0; zB:=Bh eq 0; deg:=zU or zV or zA or zB;
 sU:=IsSquare(Uh/({d[0]})); sV:=IsSquare(Vh/({d[1]})); sA:=IsSquare(Ah/({d[2]})); sB:=IsSquare(Bh/({d[3]})); parent:=sU and sV and sA and sB;
 if deg then receiver_deg +:= 1; end if; if parent then full_parent +:= 1; end if; if parent and not deg then nondeg_parent +:= 1; end if;
 print "POINT:",P," ZEROS_UVAB:",zU,zV,zA,zB," SQ_UVAB:",sU,sV,sA,sB," PARENT:",parent;
end for;
print "RECEIVER_DEGENERATE_COUNT:",receiver_deg; print "FULL_PARENT_LIFT_POINT_COUNT:",full_parent; print "NONDEGENERATE_FULL_PARENT_LIFT_COUNT:",nondeg_parent; print "PROOF_REPLAY_COMPLETE: true";
'''


lock = json.loads(LOCK.read_text())
assert lock["schema"] == "STAGE34_02B_D2_STAGEA2_FOUR_RANKLE1_RATIONALPOINTS_RETRY_LOCK_V1"
assert len(lock["targets"]) == 4
records = []
rawparts = []

for i, t in enumerate(lock["targets"], 1):
    attempts = []
    chosen = None
    for variant, params in VARIANTS:
        out = ""
        err = None
        try:
            http, out = submit(code_for(t, params))
            bad = any(x in out for x in ("Runtime error", "Assertion failed", "User error", "Internal error"))
            proof_complete = http == 200 and not bad and val("PROOF_REPLAY_COMPLETE:", out) == "true"
        except Exception as ex:
            proof_complete = False
            http = None
            err = f"{type(ex).__name__}: {ex}"
        attempt = {
            "variant": variant,
            "parameters": params,
            "http_status": http,
            "execution_complete": proof_complete,
            "error": err,
            "stdout_sha256": "sha256:" + hashlib.sha256(out.encode()).hexdigest(),
        }
        if out:
            for key, prefix in (
                ("quotient_identity_verified", "QUOTIENT_IDENTITY:"),
                ("complete", "COMPLETE:"),
                ("complete_qpoint_count", "POINT_COUNT:"),
                ("receiver_degenerate_count", "RECEIVER_DEGENERATE_COUNT:"),
                ("full_parent_lift_point_count", "FULL_PARENT_LIFT_POINT_COUNT:"),
                ("nondegenerate_full_parent_lift_count", "NONDEGENERATE_FULL_PARENT_LIFT_COUNT:"),
            ):
                try:
                    rawv = val(prefix, out)
                    if key in ("quotient_identity_verified", "complete"):
                        attempt[key] = rawv == "true"
                    else:
                        attempt[key] = int(rawv)
                except Exception:
                    pass
            attempt["point_lines"] = [x for x in out.splitlines() if x.startswith("POINT:")]
        attempts.append(attempt)
        rawparts.append(
            f"===== index={i} branch={t['branch_id']} model={t['model_id']} variant={variant} =====\n{out}\nERROR={err or ''}"
        )
        if proof_complete and attempt.get("complete") is True:
            chosen = attempt
            break

    rank_ok = int(t["locked_rank_bounds"][1]) <= 1
    rec = {**t, "locked_rank_condition_verified": rank_ok, "attempts": attempts}
    if chosen is not None:
        rec.update({
            "execution_complete": True,
            "chosen_variant": chosen["variant"],
            "chosen_parameters": chosen["parameters"],
            "quotient_identity_verified": chosen.get("quotient_identity_verified") is True,
            "complete": chosen.get("complete") is True,
            "complete_qpoint_count": chosen.get("complete_qpoint_count"),
            "receiver_degenerate_count": chosen.get("receiver_degenerate_count"),
            "full_parent_lift_point_count": chosen.get("full_parent_lift_point_count"),
            "nondegenerate_full_parent_lift_count": chosen.get("nondegenerate_full_parent_lift_count"),
            "point_lines": chosen.get("point_lines", []),
            "stdout_sha256": chosen["stdout_sha256"],
        })
        rec["direct_closure_candidate"] = bool(
            rank_ok
            and rec["quotient_identity_verified"]
            and rec["complete"]
            and rec["nondegenerate_full_parent_lift_count"] == 0
        )
    else:
        rec.update({"execution_complete": False, "direct_closure_candidate": False})
    records.append(rec)
    print(json.dumps({
        "branch": t["branch_id"],
        "model": t["model_id"],
        "chosen_variant": rec.get("chosen_variant"),
        "complete": rec.get("complete"),
        "qpoints": rec.get("complete_qpoint_count"),
        "nondeg_parent": rec.get("nondegenerate_full_parent_lift_count"),
        "candidate": rec["direct_closure_candidate"],
        "attempts": len(attempts),
    }, sort_keys=True))

raw = "\n".join(rawparts)
RAW.write_text(raw)
closed = [r for r in records if r["direct_closure_candidate"]]
cby = collections.Counter(r["q"] for r in closed)
base = {"20/99": 4, "24/7": 0, "48/55": 0, "60/11": 6, "80/39": 4, "84/13": 8}
rem = {k: v - 2 * cby.get(k, 0) for k, v in base.items()}
payload = {
    "schema": "STAGE34_02B_D2_STAGEA2_FOUR_RANKLE1_RATIONALPOINTS_RETRY_CERTIFICATE_V1",
    "status": "READY_FOR_HOSTILE_AUDIT_FOUR_RETRY_CANDIDATES" if len(closed) == 4 else "BOUNDED_RETRY_PARTIAL_OR_EXTERNAL_RESPONSE_OPEN",
    "source_lock": LOCK.name,
    "source_lock_sha256": "sha256:" + hashlib.sha256(LOCK.read_bytes()).hexdigest(),
    "rank_evidence": lock["rank_evidence"],
    "generation2_evidence": lock["generation2_evidence"],
    "records": records,
    "direct_closure_candidate_count": len(closed),
    "direct_closure_candidate_branch_ids": [r["branch_id"] for r in closed],
    "sign_transfer_candidate_branch_ids": [r["partner"] for r in closed],
    "candidate_closed_branches_from_retry_if_audited": 2 * len(closed),
    "candidate_remaining_from_22_if_only_retry_audited": 22 - 2 * len(closed),
    "candidate_remaining_by_q_from_22_if_only_retry_audited": rem,
    "raw_stdout_sha256": "sha256:" + hashlib.sha256(raw.encode()).hexdigest(),
    "credit": "Pre-audit bounded retry only. Exact-model repaired RankBounds supplies only rank<=1; this run must independently supply complete quotient pointsets and exact parent pullback. External-response failure is not mathematical failure. No authoritative promotion without hostile audit.",
    "firewalls": {
        "hostile_audit_passed": False,
        "candidate_is_authoritative": False,
        "authoritative_remaining_d1": 22,
        "retry_failure_is_math_failure": False,
        "D2_all_factor_branches_closed": False,
        "all_multiples_closed": False,
        "R29_EXT_CHANG_C_closed": False,
        "parent_route_closed": False,
        "perfect_cuboid_nonexistence_claim": False,
    },
}
OUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
print("FOUR_RANK1_RETRY=" + json.dumps({"status": payload["status"], "direct_candidates": len(closed)}, sort_keys=True))
