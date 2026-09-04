#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE_PATH = ROOT / "stages/stage36/MAIN-STATE.json"
CERT_PATH = ROOT / "stages/stage36/36-04/h-torsor-lift-class.json"
INV_PATH = ROOT / "stages/stage36/36-02/representative-inventory.json"
PREV_PATH = ROOT / "stages/stage36/36-03/physical-open-boundary.json"
BASE = "efe25f4ef74dc776da7ccad3f5cd786b0b2906e4"
INV_BLOB = "88130b9380a677a191f91c24df87618e65be0a2f"
PREV_BLOB = "fc1947b2de08f7d8a104bdc91902b20e88635349"

SOURCES = {
    "stage36_roadmap": ("stages/stage36/ROADMAP.md", "eeedda0e89e24f851c989b5ec83e7b320e1ad99e"),
    "stage29_exact_sign_cover_model": ("stages/stage29/29-02ha/exact-sign-cover-model.md", "fc2d5284a259750f45d2d756a952002671e3bccc"),
    "stage29_campedelli_quotient_adapter": ("stages/stage29/29-02hb/campedelli-quotient-adapter.md", "5f959d60106243bb31df06a3961ab04182d78fc7"),
    "stage29_campedelli_arithmetic_routing": ("stages/stage29/29-02hb/arithmetic-routing.md", "ff83f652e2c9e95b0670c0964b9c8cf0fbccd696"),
    "stage29_campedelli_route_contract": ("stages/stage29/29-02hb/route-contract.json", "75045d8f15786836e8a7383fc07ef95161fa86e7"),
}
ARSENAL = {
    "router": ("docs/arsenal/index.json", "aa45d19c2f1d8970c7f142bf744c5c17e75abe5a"),
    "S30-WF01": ("docs/arsenal/cards/workflows/S30-WF01.md", "8061279e07f9dba539b8c9ea96173f526abf4a3b"),
    "S30-WF02": ("docs/arsenal/cards/workflows/S30-WF02.md", "38e4625155eb079bbe3d50d663c6256559319886"),
    "S30-WF03": ("docs/arsenal/cards/workflows/S30-WF03.md", "12740198aba19ade18302819f8e890dbda4eb701"),
}
LINE6 = ["A1", "A2", "A3", "B3", "B2", "B1"]
FORMS = {"A1":"x", "A2":"y", "A3":"z", "B3":"x+y", "B2":"x+z", "B1":"y+z", "C":"x+y+z"}
STRATA = {
    "NONE": [], "B3": ["B3"], "B2": ["B2"], "B1": ["B1"], "C": ["C"],
    "B3_B2": ["B3","B2"], "B3_B1": ["B3","B1"], "B2_B1": ["B2","B1"],
}
LINE_COEFF = {"A1":(1,0,0), "A2":(0,1,0), "A3":(0,0,1), "B3":(1,1,0), "B2":(1,0,1), "B1":(0,1,1), "C":(1,1,1)}


def blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def require(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(msg)


def bits(s: str) -> tuple[int, ...]:
    require(len(s) == 6 and set(s) <= {"0","1"}, f"bad c6 bitstring: {s}")
    return tuple(int(x) for x in s)


def dot(a, b) -> int:
    return sum(x*y for x, y in zip(a,b)) % 2


def xor(a, b):
    return tuple(x ^ y for x,y in zip(a,b))


def support(c) -> tuple[str, ...]:
    out = [LINE6[i] for i,b in enumerate(c) if b]
    if sum(c) % 2:
        out.append("C")
    return tuple(out)


def support_to_c6(supports) -> tuple[int, ...]:
    s = set(supports)
    c = tuple(1 if name in s else 0 for name in LINE6)
    require(("C" in s) == (sum(c) % 2 == 1), f"support is not an even projective character: {supports}")
    require(len(s) % 2 == 0, f"support parity moved: {supports}")
    return c


def pairing_vector(H, c):
    return tuple(dot(h,c) for h in H)


def canonical_dual(H, Z, target):
    candidates = []
    for c in itertools.product((0,1), repeat=6):
        if pairing_vector(H,c) != target:
            continue
        sup = support(c)
        if set(sup) & set(Z):
            continue
        candidates.append((len(sup), sup, ''.join(map(str,c)), c))
    require(candidates, f"no dual character avoids stratum {Z}")
    return min(candidates)[3]


def span3(vs):
    return {tuple(0 for _ in range(6))} | {
        tuple((mask >> j & 1) * 0 for j in range(6)) for mask in []
    }


def in_span3(v, basis):
    for mask in range(8):
        w = (0,0,0,0,0,0)
        for i,b in enumerate(basis):
            if mask >> i & 1:
                w = xor(w,b)
        if w == v:
            return True
    return False


def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0])


