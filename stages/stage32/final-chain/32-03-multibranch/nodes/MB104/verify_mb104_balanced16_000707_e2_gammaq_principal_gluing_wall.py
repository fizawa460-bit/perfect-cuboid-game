#!/usr/bin/env python3
import hashlib
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "GENUS1-SPAN5-BALANCED16-000707-E2-GAMMAQ-PRINCIPAL-GLUING-WALL-CERTIFICATE.json"


def req(cond, msg):
    if not cond:
        raise SystemExit(f"FAIL: {msg}")


def root():
    p = HERE
    while p != p.parent:
        if (p / "AGENTS.md").is_file() and (p / "stages").is_dir():
            return p
        p = p.parent
    raise SystemExit("FAIL: repo root")


def blob_sha1(path):
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


cert = json.loads(CERT.read_text())
req(cert["schema"] == "STAGE32_MB104_000707_E2_GAMMAQ_PRINCIPAL_GLUING_WALL_V1", "schema")
rr = root()

for lock in cert["source_locks"]:
    p = rr / lock["path"]
    if not p.is_file():
        raise SystemExit(f"SOURCE_LOCK_FAIL: missing {lock['id']}: {lock['path']}")
    got = blob_sha1(p)
    if got != lock["blob_sha1"]:
        raise SystemExit(f"SOURCE_LOCK_FAIL: {lock['id']}: expected {lock['blob_sha1']}, got {got}")

locks = {x["id"]: x for x in cert["source_locks"]}
gamma = json.loads((rr / locks["GAMMAQ_CERT"]["path"]).read_text())
tors = (rr / locks["ZERO_QUARTIC_TORSION_NOTE"]["path"]).read_text()
half = (rr / locks["HALF_HYPERPLANE_NOTE"]["path"]).read_text()

req(gamma["lifted_graph"]["R_plus_edges"] == ["Q0+--Q1+","Q0---Q1-"], "R+ graph")
req(gamma["lifted_graph"]["R_minus_edges"] == ["Q0+--Q1-","Q0---Q1+"], "R- graph")
req("2 D_k ~ 0 in Pic^0(Qk)" in tors, "componentwise 2-torsion source")
req("G_1 ~ G_2" in half, "global linearization source")
req("tau(G_1)=G_2" in half, "deck exchange source")

inp = cert["conditional_input"]
req(inp["global_linearization"] == "G1~G2", "conditional linearization")
req(inp["normalized_deck_reciprocity"] == "tau^*F=1/F", "deck reciprocity")

# Exact symbolic cancellation tested over many nonzero rational values and by direct algebraic identity.
def obstruction(ap, am, bp, bm):
    return ((am / (1 / bm)) * ((1 / bp) / (1 / ap))) / ((ap / bp) * (bm / (1 / am)))

vals = [Fraction(1), Fraction(2), Fraction(3,2), Fraction(-1), Fraction(-5,3)]
for ap in vals:
    for am in vals:
        for bp in vals:
            for bm in vals:
                req(obstruction(ap, am, bp, bm) == 1, "cycle obstruction identity")

# Algebraically both numerator and denominator reduce to ap*am*bm/bp.
req(cert["cycle_obstruction"]["exact_simplification"] == 1, "cert obstruction one")
req(cert["cycle_obstruction"]["additional_gluing_condition"] is False, "no extra gluing condition")
req(cert["wolfram_crosscheck"]["output"] == 1, "Wolfram exact output")

route = cert["routing_consequence"]
req(route["componentwise_2torsion_strengthened_by_zero_quartic_union_gluing"] is False, "2-torsion not strengthened")
req(route["new_allocation_congruence_from_this_route"] is False, "no new congruence")
req(route["conductor_loop_comparison_still_required"] is True, "conductor comparison required")

for key, value in cert["credit_firewall"].items():
    if key.endswith("_authorized") or key.endswith("_credit") or key.endswith("_closed") or key.endswith("_complete") or key.endswith("_computed") or key.endswith("_proved") or key.endswith("_claim"):
        req(value is False, f"firewall {key}")

print("PASS STAGE32_MB104_000707_E2_GAMMAQ_PRINCIPAL_GLUING_WALL_V1")
print("deck_reciprocity makes zero-quartic four-cycle gluing obstruction identically 1; no new allocation condition; conductor_comparison=REQUIRED")