def det3(a,b,c):
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])


def main() -> None:
    cert = json.loads(CERT_PATH.read_text())
    state = json.loads(STATE_PATH.read_text())
    inv = json.loads(INV_PATH.read_text())

    require(cert.get("schema") == "STAGE36_36_04_EXPLICIT_H_TORSOR_LIFT_CLASS_V1", "36-04 certificate schema moved")
    require(cert.get("status") == "POINTWISE_H_TORSOR_CLASS_EXPLICIT_PENDING_HOSTILE_AUDIT", "36-04 certificate status moved")
    require(cert.get("base_main_sha") == BASE, "36-04 certificate base moved")

    # S30-WF02 predecessor binding: both load-bearing Stage36 mathematical certificates are immutable.
    require(blob_sha(INV_PATH) == INV_BLOB, "audited 36-02 inventory blob drift")
    require(blob_sha(PREV_PATH) == PREV_BLOB, "audited 36-03 certificate blob drift")
    auth = cert.get("source_authority", {})
    require(auth.get("stage36_36_03_hostile_audit_review") == 5113890803, "36-03 review moved")
    require(auth.get("stage36_36_03_audited_head") == "5fd7af75ede4cd2eceb70f9f21bd2b98ec5453a6", "36-03 audited head moved")
    require(auth.get("stage36_36_03_merge") == "45f290a443cf71b1fc62f031994122c3fa58f0e9", "36-03 audited merge moved")
    require(auth.get("stage36_36_03_promotion_merge") == BASE, "36-03 promotion merge moved")
    require(auth.get("stage36_36_03_certificate") == {"path":"stages/stage36/36-03/physical-open-boundary.json","blob_sha":PREV_BLOB}, "36-03 certificate authority moved")
    require(auth.get("stage36_36_02_inventory") == {"path":"stages/stage36/36-02/representative-inventory.json","blob_sha":INV_BLOB}, "36-02 inventory authority moved")

    declared_sources = cert.get("source_locks", {})
    for key,(rel,sha) in SOURCES.items():
        require(declared_sources.get(key) == {"path":rel,"blob_sha":sha}, f"source declaration moved: {key}")
        require(blob_sha(ROOT/rel) == sha, f"source blob drift: {key}")
    declared_arsenal = cert.get("arsenal_locks", {})
    for key,(rel,sha) in ARSENAL.items():
        row = declared_arsenal.get(key,{})
        require(row.get("path") == rel and row.get("blob_sha") == sha, f"Arsenal declaration moved: {key}")
        require(blob_sha(ROOT/rel) == sha, f"Arsenal blob drift: {key}")
    require("FINITE_EQUIVARIANT_IDENTIFICATION_AUDIT" in (ROOT/ARSENAL["S30-WF01"][0]).read_text(), "S30-WF01 role moved")
    require("IMMUTABLE_LAYERED_CERTIFICATE_REPLAY" in (ROOT/ARSENAL["S30-WF02"][0]).read_text(), "S30-WF02 role moved")
    require("ADAPTER_CREDIT_LAYER_FIREWALL" in (ROOT/ARSENAL["S30-WF03"][0]).read_text(), "S30-WF03 role moved")
    require(declared_arsenal.get("S30-W02") == "NOT_TRIGGERED_Q_FORM_ALREADY_EXACT", "S30-W02 activation moved")
    require(declared_arsenal.get("S34-W01") == "NOT_TRIGGERED_FINITE_SQUARECLASS_FAMILY_NOT_YET_PROVED", "S34-W01 activated prematurely")
    require(declared_arsenal.get("S34-W03") == "PREPARED_IN_36_03_NOT_EXECUTED", "S34-W03 credit moved")

    roadmap = (ROOT/SOURCES["stage36_roadmap"][0]).read_text()
    for needle in ["36-04", "EXPLICIT_H_TORSOR_AND_LIFT_CLASS", "POINTWISE_H_TORSOR_CLASS_EXPLICIT=true", "FINITE_TWIST_FAMILY_PROVED=false"]:
        require(needle in roadmap, f"roadmap 36-04 anchor missing: {needle}")
    sign_model = (ROOT/SOURCES["stage29_exact_sign_cover_model"][0]).read_text()
    for needle in ["[x:y:z]=[a_1^2:a_2^2:a_3^2]", "L_{a1}=x", "L_{b3}=x+y", "L_c=x+y+z", "F_2^7"]:
        require(needle in sign_model, f"sign-cover anchor missing: {needle}")
    adapter = (ROOT/SOURCES["stage29_campedelli_quotient_adapter"][0]).read_text()
    for needle in ["finite etale `H`-torsor", "S  --etale degree 8-->  C_H", "requires an `H`-torsor descent", "No converse is asserted."]:
        require(needle in adapter, f"Campedelli torsor anchor missing: {needle}")
    routing = (ROOT/SOURCES["stage29_campedelli_arithmetic_routing"][0]).read_text()
    for needle in ["H^1", "rational quotient point need not lift rationally upstairs", "finite twist list"]:
        require(needle in routing, f"arithmetic-routing H1 anchor missing: {needle}")

    model = cert.get("model", {})
    require(model.get("gamma_C0_order") == LINE6, "Gamma C=0 order moved")
    require(model.get("line_forms") == FORMS, "seven-line forms moved")
    require(cert.get("physical_receiver",{}).get("allowed_zero_strata") == STRATA, "zero-stratum list moved")

    # Independent boundary-stratum exhaustiveness on x*y*z != 0.
    for B,coord in [("B3","A3"),("B2","A2"),("B1","A1")]:
        p = cross(LINE_COEFF["C"], LINE_COEFF[B])
        require(sum(LINE_COEFF[coord][i]*p[i] for i in range(3)) == 0, f"C+{B} did not force coordinate zero")
    for left,right in [("B3","B2"),("B3","B1"),("B2","B1")]:
        p = cross(LINE_COEFF[left], LINE_COEFF[right])
        require(all(x != 0 for x in p), f"{left}+{right} left physical coordinate open")
    require(det3(LINE_COEFF["B3"],LINE_COEFF["B2"],LINE_COEFF["B1"]) != 0, "three B-lines acquired a projective intersection")

    reps = cert.get("representatives", {})
    inv_reps = inv.get("representatives", {})
    require(set(reps) == {"Q6_GEOM8","Q2_GEOM8","Q2_GEOM2"}, "36-04 representative set moved")
    targets = [(1,0,0),(0,1,0),(0,0,1)]
    for rep,row in reps.items():
        src = inv_reps.get(rep,{})
        require(row.get("H_basis") == src.get("gamma_C0_basis"), f"{rep}: H basis not inventory-derived")
        require(row.get("H_perp_supports") == src.get("character_supports"), f"{rep}: H-perp basis not inventory-derived")
        H = [bits(s) for s in row["H_basis"]]
        Hperp = [support_to_c6(s) for s in row["H_perp_supports"]]
        require(len(set(Hperp)) == 3, f"{rep}: repeated H-perp basis vector")
        for hp in Hperp:
            require(pairing_vector(H,hp) == (0,0,0), f"{rep}: declared H-perp vector not orthogonal")
        # rank 3 of the H-perp basis via eight distinct span elements
        span = set()
        for mask in range(8):
            w=(0,0,0,0,0,0)
            for i,b in enumerate(Hperp):
                if mask >> i & 1:
                    w=xor(w,b)
            span.add(w)
        require(len(span)==8, f"{rep}: H-perp basis rank moved")

        chart = row.get("dual_chart_c6", {})
        require(set(chart) == set(STRATA), f"{rep}: chart strata coverage moved")
        per_character = [set(),set(),set()]
        for stratum,Z in STRATA.items():
            chosen = chart[stratum]
            require(len(chosen)==3, f"{rep}/{stratum}: not three dual characters")
            for j,s in enumerate(chosen):
                c = bits(s)
                require(pairing_vector(H,c) == targets[j], f"{rep}/{stratum}/chi{j+1}: pairing not dual")
                require(c == canonical_dual(H,Z,targets[j]), f"{rep}/{stratum}/chi{j+1}: not canonical exact choice")
                sup = support(c)
                require(len(sup)%2==0, f"{rep}/{stratum}/chi{j+1}: odd projective support")
                require(not(set(sup)&set(Z)), f"{rep}/{stratum}/chi{j+1}: selected G vanishes on stratum")
                per_character[j].add(c)
        # Exact chart transition: any two representatives of the same H-character differ by H^perp.
        for j,choices in enumerate(per_character):
            for c,cprime in itertools.combinations(choices,2):
                d=xor(c,cprime)
                require(pairing_vector(H,d)==(0,0,0), f"{rep}/chi{j+1}: chart difference not H-invariant")
                require(in_span3(d,Hperp), f"{rep}/chi{j+1}: chart difference missing from inventory H-perp span")

    pointwise = cert.get("pointwise_class", {})
    require(pointwise.get("degree") == 8, "pointwise H-torsor degree moved")
    require("T1^2=G_c1" in pointwise.get("fiber_equations",""), "explicit fiber equations missing")
    require("delta_H(P)" in pointwise.get("definition",""), "pointwise H1 class missing")
    require("iff" in pointwise.get("rational_lift_iff","") and "rational squares" in pointwise.get("rational_lift_iff",""), "rational lift iff missing")
    require(cert.get("degenerate_cases",{}).get("selected_G_zero") is False, "selected chart permits zero Kummer coordinate")
    require(cert.get("pass_condition") == {"POINTWISE_H_TORSOR_CLASS_EXPLICIT":True,"FINITE_TWIST_FAMILY_PROVED":False}, "36-04 pass condition moved")
    promo = cert.get("promotion",{})
    require(promo.get("hostile_audit_required") is True and promo.get("promoted_to_audited_authority") is False and promo.get("next_leaf_before_audit_allowed") is False, "36-04 promotion boundary moved")
    require(promo.get("provisional_successor_after_audit") == "36-05_UNIFORM_RAMIFICATION_SUPPORT", "36-05 successor moved")
    require(all(v is False for v in cert.get("claims",{}).values()), "36-04 certificate leaked higher credit")

    require(state.get("schema") == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V8_36_04_PENDING_AUDIT", "Stage36 V8 state schema moved")
    require(state.get("status") == "ACTIVE_PENDING_HOSTILE_AUDIT" and state.get("base_main_sha") == BASE, "36-04 state lifecycle moved")
    unit = state.get("completed_units",{}).get("36-04",{})
    require(unit.get("status") == "POINTWISE_H_TORSOR_CLASS_EXPLICIT_PENDING_HOSTILE_AUDIT", "36-04 unit status moved")
    require(unit.get("POINTWISE_H_TORSOR_CLASS_EXPLICIT") is True and unit.get("FINITE_TWIST_FAMILY_PROVED") is False and unit.get("NEW_THEOREM_CREDIT") is False, "36-04 provisional credit moved")
    require(unit.get("promotion_status") == "PROVISIONAL_NOT_AUDITED", "36-04 prematurely audited")
    gates = state.get("promotion_gates",{})
    for key in ["source_authority_lock_complete","three_Q_representatives_exact","physical_open_push_and_boundary_complete"]:
        require(gates.get(key) is True, f"audited predecessor gate lost: {key}")
    require(gates.get("pointwise_H_torsor_class_explicit") is False, "36-04 gate promoted before audit")
    for key,value in gates.items():
        if key not in {"source_authority_lock_complete","three_Q_representatives_exact","physical_open_push_and_boundary_complete"}:
            require(value is False, f"later gate prematurely promoted: {key}")
    current=state.get("current",{})
    require(current.get("unit") == "36-04" and current.get("next_exact_leaf") == "36-04_EXPLICIT_H_TORSOR_AND_LIFT_CLASS", "36-05 started before audit")
    require(current.get("provisional_successor_after_hostile_audit") == "36-05_UNIFORM_RAMIFICATION_SUPPORT", "36-05 successor moved")
    require("36-05" not in state.get("completed_units",{}), "36-05 started before hostile audit")
    require(all(v is False for v in state.get("claims",{}).values()), "Stage36 state leaked higher credit")

    print("PASS STAGE36_36_04_EXPLICIT_H_TORSOR_LIFT_CLASS_V1")
    print("representatives=3; strata=8; dual characters=72 exact canonical selections")
    print("fiber=T1^2=G1,T2^2=G2,T3^2=G3; degree=8; rational lift iff delta_H(P)=1")
    print("chart transitions lie in audited H-perp span; noncoordinate zero strata covered")
    print("arsenal=S30-WF01,S30-WF02,S30-WF03; S30-W02/S34-W01 not triggered")
    print("finite_twist_family=false; hostile audit required; 36-05 not started")


if __name__ == "__main__":
    main()
